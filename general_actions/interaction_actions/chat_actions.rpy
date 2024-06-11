label person_introduction(the_person, girl_introduction = True):
    if girl_introduction:
        if the_person.is_at_job(prostitute_job):
            call prostitute_introduction(the_person) from _call_prostitute_introduction_person_introduction
        else:
            $ the_person.call_dialogue("introduction")

    #She's given us her name, now she asks for yours.
    $ title_choice = renpy.display_menu(build_person_introduction_titles(the_person), True, "Choice")
    mc.name "[title_choice], it's a pleasure to meet you."
    $ the_person.set_mc_title(title_choice)
    return

label person_new_title(the_person): #She wants a new title or to give you a new title.
    if builtins.len(the_person.get_titles()) <= 1: #There's only the one title available to them. Don't bother asking to change
        return

    $ the_person.draw_person() # make her display in default pose (she might be doing something else when you start dialogue)
    $ ran_num = the_person.obedience + renpy.random.randint(-20, 20) #Randomize their effective obedience a little so they sometimes ask, sometimes demand

    if ran_num > 120: #She just asks you for something "fresh". Her obedience is high enough that we already have control over this.
        the_person "[the_person.mc_title], do you think [the_person.title] is getting a little old? I think something new might be fun!"
        menu:
            "Change what you call her":
                $ title_choice = new_title_menu(the_person)
                if not (title_choice == "Back" or the_person.create_formatted_title(title_choice) == the_person.title):
                    mc.name "I think [title_choice] would really suit you."
                    $ the_person.set_title(title_choice)
                    "[the_person.title] seems happy with her new title."
                else:
                    mc.name "On second thought, I think [the_person.title] suits you just fine."
                    the_person "If you think so [the_person.mc_title]."

            "Don't change her title":
                mc.name "I think [the_person.title] suits you just fine."
                the_person "If you think so [the_person.mc_title]."

    elif ran_num > 95: #She picks a couple of choices and asks you to decide.
        $ (title_one, title_two) = get_two_titles_for_person(the_person.get_titles)
        if the_person.title == the_person.create_formatted_title(title_one) or the_person.title == the_person.create_formatted_title(title_two):  #If we picked the one we're currently using we have a slightly different dialogue setup.
            if the_person.title == the_person.create_formatted_title(title_two):
                $ placeholder = title_two #Swap them around so title_one is always the current title she has
                $ title_two = title_one
                $ title_one = placeholder
                $ placeholder = None
            $ formatted_title_one = the_person.title
            $ formatted_title_two = the_person.create_formatted_title(title_two)
            the_person "Hey [the_person.mc_title], do you like calling me [formatted_title_one] or do you think [formatted_title_two] sounds better?"
            menu:
                "Keep calling her [formatted_title_one]":
                    mc.name "I think [the_person.title] suits you perfectly, you should keep using it."
                    "She nods in agreement."
                    the_person "Yeah, I think you're right."
                "Change her title to [formatted_title_two]":
                    mc.name "[formatted_title_two] does have a nice ring to it. You should start using that."
                    $ the_person.set_title(title_two)
                    the_person "I think you're right. Thanks for the input!"
        else: #Both are new!
            $ formatted_title_one = the_person.create_formatted_title(title_one)
            $ formatted_title_two = the_person.create_formatted_title(title_two)
            the_person "So [the_person.mc_title], I'm thinking of changing things up a bit. Do you think [formatted_title_one] or [formatted_title_two] sounds best?"
            menu:
                "Change her title to [formatted_title_one]":
                    mc.name "I think [formatted_title_one] is the best of the two."
                    $ the_person.set_title(title_one)
                    the_person "Yeah, I think you're right. I'm going to have people call me that from now on."

                "Change her title to [formatted_title_two]":
                    mc.name "I think [formatted_title_two] is the best of the two."
                    $ the_person.set_title(title_two)
                    the_person "Yeah, I think you're right. I'm going to have people call me that from now on."

                "Refuse to change her title\n{menu_red}-5 Happiness{/menu_red}":
                    mc.name "I don't think either of those sound better than [the_person.title]. You should really just stick with that."
                    "[the_person.title] rolls her eyes."
                    $ the_person.change_happiness(-5)
                    the_person "Well that isn't very helpful [the_person.mc_title]. Fine, I guess [the_person.title] will do."

        $ formatted_title_one = None
        $ formatted_title_two = None
        $ title_one = None
        $ title_two = None
    else: #She doesn't listen to you, so she just picks one and demands that you use it, or becomes unhappy.
        $ new_title = get_random_from_list(the_person.get_titles())
        python:
            while the_person.create_formatted_title(new_title) == the_person.title:
                new_title = get_random_from_list(the_person.get_titles())

        $ formatted_new_title = the_person.create_formatted_title(new_title)
        the_person "By the way [the_person.mc_title], I want you to start referring to me as [formatted_new_title] from now on. I think it suits me better."
        menu:
            "Change her title to [formatted_new_title]":
                mc.name "I think you're right, [formatted_new_title] sounds good."
                $ the_person.set_title(new_title)

            "Refuse to change her title\n{menu_red}-10 Happiness{/menu_red}":
                mc.name "I think that sounds silly, I'm just going to keep calling you [the_person.title]."
                "[the_person.title] scoffs and rolls her eyes."
                $ the_person.change_happiness(-10)
                the_person "Whatever. It's not like I can force you to do anything."

        $ new_title = None
        $ formatted_new_title = None
    return

label person_new_mc_title(the_person):
    if builtins.len(the_person.get_player_titles()) <= 1: #There's only the one title available to them. Don't bother asking to change
        return
    $ ran_num = the_person.obedience + renpy.random.randint(-20, 20)
    if ran_num > 120: #She just asks you for something "fresh". Her obedience is high enough that we already have control over this.
        the_person "I was just thinking that I've called you [the_person.mc_title] for a pretty long time. If you're getting tired of it I could call you something else."
        menu:
            "Change what she calls you":
                $ title_choice = new_mc_title_menu(the_person)
                if not (title_choice == "Back" or title_choice == the_person.mc_title):
                    mc.name "I think you should call me [title_choice] from now on."
                    $ the_person.set_mc_title(title_choice)
                    "[the_person.title] seems happy with your new title."
                else:
                    mc.name "On second thought, I think [the_person.mc_title] is fine for now."
                    the_person "If you think so [the_person.mc_title]."

            "Don't change her title for you":
                mc.name "I think [the_person.mc_title] is fine for now."
                the_person "Okay, if you say so!"

    elif ran_num > 95: #She picks a couple of choices and asks you to decide.
        $ (title_one, title_two) = get_two_titles_for_person(the_person.get_player_titles)
        if the_person.mc_title == title_one or the_person.mc_title == title_two:  #If we picked the one we're currently using we have a slightly different dialogue setup.
            if the_person.mc_title == title_two:
                $ placeholder = title_two #Swap them around so title_one is always the current title she has
                $ title_two = title_one
                $ title_one = placeholder
                $ placeholder = None

            the_person "Hey [the_person.mc_title], would you rather I called you [title_two]?"
            menu:
                "Have her keep calling you [title_one]":
                    mc.name "I think I like [title_one], but thanks for asking."
                    "She shrugs."
                    the_person "Sure, whatever you like [the_person.mc_title]."
                "Have her call you [title_two] instead":
                    mc.name "[title_two] does have a nice ring to it. You should start using that."
                    $ the_person.set_mc_title(title_two)
                    the_person "Alright, you got it [the_person.mc_title]!"

        else: #Both are new!
            the_person "You know, I really think [title_one] or [title_two] would fit you a lot better than [the_person.mc_title]. Which one do you think is better?"
            menu:
                "Have her call you [title_one]":
                    mc.name "I think [title_one] is the best of the two."
                    $ the_person.set_mc_title(title_one)
                    the_person "Yeah, you're right. I think I'll start calling you that from now on."

                "Have her call you [title_two]":
                    mc.name "I think [title_two] is the best of the two."
                    $ the_person.set_mc_title(title_two)
                    the_person "Yeah, you're right. I think I'll start calling you that from now on."

                "Refuse to change your title\n{menu_red}-5 Happiness{/menu_red}":
                    mc.name "I don't think either of those sound better than [the_person.mc_title]. Let's stick with that for now."
                    "[the_person.title] rolls her eyes."
                    $ the_person.change_happiness(-5)
                    the_person "Fine, if you don't like change I can't make you."
        $ title_one = None
        $ title_two = None
    else: #She doesn't listen to you, so she just picks one and demands that you use it, or becomes unhappy.
        $ new_title = get_random_from_list(the_person.get_player_titles())
        python:
            while new_title == the_person.mc_title:
                new_title = get_random_from_list(the_person.get_player_titles())

        the_person "You know, I think [new_title] fits you better than [the_person.mc_title]. I'm going to start using that."
        menu:
            "Let her call you [new_title]":
                mc.name "Alright, if you think that's better."
                $ the_person.set_mc_title(new_title)

            "Demand she keeps calling you [the_person.mc_title]\n{menu_red}-10 Happiness{/menu_red}":
                mc.name "I think that sounds silly, I want you to keep calling me [the_person.mc_title]."
                "[the_person.title] scoffs and rolls her eyes."
                $ the_person.change_happiness(-10)
                the_person "Whatever. If it's so important to you then I guess I'll just do it."
        $ new_title = None
    return

label small_talk_person(the_person, apply_energy_cost = True, is_phone = False): #Tier 0. Useful for discovering a character's opinions and the first step to building up love.
    python:
        if apply_energy_cost:
            mc.change_energy(-15)
        the_person.event_triggers_dict["chatted"] = the_person.event_triggers_dict.get("chatted", 0) - 1
        day_part = time_of_day_string()
        name = renpy.random.choice([the_person.title, the_person.fname])
        renpy.say(mc.name, renpy.random.choice([
            "So [name], what's been on your mind recently?",
            "Hey [name], how are you today?",
            "Good [day_part] [name], anything new?",
            "Good [day_part] [name], it's a beautiful day, isn't it?",
            "Hello [name], what are you up to this [day_part]?"
        ]))
        the_person.discover_opinion("small talk")

    # TODO: Add a chance that she wants to talk about someone she knows.
    if not is_phone and the_person.love > 5 and the_person.primary_job and not the_person.primary_job.job_known:
        if the_person.has_job(unemployed_job):
            the_person "Well, it's hard to make ends meet, but I'll figure it out."
            "She tells you that it is not easy when you have no job."
        elif the_person.is_unique:
            "You chit chat for a while, about life, aspirations and dreams."
        else:
            $ ran_num = renpy.random.randint(0, 1)
            if ran_num == 0:
                the_person "Just having some issues at work, but nothing I can't handle."
            else:
                the_person "Being a [the_person.primary_job.job_title] is not easy, but I love my job."
            "She tells you about her job and its challenges."
        $ the_person.primary_job.job_known = True
    elif not is_phone and the_person.love > 20 and the_person.current_job and not the_person.current_job.job_known:
        $ ran_num = renpy.random.randint(0, 1)
        if the_person.current_job.job_definition == prostitute_job:
            the_person "It's nice to see you, I do like this job, but sometimes it's not so great."
        elif the_person.current_job != the_person.primary_job:
            the_person "Sometimes you got to put in the extra effort to make ends meet."
        elif ran_num == 0:
            the_person "Just having some issues at work, but nothing I can't handle."
        else:
            the_person "Sometimes making a dollar is quite challenging, but I do like my job."
        "She tells you about her job and its challenges."
        $ the_person.current_job.job_known = True
    elif renpy.random.randint(0,100) < 60 + (the_person.opinion.small_talk * 20) + (mc.charisma * 5):
        if is_phone:
            "There's a short pause, then [the_person.title] texts you back."
        else:
            if the_person.opinion.small_talk >= 0:
                "She seems glad to have a chance to take a break and make small talk with you."
            else:
                "She seems uncomfortable with making small talk, but after a little work you manage to get her talking."

        $ (opinion_learned, talk_opinion_text) = get_learned_opinion(the_person)
        if not opinion_learned is None:
            $ opinion_state = the_person.get_opinion_topic(opinion_learned)
            $ opinion_string = opinion_score_to_string(opinion_state[0])
            $ the_person.event_triggers_dict["last_opinion_learned"] = opinion_learned

            if is_phone:
                the_person "Oh, this and that."
                "The two of you text back and forth between each other for half an hour." #TODO: Either play out that conversation or add some message history to fill it in.
            else:
                "The two of you chat pleasantly for half an hour."

            the_person "So [the_person.mc_title], I'm curious what you think about [talk_opinion_text]. Do you have any opinions on it?"

            call screen main_choice_display(build_menu_items([build_opinion_smalltalk_list(talk_opinion_text, opinion_state)]))

            if is_phone:
                $ mc_opinion_string = opinion_score_to_string(_return).rstrip('s').replace('has', 'have')
                mc.name "I [mc_opinion_string] [talk_opinion_text]."

            $ prediction_difference = builtins.abs(_return - opinion_state[0])
            if prediction_difference == 4: #as wrong as possible
                the_person "Really? Wow, we really don't agree about [opinion_learned], that's for sure."
            elif prediction_difference == 3:
                the_person "You really think so? Huh, I guess we'll just have to agree to disagree."
            elif prediction_difference == 2:
                the_person "I guess I could understand that."
            elif prediction_difference == 1:
                the_person "Yeah, I'm glad you get it. I feel like we're both on the same wavelength."
            else: #prediction_difference == 0
                the_person "Exactly! It's so rare that someone feels exactly the same way about [opinion_learned] as me!"

            if opinion_state[1]:
                if is_phone:
                    "[the_person.possessive_title!c] sends you a bunch of texts about how she [opinion_string] [opinion_learned]."
                else:
                    "You listen while [the_person.possessive_title] talks about how she [opinion_string] [opinion_learned]."
            else:
                $ the_person.discover_opinion(opinion_learned)
                if is_phone:
                    "[the_person.possessive_title!c] sends you a bunch of texts, and you learn that she [opinion_string] [opinion_learned]."
                else:
                    "You listen while [the_person.possessive_title] talks and discover that she [opinion_string] [opinion_learned]."

            $ the_person.change_stats(happiness = the_person.opinion.small_talk + 1,
                love = 3 - prediction_difference, max_love = 35,
                obedience = 1 if not is_phone and mc_serum_aura_obedience.is_active else 0,
                arousal = 1 if not is_phone and mc_serum_aura_arousal.is_active else 0)

        else:
            if is_phone:
                the_person "Oh, this and that. What about you?"
                "You and [the_person.possessive_title] text back and forth for a while. You've had a fun conversation, but you don't think you've learned anything new."
            else:
                "You and [the_person.possessive_title] chat for a while. You don't feel like you've learned much about her, but you both enjoyed talking."

            $ the_person.change_happiness(the_person.opinion.small_talk)

        if the_person.love > 20 and the_person.has_role(instapic_role) and not the_person.event_triggers_dict.get("insta_known", False):
            $ the_person.event_triggers_dict["insta_known"] = True
            the_person "Hey, are you on InstaPic? You should follow me on there, so you can see what I'm up to."
            if is_phone:
                "She texts you her InstaPic profile name. You'll be able to look up her profile now."
            else:
                $ mc.phone.register_number(the_person)
                "She gives you her InstaPic profile name. You'll be able to look up her profile now."

        if the_person.opinion.small_talk >= 0:
            the_person "It was nice chatting [the_person.mc_title], we should do it more often!"
        else:
            if is_phone:
                the_person "I've got to go. Talk to you later."
            else:
                the_person "So uh... I guess that's all I have to say about that..."
                "[the_person.possessive_title!c] trails off awkwardly."
    else:
        if the_person.opinion.small_talk < 0:
            the_person "Oh, not much."
            $ the_person.change_happiness(the_person.opinion.small_talk)
            if is_phone:
                "You try and spark the conversation with a few more messages, but eventually [the_person.title] just stops responding."
            else:
                "You try and keep the conversation going, but making small talk with [the_person.title] is like talking to a wall."
        else:
            the_person "Oh, not much honestly. How about you?"
            $ the_person.change_happiness(the_person.opinion.small_talk)
            if is_phone:
                "You and [the_person.possessive_title] chat for a while. You don't feel like you've learned much about her, but you both enjoyed talking."
            else:
                "[the_person.possessive_title!c] seems happy to chitchat, and you spend half an hour just hanging out."
                "You don't feel like you've learned much about her, but at least she seems to have enjoyed talking."

    if not is_phone:
        $ the_person.apply_serum_study()

    $ mc.stats.change_tracked_stat("Girl", "Small Talk", 1)
    return

label compliment_person(the_person): #Tier 1. Raises the character's love. #TODO: just have it raise love and not sluttiness.
    $ mc.change_energy(-15)
    $ the_person.event_triggers_dict["complimented"] = the_person.event_triggers_dict.get("complimented", 0) - 1
    if the_person.is_girlfriend:
        $ the_person.call_dialogue("compliment_response_girlfriend")
    elif the_person.is_affair:
        $ the_person.call_dialogue("compliment_response_affair")
    else:
        $ the_person.call_dialogue("compliment_response")
    $ the_person.change_stats(happiness = 2,
        love = 5 if mc.charisma > 4 else 3, max_love = 20,
        obedience = 1 if mc_serum_aura_obedience.is_active else 0,
        arousal = 1 if mc_serum_aura_arousal.is_active else 0)
    the_person "It's been fun talking [the_person.mc_title], we should do this again sometime!"
    $ the_person.apply_serum_study()
    $ mc.stats.change_tracked_stat("Girl", "Complimented", 1)
    call evaluate_perception_perks(the_person) from _call_evaluate_perception_perks_compliment_person
    return

label flirt_person(the_person): #Tier 1. Raises a character's sluttiness up to a low cap while also raising their love by less than a compliment.
    $ mc.change_energy(-15)
    $ the_person.event_triggers_dict["flirted"] = the_person.event_triggers_dict.get("flirted", 0) - 1
    $ title = "uniform" if the_person.should_wear_uniform and the_person.is_wearing_uniform else "outfit"

    if the_person.is_girlfriend:
        mc.name "You're so beautiful [the_person.title], I'm so lucky to have a woman like you in my life."
        $ the_person.call_dialogue("flirt_response_girlfriend")

    elif the_person.is_affair:
        mc.name "You look so good today [the_person.title], you're making me want to do some very naughty things to you."
        $ the_person.call_dialogue("flirt_response_affair")

    elif the_person.is_at_job(prostitute_job):
        if the_person.vagina_visible:
            mc.name "You're looking extremely sexy today [the_person.title], I love the view of your beautiful pussy."
        elif the_person.tits_visible:
            mc.name "You're looking very sexy today [the_person.title], I love the view of your beautiful breasts."
        elif the_person.shows_off_her_ass:
            mc.name "Hello [the_person.title], your outfit really shows off your nice ass."
        elif the_person.shows_off_her_tits:
            mc.name "Hello [the_person.title], your outfit really shows off your [the_person.tits_description]."
        else:
            mc.name "Hi [the_person.title], you are looking quite perky today."

        the_person "Thanks, I thought I looked pretty hot in it too."

        "As she is saying that, she moves in closer, putting her arms around your shoulders."
        $ the_person.draw_person(position = "kissing")
        $ mc.change_locked_clarity(10)
        the_person "Would you like to do more than just look?"
        the_person "Well if you got the cash for it, you can even touch it."
        mc.name "Very tempting, I will let you know."
        $ the_person.draw_person()
        the_person "Alright, anything else you wanted?"

    elif the_person.love <= 20:
        #Low Love
        if the_person.outfit.outfit_slut_score > 30:
            mc.name "[the_person.title], you're looking nice today. That [title] looks good on you."
        elif the_person.happiness > 120:
            mc.name "[the_person.title], I really like your smile today, it fits with your [title]."
        else:
            mc.name "[the_person.title], are you wearing a new [title] today?"

        if the_person.energy > 15:
            if (the_person.is_employee or the_person.is_strip_club_employee) and the_person.is_wearing_uniform:
                $ the_person.call_dialogue("flirt_response_employee_uniform_low")
            else:
                $ the_person.call_dialogue("flirt_response_low")
        else:
            $ the_person.call_dialogue("flirt_response_low_energy")

    elif the_person.love <= 40 or the_person.opinion.kissing < -1: #20 to 40 or hates kissing
        # Mid Love
        if the_person.vagina_visible:
            mc.name "You're looking extremely sexy today [the_person.title], I love the view of your beautiful pussy."
        elif the_person.tits_visible:
            mc.name "You're looking very sexy today [the_person.title], I love the view of your beautiful breasts."
        elif the_person.shows_off_her_ass:
            mc.name "You're looking hot today [the_person.title]. That [title] really shows off your cute butt."
        elif the_person.shows_off_her_tits:
            mc.name "You're looking tasty today [the_person.title]. That [title] really shows off your [the_person.tits_description]."
        elif the_person.has_skirt and the_person.has_thigh_high_socks:
            mc.name "You're looking very sexy today [the_person.title]. That [title] with the skirt and stockings really show off your lovely legs."
        elif the_person.has_dress and the_person.has_thigh_high_socks:
            mc.name "You're looking very sexy today [the_person.title]. That [title] with the dress and stockings really show off your lovely legs."
        elif the_person.has_high_heels:
            mc.name "You're looking good today [the_person.title]. That [title] with those heels, just pure perfection."
        else:
            mc.name "You're looking cute today [the_person.title]. That [title] really shows off your body."

        if the_person.energy > 15:
            if (the_person.is_employee or the_person.is_strip_club_employee) and the_person.is_wearing_uniform:
                $ the_person.call_dialogue("flirt_response_employee_uniform_mid")
            else:
                $ the_person.call_dialogue("flirt_response_mid")
        else:
            $ the_person.call_dialogue("flirt_response_low_energy")

    else:
        # High Love
        if the_person.outfit.outfit_slut_score > 50:
            if the_person.vagina_visible:
                mc.name "[the_person.title], you have a beautiful pussy, any chance you would let me play with it?"
            elif the_person.tits_visible:
                mc.name "[the_person.title], you have wonderful breasts, any chance you would let me play with it?"
            elif the_person.shows_off_her_tits:
                mc.name "[the_person.title], your [title] is really showing off your [the_person.tits_description]. What are my chances of getting you out of it?"
            elif the_person.shows_off_her_ass:
                mc.name "[the_person.title], your [title] is really showing off your perky bottom. What are my chances of getting you out of it?"
            else:
                mc.name "[the_person.title], your [title] is driving me crazy. What are my chances of getting you out of it?"
        elif the_person.outfit.underwear_slut_score > 25:
            if the_person.vagina_visible:
                mc.name "[the_person.title], your pussy looks very good right now, any chance you would let me play with it?"
            elif the_person.shows_off_her_tits or the_person.tits_visible:
                mc.name "[the_person.title], any chance you are going to let me play with those [the_person.tits_description]?"
            elif the_person.shows_off_her_ass:
                mc.name "[the_person.title], any chance you are going to let me spank that beautiful butt?"
            else:
                mc.name "[the_person.title], any chance you are going to show me what you are wearing underneath your [title]?"
        else:
            mc.name "[the_person.title], you are looking good today. Any chance for me to see you naked any time soon?"

        if the_person.energy > 15:
            $ the_person.call_dialogue("flirt_response_high")
        else:
            $ the_person.call_dialogue("flirt_response_low_energy")

    python:
        mc.listener_system.fire_event("player_flirt", the_person = the_person)
        mc.stats.change_tracked_stat("Girl", "Flirted", 1)
        change_amount = 1 + the_person.opinion.flirting
        if change_amount <= 0:
            change_amount = 1

        the_person.change_stats(happiness = the_person.opinion.flirting,
            arousal = change_amount + (1 if mc_serum_aura_arousal.is_active else 0),
            slut = change_amount, max_slut = 20,
            love = 1, max_love = 25,
            obedience = 1 if mc_serum_aura_obedience.is_active else 0)
        the_person.discover_opinion("flirting")
        the_person.apply_serum_study()

    call evaluate_perception_perks(the_person) from _call_evaluate_perception_perks_flirt_person
    return

label evaluate_perception_perks(the_person):
    if perk_system.has_ability_perk("Personality Perception"):
        $ the_person.discover_random_opinion(include_normal = True, include_sexy = False)
    if personality_perception_perk_unlock():
        "Your ability to understand people is improving."
        "You have unlocked the Personality Perception perk!"
        "From now on, each time you interact with a girl, you discover one of her normal opinions."

    if perk_system.has_ability_perk("Extra Sexual Perception"):
        $ the_person.discover_random_opinion(include_normal = False, include_sexy = True)
    if sexual_preference_perception_perk_unlock():
        "Your ability to understand people is improving."
        "You have unlocked the Extra Sexual Perception perk!"
        "From now on, each time you interact with a girl, you discover one of her sexy opinions."
    return

label give_serum(the_person, add_to_log = True):
    call screen serum_inventory_select_ui(mc.inventory, the_person)
    if isinstance(_return, SerumDesign):
        $ the_serum = _return
        if add_to_log:
            "You decide to give [the_person.title] a dose of [the_serum.name]."
        $ mc.inventory.change_serum(the_serum,-1)
        $ the_person.give_serum(the_serum, add_to_log = add_to_log) #Use a copy rather than the main class, so we can modify and delete the effects without changing anything else.
        return the_serum

    if add_to_log:
        "You decide not to give [the_person.title] anything."
    return None

label date_person(the_person): #You invite them out on a proper date
    call screen main_choice_display(build_menu_items([get_date_plan_actions(the_person)]))
    if isinstance(_return, Action):
        $ _return.call_action(the_person) #This is where you're asked to plan out the date, or whatever.
    return

label lunch_date_plan_label(the_person):
    if the_person == kaya and the_person.location == coffee_shop:
        mc.name "I was thinking about getting some lunch. Do you have a lunch break?"
        if the_person.love < 40:
            the_person "Sorry, I work a short shift, so I don't get a lunch break."
            the_person "You seem nice though... maybe we could do something after I get off?"
            mc.name "Okay, I'll try to swing by later."
        else:
            the_person "You know I don't get a break! Swing by later, maybe we can get a drink after I get off?"
            mc.name "Okay, I'll try to swing by later."
        return

    # Take her out to lunch, raises love to a max of 50 if you pick the correct chat options
    if the_person.has_role(sister_role):
        mc.name "I was thinking about getting some lunch, do you want to come with me and hang out?"
        the_person "Hey, that sounds nice! You're always out of the house, I wish we got to spend more time together like we did when we were younger."

    elif the_person.has_role(mother_role):
        mc.name "I'm going to go out for lunch. You've been busy lately, would you like to take a break and join me?"
        the_person "Aww, it's so sweet that you still want to spend time with your mother. I'd love to!"

    elif the_person.has_role(aunt_role):
        mc.name "Would you like to come and have lunch with me? I haven't seen you much since I was a kid, I'm sure we have a lot to catch up on."
        the_person "It has been a long time, hasn't it. Lunch sounds wonderful!"

    elif the_person.has_role(cousin_role):
        mc.name "I'm going to get some lunch, would you like to come along with me?"
        the_person "You want me to be seen in public with you? You're really pushing it [the_person.mc_title], but sure."

    elif the_person.is_affair:
        mc.name "[the_person.title], I was going to get some lunch, would you like to join me?"
        the_person "That sounds nice, [the_person.mc_title]."
        "She pauses and seems to consider something for a moment."
        the_person "Are you sure my husband won't find out?"
        if the_person == christina:
            mc.name "You could always say you had to go over something, with [emily.fname]'s her tutor."
            the_person "You are right, let's go!"
        else:
            mc.name "Can't you go and grab lunch with an acquaintance?"
            the_person "Of course I can, let's get going!"

    elif the_person.has_significant_other and the_person.opinion.cheating_on_men < 0: #IF she likes cheating she doesn't even mention she's in a relationship
        mc.name "[the_person.title], I was going to get some lunch, would you like to join me? Maybe just grab a coffee and hang out for a while?"
        the_person "That sounds nice, [the_person.mc_title]."
        "She pauses and seems to consider something for a moment."
        the_person "Just so we're on the same page, this is just as friends, right? I have a [the_person.so_title], I don't want to get anything confused here."
        mc.name "Of course! I just want to hang out and talk, that's all."
        the_person "Okay, let's go then!"

    else:
        mc.name "Would you like to go get a coffee, maybe a little lunch, and just chat for a while? I feel like I want to get to know you better."
        the_person "That sounds nice, I think I'd like to get to know you better too."
        the_person "If you're ready to go right now I suppose I am too. Let's go!"

    call lunch_date_label(the_person) from _call_lunch_date_label #There's no need to schedule anything because this happens right away.
    return

label movie_date_plan_label(the_person):
    # She starts to wonder if she should be telling her boyfriend, etc. about this.
    if day%7 == 1 and time_of_day < 3:
        $ is_tuesday = True #It's already Tuesday and early enough that the date would be right about now.
    else:
        $ is_tuesday = False


    if the_person.has_role(sister_role):
        mc.name "Hey, I was wondering if you'd like to see a movie with me sometime? You know, spend a little more time together as brother-sister."
        the_person "It's been like, a year since I went to the movies with you. I think it was when my date ghosted me and you swept in and saved the night by coming with me."
        the_person "I can't quite remember what we saw though..."
        "She seems puzzled for a moment, then shrugs and smiles at you."
        the_person "Oh well, it's probably not important. Sure thing [the_person.mc_title], a movie sounds fun!"
        if is_tuesday:
            the_person "How about tonight? I think tickets are half price."
        else:
            the_person "How about Tuesday night? I think tickets are half price."

    elif the_person.has_role(mother_role):
        mc.name "Hey [the_person.title], would you like to come to the movies with me? I want to spend some more time together, mother and son."
        the_person "Aww, you're precious [the_person.mc_title]. I would love to go to the movies with you."
        the_person "Remember how you and I used to watch movies together every weekend? I felt like our relationship was so close because of that."
        "She seems distracted by the memory for a moment, then snaps back to the conversation."
        if is_tuesday:
            the_person "Would you be free tonight?"
        else:
            the_person "Would you be free Tuesday night?"

    elif the_person.has_role(aunt_role):
        mc.name "[the_person.title], would you like to come see a movie with me? I think it would just be nice to spend some more time together."
        the_person "You know, I haven't been out much since I left my ex, so a movie sounds like a real good time."
        if is_tuesday:
            the_person "How about later tonight? I don't have anything going on."
        else:
            the_person "How about Tuesday night? I don't have anything going on then."

    elif the_person.has_role(cousin_role):
        mc.name "Hey, do you want to come see a movie with me and spend some time together?"
        the_person "Fine, but no telling people we're related, okay? I don't want anyone to think I might be a dweeb like you."
        "She gives you a wink."
        if is_tuesday:
            the_person "How about tonight? I didn't have anything going on."
        else:
            the_person "How about Tuesday? I don't have anything going on then."

    elif the_person.has_significant_other:
        mc.name "So [the_person.title], I was going to see a movie some time this week and wanted to know if you'd like to come with me."
        mc.name "It would give us a chance to spend time together."
        if the_person.opinion.cheating_on_men > 0:
            the_person "Oh, a movie sounds fun!"
            "She gives you a playful smile."
            the_person "Just don't tell my [the_person.so_title], okay? He might not like me hanging around with a hot guy like you."
            mc.name "My lips are sealed."
            if the_person.effective_sluttiness() > 60:
                if is_tuesday:
                    the_person "Treat me right and mine might not be. He's normally out late with work tonight, how does that sound?"
                else:
                    the_person "Treat me right and mine might not be. He's normally out late with work on Tuesdays, how does that sound?"
            else:
                if is_tuesday:
                    the_person "He's normally out late with work on Tuesdays, so how about would tonight sound for you?"
                else:
                    the_person "He's normally out late with work on Tuesdays, how does that sound for you?"

        else:
            the_person "Oh, a movie sounds fun! But..."
            mc.name "Is there something wrong?"
            the_person "No, I just don't know what my [the_person.so_title] would think. He might be a little jealous of you, you know?"
            mc.name "You don't have to tell him that I'll be there, if you don't want to. There's no reason you couldn't go out by yourself if you wanted to."
            "She thinks about it for a moment, then nods and smiles."
            if is_tuesday:
                the_person "You're right, of course. He's normally busy with work tonight, so how does that sound for you?"
            else:
                the_person "You're right, of course. He's normally busy with work on Tuesdays, how does that sound for you?"

    else:
        mc.name "So [the_person.title], I was wondering if you'd like to come see a movie with me some time this week."
        mc.name "It would give us a chance to spend some time together and get to know each other better."
        if is_tuesday:
            the_person "Oh, a movie sounds fun! I don't have anything going on tonight, would that work for you?"
        else:
            the_person "Oh, a movie sounds fun! I don't have anything going on Tuesday night, would that work for you?"

    menu:
        "Plan a date for tonight" if is_tuesday:
            mc.name "Tonight would be perfect—I'll see you later."
            the_person "See you!"
            $ create_movie_date_action(the_person)

        "Plan a date for Tuesday night" if not is_tuesday:
            mc.name "Tuesday would be perfect—I'm already looking forward to it."
            the_person "Me too!"
            $ create_movie_date_action(the_person)

        "Maybe some other time":
            mc.name "I'm busy on Tuesday unfortunately."
            the_person "Well maybe next week then. Let me know, okay?"
            "She gives you a warm smile."

    return "Advance Time"

label dinner_date_plan_label(the_person):
    if day%7 == 4 and time_of_day < 3:
        $ is_friday = True #It's already Tuesday and early enough that the date would be right about now.
    else:
        $ is_friday = False

    if the_person.has_role(sister_role):
        mc.name "[the_person.title], I was wondering if you'd like to go out for a dinner date together. Some brother sister bonding time."
        if is_friday:
            the_person "That sounds great [the_person.mc_title]. Would tonight work for you?"
        else:
            the_person "That sounds great [the_person.mc_title]. Would Friday be good?"

    elif the_person.has_role(mother_role):
        mc.name "Mom, I was wondering if I could take you out to dinner, just the two of us. I'd enjoy some mother son bonding time."
        if is_friday:
            the_person "Aww, that's so sweet. How about tonight, after we're both finished with work."
        else:
            the_person "Aww, that's so sweet. How about Friday, after we're both finished with work."

    elif the_person.has_role(aunt_role):
        mc.name "[the_person.title], would you like to go out on a dinner date with me? I think it would be a nice treat for you."
        the_person "That sounds like it would be amazing. It's been tough, just me and [cousin.fname]. I don't get out much any more."
        "She smiles and gives you a quick hug."
        if is_friday:
            the_person "How about tonight?"
        else:
            the_person "How about Friday night?"

    elif the_person.has_role(cousin_role):
        mc.name "Hey, I want to take you out to dinner."
        the_person "Jesus, at least buy me dinner first. Wait a moment..."
        "She laughs at her own joke."
        if is_friday:
            the_person "Fine, how about tonight?"
        else:
            the_person "Fine, how about Friday?"

    elif the_person.has_significant_other:
        mc.name "[the_person.title], I'd love to spend some time together, just the two of us. Would you let me take you out for dinner?"
        the_person "[the_person.mc_title], you know I've got a [the_person.so_title], right? Well..."
        if the_person.opinion.cheating_on_men > 0:
            "She doesn't take very long to make up her mind."
            if is_friday:
                the_person "He's out with friends tonight and what he doesn't know can't hurt him. Shall we go tonight?"
            else:
                the_person "He won't know about it, right? What he doesn't know can't hurt him. Are you free Friday?"
        else:
            "She thinks about it for a long moment."
            if is_friday:
                the_person "Just this once, and we have to make sure my [the_person.so_title] never finds out. Shall we go tonight?"
            else:
                the_person "Just this once, and we have to make sure my [the_person.so_title] never finds out. Are you free Friday?"

    else:
        mc.name "[the_person.title], I'd love to get to know you better. Would you let me take you out for dinner?"
        if is_friday:
            the_person "That sounds delightful [the_person.mc_title]. I'm free tonight, if you are available."
        else:
            the_person "That sounds delightful [the_person.mc_title]. I'm free Friday night, if you would be available."

    menu:
        "Plan a date for tonight" if is_friday:
            mc.name "It's a date. I'll see you tonight."
            the_person "See you!"
            $ create_dinner_date_action(the_person)

        "Plan a date for Friday night" if not is_friday:
            mc.name "It's a date. I'm already looking forward to it."
            the_person "Me too!"
            $ create_dinner_date_action(the_person)

        "Maybe some other time":
            mc.name "I'm busy on Friday unfortunately."
            the_person "Well maybe next week then. Let me know, okay?"
            "She gives you a warm smile."
    return

label serum_give_label(the_person):
    $ ran_num = renpy.random.randint(0,100)
    $ chances = serum_give_calculate_chances(the_person)

    call screen main_choice_display(build_menu_items([serum_give_build_menu_options(the_person, chances)]))

    if _return == "stealth":
        "You chat with [the_person.title] for a couple of minutes, waiting to find a chance to deliver a dose of serum."
        if ran_num <= chances[0]:
            #Success
            "You're able to distract [the_person.title] and have a chance to give her a dose of serum."
            call give_serum(the_person) from _call_give_serum_enhanced_1
        else:
            #Caught!
            "You finally distract [the_person.title] and have a chance to give her a dose of serum."
            the_person "Hey, what's that?"
            "You nearly jump as [the_person.title] points down at the small vial of serum you have clutched in your hand."
            $ ran_num = renpy.random.randint(0,10)
            if ran_num < mc.charisma:
                if not the_person.is_employee:
                    mc.name "This? Oh, it's just something we're working on at the lab that I thought you might be interested in."
                    "You dive into a technical description of your work, hoping to distract [the_person.title] from your real intentions."
                else:
                    mc.name "This? Oh, it's just one of the serums I grabbed from production for quality control. I was just fidgeting with it, I guess."
                    "You make small talk with [the_person.title], hoping to distract her from your real intentions."
                "After a few minutes you've managed to avoid her suspicion, but haven't been able to deliver the dose of serum."
            else:
                mc.name "This? Uh..."
                $ the_person.draw_person(emotion="angry")
                $ the_person.change_stats(happiness = -10, obedience = -10, love = -5)
                the_person "Were you about to put that in my drink? Oh my god [the_person.mc_title]!"
                mc.name "Me? Never!"
                "[the_person.title] shakes her head and storms off. You can only hope this doesn't turn into something more serious."
                $ clear_scene()

    elif _return == "slave":
        #Auto success
        mc.name "[the_person.title], I'll help you to become a good slave. Take this."
        call give_serum(the_person) from _call_give_serum_enhanced_2

    elif _return == "ask":
        if not the_person.is_employee:
            mc.name "[the_person.title], I've got a project going on at work that could really use a test subject. Would you be interested in helping me out?"
        else:
            mc.name "[the_person.title], there's a serum design that is in need of a test subject. Would you be interested in helping out with a quick field study?"

        if ran_num <= chances[1]:
            #Success
            if not the_person.is_employee:
                if the_person == nora:
                    the_person "I'd be happy to help. I've seen your work, I have complete confidence you've tested this design thoroughly."
                else:
                    the_person "I'd be happy to help, as long as you promise it's not dangerous of course. I've always wanted to be a proper scientist!"
            else:
                the_person "I'll admit I'm curious what it would do to me. Okay, as long as it's already passed the safety test requirements, of course."
            mc.name "It's completely safe, we just need to test what the results from it will be. Thank you."
            call give_serum(the_person) from _call_give_serum_enhanced_3
        else:
            #Denies
            $ the_person.change_obedience(-2)
            the_person "I'm... I don't think I would be comfortable with that. Is that okay?"
            mc.name "Of course it is, that's why I'm asking in the first place."

    elif _return == "policy":
        #Auto success
        mc.name "[the_person.title], we're running field trials and you're one of the test subjects. I'm going to need you to take this."
        call give_serum(the_person) from _call_give_serum_enhanced_4

    elif _return == "demand":
        mc.name "[the_person.title], you're going to drink this for me."
        "You pull out a vial of serum and present it to [the_person.title]."
        the_person "What is it for, is it important?"
        mc.name "Of course it is, I wouldn't ask you to if it wasn't."
        if ran_num <= chances[2]:
            #Success
            the_person "Okay, if that's what you need me to do..."
            call give_serum(the_person) from _call_give_serum_enhanced_5
        else:
            #Refuse
            $ the_person.draw_person(emotion = "angry")
            $ the_person.change_stats(happiness = -2, obedience = -2, love = -2)
            the_person "You expect me to just drink random shit you hand to me? I'm sorry, but that's just ridiculous."

    elif _return == "pay":
        #Pay cost and proceed
        $ mc.business.change_funds(chances[3], stat = "Serum Testing")
        mc.name "[the_person.title], we're running field trials and you're one of the test subjects. I'm going to need you to take this, a bonus will be added onto your paycheck."
        call give_serum(the_person) from _call_give_serum_enhanced_6

    $ del chances
    return

label hug_person(the_person):
    python:
        day_part = time_of_day_string(time_of_day)
        if day_part == "early morning":
            day_part = "morning"
        name = renpy.random.choice([the_person.title, the_person.fname])
        renpy.say(mc.name, renpy.random.choice([
            "Catch you later [name].",
            "See you later [name]!",
            "Good [day_part] [name], don't be a stranger!",
            "Good [day_part] [name], have a good one!",
            "Take it easy [name]."
        ]))
    $ mc.change_energy(-5)
    $ kissing.redraw_scene(the_person)
    if the_person.has_relation_with_mc:
        if the_person.love <=40:
            "You pull [the_person.title] towards you and give her a nice hug"
            $ the_person.change_stats(happiness = 2, love = 1, max_love = 40, obedience = 1 if mc_serum_aura_obedience.is_active else 0)
        elif the_person.love <=60:
            "You pull [the_person.title] towards you and give her a nice long hug"
            the_person "MMmm, yes I will miss you too!"
            $ the_person.change_stats(happiness = 2, arousal = 1 + (1 if mc_serum_aura_arousal.is_active else 0), love = 1, max_love = 60, obedience = 0 + (1 if mc_serum_aura_obedience.is_active else 0))
        elif the_person.love <=80:
            "You slide your arms around [the_person.title], and pull her into a nice long hug"
            the_person "MMmm, yes I will see you soon!"
            $ the_person.change_stats(happiness = 2, arousal = 2 + (1 if mc_serum_aura_arousal.is_active else 0), love = 2, max_love = 80, obedience = 0 + (1 if mc_serum_aura_obedience.is_active else 0))
        else:
            "You slide your arms around her waist and pull [the_person.title] towards you, giving her a nice long hug, while running your hands lovingly up her back."
            the_person "MMmm, yes I can't wait to see you again!"
            $ the_person.change_stats(happiness = 2, arousal = 5 + (1 if mc_serum_aura_arousal.is_active else 0), love = 3, max_love = 100, obedience = 0 + (1 if mc_serum_aura_obedience.is_active else 0))
    else:
        the_person "MMmm, bye [the_person.mc_title]!"
        $ the_person.change_stats(happiness = 2, love = 1, max_love = 30, obedience = 1 if mc_serum_aura_obedience.is_active else 0)
    if the_person._follow_mc == True:
        $ shedule_destination = ""
        if the_person.get_destination() is the_person.home:
           $ schedule_destination = "my room"
        elif the_person.get_destination():
           $ schedule_destination = f"the {the_person.get_destination().formal_name}"
        else:
           $ schedule_destination = "somewhere else"
            
        $ the_person.follow_mc = False
        $ the_person.draw_person(position = "walking_away")
        the_person.title "Okay [the_person.mc_title], I'll head over to [schedule_destination]."
        "You tilt your head to watch her walk away."
        $ the_person.run_move()
    $ clear_scene()
    $ keep_talking = False
    return 

label kiss_person(the_person):
    python:
        day_part = time_of_day_string(time_of_day)
        name = renpy.random.choice([the_person.title, the_person.fname])
        if day_part == "early morning":
            day_part = "morning"
        renpy.say(mc.name, renpy.random.choice([
            "Mmmm [name], can't wait till next time.",
            "See you later [name]!",
            "Good [day_part] [name], keep those lips moist for me!",
            "Good [day_part] [name], till our lips meet again!",
            "See you soon, [name]."
        ]))
    $ mc.change_energy(-5)
    $ the_person.draw_person(position="kissing", emotion="happy")
    if the_person.has_relation_with_mc:
        if the_person.love <=40:
            "You step up to [the_person.title] and give her a nice sweet kiss."
            $ the_person.change_stats(happiness = 2, arousal = 1 + (1 if mc_serum_aura_arousal.is_active else 0), love = 1, max_love = 40, obedience = 1 if mc_serum_aura_obedience.is_active else 0)
        elif the_person.love <=60:
            "You pull [the_person.title] towards you and give her a nice long kiss."
            the_person "MMmm, yes I will miss you too!"
            $ the_person.change_stats(happiness = 2, arousal = 1 + (1 if mc_serum_aura_arousal.is_active else 0), love = 1, max_love = 60, obedience = 1 if mc_serum_aura_obedience.is_active else 0)
        elif the_person.love <=80:
            "You step up to [the_person.title] and give her a nice long kiss which lingers."
            the_person "MMmm, yes I will see you soon!"
            $ the_person.change_stats(happiness = 2, arousal = 2 + (1 if mc_serum_aura_arousal.is_active else 0), love = 2, max_love = 80, obedience = 1 if mc_serum_aura_obedience.is_active else 0)
        else:
            "You slide your arms around [the_person.title], pulling her into a deep long kiss which lingers."
            the_person "MMmm, yes I can't wait to see you again!"
            $ the_person.change_stats(happiness = 2, arousal = 5 + (1 if mc_serum_aura_arousal.is_active else 0), love = 3, max_love = 100, obedience = 1 if mc_serum_aura_obedience.is_active else 0)
    else:
        the_person "Mmmmmhmmm, bye [the_person.title]!"
        $ the_person.change_stats(happiness = 2, love = 1, max_love = 30, obedience = 1 if mc_serum_aura_obedience.is_active else 0)

    if the_person._follow_mc == True:
        $ shedule_destination = ""
        if the_person.get_destination() is the_person.home:
           $ schedule_destination = "my room"
        elif the_person.get_destination():
           $ schedule_destination = f"the {the_person.get_destination().formal_name}"
        else:
           $ schedule_destination = "somewhere else"
            
        $ the_person.follow_mc = False
        $ the_person.draw_person(position = "walking_away")
        the_person.title "Okay [the_person.mc_title], I'll head over to [schedule_destination]."
        "You tilt your head to watch her walk away."
        $ the_person.run_move()
    $ clear_scene()
    $ keep_talking = False
    return

label grope_person(the_person):
    # Note: the descriptors of the actual stages are stored in grope_descriptions.rpy to keep things organized.
    $ mc.change_energy(-5)
    $ the_person.event_triggers_dict["last_groped"] = (day, time_of_day)
    $ mc.stats.change_tracked_stat("Girl", "Groped", 1)
    call grope_shoulder(the_person) from _call_grope_shoulder
    if _return:
        call grope_waist(the_person) from _call_grope_waist
        if _return:
            call grope_ass(the_person) from _call_grope_ass
            if _return:
                call grope_tits(the_person) from _call_grope_tits
                if _return:
                    $ old_location = None
                    $ should_be_private = True
                    if mc.location.person_count > 1: #We aren't alone and should ask if we want to find somewhere private
                        $ extra_people_count = mc.location.person_count - 1
                        $ obedience_required = 130 - (10*the_person.opinion.public_sex)
                        if the_person.opinion.cheating_on_men < 1 and the_person.has_significant_other and not the_person.is_affair:
                            $ obedience_required += 10 + -10*the_person.opinion.cheating_on_men
                        $ the_person.discover_opinion("public sex")
                        if the_person.effective_sluttiness("touching_body") < 40 or the_person.opinion.public_sex < 0:
                            # She's nervous about it and asks to go somewhere private.
                            the_person "Wait, wait..."
                            "[the_person.possessive_title!c] glances around at the people nearby."
                            the_person "I don't want other people to watch. Let's find someplace we can be alone."
                            menu:
                                "Find somewhere quiet\n{menu_yellow}No interruptions{/menu_yellow}":
                                    mc.name "Alright, come with me."
                                    "You take [the_person.title] by her wrist and lead her away."
                                    call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_grope_person
                                    "You don't waste any time getting back to what you were doing, fondling [the_person.possessive_title]'s tits and ass."

                                "Stay where you are\n{menu_yellow}[extra_people_count] watching{/menu_yellow}" if the_person.obedience >= obedience_required:
                                    $ should_be_private = False
                                    "You scoff and keep feeling up her body."
                                    mc.name "Come on, we don't need to worry about them. Just relax."
                                    the_person "But they're going to be watching..."
                                    $ the_person.change_happiness(5*the_person.opinion.public_sex)
                                    "You ignore her and keep going. Her anxiety is obvious, but she doesn't object any further."

                                "Stay where you are\n{menu_red}Requires: [obedience_required] Obedience{/menu_red} (disabled)" if the_person.obedience < obedience_required:
                                    pass

                        else:
                            # She doesn't care, but you can find someplace private.
                            "[the_person.possessive_title!c] either doesn't notice or doesn't care, but there are other people around."
                            menu:
                                "Find somewhere quiet\n{menu_yellow}No interruptions{/menu_yellow}":
                                    mc.name "Let's find somewhere that isn't quite as busy. I don't want to be interrupted."
                                    if the_person.opinion.public_sex > 0:
                                        the_person "Aww, you don't want to put on a little show? I'm sure they would be {i}very{/i} entertained."
                                    else:
                                        the_person "Oh yeah, that's a good idea."
                                    call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_grope_person_2
                                    "You don't waste any time getting back to what you were doing, fondling [the_person.possessive_title]'s tits and ass."

                                "Stay where you are\n{menu_yellow}[extra_people_count] watching{/menu_yellow}":
                                    $ should_be_private = False
                                    pass

                    if the_person.is_at_job(prostitute_job):
                        the_person "We can continue what you started, but it would cost you two hundred dollars."
                        menu:
                            "Pay her\n{menu_red}Costs: $200{/menu_red}" if mc.business.funds > 200:
                                $ mc.business.change_funds(-200, stat = "Hookers")
                                $ the_person.change_obedience(1)
                                call fuck_person(the_person, private = should_be_private, start_position = standing_grope, start_object = None, skip_intro = True, ignore_taboo = True) from _call_fuck_person_grope_person_prostitute
                                $ the_person.call_dialogue("sex_review", the_report = _return)
                            "Pay her\n{menu_red}Requires: $200{/menu_red} (disabled)" if mc.business.funds <= 200:
                                pass
                            "No":
                                mc.name "Thanks for the offer, but no thanks."
                                "She shrugs."
                                the_person "Your loss."
                    else:
                        call fuck_person(the_person, private = should_be_private, start_position = standing_grope, start_object = None, skip_intro = True) from _call_fuck_person_43 # Enter the sex system, starting from this point.
                        $ the_person.call_dialogue("sex_review", the_report = _return)

                    if should_be_private:
                        call mc_restore_original_location(the_person) from _call_mc_restore_original_location_grope_person
                    else:
                        $ the_person.review_outfit()
    return

label command_person(the_person):
    mc.name "[the_person.title], I want you to do something for me."
    the_person "Yes [the_person.mc_title]?"

    call screen main_choice_display(build_menu_items([build_command_action_list(the_person, True)]))

    if isinstance(_return, Action):
        $ _return.call_action(the_person)
    return

label bc_talk_label(the_person):
    # Contains the Love and Sluttiness based approaches to asking someone to stop taking birth control.
    mc.name "Can we talk about something?"
    the_person "Mmhm, what's that?"
    mc.name "I want to talk about your birth control."
    if the_person.fertility_percent < 0:
        the_person "I have an IUD, so there is nothing to worry about."
        mc.name "That's good to know, thanks you for letting me know."
        $ the_person.update_birth_control_knowledge()
        return

    if the_person.has_relation_with_mc:
        #She'll talk to you about it. High Love or moderate sluttiness are needed to convince her to stop taking BC. Easier to convince her to start.
        # High influence from opinion of creampies.

        $ needed_start = 30 + (15 * the_person.opinion.creampies)
        $ needed_stop = 45 - (15 * the_person.opinion.creampies)
        if the_person.is_affair:
            $ needed_stop += -10*the_person.opinion.cheating_on_men #They think it's hot to have another man's baby

        if the_person.on_birth_control:
            if the_person.wants_creampie: #She's not happy about it
                the_person "Oh, sure. I'm taking it right now, so if you get a little too excited and unload inside me..."
                "She smiles and shrugs."
                the_person "Well that wouldn't be the end of the world."
            else:
                the_person "Oh, sure. I'm taking it right now, so we shouldn't have any \"accidents\" to worry about."
        else:
            if the_person.wants_creampie: #She's happy about not being on BC
                the_person "I'm not taking any right now, so..."
                "She smiles and shrugs."
                the_person "If you cum in me you might get me knocked up. It's kind of hot to think about that..."
            else:
                the_person "Oh, well... I'm not taking any right now."
        $ the_person.update_birth_control_knowledge()

        menu:
            "Start taking birth control" if not the_person.on_birth_control:
                mc.name "You should start taking some, I don't want you getting pregnant."
                if the_person not in (kaya, sakari) and (the_person.love >= needed_start or the_person.effective_sluttiness() >= needed_start):
                    "She thinks about it for a moment, then nods."
                    if the_person.has_taboo("condomless_sex"):
                        the_person "It would be nice to not have to worry about a condom breaking when we have sex."
                        the_person "Okay, I'll talk to my doctor and start taking it as soon as possible."
                    else:
                        the_person "If we keep doing it raw that's a smart idea."
                        the_person "I'll talk to my doctor and start taking it as soon as possible."
                    the_person "I should be able to start tomorrow, we will still need to be careful until then."
                    $ manage_bc(the_person, start = True)

                else:
                    "She shakes her head."
                    if the_person.wants_creampie:
                        the_person "I don't care about that. I love the thrill of a hot load of cum inside my perfectly fertile pussy."
                        the_person "There's nothing hotter than that. You're just going to have to accept that it's a risk."
                        $ the_person.discover_opinion("creampies")
                        $ the_person.discover_opinion("bareback sex")
                    else:
                        the_person "I'm sorry [the_person.mc_title], but I've tried it before and it plays hell with my hormones."
                        the_person "We can just use a condom, or do something else to have fun together."

            "Stop taking birth control" if the_person.on_birth_control:
                mc.name "I want you to stop taking it."
                if the_person.love >= needed_stop or the_person.effective_sluttiness() >= needed_stop:
                    if the_person.wants_creampie:
                        the_person "Yeah? I've wanted to stop too, I don't care if it's risky."
                        the_person "There's nothing that's more of a turn-on than having a hot load inside my pussy. Ah..."
                        "[the_person.possessive_title!c] sighs and seems lost in thought for a moment."
                        the_person "Sorry, I'm getting distracted."
                        $ the_person.discover_opinion("creampies")
                        $ the_person.discover_opinion("bareback sex")
                    else:
                        the_person "Do you think that's a good idea? What if something happened?"
                        mc.name "We can deal with that when it happens. If we don't want you to get pregnant we can always use a condom."
                        "She thinks about it for a long moment, then nods and smiles."
                        the_person "Okay, I won't take my birth control in the morning. We'll just be careful, it'll be fine..."

                    $ manage_bc(the_person, start = False)

                else:
                    if the_person.opinion.bareback_sex > 0:
                        the_person "I don't think that's a good idea. If I'm on my birth control you don't need to wear a condom when we fuck."
                        the_person "I love feeling you raw inside me. I don't want to have to give that up."
                        $ the_person.discover_opinion("bareback sex")
                    else:
                        the_person "I don't think that's a good idea. What if something happened? Are we ready for that change in our lives?"
                        the_person "Maybe one day, but I'm not comfortable with it right now."

            "That's all I wanted to know":
                mc.name "That's all, I just wanted to check on that."

    elif the_person.effective_sluttiness() > 40:
        $ needed_start = 40 + (15 * the_person.opinion.creampies)
        $ needed_stop = 75 - (15 * the_person.opinion.creampies)

        if the_person.on_birth_control:
            if the_person.opinion.bareback_sex > 0:
                the_person "Oh, is that all? Yeah, I'm on birth control right now because I hate how condoms feel."
                $ the_person.discover_opinion("bareback sex")
            else:
                the_person "Oh, is that all? Yeah, I'm on birth control right now so I don't have to worry about getting pregnant."
        else:
            the_person "Oh, I guess that's probably an important thing for you to know about."
            the_person "I'm not taking any birth control right now."

        $ the_person.update_birth_control_knowledge()
        menu:
            "Start taking birth control" if not the_person.on_birth_control:
                mc.name "You should probably start taking it, before something happens and you get pregnant."
                if the_person not in (kaya, sakari) and (the_person.love >= needed_start or the_person.effective_sluttiness() >= needed_start):
                    the_person "That's probably a good idea. I'll talk to my doctor as soon as possible about it."
                    $ manage_bc(the_person, start = True)
                else:
                    if the_person.wants_creampie:
                        "She shrugs and shakes her head."
                        $ the_person.discover_opinion("creampies")
                        $ the_person.discover_opinion("bareback sex")
                        the_person "I don't care about that. I love the feeling of a warm, risky creampie too much to ever give it up."
                    else:
                        the_person "Sorry, I've tried it before and it just messes with my hormones too badly."
                        the_person "We'll just be careful and use a condom, or you can pull out. Okay?"

            "Stop taking birth control" if the_person.on_birth_control:
                mc.name "You should stop taking it. Wouldn't that be really hot?"
                if the_person.love >= needed_start or the_person.effective_sluttiness() >= needed_stop:
                    if the_person.wants_creampie:
                        the_person "Do you think so? I've always wanted to, I don't think I can trust myself to tell a man to pull out."
                        the_person "Even if I know that's the smart thing to do I would probably just beg for a hot load inside me..."
                        $ play_moan_sound()
                        "She closes her eyes and moans softly, obviously lost in a fantasy of her own making."
                        "After a moment she shakes her head and focuses again."
                        $ the_person.discover_opinion("creampies")
                        $ the_person.discover_opinion("bareback sex")
                        the_person "Sorry... I guess if you think it's a good idea I can give it a try. What's the worst that can happen..."
                    else:
                        the_person "Do you really think so? I mean, it sounds kind of hot but I would have to trust you to pull out, or have you wear a condom."
                        mc.name "Then that's what I'll do. I just think it's so much sexier to know there's a little bit of risk."
                        "[the_person.possessive_title!c] thinks about it for a long moment. Finally she shrugs and nods."
                        the_person "Okay, we can give it a try. We'll just need to be very careful."
                    $ manage_bc(the_person, start = False)
                else:
                    "[the_person.possessive_title!c] shakes her head."
                    the_person "That would be crazy! There's no way I could gamble the rest of my life on some guy pulling out or me getting lucky."

            "That's all I wanted to know":
                mc.name "That's all, I just wanted to check."
    else:
        if the_person.love > 30:
            # She loves you enough to tell you her status
            the_person "Well that's kind of private, but if it really matters to you I guess I can tell you."
            if the_person.on_birth_control:
                the_person "I'm not looking to get pregnant right now, so I'm taking birth control."
            else:
                the_person "I'm not taking any birth control right now."

            $ the_person.update_birth_control_knowledge()
            "It's clear from her tone that [the_person.possessive_title] wouldn't be swayed by you telling her what to do."

        elif the_person.effective_sluttiness() > 20:
            the_person "Oh, I guess I can tell you if you're really curious."
            if the_person.on_birth_control:
                the_person "I'm taking birth control right now. I don't want to worry about getting pregnant by accident."
            else:
                the_person "I'm not taking birth control right now."

            $ the_person.update_birth_control_knowledge()
            "It's clear from her tone that [the_person.possessive_title] wouldn't be swayed by you telling her what to do."

        elif the_person.is_family:
            the_person "Come on [the_person.mc_title], you can't ask me that."
        else:
            the_person "That's a pretty personal question. Let's get to know each other a little more before we talk about that, okay?"
    return

label bc_demand_label(the_person):
    # Contains the obedience based approach to asking someone to stop taking birth control.
    # This event can have a moderately low Obedience requirement, with higher requirements to actually make changes.
    mc.name "Tell me about your birth control."
    $ the_person.update_birth_control_knowledge()

    if the_person.fertility_percent < 0:
        the_person "I have an IUD, so there is nothing to worry about."
        mc.name "That's good to know, thanks you for letting me know."
        return

    if the_person.on_birth_control:
        the_person "I'm taking birth control right now."
    else:
        the_person "I'm... not taking any right now."

    menu:
        "Start taking birth control" if not the_person.on_birth_control and the_person.obedience >= 130:
            mc.name "I want you to start taking some. I don't want you getting pregnant."
            if the_person in (kaya, sakari):
                the_person "I'm sorry, that's against everything we believe in, so I can't do that."
            else:
                "[the_person.possessive_title!c] nods."
                the_person "Okay, I can do that. I'll talk to my doctor, I think I'll be able to start taking them tomorrow."
                mc.name "Good."
                $ manage_bc(the_person, start = True)

        "Start taking birth control\n{menu_red}Requires: 130 Obedience{/menu_red} (disabled)" if not the_person.on_birth_control and the_person.obedience < 130:
            pass

        "Stop taking birth control" if the_person.on_birth_control and the_person.obedience >= 160:
            mc.name "I want you to stop taking it."
            $ complains_threshold = 45 - (15 * the_person.opinion.creampies)
            if the_person.effective_sluttiness() >= complains_threshold:
                # She's slutty enough that it's not even a concern.
                "[the_person.possessive_title!c] nods obediently."
                the_person "Okay, I'll stop right away, but I already took one this morning."
            elif the_person.is_family:
                "[the_person.possessive_title!c] shuffles nervously before working up the nerve to speak back."
                the_person "[the_person.mc_title], I can't do that. If you got me pregnant I... I don't know what I would do!"
                mc.name "I didn't say I was going to get you pregnant. I just told you to stop taking your birth control."
                mc.name "I'm sure you can avoid getting knocked up if you really put your mind to it. Now, do we have a problem?"
                "[the_person.title] starts to say something, then thinks better of it. She shakes her head."
                the_person "No, there's no problem. I won't take any birth control in the morning."

            else:
                "[the_person.possessive_title!c] shuffles nervously before working up the nerve to speak back."
                the_person "I... I don't know if that's a good idea. I don't know if I want to get pregnant."
                mc.name "I didn't ask if you wanted to get pregnant. I told you to stop taking your birth control. Is there a problem with that?"
                "She blushes and looks away under your glare."
                the_person "No. I'll stop right away. Sorry, but I already took one this morning."

            $ manage_bc(the_person, start = False)

        "Stop taking birth control\n{menu_red}Requires: 160 Obedience{/menu_red} (disabled)" if  the_person.on_birth_control and the_person.obedience < 160:
            pass

        "That's all I wanted to know":
            mc.name "Good. That's all I wanted to know."
    return

label bc_start_event(the_person, update_knowledge = True):
    $ start_birth_control(the_person, update_knowledge)
    return

label bc_stop_event(the_person, update_knowledge = True):
    $ stop_birth_control(the_person, update_knowledge)
    return
