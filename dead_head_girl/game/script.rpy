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
    callback=functools.partial(store.voice, character="default")
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
    kind=strange,
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
    color="#097969", #cadmium green
    font="fonts/SpaceMono-Regular.ttf", 
    what_font="fonts/SpaceMono-Regular.ttf"
    )

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

define cow1 = Character(name="Coworker 1", kind=strange)
define cow2 = Character(name="Coworker 2", kind=strange)

#declare ambience audio channel
define ambience = renpy.music.register_channel("ambience")

#define music file locations
define audio.house_music    = "audio/music/Insurrection Bimbo - traverse mes mains, mes bras, mon ventre.mp3"
define audio.garden_amb     = "audio/music/garden_bg_music.opus"
define audio.garden_music   = "audio/music/Rrrrrose Azerty - Feverish Soundtrack.ogg"
define audio.research_music = "audio/music/johnny_ripper - gare du nord.mp3"

#declare love interest objects
default wren_obj = store.MC(wren)
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
