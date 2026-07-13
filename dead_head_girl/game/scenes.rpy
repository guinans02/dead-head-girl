## Content Warning
label before_main_menu:
    python:
        if persistent.show_content_warning == True:
            renpy.call("content_warning")
    return

## The game starts here.
label start:
    stop music
    call debug
    call day1
    call day2
    call end_demo
    return

label debug:
    call qte_scene
    return

label content_warning:
    nvl_narrator "{size=+20}{b}!! CONTENT WARNING !!"
    nvl_narrator """
        This game contains themes and depictions of:\n\n
        - Harrasment;\n
        - Bigotry (Homophobia and Transphobia);\n
        - Sexual Assault and Rape;\n
        - Murder and Assault;\n
        - Suicide;\n
        - Self Harm;\n
        - Terminal Disease (in the form of the fictional Hanahaki Disease.)\n\n
    As well as other NSFW (and potentially offensive) topics.\n
    This game is unsuitable for minors. Please proceed with caution.\n\n
    Take care of yourself. This game has no happy endings.
    """
    nvl clear
    menu:
        "Proceed?"

        "Yes.":
            scene
            nvl clear
            return
        "No.":
            $renpy.quit()
    $renpy.quit()

label end_demo:
    scene bg_thevoid
    "End of Demo."
    return
