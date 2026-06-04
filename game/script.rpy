# Declare characters used by this game.
define wren = Character(name="Wren", color="#ffffff") #white
define ines = Character(name="Ines", color="#fd9855") #light orange
define kat = Character(name="Katriel", color="#d161a2") #light magenta
define mom = Character(
    name="Mom", 
    font="fonts/EBGaramond-VariableFont_wght.ttf", 
    what_font="fonts/EBGaramond-VariableFont_wght.ttf"
    )
define phone = Character(
    name="Phone", 
    color="#097969", #cadmium green
    font="fonts/SpaceMono-Regular.ttf", 
    what_font="fonts/SpaceMono-Regular.ttf"
    )
define strange = Character(name="Stranger")

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
    call val_scenes
    call wren_research
    call end_demo
    return

label val_scenes:

    #Intro scene, Wren at home
    scene house #bathroom?
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
    show wren_fg at max_y, mv(right, offscreenright, 0.5)
    ""
    hide mom_fg
    
    #walking to internship
    show wren_fg at max_y, mv(offscreenleft, center, 1.0)
    wren """
        yes thank you mother 3 bags full mother

        Maybe if I didn't need to get perfect grades I'd have some friends.

        Maybe if you got off your lazy ass and actually parented me I'd be better at talking to people.

        ...that's not fair. I'm sorry. I know she's trying her best. It's not easy.

        ...It's not easy...

        Could it not get any hotter? I'm already feeling faint.
        """
    show wren_fg at max_y, mv(center, offscreenright, 1.0)
    #Garden Scene
    scene garden
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
    return

label wren_research:
    # scene where wren obsessively researches Hanahaki Disease
    # frenetic. gare du nord? use a movie? animations i think

    define user1 = Character(
    name="user1", 
    color="#097969", #cadmium green
    font="fonts/SpaceMono-Regular.ttf", 
    what_font="fonts/SpaceMono-Regular.ttf"
    )

    define user2 = Character(
    name="user2", 
    color="#097969", #cadmium green
    font="fonts/SpaceMono-Regular.ttf", 
    what_font="fonts/SpaceMono-Regular.ttf"
    )

    define com = Character(
    name="Computer", 
    color="#097969", #cadmium green
    font="fonts/SpaceMono-Regular.ttf", 
    what_font="fonts/SpaceMono-Regular.ttf"
    )

    image black = "#000"
    play music "music/johnny_ripper - gare du nord.mp3" fadein 1.0 loop

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
        \" CASE STUDY: exploratory laprascopic surgery effectiveness in relieving symptoms of semi- spontaneous foreign matter in 32 yr old Male \"
        \" See patient fg. 3\"
        """
        #insert disgusting xray photo here
    com "Patient recovered lung function to the point where he no longer needed intubation."
    wren "{i}Sigh.{/i}"
    wren "{i}Click.{/i}"
    com "{b}GREENFIELD MEDICAL CENTER PATIENT SIGN UP FORM:{/b} Please use your legal name, sex, and home address."
    wren "{i}...{/i}"
    #wren typing noises
    wren "{i}Click.{/i}"
    com "Welcome MARCUS WERNER. Due to high demand, patients are encouraged to join the waitlist as soon as possible."
    com "Submitting the form costs $30, with an expediency fee of $40, combined with a 25\% administrative surcharge due to high demand."
    stop music fadeout 2.0
    wren "{i}God, mother is going to kill me.{/i}"

    return

label end_demo:
    scene bg_thevoid
    "End of Demo."
    return
