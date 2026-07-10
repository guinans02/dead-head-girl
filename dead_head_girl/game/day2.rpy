label day2:
    call garden_day2
    call kat_texts_wren
    call post_garden_day2
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

    show wren at mv(left, center, 0.5)
    wren "Hello? "
    show wren pose1 pensive
    wren "Shit. "
    show wren at mv(center, right, 0.5)
    wren "… "
    # (make her move around the screen a little, like she's walking in thought) 

    show wren pose1 woah at mv(right, left, 0.5)
    show ines mlem at mv(offscreenright, right, 0.5)
    ines "Say cheese! "
    wren "Cheese…? "
    # camera snap effect
    # camera flash
    show wren pose1 angry at max_y
    wren "Ack! Don't do that! "
    # cg of a Polaroid of Wren. It hasnt developed yet, so it's black.

    #back to Wren Ines in garden
    show ines pose1 smile one at max_y, right
    ines "You look so pretty. Ephemeral, almost, with the blurry effect. "
    show wren pose1 bashful at max_y
    wren "Do you mean ethereal? "
    show ines pose_two laugh at max_y
    ines "No, ephemeral."
    wren "Do you know what that word means? "
    ines "You're being rude. "
    wren "so, now we're even. "
    # cg wren's poloraid. Its blurred and grainy
    wren "I mean, it's a photo. "
    ines "Hmmph."
    wren "you're sweet for showing it to me. "
    ines "I don't really like photography all that much. Camera photos look too real. "
    ines "Drawings, though, capture the feeling of a living thing. I get to remember you how I see you for however long I keep the drawing."
    ines "But polaroids are still pretty cool. I like how grainy they are. It helps to hide the imperfections. "
    wren "You intend to make it look that blurry? "
    ines "Well, no. But I like the effect. "
    "A beat of silence." 
    wren "What exactly am I doing in the garden today? "
    ines "Oh, have you forgotten your promise already? "
    wren "I. "
    wren "I was scared you were messing with me. "
    ines "I'm not some high school mean girl! "
    ines "Wren, you have this sort of worldly air to you. Like you know something. I want to find out what it is. "
    ines "I must paint you. "

    #wren blushes
    wren "If you really want to that bad… "
    ines "I brought some props from home. I'm so excited! "

    # rummage sound effect
    ines "Let's see, lets see"
    ines "I have a piece of muslin fabric for draping"
    ines "I like doing texture work, so I also have some lace.. "
    ines "ooh! Or what about something here, from the garden! "
    ines "paying homage to the flowers you crushed, a mourning piece! "
    wren "{i}what. "
    ines "um or actually "
    ines "I brought something I made for you. "
    ines "it took me a while, but I think you'd look just perfect in it. "
    ines "what do you think?? "

    #choices
    menu:
        "Is that a crown of leaves?":
            # +1 Ines affection
            $ines_obj.update_score(1)
            jump crown_of_leaves
        
        "Do I have to?":
            jump do_i_have_to
    
    label crown_of_leaves:
    ines "Yes, I thought it would symbolize renewal."
    ines "I knew you had a good eye for the arts."
    wren "{i}I guess I get how the leaves are renewal. "
    wren "{i}But I don't get those other ideas. "
    wren "{i}Who would mourn a bush? It didn't even die." 

    wren "I'll just go with the crown."
    ines "Yay! I love working with live models. "
    # Ines moves closer to Wren "
    ines "Ok. Sit down like that. Spread out your arms a little."
    ines "Hm… look up. there we go! "
    # my inspiration is jesus on the crucifix with his crown of thorns lookin up. wowie
    # wren sprite w a green crown
    # humming music 
    ines "Perfect. Such a good girl. "
    # pencil scratch noises. "
    ines "Hm hm hmmm."
    # pencil scratch noises "
    wren "Can ines "
    ines "Stay still please!! I'm capturing your lips. "
    wren "(internally) But something is poking me…  "
    wren "(internally) I can feel something dripping down my face. "
    # Wren sprite with crown and a line of blood"
    wren "Ines, take it off of me. "
    ines "la la la ~ (locked in on sketching)"
    wren "ines. i think i'm bleeding. "
    ines "Don't worry. the red stands out quite nicely on your pallor. "
    ines "Oh! you're just like a real life snow white. "
    wren "it's kinda hurting. "
    wren "like bad actually "
    ines "but I'm almost done! "
    wren "… "
    ines "sigh. "
    ines "alright. if you insist."
    # Ines gets closer to Wren. "
    wren "why are you"
    ines "you are like a real life fairy tale. "
    ines "my princess. "
    wren "you didn't just taste my blood. "
    ines "an artist must know her materials. "
    ines "you really do have such nice color. "
    wren "umh"
    ines "my thumb print, in your heart's blood on the canvas. "
    ines "now you'll always be with me. "

    jump post_garden_day2

    label do_i_have_to:
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
    ines "Great, I have everything I need. Thank you so much!"
    wren "(if crown of thorns was picked) - Of course. It's a pleasure. "
    wren "(if it was the other one) - Sure. You're welcome. "
    ines "I'll see you next week? "
    wren "Okay!"
    ines "Get home safe! "
    show ines at mv(right, offscreentright, 0.5)
    return

label kat_texts_wren:
    # Wren walks to outside. "
    show wren at mv(left, offscreenleft, 0.5)
    stop music
    stop ambience
    scene houses
    show wren at mv(offscreenright, center, 0.75)

    wren "{i}That was weird. "
    wren "{i}I mean. "
    wren "{i}That's mean of me. She's a perfectly nice girl. "
    wren "{i}Can I really ignore those dead art subjects though?"
    # phone notification sound"
    wren "Umh?"
    # phone screen bg"
    phone_wren "wren : Is everything ok? "
    phone_wren "wren : I'm sorry. Can we talk? "
    phone_wren "wren : KAT KAT KAT KAT KAT "
    phone_wren "wren : I saw you walking outside. You're not dead or sick. "
    phone_wren "wren : Please, Katriel. you're my best friend. "
    phone_wren "wren : I'll leave you alone if you want?"
    phone "You have [1] new message(s)."
    phone_kat "katriel:  Swedish researchers have discovered that salmon dosed with benzoylecgonine, a cocaine byproduct, swim almost twice as far as the control group."

    phone_wren "Seriously, Kat? That's your first message to me in three years?"
    phone_wren "wren : And this is relevant because…? "
    phone_kat "kat : I have your workbag. Come over when you're first available. "
    phone_wren "wren : Just leave it on my doorstop. "
    #pull choice from day one (check kat score?)"
    phone_kat "kat : No. Don't you want to continue our conversation about <LESBIANs/your family>?"
    phone_wren "I'll… just go now. "
    return

label wren_visits_kat:
    # wren in front of kat's house. "
    # DIALOGUE"
    # knocking sound"
    wren "Hello?"
    wren "Hellooooo?"
    wren "Of course Kat still doesn't lock the front door. "
    wren "Katriel? I'm here. "
    wren "Kaaat. Since you're not here, I'm going up to your room! "
    wren "KAT!"
    # coughing sounds"
    wren "I'm he-"
    # more coughing sounds. "
    # K comes on screen. "
    kat "Hey Wren."
    kat "Oh, that's some blood. "
    kat "Hey, let's come up to my room. "
    # wren and kat in kat's room. It's pink and girlish. "
    wren "It smells weird in here. "
    kat "I'm not gonna take that from someone with blood in her nose. "
    kat "Let me clean you up. "
    wren "Okay. "
    kat "What's with that cough?"
    wren "I… don't really know, actually. "
    kat "How long have you had it?"
    wren "Um, a few weeks now?"
    kat "You should really go to a hospital. "
    wren "With what money, exactly?"
    kat "Hm. Well. "
    kat "Want me to take a look? You know, aspiring toxicologist right here… "
    wren "But-"
    kat "You'll be a nice case study. "
    kat "Indulge me?"
    wren ". . ."
    kat "Just a joke. so? "
    wren "Sure. Can't hurt. "
    # Kat moves closer"
    # heartbeat sound"

    wren "You smell like it too. "
    kat "Jesus, it's only the smell of the lab. "
    wren "It's not bad just strong. "
    kat "Then, say Aah. "
    wren "What are you doing?"
    kat "Open your mouth. "
    wren "Ahh? "
    kat "Good girl."
    kat "Well. Everything looks normal? "
    kat "A bit inflamed, though. Have you been eating chips 24/7 or something? "
    wren "No? "
    wren "…  "
    kat "you-"
    wren "you-"
    wren "You smell nice "
    kat "Did you do this?"
    wren "What?"
    kat "What?"
    wren "I said you smell nice."
    kat "Thanks."
    # Kat sprite move back "
    kat "Okay well, since you're here can you help me study? "
    wren "Ah, I get it now. Got too bored studying all by yourself. "
    #kat blushes
    kat "I do actually have your bag!"
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


    return
