### PERSONALITY CHARACTERISTICS ###
# kuudere (A stock love interest who is calm and collected on the outside, and never panics. They show little emotion, and in extreme cases are completely emotionless, but may be hiding their true emotions. They tend to be leaders who are always in charge of a situation.)
# "Kuudere" (JP), also known as "Cool-dere" in Western media, is a term for a character who appears calm and expressionless most of the time, but becomes cute, loving, and deredere around their love interest. They don't talk much and have a cold uninterested attitude towards people who are not their love interest, often making blunt ice-cold statements. Although it might not appear like it at first, they are hiding a deep inner love inside that will come out after becoming close to their love interest. They will start behaving in cute ways when around their love interest and have a more loving side than most, wanting their love interest to give them lots of affection. 
### DIALOGUE ###
# update all the following the_person and actions with kuudere personality. Remember the_person is female, and mc.name is male. Use Reina Aharen from Aharen-San for ideas:```


label kuudere_introduction(the_person):
    mc.name "Excuse me, could I bother you for a moment?"
    "She pauses, then turns around slowly to face you."
    the_person "What do you want?"
    mc.name "I apologize if my approach is abrupt, but your presence has piqued my curiosity."
    the_person "My name is [the_person.name]. Are there any specific questions you'd like answered?"
    $ the_person.change_happiness(-1)
    mc.name "Well, I was hoping to learn more about you... Your interests and hobbies perhaps? Or even your aspirations for the future?"
    "Her face remains emotionless as she continues."
    $ the_person.set_title()
    $ the_person.set_possessive_title()
    the_person "Ah, you want to know about me? Well, I suppose it's alright. I'm [the_person.title], a person of few words and many interests."
    the_person "I enjoy reading, listening to music, and observing the world around me."
    the_person "As for my aspirations, I aim to become a writer, someone who can convey thoughts and emotions through words."
    the_person "But please, do not expect me to be overly enthusiastic or expressive about it. I'm not one for grand gestures or declarations."
    $ the_person.change_happiness(-2)
    the_person "Now, if you don't mind, I'd like to return to my solitude. This conversation has reached its limit."
    return

label kuudere_greetings(the_person):
    if the_person.love < 0:
        the_person "Oh god, what do you want now?"
    elif the_person.happiness < 90:
        the_person "Hey. I hope you're having a better day than I am."
    else:
        if the_person.sluttiness > 60:
            if the_person.obedience > 180:
                the_person "Hello there [the_person.mc_title]. How can I help you, do you have anything that needs attention? Anything at all?"
            else:
                the_person "Hey there [the_person.mc_title], I hope this is for pleasure and not business."
        else:
            if the_person.obedience > 180:
                the_person "Hello [the_person.mc_title]."
            else:
                the_person "Hey, how's it going?"
    return

label kuudere_sex_responses_foreplay(the_person):
    if the_person.arousal_perc < 45:
        "[the_person.possessive_title!c] seems to be enjoying herself, but doesn't seem too interested in showing it."
        the_person "That's, uh... That's pretty good."

    elif the_person.arousal_perc < 60:
        the_person "Oh... That's nice."

    elif the_person.arousal_perc < 75:
        the_person "Mmm, this feels good."

    elif the_person.arousal_perc < 90:
        the_person "Keep going, [the_person.mc_title]."
    else:
        the_person "Oh..."

    return

label kuudere_sex_responses_oral(the_person):
    if the_person.arousal_perc < 45:
        "[the_person.possessive_title!c] doesn't seem too interested in showing her excitement."
        the_person "Oh... That's nice."

    elif the_person.arousal_perc < 60:
        the_person "Mmm... This is nice."

    elif the_person.arousal_perc < 75:
        the_person "Keep going."
    else:
        the_person "Oh..."

    return

label kuudere_sex_responses_vaginal(the_person):
    if the_person.energy < 10:
        call low_energy_sex_responses_vaginal(the_person) from _vt_kuudere_call_low_energy_sex_responses_vaginal_10
        return

    if the_person.arousal_perc < 45:
        "[the_person.possessive_title!c] doesn't seem too interested in showing her excitement."
        the_person "Oh... That's nice."

    elif the_person.arousal_perc < 60:
        the_person "Mmm... This is nice."

    elif the_person.arousal_perc < 75:
        the_person "Keep going."
    else:
        the_person "Oh..."

    return

label kuudere_sex_responses_anal(the_person):
    if the_person.energy < 10:
        call low_energy_sex_responses_anal(the_person) from _vt_kuudere_call_low_energy_sex_responses_anal_10
        return

    if the_person.arousal_perc < 45:
        "[the_person.possessive_title!c] seems to be uncomfortable, but doesn't show it."
        the_person "Oh... That's nice."

    elif the_person.arousal_perc < 60:
        the_person "Mmm... This is nice."

    elif the_person.arousal_perc < 75:
        the_person "Keep going."
    else:
        the_person "Oh..."

    return

label kuudere_climax_responses_foreplay(the_person):
    the_person "Hmm, I suppose it's rather interesting that you're capable of eliciting such reactions from me."
    "She tilts her head slightly, a smirk forming on her lips."
    the_person "Well then, I suppose I'll allow myself to... indulge."
    "Her voice drops to a whisper, and she gazes at you with an air of detachment."
    the_person "You may continue. It's not as though it matters, after all."
    return

label kuudere_climax_responses_oral(the_person):
    if the_person.sluttiness > 70:
        the_person "Ah, it seems I'm quite close to climax... I suppose it's acceptable to indulge in such pleasures."
    else:
        the_person "Fascinating... I'm nearing the edge. It appears I must allow myself to experience this sensation."
    return

label kuudere_climax_responses_vaginal(the_person):
    if the_person.sluttiness > 70:
        if the_person.arousal_perc > 120:
            the_person "...more... just a bit more..."
        else:
            the_person "Ah... close... almost there..."
        "Her breathing becomes shallow and her eyes flutter shut."
    else:
        the_person "Oh... umm... yes..."
    return

label kuudere_climax_responses_anal(the_person):
    if the_person.sluttiness > 70:
        if the_person.arousal_perc > 120:
            the_person "Hmph, I suppose it can't hurt to let you do that. Shove your big cock into my ass."
        else:
            the_person "I suppose your cock does feel quite large in my ass... It's rather... intriguing."
        the_person "Hmm, interesting."
    else:
        the_person "Well, I suppose it's inevitable. Your cock is quite... persistent."
        "She looks at you with a slightly bemused expression, but her body betrays her arousal."
        the_person "It seems I'll have to... cum."
    return

label kuudere_clothing_accept(the_person):
    the_person "Hmph, I suppose it could work. But don't think this means I'm going to start dressing up just because you like it."
    return

label kuudere_clothing_reject(the_person):
    if the_person.should_wear_uniform:
        the_person "Hmm, about that... I don't think I could really pull off wearing that, could I? It's not really my style."
    elif the_person.obedience > 180:
        the_person "I appreciate the thought, but I don't think it would be a good idea for me to wear something like that. It's just not really me."
    else:
        if the_person.sluttiness > 60:
            the_person "Wow, that's quite the outfit you've got there. But honestly, I don't think it would be a good idea for me to wear something that...revealing."
        else:
            the_person "To be honest, I'm not really a fan of that outfit. Thanks for the thought, but I don't think it would be a good fit for me."
    return

label kuudere_clothing_review(the_person):
    if the_person.outfit.cum_covered:
        if (the_person.sluttiness > 40 and the_person.opinion.being_covered_in_cum >= 0) or the_person.opinion.being_covered_in_cum > 0:
            the_person "Hmph, it seems I've made a bit of a mess."
            "[the_person.title] begrudgingly starts to wipe up the cum from her outfit."
        else:
            the_person "I suppose I should clean up this... mess."
            "[the_person.title] wipes herself down, removing the excess cum from her clothing."

    if the_person.obedience > 180:
        the_person "Very well, I'll be back shortly after cleaning up."
    else:
        if the_person.sluttiness > 40:
            the_person "I wouldn't want others to see me like this. I'll return shortly, cleaned up and presentable."
        else:
            the_person "I suppose I should make some effort to look presentable. Wait here while I find a mirror and tidy up."
    $ the_person.apply_planned_outfit(show_dress_sequence = True)
    return

label kuudere_strip_reject(the_person, the_clothing, strip_type = "Full"):
    the_person "Hmm, I'm not really in the mood for this right now."
    mc.name "What do you mean? You said you wanted to try some new things."
    the_person "Yeah, but that was before I got distracted. Maybe another time, okay?"
    mc.name "But I was looking forward to it..."
    the_person "I'm sorry, maybe you could do something else for me instead? Like, um, give me a massage or something?"
    return

label kuudere_strip_obedience_accept(the_person, the_clothing, strip_type = "Full"):
    "[the_person.title] lets out a small chuckle as you begin to undress her, seemingly unbothered by the situation."
    if the_person.obedience > 180:
        the_person "Oh, alright then. I guess it's alright if you want to do that."
    else:
        the_person "Hmm, alright...I suppose it's just a little embarrassing, that's all."
    return

label kuudere_grope_body_reject(the_person):
    the_person "Ah!"
    "[the_person.title] steps back as you touch her, then raises an eyebrow with a slightly amused expression."
    the_person "What do you think you're doing?"
    mc.name "Oh, I just... I thought you might want some... company."
    the_person "Company? I'm not sure what you're implying, but I'm not really in the mood for... that."
    mc.name "Oh, I see. Sorry, I didn't realize."
    the_person "It's fine. Just... keep your distance, okay? I'm not really comfortable with that kind of thing."
    "You nod, feeling a bit embarrassed but also understanding of her boundaries. She seems to relax a bit after setting the boundary, but you can tell she's still a little on edge."
    return

label kuudere_sex_accept(the_person, the_position):
    "Her face is a mask of composure, her eyes giving away nothing. But her slight smile suggested that she was, in fact, looking forward to the encounter."
    "She studies you with her cool, indifferent expression, her voice calm and collected."
    the_person "So, we're doing this, then?"
    if the_person.sluttiness > 60:
        if the_person.obedience < 80:
            the_person "[the_person.mc_title], let's do it. I have a few ideas we could try out."
        else:
            if the_position.skill_tag == "Foreplay":
                the_person "Just thinking about it gets me excited, [the_person.mc_title]."
            elif the_position.skill_tag == "Oral":
                if "getting head" in the_position.opinion_tags:
                    the_person "Come here, [the_person.mc_title], get down there and make me cum."
                else:
                    the_person "Here, I need to suck on that lovely dick right now."
            else:
                the_person "Oh yes, [the_person.mc_title], I need you to fuck me hard and deep."
    else:
        the_person "Come here, [the_person.mc_title], let's do it."
    return

label kuudere_sex_obedience_accept(the_person):
    if the_person.sluttiness > 70:
        the_person "Hmm, I suppose I have no choice but to submit to your desires, [the_person.mc_title]."
    else:
        if the_person.obedience > 180:
            the_person "If you insist, I will follow your commands, even if it goes against my better judgment."
        else:
            the_person "I shouldn't be doing this, but if you really want to explore this further, I'll give it a try. I'm not one to turn down a new experience, after all."
    return

label kuudere_sex_gentle_reject(the_person):
    the_person "Hmm, I don't know if I'm in the mood for that right now, [the_person.mc_title]."
    return

label kuudere_sex_angry_reject(the_person):
    the_person "What do you think you're doing? That's completely out of the question."
    "She crosses her arms, giving you a cold, calculating stare."
    return

label kuudere_seduction_response(the_person):
    the_person "Hmm, I suppose you're feeling a bit...restless, aren't you? I'll indulge you for a moment."
    return

label kuudere_seduction_accept_crowded(the_person):
    the_person "Hmm, fine. We can sneak away for a few minutes, but don't expect me to be too...cooperative in public."
    return

label kuudere_seduction_accept_alone(the_person):
    the_person "Alright, let's get this over with. But remember, I'm only doing this because I want to."
    return

label kuudere_seduction_refuse(the_person):
    the_person "I'm not interested in getting involved with you right now. We can talk about something else if you'd like."
    return

label kuudere_compliment_response(the_person):
    mc.name "Hey [the_person.fname]. How are you? You're looking quite perky today."
    if the_person.is_at_work:
        if (the_person.is_employee or the_person.is_strip_club_employee) and the_person.is_wearing_uniform:
            call kuudere_flirt_response_employee_uniform_low(the_person) from _call_kuudere_flirt_response_employee_uniform_low_compliment_response
        elif the_person.is_at_job(prostitute_job):
            the_person "Hmm, fun? I suppose we could find something to do. But don't get any wrong ideas."
    the_person "Oh, stop it. I'm fine, thank you."
    "You chat with [the_person.possessive_title] for a while and she appreciates your concern."
    return

label kuudere_compliment_response_girlfriend(the_person):
    mc.name "Hey [the_person.title]. You look quite... composed this [StringInfo.time_of_day_string]."
    if the_person.is_at_work:
        if the_person.is_employee or the_person.is_strip_club_employee and the_person.is_wearing_uniform:
            call kuudere_flirt_response_employee_uniform_mid(the_person) from _call_kuudere_flirt_response_employee_uniform_mid_compliment_response_girlfriend
            $ the_person.call_dialogue("flirt_response_employee_uniform_mid")
        elif the_person.sluttiness > 50:
            the_person "Mmm, thank you, [the_person.mc_title]. Wanna find out how composed I am..."
        else:
            the_person "Ah, really? Thanks, [the_person.mc_title]. You're not looking too bad yourself."
    else:
        the_person "Aww, thank you, I'm fine. You look quite... put-together yourself..."
    "You continue the conversation with [the_person.possessive_title], making subtle, aloof comments. She seems to appreciate your understated flattery."
    return

label kuudere_compliment_response_affair(the_person):
    mc.name "Hey [the_person.title]. You look rather... polished this [StringInfo.time_of_day_string]."
    if the_person.is_at_work:
        if the_person.is_employee or the_person.is_strip_club_employee and the_person.is_wearing_uniform:
            call kuudere_flirt_response_employee_uniform_mid(the_person) from _call_kuudere_flirt_response_employee_uniform_mid_compliment_response_affair
        elif the_person.sluttiness > 50:
            the_person "Mmmm, thank you [the_person.mc_title], shall we find a more discreet location where we can explore this further?"
        else:
            the_person "Shh, [the_person.mc_title]... You find my work attire appealing? Perhaps we could discuss it over a quiet dinner..."
    else:
        the_person "You like this? Let's have a drink and see where the evening takes us..."
    "You continue the conversation with [the_person.possessive_title], subtly emphasizing her attractiveness. She seems to appreciate your understated interest."
    return

label kuudere_flirt_response(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 50:
            the_person "You know, you don't have to ask nicely. I might just give it to you anyways."
        else:
            the_person "Thank you, I'm glad you find me pleasing."
    elif the_person.has_significant_other:
        if the_person.sluttiness + (the_person.opinion.cheating_on_men*5) > 50:
            the_person "Then why don't you make a move? I don't think my [the_person.so_title] needs to know about this little secret, do you?"
            "[the_person.title] gives you a sly look and a wink."
        else:
            the_person "You're treading on dangerous ground, [the_person.mc_title]. I have a [the_person.so_title], and I don't think he would appreciate your attention."
            mc.name "And what about you? Do you appreciate it?"
            "She gives a cool, detached smile."
            the_person "Maybe I do."
    else:
        if the_person.sluttiness > 50:
            the_person "Then why don't you take a chance? I might just give in if you're persuasive enough."
        else:
            the_person "Well, thank you. I suppose you'll have to prove yourself worthy of my attention."
            the_person "I have high standards, after all."
    return

label kuudere_flirt_response_employee_uniform_low(the_person):
    if the_person.is_wearing_forced_uniform:
        the_person "Hmph. I suppose it's not so bad being practically naked... for work."
        mc.name "I know you don't like it, but I needed to make a point."
        the_person "I know, I know. It's just a little... revealing."
        $ mc.change_locked_clarity(5)
        "She shrugs nonchalantly, not seeming too bothered by the situation."
    elif the_person.judge_outfit(the_person.outfit):
        #She's in uniform and likes how it looks.
        the_person "Ah, yes. I must admit, I do feel a bit more... attractive in this uniform."
        the_person "It's nice to work somewhere where I can show off a little."
        $ mc.change_locked_clarity(5)
        "She gives you a brief, indifferent smile, as if she's not really interested in the attention."
    else:
        #She's in uniform, but she thinks it's a little too slutty.
        if the_person.vagina_visible:
            # Her pussy is on display.
            the_person "Hmph. I suppose it's not so bad being practically naked... for work."
            mc.name "Well, you know that it's..."
            the_person "Yes, I know. It's company policy. I'm not complaining, exactly."
            mc.name "Give it some time and you'll get used to it."
            $ mc.change_locked_clarity(5)
            "She nods, still seeming a bit indifferent to the situation."

        elif the_person.tits_visible:
            # Her tits are out
            the_person "Ah, yes. Well, at least it's not too uncomfortable to wear."
            mc.name "You look incredible and you're comfortable. I call that a success."
            $ mc.change_locked_clarity(5)
            "She gives you a brief, noncommittal smile."

        elif the_person.underwear_visible:
            # Her underwear is visible.
            the_person "Well, I suppose it's not so bad. At least it's a comfortable uniform."
            mc.name "It may be a little unconventional, but you look fantastic. You've got exactly the right kind of body for it."
            the_person "Hmm. I suppose that's true."
            $ mc.change_locked_clarity(5)
            "She shrugs, not seeming too interested in the conversation."

        else:
            # It's just generally slutty.
            the_person "Ah, yes. Well, at least the uniform is well-made."
            $ mc.change_locked_clarity(5)
            "She gives you a brief, indifferent smile."
    return

label kuudere_flirt_response_employee_uniform_mid(the_person):
    if the_person.is_wearing_forced_uniform:
        $ mc.change_locked_clarity(10)
        the_person "I suppose my outfit does make me stand out, doesn't it?"
        mc.name "Yes, it does. You look very nice."
        the_person "Thank you. I'm just trying to make the best of it. But I must say, I do enjoy the attention."
        mc.name "I'm sure you do."
    elif the_person.judge_outfit(the_person.outfit):
        $ mc.change_locked_clarity(10)
        the_person "Hmm, I suppose this uniform does show off my figure a bit more than I'd like. But I can't deny I look good in it."
        mc.name "You certainly do."
        the_person "Yeah, well, I guess it's a small price to pay for looking good."
    else:
        the_person "I think this uniform could use a bit more... flair. But I'll make do with what I have."
        $ mc.change_locked_clarity(10)
        the_person "Still, I suppose it's not the worst thing I've ever worn."
        mc.name "That's true."

    return

label kuudere_flirt_response_low(the_person):
    #She's in her own outfit.
    mc.name "I think it's cute. The color suits you."
    $ the_person.draw_person(position = "back_peek")
    $ mc.change_locked_clarity(5)
    "She shows off her back, looking at you with a hint of a smirk."
    the_person "I'm glad you think so. I did put some effort into choosing this outfit."
    return

label kuudere_flirt_response_low1(the_person):
    if the_person.has_significant_other:
        the_person "Hmm, I suppose you should be careful. I wouldn't want you to get into trouble with [the_person.so_title]."
        mc.name "I'll keep that in mind."
        the_person "Good. But I will say, I don't think he'd be able to resist me either."
    else:
        the_person "Well, you're certainly welcome to try. But I warn you, I'm not easily impressed."
        the_person "You'll have to show me something really special if you want to catch my eye."
    $ mc.change_locked_clarity(5)
    return

label kuudere_flirt_response_mid(the_person):
    if mc.location.person_count > 1 and the_person.effective_sluttiness("kissing") < (25 - (5*the_person.opinion.public_sex)):
        $ mc.change_locked_clarity(10)
        if the_person.tits_visible:
            the_person "Hmm, I know I look good in this outfit. Do you like it?"
            "She tilts her head, her eyes half-lidded and her lips slightly parted."
            mc.name "Yeah, you look great. All of you looks good, tits included."
            the_person "Heh, I knew you would appreciate it. I put a lot of effort into my appearance."
        else:
            the_person "Thanks! I thought this was a pretty good outfit when I chose it."
        the_person "Maybe I'll take you shopping sometime and let you pick out some things for me to wear."
        mc.name "I'd like that. I have a few ideas already."
        the_person "I'm sure you do."
    else:
        the_person "Thanks, I think I look pretty good in it too."
        the_person "You want a better view, huh? Here, how does this look?"
        $ the_person.draw_person(position = "back_peek")
        $ mc.change_locked_clarity(10)
        the_person "Not bad, right?"
        mc.name "Quite impressive."
        "[the_person.possessive_title!c] smirks and turns back to face you."
        $ the_person.draw_person()
        the_person "I'm glad you think so. Maybe we can go out sometime and see if we can find something even better."
    return

label kuudere_flirt_response_mid1(the_person):
    $ mc.change_locked_clarity(10)
    the_person "Thanks, I do look amazing in this outfit."
    if (the_person.has_skirt or the_person.has_dress) and not the_person.has_thigh_high_socks:
        mc.name "You could change it up with some high stockings, I would like to see that."
        the_person "I bet you would, you naughty boy."

    mc.name "How about you and me go and grab a coffee sometime?"
    the_person "Hmm, I'm not sure. I'm quite busy most of the time, but I suppose I could make an exception for someone as charming as you."
    the_person "Just let me know when, and I'll see what I can do."
    return

label kuudere_flirt_response_high(the_person):
    if mc.location.person_count > 1 and the_person.effective_sluttiness() < (25 - (5*the_person.opinion.public_sex)): # There are other people here, if she's not slutty she asks if you want to find somewhere quiet
        the_person "Driving you crazy, huh? Well..."
        "She glances around before smiling mischievously."
        the_person "We'll have to do something about that, but not here."
        menu:
            "Find somewhere more quiet\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                mc.name "Then let's find somewhere that isn't here."
                the_person "Eager, huh? Alright, let's go find somewhere."
                call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_kuudere_flirt_response_high_2
                the_person "So... Now what's your plan?"

                if the_person.is_willing(kissing):
                    $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
                    if the_person.has_taboo("kissing"):
                        "You step close to [the_person.title] and put your arm around her waist, pulling her close."
                        $ the_person.call_dialogue("kissing_taboo_break")
                        $ the_person.break_taboo("kissing")
                        "You kiss her. She eagerly presses her body against yours in response."
                    else:
                        "You step close to [the_person.title] and put your arm around her waist, pulling her close and kissing her."
                        "She responds immediately and eagerly presses her body against yours."
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _vt_kuudere_call_fuck_person_49
                else:
                    if the_person.has_taboo("touching_body"):
                        $ the_person.call_dialogue("touching_body_taboo_break")
                        $ the_person.break_taboo("touching_body")
                        "You take her hand and pull her close against you. She looks into your eyes."
                    else:
                        "You answer by pulling her close against you."
                    call fuck_person(the_person, private = True, start_position = standing_grope, skip_intro = True) from _vt_kuudere_call_fuck_person_kuudere_flirt_grope

                $ the_person.call_dialogue("sex_review", the_report = _return)
                call mc_restore_original_location(the_person) from _call_mc_restore_original_location_kuudere_flirt_response_high_2

            "Just flirt":
                mc.name "Not here, huh? How about back at your place then?"
                the_person "Bold. I like it. Maybe if you buy me dinner you'll get your chance."

    else:
        if mc.location.person_count == 1: #You're alone, so she just didn't meet the sluttiness threshold
            "[the_person.possessive_title!c] bites her lower lip and glances around, confirming you're alone."
            the_person "Well it's just the two of us here, so now's your chance to find out. What's your plan?"

        else:  # You aren't alone but she's still into it.
            the_person "Feeling bold today, huh? Well I think your chances are pretty good."
            if the_person.has_large_tits: #Bounces her tits for you
                $ mc.change_locked_clarity(15)
                "[the_person.title] grabs her tits and jiggles them for you."
                the_person "Maybe I can get these girls out for you. Does that sound nice?"

            else: #No big tits, so she can't bounce them (as much)
                "[the_person.title] runs her hands over her hips sensually, obviously encouraging you to take things further."

        menu:
            "Touch her" if not the_person.is_willing(kissing):
                "You step closer to [the_person.title] and move your hands down her waist."
                if the_person.has_taboo("touching_body"):
                    $ the_person.call_dialogue("touching_body_taboo_break")
                    $ the_person.break_taboo("touching_body")

                call fuck_person(the_person, start_position = standing_grope, private = False) from _call_fuck_person_flirt_response_kuudere_touching

            "Kiss her" if the_person.is_willing(kissing):
                $ the_person.draw_person()
                if the_person.has_taboo("kissing"):
                    "You put your arm around [the_person.possessive_title] and lean in close."
                    $ the_person.call_dialogue("kissing_taboo_break")
                    $ the_person.break_taboo("kissing")
                    "You kiss her. She returns the kiss and presses her body against you."
                else:
                    "You put your arm around [the_person.possessive_title] and pull her close, leaning in to kiss her."
                    "She responds immediately, pressing her body against yours and kissing you back."

                call mc_move_to_private_location(the_person) from  _call_mc_move_to_private_location_kuudere_flirt_response_high
                call fuck_person(the_person, start_position = kissing, private = _return, skip_intro = True) from _vt_kuudere_call_fuck_person_50
                $ the_person.call_dialogue("sex_review", the_report = _return)
                call mc_restore_original_location(the_person) from _call_mc_restore_original_location_kuudere_flirt_response_high

            "Just flirt":
                $ the_person.draw_person()
                mc.name "Very tempting, but you're going to have to contain yourself for now."
                "[the_person.title] pouts melodramatically."
                the_person "You're so cruel. Maybe you can take me out to dinner to make up for it."
    return

label kuudere_flirt_response_low_energy(the_person):
    the_person "Hmph, thank you for noticing, but I'm not really in the mood for anything right now." 
    return

label kuudere_flirt_response_girlfriend(the_person):
    # Lead in: mc.name "You're so beautiful [the_person.title], I'm so lucky to have a woman like you in my life."
    if mc.location.person_count > 1:
        # There are other people around, so she'll only start making out with you if she's slutty.
        if the_person.effective_sluttiness("kissing") < (25 - (5*the_person.opinion.public_sex)):
            # Not very slutty, so she wants to find somewhere private
            the_person "Oh my god, you're such a sap. Come here."
            "She pulls you against her and kisses you intensely. She smiles when she breaks the kiss a moment later."
            the_person "There, that's how you should show a woman how you feel."
            mc.name "Uh huh, I think I've got the idea..."
            "You put your arms around her and kiss her back, matching her own intensity."
            the_person "Mmm, yeah you've got it. Don't get too excited though, we have to wait until we're alone to do anything more."
            menu:
                "Find somewhere more quiet\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                    mc.name "Why wait? Come on, I'm sure we can find somewhere quiet."
                    the_person "That eager, huh? Alright, let's go!"
                    "You and [the_person.possessive_title] hurry off, searching for a private spot."
                    call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_kuudere_flirt_response_girlfriend_2
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _vt_kuudere_call_fuck_person_76
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_kuudere_flirt_response_girlfriend_2

                "Just flirt":
                    $ mc.change_locked_clarity(10)
                    "You reach behind [the_person.possessive_title] and grab her ass, giving it a firm squeeze."
                    mc.name "Alright, I'll be patient. This ass is worth waiting for."
                    "She wiggles her hips back against your hand."
                    the_person "Damn right it is."

        else:
            the_person "Well if I'm so beautiful then hurry up and kiss me, hot stuff."
            "You put your arm around her waist and lean close, kissing her on her lips."
            "When you break the kiss [the_person.possessive_title] sighs happily and leans her head against your shoulder."
            the_person "Why did you stop? I was having such a good time..."
            menu:
                "Make out":
                    "You don't say a word as you lean back and kiss her again, slowly and sensually this time."
                    "[the_person.title] presses her body against you in response, grinding her hips against your thigh."

                    call mc_move_to_private_location(the_person) from  _call_mc_move_to_private_location_kuudere_flirt_response_girlfriend
                    call fuck_person(the_person, start_position = kissing, private = _return, skip_intro = True) from _vt_kuudere_call_fuck_person_77
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_kuudere_flirt_response_girlfriend

                "Just flirt":
                    mc.name "I just like to tease you."
                    $ mc.change_locked_clarity(10)
                    "You reach around and grab her ass, squeezing it playfully."
                    "She pouts melodramatically and rubs your chest."
                    the_person "Ugh, you're the worst. I was already getting turned on..."
    else:
        # You're alone, so she's open to fooling around.
        the_person "Well you've got me all alone, so how about you show me just how lucky you feel?"
        "She reaches down to your waist and cups your crotch, rubbing it gently."
        menu:
            "Kiss her":
                if the_person.has_taboo("kissing"):
                    $ the_person.call_dialogue("kissing_taboo_break")
                    $ the_person.break_taboo("kissing")

                "You put your arms around [the_person.possessive_title]'s waist and rest your hands on her ass. You pull her close and kiss her sensually."
                "She responds by pressing her body against you and grinding her hips against your thigh."
                call fuck_person(the_person, start_position = kissing, skip_intro = True) from _vt_kuudere_call_fuck_person_78
                $ the_person.call_dialogue("sex_review", the_report = _return)
                $ the_person.review_outfit()

            "Just flirt":
                "You reach your arms around her waist and grab her ass, squeezing it playfully."
                mc.name "I'm sorry, but I'm going to make you wait a bit for that. I just like seeing you get all worked up."
                "She pouts melodramatically."
                the_person "Ugh, you're the worst. I was already getting so turned on..."
    return

label kuudere_flirt_response_affair(the_person):
    # Lead in: mc.name "You look so good today [the_person.title], you're making me want to do some very naughty things to you."
    if mc.location.person_count > 1: #There are other people around, she's nervous about people finding out what you're doing.
        if (the_person.opinion.cheating_on_men *15) + the_person.effective_sluttiness() > 50: #SHe's turned on by flirting in public or doesn't think anything is wrong with it
            "[the_person.possessive_title!c] bites her lower lip and looks you up and down, eyes lingering on your crotch."
            the_person "Yeah? Well... I've got some spare time, how about we slip away and you can show me what you mean."
            menu:
                "Find somewhere more quiet\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                    mc.name "Alright, let's go."
                    "You and [the_person.title] hurry off to find a quiet spot."
                    call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_kuudere_flirt_response_affair
                    $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
                    "As soon as you're alone she pulls you into a deep and passionate kiss."
                    $ the_person.draw_person(position = "kissing")
                    the_person "Ah... You aren't the only one having dirty thoughts. You get me so fucking horny!"
                    "You wrap your arms around her waist and kiss her back."
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _vt_kuudere_call_fuck_person_79
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_kuudere_flirt_response_affair

                "Just flirt":
                    "You slide your arm around [the_person.title]'s waist and rest your hand on her ass, rubbing it gently."
                    mc.name "You'll have to wait a little bit, we don't have time for all the things I want to do to you right now."
                    $ mc.change_locked_clarity(20)
                    "She glances around and checks to make sure nobody else is watching, then she slides her hand down your waist and to your crotch."
                    "[the_person.possessive_title!c] massages your bulge lightly and pouts."
                    the_person "That's a shame. I can think of so many fun things to do with this..."
                    the_person "Just don't make me wait too long, okay? I barely get any action from my [the_person.so_title]."
                    "You give her ass a slap before letting go."
                    mc.name "It won't be too long, I promise."

        else: #She's shy or nervous about being discovered
            "[the_person.possessive_title!c] laughs, then shakes her head and glances around."
            the_person "You're looking pretty hot too, but you need to be a little more subtle."
            the_person "I don't want any rumours getting back to my [the_person.so_title]. That would really throw a wrench into our little affair..."
            $ mc.change_locked_clarity(15)
            "After checking again that nobody else is watching she reaches over and cups your crotch, massaging the bulge through your pants."
            the_person "Just be patient. I'll be all over this dick soon enough."
            mc.name "Alright, I think I can contain myself a little while longer."
            "She pulls her hand back and smiles."
    else:
        # the_person "Yeah? Well there's nobody around, and I'm not going to stop you."
        the_person "Oh yeah? Well then, do you want to share what all of these naughty things are? You have my attention."
        menu:
            "Feel her up":
                "You put your arms around [the_person.possessive_title]'s waist and rest your hands on her ass."
                mc.name "Well, first I want to get my hands all over your beautiful body."
                "You massage her butt. She sighs happily and leans against your body."
                the_person "What next? What do you want to do to me?"
                "You spin her around and shift your hands to her breasts, squeezing them."
                mc.name "No need to rush things. Just relax and enjoy for now..."
                call fuck_person(the_person, private = True, start_position = standing_grope, skip_intro = True) from _vt_kuudere_call_fuck_person_80
                $ the_person.call_dialogue("sex_review", the_report = _return)
                $ the_person.review_outfit()

            "Just flirt":
                $ mc.change_locked_clarity(10)
                "You put your arms around [the_person.possessive_title]'s waist and rest your hands on her ass."
                mc.name "I wish I had the time. You'll have to wait until later."
                "You massage her butt. She sighs happily and leans her weight against you."
                the_person "Aww, are you sure?"
                "You slap her ass and step back. She clings to you reluctantly before letting go."
                the_person "Fine, but don't make me wait too long, okay?"
                the_person "I have needs, and my [the_person.so_title] sure as hell isn't fulfilling them."
                mc.name "I won't make you wait long. I promise."
    return

label kuudere_flirt_response_text(the_person):
    mc.name "Hey [the_person.title], what's up. I'm bored and figured we could chat."
    "Her response is curt but polite."
    the_person "I'm fine, just occupied with my thoughts. I'm not one for idle conversation, but I suppose we could exchange pleasantries."
    if the_person.is_affair:
        the_person "If you're bored, we could engage in something more stimulating together."
        the_person "When do you propose we meet?"

    elif the_person.is_girlfriend:
        the_person "It would be nice to spend time together, away from the mundanity of daily life."
        the_person "When will you make time for me?"

    elif the_person.love < 40:
        if the_person.effective_sluttiness() > the_person.love:
            the_person "Bored, are you? Perhaps I can alleviate that."
        else:
            the_person "Boredom is a trivial concern, don't you think?"

    else:
        if the_person.effective_sluttiness() > the_person.love:
            the_person "Bored, are you? Well, I can think of ways to occupy our time."
            the_person "What seems to interest you?"
        else:
            the_person "Bored, you say? Perhaps we can find a more suitable way to pass the time."
            the_person "What would you like to discuss?"
    return

label kuudere_condom_demand(the_person):
    the_person "You should probably put on a condom, you know. It's just a sensible precaution."
    the_person "I know it's not exactly what you had in mind, but trust me, it's better this way."
    return

label kuudere_condom_ask(the_person):
    the_person "Condoms? I suppose it's wise to use them."
    if not the_person.on_birth_control:
        the_person "I'm not on any birth control, so it's better to be safe."
        $ the_person.update_birth_control_knowledge()
    elif the_person.wants_creampie:
        the_person "But if you really want to cum inside me, we should still use a condom."
        the_person "It's less fun than fucking raw, but it's better than risking an unplanned pregnancy."
        $ the_person.discover_opinion("creampies")
    else:
        the_person "So, condom or withdrawal? I trust you to pull out if we choose the latter."
    return

label kuudere_condom_bareback_ask(the_person):
    if the_person.wants_creampie:
        if the_person.is_infertile:
            the_person "You aren't thinking of wearing a condom, are you? That's unnecessary. I'm fine with you cumming inside me."
            the_person "Besides, I don't have any issues with getting pregnant."
        elif the_person.on_birth_control:
            the_person "You aren't thinking of wearing a condom, are you? Fuck that, I'm on the pill."
            the_person "You can cum right inside me, no worries."
            $ the_person.update_birth_control_knowledge()
        else:
            the_person "You don't need a condom, do you? I'd rather feel your bare skin against mine."
            if not the_person.knows_pregnant:
                the_person "I don't care about the risks, it's worth it for the sensation."
            the_person "So go ahead, fuck me bareback."
            the_person "It'll be our little secret."
        $ the_person.discover_opinion("creampies")
    else:
        the_person "Don't bother with a condom [the_person.mc_title], I want to feel you raw."
        if not the_person.knows_pregnant:
            the_person "I don't care about the risks, it's worth it for the sensation."
        else:
            the_person "So go ahead, fuck me bareback."
            the_person "It'll be our little secret."
    return

label kuudere_condom_bareback_demand(the_person):
    the_person "I don't care about that latex nonsense. Just fuck me raw."
    if the_person.has_breeding_fetish: #Actively looking to get knocked up.
        if the_person.knows_pregnant:
            the_person "I want to feel you cum inside me. Get me pregnant already!"
        elif the_person.is_infertile:
            the_person "It doesn't matter if I can't get pregnant. I still want to feel you deep inside me."
        else:
            the_person "I want to feel you cum inside me and knock me up. Don't you dare use a condom."
    elif the_person.wants_creampie: #Just likes raw sex
        if the_person.is_infertile:
            the_person "I don't care if I can't get pregnant. I still want to feel you deep inside me."
        elif the_person.on_birth_control:
            the_person "I'm on the pill, so it's fine. Fuck me raw and cum inside me."
            $ the_person.update_birth_control_knowledge()
        else:
            the_person "I don't care about birth control. I want to feel you deep inside me."
    else:
        if the_person.is_infertile:
            the_person "I don't care if I can't get pregnant. I still want to feel you deep inside me."
        elif the_person.on_birth_control:
            the_person "I'm on the pill, so it's fine. Fuck me raw."
            $ the_person.update_birth_control_knowledge()
        else:
            the_person "I don't care about birth control. I want to feel you deep inside me."
    return

label kuudere_cum_face(the_person):
    if the_person.has_cum_fetish or the_person.obedience > 180:
        the_person "A curious expression crosses [the_person.title]'s face as she examines the semen on her lips."
        "She doesn't seem disgusted or embarrassed, just... interested."
        if the_person.has_cum_fetish or the_person.effective_sluttiness() > 60 or the_person.opinion.cum_facials > 0:
            the_person "What do you think? Is this a good look [the_person.mc_title]?"
            "[the_person.title] licks her lips, moving a few drops of your semen that had run down her face with her fingers to her mouth."
        else:
            the_person "I hope you had a good time [the_person.mc_title]. It certainly seems like you did."
            "[the_person.title] runs a finger along her cheek, wiping away some of your semen."
    else:
        if the_person.effective_sluttiness() > 80 or the_person.opinion.cum_facials > 0:
            the_person "Mmm, that's such a good feeling. Do you think I look cute like this?"
            "[the_person.title] runs her tongue along her lips, then smiles and laughs."
        else:
            the_person "Whew, glad you got that over with. Take a good look while it lasts."
    return

label kuudere_cum_mouth(the_person):
    if the_person.has_cum_fetish or the_person.obedience > 180:
        if the_person.has_cum_fetish or the_person.effective_sluttiness() > 60 or the_person.opinion.drinking_cum > 0:
            the_person "I suppose it's a unique flavor, [the_person.mc_title]."
        else:
            the_person "Hmm, that was an interesting sensation, [the_person.mc_title]."
    else:
        the_person "Your taste is... unusual, [the_person.mc_title]. I don't think I'll get used to it anytime soon."
    return

label kuudere_cum_pullout(the_person):
    # Lead in: "I'm going to cum!"
    if mc.condom:
        if the_person.wants_creampie and not the_person.has_taboo("condomless_sex"): #TODO: FIgure out we want any more requirements for this to fire.
            if the_person.knows_pregnant:
                the_person "Fine... Cum inside me."
                "She seems resigned to her fate."
            elif the_person.on_birth_control:
                the_person "Oh, just this once... Cum inside me."
                "She closes her eyes, trying to enjoy the moment."
            else:
                the_person "I can't... I can't think straight!"
                "She moans desperately."
                the_person "Fine... Cum inside me."
                $ the_person.update_birth_control_knowledge()
                the_person "I want you to get me pregnant and fuck my life up!"
            menu: #TODO: Add a variant of this normally so you can stealth a girl (don't do that in real life, it's super fucked up).
                "Take off the condom":
                    "You don't have much time to spare. You pull out, barely clearing her pussy, and pull the condom off as quickly as you can manage."
                    $ mc.condom = False
                    $ use_condom = False  # prevent putting on a new condom next sex loop
                "Leave it on":
                    "You ignore [the_person.possessive_title]'s request and continue to thrust inside her."
        else:
            the_person "I'm going to make you cum... hard."
    else:
        if the_person.wants_creampie:
            if the_person.knows_pregnant: #She's already knocked up, so who cares!
                the_person "Cum inside me... please."
            elif the_person.opinion.creampies > 0:
                "[the_person.possessive_title!c] nibbles her lip trying to hide her desperation."
                if the_person.on_birth_control: #She just likes creampies.
                    the_person "Cum inside me... I want it."
                else: #Yeah, she's not on BC and asking for you to creampie her. She's looking to get pregnant.
                    $ the_person.update_birth_control_knowledge()
                    the_person "Cum inside me... I want to get pregnant."
            elif the_person.is_infertile:
                the_person "Just cum wherever."
            elif the_person.on_birth_control: #She's on the pill, so she's probably fine
                $ the_person.update_birth_control_knowledge()
                the_person "Cum inside me... I'm on the pill."
            else: #Too distracted to care about getting pregnant or not. Oh well, what could go wrong?
                the_person "Cum... please."
        else:
            if the_person.is_infertile:
                the_person "Pull out... please."
            elif not the_person.on_birth_control: #You need to pull out, I'm not on the pill!
                $ the_person.update_birth_control_knowledge()
                the_person "Pull out... I'm not on the pill."
            elif the_person.opinion.creampies < 0:
                the_person "Pull out... I don't want you to cum inside me."
            else:
                the_person "Pull out... I need to feel your release."
                "She looks away, trying to compose herself."
    return

label kuudere_cum_condom(the_person):
    the_person "Cum inside me? I hope you're using a condom. It's not that I mind the mess, but I'd rather not clean it up afterward."
    if the_person.effective_sluttiness() > 75 or the_person.opinion.creampies > 0:
        the_person "Though, it might be an interesting experience...if the condom broke."
    return

label kuudere_cum_vagina(the_person):
    if the_person.has_taboo("creampie"):
        $ the_person.call_dialogue("creampie_taboo_break")
        $ the_person.break_taboo("creampie")
        return
    if the_person.wants_creampie:
        the_person "Hmm, I suppose it's no surprise that you know what I find acceptable... don't make a habit of it, though."
        if the_person.knows_pregnant:
            the_person "It's rather predictable, really. I do enjoy the sensation of your cum within me."
        elif the_person.is_infertile:
            the_person "Excellent. I find the sensation of your cum quite pleasing, so I'll take all of it, please."
        elif the_person.on_birth_control:
            if the_person.has_significant_other:
                the_person "Curious. Your [the_person.so_title] doesn't seem to be able to provide me with this kind of satisfaction..."
            else:
                if the_person.knows_pregnant:
                    the_person "Fortunate for me, I'm already pregnant. It seems you're not quite as skilled at contraceptives."
                elif the_person.is_infertile:
                    the_person "Well, well. It seems I'll be enjoying the taste of your cum all day, then."
                else:
                    the_person "Thankfully, I'm on the pill. It appears you have a... generous nature."
                $ the_person.update_birth_control_knowledge()
        elif the_person.effective_sluttiness() > 75 or the_person.opinion.creampies > 0:
            if the_person.has_significant_other:
                the_person "Ah, splendid. I'll just have to tell my [the_person.so_title] that it was your child..."
            else:
                the_person "Delightful. I'll worry about the consequences later. For now, just keep going."
        else:
            if the_person.has_significant_other:
                the_person "I suppose it can't be helped. I'll just have to deal with the consequences when I return to my [the_person.so_title]."
            else:
                the_person "Hmm, quite the vigorous session. I'll have to be more careful in the future."
    else: #She's angry
        if the_person.knows_pregnant:
            the_person "Well, I did ask you to pull out. But since I'm already pregnant, I suppose it's no great matter."
        elif not the_person.on_birth_control:
            if the_person.has_significant_other:
                the_person "Oh dear. [the_person.mc_title], why did you fail to pull out? My [the_person.so_title] will be most displeased."
                if the_person.kids > 0:
                    the_person "... Again."
            else:
                the_person "Oh dear, I specifically asked you to pull out. What if I were to become pregnant?"
                $ the_person.update_birth_control_knowledge()
                the_person "It seems I'll have to reconsider my birth control options, then."
        elif the_person.is_infertile:
            the_person "Ah, well. I suppose it can't be helped. But do try to be more careful in the future."
        elif the_person.has_significant_other:
            the_person "I specifically asked you to pull out. I have a [the_person.so_title] to consider, after all."
            $ the_person.update_birth_control_knowledge()
            the_person "Please, be more cautious in the future."
        elif the_person.opinion.creampies < 0:
            the_person "Hmm, quite the mess you've made. I suppose I should be more careful next time."
        else:
            the_person "I asked you to pull out. Did you become too... carried away?"
            the_person "Please, try to be more considerate in the future."
    return

label kuudere_cum_anal(the_person):
    if the_person.has_taboo("anal creampie"):
        $ the_person.call_dialogue("anal_creampie_taboo_break")
        $ the_person.break_taboo("anal creampie")
        return

    if the_person.sluttiness > 75 or the_person.opinion.anal_creampies > 0:
        the_person "Hmm, I suppose it's no great surprise that you'd want to do this... very well, let's proceed."
    elif the_person.opinion.anal_creampies < 0:
        the_person "Oh dear, I suppose I should have expected as much... but please, be careful."
    else:
        the_person "Hmm, I suppose it's not an unreasonable request... proceed, then."
    return

label kuudere_surprised_exclaim(the_person):
    $rando = renpy.random.choice(["Ah, really?", "Well, that's interesting.", "Fascinating.", "Quite unexpected.", "I suppose that makes sense.", "Hmph.", "Hmm, I see.", "Oh dear.", "Well, well, well.", "Interesting development."])
    the_person "[rando]"
    return

label kuudere_talk_busy(the_person):
    if the_person.obedience > 120:
        the_person "I'm in the middle of something rather important, perhaps we could discuss it later, [the_person.mc_title]?"
    else:
        the_person "Hmm, I do have a few pressing matters to attend to at the moment, [the_person.mc_title]. Maybe some other time?"
    return

label kuudere_sex_strip(the_person):
    if the_person.sluttiness < 20:
        if the_person.arousal_perc < 50:
            the_person "I suppose I should remove something..."
        else:
            the_person "Ah, too many clothes are rather cumbersome. Let me rectify that."
    elif the_person.sluttiness < 60:
        if the_person.arousal_perc < 50:
            the_person "I find it rather cumbersome to be dressed like this..."
        else:
            the_person "Wait, I'd like to become a bit less... encumbered for you."
    else:
        if the_person.arousal_perc < 50:
            the_person "Allow me a brief moment to shed something. For your sake."
        else:
            the_person "Ugh, let me get out of these. I want you to feel me against you, intimately."
    return

label kuudere_sex_watch(the_person, the_sex_person, the_position):
    $ title = the_person.title if not the_person.is_stranger else "The stranger"
    if the_person.sluttiness < the_position.slut_requirement - 20:
        $ the_person.draw_person(emotion = "angry", display_transform = character_left_flipped)
        the_person "Ugh, could you two at least keep it down? This is too much."
        $ the_person.change_stats(obedience = -2, happiness = -1)
        "[title] looks away while you and [the_sex_person.fname] [the_position.verb]."
        return False
    if the_person.sluttiness < the_position.slut_requirement - 10:
        $ the_person.draw_person(display_transform = character_left_flipped)
        the_person "I don't want to hear this... Could you two at least keep it quiet?"
        $ the_person.change_happiness(-1)
        "[title] tries to avert her gaze and ignore you and [the_sex_person.fname] [the_position.verb]."
        return False
    if the_person.sluttiness < the_position.slut_requirement:
        $ the_person.draw_person(display_transform = character_left_flipped)
        if not is_watching(the_person):
            the_person "Well, I suppose if you're enjoying it, then I'll just watch..."
        $ the_person.change_slut(1, 30)
        "[title] watches while you and [the_sex_person.fname] keep [the_position.verbing]."
        return True
    if the_person.sluttiness >= the_position.slut_requirement and the_person.sluttiness < the_position.slut_cap:
        $ the_person.draw_person(display_transform = character_left_flipped)
        if not is_watching(the_person):
            the_person "Hmm, this looks interesting... I wonder what it would be like to join in?"
        $ the_person.change_slut(1, 50)
        "[title] watches you and [the_sex_person.fname] [the_position.verb]."
        return True
    $ the_person.draw_person(emotion = "happy", display_transform = character_left_flipped)
    if renpy.random.randint(0, 1) == 0:
        the_person "I suppose it's not the worst thing in the world... but you should really be more considerate, [the_sex_person.fname]."
    else:
        call watcher_position_comment(the_person, the_sex_person, the_position) from _call_watcher_position_comment_kuudere_sex_watch
    "[title] watches with a small smile while you and [the_sex_person.fname] [the_position.verb]."
    return True

label kuudere_being_watched(the_person, the_watcher, the_position):
    $ title = the_watcher.fname if not the_watcher.is_stranger else "the stranger"
    if the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #They agree you should give it to her harder
        the_person "[mc.name], be rough with me. I can handle it."
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [title] watching you and her [the_position.verb]."
    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's super slutty and doesn't care what people think.
        the_person "I bet [title] just wishes she was the one being [the_position.verb]ed by you."
    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #She's super slutty and encourages the watcher to be slutty.
        the_person "Oh god, you need to get a little of this yourself, [title]!"
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [title] watching you and her [the_position.verb]."
    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #She's into it and encouraged by the slut watching her.
        "[the_person.fname] responds to [title]."
        the_person "I'm giving him all I can right now. Any more and he's going to break me!"
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [title] watching you and her [the_position.verb]."
    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's into it but shamed by the prude watching her.
        the_person "Fuck, maybe we should go somewhere a little quieter..."
        $ the_person.change_stats(arousal = -1, slut = -1)
        "[the_person.title] seems uncomfortable with [title] nearby."
    else: #the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #They're both into it but not fanatical about it.
        "[the_person.possessive_title!c] looks directly at [title] and says..."
        the_person "Ah, now this is a party! Maybe when he's done you can tap in and take a turn!"
        $ the_person.change_stats(arousal = 1, slut = 1, max_slut = 30)
        "[the_person.title] seems more comfortable [the_position.verbing] you with [title] around."
    return

label kuudere_work_enter_greeting(the_person):
    if the_person.happiness < 80 or the_person.love < 0:
        "[the_person.title] glances at you without interest when you enter the room, her expression unchanging."
        the_person "You're here."
    elif the_person.happiness > 130:
        if the_person.sluttiness > 40:
            the_person "Hmm, [the_person.mc_title]. You've arrived. What brings you to this place?"
            "Her tone is detached, but her eyes sparkle with a hint of curiosity."
        else:
            "[the_person.title] looks up from her work and regards you with a cool, calm gaze."
            the_person "Ah, [the_person.mc_title]. You've arrived. What do you require?"
    else:
        if the_person.sluttiness > 60:
            $ the_person.draw_person(position = "stand4")
            "[the_person.title] approaches you with an indifferent air, her eyes half-lidded."
            the_person "You've come. Is there something you need?"
            "Her voice is low and smooth, but it lacks warmth."
        else:
            the_person "Ah, [the_person.mc_title]. You're here. What do you want?"
    return

label kuudere_date_seduction(the_person):
    if the_person.is_girlfriend:
        "You notice [the_person.possessive_title!c] staring at you with an intense expression."
        the_person "Hey, that was a great time, wasn't it?"
        "Her voice is calm and collected, yet there's a hint of longing in her words."
        $ mc.change_locked_clarity(30)
        if the_person.effective_sluttiness(["vaginal_sex", "condomless_sex"]) > 60 and the_person.wants_creampie and the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex >= 0 and the_person.opinion.creampies >= 0 and not the_person.on_birth_control and not the_person.knows_pregnant:
            if the_person.opinion.creampies > 0: #No condoms, loves creampies, she's basically asking you to knock her up. So... have her ask you to knock her up!
                the_person "Let's go back to my place and fuck until you knock me up."
                the_person "You know, I think I'd look good with a big belly, don't you? You can make that happen."
            else:
                the_person "Let's go back to my place, I want you to throw me on the bed and fuck me bareback."
                the_person "I like the idea of getting fucked up with your cock."
        elif the_person.effective_sluttiness(["vaginal_sex", "condomless_sex"]) > 60 and the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex > 0:
            the_person "Let's go back to my place. You can fuck me any way you want, as long as you follow my one simple rule: No condoms."
            the_person "I like the way it feels getting fucked bareback, it's just... different."
        elif the_person.effective_sluttiness(["vaginal_sex"]) > 50 and the_person.opinion.vaginal_sex > 0:
            the_person "Let's go back to my place, alright? I want to get my little pussy pounded, and you're the guy for the job."
            the_person "Do you think you can do that? Can you come fuck me up with that big cock?"
        elif the_person.effective_sluttiness(["anal_sex"]) > 60 and the_person.opinion.anal_sex > 0:
            the_person "Let's go back to my place, alright? I want to get my ass stretched out tonight, and you've got the cock that I love."
            the_person "Doesn't that sound like a fun way to end our night together?"
        elif the_person.effective_sluttiness(["sucking_cock"]) > 40 and the_person.opinion.giving_blowjobs > 0:
            the_person "Let's go back to my place. I want to reward you for giving me such a wonderful night."
            the_person "How does a nice long, sloppy blowjob sound? I think it sounds pretty fun."
        elif the_person.effective_sluttiness() > 40 and the_person.opinion.being_covered_in_cum > 0:
            the_person "Let's go back to my place. We can have some fun, and I can end this night in my favourite way..."
            "She licks her lips playfully."
            the_person "Covered in your hot cum. Sound like fun?"
        elif the_person.effective_sluttiness(["touching_body"]) > 40 and the_person.opinion.giving_tit_fucks > 0 and the_person.has_large_tits:
            the_person "Let's go back to my place, then I can repay you for this wonderful night."
            the_person "I'll slide that big cock of yours between my tits and fuck it until you cum. How does that sound?"
        else: #She's not very slutty, so she leaves the invitation open to interpretation
            the_person "It doesn't have to be over yet, does it? Let's go back to my place and we can keep the fun going."
            "She gives you a calm, knowing smile."

    elif the_person.is_affair:
        the_person "So my [the_person.so_title] won't be home tonight, I was thinking..."
        "Her lips curl into a sly smile as she reaches down and cups your crotch, rubbing it gently through your pants."
        $ mc.change_locked_clarity(40)
        if the_person.wants_creampie and the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex >= 0 and the_person.opinion.creampies >= 0 and not the_person.on_birth_control and not the_person.knows_pregnant:
            if the_person.opinion.creampies > 0: #No condoms, loves creampies, she's basically asking you to knock her up. So... have her ask you to knock her up!
                the_person "Let's go back to my place so you can pin me to the bed and creampie me all night long."
                the_person "All that cum in my unprotected pussy and I'm sure to get knocked up. Just thinking about it is making me wet!"
            else:
                the_person "Let's go back to my place. You can pin me to the bed and fuck me bareback all night long."
                the_person "Cum inside me, over my face, whatever. I just want you to fuck me up with your cock."
        elif the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex > 0:
            # the_person "Do you want to come over to my place and fuck me all night long? No condoms allowed."
            the_person "Let's go back to my place. You can fuck me all night, any way you want, as long as you follow one simple rule."
            the_person "No condoms. If you're fucking me you're doing it bareback."
        elif the_person.opinion.vaginal_sex > 0:
            the_person "Let's go back to my place and you can pound my tight fucking pussy until I'm just a quivering, cum-covered wreck."
            the_person "How does that sound? Do I have your attention?"
        elif the_person.opinion.anal_sex > 0:
            the_person "Let's go back to my place so you can stretch out my tight little asshole with that monster cock of yours."
        elif the_person.opinion.giving_blowjobs > 0:
            the_person "Let's go back to my place, and you can choke me out on that monster cock of yours."
            the_person "I want to throat it so fucking deep. I want to feel your balls against my chin when you cum."
        elif the_person.opinion.being_covered_in_cum > 0:
            the_person "Let's go back to my place, and you can spend all night glazing me like a slutty donut."
            the_person "I want to be absolutely covered in your sperm, head to toe."
        elif the_person.opinion.giving_tit_fucks > 0 and the_person.has_large_tits:
            the_person "Let's go back to my place so I can wrap these big fucking tits around your big fucking cock."
            the_person "Then I'll fuck that thing until you explode. Sound like fun?"
        elif the_person.opinion.cheating_on_men > 0:
            the_person "Let's go back to my place, and you can do all the fucked up things I tell my husband I hate."
            the_person "He tries to treat me like a lady, but all I want to be is your cock drunk slut."
        else:
            the_person "Let's go back to my place and make him really regret leaving me alone for the night."
    elif not the_person.has_significant_other:
        $ mc.change_locked_clarity(20)
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                the_person "I've had a blast [the_person.mc_title], but there are a few more things I'd like to do with you. Want to come back to my place and find out what they are?"
            else:
                the_person "You've been a blast [the_person.mc_title]. Want to come back to my place, have a few drinks, and see where things lead?"
        else:
            if the_person.love > 40:
                the_person "Tonight's been amazing [the_person.mc_title], I just don't want to say goodbye. Do you want to come back to my place and have a few drinks?"
            else:
                the_person "This might be crazy, but I had a great time tonight and you make me a little crazy. Do you want to come back to my place and see where things go?"
    else:
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                $ mc.change_locked_clarity(20)
                the_person "I've had a blast [the_person.mc_title], but I'm not done with you yet. Want to come back to my place?"
                the_person "My [the_person.so_title] won't be home until morning, so we would have plenty of time."
            else:
                $ mc.change_locked_clarity(20)
                the_person "This might be crazy, but do you want to come back to have another drink with me?"
                the_person "My [the_person.so_title] is stuck at work and I don't want to be left all alone."
        else:
            if the_person.love > 40:
                $ mc.change_locked_clarity(20)
                the_person "You're making me feel crazy [the_person.mc_title]. Do you want to come have a drink at my place?"
                the_person "My [the_person.so_title] won't be home until morning, and we have a big bed you could help me warm up."
            else:
                $ mc.change_locked_clarity(20)
                the_person "This is crazy, but would you want to have one last drink at my place? My [the_person.so_title] won't be home until morning..."
    return

label kuudere_sex_end_early(the_person):
    if the_person.sluttiness > 50:
        if the_person.love > 40:
            if the_person.arousal_perc > 60:
                the_person "You're done already? Hmm, I suppose I'll just have to find another way to release this pent-up energy then..."
            else:
                the_person "Well, that was quick. I guess I'll just have to find some other way to entertain myself now..."
        else:
            if the_person.arousal_perc > 60:
                the_person "Hmph, I'm still feeling rather... aroused, if you must know."
            else:
                the_person "I suppose that was enough, but I would've preferred a longer session."
    else:
        if the_person.love > 40:
            if the_person.arousal_perc > 60:
                the_person "Well, that was quite the experience, [mc.name]."
            else:
                the_person "I hope you enjoyed yourself."
        else:
            if the_person.arousal_perc > 60:
                the_person "Phew, that was quite intense."
            else:
                the_person "Good, now we can move on to other things."
    return

label kuudere_sex_take_control(the_person):
    if the_person.arousal_perc > 60:
        the_person "Hmph, I don't think so. You're not getting away that easily, [mc.name]."
    else:
        the_person "Hold up, you think you're just going to leave me like this? I'm not done yet!"
    return

label kuudere_sex_beg_finish(the_person):
    the_person "Stop teasing me, [mc.name]. I'm on the verge of... something. Just let me finish, please."
    return

label kuudere_sex_review(the_person, the_report):
    $ comment_position = the_person.pick_position_comment(the_report)
    if comment_position is None:
        return #You didn't actually do anything, no need to comment.
    $ used_obedience = the_report.get("obedience_used", False) #True if a girl only tried a position because you ordered her to.
    $ the_person.draw_person()  # make sure she stands up for talking with you
    #She's worried about her SO finding out because it was in public
    if the_report.get("was_public", False) and the_person.has_significant_other and the_person.opinion.cheating_on_men <= 0: #It was public and she cares.
        if the_person.is_affair: #Dialogue about her being into it, but you can't do this in case she gets caught.
            the_person "Hmph, that was quite the experience. But we should probably be more careful next time, alright?"
            the_person "Someone might tell my [the_person.so_title] about this."
        elif used_obedience:
            the_person "Ugh, everyone is watching us... I'm so embarrassed."
        else:
            the_person "Oh no, everyone saw us... This is going to get back to my friends, isn't it?"
    #She's single, but worried that you did in public.
    elif the_report.get("was_public", False) and (the_person.effective_sluttiness()+10*the_person.opinion.public_sex < comment_position.slut_cap):
        if used_obedience:
            the_person "Ugh, everyone is watching us... I'm so embarrassed."
        else:
            the_person "Oh no, everyone saw us... This is going to get back to my friends, isn't it?"
    elif the_report.get("girl orgasms", 0) > 2:
        if used_obedience:
            the_person "Wow... That was quite the experience... I think I'm still shaking."
            mc.name "I'm glad you enjoyed it."
            the_person "Yeah, me too... But let's keep this between us, alright?"
        else:
            the_person "Wow, I didn't expect to enjoy that so much... Thanks for that."
            "She smiles shyly, still a bit surprised by her own reaction."
        call sex_review_trance(the_person) from _call_sex_review_trance_kuudere_sex_review
    #No special conditions, just respond based on how orgasmed and how slutty the position was.
    elif the_report.get("girl orgasms", 0) > 0 and the_report.get("guy orgasms", 0) > 0: #You both came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position cap, it was tame
            the_person "Hmm, that was nice... But I think we could try something more daring next time."
            the_person "Doesn't that sound like fun? I'm a little excited just thinking about it."
        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "Ah, that was just what I needed! I think we're very compatible [the_person.mc_title]."
            the_person "Let's do it again some time soon, okay?"
        elif used_obedience: #She only did it because she was commanded
            the_person "Ugh, I... I didn't think I was going to enjoy that so much."
            mc.name "Aren't you going to thank me? You obviously had a good time."
            the_person "Shut up... I'm not admitting to anything."
        else: # She's surprised she even tried that.
            the_person "Wow, that was quite the experience... I didn't expect that."
            the_person "But don't think that means I'm going to do that again anytime soon."
    elif the_report.get("girl orgasms", 0) > 0: #Only she came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            the_person "Hmm, that was quite the ride... But I think I can top that next time."
            the_person "I've got a few ideas that are going to blow your mind."
            "She smirks, already planning your next encounter."
        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "Wow, that was quite something... I'll repay the favor next time, alright?"
        elif used_obedience: #She only did it because she was commanded
            the_person "Ugh, I... I didn't expect to enjoy that so much."
            mc.name "Some other time. I just wanted to see what you look like when you cum."
            the_person "Shut up... I'm not admitting to anything."
        else: # She's surprised she even tried that.
            the_person "Wow, that was quite the experience... Thanks for that."
            the_person "You're probably tired after all that work. I promise I'll repay the favour next time, okay?"
    elif the_report.get("guy orgasms", 0) > 0: #Only you came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            the_person "Hmph. Tired already? I suppose that's to be expected."
            mc.name "Sorry, I'll make it up to you next time."
            the_person "I expect that much. I have some ideas that should make both of us scream. Interested?"
            mc.name "Yeah, I could get behind that."
        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "You're already done? That's... disappointing."
            mc.name "Sorry, I'll make it up to you next time."
            the_person "You better. I won't be so easily pleased next time, I assure you."
        elif used_obedience: #She only did it because she was commanded
            the_person "I suppose we're done for now. Good."
            mc.name "Yeah, that's all for now."
            "She nods, her expression unreadable."
        else:  # She's surprised she even tried that.
            the_person "Phew, that was... intense. I think I got a little carried away."
        the_person "Probably a good idea we stop, before we take this too far."
    elif the_person.energy < 10: #Nobody came and she's tired
        the_person "Sorry, but I'm too tired. We can try again another time."
        mc.name "No problem, we'll continue this another time."
    else: #Nobody came.
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            the_person "You're done already? How uninteresting."
            "She shrugs, her expression neutral."
        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "We're stopping already? What a shame."
            mc.name "Sorry [the_person.title], I'll have to make it up to you some other time."
            the_person "You'd better. I won't be so easily impressed next time."
        elif used_obedience: #She only did it because she was commanded
            the_person "That's all? I suppose I shouldn't be surprised."
            mc.name "You aren't disappointed, are you?"
            the_person "No, I just... Thought this was all going to be more... interesting."
            the_person "Whatever, it doesn't matter."
        else:  # She's surprised she even tried that.
            the_person "I suppose we should stop before we do something foolish."
            the_person "I don't want to get carried away and ruin the mood."
    # Gave creampie while she is not on birth control (extra dialogue when she could get pregnant)
    if the_report.get("creampies", 0) > 0 and not the_person.on_birth_control and not the_person.knows_pregnant:
        the_person "Oh, well played, [mc.name]. You really know how to make a girl feel special."

    $ del comment_position
    return

## Role Specific Section ##
label kuudere_improved_serum_unlock(the_person):
    mc.name "[the_person.title], now that you've had some time to get used to the lab there is something I want to talk to you about."
    the_person "Sure, what can I help you with?"
    mc.name "Our R&D up to this point has been based on my old notes from university."
    mc.name "There were some unofficial experiment results that suggested the effects might be enhanced by sexual arousal."
    "[the_person.title] nods her understanding."
    the_person "Ah, so you had noticed that too? I have a hypothesis that an orgasm opens chemical receptors that are normally blocked."
    mc.name "What else can we do if we assume that is true? Does that open up any more paths for our research?"
    the_person "If it's true I could leverage the effect to induce greater effects in our subjects."
    "[the_person.possessive_title!c] thinks for a long moment, then smiles mischievously."
    the_person "But we'll need to do some experiments to be sure."
    mc.name "What sort of experiments?"
    the_person "I want to take a dose of serum myself, and you can record the effects."
    the_person "Then I'll make myself cum, and we can compare the effects after."
    mc.name "Do you think that's a good idea?"
    the_person "Not entirely, no. But we can't trust anyone else with this information if we're right."
    the_person "We might be able to make progress by brute force, but this is a chance to catapult our knowledge to another level."
    the_person "A finished dose of serum that raises my Suggestibility. The higher it gets my Suggestibility the better, but any amount should do."
    the_person "Then we'll just need some time and some privacy for me to see what sort of effects my orgasms will have."
    return



#
# label kuudere_improved_serum_unlock(the_person):
#     mc.name "[the_person.title], now that you've had some time in the lab there's something I wanted to talk to you about."
#     the_person "Okay, how can I help?"
#     mc.name "All of our research and development up until this point has been based on the limited notes I have from my university days. I'm sure there's more we could learn, and I want you to look into it for me."
#     "[the_person.title] smiles mischievously."
#     the_person "Well, I've got an idea in mind. It's risky, but I think it could really push our research to a new level."
#     mc.name "Go on, I'm interested."
#     the_person "Our testing procedures focus on human safety, which I'll admit is important, but it doesn't leave us with much information about the subjective effects of our creations."
#     the_person "What I want to do is take a dose of our serum myself, then have you record me while you run me through some questions."
#     return

## Taboo break dialogue ##
label kuudere_kissing_taboo_break(the_person):
    the_person "So we're doing this, huh?"
    mc.name "I guess we are. What do you think?"
    the_person "It's about time, I've wanted to make out with you for a long time."
    if the_person.effective_sluttiness() >= 30:
        the_person "I've been waiting for this moment, and I'm not going to let it pass by without enjoying every second of it."
    else:
        the_person "I don't know about this [the_person.mc_title], do you think we're taking this too fast?"
        mc.name "Are you scared?"
        the_person "No! Just... Nervous. Excited, maybe."
        mc.name "Then just trust me."
    return

label kuudere_touching_body_taboo_break(the_person):
    the_person "So you're going to try something like this, huh?"
    mc.name "Yeah, I've been thinking about it for a while."
    the_person "Well, I'll be honest. I'm not really one for physical contact, but if it's something you really want..."
    mc.name "It's not just that. I think there's something between us, and I want to explore it."
    the_person "Hmm. You're very forward, aren't you?"
    mc.name "Maybe. But I'm not afraid of what others might think, and I trust you."
    the_person "That means a lot to me. But I still need some convincing."
    mc.name "I'll do my best."
    the_person "Alright, then show me."
    "You slowly start to touch her, and she doesn't pull away. Instead, she seems to be considering your advances."
    the_person "You know, I'm not used to this kind of thing. But I have to admit, it's kind of... nice."
    mc.name "I'm glad to hear that."
    the_person "Yeah, me too. But let's not get too carried away, okay? I'm still not sure about all of this."
    mc.name "Of course. We can take it slow."
    return

label kuudere_touching_penis_taboo_break(the_person):
    the_person "So you're really going to do this, huh? You're not one for subtle hints, are you?"
    mc.name "Not when I'm this excited. Besides, I think we both know you're curious."
    the_person "Curious? Maybe a little. But I'm not just going to jump into something without thinking about it."
    mc.name "I understand that. But I need you to trust me. Just touch it for a second, and if you don't like it, we can stop."
    the_person "Alright, but if I don't like it, I'm not promising anything."
    mc.name "Fair enough."
    "[the_person.possessive_title!c] slowly reaches out and touches your penis. She seems surprised by its size and hardness."
    the_person "Wow, you're really... well-endowed, aren't you?"
    mc.name "I think you'll find it's more than just size that matters."
    the_person "Hmm, we'll see about that."
    return

label kuudere_touching_vagina_taboo_break(the_person):
    the_person "So you think you're ready to see what you've been missing, huh? You're not one for hesitation, are you?"
    mc.name "I've been wanting to do this for a while now. Just touch me."
    the_person "Hmm, I suppose I can oblige. But don't think this means I'm going to start being all lovey-dovey or anything."
    mc.name "Fair enough. Just touch me for a second and then we'll see."
    "The_person slowly reaches out and touches your genitals. She seems to be hesitating, but then her expression changes and she looks more interested."
    the_person "Oh... wow. I didn't think I'd like that."
    mc.name "I told you it would feel good."
    the_person "Yeah, you did. But I didn't expect it to feel... like this."
    mc.name "Like what?"
    the_person "Like... something I want more of."
    mc.name "Really?"
    the_person "Yeah. But don't get any ideas. We're just exploring, okay?"
    mc.name "Okay."
    return

label kuudere_sucking_cock_taboo_break(the_person):
    mc.name "I want you to do something for me."
    the_person "Oh yeah? What do you want me to do to you?"
    mc.name "I want you to suck on my cock."
    the_person "You want me to... do that? Right now?"
    mc.name "Yes, if you're willing."
    the_person "Hmm, I don't know. It's not something I usually do."
    mc.name "I understand. But I think it would feel good, and it's something we both want."
    the_person "I suppose that's true. Alright, I'll give it a try."
    "She kneels down in front of you, her eyes locked on your cock. She takes it in her hand and starts to stroke it slowly."
    the_person "Hmm, this isn't so bad. It's actually quite nice."
    mc.name "I'm glad you think so. Just keep going, and see how it feels."
    "She continues to suck and stroke you, her eyes never leaving yours. You can see the hesitation in her eyes, but she's determined to see this through."
    return

label kuudere_licking_pussy_taboo_break(the_person):
    mc.name "I want to taste your pussy [the_person.title]. Are you ready?"
    the_person "Hmm, I don't know if I'm ready for that. It's a little... intimate, isn't it?"
    mc.name "Yes, it is. But I think it's something we both want. And it'll be worth it, I promise."
    the_person "Hmm, I suppose you're right. Alright, but just a little, okay?"
    mc.name "Just a little. I'll make sure you enjoy it."
    "She slowly parts her legs, and you lean in to taste her. She gasps and closes her eyes."
    the_person "Oh... wow. That's... nice."
    mc.name "I told you it would be worth it."
    the_person "Yeah, you did. But I didn't expect it to feel... so good."
    mc.name "I know, right? It's like a whole new world."
    the_person "Hmm, maybe it is. But we should probably stop now, before we get carried away."
    mc.name "Alright, for now. But I promise, this isn't the last time we'll do this."
    return

label kuudere_vaginal_sex_taboo_break(the_person):
    mc.name "Are you ready for this?"
    the_person "Hmm, I think so. But don't go too fast, okay? I want to enjoy this."
    mc.name "I'll try my best. But you have to promise me you'll tell me if it hurts or if you need me to stop."
    the_person "I promise. Now come on, get it over with already!"
    "You slowly push inside her, and she moans as you fill her. She looks up at you, her eyes half-closed in pleasure."
    the_person "Oh... that's... nice. Keep going, but don't go too fast."
    mc.name "I'll try my best. But you have to promise me you'll tell me if you want me to stop."
    the_person "I promise. Now come on, show me what you've got!"
    "You start to move faster, and she starts to moan louder. She grabs onto your arms, her nails digging into your skin."
    the_person "Oh fuck, yes! Keep going, don't stop!"
    mc.name "I won't stop until we're both done."
    return

label kuudere_anal_sex_taboo_break(the_person):
    mc.name "Are you ready for this?"
    the_person "Hmm, I think so. But don't go too fast, okay? I want to enjoy this."
    mc.name "I'll try my best. But you have to promise me you'll tell me if it hurts or if you need me to stop."
    the_person "I promise. Now come on, get it over with already!"
    "You slowly push inside her, and she moans as you fill her. She looks up at you, her eyes half-closed in pleasure."
    the_person "Oh... that's... nice. Keep going, but don't go too fast."
    mc.name "I'll try my best. But you have to promise me you'll tell me if you want me to stop."
    the_person "I promise. Now come on, show me what you've got!"
    "You start to move faster, and she starts to moan louder. She grabs onto your arms, her nails digging into your skin."
    the_person "Oh fuck, yes! Keep going, don't stop!"
    mc.name "I won't stop until we're both done."
    return

label kuudere_condomless_sex_taboo_break(the_person):
    if the_person.knows_pregnant:
        the_person "That's pretty hot."
        if the_person.wants_creampie:
            the_person "It would be so easy for you to cum inside me though."
            the_person "So easy for you to pump my little cunt full of hot cum..."
            "She doesn't sound like she would mind very much at all."
        else:
            the_person "Please cover me with all your hot cum."
    elif the_person.opinion.bareback_sex > 0:
        the_person "That's pretty hot."
        if the_person.on_birth_control:
            the_person "I'm on the pill, so you don't need to worry about cumming inside me."
            $ the_person.update_birth_control_knowledge()
        elif the_person.wants_creampie:
            the_person "It would be so easy for you to cum inside me though."
            the_person "So easy for you to pump my little cunt full of hot cum..."
            "She doesn't sound like she would mind very much at all."
        elif the_person.opinion.creampies < 0:
            the_person "You better make sure you pull out though. I'd be pissed if you got me knocked up."
        else:
            the_person "You'll need to pull out so you don't knock me up then. Got it? Good."
    elif the_person.love > 60:
        if the_person.on_birth_control:
            the_person "I suppose it could be a nice change of pace."
            the_person "I'm on the pill, so there's no need to worry about pregnancy."
            $ the_person.update_birth_control_knowledge()
        elif the_person.wants_creampie:
            the_person "I guess if I can't trust you I can't trust anyone. You make me make terrible decisions, you know that?"
            the_person "Well fuck it, if we're doing this I want you to go the whole nine yards and finish inside me."
            mc.name "Are you on the pill?"
            "She shakes her head."
            the_person "Of course not. If we're fucking raw I want you to be trying to get me knocked up every single time."
            $ the_person.update_birth_control_knowledge()
        elif the_person.opinion.creampies < 0:
            the_person "I guess if I can't trust you I can't trust anyone. You make me make terrible decisions, you know that?"
            the_person "You'll need to pull out though. If you get me knocked up there's no way we're ever doing it unprotected again."
        else:
            the_person "I guess if I can't trust you I can't trust anyone. You make me make terrible decisions, you know that?"
            if the_person.kids == 0:
                the_person "I need you to pull out though. I'm not quite ready to be a mother, even with you."
            elif the_person.kids == 1:
                the_person "I need you to pull out though. I've already got a kid, I don't need another one."
            else:
                the_person "I need you to pull out though. I've already got kids, I don't need another one."
    else:
        if the_person.on_birth_control:
            the_person "Yeah, you want to fuck me raw? Well, I'm on the pill, so why not? It's not like I'm going to end up pregnant."
            $ the_person.update_birth_control_knowledge()
        elif the_person.has_taboo("vaginal_sex"):
            the_person "You really don't think we should use a condom? I'm not on the pill, aren't you worried about knocking me up?"
            $ the_person.update_birth_control_knowledge()
            the_person "Or is this your master plan to sneak a baby into me?"
            mc.name "I promise I'll pull out. Don't you want our first time together to be special?"
            "She rolls her eyes and sighs."
            the_person "God damn it, now you're getting me all sentimental. Fine, you don't need to put anything on."
            the_person "But you better fucking pull out, understand? Good."
        else:
            the_person "You're sure about this? I'm not on the pill and I don't want to end up pregnant."
            $ the_person.update_birth_control_knowledge()
            the_person "Or is this just some sort of thrill for you?"
            mc.name "It'll feel so much better without anything between us."
            the_person "Hmm, alright then. But don't say I didn't warn you."
    return

label kuudere_underwear_nudity_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > 30 - (the_person.opinion.skimpy_outfits * 5):
        the_person "Hmm, you want to see me in my underwear, huh? Suit yourself."
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "Come on, let's get this off."
        else:
            mc.name "Like I said, I've already seen you naked. What's the big deal?"
        the_person "Yeah, well, some people like to keep things classy. Your choice."
    elif the_person.love > 15:
        the_person "Oh, you want to get cozy, huh? Fine by me."
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "Well then let's stop wasting time and get your [the_clothing.display_name] off."
        else:
            the_person "If you insist. But remember, I'm only doing this for you."
            mc.name "Well let's make more memories and get your [the_clothing.display_name] off."
    else:
        the_person "If you take my [the_clothing.display_name] I'll only have my underwear on, you know that?"
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "Yeah, that's kind of the point."
            "She shakes her head and laughs to herself."
            the_person "Oh [the_person.title], what have you gotten yourself into! Come on, let's do this before I chicken out!"
        else:
            mc.name "Yeah, that's kind of the point. I've already seen you naked, so what are you worrying about?"
            the_person "Whatever, I guess you're right. Come on, let's get it off."
    return

label kuudere_bare_tits_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > (40 - the_person.opinion.showing_her_tits * 5):
        the_person "You finally want a look at my tits [the_person.mc_title], huh?"
        if the_person.has_large_tits:
            "She shrugs off her [the_clothing.display_name] to reveal the [the_person.tits_description] hidden underneath, barely contained."
        else:
            "She shrugs off her [the_clothing.display_name] to reveal her [the_person.tits_description]."
        the_person "What took you so long to ask?"
        if the_person.has_large_tits:
            mc.name "No time like the present, right? Let's get those puppies out where I can enjoy them."
        else:
            mc.name "No time like the present, right? Let's get those cute little things out."

    elif the_person.love > 25:
        the_person "Ready to see my tits [the_person.mc_title]?"
        if the_person.has_large_tits:
            "She casually shrugs off her [the_clothing.display_name], revealing the [the_person.tits_description]."
        else:
            "She shrugs off her [the_clothing.display_name], revealing her [the_person.tits_description]."
        mc.name "Oh yeah, I'm ready."
        the_person "Let 'em out then, and have fun."

    else:
        the_person "Wait a second! Jesus, you should at least ask a girl before you try and put her tits on full display."
        mc.name "Come on, don't you want to show them off? I bet they look great."
        the_person "Oh, they do. I just... Feel a little self-conscious about being naked around you, alright?"
        mc.name "There's no need to be, just relax and let me take your [the_clothing.display_name] off for you."
        the_person "Oh man, what are you getting me into [the_person.mc_title]? Fine, let's do it!"
    return

label kuudere_bare_pussy_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > (50 - the_person.opinion.showing_her_ass * 5):
        the_person "I suppose you want to get me out of my [the_clothing.display_name]."
    elif the_person.love > 35:
        the_person "You want to get me out of my [the_clothing.display_name] to see my pussy?"
        if the_person.has_taboo("touching_vagina"):
            mc.name "Yes, that's the plan."
            the_person "Well... I suppose it was inevitable. Alright, go ahead."
        else:
            mc.name "I've already felt it, so I might as well see it."
            the_person "I suppose you're right. Go on then."
    else:
        the_person "You're already trying to get me out of my [the_clothing.display_name], huh?"
        if the_person.has_taboo("touching_vagina"):
            mc.name "Yes, I am. Do you have a problem with that?"
            the_person "Well... Maybe if you ask nicely."
            mc.name "[the_person.title], may I please remove your [the_clothing.display_name] and take a look at your pussy?"
            the_person "You're such a charmer. Of course you can."
        else:
            mc.name "Yes, I am. I've already touched your pussy, now I want to see it."
            the_person "Oh, you're such a charmer. Alright then, what are you waiting for?"
    return


#==================================================================



#==================================================================
# update all the following the_person and actions with kuudere personality. Remember the_person is female, and mc.name is male. Use Reina Aharen from Aharen-San for ideas:```

# label kuudere_facial_cum_taboo_break(the_person):

#     return

# label kuudere_mouth_cum_taboo_break(the_person):

#     return

# label kuudere_body_cum_taboo_break(the_person):

#     return


label kuudere_creampie_taboo_break(the_person):
    if the_person.wants_creampie:
        if the_person.knows_pregnant:
            the_person "Interesting... fill me with your seed."
            "She gazes at you with a cool, detached expression."

        elif the_person.on_birth_control:
            if the_person.has_significant_other:
                the_person "I'm such a terrible [the_person.so_girl_title], but I needed this."
                the_person "My partner would understand, though. A woman's desires must be satisfied."

            else:
                the_person "It's about time I got what I wanted."
                the_person "I finally found someone to satisfy my desires."

            "She raises an eyebrow."
            the_person "Are you ready for another round? I'm not finished with you yet."

        elif the_person.effective_sluttiness() > 75 or the_person.opinion.creampies > 0:
            if the_person.has_significant_other:
                the_person "I've always been curious about this... fucking and getting pregnant."
                the_person "It's a taboo, but I can't help myself."
                the_person "I want to feel you inside me, pumping your seed into me."
            else:
                the_person "It's about time I took a risk like this."
                the_person "I want to feel you deep inside me, filling me with your cum."
            "She looks at you with a hint of mischief."
            the_person "Let's see if we can make this baby."

        else:
            if the_person.has_significant_other:
                the_person "Oh dear... I may have acted rashly."
                "She shrugs, as if it doesn't matter."
                the_person "But that felt so good!"

            else:
                the_person "Oh dear... I may have made a mistake."
                "She looks away, her expression unreadable."
                the_person "But it felt so good!"

            the_person "I suppose I'll just have to hope I didn't get pregnant."
            "She says it as if it's of little consequence."

    else:
        if the_person.knows_pregnant:
            the_person "Oh dear, you came inside me."

        elif not the_person.on_birth_control:
            the_person "Oh dear, did you cum inside me?"

            if the_person.has_significant_other:
                the_person "What if you got me pregnant? I would be such a terrible [the_person.so_girl_title]."

            else:
                the_person "What if I get pregnant? I'm not ready for that kind of responsibility!"

            the_person "You'll have to wear a condom if we ever do this again, I just can't risk it."

        elif the_person.has_significant_other:
            the_person "Did you really just creampie me after I told you to pull out?"
            "She sighs, her cheeks flushing."
            the_person "God, I'm such a terrible [the_person.so_girl_title]. Maybe next time I'll make you wear a condom as punishment."

        elif the_person.opinion.creampies < 0:
            the_person "Oh man, really? Ugh, I hate this feeling. Couldn't you have cum on my face or something?"

        else:
            the_person "Hey, I said to pull out!"
            "She sighs, her voice tinged with annoyance."
            the_person "Whatever, can you at least try to pull out next time?"
    return

label kuudere_anal_creampie_taboo_break(the_person):
    if the_person.opinion.anal_creampies > 0:
        if the_person.effective_sluttiness() > 75 or the_person.opinion.anal_creampies > 1:
            if the_person.has_significant_other:
                the_person "Hmm, I don't mind if it's not my [the_person.so_title]'s sperm inside me right now..."
                the_person "The warmth of your cum feels nice, like a secret we share."
            else:
                the_person "Finally! You should have done this sooner!"
                the_person "I'll just make sure to mention it in my next relationship, so they know what to expect."

            "She pants happily for a moment."
            the_person "Yeah, I'll be thinking about this all day... cum leaking out of my ass and all."

        else:
            if the_person.has_significant_other:
                the_person "Ugh, I should've told you to pull out... but I kind of like this feeling..."
                the_person "My [the_person.so_title] never does this, but you can... whenever you want."

            else:
                the_person "Promise me you'll fill me up every time... it feels so good..."
                the_person "And I love the thought of all that cum in my little ass."

    else:
        if the_person.has_significant_other:
            the_person "Ugh, [the_person.mc_title], I told you to pull out! My [the_person.so_title] will see your cum on my ass..."
            the_person "Maybe next time just shoot your load on my ass... I won't mind."

        elif the_person.opinion.anal_creampies < -1:
            the_person "Ugh, [the_person.mc_title], I said no cum inside! I'll be leaking it all day."

        else:
            the_person "Ugh, [the_person.mc_title], not inside! My ass is not a sperm bank... but it does sound kind of hot."
            the_person "Just keep it to yourself, okay? Let's keep this our little secret."
    return

label kuudere_dual_penetration_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 75:
        the_person "It's... impressive. I wasn't expecting that."
        "She seems more interested than worried."
        mc.name "I'll make sure to fill you up."
    elif the_person.love >= 60:
        the_person "This might be a bit uncomfortable. I'm not sure how you're going to fit all of that inside me..."
        mc.name "I'll manage."
        the_person "Alright... just be careful not to tear anything."
    else:
        if the_person.has_taboo("vaginal_sex"):
            the_person "I'm not sure if my ass can handle that. It's a bit tight."
            mc.name "I'll make it work."
            the_person "Okay, just... take your time, alright?"
        else:
            the_person "Deep breaths, [the_person.fname]. You can do this..."
            mc.name "Are you alright?"
            the_person "Yeah, I'm just a bit nervous. This isn't something I do every day."
            the_person "But I guess it's not every day I meet someone like you, either."
            mc.name "Hopefully that's a good thing."
            the_person "I think it is. Let's just get this over with before I change my mind."
    return

label kuudere_sleepover_yourplace_response(the_person): #Invited her over to spend the night
    if the_person.sluttiness < 80:
        the_person "Hmm, I suppose it's okay to spend the night at your place. Just don't think you can get fresh with me or anything."
    else:
        the_person "I'll come over, but don't get any ideas. I'm only staying because it's more convenient than going home."
    return

label kuudere_sleepover_herplace_response(the_person): #Spending the night at her place
    if the_person.sluttiness < 80:
        the_person "I suppose it's fine for you to spend the night at my place. We can have a quiet evening."
    else:
        the_person "Oh hell yeah, come on over and let's get freaky! I've been waiting for this all day."
    return

label kuudere_sleepover_yourplace_sex_start(the_person): #Right before sexy times at your place
    "[the_person.title] saunters over to you, her gaze somewhat indifferent."
    the_person "Alright, let's get this over with."
    return

label kuudere_sleepover_herplace_sex_start(the_person): #Right before sexy times at her place
    the_person "Are you just going to stand there staring at me? Get over here already."
    "She gives you a rather indifferent smirk."
    mc.name "Are you ready?"
    the_person "Hmph. Whatever. Just get it over with."
    "She gestures for you to come closer."
    the_person "Fine, get it done. Hurry up already."
    return

label kuudere_sleepover_impressed_response(the_person):  #If you've made her cum a lot
    the_person "Hmph, you're not so bad in bed, I suppose. Don't think it means anything, though."
    "[the_person.title] gets up and gets back into bed, leaving you to follow."
    the_person "I might just lie here for a bit. You can stay if you want."
    return

label kuudere_sleepover_good_response(the_person):  #If you've made her cum
    the_person "Hmph, that was fine, I suppose."
    "[the_person.title] gets up and gets back into bed, leaving you to follow."
    the_person "I might just lie here for a bit. You can join me if you want."
    return

label kuudere_sleepover_bored_response(the_person):  #If she hasn't cum yet
    the_person "Hmph, you call that good? I've had better."
    "[the_person.title] rolls her eyes and lies down, seemingly uninterested in continuing."
    the_person "Do whatever you want, I'm just going to rest."
    return
