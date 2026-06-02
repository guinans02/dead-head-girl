# Declare characters used by this game.
define wren = Character(_("Wren"), color="#ffffff")
define ines = Character(_("Ines"), color="#fd9855")
define kat = Character(_("Katriel"), color="#d161a2")
define mom = Character(_("Mom"))
define phone = Character(_("Phone"))
define strange = Character(_("Stranger"))

# The game starts here.
label start:
    jump val_scenes
    return

label val_scenes:

    #Intro scene, Wren at home
    scene bg_thevoid
    show borzoi
    #no name
    "It's okay."
    "It's just odd that it happened twice."
    #edit these out when art has been installed
    hide borzoi

    "*wren steps outside into a hot summer day*"

    show whitney at left
    show borzoi at right
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
    hide borzoi
    "*wren is finally allowed to leave*"

    show borzoi 
    "{sc}-bzzzzzzz-{/sc}"
    # import a monospaced font .ttf file
    # e.g. "Try out the {font=mikachan.ttf}mikachan font{/font}."
    phone "Reminder: Volunteer work."
    wren "{i}Why did they HAVE to assign me to the garden? There really wasn't anything else there?{/i}"
    hide borzoi

    #Garden Scene
    "At the garden..."
    show borzoi at left
    "She goes to the garden and no one is there. She feels numb/cold looking at all the wilting flowers."
    wren "{i}Someone else should be here by now.{/i}"

    "She starts playing with a flower bud, eventually crushing it."
    wren "{i}Wow{/i}."
    "She reaches out and-"
    show gs_dog at right
    strange "{b}{sc}WHAT ARE YOU DOING ??????{/sc}{/b}"
    wren "Nothing."
    strange "Oh my god, seriously? That wasn't even one that needed pruning?? Get out!!"
    wren "I'm here to volunteer though…"
    #ines is introduced ?
    ines "Oh. OH! Omg ur the new volunteer they assigned me hey thnxxxx"


    return

label test:

    scene bg_thevoid
    show borzoi
    wren "I'm wren!!"
    show gs_dog
    ines "wowie."

    return