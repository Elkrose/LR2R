### PERSONALITY CHARACTERISTICS ###
# The popular phrase tomboy refers to girls who display many characteristics that are mainly attributed to boys. These are girls who are very spirited and like to run and play sports. They have a lot of energy, dislike dresses, and may have more friends who are boys than girls.
#==================================================================
# add more tomboy personality, use different words, and movements.
# update all the following the_person and movements with tomboy personality. Use Juno MacGuff from Juno or Wendy Corduroy from Gravity Falls, for ideas, keep to the structure. Movements in quotations:
### DIALOGUE ###

label tomboy_introduction(the_person):
    mc.name "Hey, can I talk to you for a sec?"
    "[the_person.title] turns around, a look of mild annoyance on her face as she shoves her hands into her pockets."
    the_person "What's up?"
    mc.name "I'm sorry if this is awkward, but you seem like an interesting person."
    "[the_person.title] raises an eyebrow, a hint of a smirk on her lips as she leans against the wall."
    the_person "Interesting? Yeah, I get that a lot. Usually from people who don't know what to make of me."
    mc.name "Well, I was wondering if you'd like to... do something together sometime."
    "[the_person.title] snorts, a dry laugh escaping her lips as she shakes her head."
    the_person "You mean, like, a date or something? No thanks. I'm not really into that sort of thing."
    mc.name "Haha, no, I mean, if you're interested, we could maybe grab coffee or something."
    "[the_person.title] looks at you sideways, a small smile playing on her lips as she shrugs."
    the_person "I guess that sounds okay. But don't expect me to go all gooey on you or anything."
    mc.name "Heh, thanks? I'll take that as a compliment."
    $ the_person.set_title()
    $ the_person.set_possessive_title()
    the_person "So, what's your name, anyway?"
    mc.name "I'm [mc.name]. Nice to meet you..."
    the_person "I'm [the_person.name]. Nice to meet you too, I guess."
    $ the_person.change_happiness(1)
    return

label tomboy_greetings(the_person):
    if the_person.love < 0:
        the_person "Gah, what's your problem now?"
        "She looks up at you with a scowl, her arms crossed over her chest."

    elif the_person.happiness < 90:
        the_person "Hey, I guess. Just don't expect me to be all peppy or anything."
        "She shrugs and looks away, her expression neutral."

    else:
        if the_person.sluttiness > 60:
            if the_person.obedience > 180:
                the_person "Oh, great. You're here again. What do you want, [the_person.mc_title]?"
                "She raises an eyebrow, her tone sarcastic."
            else:
                the_person "Hey, [the_person.mc_title]. Just remember, I'm only doing this because I have to, not because I want to."
                "She looks at you with a hint of annoyance, her arms crossed over her chest."

        else:
            if the_person.obedience > 180:
                the_person "Hey, [the_person.mc_title]. What's up?"
                "She looks at you with a small smile, her expression friendly."
            else:
                the_person "Hey, what's going on? Don't tell me you're here to bother me again, are you?"
                "She looks at you with a mischievous grin, her eyes sparkling with amusement."
    return

label tomboy_sex_responses_foreplay(the_person):
    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] lets out a low, husky moan, her eyes narrowing in pleasure."
            the_person "Gah, okay. You're not totally terrible at this, I guess."
            "She shifts her hips, her movements subtle but encouraging."
        else:
            "[the_person.possessive_title!c] makes a soft, throaty sound, her face relaxing into a gentle smile."
            the_person "I suppose this is kinda okay, I mean."

    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            the_person "Huh, you're not as clueless as I thought. But don't get too cocky, got it?"
            "She raises an eyebrow, her tone teasing but her eyes sparkling with amusement."
        else:
            the_person "I mean, it's not awful or anything. You're not totally useless, I guess."
            "She shrugs, her movements casual but her breathing quickening."

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            the_person "Oh, all right. You're doing something right, I suppose. But don't think this means I'm going to go all gooey on you."
            "She rolls her eyes, her tone sarcastic but her body language betraying her growing arousal."
        else:
            the_person "Alright, alright. You're doing it right, I guess. But don't expect me to get all mushy about it."
            "She nods, her movements curt but her eyes locked on yours."

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "Mmm, I suppose you're getting the hang of this. But don't think this means I'm going to be your little plaything or anything."
            "She smirks, her tone confident but her body language revealing her growing excitement."
        else:
            the_person "You're doing alright, [the_person.mc_title]. But don't expect me to get all affectionate about it or anything."
            "She looks at you, her eyes sparkling with amusement but her expression still guarded."

    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                the_person "Oh, fine. You're getting close to making me cum. But don't think this means I'm going to fall for you or anything."
                "She raises an eyebrow, her tone teasing but her eyes locked on yours."
            else:
                the_person "The way you touch me is just... different, I guess. But don't think this means I've forgiven you for being such a pain in the butt."
                "She smirks, her tone sarcastic but her body language revealing her growing arousal."
        else:
            the_person "Alright, you're almost there. But don't expect me to get all happy and stuff about it."
            "She nods, her movements curt but her eyes sparkling with excitement."
    return

label tomboy_sex_responses_oral(the_person):
    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] looks away, a hint of embarrassment on her face, and mutters under her breath."
            the_person "Gah, you don't have to do that, [the_person.mc_title]... but I guess it's not like I'm going to stop you or anything..."
        else:
            "[the_person.possessive_title!c] looks up at you, her cheeks flushed, and shrugs."
            the_person "I mean, if you want to, I guess it's okay... but don't expect me to be all excited about it or anything..."

    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            the_person "Mmm, I suppose it's not so bad... but don't think this means I'm going to start doing this all the time or anything..."
            "[the_person.possessive_title!c] smirks, her tone teasing but her body language revealing her growing arousal."
        else:
            the_person "Oh, you really want to? Fine... but don't expect me to be all grateful or anything..."

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            the_person "Hmph, well, if you insist... but don't think this means I'm going to start enjoying it or anything..."
            "[the_person.possessive_title!c] lets out a small sigh, her body slightly relaxing, and looks away."
        else:
            the_person "Alright, but don't think I'm doing this because I want to... I'm just humoring you, got it?"
            "[the_person.possessive_title!c] raises an eyebrow, her tone sarcastic but her body language revealing her growing arousal."

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "Mmm, you know, maybe this isn't so bad after all... but don't think this means I'm going to start doing this all the time or anything..."
            "[the_person.possessive_title!c] smirks, her tone teasing but her body language revealing her growing excitement."
        else:
            the_person "Hmph, you're pretty good at this, I'll give you that... but don't expect me to be all impressed or anything..."
            "[the_person.possessive_title!c] nods, her movements curt but her eyes sparkling with amusement."

    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                the_person "Oh, wow... I didn't know you could do that... maybe I should let you do it more often..."
                "[the_person.possessive_title!c] looks up at you, her eyes sparkling with excitement, and smiles."
            else:
                the_person "Mmm, maybe I should let you do that more often... when [the_person.so_title] isn't around, of course..."
                "[the_person.possessive_title!c] smirks, her tone teasing but her body language revealing her growing arousal."
        else:
            the_person "Ugh, fine, but don't think I'm enjoying this... I'm just tolerating it, got it?"
            "[the_person.possessive_title!c] rolls her eyes, her tone sarcastic but her body language revealing her growing excitement."
    return

label tomboy_sex_responses_vaginal(the_person):
    if the_person.energy < 10:
        call low_energy_sex_responses_vaginal(the_person) from _vt_tomboy_call_low_energy_sex_responses_vaginal_10
        return
    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            $ play_moan_sound()
            "[the_person.possessive_title!c] lets out a low, husky moan and shifts her hips, her eyes narrowing in pleasure."
            the_person "Gah, okay. You're not totally terrible at this, I guess. My pussy feels...fine, I suppose."
            "She looks away, her face flushed but her body language revealing her growing arousal."
        else:
            "[the_person.possessive_title!c] bites her lip and stifles a moan, her eyes flashing with annoyance."
            "She looks up at you, her expression neutral but her body language tense."

    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            the_person "Meh, you can keep going if you want, I guess. But don't expect me to be all grateful or anything."
            "She shrugs, her movements casual but her body language revealing her growing arousal."
        else:
            the_person "Ugh, I guess your cock is...alright, I suppose. But don't think this means I'm enjoying it or anything."
            "She looks away, her expression neutral but her body language tense."

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            the_person "Hmm, I suppose you're not completely terrible at this...but don't think this means I'm going to start doing this all the time or anything."
            "She smirks, her tone teasing but her body language revealing her growing excitement."
        else:
            the_person "Yeah, your cock is...okay, I guess. But don't think this means I'm impressed or anything."
            "She shrugs, her movements casual but her body language revealing her growing arousal."

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "You're not the worst, I guess. Keep going and maybe I'll...you know, finish or something. But don't expect me to be all happy about it or anything."
            "She looks up at you, her eyes sparkling with amusement but her body language revealing her growing excitement."
        else:
            the_person "Fine, keep doing what you're doing. It's not like I have anything better to do, I guess."
            "She shrugs, her movements casual but her body language revealing her growing arousal."

    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                the_person "Ugh, I guess I'm close. But don't think this means I'm impressed or anything. Just finish and get it over with already."
                "She looks up at you, her eyes flashing with annoyance but her body language revealing her growing excitement."
            else:
                the_person "Yeah, whatever. You're stretching me out, but it's not like it means anything. Just finish and get it over with already."
                "She rolls her eyes, her tone sarcastic but her body language revealing her growing arousal."
        else:
            the_person "Hmph, I suppose I'm almost there. But don't think I'm enjoying this or anything. Just finish and let's get this over with already."
            "She looks away, her expression neutral but her body language tense."
    return

label tomboy_sex_responses_anal(the_person):
    if the_person.energy < 10:
        call low_energy_sex_responses_anal(the_person) from _vt_tomboy_call_low_energy_sex_responses_anal_10
        return

    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            the_person "Gah, fine. But don't expect me to be all smiles about it, okay?"
            "She huffs and puffs, clearly not thrilled about the situation, and looks away with a scowl."
        else:
            $ the_person.call_dialogue("annoyed_exclaim")
            the_person "Ugh, great. Just what I always wanted: a big, thick cock up my ass. Just peachy."
            "She grumbles to herself, clearly unenthusiastic, and crosses her arms over her chest."

    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            $ the_person.call_dialogue("surprised_exclaim")
            the_person "Whoa, this is... actually kind of nice, I guess."
            "She squirms a bit, trying to get used to the sensation, and looks up at you with a hint of surprise."
        else:
            the_person "Ugh, this is so uncomfortable... can we just get this over with already?"
            "She shifts her hips, trying to get more comfortable, and looks away with a scowl."

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            the_person "Okay, okay. You can keep going, I guess."
            "She grits her teeth, trying to keep up the appearance of being tough, and looks up at you with a hint of challenge."
        else:
            the_person "Gah, why do you have to be so rough?! Can't you just be gentle for once?"
            "She looks up at you with a scowl, her eyes flashing with annoyance."

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            if mc.condom:
                the_person "Just get it over with already... I'm not exactly enjoying this, okay?"
            else:
                the_person "Ugh, you really want to do this raw, huh? You're such a risk-taker, I'll give you that."
        else:
            the_person "Gah, why do you always have to be so insistent?! Can't you just take no for an answer for once?"
            "She looks up at you with a scowl, her eyes flashing with annoyance."

    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                the_person "Fine, I'll cum... but don't think this means I like it or anything, okay?"
                "She looks up at you with a hint of defiance, her eyes sparkling with amusement."
            else:
                the_person "You're just like my [the_person.so_title], always trying to get me to cum... I swear, you two are like two peas in a pod."
                "She sighs, resigned to her fate, and looks away with a scowl."
        else:
            $ the_person.call_dialogue("annoyed_exclaim")
            the_person "Great, just what I needed: another orgasm... just what I always wanted."
            "She mutters to herself, clearly not thrilled about the prospect, and looks away with a scowl."
    return

label tomboy_climax_responses_foreplay(the_person):
    if the_person.sluttiness > 50:
        the_person "Gah, stop teasing me and just make me cum already! I'm not exactly enjoying this waiting game, okay?"
        "She huffs and puffs, clearly on the verge of climax, and looks up at you with a scowl."
    else:
        the_person "Ugh, why do you always have to make this so difficult? Can't you just get me off already?"
        "She shifts her hips, trying to get more comfortable, and looks away with a scowl."
    return

label tomboy_climax_responses_oral(the_person):
    if the_person.sluttiness > 70:
        the_person "Gah, why do you have to be so good at that?! Fine, I'll cum, but don't think this means I'm going to start doing this all the time or anything, okay?"
        "She looks up at you with a hint of annoyance, her eyes flashing with amusement."
    else:
        the_person "You're, like, really good at that... I didn't think I'd... I'm going to cum, I guess."
        "She looks away, her face flushed, and her body language tense."
    return

label tomboy_climax_responses_vaginal(the_person):
    if the_person.sluttiness > 70:
        if the_person.arousal_perc > 120:
            the_person "Fine, I'll cum. But don't think this means I'm enjoying myself or anything, okay? I'm just getting off, that's all."
            "She looks up at you with a scowl, her eyes flashing with annoyance."
        else:
            the_person "Ugh, just a little more... I'm... Ah, fuck! Finally!"
            "She grits her teeth and squeezes her eyes shut, her body language tense."
    else:
        the_person "Oh... I don't know... I'm going to... Ah! Whatever, just get it over with already!"
        "She looks away, her face flushed, and her body language tense."
    return

label tomboy_climax_responses_anal(the_person):
    if the_person.sluttiness > 70:
        if the_person.arousal_perc > 120:
            the_person "Gah, fine. You win. I'll cum. But don't think I'm doing this because I want to or anything, okay?"
            "She looks up at you with a scowl, her eyes flashing with annoyance."
        else:
            the_person "Ugh, just a little more... My ass is going to... Ah, damn it!"
            "She squeezes her eyes shut, trying to fight off the pleasure, and grits her teeth."
    else:
        the_person "Oh... My... Ass... I... Ah, whatever!"
        "She barely finishes her sentence before her body is racked with pleasure, and she looks away with a scowl."
    return

label tomboy_clothing_accept(the_person):
    if the_person.obedience > 180:
        the_person "Whatever, just don't think you're making me into some kind of fashionista or anything, okay? I'm only wearing this because I have to."
        "She shrugs and looks away, her expression neutral."
    else:
        the_person "Yeah, whatever. Just don't expect me to go around looking like a total poser or anything, got it?"
        "She rolls her eyes and looks away, her expression annoyed."
    return

label tomboy_clothing_reject(the_person):
    if the_person.should_wear_uniform:
        the_person "Hey, I guess I should get my uniform sorted out, right? One second. I don't want to get in trouble or anything."
        "She looks away, her expression neutral, and starts to get changed."
    elif the_person.obedience > 180:
        the_person "I don't... I'm sorry, but I really don't think I could get away with wearing something like this. I appreciate the thought, though, I guess."
        "She looks down, her expression embarrassed, and fidgets with her hands."
    else:
        if the_person.sluttiness > 60:
            the_person "Hmm, I don't know about this one. It's a bit too revealing for my taste, I think. I mean, I'm not exactly a prude or anything, but..."
            "She looks away, her expression thoughtful, and shrugs."
        else:
            the_person "You've got to be kidding me, right? This is ridiculous. I'm not wearing this, no way."
            "She looks up at you, her expression annoyed, and crosses her arms over her chest."
    return

label tomboy_clothing_review(the_person):
    if the_person.outfit.cum_covered:
        if (the_person.sluttiness > 40 and the_person.opinion.being_covered_in_cum >=0) or the_person.opinion.being_covered_in_cum > 0:
            the_person "Gah, why do I always get so messy with you...? I guess I'll just have to clean up this mess, huh?"
            "[the_person.title] starts to wipe up the biggest splashes of cum on her, looking annoyed but resigned to her fate."
        else:
            the_person "Ugh, seriously? I need to clean up this mess! Let me know if I've missed any, okay? I don't want to walk around looking like a total slob."
            "[the_person.title] wipes herself down, cleaning up all the cum she can find, and looks up at you with a scowl."

    if the_person.obedience > 180:
        the_person "Fine, I'll be back in a moment. I need to get cleaned up for you, I guess. Don't expect me to be all smiles about it or anything."
        "She shrugs and heads off to clean up, looking neutral but slightly annoyed."
    else:
        if the_person.sluttiness > 40:
            the_person "I don't know why I do this, but I want to look good for you, I guess. I'll be back in a second, I just want to get cleaned up and stuff."
            "She smiles slightly and heads off to clean up, looking a bit more enthusiastic but still slightly annoyed."
        else:
            the_person "Ugh, everything's such a mess after that. Wait here a moment, I'm just going to find a mirror and try and look somewhat presentable, okay? I don't want to look like a total mess in front of you."
            "She rolls her eyes and heads off to clean up, looking annoyed but slightly resigned to her fate."
    $ the_person.apply_planned_outfit(show_dress_sequence = True)
    return

label tomboy_strip_reject(the_person, the_clothing, strip_type = "Full"):
    if the_person.obedience > 180:
        the_person "Hey, could we leave my [the_clothing.display_name] on for now, please? I'm still a little cold, okay? Don't want to freeze my butt off or anything."
        "She looks up at you with a hint of pleading in her eyes, but still looks slightly annoyed."
    elif the_person.obedience < 70:
        the_person "No, no, no, I'll decide what comes off and when, okay? Don't rush me, got it? I'm not some kind of strip tease or anything."
        "She crosses her arms over her chest and looks up at you with a scowl, her eyes flashing with annoyance."
    else:
        the_person "Not yet... I don't know if I'm ready to take off my [the_clothing.display_name]. Maybe we can try something else first, huh? I'm not exactly feeling super confident or anything."
        "She looks away, her expression neutral but slightly hesitant, and fidgets with her hands."
    return

label tomboy_strip_obedience_accept(the_person, the_clothing, strip_type = "Full"):
    "[the_person.title] laughs nervously as you start to slide her [the_clothing.display_name] away, but she doesn't stop you, looking slightly resigned to her fate."
    if the_person.obedience > 180:
        the_person "Alright, fine... I guess I can trust you with this, okay? Just don't expect me to be all smiles about it or anything."
        "She looks up at you with a hint of annoyance, but still looks slightly trusting."
    else:
        the_person "I don't know if this is a good idea, but I'll let you do it this once... just don't think this means I'm going to start doing this all the time or anything, got it?"
        "She looks away, her expression neutral but slightly hesitant, and fidgets with her hands."
    return

label tomboy_grope_body_reject(the_person):
    if the_person.effective_sluttiness("touching_body") < 5: #Fail point for touching shoulder
        the_person "Gah, what's your problem? Personal space, dude!"
        "[the_person.title] steps back as you touch her, then crosses her arms over her chest and gives you a scowl."
        the_person "Just keep your hands to yourself, okay? You're making me super uncomfortable."
        mc.name "Oh, sorry. I didn't mean to make you feel that way."
        the_person "Yeah, well, try to be more careful next time, alright? I don't appreciate the grabby hands."
        "She seems a little put off by the situation, but you both try to move on and put it behind you."
    else: #Fail point for touching waist
        the_person "Hey, could you just... not do that, okay?"
        "[the_person.title] takes your hand and pulls it off of her waist, giving you a warning look and a slight scowl."
        the_person "... Keep your hands to yourself, got it? I'm not some kind of plaything or anything."
        mc.name "Oh yeah, of course. My bad."
        the_person "Just make sure you don't do it again, okay? I don't appreciate the touching without permission."
        "She doesn't say anything else, but you can tell she's still a bit annoyed about the situation and is trying to brush it off."
    return

label tomboy_sex_accept(the_person, the_position):
    if the_person.sluttiness > 70:
        if the_person.obedience < 70:
            the_person "Fine, let's do it. But don't think this means I'm going to put out every time you ask, got it? I'm not some kind of sex machine or anything."
            "She looks up at you with a hint of annoyance, but still seems slightly enthusiastic about the prospect of sex."
        else:
            if the_position.skill_tag == "Foreplay":
                the_person "Oh, I've been wanting you to do that for a while now. Just thinking about it makes me...you know, kinda wet, I guess."
                "She looks away, her face flushing slightly, but still seems slightly enthusiastic about the prospect of foreplay."
            elif the_position.skill_tag == "Oral":
                if "getting head" in the_position.opinion_tags:
                    the_person "Ugh, I'm so down for that right now. Just get down there and suck my [pussy/clit] already, okay?"
                    "She looks up at you with a hint of impatience, but still seems slightly enthusiastic about the prospect of oral sex."
                else:
                    the_person "You're going down on me right now, and you're going to make me cum, got it? I'm not leaving until that happens."
                    "She looks up at you with a hint of determination, and seems slightly enthusiastic about the prospect of oral sex."
            else:
                the_person "Get over here and fuck me already. I've been waiting for this, and I'm not leaving until it happens, okay?"
                "She looks up at you with a hint of impatience, but still seems slightly enthusiastic about the prospect of sex."
    else:
        the_person "Come here, let's do it. But don't think I'm going to do this all the time, got it? I'm not some kind of sex addict or anything."
        "She looks up at you with a hint of annoyance, but still seems slightly enthusiastic about the prospect of sex."
    return

label tomboy_sex_obedience_accept(the_person):
    if the_person.sluttiness > 70:
        the_person "Gah, fine. I don't want to admit it, but you've gotten to me, I guess. Do whatever you want to me, [the_person.mc_title], but don't expect me to be all smiles about it, okay?"
        "She looks away, her face flushing slightly, and shrugs."
    else:
        if the_person.obedience > 180:
            the_person "Alright, I'll do what you say, but don't think this means I'm going to like it or anything, got it? I'm only doing this because I have to."
            "She looks up at you with a hint of annoyance, but still seems slightly resigned to her fate."
        else:
            the_person "I shouldn't be saying this, but if you really want to... I'll give it a try, I guess. Just this once, okay? Don't expect me to make a habit of it or anything."
            "She looks away, her face flushing slightly, and fidgets with her hands."
    return

label tomboy_sex_gentle_reject(the_person):
    if the_person.sluttiness > 50:
        the_person "Ugh, not like that, [the_person.mc_title]. I need a little more... you know, foreplay first, okay? Don't just rush into it like a caveman or anything."
        "She rolls her eyes and looks away, her expression annoyed but slightly amused."
    else:
        the_person "No, no, no. I want to have fun, but I don't want to get too serious, okay? Let's just keep it light and casual, like a hookup or something."
        "She shrugs and looks away, her expression neutral but slightly hesitant."
    return

label tomboy_sex_angry_reject(the_person):
    if the_person.has_significant_other:
        the_person "What? Are you out of your mind? I have a [the_person.so_title], so you can forget about doing anything like that, ever. I'm not some kind of cheat or anything."
        "She glares at you and turns away, clearly offended and slightly hurt."
    elif the_person.sluttiness < 20:
        the_person "Are you serious? You've got to be kidding me! Get away from me, I never want to see you like this again, you creep!"
        "[the_person.title] glares at you and takes a step back, her face red with anger and her eyes flashing with annoyance."
    else:
        the_person "What? Are you out of your mind? You can't be serious! Get away from me, I'm not interested in anything like that, okay? I'm not some kind of sex object or anything."
        "[the_person.title] glares at you and steps back, her face showing clear disapproval and her eyes flashing with annoyance."
    return

label tomboy_seduction_response(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 50:
            the_person "Gah, I think I know what you need right now, okay? Let me take care of you, but don't expect me to be all smiles about it."
            "She looks away, her face flushing slightly, and shrugs."
        else:
            the_person "Okay, I'll give you a few minutes, I guess. But don't think this means I'm going to be your slave or anything, got it?"
            "She looks up at you with a hint of annoyance, but still seems slightly resigned to her fate."
    else:
        if the_person.sluttiness > 50:
            the_person "Mmm, you're feeling as horny as me then? Come on, let's go find a place to get out of sight, okay?"
            "[the_person.title] takes your hand and leads you off to find some place private, looking slightly excited but still trying to play it cool."
        elif the_person.sluttiness > 10:
            the_person "I know that look you're giving me, I think I know what you want, okay? But don't expect me to give it up that easily, got it?"
            "She looks up at you with a hint of challenge, her eyes sparkling with amusement."
        else:
            the_person "[mc.name], I know what you mean... Okay, I can spare a few minutes, I guess. But don't get your hopes up or anything, okay?"
            "She looks away, her face flushing slightly, and shrugs."
    return

label tomboy_seduction_accept_crowded(the_person):
    if not the_person.has_significant_other:
        if the_person.sluttiness < 20:
            the_person "Alright, let's sneak away for a few minutes and you can, like, convince me a little more or something, okay?"
            "She looks around nervously, making sure no one is watching, and then nods."
        elif the_person.sluttiness < 50:
            the_person "Come on, I know someplace nearby where we can get a few minutes privacy, okay? Just make it quick, I don't want to get caught or anything."
            "She looks around, making sure no one is watching, and then takes your hand and leads you off."
        else:
            the_person "Oh, I don't know if I can wait much longer, [the_person.mc_title]... Let's just find a place to get out of sight, okay?"
            "She looks up at you with a hint of desperation, her eyes sparkling with amusement."
    else:
        if the_person.sluttiness + (5*the_person.opinion.cheating_on_men) > 50:
            the_person "Fuck it, let's do this! I don't care about my [the_person.so_title] right now, okay?"
            "She looks up at you with a hint of defiance, her eyes sparkling with amusement."
        else:
            the_person "Ugh, you're bad for me, [the_person.mc_title]... Come on, we need to find somewhere quiet so my [the_person.so_title] doesn't catch us, okay?"
            "She looks around nervously, making sure no one is watching, and then nods."
    return

label tomboy_seduction_accept_alone(the_person):
    if not the_person.has_significant_other:
        if the_person.sluttiness < 20:
            the_person "Alright, you've got one chance to impress me, okay? Don't blow it or anything."
            "She looks up at you with a hint of challenge, her eyes sparkling with amusement."
        elif the_person.sluttiness < 50:
            the_person "Come on, let's get this over with and see if you're any good, okay? I'm not exactly expecting much or anything."
            "She shrugs and looks away, her expression neutral but slightly hesitant."
        else:
            the_person "Fuck, I'm so turned on right now, [the_person.mc_title]. Just do me already, okay?"
            "She looks up at you with a hint of desperation, her eyes sparkling with amusement."
    else:
        if the_person.sluttiness + (5*the_person.opinion.cheating_on_men) > 50:
            the_person "You know I shouldn't be doing this with you, but fuck it, okay? Let's do this!"
            "She looks up at you with a hint of defiance, her eyes sparkling with amusement."
        else:
            the_person "You're trouble, [the_person.mc_title], but I guess I just can't help myself, okay? Come here."
            "She looks up at you with a hint of resignation, her eyes sparkling with amusement."
    return

label tomboy_seduction_refuse(the_person):
    if the_person.sluttiness < 20:
        the_person "Gah, why are you always trying to flirt with me, [mc.name]? I'm just not in the mood for this right now, okay? Can't you see I'm busy or something?"
        "[the_person.title] folds her arms and looks away, her expression annoyed but slightly amused."
    elif the_person.sluttiness < 50:
        the_person "Fine, I'll admit you're kind of cute, but don't think this means I'm actually interested or anything, okay? Maybe some other time, when I'm in a better mood and not so... distracted."
        "[the_person.title] playfully pokes [mc.name]'s chest with her finger, her expression teasing but slightly guarded."
    else:
        the_person "Eh, you're always trying to get me into bed, [mc.name], but I'm not going to make it easy for you, okay? You'll have to wait until I'm good and ready to fool around... which might be never, who knows?"
        "[the_person.title] grins mischievously and walks away, leaving [mc.name] to wonder what she's thinking, and looking slightly pleased with herself."
    return

label tomboy_compliment_response(the_person):
    mc.name "Hey [the_person.fname], you look really beautiful today. Is there a special occasion or something?"
    if the_person.is_at_work:
        if (the_person.is_employee or the_person.is_strip_club_employee) and the_person.is_wearing_uniform:
            call tomboy_flirt_response_employee_uniform_low(the_person) from _call_tomboy_flirt_response_employee_uniform_low_compliment_response
        elif the_person.is_at_job(prostitute_job):
            the_person "Ugh, why do you always want to hang out with me? Can't you see I'm busy trying to make a living or something?"
            "She rolls her eyes and looks away, her expression annoyed but slightly amused."
        elif the_person.sluttiness > 50:
            the_person "I'm doing great, thanks for asking. But don't think this means I'm actually interested in you or anything, okay? I'm just trying to make a good impression."
            "She smirks and looks away, her expression teasing but slightly guarded."
        else:
            the_person "Oh, stop it, you're making me blush. There's no special occasion, I just felt like dressing up today, okay?"
            "She looks away, her face flushing slightly, and smiles slightly."
    else:
        the_person "Well, I did put in a bit of extra effort today, I guess. You're just the first one to notice, so thanks for that, I suppose."
        "She shrugs and looks away, her expression neutral but slightly pleased with herself."
    "You try to press for more information, but [the_person.possessive_title] just smiles coyly and changes the subject, leaving you wondering what's going on and looking slightly amused."
    return

label tomboy_compliment_response_girlfriend(the_person):
    mc.name "Hey [the_person.title]. You're looking very nice this [StringInfo.time_of_day_string]."
    if the_person.is_at_work:
        if (the_person.is_employee or the_person.is_strip_club_employee) and the_person.is_wearing_uniform:
            call tomboy_flirt_response_employee_uniform_mid(the_person) from _call_tomboy_flirt_response_employee_uniform_mid_compliment_response_girlfriend
            $ the_person.call_dialogue("flirt_response_employee_uniform_mid")
        elif the_person.sluttiness > 50:
            the_person "Gah, thanks, [the_person.mc_title]. You're not so bad yourself, I guess. Want to find out how nice I am... in private, maybe?"
            "She winks at you, her expression playful but slightly teasing."
        else:
            the_person "Hmph, really? Thanks, [the_person.mc_title]. You're not so bad yourself, I suppose."
            "She looks away, her face flushing slightly, and smiles slightly."
    else:
        the_person "Ugh, don't be ridiculous. It's just a normal day... but thanks, I guess."
        mc.name "Oh come on, don't be like that. You know you look great."
        the_person "Aww, stop it, [the_person.mc_title]. You're making me blush... and annoyed at the same time. Just stop, okay?"
        "She rolls her eyes and looks away, her expression annoyed but slightly amused."
    "You chat with [the_person.possessive_title] for a while, and although she's initially annoyed by your compliments, she starts to warm up to you and seems slightly more receptive to your advances."
    return

label tomboy_compliment_response_affair(the_person):
    mc.name "Hey [the_person.title]. You're looking absolutely amazing this [StringInfo.time_of_day_string]."
    if the_person.is_at_work:
        if (the_person.is_employee or the_person.is_strip_club_employee) and the_person.is_wearing_uniform:
            call tomboy_flirt_response_employee_uniform_mid(the_person) from _call_tomboy_flirt_response_employee_uniform_mid_compliment_response_affair
        elif the_person.sluttiness > 50:
            the_person "Mmmm, thank you [the_person.mc_title], wanna go somewhere a little more... private, maybe? So you can make me feel how amazing I am, in person?"
            "She winks at you, her expression playful but slightly teasing, and leans in close."
        else:
            the_person "Hmph, really? Thanks, [the_person.mc_title]. You're not so bad yourself, I suppose."
            "She looks away, her face flushing slightly, and smiles slightly."
    else:
        the_person "Ugh, don't be silly. It's just a normal day... but thanks, I suppose."
        mc.name "Oh come on, don't be like that. You know you look great."
        the_person "Aww, stop it, [the_person.mc_title]. You're making me blush... and a little annoyed, okay? Just stop, already."
        "She rolls her eyes and looks away, her expression annoyed but slightly amused, and seems slightly more receptive to your advances."
    "You keep chatting with [the_person.possessive_title] for a while, slipping in a few more compliments and trying to charm her with your words. She seems quite charmed by your attentiveness and starts to open up to you."
    return

label tomboy_flirt_response(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 50:
            the_person "Gah, fine. You're not totally terrible, [the_person.mc_title], I guess."
            "She looks away, her face flushing slightly, and shrugs."
        else:
            the_person "Whatever. Thanks for the compliment, [the_person.mc_title]. You're not a complete loser, I suppose."
            "She rolls her eyes and looks away, her expression annoyed but slightly amused."

    elif the_person.has_significant_other:
        if the_person.sluttiness + (the_person.opinion.cheating_on_men*5) > 50:
            the_person "Oh, you think you're so clever, don't you? I'll give you that, I guess."
            "[the_person.title] gives you a sly look, her eyes narrowing and her expression teasing."
        else:
            the_person "You're really pushing your luck, [the_person.mc_title]. I have a [the_person.so_title] you know, and I'm not exactly looking for a replacement or anything."
            mc.name "What about you, do you appreciate it?"
            "She rolls her eyes and crosses her arms, looking annoyed but slightly amused."
            the_person "Maybe I do, maybe I don't. It's none of your business, okay? Just drop it."

    else:
        if the_person.sluttiness > 50:
            the_person "Fine. Maybe you're worth my time, [the_person.mc_title], I guess."
            "[the_person.title] gives you a half-smile, but her eyes remain guarded and her expression teasing."
        else:
            the_person "Whatever. You're not unattractive, I suppose. But don't think that means I'll go easy on you or anything, got it?"
            the_person "You'll have to really impress me though, I have high standards and I'm not exactly looking for anyone to sweep me off my feet or anything."
            "She looks away, her face flushing slightly, and shrugs."
    return

label tomboy_flirt_response_employee_uniform_low(the_person):
    if the_person.is_wearing_forced_uniform:
        the_person "Gah, I suppose you like seeing me in this uniform... I mean, I'm practically naked, okay?"
        mc.name "I know you don't like it, but I needed to make a point."
        the_person "I know, I know. You always were one to make a point, even if it's a stupid one."
        mc.name ".... HEY!"
        $ mc.change_locked_clarity(5)
        "She crosses her arms over her chest, looking annoyed but slightly amused, and can't hide the small smile on her face."
    elif the_person.judge_outfit(the_person.outfit):
        #She's in uniform and likes how it looks.
        the_person "Oh, you noticed? I thought it was a bit much, but I guess it's not so bad, okay?"
        the_person "I mean, it's nice to work somewhere where I can show off a little, even if it's not exactly my style."
        $ mc.change_locked_clarity(5)
        "She winks at you, then turns to adjust her uniform, accentuating her hips and looking slightly playful."
    else:
        #She's in uniform, but she thinks it's a little too slutty.
        if the_person.vagina_visible:
            # Her pussy is on display.
            the_person "Gah, I suppose you like seeing me like this... I mean, I'm practically naked, okay?"
            mc.name "Well, you know that it's..."
            the_person "I know, I know. It's company policy. But don't think you're the only one who's annoyed by it, got it?"
            mc.name "Give it some time and you'll get used to it."
            $ mc.change_locked_clarity(5)
            "She rolls her eyes, looking annoyed but slightly amused, and doesn't argue."

        elif the_person.tits_visible:
            # Her tits are out
            the_person "Ugh, I'm still getting used to being so... exposed in this uniform. At least I don't have to wear a bra, I guess."
            mc.name "You look incredible and you're comfortable. I call that a success."
            $ mc.change_locked_clarity(5)
            "She huffs, looking annoyed but slightly amused, but can't hide her smile."
            the_person "Yeah, yeah. You're just trying to make me feel better, okay?"

        elif the_person.underwear_visible:
            # Her underwear is visible.
            the_person "Hmph, I probably would have picked something that kept me a little more covered, but at least our uniform is comfortable, I guess."
            mc.name "It may be a little unconventional, but you look fantastic. You've got exactly the right kind of body for it."
            the_person "Well, that's one way to look at it, I suppose. But don't think I'm going to start wearing this all the time or anything."
            $ mc.change_locked_clarity(5)
            "She playfully rolls her eyes and turns to adjust her uniform, showing off her body and looking slightly playful."
        else:
            # It's just generally slutty.
            the_person "Ugh, well thank you, I guess. Our uniforms are a little bold for my taste, but I suppose I look good in it, okay?"
            $ mc.change_locked_clarity(5)
            "She blushes and looks away, looking slightly embarrassed but also slightly amused, and you catch a glimpse of her small smile."
    return

label tomboy_flirt_response_employee_uniform_mid(the_person):
    if the_person.is_wearing_forced_uniform:
        $ mc.change_locked_clarity(10)
        if the_person.vagina_visible:
            the_person "Gah, fine. You caught me off guard, okay? I'll admit, this uniform does make me look good, especially down here... but don't think this means I'm comfortable with it or anything."
            mc.name "It's a great uniform, but that's not what's important here."
            the_person "Yeah, yeah. You're right. It's just hard not to feel like a sex object in this thing, especially with my pussy on display. It's kinda degrading, if you ask me."
        elif the_person.tits_visible:
            the_person "Gah, fine. You caught me off guard, okay? I'll admit, this uniform does make me look good, especially up here... but don't think this means I'm comfortable with it or anything."
            mc.name "It's a great uniform, but that's not what's important here."
            the_person "Yeah, yeah. You're right. It's just hard not to feel like a sex object in this thing, especially with my boobs popping out. It's kinda annoying, if you ask me."
        else:
            the_person "Gah, fine. You caught me off guard, okay? I'll admit, this uniform does make me look good... but don't think this means I'm comfortable with it or anything."
            mc.name "It's a great uniform, but that's not what's important here."
            the_person "Yeah, yeah. You're right. It's just hard not to feel like a sex object in this thing. It's kinda frustrating, if you ask me."
        mc.name "Rules are rules and I can't make any exceptions, even if they look good."
        "She sighs and nods, looking slightly annoyed but also slightly amused."
        the_person "Yeah, I know. At least you're having a good time, I suppose. I don't mind that so much, I guess."
    elif the_person.judge_outfit(the_person.outfit):
        $ mc.change_locked_clarity(10)
        if the_person.tits_visible:
            the_person "Hmph, maybe I should wear this outfit more often, okay? It's getting a lot of attention, especially for my boobs... but don't think this means I'm going to start dressing like this all the time or anything."
            mc.name "It's a great outfit, but I'm more interested in the person wearing it."
            the_person "Oh, really? Is that so? I guess my boobs are hard to ignore, huh?"
        else:
            the_person "Hmph, maybe I should wear this outfit more often, okay? It's getting a lot of attention... but don't think this means I'm going to start dressing like this all the time or anything."
            mc.name "It's a great outfit, but I'm more interested in the person wearing it."
            the_person "Oh, really? Is that so? I guess my vagina is hard to ignore, huh?"
        the_person "Maybe I'll invite you shopping one day and you can tell me what else you want to see me in, okay? But don't expect me to take your fashion advice too seriously or anything."
        mc.name "Sounds like a good time, I suppose."

    else:
        # the_person "I think it shows off a little too much!"
        the_person "Ugh, fine. You're not gonna make this easy for me, are you, okay?"
        $ mc.change_locked_clarity(10)
        if the_person.vagina_visible:
            the_person "I'm trying to focus on my work here, not flirt with you all day, okay? And definitely not with my pussy on display. It's kinda distracting, if you ask me."
        elif the_person.tits_visible:
            the_person "I'm trying to focus on my work here, not flirt with you all day, okay? And definitely not with my boobs popping out. It's kinda annoying, if you ask me."
        else:
            the_person "I'm trying to focus on my work here, not flirt with you all day, okay? It's kinda frustrating, if you ask me."
        mc.name "I understand, but I promise it's important for the business."
        "She sighs and nods, looking slightly annoyed but also slightly amused."
        the_person "Yeah, I know. You're a real pain, you know that, okay? But I guess I can deal with it."
    return

label tomboy_flirt_response_low(the_person):
    #She's in her own outfit.
    the_person "Gah, I suppose it's not the worst outfit I've ever worn, okay?"
    $ the_person.draw_person(position = "walking_away")
    $ mc.change_locked_clarity(5)
    "She rolls her eyes and gives you a quick spin, showing off her outfit from every angle, and looks slightly annoyed but also slightly amused."
    the_person "I mean, I guess it's not too bad, right? But don't expect me to start dressing like this all the time or anything."
    $ the_person.draw_person()
    mc.name "I think it looks great on you."
    the_person "Oh, shut up. You're just saying that to be nice, okay? Don't try to butter me up or anything."
    return

label tomboy_flirt_response_low1(the_person):
    if the_person.has_significant_other:
        the_person "Ugh, what's with you and the flirting? I've got a [the_person.so_title], and I don't think he'd appreciate you getting all up in my grill, okay?"
        mc.name "What about you, do you appreciate it?"
        "She rolls her eyes and smirks, looking slightly annoyed but also slightly amused."
        the_person "Maybe I do... but don't think you're getting anywhere with me that easily, got it? I'm not some kind of easy target or anything."
    else:
        the_person "Well, thanks for the compliment, I guess. But don't think you're getting off that easy, okay? I have high standards, and you'll need to prove yourself to me if you want to get anywhere."
        the_person "But if you can impress me, who knows what might happen... maybe I'll even consider going out with you or something."
    $ mc.change_locked_clarity(5)
    return

label tomboy_flirt_response_mid(the_person):
    if mc.location.person_count > 1 and the_person.effective_sluttiness("kissing") < (25 - (5*the_person.opinion.public_sex)):
        $ mc.change_locked_clarity(10)
        the_person "Gah, I was wondering if you actually noticed my outfit today... or if you're just being oblivious as usual."
        "Her eyes narrow slightly, but she's still trying to appear casual and slightly annoyed."
        mc.name "I noticed. It looks great on you."
        the_person "Oh, really? Thanks, I guess. I was thinking you might say something like that, but I didn't expect you to be so... obvious."
        "She crosses her arms, trying to maintain a tough exterior and looking slightly annoyed but also slightly amused."
        if the_person.tits_visible:
            mc.name "I noticed. It looks great on you. Especially your boobs."
            the_person "Oh, really? Thanks, I guess. I was thinking you might say something like that, but don't think this means I'm going to start showing them off all the time or anything."
            "She crosses her arms, trying to maintain a tough exterior and looking slightly annoyed but also slightly amused."
        else:
            mc.name "Well, it's true. You look amazing."
        the_person "Hmph. Maybe I'll invite you shopping one day, so you can tell me what else you want to see me in... but don't expect me to take your fashion advice too seriously or anything."
        "She leans in slightly, a hint of flirtation in her voice and a slightly playful tone."
        mc.name "I can think of a few things already... and I'm sure I'd enjoy seeing you in them."
        the_person "I'm sure you would. So, what do you say? Want to take me out for a drink and maybe we can discuss my wardrobe some more... or maybe just get to know each other a little better?"
    else:
        the_person "Thanks, I thought I looked pretty hot in it too... but don't think this means I'm going to start dressing like this all the time or anything."
        the_person "You want a better look, right? Here, how does it make my ass look?"
        $ the_person.draw_person(position = "back_peek")
        $ mc.change_locked_clarity(10)
        the_person "Good, right? I mean, I'm not exactly a fashion expert or anything, but I think I look pretty good."
        mc.name "Fantastic. I wish I could get an even better look at it."
        "[the_person.possessive_title!c] smiles and turns back to face you, looking slightly playful and flirtatious."
        $ the_person.draw_person()
        the_person "I'm sure you do. Take me out for a drink and maybe we can work something out... or maybe just have a good time, okay?"
    return

label tomboy_flirt_response_mid1(the_person):
    $ mc.change_locked_clarity(10)
    the_person "Gah, thanks, I guess. I do look pretty amazing in this outfit, if I do say so myself."
    if (the_person.has_skirt or the_person.has_dress) and not the_person.has_thigh_high_socks:
        mc.name "You could change it up with some high stockings, I would like to see that."
        the_person "Oh, really? And why would you want to see that, huh? You're not going to get a peek or anything, are you? Don't think I'm going to start dressing up just for you or anything."
        mc.name "Because it would look great on you, and I would enjoy the view, okay? Don't be so paranoid."

    mc.name "How about you and me go and grab a coffee sometime?"
    if the_person.has_significant_other:
        the_person "Sure, my [the_person.so_title] doesn't mind... as long as they're not around to witness how much fun we're going to have, I guess. But don't think this means I'm going to start cheating on them or anything, got it?"
    else:
        the_person "Why not, I could use a pick-me-up once in a while... and maybe someone to pick me up from the ground when I fall for you, I suppose. But don't think this means I'm going to start getting all mushy or anything, okay?"
    the_person "Just let me know when, I would love to... and don't think I won't notice if you're trying to get a glimpse of my legs under the table, got it? I'm not exactly oblivious or anything."
    mc.name "I'll keep that in mind, and maybe we can discuss what else you want to wear in the future... or not wear."
    the_person "Hmph, maybe. But don't think you're getting a discount on my wardrobe just because we're going out for coffee... or anything else, okay? I'm not exactly a charity case or anything."
    return

label tomboy_flirt_response_high(the_person):
    if mc.location.person_count > 1 and the_person.effective_sluttiness() < (25 - (5*the_person.opinion.public_sex)): # There are other people here, if she's not slutty she asks if you want to find somewhere quiet
        the_person "Gah, you're really persistent, huh? Fine, but not here... let's find somewhere a little more private, okay?"
        "She glances around before giving you a sly smile and a slightly annoyed look."
        menu:
            "Find somewhere more quiet\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                mc.name "Then let's find somewhere that isn't here."
                the_person "Hmph, eager much? Alright, let's go. But don't think this means I'm going to start making out with you in public or anything."
                call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_tomboy_flirt_response_high_2
                the_person "So... Now what's your plan, huh?"

                if the_person.is_willing(kissing):
                    $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
                    if the_person.has_taboo("kissing"):
                        "You lean in close to kiss [the_person.title]."
                        $ the_person.call_dialogue("kissing_taboo_break")
                        $ the_person.break_taboo("kissing")
                        "She responds passionately, her arms wrapping around your neck and her eyes closing."
                    else:
                        "You step close to [the_person.title] and put your arm around her waist, pulling her close and kissing her."
                        "She responds immediately and eagerly presses her body against yours, her eyes closing."
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _vt_tomboy_call_fuck_person_49
                else:
                    if the_person.has_taboo("touching_body"):
                        $ the_person.call_dialogue("touching_body_taboo_break")
                        $ the_person.break_taboo("touching_body")
                        "You take her hand and pull her close against you. She looks into your eyes, her expression slightly hesitant."
                    else:
                        "You take her hand and pull her close, your lips brushing against her ear and your voice whispering sweet nothings."
                    call fuck_person(the_person, private = True, start_position = standing_grope, skip_intro = True) from _call_fuck_person_tomboy_flirt_grope

                $ the_person.call_dialogue("sex_review", the_report = _return)
                call mc_restore_original_location(the_person) from _call_mc_restore_original_location_tomboy_flirt_response_high_2

    else:
        if mc.location.person_count == 1: #You're alone, so she just didn't meet the sluttiness threshold
            the_person "Gah, you're really eager, aren't you? Well, I suppose it's just the two of us here... so what's your plan, huh?"
            "[the_person.possessive_title!c] glances around, confirming you're alone and looking slightly annoyed but also slightly amused."
            the_person "So, what's it going to be? Are you going to make a move or just stand there like a total dweeb?"

        else:  # You aren't alone but she's still into it.
            the_person "Feeling bold today, huh? Well, I think your chances are pretty good... but don't think this means I'm going to start making out with you in public or anything, got it?"
            "[the_person.title] smirks, clearly enjoying the attention and looking slightly playful."
            if the_person.has_large_tits: #Bounces her tits for you
                $ mc.change_locked_clarity(15)
                "[the_person.title] grabs her tits and jiggles them for you, looking slightly mischievous and playful."
                the_person "Maybe I can get these girls out for you. Does that sound nice, huh?"

            else: #No big tits, so she can't bounce them (as much)
                "[the_person.title] runs her hands over her hips sensually, obviously encouraging you to take things further and looking slightly seductive."

        menu:
            "Touch her" if not the_person.is_willing(kissing):
                "You step closer to [the_person.title] and move your hands down her waist, looking slightly hesitant but also slightly eager."
                if the_person.has_taboo("touching_body"):
                    the_person "Oh, you're brave. I like that, I guess."
                    $ the_person.call_dialogue("touching_body_taboo_break")
                    $ the_person.break_taboo("touching_body")

                call fuck_person(the_person, start_position = standing_grope, private = False) from _call_fuck_person_flirt_response_tomboy_touching

            "Kiss her" if the_person.is_willing(kissing):
                $ the_person.draw_person()
                if the_person.has_taboo("kissing"):
                    "You put your arm around [the_person.possessive_title] and lean in close, looking slightly hesitant but also slightly eager."
                    $ the_person.call_dialogue("kissing_taboo_break")
                    $ the_person.break_taboo("kissing")
                    "She responds with a passionate kiss, her arms wrapping around your neck and her eyes closing."
                else:
                    "You pull [the_person.possessive_title!] close and kiss her, looking slightly eager and slightly playful."
                    "She responds with a passionate kiss, her arms wrapping around your neck and her eyes closing."

                call mc_move_to_private_location(the_person) from  _call_mc_move_to_private_location_tomboy_flirt_response_high
                call fuck_person(the_person, start_position = kissing, private = _return, skip_intro = True) from _vt_tomboy_call_fuck_person_50
                $ the_person.call_dialogue("sex_review", the_report = _return)
                call mc_restore_original_location(the_person) from _call_mc_restore_original_location_tomboy_flirt_response_high

            "Just flirt":
                $ the_person.draw_person()
                mc.name "Very tempting, but you're going to have to contain yourself for now, okay?"
                the_person "Oh, you're not going to take advantage of me right now, are you? Fine, be that way, I guess."
                "[the_person.title] pouts, clearly enjoying the flirtation and looking slightly playful."
    return

label tomboy_flirt_response_low_energy(the_person):
    if the_person.sluttiness > 40:
        the_person "Gah, thanks for the compliment, I guess... but I'm totally exhausted right now, okay? Can't this wait or something?"
        "She looks away, her eyes half-closed and her expression slightly annoyed."
    else:
        the_person "Thanks, but I'm totally beat, okay? Can we pick this up later or something? I'm not exactly feeling my best right now."
        "She shrugs and looks away, her expression neutral but slightly hesitant."
    return

label tomboy_flirt_response_girlfriend(the_person):
    # Lead in: mc.name "You're so beautiful [the_person.title], I'm so lucky to have a woman like you in my life."
    if mc.location.person_count > 1:
        # There are other people around, so she'll only start making out with you if she's slutty.
        if the_person.effective_sluttiness("kissing") < (25 - (5*the_person.opinion.public_sex)):
            # Not very slutty, so she wants to find somewhere private
            the_person "Gah, you're so cheesy, okay? But I guess I like it a little bit."
            "She pulls you against her and kisses you, her lips soft and gentle, but also slightly hesitant."
            the_person "There, now you can't say I don't know how to kiss, okay?"
            mc.name "Haha, yeah I guess not..."
            "You put your arms around her and kiss her back, feeling her warmth and her slightly guarded expression."
            the_person "Mmm, yeah, like that... but let's not do this here, okay?"
            menu:
                "Find somewhere more quiet\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                    mc.name "Why wait? Come on, I'm sure we can find somewhere quiet, okay?"
                    the_person "You're always so eager, aren't you? Alright, let's go, but don't think this means I'm going to start making out with you in public or anything."
                    "You and [the_person.possessive_title] hurry off, searching for a private spot and looking slightly annoyed but also slightly amused."
                    call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_tomboy_flirt_response_girlfriend_2
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _vt_tomboy_call_fuck_person_76
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_tomboy_flirt_response_girlfriend_2

                "Just flirt":
                    $ mc.change_locked_clarity(10)
                    "You reach around and pull her closer, running your hand down her back and looking slightly playful."
                    mc.name "You're so beautiful, and you know it, okay?"
                    "She rolls her eyes but leans in for a quick kiss, looking slightly annoyed but also slightly amused."
                    the_person "Fine, you caught me. But don't think this means I'm going easy on you or anything, got it?"

        else:
            the_person "Well if I'm so beautiful, then why are you just standing there, huh? Come on, kiss me already!"
            "You put your arm around her waist and pull her close, kissing her deeply and passionately."
            "When you break the kiss, [the_person.possessive_title] sighs and leans against you, looking slightly pleased but also slightly annoyed."
            the_person "You're not so bad yourself, I guess... but don't think this means I'm going to start making out with you all the time or anything."
            menu:
                "Make out":
                    "You lean back in and kiss her again, this time more passionately and looking slightly eager."
                    "[the_person.title] responds eagerly, wrapping her arms around your neck and looking slightly pleased but also slightly annoyed."

                    call mc_move_to_private_location(the_person) from  _call_mc_move_to_private_location_tomboy_flirt_response_girlfriend
                    call fuck_person(the_person, start_position = kissing, private = _return, skip_intro = True) from _vt_tomboy_call_fuck_person_77
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_tomboy_flirt_response_girlfriend

                "Just flirt":
                    mc.name "I'm not bad? You're the one who's hard to resist, okay?"
                    $ mc.change_locked_clarity(10)
                    "You reach out and touch her cheek, a playful grin on your face and a slightly teasing tone."
                    the_person "Ugh, you're so annoying, okay? But I guess I like that about you... a little bit, maybe."

    else:
        # You're alone, so she's open to fooling around.
        the_person "Well you've got me all alone, so how about you show me just how lucky you feel, huh?"
        "She reaches down to your waist and cups your crotch, rubbing it gently and looking slightly playful but also slightly annoyed."
        mc.name "You're so wet for me already, okay?"
        the_person "Hmph, maybe... but don't think this means I'm going to start throwing myself at you or anything, got it?"
        "She grinds against you, her hips moving in a slow circle and her expression slightly pleased but also slightly annoyed."
        mc.name "Damn, you feel so good, okay?"
        "You reach up and grab her breasts, squeezing them gently and looking slightly eager."
        the_person "Ooh, don't do that, okay? But also, don't stop, maybe..."
        "But she doesn't pull away, her body still pressed against yours and her expression slightly pleased but also slightly annoyed."
        menu:
            "Kiss her":
                if the_person.has_taboo("kissing"):
                    $ the_person.call_dialogue("kissing_taboo_break")
                    $ the_person.break_taboo("kissing")

                "You put your arms around [the_person.possessive_title]'s waist and rest your hands on her ass, pulling her close and kissing her sensually."
                "She responds by pressing her body against you and grinding her hips against your thigh, looking slightly pleased but also slightly annoyed."
                "You grab her hips and pull her closer, your crotches pressed together and your bodies entwined."
                call fuck_person(the_person, start_position = kissing, skip_intro = True) from _vt_tomboy_call_fuck_person_78
                $ the_person.call_dialogue("sex_review", the_report = _return)
                $ the_person.review_outfit()

            "Just flirt":
                mc.name "I'm going to make you beg for it, okay?"
                "You lean in close, your breath hot against her ear and your voice low and husky."
                the_person "Ooh, you're such a bad boy, okay? I love it, maybe... but also, don't think this means I'm going to start begging for it or anything, got it?"
                "She rubs her body against yours, her hips moving seductively and her expression slightly pleased but also slightly annoyed."
                the_person "But don't think you're getting off that easy, okay? I'm going to make you work for it... maybe."
    return
### DIALOGUE ###

label tomboy_flirt_response_affair(the_person):
    # Lead in: mc.name "You look so good today [the_person.title], you're making me want to do some very naughty things to you."
    if mc.location.person_count > 1: #There are other people around, she's nervous about people finding out what you're doing.
        if (the_person.opinion.cheating_on_men *15) + the_person.effective_sluttiness() > 50: #SHe's turned on by flirting in public or doesn't think anything is wrong with it
            "[the_person.possessive_title!c] blushes and playfully bats her eyes at you, looking slightly annoyed but also slightly amused."
            the_person "Gah, you're making me blush, okay? I'm not used to this kind of attention from you, especially not in public."
            the_person "But I have to admit, I'm curious. What do you have in mind, huh?"
            menu:
                "Find somewhere more quiet\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                    mc.name "I was thinking we could slip away and find a more private spot, okay?"
                    "You and [the_person.title] exchange a flirtatious glance before hurrying off to find a quiet spot, looking slightly eager and slightly playful."
                    call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_tomboy_flirt_response_affair
                    $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
                    "As soon as you're alone she pulls you into a deep and passionate kiss, her lips soft and gentle but also slightly hesitant."
                    $ the_person.draw_person(position = "kissing")
                    the_person "Mmm... I've been wanting to do that for a while now, okay?"
                    "You wrap your arms around her waist and kiss her back, feeling her warmth and her slightly guarded expression."
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _vt_tomboy_call_fuck_person_79
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_tomboy_flirt_response_affair

                "Just flirt":
                    mc.name "I can't help but notice how beautiful you look today, [the_person.title], okay?"
                    the_person "Stop it, you're making me blush! But I have to admit, you look pretty great yourself, I guess."
                    the_person "Just don't get too cocky, okay? I'm still in charge here, and don't you forget it."
                    $ mc.change_locked_clarity(20)
                    "[the_person.possessive_title!c] playfully swats at your arm before leaning in close, looking slightly playful and slightly flirtatious."
                    the_person "But I have to admit, I'm getting a little turned on by this whole thing, okay? Maybe we should take this somewhere else..."
                    "You can't help but feel a little flustered as she teases you, but also slightly excited and eager."

        else: #She's shy or nervous about being discovered
            "[the_person.possessive_title!c] looks around nervously, then back at you with a sheepish grin, looking slightly annoyed but also slightly amused."
            the_person "Oh, um, you look nice today, I guess. I should probably get going though... before things get too complicated or anything."
            mc.name "Wait, don't go! I was thinking we could... uh, grab a drink or something, okay?"
            $ mc.change_locked_clarity(15)
            the_person "Oh, you want to grab a drink? Okay, sure. But just for a little bit, okay? I don't want to be out too late or anything."
            "She glances around again, then leans in close and whispers, her voice low and husky."
            the_person "And just so you know, I'm still in charge here, even if we're just grabbing a drink, got it?"
            "You can't help but feel a little excited by her assertiveness and slightly playful tone."
            mc.name "Okay, okay. I'll behave, I promise."

    else:
        # the_person "Yeah? Well there's nobody around, and I'm not going to stop you."
        the_person "Oh yeah? Well then, do you want to share what all of these naughty things are, huh? You have my attention, I guess."
        menu:
            "Feel her up":
                "You put your arms around [the_person.possessive_title]'s waist and rest your hands on her ass, looking slightly eager and slightly playful."
                mc.name "You know, I've been waiting for this moment for a while now, okay?"
                "You massage her butt, and she blushes and pushes you away lightly, looking slightly annoyed but also slightly amused."
                the_person "Hey, no need to be so forward, okay? What's gotten into you?"
                "You pull her close again and shift your hands to her breasts, squeezing them gently and looking slightly eager and slightly playful."
                mc.name "Come on, don't be like that. I just wanted to make you feel good for once, okay?"
                call fuck_person(the_person, private = True, start_position = standing_grope, skip_intro = True) from _vt_tomboy_call_fuck_person_80
                $ the_person.call_dialogue("sex_review", the_report = _return)
                $ the_person.review_outfit()

            "Just flirt":
                $ mc.change_locked_clarity(10)
                "You put your arms around [the_person.possessive_title]'s waist and rest your hands on her ass, looking slightly playful and slightly flirtatious."
                mc.name "I wish I had the time, okay? You'll have to wait until later, I guess."
                "You massage her butt, and she sighs happily and leans her weight against you, looking slightly pleased and slightly relaxed."
                the_person "Aww, are you sure, okay? I was kind of hoping we could... you know, take things a little further or something."
                "You slap her ass and step back, looking slightly playful and slightly flirtatious."
                the_person "Fine, but don't make me wait too long, okay? I have needs, and my [the_person.so_title] sure as hell isn't fulfilling them or anything."
                mc.name "I won't make you wait long, I promise, okay?"
                "She looks up at you with a playful pout, looking slightly annoyed but also slightly amused."
                the_person "Promise you won't make me wait, huh? I'm not sure I can handle it if you do, okay?"
                mc.name "I promise, baby, okay?"
                "You both share a flirtatious smile, looking slightly playful and slightly eager."
                the_person "Good. Because I'm not sure I can handle it if you do, okay?"
    return

label tomboy_flirt_response_text(the_person):
    mc.name "Hey [the_person.title], how's it going? I'm feeling a bit bored and thought we could chat, okay?"
    "She replies with a hint of annoyance and a slightly playful tone."
    if the_person.is_affair:
        the_person "Gah, great, you're bored again? You always seem to find ways to bother me, don't you?"
        the_person "Well, what do you want this time, huh? I'm not exactly thrilled about entertaining you or anything."
        the_person "When can we get together, okay? Make it quick, I'm busy."
        mc.name "Some time soon, I'll let you know, okay?"

    elif the_person.is_girlfriend:
        the_person "Bored, huh? That's not exactly a surprise, okay? You're always looking for something new to entertain yourself, I guess."
        the_person "But fine, we can hang out, I suppose. Just don't expect me to do anything special or anything, got it?"
        mc.name "Some time soon, I'll let you know, okay?"

    elif the_person.love < 40:
        if the_person.effective_sluttiness() > the_person.love:
            the_person "Ugh, bored, really? Well, I suppose I can keep you company for a bit, okay? But don't think this means I'm going to start flirting with you or anything."
        else:
            the_person "Bored, eh? That's not surprising, okay? You're always looking for a new distraction or something, I guess."

    else:
        if the_person.effective_sluttiness() > the_person.love:
            the_person "Fine, I'll talk to you, okay? But don't think this means I'm happy about it or anything, got it?"
            the_person "So, what do you want to talk about, huh? I'm not exactly thrilled about this, but I'll play along, I guess."
        else:
            the_person "You're bored, huh? Well, that's your problem, not mine, okay?"
            the_person "So, what do you want, huh? Just don't expect me to be all lovey-dovey about it or anything, got it?"
    return

label tomboy_condom_demand(the_person):
    if the_person.wants_creampie:
        the_person "Geez, get a grip, dude. You're not even wrapped up yet. What's the holdup?"
        "She rolls her eyes and crosses her arms, looking slightly annoyed but also slightly amused."
        the_person "I know, I know, it's a drag, but come on, it's necessary, okay?"
    else:
        the_person "Seriously? You're not even carrying? Get a condom, pronto, or this isn't happening, got it?"
        "She puts her hands on her hips, looking slightly annoyed but also slightly assertive."
        the_person "I don't want to have to deal with any... unpleasantness because you were too lazy to wrap it up, okay?"
    return

label tomboy_condom_ask(the_person):
    if the_person.on_birth_control:
        the_person "You're asking me if you should use a condom? Uh, I'm on the pill, so it's not like it's a huge deal or anything, okay?"
        "She shrugs and looks away, looking slightly nonchalant but also slightly amused."
        the_person "But hey, better safe than sorry, right? Go ahead and use one if it makes you feel better, I guess."
        $ the_person.update_birth_control_knowledge()
    elif the_person.wants_creampie:
        the_person "Ugh, you want to go bareback? Are you kidding me? Just put on a condom already, geez."
        "She throws up her hands, looking slightly exasperated but also slightly playful."
        the_person "I mean, I know it's not the most fun thing in the world, but come on, it's better than the alternative, right?"
        $ the_person.discover_opinion("creampies")
    else:
        the_person "Fine, use a condom, okay? Just don't make a mess of it, or I'll have to clean up after you, and that's just not happening, got it?"
        "She gives you a stern look, looking slightly annoyed but also slightly assertive."
        the_person "And don't even think about pulling out, okay? That's just a recipe for disaster, and I'm not exactly in the mood for it, okay?"
    return

label tomboy_condom_bareback_ask(the_person):
    if the_person.wants_creampie:
        if the_person.is_infertile:
            the_person "Gah, condoms are so overrated, don't you think? Just give me the real deal, okay?"
            "She smirks and winks at you, looking slightly playful but also slightly assertive."
            the_person "I want to feel you inside me, no barriers, no BS. Just us, raw and unfiltered."
        elif the_person.on_birth_control:
            the_person "Ugh, don't even think about wrapping it up, [the_person.mc_title]. I've got this, okay?"
            "She pats her pocket, where her birth control is, and gives you a sassy grin."
            the_person "I'm on the pill, so we're good to go. Just give me what I want, and let's get this party started."
            $ the_person.update_birth_control_knowledge()
        else:
            the_person "Screw the condom, [the_person.mc_title]. I want to feel you, all of you, inside me."
            "She takes a step closer, her eyes locked on yours, and her voice low and husky."
            the_person "I don't care about the risks, it's worth it for this kind of pleasure. And who knows, maybe we'll get lucky and make something beautiful happen."
            if not the_person.knows_pregnant:
                the_person "Imagine how hot it would be to get knocked up, huh? The ultimate rebellion against the norm."
        $ the_person.discover_opinion("creampies")
    else:
        the_person "Don't bother with the condom, [the_person.mc_title]. I want it raw, I want it real, and I want it now."
        "She grabs your arm, her grip firm but gentle, and her eyes sparkling with mischief."
        if not the_person.knows_pregnant:
            the_person "I don't care about the risks, it's worth it for the rush. And if something happens, well, that's just part of the adventure, right?"
        else:
            the_person "I love it when you take me raw, [the_person.mc_title]. It's like we're two rebels, taking on the world, one fuck at a time."
    return

label tomboy_condom_bareback_demand(the_person):
    if the_person.has_breeding_fetish: #Actively looking to get knocked up.
        if the_person.knows_pregnant:
            the_person "Gah, what's the holdup? I want to get knocked up, so ditch the condom already!"
            "She rolls her eyes and taps her foot impatiently, looking slightly annoyed but also slightly excited."
            the_person "Come on, I'm ready to take the risk. Give me that hot, sticky load and make me pregnant!"
        elif the_person.is_infertile:
            the_person "Ugh, thanks for reminding me I'm barren, okay? That's just what I needed to hear."
            "She crosses her arms and looks away, her expression slightly bitter and slightly annoyed."
        else:
            the_person "What's the point of screwing if you're not going to give me a baby, huh?"
            "She puts her hands on her hips and looks at you expectantly, her expression slightly assertive and slightly playful."
            the_person "Come on, I'm ready to take the risk. Give me that cock and make me pregnant!"
    elif the_person.wants_creampie: #Just likes raw sex
        if the_person.is_infertile:
            the_person "Gah, condoms are so overrated, don't you think? I'm not getting pregnant anyway, so what's the point?"
            "She shrugs and looks at you with a slightly playful expression."
        elif the_person.on_birth_control:
            the_person "Forget the condom, [the_person.mc_title]. I've got this covered, okay?"
            "She pats her pocket, where her birth control is, and gives you a sassy grin."
            the_person "Take me bareback and make me scream, [the_person.mc_title]. I'm ready for it."
            $ the_person.update_birth_control_knowledge()
        else:
            the_person "Ugh, condoms are so annoying. Just get inside me already, okay?"
            "She grabs your arm and pulls you closer, her expression slightly impatient and slightly playful."
    else:
        if the_person.is_infertile:
            the_person "Take me bareback, [the_person.mc_title]. It's not like I can get pregnant or anything, okay?"
            "She shrugs and looks at you with a slightly nonchalant expression."
            the_person "Just make me feel good, [the_person.mc_title]. That's all I care about."
        elif the_person.on_birth_control:
            the_person "Forget the condom, [the_person.mc_title]. I'm on the pill, so we're good to go, okay?"
            "She gives you a thumbs up and a slightly playful grin."
            the_person "Take me bareback and make me feel every inch of you, [the_person.mc_title]. I'm ready for it."
            $ the_person.update_birth_control_knowledge()
        else:
            the_person "Ugh, condoms are so annoying. Just get inside me already, okay?"
            "She grabs your arm and pulls you closer, her expression slightly impatient and slightly playful."
            the_person "I need to feel you deep inside me, [the_person.mc_title]. Make it happen."
    return

label tomboy_cum_face(the_person):
    if the_person.has_cum_fetish or the_person.obedience > 180:
        if the_person.has_cum_fetish or the_person.effective_sluttiness() > 60 or the_person.opinion.cum_facials > 0:
            the_person "Gah, I'm such a mess, [the_person.mc_title]! But I guess it's kinda hot, huh?"
            "[the_person.title] smirks, then licks her lips and runs a finger through your semen, bringing it to her mouth and making a slightly playful face."
            the_person "Mmm, taste the victory, I guess. You win this round, [the_person.mc_title]."
        else:
            the_person "Hmph, I suppose it's not the worst look I've ever had. But I'm still not thrilled about it, okay?"
            "[the_person.title] wipes away some of your semen from her face, looking slightly annoyed but also slightly amused."
    else:
        if the_person.effective_sluttiness() > 80 or the_person.opinion.cum_facials > 0:
            the_person "Well, I guess this is one way to end things, huh? Do you think I look good like this, [the_person.mc_title]?"
            "[the_person.title] smirks, then laughs and wipes away some of your semen from her face, looking slightly playful and slightly flirtatious."
        else:
            the_person "Ugh, just get that over with already, okay? And don't think you're getting a second chance or anything."
            "[the_person.title] wipes away your semen, looking slightly put off and slightly annoyed."
    return

label tomboy_cum_mouth(the_person):
    if the_person.has_cum_fetish or the_person.obedience > 180:
        if the_person.has_cum_fetish or the_person.effective_sluttiness() > 60 or the_person.opinion.drinking_cum > 0:
            the_person "Mmm, that's so... satisfying, [the_person.mc_title]. You really know how to make me feel good, I guess."
            the_person "I mean, it's not like I'm going to start doing this all the time or anything, but... yeah."
        else:
            "[the_person.title]'s face twists in disgust as she swallows your cum, looking slightly annoyed and slightly grossed out."
            the_person "Ugh, there, done. Don't think I enjoyed that one bit, okay? That was just... ugh."
    else:
        if the_person.effective_sluttiness() > 80  or the_person.opinion.drinking_cum > 0:
            the_person "Mmm, you're quite the stud, [the_person.mc_title]. I can see why you're so popular, I guess."
            the_person "But don't think this means I'm going to start worshiping you or anything, okay? I'm still in charge here."
        else:
            the_person "Ugh, that's... quite a taste, [the_person.mc_title]. I hope you're happy, I guess."
            the_person "But next time, can we just stick to something a little more... normal, okay? This was just... weird."
    return
### DIALOGUE ###

label tomboy_cum_pullout(the_person):
    # Lead in: "I'm going to cum!"
    if mc.condom:
        if the_person.wants_creampie and not the_person.has_taboo("condomless_sex"): #TODO: FIgure out we want any more requirements for this to fire.
            if the_person.knows_pregnant:
                the_person "Gah, forget the condom, just cum inside me and make me pregnant already, okay?"
                "She looks up at you with a slightly annoyed but also slightly playful expression."
                the_person "I don't care about the consequences right now, I just want your cum filling me up and making me feel good, got it?"
            elif the_person.on_birth_control:
                the_person "Oh, for crying out loud... take that stupid condom off, [the_person.mc_title]!"
                "She rolls her eyes and looks at you with a slightly exasperated expression."
                the_person "I give in, I want you to cum inside me and make me feel good, okay?"
            else:
                "She looks up at you with a slightly desperate expression."
                the_person "I don't care about anything right now, just take off the condom and cum inside me, okay?"
                $ the_person.update_birth_control_knowledge()
                the_person "I want you to make me cum and then make me pregnant, you dirty bastard!"
            menu: #TODO: Add a variant of this normally so you can stealth a girl (don't do that in real life, it's super fucked up).
                "Take off the condom":
                    "You pull out, barely clearing her pussy, and pull the condom off as quickly as you can manage, looking slightly eager and slightly playful."
                    $ mc.condom = False
                    $ use_condom = False  # prevent putting on a new condom next sex loop
                "Leave it on":
                    "You ignore [the_person.possessive_title]'s request and keep the condom in place, looking slightly annoyed but also slightly amused."
        else:
            the_person "Hell yeah, I'm going to make you cum, [the_person.mc_title]! Get ready for it, okay?"
    else:
        if the_person.wants_creampie:
            if the_person.knows_pregnant: #She's already knocked up, so who cares!
                the_person "Creampie me, you dirty bastard, and make me cum already, okay?"
                "She looks up at you with a slightly playful and slightly flirtatious expression."
            elif the_person.opinion.creampies > 0:
                "[the_person.possessive_title!c] moans happily and looks up at you with a slightly pleased expression."
                if the_person.on_birth_control: #She just likes creampies.
                    the_person "Fuck yeah, fill me up with your cum, [the_person.mc_title]! Creampie me and make me feel good, okay?"
                else: #Yeah, she's not on BC and asking for you to creampie her. She's looking to get pregnant.
                    $ the_person.update_birth_control_knowledge()
                    the_person "Oh, for crying out loud... cum inside me and knock me up, [the_person.mc_title]! I want you to breed me like a dirty slut, okay?"
            elif the_person.is_infertile:
                the_person "Cum wherever you want, you dirty bastard, I'm not going to get pregnant or anything, okay?"
                "She shrugs and looks at you with a slightly nonchalant expression."
            elif the_person.on_birth_control: #She's on the pill, so she's probably fine
                $ the_person.update_birth_control_knowledge()
                the_person "Cum wherever you want, you dirty bastard, I'm on the pill, so it's not like it matters or anything, okay?"
            else: #Too distracted to care about getting pregnant or not. Oh well, what could go wrong?
                the_person "Just do it already, okay? Cum and make me feel good, I don't care about anything else, got it?"
        else:
            if the_person.is_infertile:
                the_person "Just pull out, okay? I don't want your cum inside me, you dirty bastard, it's not like it's going to do anything or anything."
            elif not the_person.on_birth_control: #You need to pull out, I'm not on the pill!
                $ the_person.update_birth_control_knowledge()
                the_person "Fuck, pull out, you dirty bastard! I'm not on the pill, so don't even think about cumming inside me, got it?"
            elif the_person.opinion.creampies < 0:
                the_person "Pull out, okay? I don't want you to cum in me, you dirty bastard, it's just not my thing, sorry."
            else:
                the_person "Hell yeah, pull out and cum all over me like a dirty slut, [the_person.mc_title]! Make me feel good, okay?"
    return

label tomboy_cum_condom(the_person):
    if the_person.effective_sluttiness() > 75 or the_person.opinion.creampies > 0:
        the_person "Gah, this feels so freaking amazing! If your condom broke, I'd be totally screwed... and possibly pregnant, okay?"
        "She looks up at you with a slightly mischievous expression, her eyes sparkling with amusement."
    else:
        the_person "Oh man, I hope you didn't skimp on the condoms, because that's a whole lot of... stuff, okay?"
        "She raises an eyebrow and looks at you with a slightly skeptical expression."
        the_person "But hey, maybe you're secretly hoping to knock me up and get me pregnant or something, huh? Well, let's just hope that doesn't happen, okay?"
    return

label tomboy_cum_vagina(the_person):
    if the_person.has_taboo("creampie"):
        $ the_person.call_dialogue("creampie_taboo_break")
        $ the_person.break_taboo("creampie")
        return
    if the_person.wants_creampie:
        if the_person.knows_pregnant:
            the_person "Gah, fine... I guess I can admit it now, but only because I'm already knocked up from your other, uh, impressive performances... Your cum just feels so freaking amazing inside me, okay?"
            "She looks up at you with a slightly mischievous expression, her eyes sparkling with amusement."
        elif the_person.is_infertile:
            the_person "Oh, stop being so dramatic! Of course you're not going to get me pregnant, I'm infertile, remember? But seriously, your cum is pretty great... just don't expect me to admit it to anyone else, got it?"
            "She rolls her eyes and looks at you with a slightly playful expression."
        elif the_person.on_birth_control:
            if the_person.has_significant_other:
                the_person "Well, well, well... Look at you go! I guess it's a good thing I'm on the pill, huh? Or maybe I'll just tell [the_person.so_name] that it was someone else's... Ugh, why do you have to be so frustrating, okay?"
                "She throws up her hands and looks at you with a slightly exasperated expression."
            else:
                if the_person.knows_pregnant:
                    the_person "Oh fuck, that's a lot of cum! Good thing I'm already pregnant, because I don't think you're firing blanks or anything, okay?"
                elif the_person.is_infertile:
                    the_person "Oh fuck, that's a lot of cum! I'll be dripping your cum all day long, thanks for that, I guess."
                else:
                    the_person "Oh fuck, that's a lot of cum! Good thing I'm on the pill, because I don't think you're firing blanks or anything, okay?"
                $ the_person.update_birth_control_knowledge()
        elif the_person.effective_sluttiness() > 75 or the_person.opinion.creampies > 0:
            if the_person.has_significant_other:
                the_person "Okay, okay, I get it! You're great in bed, but don't think I'm going to start flaunting our little secret around my [the_person.so_title]... At least, not until I figure out how to explain it, okay?"
                "She looks at you with a slightly mischievous expression, her eyes sparkling with amusement."
            else:
                the_person "Ugh, fine... I'll admit it, you're pretty amazing when you're like this... But don't think this means I'm going to start begging for more or anything, got it?"
                "She looks at you with a slightly playful expression, her eyes sparkling with amusement."
        else:
            if the_person.has_significant_other:
                the_person "You really know how to make a girl feel special, don't you? But let's keep this between us, okay? I don't think [the_person.so_name] would understand... or care, for that matter."
                "She looks at you with a slightly serious expression, her eyes narrowed slightly."
            else:
                the_person "Wow... I guess I didn't expect that from you. But I have to admit, it was kind of nice... Just don't get any ideas, okay? I'm not ready for anything serious or anything."
                "She looks at you with a slightly playful expression, her eyes sparkling with amusement."
    else: #She's angry
        if the_person.knows_pregnant:
            the_person "Ugh, what is wrong with you? I specifically told you not to do that! Oh well, since I'm already pregnant... I guess it doesn't matter now, okay?"
            "She throws up her hands and looks at you with a slightly exasperated expression."
        elif not the_person.on_birth_control:
            if the_person.has_significant_other:
                the_person "Oh, great. Just what I needed. You forgot to pull out, and now I'm going to have to deal with [the_person.so_name]'s anger... again, probably."
                "She rolls her eyes and looks at you with a slightly annoyed expression."
            else:
                the_person "Oh fuck, I said to pull out! I'm not on the pill [the_person.mc_title], what happens if I get pregnant, huh?"
                $ the_person.update_birth_control_knowledge()
                the_person "What is wrong with you? You know I'm not on the pill! Now look what you've done... I guess next time we'll have to use a condom, okay?"
                "She looks at you with a slightly annoyed expression, her eyes narrowed slightly."
        elif the_person.is_infertile:
            the_person "Unbelievable! I told you to pull out, and now you've gone and made a mess... What a pain in the ass, okay?"
            "She throws up her hands and looks at you with a slightly exasperated expression."
        elif the_person.has_significant_other:
            the_person "You're really going to make me tell [the_person.so_name] about this, aren't you? Fine, I'll deal with it. Just be more careful next time, okay?"
            $ the_person.update_birth_control_knowledge()
            the_person "I don't want to have to make you wear a condom, so be a little more careful next time, got it?"
            "She looks at you with a slightly serious expression, her eyes narrowed slightly."
        elif the_person.opinion.creampies < 0:
            the_person "Oh, great. Just what I needed. You couldn't even follow a simple instruction, could you? Now look at what a mess you've made, okay?"
            "She looks at you with a slightly annoyed expression, her eyes narrowed slightly."
        else:
            the_person "You really need to work on your timing, okay? I told you to pull out, not do the exact opposite!"
            the_person "Just remember, I'm not going to be as forgiving next time if you can't follow simple instructions, got it?"
            "She looks at you with a slightly serious expression, her eyes narrowed slightly."
    return

label tomboy_cum_anal(the_person):
    if the_person.has_taboo("anal creampie"):
        $ the_person.call_dialogue("anal_creampie_taboo_break")
        $ the_person.break_taboo("anal creampie")
        return

    if the_person.sluttiness > 75 or the_person.opinion.anal_creampies > 0:
        the_person "Gah, fine... I guess it's okay if you do that, but don't think I'm going to start asking for it all the time or anything, got it?"
        "She looks at you with a slightly playful expression, her eyes sparkling with amusement."
    elif the_person.opinion.anal_creampies < 0:
        the_person "Oh, come on... not in there, okay? I don't need to be embarrassed like that, especially not right now."
        "She crosses her arms and looks away, her expression slightly annoyed."
    else:
        the_person "Oh, alright... if you insist, I guess. But just this once, and don't think I'm going to start liking it or anything, okay?"
        "She looks at you with a slightly hesitant expression, her eyes narrowed slightly."
    return

label tomboy_surprised_exclaim(the_person):
    $rando = renpy.random.choice(["What the freaking hell?", "Ugh, seriously?", "Why now, of all times?", "This again? Really?", "Not again, okay?", "Seriously, what's going on?", "Great, just what I needed...", "Oh, joy... just peachy...", "Freaking perfect, just what I wanted...", "Unbelievable, okay?", "Not again, not now!", "Why can't I just have a normal day for once?"])
    the_person "[rando]"
    "She throws up her hands and looks at you with a slightly exasperated expression."
    return

label tomboy_talk_busy(the_person):
    if the_person.obedience > 120:
        the_person "Gah, I don't have time for this, okay? I've got way too much on my plate right now, [the_person.mc_title]. Can it wait?"
        "She looks at you with a slightly annoyed expression, her eyes narrowed slightly."
    else:
        the_person "Listen, I'd love to catch up and all, but I'm totally swamped with things to do right now. Maybe we can talk later, okay?"
        "She looks at you with a slightly apologetic expression, her eyes sparkling with amusement."
    return

label tomboy_sex_strip(the_person):
    if the_person.sluttiness < 20:
        if the_person.arousal_perc < 50:
            the_person "Gah, fine. I'll take off some clothes, but don't think I'm doing this because I'm into you or anything. I just need to get comfy, okay?"
            "She crosses her arms and looks away, her expression slightly annoyed."
            mc.name "Come on, relax. It's just us here. You can chill out."
            the_person "I don't care! I'm still not comfortable. And don't call me 'babe' or anything like that, got it? That's just weird."
            "She looks at you with a slightly exasperated expression, her eyes narrowed slightly."
            mc.name "Okay, okay. I'll stop. Just take your time, okay?"
        else:
            the_person "Alright, alright. I'll take off a few things, but don't expect me to be all impressed by your reaction or anything. I'm just taking off some clothes, big whoop."
            "She shrugs and starts to undress, her expression slightly nonchalant."
            mc.name "Aww, come on. You're being a little rough. Just let me see you a little more, okay?"
            the_person "Fine, but only because you asked nicely. And don't think this means I'm into you or anything, got it?"
            "She looks at you with a slightly playful expression, her eyes sparkling with amusement."
    elif the_person.sluttiness < 60:
        if the_person.arousal_perc < 50:
            the_person "Fine, I'll make an exception and get a little more comfortable. But don't get any ideas, okay?"
            "She looks at you with a slightly serious expression, her eyes narrowed slightly."
            mc.name "I promise, I won't get any ideas. I just want to make sure you're comfortable."
            the_person "Ugh, fine. But don't think I'm doing this for you. I just need to get a little more comfortable, okay?"
            "She starts to undress, her expression slightly hesitant."
            mc.name "I understand. Just take your time and let me know if you need anything."
        else:
            the_person "Okay, okay. I'll take off a few more things if it'll make you happy. But don't think I'm doing this because I'm into you or anything, got it?"
            "She rolls her eyes and starts to undress, her expression slightly playful."
            mc.name "I know, I know. You're just doing it because you want to, right?"
            the_person "Whatever. Just let me get this off and we can get on with this. And don't think this means I'm going to start liking you or anything, okay?"
            "She looks at you with a slightly annoyed expression, her eyes narrowed slightly."
    else:
        if the_person.arousal_perc < 50:
            the_person "Ugh, fine. I'll do it. But just for you, I'll make an exception. And don't think I'm doing this because I'm into you or anything, got it?"
            "She looks at you with a slightly exasperated expression, her eyes narrowed slightly."
            mc.name "Thanks, I guess. You're making me really happy right now."
            the_person "Don't get too happy. I'm just doing this because I have to, okay?"
            "She starts to undress, her expression slightly hesitant."
        else:
            the_person "Great, now let me get this off and we can get on with this. I'm dying over here! But don't expect me to be all happy about it or anything, got it?"
            "She looks at you with a slightly playful expression, her eyes sparkling with amusement."
            mc.name "Aww, come on. You're being a little grumpy. Let's just have some fun, okay?"
            the_person "Fine. But don't expect me to start smiling and laughing or anything, okay? I'm just here for the sex."
            "She looks at you with a slightly annoyed expression, her eyes narrowed slightly."
    return

label tomboy_sex_watch(the_person, the_sex_person, the_position):
    $ title = the_person.title if not the_person.is_stranger else "The stranger"
    if the_person.sluttiness < the_position.slut_requirement - 20:
        $ the_person.draw_person(emotion = "angry", display_transform = character_left_flipped)
        the_person "Gah, seriously? Can you two keep it down? I'm trying to [the_person.possessive_pronoun] focus on something else here."
        "She rolls her eyes and shakes her head, looking slightly annoyed."
        $ the_person.change_stats(obedience = -2, happiness = -1)
        "[title] tries to ignore you and [the_sex_person.fname] [the_position.verb], but can't help sneaking a peek."
        return False
    if the_person.sluttiness < the_position.slut_requirement - 10:
        $ the_person.draw_person(display_transform = character_left_flipped)
        the_person "Honestly, you two are so extra. Can't you just keep it on the down low for once?"
        "She looks away, trying to pretend she's not interested in what you and [the_sex_person.fname] are doing, but can't help sneaking a glance."
        $ the_person.change_happiness(-1)
        "[title] tries to act nonchalant, but her curiosity is piqued."
        return False
    if the_person.sluttiness < the_position.slut_requirement:
        $ the_person.draw_person(display_transform = character_left_flipped)
        if not is_watching(the_person):
            the_person "You're really getting into it, aren't you? I suppose it's kind of... intriguing."
        "She watches you and [the_sex_person.fname] [the_position.verb] with a mixture of fascination and embarrassment."
        $ the_person.change_slut(1, 30)
        "[title] can't help but be drawn in by the scene unfolding before her."
        return True
    if the_person.sluttiness >= the_position.slut_requirement and the_person.sluttiness < the_position.slut_cap:
        $ the_person.draw_person(display_transform = character_left_flipped)
        if not is_watching(the_person):
            the_person "Oh, wow... this looks like so much fun. Can I join the party?"
        "She watches you and [the_sex_person.fname] [the_position.verb] with a mischievous glint in her eye."
        $ the_person.change_slut(1, 50)
        "[title] is clearly turned on by the scene, and is considering joining in."
        return True
    $ the_person.draw_person(emotion = "happy", display_transform = character_left_flipped)
    if renpy.random.randint(0, 1) == 0:
        the_person "You know, [the_person.mc_title], [the_sex_person.fname] is really getting into this. Maybe you should, uh, take it up a notch?"
    else:
        call watcher_position_comment(the_person, the_sex_person, the_position) from _call_watcher_position_comment_tomboy_sex_watch
    "[title] watches with interest as you and [the_sex_person.fname] [the_position.verb], her eyes sparkling with excitement."
    return True

label tomboy_being_watched(the_person, the_watcher, the_position):
    $ title = the_watcher.fname if not the_watcher.is_stranger else "the stranger"
    if the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #They agree you should give it to her harder
        the_person "Gah, I guess you're right, [the_person.mc_title]. But don't think I'm going easy on you just because we've got an audience, got it?"
        "She gives you a sassy grin and winks at [title]."
        the_person "I'm still in charge here, and don't you forget it."
        $ the_person.change_arousal(1)
        "[the_person.title] seems totally turned on by [title] watching you and her [the_position.verb]."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's super slutty and doesn't care what people think.
        the_person "You know, [title], I don't really care what you think, but it's pretty obvious you're totally checking us out right now, okay?"
        "She raises an eyebrow and looks at [title] with a slightly amused expression."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #She's super slutty and encourages the watcher to be slutty.
        the_person "Oh, come on, [title]! Don't be such a prude! You know you want a taste of this action, okay?"
        "She winks at [title] and gives her a playful nudge."
        $ the_person.change_arousal(1)
        "[the_person.title] seems totally turned on by [title] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #She's into it and encouraged by the slut watching her.
        "[the_person.fname] glances at [title] and gives her a slightly shy smile."
        the_person "Yeah, I guess I can handle a little more... for now, okay?"
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [title] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's into it but shamed by the prude watching her.
        the_person "Ugh, why do you have to be here, [title]? Can't you just leave me alone, okay?"
        "She looks at [title] with a slightly annoyed expression and crosses her arms."
        $ the_person.change_stats(arousal = -1, slut = -1)
        "[the_person.title] seems totally uncomfortable with [title] nearby."

    else: #the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #They're both into it but not fanatical about it.
        "[the_person.possessive_title!c] rolls her eyes at [title] and gives her a slightly playful grin."
        the_person "Whatever, [title], you're missing out. Maybe next time you'll get a chance, okay?"
        $ the_person.change_stats(arousal = 1, slut = 1, max_slut = 30)
        "[the_person.title] seems more comfortable [the_position.verbing] you with [title] around, but still a little hesitant."

    return

label tomboy_work_enter_greeting(the_person):
    if the_person.happiness < 80 or the_person.love < 0:
        "[the_person.title] barely looks up from her work when you enter the room, her expression slightly annoyed."
        the_person "What do you want, huh? Can't you see I'm busy?"
        "She mutters under her breath and goes back to her work, not looking up again."

    elif the_person.happiness > 130:
        if the_person.sluttiness > 40:
            the_person "Hey [the_person.mc_title], what's up? Just the person I was hoping to see, I guess."
            "She looks up from her work and gives you a slightly playful grin, her eyes sparkling with mischief."
            the_person "You know what they say: all work and no play makes for a total bore, right?"
            "She winks, inviting you to join her in some 'play', but still looks slightly hesitant."
        else:
            "[the_person.title] looks up from her work and gives you a slightly shy smile when you enter the room."
            the_person "Hey [the_person.mc_title], it's cool that you stopped by, I guess. Just to say hi, or whatever."
            "She looks away, slightly blushing, before quickly glancing back at you with a slightly playful expression."

    else:
        if the_person.sluttiness > 60:
            $ the_person.draw_person(position = "stand4")
            "[the_person.title] walks over to you when you come into the room, her movements slightly confident and playful."
            the_person "Well, well, well. Look who decided to drop by, huh?"
            "She leans in close, her voice slightly husky and sultry, but still with a playful tone."
            the_person "I've been waiting for you, [the_person.mc_title]. You know, just to catch up and stuff."
            "She brushes her fingers against your arm, sending shivers down your spine, but still looks slightly playful and teasing."
        else:
            the_person "Hey [the_person.mc_title]. Need anything, or are you just here to bother me, huh?"
            "She looks up at you, her eyes slightly soft and inviting, but still with a playful glint."
    return

label tomboy_date_seduction(the_person):
    if the_person.is_girlfriend:
        "[the_person.possessive_title!c] grabs your hand and pulls you around to look at her, a slightly playful expression on her face."
        the_person "Hey, that was such a blast. So I was thinking..."
        $ mc.change_locked_clarity(30)
        if the_person.effective_sluttiness(["vaginal_sex", "condomless_sex"]) > 60 and the_person.wants_creampie and the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex >= 0 and the_person.opinion.creampies >= 0 and not the_person.on_birth_control and not the_person.knows_pregnant:
            if the_person.opinion.creampies > 0: #No condoms, loves creampies, she's basically asking you to knock her up. So... have her ask you to knock her up!
                the_person "You're probably just going to say no, but I really want to get knocked up by someone like you, okay?"
                the_person "So, are you going to make me pregnant or what? I bet you could give me some amazing kids, huh?"
            else:
                the_person "I don't care if you don't use a condom, okay? I just want you to fuck me and make me feel good."
                the_person "You're so much better than those other guys, anyway. I mean, they're just so... basic."
        elif the_person.effective_sluttiness(["vaginal_sex", "condomless_sex"]) > 60 and the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex > 0:
            the_person "Ugh, fine. If you really want to know, I'd rather not use a condom, okay?"
            the_person "But don't think I'm doing it for you or anything. It just feels better that way, I guess."
        elif the_person.effective_sluttiness(["vaginal_sex"]) > 50 and the_person.opinion.vaginal_sex > 0:
            the_person "You know, I didn't really want to go home with someone like you, but..."
            the_person "You're kind of growing on me, I guess. So, do you want to fuck me or what?"
        elif the_person.effective_sluttiness(["anal_sex"]) > 60 and the_person.opinion.anal_sex > 0:
            the_person "I don't know why I'm even bothering to ask you this, but... do you want to fuck my ass, okay?"
            the_person "It's not like I'm asking for much, but you're probably just going to say no anyway, huh?"
        elif the_person.effective_sluttiness(["sucking_cock"]) > 40 and the_person.opinion.giving_blowjobs > 0:
            the_person "You know, I'm not really in the mood to do this, but... you're kind of cute when you're all worked up, okay?"
            the_person "So, do you want a blowjob or what? I mean, I'm not exactly begging for it or anything."
        elif the_person.effective_sluttiness() > 40 and the_person.opinion.being_covered_in_cum > 0:
            the_person "Ugh, fine. If you really want to know, I'd be okay with getting covered in your cum, okay?"
            the_person "But don't expect me to be all happy about it or anything, got it?"
        elif the_person.effective_sluttiness(["touching_body"]) > 40 and the_person.opinion.giving_tit_fucks > 0 and the_person.has_large_tits:
            the_person "I don't know why I'm even telling you this, but... I'd be okay with sucking you off between my tits, okay?"
            the_person "But don't think I'm doing it because I like you or anything, got it?"
        else: #She's not very slutty, so she leaves the invitation open to interpretation
            the_person "You know, I don't really feel like going home with you or anything, but..."
            the_person "I guess I could be persuaded if you do something really good, okay?"
            "She smirks, leaving the invitation open-ended and slightly playful."

    elif the_person.is_affair:
        the_person "So my [the_person.so_title] won't be home tonight, I was thinking..."
        "She reaches down and cups your crotch, rubbing it gently through your pants, a slightly mischievous expression on her face."
        $ mc.change_locked_clarity(40)
        if the_person.wants_creampie and the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex >= 0 and the_person.opinion.creampies >= 0 and not the_person.on_birth_control and not the_person.knows_pregnant:
            if the_person.opinion.creampies > 0: #No condoms, loves creampies, she's basically asking you to knock her up. So... have her ask you to knock her up!
                the_person "Fine, let's go back to my place so you can pin me to the bed and creampie me all night long, okay?"
                the_person "I swear, just the thought of your cum inside me is making me want to puke and yet... I'm getting wet, huh?"
            else:
                the_person "Alright, let's go back to my place. You can pin me to the bed and fuck me bareback all night long, okay?"
                the_person "I hate how much I want this, but I do. So just fuck me up with your cock already, got it?"
        elif the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex > 0:
            the_person "Ugh, fine. Let's go back to my place and fuck all night, no condoms, okay?"
            the_person "I don't want to admit it, but I'm really looking forward to this, huh?"
        elif the_person.opinion.vaginal_sex > 0:
            the_person "Fine, let's go back to my place and you can pound my tight fucking pussy until I'm a wreck, okay?"
            the_person "I hate how much I enjoy this, but... I do. So do it, got it?"
        elif the_person.opinion.anal_sex > 0:
            the_person "Ugh, alright. Let's go back to my place so you can... you know, okay?"
            the_person "I don't want to admit it, but my ass is really excited for this, huh?"
        elif the_person.opinion.giving_blowjobs > 0:
            the_person "Fine, let's go back to my place and you can choke me out with your cock, okay?"
            the_person "I hate how much I want this, but I do. So just do it already, got it?"
        elif the_person.opinion.being_covered_in_cum > 0:
            the_person "Ugh, alright. Let's go back to my place, and you can cover me in your sperm all night, okay?"
            the_person "I hate how much I enjoy this, but... I do. So just do it, got it?"
        elif the_person.opinion.giving_tit_fucks > 0 and the_person.has_large_tits:
            the_person "Fine, let's go back to my place so I can... you know, okay?"
            the_person "I hate how much I enjoy this, but I do. So just do it already, got it?"
        elif the_person.opinion.cheating_on_men > 0:
            the_person "Ugh, fine. Let's go back to my place, and you can do all the things I tell my [the_person.so_title] I hate, okay?"
            the_person "I don't want to admit it, but I'm really looking forward to this, huh?"
        else:
            the_person "Ugh, let's go back to my place and make him really regret leaving me alone for the night, okay?"

    elif not the_person.has_significant_other:
        $ mc.change_locked_clarity(20)
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                the_person "Ugh, fine. I've had a blast [the_person.mc_title], but there are a few more things I'd like to do with you, okay?"
                the_person "Want to come back to my place and find out what they are, huh?"
            else:
                the_person "Whatever. You've been a blast [the_person.mc_title]. Want to come back to my place, have a few drinks, and see where things lead, okay?"
                the_person "I suppose."
        else:
            if the_person.love > 40:
                the_person "Fine, I don't want to say goodbye either. Tonight's been amazing [the_person.mc_title], okay?"
                the_person "Do you want to come back to my place and have a few drinks, huh?"
            else:
                the_person "Whatever. This might be crazy, but I had a great time tonight and you make me a little crazy, okay?"
                the_person "Do you want to come back to my place and see where things go, huh? I don't know why I'm even asking."

    else:
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                $ mc.change_locked_clarity(20)
                the_person "Ugh, fine. I'm not done with you yet [the_person.mc_title], okay?"
                the_person "Want to come back to my place, but don't think you're getting away with anything, got it?"
                the_person "My [the_person.so_title] won't be home until morning, so we would have plenty of time, huh?"
            else:
                $ mc.change_locked_clarity(20)
                the_person "Whatever. This might be crazy, but do you want to come back to have another drink with me, okay?"
                the_person "My [the_person.so_title] is stuck at work and I don't want to be left all alone, huh?"
        else:
            if the_person.love > 40:
                $ mc.change_locked_clarity(20)
                the_person "Whatever. You're making me feel crazy [the_person.mc_title], okay?"
                the_person "Do you want to come have a drink at my place, but don't think this means anything, got it?"
                the_person "My [the_person.so_title] won't be home until morning, and we have a big bed you could help me warm up, huh?"
            else:
                $ mc.change_locked_clarity(20)
                the_person "Whatever. This is crazy, but would you want to have one last drink at my place, okay?"
                the_person "My [the_person.so_title] won't be home until morning... I suppose."
    return

label tomboy_sex_end_early(the_person):
    if the_person.sluttiness > 50:
        if the_person.love > 40:
            if the_person.arousal_perc > 60:
                the_person "Gah, seriously? You're done already? I was just getting into the zone, [mc.name]... You're not exactly the most energetic partner I've ever had, but I guess you tried, huh?"
                "She raises an eyebrow and looks at you with a slightly playful expression."
                the_person "But hey, I'll give you credit, you did try your best. Or at least, as best as you could, considering."
            else:
                the_person "Well, I suppose that's a wrap? I was ready to give you a lot more... But I guess you're not exactly the most enthusiastic about this whole situation, are you, huh?"
                "She shrugs and looks at you with a slightly nonchalant expression."
        else:
            if the_person.arousal_perc > 60:
                the_person "Hmph, you're sure you're finished? I was really getting into this... You know, I don't usually do this, but I was actually starting to enjoy myself, okay?"
                "She looks at you with a slightly annoyed expression."
                the_person "But I guess you're not exactly the most experienced, are you? I mean, it's not like I'm the one who needs to learn how to do this properly, got it?"
            else:
                the_person "I guess it was okay, I suppose. I mean, it's not like I was expecting much from you in the first place, but... yeah."
                "She shrugs and looks away, slightly disappointed."
    else:
        if the_person.love > 40:
            if the_person.arousal_perc > 60:
                the_person "Oh, come on, [mc.name], don't leave me hanging like this... I mean, I was actually starting to enjoy this, okay?"
                "She looks at you with a slightly playful expression, her eyes sparkling with amusement."
                the_person "But hey, I guess you're not exactly the most romantic guy out there, are you, huh?"
            else:
                the_person "Well, that was a nice little interlude, I suppose. I mean, it's not like I'm the type to be all lovey-dovey and shit, but... yeah."
                "She shrugs and looks away, slightly nonchalant."
        else:
            if the_person.arousal_perc > 60:
                the_person "Geez, I guess that was enough... I mean, I don't know why you even bother trying, you're not exactly the best at this, are you, huh?"
                "She rolls her eyes and looks away, slightly annoyed."
            else:
                the_person "Good, it's over. Now let's get this over with. I mean, I've got better things to do than hang around with someone who can't even manage to get it right, okay?"
                "She stands up and looks at you with a slightly impatient expression."
    return

label tomboy_sex_take_control(the_person):
    if the_person.arousal_perc > 60:
        the_person "What do you think you're doing, [mc.name]? Don't just leave me hanging like this! I mean, I'm the one who's supposed to be in control here, not you, got it?"
        "She looks at you with a slightly annoyed expression, her eyes narrowed slightly."
        the_person "But hey, if you're not going to finish the job, then I will. And don't think for a second that I won't make you regret it, okay?"
    else:
        the_person "Ugh, really? You're not even going to finish what you started? Fine, I'll do it myself then! And don't think you can just waltz in here and expect me to be all weak and submissive, got it?"
        "She looks at you with a slightly defiant expression, her eyes sparkling with amusement."
        the_person "I'm not that kind of girl, [mc.name]. I'm in control here, and don't you forget it."
    return

label tomboy_sex_beg_finish(the_person):
    the_person "Okay, fine, [mc.name], you want to play it cool? I'll let you off the hook this time, but just know that I'm going to make you pay for this, okay?"
    "She looks at you with a slightly playful expression, her eyes sparkling with amusement."
    the_person "And when I'm done, I'm going to make sure you know exactly who's in control here, got it?"
    return

label tomboy_sex_review(the_person, the_report):
    $ comment_position = the_person.pick_position_comment(the_report)
    if comment_position is None:
        return #You didn't actually do anything, no need to comment.

    $ used_obedience = the_report.get("obedience_used", False) #True if a girl only tried a position because you ordered her to.
    $ the_person.draw_person()  # make sure she stands up for talking with you

    #She's worried about her SO finding out because it was in public
    if the_report.get("was_public", False) and the_person.has_significant_other and the_person.opinion.cheating_on_men <= 0: #It was public and she cares.
        if the_person.is_affair: #Dialogue about her being into it, but you can't do this in case she gets caught.
            the_person "Gah, this is so crazy! I'm really getting into this, but we can't get caught, okay?"
            the_person "What if someone sees us and tells my [the_person.so_title]? I'll never hear the end of it, ugh!"
            "She looks around nervously, her eyes darting back and forth."
        elif used_obedience:
            the_person "I'm freaking out, [mc.name]! We're doing this in public! Someone might recognize me and tell my [the_person.so_title]."
            mc.name "Don't worry, nobody's going to tell anyone. We're being careful, okay?"
            the_person "I hope you're right... I don't want anyone finding out about this, got it?"
            "She looks at you with a slightly anxious expression."
        else:
            $ the_person.call_dialogue("surprised_exclaim")
            the_person "Oh no, we're out in public! Someone might see us and tell my [the_person.so_title]. I'll be so screwed, ugh!"
            mc.name "Don't worry, nobody's paying attention to us. Nobody's going to tell your [the_person.so_title], okay?"
            the_person "I hope you're right... I don't want anyone knowing about this, got it?"
            "She looks around nervously, her eyes darting back and forth."

    #She's single, but worried that you did in public.
    elif the_report.get("was_public", False) and (the_person.effective_sluttiness()+10*the_person.opinion.public_sex < comment_position.slut_cap):
        if used_obedience:
            the_person "Ugh, I'm so embarrassed! We're doing this in public! Everyone's staring at us like we're some kind of freaks..."
            the_person "I'll never live this down, [mc.name]. People are going to talk about this for weeks, ugh!"
            "She covers her face with her hands, looking mortified."
        else:
            the_person "Oh no, we're in public! Everyone's watching us and judging us for this... Ugh, this is so humiliating!"
            mc.name "Don't worry, nobody really cares what we're doing. They're just curious, okay?"
            the_person "I hope you're right, or I'm going to end up with a terrible reputation for this sort of thing... Ugh, I don't even want to think about it."

    elif the_report.get("girl orgasms", 0) > 2:
        if used_obedience:
            the_person "Oh my god, [mc.name]... I loved what you did to me... I never knew being submissive could feel so good, okay?"
            mc.name "I do enjoy when you keep begging me to make you cum again. It's almost like you're addicted to it, huh?"
            the_person "Shut up and kiss me, [mc.name]... Ugh, I'm so turned on right now."
            "She leans in close, her eyes sparkling with desire."
        else:
            the_person "I have never... cum that hard... It was just amazing... I guess I needed that, huh?"
            "She seems dazed by her orgasm as she tries to form coherent sentences."
            the_person "You really... know how to give a girl a good time... just gimme a second to catch my breath, okay?"
            mc.name "Take your time, I'm not going anywhere."
            the_person "Thanks, [mc.name]... I think I need a minute to recover before we can start again, huh?"

        call sex_review_trance(the_person) from _call_sex_review_trance_tomboy_sex_review

    #No special conditions, just respond based on how orgasmed and how slutty the position was.
    elif the_report.get("girl orgasms", 0) > 0 and the_report.get("guy orgasms", 0) > 0: #You both came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position cap, it was tame
            the_person "Ah, that was freaking nice... But I think we could go even further next time, [mc.name]. I'm not afraid to push the limits, okay?"
            the_person "Doesn't that sound like fun? I'm getting wet just thinking about it, ugh."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "Ah, that was just what I needed! I think we're very compatible, [mc.name]."
            the_person "Let's do it again some time soon, okay? I want to see how much further we can go, huh?"

        elif used_obedience: #She only did it because she was commanded
            the_person "Fuck, I... I didn't think I was going to cum like that. I guess I just can't resist a good command, huh?"
            mc.name "Aren't you going to thank me? You obviously had a good time, okay?"
            the_person "Shut up and don't get too full of yourself, [mc.name]. I'm still in charge here."

        else: # She's surprised she even tried that.
            the_person "Oh fuck, that was intense! I didn't think I was going to take it so far, but it just felt right, you know?"
            the_person "Don't think that's going to happen every time though, alright? I'm not a slut! I just like to push my boundaries sometimes, okay?"
        if the_person.love > 40:
            the_person "You know, I never thought I'd say this, but I think I might actually like this whole 'relationship' thing with you, [mc.name]."
        else:
            the_person "Well, that was fun. Let's do it again sometime, but not too soon, okay? I need to recover my dignity first, ugh."

    elif the_report.get("girl orgasms", 0) > 0: #Only she came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            the_person "Done already? Well, that's just not right. Next time I'm going to make sure we both cum and then some, okay?"
            the_person "I've got a few ideas that are going to blow you away, [mc.name]."
            "She smiles mischievously, already imagining your next encounter."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "You're all done? Well, that was freaking hot either way, [mc.name]."
            the_person "I'll repay the favour next time, alright? I promise. And maybe we can try something new, huh?"
            "She leans in close, whispering in your ear."

        elif used_obedience: #She only did it because she was commanded
            the_person "That's it? I mean, not like I wanted to do anything more, I just thought you were going to finish, okay?"
            mc.name "Some other time. I just wanted to see what you look like when you cum."
            the_person "I... Fuck, well, I guess you got what you wanted. But don't think I'm going to make it easy for you next time, got it?"
            the_person "It could have been worse, I guess."

        else: # She's surprised she even tried that.
            the_person "Oh fuck, that was intense! You really know how to make a girl feel good, [mc.name]."
            the_person "You're probably tired after all that work. I promise I'll repay the favour next time, okay? And maybe we can try something different, huh?"
            "She smiles, already looking forward to your next encounter."

    elif the_report.get("guy orgasms", 0) > 0: #Only you came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            the_person "Gah, you're already done? That's so lame!"
            "She rolls her eyes and looks at you with a slightly annoyed expression."
            mc.name "Sorry, I'll make it up to you next time."
            the_person "Well, I suppose I could be persuaded to try again. But don't expect any special treatment, got it?"
            mc.name "Yeah, I think I could handle that."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "You're already done? Such a tease! Fine, I'll let you off this time..."
            "She pouts and looks away, slightly disappointed."
            mc.name "Sorry, I'll make it up to you next time."
            the_person "You'd better, or you won't be hearing the word 'please' from me again, okay?"

        elif used_obedience: #She only did it because she was commanded
            the_person "I suppose you're worn out from all that... We're finished then?"
            "She shrugs and looks at you with a slightly nonchalant expression."
            mc.name "Yeah, that's all for now."
            the_person "Fine, but don't think this means you get to slack off next time, got it?"

        else:  # She's surprised she even tried that.
            the_person "Wow, that was... quite an experience. I think I got a little carried away there, huh?"
            "She looks at you with a slightly dazed expression, still trying to process what just happened."
            the_person "Maybe it's for the best that we stop here. I need to think about what I just did, okay?"

    elif the_person.energy < 10: #Nobody came and she's tired
        the_person "Ugh, I'm so done. Another time, maybe?"
        "She stretches and yawns, looking exhausted."
        mc.name "No worries, we'll do it another day."
        the_person "Just don't expect any special treatment when we try again, okay?"

    else: #Nobody came.
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            the_person "Gah, you're already done? What's the rush? We could've had more fun, huh?"
            "She crosses her arms and looks at you with a slightly annoyed expression."
            the_person "You're such a spoilsport [the_person.mc_title], okay?"

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "We're stopping? But we were just getting to the good stuff, okay?"
            "She pouts and looks away, slightly disappointed."
            mc.name "Sorry [the_person.title], maybe another time."
            the_person "Yeah, maybe. You can't just leave a girl hanging like that, you know, huh?"

        elif used_obedience: #She only did it because she was commanded
            the_person "Well, I wasn't expecting that. I thought you had more in mind, okay?"
            "She shrugs and looks at you with a slightly nonchalant expression."
            mc.name "You aren't disappointed, are you?"
            the_person "No, no. I just...wanted to see where things would go, that's all, huh?"
            the_person "It's fine. I'll just have to find someone else to take me further, okay?"

        else:  # She's surprised she even tried that.
            the_person "Ugh, you're probably right. We should stop now before we get too carried away, okay?"
            "She looks at you with a slightly nervous expression, still trying to process what just happened."
            the_person "I don't want to do something I'll regret later. Let's just keep this casual, huh?"

    # Gave creampie while she is not on birth control (extra dialogue when she could get pregnant)
    if the_report.get("creampies", 0) > 0 and not the_person.on_birth_control and not the_person.knows_pregnant:
        the_person "Well, I guess we just made things a little more interesting, didn't we, huh?"
        "She looks at you with a slightly mischievous expression, a hint of excitement in her voice."
        the_person "If I get pregnant, it'll serve you right for being so reckless, okay?"

    $ del comment_position
    return

## Role Specific Section ##

label tomboy_improved_serum_unlock(the_person):
    mc.name "[the_person.title], now that you've had some time to get used to the lab, I want to bounce some ideas off you."
    the_person "Yeah, what's on your mind, [mc.name]?"
    mc.name "Our R&D up to this point has been based on my old notes from university, but I've been thinking..."
    mc.name "There were some unofficial experiment results that suggested the effects might be enhanced by, uh, 'extracurricular activities'."
    "[the_person.title] raises an eyebrow, a hint of a grin on her face."
    the_person "Oh, you mean like how a good orgasm can make you feel like you're on top of the world?"
    mc.name "Well, yeah. Something like that. Does that sound crazy?"
    the_person "Not at all. I've been thinking the same thing. I have a hypothesis that an orgasm opens up chemical receptors that are normally blocked."
    mc.name "Whoa, that's deep. What if that's true? Does that open up any more paths for our research?"
    the_person "If it's true, I could leverage the effect to induce greater effects in our subjects. We could be talking about a whole new level of suggestibility here."
    "[the_person.possessive_title!c] grins mischievously, a spark of excitement in her eyes."
    the_person "We'll need to do some experiments to be sure, but I think we're onto something big here."
    mc.name "What kind of experiments?"
    the_person "I want to take a dose of serum myself, and you can record the effects. Then I'll...ahem...take care of myself, and we can compare the effects after."
    mc.name "Do you really think that's a good idea?"
    the_person "Not really, but we can't trust anyone else with this information if we're right. We have to be careful, but we can't just sit on this either."
    the_person "We might be able to make progress by brute force, but this is a chance to take our research to the next level. We could be talking about a breakthrough here."
    the_person "A finished dose of serum that raises my suggestibility. The higher it gets, the better. Then we'll just need some time and some privacy for me to see what sort of effects my...ahem...stimulation will have."
    "She winks at you, a confident glint in her eye."
    return

## Taboo break dialogue ##

label tomboy_kissing_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 30:
        the_person "Gah, fine. Let's just get this over with already. You've been eyeing me for ages, right?"
        "She rolls her eyes and looks at you with a slightly annoyed expression."
        mc.name "That's not true, but I'll play along."
        the_person "Whatever. Just shut up and kiss me already, okay?"
        mc.name "Oh, I'm not going to shut up that easily."
        the_person "Suit yourself. I'll just have to find someone else who's willing to kiss me, then."
        mc.name "Hold on, wait a minute. I'm not going anywhere."
        the_person "Oh? You're not going anywhere? Then get over here and kiss me already, geez!"
        mc.name "Alright, alright. Here I come."
    elif the_person.love >= 20:
        the_person "So we're doing this, huh? About time, if you ask me."
        "She looks at you with a slightly playful expression, a hint of excitement in her eyes."
        mc.name "I guess we are. What do you think?"
        the_person "It's about time we finally made out, [the_person.mc_title]. I've been waiting for this."
        mc.name "I'm glad you feel that way."
        the_person "Me too. Just be gentle, okay? I don't want to get hurt."
        mc.name "I will."
    else:
        the_person "I don't know if this is a good idea, [the_person.mc_title]. We're taking things too fast, aren't we?"
        "She looks at you with a slightly nervous expression, her eyes darting back and forth."
        mc.name "Are you scared?"
        the_person "No! I'm just...not sure if this is a good idea. But I trust you, I guess."
        mc.name "Good. Because I'm not going to let you back out now."
        the_person "Hmph. Fine. But if this is a mistake, it's on you, got it?"
        mc.name "It'll be worth it, I promise."

    return

label tomboy_touching_body_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 30:
        the_person "Come on then, don't be shy. You've wanted to touch me for ages, haven't you?"
        "She raises an eyebrow and looks at you with a slightly teasing expression."
        mc.name "Hey, I'm not that obvious!"
        the_person "Oh, please. I can see the way you look at me. You're practically drooling."
        mc.name "Well, I can't help it if you're irresistible."
        the_person "Irresistible? Pfft, you're just trying to get in my pants, okay?"
    elif the_person.love >= 20:
        the_person "So you're ready for this?"
        "You nod, and she looks at you with a slightly nervous expression."
        the_person "Me too, I think. I didn't think I'd be so nervous when you actually made a move."
        mc.name "Just relax. You trust me, right?"
        the_person "Of course. Just don't expect me to be all touchy-feely about it, okay?"
    else:
        the_person "I think you're getting a little ahead of yourself here [the_person.mc_title]."
        mc.name "What do you mean?"
        the_person "I mean I don't just let anyone feel me up. Maybe we should cool things down, huh?"
        mc.name "You're not scared, are you?"
        the_person "Scared? Of course not! I'm just...cautious, okay?"
        mc.name "Well then just relax and go with it. It doesn't have to mean anything unless we want it to."
        "You see her answer in her eyes before she says anything."
        the_person "You're so bad for me, you know that?"
        mc.name "Well let me make up for it then."
        the_person "Hmm, maybe I'll let you."
    return

label tomboy_touching_penis_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 35:
        the_person "Gah, you're totally hard, aren't you? Look at that thing."
        "She looks at your cock with a slightly amused expression, a hint of excitement in her eyes."
        mc.name "Do you want to feel it? You can if you want."
        the_person "Yeah, why not? I'll try not to break it, okay?"
        "She grins mischievously and reaches out to touch your cock."

    elif the_person.love >= 20:
        the_person "Your cock looks pretty sweet when it's hard, [mc.name]. Can I give it a try?"
        mc.name "Go ahead, it doesn't bite... unless you want it to, that is."
        the_person "Well, we'll see about that, okay?"
        "She smiles playfully and reaches out to touch your cock."

    else:
        mc.name "My cock is so hard right now [the_person.title]. Put your hand on it and touch it for me, okay?"
        the_person "What? That's taking things a little far, don't you think, [mc.name]?"
        mc.name "Come on, you know you want to. Just a few strokes, then if you aren't impressed you can stop, deal?"
        the_person "Fine, but don't expect me to make any promises after this, got it?"
        mc.name "I wouldn't dream of it."
        the_person "Hmm, okay then. I'll give it a try, but don't say I didn't warn you."
        "She looks at you with a slightly nervous expression, then reaches out and wraps her hand around your cock, her touch gentle but firm."
    "You feel a surge of pleasure as she starts to stroke you, her hand moving up and down your shaft."
    the_person "Mmm, you're really nice when you're hard, [mc.name]. I have to admit, I'm a little impressed."
    return

label tomboy_touching_vagina_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 35:
        the_person "Gah, come on already! You've been eyeing my pussy for ages, admit it."
        "She rolls her eyes and looks at you with a slightly annoyed expression, but a hint of excitement in her eyes."
        mc.name "Okay, okay. I'll touch it."
        the_person "About time, geez."

    elif the_person.love >= 20:
        the_person "Oh man, you've got my pussy totally tingling. I want you to touch it, [the_person.mc_title]."
        "She looks at you with a slightly playful expression, her eyes sparkling with desire."
        mc.name "You sure? I don't want to push you too far."
        the_person "No, I want it. I want you to touch me, okay?"
        "She nods and looks at you with a slightly eager expression."

    else:
        the_person "I don't know if we should be doing this, [the_person.mc_title]... It feels kinda weird."
        "She looks at you with a slightly nervous expression, her eyes darting back and forth."
        mc.name "Just take a deep breath and relax, okay? I'm just going to touch you a little, and if you don't like it I'll stop."
        the_person "Just a little?"
        mc.name "Just a little. Trust me, it's going to feel amazing."
        the_person "Hmm, okay. But don't think this means I'm easy, got it?"
        mc.name "I wouldn't dream of it."
        "She nods and looks at you with a slightly hesitant expression, but a hint of curiosity in her eyes."
    return

label tomboy_sucking_cock_taboo_break(the_person):
    mc.name "I want you to do something for me."
    the_person "Oh yeah? What do you want me to do to you, huh?"
    mc.name "I want you to suck on my cock."
    if the_person.effective_sluttiness() >= 45:
        the_person "Mmm, I think I'm down for that. It's not going to be too big for me, is it?"
        "She raises an eyebrow and looks at you with a slightly playful expression."
        mc.name "I think you'll be able to handle it."
        the_person "Alright, I don't want it choking me... but a little choking is okay, I guess."
        "She winks at you and bites her lip, a hint of excitement in her eyes."

    elif the_person.love >= 30:
        the_person "I guess we've been dancing around it for a while, huh?"
        "She looks your body up and down, a slightly hungry expression on her face."
        the_person "Alright, let's do this. But don't expect me to be all slobbery and gross, okay?"
        "She smirks and looks at you with a slightly playful expression."

    else:
        the_person "Oh, I was wondering if this was going to come up... Ugh, I don't know [the_person.mc_title]."
        "She laughs nervously and looks away from you, her eyes darting back and forth."
        mc.name "Don't overthink it. Just kneel down and suck on it for me. If you don't like doing it, we can just forget it happened, okay?"
        "You can see in her eyes the moment her resolve breaks. She bites her lip and nods, a slightly determined expression on her face."
        the_person "Alright, let's do this. But don't think this means I'm going to start sucking cock all the time, got it?"
        "She slowly gets down on her knees, her eyes darting between your face and your cock with a mix of reluctance and curiosity."
        the_person "You know, I never thought I'd be doing this. But I guess I'm willing to try new things for you, huh?"
        "She takes a deep breath, her hand wrapping around the base of your cock as she leans in to take it in her mouth."
        "As she starts to suck, her eyes flash up to meet yours, a hint of defiance and challenge in them."
        the_person "Satisfied now, or what?"
    return

label tomboy_licking_pussy_taboo_break(the_person):
    mc.name "I want to taste your pussy [the_person.title]. Are you ready?"
    if the_person.effective_sluttiness() >= 45:
        the_person "Gah, fine. I'm ready, I guess. But don't think this means I'm going to start getting all mushy on you or anything."
        "She rolls her eyes and looks at you with a slightly annoyed expression."
        mc.name "Good. But don't expect me to go easy on you just because it's your first time, got it?"
        the_person "Oh, please. I've had better, okay? Just get on with it."

    elif the_person.love >= 30:
        the_person "Finally, a guy who knows how to treat a girl right. I'm ready when you are, [mc.name]."
        "She smiles and looks at you with a slightly playful expression."
        mc.name "That's what I like to hear."
        the_person "Just don't expect me to be all slobbery and gross, okay? I'm still a lady, after all."

    else:
        if the_person.has_taboo("sucking_cock"):
            the_person "You know, I never thought I'd see the day where you'd be willing to do this, [mc.name]."
            "She bites her lip and smirks at you, a hint of amusement in her eyes."
            the_person "But I guess I'm not going to complain or anything. Just don't expect me to be all grateful, got it?"
        else:
            the_person "About time you decided to make up for not sucking my pussy, [mc.name]."
            "She rolls her eyes and smiles, a slightly teasing expression on her face."
            the_person "But fine, I'm ready. Just don't expect me to be all appreciative or anything, okay?"
    "She lies back, her eyes darting between yours and the area you're about to explore, a hint of nervousness in her expression."
    the_person "And don't think this means I'm some kind of slut for letting you do this, got it?"
    mc.name "I wouldn't dream of it. You're just being a good sport, right?"
    the_person "Something like that... Ugh, just get on with it already."
    "She closes her eyes, her face flushed with embarrassment as you start to lick her, her body tensing up slightly in anticipation."
    return

label tomboy_vaginal_sex_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 60:
        the_person "Gah, finally! I've been waiting for this moment all night. Come on then, get that cock inside me and fuck me like you mean it, already!"
        "She rolls her eyes and looks at you with a slightly impatient expression, her hips shifting slightly in anticipation."
    elif the_person.love >= 45:
        the_person "Alright, show me what you've got. I'm ready for this, [mc.name]."
        "She looks at you with a slightly playful expression, a hint of excitement in her eyes."
        mc.name "You better be. I'm going to make sure you remember this."
        the_person "Bring it on! I can take it, okay? I'm not some delicate flower or anything."
    else:
        if the_person.has_taboo("anal_sex"):
            the_person "Well, well, well. Look at that cock. I guess we're going to find out just how tight my pussy is, huh?"
            "She raises an eyebrow and looks at you with a slightly amused expression, a hint of curiosity in her eyes."
            mc.name "That's the plan. And if you're a good girl, I might just make it worth your while."
            the_person "Hmph, I'm always good. Now get to it before I change my mind, okay?"
        else:
            the_person "Oh, so that's what you're going to do with that big cock of yours. Well, I guess we'll see how it feels, huh?"
            "She looks at you with a slightly skeptical expression, a hint of uncertainty in her eyes."
            mc.name "We sure will. And if you're lucky, I might just make it feel even better."
            the_person "Ugh, just get on with it already! I'm not getting any younger, okay? And I'm not exactly thrilled about this either."
    return
### DIALOGUE ###

label tomboy_anal_sex_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 75:
        the_person "Gah, fine. But only because I'm a total sucker for a good time. Your cock is freaking huge, by the way."
        "She grins mischievously and looks at you with a slightly playful expression, her eyes sparkling with excitement."
        mc.name "Don't worry, I'll take it slow and make sure you're comfortable, okay?"
        the_person "Yeah, yeah. Just get on with it already! I'm not exactly a fragile little flower, you know."

    elif the_person.love >= 60:
        the_person "Are you sure you want to do this? I'm not exactly the most experienced person when it comes to anal... stuff."
        "She looks at you with a slightly nervous expression, a hint of uncertainty in her eyes."
        mc.name "I'll be gentle, don't worry. I promise I won't hurt you."
        the_person "Alright, but if it hurts too much, I'm stopping. I'm not exactly a masochist, okay?"

    else:
        if the_person.has_taboo("vaginal_sex"):
            the_person "Wait, are you sure you want to do this? My ass might be too tight for your... um... equipment."
            "She raises an eyebrow and looks at you with a slightly skeptical expression, a hint of amusement in her eyes."
            mc.name "I'll make it fit, but you might feel a little sore afterward, okay?"
            the_person "Oh, great. Just what I needed. More pain in my life."

        else:
            the_person "Come on, [mc.name]. Let's just get this over with already. I don't know what's gotten into me today, but I'm feeling kinda... reckless, I guess."
            "She shrugs and looks away, a hint of embarrassment in her expression."
            mc.name "Are you sure you're okay with this?"
            the_person "Of course, I'm just... nervous. And a little embarrassed. But let's just do this already, okay?"
            "She blushes and looks away, her face reddening slightly."
            mc.name "Alright, let's get started then."
            the_person "Hurry up, I'm ready when you are. Just don't expect me to be all smiles and rainbows about it, got it?"
    return
### DIALOGUE ###

label tomboy_condomless_sex_taboo_break(the_person):
    if the_person.knows_pregnant:
        the_person "Ugh, you really want to do it without a condom? Fine, but don't say I didn't warn you, okay?"
        if the_person.wants_creampie:
            the_person "If you're going to cum inside me, please make it worth my while. I'm not exactly looking forward to this, but I'll deal."
        else:
            the_person "Just make sure to cover me with your... you know, stuff. I don't want to be stuck cleaning up after you."

    elif the_person.opinion.bareback_sex > 0:
        the_person "Whatever, you want to do it bareback, huh? Just don't say I didn't warn you, got it?"
        if the_person.on_birth_control:
            the_person "I'm on the pill, so you don't have to worry about it. But don't think this means you can just go wild, okay?"
            $ the_person.update_birth_control_knowledge()
        elif the_person.wants_creampie:
            the_person "But if you're going to cum inside me, you'd better make it worth my while. I'm not exactly looking for a quickie here."
        elif the_person.opinion.creampies < 0:
            the_person "Just don't get me pregnant, okay? That would be a huge pain in the ass."
        else:
            the_person "Alright, just make sure you pull out this time. I don't want to have to deal with any... accidents."

    elif the_person.love > 60:
        if the_person.on_birth_control:
            the_person "Ugh, fine, I'm on the pill. Don't say I didn't warn you, okay?"
            $ the_person.update_birth_control_knowledge()
        elif the_person.wants_creampie:
            the_person "You're always trying to make me do stupid things, aren't you? Fine, if we're going to do this, make it worth my while."
            mc.name "Are you on the pill?"
            "She rolls her eyes and looks at you with a slightly annoyed expression."
            the_person "No, I'm not. But if you're going to cum inside me, you'd better make it worth it, got it?"
            $ the_person.update_birth_control_knowledge()
        elif the_person.opinion.creampies < 0:
            the_person "You're always trying to make me do stupid things, aren't you? Fine, just don't get me pregnant, okay?"
            the_person "I'm not ready for that kind of responsibility again. I've got enough on my plate already."
        else:
            the_person "You're always trying to make me do stupid things, aren't you? Fine, just make sure you pull out this time, okay?"
            if the_person.kids == 0:
                the_person "I need you to pull out though. I'm not quite ready to be a mom, even with you."
            elif the_person.kids == 1:
                the_person "I need you to pull out though. I've already got a kid, I don't need another one, okay?"
            else:
                the_person "I need you to pull out though. I've already got kids, I don't need another one, got it?"

    else:
        if the_person.on_birth_control:
            the_person "Hmph, you want to get busy without a rubber? Well, I'm on the pill, so I guess it's fine. Just don't expect any special treatment, okay?"
            $ the_person.update_birth_control_knowledge()
        elif the_person.has_taboo("vaginal_sex"):
            the_person "You're really not going to use a condom? I'm not on the pill, so we could end up with a little surprise, huh?"
            $ the_person.update_birth_control_knowledge()
            the_person "Or is this your sneaky plan to make a baby out of me? Because if it is, you're in for a rude awakening."
            mc.name "I swear I'll pull out. I want our first time to be memorable, okay?"
            "She crosses her arms and gives a half-hearted sigh, looking at you with a slightly skeptical expression."
            the_person "Ugh, fine. But you better pull out, or you'll regret it, got it?"
        else:
            the_person "You're really not going to use a condom? I'm not on the pill, so we could end up with a little surprise, okay?"
            $ the_person.update_birth_control_knowledge()
            the_person "Or is this your sneaky plan to make a baby out of me? Because if it is, you're in for a rude awakening, buddy."
            mc.name "I promise I'll pull out. It'll feel so much better without anything between us, trust me."
            the_person "God, I know. I'm trying to be rational here, not some lust-driven animal, okay?"
            "She huffs and puffs, looking at you with a slightly frustrated expression."
            the_person "Fine, no condom. Just remember to pull out, got it? Good. Don't make me regret this."
    return

label tomboy_underwear_nudity_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > 30 - (the_person.opinion.skimpy_outfits * 5):
        the_person "Gah, you want to see me in my underwear, huh? It's about time you asked, I guess."
        "She looks at you with a slightly playful expression, a hint of amusement in her eyes."
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "What are we waiting for then, let's get this off of you already."
            "She rolls her eyes and smirks at you."
            the_person "Fine, but don't say I didn't warn you, okay?"
        else:
            mc.name "Yeah, yeah. We've been over this. You're not exactly subtle about it, huh?"
            the_person "Shut up! I just don't want you to get the wrong idea, okay?"
            mc.name "Wrong idea? Like how you're not wearing anything under this, maybe?"
            the_person "Ugh, fine. But don't say I didn't warn you, got it?"

    elif the_person.love > 15:
        the_person "You want me to strip down a little? It's about time, I was wondering why you were taking things so slow, okay?"
        "She looks at you with a slightly playful expression, a hint of curiosity in her eyes."
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "Oh, don't give me that. You know you want to show off, huh?"
            the_person "Fine, but if this gets out of hand, I'm blaming you, got it?"
            mc.name "Promise?"
            the_person "Yeah, yeah. Now get this [the_clothing.display_name] off already."

        else:
            mc.name "Yeah, I know. You've been teasing me for weeks, okay?"
            the_person "Teasing? I'm just being friendly, huh?"
            mc.name "Right. Now let's get you out of these clothes."
            the_person "Ugh, fine. But don't think this means I'm going easy on you, got it?"
            "She slowly starts taking [the_clothing.display_name] off, a hint of hesitation in her movements."

    else:
        the_person "You really want to see me like this? Fine, but don't say I didn't warn you, okay?"
        the_person "If you take my [the_clothing.display_name] I'll only have my underwear on, you know that, right?"
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "Yeah, that's kind of the point, huh?"
            "She shakes her head and laughs to herself, a hint of nervousness in her expression."
            the_person "Whatever, but if you think I'm doing this because I want to... Ugh, never mind."
        else:
            mc.name "Yeah, I know. You're not exactly shy, okay?"
            the_person "Hey, I'm just being cautious. You can't blame a girl for being careful, right?"
            mc.name "Of course not. Now let's get you out of these clothes."
            the_person "Fine, but don't think this means I'm going easy on you, got it?"
    return

label tomboy_bare_tits_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > (40 - the_person.opinion.showing_her_tits * 5):
        the_person "Gah, why do you want to see my tits now, all of a sudden? Like I don't already know you're checking me out, huh?"
        "She looks at you with a slightly playful expression, a hint of amusement in her eyes."
        if the_person.has_large_tits:
            "She gives her chest a little shake, jiggling the [the_person.tits_description] hidden underneath her [the_clothing.display_name]."
        else:
            "She gives her chest a little shake and her [the_person.tits_description] a little jiggle, looking at you with a slightly teasing expression."
        the_person "You're always so eager, aren't you? I guess I can show you, but don't get too excited, okay?"
        if the_person.has_large_tits:
            mc.name "Oh, I've been looking. Now let's get those puppies out where I can enjoy them, huh?"
        else:
            mc.name "Oh, I've been looking. Now let's get those cute little things out, okay?"

    elif the_person.love > 25:
        the_person "Are you really sure you want to see my tits, [the_person.mc_title]? I mean, I know you've been staring and all..."
        "She looks at you with a slightly playful expression, a hint of curiosity in her eyes."
        if the_person.has_large_tits:
            "She rolls her eyes and gives her chest a little shake, jiggling her nice [the_person.tits_description], barely restrained by her [the_clothing.display_name]."
        else:
            "She rolls her eyes and gives her chest a little shake, giving her [the_person.tits_description] a little jiggle."
        mc.name "Of course I am. You know I love your tits, okay?"
        the_person "Well, I suppose you're entitled to see them then... but don't think this means I'm going to start showing them off to everyone, got it?"

    else:
        the_person "Wait, no! Don't look at me like that! You should at least ask a girl before you try and put her tits on full display, okay?"
        "She looks at you with a slightly annoyed expression, a hint of embarrassment in her eyes."
        mc.name "Come on, don't be like that. I bet your tits look great, huh?"
        the_person "They do, but I still feel a little self-conscious about being naked around you, alright? It's not exactly my thing."
        mc.name "There's no need to be. Just relax and let me take your [the_clothing.display_name] off for you, okay?"
        the_person "Ugh, fine... but don't think this means I'm going to start showing off my body to everyone, got it?"
    return

label tomboy_bare_pussy_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > (50 - the_person.opinion.showing_her_ass * 5):
        the_person "Gah, so you want to see my pussy, huh? Like I don't already know you're thinking about it, okay?"
        "She looks at you with a slightly playful expression, a hint of amusement in her eyes."
        if the_person.has_taboo("touching_vagina"):
            "She reluctantly lifts her hips, allowing you to slowly remove her [the_clothing.display_name] and reveal her pussy, a hint of hesitation in her movements."
        else:
            "She lifts her hips, giving you a quick glimpse of her pussy before covering it back up, a slightly teasing expression on her face."
        the_person "Well, you got your wish. Don't say I didn't warn you, got it?"

    elif the_person.love > 35:
        the_person "You want to see my pussy, really? Are you sure you're ready for that, huh?"
        "She looks at you with a slightly curious expression, a hint of uncertainty in her eyes."
        if the_person.has_taboo("touching_vagina"):
            mc.name "I think I am. I've been wanting to see it for a while, okay?"
            the_person "Hmm, well... I suppose you've earned it. Just remember, you asked for this, got it?"
        else:
            mc.name "I've already felt it up, I thought I should see it too, huh?"
            the_person "You really are persistent, aren't you? Fine, go on then. But don't think this means I'm going to start showing it off to everyone, okay?"

    else:
        the_person "Hold on, you're not getting me out of my [the_clothing.display_name] that easily, okay?"
        "She looks at you with a slightly annoyed expression, a hint of embarrassment in her eyes."
        if the_person.has_taboo("touching_vagina"):
            mc.name "Come on, just let me see it. I promise I'll be gentle, okay?"
            the_person "You're such a liar... But fine, go ahead. Just don't expect me to be all smiles and rainbows about it, got it?"
        else:
            mc.name "I've already felt your pussy up, I want to get a look at it now, huh?"
            the_person "You're so pushy! Alright, but don't say I didn't warn you. And don't think this means I'm going to start letting you do whatever you want, okay?"
    return

# label tomboy_facial_cum_taboo_break(the_person):

#     return

# label tomboy_mouth_cum_taboo_break(the_person):

#     return

# label tomboy_body_cum_taboo_break(the_person):

#     return
#==================================================================

label tomboy_creampie_taboo_break(the_person):
    if the_person.wants_creampie:
        if the_person.knows_pregnant:
            the_person "Gah, you want to get me pregnant, huh? Fine, I suppose it's about time someone knocked me up, okay?"
            "She shrugs and looks at you with a slightly resigned expression, a hint of amusement in her eyes."

        elif the_person.on_birth_control:
            if the_person.has_significant_other:
                the_person "Oh my god, I'm such a horrible [the_person.so_girl_title]! But I needed this so badly, okay?"
                the_person "Maybe if we're lucky, my [the_person.so_name] won't find out and freak out on me."
                "She looks at you with a mischievous grin, a hint of excitement in her eyes."
            else:
                the_person "Oh my god, I needed this so badly! Ah... I guess I'll just have to deal with the consequences, huh?"

        elif the_person.effective_sluttiness() > 75 or the_person.opinion.creampies > 0:
            if the_person.has_significant_other:
                the_person "You want to get me pregnant? Fine, I suppose it's about time someone knocked me up, okay?"
                the_person "Maybe my [the_person.so_name] will finally notice how unhappy I am and do something about it, huh?"

            else:
                the_person "You want to get me pregnant? Fine, I suppose it's about time someone knocked me up, okay?"
                the_person "I guess I'll just have to deal with the consequences, whatever they are."

            "She sighs happily, but with a hint of annoyance, looking at you with a slightly playful expression."
            the_person "How long until you're ready for round two? I want as much of your cum inside my pussy as possible, okay?"
            the_person "Just don't expect me to be all happy and grateful about it, got it?"

        else:
            if the_person.has_significant_other:
                the_person "Oh fuck... I'm such a terrible [the_person.so_girl_title], okay?"
                "She sighs happily, but with a hint of guilt, looking at you with a slightly nervous expression."
                the_person "But that felt so good, I guess I can forgive myself this time."
            else:
                the_person "Oh fuck, that was so risky, okay?"
                "She sighs happily, but with a hint of annoyance, looking at you with a slightly playful expression."
                the_person "But it felt so good, I guess I'll just have to deal with the consequences, huh?"
            the_person "I'll just have to hope you haven't knocked me up, okay? We really shouldn't do this again, my luck is going to run out at some point."
            the_person "Besides, I'm not exactly thrilled about the idea of being tied down to a man right now, got it?"

    else:
        if the_person.knows_pregnant:
            the_person "Ugh, you're kidding me, right? You got me pregnant, okay?"

        elif not the_person.on_birth_control:
            the_person "Seriously? You didn't even use protection? What if I get pregnant, huh?"

            if the_person.has_significant_other:
                the_person "What if you just got me pregnant? I would be the worst [the_person.so_girl_title] of all time, okay?"

            else:
                the_person "What if I get pregnant? I'm not ready for that kind of responsibility, okay?"
            the_person "You'd better start buying me chocolate and flowers to make up for this, got it?"
            the_person "Next time, we're using condoms, or we're not doing it at all, okay? You got it?"

        elif the_person.has_significant_other:
            the_person "Did you really just creampie me after I told you to pull out, okay?"
            "She sighs unhappily, looking at you with a slightly annoyed expression."
            the_person "God, I'm such a terrible [the_person.so_girl_title]. Maybe next time I'll make you wear a condom as punishment, huh?"

        elif the_person.opinion.creampies < 0:
            the_person "Ugh, this is so unpleasant, okay? Couldn't you have at least made it worth my while, huh?"
            "She rolls her eyes and looks at you with a slightly annoyed expression."
            the_person "Next time, at least have the decency to ask if I'm in the mood for a creampie, okay? Or better yet, don't even bother if you're just going to be careless like this."
            the_person "Next time, ask me first if I want a baby, got it?"

        else:
            the_person "Are you serious right now, okay? You're really going to give me that attitude after you just...you know, huh?"
            "She huffs and crosses her arms, looking at you with a slightly annoyed expression."
            the_person "I swear, you're going to be the death of me, okay? Fine, next time, at least have the decency to clean up after yourself, got it?"
    return

label tomboy_anal_creampie_taboo_break(the_person):
    if the_person.opinion.anal_creampies > 0:
        if the_person.effective_sluttiness() > 75 or the_person.opinion.anal_creampies > 1:
            if the_person.has_significant_other:
                the_person "Gah, fine. I won't tell my [the_person.so_title] about this. But don't think I'm enjoying this or anything, okay?"
                "She says this while wincing in pleasure as you fill her ass with your cream, a hint of a smile on her face."
                the_person "Ugh, it's just... weirdly satisfying, I guess. Don't tell anyone I said that, got it?"
            else:
                the_person "Ugh, finally! You're actually doing this! I've been waiting for this forever, okay?"
                the_person "Okay, okay, I know it's wrong, but... it feels so good, I guess. Don't judge me, okay?"
            "She bites her lip, trying to contain her excitement, her eyes sparkling with amusement."
            the_person "I guess it's nice... having your cum in my ass, okay? Don't think this means I'm going to start doing this all the time, though."
        else:
            if the_person.has_significant_other:
                the_person "Ugh, what are you doing? My [the_person.so_title] is going to kill me if he finds out about this, okay?"
                "She moans softly as you continue to fill her ass, a hint of guilt in her expression."
                the_person "Ugh, I don't know why I'm letting you do this... It's just so taboo, I guess."
            else:
                the_person "Ugh, promise you'll do this again? I don't know why I'm saying this, but... it's kind of hot, okay?"
                the_person "All that cum in my tight little ass... Yeah, that's definitely a thing now."

    else:
        if the_person.has_significant_other:
            the_person "Ugh, seriously? You couldn't pull out? My [the_person.so_title] is going to kill me, okay?"
            "She starts to squirm and try to get away from you, a hint of panic in her expression."
            the_person "Next time, just shoot your load on my ass, okay? Don't make me have to deal with this crap."
        elif the_person.opinion.anal_creampies < -1:
            the_person "Ugh, seriously? You can't even follow simple instructions? My ass is not a creampie dispenser, got it?"
            "She looks at you with a slightly annoyed expression, a hint of frustration in her eyes."
        else:
            the_person "Ugh, not inside! My ass is not a dirty little secret, although that sounds kind of hot, okay?"
            "She looks at you with a slightly playful expression, a hint of amusement in her eyes."
    return

label tomboy_dual_penetration_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 75:
        the_person "Gah, why do you always have to push me to do this stuff? Fine, but don't expect me to be all smiles and rainbows about it, okay?"
        "She rolls her eyes and crosses her arms, clearly annoyed but still willing to go through with it, a hint of a smirk on her face."
        mc.name "Don't worry, it'll be worth it, I promise."
        the_person "I doubt that, but whatever. Just don't say I didn't warn you, got it?"

    elif the_person.love >= 60:
        the_person "You're really sure about this? It's going to be a tight fit, okay?"
        mc.name "I'll make sure it fits perfectly, don't worry."
        the_person "Ugh, just be careful not to hurt me, okay? I don't want any scars or anything, got it?"
        "She looks at you with a slightly nervous expression, a hint of uncertainty in her eyes."

    else:
        if the_person.has_taboo("vaginal_sex"):
            the_person "Are you sure my pussy wouldn't be tight enough for you? I mean, I've never done this before, okay?"
            mc.name "It's okay, I'll make it fit. Just try to relax, okay?"
            the_person "Ugh, this is so embarrassing... I don't know why I'm doing this, got it?"
            "She looks at you with a slightly embarrassed expression, a hint of hesitation in her eyes."

        else:
            the_person "Ugh, fine. I guess we're doing this, right? I mean, I can't back out now, okay?"
            mc.name "Are you sure you're ready for this?"
            the_person "Yeah, whatever. Let's just get this over with, okay? I'm not exactly thrilled about this, got it?"
            "She looks at you with a slightly annoyed expression, a hint of frustration in her eyes."

    return

label tomboy_sleepover_yourplace_response(the_person): #Invited her over to spend the night
    if the_person.love >= 70:
        the_person "Ugh, fine. I'll come over. But don't expect me to be all lovey-dovey or anything, okay? I'm not exactly the cuddly type."
        mc.name "I wouldn't dream of it. We'll just have a good time, okay?"
        the_person "Yeah, yeah. Just don't get too close, okay? I don't like cuddling or anything, got it?"
        "She looks at you with a slightly playful expression, a hint of amusement in her eyes."

    elif the_person.sluttiness >= 80:
        the_person "Oh god, I'm so down for this. Make sure you have everything ready, so we can have a great night, okay?"
        "She looks at you with a slightly excited expression, a hint of anticipation in her eyes."

    else:
        the_person "I guess I could come over... But don't expect me to do anything I'm not comfortable with, okay? I'm not exactly looking for anything serious, got it?"
        "She looks at you with a slightly cautious expression, a hint of uncertainty in her eyes."
    return

label tomboy_sleepover_herplace_response(the_person): #Spending the night at her place
    if the_person.love >= 70:
        the_person "Gah, fine. Come over and stay the night, but don't expect me to be all mushy or anything, okay?"
        "She rolls her eyes and looks at you with a slightly playful expression, a hint of amusement in her eyes."
        mc.name "I wouldn't dream of it. We'll just have a good time, okay?"
        the_person "Yeah, yeah. Just don't get too close, okay? I don't do cuddles or anything, got it?"

    elif the_person.sluttiness >= 80:
        the_person "Oh man, I'm so down for this. Make sure you're ready for a wild night, okay?"
        "She looks at you with a slightly excited expression, a hint of anticipation in her eyes."

    else:
        the_person "I guess you can come over... But don't expect me to do anything I'm not cool with, okay?"
        "She looks at you with a slightly cautious expression, a hint of uncertainty in her eyes."
    return

label tomboy_sleepover_yourplace_sex_start(the_person):
    "[the_person.title] rolls her eyes and walks over to you, her expression a mix of annoyance and desire, a hint of a smirk on her face."
    the_person "Ugh, fine. Let's get this over with already. Just don't expect me to be all lovey-dovey or anything, okay?"
    "She looks at you with a slightly playful expression, a hint of amusement in her eyes."
    return

label tomboy_sleepover_herplace_sex_start(the_person):
    the_person "Gah, finally. Get over here already, okay?"
    "She smirks and crosses her arms, clearly annoyed but still eager for the action to begin, a hint of excitement in her eyes."
    mc.name "Are you ready?"
    the_person "Hah! Like I need to be ready for this. Just get in here and do your worst, okay?"
    "She leans back on the couch, her legs spread wide in invitation, a hint of a smile on her face."
    the_person "Hurry up, I'm not getting any younger, okay? And don't think this means I'm going easy on you, got it?"
    return

label tomboy_sleepover_impressed_response(the_person):  #If you've made her cum a lot
    the_person "Gah, you're really freaking good at that... Don't expect me to admit it, but you're making me feel all sorts of crazy things, okay?"
    "She rolls her eyes and smirks, trying to hide her true feelings, a hint of a blush on her cheeks."
    mc.name "You want more?"
    the_person "Hmph, maybe. But don't think you've won me over or anything, got it? I can still handle more... I think."
    "[the_person.title] lies down in bed, her breathing still ragged from the previous rounds, a hint of exhaustion in her eyes."
    the_person "I might be able to go for another round... But don't get too excited, I'm not making any promises, okay? I'm not exactly a machine or anything."

    return

label tomboy_sleepover_good_response(the_person):  #If you've made her cum
    the_person "Ugh, fine. That wasn't too terrible, I suppose, okay?"
    "She rolls her eyes and smirks, trying to hide her true feelings, a hint of a smile on her face."
    mc.name "You want more?"
    $ the_person.draw_person(position = "missionary")
    the_person "Hmph, maybe. But don't think you've won me over or anything, got it? I can still handle more... I think."
    "[the_person.title] lies down in bed, her breathing still ragged from the previous round, a hint of anticipation in her eyes."
    the_person "Could you give me another pounding before we go to sleep? But don't expect me to be all lovey-dovey or anything, okay? I'm not exactly the cuddly type."

    return

label tomboy_sleepover_bored_response(the_person):  #If she hasn't cum yet
    the_person "Ugh, is that the best you can do? I was expecting more than that from you, okay? You're not exactly setting the world on fire here."
    "She crosses her arms and looks at you with a bored expression, clearly unimpressed, a hint of disappointment in her eyes."
    mc.name "What's wrong?"
    the_person "You know, just do better, okay? I expect more from you than this... mediocrity."
    "She rolls her eyes and smirks, still rubbing her pussy in anticipation, a hint of frustration in her movements."
    the_person "You'd better step it up if you want to keep me interested, got it? I'm not exactly known for my patience."

    return



# add more tomboy personality, use different words, and movements.
# update all the following the_person and movements with tomboy personality. Use Juno MacGuff from Juno or Wendy Corduroy from Gravity Falls, for ideas, keep to the structure. Movements in quotations:
### DIALOGUE ###

