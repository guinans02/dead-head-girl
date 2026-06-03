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
    jump val_scenes
    jump end_demo
    return

label val_scenes:

    #Intro scene, Wren at home
    scene house
    show borzoi at max_y, center#get more silly with this i think
    
    # python:
    #     for i in range(1, 10):
    #         renpy.show("borzoi", atl=chromatic(i))

    #no name, mirror. chromatic abberation? blur?
    "It's okay."
    "It's just odd that it happened twice."
    show borzoi at max_y, center
    hide borzoi

    "*wren steps outside into-*"

    show whitney at left, max_y
    show borzoi at max_y, mv(offscreenleft, right, 1.0)
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

    #out in public
    show bg_thevoid
    show borzoi at max_y
    phone "{sc}-bzzzzzzz-{/sc}"
    phone "Reminder: Volunteer work."
    wren "{i}Why did they HAVE to assign me to the garden? There really wasn't anything else there?{/i}"
    hide borzoi

    #Garden Scene
    show garden
    "At the garden..."
    show borzoi at left, max_y
    "She goes to the garden and no one is there. She feels numb/cold looking at all the wilting flowers."
    wren "{i}Someone else should be here by now.{/i}"

    "She starts playing with a flower bud, eventually crushing it."
    wren "{i}Wow.{/i}"
    "She reaches out and-"
    show gs_dog at mv(offscreenright, right, 0.25), max_y #ines jumpscare
    strange "{b}{sc}WHAT ARE YOU DOING ??????{/sc}{/b}"
    wren "Nothing."
    strange "Oh my god, seriously? That wasn't even one that needed pruning?? Get out!!"
    wren "I'm here to volunteer though…"
    #ines is introduced ?
    ines "Oh. OH! Omg ur the new volunteer they assigned me hey thnxxxx"
    return

label end_demo:
    scene bg_thevoid
    "End of Demo."
    return
