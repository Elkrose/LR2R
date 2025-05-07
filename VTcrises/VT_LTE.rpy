init 5 python:
#making it a habit to init hijank label lower priority
 
    config.label_overrides["sleep_climax_manager"] = "improved_sleep_climax_manager"




label improved_sleep_climax_manager(the_person, straddle = False, stomach_allowed = False, face_allowed = False, tits_allowed = False, throat_allowed = False, inside_allowed = False, pussy_allowed = False): #Helper that collects all of the orgasm checks
    $ climax_controller = ClimaxController(*build_sleep_climax_menu_options(the_person, straddle, stomach_allowed, face_allowed, tits_allowed, throat_allowed, inside_allowed, pussy_allowed))
    $ the_choice = climax_controller.show_climax_menu()
    "You take a deep breath and pass the point of no return."
    if the_choice == "Cum in your hand":
        call sleep_cum_hand(the_person, climax_controller) from VT_call_sleep_cum_hand
        return _return

    elif the_choice == "Cum on her stomach":
        call sleep_cum_stomach(the_person, climax_controller) from VT_call_sleep_cum_stomach
        return _return

    elif the_choice == "Cum on her pussy":
        call sleep_cum_pussy(the_person, climax_controller) from VT_call_sleep_cum_pussy
        return _return

    elif the_choice == "Cum on her face":
        call sleep_cum_face(the_person, climax_controller, straddle = straddle) from VT_call_sleep_cum_face
        return _return

    elif the_choice == "Cum on her tits":
        call sleep_cum_tits(the_person, climax_controller, straddle = straddle) from VT_call_sleep_cum_tits
        return _return

    elif the_choice == "Cum down her throat":
        call sleep_cum_throat(the_person, climax_controller) from VT_call_sleep_cum_throat
        return _return

    elif the_choice == "Cum inside her":
        call sleep_cum_vagina(the_person, climax_controller) from VT_call_sleep_cum_vagina
        return _return

    return False


label sleep_cum_pussy(the_person, climax_controller):
    $ the_person.draw_person(position = "missionary")

    $ climax_controller.do_clarity_release(the_person)
    "Your heart hammers as you free yourself, the cool air contrasting with the heat building in your groin. The intoxicating mix of her sleep-warmed skin and the faint musk of arousal makes your head swim."
    $ wake_chance = 40
    "With gritted teeth, you stroke yourself to the rhythm of her breathing. When release comes, it's a white-hot flood painting stripes across [the_person.possessive_title]'s inner thighs and mound."
    $ mc.change_locked_clarity(30)
    $ wake_chance += -5*the_person.opinion.creampies

    if renpy.random.randint(0,100) < wake_chance - 5*the_person.opinion.creampies:
        "A floorboard creaks as you shift your weight. [the_person.possessive_title]'s breathing hitches - then stops entirely."
        the_person "[the_person.mc_title]?"
         "Her nostrils flare as the scent of your release reaches her. Long before your breathing steadies, her eyelids flutter open - but there's no surprise in those drowsy eyes."
        "[the_person.possessive_title!c] lifts her head, her gaze locking onto the cum-covered mess between her legs."
        if the_person.effective_sluttiness() + (5 * the_person.opinion(("being submissive", "creampies"))) > 70 and not the_person.has_taboo("vaginal_sex"):
            the_person "Oh... that's what I was dreaming about. You, inside me, filling me with your cum."
            "She lets out a sultry sigh, her eyes gleaming with desire. She reaches down and touches the cum on her skin, feeling its warmth and texture."
            "A knowing smile curves her lips as she trails fingers through the cooling mess. You watch, transfixed, as she gathers your cum on three fingertips and slowly circles her clit."
            the_person "Thank you [the_person.mc_title]. Mmm... I love the way your cum feels on my skin. It's so hot, so sticky."
            mc.name "I couldn't resist the sight of you lying there, so vulnerable and sexy."
            the_person "Wait, did you... cum on me?"
            mc.name "I couldn't help myself. You're just too hot, too tempting."
            
            if the_person.wants_creampie:
               "Her back arches as she pushes two cum-slick fingers inside herself. 'Couldn't wait for an invitation?' she pants, working her wrist in smooth motions that make your spent cock twitch. 'Next time... ah... wake me when you're still hard.'"
                # Accidental creampie
                if renpy.random.randint(0,100) < 20:
                    "As she touches herself, a glob of your cum slips inside her, and she gasps in surprise."
                    $ play_moan_sound()
                    $ the_person.cum_in_vagina()
                    the_person "Oh shit... I think some of it went inside me..."
                    "You watch her silently, half in awe and half excitedly as you watch her finger herself."
                    the_person "It's okay... I think I like it. It feels so good, so right."
                    $ mc.change_locked_clarity(20)
                    $ the_person.event_triggers_dict["immaculate_conception"] = True
            else:
                the_person "You're so naughty, [the_person.mc_title]. Now I'm all sticky and wet. But I have to admit, it feels kind of good and makes me feel sexy and desired."
            mc.name "I'll try to be more careful next time. But for now, just enjoy the feeling of my cum on your skin."
            "She seems to drift off to sleep again, her fingers absently tracing the cum on her pussy as she moans softly, a finger slips in to massage her clit."
             "She murmurs something unintelligible, hips rolling in a sleepy grind that smears your cum between her thighs. Her fingers twitch near her neglected pussy but ultimately remain still."
        else:
            the_person "You're... standing over me."
            mc.name "Hey [the_person.title]... I just couldn't resist."
            the_person "You can't... We can't have sex [the_person.mc_title], it's not right! What did you do?"
            mc.name "I may have gotten a little carried away..."
            "She gasps, her eyes wide with shock."
            the_person "You... came on me? Please tell me that's not what I feel!"
            mc.name "I'm sorry, [the_person.possessive_title!c]. I didn't mean to make a mess."
            the_person "You... should go. You're finished, right?"
            mc.name "Yeah, I'm feeling pretty satisfied."
            "You back up and retreat out of the room, leaving [the_person.title] to deal with the aftermath."

            # Accidental creampie
            if renpy.random.randint(0,100) < 20:
                "As you walk out of the room, you recall that the head of your penis had slipped inside her, and some of your cum had spilled into her vagina.... oh shit."
                $ the_person.cum_in_vagina()
                "You wonder if she'll notice when she wakes up."
                $ the_person.event_triggers_dict["immaculate_conception"] = True
        "You slip away already imagining how she'll react when she finds your dried cum gluing her thighs together tomorrow."
        return True
    else:
        "A breathy 'please' escapes her lips - whether from current sensation or dream memory, you can't tell."
        $ play_moan_sound()
        if the_person.wants_creampie:
            the_person "Mmm... more..."
            $ mc.change_locked_clarity(20)
            "She moans softly, her fingers absently tracing the cum on her skin as she sleeps. Her hips shift slightly, as if she's trying to guide your cum inside her."
            "Her fingers dip lower, brushing against her pussy lips as she tries to push your cum inside. You can see the desire in her movements, even though she's still asleep."
        else:
            "She moans and shifts underneath the covers, her body responding to the sensation of your cum on her skin. Her fingers move restlessly, as if she's trying to find a way to get your cum inside her."
        "She murmurs something unintelligible, hips rolling in a sleepy grind that smears your cum between her thighs. Her fingers twitch near her neglected pussy but ultimately remain still."
        # Accidental creampie
        if renpy.random.randint(0,100) < 20:
            "As she moves, her fingers accidentally push some of your cum inside her. She gasps softly, her body responding to the sensation of your cum entering her."
            "A knowing smile curves her lips as she trails fingers through the cooling mess. You watch, transfixed, as she gathers your cum on three fingertips and slowly circles her clit."
            $ the_person.cum_in_vagina()
            $ the_person.event_triggers_dict["immaculate_conception"] = True
            "You wonder if she'll notice when she wakes up, or if she'll just feel the aftermath of your cum inside her."
        "You back up off of her bed and stand up, watching as she continues to finger herself in her sleep. The sight of her touching herself, even in her sleep, is incredibly arousing."
        "Your cum leaks onto her skin, and you wonder when, or if, she'll notice when she wakes up. But for now, you're just happy to watch her enjoy the sensation of your cum on her skin."
        "You slip away already imagining how she'll react when she finds your dried cum gluing her thighs together tomorrow."

    return False










