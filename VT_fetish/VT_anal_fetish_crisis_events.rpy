
label VT_aggressive_anal_fetish_employee_label():
    $ the_person = VT_get_needy_anal_fetish_employee()
    if the_person is None:
        return

    $ mc.start_text_convo(the_person)
    the_person "Hey, I really need your help with something. Can you meet me in your office really quick?"
    mc.name "Sure, I'll meet you there in five."
    $ mc.end_text_convo()
    $ mc.change_location(ceo_office)
    "You step into your office. [the_person.possessive_title!c] isn't there yet so you sit down at your desk."
    $ the_person.draw_person()
    "In a minute, you see her step into your office, close the door and lock it."
    mc.name "Ah, hello [the_person.title]. Is there something I..."
    "She interrupts you."
    the_person "Yes, there's something I need very much right now."
    "You stand up and start to walk around your desk. She wraps her arms around you."
    $ mc.change_locked_clarity(20)
    $ the_person.draw_person(position = "kissing")
    if the_person.obedience < 100:
        the_person "I don't know how long it's been since you've been in my ass, but it's been too long!"
        "She pushes you back onto the desk."
        if the_person.vagina_available:
            the_person "Don't worry, I'll take care of everything, you just lay back."
        else:
            "As you lay back on the desk, she starts to strip."
            $ the_person.strip_outfit(exclude_upper = True)
            the_person "There we go. Don't worry, I'll take care of everything, you just lay back."
        call get_fucked(the_person,  private= True, start_position = anal_cowgirl) from _call_get_fucked_VT_aggressive_anal_fetish_employee_1
    else:
        "She looks up at you and bats her eyelashes."
        the_person "I... I just really need you in my ass. I don't know how longs it's been, but it's been too long!"
        the_person "Please? I'll take care of everything, all you have to do is lay back."
        $ mc.change_locked_clarity(50)
        menu:
            "Let her":
                "Your influences resulted in her anal fetish in the first place, so you feel a little obliged to let her work her fetish out."
                mc.name "Go ahead."
                the_person "Oh thank god! Don't worry, I'll take care of everything."
                "She pushes you back on to your desk."
                if not the_person.vagina_available:
                    "As you lay back on the desk, she starts to strip."
                    $ the_person.strip_outfit(exclude_upper = True)
                call get_fucked(the_person,  private= True, start_position = anal_cowgirl) from _call_get_fucked_VT_aggressive_anal_fetish_employee_2
            "Too busy":
                "You chastise her for being so aggressive."
                mc.name "I know the cravings are strong, but I have a lot to get done today. Get back to work, I'll try to relieve your urges later."
                $ the_person.draw_person(emotion = "sad")
                the_person "But sir..."
                mc.name "I have spoken."
                $ the_person.change_stats(happiness = -10, obedience = 10, love = -5)
                #$ the_person.set_event_day("LastAnalFetish")
                $ VT_fetish_timer_reset(the_person, "anal", 1, False)
                "[the_person.possessive_title!c] backs away and quietly leaves your office. You feel a bit bad for chastising her, but that bitch should know better."
                return
    if the_person.outfit.has_creampie_cum:
        the_person "Mmmm, your cum feels good in my ass..."
    "[the_person.title] gets up."
    $ the_person.draw_person()
    the_person "I feel like I can think clearly again... thank you, I {i}really{/i} needed that."
    $ the_person.review_outfit()
    $ the_person.draw_person()
    "[the_person.possessive_title!c] cleans herself up a bit. You both leave your office and get back to work."
    return

label VT_aggressive_anal_fetish_non_employee_label():
    $ the_person = VT_get_needy_anal_fetish_non_employee()
    if the_person is None:
        return

    "While going about your day, your phone suddenly rings."

    the_person "Hello, [the_person.mc_title]? Do you have a minute?"
    mc.name "Oh, hey [the_person.title], it's you. Sure, what's up?"
    the_person "Could we meet up, right now? I have a little problem, that I need you to solve."
    mc.name "What kind of problem?"
    the_person "Well, eh, I'm desperately in need of a rectal massage."

    "It seems she is desperate for you to satisfy her anal fetish, what will you do?"
    $ mc.change_locked_clarity(20)

    menu:
        "All right":
            mc.name "All right, meet me at my place in 10 minutes."
            $ mc.change_location(hall)
            "You just got home, when your doorbell rings."

            $ the_person.draw_person()
            the_person "Hey [the_person.mc_title], I came as fast as I could."

            "[the_person.possessive_title!c] pushes you inside and immediately takes some of her clothes off."
            $ the_person.strip_outfit(exclude_upper = True)
            $ the_person.draw_person(position = "standing_doggy")
            "[the_person.possessive_title!c] bends over in front of you, with her hands on the cupboard beside the door."
            "You can see she is still wearing her princess butt plug, that seems to have become a part of her daily outfit."
            "You slowly pull out the pink jewelled butt plug from [the_person.possessive_title]'s rectum. She quivers in anticipation of what you are about to do to her."
            $ the_person.change_arousal(the_person.opinion.anal_sex)
            $ mc.change_locked_clarity(50)
            the_person "Oh my god, I need you in my ass right now... shove your big cock up my fucking ass right now!"
            $ the_person.break_taboo("anal_sex")
            "You drop your pants, take out your already hard cock and you shove it right up her greedy butt hole, eliciting a satisfying grunt from [the_person.possessive_title]."

            call fuck_person(the_person, start_position = anal_standing, start_object = make_desk(), skip_intro = True, skip_condom = True) from _call_fuck_person_VT_aggressive_anal_fetish_non_employee

            the_person "That was so good. I've been thinking about that all day."
            "[the_person.possessive_title!c] gets her butt plug and slowly pushes it back into her ass."
            $ the_person.apply_planned_outfit(show_dress_sequence = True)
            $ the_person.draw_person(emotion = "happy")
            the_person "Thanks again, [the_person.mc_title]. We should do this again... and soon."
            $ the_person.draw_person(position = "walking_away")
            "And just like that she turns around and is gone out of the door."

        "Sorry":
            mc.name "I'm sorry, I don't have time right now."
            "[the_person.possessive_title!c] is caught completely off guard by your refusal."
            $ the_person.change_stats(happiness = -5, obedience = -5)
            #$ the_person.set_event_day("LastAnalFetish")
            $ VT_fetish_timer_reset(the_person, "anal", 2, False)
            the_person "Oh!... Okay... Well... hey I understand... Maybe another time?"
            "You hang up your phone and continue with your day."

    $ clear_scene()
    return

label VT_anal_fetish_employee_evening_approach_label():
    $ the_person = VT_get_needy_anal_fetish_employee()

    if the_person is None:
        $ the_person = VT_get_anal_fetish_employee()
        if the_person is None:
            return
    "As you are packing up your stuff to head home for the day, you hear [the_person.possessive_title]'s sweet voice call out to you."

    if mc.business.is_work_day:
        $ the_person.draw_person()
        the_person "Hey, [the_person.mc_title]. Just wondering if... you know... you wanna stick around for a bit after work today?"
        "She flashes you a quick smile. You wonder if she has in that butt plug she showed you last time you stayed late at the office with her..."
        $ mc.change_locked_clarity(20)
        mc.name "Sure, I can probably stick around for a little bit. Just give me a few minutes."
        the_person "Oh! Thanks, [the_person.mc_title], I'll meet you in your office in a few minutes! You won't regret this!"
        $ the_person.draw_person(position = "walking_away")
        "You finish up what you were doing and say goodbye to your employees and head to your office."
        $ clear_scene()
        $ mc.change_location(ceo_office)
        "Your curiosity about what [the_person.possessive_title] needs is answered when she steps into your office."
        $ set_special_fetish_outfit(the_person)
        $ the_person.outfit.remove_panties()
        $ the_person.draw_person()
        "[the_person.possessive_title!c] has changed into some sexy lingerie. You notice as she walks up that she isn't wearing any panties..."
        "She walks up and stands next to you by your desk. Then she turns around."
        $ the_person.draw_person(position = "back_peek")
        "Between her pillowy cheeks is her pink jewelled butt plug."
        the_person "What do you say, [the_person.mc_title]? Want to replace my plug with something else?"
        $ mc.change_locked_clarity(50)
    else:
        $ set_special_fetish_outfit(the_person)
        $ the_person.draw_person()
        the_person "Hey, [the_person.mc_title]. I was wondering if you would be here on the weekend! Want to have some fun before you head home?"
        "[the_person.possessive_title!c] is dressed to impress. You wonder if she has in that butt plug she showed you last time you stayed late at the office with her..."
        "As if sensing your thoughts, [the_person.possessive_title] turns around."
        $ the_person.draw_person(position = "back_peek")
        "Between her pillowy cheeks is her pink jewelled butt plug."
        the_person "What do you say, [the_person.mc_title]? Want to replace my plug with something else?"
        $ mc.change_locked_clarity(50)
    menu:
        "Fuck her ass":
            the_person "Mmmm, I can't wait to feel it."
            $ the_person.draw_person(position = "standing_doggy")
            "[the_person.possessive_title!c] walks over in front of you, with her hands on your desk."
            ###Anal Scene, standing variant###
            "You slowly pull out the pink jewelled butt plug from [the_person.possessive_title]'s rectum. She quivers in anticipation of what you are about to do to her."
            $ the_person.change_arousal(the_person.opinion.anal_sex)
            "You work a couple fingers into her bottom. It is clear she loves anal sex so much, she keeps herself lubed up with the plug in throughout the day hoping for you to come fuck it."
            "You decide to tease her before you put it in."
            mc.name "You're such a buttslut, [the_person.title]. Are you sure you want it back there? Your pussy looks like it could use a proper fucking too..."
            "[the_person.possessive_title!c] tries to push back against you and begins to beg."
            the_person "No! I need you in my ass right now... I need the heat and intensity of you fucking my ass right now!"
            $ mc.change_locked_clarity(50)
            $ the_person.break_taboo("anal_sex")
            "When you're ready you push forward. Her back passage greedily accepts your erection, eliciting a satisfied sigh from [the_person.possessive_title]."
            call fuck_person(the_person, start_position = anal_standing, start_object = make_desk(), skip_intro = True, skip_condom = True) from _call_fuck_person_VT_anal_fetish_employee_evening_approach

            $ the_person.draw_person(emotion = "happy")
            the_person "It was so good. I've been thinking about that all day."
            "[the_person.possessive_title!c] gets her butt plug and slowly pushes it back into her ass."
            the_person "Thanks again, [the_person.mc_title]. We should do this again... and soon."
            $ the_person.draw_person("walking_away")
            "You wave goodbye to [the_person.possessive_title] and get ready to head home for the night."
        "No Thanks":
            "[the_person.possessive_title!c] is caught completely off guard by your refusal."
            $ the_person.change_stats(happiness = -10, obedience = -10)
            #$ the_person.set_event_day("LastAnalFetish")
            $ VT_fetish_timer_reset(the_person, "anal", 2, False)
            the_person "Oh!... Okay... Well... hey I understand... Maybe some other time yeah?"
            "[the_person.possessive_title!c] quickly sulks off. Maybe you should've?"
        "Too Tired" if mc.energy < 30:
            "[the_person.possessive_title!c] is surprised by your answer."
            $ the_person.change_stats(happiness = -5, obedience = -5)
            #$ the_person.set_event_day("LastAnalFetish")
            $ VT_fetish_timer_reset(the_person, "anal", False)
            the_person "Oh! I'm sorry... I know you work so hard around here. Maybe tomorrow then?"
            "[the_person.possessive_title!c] quickly sulks off."

    $ the_person.apply_planned_outfit()
    $ clear_scene()
    return
