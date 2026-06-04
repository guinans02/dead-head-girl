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
    call wren_research
    call val_scenes
    call end_demo
    return

label val_scenes:

    #Intro scene, Wren at home
    scene house #bathroom?
    show wren_fg at max_y, center#get more silly with this i think
    
    # python:
    #     for i in range(1, 10):
    #         renpy.show("wren_fg", atl=chromatic(i))

    #no name, mirror. chromatic abberation? blur?
    "It's okay."
    "It's just odd that it happened twice."
    show wren_fg at max_y, center
    hide wren_fg

    "*wren steps outside into-*"

    show whitney at left, max_y
    show wren_fg at max_y, mv(offscreenleft, right, 1.0)
    mom "Wren? Are you okay?"
    #wren's name is now known to the reader
    wren "Why?"
    mom "You look pale. Have you been getting enough Vitamin A?"
    wren "Yes mother. "
    mom "Well. Good then. " 
    mom "It's because you haven't spent enough time with your little friends. Loneliness is worse for you than cigarettes. "
    wren "{i}You don't have any friends, mother.{/i}"
    wren "Yes mother. I'll do that mother."
    hide whitney
    hide wren_fg
    "*wren is finally allowed to leave*"

    #out in public
    show bg_thevoid
    show wren_fg at max_y
    phone "{sc}-bzzzzzzz-{/sc}"
    phone "Reminder: Volunteer work."
    wren "{i}Why did they HAVE to assign me to the garden? There really wasn't anything else there?{/i}"
    hide wren_fg

    #Garden Scene
    show garden
    "At the garden..."
    show wren_fg at left, max_y
    "She goes to the garden and no one is there. She feels numb/cold looking at all the wilting flowers."
    wren "{i}Someone else should be here by now.{/i}"

    "She starts playing with a flower bud, eventually crushing it."
    wren "{i}Wow.{/i}"
    "She reaches out and-"
    show gs_dog at mv(offscreenright, right, 0.25), max_y #ines jumpscare
    strange "{sc}{b}WHAT ARE YOU DOING ??????{/b}{/sc}"
    wren "Nothing."
    strange "Oh my god, seriously? That wasn't even one that needed pruning?? Get out!!"
    wren "I'm here to volunteer though…"
    #ines is introduced ?
    ines "Oh. OH! Omg ur the new volunteer they assigned me hey thnxxxx"
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
    wren "{i}God, Mom is going to kill me.{/i}"

    stop music fadeout 1.0
    return

label end_demo:
    scene bg_thevoid
    "End of Demo."
    return
