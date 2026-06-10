#run this python code on startup
init python:
    import os, random, functools
    #class for recording the individual data for each character

    #paraphrased from Bored Chris on youtube
    def voice(event, character="default", **kwargs):
        i = 0
        voice_path="game/audio/voices/" + character + "/"
        #make a list of the files in the voicepath directory that we're going to use
        #inconsistent because apparently python and renpy CWDs aren't consistent??
        voices = ["audio/voices/" + character + "/" + fname for fname in os.listdir(voice_path)]

        num_voices =  len(voices)
        
        while i < 50: #avoids infinite loops
            #get a random voice from our list of voices
            sfx = voices[random.randint(0, num_voices - 1)]
            #when to talk...
            if event == "show":
                renpy.music.queue(filenames=sfx, channel="sound", loop=False)
            #...and when to not
            elif event == "slow_done" or event == "end":
                renpy.music.stop(channel="sound")
            
            i += 1

    class MC:
        callback = voice # does this work?
        def __init__(self, character:Character=None, init_score:int=0):
            self.ch = character
            self.score = init_score
            return
        
        def update_score(self, n:int):
            self.score += n

        def get_score(self):
            return self.score
        
        def get_name(self):
            return self.ch.name

# Declare characters used by this game.
define strange = Character(
    name="Stranger",
    callback=functools.partial(store.voice, character="mom")
    )
define wren = Character(
    name="Wren", 
    color="#ffffff", #white
    callback=functools.partial(store.voice, character="wren")
    )
define ines = Character(
    name="Ines", 
    color="#fd9855", #light orange
    font="SofiaSans-VariableFont_wght.ttf",
    what_font="SofiaSans-VariableFont_wght.ttf",
    callback=functools.partial(store.voice, character="ines")
    #kind=strange
    )
define kat = Character(
    name="Katriel", 
    color="#d161a2", #light magenta
    kind=strange
    )
define mom = Character(
    name="Mom", 
    font="fonts/EBGaramond-VariableFont_wght.ttf", 
    what_font="fonts/EBGaramond-VariableFont_wght.ttf",
    kind=strange
    )
define phone = Character(
    name="Phone", 
    color="#097969", #cadmium green
    font="fonts/SpaceMono-Regular.ttf", 
    what_font="fonts/SpaceMono-Regular.ttf"
    )

#declare ambience audio channel
#this can't be right
define ambience = renpy.music.register_channel("ambience")

#declare love interest objects
default wren_obj = store.MC(wren)
#no way this works
#wren_obj.ch.callback = wren_obj.voice
default ines_obj = store.MC(ines)
default kat_obj = store.MC(kat)

#transform for all foreground images to make them the same height
transform max_y:
    ysize(600)
    fit "contain"

#animation for moving sprites around the screen
#default pos0 current position?
transform mv(pos0, pos1, spd=1.0):
    pos0
    linear spd pos1

# The game starts here.
label start:
    stop music
    
    # call debug
    call wren_selfcare
    call val_scenes
    call wren_research
    call end_demo
    return

label debug:
    return

label val_scenes:

    define audio.house_music  = "audio/music/Insurrection Bimbo - traverse mes mains, mes bras, mon ventre.mp3"
    define audio.garden_amb   = "audio/music/garden_bg_music.opus"
    define audio.garden_music =  "audio/music/Rrrrrose Azerty - Feverish Soundtrack.ogg"
    #create ambient sound channel for this tbh

    #Intro scene, Wren at home
    scene house #bathroom?
    play music house_music
    show wren_fg at max_y, center#get more silly with this i think
    
    # python:
    #     for i in range(1, 10):
    #         renpy.show("wren_fg", atl=chromatic(i))

    # mirror. chromatic abberation? blur?
    wren "It's okay."
    wren "It's just odd that it happened twice."
    show wren_fg at max_y, center
    hide wren_fg

    "*wren steps outside into-*"

    show mom_fg at left, max_y
    show wren_fg at max_y, mv(offscreenleft, right, 1.0)
    wren "Mother?"
    #wren's name is now known to the reader
    mom "I told you, you don't need to ask me to sign any forms. Ive already shown you my signature."
    wren "..."
    wren "I've been feeling kind of sick. I-"
    mom "You spend far too much time in your room, Wren. How many times do I need to tell you that fresh air and time in nature is what you need?"
    wren "It's-" 
    mom "Or get some little friends to spend time with. Loneliness is worse for you than cigarettes!"
    wren "{i}You don't have any friends, mother.{/i}"
    wren "Thank you for the advice."
    phone "{sc}bzzz{\sc}"
    phone "Reminder: volunteer at greenhouse"
    show wren_fg at max_y, mv(right, offscreenright, 0.5)
    ""
    hide mom_fg
    stop music
    
    #walking to internship
    show wren_fg at max_y, mv(offscreenleft, center, 1.0)
    wren """
        yes thank you mother 3 bags full mother

        Maybe if I didn't need to get perfect grades I'd have some friends.

        Maybe if you got off your lazy ass and actually parented me I'd be better at talking to people.

        Maybe if you actually looked at me for once instead of-

        ...that's not fair. I'm sorry. I know she's trying her best. It's not easy.

        ...It's not easy...

        Could it not get any hotter? I'm already feeling faint.
        """
    show wren_fg at max_y, mv(center, offscreenright, 1.0)
    #Garden Scene
    scene garden
    play ambience garden_amb
    play music garden_music
    show wren_fg at max_y, mv(offscreenleft, center, 1.0)
    #transform flip wren horiz too goofy?
    wren """
        Hello?

        Is anyone here?

        Excuse me?

        Sure. I guess. That's okay.
        """ 

    show wren_fg at mv(center, left, 1.0), max_y

    wren "{i}What am I supposed to...?{/i}"

    "She starts playing with a flower bud."

    wren "{i}Hm.{/i}"

    "She's crushed it."

    #Sound effect, boss music?
    show gs_dog at mv(offscreenright, right, 0.25), max_y #ines jumpscare
    strange "I- {b}excuse me!? {/b}{sc}{b}What are you doing??{/b}{/sc}"
    wren "Nothing."
    strange "Seriously? You didn't even pick it... get out! Open hours are closed!"
    wren "I was supposed to volunteer here..."
    #ines is introduced ?
    ines "Oh. OH!"
    ines "Sorry! I'm Ines, sorry for yelling."
    wren "I'm Wren. Thanks."
    ines "Welcome to the Local Gardens! So, how'd you get started with us here?"
    wren "It's the closest to my house that accepts volunteers."
    ines "Oh. Okay. Do you have any experience gardening?"
    wren "No."
    ines "Haha ummmm that's okay, I'll teach you! Do you have a favorite plant?"
    wren "No." #Girlboss behavior right there
    ines "That's..." 
    # Ines nervous smile
    ines "...so..."

    wren "Is something wrong? Why are you nervous?"
    ines """
        I-

        Look. I'm nervous around pretty girls, okay! Especially when they don't like me...
        """
    
    menu ines_one:
        "Who, me?":
            #+1 ines affection
            $ines_obj.update_score(1)
            jump who_me

        "I get it already. Stop making fun of me.":
            jump no_fun

    label who_me:
    wren "Who, me?"
    "*Ines blushes."
    ines "Yes, you."
    wren """
        .

        ..

        ...
        """
    ines "Can I draw you?"
    jump post_ines_one

    label no_fun:
    wren "I get it already. Stop making fun of me."
    ines "I'm not making fun of you!"
    wren "How do I know that?"
    ines "Well... How about I draw what I see?"
    "*Wren blushes.*"
    wren "Yes?"
    wren "{i}What the hell am I doing?{\i}"

    label post_ines_one:
    wren "I've just never done something like this before."
    ines "You're a natural."
    wren "Should I arch my back a little bit more?"
    ines "No, just stay still."
    wren "You... feel familiar?"
    ines "Do I?"
    
    label highschool_flashback:
    """*(Flashback to hs, 
    a non transitioned wren looks through a window at Ines, 
    younger, happily making an abstract painting, who waves 
    and smiles and points at her piece to show wren. wren feels EXTREME Jealousy, 
    to the point of violence, then gets confused and retreats)*"""
    
    wren "Maybe, I don't know"
    ines "You're so weird."
    ines "Do you really hate my garden that bad?"
    wren "No- I mean yes."
    ines "What?!"
    wren "It's not {i}your{\i} garden. It's pretty much any garden."
    ines "Why?"
    wren "I stepped in an underground wasps nest. It doesn't really matter."
    ines """
        If you say so.

        Can you keep that expression, just like that?
        """
    wren "Okay."
    #Drawing done
    "Wren looks at the finished drawing."
    wren """
        {i}It's kind of warm and soft and melty.

        It looks like me if I was in love...{\i}
        """
    ines "You're-"
    ines "You're going to come back, right?"
    wren "I have to. I committed to the hours."
    wren "And I need a good letter of recommendation."
    ines "Okay! So you're not mad at me!! You'll work with me!!!"
    wren "Work?"
    ines "I'm trying to flesh out my portfolio... I need someone to pose for me?"
    wren "Okay?"
    ines "Oh..."
    wren "I gotta go now."
    ines "Fine! I'll do your part of the garden work! Just let me draw you! I promise, it'll be really easy!"
    wren "Whatever."
    ines "That's a yes?!"
    wren "Sure."
    ines "You're so super amazing awesome Wren!"

    stop music
    stop ambience
    "Ines impulsively hugs wren who stiffens, turns red, and feels a twisting in her chest."
    #cut to the visual of a flower stem sprouting in a body

    wren """
        {i}I spent way longer than I intended.

        I don't even have any time to lay down, I already have to go to my job.

        I can't believe she said I was cute...{\i}
        """
    
    label wren_work:
    scene bg_thevoid
    """
    Wren walks into busy office. No one says hi to her. 

    She overhears a conversation: maybe something about kink? And his disgusting it is? Office gossip? Trans phobia? Homophobia? It's not pleasant.
    """
    wren "{i}It's a paycheck. I'm getting money for this.{\i}"
    wren "{i}They can't fix the office door?{\i}"

    "The hours pass by in a blur."

    "*Wren leaves work*"

    return

#katriel scenes!!
label wren_bumps_into_kat:
    wren "..."
    kat "..."
    kat "Wren."
    wren "...hey."
    wrem "{i}I forgot she would be here.{\i}"
    "kat sighs"
    kat "So, how's college going for you? It's been a while."
    wren """
        Pretty decent.
    
        {i} Not. {\i}

        What have you been up to?
    """
    "Kat talks in detail-- she's been doing a lot."
    wren "{i} Of course she's doing well.{\i}"
    return

label wren_research:
    # scene where wren obsessively researches Hanahaki Disease
    # frenetic. gare du nord? use a movie? animations i think

    define user1 = Character(
    name="user1", 
    color="#097969", #cadmium green
    font="fonts/SpaceMono-Regular.ttf", 
    what_font="fonts/SpaceMono-Regular.ttf",
    text_cps=renpy.random.randint(50, 60)
    )

    define user2 = Character(
    name="user2", 
    color="#097969", #cadmium green
    font="fonts/SpaceMono-Regular.ttf", 
    what_font="fonts/SpaceMono-Regular.ttf",
    text_cps=renpy.random.randint(30, 40)
    )

    define com = Character(
    name="Computer", 
    color="#097969", #cadmium green
    font="fonts/SpaceMono-Regular.ttf", 
    what_font="fonts/SpaceMono-Regular.ttf",
    callback=functools.partial(store.voice, character="computer")

    #text_cps=0 #computer is always instant
    )

    image black = "#000"
    play music "audio/music/johnny_ripper - gare du nord.mp3" fadein 1.0 loop

    scene black #bedroom?
    show wren_fg at center, max_y
    #desk, glow effect from screen
    #Wren clearly hasnt been sleeping.
    "Wren desperately searches for anything that could help"
    wren "{i}google why am i vomiting flowers{/i}"
    user2 "OMG i cant believe that stupid bitch got hanahaki OBVS shes not in love blah blah blah"
    user1 "dont joke about that?? its real, my aunt almost died from it >:("
    wren "{i}huh?{/i}"
    user1 "my mom made her schedule a surgery but the day before she mysteriously got better."
    user1 "it was really weird. my mom doesnt talk about her anymore."
    wren "{i}...?{/i}"
    user1 "anyway i managed to reach out to her, and she's still living happily with her roommate."
    user1 "lol, i think they met around the same time??"
    user2 "LOL you mean girlfriend, right?"
    user1 "what?"
    wren "{i}Hm.{/i}"
    wren "{i}Would surgery work?{/i}"

    "{i} Three hours later. {/i}"

    #Wren is somehow even more exhausted looking.
    wren "{i}Click.{/i}"
    com "Diagnostic Yield of Fiberoptic Bronchoscopy in Evaluating Solitary Pulmonary Nodules. Baaklini et al."
    wren "{i}Click.{/i}"
    # com """
    #     \"Advances in medical imaging and cutting edge robotic surgical assistance have made breakthroughs in 
    #     patient survival with successful recovery rates approaching seventy percent.\" says Dr. Sylvia-
    #     """
    com """
        "CASE STUDY: exploratory laprascopic surgery effectiveness in relieving symptoms of semi- spontaneous foreign matter in 32 yr old Male"
        "See patient fg. 3"
        """
        #insert disgusting xray photo here
    com "Patient recovered lung function to the point where he no longer needed intubation."
    wren "{i}Sigh.{/i}"
    wren "{i}Click.{/i}"
    com "{b}GREENFIELD MEDICAL CENTER PATIENT SIGN UP FORM:{/b} \nPlease use your legal name, sex, and home address."
    wren "{i}...{/i}"
    #wren typing noises
    wren "{i}Click.{/i}"
    com "Welcome MARCUS WERNER. Due to high demand, patients are encouraged to join the waitlist as soon as possible."
    com "Submitting the form costs $30, with an expediency fee of $40, combined with a 25\% administrative surcharge due to high demand."
    stop music fadeout 2.0
    wren "{i}God, mother is going to kill me.{/i}"

    return

label wren_selfcare:

    wren "{i}Yawwwwwwn"
    wren "Fuck this, I'm going to bed."
    "Wren wakes up in"

    return

label end_demo:
    scene bg_thevoid
    "End of Demo."
    return
