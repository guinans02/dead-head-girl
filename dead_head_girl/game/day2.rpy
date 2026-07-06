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

    show wren pose2 pain2 at max_y, mv(offscreenleft, left, 0.5)
    #  Wren walking into ines's garden. 

    wren "Where is she?? "
    wren "I know I'm late, I'm sorry. "

    show wren at mv(left, center, 0.5)
    wren "Hello? "
    show wren pose2 pain1
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
    show wren pose1 angry
    wren "Ack! Don't do that! "
    # cg of a Polaroid of Wren. It hasnt developed yet, so it's black.

    #back to Wren Ines in garden
    show ines pose1 smile one
    ines "You look so pretty. Ephemeral, almost, with the blurry effect. "
    show wren pose1 
    wren "Do you mean ethereal? "
    ines "No, ephemeral."
    wren "do you know what that word means? "
    ines "You're being rude. "
    wren "so, now we're even. "
    # cg wren's poloraid. Its blurred and grainy
    wren "I mean, it's a photo. "
    ines "hmmph"
    wren "you're sweet for showing it to me. "
    ines "I don't really like photography all that much. Camera photos look too real. "
    ines "drawings, though, capture the feeling of a living thing. I get to remember you how I see you for however long I keep the drawing."
    ines "But polaroids are still pretty cool. I like how grainy they are. It helps to hide the imperfections. "
    wren "you intend to make it look that blurry? "
    ines "well, no. But I like the effect. "
    "A beat of silence." 
    wren "what exactly am I doing in the garden today? "
    ines "Oh, have you forgotten your promise already? "
    wren "i. "
    wren "I was scared you were messing with me. "
    ines "I'm not some high school mean girl! "
    ines "Wren, you have this sort of worldly air to you. Like you know something. I want to find out what it is. "
    ines "I must paint you. "

    #wren blushes
    wren "if you really want to that bad… "
    ines "I brought some props from home. I'm so excited! "

    # rummage sound effect
    ines "let's see, lets see
    ines "I have a piece of muslin fabric for draping
    ines "I like doing texture work, so I also have some lace.. 
    ines "ooh! Or what about something here, from the garden! 
    ines "paying homage to the flowers you crushed, a mourning piece! 
    wren "{i}what. 
    ines "um or actually 
    ines "I brought something I made for you. 
    ines "it took me a while, but I think you'd look just perfect in it. 
    ines "what do you think?? 

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
    wren "Can ines ""
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
    wren "Let's do the piece here, mourning the flower ines ""
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
    wren "(internal?) Y’know Kat, it feels like you’ve changed so much, but at the same time you feel the same. But the old you and the current you… they’re both beyond what I could be. Everything you do. I just wonder if you know what you could be. What you want to do.
    wren "why did you go back to toxicology? 
    kat "it's just the best path forward for me. 
    wren "it didn't seem like that when we last spoke.
    kat "gosh, just lay off me already, will you? people change.
    wren "i know you though. 
    wren "is this really what you want for yourself? 
    kat "are you fucking serious? 
    kat "of course not. i hate talking to those bitches with their heads up their asses and i hate the stagnance in that fuckass company with their bullshit about reinventing the wheel. 
    kat "but i've tried my hardest for too long to be left languishing with the rest of the unwashed masses. even if it means devoting myself to something i find completely meaningless or presenting myself as the perfect person or ignoring that gnawing gap inside or that I can never have what I really want-
    #smtg like how she's abt to blurt out she realises internally that she highkey a lesbian but more subtle]
    kat "it doesn't matter. 
    kat "i have to succeed. i'll be the best in my field. the first person everyone rushes to talk to when i walk into a room. 
    menu:

        "you're the most successful person I know":
            jump most_successful_person

        "You're just human too.":
            jump just_human

    label most_successful_person:
    kat "thanks. "
    kat "still. i always have room to grow. i always have more to improve at. "
    #idk smtg abt a spider respinning its web constantly lol until it's left the space to thrive or someone kills it "

    label just_human:
    wren "Oh."
    wren "You're just human too. "
    kat "don't put me down on your level. "
    kat "you have no goals, no aspirations, no presence. hearing that from you—god, that's such a low bar. few years no see, one word from me and you're back following me around like a sad little dog with nowhere to go and no one to play with."
    wren "you're talking? you're no one special. you try to sound intelligent but you're really just a pretentious soulless corporate suck up. there's millions of girls like you out there. "
    kat "at least i have self control. i wouldn't have let some random feelings for a girl–i mean, a momentary lapse of judgement–ruin everything i've built. "


    return
