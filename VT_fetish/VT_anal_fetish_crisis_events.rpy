
label VT_aggressive_anal_fetish_employee_label():
    $ the_person = VT_get_needy_anal_fetish_employee()
    if the_person is None:
        return

    $ mc.start_text_convo(the_person)
    the_person "I'm desperate for your attention. Can you meet me in your office ASAP?"
    mc.name "I'll be there in five. Try to calm down."
    $ mc.end_text_convo()
    $ mc.change_location(ceo_office)
    "You enter your office, but [the_person.possessive_title!c] isn't there yet. You take a seat behind your desk, anticipating her arrival."
    $ the_person.draw_person()
    "Moments later, she bursts into your office, slamming the door shut behind her and locking it."
    mc.name "Ah, [the_person.title]. What's going on?"
    "She strides over to you, her eyes blazing with desire."
    the_person "I need you inside me, now."
    "You rise from your seat, and she wraps her arms around you, pulling you close."
    $ mc.change_locked_clarity(20)
    $ the_person.draw_person(position = "kissing")
    if the_person.obedience < 100:
        the_person "It's been far too long since you've claimed my ass. I'm aching for it."
        "She shoves you back onto the desk, her hands already working to undo your pants."
        if the_person.vagina_available:
            the_person "Don't worry, I'll take care of everything. Just lay back and enjoy the ride."
        else:
            "As you lay back on the desk, she begins to strip, her clothes flying off in a frenzy."
            $ the_person.strip_outfit(exclude_upper = True)
            the_person "There, that's better. Now, just relax and let me take care of you."
        call get_fucked(the_person,  private= True, start_position = anal_cowgirl) from _call_get_fucked_VT_aggressive_anal_fetish_employee_1
    else:
        "She gazes up at you, her eyelashes batting coquettishly."
        the_person "I... I just really need you in my ass. It's been too long, and I'm going crazy."
        the_person "Please? I'll take care of everything. Just lay back and let me do the work."
        $ mc.change_locked_clarity(50)
        menu:
            "Let her":
                "You feel a pang of responsibility for her anal fetish, so you decide to indulge her."
                mc.name "Go ahead. Take what you need."
                the_person "Oh, thank you! I'll make sure you enjoy it too."
                "She pushes you back onto the desk, her hands already working to undo your pants."
                if not the_person.vagina_available:
                    "As you lay back on the desk, she begins to strip, her clothes flying off in a frenzy."
                    $ the_person.strip_outfit(exclude_upper = True)
                call get_fucked(the_person,  private= True, start_position = anal_cowgirl) from _call_get_fucked_VT_aggressive_anal_fetish_employee_2
            "Too busy":
                "You reprimand her for her aggressive behavior."
                mc.name "I know you're craving it, but I have a lot on my plate today. Get back to work, and I'll try to satisfy your urges later."
                $ the_person.draw_person(emotion = "sad")
                the_person "But sir..."
                mc.name "I've spoken. Don't make me repeat myself."
                $ the_person.change_stats(happiness = -10, obedience = 10, love = -5)
                #$ the_person.set_event_day("LastAnalFetish")
                $ VT_fetish_timer_reset(the_person, "anal", 1, False)
                "[the_person.possessive_title!c] backs away, looking crestfallen, and quietly exits your office. You feel a twinge of guilt for chastising her, but she should know better than to be so forward."
                return
    if the_person.outfit.has_creampie_cum:
        the_person "Mmmm, your cum feels amazing in my ass... I can feel it dripping out of me."
    "[the_person.title] rises from the desk, a satisfied smile spreading across her face."
    $ the_person.draw_person()
    the_person "I feel like I can think clearly again... thank you, I really needed that. You have no idea how much I {i}appreciate{/i} it."
    $ the_person.review_outfit()
    $ the_person.draw_person()
    "[the_person.possessive_title!c] takes a moment to clean herself up, smoothing out her clothes and composing herself. You both exit your office, returning to your respective duties."
    return

label VT_aggressive_anal_fetish_non_employee_label():
    $ the_person = VT_get_needy_anal_fetish_non_employee()
    if the_person is None:
        return

    "Your phone rings, shrill in the silence. You answer, and [the_person.title]'s voice is on the other end, husky with desire."
    the_person "Hey, [the_person.mc_title]. I need to see you. Now."
    mc.name "What's going on? You sound... urgent."
    the_person "I am. I need you to take care of something for me. Something only you can do."
    mc.name "What is it?"
    the_person "I need a rectal massage. Badly. I've been thinking about it all day, and I just can't take it anymore."
    "It's clear she's desperate for you to satisfy her anal fetish. What do you do?"
    $ mc.change_locked_clarity(20)

    menu:
        "All right":
            mc.name "Okay, meet me at my place in 10 minutes. And come ready."
            $ mc.change_location(hall)
            "You've barely got the door open when [the_person.possessive_title!c] pushes her way inside, already stripping off her clothes."
            $ the_person.strip_outfit(exclude_upper = True)
            $ the_person.draw_person(position = "standing_doggy")
            "[the_person.possessive_title!c] bends over in front of you, her hands grasping the cupboard beside the door for support."
            "You notice she's still wearing her princess butt plug, a constant companion in her daily life."
            "You slowly extract the pink jewelled butt plug from [the_person.possessive_title]'s rectum, and she shudders in anticipation of what's to come."
            $ the_person.change_arousal(the_person.opinion.anal_sex)
            $ mc.change_locked_clarity(50)
            the_person "Oh god, please... I need you inside me now. Shove your cock up my ass and make me scream."
            $ the_person.break_taboo("anal_sex")
            "You drop your pants, freeing your already-hard cock, and shove it deep into her eager butt hole, eliciting a guttural grunt from [the_person.possessive_title]."

            call fuck_person(the_person, start_position = anal_standing, start_object = make_desk(), skip_intro = True, skip_condom = True) from _call_fuck_person_VT_aggressive_anal_fetish_non_employee

            the_person "That was incredible. I've been fantasizing about that all day."
            "[the_person.possessive_title!c] retrieves her butt plug and slowly inserts it back into her ass, a look of satisfaction on her face."
            $ the_person.apply_planned_outfit(show_dress_sequence = True)
            $ the_person.draw_person(emotion = "happy")
            the_person "Thanks again, [the_person.mc_title]. We should do this again soon. Very soon."
            $ the_person.draw_person(position = "walking_away")
            "And with that, she turns on her heel and disappears out the door, leaving you to wonder what just hit you."

        "Sorry":
            mc.name "I'm sorry, I don't have time right now. Maybe another time?"
            "[the_person.possessive_title!c] is taken aback by your refusal, her voice tinged with disappointment."
            $ the_person.change_stats(happiness = -5, obedience = -5)
            #$ the_person.set_event_day("LastAnalFetish")
            $ VT_fetish_timer_reset(the_person, "anal", 2, False)
            the_person "Oh... okay. I understand, I guess. Maybe another time, then?"
            "You hang up the phone, feeling a twinge of guilt for rebuffing her advances."

    $ clear_scene()
    return

label VT_anal_fetish_employee_evening_approach_label():
    $ the_person = VT_get_needy_anal_fetish_employee()

    if the_person is None:
        $ the_person = VT_get_anal_fetish_employee()
        if the_person is None:
            return
    "As you're wrapping up your work for the day, you hear [the_person.possessive_title]'s sultry voice calling out to you."

    if mc.business.is_work_day:
        $ the_person.draw_person()
        the_person "Hey, [the_person.mc_title]. Want to stick around for a bit after work today? I have a little something in mind..."
        "She flashes you a flirtatious smile, and you can't help but wonder if she's wearing that butt plug she showed you last time you stayed late at the office..."
        $ mc.change_locked_clarity(20)
        mc.name "Sure, I can probably stick around for a little bit. Just give me a few minutes to wrap things up."
        the_person "Oh, thanks, [the_person.mc_title]! I'll meet you in your office in a few minutes. You won't regret this, I promise!"
        $ the_person.draw_person(position = "walking_away")
        "You finish up what you were doing and say goodbye to your employees, then head to your office to see what [the_person.possessive_title] has in store for you."
        $ clear_scene()
        $ mc.change_location(ceo_office)
        "Your curiosity is piqued when [the_person.possessive_title] steps into your office, looking like a vision in her sexy lingerie."
        $ set_special_fetish_outfit(the_person)
        $ the_person.outfit.remove_panties()
        $ the_person.draw_person()
        "[the_person.possessive_title!c] has changed into something truly stunning. You notice as she walks up that she's not wearing any panties..."
        "She walks up and stands next to you by your desk, then turns around to show off her assets."
        $ the_person.draw_person(position = "back_peek")
        "Between her pillowy cheeks is her pink jewelled butt plug, glinting in the light."
        the_person "What do you say, [the_person.mc_title]? Want to replace my plug with something a little more... substantial?"
        $ mc.change_locked_clarity(50)
    else:
        $ set_special_fetish_outfit(the_person)
        $ the_person.draw_person()
        the_person "Hey, [the_person.mc_title]. I was hoping to catch you here on the weekend. Want to have a little fun before you head home?"
        "[the_person.possessive_title!c] is dressed to impress, and you can't help but wonder if she's wearing that butt plug she showed you last time you stayed late at the office..."
        "As if sensing your thoughts, [the_person.possessive_title] turns around to show off her assets."
        $ the_person.draw_person(position = "back_peek")
        "Between her pillowy cheeks is her pink jewelled butt plug, glinting in the light."
        the_person "What do you say, [the_person.mc_title]? Want to replace my plug with something a little more... substantial?"
        $ mc.change_locked_clarity(50)
    menu:
        "Fuck her ass":
            the_person "Mmmm, I've been waiting all day for this."
            $ the_person.draw_person(position = "standing_doggy")
            "[the_person.possessive_title!c] walks over in front of you, her hands grasping your desk for support."
            ###Anal Scene, standing variant###
            "You slowly extract the pink jewelled butt plug from [the_person.possessive_title]'s rectum, and she shudders in anticipation of what's to come."
            $ the_person.change_arousal(the_person.opinion.anal_sex)
            "You work a couple fingers into her bottom, and it's clear she loves anal sex so much, she keeps herself lubed up with the plug in throughout the day, hoping for you to come and fuck her."
            "You decide to tease her a bit before you put it in."
            mc.name "You're such a dirty girl, [the_person.title]. Are you sure you want it back there? Your pussy looks like it could use a proper fucking too..."
            "[the_person.possessive_title!c] tries to push back against you, begging for more."
            the_person "No, please! I need you in my ass right now... I need the heat and intensity of you fucking my ass right now!"
            $ mc.change_locked_clarity(50)
            $ the_person.break_taboo("anal_sex")
            "When you're ready, you push forward, and her back passage greedily accepts your erection, eliciting a satisfied sigh from [the_person.possessive_title]."
            call fuck_person(the_person, start_position = anal_standing, start_object = make_desk(), skip_intro = True, skip_condom = True) from _call_fuck_person_VT_anal_fetish_employee_evening_approach

            $ the_person.draw_person(emotion = "happy")
            the_person "That was amazing. I've been thinking about that all day."
            "[the_person.possessive_title!c] retrieves her butt plug and slowly inserts it back into her ass, a look of satisfaction on her face."
            the_person "Thanks again, [the_person.mc_title]. We should do this again... and soon."
            $ the_person.draw_person("walking_away")
            "You wave goodbye to [the_person.possessive_title] and get ready to head home for the night, feeling a sense of satisfaction."
        "No Thanks":
            "[the_person.possessive_title!c] looks crestfallen at your refusal."
            $ the_person.change_stats(happiness = -10, obedience = -10)
            #$ the_person.set_event_day("LastAnalFetish")
            $ VT_fetish_timer_reset(the_person, "anal", 2, False)
            the_person "Oh... okay. Well, I guess I'll just have to wait for another time, then."
            "[the_person.possessive_title!c] quickly sulks off, looking disappointed."
        "Too Tired" if mc.energy < 30:
            "[the_person.possessive_title!c] looks surprised by your answer."
            $ the_person.change_stats(happiness = -5, obedience = -5)
            #$ the_person.set_event_day("LastAnalFetish")
            $ VT_fetish_timer_reset(the_person, "anal", False)
            the_person "Oh, I'm sorry... I know you work hard. Maybe tomorrow, then?"
            "[the_person.possessive_title!c] quickly sulks off, looking a bit disappointed."

    $ the_person.apply_planned_outfit()
    $ clear_scene()
    return
