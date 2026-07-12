label day2:
    call garden_day2
    call kat_texts_wren
    call wren_visits_kat
    return

## DAY 2 SCENES

label garden_day2:
    scene garden
    play ambience garden_amb
    play music garden_bg_music

    show wren pose1 pain at max_y, mv(offscreenleft, left, 0.5)
    #  Wren walking into ines's garden. 

    wren "Where is she?? "
    wren "I know I'm late, I'm sorry. "

    show wren at mv(left, center, 0.5), max_y
    wren "Hello? "
    show wren pose1 pensive
    wren "Shit. "
    show wren at mv(center, right, 0.5), max_y
    wren "… "
    # (make her move around the screen a little, like she's walking in thought) 

    show wren pose1 woah at mv(right, left, 0.5), max_y
    show ines mlem at mv(offscreenright, right, 0.5), max_y
    ines "Say cheese! "
    wren "Cheese…? "
    # camera snap effect
    # camera flash
    show wren pose1 angry at max_y
    wren "Ack! Don't do that! "
    # cg of a Polaroid of Wren. It hasnt developed yet, so it's black.

    #back to Wren Ines in garden
    show ines smile one at max_y, right
    ines "You look so pretty. Ephemeral, almost, with the blurry effect. "
    show wren pose1 bashful at max_y
    wren "Do you mean ethereal? "
    show ines pose_two laugh at max_y
    ines "No, ephemeral."
    show wren pose1 angry
    wren "Do you know what that word means? "
    show ines blush one
    ines "You're being rude. "
    show wren pose1 smile
    wren "so, now we're even. "
    # cg wren's poloraid. Its blurred and grainy
    show wren pose1 pensive
    wren "I mean, it's a photo. "
    show ines pose_two frustrated
    ines "Hmmph."
    show wren pose1 woah
    wren "you're sweet for showing it to me. "
    show ines pose_two pensive one
    ines "I don't really like photography all that much. Camera photos look too real. "
    show ines pose_two fan
    ines "Drawings, though, capture the feeling of a living thing. I get to remember you how I see you for however long I keep the drawing."
    show ines pose_two smile
    ines "But polaroids are still pretty cool. I like how grainy they are. It helps to hide the imperfections. "
    show wren pose1 worried one
    wren "You intend to make it look that blurry? "
    show ines mlem
    ines "Well, no. But I like the effect. "
    #"A beat of silence." 
    show wren pose1 eyesclosed
    ""
    show wren pose1 pensive
    wren "What exactly am I doing in the garden today? "
    show ines laugh one
    ines "Oh, have you forgotten your promise already? "
    show wren pose1 woah
    wren "I. "
    show wren pose1 embarrased two
    wren "I was scared you were messing with me. "
    show ines pose_two shock
    ines "I'm not some high school mean girl! "
    show ines pose_two fan
    ines "Wren, you have this sort of worldly air to you. Like you know something. I want to find out what it is. "
    show ines fanatic one
    ines "I must paint you. "

    #wren blushes
    show wren pose1 smile
    wren "If you really want to that bad… "
    show ines laugh two
    ines "I brought some props from home. I'm so excited! "

    # rummage sound effect
    show ines smile one
    ines "Let's see, lets see"
    show ines pose_two pensive one
    ines "I have a piece of muslin fabric for draping"
    show ines pose_two pensive two
    ines "I like doing texture work, so I also have some lace.. "
    show ines laugh one
    ines "ooh! Or what about something here, from the garden! "
    show ines laugh two
    ines "paying homage to the flowers you crushed, a mourning piece! "
    show wren pose1 worried one
    wren "{i}what. "
    show ines worried
    ines "um or actually "
    show ines fanatic one
    ines "I brought something I made for you. "
    show ines smile two
    ines "it took me a while, but I think you'd look just perfect in it. "
    ines "what do you think?? "
    show wren pose1 worried two

    #choices
    default crown = False
    menu:
        "Is that a crown of leaves?":
            # +1 Ines affection
            $ines_obj.update_score(1)
            jump crown_of_leaves
        
        "Do I have to?":
            jump do_i_have_to
    
label crown_of_leaves:
    $crown = True
    show wren pose1 pensive
    ines "Yes, I thought it would symbolize renewal."
    show ines pose_two shock
    ines "I knew you had a good eye for the arts."
    show ines pose_two laugh
    wren "{i}I guess I get how the leaves are renewal. "
    wren "{i}But I don't get those other ideas. "
    wren "{i}Who would mourn a bush? It didn't even die." 

    show wren pose1 eyesclosed
    wren "I'll just go with the crown."
    show ines pose_two fan
    show wren pose1 neutralsad
    ines "Yay! I love working with live models. "
    show ines pose_two at mv(right, center, 0.5), max_y
    # Ines moves closer to Wren "
    show wren pose1 crown
    ines "Ok. Sit down like that. Spread out your arms a little."
    show ines pose_two pensive two
    ines "Hm… look up. there we go! "
    # my inspiration is jesus on the crucifix with his crown of thorns lookin up. wowie
    # wren sprite w a green crown
    # humming music 
    show ines fanatic one
    ines "Perfect. Such a good girl. "
    #show wren pose1 neutralblush
    # pencil scratch noises. "
    ines "Hm hm hmmm."
    # pencil scratch noises "
    #show wren pose1 pain
    wren "Hey ines-"
    show ines mlem
    ines "Stay still please!! I'm capturing your lips. "
    show wren pose1 crown bloody
    wren "{i}But something is poking me…  "
    wren "{i}I can feel something dripping down my face. "
    # Wren sprite with crown and a line of blood"
    #show wren pose1 woah
    wren "Ines, take it off of me. "
    ines "..."
    #show wren pose1 cry
    wren "ines. i think i'm bleeding. "
    show ines fanatic one
    ines "Don't worry. the red stands out quite nicely on your pallor. "
    ines "Oh! you're just like a real life snow white. "
    wren "it's kinda hurting. "
    wren "like bad actually "
    ines "but I'm almost done! "
    wren "… "
    ines "sigh. "
    ines "alright. if you insist."
    # Ines gets closer to Wren. "
    show wren pose1 cry
    wren "why are you"
    ines "you are like a real life fairy tale. "
    ines "my princess. "
    show wren pose1 pain
    wren "you didn't just taste my blood. "
    ines "an artist must know her materials. "
    ines "you really do have such nice color. "
    show wren pose1 pensive
    wren "umh"
    ines "my thumb print, in your heart's blood on the canvas. "
    ines "now you'll always be with me. "

    jump post_garden_day2

label do_i_have_to:
    show wren pose1 pain
    wren "Honestly-"
    wren "I don't really like any of these?"
    #ines very sad"
    ines "If you have something better to do, you can leave."
    wren "I might get going soon."
    ines "Another promise… broken…."
    wren "Umh"
    wren "(thinking) All of these are bad but…"
    wren "Let's do the piece here, mourning the flower ines "
    ines "Oh, I'm so happy!"
    wren "{size=10}I'm glad. "
    ines "Here, sit here while I prime my canvas and think about the pose."
    # a moment of silence"
    wren "Are you upset about me crushing that flower?"
    ines "Am I upset?"
    ines "No. "
    wren "Then why are you memorializing it?"
    ines "If you've killed something, it's yours now. "
    ines "I'm taking my flower back. "
    wren "{i}Who are you? Who raised you?"
    wren "It's not that important. "
    ines "I dreamed about it. "
    wren "So now it's important? I have all sorts of crazy dreams, but I never pay any attention to them. "
    ines "{b}Why not?{/b} They're portals to the soul. "
    wren "Is a recurring nightmare of me running in a maze with a thicket of thorns saying something about my soul?"
    ines "Oh? And how does that end? "
    wren "I guess I get crushed by the thorns. It's weird."
    ines "And then?"
    wren "I die. The thorns go into my eyes. Then I wake up."
    ines "What do you have against thorns? They're so lovely. "
    wren " It's just a nightmare. "
    ines "~"
    ines "I have the perfect idea. "
    # ines moves closer to wren. "
    ines "Lie down like this?"
    ines "There we go. "
    # music change : ines humming a melancholic tune. Painting/sketch noises until scene end. "
    #https://en.wikipedia.org/wiki/Ophelia_%28Heyser%29#/media/File:Friedrich_Wilhelm_Theodor_Heyser_-_Ophelia.jpg (maybe like this owo. the dead flower goes on wren's eye."
    # implement if have time. Okay if no. "
    wren "(thinking) Is this what art models usually do? "
    wren "(internal) Well, anything flies as long as I'm not back home with Mother. "
    wren "(internal )It helps that she's a cute girl. "
    wren "(internal) Wren, don't think like that. "
    ines "Lovely. "
    ines "I can't wait to go deeper into your psyche."
    wren "I'm just your art model. "
    wren "NOTHING more. "
    #ines smile
    ines "And nothing less."
    ines "There. "
    return


label post_garden_day2:
    play music garden_bg_music
    # music back to default garden
    show wren pose1 neutralsad
    ines "Great, I have everything I need. Thank you so much!"
    show ines at mv(center, right, 1.0)

    python:
        if crown == True:
            renpy.jump("pleasure")
        else:
            renpy.jump("welcome")
    label pleasure:
    show wren pose1 smile
    wren "Of course. It's a pleasure. "
    jump next_week
    label welcome:
    show wren pose1 neutralblush
    wren "Sure. You're welcome. "
    label next_week:
    ines "I'll see you next week? "
    wren "Okay!"
    ines "Get home safe! "
    show ines at mv(right, offscreenright, 0.5)
    return

label kat_texts_wren:
    # Wren walks to outside. "
    show wren at mv(left, offscreenleft, 0.5)
    stop music
    stop ambience
    scene houses
    show wren pose1 neutralsad at mv(offscreenright, center, 0.75), max_y

    wren "{i}That was weird. "
    wren "{i}I mean. "
    wren "{i}That's mean of me. She's a perfectly nice girl. "

    show wren pose1 pensive
    wren "{i}Can I really ignore those dead art subjects though?"
    # phone notification sound"
    show wren pose1 neutralsad
    wren "Umh?"
    # phone screen bg"
    phone_wren "Is everything ok? "
    phone_wren "I'm sorry. Can we talk? "
    phone_wren "KAT KAT KAT KAT KAT "
    phone_wren "I saw you walking outside. You're not dead or sick. "
    phone_wren "Please, Katriel. you're my best friend. "
    phone_wren "I'll leave you alone if you want?"
    phone "You have [1] new message(s)."
    phone_kat  "Swedish researchers have discovered that salmon dosed with benzoylecgonine, a cocaine byproduct, swim almost twice as far as the control group."

    wren "Seriously, Kat? That's your first message to me in three years?"
    phone_wren "And this is relevant because…? "
    phone_wren "I have your workbag. Come over when you're first available. "
    phone_wren "Just leave it on my doorstop. "
    #pull choice from day one (check kat score?)"
    python:
        if kat_obj.get_score() > 0:
            renpy.jump("lesbians")
        else:
            renpy.jump("family")
    label lesbians:
        phone_wren "No. Don't you want to continue our conversation about LESBIANs?"
        jump go_now
    label family:
        phone_wren "No. Don't you want to continue our conversation about your family?"
    label go_now:
    phone_wren "I'll… just go now. "
    return

label wren_visits_kat:
    # wren in front of kat's house. "
    # DIALOGUE"
    # knocking sound"
    show wren pose1 neutralsad at center, max_y
    wren "Hello?"
    wren "Hellooooo?"
    wren "Of course Kat still doesn't lock the front door. "
    wren "Katriel? I'm here. "
    wren "Kaaat. Since you're not here, I'm going up to your room! "
    wren "KAT!"
    show wren pose1 pain
    # coughing sounds"
    wren "I'm he-"
    show wren pose1 cry at max_y, mv(center, left, 1.0)
    # more coughing sounds. "
    # K comes on screen. "
    show kat pose2 happy at mv(offscreenright, right, 1.0), max_y
    kat "Hey Wren."
    show kat pose2 shock
    kat "Oh, that's some blood. "
    kat "Hey, let's come up to my room. "
    show kat at mv(right, offscreenright, 1.0)
    show wren at mv(left, offscreenright, 0.5)
    scene kat_bedroom
    show kat pose1 neutralsad at mv(offscreenleft, right, 0.5), max_y
    show wren pose1 neutralsad at mv(offscreenleft, left, 1.0), max_y
    # wren and kat in kat's room. It's pink and girlish. "
    show wren pose1 pain
    wren "It smells weird in here. "
    show kat pose2 eyesclosed blush
    kat "I'm not gonna take that from someone with blood in her nose. "
    show kat pose2 neutral
    kat "Let me clean you up. "
    show wren pose1 neutralsad
    wren "Okay. "
    show kat pose2 worried one
    kat "What's with that cough?"
    show wren pose1 embarrased one
    wren "I… don't really know, actually. "
    show kat pose2 worried two
    kat "How long have you had it?"
    show wren pose1 embarrased two
    wren "Um, a few weeks now?"
    show kat pose2 worried three
    kat "You should really go to a hospital. "
    show wren pose1 neutralsad
    wren "With what money, exactly?"
    show kat pose1 sad
    kat "Hm. Well. "
    show kat pose1 relieved
    kat "Want me to take a look? You know, aspiring toxicologist right here… "
    wren "But-"
    show kat pose2 happy
    kat "You'll be a nice case study. "
    show kat pose2 smile blush
    kat "Indulge me?"
    show wren pose1 woah
    wren ". . ."
    show kat pose2 smile blush
    kat "Just a joke. so? "
    show wren pose1 bashful
    wren "Sure. Can't hurt. "
    # Kat moves closer"
    # heartbeat sound"
    show kat pose2 smile blush at mv(right, center, 0.5), max_y
    show wren pose1 bashful
    wren "You smell like it too. "
    show kat pose1 sad
    kat "Jesus, it's only the smell of the lab. "
    show wren pose1 worried two
    wren "It's not bad just strong. "
    show kat pose2 neutral
    kat "Then, say Aah. "
    show wren pose1 pensive
    wren "What are you doing?"
    show kat pose1 relieved
    kat "Open your mouth. "
    show wren pose1 woah
    wren "Ahh? "
    show kat pose2 smile blush
    kat "Good girl."
    show kat pose2 worried sad
    kat "Well. Everything looks normal? "
    show kat pose1 relieved
    kat "A bit inflamed, though. Have you been eating chips 24/7 or something? "
    show wren pose1 pensive
    wren "No? "
    show wren pose1 neutralblush
    wren "…  "
    show kat pose2 eyesclosed blush
    kat "you-"
    wren "you-"
    show wren pose1 smile
    wren "You smell nice "
    show kat pose2 shock
    kat "Did you do this?"
    show wren pose1 embarrased one
    wren "What?"
    kat "What?"
    show wren pose1 embarrased two
    wren "I said you smell nice."
    show kat pose2 smile blush
    kat "Thanks."
    # Kat sprite move back "
    show kat pose1 relieved
    kat "Okay well, since you're here can you help me study? "
    show wren pose1 happy
    wren "Ah, I get it now. Got too bored studying all by yourself. "
    #kat blushes
    show kat pose2 smile blush
    kat "I do actually have your bag!"
    show wren pose1 bashful
    wren "Could have just left it on my doorstep. "
    kat "It's not a crime to want to see you, Wren. "
    wren "{i}After years of avoiding me with no explanation, it is. "
    wren "{i}Ah, I don't care, I just want to talk with you. "
    wren "You win. Let's study. "
    kat "Let's sit on my bed. "
    wren "… "
    # maybe fade to black? To show time passing or # Wren falling asleep the eeper "
    # timer sound. "
    kat "There, just finished up with two hours. "
    kat "Break time. "
    wren "Wuh? "
    kat "You're so tired all the time. "
    wren "I can't keep awake just watching you study. "
    kat "Bleh. "
    wren "Your room has changed so much…."
    kat "It's essentially the same. "
    wren "It's completely different. "
    kat "It's een at least 5 years since you were last here, so you're likely remembering it wrong."
    wren "No…"
    wren "I remember you had a… what was it, a model car collection…? You polished them over and over again, all the paint was stripping off. "
    kat "Did I? "
    wren "I like your room now too, though. It's pretty. "
    kat "Of course."
    wren "Man, whats the point of all this studying? "


    #(W's very sleepy. Kat's still flipping through a textbook)
    wren "(internal?) Y'know Kat, it feels like you've changed so much, but at the same time you feel the same. But the old you and the current you… they're both beyond what I could be. Everything you do. I just wonder if you know what you could be. What you want to do."
    wren "why did you go back to toxicology? "
    kat "it's just the best path forward for me. "
    wren "it didn't seem like that when we last spoke."
    kat "gosh, just lay off me already, will you? people change."
    wren "i know you though. "
    wren "is this really what you want for yourself? "
    kat "are you fucking serious? "
    kat "of course not. i hate talking to those bitches with their heads up their asses and i hate the stagnance in that fuckass company with their bullshit about reinventing the wheel. "
    kat "but i've tried my hardest for too long to be left languishing with the rest of the unwashed masses. even if it means devoting myself to something i find completely meaningless or presenting myself as the perfect person or ignoring that gnawing gap inside or that I can never have what I really want-"
    #smtg like how she's abt to blurt out she realises internally that she highkey a lesbian but more subtle]"
    kat "it doesn't matter. "
    kat "i have to succeed. i'll be the best in my field. the first person everyone rushes to talk to when i walk into a room. "
    menu:

        "you're the most successful person I know":
            jump most_successful_person

        "You're just human too.":
            jump just_human

label most_successful_person:
    kat "thanks. "
    kat "still. i always have room to grow. i always have more to improve at. "
    #idk smtg abt a spider respinning its web constantly lol until it's left the space to thrive or someone kills it "
    jump post_kat_day2

label just_human:
    wren "Oh."
    wren "You're just human too. "
    kat "don't put me down on your level. "
    kat "you have no goals, no aspirations, no presence. hearing that from you—god, that's such a low bar. few years no see, one word from me and you're back following me around like a sad little dog with nowhere to go and no one to play with."
    wren "you're talking? you're no one special. you try to sound intelligent but you're really just a pretentious soulless corporate suck up. there's millions of girls like you out there. "
    kat "at least i have self control. I wouldn't have let some random feelings-"
    kat "-i mean, a momentary lapse of judgement-"
    kat "-ruin everything i've built. "


label post_kat_day2:
    ## added july 10th
    wren "It's sad. Why can't you admit that? "
    kat "I'm sad? What, projecting much? "
    wren "Kat! "
    kat "Don't say my name like that. "
    wren "Fine then, bitch. "
    kat "You're a bitch. "
    kat "Worse, actually , you're a stray dog. "
    wren "Do you try to flirt with stray dogs often? "
    # smack sound"
    kat "Does that feel like flirting to you? "
    # Wren sprite gets closer to Kat sprite. "
    # red screen tint/ chromatic abberation from wren"
    wren "You want me to be a stray dog? "
    kat "ackth uh"
    wren "I didn't hear you. "
    wren "What was that? "
    wren "Don't make me squeeze harder. "
    kat "whimper"
    wren "Hey, no, I'm sorry. "
    kat "gasp"
    kat "koff koff"
    kat "Wren, don't cry. "
    kat "Stop crying, Wren. "
    kat "We both know I pissed you off on purpose okay? You know me better than to blame yourself. "
    kat "Dad hasn't been home so it's just been…  me and Taylor. "
    wren "Your schizo aunt is still around? "
    kat "God willing and the creek don't rise. "
    kat "So. "
    kat "I really, really need you back in my life right now Wren. "
    wren "You could literally just fucking ask next time? "

    kat "Where's the fun in that? "
    kat "Okay, now get out, I need to hide the marks you just gave me. "
    wren "Didn't you need me in your life? "
    kat "Yes, I do actually. But I need to change clothes. "
    wren "Ha. "
    kat "There, I kissed your booboos all better. "
    kat "Now shoo. "
    # Wren walks out. "
    # in front of wren's house. "
    wren "I'm the only one who really knows her. "
    wren "I knew it meant something. "
    wren "I knew it! I knew it! I knew it!! "
    wren "I think I need a nap . "
    # bg change to Wren house living room "
    mom "Wren. "
    wren "Yes, mother?"
    mom "Your room is just filthy. I hate repeating myself; you're not a child anymore. "
    wren "What are you—Of course, mother. My apologies. "
    mom "The flowers, Wren?"
    wren "{i}The ones with all the blood on them? "
    mom "I hope you aren't seeing anyone. Please do remember that you are living here on my dime. "
    wren "Right. "
    wren "May I go to my room now? Please? "
    mom "Ah… "
    # (depending on who you have more affection with) "
    # more Kat points mom "That girl next door, what's her name… Katherine? "
    # more Ines points mom "That girl with the tree club that you joined, the one with the sweater? "
    # equal points  mom "You've been spending a lot of time outdoors, with those people you've met- the girls with the clothes? "
    mom "No matter. "
    mom "Don't let some girl—I mean, anyone, distract you from what you should be doing. "
    mom "These youthful affairs never last long, Wren. "
    # Mother leaves"
    wren "What the fuck is she talking about? "
    # screen to black"
    wren "Hnn"
    wren "Can't believe it's nearly the end of the summer. "
    wren "I still don't have nearly enough money to figure out my fucking cough. "
    wren "This sucks. I don't know a thing about medicine. Or these disgusting bloody flowers. "
    # phone notification sound"
    wren "It couldn't hurt to ask Kat or Ines? "
    # this is fucking lazy but I can't think of another way to transition it."

    # Wren move to garden "
    # ines is there"
    ines "Hey Wren! "
    wren "Hi, Ines. "
    wren "So what are we going to do today? "
    ines "The same as always??? "
    wren "Oh. I guess I didn't know you could paint in the rain. "
    ines "IT'S GONNA RAIN?? "
    ines "Aw, boo. "
    ines "Well, there goes another masterpiece. "
    wren "Story of your life. "
    ines "Let's go to a cafe and get something warm! "
    # change to cafe bg "
    ines "and you just have to try the miso coffee they have here, it's mouthwatering. "
    ines "Oooh! I just remembered I have my pencils on me! Hand me that napkin, please? "
    wren "Hey, can I ask you something. "
    ines "Certainly <3 "
    wren "Is it possible to identify a flower just from the petal? "
    ines "Depends on the freshness. And the flower. Why? "
    wren "Well. Do you know what this one is? "
    ines "Oh hm. "

    # depends on the route ur on: "
    # high Ines ines "Oh, that looks like a lilac! They're my favorite flower!! Did you know they're edible? You can't eat too much though, or they'll make you throw up. "
    # high katriel ines "I bet that's an Amaryllis? They're commonly confused for lilies cause they look really similar. But they are superrrrr poisonous. "
    # equal ines "Hmm, it's a little hard to tell. If I had to guess, maybe some kind of Iberis? A candytuft flower."

    python:
        if ines_obj.get_score() > kat_obj.get_score():
            #ines' affection score is higher than kat's
            renpy.jump("lilac")
        
        elif ines_obj.get_score() < kat_obj.get_score():
            #kat's affection score is higher than ines'
            renpy.jump("amaryllis")
        
        else:
            #both scores are equal
            renpy.jump("iberis")

label iberis:
    ines "Hmm, it's a little hard to tell. If I had to guess, maybe some kind of Iberis? A candytuft flower."
    jump post_flower_day2

label lilac:
    ines "Oh, that looks like a lilac! They're my favorite flower!! Did you know they're edible? You can't eat too much though, or they'll make you throw up. "
    jump post_flower_day2

label amaryllis:
    ines "I bet that's an Amaryllis? They're commonly confused for lilies cause they look really similar. But they are superrrrr poisonous. "
    jump post_flower_day2
    
label post_flower_day2:
    ines "Where'd you get these? "
    wren "I found them??"
    wren "In my room after I woke up one day??! "
    ines "That's fun! "
    ines "Totally reminds me of this urban legend I saw in a video. "
    ines "It was called like, the Lover's Bloom. "
    ines "You fall SO DEEPLY in love with someone that a flower blooms inside of you."
    ines "And then, when the time is right and it hits midnight, you spit up the bouquet and give it to them. "
    ines "Ahh! It's so romantic, can you imagine a better way to show your dedication to another!"
    ines " Such a shame that it's not real. "
    ines "I wish I could experience it, it sounds so lovely and fun. "
    wren "What the fuck?"
    ines "Huh? "
    wren "That's really fucked up. Why would you ever want that to happen to you?? "
    ines "What's wrong with imagining? "
    wren "Because it's a dumb-fuck way to waste your time. Imagining suffocating in itchy petals? "
    wren "“ oh em gee I luuuuv pretty toxins seeping into my bloodstream all day teehee” "
    wren "“ La la yaaaay I'm a complete and total idiot now I throw my life at your feet save me LOVE!!! “"
    wren "That's not how it works. "
    wren "And if they don't love you back? What then, huh? "
    ines "I didn't really read that far. "
    wren "Of course you didn't. "
    ines "What's with you today? you're being so –"
    wren "Shut up. "
    ines "I'm literally just trying to make conversation! What's unreasonable about that? "
    wren "Oh, I don't know. "
    wren "Maybe I'm tired of being lectured about what is or isn't pretty by a privileged, spoiled brat? "
    wren "You dedicate your life to to this shit and it's still complete, overwrought, garbage! "
    ines "No it's not! Take that back! "
    wren "Then why does no one show up to your art shows, huh? "
    ines "I.. *sniff* told you that in confidence. "
    wren "Grow up."
    ines "I don't—"
    ines "That was really mean."
    wren "What, want me to apologize for the big, scawy, reality of who you are? "
    ines "Fine then. No one respects me. Not the other artists, not the teachers at school, and not even my family. "
    ines "I thought you would understand. Clearly not."
    # Ines runs away"
    # Wren goes out side. "
    wren "I wished I smoked so I could have a cigarette right now. "
    # phone notification sound. "
    wren "FUCK. WORK. "
    # Wren in her office"
    wren "{i}Sick of this shit. "
    wren "{i}It's not my fault. She started it."
    wren "{i}Fuck fuck fuck. Fu-"
    cow1 "Heyyy Mack can you please verify and order this for the new client. Here's the card! "
    wren "I don't handle transactions? "
    cow1 "Then who does? "
    wren "I don't know."
    cow1 "Well, Gina told me it was you, so. Here. "
    wren "I'm busy, wait. "
    cow1 "K thx bye ! "
    # coworker leaves"
    wren "… "
    wren "What ever. "
    # type sounds "
    comp "PURCHASE. COMPLETE. "

    wren "sigh. "
    # backgroun blurs. "
    wren "{I}I'm sorry for bieng a dick earlier. "
    wren "{I}No. "
    wren "{I}I didn't mean what I said, it's just that you. "
    # background unblurs coworker Sprite comes in. "
    cow1 "You think I wouldn't notice? "
    wren "What? "
    cow1 "Did you seriously order that on the company card?"
    wren "I'm sorry?"
    cow1 "Cigarettes, you daft bint! I'm supposed to explain why 5 cigarette packs showed up to the lab INSTEAD OF THE 5 CENTRIFUGES??"
    # katriel sprite comes in"
    cow1 "Hey uh… Kathy, you file the paperwork for this. I'm not dealing with this right now. I got a meeting. "
    kat "I'm not-"
    cow1 "Well it's either you or Danny so. "
    kat "Hand it here. "
    # katriel sprite and coworker sprite leave"
    # music shift. "
    # background blur"
    # Wren chromatic "
    # kat sprite "
    kat "What the fuck was that about? My manager screamed herself hoarse. Could you be a bigger fuck-up if you tried? "
    # outside of work bg "
    wren "I'm. oh. "
    kat "Wren. "
    wren "Hey Kat. "
    kat "Lets just go. "
    # they move to outside wren's house "
    kat "Looks like we're here. "
    kat "Time for me to leave. "
    kat "Wren? "
    wren "Bye Kat. "
    kat "You high? "
    wren "What? "
    kat "Fucking answer my question! "
    wren "No, I'm not high "
    kat "Then. What. Could. Possibly. Be the Reason. For that disaster. "
    wren "Sorry, for being so distracted? "
    kat "Dude. "
    wren "My.. mom's sick. "
    kat "Oh. "
    wren "Yeah. "
    kat "I'm really sorry. "
    wren "Thanks. "
    kat "Is it cancer? "
    wren "No, the doctors don't know what it is. "
    wren "She's really tired, her throat is sore, and she's fatigued. "
    kat "Fuck, that could be anything."
    wren "And, she's coughing up these petals. "
    kat "Like… ? "
    wren "Like flower petals, yeah. "
    kat "Holy shit. Out her mouth? "
    wren "Covered in blood. It's been really scary for her. "
    kat "I can imagine. "
    # for the next line have it go off screen, and speaking rlly fast"
    kat "Have the doctors tested her immunoglobulin levels? Maybe it's some kinda Munchausen's? Or a weird blend of pica and a GI bleed that she's too embarrassed to talk about? I wonder if it could be something really obscure, maybe they'll even name a disease after her… "
    wren "Um, I don't really know. "
    kat "Of course not. Hm. Has she tried some immune boosting tea? "
    kat "What pain management meds is she on? "
    wren ""
    kat "Can I hug you? "
    wren "yes. "
    wren "thanks. "
    kat "Of course. "
    kat "You should have told me, I could have helped you cover! "
    kat "I wouldn't have blown up either. "
    wren "It's okay, you didn't know. "
    kat "Hey, I'm really behind on inputting my data. "
    kat "You could come over tonight? "
    kat "I'll even make up a packet of over the counter medicines to give to your mom. "
    kat "Okay? "
    wren "I'll…  think about it. "
    wren "Thanks. "
    kat "Take care of yourself. "
    # Katriel goes off screen. "
    # Wren up to her room. No convo w mom. The room is dark. "
    wren "I feel too gross to jerk off. "
    wren "I'm too tired to fall asleep. "
    wren "I haven't slept good in weeks… "
    wren "I guess I could go "
    wren "koff"
    wren "I guess I could go hang"
    wren "blegh "
    # Wren bloody sprite"
    wren "What the fuck… "
    wren "I can't I can't I CAN'T with this. "
    wren "I… "
    # phone bg"
    phone "2 NEW NOTIFICATIONS"
    wren "Would it be worth it to try? "
    # back to Wrens room. She looks exhausted. "
    wren "Ah. "

    # implement QTE 
    # if fail, go to fail end. If succeed, go to last decision
    call qte

label last_decision:
    # LAST DECISION
    wren "FUCK! "
    wren "I don't want to. "
    wren "I just need to stop being a whiny bitch "
    wren "I'd literally rather die than go out to tonight. "
    #  wheezing SFX, screen shake/ red and/ or Wren goes chromatic. Wren wheezing, screen going black. 
    wren "Ugh. Ugh! "
    wren "Go  "
    wren "now! "
    wren "okay, NOW! "
    wren "AHHH"
    # choices 

    # Fine, I pick : 
    # (Put choice here) 
    # Ines
    # Katriel
    default pick_ines = False
    default pick_kat = False
    menu:
        "Fine, I pick"

        "Ines":
            $pick_ines = True
            pass

        "Katriel":
            $pick_kat = True
            pass
        
    wren "Why do I feel so nauseous?"
    # phone typing noise. 
    wren "I have to. It's because I have to. "
    wren "Mother doesn't keep any alcohol in the house. "
    wren "Well, she'd kill me if I even tasted her wine. "
    wren "I'm wasting time. "
    wren "God. "
    #wrens phone
    nvl clear
    phone_wren "{color=wren_color}wren{/color}: hey"
    # if affection is 0 with who you picked, go to fail end. 
    # now go to either KATRIEL or INES 

    python:
        if pick_ines:
            #the player decided to confess to ines
            if ines_obj.get_score() == 0:
                #if ines doesn't like you back, bad end
                renpy.jump("fail_end")
            else:
                #otherwise, ines 'good' end
                renpy.jump("ines_end")

        elif pick_kat:
            #the player decided to confess to kat
            if kat_obj.get_score() == 0:
                #if kat doesn't like you back, bad end
                renpy.jump("fail_end")
            else:
                #otherwise, kat 'good' end
                renpy.jump("kat_end")
        else:
            #something broke with the player choosing who to confess to :(
            "ERROR"
            renpy.quit()

label fail_end:
    wren "Actually. "
    wren "I'm going to lay down. "
    # Screen goes red and shaky
    wren "{i}No one checks in on me. Everyday the same."
    # Wren chromatic wren "People are all terrible anyways. 
    # Scary music 
    # Wren wheezing 
    wren "I hope whoever cleans my body has a grand 'ol time. "
    wren "Bye Ines. "
    wren "Bye Katriel. "
    wren "Bye Mother. "
    wren "Bye, Wre-"
    wren "Okay, Wren. It's okay. "
    # Screen goes black 
    # Fly buzzing sounds. 
    # if we have time, draw wrens corpse in bed, Flowers and petals and blood and leaves around her. 
    # Maybe even where who ever had the highest affection w Wren jolts up from her desk and goes, ah, why did my chest hurt? (Feel free to cut if too stupid/ time crunch) 
    
    # END
    return

    # (Possible post credits where Ines and kat have a convo, about wren like 10 yrs later??? Cut for time) 

label kat_end:
    # KATRIEL
    phone_wren "{color=wren_color}wren{/color}: are you free right now?"
    phone_kat "maybe. "
    phone_wren "I'm coming over. "
    phone_kat "okay. "
    # Wren outside katriels house. 
    # katriel comes out. 
    kat "So."
    wren "Can we go up to your room?"
    kat "What did you want to tell me, Wren."
    wren "It's not my mom that's sick."
    kat "Duh."
    wren "I'm sick. And I keep getting sicker."
    kat "Oh my God, Wren."
    wren "And I don't know what it is, and I can't sleep and it hurts all the time."
    kat "Hey, I understand."
    wren "I didn't mean to get stuff at work wrong."
    wren "I didn't want to get you in trouble."
    wren "*snif"
    kat "Hey, it's not terminal, right?"
    kat "I'm not ready to mourn you."
    #wren sprite moves closer to kat sprite"
    wren "{i}I love you."
    kat "Wren, it'll be okay. We can figure something out!"
    wren "{sc=1}I love you."
    kat "Oh!"
    wren "Sorry."
    # if affection with kat is higher or equal to Ines, go to Kat Bad. 
    # if affection to Kat is lower than Ines, go to Kat worse. 

    # Goto Katbad or katworse. 

    #does this work?
    $if kat_obj.get_score() < ines_obj.get_score(): renpy.jump("kat_worse")

label kat_bad:
    #KatBAD-
    kat ".... "
    wren "… "
    kat "Why. "
    kat "You selfish little monster! "
    kat "Why do you have to do this now. "
    kat "You've ruined EVERYTHING. "
    # Kat starts crying, if we have a sprite for that. 
    kat "I can't believe you're still fucking with me. "
    kat "After everything I've done for you! "
    kat "I'm not gonna be your little fetish. "
    kat "All I've EVER wanted to do is help you. "
    kat "Go run back to your mommy, Wren. "
    kat "Stop breaking girl's hearts. "
    kat "Are you even really sick? "
    wren "I'm serious Katriel."
    wren "So stop being a complete dick right now? "
    kat "Sigh. "
    # music change 
    kat "Okay. It's just. It's just a lot okay? "
    kat "I wish you weren't sick!"
    wren "Woah, you can stop gripping my shirt so tight. "
    kat "I bet you taste like blood right now. "
    kat "I wanna see what it's like. "
    wren "Back off Katriel. "
    kat "What. Didn't you JUST confess to me. "
    kat "Why are you doing this to me this now? "
    wren "How about let's.. go inside? "
    kat "FUCK YOU WREN! "
    wren "No? "
    kat "."
    kat ". . "
    kat "What am I doing? "
    kat " Ugh God"
    kat "I'm sorry Wren. I'm so sorry. "
    kat "I didn't get enough to eat today and my dad was really- "
    kat "It doesn't matter. It's not your fault. "
    kat "You look pale"
    kat "I'm so sorry for my outburst. "
    kat "Wren. Lets go?"
    wren "Your hand is warm… "
    wren "It's nice. "
    wren "It's the same as all those years ago. "
    kat "It feels different to me."
    # fade to black 
    # [] if have time write Kat and Wren sex scene? 
    # fade to into a hospital clinic. 
    # Wren and Kat are next to each other, talking to a researcher. Wren is pale and sickly. 
    kat "Well, we already got her a blood culture and they didn't find any sign of sepsis. "
    wren "{i}I didn't know that. "
    kat "And so far all she's done is answer questions and take tests! "
    kat "I even brought you the petals and you won't take a look. "
    researcher "That counts as a biohazard, Miss. We have to throw those away. "
    wren "I - "
    researcher "And has small cell carcinoma been ruled out? "
    kat "Yes, we just got the results a week ago. "
    researcher "Hmm, actually, about those hives and itchiness. "
    kat "Yes? "
    researcher "We could do a biopsy, and I'll send it to the Novel Research Lab as well. See what they have to say. "
    kat "That would be lovely. "
    researcher "It won't be a long procedure. Let's schedule it. "
    kat "O-"
    #wren speaks fast
    wren "{sc=5.0}No. No biopsy. "
    kat "She can do it. "
    wren "No!"
    researcher "Well. Umh."
    wren "Not that. Just- isn't there anything else? "
    researcher "Well, I suppose we could do a liquid biopsy. "
    kat "Wren. "
    wren "Yes. Let's do that. "
    # go to outside Kat's house. Wren and katriel are there. 
    wren "Are you still mad at me? "
    kat "Do you even have to ask? "
    wren "You shouldn't be mad about me not wanting strangers to look at me. "
    kat "I'm mad because you refuse to do the right thing! "
    kat "Just cooperate with the very nice, very busy, nice researchers who just want to help you. "
    wren "Who want to put a knife to me. While I'm asleep. "
    kat "It's just one sample! "
    wren "It's my fucking disease. "
    kat "Oh. OHHHHHH. "
    kat "Is it now, Wren? "
    kat "Despite it being your fucking disease, I end up scheduling all the appointments. I pick up your prescriptions. I remind you for everything, everything! "
    wren "Aw shucks. Thanks for completely invading my entire life even though I didn't ask. "
    kat "As if you wouldn't be rotting in your bed right now without me. "
    wren "Oh, yes, of course, my bad. You think you can run my life because you're so much better than me. "
    kat "I don't think that. "
    wren "You've literally told me that, Katriel. "
    kat "Fuck off already. "
    wren "Go fuck yourself. "
    kat "FUCK YOU! "
    # katriel sprite runs off screen. Breathing heavily sound. 
    wren "So there. "
    wren "Ah. "
    wren "I should go apologize. "
    wren "Fuck you Kat. "
    wren "I should really go and apologize… "
    # katriel room kay is already there Wren sprite comes in. 
    kat "Snif! Sob! "
    wren "Hey. "
    kat "Mmfh. "
    wren "I got pretty heated. "
    wren "I'm actually um. "
    wren "really grateful for everything you do for me. "
    wren "You're amazing Kat. "
    kat "You mean it? "
    wren "Yeah. "
    kat "I just want to help you. You're so special to me, I love you so much. "
    wren "I know. Hey, I know. "
    kat "Do you love me as much as I love you? "
    wren "You're the best person in my life right now. "
    kat "That's not a yes. "
    wren "I love you. "
    kat "Then why won't you let me help you get better? "
    wren "It's not about that. "
    kat "Then what is it about? "
    wren "…  "
    kat "You don't want to feel better. "
    wren "I'd kill to have my lungs work again. "
    kat "So. You don't want to be with me."
    wren "Where are you pulling this from? "
    kat "I can't think of any other reason why you fight against a cure at every turn. "
    wren "I just hate the doctors poking and prodding and stealing bits of me away. "
    wren "I'm so tired of filling out papers about when the last time I shit was. "
    wren "I just keep getting worse. "
    kat "This could have been the one to help. "
    wren "It's not your fault. "
    kat "You know, if I had known, I wouldn't have played doctor for you. "
    wren "Please don't stop."
    kat "But you just said? "
    wren "It's not okay for strangers to do it. "
    wren "You're…  more gentle than them. "
    wren "…"
    wren "Do you want to take the sample?"
    kat "Really? "
    wren "I'm sure."
    kat "They won't accept me bringing in a lump of your flesh. "
    wren "I just need you to do it. "
    kat "Why? "
    wren "Before they touch me. You have to be the one. "
    kat "Okay. I'll do that for you. "
    kat "Lie on the bed for me, okay? "
    kat "I don't have any of my fancy tools with me, but I sterilized the box cutter. "
    wren "Are you sure? "
    kat "If you are. "
    wren "Okay. Do it. "
    # screen goes red, then black, if we have time for the cg where kat cut wrens wrist with a box cutter is blooming, please place that here, if not, put some really lush and blooming but still gloomy foliage. 
    kat "You're beautiful. "
    kat "Wren, you're beautiful. "
    # END! roll credits! 
    return

label kat_worse:
    #katriel worse- 
    kat "You don't have to give me that, Wren. "
    kat "Not if you don't want to. "
    kat "I'll take care of you. I don't need... "
    wren "Okay, okay. "
    kat "You can trust me with that kinda stuff, all right? "
    kat "I was just. Really sensitive today. "
    kat "My dad keeps hassling me to find a fiance. And he just called, and said a bunch of stuff, and…"
    wren "You're really accomplished, and smart. It would be stupid to waste you on a man. "
    wren "You're gonna change the world. "
    kat "Can hug you? "
    #kat and Wren sprite get closer 
    #wren quiet
    wren "I don't know why dating me would be so bad… "
    # K smiles 
    kat "Let me clean you up, my Wren. "
    wren "I'm sorry for everything I said. "
    kat "I forgive you. "
    wren "You're pretty and I like you and"
    # sound effect of a slap? 
    wren "mmfhhg?? Nblh??? "
    kat "I thought I saw something in your mouth. "
    kat "Here we are. "
    # K takes her hand out. Something long and slimy is attached to her hand, and Wrens throat. 
    # if we don't have time, just show the nasty cg from earlier lol
    kat "Gross. I don't even know that is. "
    # fade to black. 
    # wren is in her bedroom. It's dark. 
    kat "Yes, I'm ever so grateful Ms. Warner."
    mom "I'm the one who is grateful. She's really perked up since she's been with you. "
    mom "She could learn a thing or two from you. "
    kat "Haha, yes, she could. "
    mom "But she really appreciates you, Katriel. you really are a lovely girl. "
    kat "Thank you Ms. Warner. "
    wren "… . "
    # Footsteps sounds 
    # W Face tightens. 
    # Door open sound. 
    kat "Wren! How are you feeling! "
    kat "Oh, gosh, you knocked over your cup. Not good, not good. "
    kat "Here, we need to change your bandages. "
    wren "Ouch. "
    kat "No. No ouch. "
    kat "These could have been avoided. "
    kat "You deserve them Wren."
    wren "They still hurt. And I'm feverish. "
    kat "It would hurt less if you stayed still. "
    wren "Can I sleep alone tonight? Please? "
    kat "Why would you ask me that? "
    kat "I mean, of course, but why? "
    wren "I don't know. "
    kat "That's not a real reason."
    kat "What's the real reason? "
    wren "It's hot with you in here. "
    kat "I'll turn on the fan! No issue."
    wren "… "
    kat "So we're good right? "
    kat "Wren, are we good?"
    kat "I don't even get a thank you? "
    kat "God. We can just put you in a hospital if that's what you want. "
    kat "Where they'll call you Marcus and stab you with needles . "
    kat "And there will be no one to hold your hand. "
    kat "sniff! Sob! "
    wren "No no no, hey. "
    wren "Sleep with me tonight. "
    kat "You're just saying that to make me feel better. "
    wren "I really want you to sleep with me tonight. "
    kat "You mean it? "
    wren "Pinky promise. "
    kat "You sappy bitch. "
    kat "Sigh. You know you can tell me anything, right? "
    wren "Of course. "
    kat "You would tell me if anything was wrong, right? "
    wren "Of course. "
    kat "… "
    wren "Leave it alone. "
    kat "Is it what happened at the restaurant earlier? "
    wren "No…  I mean.. Yes? Maybe? A little? "
    kat "I'm really really sorry. "
    kat "I shouldn't have messed around like that. "
    kat "You're just so cute when you're all worked up like that, and I'm sure the waitress didn't mind. "
    wren "I felt like you wanted her more than me. "
    kat "That's not true. "
    kat "I really love you a lot Wren. "
    wren "Yeah, me too. "
    kat "You know how hard it is for me to be vulnerable and affectionate with words. "
    kat "My actions show my love. Every day. "
    kat "I would do anything for you. "
    wren "I promise it's okay. Let's just go to bed. "
    kat "It's clearly not okay! You're not okay! "
    wren "What do you want from me?"
    kat "Some fucking honesty! "
    wren "That's rich, coming from you. "
    kat "What the fuck is that supposed to mean. "
    wren "I'm going to sleep. "
    kat "No, Wren. "
    wren "Goodnight. "
    kat "This isn't fair!"
    wren "How is this not fair. "
    kat "I help you so much. Your room is clean because of me. You have a job because of me. You mistreat me and screw up and I'm patient because I know you are sick. "
    kat "And the one time, the one time I dare to even try and joke around, you call me an abuser? "
    kat "Is that it? Is that how it is now? "
    wren "That's not what I meant… "
    kat "Then what did you mean"
    kat "Because I want to leave right now. "
    wren "No, c'mon Kat. "
    kat "Oh so now it's Kat. Not “ abusive piece of shit. “ "
    wren "Please? I'm sorry. "
    wren "I'll never do it again. "
    kat "… "
    wren "Kiss me? "
    kat "No. "
    kat "Good night. "
    wren "Night."
    kat "Are you sure you're okay? "
    wren "I love you. "
    kat "I love you too. "
    # We zoom out and see Kat and Wren spooning, Kat bieng little spoon, Wren big. Kat makes a happy sound and nuzzles closer to Wren. 
    # 
    # Wren doesn't react. We see the back of her head, which is filled with roots and flowers. 
    "This hasn't been Wren for weeks. Kat doesn't seem to mind."

    #END
    return  

