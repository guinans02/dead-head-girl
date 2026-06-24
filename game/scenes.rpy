
# The game starts here.
label start:
    stop music
    
    call val_scenes_1
    call garden_day1
    call wren_work
    call wren_research
    call end_demo
    return

label wren_work:
    scene office_bg
    show wren_fg at max_y, center

    """
    Wren walks into busy office. No one says hi to her. 

    She overhears a conversation: maybe something about kink? And his disgusting it is? Office gossip? Trans phobia? Homophobia? It's not pleasant.
    """
    wren "{i}It's a paycheck. I'm getting money for this.{\i}"
    wren "{i}They can't fix the office door?{\i}"

    "The hours pass by in a blur."

    "*Wren leaves work*"

    return

label garden_day1:
    #Garden Scene
    scene garden
    #something weird going on here. only birdsong
    #actually, no bug, just that this music is quiet. make it louder?
    play music garden_music
    play ambience garden_amb
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
    
    #might be a better way to implement this
    #capture initial ines score 
    #(Should be zero, but this implementation allows for this scene to move around and still work)
    default ines_initial_score = 0
    $ines_initial_score = ines_obj.get_score()

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
    ines "Yes, you!"
    wren """
        ...

        he-

        wh-
        """
    ines "Umh! Okay! Wow! Well, let's take care of the gardenias, they need some pruning before they flower."
    "Wren follows Ines to a gardenia bush, covered in buds and a few partial blooms. "
    ines "I like to pinch off the smaller buds, so I can get a few really big blooms."
    ines "It used to be used as medicine way back, but now people just use it for decoration."
    ines "Look, they are just starting to get the scent."
    "Ines plucks off one of the partially blooming flowers and cups it in her hand."

    wren "{i}It looks like a little maggot.{/i}"
    wren "I'm not sure…"
    "Ines hold it up to her face and against her better instincts Wren leans in."
    #dreamy music plays, the moment lingers
    ines "Could I draw you?"
    jump post_ines_one

    label no_fun:
    wren "I get it already. Stop making fun of me."
    ines "I'm not making fun of you!"
    wren "How do I know that?"
    ines "First of all, I don't even know you."
    wren "{i}Wow.{/i}"
    ines "Second, look at your face, your hair!"
    ines "...your eyebrows. You'd look so lovely in Matisse's style."
    wren "Why matisse..."
    ines "Ugh, and she knows the Fauvists! Actually-"
    ines "Could I draw you?"

    label post_ines_one:
    #Transition back to normal garden 
    wren "what? Why?"  
    ines "I'm taking a portraiture class and I'm behind."
    ines "Well, actually I'm not, but my portfolio makes me want to vomit and I need new pieces." 
    ines "C'mon, you clearly don't like the garden." 
    wren "What do I need to do?" 
    ines "Just sit here and pose."

    wren "I've just never done something like this before." 
    I- You're a natural." 
    "sketch sketch sketch scribble noise"
    #add sound effect
    wren "{i}I'm sweaty and my hearts running a mile a minute and I'm sure I have armpit stains and she's just staring at me.{/i}" 
    wren "Should I move my hands or smile more?
    I - "No, just stay still. Whatever I paint will turn out beautiful."
    wren "You've said that…" 
    I - "Have I?" 

    
    label highschool_flashback:
    """A non-transitioned Wren dressed much more shabbily than we know her. She's in a faceless crowd following a random upperclassman as they get a tour for a club fair. 
    upperclassman - and here is the art club room
    *"""
    strange "Hey Ines, come say hi to the fresh meat."
    ines "aw, don't be mean Macy."
    ines "hi everyone! I'm Ines, the vice president of the art club here!"
    ines "“Heya, I'm Ines, the vice president of the art club. You all came at the perfect time! I've just put the final touches on my painting! *spins around* Isn’t it pretty?"
    strange - "The colors are gorgeous!"
    wren "(wasn't paying attention, but speaks in shock) Is that… a dead bird?"
    ines "Yes! What, do you think the shading is off?" 
    wren "Well… the subject matter is…"
    wren "{i}Wierd. If I went home with paint streaked clothes, or a painting like that… well, mother would certainly be hysterical.{/i}" 
    ines "What? The subject doesn't matter. Whatever I paint will turn out beautiful."
    "{i}Ines smiles.{/i}"
    strange "Okay, okay, time to go to the next club. See you around, Ines."
    ines "Bye! Hope to see you all in here again." 
    "As the students file out, Ines makes eye contact with Wren, smiles, and waves to just her." 
    wren "{i}Such a hypocrite. What a liar. It's cruel to make people look at decaying shit like that.{/i}" 
    wren "{i}Why not paint a still life.{/i}"
    wren "{i}Nah, you're too good for that Ms. \"subject matter doesn't matter.\"{/i}"
    wren "{i}I'm never coming here again.{/i}"

    #snap back to reality
    wren "Maybe, I don't know"
    ines "You're so weird."
    ines "Sorry."
    ines "Do you really hate my garden that bad?"
    wren "No- I mean yes."
    ines "What?!"
    wren "It's not {i}your{\i} garden. It's pretty much any garden."
    ines "Why?"
    wren "I stepped in an underground wasps nest at the botanical garden once. It doesn't really matter."
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
    "{i}However, the proportions are a little off, and the color makes Wren look like she's not a living body.{/i}"
    ines "So!!! What do you think?!"
    wren "It's..."

    #two options, depending on what the player chose earlier
    python:
        #if ines' opinion of wren increased during the garden scene
        if ines_obj.get_score() > ines_initial_score:
            #player chose "who, me?"
            pass
        
        else:
            #player chose "stop making fun of me"
            
            

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
    return


label val_scenes_1:
    #Intro scene, Wren at home
    scene bathroom #bathroom?
    play music house_music
    show wren_fg at max_y, center#get more silly with this i think
    
    wren "It's okay."
    wren "It's just odd that it happened twice."
    show wren_fg at max_y, center
    hide wren_fg

    #Wren talks to mom
    scene house
    "*wren steps outside into-*"

    show mom_fg at left, max_y
    show wren_fg at max_y, mv(offscreenleft, right, 1.0)
    mom "Wren? Are you okay?"
    wren "Why?"
    mom "You look pale. Have you been getting enough sun?"
    wren "Yes mother."
    mom """
        Well, good then.

        It's because you don't have friends. Loneliness is worse for you than cigarettes.
        """
    wren "{i}You don't have any friends, mother.{/i}"
    wren "Yes mother. I'll do that mother."

    "Wren leaves the house."
    hide mom_fg

    phone "{sc}bzzz{\sc}"
    phone "Reminder: volunteer at greenhouse"

    wren "{i}Why did they HAVE to assign me to the garden? Was there really nothing else?{/i}"
    show wren_fg at max_y, mv(right, offscreenright, 0.5)

    return

label val_scenes_0:

    #Intro scene, Wren at home
    scene bathroom #bathroom?
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

    scene house
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

    #walking to internship
    scene bg_thevoid
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

    play music research_music fadein 1.0 loop

    scene wren_bedroom
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
    #wren tries to masturbate or something
    wren "{i}Yawwwwwwn"
    wren "Fuck this, I'm going to bed."
    "Wren wakes up in"

    return

label qte_fail:
    stop music
    scene wren_bedroom
    show wren at max_y, center

    wren """
        ...

        I've had enough.

        I'm going to lay down.
        """
    #Screen goes red and shaky
    wren "No one checks in on me. I do so much for others."

    #Screen starts dripping
    wren "People are all terrible anyways."

    #Scary music
    wren "{i}ragged breath{/i}"

    wren """
        I hope whoever cleans my body has a ball.

        Bye Ines.

        Bye Katriel.

        Bye, wr-

        Okay, Wren. It's okay.
        """
    #screen goes black, zoom out

    #wren is lying face down on her floor

    #fly buzzing sounds. she's alone

    #Flowers and petals and blood and leaves form in a pool around her.

    #There's a blank piece of paper

    #End of game.

    return

label wren_chooses:
    scene wren_bedroom
    show wren_fg at max_y, center
    image black = "#000"

    wren """
        I don't want to.

        Ah, I just need to stop being a whiny bitch and choose.

        I'd literally rather die.
        """

    #screen goes bloody, cough SFX
    wren "{i}wheeeeeze{/i}"
    #screen goes black
    scene black

    wren "Ugh. Ugh!"
    default choice = ""
    menu wren_favorite:
        "Fine. I pick:"

        "Ines.":
            $choice = "Ines"
            jump fave_choice_out
        
        "Katriel.":
            $choice = "Kat"
            jump fave_choice_out

        "Myself.":
            $choice = "Wren"
            jump wren_chooses_wren

    label fave_choice_out:
    scene bg_thevoid
    wren "Why do I feel so nauseous."
    "wren taps away at her phone"
    wren """
        I have to. It's because I have to.
        
        Mother doesn't keep any alcohol in the house.

        Well, she'd kill me if I tasted her wine anyways.

        I'm wasting time.

        God.

        Fine fine fine.
        """
    
    if choice != "Wren":
        #cut to wren phone
        #$ choice = "Hey, " + choice + " can we meet tonight? I have something to tell you."
        phone "Hey, [choice] can we meet tonight? I have something to tell you."

    if choice == "Ines":
        phone "okay!!! <3 <3 <3"
    
    elif choice == "Kat":
        phone "I'll be there."
    
    return
    
label katriel_meetup:
    kat "I'm here."
    wren "{i}sputters, chokes{/i}"
    kat "What did you want to tell me, Wren?"
    wren "I-"
    kat "Don't tell me it's terminal. I'm not ready to mourn you."
    "*Katriel chuckles*"
    wren "It's not that, it's-"
    "Wren swallows down a lump of petals."
    wren "I love you."
    wren "That's what I wanted to say."
    "Wren turns bright red and walks away."

    call kat_end
    return

label end_demo:
    scene bg_thevoid
    "End of Demo."
    return
