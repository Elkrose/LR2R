### PERSONALITY CHARACTERISTICS ###
# tsundere (A stock love interest who is usually harsh, stern, cold or hostile to the person they like, while occasionally letting slip the warm and loving feelings hidden inside due to being shy, nervous, insecure or simply unable to help acting badly in front of the person they like. )
#"Tsundere" (JP) is a term for a character who can't be honest with their feelings of love towards their love interest so they act distant, standoffish, and stuck-up to conceal them. They can't be honest with the person they like and will pretend not to be interested in them at first. However, after becoming closer to their love interest and falling in love to the point that they can no longer deny their feelings, they will start to show a more honest and loving affectionate deredere side towards them. They will start behaving in cute ways and wanting their love interest to be intimate with them or tell them that they love them, actively seeking their affection. 
#==================================================================
# update all the following the_person and actions with tsundere personality. Remember the_person is female, and mc.name is male. Use Asuka Langley from Neon Genesis Evangelion for ideas, keep to the structure and don't use the same dialogs:```
### DIALOGUE ###

label tsundere_introduction(the_person):
    mc.name "Hey, can I talk to you for a sec?"
    "She turns around, looking annoyed."
    the_person "What do you want?"
    mc.name "I'm sorry if this is awkward, but you seem like an interesting person."
    "She rolls her eyes."
    the_person "Oh great, another one who thinks they can just talk to me out of nowhere. What could you possibly want to talk about?"
    mc.name "Well, I was wondering if you'd like to... do something together sometime."
    "She scoffs."
    the_person "Yeah, sure, because that's exactly what I wanted. Someone to pester me even more."
    mc.name "Haha, no, I mean, if you're interested, we could maybe grab coffee or something."
    "She looks away, trying to hide a small smile."
    the_person "Fine. But only because I'm curious. And don't think this means I like you or anything."
    mc.name "Heh, thanks? I'll take that as a compliment."
    $ the_person.set_title()
    $ the_person.set_possessive_title()
    the_person "So, what's your name, anyway?"
    mc.name "I'm [mc.name]. Nice to meet you..."
    the_person "My name is [the_person.name]."
    $ the_person.change_happiness(1)
    return

label tsundere_greetings(the_person):
    if the_person.love < 0:
        the_person "Ugh, why do you always bother me for something?"
    elif the_person.happiness < 90:
        the_person "Hi. I guess it's better than nothing, but I'm still having a rough day."
    else:
        if the_person.sluttiness > 60:
            if the_person.obedience > 180:
                the_person "Oh, it's you. What do you want, [the_person.mc_title]? Don't tell me you're here for more of my services."
            else:
                the_person "Hey there, [the_person.mc_title]. Just remember, I'm only doing this because it's my job."
        else:
            if the_person.obedience > 180:
                the_person "Hi, [the_person.mc_title]. What can I do for you?"
            else:
                the_person "Hey, what's up? Don't tell me you're here to bother me again."
    return

label tsundere_sex_responses_foreplay(the_person):
    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] moans enthusiastically, clearly enjoying herself already."
            the_person "Hmph, fine. You're not too terrible at this, I suppose."
        else:
            "[the_person.possessive_title!c] moans happily to herself."
            the_person "I suppose this is okay, I guess."
    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            the_person "You know, this is almost decent. Don't get too cocky, though."
        else:
            the_person "I mean, it's not bad. You're not completely useless."
    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            the_person "Oh, all right. I suppose you're doing something right. But don't think this means I owe you anything."
        else:
            the_person "Alright, alright. You're doing it right. But don't expect me to be all mushy about it."
    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "Mmm, I suppose you're getting the hang of this. But don't think this means I'm going to be your little plaything."
        else:
            the_person "You're doing alright, [the_person.mc_title]. But don't expect me to be all affectionate about it."
    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                the_person "Oh, fine. You're getting close to making me cum. But don't think this means I'm going to fall for you."
            else:
                the_person "The way you touch me is just... different, I guess. But don't think this means I've forgiven you for being such a nuisance."
        else:
            the_person "Alright, you're almost there. But don't expect me to be all happy and stuff about it."

    return

label tsundere_sex_responses_oral(the_person):
    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] blinks, a hint of embarrassment on her face."
            the_person "U-uh, you really don't have to, [the_person.mc_title]..."
        else:
            "[the_person.possessive_title!c] looks up at you, her cheeks flushed."
            the_person "Y-you don't have to, but... if you want to..."

    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            the_person "Mmm, I guess it wouldn't hurt..."
        else:
            the_person "Oh, you really want to? Fine..."

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            the_person "Hmph, well, if you insist..."
            "[the_person.possessive_title!c] lets out a small sigh, her body slightly relaxing."
        else:
            the_person "Alright, but don't think I'm doing this because I want to..."

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "Mmm, you know, maybe this isn't so bad..."
        else:
            the_person "Hmph, you're pretty good at this, I'll give you that..."
    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                the_person "Oh, wow... I didn't know you could do that..."
            else:
                the_person "Mmm, maybe I should let you do that more often... when [the_person.so_title] isn't around..."
        else:
            the_person "Ugh, fine, but don't think I'm enjoying this..."

    return

label tsundere_sex_responses_vaginal(the_person):
    if the_person.energy < 10:
        call low_energy_sex_responses_vaginal(the_person) from _vt_tsundere_call_low_energy_sex_responses_vaginal_10
        return
    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            $ play_moan_sound()
            "[the_person.possessive_title!c] moans and wiggles her hips with your cock inside her."
            the_person "You're not bad, I guess. My pussy feels alright."
        else:
            "[the_person.possessive_title!c] bites her lip and stifles a moan."
    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            the_person "Fine, you can keep going if you want. But don't expect me to thank you or anything."
        else:
            the_person "Ugh, I guess your cock is alright..."

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            the_person "Mmm, I suppose you're not completely terrible at this..."
        else:
            the_person "Hmm, your cock is okay, I suppose."

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "You're not the worst, I guess. Keep going and maybe I'll...you know, finish or something."
        else:
            the_person "Fine, keep doing what you're doing. It's not like I have anything better to do."
    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                the_person "Ugh, I guess I'm close. But don't think this means I'm impressed or anything."
            else:
                the_person "Yeah, whatever. You're stretching me out, but it's not like it means anything."
                the_person "Just finish and get it over with."
        else:
            the_person "Hmph, I suppose I'm almost there. But don't think I'm enjoying this or anything."
            the_person "Just finish and let's get this over with."
    return

label tsundere_sex_responses_anal(the_person):
    if the_person.energy < 10:
        call low_energy_sex_responses_anal(the_person) from _vt_tsundere_call_low_energy_sex_responses_anal_10
        return

    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            the_person "Ugh, fine. But don't expect me to be all smiles about it..."
            "She huffs and puffs, clearly not thrilled about the situation."
        else:
            $ the_person.call_dialogue("annoyed_exclaim")
            the_person "Oh, great. Just what I always wanted: a big, thick cock up my ass."
            "She grumbles to herself, clearly unenthusiastic."

    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            $ the_person.call_dialogue("surprised_exclaim")
            the_person "Wow, this is... different."
            "She squirms a bit, trying to get used to the sensation."
        else:
            the_person "Ugh, this is so uncomfortable..."

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            the_person "Okay, okay. You can keep going."
            "She grits her teeth, trying to keep up the appearance of being tough."
        else:
            the_person "Why do you have to be so rough?!"

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            if mc.condom:
                the_person "Just get it over with already..."
            else:
                the_person "Ugh, you really want to do this raw, huh?"
        else:
            the_person "Why do you always have to be so insistent?"
    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                the_person "Fine, I'll cum... but don't think this means I like it!"
            else:
                the_person "You're just like my [the_person.so_title], always trying to get me to cum..."
                "She sighs, resigned to her fate."
        else:
            $ the_person.call_dialogue("annoyed_exclaim")
            the_person "Great, just what I needed: another orgasm..."
            "She mutters to herself, clearly not thrilled about the prospect."

    return

label tsundere_climax_responses_foreplay(the_person):
    if the_person.sluttiness > 50:
        the_person "Oh, stop being so annoying and just make me cum already!"
    else:
        the_person "Why do you always have to make this so difficult?"
        "She huffs, clearly on the verge of climax."
    return

label tsundere_climax_responses_oral(the_person):
    if the_person.sluttiness > 70:
        the_person "Why do you have to be so good at that? Fine, I'll cum!"
    else:
        the_person "You're really good at that... I didn't think I'd... I'm going to cum..."
    return

label tsundere_climax_responses_vaginal(the_person):
    if the_person.sluttiness > 70:
        if the_person.arousal_perc > 120:
            the_person "Fine, I'll cum. But don't think this means I'm enjoying myself."
        else:
            the_person "Ugh, just a little more... I'm... Ah, fuck!"
        "She grits her teeth and squeezes her eyes shut."
    else:
        the_person "Oh... I can't... I'm going to... Ah!"
    return

label tsundere_climax_responses_anal(the_person):
    if the_person.sluttiness > 70:
        if the_person.arousal_perc > 120:
            the_person "Fine, you win. I'll cum. But don't think I'm doing this because I want to."
        else:
            the_person "Ugh, just a little more... My ass is going to... Ah!"
        "She squeezes her eyes shut, trying to fight off the pleasure."
    else:
        the_person "Oh... My... Ass... I... Ah!"
        "She barely finishes her sentence before her body is racked with pleasure."
    return

label tsundere_clothing_accept(the_person):
    if the_person.obedience > 180:
        the_person "Whatever, just don't think you're making me into some kind of slutty fashion model."
    else:
        the_person "Yeah, whatever. Just don't expect me to go around looking like a total slut."
    return

label tsundere_clothing_reject(the_person):
    if the_person.should_wear_uniform:
        the_person "Hey, I guess I should get my uniform sorted out, right? One second."
    elif the_person.obedience > 180:
        the_person "I don't... I'm sorry, but I really don't think I could get away with wearing something like this. I appreciate the thought though."
    else:
        if the_person.sluttiness > 60:
            the_person "Hmm, I don't know about this one. It's a bit too revealing for my taste."
        else:
            the_person "You've got to be kidding me, right? This is ridiculous. I'm not wearing this."
    return

label tsundere_clothing_review(the_person):
    if the_person.outfit.cum_covered:
        if (the_person.sluttiness > 40 and the_person.opinion.being_covered_in_cum >=0) or the_person.opinion.being_covered_in_cum > 0:
            the_person "Ugh, why do I always get so messy with you...? I guess I can't walk around like this all day..."
            "[the_person.title] starts to wipe up the biggest splashes of cum on her."
        else:
            the_person "For fuck's sake, I need to clean up this mess! Let me know if I've missed any, okay?"
            "[the_person.title] wipes herself down, cleaning up all the cum she can find."

    if the_person.obedience > 180:
        the_person "Fine, I'll be back in a moment. I need to get cleaned up for you."
    else:
        if the_person.sluttiness > 40:
            the_person "I don't know why I do this, but I want to look good for you. I'll be back in a second, I just want to get cleaned up."
        else:
            the_person "Ugh, everything's such a mess after that. Wait here a moment, I'm just going to find a mirror and try and look somewhat presentable."
    $ the_person.apply_planned_outfit(show_dress_sequence = True)
    return

label tsundere_strip_reject(the_person, the_clothing, strip_type = "Full"):
    if the_person.obedience > 180:
        the_person "Hey, could we leave my [the_clothing.display_name] on for now, please? I'm still a little cold..."
    elif the_person.obedience < 70:
        the_person "No, no, no, I'll decide what comes off and when, okay? Don't rush me!"
    else:
        the_person "Not yet... I don't know if I'm ready to take off my [the_clothing.display_name]. Maybe we can try something else first?"
    return

label tsundere_strip_obedience_accept(the_person, the_clothing, strip_type = "Full"):
    "[the_person.title] laughs nervously as you start to slide her [the_clothing.display_name] away, but she doesn't stop you."
    if the_person.obedience > 180:
        the_person "Alright, fine... I guess I can trust you with this."
    else:
        the_person "I don't know if this is a good idea, but I'll let you do it this once..."
    return

label tsundere_grope_body_reject(the_person):
    if the_person.effective_sluttiness("touching_body") < 5: #Fail point for touching shoulder
        the_person "Hmph! What do you think you're doing?"
        "[the_person.title] steps back as you touch her, then crosses her arms over her chest."
        the_person "Just get your hands off me, okay? You're making me uncomfortable."
        mc.name "Oh, sorry. I didn't mean to make you feel that way."
        the_person "Yeah, well, try to be more careful next time, alright?"
        "She seems a little put off by the situation, but you both try to move on and put it behind you."
    else: #Fail point for touching waist
        the_person "Hey, could you just..."
        "[the_person.title] takes your hand and pulls it off of her waist, giving you a warning look."
        the_person "... Keep your hands to yourself, got it?"
        mc.name "Oh yeah, of course. My bad."
        the_person "Just make sure you don't do it again, okay? I don't appreciate it."
        "She doesn't say anything else, but you can tell she's still a bit annoyed about the situation."
    return

label tsundere_sex_accept(the_person, the_position):
    if the_person.sluttiness > 70:
        if the_person.obedience < 70:
            the_person "Fine, let's do it. But don't think this means I'm going to put out every time you ask."
        else:
            if the_position.skill_tag == "Foreplay":
                the_person "Oh, I've been wanting you to do that for a while now. Just thinking about it makes me wet."
            elif the_position.skill_tag == "Oral":
                if "getting head" in the_position.opinion_tags:
                    the_person "Ugh, I can't wait any longer. Suck my [pussy/clit] already!"
                else:
                    the_person "You're going down on me right now, and you're going to make me cum."
            else:
                the_person "Get over here and fuck me already. I've been waiting for this."
    else:
        the_person "Come here, let's do it. But don't think I'm going to do this all the time, got it?"
    return

label tsundere_sex_obedience_accept(the_person):
    if the_person.sluttiness > 70:
        the_person "Ugh, fine. I don't want to admit it, but you've gotten to me. Do whatever you want to me, [the_person.mc_title]."
    else:
        if the_person.obedience > 180:
            the_person "Alright, I'll do what you say, but don't think this means I'm going to like it."
        else:
            the_person "I shouldn't be saying this, but if you really want to... I'll give it a try. Just this once, okay?"
    return

label tsundere_sex_gentle_reject(the_person):
    if the_person.sluttiness > 50:
        the_person "Ugh, not like that, [the_person.mc_title]. I need a little more foreplay first."
    else:
        the_person "No, no, no. I want to have fun, but I don't want to get too serious. Let's just keep it light."
    return

label tsundere_sex_angry_reject(the_person):
    if the_person.has_significant_other:
        the_person "What? Are you out of your mind? I have a [the_person.so_title], so you can forget about doing anything like that. Ever."
        "She glares at you and turns away, clearly offended."
    elif the_person.sluttiness < 20:
        the_person "Are you serious? You've got to be kidding me! Get away from me, I never want to see you like this again!"
        "[the_person.title] glares at you and takes a step back, her face red with anger."
    else:
        the_person "What? Are you out of your mind? You can't be serious! Get away from me, I'm not interested in anything like that."
        "[the_person.title] glares at you and steps back, her face showing clear disapproval."
    return

label tsundere_seduction_response(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 50:
            the_person "Oh, I think I know what you need right now. Let me take care of you."
        else:
            the_person "Okay, I'll give you a few minutes. But don't think this means I'm going to be your slave or anything."
    else:
        if the_person.sluttiness > 50:
            the_person "Mmm, you're feeling as horny as me then? Come on, let's go find a place to get out of sight."
            "[the_person.title] takes your hand and leads you off to find some place private."
        elif the_person.sluttiness > 10:
            the_person "I know that look you're giving me, I think I know what you want. But don't expect me to give it up that easily."
        else:
            the_person "[mc.name], I know what you mean... Okay, I can spare a few minutes. But don't get your hopes up."
    return

label tsundere_seduction_accept_crowded(the_person):
    if not the_person.has_significant_other:
        if the_person.sluttiness < 20:
            the_person "Alright, let's sneak away for a few minutes and you can convince me a little more."
        elif the_person.sluttiness < 50:
            the_person "Come on, I know someplace nearby where we can get a few minutes privacy. Just make it quick."
        else:
            the_person "Oh, I don't know if I can wait much longer [the_person.mc_title]..."
    else:
        if the_person.sluttiness + (5*the_person.opinion.cheating_on_men) > 50:
            the_person "Fuck it, let's do this!"
            the_person "I hope you don't mind that I've got a [the_person.so_title], but I don't care right now."
        else:
            the_person "Ugh, you're bad for me [the_person.mc_title]... Come on, we need to find somewhere quiet so my [the_person.so_title] doesn't catch us."
    return

label tsundere_seduction_accept_alone(the_person):
    if not the_person.has_significant_other:
        if the_person.sluttiness < 20:
            the_person "Alright, you've got one chance to impress me."
        elif the_person.sluttiness < 50:
            the_person "Come on, let's get this over with and see if you're any good."
        else:
            the_person "Fuck, I'm so turned on right now. Just do me already!"
    else:
        if the_person.sluttiness + (5*the_person.opinion.cheating_on_men) > 50:
            the_person "You know I shouldn't be doing this with you, but fuck it. Let's do this!"
        else:
            the_person "You're trouble, [the_person.mc_title], but I can't help myself. Come here."
    return

label tsundere_seduction_refuse(the_person):
    if the_person.sluttiness < 20:
        the_person "Ugh, why are you always trying to flirt with me, [mc.name]? I'm just not in the mood for this right now, okay?"
        "[the_person.title] folds her arms and looks away."
    elif the_person.sluttiness < 50:
        the_person "Fine, I'll admit you're kind of cute, but don't think this means I'm actually interested. I just don't feel like messing around right now, okay? Maybe some other time, when I'm in a better mood."
        "[the_person.title] playfully pokes [mc.name]'s chest with her finger."
    else:
        the_person "Eh, you're always trying to get me into bed, [mc.name], but I'm not going to make it easy for you. You'll have to wait until I'm good and ready to fool around. Maybe that'll be never, who knows?"
        "[the_person.title] grins mischievously and walks away, leaving [mc.name] to wonder what she's thinking."
    return

label tsundere_compliment_response(the_person):
    mc.name "Hey [the_person.fname], you look really beautiful today. Is there a special occasion or something?"
    if the_person.is_at_work:
        if (the_person.is_employee or the_person.is_strip_club_employee) and the_person.is_wearing_uniform:
            call tsundere_flirt_response_employee_uniform_low(the_person) from _call_tsundere_flirt_response_employee_uniform_low_compliment_response
        elif the_person.is_at_job(prostitute_job):
            the_person "Ugh, why do you always want to hang out with me? Can't you see I'm busy?"
        elif the_person.sluttiness > 50:
            the_person "I'm doing great.  But don't think this means I'm actually interested in you or anything."
        else:
            the_person "Oh, stop it, you're making me blush. There's no special occasion, I just felt like dressing up today."
    else:
        the_person "Well, I did put in a bit of extra effort today. You're just the first one to notice. But thanks, I guess."
    "You try to press for more information, but [the_person.possessive_title] just smiles coyly and changes the subject, leaving you wondering what's going on."
    return

label tsundere_compliment_response_girlfriend(the_person):
    mc.name "Hey [the_person.title]. You're looking very nice this [StringInfo.time_of_day_string]."
    if the_person.is_at_work:
        if (the_person.is_employee or the_person.is_strip_club_employee) and the_person.is_wearing_uniform:
            call tsundere_flirt_response_employee_uniform_mid(the_person) from _call_tsundere_flirt_response_employee_uniform_mid_compliment_response_girlfriend
            $ the_person.call_dialogue("flirt_response_employee_uniform_mid")
        elif the_person.sluttiness > 50:
            the_person "Mmm, thank you, [the_person.mc_title]. Wanna find out how nice I am..."
        else:
            the_person "Hmph, really? Thanks, [the_person.mc_title]. You're not so bad yourself."
    else:
        the_person "Ugh, don't be ridiculous. It's just a normal day... but thanks, I guess."
        mc.name "Oh come on, don't be like that. You know you look great."
        the_person "Aww, stop it, [the_person.mc_title]. You're making me blush... and annoyed at the same time."
    "You chat with [the_person.possessive_title] for a while, and although she's initially annoyed by your compliments, she starts to warm up to you."
    return

label tsundere_compliment_response_affair(the_person):
    mc.name "Hey [the_person.title]. You're looking absolutely amazing this [StringInfo.time_of_day_string]."
    if the_person.is_at_work:
        if (the_person.is_employee or the_person.is_strip_club_employee) and the_person.is_wearing_uniform:
            call tsundere_flirt_response_employee_uniform_mid(the_person) from _call_tsundere_flirt_response_employee_uniform_mid_compliment_response_affair
        elif the_person.sluttiness > 50:
            the_person "Mmmm, thank you [the_person.mc_title], wanna go somewhere a little more private, so you can make me feel how amazing I am?"
        else:
            the_person "Hmph, really? Thanks, [the_person.mc_title]. You're not so bad yourself."
    else:
        the_person "Ugh, don't be silly. It's just a normal day... but thanks, I suppose."
        mc.name "Oh come on, don't be like that. You know you look great."
        the_person "Aww, stop it, [the_person.mc_title]. You're making me blush... and a little annoyed."
    "You keep chatting with [the_person.possessive_title] for a while, slipping in a few more compliments. She is quite charmed by your attentiveness."
    return

label tsundere_flirt_response(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 50:
            the_person "Ugh, fine. You're not totally terrible, [the_person.mc_title]."
        else:
            the_person "Whatever. Thanks for the compliment, [the_person.mc_title]. You're not a complete loser."

    elif the_person.has_significant_other:
        if the_person.sluttiness + (the_person.opinion.cheating_on_men*5) > 50:
            the_person "Oh, you think you're so clever, don't you? I'll give you that."
            "[the_person.title] gives you a sly look, her eyes narrowing."
        else:
            the_person "You're really pushing your luck, [the_person.mc_title]. I have a [the_person.so_title] you know."
            mc.name "What about you, do you appreciate it?"
            "She rolls her eyes and crosses her arms."
            the_person "Maybe I do, maybe I don't. It's none of your business."

    else:
        if the_person.sluttiness > 50:
            the_person "Fine. Maybe you're worth my time, [the_person.mc_title]."
            "[the_person.title] gives you a half-smile, but her eyes remain guarded."
        else:
            the_person "Whatever. You're not unattractive, I suppose. But don't think that means I'll go easy on you."
            the_person "You'll have to really impress me though, I have high standards."
    return

label tsundere_flirt_response_employee_uniform_low(the_person):
    if the_person.is_wearing_forced_uniform:
        the_person "Hmph, I suppose you like seeing me in this uniform... I mean, I'm practically naked!"
        mc.name "I know you don't like it, but I needed to make a point."
        the_person "I know, I know. You always were one to make a point."
        $ mc.change_locked_clarity(5)
        "She crosses her arms over her chest, but can't hide the small smile on her face."
    elif the_person.judge_outfit(the_person.outfit):
        #She's in uniform and likes how it looks.
        the_person "Oh, you noticed? I thought it was a bit much, but I guess it's not so bad."
        the_person "I mean, it's nice to work somewhere where I can show off a little."
        $ mc.change_locked_clarity(5)
        "She winks at you, then turns to adjust her uniform, accentuating her hips."
    else:
        #She's in uniform, but she thinks it's a little too slutty.
        if the_person.vagina_visible:
            # Her pussy is on display.
            the_person "Hmph, I suppose you like seeing me like this... I mean, I'm practically naked!"
            mc.name "Well, you know that it's..."
            the_person "I know, I know. It's company policy. But don't think you're the only one who's annoyed by it."
            mc.name "Give it some time and you'll get used to it."
            $ mc.change_locked_clarity(5)
            "She rolls her eyes, but doesn't argue."

        elif the_person.tits_visible:
            # Her tits are out
            the_person "Ugh, I'm still getting used to being so... exposed in this uniform. At least I don't have to wear a bra!"
            mc.name "You look incredible and you're comfortable. I call that a success."
            $ mc.change_locked_clarity(5)
            "She huffs, but can't hide her smile."
            the_person "Yeah, yeah. You're just trying to make me feel better."

        elif the_person.underwear_visible:
            # Her underwear is visible.
            the_person "Hmph, I probably would have picked something that kept me a little more covered, but at least our uniform is comfortable."
            mc.name "It may be a little unconventional, but you look fantastic. You've got exactly the right kind of body for it."
            the_person "Well, that's one way to look at it, I suppose."
            $ mc.change_locked_clarity(5)
            "She playfully rolls her eyes and turns to adjust her uniform, showing off her body."
        else:
            # It's just generally slutty.
            the_person "Ugh, well thank you! Our uniforms are a little bold for my taste, but I guess I look good in it."
            $ mc.change_locked_clarity(5)
            "She blushes and looks away, but not before you catch a glimpse of her small smile."
    return

label tsundere_flirt_response_employee_uniform_mid(the_person):
    if the_person.is_wearing_forced_uniform:
        $ mc.change_locked_clarity(10)
        if the_person.vagina_visible:
            the_person "Ugh, fine. You caught me off guard. I'll admit, this uniform does make me look good, especially down here."
            mc.name "It's a great uniform, but that's not what's important here."
            the_person "Yeah, yeah. You're right. It's just hard not to feel like a sex object in this thing, especially with my pussy on display."
        elif the_person.tits_visible:
            the_person "Ugh, fine. You caught me off guard. I'll admit, this uniform does make me look good, especially up here."
            mc.name "It's a great uniform, but that's not what's important here."
            the_person "Yeah, yeah. You're right. It's just hard not to feel like a sex object in this thing, especially with my boobs popping out."
        else:
            the_person "Ugh, fine. You caught me off guard. I'll admit, this uniform does make me look good."
            mc.name "It's a great uniform, but that's not what's important here."
            the_person "Yeah, yeah. You're right. It's just hard not to feel like a sex object in this thing."
        mc.name "Rules are rules and I can't make any exceptions, even if they look good."
        "She sighs and nods."
        the_person "Yeah, I know. At least you're having a good time. I don't mind that so much."
    elif the_person.judge_outfit(the_person.outfit):
        $ mc.change_locked_clarity(10)
        if the_person.tits_visible:
            the_person "Hmph, maybe I should wear this outfit more often. It's getting a lot of attention, especially for my boobs."
            mc.name "It's a great outfit, but I'm more interested in the person wearing it."
            the_person "Oh, really? Is that so? I guess my boobs are hard to ignore."
        else:
            the_person "Hmph, maybe I should wear this outfit more often. It's getting a lot of attention."
            mc.name "It's a great outfit, but I'm more interested in the person wearing it."
            the_person "Oh, really? Is that so? I guess my vagina is hard to ignore."
        the_person "Maybe I'll invite you shopping one day and you can tell me what else you want to see me in."
        mc.name "Sounds like a good time."

    else:
        # the_person "I think it shows off a little too much!"
        the_person "Ugh, fine. You're not gonna make this easy for me, are you?"
        $ mc.change_locked_clarity(10)
        if the_person.vagina_visible:
            the_person "I'm trying to focus on my work here, not flirt with you all day. And definitely not with my pussy on display."
        elif the_person.tits_visible:
            the_person "I'm trying to focus on my work here, not flirt with you all day. And definitely not with my boobs popping out."
        else:
            the_person "I'm trying to focus on my work here, not flirt with you all day!"
        mc.name "I understand, but I promise it's important for the business."
        "She sighs and nods."
        the_person "Yeah, I know. You're a real pain, you know that?"
    return

label tsundere_flirt_response_low(the_person):
    #She's in her own outfit.
    the_person "Hmph, I suppose it's not the worst outfit I've ever worn."
    $ the_person.draw_person(position = "walking_away")
    $ mc.change_locked_clarity(5)
    "She rolls her eyes and gives you a quick spin, showing off her outfit from every angle."
    the_person "I mean, I guess it's not too bad, right?"
    $ the_person.draw_person()
    mc.name "I think it looks great on you."
    the_person "Oh, shut up. You're just saying that."
    return

label tsundere_flirt_response_low1(the_person):
    if the_person.has_significant_other:
        the_person "Ugh, what's with you and the flirting? I've got a [the_person.so_title], and I don't think he'd appreciate you getting all up in my grill."
        mc.name "What about you, do you appreciate it?"
        "She rolls her eyes and smirks."
        the_person "Maybe I do... but don't think you're getting anywhere with me that easily."
    else:
        the_person "Well, thanks for the compliment. But don't think you're getting off that easy. I have high standards, and you'll need to prove yourself to me."
        the_person "But if you can impress me, who knows what might happen..."
    $ mc.change_locked_clarity(5)
    return

label tsundere_flirt_response_mid(the_person):
    if mc.location.person_count > 1 and the_person.effective_sluttiness("kissing") < (25 - (5*the_person.opinion.public_sex)):
        $ mc.change_locked_clarity(10)
        the_person "You know, I was wondering if you actually noticed my outfit today..."
        "Her eyes narrow slightly, but she's still trying to appear casual."
        mc.name "I noticed. It looks great on you."
        the_person "Oh, really? Thanks, I guess. I was thinking you might say something like that."
        "She crosses her arms, trying to maintain a tough exterior."
        if the_person.tits_visible:
            mc.name "I noticed. It looks great on you. Especially your boobs."
            the_person "Oh, really? Thanks, I guess. I was thinking you might say something like that."
            "She crosses her arms, trying to maintain a tough exterior."
        else:
            mc.name "Well, it's true. You look amazing."
        the_person "Hmph. Maybe I'll invite you shopping one day, so you can tell me what else you want to see me in."
        "She leans in slightly, a hint of flirtation in her voice."
        mc.name "I can think of a few things already... and I'm sure I'd enjoy seeing you in them."
        the_person "I'm sure you would. So, what do you say? Want to take me out for a drink and maybe we can discuss my wardrobe some more?"

    else:
        the_person "Thanks, I thought I looked pretty hot in it too."
        the_person "You want a better look, right? Here, how does it make my ass look?"
        $ the_person.draw_person(position = "back_peek")
        $ mc.change_locked_clarity(10)
        the_person "Good, right?"
        mc.name "Fantastic. I wish I could get an even better look at it."
        "[the_person.possessive_title!c] smiles and turns back to face you."
        $ the_person.draw_person()
        the_person "I'm sure you do. Take me out for a drink and maybe we can work something out."
    return

label tsundere_flirt_response_mid1(the_person):
    $ mc.change_locked_clarity(10)
    the_person "Thanks, I do look amazing in this outfit."
    if (the_person.has_skirt or the_person.has_dress) and not the_person.has_thigh_high_socks:
        mc.name "You could change it up with some high stockings, I would like to see that."
        the_person "Oh, really? And why would you want to see that? You're not going to get a peek or anything, are you?"
        mc.name "Because it would look great on you, and I would enjoy the view."

    mc.name "How about you and me go and grab a coffee sometime?"
    if the_person.has_significant_other:
        the_person "Sure, my [the_person.so_title] doesn't mind... as long as they're not around to witness how much fun we're going to have."
    else:
        the_person "Why not, I could use a pick-me-up once in a while... and maybe someone to pick me up from the ground when I fall for you."
    the_person "Just let me know when, I would love to... and don't think I won't notice if you're trying to get a glimpse of my legs under the table."
    mc.name "I'll keep that in mind, and maybe we can discuss what else you want to wear in the future... or not wear."
    the_person "Hmph, maybe. But don't think you're getting a discount on my wardrobe just because we're going out for coffee... or anything else."
    return

label tsundere_flirt_response_high(the_person):
    if mc.location.person_count > 1 and the_person.effective_sluttiness() < (25 - (5*the_person.opinion.public_sex)): # There are other people here, if she's not slutty she asks if you want to find somewhere quiet
        the_person "You're really persistent, huh? Fine, but not here..."
        "She glances around before giving you a sly smile."
        menu:
            "Find somewhere more quiet\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                mc.name "Then let's find somewhere that isn't here."
                the_person "Hmph, eager much? Alright, let's go."
                call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_tsundere_flirt_response_high_2
                the_person "So... Now what's your plan?"

                if the_person.is_willing(kissing):
                    $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
                    if the_person.has_taboo("kissing"):
                        "You lean in close to kiss [the_person.title]."
                        $ the_person.call_dialogue("kissing_taboo_break")
                        $ the_person.break_taboo("kissing")
                        "She responds passionately, her arms wrapping around your neck."
                    else:
                        "You step close to [the_person.title] and put your arm around her waist, pulling her close and kissing her."
                        "She responds immediately and eagerly presses her body against yours."
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _vt_tsundere_call_fuck_person_49
                else:
                    if the_person.has_taboo("touching_body"):
                        $ the_person.call_dialogue("touching_body_taboo_break")
                        $ the_person.break_taboo("touching_body")
                        "You take her hand and pull her close against you. She looks into your eyes."
                    else:
                        "You take her hand and pull her close, your lips brushing against her ear."
                    call fuck_person(the_person, private = True, start_position = standing_grope, skip_intro = True) from _call_fuck_person_tsundere_flirt_grope

                $ the_person.call_dialogue("sex_review", the_report = _return)
                call mc_restore_original_location(the_person) from _call_mc_restore_original_location_tsundere_flirt_response_high_2

            "Just flirt":
                mc.name "You know you want to, come on. I'll take you out for dinner, and then we can see where the night takes us."
                the_person "Hmm, you're really trying to charm me, aren't you? Well, I'll tell you what... If you can make me laugh, I might consider it."
                "She smiles mischievously, clearly enjoying the challenge."
    else:
        if mc.location.person_count == 1: #You're alone, so she just didn't meet the sluttiness threshold
            the_person "Hmm, you're really eager, aren't you? Well, I suppose it's just the two of us here..."
            "[the_person.possessive_title!c] glances around, confirming you're alone."
            the_person "So what's your plan?"

        else:  # You aren't alone but she's still into it.
            the_person "Feeling bold today, huh? Well, I think your chances are pretty good..."
            "[the_person.title] smirks, clearly enjoying the attention."
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
                    the_person "Oh, you're brave. I like that."
                    $ the_person.call_dialogue("touching_body_taboo_break")
                    $ the_person.break_taboo("touching_body")

                call fuck_person(the_person, start_position = standing_grope, private = False) from _call_fuck_person_flirt_response_tsundere_touching

            "Kiss her" if the_person.is_willing(kissing):
                $ the_person.draw_person()
                if the_person.has_taboo("kissing"):
                    "You put your arm around [the_person.possessive_title] and lean in close."
                    $ the_person.call_dialogue("kissing_taboo_break")
                    $ the_person.break_taboo("kissing")
                    "She responds with a passionate kiss, her arms wrapping around your neck."
                else:
                    "You pull [the_person.possessive_title!] close and kiss her."
                    "She responds with a passionate kiss, her arms wrapping around your neck."

                call mc_move_to_private_location(the_person) from  _call_mc_move_to_private_location_tsundere_flirt_response_high
                call fuck_person(the_person, start_position = kissing, private = _return, skip_intro = True) from _vt_tsundere_call_fuck_person_50
                $ the_person.call_dialogue("sex_review", the_report = _return)
                call mc_restore_original_location(the_person) from _call_mc_restore_original_location_tsundere_flirt_response_high

            "Just flirt":
                $ the_person.draw_person()
                mc.name "Very tempting, but you're going to have to contain yourself for now."
                the_person "Oh, you're not going to take advantage of me right now, are you? Fine, be that way."
                "[the_person.title] pouts, clearly enjoying the flirtation."
    return

label tsundere_flirt_response_low_energy(the_person):
    if the_person.sluttiness > 40:
        the_person "Ugh, thanks for the compliment, but I'm so tired right now."
    else:
        the_person "Thanks, but I'm beat. Can we pick this up later?"
    return

label tsundere_flirt_response_girlfriend(the_person):
    # Lead in: mc.name "You're so beautiful [the_person.title], I'm so lucky to have a woman like you in my life."
    if mc.location.person_count > 1:
        # There are other people around, so she'll only start making out with you if she's slutty.
        if the_person.effective_sluttiness("kissing") < (25 - (5*the_person.opinion.public_sex)):
            # Not very slutty, so she wants to find somewhere private
            the_person "Oh my god, you're so cheesy. Come here."
            "She pulls you against her and kisses you, her lips soft and gentle."
            the_person "There, now you can't say I don't know how to kiss."
            mc.name "Haha, yeah I guess not..."
            "You put your arms around her and kiss her back, feeling her warmth."
            the_person "Mmm, yeah, like that."
            menu:
                "Find somewhere more quiet\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                    mc.name "Why wait? Come on, I'm sure we can find somewhere quiet."
                    the_person "You're always so eager, aren't you? Alright, let's go!"
                    "You and [the_person.possessive_title] hurry off, searching for a private spot."
                    call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_tsundere_flirt_response_girlfriend_2
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _vt_tsundere_call_fuck_person_76
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_tsundere_flirt_response_girlfriend_2

                "Just flirt":
                    $ mc.change_locked_clarity(10)
                    "You reach around and pull her closer, running your hand down her back."
                    mc.name "You're so beautiful, and you know it."
                    "She rolls her eyes but leans in for a quick kiss."
                    the_person "Fine, you caught me. But don't think this means I'm going easy on you."

        else:
            the_person "Well if I'm so beautiful, then why are you just standing there? Come on, kiss me!"
            "You put your arm around her waist and pull her close, kissing her deeply."
            "When you break the kiss, [the_person.possessive_title] sighs and leans against you."
            the_person "You're not so bad yourself..."
            menu:
                "Make out":
                    "You lean back in and kiss her again, this time more passionately."
                    "[the_person.title] responds eagerly, wrapping her arms around your neck."

                    call mc_move_to_private_location(the_person) from  _call_mc_move_to_private_location_tsundere_flirt_response_girlfriend
                    call fuck_person(the_person, start_position = kissing, private = _return, skip_intro = True) from _vt_tsundere_call_fuck_person_77
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_tsundere_flirt_response_girlfriend

                "Just flirt":
                    mc.name "I'm not bad? You're the one who's hard to resist."
                    $ mc.change_locked_clarity(10)
                    "You reach out and touch her cheek, a playful grin on your face."
                    the_person "Ugh, you're so annoying. But I guess I like that about you..."
    else:
        # You're alone, so she's open to fooling around.
        the_person "Well you've got me all alone, so how about you show me just how lucky you feel?"
        "She reaches down to your waist and cups your crotch, rubbing it gently."
        mc.name "You're so wet for me already."
        the_person "Hmph, maybe."
        "She grinds against you, her hips moving in a slow circle."
        mc.name "Damn, you feel so good."
        "You reach up and grab her breasts, squeezing them gently."
        the_person "Ooh, don't do that."
        "But she doesn't pull away, her body still pressed against yours."
        menu:
            "Kiss her":
                if the_person.has_taboo("kissing"):
                    $ the_person.call_dialogue("kissing_taboo_break")
                    $ the_person.break_taboo("kissing")

                "You put your arms around [the_person.possessive_title]'s waist and rest your hands on her ass. You pull her close and kiss her sensually."
                "She responds by pressing her body against you and grinding her hips against your thigh."
                "You grab her hips and pull her closer, your crotches pressed together."
                call fuck_person(the_person, start_position = kissing, skip_intro = True) from _vt_tsundere_call_fuck_person_78
                $ the_person.call_dialogue("sex_review", the_report = _return)
                $ the_person.review_outfit()

            "Just flirt":
                mc.name "I'm going to make you beg for it."
                "You lean in close, your breath hot against her ear."
                the_person "Ooh, you're such a bad boy. I love it."
                "She rubs her body against yours, her hips moving seductively."
                the_person "But don't think you're getting off that easy. I'm going to make you work for it..."
    return

label tsundere_flirt_response_affair(the_person):
    # Lead in: mc.name "You look so good today [the_person.title], you're making me want to do some very naughty things to you."
    if mc.location.person_count > 1: #There are other people around, she's nervous about people finding out what you're doing.
        if (the_person.opinion.cheating_on_men *15) + the_person.effective_sluttiness() > 50: #SHe's turned on by flirting in public or doesn't think anything is wrong with it
            "[the_person.possessive_title!c] blushes and playfully bats her eyes at you."
            the_person "Oh, you're making me blush. I'm not used to this kind of attention from you."
            the_person "But I have to admit, I'm curious. What do you have in mind?"
            menu:
                "Find somewhere more quiet\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                    mc.name "I was thinking we could slip away and find a more private spot."
                    "You and [the_person.title] exchange a flirtatious glance before hurrying off to find a quiet spot."
                    call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_tsundere_flirt_response_affair
                    $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
                    "As soon as you're alone she pulls you into a deep and passionate kiss."
                    $ the_person.draw_person(position = "kissing")
                    the_person "Mmm... I've been wanting to do that for a while now."
                    "You wrap your arms around her waist and kiss her back."
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _vt_tsundere_call_fuck_person_79
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_tsundere_flirt_response_affair

                "Just flirt":
                    mc.name "I can't help but notice how beautiful you look today, [the_person.title]."
                    the_person "Stop it, you're making me blush! But I have to admit, you look pretty great yourself."
                    the_person "Just don't get too cocky, okay? I'm still in charge here."
                    $ mc.change_locked_clarity(20)
                    "[the_person.possessive_title!c] playfully swats at your arm before leaning in close."
                    the_person "But I have to admit, I'm getting a little turned on by this whole thing."
                    "You can't help but feel a little flustered as she teases you."
                    mc.name "I can see that. Maybe we should find a more private place to continue this..."
                    the_person "Mmm, maybe we should. But first, let's enjoy this little moment here."

        else: #She's shy or nervous about being discovered
            "[the_person.possessive_title!c] looks around nervously, then back at you with a sheepish grin."
            the_person "Oh, um, you look nice today. I guess I should probably get going though..."
            mc.name "Wait, don't go! I was thinking we could... uh, grab a drink or something?"
            $ mc.change_locked_clarity(15)
            the_person "Oh, you want to grab a drink? Okay, sure. But just for a little bit, okay? I don't want to be out too late."
            "She glances around again, then leans in close and whispers."
            the_person "And just so you know, I'm still in charge here, even if we're just grabbing a drink."
            "You can't help but feel a little excited by her assertiveness."
            mc.name "Okay, okay. I'll behave."
    else:
        # the_person "Yeah? Well there's nobody around, and I'm not going to stop you."
        the_person "Oh yeah? Well then, do you want to share what all of these naughty things are? You have my attention."
        menu:
            "Feel her up":
                "You put your arms around [the_person.possessive_title]'s waist and rest your hands on her ass."
                mc.name "You know, I've been waiting for this moment for a while now."
                "You massage her butt. She blushes and pushes you away lightly."
                the_person "Hey, no need to be so forward! What's gotten into you?"
                "You pull her close again and shift your hands to her breasts, squeezing them gently."
                mc.name "Come on, don't be like that. I just wanted to make you feel good for once."
                call fuck_person(the_person, private = True, start_position = standing_grope, skip_intro = True) from _vt_tsundere_call_fuck_person_80
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
                "She looks up at you with a playful pout."
                the_person "Promise you won't make me wait?"
                mc.name "I promise, baby."
                "You both share a flirtatious smile."
                the_person "Good. Because I'm not sure I can handle it if you do."
    return

label tsundere_flirt_response_text(the_person):
    mc.name "Hey [the_person.title], how's it going? I'm feeling a bit bored and thought we could chat."
    "She replies with a hint of annoyance."
    if the_person.is_affair:
        the_person "Oh, great, you're bored again? You always seem to find ways to bother me."
        the_person "Well, what do you want this time? I'm not exactly thrilled about entertaining you."
        the_person "When can we get together?"
        mc.name "Some time soon. I'll let you know."

    elif the_person.is_girlfriend:
        the_person "Bored, huh? That's not exactly a surprise. You're always looking for something new to entertain yourself."
        the_person "But fine, we can hang out. Just don't expect me to do anything special."
        mc.name "Some time soon. I'll let you know."

    elif the_person.love < 40:
        if the_person.effective_sluttiness() > the_person.love:
            the_person "Ugh, bored, really? Well, I suppose I can keep you company for a bit."
        else:
            the_person "Bored, eh? That's not surprising. You're always looking for a new distraction."

    else:
        if the_person.effective_sluttiness() > the_person.love:
            the_person "Fine, I'll talk to you. But don't think this means I'm happy about it."
            the_person "So, what do you want to talk about? I'm not exactly thrilled about this."
        else:
            the_person "You're bored, huh? Well, that's your problem, not mine."
            the_person "So, what do you want? Just don't expect me to be all lovey-dovey about it."
    return

label tsundere_condom_demand(the_person):
    if the_person.wants_creampie:
        the_person "Ugh, seriously? You need to put on a condom before we even think about doing anything."
        the_person "I hate that we have to, but you know it's necessary."
    else:
        the_person "For crying out loud, do you have a condom on you? Put one on before you even think about touching me."
        the_person "I don't want to be stuck with some stupid disease because you were too careless."
    return

label tsundere_condom_ask(the_person):
    if the_person.on_birth_control:
        the_person "You want a condom? Fine, but I'm on the pill, so it's not like I really need it."
        $ the_person.update_birth_control_knowledge()
    elif the_person.wants_creampie:
        the_person "Ugh, you want to cum inside me? Just put on a condom, would you? It's not like I want to get pregnant or anything."
        the_person "But I guess it's better than the alternative, right?"
        $ the_person.discover_opinion("creampies")
    else:
        the_person "Fine, I guess you should use a condom...but can you at least not make a mess with it? I don't want to clean up after you."
        the_person "And please, no pulling out method. That's just asking for trouble."
    return

label tsundere_condom_bareback_ask(the_person):
    if the_person.wants_creampie:
        if the_person.is_infertile:
            the_person "You're not seriously considering a condom, are you? Please, just give me your hot, sticky load."
            the_person "I want to feel you fill me up and make me scream with pleasure."
        elif the_person.on_birth_control:
            the_person "Don't even think about putting a condom on, [the_person.mc_title]. I'm on the pill, so we're good to go."
            the_person "Just fuck me raw and make me feel every inch of you."
            $ the_person.update_birth_control_knowledge()
        else:
            the_person "Forget the condom, [the_person.mc_title], I want to feel you deep inside me."
            the_person "I don't care about the risks, it's worth it for this kind of pleasure."
            if not the_person.knows_pregnant:
                the_person "Imagine how hot it would be to get knocked up, too."
        $ the_person.discover_opinion("creampies")
    else:
        the_person "Don't bother with a condom, [the_person.mc_title]. I want to feel you raw and unprotected."
        if not the_person.knows_pregnant:
            the_person "I don't care about the risks, it's worth it for the intensity."
        else:
            the_person "I love it when you fuck me raw and make me feel like I'm yours."
    return

label tsundere_condom_bareback_demand(the_person):
    if the_person.has_breeding_fetish: #Actively looking to get knocked up.
        if the_person.knows_pregnant:
            the_person "Ugh, why bother with a condom? I want to get pregnant, so fuck me raw!"
            the_person "Hurry up, I can't wait to feel you inside me."
        elif the_person.is_infertile:
            the_person "Oh, great, you're going to remind me I can't get pregnant? Thanks a lot."
        else:
            the_person "Ugh, what's the point of fucking if you're not going to knock me up?"
            the_person "Hurry up and give me that cock!"
    elif the_person.wants_creampie: #Just likes raw sex
        if the_person.is_infertile:
            the_person "Ugh, why bother with a condom? I can't get pregnant anyway."
        elif the_person.on_birth_control:
            the_person "Forget the condom, [the_person.mc_title]. I'm on the pill, so it's not a problem."
            the_person "Take me bareback and make me scream."
            $ the_person.update_birth_control_knowledge()
        else:
            the_person "Ugh, condoms are so annoying. Just get inside me already!"
    else:
        if the_person.is_infertile:
            the_person "Take me bareback, [the_person.mc_title]. It's not like I can get pregnant."
            the_person "Just make me feel good."
        elif the_person.on_birth_control:
            the_person "Forget the condom, [the_person.mc_title]. I'm on the pill."
            the_person "Take me bareback and make me feel every inch of you."
            $ the_person.update_birth_control_knowledge()
        else:
            the_person "Ugh, condoms are so annoying. Just get inside me already!"
            the_person "I need to feel you deep inside me."
    return

label tsundere_cum_face(the_person):
    if the_person.has_cum_fetish or the_person.obedience > 180:
        if the_person.has_cum_fetish or the_person.effective_sluttiness() > 60 or the_person.opinion.cum_facials > 0:
            the_person "So, do you think this is a good look for me, [the_person.mc_title]?"
            "[the_person.title] smirks, then licks her lips and runs a finger through your semen, bringing it to her mouth."
            the_person "Mmm, taste your victory."
        else:
            the_person "Hmph, I suppose it's not a terrible look. But I'm glad we're done here."
            "[the_person.title] wipes away some of your semen from her face, looking annoyed."
    else:
        if the_person.effective_sluttiness() > 80 or the_person.opinion.cum_facials > 0:
            the_person "Well, I guess this is one way to end things. Do you think I look good like this?"
            "[the_person.title] smirks, then laughs and wipes away some of your semen from her face."
        else:
            the_person "Ugh, just get that over with already. And don't think you're getting a second chance."
            "[the_person.title] wipes away your semen, looking put off."
    return

label tsundere_cum_mouth(the_person):
    if the_person.has_cum_fetish or the_person.obedience > 180:
        if the_person.has_cum_fetish or the_person.effective_sluttiness() > 60 or the_person.opinion.drinking_cum > 0:
            the_person "Mmm, that's so... satisfying [the_person.mc_title]."
            the_person "You really know how to make me feel good."
        else:
            "[the_person.title]'s face twists in disgust as she swallows your cum."
            the_person "Ugh, there, done. Don't think I enjoyed that one bit."
    else:
        if the_person.effective_sluttiness() > 80  or the_person.opinion.drinking_cum > 0:
            the_person "Mmm, you're quite the stud, [the_person.mc_title]."
            the_person "I can see why you're so popular."
        else:
            the_person "Ugh, that's... quite a taste. I hope you're happy."
    return

label tsundere_cum_pullout(the_person):
    # Lead in: "I'm going to cum!"
    if mc.condom:
        if the_person.wants_creampie and not the_person.has_taboo("condomless_sex"): #TODO: FIgure out we want any more requirements for this to fire.
            if the_person.knows_pregnant:
                the_person "Oh, don't bother with the condom, just cum inside me and make me pregnant!"
                the_person "I don't care about the consequences right now, I just want your cum filling me up!"
            elif the_person.on_birth_control:
                the_person "Oh fuck... I can't take it any more, take that condom off [the_person.mc_title]!"
                "She moans desperately."
                the_person "I give in, I want you to cum inside me!"
            else:
                "She moans desperately."
                the_person "I can't think straight, just take off the condom and cum inside me!"
                $ the_person.update_birth_control_knowledge()
                the_person "I want you to make me cum and then make me pregnant, you dirty fucker!"
            menu: #TODO: Add a variant of this normally so you can stealth a girl (don't do that in real life, it's super fucked up).
                "Take off the condom":
                    "You pull out, barely clearing her pussy, and pull the condom off as quickly as you can manage."
                    $ mc.condom = False
                    $ use_condom = False  # prevent putting on a new condom next sex loop
                "Leave it on":
                    "You ignore [the_person.possessive_title]'s request and keep the condom in place."
        else:
            the_person "Fuck yeah, I'm going to make you cum!"
    else:
        if the_person.wants_creampie:
            if the_person.knows_pregnant: #She's already knocked up, so who cares!
                the_person "Creampie me, you dirty fucker, and make me cum!"
            elif the_person.opinion.creampies > 0:
                "[the_person.possessive_title!c] moans happily."
                if the_person.on_birth_control: #She just likes creampies.
                    the_person "Fuck yeah, fill me up with your cum [the_person.mc_title]! Creampie me!"
                else: #Yeah, she's not on BC and asking for you to creampie her. She's looking to get pregnant.
                    $ the_person.update_birth_control_knowledge()
                    the_person "Oh fuck, cum inside me and knock me up [the_person.mc_title]! I want you to breed me like a dirty slut!"
            elif the_person.is_infertile:
                the_person "Cum wherever you want, you dirty fucker, I can't get pregnant."
            elif the_person.on_birth_control: #She's on the pill, so she's probably fine
                $ the_person.update_birth_control_knowledge()
                the_person "Cum wherever you want, you dirty fucker, I'm on the pill!"
            else: #Too distracted to care about getting pregnant or not. Oh well, what could go wrong?
                the_person "Do it! Cum!"
        else:
            if the_person.is_infertile:
                the_person "Just pull out, I don't want your cum inside me, you dirty fucker!"
            elif not the_person.on_birth_control: #You need to pull out, I'm not on the pill!
                $ the_person.update_birth_control_knowledge()
                the_person "Fuck, pull out, you dirty fucker! I'm not on the pill!"
            elif the_person.opinion.creampies < 0:
                the_person "Pull out, I don't want you to cum in me, you dirty fucker!"
            else:
                the_person "Hell yeah, pull out and cum all over me like a dirty slut!"
    return

label tsundere_cum_condom(the_person):
    if the_person.effective_sluttiness() > 75 or the_person.opinion.creampies > 0:
        the_person "Oh god, it feels so good. If your condom broke it would be inside me, and I'd be pregnant."
    else:
        the_person "Oh god, I hope you buy good condoms because that's a lot of cum."
        the_person "But then again, maybe you're dreaming of knocking me up and getting me pregnant."
    return

label tsundere_cum_vagina(the_person):
    if the_person.has_taboo("creampie"):
        $ the_person.call_dialogue("creampie_taboo_break")
        $ the_person.break_taboo("creampie")
        return
    if the_person.wants_creampie:
        if the_person.knows_pregnant:
            the_person "Ugh, fine... I guess I can admit it now, but only because I'm already pregnant from your other, uh, impressive performances... Your cum just feels so good inside me!"
        elif the_person.is_infertile:
            the_person "Oh, stop being so dramatic! Of course you're not going to get me pregnant, I'm infertile, remember? But seriously, your cum is pretty great... just don't expect me to admit it to anyone else!"
        elif the_person.on_birth_control:
            if the_person.has_significant_other:
                the_person "Well, well, well... Look at you go! I guess it's a good thing I'm on the pill, huh? Or maybe I'll just tell [the_person.so_title] that it was someone else's... Ugh, why do you have to be so frustrating?"
            else:
                if the_person.knows_pregnant:
                    the_person "Oh fuck that's a lot of cum. Good thing I'm already pregnant, because I don't think you're firing blanks."
                elif the_person.is_infertile:
                    the_person "Oh fuck that's a lot of cum. I will be dripping your cum all day long."
                else:
                    the_person "Oh fuck that's a lot of cum. Good thing I'm on the pill, because I don't think you're firing blanks."
                $ the_person.update_birth_control_knowledge()
        elif the_person.effective_sluttiness() > 75 or the_person.opinion.creampies > 0:
            if the_person.has_significant_other:
                the_person "Okay, okay, I get it! You're great in bed, but don't think I'm going to start flaunting our little secret around my [the_person.so_title]... At least, not until I figure out how to explain it."
            else:
                the_person "Ugh, fine... I'll admit it, you're pretty amazing when you're like this... But don't think this means I'm going to start begging for more! I just need to... process this, okay?"
        else:
            if the_person.has_significant_other:
                the_person "You really know how to make a girl feel special, don't you? But let's keep this between us, okay? I don't think [the_person.so_title] would understand..."
            else:
                the_person "Wow... I guess I didn't expect that from you. But I have to admit, it was kind of nice... Just don't get any ideas, okay? I'm not ready for anything serious."
    else: #She's angry
        if the_person.knows_pregnant:
            the_person "Ugh, what is wrong with you? I specifically told you not to do that! Oh well, since I'm already pregnant..."
        elif not the_person.on_birth_control:
            if the_person.has_significant_other:
                the_person "Oh, great. Just what I needed. You forgot to pull out, and now I'm going to have to deal with [the_person.so_title]'s anger."
                if the_person.kids > 0:
                    the_person "... Again."
            else:
                the_person "Oh fuck, I said to pull out! I'm not on the pill [the_person.mc_title], what happens if I get pregnant?"
                $ the_person.update_birth_control_knowledge()
                the_person "What is wrong with you? You know I'm not on the pill! Now look what you've done... I guess next time we'll have to use a condom."
        elif the_person.is_infertile:
            the_person "Unbelievable! I told you to pull out, and now you've gone and made a mess... What a pain in the ass..."
        elif the_person.has_significant_other:
            the_person "You're really going to make me tell [the_person.so_title] about this, aren't you? Fine, I'll deal with it. Just be more careful next time."
            $ the_person.update_birth_control_knowledge()
            the_person "I don't want to have to make you wear a condom, so be a little more careful next time."
        elif the_person.opinion.creampies < 0:
            the_person "Oh, great. Just what I needed. You couldn't even follow a simple instruction, could you? Now look at what a mess you've made..."
        else:
            the_person "You really need to work on your timing. I told you to pull out, not do the exact opposite!"
            the_person "Just remember, I'm not going to be as forgiving next time if you can't follow simple instructions."
    return

label tsundere_cum_anal(the_person):
    if the_person.has_taboo("anal creampie"):
        $ the_person.call_dialogue("anal_creampie_taboo_break")
        $ the_person.break_taboo("anal creampie")
        return

    if the_person.sluttiness > 75 or the_person.opinion.anal_creampies > 0:
        the_person "Ugh, fine... I guess it's okay if you do that... But don't think I'm going to start asking for it all the time!"
    elif the_person.opinion.anal_creampies < 0:
        the_person "Oh, come on... not in there! I don't need to be embarrassed like that!"
    else:
        the_person "Oh, alright... if you insist... But just this once, and don't think I'm going to start liking it or anything..."
    return

label tsundere_surprised_exclaim(the_person):
    $rando = renpy.random.choice(["What the hell?","Ugh, really?","Why now?","This again?","Not again!", "Seriously?", "Great...", "Oh, joy...", "Fucking perfect...", "Unbelievable!", "Not again!", "Why can't I have a normal day?"])
    the_person "[rando]"
    return

label tsundere_talk_busy(the_person):
    if the_person.obedience > 120:
        the_person "Ugh, I don't have time for this. I've got way too much on my plate right now, [the_person.mc_title]."
    else:
        the_person "Listen, I'd love to catch up, but I'm swamped with things to do. Maybe we can talk later?"
    return

label tsundere_sex_strip(the_person):
    if the_person.sluttiness < 20:
        if the_person.arousal_perc < 50:
            the_person "Ugh, fine. I'll take off some clothes, but don't think I'm doing this because I like you or anything. I just need to get comfortable, that's all."
            mc.name "Come on, babe. It's just us here. You can relax."
            the_person "I don't care! I'm still not comfortable. And don't call me 'babe'. That's weird."
            mc.name "Okay, okay. I'll stop. Just take your time, okay?"
        else:
            the_person "Alright, alright. I'll take off a few things, but don't expect me to be impressed by your reaction. I'm just taking off some clothes, big deal."
            mc.name "Aww, come on. You're being a little rough. Just let me see you a little more, okay?"
            the_person "Fine, but only because you asked nicely. And don't think this means I like you or anything."
    elif the_person.sluttiness < 60:
        if the_person.arousal_perc < 50:
            the_person "Fine, I'll make an exception and get a little more comfortable. But don't get any ideas, okay?"
            mc.name "I promise, I won't get any ideas. I just want to make sure you're comfortable."
            the_person "Ugh, fine. But don't think I'm doing this for you. I just need to get a little more comfortable."
            mc.name "I understand. Just take your time and let me know if you need anything."
        else:
            the_person "Okay, okay. I'll take off a few more things if it'll make you happy. But don't think I'm doing this because I'm into you or anything."
            mc.name "I know, I know. You're just doing it because you want to, right?"
            the_person "Whatever. Just let me get this off and we can get on with this. And don't think this means I'm going to start liking you or anything."
    else:
        if the_person.arousal_perc < 50:
            the_person "Ugh, fine. I'll do it. But just for you, I'll make an exception. And don't think I'm doing this because I like you or anything."
            mc.name "Thanks, babe. You're making me really happy right now."
            the_person "Don't call me 'babe'. And don't get too happy. I'm just doing this because I have to."
        else:
            the_person "Great, now let me get this off and we can get on with this. I'm dying over here! But don't expect me to be all happy about it or anything."
            mc.name "Aww, come on. You're being a little grumpy. Let's just have some fun, okay?"
            the_person "Fine. But don't expect me to start smiling and laughing or anything."
    return

label tsundere_sex_watch(the_person, the_sex_person, the_position):
    $ title = the_person.title if not the_person.is_stranger else "The stranger"
    if the_person.sluttiness < the_position.slut_requirement - 20:
        $ the_person.draw_person(emotion = "angry", display_transform = character_left_flipped)
        the_person "Ugh, seriously? Can you two keep it down? I'm trying to fucking concentrate."
        $ the_person.change_stats(obedience = -2, happiness = -1)
        "[title] rolls her eyes and tries to ignore you and [the_sex_person.fname] [the_position.verb]."
        return False
    if the_person.sluttiness < the_position.slut_requirement - 10:
        $ the_person.draw_person(display_transform = character_left_flipped)
        the_person "Honestly, you two are so embarrassing. Can't you keep it a little more private?"
        $ the_person.change_happiness(-1)
        "[title] looks away, trying to pretend she's not interested in what you and [the_sex_person.fname] are doing."
        return False
    if the_person.sluttiness < the_position.slut_requirement:
        $ the_person.draw_person(display_transform = character_left_flipped)
        if not is_watching(the_person):
            the_person "You're really getting into it, aren't you? I suppose it's kind of hot..."
        $ the_person.change_slut(1, 30)
        "[title] watches you and [the_sex_person.fname] [the_position.verb], trying not to blush."
        return True
    if the_person.sluttiness >= the_position.slut_requirement and the_person.sluttiness < the_position.slut_cap:
        $ the_person.draw_person(display_transform = character_left_flipped)
        if not is_watching(the_person):
            the_person "Oh, wow... this looks like so much fun. Can I join in?"
        $ the_person.change_slut(1, 50)
        "[title] watches you and [the_sex_person.fname] [the_position.verb], her eyes sparkling with excitement."
        return True
    $ the_person.draw_person(emotion = "happy", display_transform = character_left_flipped)
    if renpy.random.randint(0, 1) == 0:
        the_person "You know, [the_person.mc_title], [the_sex_person.fname] is really getting into this. Maybe you should, uh, spice things up a bit?"
    else:
        call watcher_position_comment(the_person, the_sex_person, the_position) from _call_watcher_position_comment_tsundere_sex_watch
    "[title] watches with interest as you and [the_sex_person.fname] [the_position.verb]."
    return True

label tsundere_being_watched(the_person, the_watcher, the_position):
    $ title = the_watcher.fname if not the_watcher.is_stranger else "the stranger"
    if the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #They agree you should give it to her harder
        the_person "Hmph, I guess you're right, [the_person.mc_title]."
        the_person "But don't think I'm going easy on you just because there's an audience..."
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [title] watching you and her [the_position.verb]."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's super slutty and doesn't care what people think.
        the_person "You know, [title], I don't really care what you think, but it's pretty obvious you're turned on right now."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #She's super slutty and encourages the watcher to be slutty.
        the_person "Oh, come on, [title]! Don't be shy! You know you want a taste of this action!"
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [title] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #She's into it and encouraged by the slut watching her.
        "[the_person.fname] glances at [title]."
        the_person "Yeah, I guess I can handle a little more... for now."
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [title] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's into it but shamed by the prude watching her.
        the_person "Ugh, why do you have to be here, [title]? Can't you just leave me alone?"
        $ the_person.change_stats(arousal = -1, slut = -1)
        "[the_person.title] seems uncomfortable with [title] nearby."

    else: #the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #They're both into it but not fanatical about it.
        "[the_person.possessive_title!c] rolls her eyes at [title]."
        the_person "Whatever, [title], you're missing out. Maybe next time you'll get a chance."
        $ the_person.change_stats(arousal = 1, slut = 1, max_slut = 30)
        "[the_person.title] seems more comfortable [the_position.verbing] you with [title] around."

    return

label tsundere_work_enter_greeting(the_person):
    if the_person.happiness < 80 or the_person.love < 0:
        "[the_person.title] glances at you when you enter the room, her expression unreadable."
        the_person "What do you want? I'm in the middle of something."
        "She goes back to her work, not looking up again."

    elif the_person.happiness > 130:
        if the_person.sluttiness > 40:
            the_person "Hey [the_person.mc_title], just the person I was hoping to see."
            "Her eyes sparkle with mischief as she leans against her desk."
            the_person "You know what they say: all work and no play makes for a dull girl."
            "She winks, inviting you to join her in some 'play'."
        else:
            "[the_person.title] looks up from her work and smiles at you when you enter the room."
            the_person "Hey [the_person.mc_title], it's nice to have you stop by. You know, just to say hi."
            "She blushes slightly, looking away before quickly glancing back at you."
    else:
        if the_person.sluttiness > 60:
            $ the_person.draw_person(position = "stand4")
            "[the_person.title] walks over to you when you come into the room, her hips swaying seductively."
            the_person "Well, well, well. Look who decided to drop by."
            "She leans in close, her voice husky and sultry."
            the_person "I've been waiting for you, [the_person.mc_title]. You know, just to catch up."
            "She brushes her fingers against your arm, sending shivers down your spine."
        else:
            the_person "Hey [the_person.mc_title]. Need anything? I mean, if you're not too busy..."
            "She looks up at you, her eyes soft and inviting."
    return

label tsundere_date_seduction(the_person):
    if the_person.is_girlfriend:
        "[the_person.possessive_title!c] grabs your hand and pulls you around to look at her."
        the_person "Hey, that was such a great time. So I was thinking..."
        $ mc.change_locked_clarity(30)
        if the_person.effective_sluttiness(["vaginal_sex", "condomless_sex"]) > 60 and the_person.wants_creampie and the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex >= 0 and the_person.opinion.creampies >= 0 and not the_person.on_birth_control and not the_person.knows_pregnant:
            if the_person.opinion.creampies > 0: #No condoms, loves creampies, she's basically asking you to knock her up. So... have her ask you to knock her up!
                the_person "You're probably just going to say no, but I really want to get knocked up by someone like you."
                the_person "So, are you going to make me pregnant or what? I bet you could give me some amazing kids."
            else:
                the_person "I don't care if you don't use a condom. I just want you to fuck me and make me feel good."
                the_person "You're so much better than those other guys, anyway."
        elif the_person.effective_sluttiness(["vaginal_sex", "condomless_sex"]) > 60 and the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex > 0:
            the_person "Ugh, fine. If you really want to know, I'd rather not use a condom."
            the_person "But don't think I'm doing it for you or anything. It just feels better that way."
        elif the_person.effective_sluttiness(["vaginal_sex"]) > 50 and the_person.opinion.vaginal_sex > 0:
            the_person "You know, I didn't really want to go home with someone like you."
            the_person "But you're kind of growing on me."
            the_person "So, do you want to fuck me or what?"
        elif the_person.effective_sluttiness(["anal_sex"]) > 60 and the_person.opinion.anal_sex > 0:
            the_person "I don't know why I'm even bothering to ask you this, but... do you want to fuck my ass?"
            the_person "It's not like I'm asking for much, but you're probably just going to say no anyway."
        elif the_person.effective_sluttiness(["sucking_cock"]) > 40 and the_person.opinion.giving_blowjobs > 0:
            the_person "You know, I'm not really in the mood to do this, but... you're kind of cute when you're all worked up."
            the_person "So, do you want a blowjob or what?"
        elif the_person.effective_sluttiness() > 40 and the_person.opinion.being_covered_in_cum > 0:
            the_person "Ugh, fine. If you really want to know, I'd be okay with getting covered in your cum."
            the_person "But don't expect me to be all happy about it or anything."
        elif the_person.effective_sluttiness(["touching_body"]) > 40 and the_person.opinion.giving_tit_fucks > 0 and the_person.has_large_tits:
            the_person "I don't know why I'm even telling you this, but... I'd be okay with sucking you off between my tits."
            the_person "But don't think I'm doing it because I like you or anything."
        else: #She's not very slutty, so she leaves the invitation open to interpretation
            the_person "You know, I don't really feel like going home with you or anything..."
            the_person "But I guess I could be persuaded if you do something really good."
            "She smirks, leaving the invitation open-ended."
    elif the_person.is_affair:
        the_person "So my [the_person.so_title] won't be home tonight, I was thinking..."
        "She reaches down and cups your crotch, rubbing it gently through your pants."
        $ mc.change_locked_clarity(40)
        if the_person.wants_creampie and the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex >= 0 and the_person.opinion.creampies >= 0 and not the_person.on_birth_control and not the_person.knows_pregnant:
            if the_person.opinion.creampies > 0: #No condoms, loves creampies, she's basically asking you to knock her up. So... have her ask you to knock her up!
                the_person "Fine, let's go back to my place so you can pin me to the bed and creampie me all night long."
                the_person "I swear, just the thought of your cum inside me is making me want to puke and yet... I'm getting wet."
            else:
                the_person "Alright, let's go back to my place. You can pin me to the bed and fuck me bareback all night long."
                the_person "I hate how much I want this, but I do. So just fuck me up with your cock already."
        elif the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex > 0:
            # the_person "Do you want to come over to my place and fuck me all night long? No condoms allowed."
            the_person "Ugh, fine. Let's go back to my place and fuck all night. No condoms."
            the_person "I don't want to admit it, but I'm really looking forward to this."
        elif the_person.opinion.vaginal_sex > 0:
            the_person "Fine, let's go back to my place and you can pound my tight fucking pussy until I'm a wreck."
            the_person "I hate how much I enjoy this, but... I do. So do it."
        elif the_person.opinion.anal_sex > 0:
            the_person "Ugh, alright. Let's go back to my place so you can... you know."
            the_person "I don't want to admit it, but my ass is really excited for this."
        elif the_person.opinion.giving_blowjobs > 0:
            the_person "Fine, let's go back to my place and you can choke me out with your cock."
            the_person "I hate how much I want this, but I do. So just do it already."
        elif the_person.opinion.being_covered_in_cum > 0:
            the_person "Ugh, alright. Let's go back to my place, and you can cover me in your sperm all night."
            the_person "I hate how much I enjoy this, but... I do. So just do it."
        elif the_person.opinion.giving_tit_fucks > 0 and the_person.has_large_tits:
            the_person "Fine, let's go back to my place so I can... you know."
            the_person "I hate how much I enjoy this, but I do. So just do it already."
        elif the_person.opinion.cheating_on_men > 0:
            the_person "Ugh, fine. Let's go back to my place, and you can do all the things I tell my [the_person.so_title] I hate."
            the_person "I don't want to admit it, but I'm really looking forward to this."
        else:
            the_person "Ugh, let's go back to my place and make him really regret leaving me alone for the night."
    elif not the_person.has_significant_other:
        $ mc.change_locked_clarity(20)
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                the_person "Ugh, fine. I've had a blast [the_person.mc_title], but there are a few more things I'd like to do with you. Want to come back to my place and find out what they are?"
            else:
                the_person "Whatever. You've been a blast [the_person.mc_title]. Want to come back to my place, have a few drinks, and see where things lead? I suppose."
        else:
            if the_person.love > 40:
                the_person "Fine, I don't want to say goodbye either. Tonight's been amazing [the_person.mc_title]. Do you want to come back to my place and have a few drinks?"
            else:
                the_person "Whatever. This might be crazy, but I had a great time tonight and you make me a little crazy. Do you want to come back to my place and see where things go? I don't know why I'm even asking."
    else:
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                $ mc.change_locked_clarity(20)
                the_person "Ugh, fine. I'm not done with you yet [the_person.mc_title]. Want to come back to my place? But don't think you're getting away with anything."
                the_person "My [the_person.so_title] won't be home until morning, so we would have plenty of time."
            else:
                $ mc.change_locked_clarity(20)
                the_person "Whatever. This might be crazy, but do you want to come back to have another drink with me? I suppose."
                the_person "My [the_person.so_title] is stuck at work and I don't want to be left all alone."
        else:
            if the_person.love > 40:
                $ mc.change_locked_clarity(20)
                the_person "Whatever. You're making me feel crazy [the_person.mc_title]. Do you want to come have a drink at my place? But don't think this means anything."
                the_person "My [the_person.so_title] won't be home until morning, and we have a big bed you could help me warm up."
            else:
                $ mc.change_locked_clarity(20)
                the_person "Whatever. This is crazy, but would you want to have one last drink at my place? My [the_person.so_title] won't be home until morning... I suppose."
    return

label tsundere_sex_end_early(the_person):
    if the_person.sluttiness > 50:
        if the_person.love > 40:
            if the_person.arousal_perc > 60:
                the_person "Ugh, really? You're done already? I was just getting into it, [mc.name]... I mean, you're not exactly the most energetic partner I've ever had..."
                the_person "But hey, I'll give you credit, you did try your best. Or at least, as best as you could."
            else:
                the_person "Well, I suppose that's it? I was ready to give you a lot more... But I guess you're not exactly the most enthusiastic about this whole situation, are you?"
        else:
            if the_person.arousal_perc > 60:
                the_person "Hmph, you're sure you're finished? I was really enjoying this... You know, I don't usually do this, but I was actually getting kind of into it."
                the_person "But I guess you're not exactly the most experienced, are you? I mean, it's not like I'm the one who needs to learn how to do this properly..."
            else:
                the_person "I guess it was okay, I suppose. I mean, it's not like I was expecting much from you in the first place..."
    else:
        if the_person.love > 40:
            if the_person.arousal_perc > 60:
                the_person "Oh, come on, [mc.name], you can't leave me hanging like this... I mean, I was actually starting to enjoy this!"
                the_person "But hey, I guess you're not exactly the most romantic guy out there, are you?"
            else:
                the_person "Well, that was a nice little interlude, I suppose. I mean, it's not like I'm the type to be all lovey-dovey and shit..."
        else:
            if the_person.arousal_perc > 60:
                the_person "Geez, I guess that was enough... I mean, I don't know why you even bother trying, you're not exactly the best at this, are you?"
            else:
                the_person "Good, it's over. Now let's get this over with. I mean, I've got better things to do than hang around with someone who can't even manage to get it right..."
    return

label tsundere_sex_take_control(the_person):
    if the_person.arousal_perc > 60:
        the_person "What do you think you're doing, [mc.name]? Don't just leave me hanging like this! I mean, I'm the one who's supposed to be in control here, not you!"
        the_person "But hey, if you're not going to finish the job, then I will. And don't think for a second that I won't make you regret it."
    else:
        the_person "Ugh, really? You're not even going to finish what you started? Fine, I'll do it myself then! And don't think you can just waltz in here and expect me to be all weak and submissive. I'm not that kind of girl, [mc.name]."
    return

label tsundere_sex_beg_finish(the_person):
    the_person "Okay, fine, [mc.name], you want to play it cool? I'll let you off the hook this time, but just know that I'm going to make you pay for this. And when I'm done, I'm going to make sure you know exactly who's in control here."
    return

label tsundere_sex_review(the_person, the_report):
    $ comment_position = the_person.pick_position_comment(the_report)
    if comment_position is None:
        return #You didn't actually do anything, no need to comment.

    $ used_obedience = the_report.get("obedience_used", False) #True if a girl only tried a position because you ordered her to.
    $ the_person.draw_person()  # make sure she stands up for talking with you

    #She's worried about her SO finding out because it was in public
    if the_report.get("was_public", False) and the_person.has_significant_other and the_person.opinion.cheating_on_men <= 0: #It was public and she cares.
        if the_person.is_affair: #Dialogue about her being into it, but you can't do this in case she gets caught.
            the_person "Ugh, this is so dangerous! I'm really getting into this, but we can't get caught..."
            the_person "What if someone sees us and tells my [the_person.so_title]? I'll never hear the end of it!"
        elif used_obedience:
            the_person "I can't believe we're doing this out in the open! Someone might recognize me and tell my [the_person.so_title]."
            mc.name "Don't worry, nobody's going to tell anyone. We're being careful."
            the_person "I hope you're right... I don't want anyone finding out about this."
        else:
            $ the_person.call_dialogue("surprised_exclaim")
            the_person "Oh no, we're out in public! Someone might see us and tell my [the_person.so_title]. I'll be so screwed!"
            mc.name "Don't worry, nobody's paying attention to us. Nobody's going to tell your [the_person.so_title]."
            the_person "I hope you're right... I don't want anyone knowing about this."

    #She's single, but worried that you did in public.
    elif the_report.get("was_public", False) and (the_person.effective_sluttiness()+10*the_person.opinion.public_sex < comment_position.slut_cap):
        if used_obedience:
            the_person "Ugh, I can't believe we're doing this in public! Everyone's staring at us like we're some kind of perverts..."
            the_person "I'll never live this down, [mc.name]. People are going to talk about this for weeks!"
        else:
            the_person "Oh no, we're in public! Everyone's watching us and judging us for this..."
            mc.name "Don't worry, nobody really cares what we're doing. They're just curious."
            the_person "I hope you're right, or I'm going to end up with a terrible reputation for this sort of thing..."

    elif the_report.get("girl orgasms", 0) > 2:
        if used_obedience:
            the_person "Oh fuck... baby... I loved what you did to me... I never knew being submissive could feel so good..."
            mc.name "I do enjoy when you keep begging me to make you cum again. It's almost like you're addicted to it."
            the_person "Shut up and kiss me, [mc.name]..."
        else:
            the_person "I have never... cum that hard... It was just amazing... I guess I needed that."
            "She seems dazed by her orgasm as she tries to form coherent sentences."
            the_person "You really... know how to give a girl a good time... just gimme a second to catch my breath."
            mc.name "Take your time, I'm not going anywhere."
            the_person "Thanks, [mc.name]... I think I need a minute to recover before we can start again."

        call sex_review_trance(the_person) from _call_sex_review_trance_tsundere_sex_review

    #No special conditions, just respond based on how orgasmed and how slutty the position was.
    elif the_report.get("girl orgasms", 0) > 0 and the_report.get("guy orgasms", 0) > 0: #You both came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position cap, it was tame
            the_person "Ah, that was fucking nice... But I think we could go even further next time. I'm not afraid to push the limits, [mc.name]."
            the_person "Doesn't that sound like fun? I'm getting wet just thinking about it."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "Ah, that was just what I needed! I think we're very compatible, [mc.name]."
            the_person "Let's do it again some time soon, okay? I want to see how much further we can go."

        elif used_obedience: #She only did it because she was commanded
            the_person "Fuck, I... I didn't think I was going to cum like that. I guess I just can't resist a good command, huh?"
            mc.name "Aren't you going to thank me? You obviously had a good time."
            the_person "Shut up and don't get too full of yourself, [mc.name]."

        else: # She's surprised she even tried that.
            the_person "Oh fuck, that was intense! I didn't think I was going to take it so far, but it just felt right, you know?"
            the_person "Don't think that's going to happen every time though, alright? I'm not a slut! I just like to push my boundaries sometimes."
        if the_person.love > 40:
            the_person "You know, I never thought I'd say this, but I think I might actually like this whole 'relationship' thing with you, [mc.name]."
        else:
            the_person "Well, that was fun. Let's do it again sometime, but not too soon, okay? I need to recover my dignity first."
    elif the_report.get("girl orgasms", 0) > 0: #Only she came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            the_person "Done already? Well, that's just not right. Next time I'm going to make sure we both cum and then some."
            the_person "I've got a few ideas that are going to blow you away, [mc.name]."
            "She smiles mischievously, already imagining your next encounter."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "You're all done? Well, that was fucking hot either way, [mc.name]."
            the_person "I'll repay the favour next time, alright? I promise. And maybe we can try something new."
            "She leans in close, whispering in your ear."

        elif used_obedience: #She only did it because she was commanded
            the_person "That's it? I mean, not like I wanted to do anything more, I just thought you were going to finish."
            mc.name "Some other time. I just wanted to see what you look like when you cum."
            the_person "I... Fuck, well, I guess you got what you wanted. But don't think I'm going to make it easy for you next time."
            the_person "It could have been worse, I guess."

        else: # She's surprised she even tried that.
            the_person "Oh fuck, that was intense! You really know how to make a girl feel good, [mc.name]."
            the_person "You're probably tired after all that work. I promise I'll repay the favour next time, okay? And maybe we can try something different."
            "She smiles, already looking forward to your next encounter."

    elif the_report.get("guy orgasms", 0) > 0: #Only you came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            the_person "Hmph, you're all tired out already? That's so frustrating!"
            mc.name "Sorry, I'll make it up to you next time."
            the_person "Well, I suppose I could be persuaded to try again. But don't expect any special treatment!"
            mc.name "Yeah, I think I could handle that."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "You're already done? Such a tease! Fine, I'll let you off this time..."
            mc.name "Sorry, I'll make it up to you next time."
            the_person "You'd better, or you won't be hearing the word 'please' from me again!"

        elif used_obedience: #She only did it because she was commanded
            the_person "I suppose you're worn out from all that... We're finished then?"
            mc.name "Yeah, that's all for now."
            the_person "Fine, but don't think this means you get to slack off next time!"

        else:  # She's surprised she even tried that.
            the_person "Wow, that was... quite an experience. I think I got a little carried away there."
            the_person "Maybe it's for the best that we stop here. I need to think about what I just did..."

    elif the_person.energy < 10: #Nobody came and she's tired
        the_person "Ugh, I can't believe I'm saying this, but I'm just too exhausted. Another time, maybe?"
        mc.name "No worries, we'll do it another day."
        the_person "Just don't expect any special treatment when we try again, got it?"

    else: #Nobody came.
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            the_person "Hmph, you're already done? What's the rush? We could've had more fun!"
            "She crosses her arms, pretending to be upset."
            the_person "You're such a spoilsport [the_person.mc_title]."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "We're stopping? But we were just getting to the good stuff!"
            mc.name "Sorry [the_person.title], maybe another time."
            the_person "Yeah, maybe. You can't just leave a girl hanging like that, you know."

        elif used_obedience: #She only did it because she was commanded
            the_person "Well, I wasn't expecting that. I thought you had more in mind."
            mc.name "You aren't disappointed, are you?"
            the_person "No, no. I just...wanted to see where things would go, that's all."
            the_person "It's fine. I'll just have to find someone else to take me further."

        else:  # She's surprised she even tried that.
            the_person "Ugh, you're probably right. We should stop now before we get too carried away."
            the_person "I don't want to do something I'll regret later. Let's just keep this casual, okay?"

    # Gave creampie while she is not on birth control (extra dialogue when she could get pregnant)
    if the_report.get("creampies", 0) > 0 and not the_person.on_birth_control and not the_person.knows_pregnant:
        the_person "Well, I guess we just made things a little more interesting, didn't we?"
        the_person "If I get pregnant, it'll serve you right for being so reckless!"

    $ del comment_position
    return

## Role Specific Section ##

label tsundere_improved_serum_unlock(the_person):
    mc.name "[the_person.title], now that you've had some time to get used to the lab there is something I want to talk to you about."
    the_person "Yeah, what's on your mind?"
    mc.name "Our R&D up to this point has been based on my old notes from university."
    mc.name "There were some unofficial experiment results that suggested the effects might be enhanced by sexual arousal."
    "[the_person.title] raises an eyebrow."
    the_person "Ah, so you noticed that too? I have a hypothesis that an orgasm opens chemical receptors that are normally blocked."
    mc.name "What if that's true? Does that open up any more paths for our research?"
    the_person "If it's true, I could leverage the effect to induce greater effects in our subjects."
    "[the_person.possessive_title!c] grins mischievously."
    the_person "We'll need to do some experiments to be sure."
    mc.name "What kind of experiments?"
    the_person "I want to take a dose of serum myself, and you can record the effects."
    the_person "Then I'll...ahem...stimulate myself, and we can compare the effects after."
    mc.name "Do you really think that's a good idea?"
    the_person "Not really, but we can't trust anyone else with this information if we're right."
    the_person "We might be able to make progress by brute force, but this is a chance to take our research to the next level."
    the_person "A finished dose of serum that raises my Suggestibility. The higher it gets, the better."
    the_person "Then we'll just need some time and some privacy for me to see what sort of effects my...ahem...stimulation will have."
    return

#
# label tsundere_improved_serum_unlock(the_person):
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

label tsundere_kissing_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 30:
        the_person "Fine, let's just get this over with. You've always been curious, right?"
        mc.name "That's not true, but I'll play along."
        the_person "Hmph, whatever. Just shut up and kiss me already."
        mc.name "Oh, I'm not going to shut up that easily."
        the_person "Suit yourself. I'll just have to find someone else who's willing to kiss me."
        mc.name "Hold on, wait a minute. I'm not going anywhere."
        the_person "Oh? You're not going anywhere? Then get over here and kiss me already!"
        mc.name "Alright, alright. Here I come."
    elif the_person.love >= 20:
        the_person "So we're doing this, huh? About time, if you ask me."
        mc.name "I guess we are. What do you think?"
        the_person "It's about time we finally made out, [the_person.mc_title]."
        mc.name "I'm glad you feel that way."
        the_person "Me too. Just be gentle, okay?"
        mc.name "I will."
    else:
        the_person "I don't know if this is a good idea, [the_person.mc_title]. We're taking things too fast, aren't we?"
        mc.name "Are you scared?"
        the_person "No! I'm just...not sure if this is a good idea. But I trust you."
        mc.name "Good. Because I'm not going to let you back out now."
        the_person "Hmph. Fine. But if this is a mistake, it's on you."
        mc.name "It'll be worth it, I promise."
    return

label tsundere_touching_body_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 30:
        the_person "Come on then, don't be shy. You've wanted to touch me for ages, haven't you?"
        mc.name "Hey, I'm not that obvious!"
        the_person "Oh, please. I can see the way you look at me."
        mc.name "Well, I can't help it if you're irresistible."
        the_person "Irresistible? Pfft, you're just trying to get in my pants."
    elif the_person.love >= 20:
        the_person "So you're ready for this?"
        "You nod."
        the_person "Me too, I think. I didn't think I'd be so nervous when you actually made a move."
        mc.name "Just relax. You trust me, right?"
        the_person "Of course. Just don't expect me to be all touchy-feely about it."
    else:
        the_person "I think you're getting a little ahead of yourself here [the_person.mc_title]."
        mc.name "What do you mean?"
        the_person "I mean I don't just let anyone feel me up. Maybe we should cool things down."
        mc.name "You're not scared, are you?"
        the_person "Scared? Of course not!"
        mc.name "Well then just relax and go with it. It doesn't have to mean anything unless we want it to."
        "You see her answer in her eyes before she says anything."
        the_person "You're so bad for me, you know that?"
        mc.name "Well let me make up for it then."
        the_person "Hmm, maybe I'll let you."
    return

label tsundere_touching_penis_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 35:
        the_person "Oh, you're really enjoying this, aren't you? Look how hard you are."
        mc.name "Do you want to feel it? You can if you want."
        the_person "Yeah, why not? I'll try not to hurt it."

    elif the_person.love >= 20:
        the_person "Your cock looks so nice when it's hard. Can I touch it?"
        mc.name "Go ahead, it doesn't bite."
        the_person "Well, it might if you're not careful."

    else:
        mc.name "My cock is so hard right now [the_person.title]. Put your hand on it and touch it for me."
        the_person "What? That's taking things a little far, don't you think?"
        mc.name "Come on, you know you want to. Just a few strokes, then if you aren't impressed you can stop."
        the_person "Fine, but don't expect me to make any promises after this."
        mc.name "I wouldn't dream of it."
        the_person "Hmm, okay then. I'll give it a try."
    "She reaches out and wraps her hand around your cock, her touch gentle but firm."
    "You feel a surge of pleasure as she starts to stroke you."
    the_person "Mmm, you're really nice when you're hard."
    return

label tsundere_touching_vagina_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 35:
        the_person "Come on, don't be shy. You've been dying to touch my pussy, admit it."
    elif the_person.love >= 20:
        the_person "Oh fuck, you've got my pussy tingling. I want you to touch it [the_person.mc_title]."
        mc.name "You sure? I don't want to push you too far."
        the_person "No, I want it. I want you to touch me."
    else:
        the_person "I don't know if we should be doing this [the_person.mc_title]..."
        mc.name "Just take a deep breath and relax. I'm just going to touch you a little, and if you don't like it I'll stop."
        the_person "Just a little?"
        mc.name "Just a little. Trust me, it's going to feel amazing."
        the_person "Hmm, okay. But don't think this means I'm easy."
        mc.name "I wouldn't dream of it."
    return

label tsundere_sucking_cock_taboo_break(the_person):
    mc.name "I want you to do something for me."
    the_person "Oh yeah? What do you want me to do to you?"
    mc.name "I want you to suck on my cock."
    if the_person.effective_sluttiness() >= 45:
        the_person "Mmm, I think I'm up for that. It's not going to be too big for me, is it?"
        mc.name "I think you'll be able to handle it."
        the_person "Alright, I don't want it choking me."
        "She bites her lip and winks at you."
        the_person "That's a lie. A little choking is okay."
    elif the_person.love >= 30:
        the_person "I guess we've been dancing around it for a while."
        "She bites her lip and looks your body up and down."
        the_person "Alright, let's do this."
    else:
        the_person "Oh, I was wondering if this was going to come up..."
        "She laughs nervously and looks away from you."
        the_person "I don't know [the_person.mc_title]..."
        "You reach up and hold her chin, turning her head back to face you."
        mc.name "Don't overthink it. Just kneel down and suck on it for me. If you don't like doing it, we can just forget it happened."
        "You can see in her eyes the moment her resolve breaks. She bites her lip and nods."
        the_person "Alright, let's do this."
        "She slowly gets down on her knees, her eyes darting between your face and your cock with a mix of reluctance and curiosity."
        the_person "You know, I never thought I'd be doing this. But I guess I'm willing to try new things for you."
        "She takes a deep breath, her hand wrapping around the base of your cock as she leans in to take it in her mouth."
        "As she starts to suck, her eyes flash up to meet yours, a hint of defiance and challenge in them."
        the_person "Satisfied now?"
    return

label tsundere_licking_pussy_taboo_break(the_person):
    mc.name "I want to taste your pussy [the_person.title]. Are you ready?"
    if the_person.effective_sluttiness() >= 45:
        the_person "Hmph, I don't need your permission or anything, but fine. I'm ready."
        mc.name "Good. But don't expect me to go easy on you just because it's your first time."
        the_person "Oh, please. I've had better."
    elif the_person.love >= 30:
        the_person "Finally, a man who knows how to treat a woman right. I'm ready when you are."
        mc.name "That's what I like to hear."
    else:
        if the_person.has_taboo("sucking_cock"):
            the_person "You know, I never thought I'd see the day where you'd be willing to do this."
            "She bites her lip and smirks at you."
            the_person "But I guess I'm not going to complain. Just don't expect me to be all grateful or anything."
        else:
            the_person "About time you decided to make up for not sucking my cock."
            "She rolls her eyes and smiles."
            the_person "But fine, I'm ready. Just don't expect me to be all appreciative or anything."
    "She lies back, her eyes darting between yours and the area you're about to explore."
    the_person "And don't think this means I'm some kind of slut for letting you do this."
    mc.name "I wouldn't dream of it. You're just being a good sport, right?"
    the_person "Something like that..."
    "She closes her eyes, her face flushed with embarrassment as you start to lick her."
    return

label tsundere_vaginal_sex_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 60:
        the_person "Ugh, finally! I've been waiting for this moment all night. Come on then, get that cock inside me and fuck me like you mean it!"
    elif the_person.love >= 45:
        the_person "Alright, show me what you've got. I'm ready for this."
        mc.name "You better be. I'm going to make sure you remember this."
        the_person "Bring it on! I can take it."
    else:
        if the_person.has_taboo("anal_sex"):
            the_person "Well, well, well. Look at that cock. I guess we're going to find out just how tight my pussy is."
            mc.name "That's the plan. And if you're a good girl, I might just make it worth your while."
            the_person "Hmph, I'm always good. Now get to it before I change my mind."
        else:
            the_person "Oh, so that's what you're going to do with that big cock of yours. Well, I guess we'll see how it feels."
            mc.name "We sure will. And if you're lucky, I might just make it feel even better."
            the_person "Ugh, just get on with it already! I'm not getting any younger."
    return

label tsundere_anal_sex_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 75:
        the_person "Ugh, fine. But only because I can't resist you. Your cock is so big, I'm surprised it fits in your pants!"
        "She seems more excited by the prospect than intimidated."
        mc.name "Don't worry, I'll take it slow and make sure you're comfortable."
    elif the_person.love >= 60:
        the_person "Are you sure you want to do this? I'm not exactly the most experienced person when it comes to anal..."
        mc.name "I'll be gentle, don't worry."
        the_person "Alright, but if it hurts too much, I'm stopping."
    else:
        if the_person.has_taboo("vaginal_sex"):
            the_person "Wait, are you sure you want to do this? My ass might be too tight for your cock!"
            mc.name "I'll make it fit, but you might feel a little sore afterward."
            the_person "Oh, great. Just what I needed."
        else:
            the_person "Come on, [mc.name]. Let's just get this over with. I don't know what's gotten into me today."
            mc.name "Are you sure you're okay with this?"
            the_person "Of course, I'm just... nervous. And a little embarrassed. But let's just do this already!"
            "She blushes and looks away."
            mc.name "Alright, let's get started then."
            the_person "Hurry up, I'm ready when you are."
    return

label tsundere_condomless_sex_taboo_break(the_person):
    if the_person.knows_pregnant:
        the_person "Ugh, you really want to do it without a condom? Fine, but don't say I didn't warn you."
        if the_person.wants_creampie:
            the_person "If you're going to cum inside me, please make it worth my while."
        else:
            the_person "Just make sure to cover me with your... you know, stuff."
    elif the_person.opinion.bareback_sex > 0:
        the_person "Whatever, you want to do it bareback, huh? Just don't say I didn't warn you."
        if the_person.on_birth_control:
            the_person "I'm on the pill, so you don't have to worry about it."
            $ the_person.update_birth_control_knowledge()
        elif the_person.wants_creampie:
            the_person "But if you're going to cum inside me, you'd better make it worth my while."
        elif the_person.opinion.creampies < 0:
            the_person "Just don't get me pregnant, okay? That would be a huge pain."
        else:
            the_person "Alright, just make sure you pull out this time."

    elif the_person.love > 60:
        if the_person.on_birth_control:
            the_person "Ugh, fine, I'm on the pill. Don't say I didn't warn you."
            $ the_person.update_birth_control_knowledge()
        elif the_person.wants_creampie:
            the_person "You're always trying to make me do stupid things, aren't you? Fine, if we're going to do this, make it worth my while."
            mc.name "Are you on the pill?"
            "She rolls her eyes."
            the_person "No, I'm not. But if you're going to cum inside me, you'd better make it worth it."
            $ the_person.update_birth_control_knowledge()
        elif the_person.opinion.creampies < 0:
            the_person "You're always trying to make me do stupid things, aren't you? Fine, just don't get me pregnant."
            the_person "I'm not ready for that kind of responsibility again."
        else:
            the_person "You're always trying to make me do stupid things, aren't you? Fine, just make sure you pull out this time."
            if the_person.kids == 0:
                the_person "I need you to pull out though. I'm not quite ready to be a mother, even with you."
            elif the_person.kids == 1:
                the_person "I need you to pull out though. I've already got a kid, I don't need another one."
            else:
                the_person "I need you to pull out though. I've already got kids, I don't need another one."

    else:
        if the_person.on_birth_control:
            the_person "Hmph, you want to get busy without a rubber? Well, I'm on the pill, so I guess it's fine. Just don't expect any special treatment."
            $ the_person.update_birth_control_knowledge()
        elif the_person.has_taboo("vaginal_sex"):
            the_person "You're really not going to use a condom? I'm not on the pill, so we could end up with a little surprise."
            $ the_person.update_birth_control_knowledge()
            the_person "Or is this your sneaky plan to make a baby out of me?"
            mc.name "I swear I'll pull out. I want our first time to be memorable."
            "She crosses her arms and gives a half-hearted sigh."
            the_person "Ugh, fine. But you better pull out, or you'll regret it."
        else:
            the_person "You're really not going to use a condom? I'm not on the pill, so we could end up with a little surprise."
            $ the_person.update_birth_control_knowledge()
            the_person "Or is this your sneaky plan to make a baby out of me?"
            mc.name "I promise I'll pull out. It'll feel so much better without anything between us."
            the_person "God, I know. I'm trying to be rational here, not some lust-driven animal."
            "She huffs and puffs."
            the_person "Fine, no condom. Just remember to pull out, got it? Good."
    return

label tsundere_underwear_nudity_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > 30 - (the_person.opinion.skimpy_outfits * 5):
        the_person "You want to see me in my underwear, huh? It's about time you asked."
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "What are we waiting for then, let's get this off of you."
        else:
            mc.name "Yeah, yeah. We've been over this. You're not exactly subtle about it."
            the_person "Shut up! I just don't want you to get the wrong idea."
            mc.name "Wrong idea? Like how you're not wearing anything under this skirt?"
            the_person "Ugh, fine. But don't say I didn't warn you."
    elif the_person.love > 15:
        the_person "You want me to strip me down a little? It's about time, I was wondering why you were taking things so slow."
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "Oh, don't give me that. You know you want to show off."
            the_person "Fine, but if this gets out of hand, I'm blaming you."
            mc.name "Promise?"
            the_person "Yeah, yeah. Now get this [the_clothing.display_name] off."

        else:
            mc.name "Yeah, I know. You've been teasing me for weeks."
            the_person "Teasing? I'm just being friendly."
            mc.name "Right. Now let's get you out of these clothes."
            the_person "Ugh, fine. But don't think this means I'm going easy on you."
            "She slowly starts taking [the_clothing.display_name] off."

    else:
        the_person "You really want to see me like this? Fine, but don't say I didn't warn you."
        the_person "If you take my [the_clothing.display_name] I'll only have my underwear on, you know that?"
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "Yeah, that's kind of the point."
            "She shakes her head and laughs to herself."
            the_person "Whatever, but if you think I'm doing this because I want to..."
        else:
            mc.name "Yeah, I know. You're not exactly shy."
            the_person "Hey, I'm just being cautious. You can't blame a girl for being careful."
            mc.name "Of course not. Now let's get you out of these clothes."
            the_person "Fine, but don't think this means I'm going easy on you."
    return

label tsundere_bare_tits_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > (40 - the_person.opinion.showing_her_tits * 5):
        the_person "Why do you want to see my tits now, all of a sudden? Like I don't already know you're checking me out."
        if the_person.has_large_tits:
            "She reluctantly shakes her chest for you, jiggling the [the_person.tits_description] hidden underneath her [the_clothing.display_name]."
        else:
            "She reluctantly shakes her chest and gives her [the_person.tits_description] a little jiggle."
        the_person "You're always so eager, aren't you? I guess I can show you, but don't get too excited."
        if the_person.has_large_tits:
            mc.name "Oh, I've been looking. Now let's get those puppies out where I can enjoy them."
        else:
            mc.name "Oh, I've been looking. Now let's get those cute little things out."

    elif the_person.love > 25:
        the_person "Are you really sure you want to see my tits, [the_person.mc_title]?"
        if the_person.has_large_tits:
            "She rolls her eyes and shakes her chest, jiggling her nice [the_person.tits_description], barely restrained by her [the_clothing.display_name]."
        else:
            "She rolls her eyes and shakes her chest, giving her [the_person.tits_description] a little jiggle."
        mc.name "Of course I am. You know I love your tits."
        the_person "Well, I suppose you're entitled to see them then... but don't think this means I'm going to start showing them off to everyone."

    else:
        the_person "Wait, no! Don't look at me like that! You should at least ask a girl before you try and put her tits on full display!"
        mc.name "Come on, don't be like that. I bet your tits look great."
        the_person "They do, but I still feel a little self-conscious about being naked around you, alright?"
        mc.name "There's no need to be. Just relax and let me take your [the_clothing.display_name] off for you."
        the_person "Ugh, fine... but don't think this means I'm going to start showing off my body to everyone!"
    return

label tsundere_bare_pussy_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > (50 - the_person.opinion.showing_her_ass * 5):
        the_person "So you want to see my pussy, huh? Like I don't already know you're thinking about it."
        if the_person.has_taboo("touching_vagina"):
            "She reluctantly lifts her hips, allowing you to slowly remove her [the_clothing.display_name] and reveal her pussy."
        else:
            "She lifts her hips, giving you a quick glimpse of her pussy before covering it back up."
        the_person "Well, you got your wish. Don't say I didn't warn you."

    elif the_person.love > 35:
        the_person "You want to see my pussy, really? Are you sure you're ready for that?"
        if the_person.has_taboo("touching_vagina"):
            mc.name "I think I am. I've been wanting to see it for a while."
            the_person "Hmm, well... I suppose you've earned it. Just remember, you asked for this."
        else:
            mc.name "I've already felt it up, I thought I should see it too."
            the_person "You really are persistent, aren't you? Fine, go on then."

    else:
        the_person "Hold on, you're not getting me out of my [the_clothing.display_name] that easily!"
        if the_person.has_taboo("touching_vagina"):
            mc.name "Come on, just let me see it. I promise I'll be gentle."
            the_person "You're such a liar... But fine, go ahead."
        else:
            mc.name "I've already felt your pussy up, I want to get a look at it now."
            the_person "You're so pushy! Alright, but don't say I didn't warn you."
    return

# label tsundere_facial_cum_taboo_break(the_person):

#     return

# label tsundere_mouth_cum_taboo_break(the_person):

#     return

# label tsundere_body_cum_taboo_break(the_person):

#     return
#==================================================================

label tsundere_creampie_taboo_break(the_person):
    if the_person.wants_creampie:
        if the_person.knows_pregnant:
            the_person "You want to get me pregnant, huh? Fine, I suppose it's about time someone knocked me up."
            "She sighs happily, seeming almost resigned to the idea."

        elif the_person.on_birth_control:
            if the_person.has_significant_other:
                the_person "Oh my god, I'm such a horrible [the_person.so_title]! But I needed this so badly."
                the_person "Maybe if we're lucky, my [the_person.so_title] won't find out."
                "She looks at you with a mischievous grin."
            else:
                the_person "Oh my god, I needed this so badly! Ah... I guess I'll just have to deal with the consequences."

        elif the_person.effective_sluttiness() > 75 or the_person.opinion.creampies > 0:
            if the_person.has_significant_other:
                the_person "You want to get me pregnant? Fine, I suppose it's about time someone knocked me up."
                the_person "Maybe my [the_person.so_title] will finally notice how unhappy I am and do something about it."

            else:
                the_person "You want to get me pregnant? Fine, I suppose it's about time someone knocked me up."
                the_person "I guess I'll just have to deal with the consequences."

            "She sighs happily, but with a hint of annoyance."
            the_person "How long until you're ready for round two? I want as much of your cum inside my pussy as possible."
            the_person "Just don't expect me to be all happy and grateful about it."

        else:
            if the_person.has_significant_other:
                the_person "Oh fuck... I'm such a terrible [the_person.so_title]!"
                "She sighs happily, but with a hint of guilt."
                the_person "But that felt so good..."
            else:
                the_person "Oh fuck, that was so risky."
                "She sighs happily, but with a hint of annoyance."
                the_person "But it felt so good..."
            the_person "I'll just have to hope you haven't knocked me up. We really shouldn't do this again, my luck is going to run out at some point."
            the_person "Besides, I'm not exactly thrilled about the idea of being tied down to a man right now."
    else:
        if the_person.knows_pregnant:
            the_person "Ugh, you're kidding me, right? You got me pregnant?"

        elif not the_person.on_birth_control:
            the_person "Seriously? You didn't even use protection? What if I get pregnant?"

            if the_person.has_significant_other:
                the_person "What if you just got me pregnant? I would be the worst [the_person.so_title] of all time!"

            else:
                the_person "What if I get pregnant? I'm not ready for that kind of responsibility!"
            the_person "You'd better start buying me chocolate and flowers to make up for this."
            the_person "Next time, we're using condoms, or we're not doing it at all! You got it?"

        elif the_person.has_significant_other:
            the_person "Did you really just creampie me after I told you to pull out?"
            "She sighs unhappily."
            the_person "God, I'm such a terrible [the_person.so_title]. Maybe next time I'll make you wear a condom as punishment."

        elif the_person.opinion.creampies < 0:
            the_person "Ugh, this is so unpleasant. Couldn't you have at least made it worth my while?"
            "She rolls her eyes."
            the_person "Next time, at least have the decency to ask if I'm in the mood for a creampie. Or better yet, don't even bother if you're just going to be careless like this."
            the_person "Next time, ask me first if I want a baby."
        else:
            the_person "Are you serious right now? You're really going to give me that attitude after you just...you know?"
            "She huffs and crosses her arms."
            the_person "I swear, you're going to be the death of me. Fine, next time, at least have the decency to clean up after yourself."
    return

label tsundere_anal_creampie_taboo_break(the_person):
    if the_person.opinion.anal_creampies > 0:
        if the_person.effective_sluttiness() > 75 or the_person.opinion.anal_creampies > 1:
            if the_person.has_significant_other:
                the_person "Ugh, fine. I won't tell my [the_person.so_title] about this. But don't think I'm enjoying this..."
                "She says this while wincing in pleasure as you fill her ass with your cream."
                the_person "Ugh, it's just... weirdly satisfying, I guess..."
            else:
                the_person "Ugh, finally! You're actually doing this! I've been waiting for this forever..."
                the_person "Okay, okay, I know it's wrong, but... it feels so good..."
            "She bites her lip, trying to contain her excitement."
            the_person "I guess it's nice... having your cum in my ass..."
        else:
            if the_person.has_significant_other:
                the_person "Ugh, what are you doing? My [the_person.so_title] is going to kill me if he finds out about this..."
                "She moans softly as you continue to fill her ass."
                the_person "Ugh, I can't believe I'm letting you do this... It's just so taboo..."
            else:
                the_person "Ugh, promise you'll do this again? I can't believe I'm saying this, but... it's kind of hot..."
                the_person "All that cum in my tight little ass..."
    else:
        if the_person.has_significant_other:
            the_person "Ugh, seriously? You couldn't pull out? My [the_person.so_title] is going to kill me..."
            "She starts to squirm and try to get away from you."
            the_person "Next time, just shoot your load on my ass, okay?"
        elif the_person.opinion.anal_creampies < -1:
            the_person "Ugh, seriously? You can't even follow simple instructions? My ass is not a creampie dispenser!"
        else:
            the_person "Ugh, not inside! My ass is not a dirty little secret, although that sounds kind of hot..."
    return

label tsundere_dual_penetration_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 75:
        the_person "Ugh, why do you always have to push me to do this? Fine, but don't expect me to enjoy it..."
        "She rolls her eyes and crosses her arms, clearly annoyed but still willing to go through with it."
        mc.name "Don't worry, it'll be worth it."
        the_person "I doubt that, but whatever."
    elif the_person.love >= 60:
        the_person "You're really sure about this? It's going to be a tight fit..."
        mc.name "I'll make sure it fits perfectly."
        the_person "Ugh, just be careful not to hurt me, okay? I don't want any scars..."
    else:
        if the_person.has_taboo("vaginal_sex"):
            the_person "Are you sure my pussy wouldn't be tight enough for you? I mean, I've never done this before..."
            mc.name "It's okay, I'll make it fit. Just try to relax."
            the_person "Ugh, this is so embarrassing..."
        else:
            the_person "Ugh, fine. I guess we're doing this, right? I mean, I can't back out now..."
            mc.name "Are you sure you're ready for this?"
            the_person "Yeah, whatever. Let's just get this over with..."
    return

label tsundere_sleepover_yourplace_response(the_person): #Invited her over to spend the night
    if the_person.love >= 70:
        the_person "Ugh, fine. I'll come over. But don't expect me to be all lovey-dovey or anything..."
        mc.name "I wouldn't dream of it. We'll just have a good time."
        the_person "Yeah, yeah. Just don't get too close, okay? I don't like cuddling or anything."
    elif the_person.sluttiness >= 80:
        the_person "Oh god, I can't wait to get my hands on you. Make sure you have everything ready, so we can have a great night!"
    else:
        the_person "I guess I could come over... But don't expect me to do anything I'm not comfortable with, okay?"
    return

label tsundere_sleepover_herplace_response(the_person): #Spending the night at her place
    if the_person.love >= 70:
        the_person "Ugh, fine. Come over and stay the night, but don't expect me to be all lovey-dovey or anything..."
        mc.name "I wouldn't dream of it. We'll just have a good time."
        the_person "Yeah, yeah. Just don't get too close, okay? I don't like cuddling or anything."
    elif the_person.sluttiness >= 80:
        the_person "Oh god, I can't wait to get you all to myself. Make sure you're ready for a wild night!"
    else:
        the_person "I guess you can come over... But don't expect me to do anything I'm not comfortable with, okay?"
    return

label tsundere_sleepover_yourplace_sex_start(the_person):
    "[the_person.title] rolls her eyes and walks over to you, her expression a mix of annoyance and desire."
    the_person "Ugh, fine. Let's get this over with. Just don't expect me to be all lovey-dovey or anything..."
    return

label tsundere_sleepover_herplace_sex_start(the_person):
    the_person "Ugh, finally. Get over here already."
    "She smirks and crosses her arms, clearly annoyed but still eager for the action to begin."
    mc.name "Are you ready?"
    the_person "Hah! Like I need to be ready for this. Just get in here and do your worst."
    "She leans back on the couch, her legs spread wide in invitation."
    the_person "Hurry up, I'm not getting any younger!"
    return

label tsundere_sleepover_impressed_response(the_person):  #If you've made her cum a lot
    the_person "Ugh, you're really good at that... Don't expect me to admit it, but you're making me feel things..."
    "She rolls her eyes and smirks, trying to hide her true feelings."
    mc.name "You want more?"
    the_person "Hmph, maybe. But don't think you've won me over or anything. I can still handle more..."
    "[the_person.title] lies down in bed, her breathing still ragged from the previous rounds."
    the_person "I might be able to go for another round... But don't get too excited, I'm not making any promises!"
    return

label tsundere_sleepover_good_response(the_person):  #If you've made her cum
    the_person "Ugh, fine. That wasn't too terrible, I suppose."
    "She rolls her eyes and smirks, trying to hide her true feelings."
    mc.name "You want more?"
    $ the_person.draw_person(position = "missionary")
    the_person "Hmph, maybe. But don't think you've won me over or anything. I can still handle more..."
    "[the_person.title] lies down in bed, her breathing still ragged from the previous round."
    the_person "Could you give me another pounding before we go to sleep? But don't expect me to be all lovey-dovey or anything..."
    return

label tsundere_sleepover_bored_response(the_person):  #If she hasn't cum yet
    the_person "Ugh, is that the best you can do? I was expecting more than that from you..."
    "She crosses her arms and looks at you with a bored expression, clearly unimpressed."
    mc.name "What's wrong?"
    the_person "You know, just do better. I expect more from you than this..."
    "She rolls her eyes and smirks, still rubbing her pussy in anticipation."
    the_person "You'd better step it up if you want to keep me interested..."
    return
