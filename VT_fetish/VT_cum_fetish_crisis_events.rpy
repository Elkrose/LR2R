label VT_cum_fetish_morning_shower_label():
    $ the_person = VT_get_fetish_shower_cum_girl()
    if the_person is None:
        return
    "You wake up a little groggy. Your head kinda hurts, so you grab some clothes and head towards the bathroom to take a hot shower. Hopefully the steam will help you feel better."
    $ mc.change_location(home_shower)
    "You stand in the shower, enjoying the hot water for several minutes. The steam is beginning to cloud up the bathroom."
    "You hear the shower door open and see [the_person.possessive_title] getting in the shower with you."
    $ the_person.apply_outfit(Outfit("Nude"))
    $ the_person.draw_person()
    $ mc.change_locked_clarity(30)
    the_person "Good morning [the_person.mc_title]. Mind if I join you?"
    mc.name "Of course! Come on in."
    the_person "Thanks! I saw you get in the shower this morning... I was feeling thirsty, so I decided to hop in."
    "[the_person.possessive_title!c] reaches down and begins to stroke your cock."
    the_person "I had so many crazy dreams last night, all about you... cumming really hard!"
    the_person "It was amazing! You just kept cumming and cumming... all over me, and I was swallowing as much as a could and I was covered in it..."
    $ the_person.draw_person(position = "kneeling1")
    $ mc.change_locked_clarity(50)
    "[the_person.possessive_title!c] gets down on her knees."
    the_person "I'm sorry, I know I shouldn't approach you like this... but I can't help myself this morning! Give me your cum please!"
    "[the_person.possessive_title!c] looks up at your from her knees. She looks you right in the eyes as she leans forward and slides her lips over the tip of your dick."
    call get_fucked(the_person, sex_path = build_blowjob_path(the_person), start_object = make_floor(), skip_intro = True, allow_continue = False) from _call_get_fucked_VT_cum_fetish_morning_shower_label
    the_person "Oh my god, thank you [the_person.mc_title]. I needed that so bad."
    "[the_person.possessive_title!c] stands up. Her hunger for cum satisfied for now."
    $ the_person.draw_person(position = "stand4")
    the_person "Okay... I'm going to hop out and let your finish showering now. Please give me more cum soon!"
    "[the_person.possessive_title!c] gets out. You finish up with your shower, balls empty and ready for the day!"

    python:
        the_person.apply_planned_outfit()
        mc.change_location(bedroom)
        clear_scene()
    return

label VT_cum_fetish_employee_dosage_request_label():
    $ the_person = VT_get_fetish_cum_dosage_employee()
    if the_person is None:
        return
    "As you finish up with one of your work tasks, you decide to take a quick break."
    $ mc.change_location(ceo_office)
    "You step into your office and sit down for a minute. You hop on your laptop and start browsing the internet."
    "*KNOCK KNOCK*"
    $ the_person.draw_person()
    "You look up and see [the_person.possessive_title] at your door."
    if mc.business.is_open_for_business:
        mc.name "Hello [the_person.title], come in."
        "[the_person.possessive_title!c] walks into your office."
        the_person "Hey [the_person.mc_title]. So... I saw you walk into your office a minute ago and I was just thinking that it's been a while..."
        mc.name "A while since what?"
        "[the_person.possessive_title!c] stutters for a second."
        the_person "... A while since you let me have your cum, so I thought..."
        "[the_person.possessive_title!c] voice trails off. It seems she is craving it again."
    else:
        "You are surprised to see her, considering the business is closed for the day."
        mc.name "Hello [the_person.title], come in."
        "[the_person.possessive_title!c] walks into your office."
        the_person "Oh [the_person.mc_title]! Thank goodness you are here, you're just the man I wanted to see."
        the_person "You know how much I need your cum... so I was wondering... want to take a five minute break? I promise I won't be a bother!"
    $ mc.change_locked_clarity(20)
    menu:
        "Suck me off":
            the_person "Yes! Oh thank you [the_person.mc_title]!"
            "[the_person.possessive_title!c] walks over to you and immediately drops down on her knees. You consider asking her to strip down a bit, but she is already too busy stroking your cock."
            $ the_person.draw_person(position = "blowjob")
            ###cum Scene, standing variant###
            call get_fucked(the_person, sex_path = build_blowjob_path(the_person), start_object = make_floor(), skip_intro = True, allow_continue = False) from _call_get_fucked_VT_cum_fetish_employee_dosage_request
            the_person "Oh my god, thank you [the_person.mc_title]... I wish I had time to make you cum again... but I know you're a busy man..."
            "[the_person.possessive_title!c] starts to get up. Her hunger for cum satisfied for now."
            the_person "Thanks again, [the_person.mc_title]. Don't hesitate to ask if you ever need to be... you know... serviced."
            "You wave goodbye to [the_person.possessive_title] as she leaves your office. Damn that was good!"
        "No Thanks":
            "[the_person.possessive_title!c] is caught completely off guard by your refusal."
            $ the_person.change_stats(happiness = -10, obedience = -10)
            #$ the_person.set_event_day("LastCumFetish")
            $ VT_fetish_timer_reset(the_person, "cum", 2, False)
            the_person "Oh!... Okay... Well... hey I understand... Maybe some other time yeah?"
            "[the_person.possessive_title!c] quickly sulks off. Maybe you should've?"
        "Too Tired" if mc.energy < 30:
            "[the_person.possessive_title!c] is surprised by your answer."
            $ the_person.change_stats(happiness = -5, obedience = -5)
            #$ the_person.set_event_day("LastCumFetish")
            $ VT_fetish_timer_reset(the_person, "cum", False)
            the_person "Oh! I'm sorry... I know you work so hard around here. Maybe tomorrow then?"
            "[the_person.possessive_title!c] quickly sulks off."
    python:
        the_person.apply_planned_outfit()
        clear_scene()
    return

label VT_cum_fetish_non_employee_dosage_request_label():
    $ the_person = VT_get_fetish_cum_dosage_non_employee()
    if the_person is None:
        return
    "While going about your day, your phone suddenly rings."
    the_person "Hello, [the_person.mc_title]? Do you have a minute?"
    mc.name "Oh, hey [the_person.title], it's you. Sure, what's up?"
    the_person "Could we meet up, right now? I have a little problem, that I need you to solve."
    mc.name "What kind of problem?"
    the_person "Well, eh, I'm desperately in need of some proteins."
    "It seems she is desperate for you to satisfy her cum fetish, what will you do?"
    menu:
        "All right":
            if mc.is_at_office:
                mc.name "All right, can you come down to my business, I can make some time for you."
                the_person "No problem, I'll be in your office in 10 minutes."
                if not mc.location == ceo_office:
                    "You go up to your office to await [the_person.possessive_title]'s arrival."
                    $ mc.change_location(ceo_office)
                "You relax a while in your office, until there is a knock at your door."
            else:
                mc.name "All right, meet me at my place in 10 minutes."
                $ mc.change_location(hall)
                $ her_hallway.show_background()
                "You just got home, when your doorbell rings."

            $ the_person.draw_person()
            $ mc.change_locked_clarity(30)
            the_person "Hey [the_person.mc_title], I came as fast as I could."
            if mc.is_at_office:
                "[the_person.possessive_title!c] walks up to you and immediately drops down on her knees."
            else:
                "[the_person.possessive_title!c] pushes you inside and immediately drops down on her knees."
            $ the_person.draw_person(position = "kneeling1")
            "You consider asking her to strip down a bit, but she has already managed to pull your cock out of your pants."
            call get_fucked(the_person, sex_path = build_blowjob_path(the_person), start_object = make_floor(), skip_intro = True, allow_continue = False) from _call_get_fucked_VT_cum_fetish_non_employee_dosage_request
            the_person "Oh my god, thank you [the_person.mc_title]... I wish I had time to make you cum again... but I know you're a busy man..."
            "[the_person.possessive_title!c] starts to get up. Her hunger for cum satisfied for now."
            $ the_person.draw_person(emotion = "happy")
            the_person "Thanks again, [the_person.mc_title]. Don't hesitate to give me a call when you... you know... need my service."
            $ the_person.draw_person(position = "walking_away")
            "She gives you a smile and a wink, turns around and walks out of the door."
        "Sorry":
            mc.name "I'm sorry, I don't have time right now."
            "[the_person.possessive_title!c] is caught completely off guard by your refusal."
            $ the_person.change_stats(happiness = -5, obedience = -5)
            #$ the_person.set_event_day("LastCumFetish")
            $ VT_fetish_timer_reset(the_person, "cum", 1, False)
            the_person "Oh!... Okay... Well... hey I understand... Maybe another time?"
            "You hang up your phone and continue with your day."

    $ clear_scene()
    $ the_person.apply_planned_outfit()
    return
