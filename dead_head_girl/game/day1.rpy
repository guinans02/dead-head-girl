
label day1:
    call home_day1
    call garden_day1
    call work_day1
    call wren_returns_home_day1
    return


# DAY ONE SCENES
label work_day1:
    scene office_bg
    stop music
    show wren pose1 neutralsad at max_y, center
    wren "{i}4 more hours.{\i}"
    cow1 "Hey, do you know why Liza's been out for the past few days?"
    cow2 "Don't tell anyone else I said this, but it's because her daughter eloped with some {i}woman!{/i} She's been going to grief counseling, poor thing. "
    cow1 "And I thought she was normal... How could she do that to her mother?"
    show wren pose1 eyesclosed
    wren "{i}Sigh.{\i}"
    wren "{i}It's a paycheck. I'm getting money for this.{\i}"
    show wren pose1 pain
    wren "{i}They can't fix the office door?{\i}"
    show wren pose1 neutralsad

    #blurry image
    #wren aberrates chromatically
    phone "{sc}Riiiiiiing{/sc}"

    wren "Yes ma'am. No sir. Let me check that with my supervisor."
    cow1 "Hey um. Uhm. Hey-you."
    wren "Yes? "
    cow1 "Mind swinging by the lab and dropping this package off?"
    wren "I've never been…"
    cow1 "Oh, it's in lab B, 2 doors down and a left."
    cow1 "Careful! That lab equipment is {i}very{/i} expensive!"
    wren "{i}If it matters so much, why don't you take it then?{/i}"

    #wren walks to the lab
    show wren pose1 neutralsad at mv(center, offscreenright, spd=1.0), max_y

    scene lab
    show wren pose1 neutralsad at mv(offscreenleft, left, spd=1.0), max_y
    show kat pose2 neutral at right, max_y
    wren "...?"
    wren "…Kat."
    wren "{i}No way that's Kat. She was so serious about never going into medicine.{\i}" 
    wren "{i}\"I disavow the lab forever!\" and she really believed herself when she said that.{\i}"
    wren "{i}But that's unmistakably Kat.{\i}"
    show kat pose2 shock
    kat "Wren…!?"
    #wren happy
    show wren pose1 smile
    wren "Why are you here?"
    wren "{i}It's been years and you look so different.{\i}"
    wren "I really, really missed you."

    scene school_library
    show wren pose1 neutralsad at max_y, left
    show kat pose2 neutral at max_y, right
    # (Cut to flashback to school library ) 
    wren "Come over to my place!"
    show kat pose1 eyesclosed
    kat "No, your mom's weird. "
    wren "Okay, then I'll come over to yours. "
    show kat pose1 regret
    kat "I told my mom you're a girl now and she doesn't want you in the house. She doesn't want me to get ideas. "
    # (For context, Wren told Kat she was trans long before she was out at school. She came out freshman year to most people, but figured out she was trans in middle school. She only told Kat and her mother.) "
    show wren pose1 pensive
    wren "Well that fuckin' sucks. "
    kat "Yeah, it fuckin' does. "
    show wren pose1 worried one
    wren "Let's just stay here then? "
    show kat pose2 happy
    kat "Fine. Just stop stealing my makeup. If you want it you can just ask. "
    show wren pose1 smile
    wren "You're so much prettier than me. "
    show kat pose2 eyesclosed blush
    kat "LIE. "
    show wren pose1 neutralblush
    wren "Well, my mother at least seems to think so. "
    kat "Ugh, but lace is so itchy. And it doesn't matter when it gets in the way of being a chef. "
    show wren pose1 eyesclosed
    wren "{i}I can't keep up with all her career changes. Last week it was an aeronautics engineer. "
    show wren pose1 bashful
    wren "I'm so jealous."
    kat "Well, if you want to be pretty so bad, let's just do it. "
    show wren pose1 woah
    wren "What?" 
    kat "Follow me."
    # scenery change supply closet 
    scene broomcloset
    show wren pose1 embarrased two at left, max_y
    show kat pose2 smile blush at right, max_y
    # A moment of silence between the two of them. 
    wren "You shouldn't do this kinda thing."
    show kat pose1 relieved
    kat "Why not? If you want it, you should get it."
    wren "I guess."
    show wren pose1 embarrased one
    show kat pose2 happy
    kat "You're lucky I'm here to teach you. My mom is so mean about this sort of thing."
    wren "…"
    show kat pose2 neutralsad
    kat "It's not like I even really wanted those shorts anyways."
    kat "She says I do it just to piss her off."
    show kat pose2 worried three
    kat "That's such bullshit, don't you agree?"
    show wren pose1 bashful
    wren "…"
    show kat pose2 worried one
    kat "What's with you? You normally love this kinda thing. "
    show wren pose1 eyesclosed
    wren "I don't really know how to say it."
    show kat pose2 worried sad
    kat "What, did someone hurt you? Or did you hurt someone? That's okay, it doesn't matter to me. "
    show kat pose2 neutralsad
    kat "I'll go to hell if I need to. "
    wren "{i}You're so dramatic. "
    wren "What if-"
    # foot step sound effect "
    show kat pose2 worried two at mv(right, center, 0.5), max_y
    kat "Shh. "
    # K gets close to w "
    show wren pose1 embarrased one
    kat "..."
    kat "Ok, good. It's clear. So, what were you saying?"
    show kat pose2 happy at mv(center, right, 1.0), max_y
    wren "Um… so…"
    wren "Are you… do you think…"
    wren "What would you say if two girls dated?"
    show kat pose2 worried two
    wren "I kind of have been thinking about it. "
    show wren pose1 smile
    wren "We make a good pair, right? "
    show kat pose2 shock
    stop music
    # music stops "
    kat "…"
    show kat pose1 regret
    kat "I'm not a lesbian. "
    show wren pose1 woah
    wren "I- I'm not saying you are one, but hear me out-"
    show kat pose1 eyesclosed
    kat "What the fuck are you talking about? "
    show wren pose1 pain
    show kat pose1 neutralsad
    wren "Wow you're mad I'm sorry I didn't realize-"
    kat "Let's not do this right now. I have to go. I'll talk to you later. "
    show wren pose1 cry
    wren "Kat. "
    show kat at mv(right, offscreenright, 1.0)
    show wren at mv(left, center, 0.5)
    wren "Kat wait-"
    #play music
    # music starts 
    # Kat leaves, wren is alone in closet 
    # a beat
    # flash back over bg change to lab 

    #snap back to reality

    scene lab
    show wren pose1 neutralsad at left, max_y
    show kat pose2 shock at right, max_y
    kat "It's been a while. "
    wren "{i}That's all you have to say. Is this how it's going to be with you?{\i}"
    wren "Yes, it has. "
    show kat pose2 neutralsad
    kat "So I'm a lab tech now, mostly been supporting the research and development division."
    wren "Mhm… "
    show kat pose2 happy
    kat "They're trusting me with a lot of responsibility. I recently went to a talk given by Dr. Grice, I'm so lucky to work under such a prestigious director. Running the bio- assays is- "
    kat "I hope I'm not boring you. "
    show wren pose1 pensive
    wren "It's interesting, go on. "
    show kat pose2 neutral
    kat "No, I don't think so. "
    show wren pose1 bashful
    wren "{size=15}I just thought you were done with this stuff."

    kat "What? I've never said anything like that. "
    wren "Isn't this directly in the medical corporate culture you hated? "
    kat "I don't even know why you would bring that up."
    show kat pose2 shock
    kat "I'm not gonna apologize for my success. "
    show wren pose1 neutralsad
    wren "Yes… you're clearly doing well for yourself now."
    show kat pose1 relieved
    kat "Yeah, well, I grinded my ass off to get this position so I'm going to enjoy it. "
    wren "That's great. "
    kat "Agh! "
    show wren pose1 angry
    wren "What do you want me to say? "
    show kat pose1 eyesclosed
    kat "Wren. "
    show kat pose2 happy
    kat "You'll join me on my walk home together after work? "
    show wren pose1 embarrased one
    wren "{size=15}Whatever you want."
    show kat pose2 happy
    kat "What?"
    show wren pose1 bashful
    wren "I said yes."
    show kat pose2 smile blush
    kat "Okay. Nice. Good. "
    kat "It'll be like old times. "
    show kat pose1 relieved
    kat "By the way, don't mention anything to anyone here. I don't do office rumors and I hate lying bitches."
    # (Wren back at her desk.) 
    scene office_bg
    show wren pose1 embarrased one at center, max_y
    wren "{i} Mother, no, it's fine. Yes I'm showing up with my friend who I haven't talked to in years and that I spent an entire month sobbing about. "
    wren "{i} No, I don't want anything. No, I don't know where she gets her clothes from. "
    show wren pose1 eyesclosed
    wren "{i}Mother, are you fucking stupid? "
    show wren pose1 neutralsad
    cow2 "Ahh, the end of another daily grind. "
    show wren at mv(center, offscreenright, 1.0)
    wren "Bye."
    scene houses
    show wren pose1 neutralsad at mv(offscreenleft, left, 0.5), max_y
    show kat pose2 neutralsad at right, max_y
    # bg change to outside, at night. Kat is already there. "
    #"They are both silent. "
    play ambience cicadas_quiet fadein 2.0
    wren "..."
    kat "..."
    # cicada noise in bg "
    #Cicadas: BZZZZZZ ( too silly??) "
    ""
    show wren pose1 bashful
    wren "{i}I knew you were too cowardly to speak first, Kat. "

    #we need cicada ambience stat

    menu kat_one:
        "Why did you ignore all of my messages after graduation?":
            #+1 kat affection
            $kat_obj.update_score(1)
            show kat pose2 shock
            kat "Whatever do you mean? "
            show wren pose1 eyesclosed
            wren "You know what I'm talking about. After that conversation, you just stopped talking to me entirely."
            show kat pose1 sad
            kat "I don't recall that."
            show wren pose1 angry
            wren "Does the word L-E-S-B-I-A-N mean anything to you? "
            show kat pose1 regret
            kat "Shut the fuck up, you don't know anything about me. "
            wren "Make me. "
            show kat pose2 eyesclosed blush
            kat "..."
            wren "{i} I knew that would get something out of you. {/i}"
            
        
        "How's your parents' business? Still booming?":
            show kat pose2 neutral
            kat "They're doing better than ever. My father's taking a trip to Shanghai to promote the business right now. "
            show wren pose1 neutralsad
            wren "How lovely. "
            wren "You'd think with all that money they'd buy you some human decency."
            kat "Stop taking out your stress on me. I'm being nice here."
            wren "You're so wierd." 
            show kat pose2 happy
            kat "How are yours doing? Is your dad still gone and your mom still nutso? "
            show wren pose1 angry
            wren "… Fuck you."
            show kat pose2 smile blush
            kat "Ha. As if, you'd just run out of the room as soon as I got naked. "
            show wren pose1 neutralblush
            wren "You're the nutter."
            kat "I could do whatever I want with you. "
            wren "So do it."
            kat "The cops will never believe you."
            wren "{b}What???{/b}"
            show wren pose1 neutralsad

    kat "Hey, we're here."
    #scene houses 
    show kat pose2 smile blush at max_y, right
    kat "Bye, Wren. It was wonderful catching up with you!"
    wren "I don't get you."
    kat "That's okay."
    kat "As long as you keep talking to me?"
    kat "Please."
    wren "You're not gonna ghost me again, are you?"
    kat "I couldn't live with myself. It was so hard the last time. "
    kat "Well?"
    kat "Wren?"
    #wren twist in the chest scene
    #scene houses
    wren "I'll see you at work. Bye."
    stop ambience
    stop music
    return

label garden_day1:
    #Garden Scene
    scene garden
    #something weird going on here. only birdsong
    #actually, no bug, just that this music is quiet. make it louder?
    play music garden_music
    play ambience garden_amb
    show wren pose1 neutralsad at max_y, mv(offscreenleft, center, 1.0)
    #transform flip wren horiz too goofy?
    wren """
        Hello?

        Is anyone here?

        Excuse me?

        Sure. I guess. That's okay.
        """ 

    show wren pose1 neutralsad at mv(center, left, 1.0), max_y

    wren "{i}What am I supposed to...?{/i}"

    show target at truecenter

    wren "{i} What an ugly thing. {/i}"

    # flower bud pre crush scene

    show crushed at truecenter

    hide target

    wren "{i}Hm.{/i}"

    hide crushed with dissolve

    # flower bud post crush
    #scene garden

    #Sound effect, boss music?
    #show ines_fg at mv(offscreenright, right, 0.25), max_y #ines jumpscare
    show ines pose2 frustrated at mv(offscreenright, right, 0.25), max_y #ines jumpscare
    strange "I- {b}excuse me!? {/b}{sc}{b}What are you doing??{/b}{/sc}"
    wren "Nothing."
    strange "Seriously? You crushed the flower and didn't even pick it... get out! Open hours are closed!"
    wren "I was supposed to volunteer here..."
    
    show ines pose2 shock
    strange "Oh. OH!"
    ines "Welcome! I'm Ines, sorry for yelling."

    show ines smile 
    wren "I'm Wren. Thanks."
    ines "This is the Dreamflower Gardens! So, how'd you get started with us here?"
    wren "It's the closest to my house that accepts volunteers."
    ines "Oh. Okay. Do you have any experience gardening?"
    wren "No."

    show ines worried
    ines "Haha ummmm that's okay, I'll teach you! Do you have a favorite plant?"
    wren "No." #Girlboss behavior right there

    show ines pose2 fanatic 
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
    #"*Ines blushes."
    show ines pose2 shock
    ines "Yes, you!"
    wren """
        ...

        He-

        Wh-
        """
    
    show ines pose2 smile
    ines "Umh! Okay! Wow! Well, let's take care of the gardenias, they need some pruning before they flower."
    ines "I like to pinch off the smaller buds, so I can get a few really big blooms."
    show ines pose2
    ines "It used to be used as medicine way back, but now people just use it for decoration."
    ines "Look, they are just starting to get the scent."
    # cg add maggot bud cg
    show target at truecenter
    wren "{i}It looks like a little maggot.{/i}"
    wren "I'm not sure…"
    hide target 
    #dreamy music plays, the moment lingers
    ""
    ines "Could I draw you?"
    jump post_ines_one

    label no_fun:
    wren "I get it already. Stop making fun of me."
    show ines pose2 frustrated
    ines "I'm not making fun of you!"
    wren "How do I know that?"
    ines "First of all, I don't even know you."
    wren "{i}Wow.{/i}"
    show ines pose2 fan
    ines "Second, look at your face, your hair!"
    ines "...your eyebrows. You'd look so lovely in Matisse's style."
    wren "Why Matisse..."
    show ines pose2 woah
    ines "Ugh, and she knows the Fauvists! Actually-"
    show ines pose2 smile
    ines "Could I draw you?"

    label post_ines_one:
    #Transition back to normal garden 
    show ines smile two
    wren "what? Why?"  
    ines "I'm taking a portraiture class and I'm behind."
    ines "Well, actually I'm not, but my portfolio makes me want to vomit and I need new pieces." 
    ines "C'mon, you clearly don't like the garden." 
    wren "What do I need to do?" 
    ines "Just sit here and pose."

    wren "I've just never done something like this before." 
    ines "You're a natural." 
    "sketch sketch sketch scribble noise"
    #add sound effect
    wren "{i}I'm sweaty and my hearts running a mile a minute and I'm sure I have armpit stains and she's just staring at me.{/i}" 
    wren "Should I move my hands or smile more?"
    ines "No, just stay still. Whatever I paint will turn out beautiful."
    wren "You've said that…" 
    ines "Have I?" 

    
    label highschool_flashback:
    # """
    # A non-transitioned Wren dressed much more shabbily than we know her. She's in a faceless crowd following a random upperclassman as they get a tour for a club fair. 
    # upperclassman - and here is the art club room
    # *"""
    show wren pain
    wren "Why do I remember her...?"
    stop ambience
    scene artclass
    show wren_baby at left, max_y
    show ines_baby at right, max_y

    strange "Hey Ines, come say hi to the fresh meat."
    ines "Aw, don't be mean Macy."
    ines "“Heya, I'm Ines, the vice president of the art club. You all came at the perfect time! I've just put the final touches on my painting! Isn't it pretty?"
    strange "The colors are gorgeous!"
    #wren surprised
    show ines_look_at_this_photograph at center:
        xysize (1280, 720)
    wren "Is that… a dead bird?"
    ines "Yes! What, do you think the shading is off?" 
    wren "Well… the subject matter is…"
    wren "{i}Weird. If I went home with paint streaked clothes, or a painting like that… well, mother would certainly be hysterical.{/i}" 
    ines "What? The subject doesn't matter. Whatever I paint will turn out beautiful."
    hide ines_look_at_this_photograph
    #"{i}Ines smiles.{/i}"
    strange "Okay, okay, time to go to the next club. See you around, Ines."
    ines "Bye! Hope to see you all in here again." 
    #"As the students file out, Ines makes eye contact with Wren, smiles, and waves to just her." 
    wren "{i}Why is she looking right at me.{/i}" 
    wren "{i}Such a hypocrite. What a liar. It's cruel to make people look at decaying shit like that.{/i}" 
    wren "{i}Why not paint a still life.{/i}"
    wren "{i}Nah, you're too good for that Ms. \"subject matter doesn't matter.\"{/i}"
    wren "{i}I'm never coming here again.{/i}"

    #snap back to reality
    scene garden
    play ambience garden_amb fadein 1.0
    show wren pose1 cry at left, max_y
    show ines pose2 smile at right, max_y

    wren "{i}..."

    show wren pose1 eyesclosed
    wren "Maybe. I don't know."

    show wren pose1 neutralblush
    ines "You're so weird."
    ines "Sorry."
    show ines worried
    ines "Do you really hate my garden that bad?"
    show wren pose1 worried one
    wren "No-I mean yes."
    show ines pose2 shock
    ines "What?!"
    show wren pose1 bashful
    wren "It's not {i}your{\i} garden. It's pretty much any garden."
    show ines pose2 sad
    ines "Why?"
    show wren pose1 embarrased one
    wren "I stepped in one of those underground wasp's nests. At the botanical garden off Main?"
    wren "It doesn't really matter."
    show ines pose2 neutralsad
    ines "If you say so."
    show wren pose1 neutralsad
    show ines smile one
    ines "Can you keep that expression, just like that?"
    wren "Okay."
    #Drawing done
    show ines_wren_sketch at truecenter: 
        zoom 0.5
    wren """
        {i}It's kind of warm and soft and melty.
        It looks like me if I was in love...

        Then why is it so creepy? {\i}
        """
    hide ines_wren_sketch
    show ines laugh two
    ines "So!!! What do you think?!"
    wren "It's..."

    #two options, depending on what the player chose earlier
    python:
        #if ines' opinion of wren increased during the garden scene
        if ines_obj.get_score() > ines_initial_score:
            #player chose "who, me?"
            renpy.jump("ines_day1_good")

        else:
            #player chose "stop making fun of me"
            renpy.jump("ines_day1_bad")
            

    label ines_day1_good:
        wren "I've never looked like this." 
        show ines fanatic one
        ines "Yes you do. When I look at you. I can see what you keep hidden underneath that layer of grime. "
        wren "Excuse me? I literally showered this morning?" 
        show ines laugh one
        ines "Not like that!"
        show ines blush two
        ines "I mean to say, I see you."
        jump ines_day1_post_choice

    label ines_day1_bad:
        wren "You really weren't lying"
        show ines fanatic one
        ines "I love showing people a new way of seeing the world. "
        ines "It's stupid to not see the beauty in yourself." 
        show ines pose2 frustrated
        wren "Don't call me stupid." 
        ines "God, I just can't say the right thing."
        show ines pose2 neutralsad
        ines "I mean to say, I see you."

    label ines_day1_post_choice:
    #Phone alert
    phone "{i}{sc}Bzzzzzzz."
    wren "And that's time. I'm out of here."
    show ines pose2 shock
    ines "What?!"
    show ines pose2 worried
    ines "You're going to come back, right?"
    wren "I have to. I committed to the hours."
    wren "{i}And I need to do something that isn't staying at home.{/i}"
    show ines pose2 laugh
    ines "I knew you didn't hate me! It'll be so much fun to work with you!!"
    wren "Work?"
    show ines pose2 smile
    ines "I want a really big piece for my portfolio, so I need someone to pose for me an oil painting?"
    wren "Um?"
    show ines pose2 worried
    ines "Oh..."
    wren "I gotta go now."
    show ines pose2 pain 
    ines "Fine! I'll do your part of the garden work! Just let me draw you! I promise, it'll be really easy!"
    wren "Whatever."
    show ines pose2 shock
    ines "That's a yes?!"
    wren "Sure."
    show ines pose2 laugh
    ines "You're so super amazing awesome Wren!"
    ines "Come here. A hug for my special girl." 

    stop music
    stop ambience
    show ines blush three
    #"Ines impulsively hugs wren who stiffens, turns red, and feels a twisting in her chest."
    #cut to the visual of a flower stem sprouting in a body

    wren """
        {i}I spent way longer than I intended.

        I don't even have any time to lay down, why is my shift so soon...

        I can't believe she wants me to model...{\i}
        """
    return


label home_day1:
    #Intro scene, Wren at home
    scene bathroom #bathroom?
    play music house_music
    show wren pose1 neutralsad at max_y, center#get more silly with this I think
    
    wren "It's okay."
    wren "It's just odd that it happened twice."
    hide wren

    #Wren talks to mom
    scene living_room
    #"*wren steps outside into-*"

    show mom_fg at left, max_y
    show wren pose1 neutralsad at max_y, mv(offscreenleft, right, 1.0)
    mom "Wren? Are you okay?"
    show wren pose1 eyesclosed
    wren "Why?"
    mom "You look pale. Have you been getting enough sun?"
    show wren pose1 neutralsad
    wren "Yes, Mother."
    mom """
        Well, good then.

        It's because you don't have friends. Loneliness is worse for you than cigarettes.
        """
    show wren pose1 angry
    wren "{i}You don't have any friends, Mother.{/i}"
    show wren pose1 neutralsad
    wren "Yes Mother. I'll do that Mother."

    #"Wren leaves the house."
    hide mom_fg

    phone "{sc}bzzz{\sc}"
    phone "Reminder: volunteer at greenhouse1!!"
    show wren pose1 angry
    wren "{i}Why did they HAVE to assign me to the garden? Was there really nothing else?{/i}"
    show wren at max_y, mv(right, offscreenright, 0.5)

    return

#katriel scenes!!

label wren_research:
    # scene where wren obsessively researches Hanahaki Disease
    # frenetic. gare du nord? use a movie? animations I think

    #play music research_music fadein 1.0 loop

    scene wren_bedroom
    show wren pose1 neutralsad at center, max_y
    #desk, glow effect from screen
    #Wren clearly hasnt been sleeping.
    wren "Think think think."
    wren "{i}google why am I vomiting flowers{/i}"
    user2 "OMG I cant believe that stupid bitch got hanahaki OBVS shes not in love! she doesn't spend enough time outside for that lel"
    user1 "dont joke about that?? its real, my aunt almost died from it >:("
    wren "{i}huh?{/i}"
    user1 "my mom made her schedule a surgery but the day before she felt way better."
    user1 "it was really weird. my mom doesnt talk about her anymore."
    wren "{i}...?{/i}"
    user1 "yeah I think she's some kinda bookstore owner now with her partner"
    user2 "LOL you mean girlfriend, right?"
    user1 "what?"
    wren "{i}Hm.{/i}"
    wren "{i}Would surgery work?{/i}"

    #"{I} Three hours later. {/i}"

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

label qte_fail:
    stop music
    scene wren_bedroom
    show wren pose1 neutralsad at max_y, center

    wren """
        Actually.
        I'm going to lay down.
        """
    #Screen goes red and shaky
    wren "No one checks in on me. Everyday the same."

    #Screen starts dripping
    wren "People are all terrible anyways."

    #Scary music
    wren "{i}Hah... Fuck...{/i}"

    wren """
        I hope whoever cleans my body has a ball.

        Bye Ines.

        Bye Katriel.
        
        Bye Mother. 

        Bye, Wr-

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
    show wren pose1 neutralsad at max_y, center
    image black = "#000"

    wren """
        {b}FUCK!{/b}

        I don't want to.

        Ah, I just need to stop being a whiny bitch and choose.

        I'd literally rather die than go out tonight.
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
            $choice = "wren "
            jump wren_chooses_wren

    label fave_choice_out:
    scene bg_thevoid
    wren "Why do I feel so nauseous?"
    # typing noises
    wren """
        I have to. It's because I have to.
        
        Mother doesn't keep any alcohol in the house.

        Well, she'd kill me if I tasted her wine anyways.

        I'm wasting time.

        God.

        Fine fine fine.
        """
    
    if choice != "wren ":
        #cut to wren phone
        #$ choice = "Hey, " + choice + " can we meet tonight? I have something to tell you."
        phone "Hey, [choice] can we meet tonight? I have something to tell you."

    if choice == "Ines":
        phone "okay!!! <3 <3 <3"
    
    elif choice == "Kat":
        phone "I'll be there."
    
    return

label wren_returns_home_day1:
    scene living_room
    show mom_fg at right, max_y, Transform(xzoom=-1.0)
    show wren pose1 neutralsad at mv(offscreenleft, left, 0.5), max_y

    wren "Hello Mother. "
    mom "You're back late. Remember it's unsafe out there for a girl your age! "
    wren "Yes, Mother. "
    mom "You can be so forgetful. It makes me worry for you. "
    wren "Maybe I should get it checked out by a doctor, do you think? "
    mom "Darling, you just need to try harder. You can't stay a child forever. "
    wren "Thank you. "
    mom "…. "
    wren "I'm going up to my room now, is that okay? "
    mom "Get some rest, Wren. "

    show wren pose1 neutralsad at mv(left, offscreenright, 1.0)
    scene wren_bedroom
    show wren pose1 neutralsad at mv(offscreenleft, center, 1.0), max_y
    play music wren_room

 
    wren "Ugh, it feels like something is crawling up my nose. "
    #Screen effect, coughing up petal, nasty sound fx
    wren "Ugh… "
    wren "Did I loose a tooth from coughing that hard? "
    wren "It's too soft for that. "
    wren "It looks like a flower petal… "
    wren "It's always me who has to deal with shit like this. "

    call wren_research

    stop music
    play music obsession
    wren "You know what? "
    wren "No. "
    wren "google xxxflixx.net"
    com "{b}SISSYBOY GETS URETHRA POUNDED AND STRETCHED BY MISTRESSES ELECTRIFIED IRON ROD{/b}"
    wren "Sigh. "
    play ambience zipper noloop
    #(Unzip sound, music change?)
    # (add jerking off sounds)
    wren "ghn"
    wren "ack"
    wren "I need to open a window! "
    wren "Help..  "
    # ( add bloody lump cg) 
    wren "hnnnnn"
    wren "That's so gross. "
    wren "Did I just cough up my own lung?"
    wren "No, it's too soft for that. "
    wren "Some kind of... plant?"
    wren "Ew ew ew!"
    wren "I don't know wether to flush you down the toilet, or just throw you out the window."
    #(Lmao would it be funny to have a player choice here where it just changes the sound effect, u either have a toilet flush or a window sound) "
    wren "Wait, should I have saved it for a doctor?"
    wren "But I can't afford that. "
    wren "How am I.. Could I… ? "
    wren "You know what? "
    stop music

    wren "I'm done with today."
    scene wren_bed
    wren "..."
    wren "How desperate do I have to get? "
    return
