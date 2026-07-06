#run this python code on startup
init python:
    import os, random, functools
    #class for recording the individual data for each character

    # Change CWD to the project's game directory
    os.chdir(renpy.config.gamedir)

    #paraphrased from Bored Chris on youtube
    def voice(event, character="default", **kwargs):
        i = 0
        voice_path="audio/voices/" + character + "/"
        #make a list of the files in the voicepath directory that we're going to use
        #inconsistent because apparently python and renpy CWDs aren't consistent??
        voices = [voice_path + fname for fname in os.listdir(voice_path)]

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

#Declare colors
define wren_color  = "#ffffff" #white
define kat_color   = "#d161a2" #light magenta
define ines_color  = "#fd9855" #light orange
define comp_color  = "#097969" #cadmium green

# Declare characters used by this game.
define strange = Character(
    name="Stranger",
    callback=functools.partial(store.voice, character="message")
    )
define wren = Character(
    name="Wren", 
    color=wren_color, #white
    callback=functools.partial(store.voice, character="wren")
    )
define ines = Character(
    name="Ines", 
    color=ines_color, #light orange
    font="SofiaSans-VariableFont_wght.ttf",
    what_font="SofiaSans-VariableFont_wght.ttf",
    callback=functools.partial(store.voice, character="ines")
    #kind=strange
    )
define kat = Character(
    name="Katriel", 
    color=kat_color, #light magenta
    callback=functools.partial(store.voice, character="kat")
    )
define mom = Character(
    name="Mom", 
    font="fonts/EBGaramond-VariableFont_wght.ttf", 
    what_font="fonts/EBGaramond-VariableFont_wght.ttf",
    kind=strange,
    callback=functools.partial(store.voice, character="mom")
    )
define phone = Character(
    name="Phone", 
    color=comp_color, #cadmium green
    font="fonts/SpaceMono-Regular.ttf", 
    what_font="fonts/SpaceMono-Regular.ttf"
    )

define user1 = Character(
    name="user1", 
    color=comp_color, #cadmium green
    font="fonts/SpaceMono-Regular.ttf", 
    what_font="fonts/SpaceMono-Regular.ttf",
    text_cps=renpy.random.randint(50, 60)
    )

define user2 = Character(
    name="user2", 
    color=comp_color, #cadmium green
    font="fonts/SpaceMono-Regular.ttf", 
    what_font="fonts/SpaceMono-Regular.ttf",
    text_cps=renpy.random.randint(30, 40)
    )

define com = Character(
    name="Computer", 
    color=comp_color, #cadmium green
    font="fonts/SpaceMono-Regular.ttf", 
    what_font="fonts/SpaceMono-Regular.ttf",
    callback=functools.partial(store.voice, character="computer")

    #text_cps=0 #computer is always instant
    )

define phone_wren = Character(
    kind=nvl,
    color="#ffffff", #white
    callback=functools.partial(store.voice, character="computer") #change?
    )
define phone_kat = Character(
    kind=nvl,
    color=kat_color, #light magenta
    callback=functools.partial(store.voice, character="computer")
    )

define cow1 = Character(name="Coworker 1", kind=strange)
define cow2 = Character(name="Coworker 2", kind=strange)

#declare ambience audio channel
define ambience = renpy.music.register_channel("ambience")

#define music file locations
define audio.house_music    = "audio/music/Insurrection Bimbo - traverse mes mains, mes bras, mon ventre.mp3"
define audio.garden_amb     = "audio/music/garden_bg_music.opus"
define audio.garden_music   = "audio/music/Rrrrrose Azerty - Feverish Soundtrack.ogg"
define audio.research_music = "audio/music/johnny_ripper - gare du nord.mp3"
define audio.wren_selfcare  = "audio/music/CXR ATK - Tenfold.mp3"

define audio.zipper         = "audio/zipper.opus"

#declare love interest objects
default wren_obj = store.MC(wren)
default ines_obj = store.MC(ines)
default kat_obj = store.MC(kat)

## declare character image tags and attributes

## wren
image wren pose1 angry              = "images/wren_fgs/wren_pose1_angry.png"
image wren pose1 bashful            = "images/wren_fgs/wren_pose1_bashful.png"
image wren pose1 cry                = "images/wren_fgs/wren_pose1_cry.png"
image wren pose1 embarrased one     = "images/wren_fgs/wren_pose1_embarrased.png"
image wren pose1 embarrased two     = "images/wren_fgs/wren_pose1_embarrased_two.png"
image wren pose1 eyesclosed         = "images/wren_fgs/wren_pose1_eyesclosed.png"
image wren pose1 neutralblush       = "images/wren_fgs/wren_pose1_neutralblush.png"
image wren pose1 neutralsad         = "images/wren_fgs/wren_pose1_neutralsad.png"
image wren pose1 pain               = "images/wren_fgs/wren_pose1_pain.png"
image wren pose1 pensive            = "images/wren_fgs/wren_pose1_pensive.png"
image wren pose1 smile              = "images/wren_fgs/wren_pose1_smile.png"
image wren pose1 woah               = "images/wren_fgs/wren_pose1_woah.png"
image wren pose1 worried one        = "images/wren_fgs/wren_pose1_worried.png"
image wren pose1 worried two        = "images/wren_fgs/wren_pose1_worried_two.png"

## ines
image ines blush two                = "images/ines_fgs/ines_blush_2.png"
image ines blush three              = "images/ines_fgs/ines_blush_3.png"
image ines blush one                = "images/ines_fgs/ines_blush.png"
image ines fanatic one              = "images/ines_fgs/ines_fanatic.png"
image ines laugh two                = "images/ines_fgs/ines_laugh_2.png"
image ines laugh one                = "images/ines_fgs/ines_laugh.png"
image ines pose_two woah            = "images/ines_fgs/ines_pose2_:0.png"
image ines pose_two fan             = "images/ines_fgs/ines_pose2_fanatic.png"
image ines pose_two frustrated      = "images/ines_fgs/ines_pose2_frustrated.png"
image ines pose_two grimace         = "images/ines_fgs/ines_pose2_grimace.png"
image ines pose_two laugh           = "images/ines_fgs/ines_pose2_laugh.png"
image ines pose_two neutralsad      = "images/ines_fgs/ines_pose2_neutralsad.png"
image ines pose_two pain two        = "images/ines_fgs/ines_pose2_pain2.png"
image ines pose_two pain one        = "images/ines_fgs/ines_pose2_pain.png"
image ines pose_two pensive two     = "images/ines_fgs/ines_pose2_pensive2.png"
image ines pose_two pensive one     = "images/ines_fgs/ines_pose2_pensive.png"
image ines pose_two                 = "images/ines_fgs/ines_pose2.png"
image ines pose_two sad             = "images/ines_fgs/ines_pose2_sad.png"
image ines pose_two shock           = "images/ines_fgs/ines_pose2_shock.png"
image ines pose_two smile           = "images/ines_fgs/ines_pose2_smile.png"
image ines pose_two worried         = "images/ines_fgs/ines_pose2_worried.png"
image ines mlem                     = "images/ines_fgs/ines_:P.png"
image ines smile two                = "images/ines_fgs/ines_smile_2.png"
image ines smile one                = "images/ines_fgs/ines_smile.png"
image ines worried                  = "images/ines_fgs/ines_worried.png"

## kat
image kat pose1 eyesclosed          = 'images/kat_fgs/kat pose1 eyesclosed.png'
image kat pose1 neutralsad          = 'images/kat_fgs/kat pose1 neutralsad.png'
image kat pose1 regret              = 'images/kat_fgs/kat pose1 regret.png'
image kat pose1 relieved            = 'images/kat_fgs/kat pose1 relieved.png'
image kat pose1 sad                 = 'images/kat_fgs/kat pose1 sad.png'
image kat pose2 eyesclosed blush    = 'images/kat_fgs/kat pose2 eyeclosed blush.png'
image kat pose2 happy               = 'images/kat_fgs/kat pose2 happy.png'
image kat pose2 neutral             = 'images/kat_fgs/kat pose2 neutral.png'
image kat pose2 neutralsad          = 'images/kat_fgs/kat pose2 neutralsad.png'
image kat pose2 shock               = 'images/kat_fgs/kat pose2 shock.png'
image kat pose2 smile blush         = 'images/kat_fgs/kat pose2 smile blush.png'
image kat pose2 worried two         = 'images/kat_fgs/kat pose2 worried 2.png'
image kat pose2 worried three       = 'images/kat_fgs/kat pose2 worried 3.png'
image kat pose2 worried one         = 'images/kat_fgs/kat pose2 worried.png'
image kat pose2 worried sad         = 'images/kat_fgs/kat pose2 worriedsad.png'


#transform for all foreground images to make them the same height
transform max_y:
    ysize(600)
    fit "contain"

#animation for moving sprites around the screen
#default pos0 current position?
transform mv(pos0, pos1, spd=1.0):
    pos0
    linear spd pos1

# shooting minigame QTE logic
label shoot:
    init python:
        def hide_target():
            global target_visible
            target_visible = False
            renpy.restart_interaction()

        def hit_target():
            global score, target_visible
            #replace with the sound of wren taking a ragged breath
            #renpy.play("audio/Gun1.ogg")
            score += 1
            target_visible = False
            renpy.restart_interaction()
    $ score = 0
    $ time_left = 10
    "Ready to shoot? Hit as many targets as you can!"
    $ renpy.pause(1.0)
    call screen target_shooter
    
    return
