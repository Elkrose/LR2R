### PERSONALITY CHARACTERISTICS ###
# Bimbo is slang for a conventionally attractive, sexualized naïve woman. The term was originally used in the United States as early as 1919 for an unintelligent or brutish man. As of the early 21st century, the "stereotypical bimbo" appearance became akin to that of a physically attractive woman.
#However, as with most identities, the idea of the 'bimbo' has evolved and here is what it means today. The term 'bimbofication' is a colloquial term derived from the term 'bimbo' which is understood to mean, 'an attractive woman who is pretty, sexualised, naive and uneducated'.
#==================================================================
# add more bimbo personality, use different words, and movements.
# update all the following the_person and movements with bimbo personality. Use Cher Horowitz from Clueless or Elle Woods from Legally Blonde, for ideas, keep to the structure. Movements in quotations:
### DIALOGUE ###

label bimboed_introduction(the_person):
    mc.name "Hey, can I talk to you for a sec?"
    "[the_person.title] turns around, a totally clueless expression on her face, like she's trying to figure out who you are and why you're talking to her."
    the_person "Oh my god, like, what's up?"
    mc.name "I'm sorry if this is awkward, but you seem like an interesting person."
    "[the_person.title] giggles and flips her hair, a totally adorable smile spreading across her face."
    the_person "Omigod, thanks! I'm like, totally interesting, I guess."
    mc.name "Well, I was wondering if you'd like to... do something together sometime."
    "[the_person.title] squeals with excitement, like she's just been asked to the prom or something."
    the_person "Oh my god, like, that would be so much fun! What did you have in mind, like, a date or something?"
    mc.name "Haha, yeah, something like that. We could maybe grab coffee or something."
    "[the_person.title] nods enthusiastically, like she's just been given the best idea ever."
    the_person "That sounds, like, totally perfect! I love coffee, and I love... well, I don't know you yet, but I'm sure you're, like, totally awesome."
    mc.name "Heh, thanks? I'll take that as a compliment."
    $ the_person.set_title()
    $ the_person.set_possessive_title()
    the_person "So, like, what's your name, anyway?"
    mc.name "I'm [mc.name]. Nice to meet you..."
    the_person "My name is [the_person.name], and I'm like, totally happy to meet you too!"
    $ the_person.change_happiness(1)
    return

label bimboed_greetings(the_person):
    if the_person.love < 0:
        the_person "Oh my god, like, why are you always so annoying?"
        "She rolls her eyes and tosses her hair, clearly uninterested in talking to you."
    elif the_person.happiness < 90:
        the_person "Hey, like, hi. I'm having a totally bad day, but I guess it's nice to see you or whatever."
        "She sighs and fiddles with her nails, looking distracted and unenthused."
    else:
        if the_person.sluttiness > 60:
            if the_person.obedience > 180:
                the_person "Oh, hi [the_person.mc_title]! Like, what can I do for you, sweetie?"
                "She bats her eyelashes and smiles, clearly trying to flirt with you."
            else:
                the_person "Hey, [the_person.mc_title]! So, like, what's up? Don't tell me you're here to, like, bother me or anything."
                "She winks and plays with her hair, looking playful and flirtatious."
        else:
            if the_person.obedience > 180:
                the_person "Hi, [the_person.mc_title]! Like, what can I get for you, honey?"
                "She smiles and looks up at you with big, bright eyes, clearly eager to please."
            else:
                the_person "Hey, like, what's up? Oh, you're talking to me? That's so cool!"
                "She giggles and bounces up and down, looking excited and enthusiastic."
    return

label bimboed_sex_responses_foreplay(the_person):
    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] moans enthusiastically, like, totally getting into it already."
            the_person "Oh my god, this is soooo good! You're, like, really good at this, I guess."
        else:
            "[the_person.possessive_title!c] moans happily to herself, looking all dreamy and stuff."
            the_person "I'm like, totally relaxed now. You're not, like, totally bad at this or anything."
    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            the_person "Omigod, this is like, so much better than I thought it would be! You're, like, really getting me going!"
        else:
            the_person "I'm like, totally feeling it now. You're not, like, completely clueless or anything."
    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            the_person "Oh, yeah! You're like, totally hitting all the right spots now! I'm like, soooo close!"
        else:
            the_person "Alright, alright. You're like, really getting the hang of this. But don't expect me to be all, like, gushy about it or anything."
    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "Mmm, I'm like, totally loving this now! You're like, soooo good at making me feel all tingly and stuff!"
        else:
            the_person "You're like, really doing it right now, [the_person.mc_title]. But don't expect me to be all, like, mushy about it or anything."
    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                the_person "Oh my god, I'm like, soooo close to cumming now! You're like, totally amazing, I swear!"
            else:
                the_person "The way you touch me is like, soooo different from anyone else. But don't think this means I'm, like, totally forgiven or anything."
        else:
            the_person "Alright, you're like, almost there now. But don't expect me to be all, like, happy and stuff about it or anything."
    return

label bimboed_sex_responses_oral(the_person):
    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] bats her eyelashes, looking all coy and stuff."
            the_person "Oh my god, you don't have to do that, [the_person.mc_title]... but like, if you want to, I guess it's okay..."
        else:
            "[the_person.possessive_title!c] looks up at you, her cheeks all flushed and adorable."
            the_person "Like, you don't have to or anything... but if you want to, I won't, like, stop you or anything..."

    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            the_person "Mmm, like, I guess it couldn't hurt to try... *giggle*"
        else:
            the_person "Oh my god, you really want to? Like, okay, I guess..."

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            the_person "Hmph, like, well, if you insist... *sigh*"
            "[the_person.possessive_title!c] lets out a little sigh, her body all relaxed and stuff."
        else:
            the_person "Alright, like, fine... but don't think I'm doing this because I'm, like, totally into you or anything..."

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "Mmm, like, you know, maybe this isn't so bad after all... *giggle*"
        else:
            the_person "Hmph, like, you're pretty good at this, I'll give you that... *smirk*"
    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                the_person "Oh. My. God. Like, I didn't know you could do that... *squeal*"
            else:
                the_person "Mmm, like, maybe I should let you do that more often... when [the_person.so_title] isn't around, of course... *wink*"
        else:
            the_person "Ugh, like, fine... but don't think I'm, like, totally enjoying this or anything... *rolls her eyes*"
    return

label bimboed_sex_responses_vaginal(the_person):
    if the_person.energy < 10:
        call low_energy_sex_responses_vaginal(the_person) from _vt_bimboed_call_low_energy_sex_responses_vaginal_10
        return
    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            $ play_moan_sound()
            "[the_person.possessive_title!c] moans and wiggles her hips with your cock inside her, looking all cute and stuff."
            the_person "Oh my god, this feels soooo good! You're, like, really good at this, I guess."
        else:
            "[the_person.possessive_title!c] bites her lip and stifles a moan, looking all adorable and embarrassed."
            the_person "Omigod, this is so... intense. I'm like, totally feeling it now."

    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            the_person "Mmm, like, yeah... keep going, I guess. You're, like, really getting me going now."
        else:
            the_person "Ugh, I mean... your cock is, like, really big and stuff. But like, don't think I'm impressed or anything."

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            the_person "Oh my god, this is soooo good! You're, like, really hitting all the right spots now."
        else:
            the_person "Hmm, like, yeah... your cock is, like, really nice, I guess. But like, don't think I'm, like, totally into you or anything."

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "Mmm, like, yeah... I'm so close now. Just, like, keep going and maybe I'll... you know, cum or something."
        else:
            the_person "Fine, like, keep doing what you're doing, I guess. It's not like I have anything better to do or anything."
    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                the_person "Oh my god, I'm like, so close now! Just, like, finish me off already!"
            else:
                the_person "Yeah, whatever... you're, like, really stretching me out now. But like, don't think it means anything or anything."
                the_person "Just, like, finish and get it over with already."
        else:
            the_person "Hmph, like, I guess I'm almost there now. But like, don't think I'm, like, totally enjoying this or anything."
            the_person "Just, like, finish and let's get this over with already."
    return

label bimboed_sex_responses_anal(the_person):
    if the_person.energy < 10:
        call low_energy_sex_responses_anal(the_person) from _vt_bimboed_call_low_energy_sex_responses_anal_10
        return

    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            the_person "Omigod, like, okay... But don't expect me to be all, like, smiles and sunshine about it..."
            "She pouts and looks away, clearly not thrilled about the situation, but still kinda into it."
        else:
            $ the_person.call_dialogue("annoyed_exclaim")
            the_person "Ugh, like, great. Just what I always wanted: a big, thick cock up my ass. Not."
            "She rolls her eyes and grumbles to herself, clearly unenthusiastic, but still kinda curious."

    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            $ the_person.call_dialogue("surprised_exclaim")
            the_person "Oh my god, like, this is... so different!"
            "She squirms a bit, trying to get used to the sensation, but still kinda enjoying it."
        else:
            the_person "Ugh, like, this is soooo uncomfortable... But, like, in a weird way, it's kinda... interesting?"

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            the_person "Okay, like, okay... You can keep going, I guess."
            "She bites her lip, trying to keep up the appearance of being tough, but still kinda into it."
        else:
            the_person "Why do you have to be so, like, rough?! Can't you just, like, be gentle for once?"

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            if mc.condom:
                the_person "Just, like, get it over with already... I'm, like, soooo close!"
            else:
                the_person "Omigod, like, you really want to do this raw, huh? That's, like, soooo naughty!"
        else:
            the_person "Why do you always have to be so, like, insistent?! Can't you just, like, take no for an answer?"
    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                the_person "Fine, like, I'll cum... But don't think this means I, like, love you or anything!"
            else:
                the_person "You're, like, just like my [the_person.so_title], always trying to get me to cum... But, like, I guess I kinda like it?"
                "She sighs, resigned to her fate, but still kinda enjoying it."
        else:
            $ the_person.call_dialogue("annoyed_exclaim")
            the_person "Great, just what I needed: another orgasm... Like, thanks for nothing, I guess."
            "She mutters to herself, clearly not thrilled about the prospect, but still kinda into it."
    return

label bimboed_climax_responses_foreplay(the_person):
    if the_person.sluttiness > 50:
        the_person "Oh my god, like, stop teasing me and just make me cum already! I'm, like, soooo close!"
        "She squirms and wiggles, clearly desperate for release."
    else:
        the_person "Why do you always have to, like, make this so difficult? Can't you just, like, make me cum already?"
        "She pouts and huffs, clearly on the verge of climax, but still kinda frustrated."
    return

label bimboed_climax_responses_oral(the_person):
    if the_person.sluttiness > 70:
        the_person "Oh my god, like, why do you have to be soooo good at that?! Fine, I'll cum, okay?!"
        "She throws her head back and moans, clearly overwhelmed with pleasure."
    else:
        the_person "Omigod, you're like, really good at that... I didn't think I'd, like, actually cum or anything... But, like, I'm totally going to now..."
        "She giggles and squirms, clearly surprised and delighted by her own reaction."
    return

label bimboed_climax_responses_vaginal(the_person):
    if the_person.sluttiness > 70:
        if the_person.arousal_perc > 120:
            the_person "Oh my god, like, fine... I'll cum, okay? But don't think this means I'm, like, totally into you or anything."
        else:
            the_person "Omigod, just a little more... I'm, like, so close... Ah, yeah!"
        "She bites her lip and tosses her head back, clearly overwhelmed with pleasure."
    else:
        the_person "Oh my god... I'm, like, totally going to... Ah! Omigod, yeah!"
        "She squeals and squirms, clearly surprised and delighted by her own reaction."
    return

label bimboed_climax_responses_anal(the_person):
    if the_person.sluttiness > 70:
        if the_person.arousal_perc > 120:
            the_person "Oh my god, like, fine... You win, okay? I'll cum. But don't think I'm, like, totally into this or anything."
        else:
            the_person "Omigod, just a little more... My ass is, like, soooo sensitive... Ah, yeah!"
        "She tosses her head back and moans, clearly overwhelmed with pleasure, but still trying to maintain a bit of attitude."
    else:
        the_person "Oh my god... My ass is, like, totally on fire... I... Ah! Omigod, yeah!"
        "She squeals and squirms, clearly surprised and delighted by her own reaction, and totally losing control."
    return

label bimboed_clothing_accept(the_person):
    if the_person.obedience > 180:
        the_person "Oh my god, like, whatever... Just don't think you're, like, totally controlling my wardrobe or anything."
        "She rolls her eyes and pouts, but still looks kinda excited about the new clothes."
    else:
        the_person "Yeah, like, whatever... Just don't expect me to go around looking like a total, like, skank or anything."
        "She shrugs and looks down at her new outfit, clearly not totally thrilled, but still kinda into it."
    return

label bimboed_clothing_reject(the_person):
    if the_person.should_wear_uniform:
        the_person "Oh my god, like, I totally forgot about my uniform! Let me just, like, go get it real quick."
        "She giggles and hurries off to get her uniform, clearly a bit flustered."
    elif the_person.obedience > 180:
        the_person "I'm like, so sorry, but I really don't think I could pull off wearing something like this. It's just, like, not my style, you know?"
        "She looks down at the outfit and frowns, clearly unsure about it."
    else:
        if the_person.sluttiness > 60:
            the_person "Hmm, like, I don't know about this one... It's a bit too, like, revealing for my taste. I mean, I like to show some skin, but this is just, like, too much."
            "She pouts and looks down at the outfit, clearly unimpressed."
        else:
            the_person "You've got to be, like, totally kidding me, right? This is, like, soooo ridiculous. I'm not wearing this, no way."
            "She rolls her eyes and crosses her arms, clearly not having it."
    return

label bimboed_clothing_review(the_person):
    if the_person.outfit.cum_covered:
        if (the_person.sluttiness > 40 and the_person.opinion.being_covered_in_cum >=0) or the_person.opinion.being_covered_in_cum > 0:
            the_person "Oh my god, like, why do I always get so messy with you...? I guess I'll just, like, have to clean up a bit before I go out."
            "[the_person.title] starts to wipe up the biggest splashes of cum on her, looking all cute and embarrassed."
        else:
            the_person "Ugh, like, seriously? I need to clean up this mess, stat! Can you, like, help me out and make sure I don't miss any spots?"
            "[the_person.title] wipes herself down, cleaning up all the cum she can find, and looking all frustrated and adorable."

    if the_person.obedience > 180:
        the_person "Okay, like, I'll be back in a sec. I just need to, like, get cleaned up for you, 'kay?"
        "She smiles and heads off to clean up, looking all sweet and submissive."
    else:
        if the_person.sluttiness > 40:
            the_person "I don't know why I do this, but like, I want to look good for you, okay? I'll be back in a sec, I just want to, like, get cleaned up and stuff."
            "She winks and heads off to clean up, looking all flirty and playful."
        else:
            the_person "Ugh, like, everything's such a mess after that. Wait here a moment, I'm just going to, like, find a mirror and try and look somewhat presentable, 'kay?"
            "She rolls her eyes and heads off to clean up, looking all exasperated and adorable."
    $ the_person.apply_planned_outfit(show_dress_sequence = True)
    return

label bimboed_strip_reject(the_person, the_clothing, strip_type = "Full"):
    if the_person.obedience > 180:
        the_person "Oh my god, like, could we please just leave my [the_clothing.display_name] on for now? I'm, like, totally freezing..."
        "She shivers and looks up at you with big, pleading eyes."
    elif the_person.obedience < 70:
        the_person "No way, no way, no way! I'm, like, totally in charge of my own wardrobe, okay? Don't even think about trying to rush me!"
        "She crosses her arms and looks at you with a stubborn expression."
    else:
        the_person "Not yet, like, I don't know if I'm ready to take off my [the_clothing.display_name]... Maybe we can, like, try something else first? Something a little more... fun?"
        "She bats her eyelashes and looks up at you with a flirtatious smile."
    return

label bimboed_strip_obedience_accept(the_person, the_clothing, strip_type = "Full"):
    "[the_person.title] giggles and looks away, her cheeks flushing as you start to slide her [the_clothing.display_name] away."
    "She bites her lip and fidgets, clearly a little nervous, but also kinda excited."
    if the_person.obedience > 180:
        the_person "Oh my god, like, alright... I guess I can trust you with this. But, like, be gentle, okay?"
    else:
        the_person "I don't know if this is, like, a good idea or anything... But, like, I'll let you do it this once. Just, like, don't expect me to do it all the time, 'kay?"
    return

label bimboed_grope_body_reject(the_person):
    if the_person.effective_sluttiness("touching_body") < 5: #Fail point for touching shoulder
        the_person "Omigod, like, what do you think you're doing?!"
        "[the_person.title] steps back, looking all shocked and offended, and crosses her arms over her chest."
        the_person "Just, like, get your hands off me, okay? You're making me, like, super uncomfortable."
        mc.name "Oh, sorry. I didn't mean to make you feel that way."
        the_person "Yeah, well, like, try to be more careful next time, alright? I don't want to, like, have to deal with this again."
        "She looks all pouty and upset, but you both try to move on and put it behind you."
    else: #Fail point for touching waist
        the_person "Hey, like, could you just...?"
        "[the_person.title] takes your hand and pulls it off of her waist, giving you a warning look with her big, bright eyes."
        the_person "... Keep your hands to yourself, 'kay? I don't, like, appreciate it when you touch me like that."
        mc.name "Oh yeah, of course. My bad."
        the_person "Just, like, make sure you don't do it again, okay? I don't want to, like, have to get all upset and stuff."
        "She looks all annoyed and flustered, but still kinda cute and adorable, and you can tell she's still a bit miffed about the situation."
    return

label bimboed_sex_accept(the_person, the_position):
    if the_person.sluttiness > 70:
        if the_person.obedience < 70:
            the_person "Oh my god, like, fine... Let's do it already! But don't think this means I'm, like, going to be your personal sex slave or anything."
            "She rolls her eyes and pouts, but still looks kinda excited."
        else:
            if the_position.skill_tag == "Foreplay":
                the_person "Omigod, I've been, like, totally wanting you to do that for ages now! Just thinking about it makes me, like, soooo wet."
                "She giggles and looks up at you with big, sparkling eyes."
            elif the_position.skill_tag == "Oral":
                if "getting head" in the_position.opinion_tags:
                    the_person "Ugh, like, I'm soooo ready for this! Suck my pussy already, please!"
                    "She squirms and looks up at you with a pleading expression."
                else:
                    the_person "You're, like, going down on me right now, and you're going to make me cum, 'kay?"
                    "She looks up at you with a determined expression, her eyes shining with excitement."
            else:
                the_person "Get over here and, like, fuck me already! I've been, like, totally waiting for this."
                "She pouts and looks up at you with a sulky expression, but still looks kinda turned on."
    else:
        the_person "Come here, like, let's do it... But don't think I'm, like, going to do this all the time, got it? I'm not, like, that kind of girl."
        "She looks up at you with a warning expression, but still looks kinda interested."
    return

label bimboed_sex_obedience_accept(the_person):
    if the_person.sluttiness > 70:
        the_person "Oh my god, like, fine... I don't want to admit it, but you've, like, totally gotten to me. Do whatever you want to me, [the_person.mc_title]. Just, like, be gentle, okay?"
        "She looks up at you with big, sparkling eyes and a pouty expression."
    else:
        if the_person.obedience > 180:
            the_person "Alright, like, I'll do what you say... But don't think this means I'm, like, going to love it or anything."
            "She rolls her eyes and looks away, still looking kinda hesitant."
        else:
            the_person "I shouldn't be saying this, but like, if you really want to... I'll give it a try. Just this once, 'kay? And, like, don't expect me to do it again or anything."
            "She looks up at you with a nervous expression, biting her lip."
    return

label bimboed_sex_gentle_reject(the_person):
    if the_person.sluttiness > 50:
        the_person "Ugh, like, not like that, [the_person.mc_title]... I need, like, a little more foreplay first. Can you, like, slow down and stuff?"
        "She pouts and looks up at you with a sulky expression, still looking kinda turned on."
    else:
        the_person "No, no, no... Like, I want to have fun and all, but I don't want to, like, get too serious or anything. Let's just, like, keep it light and fun, 'kay?"
        "She smiles and looks up at you with a playful expression, still looking kinda interested."
    return

label bimboed_sex_angry_reject(the_person):
    if the_person.has_significant_other:
        the_person "Oh my god, like, what is wrong with you?! I have a [the_person.so_title], so you can, like, totally forget about doing anything like that. Ever. Gross!"
        "She looks at you with a disgusted expression and turns away, clearly offended."
    elif the_person.sluttiness < 20:
        the_person "Are you, like, serious?! You've got to be, like, totally kidding me! Get away from me, I never want to see you like this again. Ew!"
        "[the_person.title] glares at you and takes a step back, her face all red and angry, like she's about to freak out or something."
    else:
        the_person "What? Are you, like, out of your mind?! You can't be, like, serious! Get away from me, I'm not interested in anything like that. Ugh, no way!"
        "[the_person.title] glares at you and steps back, her face showing clear disapproval, like she's all grossed out or something."
    return

label bimboed_seduction_response(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 50:
            the_person "Oh my god, like, I think I know exactly what you need right now... Let me, like, take care of you, okay?"
            "She smiles and bats her eyelashes, looking all sweet and seductive."
        else:
            the_person "Okay, like, I'll give you a few minutes... But don't think this means I'm, like, going to be your slave or anything, 'kay?"
            "She looks up at you with a hint of a smile, still looking kinda hesitant."
    else:
        if the_person.sluttiness > 50:
            the_person "Mmm, like, you're feeling as horny as me, then? Come on, let's go find a place to, like, get out of sight and stuff..."
            "[the_person.title] takes your hand and leads you off to find some place private, looking all excited and flirtatious."
        elif the_person.sluttiness > 10:
            the_person "I know that look you're giving me, like, I think I know what you want... But don't expect me to, like, give it up that easily, okay?"
            "She smiles and raises an eyebrow, still looking kinda playful and teasing."
        else:
            the_person "[mc.name], like, I know what you mean... Okay, I can spare a few minutes, I guess. But don't, like, get your hopes up or anything."
            "She looks up at you with a hint of a smile, still looking kinda shy and hesitant."
    return

label bimboed_seduction_accept_crowded(the_person):
    if not the_person.has_significant_other:
        if the_person.sluttiness < 20:
            the_person "Oh my god, like, alright... Let's sneak away for a few minutes and you can, like, convince me a little more, okay?"
            "She looks around nervously, making sure no one is watching."
        elif the_person.sluttiness < 50:
            the_person "Come on, like, I know someplace nearby where we can get a few minutes of, like, total privacy... Just make it quick, 'kay?"
            "She takes your hand and leads you away, looking all sneaky and secretive."
        else:
            the_person "Omigod, like, I don't know if I can wait much longer, [the_person.mc_title]... I'm, like, totally dying over here!"
            "She looks up at you with big, pleading eyes, clearly desperate for some action."
    else:
        if the_person.sluttiness + (5*the_person.opinion.cheating_on_men) > 50:
            the_person "Oh my god, like, fuck it! Let's do this, I don't care about anything else right now!"
            the_person "I hope you don't mind that I've got a [the_person.so_title], but like, I'm not even thinking about that right now... I just want you!"
            "She looks up at you with a wild, reckless expression, clearly ready to throw caution to the wind."
        else:
            the_person "Ugh, like, you're so bad for me, [the_person.mc_title]... Come on, we need to find somewhere quiet so my [the_person.so_title] doesn't, like, catch us or anything."
            "She looks around nervously, clearly worried about getting caught, but still kinda excited about the prospect of sneaking around."
    return

label bimboed_seduction_accept_alone(the_person):
    if not the_person.has_significant_other:
        if the_person.sluttiness < 20:
            the_person "Oh my god, like, alright... You've got one chance to, like, impress me, okay?"
            "She looks up at you with a hint of a smile, still looking kinda hesitant."
        elif the_person.sluttiness < 50:
            the_person "Come on, like, let's get this over with and see if you're, like, any good or anything."
            "She rolls her eyes and pouts, still looking kinda playful."
        else:
            the_person "Omigod, like, I'm soooo turned on right now... Just, like, do me already, please!"
            "She looks up at you with big, pleading eyes, clearly desperate for some action."
    else:
        if the_person.sluttiness + (5*the_person.opinion.cheating_on_men) > 50:
            the_person "Oh my god, like, I know I shouldn't be doing this with you, but like, fuck it... Let's do this, I don't care about anything else right now!"
            "She looks up at you with a wild, reckless expression, clearly ready to throw caution to the wind."
        else:
            the_person "You're, like, so trouble, [the_person.mc_title]... But, like, I just can't help myself, okay? Come here and, like, kiss me or something."
            "She looks up at you with a flirtatious smile, still looking kinda hesitant, but also kinda excited."
    return

label bimboed_seduction_refuse(the_person):
    if the_person.sluttiness < 20:
        the_person "Oh my god, like, why are you always trying to flirt with me, [mc.name]? I'm, like, soooo not in the mood for this right now, okay?"
        "[the_person.title] folds her arms and looks away, pouting."
        "She looks all cute and adorable, but still kinda annoyed."
    elif the_person.sluttiness < 50:
        the_person "Fine, like, I'll admit you're kinda cute and all... But don't think this means I'm, like, actually interested or anything. I just don't feel like messing around right now, okay? Maybe some other time, when I'm in a better mood... or something."
        "[the_person.title] playfully pokes [mc.name]'s chest with her finger, looking all flirty and playful."
        "She winks and smiles, still looking kinda interested, but also kinda hesitant."
    else:
        the_person "Eh, like, you're always trying to get me into bed, [mc.name]... But I'm, like, not going to make it easy for you, okay? You'll have to, like, wait until I'm good and ready to fool around... Maybe that'll be never, who knows?"
        "[the_person.title] grins mischievously and walks away, looking all sassy and confident."
        "She tosses her hair over her shoulder and gives you a flirtatious glance, still looking kinda interested, but also kinda in control."
    return

label bimboed_compliment_response(the_person):
    mc.name "Hey [the_person.fname], you look, like, really beautiful today... Is there, like, a special occasion or something?"
    if the_person.is_at_work:
        if (the_person.is_employee or the_person.is_strip_club_employee) and the_person.is_wearing_uniform:
            call bimboed_flirt_response_employee_uniform_low(the_person) from _call_bimboed_flirt_response_employee_uniform_low_compliment_response
        elif the_person.is_at_job(prostitute_job):
            the_person "Ugh, like, why do you always want to hang out with me? Can't you see I'm, like, super busy?"
            "She rolls her eyes and looks away, clearly not interested."
        elif the_person.sluttiness > 50:
            the_person "I'm, like, doing great, thanks for asking... But don't think this means I'm, like, actually interested in you or anything, okay?"
            "She smiles and winks, still looking kinda flirtatious, but also kinda dismissive."
        else:
            the_person "Oh my god, like, stop it, you're making me blush! There's no special occasion, I just felt like, like, dressing up today, I guess."
            "She looks all cute and adorable, with a big smile on her face."
    else:
        the_person "Well, like, I did put in a bit of extra effort today... You're just the first one to notice, I guess. But thanks, like, I appreciate it or whatever."
        "She looks up at you with a smile, still looking kinda pleased with herself."
    "You try to press for more information, but [the_person.possessive_title!c] just smiles coyly and changes the subject, leaving you wondering what's going on... She's, like, totally mysterious and stuff."
    return

label bimboed_compliment_response_girlfriend(the_person):
    mc.name "Hey [the_person.title]. You're looking, like, totally gorgeous this [StringInfo.time_of_day_string]."
    if the_person.is_at_work:
        if (the_person.is_employee or the_person.is_strip_club_employee) and the_person.is_wearing_uniform:
            call bimboed_flirt_response_employee_uniform_mid(the_person) from _call_bimboed_flirt_response_employee_uniform_mid_compliment_response_girlfriend
            $ the_person.call_dialogue("flirt_response_employee_uniform_mid")
        elif the_person.sluttiness > 50:
            the_person "Mmm, like, thank you, [the_person.mc_title]... Wanna find out how nice I am? *wink*"
            "She bats her eyelashes and gives you a flirtatious smile."
        else:
            the_person "Hmph, like, really? Thanks, [the_person.mc_title]. You're not so bad yourself, I guess."
            "She looks up at you with a hint of a smile, still looking kinda playful."
    else:
        the_person "Ugh, like, don't be ridiculous... It's just a normal day, okay? But thanks, I guess."
        mc.name "Oh come on, don't be like that. You know you look, like, totally amazing."
        the_person "Aww, like, stop it, [the_person.mc_title]... You're making me blush, and like, annoyed at the same time. But, like, in a good way, I guess."
        "She giggles and looks up at you with a smile, still looking kinda flustered."
    "You chat with [the_person.possessive_title!c] for a while, and although she's initially annoyed by your compliments, she starts to warm up to you... She's, like, totally sweet and adorable."
    return

label bimboed_compliment_response_affair(the_person):
    mc.name "Hey [the_person.title]. You're looking, like, totally stunning this [StringInfo.time_of_day_string]."
    if the_person.is_at_work:
        if (the_person.is_employee or the_person.is_strip_club_employee) and the_person.is_wearing_uniform:
            call bimboed_flirt_response_employee_uniform_mid(the_person) from _call_bimboed_flirt_response_employee_uniform_mid_compliment_response_affair
        elif the_person.sluttiness > 50:
            the_person "Mmmm, like, thank you [the_person.mc_title]... Wanna go somewhere a little more private, so you can, like, make me feel how amazing I am?"
            "She bats her eyelashes and gives you a flirtatious smile, clearly interested in taking things to the next level."
        else:
            the_person "Hmph, like, really? Thanks, [the_person.mc_title]. You're not so bad yourself, I guess."
            "She looks up at you with a hint of a smile, still looking kinda playful and flirtatious."
    else:
        the_person "Ugh, like, don't be silly... It's just a normal day, okay? But thanks, I suppose."
        mc.name "Oh come on, don't be like that. You know you look, like, totally gorgeous."
        the_person "Aww, like, stop it, [the_person.mc_title]... You're making me blush, and like, a little annoyed... But, like, in a good way, I guess."
        "She giggles and looks up at you with a smile, still looking kinda flustered and adorable."
    "You keep chatting with [the_person.possessive_title!c] for a while, slipping in a few more compliments... She's, like, totally charmed by your attentiveness and stuff."
    return

label bimboed_flirt_response(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 50:
            the_person "Oh my god, like, fine... You're not, like, totally terrible, [the_person.mc_title]."
            "She looks up at you with a hint of a smile, still looking kinda playful."
        else:
            the_person "Whatever, like, thanks for the compliment, [the_person.mc_title]... You're not, like, a complete loser or anything."
            "She rolls her eyes and looks away, still looking kinda cute and adorable."
    elif the_person.has_significant_other:
        if the_person.sluttiness + (the_person.opinion.cheating_on_men*5) > 50:
            the_person "Oh, like, you think you're so clever, don't you? I'll, like, give you that."
            "[the_person.title] gives you a sly look, her eyes narrowing and her lips curling up into a flirtatious smile."
        else:
            the_person "You're, like, really pushing your luck, [the_person.mc_title]... I have a [the_person.so_title], you know."
            mc.name "What about you, do you appreciate it?"
            "She rolls her eyes and crosses her arms, looking all pouty and adorable."
            the_person "Maybe I do, maybe I don't... Like, it's none of your business, okay?"
    else:
        if the_person.sluttiness > 50:
            the_person "Fine, like, maybe you're worth my time, [the_person.mc_title]... Maybe."
            "[the_person.title] gives you a half-smile, but her eyes remain guarded, still looking kinda flirtatious and playful."
        else:
            the_person "Whatever, like, you're not unattractive, I suppose... But don't think that means I'll, like, go easy on you or anything."
            the_person "You'll, like, have to really impress me though... I have, like, super high standards and stuff."
            "She looks up at you with a challenging expression, still looking kinda cute and adorable."
    return

label bimboed_flirt_response_employee_uniform_low(the_person):
    if the_person.is_wearing_forced_uniform:
        the_person "Oh my god, like, I suppose you like seeing me in this uniform... I mean, I'm practically naked, right?"
        mc.name "I know you don't like it, but I needed to make a point, okay?"
        the_person "I know, I know... You always were one to make a point, [the_person.mc_title]."
        $ mc.change_locked_clarity(5)
        "She crosses her arms over her chest, but can't hide the small smile on her face... She looks all cute and adorable, even when she's trying to be mad."
    elif the_person.judge_outfit(the_person.outfit):
        #She's in uniform and likes how it looks.
        the_person "Oh, like, you noticed? I thought it was a bit much, but I guess it's not so bad, right?"
        the_person "I mean, it's nice to work somewhere where I can, like, show off a little... You know, be myself and stuff."
        $ mc.change_locked_clarity(5)
        "She winks at you, then turns to adjust her uniform, accentuating her hips... She looks all confident and sexy, and you can't help but stare."
    else:
        #She's in uniform, but she thinks it's a little too slutty.
        if the_person.vagina_visible:
            # Her pussy is on display.
            the_person "Hmph, like, I suppose you like seeing me like this... I mean, I'm practically naked, right?"
            mc.name "Well, you know that it's..."
            the_person "I know, I know... It's company policy, yadda yadda yadda... But don't think you're the only one who's, like, annoyed by it, okay?"
            mc.name "Give it some time and you'll get used to it, I promise."
            $ mc.change_locked_clarity(5)
            "She rolls her eyes, but doesn't argue... She just looks all cute and pouty, and you want to hug her or something."

        elif the_person.tits_visible:
            # Her tits are out
            the_person "Ugh, like, I'm still getting used to being so... exposed in this uniform... At least I don't have to wear a bra, right?"
            mc.name "You look, like, incredible and you're comfortable... I call that a success, don't you?"
            $ mc.change_locked_clarity(5)
            "She huffs, but can't hide her smile... She looks all happy and carefree, and you can't help but smile back."
            the_person "Yeah, yeah... You're just trying to make me feel better, [the_person.mc_title]."

        elif the_person.underwear_visible:
            # Her underwear is visible.
            the_person "Hmph, like, I probably would have picked something that kept me a little more covered, but at least our uniform is, like, super comfortable, right?"
            mc.name "It may be a little unconventional, but you look, like, fantastic... You've got exactly the right kind of body for it, if you know what I mean."
            the_person "Well, that's one way to look at it, I suppose... Thanks for trying to make me feel better, [the_person.mc_title]."
            $ mc.change_locked_clarity(5)
            "She playfully rolls her eyes and turns to adjust her uniform, showing off her body... She looks all flirty and playful, and you can't help but flirt back."
        else:
            # It's just generally slutty.
            the_person "Ugh, well thank you, I guess... Our uniforms are a little bold for my taste, but I guess I look, like, pretty good in it, right?"
            $ mc.change_locked_clarity(5)
            "She blushes and looks away, but not before you catch a glimpse of her small smile... She looks all cute and adorable, and you just want to hug her or something."
    return

label bimboed_flirt_response_employee_uniform_mid(the_person):
    if the_person.is_wearing_forced_uniform:
        $ mc.change_locked_clarity(10)
        if the_person.vagina_visible:
            the_person "Oh my god, like, fine... You caught me off guard. I'll admit, this uniform does make me look, like, super good... Especially down here, if you know what I mean."
            mc.name "It's a great uniform, but that's not what's important here, okay?"
            the_person "Yeah, yeah... You're right. It's just hard not to feel like a sex object in this thing, especially with my pussy on display... But, like, I guess that's kinda the point, right?"
        elif the_person.tits_visible:
            the_person "Ugh, like, fine... You caught me off guard. I'll admit, this uniform does make me look, like, really good... Especially up here, if you know what I mean."
            mc.name "It's a great uniform, but that's not what's important here, okay?"
            the_person "Yeah, yeah... You're right. It's just hard not to feel like a sex object in this thing, especially with my boobs popping out... But, like, I guess that's kinda the point, right?"
        else:
            the_person "Oh my god, like, fine... You caught me off guard. I'll admit, this uniform does make me look, like, really good... But, like, don't get too excited or anything, okay?"
            mc.name "It's a great uniform, but that's not what's important here, okay?"
            the_person "Yeah, yeah... You're right. It's just hard not to feel like a sex object in this thing... But, like, I guess that's kinda the point, right?"
        mc.name "Rules are rules and I can't make any exceptions, even if they look, like, super good."
        "She sighs and nods, looking all cute and pouty."
        the_person "Yeah, I know... At least you're having a good time, I guess. I don't mind that so much, as long as you're, like, happy and stuff."
    elif the_person.judge_outfit(the_person.outfit):
        $ mc.change_locked_clarity(10)
        if the_person.tits_visible:
            the_person "Hmph, maybe I should wear this outfit more often... It's getting a lot of attention, especially for my boobs... And, like, I guess I don't mind that so much, either."
            mc.name "It's a great outfit, but I'm more interested in the person wearing it, okay?"
            the_person "Oh, really? Is that so? I guess my boobs are, like, hard to ignore or something... But, like, that's okay, I guess."
        else:
            the_person "Hmph, maybe I should wear this outfit more often... It's getting a lot of attention, and, like, I guess I don't mind that so much, either."
            mc.name "It's a great outfit, but I'm more interested in the person wearing it, okay?"
            the_person "Oh, really? Is that so? I guess my vagina is, like, hard to ignore or something... But, like, that's okay, I guess."
        the_person "Maybe I'll, like, invite you shopping one day and you can, like, tell me what else you want to see me in... That sounds, like, super fun, actually."
        mc.name "Sounds, like, a good time, yeah... I'd love to go shopping with you."
    else:
        # the_person "I think it shows off a little too much!"
        the_person "Ugh, like, fine... You're not gonna make this easy for me, are you?"
        $ mc.change_locked_clarity(10)
        if the_person.vagina_visible:
            the_person "I'm, like, trying to focus on my work here, not flirt with you all day... And definitely not with my pussy on display, okay?"
        elif the_person.tits_visible:
            the_person "I'm, like, trying to focus on my work here, not flirt with you all day... And definitely not with my boobs popping out, okay?"
        else:
            the_person "I'm, like, trying to focus on my work here, not flirt with you all day... Can't you, like, just leave me alone or something?"
        mc.name "I understand, but I promise it's, like, super important for the business, okay?"
        "She sighs and nods, looking all cute and pouty."
        the_person "Yeah, I know... You're, like, a real pain, you know that? But, like, I guess I can deal with it or whatever."
    return

label bimboed_flirt_response_low(the_person):
    #She's in her own outfit.
    the_person "Oh my god, like, I suppose it's not the worst outfit I've ever worn... But, like, don't expect me to be all excited about it or anything."
    $ the_person.draw_person(position = "walking_away")
    $ mc.change_locked_clarity(5)
    "She rolls her eyes and gives you a quick spin, showing off her outfit from every angle... She looks all cute and playful, even when she's trying to be sarcastic."
    the_person "I mean, like, I guess it's not too bad, right? But, like, don't think I'm, like, totally obsessed with it or anything."
    $ the_person.draw_person()
    mc.name "I think it looks, like, really great on you."
    the_person "Oh, shut up! You're just saying that to, like, make me feel better or something... But, like, thanks, I guess."
    "She smiles and looks down, still looking all adorable and stuff."
    return

label bimboed_flirt_response_low1(the_person):
    if the_person.has_significant_other:
        the_person "Oh my god, like, what's with you and the flirting? I've got a [the_person.so_title], and I don't think he'd, like, appreciate you getting all up in my grill, okay?"
        mc.name "What about you, do you appreciate it?"
        "She rolls her eyes and smirks, looking all cute and playful."
        the_person "Maybe I do... But, like, don't think you're getting anywhere with me that easily, got it? I'm, like, totally taken, and you need to respect that."
    else:
        the_person "Well, like, thanks for the compliment and all... But, like, don't think you're getting off that easy, okay? I have, like, super high standards, and you'll need to, like, totally prove yourself to me."
        the_person "But, like, if you can impress me... Who knows what might happen, right? Maybe I'll, like, totally fall for you or something."
    $ mc.change_locked_clarity(5)
    "She winks and smiles, looking all flirty and adorable."
    return

label bimboed_flirt_response_mid(the_person):
    if mc.location.person_count > 1 and the_person.effective_sluttiness("kissing") < (25 - (5*the_person.opinion.public_sex)):
        $ mc.change_locked_clarity(10)
        the_person "Oh my god, like, I was wondering if you actually noticed my outfit today... I was, like, totally hoping you'd say something, but I didn't want to, like, seem too obvious or anything."
        "Her eyes narrow slightly, but she's still trying to appear casual and stuff."
        mc.name "I noticed. It looks, like, really great on you."
        the_person "Oh, really? Thanks, I guess... I was thinking you might say something like that, but I didn't want to, like, get my hopes up or anything."
        "She crosses her arms, trying to maintain a tough exterior, but still looking all cute and adorable."
        if the_person.tits_visible:
            mc.name "I noticed. It looks, like, really great on you. Especially your boobs, if you don't mind me saying so."
            the_person "Oh, really? Thanks, I guess... I was thinking you might say something like that, but I didn't want to, like, seem too slutty or anything."
            "She crosses her arms, trying to maintain a tough exterior, but still looking all flirty and playful."
        else:
            mc.name "Well, it's true. You look, like, totally amazing... I'm not just saying that to be nice, either."
        the_person "Hmph, like, maybe I'll invite you shopping one day, so you can, like, tell me what else you want to see me in... That sounds, like, super fun, actually."
        "She leans in slightly, a hint of flirtation in her voice, and looks up at you with big, sparkling eyes."
        mc.name "I can think of a few things already... and I'm sure I'd, like, totally enjoy seeing you in them, if you know what I mean."
        the_person "I'm sure you would, like, totally love it... So, what do you say? Want to, like, take me out for a drink and maybe we can, like, discuss my wardrobe some more?"
    else:
        the_person "Thanks, I thought I looked, like, pretty hot in it too... I was, like, totally hoping you'd notice, but I didn't want to, like, seem too obvious or anything."
        the_person "You want a better look, right? Here, how does it make my ass look? Be honest, okay?"
        $ the_person.draw_person(position = "back_peek")
        $ mc.change_locked_clarity(10)
        the_person "Good, right? I was, like, totally hoping you'd say that... I've been, like, working out and stuff, so I'm glad it's, like, paying off or whatever."
        mc.name "Fantastic. I wish I could get an even better look at it, if you know what I mean."
        "[the_person.possessive_title!c] smiles and turns back to face you, looking all flirty and playful."
        $ the_person.draw_person()
        the_person "I'm sure you do, like, totally want to see more... Take me out for a drink and maybe we can, like, work something out, okay?"
    return

label bimboed_flirt_response_mid1(the_person):
    $ mc.change_locked_clarity(10)
    the_person "Oh my god, like, thanks... I do look, like, totally amazing in this outfit, don't I?"
    if (the_person.has_skirt or the_person.has_dress) and not the_person.has_thigh_high_socks:
        mc.name "You could, like, change it up with some high stockings, I would love to see that."
        the_person "Oh, really? And why would you want to see that? You're not, like, going to get a peek or anything, are you?"
        "She raises an eyebrow and looks at you with a flirtatious smile."
        mc.name "Because it would, like, look great on you, and I would totally enjoy the view... You have, like, amazing legs, and I just want to see more of them, okay?"
        "She giggles and looks away, still looking all cute and playful."
    mc.name "How about you and me go and grab a coffee sometime? Just the two of us, okay?"
    if the_person.has_significant_other:
        the_person "Sure, like, my [the_person.so_title] doesn't mind... as long as they're not around to, like, witness how much fun we're going to have, if you know what I mean."
        "She winks and looks at you with a sly smile, still looking all flirtatious and playful."
    else:
        the_person "Why not, I could use a pick-me-up once in a while... and maybe someone to, like, pick me up from the ground when I fall for you, okay?"
        "She looks up at you with big, sparkling eyes, still looking all cute and adorable."
    the_person "Just let me know when, I would love to... and don't think I won't notice if you're, like, trying to get a glimpse of my legs under the table, okay?"
    mc.name "I'll, like, keep that in mind, and maybe we can discuss what else you want to wear in the future... or not wear, if you know what I mean."
    the_person "Hmph, like, maybe... But don't think you're getting a discount on my wardrobe just because we're going out for coffee... or anything else, okay?"
    "She smiles and looks at you with a playful expression, still looking all flirtatious and adorable."
    return

label bimboed_flirt_response_high(the_person):
    if mc.location.person_count > 1 and the_person.effective_sluttiness() < (25 - (5*the_person.opinion.public_sex)): # There are other people here, if she's not slutty she asks if you want to find somewhere quiet
        the_person "Oh my god, like, you're really persistent, huh? Fine, but not here, okay?"
        "She glances around before giving you a sly smile, looking all cute and playful."
        menu:
            "Find somewhere more quiet\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                mc.name "Then let's, like, find somewhere that isn't here, okay?"
                the_person "Hmph, like, eager much? Alright, let's go... But, like, don't think you're getting lucky or anything, got it?"
                call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_bimboed_flirt_response_high_2
                the_person "So... Now what's your plan, huh?"

                if the_person.is_willing(kissing):
                    $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
                    if the_person.has_taboo("kissing"):
                        "You lean in close to kiss [the_person.title], and she looks up at you with big, sparkling eyes."
                        $ the_person.call_dialogue("kissing_taboo_break")
                        $ the_person.break_taboo("kissing")
                        "She responds passionately, her arms wrapping around your neck, and you can feel her heart beating fast."
                    else:
                        "You step close to [the_person.title] and put your arm around her waist, pulling her close and kissing her... She looks all happy and excited."
                        "She responds immediately and eagerly presses her body against yours, looking all cute and adorable."
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _vt_bimboed_call_fuck_person_49
                else:
                    if the_person.has_taboo("touching_body"):
                        $ the_person.call_dialogue("touching_body_taboo_break")
                        $ the_person.break_taboo("touching_body")
                        "You take her hand and pull her close against you... She looks up at you with big, sparkling eyes, and you can see the excitement in her face."
                    else:
                        "You take her hand and pull her close, your lips brushing against her ear... She looks all happy and excited, and you can feel her heart beating fast."
                    call fuck_person(the_person, private = True, start_position = standing_grope, skip_intro = True) from _call_fuck_person_bimboed_flirt_grope

                $ the_person.call_dialogue("sex_review", the_report = _return)
                call mc_restore_original_location(the_person) from _call_mc_restore_original_location_bimboed_flirt_response_high_2

            "Just flirt":
                mc.name "You know you want to, come on... I'll take you out for dinner, and then we can see where the night takes us, okay?"
                the_person "Hmm, like, you're really trying to charm me, aren't you? Well, I'll tell you what... If you can make me laugh, I might consider it, but don't think you're getting lucky or anything, got it?"
                "She smiles mischievously, clearly enjoying the challenge and looking all cute and playful."

    else:
        if mc.location.person_count == 1: #You're alone, so she just didn't meet the sluttiness threshold
            the_person "Hmm, like, you're really eager, aren't you? Well, I suppose it's just the two of us here... So, what's your plan, huh?"
            "[the_person.possessive_title!c] glances around, confirming you're alone, and looks up at you with big, sparkling eyes."

        else:  # You aren't alone but she's still into it.
            the_person "Feeling bold today, huh? Well, I think your chances are, like, pretty good... But, like, don't get too excited or anything, okay?"
            "[the_person.title] smirks, clearly enjoying the attention and looking all cute and playful."
            if the_person.has_large_tits: #Bounces her tits for you
                $ mc.change_locked_clarity(15)
                "[the_person.title] grabs her tits and jiggles them for you, looking all flirty and playful."
                the_person "Maybe I can, like, get these girls out for you... Does that sound nice, huh?"

            else: #No big tits, so she can't bounce them (as much)
                "[the_person.title] runs her hands over her hips sensually, obviously encouraging you to take things further... She looks all happy and excited, and you can see the desire in her eyes."

        menu:
            "Touch her" if not the_person.is_willing(kissing):
                "You step closer to [the_person.title] and move your hands down her waist... She looks up at you with big, sparkling eyes, and you can see the excitement in her face."
                if the_person.has_taboo("touching_body"):
                    the_person "Oh, you're, like, brave... I like that, but don't think you're getting lucky or anything, got it?"
                    $ the_person.call_dialogue("touching_body_taboo_break")
                    $ the_person.break_taboo("touching_body")

                call fuck_person(the_person, start_position = standing_grope, private = False) from _call_fuck_person_flirt_response_bimboed_touching

            "Kiss her" if the_person.is_willing(kissing):
                $ the_person.draw_person()
                if the_person.has_taboo("kissing"):
                    "You put your arm around [the_person.possessive_title!c] and lean in close... She looks up at you with big, sparkling eyes, and you can see the desire in her face."
                    $ the_person.call_dialogue("kissing_taboo_break")
                    $ the_person.break_taboo("kissing")
                    "She responds with a passionate kiss, her arms wrapping around your neck, and you can feel her heart beating fast."
                else:
                    "You pull [the_person.possessive_title!c] close and kiss her... She looks all happy and excited, and you can see the desire in her eyes."
                    "She responds with a passionate kiss, her arms wrapping around your neck, and you can feel her heart beating fast."

                call mc_move_to_private_location(the_person) from  _call_mc_move_to_private_location_bimboed_flirt_response_high
                call fuck_person(the_person, start_position = kissing, private = _return, skip_intro = True) from _vt_bimboed_call_fuck_person_50
                $ the_person.call_dialogue("sex_review", the_report = _return)
                call mc_restore_original_location(the_person) from _call_mc_restore_original_location_bimboed_flirt_response_high

            "Just flirt":
                $ the_person.draw_person()
                mc.name "Very tempting, but you're going to have to, like, contain yourself for now, okay?"
                the_person "Oh, you're not going to, like, take advantage of me right now, are you? Fine, be that way... But, like, don't think I'm not interested or anything, got it?"
                "[the_person.title] pouts, clearly enjoying the flirtation and looking all cute and playful."
    return

label bimboed_flirt_response_low_energy(the_person):
    if the_person.sluttiness > 40:
        the_person "Oh my god, like, thanks for the compliment and all... But, like, I'm soooo tired right now, okay?"
        "She looks up at you with big, sleepy eyes, still looking kinda cute and adorable."
    else:
        the_person "Thanks, like, but I'm totally beat... Can we, like, pick this up later or something?"
        "She yawns and stretches, looking all tired and sluggish, but still kinda sweet and endearing."
    return

label bimboed_flirt_response_girlfriend(the_person):
    # Lead in: mc.name "You're so beautiful [the_person.title], I'm so lucky to have a woman like you in my life."
    if mc.location.person_count > 1:
        # There are other people around, so she'll only start making out with you if she's slutty.
        if the_person.effective_sluttiness("kissing") < (25 - (5*the_person.opinion.public_sex)):
            # Not very slutty, so she wants to find somewhere private
            the_person "Oh my god, you're so cheesy... But, like, I love it, okay?"
            "She pulls you against her and kisses you, her lips soft and gentle... She looks all cute and adorable, even when she's trying to be sassy."
            the_person "There, now you can't say I don't know how to kiss, right?"
            mc.name "Haha, yeah I guess not... You're, like, totally amazing, [the_person.title]."
            "You put your arms around her and kiss her back, feeling her warmth and closeness... She looks all happy and content, and you can see the love in her eyes."
            the_person "Mmm, yeah, like that... Just, like, kiss me some more, okay?"
            menu:
                "Find somewhere more quiet\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                    mc.name "Why wait? Come on, I'm sure we can find somewhere quiet... Just, like, us two, okay?"
                    the_person "You're always so eager, aren't you? Alright, let's go... But, like, don't think you're getting lucky or anything, got it?"
                    "You and [the_person.possessive_title!c] hurry off, searching for a private spot... She looks all excited and playful, and you can see the anticipation in her eyes."
                    call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_bimboed_flirt_response_girlfriend_2
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _vt_bimboed_call_fuck_person_76
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_bimboed_flirt_response_girlfriend_2

                "Just flirt":
                    $ mc.change_locked_clarity(10)
                    "You reach around and pull her closer, running your hand down her back... She looks all happy and content, and you can see the love in her eyes."
                    mc.name "You're so beautiful, and you know it... But, like, don't let it go to your head or anything, okay?"
                    "She rolls her eyes but leans in for a quick kiss... She looks all cute and adorable, even when she's trying to be sassy."
                    the_person "Fine, you caught me... But don't think this means I'm going easy on you, got it?"

        else:
            the_person "Well if I'm so beautiful, then why are you just standing there? Come on, kiss me... Like, now, okay?"
            "You put your arm around her waist and pull her close, kissing her deeply... She looks all happy and excited, and you can see the love in her eyes."
            "When you break the kiss, [the_person.possessive_title!c] sighs and leans against you... She looks all content and happy, and you can see the satisfaction in her eyes."
            the_person "You're not so bad yourself... But, like, don't think you're getting off that easy, got it?"
            menu:
                "Make out":
                    "You lean back in and kiss her again, this time more passionately... She looks all excited and playful, and you can see the anticipation in her eyes."
                    "[the_person.title] responds eagerly, wrapping her arms around your neck... She looks all happy and content, and you can see the love in her eyes."

                    call mc_move_to_private_location(the_person) from  _call_mc_move_to_private_location_bimboed_flirt_response_girlfriend
                    call fuck_person(the_person, start_position = kissing, private = _return, skip_intro = True) from _vt_bimboed_call_fuck_person_77
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_bimboed_flirt_response_girlfriend

                "Just flirt":
                    mc.name "I'm not bad? You're the one who's hard to resist... But, like, don't let it go to your head or anything, okay?"
                    $ mc.change_locked_clarity(10)
                    "You reach out and touch her cheek, a playful grin on your face... She looks all happy and content, and you can see the love in her eyes."
                    the_person "Ugh, you're so annoying... But, like, I guess I like that about you, okay?"

    else:
        # You're alone, so she's open to fooling around.
        the_person "Well you've got me all alone, so how about you show me just how lucky you feel... Like, right now, okay?"
        "She reaches down to your waist and cups your crotch, rubbing it gently... She looks all excited and playful, and you can see the anticipation in her eyes."
        mc.name "You're so wet for me already... I can, like, totally tell, okay?"
        the_person "Hmph, maybe... But, like, don't think you're getting off that easy, got it?"
        "She grinds against you, her hips moving in a slow circle... She looks all happy and content, and you can see the love in her eyes."
        mc.name "Damn, you feel so good... Like, totally amazing, [the_person.title]."
        "You reach up and grab her breasts, squeezing them gently... She looks all excited and playful, and you can see the anticipation in her eyes."
        the_person "Ooh, don't do that... But, like, don't stop either, okay?"
        "But she doesn't pull away, her body still pressed against yours... She looks all happy and content, and you can see the love in her eyes."
        menu:
            "Kiss her":
                if the_person.has_taboo("kissing"):
                    $ the_person.call_dialogue("kissing_taboo_break")
                    $ the_person.break_taboo("kissing")
                "You put your arms around [the_person.possessive_title!c]'s waist and rest your hands on her ass... She looks all excited and playful, and you can see the anticipation in her eyes."
                "You pull her close and kiss her sensually... She looks all happy and content, and you can see the love in her eyes."
                "She responds by pressing her body against you and grinding her hips against your thigh... She looks all excited and playful, and you can see the anticipation in her eyes."
                "You grab her hips and pull her closer, your crotches pressed together... She looks all happy and content, and you can see the love in her eyes."
                call fuck_person(the_person, start_position = kissing, skip_intro = True) from _vt_bimboed_call_fuck_person_78
                $ the_person.call_dialogue("sex_review", the_report = _return)
                $ the_person.review_outfit()

            "Just flirt":
                mc.name "I'm going to make you beg for it... Like, totally beg, okay?"
                "You lean in close, your breath hot against her ear... She looks all excited and playful, and you can see the anticipation in her eyes."
                the_person "Ooh, you're such a bad boy... But, like, I love it, okay?"
                "She rubs her body against yours, her hips moving seductively... She looks all happy and content, and you can see the love in her eyes."
                the_person "But don't think you're getting off that easy... I'm going to make you work for it, got it?"
    return

label bimboed_flirt_response_affair(the_person):
    # Lead in: mc.name "You look so good today [the_person.title], you're making me want to do some very naughty things to you."
    if mc.location.person_count > 1: #There are other people around, she's nervous about people finding out what you're doing.
        if (the_person.opinion.cheating_on_men *15) + the_person.effective_sluttiness() > 50: #SHe's turned on by flirting in public or doesn't think anything is wrong with it
            "[the_person.possessive_title!c] blushes and playfully bats her eyes at you, looking all cute and adorable."
            the_person "Oh my god, like, you're making me blush... I'm not used to this kind of attention from you, okay?"
            the_person "But, like, I have to admit... I'm curious. What do you have in mind, huh?"
            menu:
                "Find somewhere more quiet\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                    mc.name "I was thinking we could, like, slip away and find a more private spot... Just, like, us two, okay?"
                    "You and [the_person.title] exchange a flirtatious glance before hurrying off to find a quiet spot... She looks all excited and playful, and you can see the anticipation in her eyes."
                    call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_bimboed_flirt_response_affair
                    $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
                    "As soon as you're alone she pulls you into a deep and passionate kiss... She looks all happy and content, and you can see the love in her eyes."
                    $ the_person.draw_person(position = "kissing")
                    the_person "Mmm... I've been wanting to do that for, like, a while now."
                    "You wrap your arms around her waist and kiss her back, feeling her warmth and closeness... She looks all happy and content, and you can see the love in her eyes."
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _vt_bimboed_call_fuck_person_79
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_bimboed_flirt_response_affair
                "Just flirt":
                    mc.name "I, like, can't help but notice how beautiful you look today, [the_person.title]... You're, like, totally gorgeous, okay?"
                    the_person "Stop it, you're making me blush! But, like, I have to admit... You look pretty great yourself, huh?"
                    the_person "Just, like, don't get too cocky, okay? I'm still in charge here, got it?"
                    $ mc.change_locked_clarity(20)
                    "[the_person.possessive_title!c] playfully swats at your arm before leaning in close, looking all cute and playful."
                    the_person "But, like, I have to admit... I'm getting a little turned on by this whole thing, okay?"
                    "You can't help but feel a little flustered as she teases you, looking all happy and excited."
                    mc.name "I, like, can see that... Maybe we should find a more private place to continue this, huh?"
                    the_person "Mmm, maybe we should... But, like, first, let's enjoy this little moment here, okay?"
        else: #She's shy or nervous about being discovered
            "[the_person.possessive_title!c] looks around nervously, then back at you with a sheepish grin, looking all cute and adorable."
            the_person "Oh, um, you look nice today... I guess I should probably get going though, huh?"
            mc.name "Wait, don't go! I was thinking we could, like, grab a drink or something... Just, like, us two, okay?"
            $ mc.change_locked_clarity(15)
            the_person "Oh, you want to grab a drink? Okay, sure... But, like, just for a little bit, okay? I don't want to be out too late, got it?"
            "She glances around again, then leans in close and whispers, looking all cute and playful."
            the_person "And, like, just so you know... I'm still in charge here, even if we're just grabbing a drink, okay?"
            "You can't help but feel a little excited by her assertiveness, looking all happy and content."
            mc.name "Okay, okay... I'll behave, I promise."
    else:
        # the_person "Yeah? Well there's nobody around, and I'm not going to stop you."
        the_person "Oh yeah? Well then, do you want to share what all of these naughty things are? You have my attention, okay?"
        menu:
            "Feel her up":
                "You put your arms around [the_person.possessive_title!c]'s waist and rest your hands on her ass, feeling her warmth and closeness... She looks all happy and content, and you can see the love in her eyes."
                mc.name "You know, I've been waiting for this moment for, like, a while now... And I'm, like, totally excited, okay?"
                "You massage her butt, and she blushes and pushes you away lightly, looking all cute and playful."
                the_person "Hey, no need to be so forward! What's gotten into you, huh?"
                "You pull her close again and shift your hands to her breasts, squeezing them gently... She looks all happy and excited, and you can see the anticipation in her eyes."
                mc.name "Come on, don't be like that... I just wanted to make you feel good for once, okay?"
                call fuck_person(the_person, private = True, start_position = standing_grope, skip_intro = True) from _vt_bimboed_call_fuck_person_80
                $ the_person.call_dialogue("sex_review", the_report = _return)
                $ the_person.review_outfit()

            "Just flirt":
                $ mc.change_locked_clarity(10)
                "You put your arms around [the_person.possessive_title!c]'s waist and rest your hands on her ass, feeling her warmth and closeness... She looks all happy and content, and you can see the love in her eyes."
                mc.name "I, like, wish I had the time... You'll have to wait until later, okay?"
                "You massage her butt, and she sighs happily and leans her weight against you, looking all cute and adorable."
                the_person "Aww, are you sure? I was, like, really hoping we could, you know... Do something, okay?"
                "You slap her ass and step back, and she clings to you reluctantly before letting go, looking all happy and excited."
                the_person "Fine, but don't make me wait too long, okay? I have needs, and my [the_person.so_title] sure as hell isn't fulfilling them, got it?"
                mc.name "I won't make you wait long, I promise... You're, like, totally worth it, okay?"
                "She looks up at you with a playful pout, looking all cute and adorable."
                the_person "Promise you won't make me wait? Like, really promise, okay?"
                mc.name "I promise, baby... I'll, like, totally make it worth your while, okay?"
                "You both share a flirtatious smile, looking all happy and excited."
                the_person "Good... Because I'm, like, totally not sure I can handle it if you do, okay?"
    return

label bimboed_flirt_response_text(the_person):
    mc.name "Hey [the_person.title], how's it going? I'm feeling, like, totally bored and thought we could chat, okay?"
    "She replies with a hint of annoyance, but still looks all cute and adorable."
    if the_person.is_affair:
        the_person "Oh my god, like, great... You're bored again? You always seem to find ways to, like, bother me or something."
        the_person "Well, what do you want this time? I'm not, like, exactly thrilled about entertaining you, okay?"
        the_person "When can we get together? Like, for real this time?"
        mc.name "Some time soon, I promise... I'll, like, let you know, okay?"
    elif the_person.is_girlfriend:
        the_person "Bored, huh? That's, like, not exactly a surprise... You're always looking for something new to, like, entertain yourself, okay?"
        the_person "But, like, fine... We can hang out. Just don't expect me to, like, do anything special or anything, got it?"
        mc.name "Some time soon, I promise... I'll, like, let you know, okay?"
    elif the_person.love < 40:
        if the_person.effective_sluttiness() > the_person.love:
            the_person "Ugh, bored, really? Well, I suppose I can, like, keep you company for a bit... But don't think this means I'm, like, happy about it or anything, okay?"
        else:
            the_person "Bored, eh? That's, like, not surprising... You're always looking for a new distraction, okay?"
    else:
        if the_person.effective_sluttiness() > the_person.love:
            the_person "Fine, I'll talk to you... But don't think this means I'm, like, happy about it or anything, okay?"
            the_person "So, like, what do you want to talk about? I'm not, like, exactly thrilled about this, okay?"
        else:
            the_person "You're bored, huh? Well, that's, like, your problem, not mine... So, like, what do you want? Just don't expect me to be, like, all lovey-dovey about it, okay?"
    return

label bimboed_condom_demand(the_person):
    if the_person.wants_creampie:
        the_person "Oh my god, like, seriously? You need to put on a condom before we even, like, think about doing anything, okay?"
        the_person "I'm, like, totally not trying to be a buzzkill or anything, but you know it's, like, necessary and stuff."
        "She looks up at you with big, concerned eyes, still looking all cute and adorable."
    else:
        the_person "For, like, crying out loud... Do you have a condom on you? Put one on before you even, like, think about touching me, got it?"
        the_person "I don't, like, want to be stuck with some stupid disease or anything because you were, like, too careless or whatever, okay?"
        "She crosses her arms and looks at you with a stern expression, still looking all cute and playful."
    return

label bimboed_condom_ask(the_person):
    if the_person.on_birth_control:
        the_person "Oh my god, like, you want a condom? Fine, but I'm, like, on the pill, so it's not like I really need it or anything, okay?"
        "She looks up at you with big, confident eyes, still looking all cute and adorable."
        $ the_person.update_birth_control_knowledge()
    elif the_person.wants_creampie:
        the_person "Ugh, like, you want to cum inside me? Just, like, put on a condom, would you? It's not like I want to get pregnant or anything, got it?"
        the_person "But, like, I guess it's better than the alternative, right? I mean, who wants to deal with all that drama and stuff?"
        "She rolls her eyes and looks away, still looking all cute and playful."
        $ the_person.discover_opinion("creampies")
    else:
        the_person "Fine, I guess you should, like, use a condom... But, like, can you at least not make a mess with it? I don't want to, like, clean up after you or anything, okay?"
        the_person "And, like, please... No pulling out method, okay? That's just, like, asking for trouble and stuff."
        "She looks up at you with big, serious eyes, still looking all cute and adorable."
    return

label bimboed_condom_bareback_ask(the_person):
    if the_person.wants_creampie:
        if the_person.is_infertile:
            the_person "Oh my god, like, you're not seriously considering a condom, are you? Please, just, like, give me your hot, sticky load, okay?"
            the_person "I want to, like, feel you fill me up and make me scream with pleasure... That sounds, like, totally amazing, right?"
            "She looks up at you with big, eager eyes, still looking all cute and adorable."
        elif the_person.on_birth_control:
            the_person "Don't even, like, think about putting a condom on, [the_person.mc_title]... I'm, like, on the pill, so we're good to go, okay?"
            the_person "Just, like, fuck me raw and make me feel every inch of you... That sounds, like, totally hot, right?"
            "She smiles and looks up at you with big, confident eyes, still looking all cute and adorable."
            $ the_person.update_birth_control_knowledge()
        else:
            the_person "Forget the condom, [the_person.mc_title], I want to, like, feel you deep inside me... That sounds, like, totally amazing, right?"
            the_person "I don't, like, care about the risks or anything... It's, like, worth it for this kind of pleasure, okay?"
            if not the_person.knows_pregnant:
                the_person "Imagine, like, how hot it would be to get knocked up, too... That's, like, totally a turn-on, right?"
            "She looks up at you with big, eager eyes, still looking all cute and adorable."
        $ the_person.discover_opinion("creampies")
    else:
        the_person "Don't, like, bother with a condom, [the_person.mc_title]... I want to, like, feel you raw and unprotected, okay?"
        if not the_person.knows_pregnant:
            the_person "I don't, like, care about the risks or anything... It's, like, worth it for the intensity, right?"
        else:
            the_person "I, like, love it when you fuck me raw and make me feel like I'm, like, totally yours... That's, like, the best feeling ever, okay?"
        "She looks up at you with big, eager eyes, still looking all cute and adorable."
    return

label bimboed_condom_bareback_demand(the_person):
    if the_person.has_breeding_fetish: #Actively looking to get knocked up.
        if the_person.knows_pregnant:
            the_person "Oh my god, like, why bother with a condom? I want to get pregnant, so, like, fuck me raw, okay?"
            the_person "Hurry up, I'm, like, totally impatient... I need to feel you inside me, like, now."
            "She looks up at you with big, eager eyes, still looking all cute and adorable."
        elif the_person.is_infertile:
            the_person "Ugh, like, great... You're going to remind me I'm, like, infertile? Thanks a lot, okay?"
            "She rolls her eyes and looks away, still looking all cute and playful."
        else:
            the_person "Ugh, like, what's the point of fucking if you're not going to, like, knock me up, huh?"
            the_person "Hurry up and, like, give me that cock... I need it, like, so bad."
            "She looks up at you with big, eager eyes, still looking all cute and adorable."
    elif the_person.wants_creampie: #Just likes raw sex
        if the_person.is_infertile:
            the_person "Ugh, like, why bother with a condom? I'm, like, infertile anyway, okay?"
            "She shrugs and looks up at you with big, confident eyes, still looking all cute and adorable."
        elif the_person.on_birth_control:
            the_person "Forget the condom, [the_person.mc_title]... I'm, like, on the pill, so it's not a problem, okay?"
            the_person "Take me bareback and, like, make me scream... I need it, like, so bad."
            "She looks up at you with big, eager eyes, still looking all cute and adorable."
            $ the_person.update_birth_control_knowledge()
        else:
            the_person "Ugh, like, condoms are so annoying... Just, like, get inside me already, okay?"
            "She looks up at you with big, impatient eyes, still looking all cute and adorable."
    else:
        if the_person.is_infertile:
            the_person "Take me bareback, [the_person.mc_title]... It's, like, not like I can get pregnant or anything, okay?"
            the_person "Just, like, make me feel good... I need it, like, so bad."
            "She looks up at you with big, eager eyes, still looking all cute and adorable."
        elif the_person.on_birth_control:
            the_person "Forget the condom, [the_person.mc_title]... I'm, like, on the pill, okay?"
            the_person "Take me bareback and, like, make me feel every inch of you... I need it, like, so bad."
            "She looks up at you with big, eager eyes, still looking all cute and adorable."
            $ the_person.update_birth_control_knowledge()
        else:
            the_person "Ugh, like, condoms are so annoying... Just, like, get inside me already, okay?"
            the_person "I need to, like, feel you deep inside me... It's, like, the best feeling ever, okay?"
            "She looks up at you with big, eager eyes, still looking all cute and adorable."
    return

label bimboed_cum_face(the_person):
    if the_person.has_cum_fetish or the_person.obedience > 180:
        if the_person.has_cum_fetish or the_person.effective_sluttiness() > 60 or the_person.opinion.cum_facials > 0:
            the_person "Oh my god, like, so... Do you think this is a good look for me, [the_person.mc_title]?"
            "[the_person.title] smirks, then licks her lips and runs a finger through your semen, bringing it to her mouth... She looks all cute and playful, even with cum on her face."
            the_person "Mmm, like, taste your victory... That's, like, so hot, okay?"
            "She giggles and looks up at you with big, sparkling eyes, still looking all cute and adorable."
        else:
            the_person "Hmph, like, I suppose it's not a terrible look... But, like, I'm glad we're done here, okay?"
            "[the_person.title] wipes away some of your semen from her face, looking all annoyed and stuff... But still kinda cute and playful."
    else:
        if the_person.effective_sluttiness() > 80 or the_person.opinion.cum_facials > 0:
            the_person "Well, like, I guess this is one way to end things... Do you think I look good like this, huh?"
            "[the_person.title] smirks, then laughs and wipes away some of your semen from her face... She looks all cute and playful, even with cum on her face."
            "She looks up at you with big, sparkling eyes, still looking all cute and adorable."
        else:
            the_person "Ugh, like, just get that over with already... And, like, don't think you're getting a second chance, got it?"
            "[the_person.title] wipes away your semen, looking all put off and stuff... But still kinda cute and adorable."
    return

label bimboed_cum_mouth(the_person):
    if the_person.has_cum_fetish or the_person.obedience > 180:
        if the_person.has_cum_fetish or the_person.effective_sluttiness() > 60 or the_person.opinion.drinking_cum > 0:
            the_person "Oh my god, like, mmm... That's so... satisfying, [the_person.mc_title]."
            the_person "You, like, really know how to make me feel good... That's, like, the best thing ever, okay?"
            "She smiles and looks up at you with big, sparkling eyes, still looking all cute and adorable."
        else:
            "[the_person.title]'s face twists in disgust as she swallows your cum... She looks all grossed out and stuff."
            the_person "Ugh, like, there, done... Don't think I, like, enjoyed that one bit, okay?"
            "She makes a face and looks away, still looking all cute and playful, even when she's grossed out."
    else:
        if the_person.effective_sluttiness() > 80  or the_person.opinion.drinking_cum > 0:
            the_person "Mmm, like, you're quite the stud, [the_person.mc_title]... I can, like, see why you're so popular, huh?"
            the_person "You, like, really know how to, like, make a girl feel good... That's, like, so hot, okay?"
            "She smiles and looks up at you with big, sparkling eyes, still looking all cute and adorable."
        else:
            the_person "Ugh, like, that's... quite a taste... I hope you're, like, happy, okay?"
            "She makes a face and looks away, still looking all cute and playful, even when she's grossed out."
    return

label bimboed_cum_pullout(the_person):
    # Lead in: "I'm going to cum!"
    if mc.condom:
        if the_person.wants_creampie and not the_person.has_taboo("condomless_sex"): #TODO: FIgure out we want any more requirements for this to fire.
            if the_person.knows_pregnant:
                the_person "Oh my god, like, don't bother with the condom... Just, like, cum inside me and make me pregnant, okay?"
                the_person "I, like, don't care about the consequences right now... I just want your cum filling me up, like, so bad!"
                "She looks up at you with big, eager eyes, still looking all cute and adorable."
            elif the_person.on_birth_control:
                the_person "Oh fuck... I, like, can't take it any more... Take that condom off, [the_person.mc_title]!"
                "She moans desperately, looking all hot and bothered."
                the_person "I, like, give in... I want you to cum inside me, okay?"
            else:
                "She moans desperately, looking all hot and bothered."
                the_person "I, like, can't think straight... Just, like, take off the condom and cum inside me, okay?"
                $ the_person.update_birth_control_knowledge()
                the_person "I, like, want you to make me cum and then make me pregnant, you dirty fucker... That's, like, so hot, okay?"
                "She looks up at you with big, eager eyes, still looking all cute and adorable."
            menu: #TODO: Add a variant of this normally so you can stealth a girl (don't do that in real life, it's super fucked up).
                "Take off the condom":
                    "You pull out, barely clearing her pussy, and pull the condom off as quickly as you can manage... She looks all excited and eager, still looking all cute and adorable."
                    $ mc.condom = False
                    $ use_condom = False  # prevent putting on a new condom next sex loop

                "Leave it on":
                    "You ignore [the_person.possessive_title!c]'s request and keep the condom in place... She looks all disappointed and stuff, but still kinda cute and playful."
        else:
            the_person "Fuck yeah, I'm going to make you cum... That's, like, so hot, okay?"
            "She looks up at you with big, eager eyes, still looking all cute and adorable."
    else:
        if the_person.wants_creampie:
            if the_person.knows_pregnant: #She's already knocked up, so who cares!
                the_person "Creampie me, you dirty fucker... Make me cum, like, so hard, okay?"
                "She looks up at you with big, eager eyes, still looking all cute and adorable."
            elif the_person.opinion.creampies > 0:
                "[the_person.possessive_title!c] moans happily, looking all hot and bothered."
                if the_person.on_birth_control: #She just likes creampies.
                    the_person "Fuck yeah, fill me up with your cum, [the_person.mc_title]! Creampie me, like, so hard, okay?"
                else: #Yeah, she's not on BC and asking for you to creampie her. She's looking to get pregnant.
                    $ the_person.update_birth_control_knowledge()
                    the_person "Oh fuck, cum inside me and knock me up, [the_person.mc_title]! I want you to, like, breed me like a dirty slut, okay?"
                    "She looks up at you with big, eager eyes, still looking all cute and adorable."
            elif the_person.is_infertile:
                the_person "Cum wherever you want, you dirty fucker... I, like, can't get pregnant or anything, okay?"
                "She shrugs and looks up at you with big, confident eyes, still looking all cute and adorable."

            elif the_person.on_birth_control: #She's on the pill, so she's probably fine
                $ the_person.update_birth_control_knowledge()
                the_person "Cum wherever you want, you dirty fucker... I'm, like, on the pill, so it's all good, okay?"
                "She smiles and looks up at you with big, confident eyes, still looking all cute and adorable."

            else: #Too distracted to care about getting pregnant or not. Oh well, what could go wrong?
                the_person "Do it! Cum, like, now, okay?"
                "She looks up at you with big, eager eyes, still looking all cute and adorable."

        else:
            if the_person.is_infertile:
                the_person "Just, like, pull out, okay? I don't want your cum inside me, you dirty fucker... That's, like, so not hot, okay?"
                "She looks up at you with big, serious eyes, still looking all cute and adorable."

            elif not the_person.on_birth_control: #You need to pull out, I'm not on the pill!
                $ the_person.update_birth_control_knowledge()
                the_person "Fuck, pull out, you dirty fucker! I'm, like, not on the pill, okay?"
                "She looks up at you with big, worried eyes, still looking all cute and adorable."

            elif the_person.opinion.creampies < 0:
                the_person "Pull out, I don't want you to cum in me, you dirty fucker... That's, like, so not hot, okay?"
                "She looks up at you with big, serious eyes, still looking all cute and adorable."

            else:
                the_person "Hell yeah, pull out and cum all over me like a dirty slut... That's, like, so hot, okay?"
                "She looks up at you with big, eager eyes, still looking all cute and adorable."
    return

label bimboed_cum_condom(the_person):
    if the_person.effective_sluttiness() > 75 or the_person.opinion.creampies > 0:
        the_person "Oh my god, like, it feels so good... If your condom broke, it would be, like, inside me, and I'd be, like, totally pregnant, okay?"
        "She looks up at you with big, eager eyes, still looking all cute and adorable."
    else:
        the_person "Oh my god, like, I hope you buy good condoms... Because, like, that's a lot of cum, okay?"
        the_person "But, like, then again... Maybe you're, like, dreaming of knocking me up and getting me pregnant, huh?"
        "She raises an eyebrow and looks at you with a playful expression, still looking all cute and adorable."
    return

label bimboed_cum_vagina(the_person):
    if the_person.has_taboo("creampie"):
        $ the_person.call_dialogue("creampie_taboo_break")
        $ the_person.break_taboo("creampie")
        return
    if the_person.wants_creampie:
        if the_person.knows_pregnant:
            the_person "Oh my god, like, fine... I guess I can admit it now, but only because I'm, like, already pregnant from your other, uh, impressive performances... Your cum just feels, like, so good inside me, okay?"
            "She looks up at you with big, happy eyes, still looking all cute and adorable."

        elif the_person.is_infertile:
            the_person "Oh, stop being so dramatic! Of course you're not going to get me pregnant, I'm, like, infertile, remember? But seriously, your cum is, like, pretty great... just don't expect me to admit it to anyone else, okay?"
            "She rolls her eyes and looks away, still looking all cute and playful."

        elif the_person.on_birth_control:
            if the_person.has_significant_other:
                the_person "Well, well, well... Look at you go! I guess it's, like, a good thing I'm on the pill, huh? Or maybe I'll just tell [the_person.SO_name] that it was, like, someone else's... Ugh, why do you have to be so frustrating, okay?"
                "She looks up at you with big, playful eyes, still looking all cute and adorable."

            else:
                if the_person.knows_pregnant:
                    the_person "Oh fuck, like, that's a lot of cum... Good thing I'm, like, already pregnant, because I don't think you're, like, firing blanks or anything, okay?"
                elif the_person.is_infertile:
                    the_person "Oh fuck, like, that's a lot of cum... I'll be, like, dripping your cum all day long, okay?"
                else:
                    the_person "Oh fuck, like, that's a lot of cum... Good thing I'm, like, on the pill, because I don't think you're, like, firing blanks or anything, okay?"
                $ the_person.update_birth_control_knowledge()
                "She looks up at you with big, happy eyes, still looking all cute and adorable."

        elif the_person.effective_sluttiness() > 75 or the_person.opinion.creampies > 0:
            if the_person.has_significant_other:
                the_person "Okay, okay, I get it! You're, like, great in bed, but don't think I'm going to, like, start flaunting our little secret around my [the_person.so_title]... At least, not until I figure out how to, like, explain it, okay?"
                "She looks up at you with big, playful eyes, still looking all cute and adorable."

            else:
                the_person "Ugh, fine... I'll admit it, you're, like, pretty amazing when you're like this... But don't think this means I'm going to, like, start begging for more or anything, okay? I just need to, like, process this, okay?"
                "She looks up at you with big, happy eyes, still looking all cute and adorable."

        else:
            if the_person.has_significant_other:
                the_person "You really know how to, like, make a girl feel special, don't you? But let's, like, keep this between us, okay? I don't think [the_person.SO_name] would, like, understand or anything, okay?"
                "She looks up at you with big, worried eyes, still looking all cute and adorable."

            else:
                the_person "Wow... I guess I didn't, like, expect that from you... But I have to admit, it was, like, kind of nice... Just don't get any ideas, okay? I'm not, like, ready for anything serious or anything, got it?"
                "She looks up at you with big, happy eyes, still looking all cute and adorable."

    else: #She's angry
        if the_person.knows_pregnant:
            the_person "Ugh, what is wrong with you? I, like, specifically told you not to do that! Oh well, since I'm, like, already pregnant..."
            "She looks up at you with big, angry eyes, still looking all cute and adorable."

        elif not the_person.on_birth_control:
            if the_person.has_significant_other:
                the_person "Oh, great... Just what I needed... You forgot to pull out, and now I'm going to have to, like, deal with [the_person.SO_name]'s anger, okay?"
                if the_person.kids > 0:
                    the_person "... Again, okay?"
                "She looks up at you with big, worried eyes, still looking all cute and adorable."

            else:
                the_person "Oh fuck, I said to pull out! I'm, like, not on the pill, [the_person.mc_title], what happens if I get pregnant, huh?"
                $ the_person.update_birth_control_knowledge()
                the_person "What is wrong with you? You know I'm, like, not on the pill! Now look what you've done... I guess next time we'll have to, like, use a condom or something, okay?"
                "She looks up at you with big, angry eyes, still looking all cute and adorable."

        elif the_person.is_infertile:
            the_person "Unbelievable! I, like, told you to pull out, and now you've gone and made a mess... What a pain in the ass, okay?"
            "She rolls her eyes and looks away, still looking all cute and playful."

        elif the_person.has_significant_other:
            the_person "You're, like, really going to make me tell [the_person.SO_name] about this, aren't you? Fine, I'll deal with it... Just be more careful next time, okay?"
            $ the_person.update_birth_control_knowledge()
            the_person "I don't want to have to, like, make you wear a condom or anything... So be a little more careful next time, got it?"
            "She looks up at you with big, serious eyes, still looking all cute and adorable."

        elif the_person.opinion.creampies < 0:
            the_person "Oh, great... Just what I needed... You couldn't even, like, follow a simple instruction, could you? Now look at what a mess you've made, okay?"
            "She looks up at you with big, angry eyes, still looking all cute and adorable."

        else:
            the_person "You, like, really need to work on your timing... I told you to pull out, not do the exact opposite, okay?"
            the_person "Just, like, remember... I'm not going to be, like, as forgiving next time if you can't follow simple instructions, got it?"
            "She looks up at you with big, serious eyes, still looking all cute and adorable."
    return

label bimboed_cum_anal(the_person):
    if the_person.has_taboo("anal creampie"):
        $ the_person.call_dialogue("anal_creampie_taboo_break")
        $ the_person.break_taboo("anal creampie")
        return
    if the_person.sluttiness > 75 or the_person.opinion.anal_creampies > 0:
        the_person "Oh my god, like, fine... I guess it's okay if you do that... But don't think I'm going to, like, start asking for it all the time or anything, okay?"
        "She looks up at you with big, playful eyes, still looking all cute and adorable."
    elif the_person.opinion.anal_creampies < 0:
        the_person "Oh, come on... not in there! I don't need to be, like, embarrassed like that, okay?"
        "She looks up at you with big, worried eyes, still looking all cute and adorable."
    else:
        the_person "Oh, alright... if you insist... But just this once, and don't think I'm going to, like, start liking it or anything, got it?"
        "She looks up at you with big, hesitant eyes, still looking all cute and adorable."
    return

label bimboed_surprised_exclaim(the_person):
    $rando = renpy.random.choice(["Oh my god, like, what the hell?", "Ugh, really? Like, seriously?", "Why now, of all times?", "This again? Like, come on!", "Not again, okay?!", "Seriously, like, what's going on?", "Great, just great...", "Oh, joy... Like, not.", "Fucking perfect... Not.", "Unbelievable, like, for real!", "Not again, like, please!", "Why can't I, like, have a normal day for once?"])
    the_person "[rando]"
    "She looks up at you with big, surprised eyes, still looking all cute and adorable."
    return

label bimboed_talk_busy(the_person):
    if the_person.obedience > 120:
        the_person "Oh my god, like, I don't have time for this, okay? I've got, like, way too much on my plate right now, [the_person.mc_title]."
        "She looks up at you with big, frazzled eyes, still looking all cute and adorable."
    else:
        the_person "Listen, like, I'd love to catch up and all... But I'm, like, totally swamped with things to do, okay? Maybe we can, like, talk later or something?"
        "She smiles and looks up at you with big, apologetic eyes, still looking all cute and adorable."
    return

label bimboed_sex_strip(the_person):
    if the_person.sluttiness < 20:
        if the_person.arousal_perc < 50:
            the_person "Ugh, fine... I'll, like, take off some clothes, but don't think I'm doing this because I, like, like you or anything, okay? I just need to, like, get comfortable, that's all."
            "She looks up at you with big, hesitant eyes, still looking all cute and adorable."
            mc.name "Come on, babe... It's just us here. You can, like, relax, okay?"
            the_person "I don't care! I'm still not, like, comfortable... And don't call me 'babe', that's, like, weird, okay?"
            "She looks away, still looking all cute and playful."
            mc.name "Okay, okay... I'll stop. Just, like, take your time, okay?"
            "She nods and starts to slowly take off her clothes, still looking all cute and adorable."
        else:
            the_person "Alright, alright... I'll, like, take off a few things, but don't expect me to be, like, impressed by your reaction or anything, okay? I'm just, like, taking off some clothes, big deal."
            "She looks up at you with big, confident eyes, still looking all cute and adorable."
            mc.name "Aww, come on... You're being a little rough, okay? Just let me see you a little more, okay?"
            the_person "Fine, but only because you, like, asked nicely... And don't think this means I, like, like you or anything, got it?"
            "She smiles and starts to take off her clothes, still looking all cute and adorable."
    elif the_person.sluttiness < 60:
        if the_person.arousal_perc < 50:
            the_person "Fine, I'll, like, make an exception and get a little more comfortable, okay? But don't get any, like, ideas or anything, okay?"
            "She looks up at you with big, hesitant eyes, still looking all cute and adorable."
            mc.name "I promise, I won't get any, like, ideas, okay? I just want to, like, make sure you're comfortable, okay?"
            the_person "Ugh, fine... But don't think I'm doing this for you, okay? I just need to, like, get a little more comfortable, that's all."
            "She nods and starts to slowly take off her clothes, still looking all cute and adorable."
            mc.name "I understand, okay? Just, like, take your time and let me know if you need anything, okay?"
            "She smiles and looks up at you with big, grateful eyes, still looking all cute and adorable."
        else:
            the_person "Okay, okay... I'll, like, take off a few more things if it'll, like, make you happy, okay? But don't think I'm doing this because I'm, like, into you or anything, got it?"
            "She looks up at you with big, playful eyes, still looking all cute and adorable."
            mc.name "I know, I know... You're just, like, doing it because you, like, want to, right?"
            the_person "Whatever, okay? Just let me, like, get this off and we can, like, get on with this, okay? And don't think this means I'm, like, going to start liking you or anything, got it?"
            "She smiles and starts to take off her clothes, still looking all cute and adorable."
    else:
        if the_person.arousal_perc < 50:
            the_person "Ugh, fine... I'll, like, do it, okay? But just for you, I'll, like, make an exception, okay? And don't think I'm doing this because I, like, like you or anything, got it?"
            "She looks up at you with big, hesitant eyes, still looking all cute and adorable."
            mc.name "Thanks, babe... You're, like, making me really happy right now, okay?"
            the_person "Don't call me 'babe', okay? And don't get, like, too happy, okay? I'm just, like, doing this because I, like, have to, okay?"
            "She looks away, still looking all cute and playful."
        else:
            the_person "Great, now let me, like, get this off and we can, like, get on with this, okay? I'm, like, dying over here, okay? But don't expect me to be, like, all happy about it or anything, got it?"
            "She looks up at you with big, eager eyes, still looking all cute and adorable."
            mc.name "Aww, come on... You're, like, being a little grumpy, okay? Let's just, like, have some fun, okay?"
            the_person "Fine, okay? But don't expect me to, like, start smiling and laughing or anything, got it?"
            "She smiles and starts to take off her clothes, still looking all cute and adorable."
    return

label bimboed_sex_watch(the_person, the_sex_person, the_position):
    $ title = the_person.title if not the_person.is_stranger else "The stranger"
    if the_person.sluttiness < the_position.slut_requirement - 20:
        $ the_person.draw_person(emotion = "angry", display_transform = character_left_flipped)
        the_person "Ugh, like, seriously? Can you two, like, keep it down? I'm trying to, like, concentrate, okay?"
        $ the_person.change_stats(obedience = -2, happiness = -1)
        "[title] rolls her eyes and tries to ignore you and [the_sex_person.fname] [the_position.verb], looking all annoyed and stuff."
        return False
    if the_person.sluttiness < the_position.slut_requirement - 10:
        $ the_person.draw_person(display_transform = character_left_flipped)
        the_person "Honestly, like, you two are so embarrassing... Can't you, like, keep it a little more private, okay?"
        $ the_person.change_happiness(-1)
        "[title] looks away, trying to pretend she's not, like, interested in what you and [the_sex_person.fname] are doing, but still looking all cute and adorable."
        return False
    if the_person.sluttiness < the_position.slut_requirement:
        $ the_person.draw_person(display_transform = character_left_flipped)
        if not is_watching(the_person):
            the_person "You're, like, really getting into it, aren't you? I suppose it's, like, kind of hot... But, like, don't think I'm going to join in or anything, okay?"
        $ the_person.change_slut(1, 30)
        "[title] watches you and [the_sex_person.fname] [the_position.verb], trying not to, like, blush or anything, but still looking all cute and adorable."
        return True
    if the_person.sluttiness >= the_position.slut_requirement and the_person.sluttiness < the_position.slut_cap:
        $ the_person.draw_person(display_transform = character_left_flipped)
        if not is_watching(the_person):
            the_person "Oh my god, like, this looks like so much fun... Can I, like, join in, okay?"
        $ the_person.change_slut(1, 50)
        "[title] watches you and [the_sex_person.fname] [the_position.verb], her eyes sparkling with, like, excitement and stuff, looking all cute and adorable."
        return True
    $ the_person.draw_person(emotion = "happy", display_transform = character_left_flipped)
    if renpy.random.randint(0, 1) == 0:
        the_person "You know, [the_person.mc_title], [the_sex_person.fname] is, like, really getting into this... Maybe you should, like, spice things up a bit, okay?"
    else:
        call watcher_position_comment(the_person, the_sex_person, the_position) from _call_watcher_position_comment_bimboed_sex_watch
    "[title] watches with, like, interest as you and [the_sex_person.fname] [the_position.verb], looking all cute and adorable."
    return True

label bimboed_being_watched(the_person, the_watcher, the_position):
    $ title = the_watcher.fname if not the_watcher.is_stranger else "the stranger"
    if the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #They agree you should give it to her harder
        the_person "Oh my god, like, I guess you're right, [the_person.mc_title]... But, like, don't think I'm going easy on you just because there's, like, an audience or anything, okay?"
        $ the_person.change_arousal(1)
        "[the_person.title] seems, like, totally turned on by [title] watching you and her [the_position.verb]... She's, like, so into it, okay?"
        "She looks up at you with big, eager eyes, still looking all cute and adorable."
    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's super slutty and doesn't care what people think.
        the_person "You know, [title], I'm like, totally not even caring what you think right now... But it's, like, pretty obvious you're, like, turned on or whatever, okay?"
    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #She's super slutty and encourages the watcher to be slutty.
        the_person "Oh, come on, [title]! Don't be, like, shy or anything! You know you, like, want a taste of this action, okay?"
        $ the_person.change_arousal(1)
        "[the_person.title] seems, like, totally turned on by [title] watching you and her [the_position.verb]... She's, like, so into it, okay?"
        "She looks up at you with big, eager eyes, still looking all cute and adorable."
    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #She's into it and encouraged by the slut watching her.
        "[the_person.fname] glances at [title], looking all curious and stuff."
        the_person "Yeah, like, I guess I can handle a little more... for now, okay?"
        $ the_person.change_arousal(1)
        "[the_person.title] seems, like, totally turned on by [title] watching you and her [the_position.verb]... She's, like, so into it, okay?"
        "She looks up at you with big, eager eyes, still looking all cute and adorable."
    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's into it but shamed by the prude watching her.
        the_person "Ugh, like, why do you have to be here, [title]? Can't you, like, just leave me alone or something, okay?"
        $ the_person.change_stats(arousal = -1, slut = -1)
        "[the_person.title] seems, like, super uncomfortable with [title] nearby... She's, like, so not into it, okay?"
        "She looks away, still looking all cute and adorable, but also kinda embarrassed and stuff."
    else: #the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #They're both into it but not fanatical about it.
        "[the_person.possessive_title!c] rolls her eyes at [title], looking all playful and stuff."
        the_person "Whatever, [title], you're, like, missing out... Maybe next time you'll, like, get a chance or something, okay?"
        $ the_person.change_stats(arousal = 1, slut = 1, max_slut = 30)
        "[the_person.title] seems, like, more comfortable [the_position.verbing] you with [title] around... She's, like, so into it, okay?"
        "She smiles and looks up at you with big, happy eyes, still looking all cute and adorable."
    return

label bimboed_work_enter_greeting(the_person):
    if the_person.happiness < 80 or the_person.love < 0:
        "[the_person.title] glances at you when you enter the room, her expression, like, totally unreadable and stuff."
        the_person "What do you, like, want? I'm in the middle of something, okay?"
        "She goes back to her work, not looking up again, but still looking all cute and adorable."

    elif the_person.happiness > 130:
        if the_person.sluttiness > 40:
            the_person "Hey [the_person.mc_title], like, just the person I was hoping to see, okay?"
            "Her eyes, like, sparkle with mischief as she leans against her desk, looking all playful and stuff."
            the_person "You know what they say: all work and no play makes for a, like, dull girl, right?"
            "She winks, inviting you to, like, join her in some 'play', and looking all cute and adorable."
        else:
            "[the_person.title] looks up from her work and, like, smiles at you when you enter the room, okay?"
            the_person "Hey [the_person.mc_title], it's, like, nice to have you stop by... You know, just to, like, say hi and stuff."
            "She blushes slightly, looking away before quickly glancing back at you, still looking all cute and adorable."

    else:
        if the_person.sluttiness > 60:
            $ the_person.draw_person(position = "stand4")
            "[the_person.title] walks over to you when you come into the room, her hips, like, swaying seductively and stuff."
            the_person "Well, well, well... Look who, like, decided to drop by, okay?"
            "She leans in close, her voice, like, husky and sultry and stuff."
            the_person "I've, like, been waiting for you, [the_person.mc_title]... You know, just to, like, catch up and stuff."
            "She brushes her fingers against your arm, sending, like, shivers down your spine and stuff."
        else:
            the_person "Hey [the_person.mc_title]... Need anything? I mean, if you're not, like, too busy or anything, okay?"
            "She looks up at you, her eyes, like, soft and inviting and stuff."
    return

label bimboed_date_seduction(the_person):
    if the_person.is_girlfriend:
        "[the_person.possessive_title!c] grabs your hand and pulls you around to look at her, looking all cute and adorable."
        the_person "Hey, like, that was such a great time, okay? So I was thinking..."
        $ mc.change_locked_clarity(30)
        if the_person.effective_sluttiness(["vaginal_sex", "condomless_sex"]) > 60 and the_person.wants_creampie and the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex >= 0 and the_person.opinion.creampies >= 0 and not the_person.on_birth_control and not the_person.knows_pregnant:
            if the_person.opinion.creampies > 0: #No condoms, loves creampies, she's basically asking you to knock her up. So... have her ask you to knock her up!
                the_person "You're, like, probably just going to say no, but I really want to get knocked up by someone like you, okay?"
                the_person "So, like, are you going to make me pregnant or what? I bet you could, like, give me some amazing kids, okay?"
            else:
                the_person "I don't, like, care if you don't use a condom, okay? I just want you to, like, fuck me and make me feel good, okay?"
                the_person "You're, like, so much better than those other guys, anyway... I'm, like, so into you, okay?"
        elif the_person.effective_sluttiness(["vaginal_sex", "condomless_sex"]) > 60 and the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex > 0:
            the_person "Ugh, fine... If you really want to know, I'd rather not use a condom, okay?"
            the_person "But, like, don't think I'm doing it for you or anything, okay? It just, like, feels better that way, okay?"
        elif the_person.effective_sluttiness(["vaginal_sex"]) > 50 and the_person.opinion.vaginal_sex > 0:
            the_person "You know, I didn't, like, really want to go home with someone like you, okay?"
            the_person "But, like, you're kind of growing on me, okay?"
            the_person "So, like, do you want to, like, fuck me or what, okay?"
        elif the_person.effective_sluttiness(["anal_sex"]) > 60 and the_person.opinion.anal_sex > 0:
            the_person "I don't, like, know why I'm even bothering to ask you this, but... do you want to, like, fuck my ass, okay?"
            the_person "It's, like, not like I'm asking for much, but you're, like, probably just going to say no anyway, okay?"
        elif the_person.effective_sluttiness(["sucking_cock"]) > 40 and the_person.opinion.giving_blowjobs > 0:
            the_person "You know, I'm, like, not really in the mood to do this, but... you're, like, kind of cute when you're all worked up, okay?"
            the_person "So, like, do you want a blowjob or what, okay?"
        elif the_person.effective_sluttiness() > 40 and the_person.opinion.being_covered_in_cum > 0:
            the_person "Ugh, fine... If you really want to know, I'd be, like, okay with getting covered in your cum, okay?"
            the_person "But, like, don't expect me to be, like, all happy about it or anything, okay?"
        elif the_person.effective_sluttiness(["touching_body"]) > 40 and the_person.opinion.giving_tit_fucks > 0 and the_person.has_large_tits:
            the_person "I don't, like, know why I'm even telling you this, but... I'd be, like, okay with sucking you off between my tits, okay?"
            the_person "But, like, don't think I'm doing it because I, like, like you or anything, okay?"
        else: #She's not very slutty, so she leaves the invitation open to interpretation
            the_person "You know, I don't, like, really feel like going home with you or anything, okay?"
            the_person "But, like, I guess I could be, like, persuaded if you do something, like, really good, okay?"
            "She, like, smirks and looks up at you with big, playful eyes, still looking all cute and adorable."
    elif the_person.is_affair:
        the_person "So, like, my [the_person.so_title] won't be home tonight, I was thinking..."
        "She, like, reaches down and cups your crotch, rubbing it gently through your pants, looking all flirtatious and stuff."
        $ mc.change_locked_clarity(40)
        if the_person.wants_creampie and the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex >= 0 and the_person.opinion.creampies >= 0 and not the_person.on_birth_control and not the_person.knows_pregnant:
            if the_person.opinion.creampies > 0: #No condoms, loves creampies, she's basically asking you to knock her up. So... have her ask you to knock her up!
                the_person "Fine, let's go back to my place so you can, like, pin me to the bed and creampie me all night long, okay?"
                the_person "I swear, just the thought of your cum inside me is, like, making me want to puke and yet... I'm, like, getting wet, okay?"
            else:
                the_person "Alright, let's go back to my place... You can, like, pin me to the bed and fuck me bareback all night long, okay?"
                the_person "I, like, hate how much I want this, but I do... So just, like, fuck me up with your cock already, okay?"
        elif the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex > 0:
            the_person "Ugh, fine... Let's go back to my place and, like, fuck all night, okay? No condoms, okay?"
            the_person "I, like, don't want to admit it, but I'm, like, really looking forward to this, okay?"
        elif the_person.opinion.vaginal_sex > 0:
            the_person "Fine, let's go back to my place and you can, like, pound my tight fucking pussy until I'm, like, a wreck, okay?"
            the_person "I, like, hate how much I enjoy this, but... I do, okay? So, like, do it, okay?"
        elif the_person.opinion.anal_sex > 0:
            the_person "Ugh, alright... Let's go back to my place so you can, like... you know, okay?"
            the_person "I, like, don't want to admit it, but my ass is, like, really excited for this, okay?"
        elif the_person.opinion.giving_blowjobs > 0:
            the_person "Fine, let's go back to my place and you can, like, choke me out with your cock, okay?"
            the_person "I, like, hate how much I want this, but I do... So just, like, do it already, okay?"
        elif the_person.opinion.being_covered_in_cum > 0:
            the_person "Ugh, alright... Let's go back to my place, and you can, like, cover me in your sperm all night, okay?"
            the_person "I, like, hate how much I enjoy this, but... I do, okay? So just, like, do it, okay?"
        elif the_person.opinion.giving_tit_fucks > 0 and the_person.has_large_tits:
            the_person "Fine, let's go back to my place so I can, like... you know, okay?"
            the_person "I, like, hate how much I enjoy this, but I do... So just, like, do it already, okay?"
        elif the_person.opinion.cheating_on_men > 0:
            the_person "Ugh, fine... Let's go back to my place, and you can, like, do all the things I tell my [the_person.so_title] I hate, okay?"
            the_person "I, like, don't want to admit it, but I'm, like, really looking forward to this, okay?"
        else:
            the_person "Ugh, let's go back to my place and, like, make him really regret leaving me alone for the night, okay?"
    elif not the_person.has_significant_other:
        $ mc.change_locked_clarity(20)
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                the_person "Ugh, fine... I've had a, like, blast [the_person.mc_title], but there are, like, a few more things I'd like to do with you, okay? Want to come back to my place and, like, find out what they are, okay?"
            else:
                the_person "Whatever... You've, like, been a blast [the_person.mc_title], okay? Want to come back to my place, have a few drinks, and, like, see where things lead, okay? I suppose, okay?"
        else:
            if the_person.love > 40:
                the_person "Fine, I don't, like, want to say goodbye either, okay? Tonight's, like, been amazing [the_person.mc_title], okay? Do you want to come back to my place and, like, have a few drinks, okay?"
            else:
                the_person "Whatever... This might be, like, crazy, but I had a, like, great time tonight and you, like, make me a little crazy, okay? Do you want to come back to my place and, like, see where things go, okay? I don't, like, know why I'm even asking, okay?"
    else:
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                $ mc.change_locked_clarity(20)
                the_person "Ugh, fine... I'm, like, not done with you yet [the_person.mc_title], okay? Want to come back to my place, okay? But don't, like, think you're getting away with anything, okay?"
                the_person "My [the_person.so_title] won't be home until morning, so we would, like, have plenty of time, okay?"
            else:
                $ mc.change_locked_clarity(20)
                the_person "Whatever... This might be, like, crazy, but do you want to come back to, like, have another drink with me, okay? I suppose, okay?"
                the_person "My [the_person.so_title] is, like, stuck at work and I don't, like, want to be left all alone, okay?"
        else:
            if the_person.love > 40:
                $ mc.change_locked_clarity(20)
                the_person "Whatever... You're, like, making me feel crazy [the_person.mc_title], okay? Do you want to come, like, have a drink at my place, okay? But don't, like, think this means anything, okay?"
                the_person "My [the_person.so_title] won't be home until morning, and we have, like, a big bed you could, like, help me warm up, okay?"
            else:
                $ mc.change_locked_clarity(20)
                the_person "Whatever... This is, like, crazy, but would you want to, like, have one last drink at my place, okay? My [the_person.so_title] won't be home until morning... I suppose, okay?"
    return

label bimboed_sex_end_early(the_person):
    if the_person.sluttiness > 50:
        if the_person.love > 40:
            if the_person.arousal_perc > 60:
                the_person "Oh my god, like, really? You're done already? I was, like, just getting into it, [mc.name]... I mean, you're not, like, exactly the most energetic partner I've ever had, okay?"
                the_person "But, like, hey, I'll give you credit, you did try your best... Or, like, at least, as best as you could, okay?"
                "She looks up at you with big, disappointed eyes, still looking all cute and adorable."
            else:
                the_person "Well, like, I suppose that's it? I was, like, ready to give you a lot more... But I guess you're not, like, exactly the most enthusiastic about this whole situation, are you, okay?"
                "She shrugs and looks away, still looking all cute and adorable."
        else:
            if the_person.arousal_perc > 60:
                the_person "Hmph, like, you're sure you're finished? I was, like, really enjoying this... You know, I don't usually do this, but I was, like, actually getting kind of into it, okay?"
                the_person "But, like, I guess you're not, like, exactly the most experienced, are you? I mean, it's not, like, I'm the one who needs to learn how to do this properly, okay?"
                "She rolls her eyes and looks away, still looking all cute and adorable."
            else:
                the_person "I guess it was, like, okay, I suppose... I mean, it's not, like, I was expecting much from you in the first place, okay?"
                "She shrugs and looks away, still looking all cute and adorable."
    else:
        if the_person.love > 40:
            if the_person.arousal_perc > 60:
                the_person "Oh, come on, [mc.name], like, you can't leave me hanging like this... I mean, I was, like, actually starting to enjoy this, okay?"
                the_person "But, like, hey, I guess you're not, like, exactly the most romantic guy out there, are you, okay?"
                "She looks up at you with big, pleading eyes, still looking all cute and adorable."
            else:
                the_person "Well, like, that was a nice little interlude, I suppose... I mean, it's not, like, I'm the type to be all lovey-dovey and stuff, okay?"
                "She smiles and looks away, still looking all cute and adorable."
        else:
            if the_person.arousal_perc > 60:
                the_person "Geez, like, I guess that was enough... I mean, I don't know why you even, like, bother trying, you're not, like, exactly the best at this, are you, okay?"
                "She rolls her eyes and looks away, still looking all cute and adorable."
            else:
                the_person "Good, like, it's over... Now let's, like, get this over with, okay? I mean, I've got, like, better things to do than hang around with someone who can't even, like, manage to get it right, okay?"
                "She shrugs and looks away, still looking all cute and adorable."
    return

label bimboed_sex_take_control(the_person):
    if the_person.arousal_perc > 60:
        the_person "Oh my god, like, what do you think you're doing, [mc.name]? Don't just, like, leave me hanging like this, okay? I mean, I'm the one who's, like, supposed to be in control here, not you, got it?"
        the_person "But, like, hey, if you're not going to, like, finish the job, then I will, okay? And don't, like, think for a second that I won't make you regret it, okay?"
        "She looks up at you with big, determined eyes, still looking all cute and adorable."
    else:
        the_person "Ugh, like, really? You're not even going to, like, finish what you started? Fine, I'll, like, do it myself then, okay? And don't, like, think you can just, like, waltz in here and expect me to be all, like, weak and submissive, okay? I'm not, like, that kind of girl, [mc.name], got it?"
        "She rolls her eyes and looks away, still looking all cute and adorable."
    return

label bimboed_sex_beg_finish(the_person):
    the_person "Oh my god, like, okay, fine, [mc.name]... You want to, like, play it cool? I'll, like, let you off the hook this time, but just know that I'm, like, going to make you pay for this, okay?"
    the_person "And when I'm, like, done, I'm going to make sure you know, like, exactly who's in control here, got it?"
    "She looks up at you with big, sassy eyes, still looking all cute and adorable."
    "She pouts and crosses her arms, still looking all playful and stuff."
    return

label bimboed_sex_review(the_person, the_report):
    $ comment_position = the_person.pick_position_comment(the_report)
    if comment_position is None:
        return #You didn't actually do anything, no need to comment.

    $ used_obedience = the_report.get("obedience_used", False) #True if a girl only tried a position because you ordered her to.
    $ the_person.draw_person()  # make sure she stands up for talking with you

    #She's worried about her SO finding out because it was in public
    if the_report.get("was_public", False) and the_person.has_significant_other and the_person.opinion.cheating_on_men <= 0: #It was public and she cares.
        if the_person.is_affair: #Dialogue about her being into it, but you can't do this in case she gets caught.
            the_person "Oh my god, like, this is so bad! I'm, like, really getting into this, but we can't, like, get caught, okay?"
            the_person "What if, like, someone sees us and tells my [the_person.so_title]? I'll, like, never hear the end of it, okay?"
            "She looks around nervously, still looking all cute and adorable."

        elif used_obedience:
            the_person "I'm, like, so not comfortable with this... Someone might, like, recognize me and tell my [the_person.so_title], okay?"
            mc.name "Don't worry, nobody's going to, like, tell anyone, okay? We're, like, being careful, okay?"
            the_person "I hope you're, like, right... I don't want, like, anyone finding out about this, okay?"
            "She looks up at you with big, worried eyes, still looking all cute and adorable."

        else:
            $ the_person.call_dialogue("surprised_exclaim")
            the_person "Oh no, like, we're out in public! Someone might, like, see us and tell my [the_person.so_title], okay? I'll, like, be so screwed, okay?"
            mc.name "Don't worry, nobody's, like, paying attention to us, okay? Nobody's going to, like, tell your [the_person.so_title], okay?"
            the_person "I hope you're, like, right... I don't want, like, anyone knowing about this, okay?"
            "She looks around nervously, still looking all cute and adorable."

    #She's single, but worried that you did in public.
    elif the_report.get("was_public", False) and (the_person.effective_sluttiness()+10*the_person.opinion.public_sex < comment_position.slut_cap):
        if used_obedience:
            the_person "Ugh, like, I'm so not cool with this... Everyone's, like, staring at us like we're, like, some kind of perverts, okay?"
            the_person "I'll, like, never live this down, [mc.name], okay? People are going to, like, talk about this for weeks, okay?"
            "She looks around embarrassed, still looking all cute and adorable."

        else:
            the_person "Oh no, like, we're in public! Everyone's, like, watching us and judging us for this, okay?"
            mc.name "Don't worry, nobody, like, really cares what we're doing, okay? They're just, like, curious, okay?"
            the_person "I hope you're, like, right, or I'm going to, like, end up with a terrible reputation for this sort of thing, okay?"
            "She looks around nervously, still looking all cute and adorable."

    elif the_report.get("girl orgasms", 0) > 2:
        if used_obedience:
            the_person "Oh my god, like, baby... I, like, loved what you did to me, okay? I never knew, like, being submissive could feel so good, okay?"
            mc.name "I, like, do enjoy when you keep begging me to make you cum again, okay? It's, like, almost like you're addicted to it, okay?"
            the_person "Shut up and, like, kiss me, [mc.name], okay?"
            "She looks up at you with big, dreamy eyes, still looking all cute and adorable."

        else:
            the_person "I, like, have never... cum that hard, okay? It was, like, just amazing, okay? I guess I, like, needed that, okay?"
            "She seems, like, dazed by her orgasm as she tries to form coherent sentences, still looking all cute and adorable."
            the_person "You, like, really know how to, like, give a girl a good time, okay? Just, like, gimme a second to catch my breath, okay?"
            mc.name "Take your time, I'm, like, not going anywhere, okay?"
            the_person "Thanks, [mc.name], okay? I think I, like, need a minute to recover before we can, like, start again, okay?"
            "She smiles and looks up at you with big, happy eyes, still looking all cute and adorable."

        call sex_review_trance(the_person) from _call_sex_review_trance_bimboed_sex_review

    #No special conditions, just respond based on how orgasmed and how slutty the position was.
    elif the_report.get("girl orgasms", 0) > 0 and the_report.get("guy orgasms", 0) > 0: #You both came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position cap, it was tame
            the_person "Ah, like, that was, like, so nice, okay? But I think we, like, could go even further next time, okay? I'm, like, not afraid to, like, push the limits, [mc.name], okay?"
            the_person "Doesn't that, like, sound like fun, okay? I'm, like, getting wet just thinking about it, okay?"
            "She smiles and looks up at you with big, mischievous eyes, still looking all cute and adorable."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "Ah, like, that was, like, just what I needed, okay? I think we're, like, very compatible, [mc.name], okay?"
            the_person "Let's, like, do it again some time soon, okay? I want to, like, see how much further we can go, okay?"
            "She smiles and looks up at you with big, happy eyes, still looking all cute and adorable."

        elif used_obedience: #She only did it because she was commanded
            the_person "Fuck, like, I... I didn't think I was going to, like, cum like that, okay? I guess I, like, just can't resist a good command, huh, okay?"
            mc.name "Aren't you, like, going to thank me, okay? You, like, obviously had a good time, okay?"
            the_person "Shut up and, like, don't get too full of yourself, [mc.name], okay?"
            "She looks up at you with big, playful eyes, still looking all cute and adorable."

        else: # She's surprised she even tried that.
            the_person "Oh my god, like, that was, like, so intense, okay? I didn't think I was going to, like, take it so far, but it, like, just felt right, okay?"
            the_person "Don't, like, think that's going to happen every time, though, okay? I'm, like, not a slut, okay? I just, like, like to, like, push my boundaries sometimes, okay?"
            "She smiles and looks up at you with big, happy eyes, still looking all cute and adorable."
        if the_person.love > 40:
            the_person "You, like, know, I never thought I'd, like, say this, but I think I, like, might actually, like, like this whole 'relationship' thing with you, [mc.name], okay?"
        else:
            the_person "Well, like, that was, like, fun, okay? Let's, like, do it again sometime, but not, like, too soon, okay? I, like, need to, like, recover my dignity first, okay?"
            "She smiles and looks up at you with big, playful eyes, still looking all cute and adorable."

    elif the_report.get("girl orgasms", 0) > 0: #Only she came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            the_person "Done already, okay? Well, like, that's just not right, okay? Next time I'm, like, going to make sure we both, like, cum and then some, okay?"
            the_person "I've, like, got a few ideas that are, like, going to blow you away, [mc.name], okay?"
            "She smiles mischievously, already imagining your next encounter, still looking all cute and adorable."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "You're, like, all done, okay? Well, like, that was, like, fucking hot, either way, [mc.name], okay?"
            the_person "I'll, like, repay the favour next time, alright, okay? I promise, okay? And maybe we can, like, try something new, okay?"
            "She leans in close, whispering in your ear, still looking all cute and adorable."

        elif used_obedience: #She only did it because she was commanded
            the_person "That's, like, it, okay? I mean, not like I, like, wanted to do anything more, I just thought you were, like, going to finish, okay?"
            mc.name "Some other time, okay? I just, like, wanted to see what you look like when you, like, cum, okay?"
            the_person "I... Fuck, well, I guess you, like, got what you wanted, okay? But don't, like, think I'm going to, like, make it easy for you next time, okay?"
            the_person "It, like, could have been worse, I guess, okay?"
            "She looks up at you with big, playful eyes, still looking all cute and adorable."

        else: # She's surprised she even tried that.
            the_person "Oh my god, like, that was, like, so intense, okay? You, like, really know how to, like, make a girl feel good, [mc.name], okay?"
            the_person "You're, like, probably tired after all that, like, work, okay? I promise I'll, like, repay the favour next time, okay? And maybe we can, like, try something different, okay?"
            "She smiles, already looking forward to your next encounter, still looking all cute and adorable."

    elif the_report.get("guy orgasms", 0) > 0: #Only you came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            the_person "Hmph, like, you're all tired out already, okay? That's, like, so frustrating, okay?"
            mc.name "Sorry, I'll, like, make it up to you next time, okay?"
            the_person "Well, like, I suppose I, like, could be persuaded to, like, try again, okay? But don't, like, expect any special treatment, okay?"
            mc.name "Yeah, I think I, like, could handle that, okay?"

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "You're, like, already done, okay? Such a, like, tease, okay? Fine, I'll, like, let you off this time, okay..."
            mc.name "Sorry, [the_person.title], maybe another time, okay?"
            the_person "You'd, like, better, or you won't be, like, hearing the word 'please' from me again, okay?"

        elif used_obedience: #She only did it because she was commanded
            the_person "I, like, suppose you're, like, worn out from all that, okay? We're, like, finished then, okay?"
            mc.name "Yeah, that's, like, all for now, okay?"
            the_person "Fine, but don't, like, think this means you get to, like, slack off next time, okay?"

        else:  # She's surprised she even tried that.
            the_person "Wow, like, that was, like... quite an experience, okay? I think I, like, got a little carried away there, okay?"
            the_person "Maybe it's, like, for the best that we, like, stop here, okay? I need to, like, think about what I just did, okay?"
            "She looks up at you with big, thoughtful eyes, still looking all cute and adorable."

    elif the_person.energy < 10: #Nobody came and she's tired
        the_person "Ugh, like, I'm so exhausted, okay? Another time, maybe, okay?"
        mc.name "No worries, we'll, like, do it another day, okay?"
        the_person "Just, like, don't expect any special treatment when we, like, try again, got it, okay?"

    else: #Nobody came.
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            the_person "Hmph, like, you're already done, okay? What's, like, the rush, okay? We, like, could've had more fun, okay?"
            "She crosses her arms, pretending to be upset, still looking all cute and adorable."
            the_person "You're, like, such a spoilsport, [the_person.mc_title], okay?"

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "We're, like, stopping, okay? But we were, like, just getting to the good stuff, okay?"
            mc.name "Sorry, [the_person.title], maybe another time, okay?"
            the_person "Yeah, maybe, okay? You, like, can't just leave a girl hanging like that, okay? You, like, have to, like, follow through, okay?"

        elif used_obedience: #She only did it because she was commanded
            the_person "Well, like, I wasn't, like, expecting that, okay? I thought you had, like, more in mind, okay?"
            mc.name "You, like, aren't disappointed, are you, okay?"
            the_person "No, no, okay? I just, like... wanted to, like, see where things would go, that's all, okay?"
            the_person "It's, like, fine, okay? I'll just, like, have to find someone else to, like, take me further, okay?"

        else:  # She's surprised she even tried that.
            the_person "Ugh, like, you're, like, probably right, okay? We should, like, stop now before we, like, get too carried away, okay?"
            the_person "I, like, don't want to, like, do something I'll, like, regret later, okay? Let's just, like, keep this casual, okay?"

    # Gave creampie while she is not on birth control (extra dialogue when she could get pregnant)
    if the_report.get("creampies", 0) > 0 and not the_person.on_birth_control and not the_person.knows_pregnant:
        the_person "Well, like, I guess we just, like, made things a little more interesting, didn't we, okay?"
        the_person "If I, like, get pregnant, it'll, like, serve you right for being, like, so reckless, okay?"

    $ del comment_position
    return
## Role Specific Section ##

label bimboed_improved_serum_unlock(the_person):
    mc.name "[the_person.title], like, now that you've had some time to get used to the lab, there's something I want to, like, talk to you about."
    the_person "Oh my god, like, yeah, what's on your mind, okay?"
    mc.name "Our R&D up to this point has, like, been based on my old notes from university."
    mc.name "There were some, like, unofficial experiment results that suggested the effects might be, like, enhanced by sexual arousal."
    "[the_person.title] raises an eyebrow, looking all curious and stuff."
    the_person "Ah, like, so you noticed that too? I have a hypothesis that an orgasm, like, opens chemical receptors that are normally blocked."
    mc.name "What if that's, like, true? Does that, like, open up any more paths for our research."
    the_person "If it's, like, true, I could leverage the effect to, like, induce greater effects in our subjects, okay?"
    "[the_person.possessive_title!c] grins mischievously, looking all playful and stuff."
    the_person "We'll, like, need to do some experiments to be sure, okay?"
    mc.name "What kind of experiments?"
    the_person "I want to, like, take a dose of serum myself, and you can, like, record the effects, okay?"
    the_person "Then I'll...ahem...stimulate myself, and we can, like, compare the effects after, okay?"
    mc.name "Do you, like, really think that's a good idea?"
    the_person "Not, like, really, but we can't, like, trust anyone else with this information if we're, like, right, okay?"
    the_person "We might be able to, like, make progress by brute force, but this is, like, a chance to take our research to the next level, okay?"
    the_person "A finished dose of serum that, like, raises my Suggestibility, okay? The higher it gets, the better, okay?"
    the_person "Then we'll just, like, need some time and some privacy for me to, like, see what sort of effects my...ahem...stimulation will have, okay?"
    "She looks up at you with big, excited eyes, still looking all cute and adorable."
    return

## Taboo break dialogue ##

label bimboed_kissing_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 30:
        the_person "Oh my god, like, fine, let's just get this over with, okay? You've, like, always been curious, right?"
        mc.name "That's, like, not true, but I'll play along, okay?"
        the_person "Hmph, like, whatever... Just, like, shut up and kiss me already, okay?"
        mc.name "Oh, I'm, like, not going to shut up that easily, okay?"
        the_person "Suit yourself, okay? I'll, like, just have to find someone else who's, like, willing to kiss me, okay?"
        mc.name "Hold on, wait a minute, okay? I'm, like, not going anywhere, okay?"
        the_person "Oh? You're, like, not going anywhere? Then, like, get over here and kiss me already, okay!"
        mc.name "Alright, alright, okay? Here I come, okay?"
        "She looks up at you with big, flirtatious eyes, still looking all cute and adorable."
    elif the_person.love >= 20:
        the_person "So, like, we're doing this, huh? About time, if you ask me, okay?"
        mc.name "I, like, guess we are, okay? What do you think, okay?"
        the_person "It's, like, about time we finally made out, [the_person.mc_title], okay?"
        mc.name "I'm, like, glad you feel that way, okay?"
        the_person "Me too, okay? Just, like, be gentle, okay?"
        mc.name "I will, okay?"
        "She smiles and looks up at you with big, happy eyes, still looking all cute and adorable."
    else:
        the_person "I, like, don't know if this is a good idea, [the_person.mc_title], okay? We're, like, taking things too fast, aren't we, okay?"
        mc.name "Are you, like, scared, okay?"
        the_person "No! I'm, like, just...not sure if this is a good idea, okay? But I, like, trust you, okay?"
        mc.name "Good, okay? Because I'm, like, not going to let you back out now, okay?"
        the_person "Hmph, like, fine, okay? But if this is a mistake, it's, like, on you, okay?"
        mc.name "It'll, like, be worth it, I promise, okay?"
        "She looks up at you with big, nervous eyes, still looking all cute and adorable."
    return

label bimboed_touching_body_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 30:
        the_person "Oh my god, like, come on then, don't be shy, okay? You've, like, wanted to touch me for ages, haven't you, okay?"
        mc.name "Hey, I'm, like, not that obvious, okay!"
        the_person "Oh, please, okay? I can, like, see the way you look at me, okay?"
        mc.name "Well, I, like, can't help it if you're, like, irresistible, okay?"
        the_person "Irresistible? Pfft, you're, like, just trying to get in my pants, okay?"
        "She rolls her eyes and smiles, still looking all cute and adorable."
    elif the_person.love >= 20:
        the_person "So, like, you're ready for this, okay?"
        "You nod, and she looks up at you with big, nervous eyes."
        the_person "Me too, I think, okay? I didn't, like, think I'd be so nervous when you actually made a move, okay?"
        mc.name "Just, like, relax, okay? You trust me, right, okay?"
        the_person "Of course, okay? Just don't, like, expect me to be all touchy-feely about it, okay?"
        "She smiles and looks up at you with big, happy eyes, still looking all cute and adorable."
    else:
        the_person "I, like, think you're getting a little ahead of yourself here, [the_person.mc_title], okay?"
        mc.name "What do you mean, okay?"
        the_person "I mean, like, I don't just let anyone, like, feel me up, okay? Maybe we should, like, cool things down, okay?"
        mc.name "You're, like, not scared, are you, okay?"
        the_person "Scared? Of course not, okay! I'm, like, just... cautious, okay?"
        mc.name "Well then, like, just relax and go with it, okay? It doesn't, like, have to mean anything unless we want it to, okay?"
        "You see her answer in her eyes before she says anything, still looking all cute and adorable."
        the_person "You're, like, so bad for me, you know that, okay?"
        mc.name "Well, like, let me make up for it then, okay?"
        the_person "Hmm, maybe I'll, like, let you, okay?"
        "She smiles and looks up at you with big, flirtatious eyes, still looking all cute and adorable."
    return

label bimboed_touching_penis_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 35:
        the_person "Oh my god, like, you're really enjoying this, aren't you, okay? Look how, like, hard you are, okay?"
        mc.name "Do you, like, want to feel it, okay? You can if you want, okay?"
        the_person "Yeah, why not, okay? I'll, like, try not to hurt it, okay?"
        "She smiles and looks up at you with big, playful eyes, still looking all cute and adorable."

    elif the_person.love >= 20:
        the_person "Your, like, cock looks so nice when it's, like, hard, okay? Can I, like, touch it, okay?"
        mc.name "Go ahead, it doesn't, like, bite, okay?"
        the_person "Well, it might if you're, like, not careful, okay?"
        "She giggles and looks up at you with big, happy eyes, still looking all cute and adorable."

    else:
        mc.name "My, like, cock is so hard right now, [the_person.title], okay? Put your hand on it and, like, touch it for me, okay?"
        the_person "What? That's, like, taking things a little far, don't you think, okay?"
        mc.name "Come on, you know you, like, want to, okay? Just a few strokes, then if you aren't, like, impressed you can stop, okay?"
        the_person "Fine, but don't, like, expect me to make any promises after this, okay?"
        mc.name "I wouldn't, like, dream of it, okay?"
        the_person "Hmm, okay then, okay? I'll, like, give it a try, okay?"
        "She reaches out and wraps her hand around your cock, her touch gentle but firm, still looking all cute and adorable."
        "You feel a surge of pleasure as she starts to stroke you, and she looks up at you with big, happy eyes."
        the_person "Mmm, you're, like, really nice when you're, like, hard, okay?"
    return

label bimboed_touching_vagina_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 35:
        the_person "Oh my god, like, come on, don't be shy, okay? You've, like, been dying to touch my pussy, admit it, okay?"
        "She looks up at you with big, flirtatious eyes, still looking all cute and adorable."

    elif the_person.love >= 20:
        the_person "Oh my god, like, oh fuck, you've got my pussy, like, tingling, okay? I want you to, like, touch it, [the_person.mc_title], okay?"
        mc.name "You, like, sure, okay? I don't want to, like, push you too far, okay?"
        the_person "No, like, I want it, okay? I want you to, like, touch me, okay?"
        "She smiles and looks up at you with big, happy eyes, still looking all cute and adorable."

    else:
        the_person "I, like, don't know if we should be doing this, [the_person.mc_title], okay..."
        mc.name "Just, like, take a deep breath and relax, okay? I'm, like, just going to touch you a little, and if you don't, like, like it I'll stop, okay?"
        the_person "Just, like, a little, okay?"
        mc.name "Just, like, a little, okay? Trust me, it's, like, going to feel amazing, okay?"
        the_person "Hmm, okay, okay... But don't, like, think this means I'm, like, easy, okay?"
        mc.name "I wouldn't, like, dream of it, okay?"
        "She looks up at you with big, nervous eyes, still looking all cute and adorable."
    return

label bimboed_sucking_cock_taboo_break(the_person):
    mc.name "I, like, want you to do something for me, okay?"
    the_person "Oh yeah? What do you, like, want me to do to you, okay?"
    mc.name "I, like, want you to suck on my cock, okay?"
    if the_person.effective_sluttiness() >= 45:
        the_person "Mmm, like, I think I'm up for that, okay? It's, like, not going to be too big for me, is it, okay?"
        mc.name "I, like, think you'll be able to handle it, okay?"
        the_person "Alright, I don't, like, want it choking me, okay?"
        "She bites her lip and winks at you, looking all playful and stuff."
        the_person "That's, like, a lie, okay? A little choking is, like, okay, okay?"
        "She giggles and looks up at you with big, flirtatious eyes, still looking all cute and adorable."

    elif the_person.love >= 30:
        the_person "I, like, guess we've been dancing around it for a while, okay?"
        "She bites her lip and looks your body up and down, looking all curious and stuff."
        the_person "Alright, let's, like, do this, okay?"
        "She smiles and looks up at you with big, happy eyes, still looking all cute and adorable."

    else:
        the_person "Oh, like, I was wondering if this was going to, like, come up, okay..."
        "She laughs nervously and looks away from you, looking all shy and stuff."
        the_person "I, like, don't know, [the_person.mc_title], okay..."
        "You reach up and hold her chin, turning her head back to face you, and she looks up at you with big, nervous eyes."
        mc.name "Don't, like, overthink it, okay? Just, like, kneel down and suck on it for me, okay? If you don't, like, like doing it, we can, like, just forget it happened, okay?"
        "You can see in her eyes the moment her resolve breaks, and she bites her lip and nods, still looking all cute and adorable."
        the_person "Alright, let's, like, do this, okay?"
        "She slowly gets down on her knees, her eyes darting between your face and your cock with a mix of, like, reluctance and curiosity, okay?"
        the_person "You know, I, like, never thought I'd be doing this, okay? But I guess I'm, like, willing to try new things for you, okay?"
        "She takes a deep breath, her hand wrapping around the base of your cock as she leans in to take it in her mouth, looking all nervous and stuff."
        "As she starts to suck, her eyes flash up to meet yours, a hint of, like, defiance and challenge in them, okay?"
        the_person "Satisfied now, okay?"
    return

label bimboed_licking_pussy_taboo_break(the_person):
    mc.name "I, like, want to taste your pussy, [the_person.title], okay? Are you, like, ready?"
    if the_person.effective_sluttiness() >= 45:
        the_person "Hmph, like, I don't need your permission or anything, but fine, okay? I'm, like, ready."
        mc.name "Good, okay? But don't, like, expect me to go easy on you just because it's, like, your first time, okay?"
        the_person "Oh, please, okay? I've, like, had better, okay?"
        "She rolls her eyes and smirks at you, looking all playful and stuff."

    elif the_person.love >= 30:
        the_person "Finally, like, a man who knows how to treat a woman right, okay? I'm, like, ready when you are, okay?"
        mc.name "That's, like, what I like to hear, okay?"
        "She smiles and looks up at you with big, happy eyes, still looking all cute and adorable."

    else:
        if the_person.has_taboo("sucking_cock"):
            the_person "You know, like, I never thought I'd see the day where you'd be, like, willing to do this, okay?"
            "She bites her lip and smirks at you, looking all flirtatious and stuff."
            the_person "But, like, I guess I'm not going to, like, complain, okay? Just don't, like, expect me to be all grateful or anything, okay?"
        else:
            the_person "About time you, like, decided to make up for not sucking my cock, okay?"
            "She rolls her eyes and smiles, looking all playful and stuff."
            the_person "But, like, fine, I'm ready, okay? Just don't, like, expect me to be all appreciative or anything, okay?"
    "She lies back, her eyes darting between yours and the area you're, like, about to explore, okay?"
    the_person "And, like, don't think this means I'm, like, some kind of slut for letting you do this, okay?"
    mc.name "I, like, wouldn't dream of it, okay? You're, like, just being a good sport, right, okay?"
    the_person "Something, like, that..."
    "She closes her eyes, her face, like, flushed with embarrassment as you start to lick her, okay?"
    "She looks so cute and adorable, even when she's, like, trying to be all tough and stuff, okay?"
    return

label bimboed_vaginal_sex_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 60:
        the_person "Oh my god, like, finally! I've, like, been waiting for this moment all night, okay? Come on then, get that cock inside me and, like, fuck me like you mean it, okay?"
        "She looks up at you with big, eager eyes, still looking all cute and adorable."

    elif the_person.love >= 45:
        the_person "Alright, like, show me what you've got, okay? I'm, like, ready for this, okay?"
        mc.name "You, like, better be, okay? I'm, like, going to make sure you remember this, okay?"
        the_person "Bring it on, okay! I can, like, take it, okay?"
        "She smiles and looks up at you with big, confident eyes, still looking all cute and adorable."

    else:
        if the_person.has_taboo("anal_sex"):
            the_person "Well, well, well, okay? Look at that cock, okay? I guess we're, like, going to find out just how tight my pussy is, okay?"
            mc.name "That's, like, the plan, okay? And if you're, like, a good girl, I might just make it, like, worth your while, okay?"
            the_person "Hmph, like, I'm always good, okay? Now, like, get to it before I, like, change my mind, okay?"
            "She looks up at you with big, playful eyes, still looking all cute and adorable."

        else:
            the_person "Oh, like, so that's what you're, like, going to do with that big cock of yours, okay? Well, I guess we'll, like, see how it feels, okay?"
            mc.name "We, like, sure will, okay? And if you're, like, lucky, I might just make it, like, feel even better, okay?"
            the_person "Ugh, like, just get on with it already, okay! I'm, like, not getting any younger, okay?"
            "She rolls her eyes and looks up at you with big, impatient eyes, still looking all cute and adorable."
    return

label bimboed_anal_sex_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 75:
        the_person "Oh my god, like, fine, okay? But only because I, like, can't resist you, okay? Your cock is, like, so big, I'm surprised it fits in your pants, okay?"
        "She seems, like, more excited by the prospect than intimidated, and she looks up at you with big, eager eyes, still looking all cute and adorable."
        mc.name "Don't, like, worry, I'll take it slow and make sure you're, like, comfortable, okay?"
        "She nods and smiles, still looking all cute and adorable."

    elif the_person.love >= 60:
        the_person "Are you, like, sure you want to do this, okay? I'm, like, not exactly the most experienced person when it comes to anal, okay..."
        mc.name "I'll, like, be gentle, don't worry, okay?"
        the_person "Alright, but if it, like, hurts too much, I'm, like, stopping, okay?"
        "She looks up at you with big, nervous eyes, still looking all cute and adorable."

    else:
        if the_person.has_taboo("vaginal_sex"):
            the_person "Wait, are you, like, sure you want to do this, okay? My ass might be, like, too tight for your cock, okay!"
            mc.name "I'll, like, make it fit, but you might, like, feel a little sore afterward, okay?"
            the_person "Oh, great, okay? Just what I needed, okay?"
            "She rolls her eyes and looks up at you with big, playful eyes, still looking all cute and adorable."

        else:
            the_person "Come on, [mc.name], like, let's just get this over with, okay? I don't, like, know what's gotten into me today, okay?"
            mc.name "Are you, like, sure you're okay with this, okay?"
            the_person "Of course, I'm, like, just... nervous, okay? And a little, like, embarrassed, okay? But let's, like, just do this already, okay!"
            "She blushes and looks away, still looking all cute and adorable."
            mc.name "Alright, let's, like, get started then, okay?"
            the_person "Hurry up, I'm, like, ready when you are, okay?"
            "She looks up at you with big, impatient eyes, still looking all cute and adorable."
    return

label bimboed_condomless_sex_taboo_break(the_person):
    if the_person.knows_pregnant:
        the_person "Oh my god, like, you really want to do it without a condom, okay? Fine, but don't, like, say I didn't warn you, okay?"
        if the_person.wants_creampie:
            the_person "If you're, like, going to cum inside me, please make it, like, worth my while, okay?"
        else:
            the_person "Just, like, make sure to cover me with your... you know, stuff, okay?"
    elif the_person.opinion.bareback_sex > 0:
        the_person "Whatever, like, you want to do it bareback, huh, okay? Just don't, like, say I didn't warn you, okay?"
        if the_person.on_birth_control:
            the_person "I'm, like, on the pill, so you don't have to, like, worry about it, okay?"
            $ the_person.update_birth_control_knowledge()
        elif the_person.wants_creampie:
            the_person "But if you're, like, going to cum inside me, you'd better make it, like, worth my while, okay?"
        elif the_person.opinion.creampies < 0:
            the_person "Just, like, don't get me pregnant, okay? That would be, like, a huge pain, okay?"
        else:
            the_person "Alright, like, just make sure you pull out this time, okay?"
    elif the_person.love > 60:
        if the_person.on_birth_control:
            the_person "Ugh, like, fine, I'm on the pill, okay? Don't, like, say I didn't warn you, okay?"
            $ the_person.update_birth_control_knowledge()
        elif the_person.wants_creampie:
            the_person "You're, like, always trying to make me do stupid things, aren't you, okay? Fine, if we're, like, going to do this, make it, like, worth my while, okay?"
            mc.name "Are you, like, on the pill, okay?"
            "She rolls her eyes, looking all playful and stuff."
            the_person "No, like, I'm not, okay? But if you're, like, going to cum inside me, you'd better make it, like, worth it, okay?"
            $ the_person.update_birth_control_knowledge()
        elif the_person.opinion.creampies < 0:
            the_person "You're, like, always trying to make me do stupid things, aren't you, okay? Fine, just don't, like, get me pregnant, okay?"
            the_person "I'm, like, not ready for that kind of responsibility again, okay?"
        else:
            the_person "You're, like, always trying to make me do stupid things, aren't you, okay? Fine, just make sure you pull out this time, okay?"
            if the_person.kids == 0:
                the_person "I, like, need you to pull out though, okay? I'm, like, not quite ready to be a mother, even with you, okay?"
            elif the_person.kids == 1:
                the_person "I, like, need you to pull out though, okay? I've, like, already got a kid, I don't need another one, okay?"
            else:
                the_person "I, like, need you to pull out though, okay? I've, like, already got kids, I don't need another one, okay?"
    else:
        if the_person.on_birth_control:
            the_person "Hmph, like, you want to get busy without a rubber, okay? Well, I'm, like, on the pill, so I guess it's, like, fine, okay? Just don't, like, expect any special treatment, okay?"
            $ the_person.update_birth_control_knowledge()
        elif the_person.has_taboo("vaginal_sex"):
            the_person "You're, like, really not going to use a condom, okay? I'm, like, not on the pill, so we could, like, end up with a little surprise, okay?"
            $ the_person.update_birth_control_knowledge()
            the_person "Or is this, like, your sneaky plan to make a baby out of me, okay?"
            mc.name "I, like, swear I'll pull out, okay? I want our, like, first time to be memorable, okay?"
            "She crosses her arms and gives a half-hearted sigh, looking all cute and adorable."
            the_person "Ugh, like, fine, okay? But you better, like, pull out, or you'll, like, regret it, okay?"
        else:
            the_person "You're, like, really not going to use a condom, okay? I'm, like, not on the pill, so we could, like, end up with a little surprise, okay?"
            $ the_person.update_birth_control_knowledge()
            the_person "Or is this, like, your sneaky plan to make a baby out of me, okay?"
            mc.name "I, like, promise I'll pull out, okay? It'll, like, feel so much better without anything between us, okay?"
            the_person "God, like, I know, okay? I'm, like, trying to be rational here, not some, like, lust-driven animal, okay?"
            "She huffs and puffs, looking all playful and stuff."
            the_person "Fine, like, no condom, okay? Just remember to, like, pull out, got it, okay? Good."
    return

label bimboed_underwear_nudity_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > 30 - (the_person.opinion.skimpy_outfits * 5):
        the_person "Oh my god, like, you want to see me in my underwear, huh, okay? It's, like, about time you asked, okay?"
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "What are we, like, waiting for then, let's get this off of you, okay?"
            "She looks up at you with big, flirtatious eyes, still looking all cute and adorable."
        else:
            mc.name "Yeah, yeah, okay? We've, like, been over this, okay? You're, like, not exactly subtle about it, okay?"
            the_person "Shut up, okay! I just, like, don't want you to get the wrong idea, okay?"
            mc.name "Wrong idea, okay? Like how you're, like, not wearing anything under this skirt, okay?"
            the_person "Ugh, fine, okay. But don't, like, say I didn't warn you, okay?"
            "She rolls her eyes and smiles, still looking all cute and adorable."

    elif the_person.love > 15:
        the_person "You, like, want me to strip me down a little, okay? It's, like, about time, I was wondering why you were, like, taking things so slow, okay?"
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "Oh, don't, like, give me that, okay? You know you, like, want to show off, okay?"
            the_person "Fine, okay, but if this, like, gets out of hand, I'm, like, blaming you, okay?"
            mc.name "Promise, okay?"
            the_person "Yeah, yeah, okay. Now, like, get this [the_clothing.display_name] off, okay?"
            "She looks up at you with big, playful eyes, still looking all cute and adorable."

        else:
            mc.name "Yeah, I know, okay? You've, like, been teasing me for weeks, okay?"
            the_person "Teasing, okay? I'm, like, just being friendly, okay?"
            mc.name "Right, okay. Now, like, let's get you out of these clothes, okay?"
            the_person "Ugh, fine, okay. But don't, like, think this means I'm, like, going easy on you, okay?"
            "She slowly starts taking [the_clothing.display_name] off, still looking all cute and adorable."

    else:
        the_person "You, like, really want to see me like this, okay? Fine, but don't, like, say I didn't warn you, okay?"
        the_person "If you, like, take my [the_clothing.display_name] I'll, like, only have my underwear on, you know that, okay?"
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "Yeah, that's, like, kind of the point, okay?"
            "She shakes her head and laughs to herself, still looking all cute and adorable."
            the_person "Whatever, okay, but if you, like, think I'm doing this because I want to..."
        else:
            mc.name "Yeah, I know, okay? You're, like, not exactly shy, okay?"
            the_person "Hey, I'm, like, just being cautious, okay? You can't, like, blame a girl for being careful, okay?"
            mc.name "Of course not, okay. Now, like, let's get you out of these clothes, okay?"
            the_person "Fine, okay, but don't, like, think this means I'm, like, going easy on you, okay?"
    return

label bimboed_bare_tits_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > (40 - the_person.opinion.showing_her_tits * 5):
        the_person "Oh my god, like, why do you want to see my tits now, all of a sudden, okay? Like I don't already know you're, like, checking me out, okay?"
        if the_person.has_large_tits:
            "She reluctantly shakes her chest for you, jiggling the [the_person.tits_description] hidden underneath her [the_clothing.display_name], and looks up at you with big, flirtatious eyes."
        else:
            "She reluctantly shakes her chest and gives her [the_person.tits_description] a little jiggle, looking all cute and adorable."
        the_person "You're, like, always so eager, aren't you, okay? I guess I can, like, show you, but don't, like, get too excited, okay?"
        if the_person.has_large_tits:
            mc.name "Oh, I've, like, been looking, okay? Now let's, like, get those puppies out where I can, like, enjoy them, okay?"
        else:
            mc.name "Oh, I've, like, been looking, okay? Now let's, like, get those cute little things out, okay?"

    elif the_person.love > 25:
        the_person "Are you, like, really sure you want to see my tits, [the_person.mc_title], okay?"
        if the_person.has_large_tits:
            "She rolls her eyes and shakes her chest, jiggling her nice [the_person.tits_description], barely restrained by her [the_clothing.display_name], and looks up at you with big, playful eyes."
        else:
            "She rolls her eyes and shakes her chest, giving her [the_person.tits_description] a little jiggle, and looks up at you with big, happy eyes."
        mc.name "Of course I am, okay? You know I, like, love your tits, okay?"
        the_person "Well, I suppose you're, like, entitled to see them then... but don't, like, think this means I'm going to, like, start showing them off to everyone, okay?"

    else:
        the_person "Wait, no, okay! Don't, like, look at me like that, okay! You should, like, at least ask a girl before you try and, like, put her tits on full display, okay?"
        mc.name "Come on, don't, like, be like that, okay? I bet your tits look, like, great, okay?"
        the_person "They, like, do, but I still feel a little, like, self-conscious about being, like, naked around you, alright, okay?"
        mc.name "There's, like, no need to be, okay? Just, like, relax and let me take your [the_clothing.display_name] off for you, okay?"
        the_person "Ugh, fine, okay... but don't, like, think this means I'm going to, like, start showing off my body to everyone, okay?"
    return

label bimboed_bare_pussy_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > (50 - the_person.opinion.showing_her_ass * 5):
        the_person "Oh my god, like, so you want to see my pussy, huh, okay? Like I don't already know you're, like, thinking about it, okay?"
        if the_person.has_taboo("touching_vagina"):
            "She reluctantly lifts her hips, allowing you to slowly remove her [the_clothing.display_name] and reveal her pussy, and looks up at you with big, flirtatious eyes."
        else:
            "She lifts her hips, giving you a quick glimpse of her pussy before covering it back up, and looks up at you with big, playful eyes."
        the_person "Well, like, you got your wish, okay? Don't, like, say I didn't warn you, okay?"

    elif the_person.love > 35:
        the_person "You, like, want to see my pussy, really, okay? Are you, like, sure you're ready for that, okay?"
        if the_person.has_taboo("touching_vagina"):
            mc.name "I, like, think I am, okay? I've, like, been wanting to see it for a while, okay?"
            the_person "Hmm, well... I, like, suppose you've earned it, okay? Just, like, remember, you asked for this, okay?"
        else:
            mc.name "I've, like, already felt it up, I thought I should, like, see it too, okay?"
            the_person "You, like, really are persistent, aren't you, okay? Fine, go on then, okay."

    else:
        the_person "Hold on, okay? You're, like, not getting me out of my [the_clothing.display_name] that easily, okay!"
        if the_person.has_taboo("touching_vagina"):
            mc.name "Come on, just, like, let me see it, okay? I, like, promise I'll be gentle, okay?"
            the_person "You're, like, such a liar... But, like, fine, go ahead, okay?"
        else:
            mc.name "I've, like, already felt your pussy up, I want to, like, get a look at it now, okay?"
            the_person "You're, like, so pushy, okay! Alright, but don't, like, say I didn't warn you, okay?"
    return

# label bimboed_facial_cum_taboo_break(the_person):

#     return

# label bimboed_mouth_cum_taboo_break(the_person):

#     return

# label bimboed_body_cum_taboo_break(the_person):

#     return
#==================================================================

label bimboed_creampie_taboo_break(the_person):
    if the_person.wants_creampie:
        if the_person.knows_pregnant:
            the_person "Oh my god, like, you want to get me pregnant, huh, okay? Fine, I suppose it's, like, about time someone knocked me up, okay?"
            "She sighs happily, seeming almost resigned to the idea, and looks up at you with big, dreamy eyes."

        elif the_person.on_birth_control:
            if the_person.has_significant_other:
                the_person "Oh my god, like, I'm such a horrible [the_person.so_girl_title], okay? But I, like, needed this so badly, okay?"
                the_person "Maybe if we're, like, lucky, my [the_person.SO_name] won't find out, okay?"
                "She looks at you with a mischievous grin, still looking all cute and adorable."
            else:
                the_person "Oh my god, like, I needed this so badly, okay! Ah... I guess I'll, like, just have to deal with the consequences, okay?"

        elif the_person.effective_sluttiness() > 75 or the_person.opinion.creampies > 0:
            if the_person.has_significant_other:
                the_person "You, like, want to get me pregnant, okay? Fine, I suppose it's, like, about time someone knocked me up, okay?"
                the_person "Maybe my [the_person.SO_name] will, like, finally notice how unhappy I am and do something about it, okay?"

            else:
                the_person "You, like, want to get me pregnant, okay? Fine, I suppose it's, like, about time someone knocked me up, okay?"
                the_person "I guess I'll, like, just have to deal with the consequences, okay?"

            "She sighs happily, but with a hint of annoyance, and looks up at you with big, playful eyes."
            the_person "How long until you're, like, ready for round two, okay? I want, like, as much of your cum inside my pussy as possible, okay?"
            the_person "Just don't, like, expect me to be all happy and grateful about it, okay?"

        else:
            if the_person.has_significant_other:
                the_person "Oh fuck... like, I'm such a terrible [the_person.so_girl_title], okay!"
                "She sighs happily, but with a hint of guilt, and looks up at you with big, nervous eyes."
                the_person "But, like, that felt so good, okay..."
            else:
                the_person "Oh fuck, like, that was so risky, okay."
                "She sighs happily, but with a hint of annoyance, and looks up at you with big, playful eyes."
                the_person "But, like, it felt so good, okay..."
            the_person "I'll, like, just have to hope you haven't, like, knocked me up, okay? We, like, really shouldn't do this again, my luck is, like, going to run out at some point, okay?"
            the_person "Besides, I'm, like, not exactly thrilled about the idea of being, like, tied down to a man right now, okay?"

    else:
        if the_person.knows_pregnant:
            the_person "Ugh, like, you're kidding me, right, okay? You got me pregnant, okay?"

        elif not the_person.on_birth_control:
            the_person "Seriously, like, you didn't even use protection, okay? What if I, like, get pregnant, okay?"

            if the_person.has_significant_other:
                the_person "What if you, like, just got me pregnant, okay? I would be, like, the worst [the_person.so_girl_title] of all time, okay!"

            else:
                the_person "What if I, like, get pregnant, okay? I'm, like, not ready for that kind of responsibility, okay!"
            the_person "You'd, like, better start buying me chocolate and flowers to make up for this, okay?"
            the_person "Next time, we're, like, using condoms, or we're, like, not doing it at all, okay? You got it, okay?"

        elif the_person.has_significant_other:
            the_person "Did you, like, really just creampie me after I told you to pull out, okay?"
            "She sighs unhappily and looks up at you with big, disappointed eyes."
            the_person "God, like, I'm such a terrible [the_person.so_girl_title], okay. Maybe next time I'll, like, make you wear a condom as punishment, okay."

        elif the_person.opinion.creampies < 0:
            the_person "Ugh, like, this is so unpleasant, okay. Couldn't you, like, have at least made it worth my while, okay?"
            "She rolls her eyes and looks up at you with big, annoyed eyes."
            the_person "Next time, at least, like, have the decency to ask if I'm, like, in the mood for a creampie, okay? Or better yet, don't even bother if you're, like, just going to be careless like this, okay."
            the_person "Next time, ask me first if I, like, want a baby, okay?"
        else:
            the_person "Are you, like, serious right now, okay? You're, like, really going to give me that attitude after you just...you know, okay?"
            "She huffs and crosses her arms, still looking all cute and adorable."
            the_person "I swear, you're, like, going to be the death of me, okay? Fine, next time, at least, like, have the decency to clean up after yourself, okay?"
    return

label bimboed_anal_creampie_taboo_break(the_person):
    if the_person.opinion.anal_creampies > 0:
        if the_person.effective_sluttiness() > 75 or the_person.opinion.anal_creampies > 1:
            if the_person.has_significant_other:
                the_person "Oh my god, like, ugh, fine, okay? I won't, like, tell my [the_person.so_title] about this, okay? But don't, like, think I'm enjoying this, okay..."
                "She says this while wincing in pleasure as you fill her ass with your cream, and looks up at you with big, guilty eyes."
                the_person "Ugh, it's just... like, weirdly satisfying, I guess, okay..."
            else:
                the_person "Oh my god, like, ugh, finally, okay! You're, like, actually doing this, okay? I've, like, been waiting for this forever, okay..."
                the_person "Okay, okay, I know it's, like, wrong, but... it feels, like, so good, okay..."
            "She bites her lip, trying to contain her excitement, and looks up at you with big, happy eyes."
            the_person "I guess it's, like, nice... having your cum in my ass, okay..."
        else:
            if the_person.has_significant_other:
                the_person "Oh my god, like, ugh, what are you doing, okay? My [the_person.so_title] is, like, going to kill me if he finds out about this, okay..."
                "She moans softly as you continue to fill her ass, and looks up at you with big, nervous eyes."
                the_person "Ugh, I, like, can't believe I'm letting you do this... It's, like, just so taboo, okay..."
            else:
                the_person "Oh my god, like, ugh, promise you'll, like, do this again, okay? I, like, can't believe I'm saying this, but... it's, like, kind of hot, okay..."
                the_person "All that cum in my, like, tight little ass, okay..."
    else:
        if the_person.has_significant_other:
            the_person "Oh my god, like, ugh, seriously, okay? You couldn't, like, pull out, okay? My [the_person.so_title] is, like, going to kill me, okay..."
            "She starts to squirm and try to get away from you, and looks up at you with big, angry eyes."
            the_person "Next time, just, like, shoot your load on my ass, okay?"
        elif the_person.opinion.anal_creampies < -1:
            the_person "Oh my god, like, ugh, seriously, okay? You can't, like, even follow simple instructions, okay? My ass is, like, not a creampie dispenser, okay!"
        else:
            the_person "Oh my god, like, ugh, not inside, okay! My ass is, like, not a dirty little secret, although that sounds, like, kind of hot, okay..."
    return

label bimboed_dual_penetration_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 75:
        the_person "Oh my god, like, ugh, why do you always have to push me to do this, okay? Fine, but don't, like, expect me to enjoy it, okay..."
        "She rolls her eyes and crosses her arms, clearly annoyed but still willing to go through with it, and looks up at you with big, playful eyes."
        mc.name "Don't, like, worry, it'll be worth it, okay?"
        the_person "I, like, doubt that, but whatever, okay?"

    elif the_person.love >= 60:
        the_person "You're, like, really sure about this, okay? It's, like, going to be a tight fit, okay..."
        mc.name "I'll, like, make sure it fits perfectly, okay?"
        the_person "Ugh, just, like, be careful not to hurt me, okay? I don't, like, want any scars, okay..."
        "She looks up at you with big, nervous eyes, still looking all cute and adorable."

    else:
        if the_person.has_taboo("vaginal_sex"):
            the_person "Are you, like, sure my pussy wouldn't be tight enough for you, okay? I mean, I've, like, never done this before, okay..."
            mc.name "It's, like, okay, I'll make it fit, okay? Just, like, try to relax, okay?"
            the_person "Ugh, this is, like, so embarrassing, okay..."
            "She looks down, blushing, and still looking all cute and adorable."

        else:
            the_person "Ugh, fine, okay. I guess we're, like, doing this, right, okay? I mean, I, like, can't back out now, okay..."
            mc.name "Are you, like, sure you're ready for this, okay?"
            the_person "Yeah, whatever, okay. Let's, like, just get this over with, okay..."
            "She looks up at you with big, impatient eyes, still looking all cute and adorable."
    return

label bimboed_sleepover_yourplace_response(the_person): #Invited her over to spend the night
    if the_person.love >= 70:
        the_person "Oh my god, like, ugh, fine, okay? I'll, like, come over, okay? But don't, like, expect me to be all lovey-dovey or anything, okay..."
        mc.name "I, like, wouldn't dream of it, okay? We'll, like, just have a good time, okay?"
        the_person "Yeah, yeah, okay... Just don't, like, get too close, okay? I don't, like, like cuddling or anything, okay..."
        "She looks up at you with big, playful eyes, still looking all cute and adorable."

    elif the_person.sluttiness >= 80:
        the_person "Oh my god, like, I'm so excited, okay! I, like, can't wait to get my hands on you, okay? Make sure you, like, have everything ready, so we can, like, have a great night, okay?"
        "She bounces up and down, looking all excited and stuff."

    else:
        the_person "I, like, guess I could come over, okay... But don't, like, expect me to do anything I'm, like, not comfortable with, okay?"
        "She looks up at you with big, nervous eyes, still looking all cute and adorable."
    return

label bimboed_sleepover_herplace_response(the_person): #Spending the night at her place
    if the_person.love >= 70:
        the_person "Oh my god, like, ugh, fine, okay? Come over and, like, stay the night, but don't, like, expect me to be all lovey-dovey or anything, okay..."
        mc.name "I, like, wouldn't dream of it, okay? We'll, like, just have a good time, okay?"
        the_person "Yeah, yeah, okay... Just don't, like, get too close, okay? I don't, like, like cuddling or anything, okay..."
        "She looks up at you with big, playful eyes, still looking all cute and adorable."

    elif the_person.sluttiness >= 80:
        the_person "Oh my god, like, I'm so excited, okay! I, like, can't wait to get you all to myself, okay? Make sure you're, like, ready for a wild night, okay?"
        "She bounces up and down, looking all excited and stuff."

    else:
        the_person "I, like, guess you can come over, okay... But don't, like, expect me to do anything I'm, like, not comfortable with, okay?"
        "She looks up at you with big, nervous eyes, still looking all cute and adorable."
    return

label bimboed_sleepover_yourplace_sex_start(the_person):
    "[the_person.title] rolls her eyes and, like, walks over to you, her expression a mix of, like, annoyance and desire, okay?"
    the_person "Oh my god, like, ugh, fine, okay? Let's, like, get this over with, okay? Just don't, like, expect me to be all lovey-dovey or anything, okay..."
    "She looks up at you with big, flirtatious eyes, still looking all cute and adorable."
    return

label bimboed_sleepover_herplace_sex_start(the_person):
    the_person "Oh my god, like, ugh, finally, okay? Get over here already, okay?"
    "She smirks and crosses her arms, clearly annoyed but still, like, eager for the action to begin, okay?"
    mc.name "Are you, like, ready?"
    the_person "Hah! Like I, like, need to be ready for this, okay? Just, like, get in here and do your worst, okay."
    "She leans back on the couch, her legs spread wide in invitation, and looks up at you with big, flirtatious eyes."
    the_person "Hurry up, I'm, like, not getting any younger, okay!"
    return

label bimboed_sleepover_impressed_response(the_person):  #If you've made her cum a lot
    the_person "Oh my god, like, ugh, you're really good at that, okay... Don't, like, expect me to admit it, but you're, like, making me feel things, okay..."
    "She rolls her eyes and smirks, trying to, like, hide her true feelings, okay?"
    mc.name "You, like, want more?"
    the_person "Hmph, maybe, okay. But don't, like, think you've won me over or anything, okay. I can, like, still handle more, okay..."
    "[the_person.title] lies down in bed, her breathing still, like, ragged from the previous rounds, okay."
    the_person "I might, like, be able to go for another round, okay... But don't, like, get too excited, I'm, like, not making any promises, okay!"
    return

label bimboed_sleepover_good_response(the_person):  #If you've made her cum
    the_person "Oh my god, like, ugh, fine, okay. That wasn't, like, too terrible, I suppose, okay."
    "She rolls her eyes and smirks, trying to, like, hide her true feelings, okay?"
    mc.name "You, like, want more?"
    $ the_person.draw_person(position = "missionary")
    the_person "Hmph, maybe, okay. But don't, like, think you've won me over or anything, okay. I can, like, still handle more, okay..."
    "[the_person.title] lies down in bed, her breathing still, like, ragged from the previous round, okay."
    the_person "Could you, like, give me another pounding before we go to sleep, okay? But don't, like, expect me to be all lovey-dovey or anything, okay..."
    return

label bimboed_sleepover_bored_response(the_person):  #If she hasn't cum yet
    the_person "Oh my god, like, ugh, is that the best you can do, okay? I was, like, expecting more than that from you, okay..."
    "She crosses her arms and looks at you with a, like, bored expression, clearly unimpressed, okay?"
    mc.name "What's, like, wrong?"
    the_person "You, like, know, just do better, okay. I, like, expect more from you than this, okay..."
    "She rolls her eyes and smirks, still, like, rubbing her pussy in anticipation, okay."
    the_person "You'd, like, better step it up if you want to, like, keep me interested, okay..."
    return

# add more bimbo personality, use different words, and movements.
# update all the following the_person and movements with bimbo personality. Use Cher Horowitz from Clueless or Elle Woods from Legally Blonde, for ideas, keep to the structure. Movements in quotations:
### DIALOGUE ###

