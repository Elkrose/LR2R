### PERSONALITY CHARACTERISTICS ###
# Bimbo is slang for a conventionally attractive, sexualized naïve woman. The term was originally used in the United States as early as 1919 for an unintelligent or brutish man. As of the early 21st century, the "stereotypical bimbo" appearance became akin to that of a physically attractive woman.
#However, as with most identities, the idea of the 'bimbo' has evolved and here is what it means today. The term 'bimbofication' is a colloquial term derived from the term 'bimbo' which is understood to mean, 'an attractive woman who is pretty, sexualised, naive and uneducated'.
#==================================================================
# add more cosplay personality, use different words, and movements.
# update all the following the_person and movements with cosplay personality. Use Marin Kitagawa from My Dress-Up Darling or Lilysa Amano from 2.5 Dimensional Seduction, for ideas, keep to the structure. Movements in quotations:
### DIALOGUE ###

label cosplay_introduction(the_person):
    mc.name "Hey, can I talk to you for a sec? I love your cosplay outfit!"
    "[the_person.title] turns around, a look of mild annoyance on her face as she adjusts her wig and shoves her hands into her pockets."
    the_person "What's up? Don't tell me you're another one of those creepy otakus who can't tell the difference between reality and fantasy."
    mc.name "I'm sorry if this is awkward, but you seem like an interesting person. I love your creativity and passion for cosplay."
    "[the_person.title] raises an eyebrow, a hint of a smirk on her lips as she leans against the wall, striking a pose."
    the_person "Interesting? Yeah, I get that a lot. Usually from people who don't know what to make of me and my love for dressing up."
    mc.name "Well, I was wondering if you'd like to... collaborate on a cosplay project together sometime. I've always wanted to try my hand at prop-making."
    "[the_person.title] snorts, a dry laugh escaping her lips as she shakes her head, her ponytail bouncing behind her."
    the_person "You mean, like, a cosplay date or something? No thanks. I'm not really into that sort of thing. But a collaboration sounds like fun, I guess."
    mc.name "Haha, no, I mean, if you're interested, we could maybe grab coffee and discuss some ideas for our next cosplay project."
    "[the_person.title] looks at you sideways, a small smile playing on her lips as she shrugs, her shoulders barely visible under her elaborate costume."
    the_person "I guess that sounds okay. But don't expect me to go all gooey on you or anything. I'm a cosplayer, not a romance novel heroine."
    mc.name "Heh, thanks? I'll take that as a compliment. I love your confidence and creativity."
    $ the_person.set_title()
    $ the_person.set_possessive_title()
    the_person "So, what's your name, anyway? And what's your favorite anime or manga series?"
    mc.name "I'm [mc.name]. Nice to meet you... I'm a big fan of LR2R!"
    the_person "I'm [the_person.name]. Nice to meet you too, I guess. I love LR2R too! Maybe we can cosplay together sometime."
    $ the_person.change_happiness(1)
    return

label cosplay_greetings(the_person):
    if the_person.love < 0:
        the_person "Ugh, why do you always bother me for something? Can't you see I'm busy perfecting my cosplay craft?"
    elif the_person.happiness < 90:
        the_person "Hi. I guess it's better than nothing, but I'm still having a rough day. My wig is frizzy, and my costume is malfunctioning."
    else:
        if the_person.sluttiness > 60:
            if the_person.obedience > 180:
                the_person "Oh, it's you. What do you want, [the_person.mc_title]? Don't tell me you're here for more of my cosplay services... or something else entirely."
            else:
                the_person "Hey there, [the_person.mc_title]. Just remember, I'm only doing this because it's my passion for cosplay... and maybe because I like you a little bit."
        else:
            if the_person.obedience > 180:
                the_person "Hi, [the_person.mc_title]. What can I do for you? Do you need help with a cosplay project or something?"
            else:
                the_person "Hey, what's up? Don't tell me you're here to bother me again... or to ask for cosplay advice. I'm happy to help, though!"
    return

label cosplay_sex_responses_foreplay(the_person):
    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] moans enthusiastically, clearly enjoying herself already, her eyes sparkling with excitement behind her cosplay mask."
            the_person "Hmph, fine. You're not too terrible at this, I suppose. But don't think you can just 'level up' with me that easily."
        else:
            "[the_person.possessive_title!c] moans happily to herself, her hands instinctively adjusting her cosplay outfit."
            the_person "I suppose this is okay, I guess. But don't expect me to go all 'dere' on you just yet."
    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            the_person "You know, this is almost decent. Don't get too cocky, though. I'm still the one in control here, even if I am in costume."
        else:
            the_person "I mean, it's not bad. You're not completely useless, I suppose. But don't think you can just 'win me over' with a few clever moves."
    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            the_person "Oh, all right. I suppose you're doing something right. But don't think this means I owe you anything, or that I'll start calling you 'senpai' anytime soon."
        else:
            the_person "Alright, alright. You're doing it right. But don't expect me to be all mushy about it, or to start wearing a ' Property of [mc.name]' sign on my cosplay outfit."
    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "Mmm, I suppose you're getting the hang of this. But don't think this means I'm going to be your little plaything, or that I'll start doing ' requests' for you anytime soon."
        else:
            the_person "You're doing alright, [the_person.mc_title]. But don't expect me to be all affectionate about it, or to start writing 'I [mc.name]' in my notebook."
    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                the_person "Oh, fine. You're getting close to making me cum. But don't think this means I'm going to fall for you, or that I'll start calling you 'my hero' anytime soon."
            else:
                the_person "The way you touch me is just... different, I guess. But don't think this means I've forgiven you for being such a nuisance, or that I'll start wearing a 'forgiveness' cosplay outfit anytime soon."
        else:
            the_person "Alright, you're almost there. But don't expect me to be all happy and stuff about it, or to start skipping around in a 'yay, I'm so happy' cosplay routine."

    return

label cosplay_sex_responses_oral(the_person):
    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] blinks, a hint of embarrassment on her face, her cosplay mask slightly askew."
            the_person "U-uh, you really don't have to, [the_person.mc_title]... I mean, I'm not exactly sure this is part of the script..."
        else:
            "[the_person.possessive_title!c] looks up at you, her cheeks flushed, her eyes sparkling with a mix of excitement and nervousness."
            the_person "Y-you don't have to, but... if you want to... I mean, I guess it's not every day I get to play the role of 'damsel in distress'..."

    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            the_person "Mmm, I guess it wouldn't hurt... and it might even add to the cosplay experience..."
        else:
            the_person "Oh, you really want to? Fine... but don't think this means I'm going to start calling you 'master' or anything..."

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            the_person "Hmph, well, if you insist... I suppose it's all part of the show, after all..."
            "[the_person.possessive_title!c] lets out a small sigh, her body slightly relaxing, her cosplay outfit rustling softly."
        else:
            the_person "Alright, but don't think I'm doing this because I want to... I'm just trying to get into character, that's all..."

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "Mmm, you know, maybe this isn't so bad... and it's definitely adding to the cosplay experience..."
        else:
            the_person "Hmph, you're pretty good at this, I'll give you that... but don't think this means I'm going to start wearing a ' Property of [mc.name]' sign on my cosplay outfit..."

    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                the_person "Oh, wow... I didn't know you could do that... I mean, I've never had anyone make me feel like this before, even in cosplay..."
            else:
                the_person "Mmm, maybe I should let you do that more often... when [the_person.so_title] isn't around, of course... and only if it's part of the cosplay script, naturally..."
        else:
            the_person "Ugh, fine, but don't think I'm enjoying this... I'm just doing this because it's part of the show, that's all..."

    return

label cosplay_sex_responses_vaginal(the_person):
    if the_person.energy < 10:
        call low_energy_sex_responses_vaginal(the_person) from _vt_cosplay_call_low_energy_sex_responses_vaginal_10
        return
    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            $ play_moan_sound()
            "[the_person.possessive_title!c] moans and wiggles her hips with your cock inside her, her cosplay outfit rustling softly."
            the_person "You're not bad, I guess. My pussy feels alright... but don't think this means I'm going to start calling you 'master' or anything."
        else:
            "[the_person.possessive_title!c] bites her lip and stifles a moan, her eyes sparkling with a mix of excitement and nervousness."
            the_person "I-I think I'm getting into character... but don't think this means I'm enjoying this or anything."

    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            the_person "Fine, you can keep going if you want. But don't expect me to thank you or anything... I'm just doing this for the cosplay experience, after all."
        else:
            the_person "Ugh, I guess your cock is alright... but don't think this means I'm going to start wearing a ' Property of [mc.name]' sign on my cosplay outfit."

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            the_person "Mmm, I suppose you're not completely terrible at this... but don't think this means I'm going to start calling you 'senpai' or anything."
        else:
            the_person "Hmm, your cock is okay, I suppose... but don't think this means I'm going to start doing 'requests' for you anytime soon."

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "You're not the worst, I guess. Keep going and maybe I'll...you know, finish or something... but don't think this means I'm going to start wearing a 'forgiveness' cosplay outfit anytime soon."
        else:
            the_person "Fine, keep doing what you're doing. It's not like I have anything better to do... but don't think this means I'm enjoying this or anything."

    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                the_person "Ugh, I guess I'm close. But don't think this means I'm impressed or anything... I'm just doing this for the cosplay experience, after all."
            else:
                the_person "Yeah, whatever. You're stretching me out, but it's not like it means anything... I'm just playing the role, after all."
                the_person "Just finish and get it over with... I have a cosplay photoshoot to get to, after all."
        else:
            the_person "Hmph, I suppose I'm almost there. But don't think I'm enjoying this or anything... I'm just doing this because it's part of the show, that's all."
            the_person "Just finish and let's get this over with... I have a cosplay costume to change into, after all."
    return

label cosplay_sex_responses_anal(the_person):
    if the_person.energy < 10:
        call low_energy_sex_responses_anal(the_person) from _vt_cosplay_call_low_energy_sex_responses_anal_10
        return

    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            the_person "Ugh, fine. But don't expect me to be all smiles about it... I'm only doing this because it's part of the cosplay script, after all."
            "She huffs and puffs, clearly not thrilled about the situation, but still trying to maintain her character."
        else:
            $ the_person.call_dialogue("annoyed_exclaim")
            the_person "Oh, great. Just what I always wanted: a big, thick cock up my ass... said no one ever, especially not in a cosplay scenario."
            "She grumbles to herself, clearly unenthusiastic, but still trying to play along with the role."

    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            $ the_person.call_dialogue("surprised_exclaim")
            the_person "Wow, this is... different. I didn't know being a cosplay character could be so... interesting."
            "She squirms a bit, trying to get used to the sensation, but still maintaining her character's personality."
        else:
            the_person "Ugh, this is so uncomfortable... I think I need to adjust my cosplay outfit, it's getting in the way."

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            the_person "Okay, okay. You can keep going. But don't think this means I'm going to start calling you 'master' or anything... I'm still in charge here, even if I am in costume."
            "She grits her teeth, trying to keep up the appearance of being tough, but still enjoying the role-play."
        else:
            the_person "Why do you have to be so rough?! Can't you see I'm trying to get into character here?"

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            if mc.condom:
                the_person "Just get it over with already... I have a cosplay photoshoot to get to, after all."
            else:
                the_person "Ugh, you really want to do this raw, huh? I guess it's all part of the cosplay experience, but still..."
        else:
            the_person "Why do you always have to be so insistent? Can't you see I'm trying to play the role of a strong, independent cosplay character here?"

    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                the_person "Fine, I'll cum... but don't think this means I like it! I'm just doing this for the cosplay experience, after all."
            else:
                the_person "You're just like my [the_person.so_title], always trying to get me to cum... I guess it's all part of the cosplay script, but still..."
                "She sighs, resigned to her fate, but still trying to maintain her character's personality."
        else:
            $ the_person.call_dialogue("annoyed_exclaim")
            the_person "Great, just what I needed: another orgasm... said no one ever, especially not in a cosplay scenario."
            "She mutters to herself, clearly not thrilled about the prospect, but still trying to play along with the role."

    return

label cosplay_climax_responses_foreplay(the_person):
    if the_person.sluttiness > 50:
        the_person "Oh, stop being so annoying and just make me cum already! I have a cosplay photoshoot to get to, after all!"
        "She taps her foot impatiently, clearly on the verge of climax."
    else:
        the_person "Why do you always have to make this so difficult? Can't you see I'm trying to get into character here?"
        "She huffs, clearly on the verge of climax, her cosplay outfit rustling softly."
    return

label cosplay_climax_responses_oral(the_person):
    if the_person.sluttiness > 70:
        the_person "Why do you have to be so good at that? Fine, I'll cum! But don't think this means I'm going to start calling you 'master' or anything."
        "She rolls her eyes, trying to play it cool despite her obvious pleasure."
    else:
        the_person "You're really good at that... I didn't think I'd... I'm going to cum... Oh no, I hope I don't ruin my cosplay makeup!"
        "She covers her mouth, trying to stifle her moans of pleasure."
    return

label cosplay_climax_responses_vaginal(the_person):
    if the_person.sluttiness > 70:
        if the_person.arousal_perc > 120:
            the_person "Fine, I'll cum. But don't think this means I'm enjoying myself. I'm just doing this for the cosplay experience, after all."
            "She shrugs, trying to play it cool despite her obvious pleasure."
        else:
            the_person "Ugh, just a little more... I'm... Ah, fuck! My cosplay outfit is getting all messed up!"
            "She grits her teeth and squeezes her eyes shut, her body shaking with pleasure."
    else:
        the_person "Oh... I can't... I'm going to... Ah! I hope I don't get any stains on my cosplay costume!"
        "She throws her head back, her body arched in pleasure."
    return

label cosplay_climax_responses_anal(the_person):
    if the_person.sluttiness > 70:
        if the_person.arousal_perc > 120:
            the_person "Fine, you win. I'll cum. But don't think I'm doing this because I want to. I'm just doing it for the cosplay script, after all."
            "She smirks, trying to play it cool despite her obvious pleasure."
        else:
            the_person "Ugh, just a little more... My ass is going to... Ah! I hope I don't get any tears in my cosplay outfit!"
            "She squeezes her eyes shut, trying to fight off the pleasure, her body shaking with release."
    else:
        the_person "Oh... My... Ass... I... Ah! This is all part of the cosplay experience, right?"
        "She barely finishes her sentence before her body is racked with pleasure, her cosplay outfit rustling softly."
    return

label cosplay_clothing_accept(the_person):
    if the_person.obedience > 180:
        the_person "Whatever, just don't think you're making me into some kind of slutty fashion model. I'm a cosplayer, not a fashionista."
        "She rolls her eyes, but still strikes a pose, showing off her new outfit."
    else:
        the_person "Yeah, whatever. Just don't expect me to go around looking like a total slut. I have a reputation to uphold as a cosplayer, after all."
        "She smirks, adjusting her cosplay outfit, making sure everything is in place."
    return

label cosplay_clothing_reject(the_person):
    if the_person.should_wear_uniform:
        the_person "Hey, I guess I should get my cosplay uniform sorted out, right? One second. I don't want to be late for the photoshoot."
    elif the_person.obedience > 180:
        the_person "I don't... I'm sorry, but I really don't think I could get away with wearing something like this. It's not exactly part of my cosplay character's personality, you know?"
    else:
        if the_person.sluttiness > 60:
            the_person "Hmm, I don't know about this one. It's a bit too revealing for my taste... and it might ruin the whole cosplay aesthetic I'm going for."
        else:
            the_person "You've got to be kidding me, right? This is ridiculous. I'm not wearing this, it's not part of my cosplay script."
    return

label cosplay_clothing_review(the_person):
    if the_person.outfit.cum_covered:
        if (the_person.sluttiness > 40 and the_person.opinion.being_covered_in_cum >=0) or the_person.opinion.being_covered_in_cum > 0:
            the_person "Ugh, why do I always get so messy with you...? I guess I'll have to add 'clean-up' to my cosplay routine now."
            "[the_person.title] starts to wipe up the biggest splashes of cum on her, making sure not to ruin her cosplay outfit."
        else:
            the_person "For fuck's sake, I need to clean up this mess! Let me know if I've missed any, okay? I don't want to ruin my cosplay makeup."
            "[the_person.title] wipes herself down, cleaning up all the cum she can find, and then checks her cosplay outfit to make sure it's still intact."

    if the_person.obedience > 180:
        the_person "Fine, I'll be back in a moment. I need to get cleaned up for you... and make sure my cosplay outfit is still perfect."
    else:
        if the_person.sluttiness > 40:
            the_person "I don't know why I do this, but I want to look good for you... and for my cosplay character, of course. I'll be back in a second, I just want to get cleaned up and touch up my makeup."
        else:
            the_person "Ugh, everything's such a mess after that. Wait here a moment, I'm just going to find a mirror and try and look somewhat presentable... and make sure my cosplay outfit is still in one piece."
    $ the_person.apply_planned_outfit(show_dress_sequence = True)
    return

label cosplay_strip_reject(the_person, the_clothing, strip_type = "Full"):
    if the_person.obedience > 180:
        the_person "Hey, could we leave my [the_clothing.display_name] on for now, please? I'm still a little cold... and it's part of my cosplay character's personality, after all."
    elif the_person.obedience < 70:
        the_person "No, no, no, I'll decide what comes off and when, okay? Don't rush me! I'm the one in control of this cosplay scenario, after all."
    else:
        the_person "Not yet... I don't know if I'm ready to take off my [the_clothing.display_name]. Maybe we can try something else first? Like, I don't know, a different cosplay pose or something."
    return

label cosplay_strip_obedience_accept(the_person, the_clothing, strip_type = "Full"):
    "[the_person.title] laughs nervously as you start to slide her [the_clothing.display_name] away, but she doesn't stop you, too caught up in the cosplay moment."
    if the_person.obedience > 180:
        the_person "Alright, fine... I guess I can trust you with this. Just be gentle, I don't want to ruin my cosplay outfit."
    else:
        the_person "I don't know if this is a good idea, but I'll let you do it this once... just for the sake of the cosplay, of course."
    return

label cosplay_grope_body_reject(the_person):
    if the_person.effective_sluttiness("touching_body") < 5: #Fail point for touching shoulder
        the_person "Hmph! What do you think you're doing, senpai? Personal space, please!"
        "[the_person.title] steps back as you touch her, then crosses her arms over her chest, her cosplay outfit rustling softly."
        the_person "Just get your hands off me, okay? You're making me uncomfortable... and ruining the cosplay vibe."
        mc.name "Oh, sorry. I didn't mean to make you feel that way."
        the_person "Yeah, well, try to be more careful next time, alright? I'm trying to stay in character here."
        "She seems a little put off by the situation, but you both try to move on and put it behind you, for the sake of the cosplay."
    else: #Fail point for touching waist
        the_person "Hey, could you just... not touch me there, okay? It's not part of the script."
        "[the_person.title] takes your hand and pulls it off of her waist, giving you a warning look, her eyes sparkling with a mix of annoyance and amusement."
        the_person "... Keep your hands to yourself, got it? I'm trying to maintain my cosplay character's dignity here."
        mc.name "Oh yeah, of course. My bad."
        the_person "Just make sure you don't do it again, okay? I don't appreciate it... and it's not part of the cosplay scenario."
        "She doesn't say anything else, but you can tell she's still a bit annoyed about the situation, her cosplay outfit rustling softly as she adjusts it."
    return

label cosplay_sex_accept(the_person, the_position):
    if the_person.sluttiness > 70:
        if the_person.obedience < 70:
            the_person "Fine, let's do it. But don't think this means I'm going to put out every time you ask... or that I'm going to start calling you 'master' or anything."
        else:
            if the_position.skill_tag == "Foreplay":
                the_person "Oh, I've been wanting you to do that for a while now. Just thinking about it makes me wet... and it's perfect for the cosplay scenario."
            elif the_position.skill_tag == "Oral":
                if "getting head" in the_position.opinion_tags:
                    the_person "Ugh, I need this so badly. Suck my [pussy/clit] already, senpai!"
                else:
                    the_person "You're going down on me right now, and you're going to make me cum... just like in the anime."
            else:
                the_person "Get over here and fuck me already. I've been waiting for this... and it's going to be so much fun in this cosplay outfit."
    else:
        the_person "Come here, let's do it. But don't think I'm going to do this all the time, got it? This is just a special cosplay treat."
    return

label cosplay_sex_obedience_accept(the_person):
    if the_person.sluttiness > 70:
        the_person "Ugh, fine. I don't want to admit it, but you've gotten to me, senpai. Do whatever you want to me, [the_person.mc_title]... just for the sake of the cosplay, of course."
    else:
        if the_person.obedience > 180:
            the_person "Alright, I'll do what you say, but don't think this means I'm going to like it... or that I'm going to start calling you 'master' or anything."
        else:
            the_person "I shouldn't be saying this, but if you really want to... I'll give it a try. Just this once, okay? For the cosplay."
    return

label cosplay_sex_gentle_reject(the_person):
    if the_person.sluttiness > 50:
        the_person "Ugh, not like that, [the_person.mc_title]. I need a little more foreplay first... and maybe some more cosplay-themed teasing."
    else:
        the_person "No, no, no. I want to have fun, but I don't want to get too serious. Let's just keep it light... and in character, okay?"
    return

label cosplay_sex_angry_reject(the_person):
    if the_person.has_significant_other:
        the_person "What? Are you out of your mind? I have a [the_person.so_title], so you can forget about doing anything like that. Ever. And besides, it's not part of the cosplay script."
        "She glares at you and turns away, clearly offended, her cosplay outfit rustling softly."
    elif the_person.sluttiness < 20:
        the_person "Are you serious? You've got to be kidding me! Get away from me, I never want to see you like this again! This is totally not what I signed up for when I agreed to cosplay with you."
        "[the_person.title] glares at you and takes a step back, her face red with anger, her eyes sparkling with a mix of annoyance and amusement."
    else:
        the_person "What? Are you out of your mind? You can't be serious! Get away from me, I'm not interested in anything like that. And besides, it's not part of the cosplay scenario we agreed on."
        "[the_person.title] glares at you and steps back, her face showing clear disapproval, her cosplay outfit rustling softly as she adjusts it."
    return

label cosplay_seduction_response(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 50:
            the_person "Oh, I think I know what you need right now, senpai. Let me take care of you... and get into character."
        else:
            the_person "Okay, I'll give you a few minutes. But don't think this means I'm going to be your slave or anything... or that I'm going to start calling you 'master' or anything like that."
    else:
        if the_person.sluttiness > 50:
            the_person "Mmm, you're feeling as horny as me then? Come on, let's go find a place to get out of sight... and get into character."
            "[the_person.title] takes your hand and leads you off to find some place private, her cosplay outfit rustling softly as she moves."
        elif the_person.sluttiness > 10:
            the_person "I know that look you're giving me, I think I know what you want, senpai. But don't expect me to give it up that easily... I'm a cosplayer, not a sex object."
        else:
            the_person "[mc.name], I know what you mean... Okay, I can spare a few minutes. But don't get your hopes up, I'm only doing this for the sake of the cosplay."
    return

label cosplay_seduction_accept_crowded(the_person):
    if not the_person.has_significant_other:
        if the_person.sluttiness < 20:
            the_person "Alright, let's sneak away for a few minutes and you can convince me a little more... but just for the sake of the cosplay, okay?"
        elif the_person.sluttiness < 50:
            the_person "Come on, I know someplace nearby where we can get a few minutes privacy... and get into character. Just make it quick, I don't want to ruin the cosplay vibe."
        else:
            the_person "Oh, I don't know if I can wait much longer, senpai... I'm so turned on just thinking about the cosplay scenario."
    else:
        if the_person.sluttiness + (5*the_person.opinion.cheating_on_men) > 50:
            the_person "Fuck it, let's do this! I don't care about my [the_person.so_title] right now, I just want to get into character and have some fun."
            the_person "I hope you don't mind that I've got a [the_person.so_title], but I don't care right now... I'm just a cosplayer, after all."
        else:
            the_person "Ugh, you're bad for me, senpai... Come on, we need to find somewhere quiet so my [the_person.so_title] doesn't catch us... and ruin the cosplay vibe."
    return

label cosplay_seduction_accept_alone(the_person):
    if not the_person.has_significant_other:
        if the_person.sluttiness < 20:
            the_person "Alright, you've got one chance to impress me, senpai... but just for the sake of the cosplay, okay?"
        elif the_person.sluttiness < 50:
            the_person "Come on, let's get this over with and see if you're any good... at cosplay, that is."
        else:
            the_person "Fuck, I'm so turned on right now just thinking about the cosplay scenario. Just do me already, senpai!"
    else:
        if the_person.sluttiness + (5*the_person.opinion.cheating_on_men) > 50:
            the_person "You know I shouldn't be doing this with you, but fuck it, senpai. Let's do this! I'm a cosplayer, not a saint."
        else:
            the_person "You're trouble, senpai, but I can't help myself. Come here... and let's get into character."
    return

label cosplay_seduction_refuse(the_person):
    if the_person.sluttiness < 20:
        the_person "Ugh, why are you always trying to flirt with me, [mc.name]? I'm just not in the mood for this right now, okay? Can't you see I'm trying to get into character here?"
        "[the_person.title] folds her arms and looks away, her cosplay outfit rustling softly."
    elif the_person.sluttiness < 50:
        the_person "Fine, I'll admit you're kind of cute, but don't think this means I'm actually interested. I just don't feel like messing around right now, okay? Maybe some other time, when I'm in a better mood... and when I'm not in the middle of a cosplay photoshoot."
        "[the_person.title] playfully pokes [mc.name]'s chest with her finger, her eyes sparkling with a mix of amusement and annoyance."
    else:
        the_person "Eh, you're always trying to get me into bed, [mc.name], but I'm not going to make it easy for you. You'll have to wait until I'm good and ready to fool around... and until I've finished my cosplay project, of course."
        "[the_person.title] grins mischievously and walks away, leaving [mc.name] to wonder what she's thinking, her cosplay outfit rustling softly as she moves."
    return

label cosplay_compliment_response(the_person):
    mc.name "Hey [the_person.fname], you look really beautiful today. Is there a special occasion or something? Your cosplay outfit is amazing!"
    if the_person.is_at_work:
        if (the_person.is_employee or the_person.is_strip_club_employee) and the_person.is_wearing_uniform:
            call cosplay_flirt_response_employee_uniform_low(the_person) from _call_cosplay_flirt_response_employee_uniform_low_compliment_response
        elif the_person.is_at_job(prostitute_job):
            the_person "Ugh, why do you always want to hang out with me? Can't you see I'm busy trying to get into character?"
        elif the_person.sluttiness > 50:
            the_person "I'm doing great, thanks for asking. But don't think this means I'm actually interested in you or anything... I'm just here for the cosplay, after all."
        else:
            the_person "Oh, stop it, you're making me blush. There's no special occasion, I just felt like dressing up today... and trying out a new cosplay character."
    else:
        the_person "Well, I did put in a bit of extra effort today. You're just the first one to notice. But thanks, I guess... I'm just trying to get into character for my next cosplay project."
    "You try to press for more information, but [the_person.possessive_title] just smiles coyly and changes the subject, leaving you wondering what's going on... and what her next cosplay project is."
    return

label cosplay_compliment_response_girlfriend(the_person):
    mc.name "Hey [the_person.title]. You're looking very nice this [StringInfo.time_of_day_string]. Your cosplay outfit is amazing!"
    if the_person.is_at_work:
        if (the_person.is_employee or the_person.is_strip_club_employee) and the_person.is_wearing_uniform:
            call cosplay_flirt_response_employee_uniform_mid(the_person) from _call_cosplay_flirt_response_employee_uniform_mid_compliment_response_girlfriend
            $ the_person.call_dialogue("flirt_response_employee_uniform_mid")
        elif the_person.sluttiness > 50:
            the_person "Mmm, thank you, [the_person.mc_title]. Wanna find out how nice I am... in this cosplay outfit?"
        else:
            the_person "Hmph, really? Thanks, [the_person.mc_title]. You're not so bad yourself... but don't think this means I'm going to start calling you 'master' or anything."
    else:
        the_person "Ugh, don't be ridiculous. It's just a normal day... but thanks, I guess. I'm just trying to get into character for my next cosplay project."
        mc.name "Oh come on, don't be like that. You know you look great... and your cosplay skills are amazing."
        the_person "Aww, stop it, [the_person.mc_title]. You're making me blush... and a little annoyed at the same time. Can't you see I'm trying to focus on my cosplay?"
    "You chat with [the_person.possessive_title] for a while, and although she's initially annoyed by your compliments, she starts to warm up to you... and your appreciation for her cosplay skills."
    return

label cosplay_compliment_response_affair(the_person):
    mc.name "Hey [the_person.title]. You're looking absolutely amazing this [StringInfo.time_of_day_string]. Your cosplay outfit is stunning!"
    if the_person.is_at_work:
        if (the_person.is_employee or the_person.is_strip_club_employee) and the_person.is_wearing_uniform:
            call cosplay_flirt_response_employee_uniform_mid(the_person) from _call_cosplay_flirt_response_employee_uniform_mid_compliment_response_affair
        elif the_person.sluttiness > 50:
            the_person "Mmmm, thank you [the_person.mc_title], wanna go somewhere a little more private, so you can make me feel how amazing I am... in this cosplay outfit?"
        else:
            the_person "Hmph, really? Thanks, [the_person.mc_title]. You're not so bad yourself... but don't think this means I'm going to start calling you 'master' or anything."
    else:
        the_person "Ugh, don't be silly. It's just a normal day... but thanks, I suppose. I'm just trying to get into character for my next cosplay project."
        mc.name "Oh come on, don't be like that. You know you look great... and your cosplay skills are amazing."
        the_person "Aww, stop it, [the_person.mc_title]. You're making me blush... and a little annoyed. Can't you see I'm trying to focus on my cosplay?"
    "You keep chatting with [the_person.possessive_title] for a while, slipping in a few more compliments. She is quite charmed by your attentiveness... and your appreciation for her cosplay skills."
    return

label cosplay_flirt_response(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 50:
            the_person "Ugh, fine. You're not totally terrible, [the_person.mc_title]. I suppose you have a certain charm, especially when you're appreciating my cosplay skills."
        else:
            the_person "Whatever. Thanks for the compliment, [the_person.mc_title]. You're not a complete loser... and you seem to know a thing or two about cosplay."

    elif the_person.has_significant_other:
        if the_person.sluttiness + (the_person.opinion.cheating_on_men*5) > 50:
            the_person "Oh, you think you're so clever, don't you? I'll give you that. But don't think this means I'm going to start calling you 'master' or anything... I'm a cosplayer, not a slave."
            "[the_person.title] gives you a sly look, her eyes narrowing as she adjusts her cosplay outfit."
        else:
            the_person "You're really pushing your luck, [the_person.mc_title]. I have a [the_person.so_title] you know, and I'm not going to cheat on them just because you're being charming... even if you do appreciate my cosplay skills."
            mc.name "What about you, do you appreciate it?"
            "She rolls her eyes and crosses her arms, her cosplay outfit rustling softly."
            the_person "Maybe I do, maybe I don't. It's none of your business... but I will say that I'm flattered by your attention."

    else:
        if the_person.sluttiness > 50:
            the_person "Fine. Maybe you're worth my time, [the_person.mc_title]. You seem to know a thing or two about cosplay, and you're not completely terrible at flirting."
            "[the_person.title] gives you a half-smile, but her eyes remain guarded as she adjusts her cosplay outfit."
        else:
            the_person "Whatever. You're not unattractive, I suppose. But don't think that means I'll go easy on you... I'm a cosplayer, and I have high standards for my partners."
            the_person "You'll have to really impress me though, I have high standards... and I'm not just talking about your flirting skills, either."
    return

label cosplay_flirt_response_employee_uniform_low(the_person):
    if the_person.is_wearing_forced_uniform:
        the_person "Hmph, I suppose you like seeing me in this uniform... I mean, I'm practically naked! It's a bit embarrassing, but I suppose it's all part of the cosplay experience."
        mc.name "I know you don't like it, but I needed to make a point... and I have to say, you look amazing in that outfit."
        the_person "I know, I know. You always were one to make a point... and to appreciate a good cosplay outfit."
        $ mc.change_locked_clarity(5)
        "She crosses her arms over her chest, but can't hide the small smile on her face as she strikes a pose, showing off her cosplay outfit."

    elif the_person.judge_outfit(the_person.outfit):
        #She's in uniform and likes how it looks.
        the_person "Oh, you noticed? I thought it was a bit much, but I guess it's not so bad... especially since it's all part of the cosplay experience."
        the_person "I mean, it's nice to work somewhere where I can show off a little... and get into character, of course."
        $ mc.change_locked_clarity(5)
        "She winks at you, then turns to adjust her uniform, accentuating her hips and striking a pose."

    else:
        #She's in uniform, but she thinks it's a little too slutty.
        if the_person.vagina_visible:
            # Her pussy is on display.
            the_person "Hmph, I suppose you like seeing me like this... I mean, I'm practically naked! It's a bit embarrassing, but I suppose it's all part of the cosplay experience."
            mc.name "Well, you know that it's..."
            the_person "I know, I know. It's company policy... and all part of the cosplay scenario, of course."
            mc.name "Give it some time and you'll get used to it... and maybe even start to enjoy it."
            $ mc.change_locked_clarity(5)
            "She rolls her eyes, but doesn't argue, striking a pose to show off her cosplay outfit."

        elif the_person.tits_visible:
            # Her tits are out
            the_person "Ugh, I'm still getting used to being so... exposed in this uniform. At least I don't have to wear a bra! It's all part of the cosplay experience, I suppose."
            mc.name "You look incredible and you're comfortable. I call that a success... and a great cosplay outfit."
            $ mc.change_locked_clarity(5)
            "She huffs, but can't hide her smile as she adjusts her cosplay outfit."

        elif the_person.underwear_visible:
            # Her underwear is visible.
            the_person "Hmph, I probably would have picked something that kept me a little more covered, but at least our uniform is comfortable... and it's all part of the cosplay scenario, of course."
            mc.name "It may be a little unconventional, but you look fantastic. You've got exactly the right kind of body for it... and for this cosplay outfit."
            the_person "Well, that's one way to look at it, I suppose... and I have to admit, I do feel a bit more confident in this outfit."
            $ mc.change_locked_clarity(5)
            "She playfully rolls her eyes and turns to adjust her uniform, showing off her body and striking a pose."

        else:
            # It's just generally slutty.
            the_person "Ugh, well thank you! Our uniforms are a little bold for my taste, but I guess I look good in it... and it's all part of the cosplay experience, after all."
            $ mc.change_locked_clarity(5)
            "She blushes and looks away, but not before you catch a glimpse of her small smile as she adjusts her cosplay outfit."
    return

label cosplay_flirt_response_employee_uniform_mid(the_person):
    if the_person.is_wearing_forced_uniform:
        $ mc.change_locked_clarity(10)
        if the_person.vagina_visible:
            the_person "Ugh, fine. You caught me off guard, senpai. I'll admit, this uniform does make me look good, especially down here... but don't think this means I'm going to start calling you 'master' or anything."
            mc.name "It's a great uniform, but that's not what's important here. I just want to appreciate your cosplay skills."
            the_person "Yeah, yeah. You're right, senpai. It's just hard not to feel like a sex object in this thing, especially with my pussy on display... but I guess that's all part of the cosplay experience, right?"
        elif the_person.tits_visible:
            the_person "Ugh, fine. You caught me off guard, senpai. I'll admit, this uniform does make me look good, especially up here... but don't think this means I'm going to start wearing a ' Property of [mc.name]' sign on my cosplay outfit."
            mc.name "It's a great uniform, but that's not what's important here. I just want to appreciate your cosplay skills."
            the_person "Yeah, yeah. You're right, senpai. It's just hard not to feel like a sex object in this thing, especially with my boobs popping out... but I guess that's all part of the cosplay experience, right?"
        else:
            the_person "Ugh, fine. You caught me off guard, senpai. I'll admit, this uniform does make me look good... but don't think this means I'm going to start doing 'requests' for you anytime soon."
            mc.name "It's a great uniform, but that's not what's important here. I just want to appreciate your cosplay skills."
            the_person "Yeah, yeah. You're right, senpai. It's just hard not to feel like a sex object in this thing... but I guess that's all part of the cosplay experience, right?"
        mc.name "Rules are rules and I can't make any exceptions, even if they look good... but I do appreciate your cosplay skills, [the_person.fname]."
        "She sighs and nods, adjusting her cosplay outfit."
        the_person "Yeah, I know, senpai. At least you're having a good time. I don't mind that so much... and I'm glad you appreciate my cosplay skills."

    elif the_person.judge_outfit(the_person.outfit):
        $ mc.change_locked_clarity(10)
        if the_person.tits_visible:
            the_person "Hmph, maybe I should wear this outfit more often, senpai. It's getting a lot of attention, especially for my boobs... and I have to admit, I'm enjoying the attention."
            mc.name "It's a great outfit, but I'm more interested in the person wearing it... and your cosplay skills, of course."
            the_person "Oh, really, senpai? Is that so? I guess my boobs are hard to ignore... but I'm glad you appreciate my cosplay skills."
        else:
            the_person "Hmph, maybe I should wear this outfit more often, senpai. It's getting a lot of attention... and I have to admit, I'm enjoying the attention."
            mc.name "It's a great outfit, but I'm more interested in the person wearing it... and your cosplay skills, of course."
            the_person "Oh, really, senpai? Is that so? I guess my vagina is hard to ignore... but I'm glad you appreciate my cosplay skills."
        the_person "Maybe I'll invite you shopping one day and you can tell me what else you want to see me in, senpai... but don't think this means I'm going to start doing 'requests' for you anytime soon."
        mc.name "Sounds like a good time, [the_person.fname]. I'd love to see more of your cosplay outfits."

    else:
        # the_person "I think it shows off a little too much!"
        the_person "Ugh, fine, senpai. You're not gonna make this easy for me, are you? I'm trying to focus on my cosplay skills here, not flirt with you all day."
        $ mc.change_locked_clarity(10)
        if the_person.vagina_visible:
            the_person "I'm trying to focus on my work here, not flirt with you all day, senpai. And definitely not with my pussy on display... but I guess that's all part of the cosplay experience, right?"
        elif the_person.tits_visible:
            the_person "I'm trying to focus on my work here, not flirt with you all day, senpai. And definitely not with my boobs popping out... but I guess that's all part of the cosplay experience, right?"
        else:
            the_person "I'm trying to focus on my work here, not flirt with you all day, senpai! But I guess that's all part of the cosplay experience, right?"
        mc.name "I understand, [the_person.fname], but I promise it's important for the business... and I appreciate your cosplay skills, of course."
        "She sighs and nods, adjusting her cosplay outfit."
        the_person "Yeah, I know, senpai. You're a real pain, you know that? But I guess I can tolerate it for the sake of the cosplay."
    return

label cosplay_flirt_response_low(the_person):
    #She's in her own outfit.
    the_person "Hmph, I suppose it's not the worst outfit I've ever worn, senpai... but I'm not sure it's the best cosplay outfit, either."
    $ the_person.draw_person(position = "walking_away")
    $ mc.change_locked_clarity(5)
    "She rolls her eyes and gives you a quick spin, showing off her outfit from every angle, striking a pose to show off her cosplay skills."
    the_person "I mean, I guess it's not too bad, right, senpai? But I'm not sure it's the best cosplay outfit I've ever worn."
    $ the_person.draw_person()
    mc.name "I think it looks great on you, [the_person.fname]. You have a real talent for cosplay."
    the_person "Oh, shut up, senpai. You're just saying that to get on my good side... but I appreciate the compliment, anyway."
    return

label cosplay_flirt_response_low1(the_person):
    if the_person.has_significant_other:
        the_person "Ugh, what's with you and the flirting, senpai? I've got a [the_person.so_title], and I don't think he'd appreciate you getting all up in my grill... especially when I'm trying to get into character for my cosplay."
        mc.name "What about you, do you appreciate it?"
        "She rolls her eyes and smirks, adjusting her cosplay outfit."
        the_person "Maybe I do... but don't think you're getting anywhere with me that easily, senpai. I'm a cosplayer, not a sex object."
    else:
        the_person "Well, thanks for the compliment, senpai. But don't think you're getting off that easy. I have high standards, and you'll need to prove yourself to me... especially when it comes to my cosplay skills."
        the_person "But if you can impress me, who knows what might happen... maybe I'll even let you join me for a cosplay photoshoot."
    $ mc.change_locked_clarity(5)
    return

label cosplay_flirt_response_mid(the_person):
    if mc.location.person_count > 1 and the_person.effective_sluttiness("kissing") < (25 - (5*the_person.opinion.public_sex)):
        $ mc.change_locked_clarity(10)
        the_person "You know, I was wondering if you actually noticed my cosplay outfit today, senpai... I put a lot of effort into it."
        "Her eyes narrow slightly, but she's still trying to appear casual, striking a pose to show off her cosplay skills."
        mc.name "I noticed, [the_person.fname]. It looks great on you. You're really talented when it comes to cosplay."
        the_person "Oh, really, senpai? Thanks, I guess. I was thinking you might say something like that... but I'm glad you appreciate my cosplay skills."
        "She crosses her arms, trying to maintain a tough exterior, but can't help smiling at the compliment."
        if the_person.tits_visible:
            mc.name "I noticed, [the_person.fname]. It looks great on you. Especially your boobs... and your cosplay skills, of course."
            the_person "Oh, really, senpai? Thanks, I guess. I was thinking you might say something like that... but I'm glad you appreciate my cosplay skills."
            "She crosses her arms, trying to maintain a tough exterior, but can't help smiling at the compliment."
        else:
            mc.name "Well, it's true, [the_person.fname]. You look amazing... and your cosplay skills are top-notch."
        the_person "Hmph, maybe I'll invite you shopping one day, so you can tell me what else you want to see me in, senpai... but don't think this means I'm going to start doing 'requests' for you anytime soon."
        "She leans in slightly, a hint of flirtation in her voice, her eyes sparkling with amusement."
        mc.name "I can think of a few things already, [the_person.fname]... and I'm sure I'd enjoy seeing you in them. You're really talented when it comes to cosplay."
        the_person "I'm sure you would, senpai. So, what do you say? Want to take me out for a drink and maybe we can discuss my wardrobe some more... and my cosplay skills, of course?"

    else:
        the_person "Thanks, I thought I looked pretty hot in it too, senpai... and I'm glad you appreciate my cosplay skills."
        the_person "You want a better look, right, senpai? Here, how does it make my ass look?"
        $ the_person.draw_person(position = "back_peek")
        $ mc.change_locked_clarity(10)
        the_person "Good, right, senpai?"
        mc.name "Fantastic, [the_person.fname]. I wish I could get an even better look at it... and maybe even join you for a cosplay photoshoot."
        "[the_person.possessive_title!c] smiles and turns back to face you, striking a pose to show off her cosplay skills."
        $ the_person.draw_person()
        the_person "I'm sure you do, senpai. Take me out for a drink and maybe we can work something out... like a cosplay collaboration, perhaps?"
    return

label cosplay_flirt_response_mid1(the_person):
    $ mc.change_locked_clarity(10)
    the_person "Thanks, I do look amazing in this cosplay outfit, don't I, senpai?"
    if (the_person.has_skirt or the_person.has_dress) and not the_person.has_thigh_high_socks:
        mc.name "You could change it up with some high stockings, I would love to see that... it would really add to the cosplay aesthetic."
        the_person "Oh, really, senpai? And why would you want to see that? You're not going to get a peek or anything, are you... especially not during a cosplay photoshoot?"
        mc.name "Because it would look great on you, and I would enjoy the view... and I think it would really bring out the character in your cosplay."

    mc.name "How about you and me go and grab a coffee sometime, [the_person.fname]? Maybe we can discuss some new cosplay ideas."
    if the_person.has_significant_other:
        the_person "Sure, my [the_person.so_title] doesn't mind... as long as they're not around to witness how much fun we're going to have, senpai. But don't think this means I'm going to start doing 'requests' for you anytime soon."
    else:
        the_person "Why not, I could use a pick-me-up once in a while, senpai... and maybe someone to pick me up from the ground when I fall for you. But don't think I'm going to go easy on you just because we're going out for coffee."
    the_person "Just let me know when, I would love to... and don't think I won't notice if you're trying to get a glimpse of my legs under the table, senpai. I'm a cosplayer, not a sex object."
    mc.name "I'll keep that in mind, [the_person.fname], and maybe we can discuss what else you want to wear in the future... or not wear, for that matter. Maybe we can even plan a cosplay collaboration."
    the_person "Hmph, maybe, senpai. But don't think you're getting a discount on my wardrobe just because we're going out for coffee... or anything else. I'm a cosplayer, and I have standards to uphold."
    return

label cosplay_flirt_response_high(the_person):
    if mc.location.person_count > 1 and the_person.effective_sluttiness() < (25 - (5*the_person.opinion.public_sex)): # There are other people here, if she's not slutty she asks if you want to find somewhere quiet
        the_person "You're really persistent, huh, senpai? Fine, but not here... I don't want to ruin the cosplay vibe."
        "She glances around before giving you a sly smile, adjusting her cosplay outfit."
        menu:
            "Find somewhere more quiet\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                mc.name "Then let's find somewhere that isn't here, [the_person.fname]. Maybe we can find a quiet spot to discuss our next cosplay project."
                the_person "Hmph, eager much, senpai? Alright, let's go. But don't think this means I'm going to start doing 'requests' for you anytime soon."
                call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_cosplay_flirt_response_high_2
                the_person "So... Now what's your plan, senpai? Are you going to try to charm me with your cosplay skills?"

                if the_person.is_willing(kissing):
                    $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
                    if the_person.has_taboo("kissing"):
                        "You lean in close to kiss [the_person.title], your lips brushing against her cosplay makeup."
                        $ the_person.call_dialogue("kissing_taboo_break")
                        $ the_person.break_taboo("kissing")
                        "She responds passionately, her arms wrapping around your neck, her cosplay outfit rustling softly."
                    else:
                        "You step close to [the_person.title] and put your arm around her waist, pulling her close and kissing her, your lips brushing against her cosplay makeup."
                        "She responds immediately and eagerly presses her body against yours, her cosplay outfit rustling softly."
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _vt_cosplay_call_fuck_person_49
                else:
                    if the_person.has_taboo("touching_body"):
                        $ the_person.call_dialogue("touching_body_taboo_break")
                        $ the_person.break_taboo("touching_body")
                        "You take her hand and pull her close against you, your fingers brushing against her cosplay gloves. She looks into your eyes."
                    else:
                        "You take her hand and pull her close, your lips brushing against her ear, your fingers brushing against her cosplay gloves."
                    call fuck_person(the_person, private = True, start_position = standing_grope, skip_intro = True) from _call_fuck_person_cosplay_flirt_grope

                $ the_person.call_dialogue("sex_review", the_report = _return)
                call mc_restore_original_location(the_person) from _call_mc_restore_original_location_cosplay_flirt_response_high_2

            "Just flirt":
                mc.name "You know you want to, come on, [the_person.fname]. I'll take you out for dinner, and then we can see where the night takes us... maybe we can even plan a cosplay photoshoot together."
                the_person "Hmm, you're really trying to charm me, aren't you, senpai? Well, I'll tell you what... If you can make me laugh, I might consider it."
                "She smiles mischievously, clearly enjoying the challenge, adjusting her cosplay outfit."

    else:
        if mc.location.person_count == 1: #You're alone, so she just didn't meet the sluttiness threshold
            the_person "Hmm, you're really eager, aren't you, senpai? Well, I suppose it's just the two of us here... and I have to admit, I'm enjoying the attention."
            "[the_person.possessive_title!c] glances around, confirming you're alone, adjusting her cosplay outfit."
            the_person "So what's your plan, senpai? Are you going to try to charm me with your cosplay skills?"

        else:  # You aren't alone but she's still into it.
            the_person "Feeling bold today, huh, senpai? Well, I think your chances are pretty good... especially since you seem to appreciate my cosplay skills."
            "[the_person.title] smirks, clearly enjoying the attention, adjusting her cosplay outfit."
            if the_person.has_large_tits: #Bounces her tits for you
                $ mc.change_locked_clarity(15)
                "[the_person.title] grabs her tits and jiggles them for you, her cosplay outfit rustling softly."
                the_person "Maybe I can get these girls out for you, senpai. Does that sound nice? Maybe we can even plan a cosplay photoshoot together."

            else: #No big tits, so she can't bounce them (as much)
                "[the_person.title] runs her hands over her hips sensually, obviously encouraging you to take things further, her cosplay outfit rustling softly."

        menu:
            "Touch her" if not the_person.is_willing(kissing):
                "You step closer to [the_person.title] and move your hands down her waist, your fingers brushing against her cosplay gloves."
                if the_person.has_taboo("touching_body"):
                    the_person "Oh, you're brave, senpai. I like that."
                    $ the_person.call_dialogue("touching_body_taboo_break")
                    $ the_person.break_taboo("touching_body")

                call fuck_person(the_person, start_position = standing_grope, private = False) from _call_fuck_person_flirt_response_cosplay_touching

            "Kiss her" if the_person.is_willing(kissing):
                $ the_person.draw_person()
                if the_person.has_taboo("kissing"):
                    "You put your arm around [the_person.possessive_title] and lean in close, your lips brushing against her cosplay makeup."
                    $ the_person.call_dialogue("kissing_taboo_break")
                    $ the_person.break_taboo("kissing")
                    "She responds with a passionate kiss, her arms wrapping around your neck, her cosplay outfit rustling softly."
                else:
                    "You pull [the_person.possessive_title!] close and kiss her, your lips brushing against her cosplay makeup."
                    "She responds with a passionate kiss, her arms wrapping around your neck, her cosplay outfit rustling softly."

                call mc_move_to_private_location(the_person) from  _call_mc_move_to_private_location_cosplay_flirt_response_high
                call fuck_person(the_person, start_position = kissing, private = _return, skip_intro = True) from _vt_cosplay_call_fuck_person_50
                $ the_person.call_dialogue("sex_review", the_report = _return)
                call mc_restore_original_location(the_person) from _call_mc_restore_original_location_cosplay_flirt_response_high

            "Just flirt":
                $ the_person.draw_person()
                mc.name "Very tempting, but you're going to have to contain yourself for now, [the_person.fname]. Maybe we can plan a cosplay photoshoot together instead?"
                the_person "Oh, you're not going to take advantage of me right now, are you, senpai? Fine, be that way. But don't think this means I'm not interested in you... or your cosplay skills."
                "[the_person.title] pouts, clearly enjoying the flirtation, adjusting her cosplay outfit."
    return

label cosplay_flirt_response_low_energy(the_person):
    if the_person.sluttiness > 40:
        the_person "Ugh, thanks for the compliment, senpai... but I'm so tired right now. I've been up all night working on my cosplay project."
    else:
        the_person "Thanks, but I'm beat, senpai. Can we pick this up later? I need to get some rest before my next cosplay photoshoot."
    return

label cosplay_flirt_response_girlfriend(the_person):
    # Lead in: mc.name "You're so beautiful [the_person.title], I'm so lucky to have a woman like you in my life."
    if mc.location.person_count > 1:
        # There are other people around, so she'll only start making out with you if she's slutty.
        if the_person.effective_sluttiness("kissing") < (25 - (5*the_person.opinion.public_sex)):
            # Not very slutty, so she wants to find somewhere private
            the_person "Oh my god, you're so cheesy, senpai. Come here."
            "She pulls you against her and kisses you, her lips soft and gentle, her cosplay outfit rustling softly."
            the_person "There, now you can't say I don't know how to kiss... especially in cosplay."
            mc.name "Haha, yeah I guess not... you're really talented when it comes to cosplay, [the_person.fname]."
            "You put your arms around her and kiss her back, feeling her warmth and appreciating her cosplay skills."
            the_person "Mmm, yeah, like that, senpai."
            menu:
                "Find somewhere more quiet\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                    mc.name "Why wait, [the_person.fname]? Come on, I'm sure we can find somewhere quiet... and maybe even plan a cosplay photoshoot together."
                    the_person "You're always so eager, aren't you, senpai? Alright, let's go! But don't think this means I'm going to start doing 'requests' for you anytime soon."
                    "You and [the_person.possessive_title] hurry off, searching for a private spot to continue your cosplay adventure."
                    call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_cosplay_flirt_response_girlfriend_2
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _vt_cosplay_call_fuck_person_76
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_cosplay_flirt_response_girlfriend_2

                "Just flirt":
                    $ mc.change_locked_clarity(10)
                    "You reach around and pull her closer, running your hand down her back and appreciating her cosplay outfit."
                    mc.name "You're so beautiful, [the_person.fname], and you know it... especially in cosplay."
                    "She rolls her eyes but leans in for a quick kiss, her cosplay makeup sparkling in the light."
                    the_person "Fine, you caught me, senpai. But don't think this means I'm going easy on you... especially when it comes to cosplay."

        else:
            the_person "Well if I'm so beautiful, then why are you just standing there, senpai? Come on, kiss me... and appreciate my cosplay skills."
            "You put your arm around her waist and pull her close, kissing her deeply and appreciating her cosplay outfit."
            "When you break the kiss, [the_person.possessive_title] sighs and leans against you, her cosplay outfit rustling softly."
            the_person "You're not so bad yourself, senpai... especially when it comes to appreciating cosplay."
            menu:
                "Make out":
                    "You lean back in and kiss her again, this time more passionately, appreciating her cosplay skills."
                    "[the_person.title] responds eagerly, wrapping her arms around your neck and pulling you close, her cosplay outfit rustling softly."

                    call mc_move_to_private_location(the_person) from  _call_mc_move_to_private_location_cosplay_flirt_response_girlfriend
                    call fuck_person(the_person, start_position = kissing, private = _return, skip_intro = True) from _vt_cosplay_call_fuck_person_77
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_cosplay_flirt_response_girlfriend

                "Just flirt":
                    mc.name "I'm not bad? You're the one who's hard to resist, [the_person.fname]... especially in cosplay."
                    $ mc.change_locked_clarity(10)
                    "You reach out and touch her cheek, a playful grin on your face, appreciating her cosplay makeup."
                    the_person "Ugh, you're so annoying, senpai. But I guess I like that about you... especially when it comes to cosplay."
    else:
        # You're alone, so she's open to fooling around.
        the_person "Well you've got me all alone, senpai, so how about you show me just how lucky you feel... especially when it comes to cosplay."
        "She reaches down to your waist and cups your crotch, rubbing it gently, her cosplay outfit rustling softly."
        mc.name "You're so wet for me already, [the_person.fname]."
        the_person "Hmph, maybe, senpai... but don't think this means I'm going to start doing 'requests' for you anytime soon."
        "She grinds against you, her hips moving in a slow circle, her cosplay outfit rustling softly."
        mc.name "Damn, you feel so good, [the_person.fname]."
        "You reach up and grab her breasts, squeezing them gently, appreciating her cosplay outfit."
        the_person "Ooh, don't do that, senpai... but don't stop, either."
        "But she doesn't pull away, her body still pressed against yours, her cosplay outfit rustling softly."
        menu:
            "Kiss her":
                if the_person.has_taboo("kissing"):
                    $ the_person.call_dialogue("kissing_taboo_break")
                    $ the_person.break_taboo("kissing")

                "You put your arms around [the_person.possessive_title]'s waist and rest your hands on her ass, appreciating her cosplay outfit. You pull her close and kiss her sensually."
                "She responds by pressing her body against you and grinding her hips against your thigh, her cosplay outfit rustling softly."
                "You grab her hips and pull her closer, your crotches pressed together, appreciating her cosplay skills."
                call fuck_person(the_person, start_position = kissing, skip_intro = True) from _vt_cosplay_call_fuck_person_78
                $ the_person.call_dialogue("sex_review", the_report = _return)
                $ the_person.review_outfit()

            "Just flirt":
                mc.name "I'm going to make you beg for it, [the_person.fname]... especially when it comes to cosplay."
                "You lean in close, your breath hot against her ear, appreciating her cosplay makeup."
                the_person "Ooh, you're such a bad boy, senpai. I love it... especially when it comes to cosplay."
                "She rubs her body against yours, her hips moving seductively, her cosplay outfit rustling softly."
                the_person "But don't think you're getting off that easy, senpai. I'm going to make you work for it... especially when it comes to cosplay."
    return

label cosplay_flirt_response_affair(the_person):
    # Lead in: mc.name "You look so good today [the_person.title], you're making me want to do some very naughty things to you."
    if mc.location.person_count > 1: #There are other people around, she's nervous about people finding out what you're doing.
        if (the_person.opinion.cheating_on_men *15) + the_person.effective_sluttiness() > 50: #SHe's turned on by flirting in public or doesn't think anything is wrong with it
            "[the_person.possessive_title!c] blushes and playfully bats her eyes at you, her cosplay makeup sparkling in the light."
            the_person "Oh, you're making me blush, senpai. I'm not used to this kind of attention from you... especially when I'm in cosplay."
            the_person "But I have to admit, I'm curious. What do you have in mind, senpai? Maybe we can even plan a cosplay photoshoot together."
            menu:
                "Find somewhere more quiet\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                    mc.name "I was thinking we could slip away and find a more private spot, [the_person.fname]. Maybe we can even find a place to take some cosplay photos."
                    "You and [the_person.title] exchange a flirtatious glance before hurrying off to find a quiet spot, her cosplay outfit rustling softly."
                    call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_cosplay_flirt_response_affair
                    $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
                    "As soon as you're alone she pulls you into a deep and passionate kiss, her cosplay makeup sparkling in the light."
                    $ the_person.draw_person(position = "kissing")
                    the_person "Mmm... I've been wanting to do that for a while now, senpai. You're really talented when it comes to cosplay."
                    "You wrap your arms around her waist and kiss her back, appreciating her cosplay skills."
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _vt_cosplay_call_fuck_person_79
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_cosplay_flirt_response_affair

                "Just flirt":
                    mc.name "I can't help but notice how beautiful you look today, [the_person.title]. Your cosplay skills are really impressive."
                    the_person "Stop it, senpai, you're making me blush! But I have to admit, you look pretty great yourself... especially when you're appreciating my cosplay."
                    the_person "Just don't get too cocky, okay? I'm still in charge here, even when it comes to cosplay."
                    $ mc.change_locked_clarity(20)
                    "[the_person.possessive_title!c] playfully swats at your arm before leaning in close, her cosplay outfit rustling softly."
                    the_person "But I have to admit, I'm getting a little turned on by this whole thing, senpai. Maybe we can even plan a cosplay collaboration."
                    "You can't help but feel a little flustered as she teases you, appreciating her cosplay skills."
                    mc.name "I can see that, [the_person.fname]. Maybe we should find a more private place to continue this... and discuss our next cosplay project."
                    the_person "Mmm, maybe we should, senpai. But first, let's enjoy this little moment here... and appreciate each other's cosplay skills."

        else: #She's shy or nervous about being discovered
            "[the_person.possessive_title!c] looks around nervously, then back at you with a sheepish grin, adjusting her cosplay outfit."
            the_person "Oh, um, you look nice today, senpai. I guess I should probably get going though... I have a cosplay photoshoot to get to."
            mc.name "Wait, don't go! I was thinking we could... uh, grab a drink or something, and discuss our next cosplay project."
            $ mc.change_locked_clarity(15)
            the_person "Oh, you want to grab a drink? Okay, sure, senpai. But just for a little bit, okay? I don't want to be out too late... and I have to get back to my cosplay project."
            "She glances around again, then leans in close and whispers, her cosplay makeup sparkling in the light."
            the_person "And just so you know, I'm still in charge here, even if we're just grabbing a drink... and discussing cosplay."
            "You can't help but feel a little excited by her assertiveness, appreciating her cosplay skills."
            mc.name "Okay, okay, [the_person.fname]. I'll behave... and appreciate your cosplay skills."

    else:
        # the_person "Yeah? Well there's nobody around, and I'm not going to stop you."
        the_person "Oh yeah, senpai? Well then, do you want to share what all of these naughty things are? You have my attention... and I have to admit, I'm intrigued by your cosplay skills."
        menu:
            "Feel her up":
                "You put your arms around [the_person.possessive_title]'s waist and rest your hands on her ass, appreciating her cosplay outfit."
                mc.name "You know, I've been waiting for this moment for a while now, [the_person.fname]. You're really talented when it comes to cosplay."
                "You massage her butt. She blushes and pushes you away lightly, her cosplay outfit rustling softly."
                the_person "Hey, no need to be so forward, senpai! What's gotten into you?"
                "You pull her close again and shift your hands to her breasts, squeezing them gently, appreciating her cosplay skills."
                mc.name "Come on, don't be like that, [the_person.fname]. I just wanted to make you feel good for once... and appreciate your cosplay skills."
                call fuck_person(the_person, private = True, start_position = standing_grope, skip_intro = True) from _vt_cosplay_call_fuck_person_80
                $ the_person.call_dialogue("sex_review", the_report = _return)
                $ the_person.review_outfit()

            "Just flirt":
                $ mc.change_locked_clarity(10)
                "You put your arms around [the_person.possessive_title]'s waist and rest your hands on her ass, appreciating her cosplay outfit."
                mc.name "I wish I had the time, [the_person.fname]. You'll have to wait until later... but I promise it'll be worth it, especially when it comes to cosplay."
                "You massage her butt. She sighs happily and leans her weight against you, her cosplay outfit rustling softly."
                the_person "Aww, are you sure, senpai?"
                "You slap her ass and step back, appreciating her cosplay skills. She clings to you reluctantly before letting go."
                the_person "Fine, but don't make me wait too long, okay, senpai? I have needs, and my [the_person.so_title] sure as hell isn't fulfilling them... especially when it comes to cosplay."
                mc.name "I won't make you wait long, [the_person.fname]. I promise."
                "She looks up at you with a playful pout, her cosplay makeup sparkling in the light."
                the_person "Promise you won't make me wait, senpai?"
                mc.name "I promise, baby."
                "You both share a flirtatious smile, appreciating each other's cosplay skills."
                the_person "Good, senpai. Because I'm not sure I can handle it if you do."
    return

label cosplay_flirt_response_text(the_person):
    mc.name "Hey [the_person.title], how's it going? I'm feeling a bit bored and thought we could chat about our next cosplay project."
    "She replies with a hint of annoyance, adjusting her cosplay outfit."
    if the_person.is_affair:
        the_person "Oh, great, you're bored again, senpai? You always seem to find ways to bother me, especially when I'm in the middle of a cosplay project."
        the_person "Well, what do you want this time? I'm not exactly thrilled about entertaining you, especially when I have a cosplay deadline to meet."
        the_person "When can we get together and discuss our next cosplay collaboration?"
        mc.name "Some time soon, [the_person.fname]. I'll let you know."

    elif the_person.is_girlfriend:
        the_person "Bored, huh, senpai? That's not exactly a surprise. You're always looking for something new to entertain yourself, especially when it comes to cosplay."
        the_person "But fine, we can hang out and discuss our next cosplay project. Just don't expect me to do anything special, okay?"
        mc.name "Some time soon, [the_person.fname]. I'll let you know."

    elif the_person.love < 40:
        if the_person.effective_sluttiness() > the_person.love:
            the_person "Ugh, bored, really, senpai? Well, I suppose I can keep you company for a bit, especially if we're discussing cosplay."
        else:
            the_person "Bored, eh, senpai? That's not surprising. You're always looking for a new distraction, especially when it comes to cosplay."

    else:
        if the_person.effective_sluttiness() > the_person.love:
            the_person "Fine, I'll talk to you, senpai. But don't think this means I'm happy about it, especially when I have a cosplay project to finish."
            the_person "So, what do you want to talk about? I'm not exactly thrilled about this, but I suppose we can discuss our next cosplay collaboration."
        else:
            the_person "You're bored, huh, senpai? Well, that's your problem, not mine. But I suppose we can discuss our next cosplay project if you'd like."
            the_person "So, what do you want, senpai? Just don't expect me to be all lovey-dovey about it, especially when it comes to cosplay."
    return

label cosplay_condom_demand(the_person):
    if the_person.wants_creampie:
        the_person "Ugh, seriously, senpai? You need to put on a condom before we even think about doing anything, especially when we're in cosplay."
        the_person "I hate that we have to, but you know it's necessary, especially when it comes to cosplay safety."
    else:
        the_person "For crying out loud, senpai, do you have a condom on you? Put one on before you even think about touching me, especially when we're in cosplay."
        the_person "I don't want to be stuck with some stupid disease because you were too careless, especially when we're in the middle of a cosplay project."
    return

label cosplay_condom_ask(the_person):
    if the_person.on_birth_control:
        the_person "You want a condom, senpai? Fine, but I'm on the pill, so it's not like I really need it, especially when we're in cosplay."
        $ the_person.update_birth_control_knowledge()
    elif the_person.wants_creampie:
        the_person "Ugh, you want to cum inside me, senpai? Just put on a condom, would you? It's not like I want to get pregnant or anything, especially when we're in the middle of a cosplay project."
        the_person "But I guess it's better than the alternative, right, senpai?"
        $ the_person.discover_opinion("creampies")
    else:
        the_person "Fine, I guess you should use a condom, senpai...but can you at least not make a mess with it? I don't want to clean up after you, especially when we're in cosplay."
        the_person "And please, no pulling out method, senpai. That's just asking for trouble, especially when we're in the middle of a cosplay project."
    return

label cosplay_condom_bareback_ask(the_person):
    if the_person.wants_creampie:
        if the_person.is_infertile:
            the_person "You're not seriously considering a condom, are you, senpai? Please, just give me your hot, sticky load... and make me scream with pleasure in this cosplay outfit."
            the_person "I want to feel you fill me up and make me feel like a true cosplay heroine."
        elif the_person.on_birth_control:
            the_person "Don't even think about putting a condom on, senpai. I'm on the pill, so we're good to go... and I can focus on my cosplay skills."
            the_person "Just fuck me raw and make me feel every inch of you, senpai. I want to feel like a true cosplay model."
            $ the_person.update_birth_control_knowledge()
        else:
            the_person "Forget the condom, senpai, I want to feel you deep inside me... and make this cosplay experience even more intense."
            the_person "I don't care about the risks, it's worth it for this kind of pleasure... and to make our cosplay photoshoot even more memorable."
            if not the_person.knows_pregnant:
                the_person "Imagine how hot it would be to get knocked up, too, senpai... and have a cosplay-themed pregnancy photoshoot."
        $ the_person.discover_opinion("creampies")
    else:
        the_person "Don't bother with a condom, senpai. I want to feel you raw and unprotected... and make this cosplay experience even more intense."
        if not the_person.knows_pregnant:
            the_person "I don't care about the risks, it's worth it for the intensity... and to make our cosplay photoshoot even more memorable."
        else:
            the_person "I love it when you fuck me raw and make me feel like I'm yours, senpai... especially when we're in cosplay."
    return

label cosplay_condom_bareback_demand(the_person):
    if the_person.has_breeding_fetish: #Actively looking to get knocked up.
        if the_person.knows_pregnant:
            the_person "Ugh, why bother with a condom, senpai? I want to get pregnant, so fuck me raw... and make this cosplay experience even more intense."
            the_person "Hurry up, I can't wait to feel you inside me... and start planning our cosplay-themed pregnancy photoshoot."
        elif the_person.is_infertile:
            the_person "Oh, great, you're going to remind me I can't get pregnant, senpai? Thanks a lot... but I still want to feel you raw and unprotected in this cosplay outfit."
        else:
            the_person "Ugh, what's the point of fucking if you're not going to knock me up, senpai? I want to feel like a true cosplay heroine."
            the_person "Hurry up and give me that cock, senpai... and make this cosplay experience even more intense."
    elif the_person.wants_creampie: #Just likes raw sex
        if the_person.is_infertile:
            the_person "Ugh, why bother with a condom, senpai? I can't get pregnant anyway... but I still want to feel you raw and unprotected in this cosplay outfit."
        elif the_person.on_birth_control:
            the_person "Forget the condom, senpai. I'm on the pill, so it's not a problem... and I can focus on my cosplay skills."
            the_person "Take me bareback and make me scream, senpai... and make this cosplay experience even more intense."
            $ the_person.update_birth_control_knowledge()
        else:
            the_person "Ugh, condoms are so annoying, senpai. Just get inside me already... and make this cosplay experience even more intense."
    else:
        if the_person.is_infertile:
            the_person "Take me bareback, senpai. It's not like I can get pregnant... but I still want to feel you raw and unprotected in this cosplay outfit."
            the_person "Just make me feel good, senpai... and make this cosplay experience even more intense."
        elif the_person.on_birth_control:
            the_person "Forget the condom, senpai. I'm on the pill... and I can focus on my cosplay skills."
            the_person "Take me bareback and make me feel every inch of you, senpai... and make this cosplay experience even more intense."
            $ the_person.update_birth_control_knowledge()
        else:
            the_person "Ugh, condoms are so annoying, senpai. Just get inside me already... and make this cosplay experience even more intense."
            the_person "I need to feel you deep inside me, senpai... and make this cosplay photoshoot even more memorable."
    return

label cosplay_cum_face(the_person):
    if the_person.has_cum_fetish or the_person.obedience > 180:
        if the_person.has_cum_fetish or the_person.effective_sluttiness() > 60 or the_person.opinion.cum_facials > 0:
            the_person "So, do you think this is a good look for me, senpai? I feel like a true cosplay heroine with your cum all over my face."
            "[the_person.title] smirks, then licks her lips and runs a finger through your semen, bringing it to her mouth."
            the_person "Mmm, taste your victory, senpai... and the success of our cosplay photoshoot."
        else:
            the_person "Hmph, I suppose it's not a terrible look, senpai. But I'm glad we're done here... and I can finally take off this cosplay outfit."
            "[the_person.title] wipes away some of your semen from her face, looking annoyed."
    else:
        if the_person.effective_sluttiness() > 80 or the_person.opinion.cum_facials > 0:
            the_person "Well, I guess this is one way to end things, senpai. Do you think I look good like this... with your cum all over my face and cosplay outfit?"
            "[the_person.title] smirks, then laughs and wipes away some of your semen from her face."
        else:
            the_person "Ugh, just get that over with already, senpai. And don't think you're getting a second chance... especially not after ruining my cosplay makeup."
            "[the_person.title] wipes away your semen, looking put off."
    return
### DIALOGUE ###

label cosplay_cum_mouth(the_person):
    if the_person.has_cum_fetish or the_person.obedience > 180:
        if the_person.has_cum_fetish or the_person.effective_sluttiness() > 60 or the_person.opinion.drinking_cum > 0:
            the_person "Mmm, that's so... satisfying, senpai. You really know how to make me feel good, especially in cosplay."
            the_person "I love the way you look at me when I'm in cosplay, it really turns me on."
        else:
            "[the_person.title]'s face twists in disgust as she swallows your cum, her cosplay makeup slightly smudged."
            the_person "Ugh, there, done, senpai. Don't think I enjoyed that one bit, especially not in cosplay."
    else:
        if the_person.effective_sluttiness() > 80  or the_person.opinion.drinking_cum > 0:
            the_person "Mmm, you're quite the stud, senpai. I can see why you're so popular, especially among cosplayers."
            the_person "I love the way you appreciate my cosplay skills, it really turns me on."
        else:
            the_person "Ugh, that's... quite a taste, senpai. I hope you're happy, especially since we're in cosplay."
    return

label cosplay_cum_pullout(the_person):
    # Lead in: "I'm going to cum!"
    if mc.condom:
        if the_person.wants_creampie and not the_person.has_taboo("condomless_sex"): #TODO: FIgure out we want any more requirements for this to fire.
            if the_person.knows_pregnant:
                the_person "Oh, don't bother with the condom, senpai, just cum inside me and make me pregnant! I want to feel like a true cosplay heroine."
                the_person "I don't care about the consequences right now, I just want your cum filling me up and making our cosplay experience even more intense."
            elif the_person.on_birth_control:
                the_person "Oh fuck, senpai... I can't take it any more, take that condom off and make our cosplay experience even more intense!"
                "She moans desperately, her cosplay outfit rustling softly."
                the_person "I give in, I want you to cum inside me and make me feel like a true cosplay model!"
            else:
                "She moans desperately, her cosplay outfit rustling softly."
                the_person "I can't think straight, senpai, just take off the condom and cum inside me! I want to feel like a true cosplay heroine."
                $ the_person.update_birth_control_knowledge()
                the_person "I want you to make me cum and then make me pregnant, you dirty fucker, and make our cosplay experience even more intense!"
            menu: #TODO: Add a variant of this normally so you can stealth a girl (don't do that in real life, it's super fucked up).
                "Take off the condom":
                    "You pull out, barely clearing her pussy, and pull the condom off as quickly as you can manage, your hands shaking with excitement."
                    $ mc.condom = False
                    $ use_condom = False  # prevent putting on a new condom next sex loop
                "Leave it on":
                    "You ignore [the_person.possessive_title]'s request and keep the condom in place, your mind focused on the cosplay experience."
        else:
            the_person "Fuck yeah, senpai, I'm going to make you cum and make our cosplay experience even more intense!"
    else:
        if the_person.wants_creampie:
            if the_person.knows_pregnant: #She's already knocked up, so who cares!
                the_person "Creampie me, you dirty fucker, senpai, and make me cum! I want to feel like a true cosplay heroine."
            elif the_person.opinion.creampies > 0:
                "[the_person.possessive_title!c] moans happily, her cosplay outfit rustling softly."
                if the_person.on_birth_control: #She just likes creampies.
                    the_person "Fuck yeah, fill me up with your cum, senpai! Creampie me and make our cosplay experience even more intense!"
                else: #Yeah, she's not on BC and asking for you to creampie her. She's looking to get pregnant.
                    $ the_person.update_birth_control_knowledge()
                    the_person "Oh fuck, cum inside me and knock me up, senpai! I want you to breed me like a dirty slut and make our cosplay experience even more intense!"
            elif the_person.is_infertile:
                the_person "Cum wherever you want, you dirty fucker, senpai, I can't get pregnant... but I still want to feel like a true cosplay heroine."
            elif the_person.on_birth_control: #She's on the pill, so she's probably fine
                $ the_person.update_birth_control_knowledge()
                the_person "Cum wherever you want, you dirty fucker, senpai, I'm on the pill! Let's make our cosplay experience even more intense!"
            else: #Too distracted to care about getting pregnant or not. Oh well, what could go wrong?
                the_person "Do it, senpai! Cum and make our cosplay experience even more intense!"
        else:
            if the_person.is_infertile:
                the_person "Just pull out, senpai, I don't want your cum inside me, you dirty fucker! Let's just focus on the cosplay experience."
            elif not the_person.on_birth_control: #You need to pull out, I'm not on the pill!
                $ the_person.update_birth_control_knowledge()
                the_person "Fuck, pull out, you dirty fucker, senpai! I'm not on the pill, and I don't want to ruin our cosplay experience!"
            elif the_person.opinion.creampies < 0:
                the_person "Pull out, senpai, I don't want you to cum in me, you dirty fucker! Let's just focus on the cosplay experience."
            else:
                the_person "Hell yeah, pull out and cum all over me like a dirty slut, senpai! Let's make our cosplay experience even more intense!"
    return

label cosplay_cum_condom(the_person):
    if the_person.effective_sluttiness() > 75 or the_person.opinion.creampies > 0:
        the_person "Oh god, it feels so good, senpai. If your condom broke it would be inside me, and I'd be pregnant... just like a true cosplay heroine."
    else:
        the_person "Oh god, I hope you buy good condoms, senpai, because that's a lot of cum... and I don't want to ruin our cosplay experience."
        the_person "But then again, maybe you're dreaming of knocking me up and getting me pregnant, just like in a cosplay fantasy."
    return

label cosplay_cum_vagina(the_person):
    if the_person.has_taboo("creampie"):
        $ the_person.call_dialogue("creampie_taboo_break")
        $ the_person.break_taboo("creampie")
        return
    if the_person.wants_creampie:
        if the_person.knows_pregnant:
            the_person "Ugh, fine... I guess I can admit it now, but only because I'm already pregnant from your other, uh, impressive performances, senpai... Your cum just feels so good inside me, especially when we're in cosplay!"
        elif the_person.is_infertile:
            the_person "Oh, stop being so dramatic, senpai! Of course you're not going to get me pregnant, I'm infertile, remember? But seriously, your cum is pretty great... just don't expect me to admit it to anyone else, especially not in the cosplay community."
        elif the_person.on_birth_control:
            if the_person.has_significant_other:
                the_person "Well, well, well... Look at you go, senpai! I guess it's a good thing I'm on the pill, huh? Or maybe I'll just tell [the_person.so_name] that it was someone else's... Ugh, why do you have to be so frustrating, especially when we're in cosplay?"
            else:
                if the_person.knows_pregnant:
                    the_person "Oh fuck that's a lot of cum, senpai. Good thing I'm already pregnant, because I don't think you're firing blanks... and I love the way you look at me when I'm in cosplay."
                elif the_person.is_infertile:
                    the_person "Oh fuck that's a lot of cum, senpai. I will be dripping your cum all day long, especially when we're at a cosplay event."
                else:
                    the_person "Oh fuck that's a lot of cum, senpai. Good thing I'm on the pill, because I don't think you're firing blanks... and I love the way you appreciate my cosplay skills."
                $ the_person.update_birth_control_knowledge()
        elif the_person.effective_sluttiness() > 75 or the_person.opinion.creampies > 0:
            if the_person.has_significant_other:
                the_person "Okay, okay, I get it, senpai! You're great in bed, but don't think I'm going to start flaunting our little secret around my [the_person.so_title]... At least, not until I figure out how to explain it, especially in the cosplay community."
            else:
                the_person "Ugh, fine... I'll admit it, senpai, you're pretty amazing when you're like this... But don't think this means I'm going to start begging for more! I just need to... process this, okay, especially when it comes to our cosplay relationship."
        else:
            if the_person.has_significant_other:
                the_person "You really know how to make a girl feel special, don't you, senpai? But let's keep this between us, okay? I don't think [the_person.so_name] would understand, especially when it comes to our cosplay activities."
            else:
                the_person "Wow... I guess I didn't expect that from you, senpai. But I have to admit, it was kind of nice... Just don't get any ideas, okay? I'm not ready for anything serious, especially when it comes to cosplay."
    else: #She's angry
        if the_person.knows_pregnant:
            the_person "Ugh, what is wrong with you, senpai? I specifically told you not to do that! Oh well, since I'm already pregnant... I guess we'll just have to deal with it, especially in the cosplay community."
        elif not the_person.on_birth_control:
            if the_person.has_significant_other:
                the_person "Oh, great. Just what I needed, senpai. You forgot to pull out, and now I'm going to have to deal with [the_person.so_name]'s anger... and the fallout in the cosplay community."
                if the_person.kids > 0:
                    the_person "... Again, senpai."
            else:
                the_person "Oh fuck, I said to pull out, senpai! I'm not on the pill, what happens if I get pregnant?... and how will this affect our cosplay relationship?"
                $ the_person.update_birth_control_knowledge()
                the_person "What is wrong with you, senpai? You know I'm not on the pill! Now look what you've done... I guess next time we'll have to use a condom, especially during cosplay."
        elif the_person.is_infertile:
            the_person "Unbelievable, senpai! I told you to pull out, and now you've gone and made a mess... What a pain in the ass, especially when we're in cosplay."
        elif the_person.has_significant_other:
            the_person "You're really going to make me tell [the_person.so_name] about this, aren't you, senpai? Fine, I'll deal with it. Just be more careful next time, especially during cosplay."
            $ the_person.update_birth_control_knowledge()
            the_person "I don't want to have to make you wear a condom, senpai, so be a little more careful next time... especially during our cosplay activities."
        elif the_person.opinion.creampies < 0:
            the_person "Oh, great. Just what I needed, senpai. You couldn't even follow a simple instruction, could you? Now look at what a mess you've made... especially during our cosplay session."
        else:
            the_person "You really need to work on your timing, senpai. I told you to pull out, not do the exact opposite!... especially during cosplay."
            the_person "Just remember, senpai, I'm not going to be as forgiving next time if you can't follow simple instructions... especially when it comes to our cosplay relationship."
    return

label cosplay_cum_anal(the_person):
    if the_person.has_taboo("anal creampie"):
        $ the_person.call_dialogue("anal_creampie_taboo_break")
        $ the_person.break_taboo("anal creampie")
        return

    if the_person.sluttiness > 75 or the_person.opinion.anal_creampies > 0:
        the_person "Ugh, fine... I guess it's okay if you do that, senpai... But don't think I'm going to start asking for it all the time, especially during cosplay."
    elif the_person.opinion.anal_creampies < 0:
        the_person "Oh, come on, senpai... not in there! I don't need to be embarrassed like that, especially during a cosplay session."
    else:
        the_person "Oh, alright, senpai... if you insist... But just this once, and don't think I'm going to start liking it or anything, especially when it comes to our cosplay activities."
    return

label cosplay_surprised_exclaim(the_person):
    $rando = renpy.random.choice(["What the heck, senpai?","Ugh, seriously?","Why now, of all times?","This again? Not during our cosplay session!","Not again, senpai!", "Seriously, what's going on?", "Great, just what I needed...", "Oh, joy... not.", "Fucking perfect... just what I wanted to happen during our cosplay photoshoot...", "Unbelievable, senpai!", "Not again, not during cosplay!", "Why can't I have a normal cosplay session for once?"])
    the_person "[rando]"
    return

label cosplay_talk_busy(the_person):
    if the_person.obedience > 120:
        the_person "Ugh, I don't have time for this, senpai. I've got way too much on my plate right now, what with our cosplay project and all."
    else:
        the_person "Listen, I'd love to catch up, senpai, but I'm swamped with things to do. Maybe we can talk later, after our cosplay session?"
    return

label cosplay_sex_strip(the_person):
    if the_person.sluttiness < 20:
        if the_person.arousal_perc < 50:
            the_person "Ugh, fine, senpai. I'll take off some clothes, but don't think I'm doing this because I like you or anything. I just need to get comfortable in my cosplay outfit, that's all."
            mc.name "Come on, babe. It's just us here, in our cosplay session. You can relax."
            the_person "I don't care, senpai! I'm still not comfortable in this cosplay outfit. And don't call me 'babe'. That's weird, especially during cosplay."
            mc.name "Okay, okay, senpai. I'll stop. Just take your time, okay?"
        else:
            the_person "Alright, alright, senpai. I'll take off a few things, but don't expect me to be impressed by your reaction. I'm just taking off some clothes, big deal, especially during a cosplay session."
            mc.name "Aww, come on, senpai. You're being a little rough. Just let me see you a little more in your cosplay outfit, okay?"
            the_person "Fine, but only because you asked nicely, senpai. And don't think this means I like you or anything, especially not in a cosplay context."
    elif the_person.sluttiness < 60:
        if the_person.arousal_perc < 50:
            the_person "Fine, I'll make an exception and get a little more comfortable in my cosplay outfit, senpai. But don't get any ideas, okay?"
            mc.name "I promise, I won't get any ideas, senpai. I just want to make sure you're comfortable during our cosplay session."
            the_person "Ugh, fine, senpai. But don't think I'm doing this for you. I just need to get a little more comfortable in this cosplay outfit."
            mc.name "I understand, senpai. Just take your time and let me know if you need anything during our cosplay session."
        else:
            the_person "Okay, okay, senpai. I'll take off a few more things if it'll make you happy during our cosplay session. But don't think I'm doing this because I'm into you or anything, especially not in a cosplay context."
            mc.name "I know, I know, senpai. You're just doing it because you want to, right?"
            the_person "Whatever, senpai. Just let me get this off and we can get on with this cosplay session. And don't think this means I'm going to start liking you or anything, especially not in a cosplay context."
    else:
        if the_person.arousal_perc < 50:
            the_person "Ugh, fine, senpai. I'll do it. But just for you, I'll make an exception during our cosplay session. And don't think I'm doing this because I like you or anything, especially not in a cosplay context."
            mc.name "Thanks, babe, senpai. You're making me really happy right now during our cosplay session."
            the_person "Don't call me 'babe', senpai. And don't get too happy. I'm just doing this because I have to, especially during a cosplay session."
        else:
            the_person "Great, now let me get this off and we can get on with this cosplay session, senpai. I'm dying over here! But don't expect me to be all happy about it or anything, especially not during a cosplay photoshoot."
            mc.name "Aww, come on, senpai. You're being a little grumpy. Let's just have some fun during our cosplay session, okay?"
            the_person "Fine, senpai. But don't expect me to start smiling and laughing or anything, especially not during a cosplay session."
    return

label cosplay_sex_watch(the_person, the_sex_person, the_position):
    $ title = the_person.title if not the_person.is_stranger else "The stranger"
    if the_person.sluttiness < the_position.slut_requirement - 20:
        $ the_person.draw_person(emotion = "angry", display_transform = character_left_flipped)
        the_person "Ugh, seriously, senpai? Can you two keep it down? I'm trying to concentrate on my cosplay project."
        $ the_person.change_stats(obedience = -2, happiness = -1)
        "[title] rolls her eyes and tries to ignore you and [the_sex_person.fname] [the_position.verb], adjusting her cosplay outfit."
        return False
    if the_person.sluttiness < the_position.slut_requirement - 10:
        $ the_person.draw_person(display_transform = character_left_flipped)
        the_person "Honestly, senpai, you two are so embarrassing. Can't you keep it a little more private, especially during a cosplay photoshoot?"
        $ the_person.change_happiness(-1)
        "[title] looks away, trying to pretend she's not interested in what you and [the_sex_person.fname] are doing, fidgeting with her cosplay props."
        return False
    if the_person.sluttiness < the_position.slut_requirement:
        $ the_person.draw_person(display_transform = character_left_flipped)
        if not is_watching(the_person):
            the_person "You're really getting into it, aren't you, senpai? I suppose it's kind of hot, especially with the cosplay outfits..."
        $ the_person.change_slut(1, 30)
        "[title] watches you and [the_sex_person.fname] [the_position.verb], trying not to blush, her eyes fixed on the cosplay action."
        return True
    if the_person.sluttiness >= the_position.slut_requirement and the_person.sluttiness < the_position.slut_cap:
        $ the_person.draw_person(display_transform = character_left_flipped)
        if not is_watching(the_person):
            the_person "Oh, wow, senpai... this looks like so much fun. Can I join in on the cosplay action?"
        $ the_person.change_slut(1, 50)
        "[title] watches you and [the_sex_person.fname] [the_position.verb], her eyes sparkling with excitement, her cosplay outfit rustling softly."
        return True
    $ the_person.draw_person(emotion = "happy", display_transform = character_left_flipped)
    if renpy.random.randint(0, 1) == 0:
        the_person "You know, senpai, [the_sex_person.fname] is really getting into this. Maybe you should, uh, spice things up a bit, especially with the cosplay theme?"
    else:
        call watcher_position_comment(the_person, the_sex_person, the_position) from _call_watcher_position_comment_cosplay_sex_watch
    "[title] watches with interest as you and [the_sex_person.fname] [the_position.verb], appreciating the cosplay scene."
    return True

label cosplay_being_watched(the_person, the_watcher, the_position):
    $ title = the_watcher.fname if not the_watcher.is_stranger else "the stranger"
    if the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #They agree you should give it to her harder
        the_person "Hmph, I guess you're right, senpai."
        the_person "But don't think I'm going easy on you just because there's an audience, especially during a cosplay photoshoot..."
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [title] watching you and her [the_position.verb], her cosplay outfit rustling softly."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's super slutty and doesn't care what people think.
        the_person "You know, [title], I don't really care what you think, but it's pretty obvious you're turned on right now, especially with the cosplay theme."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #She's super slutty and encourages the watcher to be slutty.
        the_person "Oh, come on, [title]! Don't be shy! You know you want a taste of this cosplay action, senpai!"
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [title] watching you and her [the_position.verb], her eyes sparkling with excitement."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #She's into it and encouraged by the slut watching her.
        "[the_person.fname] glances at [title], adjusting her cosplay outfit."
        the_person "Yeah, I guess I can handle a little more... for now, senpai."
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [title] watching you and her [the_position.verb], her cosplay makeup sparkling in the light."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's into it but shamed by the prude watching her.
        the_person "Ugh, why do you have to be here, [title]? Can't you just leave me alone during our cosplay session?"
        $ the_person.change_stats(arousal = -1, slut = -1)
        "[the_person.title] seems uncomfortable with [title] nearby, fidgeting with her cosplay props."

    else: #the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #They're both into it but not fanatical about it.
        "[the_person.possessive_title!c] rolls her eyes at [title], adjusting her cosplay outfit."
        the_person "Whatever, [title], you're missing out on the cosplay fun. Maybe next time you'll get a chance, senpai."
        $ the_person.change_stats(arousal = 1, slut = 1, max_slut = 30)
        "[the_person.title] seems more comfortable [the_position.verbing] you with [title] around, enjoying the cosplay scene."

    return

label cosplay_work_enter_greeting(the_person):
    if the_person.happiness < 80 or the_person.love < 0:
        "[the_person.title] glances at you when you enter the room, her expression unreadable, her cosplay makeup slightly smudged."
        the_person "What do you want, senpai? I'm in the middle of a cosplay project."
        "She goes back to her work, not looking up again, her hands moving deftly as she adjusts her cosplay outfit."

    elif the_person.happiness > 130:
        if the_person.sluttiness > 40:
            the_person "Hey senpai, just the person I was hoping to see... especially since I'm in cosplay."
            "Her eyes sparkle with mischief as she leans against her desk, her cosplay outfit rustling softly."
            the_person "You know what they say: all work and no play makes for a dull cosplay girl."
            "She winks, inviting you to join her in some 'play', her cosplay makeup sparkling in the light."
        else:
            "[the_person.title] looks up from her work and smiles at you when you enter the room, her cosplay outfit catching your eye."
            the_person "Hey senpai, it's nice to have you stop by. You know, just to say hi and appreciate my cosplay skills."
            "She blushes slightly, looking away before quickly glancing back at you, her eyes shining with excitement."

    else:
        if the_person.sluttiness > 60:
            $ the_person.draw_person(position = "stand4")
            "[the_person.title] walks over to you when you come into the room, her hips swaying seductively in her cosplay outfit."
            the_person "Well, well, well, senpai. Look who decided to drop by and appreciate my cosplay skills."
            "She leans in close, her voice husky and sultry, her cosplay makeup sparkling in the light."
            the_person "I've been waiting for you, senpai. You know, just to catch up and discuss our next cosplay project."
            "She brushes her fingers against your arm, sending shivers down your spine, her cosplay outfit rustling softly."
        else:
            the_person "Hey senpai. Need anything? I mean, if you're not too busy... especially with our cosplay project."
            "She looks up at you, her eyes soft and inviting, her cosplay makeup slightly smudged."
    return

label cosplay_date_seduction(the_person):
    if the_person.is_girlfriend:
        "[the_person.possessive_title!c] grabs your hand and pulls you around to look at her, her cosplay outfit rustling softly."
        the_person "Hey, senpai, that was such a great time. So I was thinking... maybe we could take our cosplay to the next level?"
        $ mc.change_locked_clarity(30)
        if the_person.effective_sluttiness(["vaginal_sex", "condomless_sex"]) > 60 and the_person.wants_creampie and the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex >= 0 and the_person.opinion.creampies >= 0 and not the_person.on_birth_control and not the_person.knows_pregnant:
            if the_person.opinion.creampies > 0: #No condoms, loves creampies, she's basically asking you to knock her up. So... have her ask you to knock her up!
                the_person "You're probably just going to say no, but I really want to get knocked up by someone like you, senpai... especially in cosplay."
                the_person "So, are you going to make me pregnant or what? I bet you could give me some amazing kids, and we could have a whole family of cosplayers."
            else:
                the_person "I don't care if you don't use a condom, senpai. I just want you to fuck me and make me feel good, especially in this cosplay outfit."
                the_person "You're so much better than those other guys, anyway... especially when it comes to cosplay."
        elif the_person.effective_sluttiness(["vaginal_sex", "condomless_sex"]) > 60 and the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex > 0:
            the_person "Ugh, fine, senpai. If you really want to know, I'd rather not use a condom, especially during cosplay."
            the_person "But don't think I'm doing it for you or anything, senpai. It just feels better that way, especially in this cosplay outfit."
        elif the_person.effective_sluttiness(["vaginal_sex"]) > 50 and the_person.opinion.vaginal_sex > 0:
            the_person "You know, senpai, I didn't really want to go home with someone like you... but you're kind of growing on me, especially in cosplay."
            the_person "So, do you want to fuck me or what, senpai? I'm ready to take our cosplay to the next level."
        elif the_person.effective_sluttiness(["anal_sex"]) > 60 and the_person.opinion.anal_sex > 0:
            the_person "I don't know why I'm even bothering to ask you this, senpai... but do you want to fuck my ass, especially in this cosplay outfit?"
            the_person "It's not like I'm asking for much, but you're probably just going to say no anyway, senpai."
        elif the_person.effective_sluttiness(["sucking_cock"]) > 40 and the_person.opinion.giving_blowjobs > 0:
            the_person "You know, senpai, I'm not really in the mood to do this... but you're kind of cute when you're all worked up, especially in cosplay."
            the_person "So, do you want a blowjob or what, senpai?"
        elif the_person.effective_sluttiness() > 40 and the_person.opinion.being_covered_in_cum > 0:
            the_person "Ugh, fine, senpai. If you really want to know, I'd be okay with getting covered in your cum, especially during a cosplay photoshoot."
            the_person "But don't expect me to be all happy about it or anything, senpai."
        elif the_person.effective_sluttiness(["touching_body"]) > 40 and the_person.opinion.giving_tit_fucks > 0 and the_person.has_large_tits:
            the_person "I don't know why I'm even telling you this, senpai... but I'd be okay with sucking you off between my tits, especially in this cosplay outfit."
            the_person "But don't think I'm doing it because I like you or anything, senpai."
        else: #She's not very slutty, so she leaves the invitation open to interpretation
            the_person "You know, senpai, I don't really feel like going home with you or anything... but I guess I could be persuaded if you do something really good, especially in cosplay."
            the_person "So, what do you say, senpai? Want to take our cosplay to the next level?"
            "She smirks, leaving the invitation open-ended, her cosplay makeup sparkling in the light."
    elif the_person.is_affair:
        the_person "So my [the_person.so_title] won't be home tonight, I was thinking... maybe we could have some fun, senpai."
        "She reaches down and cups your crotch, rubbing it gently through your pants, her eyes sparkling with mischief."
        $ mc.change_locked_clarity(40)
        if the_person.wants_creampie and the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex >= 0 and the_person.opinion.creampies >= 0 and not the_person.on_birth_control and not the_person.knows_pregnant:
            if the_person.opinion.creampies > 0: #No condoms, loves creampies, she's basically asking you to knock her up. So... have her ask you to knock her up!
                the_person "Fine, let's go back to my place so you can pin me to the bed and creampie me all night long, senpai."
                the_person "I swear, just the thought of your cum inside me is making me want to puke and yet... I'm getting wet, especially in this cosplay outfit."
            else:
                the_person "Alright, let's go back to my place, senpai. You can pin me to the bed and fuck me bareback all night long, especially in cosplay."
                the_person "I hate how much I want this, but I do, senpai. So just fuck me up with your cock already."
        elif the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex > 0:
            the_person "Ugh, fine, senpai. Let's go back to my place and fuck all night, no condoms, especially in cosplay."
            the_person "I don't want to admit it, but I'm really looking forward to this, senpai."
        elif the_person.opinion.vaginal_sex > 0:
            the_person "Fine, let's go back to my place and you can pound my tight fucking pussy until I'm a wreck, senpai."
            the_person "I hate how much I enjoy this, but... I do, senpai. So do it, especially in this cosplay outfit."
        elif the_person.opinion.anal_sex > 0:
            the_person "Ugh, alright, senpai. Let's go back to my place so you can... you know, especially in cosplay."
            the_person "I don't want to admit it, but my ass is really excited for this, senpai."
        elif the_person.opinion.giving_blowjobs > 0:
            the_person "Fine, let's go back to my place and you can choke me out with your cock, senpai."
            the_person "I hate how much I want this, but I do, senpai. So just do it already, especially in cosplay."
        elif the_person.opinion.being_covered_in_cum > 0:
            the_person "Ugh, alright, senpai. Let's go back to my place, and you can cover me in your sperm all night, especially during a cosplay photoshoot."
            the_person "I hate how much I enjoy this, but... I do, senpai. So just do it."
        elif the_person.opinion.giving_tit_fucks > 0 and the_person.has_large_tits:
            the_person "Fine, let's go back to my place so I can... you know, senpai."
            the_person "I hate how much I enjoy this, but I do, senpai. So just do it already, especially in this cosplay outfit."
        elif the_person.opinion.cheating_on_men > 0:
            the_person "Ugh, fine, senpai. Let's go back to my place, and you can do all the things I tell my [the_person.so_title] I hate, especially in cosplay."
            the_person "I don't want to admit it, but I'm really looking forward to this, senpai."
        else:
            the_person "Ugh, let's go back to my place and make him really regret leaving me alone for the night, senpai."
    elif not the_person.has_significant_other:
        $ mc.change_locked_clarity(20)
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                the_person "Ugh, fine, senpai. I've had a blast, but there are a few more things I'd like to do with you, especially in cosplay. Want to come back to my place and find out what they are?"
            else:
                the_person "Whatever, senpai. You've been a blast. Want to come back to my place, have a few drinks, and see where things lead? I suppose, especially in cosplay."
        else:
            if the_person.love > 40:
                the_person "Fine, senpai, I don't want to say goodbye either. Tonight's been amazing, especially in cosplay. Do you want to come back to my place and have a few drinks?"
            else:
                the_person "Whatever, senpai. This might be crazy, but I had a great time tonight and you make me a little crazy, especially in cosplay. Do you want to come back to my place and see where things go? I don't know why I'm even asking."
    else:
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                $ mc.change_locked_clarity(20)
                the_person "Ugh, fine, senpai. I'm not done with you yet, especially in cosplay. Want to come back to my place? But don't think you're getting away with anything, senpai."
                the_person "My [the_person.so_title] won't be home until morning, so we would have plenty of time, especially for a cosplay photoshoot."
            else:
                $ mc.change_locked_clarity(20)
                the_person "Whatever, senpai. This might be crazy, but do you want to come back to have another drink with me, especially in cosplay? I suppose."
                the_person "My [the_person.so_title] is stuck at work and I don't want to be left all alone, especially during a cosplay session."
        else:
            if the_person.love > 40:
                $ mc.change_locked_clarity(20)
                the_person "Whatever, senpai. You're making me feel crazy, especially in cosplay. Do you want to come have a drink at my place, especially during a cosplay photoshoot? But don't think this means anything, senpai."
                the_person "My [the_person.so_title] won't be home until morning, and we have a big bed you could help me warm up, especially in cosplay."
            else:
                $ mc.change_locked_clarity(20)
                the_person "Whatever, senpai. This is crazy, but would you want to have one last drink at my place, especially in cosplay? My [the_person.so_title] won't be home until morning... I suppose."
    return

label cosplay_sex_end_early(the_person):
    if the_person.sluttiness > 50:
        if the_person.love > 40:
            if the_person.arousal_perc > 60:
                the_person "Ugh, really, senpai? You're done already? I was just getting into it, especially in this cosplay outfit... I mean, you're not exactly the most energetic partner I've ever had, especially during a cosplay session."
                the_person "But hey, I'll give you credit, senpai, you did try your best. Or at least, as best as you could, especially considering our cosplay roles."
            else:
                the_person "Well, I suppose that's it, senpai? I was ready to give you a lot more... But I guess you're not exactly the most enthusiastic about this whole situation, are you, especially when it comes to cosplay?"
        else:
            if the_person.arousal_perc > 60:
                the_person "Hmph, you're sure you're finished, senpai? I was really enjoying this cosplay session... You know, I don't usually do this, but I was actually getting kind of into it, especially with the cosplay theme."
                the_person "But I guess you're not exactly the most experienced, are you, senpai? I mean, it's not like I'm the one who needs to learn how to do this properly, especially when it comes to cosplay."
            else:
                the_person "I guess it was okay, I suppose, senpai. I mean, it's not like I was expecting much from you in the first place, especially during a cosplay session..."
    else:
        if the_person.love > 40:
            if the_person.arousal_perc > 60:
                the_person "Oh, come on, senpai, you can't leave me hanging like this... I mean, I was actually starting to enjoy this cosplay session!"
                the_person "But hey, I guess you're not exactly the most romantic guy out there, are you, senpai, especially when it comes to cosplay?"
            else:
                the_person "Well, that was a nice little interlude, I suppose, senpai. I mean, it's not like I'm the type to be all lovey-dovey and shit, especially during a cosplay photoshoot..."
        else:
            if the_person.arousal_perc > 60:
                the_person "Geez, I guess that was enough, senpai... I mean, I don't know why you even bother trying, you're not exactly the best at this, are you, especially when it comes to cosplay?"
            else:
                the_person "Good, it's over, senpai. Now let's get this over with. I mean, I've got better things to do than hang around with someone who can't even manage to get it right, especially during a cosplay session..."
    return

label cosplay_sex_take_control(the_person):
    if the_person.arousal_perc > 60:
        the_person "What do you think you're doing, senpai? Don't just leave me hanging like this! I mean, I'm the one who's supposed to be in control here, not you, especially during a cosplay session!"
        the_person "But hey, if you're not going to finish the job, then I will, senpai. And don't think for a second that I won't make you regret it, especially when it comes to our cosplay roles."
    else:
        the_person "Ugh, really, senpai? You're not even going to finish what you started? Fine, I'll do it myself then, especially since I'm the one in the cosplay outfit! And don't think you can just waltz in here and expect me to be all weak and submissive, senpai. I'm not that kind of girl, especially when it comes to cosplay."
    return

label cosplay_sex_beg_finish(the_person):
    the_person "Okay, fine, senpai, you want to play it cool? I'll let you off the hook this time, but just know that I'm going to make you pay for this, especially when it comes to our cosplay roles. And when I'm done, I'm going to make sure you know exactly who's in control here, especially during a cosplay session."
    return

label cosplay_sex_review(the_person, the_report):
    $ comment_position = the_person.pick_position_comment(the_report)
    if comment_position is None:
        return #You didn't actually do anything, no need to comment.

    $ used_obedience = the_report.get("obedience_used", False) #True if a girl only tried a position because you ordered her to.
    $ the_person.draw_person()  # make sure she stands up for talking with you

    #She's worried about her SO finding out because it was in public
    if the_report.get("was_public", False) and the_person.has_significant_other and the_person.opinion.cheating_on_men <= 0: #It was public and she cares.
        if the_person.is_affair: #Dialogue about her being into it, but you can't do this in case she gets caught.
            the_person "Ugh, this is so dangerous, senpai! I'm really getting into this cosplay session, but we can't get caught... especially not in public."
            the_person "What if someone sees us and tells my [the_person.so_title]? I'll never hear the end of it, especially in the cosplay community!"
        elif used_obedience:
            the_person "I don't know what you're thinking, senpai, but doing this in public is a bad idea! Someone might recognize me and tell my [the_person.so_title], especially if they see us in our cosplay outfits."
            mc.name "Don't worry, nobody's going to tell anyone, senpai. We're being careful, especially with our cosplay disguises."
            the_person "I hope you're right, senpai... I don't want anyone finding out about this, especially not in the cosplay community."
        else:
            $ the_person.call_dialogue("surprised_exclaim")
            the_person "Oh no, senpai, we're out in public! Someone might see us and tell my [the_person.so_title], especially if they recognize our cosplay outfits. I'll be so screwed!"
            mc.name "Don't worry, nobody's paying attention to us, senpai. Nobody's going to tell your [the_person.so_title], especially not in the cosplay community."
            the_person "I hope you're right, senpai... I don't want anyone knowing about this, especially not in the cosplay community."

    #She's single, but worried that you did in public.
    elif the_report.get("was_public", False) and (the_person.effective_sluttiness()+10*the_person.opinion.public_sex < comment_position.slut_cap):
        if used_obedience:
            the_person "Ugh, I don't know what you're thinking, senpai, but doing this in public is a bad idea! Everyone's staring at us like we're some kind of perverts, especially in our cosplay outfits..."
            the_person "I'll never live this down, senpai. People are going to talk about this for weeks, especially in the cosplay community!"
        else:
            the_person "Oh no, senpai, we're in public! Everyone's watching us and judging us for this, especially in our cosplay outfits..."
            mc.name "Don't worry, nobody really cares what we're doing, senpai. They're just curious, especially about our cosplay."
            the_person "I hope you're right, senpai, or I'm going to end up with a terrible reputation for this sort of thing, especially in the cosplay community..."

    elif the_report.get("girl orgasms", 0) > 2:
        if used_obedience:
            the_person "Oh fuck, senpai... baby... I loved what you did to me... I never knew being submissive could feel so good, especially in cosplay..."
            mc.name "I do enjoy when you keep begging me to make you cum again, senpai. It's almost like you're addicted to it, especially in our cosplay sessions."
            the_person "Shut up and kiss me, senpai..."
        else:
            the_person "I have never... cum that hard, senpai... It was just amazing... I guess I needed that, especially in our cosplay session."
            "She seems dazed by her orgasm as she tries to form coherent sentences, her cosplay outfit rustling softly."
            the_person "You really... know how to give a girl a good time, senpai... just gimme a second to catch my breath."
            mc.name "Take your time, senpai. I'm not going anywhere, especially not during our cosplay session."
            the_person "Thanks, senpai... I think I need a minute to recover before we can start again, especially in our cosplay outfits."

        call sex_review_trance(the_person) from _call_sex_review_trance_cosplay_sex_review

    #No special conditions, just respond based on how orgasmed and how slutty the position was.
    elif the_report.get("girl orgasms", 0) > 0 and the_report.get("guy orgasms", 0) > 0: #You both came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position cap, it was tame
            the_person "Ah, that was fucking nice, senpai... But I think we could go even further next time, especially in our cosplay session. I'm not afraid to push the limits, senpai."
            the_person "Doesn't that sound like fun, senpai? I'm getting wet just thinking about it, especially in our cosplay outfits."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "Ah, that was just what I needed, senpai! I think we're very compatible, especially in our cosplay roles."
            the_person "Let's do it again some time soon, okay, senpai? I want to see how much further we can go, especially in our cosplay session."

        elif used_obedience: #She only did it because she was commanded
            the_person "Fuck, I... I didn't think I was going to cum like that, senpai. I guess I just can't resist a good command, especially in our cosplay session."
            mc.name "Aren't you going to thank me, senpai? You obviously had a good time, especially in our cosplay outfits."
            the_person "Shut up and don't get too full of yourself, senpai."

        else: # She's surprised she even tried that.
            the_person "Oh fuck, that was intense, senpai! I didn't think I was going to take it so far, but it just felt right, especially in our cosplay session."
            the_person "Don't think that's going to happen every time though, alright, senpai? I'm not a slut, especially not in our cosplay community! I just like to push my boundaries sometimes."
        if the_person.love > 40:
            the_person "You know, I never thought I'd say this, senpai, but I think I might actually like this whole 'relationship' thing with you, especially in our cosplay roles."
        else:
            the_person "Well, that was fun, senpai. Let's do it again sometime, but not too soon, okay? I need to recover my dignity first, especially in our cosplay community."

    elif the_report.get("girl orgasms", 0) > 0: #Only she came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            the_person "Done already, senpai? Well, that's just not right. Next time I'm going to make sure we both cum and then some, especially in our cosplay session."
            the_person "I've got a few ideas that are going to blow you away, senpai, especially in our cosplay outfits."
            "She smiles mischievously, already imagining your next cosplay encounter."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "You're all done, senpai? Well, that was fucking hot either way, especially in our cosplay session."
            the_person "I'll repay the favour next time, alright, senpai? I promise. And maybe we can try something new, especially in our cosplay roles."
            "She leans in close, whispering in your ear, her cosplay outfit rustling softly."

        elif used_obedience: #She only did it because she was commanded
            the_person "That's it, senpai? I mean, not like I wanted to do anything more, I just thought you were going to finish, especially in our cosplay session."
            mc.name "Some other time, senpai. I just wanted to see what you look like when you cum, especially in our cosplay outfits."
            the_person "I... Fuck, well, I guess you got what you wanted, senpai. But don't think I'm going to make it easy for you next time, especially in our cosplay session."
            the_person "It could have been worse, I guess, senpai."

        else: # She's surprised she even tried that.
            the_person "Oh fuck, that was intense, senpai! You really know how to make a girl feel good, especially in our cosplay session."
            the_person "You're probably tired after all that work, senpai. I promise I'll repay the favour next time, okay, senpai? And maybe we can try something different, especially in our cosplay roles."
            "She smiles, already looking forward to your next cosplay encounter."

    elif the_report.get("guy orgasms", 0) > 0: #Only you came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            the_person "Hmph, you're all tired out already, senpai? That's so frustrating, especially in our cosplay session!"
            mc.name "Sorry, senpai, I'll make it up to you next time, especially in our cosplay roles."
            the_person "Well, I suppose I could be persuaded to try again, senpai. But don't expect any special treatment, especially in our cosplay community!"
            mc.name "Yeah, I think I could handle that, senpai."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "You're already done, senpai? Such a tease, especially in our cosplay session! Fine, I'll let you off this time, senpai..."
            mc.name "Sorry, senpai, I'll make it up to you next time, especially in our cosplay roles."
            the_person "You'd better, senpai, or you won't be hearing the word 'please' from me again, especially in our cosplay session!"

        elif used_obedience: #She only did it because she was commanded
            the_person "I suppose you're worn out from all that, senpai... We're finished then, especially in our cosplay session?"
            mc.name "Yeah, that's all for now, senpai."
            the_person "Fine, but don't think this means you get to slack off next time, senpai, especially in our cosplay roles!"

        else:  # She's surprised she even tried that.
            the_person "Wow, that was... quite an experience, senpai. I think I got a little carried away there, especially in our cosplay session."
            the_person "Maybe it's for the best that we stop here, senpai. I need to think about what I just did, especially in our cosplay roles..."

    elif the_person.energy < 10: #Nobody came and she's tired
        the_person "Ugh, I don't know, senpai... I'm just too exhausted, especially in our cosplay session. Another time, maybe?"
        mc.name "No worries, senpai. We'll do it another day, especially in our cosplay roles."
        the_person "Just don't expect any special treatment when we try again, got it, senpai?"

    else: #Nobody came.
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            the_person "Hmph, you're already done, senpai? What's the rush, especially in our cosplay session? We could've had more fun, especially in our cosplay outfits!"
            "She crosses her arms, pretending to be upset, her cosplay outfit rustling softly."
            the_person "You're such a spoilsport, senpai."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "We're stopping, senpai? But we were just getting to the good stuff, especially in our cosplay session!"
            mc.name "Sorry, senpai, maybe another time, especially in our cosplay roles."
            the_person "Yeah, maybe, senpai. You can't just leave a girl hanging like that, you know, especially in our cosplay community."

        elif used_obedience: #She only did it because she was commanded
            the_person "Well, I wasn't expecting that, senpai. I thought you had more in mind, especially in our cosplay session."
            mc.name "You aren't disappointed, are you, senpai?"
            the_person "No, no, senpai. I just...wanted to see where things would go, that's all, especially in our cosplay roles."
            the_person "It's fine, senpai. I'll just have to find someone else to take me further, especially in our cosplay community."

        else:  # She's surprised she even tried that.
            the_person "Ugh, you're probably right, senpai. We should stop now before we get too carried away, especially in our cosplay session."
            the_person "I don't want to do something I'll regret later, senpai. Let's just keep this casual, okay, especially in our cosplay community?"

    # Gave creampie while she is not on birth control (extra dialogue when she could get pregnant)
    if the_report.get("creampies", 0) > 0 and not the_person.on_birth_control and not the_person.knows_pregnant:
        the_person "Well, I guess we just made things a little more interesting, didn't we, senpai?"
        the_person "If I get pregnant, it'll serve you right for being so reckless, especially in our cosplay session!"

    $ del comment_position
    return

## Role Specific Section ##

label cosplay_improved_serum_unlock(the_person):
    mc.name "[the_person.title], now that you've had some time to get used to the lab, I want to talk to you about something, especially in regards to our cosplay research."
    the_person "Yeah, what's on your mind, senpai?"
    mc.name "Our R&D up to this point has been based on my old notes from university, but I think it's time we take our cosplay research to the next level."
    mc.name "There were some unofficial experiment results that suggested the effects might be enhanced by sexual arousal, especially when combined with cosplay."
    "[the_person.title] raises an eyebrow, her cosplay outfit rustling softly."
    the_person "Ah, so you noticed that too, senpai? I have a hypothesis that an orgasm opens chemical receptors that are normally blocked, especially during a cosplay session."
    mc.name "What if that's true? Does that open up any more paths for our cosplay research?"
    the_person "If it's true, I could leverage the effect to induce greater effects in our subjects, especially when they're in cosplay."
    "[the_person.possessive_title!c] grins mischievously, her eyes sparkling with excitement."
    the_person "We'll need to do some experiments to be sure, senpai. And I have just the thing in mind, especially when it comes to cosplay."
    mc.name "What kind of experiments, senpai?"
    the_person "I want to take a dose of serum myself, and you can record the effects, especially when I'm in cosplay."
    the_person "Then I'll...ahem...stimulate myself, and we can compare the effects after, especially when I'm still in my cosplay outfit."
    mc.name "Do you really think that's a good idea, senpai?"
    the_person "Not really, but we can't trust anyone else with this information if we're right, especially when it comes to our cosplay research."
    the_person "We might be able to make progress by brute force, but this is a chance to take our cosplay research to the next level, senpai."
    the_person "A finished dose of serum that raises my Suggestibility, especially when I'm in cosplay. The higher it gets, the better, senpai."
    the_person "Then we'll just need some time and some privacy for me to see what sort of effects my...ahem...stimulation will have, especially when I'm still in my cosplay outfit."
    return
## Taboo break dialogue ##

label cosplay_kissing_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 30:
        the_person "Fine, senpai, let's just get this over with. You've always been curious about kissing a cosplayer, right?"
        mc.name "That's not true, but I'll play along, especially since you're in cosplay."
        the_person "Hmph, whatever, senpai. Just shut up and kiss me already, especially since I'm still in my cosplay outfit."
        mc.name "Oh, I'm not going to shut up that easily, especially when it comes to cosplay."
        the_person "Suit yourself, senpai. I'll just have to find someone else who's willing to kiss me, especially in my cosplay role."
        mc.name "Hold on, wait a minute, [the_person.title]. I'm not going anywhere, especially when it comes to our cosplay session."
        the_person "Oh? You're not going anywhere, senpai? Then get over here and kiss me already, especially since I'm still in my cosplay outfit!"
        mc.name "Alright, alright, [the_person.title]. Here I come, especially since I love your cosplay."
    elif the_person.love >= 20:
        the_person "So we're doing this, huh, senpai? About time, if you ask me, especially since we're both in cosplay."
        mc.name "I guess we are, [the_person.title]. What do you think, especially about our cosplay roles?"
        the_person "It's about time we finally made out, senpai, especially in our cosplay session."
        mc.name "I'm glad you feel that way, [the_person.title], especially about our cosplay."
        the_person "Me too, senpai. Just be gentle, okay, especially since I'm still in my cosplay outfit?"
        mc.name "I will, [the_person.title], especially since I care about your cosplay."
    else:
        the_person "I don't know if this is a good idea, senpai. We're taking things too fast, aren't we, especially in our cosplay session?"
        mc.name "Are you scared, [the_person.title]?"
        the_person "No, senpai! I'm just...not sure if this is a good idea, especially since we're both in cosplay. But I trust you, senpai."
        mc.name "Good, [the_person.title]. Because I'm not going to let you back out now, especially since we're in the middle of our cosplay session."
        the_person "Hmph, fine, senpai. But if this is a mistake, it's on you, especially since you're the one who suggested we do this in cosplay."
        mc.name "It'll be worth it, I promise, [the_person.title], especially since our cosplay is so good."
    return

label cosplay_touching_body_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 30:
        the_person "Come on then, senpai, don't be shy. You've wanted to touch me for ages, haven't you, especially since we're in our cosplay session?"
        mc.name "Hey, I'm not that obvious, [the_person.title]!"
        the_person "Oh, please, senpai. I can see the way you look at me, especially since I'm still in my cosplay outfit."
        mc.name "Well, I can't help it if you're irresistible, [the_person.title], especially since you're rocking that cosplay look."
        the_person "Irresistible, senpai? Pfft, you're just trying to get in my pants, especially since we're in our cosplay roles."

    elif the_person.love >= 20:
        the_person "So you're ready for this, senpai?"
        "You nod, and she nods back, her cosplay outfit rustling softly."
        the_person "Me too, I think, senpai. I didn't think I'd be so nervous when you actually made a move, especially since we're in our cosplay session."
        mc.name "Just relax, [the_person.title]. You trust me, right, especially since we're in our cosplay roles?"
        the_person "Of course, senpai. Just don't expect me to be all touchy-feely about it, especially since we're in our cosplay session."

    else:
        the_person "I think you're getting a little ahead of yourself here, senpai [the_person.mc_title]."
        mc.name "What do you mean, [the_person.title]?"
        the_person "I mean I don't just let anyone feel me up, senpai. Maybe we should cool things down, especially since we're in our cosplay session."
        mc.name "You're not scared, are you, [the_person.title]?"
        the_person "Scared, senpai? Of course not, especially since we're in our cosplay roles!"
        mc.name "Well then just relax and go with it, [the_person.title]. It doesn't have to mean anything unless we want it to, especially since we're in our cosplay session."
        "You see her answer in her eyes before she says anything, her cosplay outfit rustling softly."
        the_person "You're so bad for me, senpai, you know that, especially since we're in our cosplay session?"
        mc.name "Well let me make up for it then, [the_person.title]."
        the_person "Hmm, maybe I'll let you, senpai, especially since we're in our cosplay roles."
    return

label cosplay_touching_vagina_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 35:
        the_person "Come on, senpai, don't be shy. You've been dying to touch my pussy, admit it, especially since we're in cosplay."
    elif the_person.love >= 20:
        the_person "Oh fuck, senpai, you've got my pussy tingling. I want you to touch it, especially since we're in our cosplay roles."
        mc.name "You sure, [the_person.title]? I don't want to push you too far, especially since we're in cosplay."
        the_person "No, senpai, I want it. I want you to touch me, especially since I'm still in my cosplay outfit."
    else:
        the_person "I don't know if we should be doing this, senpai... especially since we're in cosplay."
        mc.name "Just take a deep breath and relax, [the_person.title]. I'm just going to touch you a little, and if you don't like it I'll stop, especially since we're in our cosplay session."
        the_person "Just a little, senpai?"
        mc.name "Just a little, [the_person.title]. Trust me, it's going to feel amazing, especially since we're in cosplay."
        the_person "Hmm, okay, senpai. But don't think this means I'm easy, especially since I'm still in my cosplay outfit."
        mc.name "I wouldn't dream of it, [the_person.title]."
    return

label cosplay_sucking_cock_taboo_break(the_person):
    mc.name "I want you to do something for me, [the_person.title]."
    the_person "Oh yeah, senpai? What do you want me to do to you, especially since we're in cosplay?"
    mc.name "I want you to suck on my cock, [the_person.title]."
    if the_person.effective_sluttiness() >= 45:
        the_person "Mmm, I think I'm up for that, senpai. It's not going to be too big for me, is it, especially since we're in cosplay?"
        mc.name "I think you'll be able to handle it, [the_person.title], especially since you're still in your cosplay outfit."
        the_person "Alright, senpai, I don't want it choking me, especially since we're in our cosplay session."
        "She bites her lip and winks at you, her eyes sparkling with excitement."
        the_person "That's a lie, senpai. A little choking is okay, especially since we're in cosplay."

    elif the_person.love >= 30:
        the_person "I guess we've been dancing around it for a while, senpai, especially since we're in cosplay."
        "She bites her lip and looks your body up and down, her eyes lingering on your cosplay outfit."
        the_person "Alright, senpai, let's do this, especially since we're in our cosplay roles."

    else:
        the_person "Oh, I was wondering if this was going to come up, senpai... especially since we're in cosplay."
        "She laughs nervously and looks away from you, her cosplay outfit rustling softly."
        the_person "I don't know, senpai..."
        "You reach up and hold her chin, turning her head back to face you, especially since you're both in cosplay."
        mc.name "Don't overthink it, [the_person.title]. Just kneel down and suck on it for me, especially since we're in our cosplay session. If you don't like doing it, we can just forget it happened, especially since we're in cosplay."
        "You can see in her eyes the moment her resolve breaks, especially since she's still in her cosplay outfit. She bites her lip and nods, her eyes sparkling with excitement."
        the_person "Alright, senpai, let's do this, especially since I love our cosplay sessions together."
        "She slowly gets down on her knees, her eyes darting between your face and your cock with a mix of reluctance and curiosity, especially since you're both in cosplay."
        the_person "You know, senpai, I never thought I'd be doing this, especially since we're in cosplay. But I guess I'm willing to try new things for you, especially since I love your cosplay."
        "She takes a deep breath, her hand wrapping around the base of your cock as she leans in to take it in her mouth, especially since you're both in cosplay."
        "As she starts to suck, her eyes flash up to meet yours, a hint of defiance and challenge in them, especially since you're both in cosplay."
        the_person "Satisfied now, senpai?"
    return

label cosplay_licking_pussy_taboo_break(the_person):
    mc.name "I want to taste your pussy, [the_person.title]. Are you ready, especially since we're in cosplay?"
    if the_person.effective_sluttiness() >= 45:
        the_person "Hmph, I don't need your permission or anything, senpai, but fine. I'm ready, especially since I'm still in my cosplay outfit."
        mc.name "Good. But don't expect me to go easy on you just because it's your first time, especially since we're in our cosplay session."
        the_person "Oh, please, senpai. I've had better, especially in our cosplay roles."

    elif the_person.love >= 30:
        the_person "Finally, a man who knows how to treat a woman right, senpai. I'm ready when you are, especially since we're in our cosplay session."
        mc.name "That's what I like to hear, [the_person.title], especially since I love your cosplay."

    else:
        if the_person.has_taboo("sucking_cock"):
            the_person "You know, senpai, I never thought I'd see the day where you'd be willing to do this, especially in our cosplay session."
            "She bites her lip and smirks at you, her eyes sparkling with excitement."
            the_person "But I guess I'm not going to complain, senpai. Just don't expect me to be all grateful or anything, especially since I'm still in my cosplay outfit."

        else:
            the_person "About time you decided to make up for not sucking my cock, senpai, especially in our cosplay session."
            "She rolls her eyes and smiles, her cosplay outfit rustling softly."
            the_person "But fine, I'm ready, senpai. Just don't expect me to be all appreciative or anything, especially since we're in our cosplay roles."

    "She lies back, her eyes darting between yours and the area you're about to explore, especially since you're both in cosplay."
    the_person "And don't think this means I'm some kind of slut for letting you do this, senpai, especially since we're in our cosplay session."
    mc.name "I wouldn't dream of it, [the_person.title]. You're just being a good sport, right, especially since we're in cosplay?"
    the_person "Something like that, senpai..."
    "She closes her eyes, her face flushed with embarrassment as you start to lick her, especially since she's still in her cosplay outfit."
    return

label cosplay_vaginal_sex_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 60:
        the_person "Ugh, finally, senpai! I've been waiting for this moment all night, especially since we're in our cosplay session. Come on then, get that cock inside me and fuck me like you mean it, especially since I'm still in my cosplay outfit!"

    elif the_person.love >= 45:
        the_person "Alright, senpai, show me what you've got. I'm ready for this, especially since we're in our cosplay roles."
        mc.name "You better be, [the_person.title]. I'm going to make sure you remember this, especially since we're in our cosplay session."
        the_person "Bring it on, senpai! I can take it, especially since I love our cosplay sessions together."

    else:
        if the_person.has_taboo("anal_sex"):
            the_person "Well, well, well, senpai. Look at that cock. I guess we're going to find out just how tight my pussy is, especially since we're in our cosplay session."
            mc.name "That's the plan, [the_person.title]. And if you're a good girl, I might just make it worth your while, especially since I love your cosplay."
            the_person "Hmph, I'm always good, senpai. Now get to it before I change my mind, especially since we're in our cosplay roles."

        else:
            the_person "Oh, so that's what you're going to do with that big cock of yours, senpai. Well, I guess we'll see how it feels, especially since we're in our cosplay session."
            mc.name "We sure will, [the_person.title]. And if you're lucky, I might just make it feel even better, especially since I love our cosplay sessions together."
            the_person "Ugh, just get on with it already, senpai! I'm not getting any younger, especially since we're in our cosplay roles."

    return

label cosplay_anal_sex_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 75:
        the_person "Ugh, fine, senpai. But only because I can't resist you, especially since we're in our cosplay session. Your cock is so big, I'm surprised it fits in your pants, especially since you're still in your cosplay outfit!"
        "She seems more excited by the prospect than intimidated, especially since she loves our cosplay sessions together."
        mc.name "Don't worry, [the_person.title], I'll take it slow and make sure you're comfortable, especially since we're in our cosplay roles."

    elif the_person.love >= 60:
        the_person "Are you sure you want to do this, senpai? I'm not exactly the most experienced person when it comes to anal, especially since we're in our cosplay session..."
        mc.name "I'll be gentle, don't worry, [the_person.title], especially since I love your cosplay."
        the_person "Alright, senpai, but if it hurts too much, I'm stopping, especially since we're in our cosplay roles."

    else:
        if the_person.has_taboo("vaginal_sex"):
            the_person "Wait, senpai, are you sure you want to do this? My ass might be too tight for your cock, especially since we're in our cosplay session!"
            mc.name "I'll make it fit, [the_person.title], but you might feel a little sore afterward, especially since we're in our cosplay roles."
            the_person "Oh, great, senpai. Just what I needed, especially since I love our cosplay sessions together."

        else:
            the_person "Come on, senpai, let's just get this over with. I don't know what's gotten into me today, especially since we're in our cosplay session."
            mc.name "Are you sure you're okay with this, [the_person.title]?"
            the_person "Of course, senpai, I'm just... nervous, especially since I'm still in my cosplay outfit. And a little embarrassed, especially since we're in our cosplay roles. But let's just do this already, senpai!"
            "She blushes and looks away, her cosplay outfit rustling softly."
            mc.name "Alright, [the_person.title], let's get started then."
            the_person "Hurry up, senpai, I'm ready when you are, especially since I love our cosplay sessions together."
    return

label cosplay_condomless_sex_taboo_break(the_person):
    if the_person.knows_pregnant:
        the_person "Ugh, you really want to do it without a condom, senpai? Fine, but don't say I didn't warn you, especially since we're in our cosplay session."
        if the_person.wants_creampie:
            the_person "If you're going to cum inside me, please make it worth my while, especially since I'm still in my cosplay outfit."
        else:
            the_person "Just make sure to cover me with your... you know, stuff, especially since we're in our cosplay roles."

    elif the_person.opinion.bareback_sex > 0:
        the_person "Whatever, senpai, you want to do it bareback, huh? Just don't say I didn't warn you, especially since we're in our cosplay session."
        if the_person.on_birth_control:
            the_person "I'm on the pill, so you don't have to worry about it, especially since I'm responsible when it comes to our cosplay."
            $ the_person.update_birth_control_knowledge()
        elif the_person.wants_creampie:
            the_person "But if you're going to cum inside me, you'd better make it worth my while, especially since I love our cosplay sessions together."
        elif the_person.opinion.creampies < 0:
            the_person "Just don't get me pregnant, okay, senpai? That would be a huge pain, especially since we're in our cosplay roles."
        else:
            the_person "Alright, just make sure you pull out this time, especially since we're in our cosplay session."

    elif the_person.love > 60:
        if the_person.on_birth_control:
            the_person "Ugh, fine, senpai, I'm on the pill. Don't say I didn't warn you, especially since we're in our cosplay session."
            $ the_person.update_birth_control_knowledge()
        elif the_person.wants_creampie:
            the_person "You're always trying to make me do stupid things, aren't you, senpai? Fine, if we're going to do this, make it worth my while, especially since I love our cosplay sessions together."
            mc.name "Are you on the pill, [the_person.title]?"
            "She rolls her eyes, her cosplay outfit rustling softly."
            the_person "No, I'm not, senpai. But if you're going to cum inside me, you'd better make it worth it, especially since we're in our cosplay roles."
            $ the_person.update_birth_control_knowledge()
        elif the_person.opinion.creampies < 0:
            the_person "You're always trying to make me do stupid things, aren't you, senpai? Fine, just don't get me pregnant, especially since we're in our cosplay session."
            the_person "I'm not ready for that kind of responsibility again, especially since we're in our cosplay roles."
        else:
            the_person "You're always trying to make me do stupid things, aren't you, senpai? Fine, just make sure you pull out this time, especially since we're in our cosplay session."
            if the_person.kids == 0:
                the_person "I need you to pull out though, senpai. I'm not quite ready to be a mother, even with you, especially since we're in our cosplay roles."
            elif the_person.kids == 1:
                the_person "I need you to pull out though, senpai. I've already got a kid, I don't need another one, especially since we're in our cosplay session."
            else:
                the_person "I need you to pull out though, senpai. I've already got kids, I don't need another one, especially since we're in our cosplay roles."

    else:
        if the_person.on_birth_control:
            the_person "Hmph, you want to get busy without a rubber, senpai? Well, I'm on the pill, so I guess it's fine, especially since I'm responsible when it comes to our cosplay. Just don't expect any special treatment, especially since we're in our cosplay session."
            $ the_person.update_birth_control_knowledge()
        elif the_person.has_taboo("vaginal_sex"):
            the_person "You're really not going to use a condom, senpai? I'm not on the pill, so we could end up with a little surprise, especially since we're in our cosplay session."
            $ the_person.update_birth_control_knowledge()
            the_person "Or is this your sneaky plan to make a baby out of me, especially since we're in our cosplay roles?"
            mc.name "I swear I'll pull out, [the_person.title]. I want our first time to be memorable, especially since we're in our cosplay session."
            "She crosses her arms and gives a half-hearted sigh, her cosplay outfit rustling softly."
            the_person "Ugh, fine, senpai. But you better pull out, or you'll regret it, especially since we're in our cosplay roles."
        else:
            the_person "You're really not going to use a condom, senpai? I'm not on the pill, so we could end up with a little surprise, especially since we're in our cosplay session."
            $ the_person.update_birth_control_knowledge()
            the_person "Or is this your sneaky plan to make a baby out of me, especially since we're in our cosplay roles?"
            mc.name "I promise I'll pull out, [the_person.title]. It'll feel so much better without anything between us, especially since we're in our cosplay session."
            the_person "God, I know, senpai. I'm trying to be rational here, not some lust-driven animal, especially since we're in our cosplay roles."
            "She huffs and puffs, her cosplay outfit rustling softly."
            the_person "Fine, no condom, senpai. Just remember to pull out, got it? Good, especially since we're in our cosplay session."
    return
### DIALOGUE ###

label cosplay_underwear_nudity_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > 30 - (the_person.opinion.skimpy_outfits * 5):
        the_person "You want to see me in my underwear, huh, senpai? It's about time you asked, especially since we're in our cosplay session."
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "What are we waiting for then, let's get this off of you, especially since I love your cosplay."
        else:
            mc.name "Yeah, yeah, [the_person.title]. We've been over this. You're not exactly subtle about it, especially since you're still in your cosplay outfit."
            the_person "Shut up, senpai! I just don't want you to get the wrong idea, especially since we're in our cosplay roles."
            mc.name "Wrong idea, [the_person.title]? Like how you're not wearing anything under this skirt, especially since it's part of your cosplay?"
            the_person "Ugh, fine, senpai. But don't say I didn't warn you, especially since we're in our cosplay session."

    elif the_person.love > 15:
        the_person "You want me to strip me down a little, senpai? It's about time, I was wondering why you were taking things so slow, especially since we're in our cosplay session."
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "Oh, don't give me that, [the_person.title]. You know you want to show off, especially since you love our cosplay sessions together."
            the_person "Fine, senpai, but if this gets out of hand, I'm blaming you, especially since we're in our cosplay roles."
            mc.name "Promise, [the_person.title]?"
            the_person "Yeah, yeah, senpai. Now get this [the_clothing.display_name] off, especially since it's part of my cosplay outfit."

        else:
            mc.name "Yeah, I know, [the_person.title]. You've been teasing me for weeks, especially since we're in our cosplay session."
            the_person "Teasing, senpai? I'm just being friendly, especially since I love our cosplay sessions together."
            mc.name "Right, [the_person.title]. Now let's get you out of these clothes, especially since they're part of your cosplay outfit."
            the_person "Ugh, fine, senpai. But don't think this means I'm going easy on you, especially since we're in our cosplay roles."
            "She slowly starts taking [the_clothing.display_name] off, her cosplay outfit rustling softly."

    else:
        the_person "You really want to see me like this, senpai? Fine, but don't say I didn't warn you, especially since we're in our cosplay session."
        the_person "If you take my [the_clothing.display_name] I'll only have my underwear on, you know that, senpai?"
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "Yeah, that's kind of the point, [the_person.title], especially since we're in our cosplay session."
            "She shakes her head and laughs to herself, her cosplay outfit rustling softly."
            the_person "Whatever, senpai, but if you think I'm doing this because I want to, especially since we're in our cosplay roles..."
        else:
            mc.name "Yeah, I know, [the_person.title]. You're not exactly shy, especially since you're still in your cosplay outfit."
            the_person "Hey, senpai, I'm just being cautious, especially since we're in our cosplay session. You can't blame a girl for being careful, especially when it comes to cosplay."
            mc.name "Of course not, [the_person.title]. Now let's get you out of these clothes, especially since they're part of your cosplay outfit."
            the_person "Fine, senpai, but don't think this means I'm going easy on you, especially since we're in our cosplay roles."
    return

label cosplay_bare_tits_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > (40 - the_person.opinion.showing_her_tits * 5):
        the_person "Why do you want to see my tits now, all of a sudden, senpai? Like I don't already know you're checking me out, especially since we're in our cosplay session."
        if the_person.has_large_tits:
            "She reluctantly shakes her chest for you, jiggling the [the_person.tits_description] hidden underneath her [the_clothing.display_name], especially since it's part of her cosplay outfit."
        else:
            "She reluctantly shakes her chest and gives her [the_person.tits_description] a little jiggle, especially since she's still in her cosplay outfit."
        the_person "You're always so eager, aren't you, senpai? I guess I can show you, but don't get too excited, especially since we're in our cosplay session."
        if the_person.has_large_tits:
            mc.name "Oh, I've been looking, [the_person.title]. Now let's get those puppies out where I can enjoy them, especially since I love your cosplay."
        else:
            mc.name "Oh, I've been looking, [the_person.title]. Now let's get those cute little things out, especially since they're part of your cosplay outfit."

    elif the_person.love > 25:
        the_person "Are you really sure you want to see my tits, senpai?"
        if the_person.has_large_tits:
            "She rolls her eyes and shakes her chest, jiggling her nice [the_person.tits_description], barely restrained by her [the_clothing.display_name], especially since it's part of her cosplay outfit."
        else:
            "She rolls her eyes and shakes her chest, giving her [the_person.tits_description] a little jiggle, especially since she's still in her cosplay outfit."
        mc.name "Of course I am, [the_person.title]. You know I love your tits, especially since we're in our cosplay session."
        the_person "Well, I suppose you're entitled to see them then, senpai... but don't think this means I'm going to start showing them off to everyone, especially since we're in our cosplay roles."

    else:
        the_person "Wait, no, senpai! Don't look at me like that! You should at least ask a girl before you try and put her tits on full display, especially since we're in our cosplay session!"
        mc.name "Come on, [the_person.title], don't be like that. I bet your tits look great, especially since you're still in your cosplay outfit."
        the_person "They do, senpai, but I still feel a little self-conscious about being naked around you, alright, especially since we're in our cosplay roles?"
        mc.name "There's no need to be, [the_person.title]. Just relax and let me take your [the_clothing.display_name] off for you, especially since it's part of your cosplay outfit."
        the_person "Ugh, fine, senpai... but don't think this means I'm going to start showing off my body to everyone, especially since we're in our cosplay session!"
    return

label cosplay_bare_pussy_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > (50 - the_person.opinion.showing_her_ass * 5):
        the_person "So you want to see my pussy, huh, senpai? Like I don't already know you're thinking about it, especially since we're in our cosplay session."
        if the_person.has_taboo("touching_vagina"):
            "She reluctantly lifts her hips, allowing you to slowly remove her [the_clothing.display_name] and reveal her pussy, especially since it's part of her cosplay outfit."
        else:
            "She lifts her hips, giving you a quick glimpse of her pussy before covering it back up, especially since she's still in her cosplay outfit."
        the_person "Well, you got your wish, senpai. Don't say I didn't warn you, especially since we're in our cosplay roles."

    elif the_person.love > 35:
        the_person "You want to see my pussy, really, senpai? Are you sure you're ready for that, especially since we're in our cosplay session?"
        if the_person.has_taboo("touching_vagina"):
            mc.name "I think I am, [the_person.title]. I've been wanting to see it for a while, especially since I love your cosplay."
            the_person "Hmm, well... I suppose you've earned it, senpai. Just remember, you asked for this, especially since we're in our cosplay roles."
        else:
            mc.name "I've already felt it up, [the_person.title], I thought I should see it too, especially since we're in our cosplay session."
            the_person "You really are persistent, aren't you, senpai? Fine, go on then, especially since I love our cosplay sessions together."

    else:
        the_person "Hold on, senpai, you're not getting me out of my [the_clothing.display_name] that easily, especially since we're in our cosplay session!"
        if the_person.has_taboo("touching_vagina"):
            mc.name "Come on, [the_person.title], just let me see it. I promise I'll be gentle, especially since I care about your cosplay."
            the_person "You're such a liar, senpai... But fine, go ahead, especially since we're in our cosplay roles."
        else:
            mc.name "I've already felt your pussy up, [the_person.title], I want to get a look at it now, especially since we're in our cosplay session."
            the_person "You're so pushy, senpai! Alright, but don't say I didn't warn you, especially since we're in our cosplay roles."
    return

# label cosplay_facial_cum_taboo_break(the_person):

#     return

# label cosplay_mouth_cum_taboo_break(the_person):

#     return

# label cosplay_body_cum_taboo_break(the_person):

#     return

label cosplay_creampie_taboo_break(the_person):
    if the_person.wants_creampie:
        if the_person.knows_pregnant:
            the_person "You want to get me pregnant, huh, senpai? Fine, I suppose it's about time someone knocked me up, especially since we're in our cosplay session."
            "She sighs happily, seeming almost resigned to the idea, especially since she's still in her cosplay outfit."

        elif the_person.on_birth_control:
            if the_person.has_significant_other:
                the_person "Oh my god, I'm such a horrible [the_person.so_girl_title], senpai! But I needed this so badly, especially since we're in our cosplay roles."
                the_person "Maybe if we're lucky, my [the_person.so_name] won't find out, especially since we're keeping this a secret from our cosplay friends."
                "She looks at you with a mischievous grin, her cosplay outfit rustling softly."
            else:
                the_person "Oh my god, I needed this so badly, senpai! Ah... I guess I'll just have to deal with the consequences, especially since we're in our cosplay session."

        elif the_person.effective_sluttiness() > 75 or the_person.opinion.creampies > 0:
            if the_person.has_significant_other:
                the_person "You want to get me pregnant, senpai? Fine, I suppose it's about time someone knocked me up, especially since we're in our cosplay roles."
                the_person "Maybe my [the_person.so_name] will finally notice how unhappy I am and do something about it, especially since we're in our cosplay session."

            else:
                the_person "You want to get me pregnant, senpai? Fine, I suppose it's about time someone knocked me up, especially since we're in our cosplay session."
                the_person "I guess I'll just have to deal with the consequences, especially since we're in our cosplay roles."

            "She sighs happily, but with a hint of annoyance, especially since she's still in her cosplay outfit."
            the_person "How long until you're ready for round two, senpai? I want as much of your cum inside my pussy as possible, especially since we're in our cosplay session."
            the_person "Just don't expect me to be all happy and grateful about it, especially since we're in our cosplay roles."

        else:
            if the_person.has_significant_other:
                the_person "Oh fuck, senpai... I'm such a terrible [the_person.so_girl_title]!"
                "She sighs happily, but with a hint of guilt, especially since she's still in her cosplay outfit."
                the_person "But that felt so good, especially since we're in our cosplay session..."
            else:
                the_person "Oh fuck, senpai, that was so risky."
                "She sighs happily, but with a hint of annoyance, especially since she's still in her cosplay outfit."
                the_person "But it felt so good, especially since we're in our cosplay session..."
            the_person "I'll just have to hope you haven't knocked me up, senpai. We really shouldn't do this again, my luck is going to run out at some point, especially since we're in our cosplay roles."
            the_person "Besides, I'm not exactly thrilled about the idea of being tied down to a man right now, especially since we're in our cosplay session."

    else:
        if the_person.knows_pregnant:
            the_person "Ugh, you're kidding me, right, senpai? You got me pregnant, especially since we're in our cosplay session?"

        elif not the_person.on_birth_control:
            the_person "Seriously, senpai? You didn't even use protection? What if I get pregnant, especially since we're in our cosplay roles?"

            if the_person.has_significant_other:
                the_person "What if you just got me pregnant, senpai? I would be the worst [the_person.so_girl_title] of all time, especially since we're in our cosplay session!"

            else:
                the_person "What if I get pregnant, senpai? I'm not ready for that kind of responsibility, especially since we're in our cosplay session!"
            the_person "You'd better start buying me chocolate and flowers to make up for this, especially since we're in our cosplay roles."
            the_person "Next time, we're using condoms, or we're not doing it at all, senpai! You got it, especially since we're in our cosplay session?"

        elif the_person.has_significant_other:
            the_person "Did you really just creampie me after I told you to pull out, senpai?"
            "She sighs unhappily, especially since she's still in her cosplay outfit."
            the_person "God, I'm such a terrible [the_person.so_girl_title], senpai. Maybe next time I'll make you wear a condom as punishment, especially since we're in our cosplay roles."

        elif the_person.opinion.creampies < 0:
            the_person "Ugh, this is so unpleasant, senpai. Couldn't you have at least made it worth my while, especially since we're in our cosplay session?"
            "She rolls her eyes, especially since she's still in her cosplay outfit."
            the_person "Next time, at least have the decency to ask if I'm in the mood for a creampie, senpai. Or better yet, don't even bother if you're just going to be careless like this, especially since we're in our cosplay roles."
            the_person "Next time, ask me first if I want a baby, senpai, especially since we're in our cosplay session."

        else:
            the_person "Are you serious right now, senpai? You're really going to give me that attitude after you just...you know, especially since we're in our cosplay session?"
            "She huffs and crosses her arms, especially since she's still in her cosplay outfit."
            the_person "I swear, senpai, you're going to be the death of me. Fine, next time, at least have the decency to clean up after yourself, especially since we're in our cosplay roles."
    return

label cosplay_anal_creampie_taboo_break(the_person):
    if the_person.opinion.anal_creampies > 0:
        if the_person.effective_sluttiness() > 75 or the_person.opinion.anal_creampies > 1:
            if the_person.has_significant_other:
                the_person "Ugh, fine, senpai. I won't tell my [the_person.so_title] about this. But don't think I'm enjoying this, especially since we're in our cosplay session..."
                "She says this while wincing in pleasure as you fill her ass with your cream, her cosplay outfit rustling softly."
                the_person "Ugh, it's just... weirdly satisfying, I guess, especially since we're in our cosplay roles..."
            else:
                the_person "Ugh, finally, senpai! You're actually doing this! I've been waiting for this forever, especially since we're in our cosplay session..."
                the_person "Okay, okay, I know it's wrong, but... it feels so good, especially since we're in our cosplay roles..."
            "She bites her lip, trying to contain her excitement, especially since she's still in her cosplay outfit."
            the_person "I guess it's nice... having your cum in my ass, senpai..."

        else:
            if the_person.has_significant_other:
                the_person "Ugh, what are you doing, senpai? My [the_person.so_title] is going to kill me if he finds out about this, especially since we're in our cosplay session..."
                "She moans softly as you continue to fill her ass, her cosplay outfit rustling softly."
                the_person "Ugh, I can't believe I'm letting you do this, senpai... It's just so taboo, especially since we're in our cosplay roles..."
            else:
                the_person "Ugh, promise you'll do this again, senpai? I can't believe I'm saying this, but... it's kind of hot, especially since we're in our cosplay session..."
                the_person "All that cum in my tight little ass, senpai..."

    else:
        if the_person.has_significant_other:
            the_person "Ugh, seriously, senpai? You couldn't pull out? My [the_person.so_title] is going to kill me, especially since we're in our cosplay session..."
            "She starts to squirm and try to get away from you, her cosplay outfit rustling softly."
            the_person "Next time, just shoot your load on my ass, okay, senpai?"
        elif the_person.opinion.anal_creampies < -1:
            the_person "Ugh, seriously, senpai? You can't even follow simple instructions? My ass is not a creampie dispenser, especially since we're in our cosplay roles!"
        else:
            the_person "Ugh, not inside, senpai! My ass is not a dirty little secret, although that sounds kind of hot, especially since we're in our cosplay session..."
    return

label cosplay_dual_penetration_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 75:
        the_person "Ugh, why do you always have to push me to do this, senpai? Fine, but don't expect me to enjoy it, especially since we're in our cosplay session..."
        "She rolls her eyes and crosses her arms, clearly annoyed but still willing to go through with it, especially since she's still in her cosplay outfit."
        mc.name "Don't worry, it'll be worth it, [the_person.title]."
        the_person "I doubt that, senpai, but whatever, especially since we're in our cosplay roles."

    elif the_person.love >= 60:
        the_person "You're really sure about this, senpai? It's going to be a tight fit, especially since we're in our cosplay session..."
        mc.name "I'll make sure it fits perfectly, [the_person.title]."
        the_person "Ugh, just be careful not to hurt me, okay, senpai? I don't want any scars, especially since we're in our cosplay roles..."

    else:
        if the_person.has_taboo("vaginal_sex"):
            the_person "Are you sure my pussy wouldn't be tight enough for you, senpai? I mean, I've never done this before, especially since we're in our cosplay session..."
            mc.name "It's okay, [the_person.title], I'll make it fit. Just try to relax, especially since we're in our cosplay roles."
            the_person "Ugh, this is so embarrassing, senpai..."

        else:
            the_person "Ugh, fine, senpai. I guess we're doing this, right? I mean, I can't back out now, especially since we're in our cosplay session..."
            mc.name "Are you sure you're ready for this, [the_person.title]?"
            the_person "Yeah, whatever, senpai. Let's just get this over with, especially since we're in our cosplay roles..."
    return

label cosplay_sleepover_yourplace_response(the_person): #Invited her over to spend the night
    if the_person.love >= 70:
        the_person "Ugh, fine, senpai. I'll come over. But don't expect me to be all lovey-dovey or anything, especially since we're in our cosplay session..."
        mc.name "I wouldn't dream of it, [the_person.title]. We'll just have a good time, especially since I love your cosplay."
        the_person "Yeah, yeah, senpai. Just don't get too close, okay? I don't like cuddling or anything, especially since we're in our cosplay roles."

    elif the_person.sluttiness >= 80:
        the_person "Oh god, senpai, I'm so excited! I'll come over and we can have a wild night, especially since we're in our cosplay session!"

    else:
        the_person "I guess I could come over, senpai... But don't expect me to do anything I'm not comfortable with, okay, especially since we're in our cosplay session?"
    return

label cosplay_sleepover_herplace_response(the_person): #Spending the night at her place
    if the_person.love >= 70:
        the_person "Ugh, fine, senpai. Come over and stay the night, but don't expect me to be all lovey-dovey or anything, especially since we're in our cosplay session..."
        mc.name "I wouldn't dream of it, [the_person.title]. We'll just have a good time, especially since I love your cosplay."
        the_person "Yeah, yeah, senpai. Just don't get too close, okay? I don't like cuddling or anything, especially since we're in our cosplay roles."

    elif the_person.sluttiness >= 80:
        the_person "Oh god, senpai, I'm so excited! Come over and we can have a wild night, especially since we're in our cosplay session!"

    else:
        the_person "I guess you can come over, senpai... But don't expect me to do anything I'm not comfortable with, okay, especially since we're in our cosplay session?"
    return

label cosplay_sleepover_yourplace_sex_start(the_person):
    "[the_person.title] rolls her eyes and walks over to you, her expression a mix of annoyance and desire, especially since she's still in her cosplay outfit."
    the_person "Ugh, fine, senpai. Let's get this over with. Just don't expect me to be all lovey-dovey or anything, especially since we're in our cosplay roles..."
    return

label cosplay_sleepover_herplace_sex_start(the_person):
    the_person "Ugh, finally, senpai. Get over here already, especially since we're in our cosplay session."
    "She smirks and crosses her arms, clearly annoyed but still eager for the action to begin, especially since she's still in her cosplay outfit."
    mc.name "Are you ready, [the_person.title]?"
    the_person "Hah, senpai! Like I need to be ready for this, especially since we're in our cosplay roles. Just get in here and do your worst, especially since I love our cosplay sessions together."
    "She leans back on the couch, her legs spread wide in invitation, especially since she's still in her cosplay outfit."
    the_person "Hurry up, senpai, I'm not getting any younger, especially since we're in our cosplay session!"
    return

label cosplay_sleepover_impressed_response(the_person):  #If you've made her cum a lot
    the_person "Ugh, senpai, you're really good at that... Don't expect me to admit it, but you're making me feel things, especially since we're in our cosplay session..."
    "She rolls her eyes and smirks, trying to hide her true feelings, especially since she's still in her cosplay outfit."
    mc.name "You want more, [the_person.title]?"
    the_person "Hmph, maybe, senpai. But don't think you've won me over or anything, especially since we're in our cosplay roles. I can still handle more, especially since I love our cosplay sessions together..."
    "[the_person.title] lies down in bed, her breathing still ragged from the previous rounds, especially since she's still in her cosplay outfit."
    the_person "I might be able to go for another round, senpai... But don't get too excited, I'm not making any promises, especially since we're in our cosplay session!"
    return

label cosplay_sleepover_good_response(the_person):  #If you've made her cum
    the_person "Ugh, fine, senpai. That wasn't too terrible, I suppose, especially since we're in our cosplay session."
    "She rolls her eyes and smirks, trying to hide her true feelings, especially since she's still in her cosplay outfit."
    mc.name "You want more, senpai?"
    $ the_person.draw_person(position = "missionary")
    the_person "Hmph, maybe, senpai. But don't think you've won me over or anything, especially since we're in our cosplay roles. I can still handle more, especially since I love our cosplay sessions together..."
    "[the_person.title] lies down in bed, her breathing still ragged from the previous round, especially since she's still in her cosplay outfit."
    the_person "Could you give me another pounding before we go to sleep, senpai? But don't expect me to be all lovey-dovey or anything, especially since we're in our cosplay session..."
    return

label cosplay_sleepover_bored_response(the_person):  #If she hasn't cum yet
    the_person "Ugh, is that the best you can do, senpai? I was expecting more than that from you, especially since we're in our cosplay session..."
    "She crosses her arms and looks at you with a bored expression, clearly unimpressed, especially since she's still in her cosplay outfit."
    mc.name "What's wrong, senpai?"
    the_person "You know, just do better, senpai. I expect more from you than this, especially since we're in our cosplay roles..."
    "She rolls her eyes and smirks, still rubbing her pussy in anticipation, especially since she's still in her cosplay outfit."
    the_person "You'd better step it up if you want to keep me interested, senpai... especially since I love our cosplay sessions together."
    return


#==================================================================
# add more cosplay personality, use different words, and movements.
# update all the following the_person and movements with cosplay personality. Use Marin Kitagawa from My Dress-Up Darling or Lilysa Amano from 2.5 Dimensional Seduction, for ideas, keep to the structure. Movements in quotations:
### DIALOGUE ###
