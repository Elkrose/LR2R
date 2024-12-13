### PERSONALITY CHARACTERISTICS ###
# Bimbo is slang for a conventionally attractive, sexualized naïve woman. The term was originally used in the United States as early as 1919 for an unintelligent or brutish man. As of the early 21st century, the "stereotypical bimbo" appearance became akin to that of a physically attractive woman.
#However, as with most identities, the idea of the 'bimbo' has evolved and here is what it means today. The term 'bimbofication' is a colloquial term derived from the term 'bimbo' which is understood to mean, 'an attractive woman who is pretty, sexualised, naive and uneducated'.
#==================================================================
# extra variables to know
# person.ideal_fertile_day
# person._baby_desire
# person._birth_control
# person.kids
# person.fertility_percent
# person.bc_penalty
# and person.kids - person.number_of_children_with_mc > 0
#
# this doesn't read properly, don't use repetitive wording, use different words, and movements. Update all the following the_person and movements with breeding personality. Use Hitomi Takami from Ane Haramix or Momoko Kuzuryu from Sumomomo, Momomo: The Strongest Bride on Earth, for ideas, keep to the structure. Movements in quotations:

label breeder_introduction(the_person):
    mc.name "Hey, can I talk to you for a sec?"
    "[the_person.title] turns around, a gentle smile spreading across her face as she tucks a strand of hair behind her ear."
    the_person "Oh, hello there. I'm happy to talk to you."
    mc.name "I'm sorry if this is awkward, but you seem like an interesting person."
    "[the_person.title] nods slowly, her eyes lighting up with a warm and nurturing expression."
    the_person "Thank you, I try my best to be a good person. I want to make sure everyone around me is happy and healthy... and has a big family to love."
    mc.name "Well, I was wondering if you'd like to... do something together sometime."
    "[the_person.title] blushes deeply, her cheeks flushing with a gentle pink color as she looks down at her feet, her hands clasped together."
    the_person "I-I think that would be nice. But I want to make sure you're interested in me for who I am, not just for... my ability to bear children."
    mc.name "Haha, no, I mean, if you're interested, we could maybe grab coffee or something."
    "[the_person.title] nods enthusiastically, her smile growing wider as she takes a step closer to you, her eyes shining with excitement."
    the_person "That sounds lovely. I love taking care of people and making them happy... and I love the idea of having a big family to love and care for."
    mc.name "Heh, it really does sound lovely."
    $ the_person.set_title()
    $ the_person.set_possessive_title()
    the_person "So, what's your name, anyway?"
    mc.name "I'm [mc.name]. Nice to meet you..."
    the_person "I'm [the_person.name]. It's nice to meet you too, [mc.name]. I hope we can have a lot of babies together... and build a happy family."
    $ the_person.change_happiness(1)
    return

label breeder_greetings(the_person):
    if the_person.love < 0:
        "[the_person.title] frowns slightly, her eyes narrowing as she crosses her arms over her chest, her hands clasped tightly."
        the_person "Ugh, why do you always bother me for something? Can't you see I'm trying to take care of my own needs?"
    elif the_person.happiness < 90:
        "[the_person.title] gives you a faint smile, but her eyes still look a bit downcast as she rubs her belly in a soothing motion."
        if the_person.number_of_children_with_mc > 0:
            the_person "Hi... I guess it's better than nothing, but I'm still having a rough day. Maybe I just need some of your seed in my womb."
        else:
            the_person "Hi... I guess it's better than nothing, but I'm still having a rough day. I just wish I could find someone to take care of me and help me build a family."
    else:
        if the_person.sluttiness > 60:
            if the_person.obedience > 180:
                "[the_person.title] looks at you with a sultry gaze, her eyes sparkling with a hint of mischief as she leans in close, her voice taking on a seductive tone."
                the_person "Oh, it's you... What do you want, [the_person.mc_title]? Don't tell me you're here to help me make some babies? I'm always ready to receive your seed and nurture it into a healthy child."
            else:
                "[the_person.title] gives you a playful wink, her eyes flashing with a hint of teasing as she bounces up and down, her breasts jiggling with the motion."
                the_person "Hey there, [the_person.mc_title]! Just remember, I'm only doing this because I love making babies and taking care of them. And I think you'd make a great father... or at least, a great sperm donor!"
        else:
            if the_person.obedience > 180:
                "[the_person.title] looks at you with a warm smile, her eyes shining with a nurturing expression as she takes your hand in hers, her touch gentle and soothing."
                the_person "Hi, [the_person.mc_title]. What can I do for you? I'm always happy to take care of you and help you build a family. We can be a happy family together, and I'll make sure to take good care of our children."
            else:
                "[the_person.title] gives you a friendly wave, her eyes sparkling with a hint of playfulness as she grins, her face lighting up with a cheerful expression."
                the_person "Hey, what's up? Don't tell me you're here to bother me again... or maybe you're here to make some babies with me? Either way, I'm happy to see you, and I hope we can have some fun together!"
    return

label breeder_sex_responses_foreplay(the_person):
    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] lets out a low moan, her body tensing up as she presses her hips against yours."
            the_person "Mmm, you're not too bad at this, I suppose. But let's see if you can actually make me feel like a mother, overflowing with your seed."
        else:
            "[the_person.possessive_title!c] closes her eyes, her face relaxing as she focuses on the sensations."
            the_person "I suppose this is okay, I guess. But I hope you're not just going to leave me hanging like this. I want to feel your seed inside me, filling me up and making me whole."

    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] starts to move her hips, her body grinding against yours as she begins to pant."
            the_person "You know, this is almost decent. Don't get too cocky, though. I still need to see if you're worthy of being a father, of planting your seed inside me and making me pregnant."
        else:
            "[the_person.possessive_title!c] starts to relax, her body opening up to your touch as she begins to enjoy herself."
            the_person "I mean, it's not bad. You're not completely useless. But I still need to see if you can actually make me pregnant, if you can fill me up with your seed and make me a mother."

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] grasps at your body, her hands pulling you closer as she starts to get more aggressive."
            the_person "Oh, all right. I suppose you're doing something right. But don't think this means I owe you anything. I just want to feel your seed inside me, filling me up and making me whole."
        else:
            "[the_person.possessive_title!c] starts to get more into it, her body moving in time with your touch as she begins to pant."
            the_person "Alright, alright. You're doing it right. But don't expect me to be all mushy about it. I just want to make a baby with you, to feel your seed inside me and know that I'm going to be a mother."

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] loses control, her body shaking with pleasure as she begins to cum."
            the_person "Mmm, I suppose you're getting the hang of this. But don't think this means I'm going to be your little plaything. I just want to be a mother, to feel your seed inside me and know that I'm going to be taking care of our child."
        else:
            "[the_person.possessive_title!c] gets more into it, her body moving in time with your touch as she begins to pant."
            the_person "You're doing alright, [the_person.mc_title]. But don't expect me to be all affectionate about it. I just want to make a family with you, to feel your seed inside me and know that we're going to be parents together."

    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                "[the_person.possessive_title!c] cums hard, her body shaking with pleasure as she screams out in ecstasy."
                the_person "Oh, fine. You're getting close to making me cum. But don't think this means I'm going to fall for you. I just want to be a mother and take care of our child, to feel your seed inside me and know that I'm going to be nurturing our baby."
            else:
                "[the_person.possessive_title!c] cums hard, her body shaking with pleasure as she screams out in ecstasy."
                the_person "The way you touch me is just... different, I guess. But don't think this means I've forgiven you for being such a nuisance. I just want to make a family with you and take care of our child, to feel your seed inside me and know that we're going to be parents together."
        else:
            "[the_person.possessive_title!c] cums hard, her body shaking with pleasure as she screams out in ecstasy."
            the_person "Alright, you're almost there. But don't expect me to be all happy and stuff about it. I just want to make a baby with you and take care of it, to feel your seed inside me and know that I'm going to be a mother."

    return

label breeder_sex_responses_oral(the_person):
    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] looks up at you with a hint of curiosity, her eyes sparkling with interest as she leans in slightly."
            the_person "U-uh, you really don't have to, [the_person.mc_title]... but if you want to, I won't stop you. I just want to make sure you're ready to be a father and take care of our child."
        else:
            "[the_person.possessive_title!c] nods slightly, her cheeks flushing with embarrassment as she looks down."
            the_person "Y-you don't have to, but... if you want to, I'll let you. I just want to feel your love and make a baby with you, to start a family and be a mother."

    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] smirks slightly, her eyes sparkling with mischief as she leans in closer."
            the_person "Mmm, I guess it wouldn't hurt... and it might even feel good. But don't think this means I'm going to go easy on you. I still want to make sure you're worthy of being a father and taking care of our child."
        else:
            "[the_person.possessive_title!c] nods, her expression softening slightly as she smiles."
            the_person "Oh, you really want to? Fine... I'll let you. But be gentle, I want to make sure we can make a healthy baby and start a happy family."

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] lets out a small sigh, her body relaxing slightly as she begins to enjoy herself."
            the_person "Hmph, well, if you insist... I suppose it's not so bad. But don't think this means I'm going to start doing this all the time. I still want to make sure you're worthy of being a father and taking care of our child."
        else:
            "[the_person.possessive_title!c] nods, her expression softening slightly as she smiles."
            the_person "Alright, but don't think I'm doing this because I want to... I'm doing it because I want to make a baby with you and start a family, to be a mother and take care of our child."

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] starts to get more into it, her body moving in time with your touch as she begins to pant."
            the_person "Mmm, you know, maybe this isn't so bad... maybe it's even good. But don't think this means I'm going to start doing this all the time. I still want to make sure you're worthy of being a father and taking care of our child."
        else:
            "[the_person.possessive_title!c] nods, her expression softening slightly as she smiles."
            the_person "Hmph, you're pretty good at this, I'll give you that... but don't think this means I'm going to start doing this all the time. I still want to make sure we can make a healthy baby and start a happy family."

    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                "[the_person.possessive_title!c] starts to cum, her body shaking with pleasure as she screams out in ecstasy."
                the_person "Oh, wow... I didn't know you could do that... maybe I should let you do that more often. But only if you promise to be a good father and take care of our child."
            else:
                "[the_person.possessive_title!c] starts to cum, her body shaking with pleasure as she screams out in ecstasy."
                the_person "Mmm, maybe I should let you do that more often... when [the_person.so_title] isn't around, of course. But only if you promise to be a good father and take care of our child."
        else:
            "[the_person.possessive_title!c] nods, her expression softening slightly as she smiles."
            the_person "Ugh, fine, but don't think I'm enjoying this... I'm only doing it because I want to make a baby with you and start a family, to be a mother and take care of our child."

    return

label breeder_sex_responses_vaginal(the_person):
    if the_person.energy < 10:
        call low_energy_sex_responses_vaginal(the_person) from _vt_breeder_call_low_energy_sex_responses_vaginal_10
        return
    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            $ play_moan_sound()
            "[the_person.possessive_title!c] moans loudly and spreads her legs wide, inviting you to penetrate her deeper."
            "She starts to move her hips, her body bucking wildly as she seeks out more pleasure from your cock."
            the_person "Mmm, your cock is so big and hard... I can feel it stretching my pussy and filling me up. I want to feel your cum inside me and know that we're making a baby."
        else:
            "[the_person.possessive_title!c] bites her lip and stifles a moan, her eyes closed in concentration as she starts to relax and enjoy the sensation of your cock inside her."
            the_person "I'm not sure I'm comfortable with this... but I suppose it's worth it if it means we can make a baby. Just be gentle, okay?"

    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] smirks and winks at you, her eyes sparkling with mischief as she starts to get more into it."
            the_person "Fine, you can keep going if you want. But don't expect me to thank you or anything... yet. I just want to feel your cum inside me and know that we're making a baby."
        else:
            "[the_person.possessive_title!c] nods slightly, her expression softening as she starts to enjoy herself and get more into it."
            the_person "Ugh, I guess your cock is alright... but I still want more. I want to feel your seed inside me and know that I'm going to be a mother."

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] starts to get more into it, her body moving in time with your touch as she begins to pant and get more excited."
            the_person "Mmm, I suppose you're not completely terrible at this... but I still want more. I want to feel your cum inside me and know that we're making a baby."
        else:
            "[the_person.possessive_title!c] nods, her expression softening as she starts to enjoy herself and get more into it."
            the_person "Hmm, your cock is okay, I suppose... but I still want more. I want to feel your seed inside me and know that I'm going to be a mother."

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] starts to lose control, her body shaking with pleasure as she begins to cum and get more excited."
            the_person "You're not the worst, I guess... but I still want more. Keep going and maybe I'll...you know, finish or something. I want to feel your cum inside me and know that we're making a baby."
        else:
            "[the_person.possessive_title!c] nods, her expression softening as she starts to enjoy herself and get more into it."
            the_person "Fine, keep doing what you're doing... it's not like I have anything better to do. I just want to make a baby with you and be a mother."

    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                "[the_person.possessive_title!c] starts to cum, her body shaking with pleasure as she screams out in ecstasy and gets more excited."
                the_person "Ugh, I guess I'm close... but don't think this means I'm impressed or anything. I just want to feel your cum inside me and know that we're making a baby."
            else:
                "[the_person.possessive_title!c] starts to cum, her body shaking with pleasure as she screams out in ecstasy and gets more excited."
                the_person "Yeah, whatever... you're stretching me out, but it's not like it means anything. I just want to feel your cum inside me and know that we're making a baby."
                the_person "Just finish and get it over with... I want to feel your cum inside me and know that I'm going to be a mother."
        else:
            "[the_person.possessive_title!c] nods, her expression softening as she starts to enjoy herself and get more into it."
            the_person "Hmph, I suppose I'm almost there... but don't think I'm enjoying this or anything. I just want to make a baby with you and be a mother."
            the_person "Just finish and let's get this over with... I want to feel your cum inside me and know that I'm going to be a mother."
    return

label breeder_sex_responses_anal(the_person):
    if the_person.energy < 10:
        call low_energy_sex_responses_anal(the_person) from _vt_breeder_call_low_energy_sex_responses_anal_10
        return

    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            the_person "I suppose this is necessary... if we want to make a baby, that is. So go ahead and fuck me in the ass."
            "She looks up at you with a hint of determination, her eyes focused on the task at hand as she leans in slightly."
            "She starts to relax, her body opening up to your touch as she begins to enjoy herself."
        else:
            $ the_person.call_dialogue("annoyed_exclaim")
            the_person "I'm not sure I'm comfortable with this... but I suppose it's for a good cause. So just be gentle, okay?"
            "She grumbles to herself, clearly unenthusiastic, but starts to get more into it as you continue to touch her."

    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            $ the_person.call_dialogue("surprised_exclaim")
            the_person "Wow, this is... actually kind of nice. I didn't know it could feel so good to have a cock in my ass."
            "She squirms a bit, trying to get used to the sensation, but starts to enjoy herself as you continue to touch her."
            "She looks up at you with a hint of excitement, her eyes sparkling with pleasure as she leans in closer."
        else:
            the_person "I'm not sure I like this... but I suppose it's worth it if it means we can make a baby. Just be gentle, okay?"

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            the_person "Okay, okay. You can keep going. I think I'm starting to like it. Fuck me harder, please."
            "She grits her teeth, trying to keep up the appearance of being tough, but starts to lose control as you continue to touch her."
            "She looks up at you with a hint of desperation, her eyes pleading for more as she leans in closer."
        else:
            the_person "Why do you have to be so rough?! Can't you just be gentle for once?"

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            if mc.condom:
                the_person "Just get it over with already... I want to feel your cum inside me and know that we're making a baby. Fuck me until you cum."
            else:
                the_person "Ugh, you really want to do this raw, huh? I suppose it's more natural that way... and it's what we need to do to make a baby. So go ahead and cum inside me."
        else:
            the_person "Why do you always have to be so insistent? Can't you just let me take care of myself for once?"

    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                the_person "Fine, I'll cum... and I hope it means we're making a baby. I want to feel your cum inside me and know that we're creating life. Cum with me, please."
            else:
                the_person "You're just like my [the_person.so_title], always trying to get me to cum... and I suppose it's worth it if it means we can make a baby. So go ahead and cum inside me."
                "She sighs, resigned to her fate, but starts to enjoy herself as you continue to touch her."
        else:
            $ the_person.call_dialogue("annoyed_exclaim")
            the_person "Great, just what I needed: another orgasm... and I hope it means we're making a baby. I want to feel your cum inside me and know that we're creating life. Cum with me, please."
            "She mutters to herself, clearly not thrilled about the prospect, but starts to get more into it as you continue to touch her."

    return

label breeder_climax_responses_foreplay(the_person):
    if the_person.sluttiness > 50:
        the_person "Oh, stop teasing me and just make me cum already! I want to feel your seed inside me."
        "She grits her teeth and squeezes her eyes shut, her body tensing up with anticipation."
    else:
        the_person "Why do you always have to make this so difficult? I just want to make a baby with you."
        "She huffs, clearly on the verge of climax, and starts to move her hips in a desperate attempt to find release."
    return

label breeder_climax_responses_oral(the_person):
    if the_person.sluttiness > 70:
        the_person "Why do you have to be so good at that? Fine, I'll cum! But only because I want to make a baby with you."
        "She throws her head back and lets out a loud moan, her body shaking with pleasure as she cums."
    else:
        the_person "You're really good at that... I didn't think I'd... I'm going to cum... and I hope it means we're making a baby."
        "She smiles and nods, her eyes closed in bliss as she enjoys the sensation of your touch."
    return

label breeder_climax_responses_vaginal(the_person):
    if the_person.sluttiness > 70:
        if the_person.arousal_perc > 120:
            the_person "Fine, I'll cum. But don't think this means I'm enjoying myself... I'm just doing it because I want to make a baby."
            "She grits her teeth and squeezes her eyes shut, her body tensing up as she tries to fight off the pleasure."
        else:
            the_person "Ugh, just a little more... I'm... Ah, fuck! I think I'm going to cum and make a baby!"
            "She throws her head back and lets out a loud moan, her body shaking with pleasure as she cums."
        "She squeezes her legs together, trying to trap your cock inside her and keep the pleasure going."
    else:
        the_person "Oh... I can't... I'm going to... Ah! I hope it means we're making a baby!"
        "She smiles and nods, her eyes closed in bliss as she enjoys the sensation of your touch."
    return

label breeder_climax_responses_anal(the_person):
    if the_person.sluttiness > 70:
        if the_person.arousal_perc > 120:
            the_person "Fine, you win. I'll cum. But don't think I'm doing this because I want to... I'm just doing it because I want to make a baby."
            "She squeezes her eyes shut, trying to fight off the pleasure and maintain her composure."
        else:
            the_person "Ugh, just a little more... My ass is going to... Ah! I think I'm going to cum and make a baby!"
            "She throws her head back and lets out a loud moan, her body shaking with pleasure as she cums."
        "She tries to catch her breath, her body still shaking with pleasure as she enjoys the aftermath of her climax."
    else:
        the_person "Oh... My... Ass... I... Ah! I hope it means we're making a baby!"
        "She barely finishes her sentence before her body is racked with pleasure and she cums loudly."
    return

label breeder_clothing_accept(the_person):
    if the_person.obedience > 180:
        the_person "I suppose this outfit is acceptable... but don't think I'm doing it just to please you. I want to look good for our future child."
        "[the_person.title] nods and smiles slightly, her eyes shining with a hint of maternal instinct."
    else:
        the_person "Yeah, whatever. Just don't expect me to go around looking like a total slut. I want to be a respectable mother."
        "[the_person.title] shrugs and looks away, her expression neutral but with a hint of determination in her eyes."
    return

label breeder_clothing_reject(the_person):
    if the_person.should_wear_uniform:
        the_person "Hey, I guess I should get my uniform sorted out, right? One second. I want to look professional for our future child's sake."
        "[the_person.title] nods and heads off to change, her movements efficient and practical."
    elif the_person.obedience > 180:
        the_person "I don't... I'm sorry, but I really don't think I could get away with wearing something like this. I appreciate the thought though. I want to be a good role model for our child."
        "[the_person.title] looks down and fidgets, her expression embarrassed but with a hint of determination in her eyes."
    else:
        if the_person.sluttiness > 60:
            the_person "Hmm, I don't know about this one. It's a bit too revealing for my taste. I want to be a respectable mother, not a sex object."
            "[the_person.title] frowns and crosses her arms, her expression disapproving but with a hint of playfulness in her eyes."
        else:
            the_person "You've got to be kidding me, right? This is ridiculous. I'm not wearing this. I want to be a good mother, not a laughing stock."
            "[the_person.title] rolls her eyes and scoffs, her expression disgusted but with a hint of amusement in her eyes."
    return

label breeder_clothing_review(the_person):
    if the_person.outfit.cum_covered:
        if (the_person.sluttiness > 40 and the_person.opinion.being_covered_in_cum >=0) or the_person.opinion.being_covered_in_cum > 0:
            the_person "Ugh, why do I always get so messy with you...? I guess I'll just have to get used to it if we're going to make a baby."
            "[the_person.title] starts to wipe up the biggest splashes of cum on her, her movements gentle and maternal."
        else:
            the_person "For goodness' sake, I need to clean up this mess! Let me know if I've missed any, okay? I want to be clean for our child's sake."
            "[the_person.title] wipes herself down, cleaning up all the cum she can find with efficient and practical movements."

    if the_person.obedience > 180:
        the_person "Fine, I'll be back in a moment. I need to get cleaned up for you... and for our future child."
        "[the_person.title] nods and heads off to change, her movements efficient and practical."
    else:
        if the_person.sluttiness > 40:
            the_person "I don't know why I do this, but I want to look good for you... and for our child. I'll be back in a second, I just want to get cleaned up."
            "[the_person.title] smiles and heads off to change, her movements bouncy and playful."
        else:
            the_person "Ugh, everything's such a mess after that. Wait here a moment, I'm just going to find a mirror and try and look somewhat presentable for our child's sake."
            "[the_person.title] sighs and heads off to change, her movements slow and deliberate."
    $ the_person.apply_planned_outfit(show_dress_sequence = True)
    return

label breeder_strip_reject(the_person, the_clothing, strip_type = "Full"):
    if the_person.obedience > 180:
        the_person "Hey, could we leave my [the_clothing.display_name] on for now, please? I want to feel a little more... modest."
        "[the_person.title] blushes and looks down, her eyes shining with a hint of shyness."
    elif the_person.obedience < 70:
        the_person "No, no, no, I'll decide what comes off and when, okay? Don't rush me! I want to feel in control."
        "[the_person.title] crosses her arms and pouts, her expression defiant and playful."
    else:
        the_person "Not yet... I don't know if I'm ready to take off my [the_clothing.display_name]. Maybe we can try something else first? I want to feel more comfortable."
        "[the_person.title] bites her lip and looks up at you, her eyes shining with a hint of curiosity."
    return

label breeder_strip_obedience_accept(the_person, the_clothing, strip_type = "Full"):
    "[the_person.title] gulps and nervously laughs as you start to slide her [the_clothing.display_name] away, but she doesn't stop you."
    if the_person.obedience > 180:
        the_person "Alright, fine... I guess I can trust you with this. Just be gentle, okay?"
        "[the_person.title] smiles slightly and nods, her eyes shining with a hint of trust."
    else:
        the_person "I don't know if this is a good idea, but I'll let you do it this once... just be careful, okay?"
        "[the_person.title] bites her lip and looks up at you, her eyes shining with a hint of uncertainty."
    return

label breeder_grope_body_reject(the_person):
    if the_person.effective_sluttiness("touching_body") < 5: #Fail point for touching shoulder
        the_person "Hmph! What do you think you're doing? That's not very gentlemanly."
        "[the_person.title] steps back and crosses her arms over her chest, her expression disapproving and stern."
        the_person "Just get your hands off me, okay? You're making me uncomfortable. I want to feel respected."
        mc.name "Oh, sorry. I didn't mean to make you feel that way."
        the_person "Yeah, well, try to be more careful next time, alright? I want to feel safe with you."
        "She seems a little put off by the situation, but you both try to move on and put it behind you."
    else: #Fail point for touching waist
        the_person "Hey, could you just... not do that, okay? It's a little too forward for me."
        "[the_person.title] takes your hand and pulls it off of her waist, giving you a warning look."
        the_person "... Just keep your hands to yourself, got it? I want to feel in control of my own body."
        mc.name "Oh yeah, of course. My bad."
        the_person "Just make sure you don't do it again, okay? I don't appreciate it. I want to feel respected and cared for."
        "She doesn't say anything else, but you can tell she's still a bit annoyed about the situation."
    return

label breeder_sex_accept(the_person, the_position):
    if the_person.sluttiness > 70:
        if the_person.obedience < 70:
            the_person "Fine, let's do it. But don't think this means I'm going to be your personal sex toy... at least, not yet. I want to feel your cock inside me and know that we're making a baby."
            "[the_person.title] smirks and winks at you, her eyes sparkling with mischief as she spreads her legs and invites you to penetrate her."
        else:
            if the_position.skill_tag == "Foreplay":
                the_person "Oh, I've been wanting you to do that for a while now. Just thinking about it makes me wet and ready to breed. I want to feel your fingers inside me and know that we're making a baby."
                "[the_person.title] bites her lip and looks up at you, her eyes shining with desire as she starts to move her hips and get into position."
            elif the_position.skill_tag == "Oral":
                if "getting head" in the_position.opinion_tags:
                    the_person "Ugh, I need your tongue on my clit, now! Make me cum and get me ready for breeding. I want to feel your mouth on my pussy and know that we're making a baby."
                    "[the_person.title] spreads her legs and pulls you in, her body tensing up with anticipation as she starts to moan and get into it."
                else:
                    the_person "You're going down on me right now, and you're going to make me cum and get me ready for breeding. I want to feel your mouth on my pussy and know that we're making a baby."
                    "[the_person.title] nods and smiles, her eyes shining with excitement as she starts to move her hips and get into position."
            else:
                the_person "Get over here and fuck me already. I've been waiting for this and I'm ready to breed. I want to feel your cock inside me and know that we're making a baby."
                "[the_person.title] grabs your arm and pulls you in, her body tensing up with anticipation as she starts to moan and get into it."
    else:
        the_person "Come here, let's do it. But don't think I'm going to do this all the time, got it? I want to breed, but I also want to be respected and treated like a lady."
        "[the_person.title] nods and smiles, her eyes shining with determination as she starts to move her hips and get into position."
    return

label breeder_sex_obedience_accept(the_person):
    if the_person.sluttiness > 70:
        the_person "Ugh, fine. I don't want to admit it, but you've gotten to me. Do whatever you want to me, [the_person.mc_title]. I'm ready to breed and make a baby with you."
        "[the_person.title] looks down and nods, her eyes shining with submission as she starts to move her hips and get into position."
    else:
        if the_person.obedience > 180:
            the_person "Alright, I'll do what you say, but don't think this means I'm going to like it. I'm only doing this because I want to breed and make a baby with you."
            "[the_person.title] nods and looks up at you, her eyes shining with determination as she starts to move her hips and get into position."
        else:
            the_person "I shouldn't be saying this, but if you really want to... I'll give it a try. Just this once, okay? I want to breed and make a baby with you, but I'm not sure if I'm ready."
            "[the_person.title] bites her lip and looks up at you, her eyes shining with uncertainty as she starts to move her hips and get into position."
    return

label breeder_sex_gentle_reject(the_person):
    if the_person.sluttiness > 50:
        the_person "Ugh, not like that, [the_person.mc_title]. I need a little more foreplay first. I want to be ready to breed and make a baby with you."
        "[the_person.title] pushes you away and looks up at you, her eyes shining with frustration as she starts to move her hips and get into position."
    else:
        the_person "No, no, no. I want to have fun, but I don't want to get too serious. Let's just keep it light and see if we're compatible for breeding and making a baby."
        "[the_person.title] shakes her head and smiles, her eyes shining with amusement as she starts to move her hips and get into position."
    return

label breeder_sex_angry_reject(the_person):
    if the_person.has_significant_other:
        the_person "How dare you! I'm already breeding with my [the_person.so_title], and I won't betray them like that. You're not worthy of my pussy or my womb."
        "She glares at you with a fierce expression, her eyes blazing with anger as she turns away and storms off."
    elif the_person.sluttiness < 20:
        the_person "You're disgusting! I would never breed with someone like you. Your cock is probably diseased and your cum is weak."
        "[the_person.title] takes a step back, her face red with anger as she crosses her arms and glares at you."
    else:
        the_person "What's wrong with you? Can't you see I'm not interested in breeding with you? Your sperm is probably worthless and your dick is small."
        "[the_person.title] shakes her head, her expression disgusted as she turns away and walks away."
    return

label breeder_seduction_response(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 50:
            the_person "I think I know what you need, and I'm happy to provide it. Let's make a baby together and fill my womb with your cum."
            "[the_person.title] smiles and nods, her eyes shining with excitement as she takes your hand and leads you to a private area."
        else:
            the_person "Okay, I'll give you a few minutes. But don't think this means I'm going to be your breeding slave or anything. I want to feel your cock inside me and know that we're making a baby."
            "[the_person.title] nods and smiles slightly, her expression neutral as she follows you to a private area."
    else:
        if the_person.sluttiness > 50:
            the_person "Mmm, you're feeling as horny as me then? Come on, let's go find a place to get out of sight and make a baby. I want to feel your cum inside me and know that we're creating life."
            "[the_person.title] takes your hand and leads you off to find some place private, her eyes shining with excitement as she smiles and giggles."
        elif the_person.sluttiness > 10:
            "[the_person.title] smirks and raises an eyebrow, her expression teasing as she leans in close and whispers in your ear."
            the_person "I know that look you're giving me, I think I know what you want. But don't expect me to give it up that easily. I want to make sure you're worthy of breeding with me and filling my womb with your cum."
        else:
            the_person "[mc.name], I know what you mean... Okay, I can spare a few minutes. But don't get your hopes up, I'm not promising anything. I want to feel your cock inside me and know that we're making a baby, but I'm not sure if I'm ready."
            "[the_person.title] nods and smiles slightly, her expression neutral as she follows you to a private area."
    return

label breeder_seduction_accept_crowded(the_person):
    if not the_person.has_significant_other:
        if the_person.sluttiness < 20:
            the_person "Alright, let's sneak away for a few minutes and you can convince me a little more. But don't think this means I'm going to breed with you right away. I want to feel your cock inside me and know that we're making a baby, but I'm not sure if I'm ready."
            "[the_person.title] nods and smiles slightly, her expression neutral as she follows you to a private area."
        elif the_person.sluttiness < 50:
            the_person "Come on, I know someplace nearby where we can get a few minutes privacy. Just make it quick, I don't want to get caught. I want to feel your cum inside me and know that we're making a baby."
            "[the_person.title] takes your hand and leads you off to find some place private, her eyes shining with excitement as she smiles and giggles."
        else:
            "[the_person.title] moans and leans in close, her eyes shining with desire as she kisses you passionately."
            the_person "Oh, I don't know if I can wait much longer [the_person.mc_title]... I need to feel your cock inside me and know that we're making a baby. I want to feel your cum filling my womb and know that we're creating life."
    else:
        if the_person.sluttiness + (5*the_person.opinion.cheating_on_men) > 50:
            the_person "Fuck it, let's do this! I don't care about my [the_person.so_title] right now, I just want to breed with you and feel your cum inside me."
            "[the_person.title] grabs your arm and pulls you in, her eyes shining with excitement as she kisses you passionately."
        else:
            the_person "Ugh, you're bad for me [the_person.mc_title]... Come on, we need to find somewhere quiet so my [the_person.so_title] doesn't catch us. I don't want to get in trouble for breeding with someone else, but I want to feel your cock inside me and know that we're making a baby."
            "[the_person.title] nods and smiles slightly, her expression neutral as she follows you to a private area."
    return

label breeder_seduction_accept_alone(the_person):
    if not the_person.has_significant_other:
        if the_person.sluttiness < 20:
            the_person "Very well, I'll give you a chance to prove yourself. Show me what you're made of and fill my womb with your cum."
            "[the_person.title] nods and leans back, her eyes sparkling with curiosity as she starts to undress and exposes her breasts."
        elif the_person.sluttiness < 50:
            the_person "Let's get down to business, shall we? I want to see if you're worthy of breeding with me and filling my pussy with your seed."
            "[the_person.title] smirks and starts to undress, her movements slow and seductive as she exposes her ass and invites you to take her."
        else:
            the_person "I'm so hot right now, I need you to take me. Fill me with your cum and make me a mother. I want to feel your cock inside me and know that we're making a baby."
            "[the_person.title] moans and throws herself at you, her body tensing up with anticipation as she wraps her legs around you and pulls you in."
    else:
        if the_person.sluttiness + (5*the_person.opinion.cheating_on_men) > 50:
            the_person "I know I shouldn't be doing this, but I just can't resist. Take me, [the_person.mc_title], and make me yours. Fill my pussy with your cum and make me a mother."
            "[the_person.title] grabs your arm and pulls you in, her eyes shining with excitement as she kisses you passionately and invites you to take her."
        else:
            the_person "You're a bad influence, [the_person.mc_title], but I just can't help myself. Come here and take me. Fill my womb with your seed and make me a mother."
            "[the_person.title] sighs and nods, her expression resigned as she submits to your advances and allows you to take her."
    return

label breeder_seduction_refuse(the_person):
    if the_person.sluttiness < 20:
        the_person "Ugh, why are you always trying to get me into bed, [mc.name]? Can't you see I'm not interested in breeding with you right now?"
        "[the_person.title] folds her arms and looks away, her expression disapproving and uninterested."
    elif the_person.sluttiness < 50:
        the_person "Fine, I'll admit you're kind of cute, but don't think this means I'm actually interested in making a baby with you. Maybe some other time, when I'm in a better mood."
        "[the_person.title] playfully pokes your chest with her finger, her eyes sparkling with amusement and teasing."
    else:
        the_person "Eh, you're always trying to get me into bed, [mc.name], but I'm not going to make it easy for you. You'll have to wait until I'm good and ready to breed. Maybe that'll be never, who knows?"
        "[the_person.title] grins mischievously and walks away, her hips swaying seductively as she leaves you to wonder what she's thinking."
    return

label breeder_compliment_response(the_person):
    mc.name "Hey [the_person.fname], you look really beautiful today. Is there a special occasion or something?"
    if the_person.is_at_work:
        if (the_person.is_employee or the_person.is_strip_club_employee) and the_person.is_wearing_uniform:
            call breeder_flirt_response_employee_uniform_low(the_person) from _call_breeder_flirt_response_employee_uniform_low_compliment_response
        elif the_person.is_at_job(prostitute_job):
            the_person "Ugh, why do you always want to hang out with me? Can't you see I'm busy making money to support my future child?"
        elif the_person.sluttiness > 50:
            the_person "I'm doing great, thanks for asking. But don't think this means I'm actually interested in breeding with you or anything."
        else:
            the_person "Oh, stop it, you're making me blush. There's no special occasion, I just felt like dressing up today to attract a potential mate."
    else:
        the_person "Well, I did put in a bit of extra effort today. You're just the first one to notice. But thanks, I guess. Maybe it'll help me find a good breeding partner."
    "You try to press for more information, but [the_person.possessive_title!c] just smiles coyly and changes the subject, leaving you wondering what's going on."
    return

label breeder_compliment_response_girlfriend(the_person):
    mc.name "Hey [the_person.title]. You're looking very nice this [StringInfo.time_of_day_string]."
    if the_person.is_at_work:
        if (the_person.is_employee or the_person.is_strip_club_employee) and the_person.is_wearing_uniform:
            call breeder_flirt_response_employee_uniform_mid(the_person) from _call_breeder_flirt_response_employee_uniform_mid_compliment_response_girlfriend
            $ the_person.call_dialogue("flirt_response_employee_uniform_mid")
        elif the_person.sluttiness > 50:
            the_person "Mmm, thank you, [the_person.mc_title]. Wanna find out how nice I am... in bed, that is?"
        else:
            the_person "Hmph, really? Thanks, [the_person.mc_title]. You're not so bad yourself. Maybe we can make a baby together soon."
    else:
        the_person "Ugh, don't be ridiculous. It's just a normal day... but thanks, I guess. You're always so sweet to me, maybe that's why I love breeding with you."
        mc.name "Oh come on, don't be like that. You know you look great, and I love making babies with you."
        the_person "Aww, stop it, [the_person.mc_title]. You're making me blush... and annoyed at the same time. But I have to admit, I love the way you make me feel when we're breeding."
    "You chat with [the_person.possessive_title!c] for a while, and although she's initially annoyed by your compliments, she starts to warm up to you and gets in the mood for breeding."
    return

label breeder_compliment_response_affair(the_person):
    mc.name "Hey [the_person.title]. You're looking absolutely amazing this [StringInfo.time_of_day_string]."
    if the_person.is_at_work:
        if (the_person.is_employee or the_person.is_strip_club_employee) and the_person.is_wearing_uniform:
            call breeder_flirt_response_employee_uniform_mid(the_person) from _call_breeder_flirt_response_employee_uniform_mid_compliment_response_affair
        elif the_person.sluttiness > 50:
            the_person "Mmmm, thank you [the_person.mc_title], wanna go somewhere a little more private, so you can make me feel how amazing I am... and maybe make a baby together?"
        else:
            the_person "Hmph, really? Thanks, [the_person.mc_title]. You're not so bad yourself. Maybe we can have a secret breeding session soon."
    else:
        the_person "Ugh, don't be silly. It's just a normal day... but thanks, I suppose. You always know how to make me feel special, and I love the way you breed with me."
        mc.name "Oh come on, don't be like that. You know you look great, and I love making babies with you in secret."
        the_person "Aww, stop it, [the_person.mc_title]. You're making me blush... and a little annoyed. But I have to admit, I love the thrill of our secret breeding sessions."
    "You keep chatting with [the_person.possessive_title!c] for a while, slipping in a few more compliments. She is quite charmed by your attentiveness and gets in the mood for a secret breeding session."
    return

label breeder_flirt_response(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 50:
            the_person "Hmm, I suppose you're not entirely unappealing, [the_person.mc_title]. You have a certain... spark."
            "[the_person.title] raises an eyebrow and gives you a sly smile, her eyes sparkling with interest."
        else:
            the_person "Whatever. Thanks for the compliment, [the_person.mc_title]. You're not completely unattractive, I suppose."
            "[the_person.title] shrugs and looks away, her expression neutral but with a hint of curiosity."

    elif the_person.has_significant_other:
        if the_person.sluttiness + (the_person.opinion.cheating_on_men*5) > 50:
            the_person "Oh, you think you're so charming, don't you? I'll give you that. You have a certain... allure."
            "[the_person.title] gives you a sly look, her eyes narrowing as she leans in close and whispers in your ear."
        else:
            the_person "You're really pushing your luck, [the_person.mc_title]. I have a [the_person.so_title] you know, and I'm not looking for a new breeding partner."
            mc.name "What about you, do you appreciate it?"
            "She rolls her eyes and crosses her arms, her expression disapproving but with a hint of amusement."
            the_person "Maybe I do, maybe I don't. It's none of your business, but I will say that I'm not interested in breeding with you."

    else:
        if the_person.sluttiness > 50:
            the_person "Fine. Maybe you're worth my time, [the_person.mc_title]. You seem like a suitable breeding partner."
            "[the_person.title] gives you a half-smile, but her eyes remain guarded as she sizes you up and considers your potential."
        else:
            the_person "Whatever. You're not unattractive, I suppose. But don't think that means I'll go easy on you. I have high standards for my breeding partners."
            the_person "You'll have to really impress me though, and prove yourself worthy of breeding with me."
            "[the_person.title] folds her arms and looks at you expectantly, her expression challenging but with a hint of interest."
    return

label breeder_flirt_response_employee_uniform_low(the_person):
    if the_person.is_wearing_forced_uniform:
        the_person "You like seeing me in this uniform, don't you? It's practically begging to be bred."
        mc.name "I know you don't like it, but I needed to make a point. You look amazing, and I want to breed with you."
        the_person "I know, I know. You always were one to make a point... and get what you want."
        $ mc.change_locked_clarity(5)
        "She crosses her arms over her chest, but can't hide the small smile on her face as she looks up at you with a hint of desire."

    elif the_person.judge_outfit(the_person.outfit):
        #She's in uniform and likes how it looks.
        the_person "Oh, you noticed? I thought it was a bit much, but I guess it's not so bad. I feel like a total breeding machine in this thing."
        the_person "I mean, it's nice to work somewhere where I can show off a little and attract some potential breeding partners."
        $ mc.change_locked_clarity(5)
        "She winks at you, then turns to adjust her uniform, accentuating her hips and breasts as she strikes a pose."

    else:
        #She's in uniform, but she thinks it's a little too slutty.
        if the_person.vagina_visible:
            # Her pussy is on display.
            the_person "Hmph, I suppose you like seeing me like this... my pussy is practically begging to be bred."
            mc.name "Well, you know that it's..."
            the_person "I know, I know. It's company policy. But don't think you're the only one who's annoyed by it. I want to be bred, not just displayed like a piece of meat."
            mc.name "Give it some time and you'll get used to it. And who knows, maybe you'll even start to enjoy it."
            $ mc.change_locked_clarity(5)
            "She rolls her eyes, but doesn't argue as she looks up at you with a hint of desire."

        elif the_person.tits_visible:
            # Her tits are out
            the_person "Ugh, I'm still getting used to being so... exposed in this uniform. At least I don't have to wear a bra, and my tits are free to bounce around and attract some attention."
            mc.name "You look incredible and you're comfortable. I call that a success. And I have to say, your tits are looking particularly delicious today."
            $ mc.change_locked_clarity(5)
            "She huffs, but can't hide her smile as she looks up at you with a hint of desire and plays with her nipples."

        elif the_person.underwear_visible:
            # Her underwear is visible.
            the_person "Hmph, I probably would have picked something that kept me a little more covered, but at least our uniform is comfortable and shows off my breeding potential."
            mc.name "It may be a little unconventional, but you look fantastic. You've got exactly the right kind of body for breeding, and I can already imagine my cum inside you."
            the_person "Well, that's one way to look at it, I suppose. But don't think you're getting inside me that easily. I want to be bred, not just used for your pleasure."
            $ mc.change_locked_clarity(5)
            "She playfully rolls her eyes and turns to adjust her uniform, showing off her body and underwear as she strikes a pose."

        else:
            # It's just generally slutty.
            the_person "Ugh, well thank you! Our uniforms are a little bold for my taste, but I guess I look good in it. And who knows, maybe it'll even attract some potential breeding partners."
            $ mc.change_locked_clarity(5)
            "She blushes and looks away, but not before you catch a glimpse of her small smile as she looks up at you with a hint of desire."

    return

label breeder_flirt_response_employee_uniform_mid(the_person):
    if the_person.is_wearing_forced_uniform:
        $ mc.change_locked_clarity(10)
        if the_person.vagina_visible:
            the_person "Ugh, fine. You caught me off guard. I'll admit, this uniform does make me look good, especially with my pussy on display. It's like I'm begging to be bred."
            mc.name "It's a great uniform, but that's not what's important here. What's important is that you're comfortable and ready to breed."
            the_person "Yeah, yeah. You're right. It's just hard not to feel like a sex object in this thing, especially with my vagina exposed and ready for your cock."
            "[the_person.title] sighs and nods, her eyes looking down at her exposed pussy."
        elif the_person.tits_visible:
            the_person "Ugh, fine. You caught me off guard. I'll admit, this uniform does make me look good, especially with my boobs popping out. It's like I'm advertising my breeding potential."
            mc.name "It's a great uniform, but that's not what's important here. What's important is that you're comfortable and ready to breed."
            the_person "Yeah, yeah. You're right. It's just hard not to feel like a sex object in this thing, especially with my tits on display and my nipples hardening at the thought of your touch."
            "[the_person.title] smirks and adjusts her uniform, accentuating her breasts and nipples."
        else:
            the_person "Ugh, fine. You caught me off guard. I'll admit, this uniform does make me look good. It's like I'm a breeding machine, ready to be used and impregnated."
            mc.name "It's a great uniform, but that's not what's important here. What's important is that you're comfortable and ready to breed."
            the_person "Yeah, yeah. You're right. It's just hard not to feel like a sex object in this thing, especially when I'm around you and your potent sperm."
            "[the_person.title] looks up at you with a hint of desire in her eyes, her body leaning in towards you."
        mc.name "Rules are rules and I can't make any exceptions, even if they look good and make me want to breed with you."
        "She sighs and nods, her expression resigned but with a hint of amusement."
        the_person "Yeah, I know. At least you're having a good time. I don't mind that so much, especially if it means you'll breed with me soon."

    elif the_person.judge_outfit(the_person.outfit):
        $ mc.change_locked_clarity(10)
        if the_person.tits_visible:
            the_person "Hmph, maybe I should wear this outfit more often. It's getting a lot of attention, especially for my boobs and my breeding potential."
            mc.name "It's a great outfit, but I'm more interested in the person wearing it and their ability to breed."
            the_person "Oh, really? Is that so? I guess my boobs are hard to ignore, especially when they're bouncing around and begging to be touched."
            "[the_person.title] smirks and adjusts her uniform, accentuating her breasts and nipples."
        else:
            the_person "Hmph, maybe I should wear this outfit more often. It's getting a lot of attention, especially for my vagina and my ability to breed."
            mc.name "It's a great outfit, but I'm more interested in the person wearing it and their ability to breed."
            the_person "Oh, really? Is that so? I guess my vagina is hard to ignore, especially when it's exposed and ready for your cock."
            "[the_person.title] smirks and spreads her legs, exposing her vagina and inviting you to breed with her."
        the_person "Maybe I'll invite you shopping one day and you can tell me what else you want to see me in... or out of."
        mc.name "Sounds like a good time, especially if it means I get to breed with you."

    else:
        # the_person "I think it shows off a little too much!"
        the_person "Ugh, fine. You're not gonna make this easy for me, are you? You're going to make me beg for your sperm and your attention."
        $ mc.change_locked_clarity(10)
        if the_person.vagina_visible:
            the_person "I'm trying to focus on my work here, not flirt with you all day and expose my vagina to the entire office. But I have to admit, it's hard to resist your charms and your potent sperm."
        elif the_person.tits_visible:
            the_person "I'm trying to focus on my work here, not flirt with you all day and show off my boobs to the entire office. But I have to admit, it's hard to resist your charms and your attention."
        else:
            the_person "I'm trying to focus on my work here, not flirt with you all day and beg for your sperm. But I have to admit, it's hard to resist your charms and your breeding potential."
        mc.name "I understand, but I promise it's important for the business and for our breeding goals."
        "She sighs and nods, her expression resigned but with a hint of amusement."
        the_person "Yeah, I know. You're a real pain, you know that? But I'll do whatever it takes to breed with you and make a baby."
    return

label breeder_flirt_response_low(the_person):
    #She's in her own outfit.
    the_person "Hmph, I suppose this outfit doesn't make me look like a complete breeding failure."
    $ the_person.draw_person(position = "back_peek")
    $ mc.change_locked_clarity(5)
    "She strikes a pose, showing off her curves and gives you a sly smile as she bats her eyelashes at you."
    the_person "I mean, I guess it's not too bad for a breeding machine like me, right?"
    $ the_person.draw_person()
    mc.name "I think it looks amazing on you, and it really shows off your breeding potential."
    the_person "Oh, shut up. You're just saying that to get in my pants and breed with me."
    return

label breeder_flirt_response_low1(the_person):
    if the_person.has_significant_other:
        the_person "Ugh, what's with you and the flirting? I've got a [the_person.so_title], and I don't think he'd appreciate you trying to breed with me behind his back."
        mc.name "What about you, do you appreciate it?"
        "She rolls her eyes and smirks, her expression teasing and playful."
        the_person "Maybe I do... but don't think you're getting anywhere with me that easily. I'm not just going to open my legs and let you breed with me without a fight."
    else:
        the_person "Well, thanks for the compliment. But don't think you're getting off that easy. I have high standards for my breeding partners, and you'll need to prove yourself to me before I let you breed with me."
        the_person "But if you can impress me, who knows what might happen... maybe we'll even make a baby together."
    $ mc.change_locked_clarity(5)
    return

label breeder_flirt_response_mid(the_person):
    if mc.location.person_count > 1 and the_person.effective_sluttiness("kissing") < (25 - (5*the_person.opinion.public_sex)):
        $ mc.change_locked_clarity(10)
        the_person "You know, I was wondering if you actually noticed my breeding potential today..."
        "Her eyes narrow slightly, but she's still trying to appear casual and uninterested in your advances."
        mc.name "I noticed. You look like a prime breeding candidate."
        the_person "Oh, really? Thanks, I guess. I was thinking you might say something like that, but I didn't think you'd be so... forward."
        "She crosses her arms, trying to maintain a tough exterior and hide her interest in your proposal."
        if the_person.tits_visible:
            mc.name "I noticed. You look like a prime breeding candidate, especially with those tits on display."
            the_person "Oh, really? Thanks, I guess. I was thinking you might say something like that, but I didn't think you'd be so... forward and explicit."
            "She blushes and looks away, trying to hide her embarrassment and interest in your proposal."
        else:
            mc.name "Well, it's true. You look like a prime breeding candidate, and I think we could make some amazing babies together."
        the_person "Hmph. Maybe I'll invite you shopping one day, so you can tell me what else you want to see me in... or out of."
        "She leans in slightly, a hint of flirtation and interest in her voice and body language."
        mc.name "I can think of a few things already... and I'm sure I'd enjoy seeing you in them, or breeding with you in general."
        the_person "I'm sure you would. So, what do you say? Want to take me out for a drink and maybe we can discuss my wardrobe... and breeding potential some more?"

    else:
        the_person "Thanks, I thought I looked pretty hot and fertile in it too."
        the_person "You want a better look, right? Here, how does it make my ass and breeding potential look?"
        $ the_person.draw_person(position = "back_peek")
        $ mc.change_locked_clarity(10)
        the_person "Good, right? You can't help but want to breed with me, can you?"
        mc.name "Fantastic. I wish I could get an even better look at it, and maybe even breed with you right now."
        "[the_person.possessive_title!c] smiles and turns back to face you, her eyes sparkling with interest and desire."
        $ the_person.draw_person()
        the_person "I'm sure you do. Take me out for a drink and maybe we can work something out... like a breeding contract, or a baby."
    return

label breeder_flirt_response_mid1(the_person):
    $ mc.change_locked_clarity(10)
    the_person "Thanks, I do look amazing and fertile in this outfit."
    if (the_person.has_skirt or the_person.has_dress) and not the_person.has_thigh_high_socks:
        mc.name "You could change it up with some high stockings, I would love to see that and imagine breeding with you."
        the_person "Oh, really? And why would you want to see that? You're not going to get a peek or anything, are you? Or maybe you just want to see my legs and imagine them wrapped around your waist as we breed."
        mc.name "Because it would look great on you, and I would enjoy the view and the thought of breeding with you."

    mc.name "How about you and me go and grab a coffee sometime and discuss our breeding potential?"
    if the_person.has_significant_other:
        the_person "Sure, my [the_person.so_title] doesn't mind... as long as they're not around to witness how much fun we're going to have and how many babies we're going to make."
    else:
        the_person "Why not, I could use a pick-me-up once in a while... and maybe someone to pick me up from the ground when I fall for you and your potent sperm."
    the_person "Just let me know when, I would love to... and don't think I won't notice if you're trying to get a glimpse of my legs under the table or imagine breeding with me."
    mc.name "I'll keep that in mind, and maybe we can discuss what else you want to wear in the future... or not wear, and how many babies we're going to make together."
    the_person "Hmph, maybe. But don't think you're getting a discount on my wardrobe just because we're going out for coffee... or anything else, like a breeding contract or a baby."
    return

label breeder_flirt_response_high(the_person):
    if mc.location.person_count > 1 and the_person.effective_sluttiness() < (25 - (5*the_person.opinion.public_sex)): # There are other people here, if she's not slutty she asks if you want to find somewhere quiet
        the_person "You're really persistent, huh? Fine, but not here... I don't want to breed in public, at least not yet."
        "She glances around before giving you a sly smile and winking at you."
        menu:
            "Find somewhere more quiet\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                mc.name "Then let's find somewhere that isn't here, where we can breed in private."
                the_person "Hmph, eager much? Alright, let's go and make some babies."
                call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_breeder_flirt_response_high_2
                the_person "So... Now what's your plan? Are you going to breed with me or just tease me some more?"

                if the_person.is_willing(kissing):
                    $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
                    if the_person.has_taboo("kissing"):
                        "You lean in close to kiss [the_person.title], your lips brushing against hers."
                        $ the_person.call_dialogue("kissing_taboo_break")
                        $ the_person.break_taboo("kissing")
                        "She responds passionately, her arms wrapping around your neck and pulling you in for a deeper kiss."
                    else:
                        "You step close to [the_person.title] and put your arm around her waist, pulling her close and kissing her."
                        "She responds immediately and eagerly presses her body against yours, her tits and pussy rubbing against you."
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _vt_breeder_call_fuck_person_49
                else:
                    if the_person.has_taboo("touching_body"):
                        $ the_person.call_dialogue("touching_body_taboo_break")
                        $ the_person.break_taboo("touching_body")
                        "You take her hand and pull her close against you, your bodies touching and rubbing against each other."
                        "She looks into your eyes, her expression teasing and playful."
                    else:
                        "You take her hand and pull her close, your lips brushing against her ear and whispering sweet nothings into it."
                    call fuck_person(the_person, private = True, start_position = standing_grope, skip_intro = True) from _call_fuck_person_breeder_flirt_grope

                $ the_person.call_dialogue("sex_review", the_report = _return)
                call mc_restore_original_location(the_person) from _call_mc_restore_original_location_breeder_flirt_response_high_2

            "Just flirt":
                mc.name "You know you want to, come on. I'll take you out for dinner, and then we can see where the night takes us... maybe to a hotel room where we can breed all night."
                the_person "Hmm, you're really trying to charm me, aren't you? Well, I'll tell you what... If you can make me laugh and cum, I might consider it."
                "She smiles mischievously, clearly enjoying the challenge and the flirting."

    else:
        if mc.location.person_count == 1: #You're alone, so she just didn't meet the sluttiness threshold
            the_person "Hmm, you're really eager, aren't you? Well, I suppose it's just the two of us here... and I'm feeling a little horny and ready to breed."
            "[the_person.possessive_title!c] glances around, confirming you're alone and safe to breed."
            the_person "So what's your plan? Are you going to breed with me or just tease me some more?"

        else:  # You aren't alone but she's still into it.
            the_person "Feeling bold today, huh? Well, I think your chances are pretty good... especially since I'm feeling a little horny and ready to breed."
            "[the_person.title] smirks, clearly enjoying the attention and the flirting."
            if the_person.has_large_tits: #Bounces her tits for you
                $ mc.change_locked_clarity(15)
                "[the_person.title] grabs her tits and jiggles them for you, her nipples hardening and poking out of her top."
                the_person "Maybe I can get these girls out for you. Does that sound nice? Do you want to see my tits and breed with me?"

            else: #No big tits, so she can't bounce them (as much)
                "[the_person.title] runs her hands over her hips sensually, obviously encouraging you to take things further and breed with her."

        menu:
            "Touch her" if not the_person.is_willing(kissing):
                "You step closer to [the_person.title] and move your hands down her waist, your fingers brushing against her skin."
                if the_person.has_taboo("touching_body"):
                    the_person "Oh, you're brave. I like that. Maybe you can even make me cum and breed with me."
                    $ the_person.call_dialogue("touching_body_taboo_break")
                    $ the_person.break_taboo("touching_body")

                call fuck_person(the_person, start_position = standing_grope, private = False) from _call_fuck_person_flirt_response_breeder_touching

            "Kiss her" if the_person.is_willing(kissing):
                $ the_person.draw_person()
                if the_person.has_taboo("kissing"):
                    "You put your arm around [the_person.possessive_title!c] and lean in close, your lips brushing against hers."
                    $ the_person.call_dialogue("kissing_taboo_break")
                    $ the_person.break_taboo("kissing")
                    "She responds with a passionate kiss, her arms wrapping around your neck and pulling you in for a deeper kiss."
                else:
                    "You pull [the_person.possessive_title!c] close and kiss her, your tongues touching and exploring each other's mouths."
                    "She responds with a passionate kiss, her arms wrapping around your neck and pulling you in for a deeper kiss."

                call mc_move_to_private_location(the_person) from  _call_mc_move_to_private_location_breeder_flirt_response_high
                call fuck_person(the_person, start_position = kissing, private = _return, skip_intro = True) from _vt_breeder_call_fuck_person_50
                $ the_person.call_dialogue("sex_review", the_report = _return)
                call mc_restore_original_location(the_person) from _call_mc_restore_original_location_breeder_flirt_response_high

            "Just flirt":
                $ the_person.draw_person()
                mc.name "Very tempting, but you're going to have to contain yourself for now. Maybe later we can breed and make some babies."
                the_person "Oh, you're not going to take advantage of me right now, are you? Fine, be that way. But I'm still going to tease you and make you want to breed with me."
                "[the_person.title] pouts, clearly enjoying the flirtation and the teasing."
    return

label breeder_flirt_response_low_energy(the_person):
    if the_person.sluttiness > 40:
        the_person "Hmph, thanks for the compliment, but I'm exhausted right now. I need a good breeding session to perk me up, but I don't think I have the energy for it."
        "[the_person.title] yawns and stretches, her body aching for a good breeding."
    else:
        the_person "Thanks, but I'm beat. Can we pick this up later? Maybe after I've had a chance to rest and recharge my breeding batteries."
        "[the_person.title] smiles weakly and leans against something, her body craving a good breeding but lacking the energy."
    return

label breeder_flirt_response_girlfriend(the_person):
    # Lead in: mc.name "You're so beautiful [the_person.title], I'm so lucky to have a woman like you in my life."
    if mc.location.person_count > 1:
        # There are other people around, so she'll only start making out with you if she's slutty.
        if the_person.effective_sluttiness("kissing") < (25 - (5*the_person.opinion.public_sex)):
            # Not very slutty, so she wants to find somewhere private
            the_person "Oh my god, you're so cheesy. But I love it. Come here and breed with me."
            "She pulls you against her and kisses you, her lips soft and gentle as she grinds against you."
            the_person "There, now you can't say I don't know how to kiss... or breed."
            mc.name "Haha, yeah I guess not... You're so wet for me already."
            "You put your arms around her and kiss her back, feeling her warmth and breeding potential."
            the_person "Mmm, yeah, like that. I love it when you touch me like that."
            menu:
                "Find somewhere more quiet\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                    mc.name "Why wait? Come on, I'm sure we can find somewhere quiet and private to breed."
                    the_person "You're always so eager, aren't you? Alright, let's go and make some babies!"
                    "You and [the_person.possessive_title!c]] hurry off, searching for a private spot to breed."
                    call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_breeder_flirt_response_girlfriend_2
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _vt_breeder_call_fuck_person_76
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_breeder_flirt_response_girlfriend_2

                "Just flirt":
                    $ mc.change_locked_clarity(10)
                    "You reach around and pull her closer, running your hand down her back and grabbing her ass."
                    mc.name "You're so beautiful, and you know it. And I know you're ready to breed."
                    "She rolls her eyes but leans in for a quick kiss, her tongue touching yours."
                    the_person "Fine, you caught me. But don't think this means I'm going easy on you. I want to breed with you, but I want it to be rough and wild."

        else:
            the_person "Well if I'm so beautiful, then why are you just standing there? Come on, kiss me and breed with me!"
            "You put your arm around her waist and pull her close, kissing her deeply and grinding against her."
            "When you break the kiss, [the_person.possessive_title!c]] sighs and leans against you, her body aching for more breeding."
            the_person "You're not so bad yourself... But I think you could be better, with a little more practice breeding with me."
            menu:
                "Make out":
                    "You lean back in and kiss her again, this time more passionately and with more breeding intent."
                    "[the_person.title] responds eagerly, wrapping her arms around your neck and pulling you in for a deeper kiss and more breeding."

                    call mc_move_to_private_location(the_person) from  _call_mc_move_to_private_location_breeder_flirt_response_girlfriend
                    call fuck_person(the_person, start_position = kissing, private = _return, skip_intro = True) from _vt_breeder_call_fuck_person_77
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_breeder_flirt_response_girlfriend

                "Just flirt":
                    mc.name "I'm not bad? You're the one who's hard to resist, with your beautiful body and breeding potential."
                    $ mc.change_locked_clarity(10)
                    "You reach out and touch her cheek, a playful grin on your face as you imagine breeding with her."
                    the_person "Ugh, you're so annoying. But I guess I like that about you... And I love the way you make me feel when we breed."

    else:
        # You're alone, so she's open to fooling around and breeding.
        the_person "Well you've got me all alone, so how about you show me just how lucky you feel... and how much you want to breed with me?"
        "She reaches down to your waist and cups your crotch, rubbing it gently and teasing you into breeding with her."
        mc.name "You're so wet for me already, and I can tell you're ready to breed."
        the_person "Hmph, maybe. But I want to make sure you're ready too, and that you can handle my breeding needs."
        "She grinds against you, her hips moving in a slow circle as she teases you."
        mc.name "Damn, you feel so good. I love the way you move your body when we breed."
        "You reach up and grab her breasts, squeezing them gently and playing with her nipples as you imagine breeding with her."
        the_person "Ooh, don't do that. But at the same time, don't stop. I love the way you touch me when we breed."
        "But she doesn't pull away, her body still pressed against yours and aching for more breeding."
        menu:
            "Kiss her":
                if the_person.has_taboo("kissing"):
                    $ the_person.call_dialogue("kissing_taboo_break")
                    $ the_person.break_taboo("kissing")

                "You put your arms around [the_person.possessive_title!c]]'s waist and rest your hands on her ass. You pull her close and kiss her sensually."
                "She responds by pressing her body against you and grinding her hips against your thigh, her body aching for more ."
                "You grab her hips and pull her closer, your crotches pressed together as you imagine breeding with her."
                call fuck_person(the_person, start_position = kissing, skip_intro = True) from _vt_breeder_call_fuck_person_78
                $ the_person.call_dialogue("sex_review", the_report = _return)
                $ the_person.review_outfit()

            "Just flirt":
                mc.name "I'm going to make you beg for it, and beg for my sperm to fill your womb."
                "You lean in close, your breath hot against her ear as you whisper sweet nothings and breeding intentions into it."
                the_person "Ooh, you're such a bad boy. I love it when you talk dirty and breed with me."
                "She rubs her body against yours, her hips moving seductively as she teases you into breeding with her."
                the_person "But don't think you're getting off that easy. I'm going to make you work for it, and prove your breeding worth to me..."
    return

label breeder_flirt_response_affair(the_person):
    # Lead in: mc.name "You look so good today [the_person.title], you're making me want to do some very naughty things to you... like breeding with you all day."
    if mc.location.person_count > 1: #There are other people around, she's nervous about people finding out what you're doing.
        if (the_person.opinion.cheating_on_men *15) + the_person.effective_sluttiness() > 50: #SHe's turned on by flirting in public or doesn't think anything is wrong with it
            "[the_person.possessive_title!c] blushes and playfully bats her eyes at you, her pussy aching for your attention."
            the_person "Oh, you're making me blush... and horny. I'm not used to this kind of attention from you, but I have to admit, I'm curious."
            the_person "But I have to admit, I'm curious. What do you have in mind... for breeding and making babies?"
            menu:
                "Find somewhere more quiet\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                    mc.name "I was thinking we could slip away and find a more private spot... where we can breed in peace."
                    "You and [the_person.title] exchange a flirtatious glance before hurrying off to find a quiet spot."
                    call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_breeder_flirt_response_affair
                    $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
                    "As soon as you're alone she pulls you into a deep and passionate kiss, her tongue touching yours and inviting you to breed with her."
                    $ the_person.draw_person(position = "kissing")
                    the_person "Mmm... I've been wanting to do that for a while now... and I've been wanting to breed with you even more."
                    "You wrap your arms around her waist and kiss her back, your crotches pressed together as you imagine breeding with her."
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _vt_breeder_call_fuck_person_79
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_breeder_flirt_response_affair

                "Just flirt":
                    mc.name "I 'can't help but notice' how beautiful you look today, [the_person.title]. You're 'making me hard' just thinking about breeding with you."
                    the_person "Stop it, you're 'making me blush'! But I have to admit, you look pretty great yourself... and I can tell you're 'ready to breed' with me."
                    the_person "Just don't get too 'cocky', okay? I'm still in charge here... and I'm still the one who decides who breeds with me."
                    $ mc.change_locked_clarity(20)
                    "[the_person.possessive_title!c] playfully swats at your arm before leaning in close and whispering in your ear."
                    the_person "But I have to admit, I'm getting a little 'turned on' by this whole thing... and I'm getting a little 'wet' thinking about breeding with you."
                    "You can't help but feel a little flustered as she teases you and invites you to breed with her."
                    mc.name "I can see that. Maybe we should find a more private place to continue this... and maybe we can even breed in private."
                    the_person "Mmm, maybe we should. But first, let's enjoy this little moment here... and let's enjoy the 'anticipation' of breeding together."

        else: #She's shy or nervous about being discovered
            "[the_person.possessive_title!c] looks around nervously, then back at you with a sheepish grin."
            the_person "Oh, um, you look nice today. I guess I should probably get going though... before someone sees us and thinks we're breeding in public."
            mc.name "Wait, don't go! I was thinking we could... uh, grab a drink or something... and maybe even breed in private."
            $ mc.change_locked_clarity(15)
            the_person "Oh, you want to grab a drink? Okay, sure. But just for a little bit, okay? I don't want to be out too late... and I don't want to be caught breeding in public."
            "She glances around again, then leans in close and whispers in your ear."
            the_person "And just so you know, I'm still in charge here, even if we're just grabbing a drink... and even if we're breeding in private."
            "You can't help but feel a little excited by her assertiveness and breeding potential."
            mc.name "Okay, okay. I'll behave... and I'll make sure to breed with you in private."

    else:
        # the_person "Yeah? Well there's nobody around, and I'm not going to stop you... from breeding with me."
        the_person "Oh yeah? Well then, do you want to share what all of these naughty things are? You have my attention... and you have my breeding interest."
        menu:
            "Feel her up":
                "You put your arms around [the_person.possessive_title!c]'s waist and rest your hands on her ass, massaging it gently and inviting her to breed with you."
                mc.name "You know, I've been waiting for this moment for a while now... and I've been waiting to breed with you for even longer."
                "You squeeze her butt and pull her close, your crotches pressed together as you imagine impreginating her."
                the_person "Hey, no need to be so 'forward'! What's gotten into you... and what's making you so 'horny' for breeding?"
                "You pull her close again and shift your hands to her breasts, squeezing them gently and inviting her to breed with you."
                mc.name "Come on, don't be like that. I just wanted to make you feel good for once... and I just wanted to breed with you for once."
                call fuck_person(the_person, private = True, start_position = standing_grope, skip_intro = True) from _vt_breeder_call_fuck_person_80
                $ the_person.call_dialogue("sex_review", the_report = _return)
                $ the_person.review_outfit()

            "Just flirt":
                $ mc.change_locked_clarity(10)
                "You put your arms around [the_person.possessive_title!c]'s waist and rest your hands on her ass, massaging it gently and inviting her to breed with you."
                mc.name "I wish I had the time... to breed with you all day and make babies with you."
                "You massage her butt and pull her close, your crotches pressed together as you imagine breeding with her."
                the_person "Aww, are you sure? I was really looking forward to breeding with you... and I was really looking forward to making babies with you."
                "You slap her ass and step back, your dick hard and ready to penetrate her."
                the_person "Fine, but don't make me wait too long, okay? I have 'needs', and my [the_person.so_title] sure as hell isn't 'fulfilling' them... and I need to breed with someone who can fulfill my needs."
                mc.name "I won't make you wait long. I promise... to breed with you and make babies with you."
                "She looks up at you with a playful pout, her eyes sparkling with desire and breeding interest."
                the_person "Good. Because I'm not sure I can handle it if you do... and I'm not sure I can handle not breeding with you."
    return

label breeder_flirt_response_text(the_person):
    mc.name "Hey [the_person.title], how's it going? I'm feeling a bit bored and thought we could chat... and maybe even breed."
    "She replies with a hint of annoyance, but also a hint of breeding interest, as she tosses her hair and bats her eyelashes at you."

    if the_person.is_affair:
        the_person "Oh, great, you're bored again? You always seem to find ways to bother me... and always seem to want to breed with me."
        "She sighs and rolls her eyes, but you can see the desire in her eyes as she thinks about breeding with you."
        the_person "Well, what do you want this time? I'm not exactly thrilled about entertaining you... but I have to admit, I'm a little wet thinking about breeding with you."
        "She leans in close and whispers in your ear, her breath hot against your skin."
        the_person "When can we get together and make some babies?"
        mc.name "Some time soon. I'll let you know... and I'll make sure to bring my A-game and plenty of sperm."
        "She smirks and winks at you, her eyes sparkling with desire and breeding interest."

    elif the_person.is_girlfriend:
        the_person "Bored, huh? That's not exactly a surprise. You're always looking for something new to entertain yourself... and always looking for new ways to breed with me."
        "She giggles and plays with her hair, her body language open and inviting as she thinks about breeding with you."
        the_person "But fine, we can hang out... and maybe even breed. Just don't expect me to do anything special, except maybe get pregnant with your baby."
        "She leans in close and kisses you, her tongue touching yours and inviting you to breed with her."
        mc.name "Some time soon. I'll let you know... and I'll make sure to bring my A-game and plenty of sperm."
        "She smiles and nods, her eyes shining with excitement and breeding interest."

    elif the_person.love < 40:
        if the_person.effective_sluttiness() > the_person.love:
            the_person "Ugh, bored, really? Well, I suppose I can keep you company for a bit... and maybe even breed with you if you're lucky."
            "She sighs and shrugs, but you can see the desire in her eyes as she thinks about breeding with you."
        else:
            the_person "Bored, eh? That's not surprising. You're always looking for a new distraction... and always looking for a new breeding partner."
            "She smirks and raises an eyebrow, her body language teasing and inviting as she thinks about breeding with you."

    else:
        if the_person.effective_sluttiness() > the_person.love:
            the_person "Fine, I'll talk to you... and maybe even breed with you if you're lucky. But don't think this means I'm happy about it."
            "She pouts and crosses her arms, but you can see the desire in her eyes as she thinks about breeding with you."
            "She leans in close and whispers in your ear, her breath hot against your skin."
            the_person "So, what do you want to talk about? I'm not exactly thrilled about this... but I have to admit, I'm a little curious about breeding with you."
        else:
            the_person "You're bored, huh? Well, that's your problem, not mine... but I have to admit, I'm a little interested in breeding with you and making some babies."
            "She smirks and winks at you, her eyes sparkling with desire and breeding interest."
            the_person "So, what do you want? Just don't expect me to be all lovey-dovey about it... but do expect me to be all about breeding and making babies with you."
            "She leans in close and kisses you, her tongue touching yours and inviting you to breed with her."
    return

label breeder_condom_demand(the_person):
    if the_person.wants_creampie:
        the_person "Ugh, seriously? You need to put on a condom before we even think about breeding... I mean, before we even think about making love."
        "She sighs and rolls her eyes, but you can see the desire in her eyes as she thinks about breeding with you."
        the_person "I hate that we have to, but you know it's necessary... I don't want to get pregnant with your baby just yet."
        "She pouts and crosses her arms, but you can see the lust in her eyes as she thinks about breeding with you."
    else:
        the_person "For crying out loud, do you have a condom on you? Put one on before you even think about touching me... before you even think about breeding with me."
        "She scowls and folds her arms, her body language closed off and uninviting as she thinks about breeding with you."
        the_person "I don't want to be stuck with some stupid disease because you were too careless... and I don't want to get pregnant with your baby without planning it."
        "She glares at you, her eyes flashing with anger and frustration as she thinks about breeding with you."
    return

label breeder_condom_ask(the_person):
    if the_person.on_birth_control:
        the_person "You want a condom? Fine, but I'm on the pill, so it's not like I really need it... and it's not like I'm going to get pregnant with your baby anytime soon."
        "She shrugs and smirks, her body language relaxed and teasing as she thinks about breeding with you."
        $ the_person.update_birth_control_knowledge()
    elif the_person.wants_creampie:
        the_person "Ugh, you want to cum inside me? Just put on a condom, would you? It's not like I want to get pregnant or anything... but at the same time, it's kind of hot thinking about your sperm filling me up."
        "She blushes and looks away, her body language flustered and aroused as she thinks about breeding with you."
        the_person "But I guess it's better than the alternative, right? I mean, who needs a baby when you can just have a good creampie?"
        "She giggles and winks at you, her eyes sparkling with mischief and breeding interest."
        $ the_person.discover_opinion("creampies")
    else:
        the_person "Fine, I guess you should use a condom... but can you at least not make a mess with it? I don't want to clean up after you... and I don't want to get pregnant with your baby without planning it."
        "She sighs and rolls her eyes, her body language exasperated and uninviting as she thinks about breeding with you."
        the_person "And please, no pulling out method. That's just asking for trouble... and that's just asking for a baby."
        "She shudders and shakes her head, her body language disgusted and uninterested in the idea of breeding without protection."
    return

label breeder_condom_bareback_ask(the_person):
    if the_person.wants_creampie:
        if the_person.is_infertile:
            the_person "You're not seriously considering a condom, are you? Please, just unload your cum inside me and make me scream with pleasure."
            "She spreads her legs and invites you to breed with her, her pussy aching for your hot, sticky load."
            the_person "I want to feel you fill me up and make me beg for more... and I want to feel your cum dripping out of me for hours after we're done."
        elif the_person.on_birth_control:
            the_person "Don't even think about putting a condom on, [the_person.mc_title]. I'm on the pill, so we're good to go and ready to breed."
            "She smirks and winks at you, her eyes sparkling with mischief and breeding interest."
            the_person "Just fuck me raw and make me feel every inch of you... and make me cum so hard I scream your name."
            $ the_person.update_birth_control_knowledge()
        else:
            the_person "Forget the condom, [the_person.mc_title], I want to feel you deep inside me and making me pregnant."
            "She leans in close and whispers in your ear, her breath hot against your skin."
            the_person "I don't care about the risks, it's worth it for this kind of pleasure and breeding excitement."
            if not the_person.knows_pregnant:
                the_person "Imagine how hot it would be to get knocked up and carrying your baby... and imagine how proud you'll be when you see me showing off my baby bump."
        $ the_person.discover_opinion("creampies")
    else:
        the_person "Don't bother with a condom, [the_person.mc_title]. I want to feel you raw and unprotected... and I want to feel your cum dripping out of me for hours after we're done."
        if not the_person.knows_pregnant:
            the_person "I don't care about the risks, it's worth it for the intensity and breeding excitement... and it's worth it to make a baby with you."
        else:
            the_person "I love it when you fuck me raw and make me feel like I'm yours... and I love it when you cum inside me and make me pregnant with your baby."
    return

label breeder_condom_bareback_demand(the_person):
    if the_person.has_breeder_fetish: #Actively looking to get knocked up.
        if the_person.knows_pregnant:
            the_person "Ugh, why bother with a condom? I want to get knocked up and carrying your baby... and I want to feel your hot cum filling me up and making me pregnant!"
            "She spreads her legs and invites you to breed with her, her pussy aching for your raw cock."
            the_person "Hurry up, I 'can't wait to feel you inside me and making me cum... and I can't wait to see my baby bump and know that I'm carrying your baby!"
        elif the_person.is_infertile:
            the_person "Oh, great, you're going to remind me I can't get pregnant? Thanks a lot... but that doesn't mean we can't fuck raw and make me feel good!"
        else:
            the_person "Ugh, what's the point of fucking if you're not going to knock me up and make me pregnant?"
            "She pouts and crosses her arms, but you can see the desire in her eyes as she thinks about breeding with you."
            the_person "Hurry up and give me that cock! I need to feel you inside me and making me cum... and I need to feel your hot cum filling me up and making me pregnant!"

    elif the_person.wants_creampie: #Just likes raw sex
        if the_person.is_infertile:
            the_person "Ugh, why bother with a condom? I can't get pregnant anyway... but that doesn't mean we can't fuck raw and make me feel good!"
        elif the_person.on_birth_control:
            the_person "Forget the condom, [the_person.mc_title]. I'm on the pill, so it's not a problem... and I'm ready to breed and make some babies!"
            "She smirks and winks at you, her eyes sparkling with mischief and breeding interest."
            the_person "Take me bareback and make me scream... and take me raw and make me feel every inch of you!"
            $ the_person.update_birth_control_knowledge()
        else:
            the_person "Ugh, condoms are so annoying. Just get inside me already and make me feel good... and just fuck me raw and make me cum!"

    else:
        if the_person.is_infertile:
            the_person "Take me bareback, [the_person.mc_title]. It's not like I can get pregnant... but that doesn't mean we can't fuck raw and make me feel good!"
            "She shrugs and smirks at you, her body language relaxed and teasing as she thinks about breeding with you."
            the_person "Just make me feel good and make me cum... and just fuck me raw and take me bareback!"
        elif the_person.on_birth_control:
            the_person "Forget the condom, [the_person.mc_title]. I'm on the pill... and I'm ready to breed and make some babies!"
            "She smirks and winks at you, her eyes sparkling with mischief and breeding interest."
            the_person "Take me bareback and make me feel every inch of you... and take me raw and make me scream!"
            $ the_person.update_birth_control_knowledge()
        else:
            the_person "Ugh, condoms are so annoying. Just get inside me already and make me feel good... and just fuck me raw and make me cum!"
            "She pouts and crosses her arms, but you can see the desire in her eyes as she thinks about breeding with you."
            the_person "I need to feel you inside me and making me cum... and I need to feel your hot cum filling me up and coating my eggs!"
    return

label breeder_cum_face(the_person):
    if the_person.has_cum_fetish or the_person.obedience > 180:
        if the_person.has_cum_fetish or the_person.effective_sluttiness() > 60 or the_person.opinion.cum_facials > 0:
            the_person "So, do you think this is a good look for me, [the_person.mc_title]? Do I look like a breeding queen, covered in your cum?"
            "[the_person.title] smirks and licks her lips, then runs a finger through your semen, bringing it to her mouth and tasting it."
            the_person "Mmm, taste your victory... and taste your cum. I love the way you cum all over my face and make me feel like a breeding queen."
            "[the_person.title] smirks and winks at you, her eyes sparkling with mischief and breeding interest."
        else:
            the_person "Hmph, I suppose it's not a terrible look. But I'm glad we're done here... and I'm glad I got to feel your cum on my face."
            "[the_person.title] wipes away some of your semen from her face, looking annoyed but also aroused."

    else:
        if the_person.effective_sluttiness() > 80 or the_person.opinion.cum_facials > 0:
            the_person "Well, I guess this is one way to end things... with a cum facial and a breeding session."
            "[the_person.title] smirks and laughs, then wipes away some of your semen from her face and looks up at you with lust in her eyes."
            the_person "Do you think I look good like this? Do I look like a breeding queen to you?"
        else:
            the_person "Ugh, just get that over with already... and don't think you're getting a second chance to breed with me."
            "[the_person.title] wipes away your semen, looking put off and uninterested in further breeding activities."
            the_person "I am saddened by all the loss of your children on my face..."
    return

label breeder_cum_mouth(the_person):
    if the_person.has_cum_fetish or the_person.obedience > 180:
        if the_person.has_cum_fetish or the_person.effective_sluttiness() > 60 or the_person.opinion.drinking_cum > 0:
            the_person "Mmm, that's so... intoxicating [the_person.mc_title]. Your cum is like a fine wine to me."
            "[the_person.title] closes her eyes and savours the taste of your cum, her tongue dancing across her lips as she swallows it down."
            the_person "You really know how to make me feel like a breeding queen... and you really know how to make me cum hard."
        else:
            "[the_person.title]'s face twists in disgust as she swallows your cum, her eyes watering at the taste."
            the_person "Ugh, there, done. Don't think I enjoyed that one bit... but I'll do it again if it means I get to breed with you."

    else:
        if the_person.effective_sluttiness() > 80  or the_person.opinion.drinking_cum > 0:
            the_person "Mmm, you're quite the stud, [the_person.mc_title]. Your cum is like a fountain of youth to me."
            "[the_person.title] smirks and winks at you, her eyes sparkling with mischief and breeding interest."
            the_person "I can see why you're so popular... and I can see why you're so good at breeding."
        else:
            the_person "Ugh, that's... quite a taste. I hope you're happy... but I'm not sure I am."
            "[the_person.title] makes a face and spits out some of your cum, her tongue flicking out to clean her lips."
            the_person "Ugh, to think I ate some of our potential babies..."
    return

label breeder_cum_pullout(the_person):
    if mc.condom:
        if the_person.wants_creampie and not the_person.has_taboo("condomless_sex"):
            if the_person.knows_pregnant:
                the_person "Tear that condom off and unleash your seed inside me! I crave the feeling of your hot cum gushing into my womb!"
                "She wraps her legs around your hips, pulling you deeper into her."
                the_person "I'm beyond caring about consequences, I just want you to breed me like a wild animal!"
                "She bucks her hips, grinding against you as she begs for your cum."
            elif the_person.on_birth_control:
                the_person "For the love of all things filthy... Remove that condom and grant me the creampie I've been begging for, [the_person.mc_title]!"
                "She shudders, her body convulsing with anticipation as she reaches down to stroke your cock."
                the_person "I submit to your desires, fill me up with your cum and make me scream with pleasure!"
                "She tilts her head back, exposing her neck as she prepares to take your load."
            else:
                "She's lost in the heat of the moment, her eyes glazing over with lust."
                the_person "I don't care about anything except feeling your cum inside me, you dirty breeder!"
                $ the_person.update_birth_control_knowledge()
                the_person "I want you to make me cum and then impregnate me, you filthy stud!"
                "She wraps her arms around your neck, pulling you down into a passionate kiss as she begs for your seed."
            menu:
                "Take off the condom":
                    "You rip the condom off, barely clearing her pussy, and prepare to unleash your load."
                    $ mc.condom = False
                    $ use_condom = False
                    "You feel a surge of excitement as you prepare to cum inside her, her eyes locked on yours with anticipation."
                "Leave it on":
                    "You ignore [the_person.possessive_title!c]'s pleas and keep the condom firmly in place, teasing her with denial."
                    "She pouts, her face twisted in frustration as she realizes she won't get the creampie she desires."
        else:
            the_person "I'll make you cum so hard, you'll be begging for mercy... and then I'll take your seed inside me!"
            "She grins, her eyes sparkling with mischief as she reaches down to stroke your cock."
    else:
        if the_person.wants_creampie:
            if the_person.knows_pregnant:
                the_person "Creampie me, you dirty breeder, and make me cum like a wild animal!"
                "She spreads her legs wide, exposing her pussy as she begs for your cum."
                the_person "I want to feel your seed gushing into my womb, filling me up with your hot cum!"
                "She bucks her hips, grinding against you as she takes your load."
            elif the_person.opinion.creampies > 0:
                "[the_person.possessive_title!c] is in a state of pure ecstasy, her body writhing with pleasure."
                if the_person.on_birth_control:
                    the_person "Fill me up with your cum, [the_person.mc_title]! I want to feel it dripping out of my pussy, a constant reminder of your dominance!"
                    "She tilts her head back, exposing her neck as she prepares to take your load."
                else:
                    $ the_person.update_birth_control_knowledge()
                    the_person "Cum inside me and knock me up, [the_person.mc_title]! I want to be your breeding vessel, your personal cumdump!"
                    "She wraps her arms around your neck, pulling you down into a passionate kiss as she begs for your seed."
            elif the_person.is_infertile:
                the_person "Cum wherever you want, you dirty breeder, I'm barren and ready to be used!"
                "She grins, her eyes sparkling with mischief as she reaches down to stroke your cock."
            elif the_person.on_birth_control:
                $ the_person.update_birth_control_knowledge()
                the_person "Cum wherever you want, you dirty breeder, I'm on the pill, so I'm ready to take your seed!"
                "She spreads her legs wide, exposing her pussy as she begs for your cum."
            else:
                the_person "Just do it! Cum inside me and make me scream with pleasure, you filthy stud!"
                "She bucks her hips, grinding against you as she takes your load."
        else:
            if the_person.is_infertile:
                the_person "Pull out, you dirty breeder! I don't want your cum inside me, even if it won't do any harm... but I still want to feel your seed on my skin."
                "She pouts, her face twisted in frustration as she realizes she won't get the creampie she desires."
            elif not the_person.on_birth_control:
                $ the_person.update_birth_control_knowledge()
                the_person "Fuck, pull out! I'm not on the pill, and I don't want to get knocked up... but I still crave your cum!"
                "She grins, her eyes sparkling with mischief as she reaches down to stroke your cock."
            elif the_person.opinion.creampies < 0:
                the_person "Pull out, you dirty breeder! I don't want your cum inside me, it's disgusting... but I'll still take it on my skin."
                "She wrinkles her nose in distaste, but still reaches down to stroke your cock."
            else:
                the_person "Hell yeah, pull out and cum all over me like a filthy slut! I want to be covered in your seed, to feel it dripping down my skin!"
                "She spreads her legs wide, exposing her pussy as she begs for your cum."
    return

label breeder_cum_condom(the_person):
    if the_person.effective_sluttiness() > 75 or the_person.opinion.creampies > 0:
        the_person "Mmmm, I can feel your cum straining against the condom, begging to be unleashed inside me."
        "She wraps her legs around your hips, pulling you deeper into her as she fantasizes about getting pregnant."
        the_person "If only the condom would break, I'd be filled to the brim with your hot seed, and I'd be carrying your child in no time."
        "She bucks her hips, grinding against you as she imagines the feeling of your cum flooding her womb."
    else:
        the_person "Oh my, that's quite a load you're packing. I hope your condoms are up to the task of containing it all."
        "She raises an eyebrow, a sly smile spreading across her face as she teases you about your virility."
        the_person "But then again, maybe you're secretly hoping to knock me up, to fill me with your cum and make me your breeding vessel."
        "She leans in close, her voice taking on a sultry tone as she whispers in your ear."
        the_person "I have to admit, the thought of carrying your child is a tantalizing one. Maybe we'll have to try that sometime... without the condom, of course."
    return

label breeder_cum_vagina(the_person):
    if the_person.has_taboo("creampie"):
        $ the_person.call_dialogue("creampie_taboo_break")
        $ the_person.break_taboo("creampie")
        return
    if the_person.wants_creampie:
        if the_person.knows_pregnant:
            the_person "Ahhh, your cum feels so divine inside me... I can feel it spreading through my womb, nourishing our growing child."
            "She wraps her arms around your neck, pulling you into a tender kiss as she revels in the sensation of your cum filling her."
        elif the_person.is_infertile:
            the_person "Mmmm, your cum is like liquid gold... I can feel it dripping out of my pussy, a constant reminder of our passionate encounter."
            "She spreads her legs wide, exposing her glistening pussy as she invites you to admire your handiwork."
        elif the_person.on_birth_control:
            if the_person.has_significant_other:
                the_person "Well, well, well... Look at you go! I guess it's a good thing I'm on the pill, huh? Or maybe I'll just tell [the_person.SO_name] that it was someone else's... Ugh, why do you have to be so frustrating?"
                "She rolls her eyes, a sly smile spreading across her face as she teases you about your virility."
            else:
                the_person "Oh my, that's quite a load you've deposited inside me... I can feel it dripping out of my pussy, a constant reminder of our breeding session."
                $ the_person.update_birth_control_knowledge()
                "She tilts her head back, exposing her neck as she invites you to claim her as your breeding vessel."
        elif the_person.effective_sluttiness() > 75 or the_person.opinion.creampies > 0:
            the_person "Ahhh, your cum feels so good inside me... I can feel it spreading through my womb, filling me with your seed."
            "She wraps her arms around your neck, pulling you into a passionate kiss as she begs for more of your cum."
        else:
            the_person "Wow... I guess I didn't expect that from you. But I have to admit, it was kind of nice... Just don't get any ideas, okay? I'm not ready for anything serious."
            "She blushes, a shy smile spreading across her face as she tries to downplay her enjoyment of your cum."
    else: #She's angry
        if the_person.knows_pregnant:
            the_person "Ugh, what is wrong with you? I specifically told you not to do that! Oh well, since I'm already pregnant..."
            "She rolls her eyes, a scowl spreading across her face as she chastises you for your lack of self-control."
        elif not the_person.on_birth_control:
            if the_person.has_significant_other:
                the_person "Oh, great. Just what I needed. You forgot to pull out, and now I'm going to have to deal with [the_person.SO_name]'s anger."
                if the_person.kids > 0:
                    the_person "... Again."
                "She sighs, a frustrated expression spreading across her face as she contemplates the consequences of your actions."
            else:
                the_person "Oh fuck, I said to pull out! I'm not on the pill [the_person.mc_title], what happens if I get pregnant?"
                $ the_person.update_birth_control_knowledge()
                the_person "What is wrong with you? You know I'm not on the pill! Now look what you've done... I guess next time we'll have to use a condom."
                "She shakes her head, a disapproving expression spreading across her face as she chastises you for your lack of responsibility."
        elif the_person.is_infertile:
            the_person "Unbelievable! I told you to pull out, and now you've gone and made a mess... What a pain in the ass..."
            "She scowls, a frustrated expression spreading across her face as she contemplates the inconvenience of your actions."
        elif the_person.has_significant_other:
            the_person "You're really going to make me tell [the_person.SO_name] about this, aren't you? Fine, I'll deal with it. Just be more careful next time."
            $ the_person.update_birth_control_knowledge()
            the_person "I don't want to have to make you wear a condom, so be a little more careful next time."
            "She raises an eyebrow, a warning expression spreading across her face as she cautions you against future mistakes."
        elif the_person.opinion.creampies < 0:
            the_person "Oh, great. Just what I needed. You couldn't even follow a simple instruction, could you? Now look at what a mess you've made..."
            "She shakes her head, a disapproving expression spreading across her face as she chastises you for your lack of self-control."
        else:
            the_person "You really need to work on your timing. I told you to pull out, not do the exact opposite!"
            the_person "Just remember, I'm not going to be as forgiving next time if you can't follow simple instructions."
            "She scowls, a frustrated expression spreading across her face as she warns you against future mistakes."
    return

label breeder_cum_anal(the_person):
    if the_person.has_taboo("anal creampie"):
        $ the_person.call_dialogue("anal_creampie_taboo_break")
        $ the_person.break_taboo("anal creampie")
        return

    if the_person.sluttiness > 75 or the_person.opinion.anal_creampies > 0:
        the_person "Mmmm, I can feel your cum dripping out of my ass... It's like a warm, gooey sensation spreading through my body."
        "She arches her back, exposing her anus as she invites you to admire your handiwork."
    elif the_person.opinion.anal_creampies < 0:
        the_person "Oh, for fuck's sake... not in my ass! I don't need to be degraded like that!"
        "She scowls, a look of disgust spreading across her face as she chastises you for your actions."
    else:
        the_person "Well, I suppose it's not every day I get to experience something like this... But don't think I'm going to start asking for it all the time, got it?"
        "She raises an eyebrow, a hint of curiosity in her voice as she explores the sensation of your cum in her ass."
    return

label breeder_surprised_exclaim(the_person):
    $rando = renpy.random.choice(["What the actual fuck?", "Ugh, are you kidding me?", "Why now, of all times?", "This again? Seriously?", "Not again, please!", "You've got to be joking!", "Great, just what I needed...", "Oh, joy... just peachy...", "Fucking perfect... just what I wanted...", "Unbelievable! You're really something else...", "Not again! Can't a girl catch a break around here?", "Why can't I just have a normal day for once?"])
    the_person "[rando]"
    return

label breeder_talk_busy(the_person):
    if the_person.obedience > 120:
        the_person "Listen, I don't have time for your games right now. I've got more important things to attend to, [the_person.mc_title]."
        "She dismisses you with a wave of her hand, her expression stern and unyielding."
    else:
        the_person "Hey, I'd love to chat, but I'm swamped with work right now. Can we catch up later, maybe over dinner or something?"
        "She smiles, a hint of apology in her voice as she puts you off until later."
    return

label breeder_sex_strip(the_person):
    if the_person.sluttiness < 20:
        if the_person.arousal_perc < 50:
            the_person "Fine, I'll undress... but don't think for a second I'm doing this for your benefit. I just need to get comfortable, that's all."
            "She slowly begins to remove her clothes, her movements hesitant and uncertain."
            mc.name "Come on, relax. It's just us here. You can let your guard down."
            the_person "I don't trust you. And don't try to sweet-talk me, it won't work."
            mc.name "Okay, okay. I'll back off. Just take your time, okay?"
            "She shoots you a suspicious glance, but continues to undress, her movements slow and deliberate."
        else:
            the_person "Alright, alright... I'll take off a few things. But don't expect me to be impressed by your reaction. I'm just undressing, big deal."
            "She begins to remove her clothes, her movements a little more confident now, but still hesitant."
            mc.name "Aww, come on. You're being a little rough. Just let me see you a little more, okay?"
            the_person "Fine, but only because you asked nicely. And don't think this means I'm interested in you or anything."
            "She gives you a small smile, but it's clear she's still not comfortable with the situation."
    elif the_person.sluttiness < 60:
        if the_person.arousal_perc < 50:
            the_person "Fine, I'll make an exception and get a little more comfortable. But don't get any ideas, okay?"
            "She begins to remove her clothes, her movements a little more fluid now, but still cautious."
            mc.name "I promise, I won't get any ideas. I just want to make sure you're comfortable."
            the_person "Ugh, fine. But don't think I'm doing this for you. I just need to get a little more comfortable."
            mc.name "I understand. Just take your time and let me know if you need anything."
            "She nods, her movements a little more relaxed now, but still guarded."
        else:
            the_person "Okay, okay... I'll take off a few more things if it'll make you happy. But don't think I'm doing this because I'm into you or anything."
            "She begins to remove her clothes, her movements a little more confident now, but still hesitant."
            mc.name "I know, I know. You're just doing it because you want to, right?"
            the_person "Whatever. Just let me get this off and we can get on with this. And don't think this means I'm going to start liking you or anything."
            "She rolls her eyes, but continues to undress, her movements a little more fluid now."
    else:
        if the_person.arousal_perc < 50:
            the_person "Ugh, fine. I'll do it. But just for you, I'll make an exception. And don't think I'm doing this because I like you or anything."
            "She begins to remove her clothes, her movements slow and deliberate, but with a hint of seduction."
            mc.name "Thanks, babe. You're making me really happy right now."
            the_person "Don't call me 'babe'. And don't get too happy. I'm just doing this because I have to."
            "She shoots you a warning glance, but continues to undress, her movements a little more fluid now."
        else:
            the_person "Great, now let me get this off and we can get on with this. I'm dying over here! But don't expect me to be all happy about it or anything."
            "She begins to remove her clothes, her movements quick and urgent, her arousal clear."
            mc.name "Aww, come on. You're being a little grumpy. Let's just have some fun, okay?"
            the_person "Fine. But don't expect me to start smiling and laughing or anything."
            "She gives you a small smile, but it's clear she's still not comfortable with the situation, despite her growing arousal."
    return

label breeder_sex_watch(the_person, the_sex_person, the_position):
    $ title = the_person.title if not the_person.is_stranger else "The stranger"
    if the_person.sluttiness < the_position.slut_requirement - 20:
        $ the_person.draw_person(emotion = "angry", display_transform = character_left_flipped)
        the_person "Ugh, seriously? Can you two keep it down? I'm trying to focus on something other than your filthy antics."
        $ the_person.change_stats(obedience = -2, happiness = -1)
        "[title] looks away, her face twisted in distaste as she tries to ignore the sounds of your passion."
        return False
    if the_person.sluttiness < the_position.slut_requirement - 10:
        $ the_person.draw_person(display_transform = character_left_flipped)
        the_person "Honestly, you two are so... enthusiastic. Can't you keep it a little more private?"
        $ the_person.change_happiness(-1)
        "[title] glances away, her cheeks flushing with embarrassment as she tries to pretend she's not interested in your activities."
        return False
    if the_person.sluttiness < the_position.slut_requirement:
        $ the_person.draw_person(display_transform = character_left_flipped)
        if not is_watching(the_person):
            the_person "You're really getting into it, aren't you? I suppose it's kind of... intriguing..."
        $ the_person.change_slut(1, 30)
        "[title] watches you and [the_sex_person.fname] [the_position.verb] with growing interest, her eyes fixed on the action."
        return True
    if the_person.sluttiness >= the_position.slut_requirement and the_person.sluttiness < the_position.slut_cap:
        $ the_person.draw_person(display_transform = character_left_flipped)
        if not is_watching(the_person):
            the_person "Oh, wow... this looks like so much fun! Can I join in on the action?"
        $ the_person.change_slut(1, 50)
        "[title] watches with rapt attention, her eyes sparkling with excitement as she imagines herself in the midst of the action."
        return True
    $ the_person.draw_person(emotion = "happy", display_transform = character_left_flipped)
    if renpy.random.randint(0, 1) == 0:
        the_person "You know, [the_person.mc_title], [the_sex_person.fname] is really getting into this. Maybe you should, uh, take it to the next level?"
    else:
        call watcher_position_comment(the_person, the_sex_person, the_position) from _call_watcher_position_comment_breeder_sex_watch
    "[title] watches with bated breath, her body tense with anticipation as she waits to see what you'll do next."
    return True

label breeder_being_watched(the_person, the_watcher, the_position):
    $ title = the_watcher.fname if not the_watcher.is_stranger else "the stranger"
    if the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #They agree you should give it to her harder
        the_person "Mmmm, yeah... give it to me harder, [the_person.mc_title]. I can feel [title]'s eyes on us, and it's only making me hotter."
        "She arches her back, exposing her breasts as she invites you to take her harder."
        $ the_person.change_arousal(1)
        "[the_person.title] seems to be reveling in the attention, her body responding eagerly to your touch."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's super slutty and doesn't care what people think.
        the_person "Ha! Look at [title] trying to pretend like they're not interested. I can see the lust in their eyes, and it's only making me more turned on."
        "She winks at the watcher, a sly smile spreading across her face as she continues to ride you."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #She's super slutty and encourages the watcher to be slutty.
        the_person "Come on, [title]! Don't be shy! Join in on the fun, and let's make this a party to remember!"
        "She reaches out, beckoning the watcher to come closer as she continues to grind against you."
        $ the_person.change_arousal(1)
        "[the_person.title] seems to be in her element, her body responding eagerly to the attention."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #She's into it and encouraged by the slut watching her.
        "[the_person.fname] glances over at [title], a look of admiration on her face."
        the_person "Mmmm, yeah... I can see why you're so into this, [title]. You're really getting off on watching us, aren't you?"
        "She smiles, a sly glint in her eye as she continues to ride you."
        $ the_person.change_arousal(1)
        "[the_person.title] seems to be feeding off the watcher's energy, her body responding eagerly to the attention."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's into it but shamed by the prude watching her.
        the_person "Ugh, [title], can you please just leave us alone? I don't need your judgmental eyes on me right now."
        "She looks away, her face flushing with embarrassment as she tries to hide her arousal."
        $ the_person.change_stats(arousal = -1, slut = -1)
        "[the_person.title] seems to be struggling with her own desires, her body responding to the attention despite her shame."

    else: #the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #They're both into it but not fanatical about it.
        "[the_person.possessive_title!c] shoots [title] a sly glance, a hint of a smile on her face."
        the_person "Maybe next time, [title], you'll be the one getting ridden. Wouldn't that be fun?"
        "She winks, a playful glint in her eye as she continues to grind against you."
        $ the_person.change_stats(arousal = 1, slut = 1, max_slut = 30)
        "[the_person.title] seems to be enjoying the attention, her body responding eagerly to the watcher's presence."

    return

label breeder_work_enter_greeting(the_person):
    if the_person.happiness < 80 or the_person.love < 0:
        "[the_person.title] barely acknowledges your presence, her gaze flicking towards you before returning to her work."
        the_person "What do you want? I'm busy."
        "Her tone is curt, her body language closed off and uninviting."

    elif the_person.happiness > 130:
        if the_person.sluttiness > 40:
            the_person "Ah, [the_person.mc_title], just the person I was craving. Come here and give me a kiss."
            "She rises from her chair, her movements fluid and sensual, and walks towards you with a confident stride."
            the_person "I've been thinking about you all day, and I just can't seem to focus on my work."
            "She leans in close, her lips brushing against your ear, sending shivers down your spine."
        else:
            "[the_person.title] looks up from her work, a warm smile spreading across her face."
            the_person "Hey [the_person.mc_title], it's so nice to see you. I was just thinking about you."
            "She blushes slightly, her eyes sparkling with affection as she gazes at you."
    else:
        if the_person.sluttiness > 60:
            $ the_person.draw_person(position = "stand4")
            "[the_person.title] sashays over to you, her hips swaying seductively as she moves."
            the_person "Well, well, well. Look who decided to drop by and brighten up my day."
            "She leans in close, her voice husky and sultry, her breath hot against your skin."
            the_person "I've been waiting for you, [the_person.mc_title]. You know, just to see if you're as interested in me as I am in you."
            "She brushes her fingers against your arm, sending shivers down your spine as she gazes up at you with desire-filled eyes."
        else:
            the_person "Hey [the_person.mc_title]. Need anything? I mean, if you're not too busy..."
            "She looks up at you, her eyes soft and inviting, a hint of a smile playing on her lips."
            "Her body language is relaxed, her posture open and receptive, as she waits for your response."
    return

label breeder_date_seduction(the_person):
    if the_person.is_girlfriend:
        "[the_person.possessive_title!c] wraps her arms around your waist, pulling you close as she gazes up at you with desire-filled eyes."
        the_person "That was such a great time... I was thinking, maybe we could take things to the next level?"
        $ mc.change_locked_clarity(30)
        if the_person.effective_sluttiness(["vaginal_sex", "condomless_sex"]) > 60 and the_person.wants_creampie and the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex >= 0 and the_person.opinion.creampies >= 0 and not the_person.on_birth_control and not the_person.knows_pregnant:
            if the_person.opinion.creampies > 0: #No condoms, loves creampies, she's basically asking you to knock her up. So... have her ask you to knock her up!
                the_person "I want you to make me pregnant... I want to feel your cum inside me, filling me up and making me whole."
                the_person "I know it's a lot to ask, but I just can't help how I feel. I want to be your breeding vessel, your cumdump."
            else:
                the_person "I don't care about condoms... I just want to feel you inside me, raw and unbridled."
                the_person "You're so much better than those other guys, anyway. I can tell you're a real man, a breeder."
        elif the_person.effective_sluttiness(["vaginal_sex", "condomless_sex"]) > 60 and the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex > 0:
            the_person "Ugh, fine... If you really want to know, I'd rather not use a condom. It just feels better that way, more intimate."
            the_person "But don't think I'm doing it for you or anything... I'm doing it for myself, because I want to feel your cum inside me."
        elif the_person.effective_sluttiness(["vaginal_sex"]) > 50 and the_person.opinion.vaginal_sex > 0:
            the_person "You know, I didn't really want to go home with someone like you... But you're kind of growing on me, and I think I'd like to get to know you better."
            the_person "So, do you want to fuck me or what? I'm game if you are."
        elif the_person.effective_sluttiness(["anal_sex"]) > 60 and the_person.opinion.anal_sex > 0:
            the_person "I don't know why I'm even bothering to ask you this, but... do you want to fuck my ass? I've been thinking about it all night."
            the_person "It's not like I'm asking for much, but you're probably just going to say no anyway... But I had to ask, just in case."
        elif the_person.effective_sluttiness(["sucking_cock"]) > 40 and the_person.opinion.giving_blowjobs > 0:
            the_person "You know, I'm not really in the mood to do this, but... you're kind of cute when you're all worked up, and I think I'd like to suck your cock."
            the_person "So, do you want a blowjob or what? I'm game if you are."
        elif the_person.effective_sluttiness() > 40 and the_person.opinion.being_covered_in_cum > 0:
            the_person "Ugh, fine... If you really want to know, I'd be okay with getting covered in your cum. It's not like I haven't done it before, anyway."
            the_person "But don't expect me to be all happy about it or anything... I'm just doing it because I want to, not because I have to."
        elif the_person.effective_sluttiness(["touching_body"]) > 40 and the_person.opinion.giving_tit_fucks > 0 and the_person.has_large_tits:
            the_person "I don't know why I'm even telling you this, but... I'd be okay with sucking you off between my tits. It's just something I've always wanted to try, I guess."
            the_person "But don't think I'm doing it because I like you or anything... I'm just doing it because I want to, because it sounds like fun."
        else: #She's not very slutty, so she leaves the invitation open to interpretation
            the_person "You know, I don't really feel like going home with you or anything... But I guess I could be persuaded if you do something really good, something that makes me feel special."
            "She smirks, leaving the invitation open-ended as she gazes up at you with a hint of mischief in her eyes."

    elif the_person.is_affair:
        the_person "My [the_person.so_title] is out for the night, and I was thinking... maybe we could have some fun together."
        "She reaches down and cups your crotch, rubbing it gently through your pants as she gazes up at you with a sultry expression."
        $ mc.change_locked_clarity(40)
        if the_person.wants_creampie and the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex >= 0 and the_person.opinion.creampies >= 0 and not the_person.on_birth_control and not the_person.knows_pregnant:
            if the_person.opinion.creampies > 0: #No condoms, loves creampies, she's basically asking you to knock her up. So... have her ask you to knock her up!
                the_person "Let's go back to my place and get messy. I want to feel your cum inside me, filling me up and making me whole."
                the_person "I know it's wrong, but I just can't help how I feel. I want to be your breeding vessel, your cumdump."
            else:
                the_person "Alright, let's go back to my place and get wild. I want to feel you inside me, raw and unbridled."
                the_person "I hate how much I want this, but I do. So just take me and make me yours."
        elif the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex > 0:
            the_person "Ugh, fine. Let's go back to my place and fuck all night. No condoms, no regrets."
            the_person "I don't want to admit it, but I'm really looking forward to this. I want to feel you inside me, skin to skin."
        elif the_person.opinion.vaginal_sex > 0:
            the_person "Fine, let's go back to my place and you can pound my tight little pussy until I'm a wreck."
            the_person "I hate how much I enjoy this, but... I do. So just take me and make me scream."
        elif the_person.opinion.anal_sex > 0:
            the_person "Ugh, alright. Let's go back to my place so you can... take me from behind."
            the_person "I don't want to admit it, but my ass is really excited for this. I want to feel you inside me, deep and hard."
        elif the_person.opinion.giving_blowjobs > 0:
            the_person "Fine, let's go back to my place and you can choke me out with your cock."
            the_person "I hate how much I want this, but I do. So just take my mouth and make me yours."
        elif the_person.opinion.being_covered_in_cum > 0:
            the_person "Ugh, alright. Let's go back to my place, and you can cover me in your sperm all night."
            the_person "I hate how much I enjoy this, but... I do. So just do it and make me yours."
        elif the_person.opinion.giving_tit_fucks > 0 and the_person.has_large_tits:
            the_person "Fine, let's go back to my place so I can... give you a tit fuck."
            the_person "I hate how much I enjoy this, but I do. So just take my tits and make me yours."
        elif the_person.opinion.cheating_on_men > 0:
            the_person "Ugh, fine. Let's go back to my place, and you can do all the things I tell my [the_person.so_title] I hate."
            the_person "I don't want to admit it, but I'm really looking forward to this. I want to feel like a naughty girl, like I'm getting away with something."
        else:
            the_person "Ugh, let's go back to my place and make him really regret leaving me alone for the night. I want to feel like I'm getting revenge, like I'm taking back control."
    elif not the_person.has_significant_other:
        $ mc.change_locked_clarity(20)
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                the_person "I'm not done with you yet, [the_person.mc_title]. Want to come back to my place and see just how wild we can get?"
                "She runs her hand up your arm, her fingers tracing the contours of your muscle as she gazes up at you with a sultry expression."
            else:
                the_person "You know, I've had a really great time tonight, [the_person.mc_title]. Want to come back to my place, have a few drinks, and see where the night takes us?"
                "She smiles, her eyes sparkling with mischief as she invites you to join her for a night of adventure."
        else:
            if the_person.love > 40:
                the_person "I don't want to say goodbye yet, [the_person.mc_title]. Tonight's been amazing, and I want to savor every moment. Do you want to come back to my place and have a few drinks with me?"
                "She takes your hand, her fingers intertwining with yours as she gazes up at you with adoration in her eyes."
            else:
                the_person "This might be crazy, but I had a really great time tonight, [the_person.mc_title]. Do you want to come back to my place and see where things go? I don't know why I'm even asking, but I just can't help myself."
                "She blushes, her eyes looking down as she invites you to join her for a night of exploration."
    else:
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                $ mc.change_locked_clarity(20)
                the_person "I'm not done with you yet, [the_person.mc_title]. Want to come back to my place and finish what we started? My [the_person.so_title] won't be home until morning, so we have all night."
                "She runs her hand up your arm, her fingers tracing the contours of your muscle as she gazes up at you with a sultry expression."
            else:
                $ mc.change_locked_clarity(20)
                the_person "This might be crazy, but do you want to come back and have another drink with me? My [the_person.so_title] is stuck at work, and I don't want to be left all alone."
                "She smiles, her eyes sparkling with mischief as she invites you to join her for a night of adventure."
        else:
            if the_person.love > 40:
                $ mc.change_locked_clarity(20)
                the_person "You're making me feel crazy, [the_person.mc_title]. Do you want to come have a drink at my place? But don't think this means anything... yet."
                "She takes your hand, her fingers intertwining with yours as she gazes up at you with adoration in her eyes."
                the_person "My [the_person.so_title] won't be home until morning, and we have a big bed you could help me warm up."
            else:
                $ mc.change_locked_clarity(20)
                the_person "This is crazy, but would you want to have one last drink at my place? My [the_person.so_title] won't be home until morning... I suppose."
                "She blushes, her eyes looking down as she invites you to join her for a night of exploration."
    return

label breeder_sex_end_early(the_person):
    if the_person.sluttiness > 50:
        if the_person.love > 40:
            if the_person.arousal_perc > 60:
                the_person "Aww, come on, [mc.name]... You're done already? I was just getting warmed up, and I was hoping for a lot more from you."
                "She pouts, her face twisted in disappointment as she gazes up at you with a sultry expression."
                the_person "But I guess you're not exactly the most energetic partner I've ever had... Still, I suppose it was a nice try, even if you didn't quite hit the mark."
            else:
                the_person "Well, I suppose that's it, then? I was ready to give you a lot more, but I guess you're not exactly the most enthusiastic about this whole situation, are you?"
                "She shrugs, her movements nonchalant as she gazes up at you with a hint of disappointment in her eyes."
        else:
            if the_person.arousal_perc > 60:
                the_person "Hmph, you're sure you're finished? I was really enjoying this... You know, I don't usually do this, but I was actually getting kind of into it."
                "She raises an eyebrow, her expression skeptical as she gazes up at you with a hint of amusement in her eyes."
                the_person "But I guess you're not exactly the most experienced, are you? I mean, it's not like I'm the one who needs to learn how to do this properly..."
            else:
                the_person "I guess it was okay, I suppose. I mean, it's not like I was expecting much from you in the first place... But still, I suppose it was a nice little distraction, even if it didn't exactly set my world on fire."
                "She shrugs, her movements nonchalant as she gazes up at you with a hint of indifference in her eyes."
    else:
        if the_person.love > 40:
            if the_person.arousal_perc > 60:
                the_person "Oh, come on, [mc.name], you can't leave me hanging like this... I mean, I was actually starting to enjoy this, and I was hoping for a lot more from you."
                "She pouts, her face twisted in disappointment as she gazes up at you with a sultry expression."
                the_person "But hey, I guess you're not exactly the most romantic guy out there, are you? Still, I suppose it was a nice try, even if you didn't quite hit the mark."
            else:
                the_person "Well, that was a nice little interlude, I suppose. I mean, it's not like I'm the type to be all lovey-dovey and shit... But still, I suppose it was a nice little distraction, even if it didn't exactly set my world on fire."
                "She smiles, her eyes sparkling with amusement as she gazes up at you with a hint of teasing in her voice."
        else:
            if the_person.arousal_perc > 60:
                the_person "Geez, I guess that was enough... I mean, I don't know why you even bother trying, you're not exactly the best at this, are you?"
                "She rolls her eyes, her expression skeptical as she gazes up at you with a hint of disappointment in her eyes."
            else:
                the_person "Good, it's over. Now let's get this over with. I mean, I've got better things to do than hang around with someone who can't even manage to get it right..."
                "She stands up, her movements abrupt as she gazes up at you with a hint of annoyance in her eyes."
    return

label breeder_sex_take_control(the_person):
    if the_person.arousal_perc > 60:
        the_person "What's wrong with you, [mc.name]? Can't even finish what you started? I'm the one who's supposed to be in control here, and I won't let you just leave me hanging like this!"
        "She grabs your wrist, her grip firm as she pulls you back into the action."
        the_person "I'll show you how it's done, and you'll be begging for mercy by the time I'm done with you."
    else:
        the_person "Unbelievable. You're not even going to finish what you started? Fine, I'll take matters into my own hands then!"
        "She pushes you aside, her movements assertive as she takes control of the situation."
        the_person "Don't think for a second that I'm some weak, submissive girl who'll just roll over and take it. I'm a breeder, and I'll show you what that means."
    return

label breeder_sex_beg_finish(the_person):
    the_person "Alright, [mc.name], you want to play it cool? I'll let you off the hook this time, but just know that I'm going to make you pay for this. And when I'm done, you'll be begging for more."
    "She leans in close, her voice husky and seductive as she whispers in your ear."
    the_person "You'll learn to respect a breeder's power, and you'll be grateful for the lesson."
    "She pulls back, a sly smile spreading across her face as she gazes up at you with a hint of dominance in her eyes."
    return

label breeder_sex_review(the_person, the_report):
    $ comment_position = the_person.pick_position_comment(the_report)
    if comment_position is None:
        return #You didn't actually do anything, no need to comment.

    $ used_obedience = the_report.get("obedience_used", False) #True if a girl only tried a position because you ordered her to.
    $ the_person.draw_person()  # make sure she stands up for talking with you

    #She's worried about her SO finding out because it was in public
    if the_report.get("was_public", False) and the_person.has_significant_other and the_person.opinion.cheating_on_men <= 0: #It was public and she cares.
        if the_person.is_affair: #Dialogue about her being into it, but you can't do this in case she gets caught.
            the_person "Oh god, this is so reckless! I'm really getting off on this, but we can't get caught... My [the_person.so_title] would kill me!"
            the_person "What if someone sees us and tells them? I'll be in so much trouble..."
            "She glances around nervously, her eyes scanning the surrounding area for potential witnesses."
        elif used_obedience:
            the_person "I'm not sure I'm comfortable with this... We're in public, and someone might recognize me and tell my [the_person.so_title]."
            mc.name "Don't worry, nobody's paying attention to us. We're being careful."
            the_person "I hope you're right... I don't want to risk getting caught and facing the consequences."
        else:
            $ the_person.call_dialogue("surprised_exclaim")
            the_person "Oh no, we're in public! Someone might see us and tell my [the_person.so_title]... I'll be so screwed!"
            mc.name "Don't worry, nobody's paying attention to us. We're just another couple in the crowd."
            the_person "I hope you're right... I don't want to risk getting caught and facing the consequences."

    #She's single, but worried that you did in public.
    elif the_report.get("was_public", False) and (the_person.effective_sluttiness()+10*the_person.opinion.public_sex < comment_position.slut_cap):
        if used_obedience:
            the_person "Ugh, I'm not sure I'm comfortable with this... We're in public, and everyone's staring at us like we're some kind of exhibitionists..."
            the_person "I don't want to be known as the girl who gets off on public sex... That's just not my style."
        else:
            the_person "Oh no, we're in public! Everyone's watching us and judging us for this... I feel so exposed!"
            mc.name "Don't worry, nobody really cares what we're doing. They're just curious."
            the_person "I hope you're right... I don't want to be the subject of gossip and rumors."

    elif the_report.get("girl orgasms", 0) > 2:
        if used_obedience:
            the_person "Oh my god... baby... I loved what you did to me... I never knew being submissive could feel so good..."
            mc.name "I do enjoy when you keep begging me to make you cum again. It's almost like you're addicted to it."
            the_person "Shut up and kiss me, [mc.name]... I need to feel your lips on mine again."
            "She pulls you in for a passionate kiss, her body still trembling with aftershocks."
        else:
            the_person "I have never... cum that hard... It was just amazing... I guess I needed that."
            "She seems dazed by her orgasm as she tries to form coherent sentences, her eyes still glazed over with pleasure."
            the_person "You really... know how to give a girl a good time... just gimme a second to catch my breath."
            mc.name "Take your time, I'm not going anywhere."
            the_person "Thanks, [mc.name]... I think I need a minute to recover before we can start again."

        call sex_review_trance(the_person) from _call_sex_review_trance_breeder_sex_review

    #No special conditions, just respond based on how orgasmed and how slutty the position was.
    elif the_report.get("girl orgasms", 0) > 0 and the_report.get("guy orgasms", 0) > 0: #You both came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position cap, it was tame
            the_person "Mmmm, that was delicious... But I think we can take it to the next level next time. I'm not afraid to get a little wild, [mc.name]."
            "She runs her tongue over her lips, her eyes sparkling with excitement as she gazes up at you."
            the_person "Doesn't that sound like fun? I'm getting wet just thinking about it... Maybe we can try something a little more... adventurous next time."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "Ah, that was just what I needed! I think we're very compatible, [mc.name]... in more ways than one."
            "She smiles, her eyes sparkling with amusement as she gazes up at you."
            the_person "Let's do it again some time soon, okay? I want to see how much further we can push each other's limits."

        elif used_obedience: #She only did it because she was commanded
            the_person "Fuck, I... I didn't think I was going to cum like that. I guess I just can't resist a good command, huh?"
            mc.name "Aren't you going to thank me? You obviously had a good time."
            the_person "Shut up and don't get too full of yourself, [mc.name]. I'm not some obedient little slave who'll do anything you say... But I have to admit, it was kind of hot being told what to do."

        else: # She's surprised she even tried that.
            the_person "Oh fuck, that was intense! I didn't think I was going to take it so far, but it just felt right, you know?"
            "She looks up at you, her eyes wide with surprise and a hint of excitement."
            the_person "Don't think that's going to happen every time though, alright? I'm not a slut! I just like to push my boundaries sometimes... And I have to admit, it was kind of exhilarating."
        if the_person.love > 40:
            the_person "You know, I never thought I'd say this, but I think I might actually like this whole 'relationship' thing with you, [mc.name]. You're not like other guys I've met... You're actually kind of sweet."
        else:
            the_person "Well, that was fun. Let's do it again sometime, but not too soon, okay? I need to recover my dignity first... And maybe take a few cold showers to calm down."

    elif the_report.get("girl orgasms", 0) > 0: #Only she came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            the_person "Already done? That's just not fair. Next time, I'm going to make sure we both cum, and then some... Maybe we can even try some new positions, or get a little more... adventurous."
            "She winks, a sly smile spreading across her face as she imagines the possibilities."
            the_person "I've got a few ideas that are going to blow your mind, [mc.name]. And I'm not just talking about the sex... although, that's definitely part of it."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "You're all done? Well, that was fucking amazing, either way, [mc.name]."
            "She leans in close, her voice husky and seductive as she whispers in your ear."
            the_person "I'll repay the favour next time, alright? I promise. And maybe we can try something new... something that'll really get your heart racing."

        elif used_obedience: #She only did it because she was commanded
            the_person "That's it? I mean, not like I wanted to do anything more, I just thought you were going to... you know, finish what you started."
            mc.name "Some other time. I just wanted to see what you look like when you cum."
            the_person "I... Fuck, well, I guess you got what you wanted. But don't think I'm going to make it easy for you next time. I'll make you work for it."
            "She pouts, a hint of annoyance in her voice, but her eyes sparkle with excitement at the prospect of their next encounter."

        else: # She's surprised she even tried that.
            the_person "Oh fuck, that was intense! You really know how to make a girl feel good, [mc.name]."
            "She smiles, her eyes wide with surprise and a hint of excitement as she gazes up at you."
            the_person "You're probably tired after all that work. I promise I'll repay the favour next time, okay? And maybe we can try something different... something that'll really get us both off."

    elif the_report.get("guy orgasms", 0) > 0: #Only you came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            the_person "Hmph, you're all spent already? That's just not satisfying... I was just getting started!"
            "She pouts, her lips curling into a sulky expression as she gazes up at you."
            mc.name "Sorry, I'll make it up to you next time."
            the_person "Well, I suppose I could be persuaded to try again... But don't expect any mercy! I'll be coming for you, hard and fast."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "You're already done? Such a tease! Fine, I'll let you off this time... But don't think you're getting off that easy!"
            "She winks, a sly smile spreading across her face as she leans in close."
            mc.name "Sorry, I'll make it up to you next time."
            the_person "You'd better, or you'll be facing the consequences... And trust me, you don't want that."

        elif used_obedience: #She only did it because she was commanded
            the_person "I suppose you're worn out from all that... We're finished then?"
            mc.name "Yeah, that's all for now."
            the_person "Fine, but don't think this means you get to slack off next time! I expect to see some real effort from you."

        else:  # She's surprised she even tried that.
            the_person "Wow, that was... quite an experience. I think I got a little carried away there... Maybe it's for the best that we stop here."
            "She looks down, her face flushing with embarrassment as she tries to process what just happened."
            the_person "I need to think about what I just did... And maybe take a few cold showers to calm down."

    elif the_person.energy < 10: #Nobody came and she's tired
        the_person "Ugh, I'm just too exhausted... Another time, maybe?"
        "She leans against you, her body limp with fatigue as she gazes up at you with a hint of apology in her eyes."
        mc.name "No worries, we'll do it another day."
        the_person "Just don't expect any special treatment when we try again, got it? I'll be coming for you, full force."

    else: #Nobody came.
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            the_person "Aww, come on! You're already done? I was just getting warmed up!"
            "She pouts, her lips curling into a sulky expression as she gazes up at you."
            the_person "You're such a tease, [the_person.mc_title]. Leaving me high and dry like this."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "We're stopping? But we were just getting to the good part!"
            mc.name "Sorry [the_person.title], maybe another time."
            the_person "Yeah, maybe. You can't just leave a girl hanging like that, you know. It's not nice to tease."

        elif used_obedience: #She only did it because she was commanded
            the_person "Well, I wasn't expecting that. I thought you had more in store for me."
            mc.name "You aren't disappointed, are you?"
            the_person "No, no. I just...wanted to see where things would go, that's all. I was curious."
            the_person "It's fine. I'll just have to find someone else to take me further... or maybe I'll just take matters into my own hands."

        else:  # She's surprised she even tried that.
            the_person "Ugh, you're probably right. We should stop now before we get too carried away... I don't want to do something I'll regret later."
            "She looks down, her face flushing with embarrassment as she tries to process what just happened."
            the_person "Let's just keep this casual, okay? I don't want to get too attached... or too pregnant."

    # Gave creampie while she is not on birth control (extra dialogue when she could get pregnant)
    if the_report.get("creampies", 0) > 0 and not the_person.on_birth_control and not the_person.knows_pregnant:
        the_person "Well, I guess we just made things a little more interesting, didn't we?"
        "She raises an eyebrow, a sly smile spreading across her face as she gazes up at you."
        the_person "If I get pregnant, it'll serve you right for being so reckless... But I have to admit, the thought of it is kind of exciting."
        "She leans in close, her voice husky and seductive as she whispers in your ear."
        the_person "Maybe we can try to make it happen again... and see what kind of trouble we can get into."

    $ del comment_position
    return

## Role Specific Section ##

label breeder_improved_serum_unlock(the_person):
    mc.name "[the_person.title], now that you've had some time to get familiar with the lab, I want to discuss something with you."
    the_person "What's on your mind, stud? You look like you've got a plan to get me pregnant or something."
    mc.name "Ha! Well, not exactly... But I do think we can take our research to the next level."
    mc.name "I've been thinking about the role of sexual arousal in enhancing the effects of the serum."
    "[the_person.title] raises an eyebrow, a hint of curiosity in her expression."
    the_person "Oh, you mean like how a good fucking can make me more receptive to your breeding plans?"
    mc.name "Uh, well... Yeah, something like that."
    the_person "I've been thinking that an orgasm might open up chemical receptors that are normally blocked... And maybe even make me more fertile."
    mc.name "What if that's true? Does that give us any new leads to pursue?"
    the_person "If it's true, I think I can use that effect to amplify the results in our subjects... And maybe even take it to the next level."
    "[the_person.possessive_title!c] grins mischievously, a sly smile spreading across her face."
    the_person "We'll need to run some experiments to confirm, of course... But I think I have just the thing in mind."
    mc.name "What kind of experiments?"
    the_person "I want to take a dose of the serum myself, and you can record the effects... Then I'll take care of the rest."
    mc.name "You mean, you'll...?"
    the_person "Yes, exactly. I'll stimulate myself, and we can compare the effects before and after... And maybe even see if we can get me pregnant in the process."
    mc.name "Are you sure that's a good idea?"
    the_person "Not really, but we can't trust anyone else with this information if we're right... And I'm willing to take the risk to see this through."
    the_person "We might be able to make progress by brute force, but this is a chance to take our research to the next level... And maybe even push the boundaries of what's possible."
    the_person "A finished dose of serum that raises my Suggestibility... The higher it gets, the better."
    the_person "Then we'll just need some time and some privacy for me to see what sort of effects my... stimulation will have."
    "She leans in close, her voice husky and seductive as she whispers in your ear."
    the_person "And maybe, just maybe, we'll discover something new about ourselves in the process... Like how to make the perfect breeding stock."
    return

## Taboo break dialogue ##

label breeder_kissing_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 30:
        the_person "Fine, let's just get this over with. You've been eyeing me for a while now, and I'm tired of waiting."
        "She steps closer, her eyes locked on yours as she runs her tongue over her lips."
        mc.name "I wouldn't say that's true, but I'll play along."
        the_person "Hmph, whatever. Just shut up and kiss me already. I'm not getting any younger, and I need to get bred."
        mc.name "Oh, I'm not going to shut up that easily. I want to savor this moment."
        the_person "Suit yourself. I'll just have to find someone else who's willing to give me what I need... And maybe even get me pregnant."
        mc.name "Hold on, wait a minute. I'm not going anywhere. I'm the one who's going to breed you, and no one else."
        the_person "Oh? You're not going anywhere? Then get over here and kiss me already! I'm ready to be taken."
        mc.name "Alright, alright. Here I come."
        "She opens her mouth, inviting you to kiss her as she wraps her arms around your waist."

    elif the_person.love >= 20:
        the_person "So we're doing this, huh? About time, if you ask me. I've been waiting for you to make a move."
        mc.name "I guess we are. What do you think?"
        the_person "It's about time we finally made out, [the_person.mc_title]. I'm ready to take our relationship to the next level... And maybe even start a family."
        mc.name "I'm glad you feel that way."
        the_person "Me too. Just be gentle, okay? I want to make sure our first time is special."
        mc.name "I will. I promise to make it a night to remember."
        "She smiles, her eyes sparkling with excitement as she leans in for a kiss."

    else:
        the_person "I don't know if this is a good idea, [the_person.mc_title]. We're taking things too fast, aren't we? I'm not sure if I'm ready to be bred yet."
        mc.name "Are you scared?"
        the_person "No! I'm just...not sure if this is a good idea. But I trust you to take care of me... And maybe even give me a baby."
        mc.name "Good. Because I'm not going to let you back out now. I'm going to make sure you're mine, and mine alone."
        the_person "Hmph. Fine. But if this is a mistake, it's on you. I'm counting on you to make this right."
        mc.name "It'll be worth it, I promise. I'll make sure you're happy, and that our family is strong and healthy."
        "She nods, her eyes locked on yours as she prepares for the kiss that will change everything."
    return

label breeder_touching_body_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 30:
        the_person "Come on then, don't be shy. You've been eyeing me for ages, and I'm tired of waiting for you to make a move."
        "She steps closer, her eyes locked on yours as she runs her hands over her body, inviting you to touch her."
        mc.name "Hey, I'm not that obvious... But I guess I am a little curious."
        the_person "Oh, please. I can see the way you look at me, like you're trying to decide if I'm in heat or something."
        mc.name "Well, I suppose I am a little drawn to you. You're just so... fertile."
        the_person "Fertile? Ha! You just want to get me pregnant, don't you? Well, I'm not going to make it easy for you."
        "She smirks, her eyes sparkling with mischief as she teases you."

    elif the_person.love >= 20:
        the_person "So you're ready for this? You want to take our relationship to the next level?"
        "You nod, and she smiles, her eyes shining with excitement."
        the_person "Me too, I think. I didn't think I'd be so nervous when you actually made a move... But I'm ready to see where this goes."
        mc.name "Just relax. You trust me, right? I'll take care of you, and make sure you're happy and healthy... And maybe even pregnant."
        the_person "Of course. Just don't expect me to be all touchy-feely about it... At least, not yet."
        "She leans in close, her voice barely above a whisper as she invites you to touch her."

    else:
        the_person "I think you're getting a little ahead of yourself here [the_person.mc_title]. Maybe we should slow things down a bit."
        mc.name "What do you mean? You're not interested?"
        the_person "I mean I don't just let anyone feel me up... Especially not when it comes to breeding. That's a big decision, and I need to make sure I'm ready."
        mc.name "You're not scared, are you?"
        the_person "Scared? Of course not! I just need to make sure I'm making the right choice... For me, and for our potential future together."
        mc.name "Well then just relax and go with it. It doesn't have to mean anything unless we want it to... And who knows, maybe we'll even start a family together."
        "You see her answer in her eyes before she says anything, a spark of excitement and curiosity that she can't hide."
        the_person "You're so bad for me, you know that? But maybe that's exactly what I need... Someone to push me out of my comfort zone and show me what I'm capable of."
        mc.name "Well let me make up for it then. Let me show you what I can do, and what we can create together."
        the_person "Hmm, maybe I'll let you... But don't think you're getting off that easy. I'll make sure you work for it."
    return

label breeder_touching_penis_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 35:
        the_person "Oh, you're really enjoying this, aren't you? Look how hard you are... Just begging to be touched."
        "She reaches out and runs her fingers over your cock, her touch light and teasing."
        mc.name "Do you want to feel it? You can if you want... I dare you."
        the_person "Yeah, why not? I'll try not to hurt it... But no promises, I'm a breeder, not a nurse."
        "She wraps her hand around your cock, her grip firm but gentle as she starts to stroke you."

    elif the_person.love >= 20:
        the_person "Your cock looks so nice when it's hard... Like it's just waiting to be ridden."
        mc.name "Go ahead, it doesn't bite... Unless you want it to, that is."
        the_person "Well, it might if you're not careful... But I'm willing to take that risk."
        "She reaches out and touches your cock, her fingers tracing the contours of your shaft as she gazes up at you with adoration in her eyes."

    else:
        mc.name "My cock is so hard right now [the_person.title]... Just thinking about breeding you is making me crazy."
        the_person "What? That's taking things a little far, don't you think? I'm not just some broodmare, you know."
        mc.name "Come on, you know you want to... Just a few strokes, then if you aren't impressed you can stop. But I think you'll find it's worth it."
        the_person "Fine, but don't expect me to make any promises after this... I'm not committing to anything just yet."
        mc.name "I wouldn't dream of it... But I do hope you'll consider my proposal. I think we could make some beautiful babies together."
        the_person "Hmm, okay then. I'll give it a try... But just remember, I'm a breeder, not a toy."
    "She reaches out and wraps her hand around your cock, her touch gentle but firm as she starts to stroke you."
    "You feel a surge of pleasure as she touches you, and you can't help but wonder what it would be like to breed her for real."
    the_person "Mmm, you're really nice when you're hard... Maybe I'll have to consider your proposal after all."
    return

label breeder_touching_vagina_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 35:
        the_person "Come on, don't be shy. You've been eyeing my breeding slit for ages, admit it."
        "She spreads her legs, inviting you to touch her as she gazes up at you with a sultry expression."
        mc.name "I... I guess I have been curious."
        the_person "Curious? Ha! You're a breeder at heart, and you can't resist the call of a fertile female like me."

    elif the_person.love >= 20:
        the_person "Oh fuck, you've got my pussy tingling. I want you to touch it [the_person.mc_title]... I want to feel your fingers inside me."
        mc.name "You sure? I don't want to push you too far."
        the_person "No, I want it. I want you to touch me, to explore me, to make me feel like a breeding vessel."
        "She takes your hand, guiding it to her vagina as she gazes up at you with adoration in her eyes."

    else:
        the_person "I don't know if we should be doing this [the_person.mc_title]... It feels so wrong, but at the same time, it feels so right."
        mc.name "Just take a deep breath and relax. I'm just going to touch you a little, and if you don't like it I'll stop... But I think you'll find it's worth it."
        the_person "Just a little?"
        mc.name "Just a little. Trust me, it's going to feel amazing... And who knows, maybe we'll even make some babies together."
        the_person "Hmm, okay. But don't think this means I'm easy... I'm just willing to take a chance on you, and on us."
        mc.name "I wouldn't dream of it... But I do hope you'll consider my proposal. I think we could make some beautiful babies together."
        "She nods, her eyes sparkling with excitement as she invites you to touch her."
    return

label breeder_sucking_cock_taboo_break(the_person):
    mc.name "I want you to do something for me... Something that'll show me you're committed to our breeding program."
    the_person "Oh yeah? What do you want me to do to you, stud?"
    mc.name "I want you to suck on my cock... To take it deep in your mouth and show me you're willing to do whatever it takes to get pregnant."
    if the_person.effective_sluttiness() >= 45:
        the_person "Mmm, I think I'm up for that. It's not going to be too big for me, is it? I want to make sure I can take it all in."
        mc.name "I think you'll be able to handle it... But if you're not sure, we can always try something else."
        the_person "No, no, I want to do this. I want to feel your cock in my mouth, to taste your cum and know that I'm one step closer to getting pregnant."
        "She bites her lip and winks at you, her eyes sparkling with excitement."
        the_person "And if it gets a little rough, that's okay too. I can handle it."

    elif the_person.love >= 30:
        the_person "I guess we've been dancing around it for a while... But I'm ready to take the next step."
        "She bites her lip and looks your body up and down, her eyes lingering on your cock."
        the_person "Alright, let's do this. I want to feel your cock in my mouth, to know that I'm yours and you're mine."
        "She kneels down, her eyes locked on yours as she takes your cock in her mouth."

    else:
        the_person "Oh, I was wondering if this was going to come up... I'm not sure if I'm ready for this."
        "She laughs nervously and looks away from you, her face flushing with embarrassment."
        the_person "I don't know [the_person.mc_title]... This is all so new to me."
        "You reach up and hold her chin, turning her head back to face you."
        mc.name "Don't overthink it. Just kneel down and suck on it for me. If you don't like doing it, we can just forget it happened... But I think you'll find it's worth it."
        "You can see in her eyes the moment her resolve breaks. She bites her lip and nods, her face set in determination."
        the_person "Alright, let's do this. I'll show you I'm willing to do whatever it takes to get pregnant."
    "She slowly gets down on her knees, her eyes darting between your face and your cock with a mix of reluctance and curiosity."
    the_person "You know, I never thought I'd be doing this... But I guess I'm willing to try new things for you, and for our future together."
    "She takes a deep breath, her hand wrapping around the base of your cock as she leans in to take it in her mouth."
    "As she starts to suck, her eyes flash up to meet yours, a hint of defiance and challenge in them."
    the_person "Satisfied now? I'm doing this for you, and for us... And I'm not going to stop until we get the results we want."
    return

label breeder_licking_pussy_taboo_break(the_person):
    mc.name "I want to taste your breeding slit [the_person.title]. Are you ready to take our relationship to the next level?"
    if the_person.effective_sluttiness() >= 45:
        the_person "Hmph, I don't need your permission or anything, but fine. I'm ready to see if you're worthy of breeding me."
        mc.name "Good. But don't expect me to go easy on you just because it's your first time... I'll make sure you're nice and wet for me."
        the_person "Oh, please. I've had better... But I'm willing to give you a chance to prove yourself."
        "She spreads her legs, inviting you to explore her as she gazes up at you with a sultry expression."

    elif the_person.love >= 30:
        the_person "Finally, a man who knows how to treat a woman right... And by 'right', I mean like a breeding vessel."
        mc.name "That's what I like to hear... You're ready to take our relationship to the next level and start a family."
        the_person "Yes, I'm ready... I want to feel your tongue inside me, to know that you're committed to our breeding program."
        "She smiles, her eyes sparkling with excitement as she invites you to explore her."

    else:
        if the_person.has_taboo("sucking_cock"):
            the_person "You know, I never thought I'd see the day where you'd be willing to do this... But I guess I'm not going to complain."
            "She bites her lip and smirks at you, her eyes flashing with amusement."
            the_person "Just don't expect me to be all grateful or anything... I'm only doing this because I want to see if you're worthy of breeding me."
        else:
            the_person "About time you decided to make up for not sucking my cock... But I suppose this is a good start."
            "She rolls her eyes and smiles, her expression playful and teasing."
            the_person "But fine, I'm ready... Just don't expect me to be all appreciative or anything... Yet."
    "She lies back, her eyes darting between yours and the area you're about to explore as she prepares for your touch."
    the_person "And don't think this means I'm some kind of slut for letting you do this... I'm just a breeder, doing what comes naturally."
    mc.name "I wouldn't dream of it... You're just being a good sport, right?"
    the_person "Something like that... But let's just say I'm willing to do whatever it takes to get pregnant."
    "She closes her eyes, her face flushed with embarrassment as you start to lick her, but she can't hide the excitement and anticipation in her voice."
    return

label breeder_vaginal_sex_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 60:
        the_person "Ah, finally! I've been waiting for this moment all night... The moment when you'll shove your cock deep inside my breeding slit and fill me up with your cum."
        "She spreads her legs, inviting you to enter her as she gazes up at you with a sultry expression."
        the_person "Come on then, get that cock inside me and fuck me like a breeding vessel. I'm ready to be bred, and I want it rough."
        mc.name "You want it rough? I'll give it to you rough. I'll pound your pussy until you're screaming for more."
        the_person "That's what I'm counting on. I want to feel your cock deep inside me, to feel your cum shooting into my womb. I want to be bred, and I want it now."

    elif the_person.love >= 45:
        the_person "Alright, show me what you've got. I'm ready to take our relationship to the next level... And start a family."
        mc.name "You better be. I'm going to make sure you remember this... And that you'll be begging for more."
        the_person "Bring it on! I can take it. I'm a breeder, after all... And I'm ready to be bred. I want to feel your cock inside me, to feel your love and your passion."
        mc.name "I'll give it to you, my love. I'll give you everything you want, and more. I'll make sure you're satisfied, and that you'll be begging for more."
        "She smiles, her eyes sparkling with excitement as she invites you to enter her."

    else:
        if the_person.has_taboo("anal_sex"):
            the_person "Well, well, well. Look at that cock. I guess we're going to find out just how tight my breeding slit is."
            mc.name "That's the plan. And if you're a good girl, I might just make it worth your while... And give you the baby you've always wanted."
            the_person "Hmph, I'm always good. Now get to it before I change my mind... And don't think about holding back. I want it all. I want to feel your cock deep inside me, to feel your cum shooting into my womb."
        else:
            the_person "Oh, so that's what you're going to do with that big cock of yours. Well, I guess we'll see how it feels... To be bred like a fertile female."
            mc.name "We sure will. And if you're lucky, I might just make it feel even better... And give you the orgasm of a lifetime."
            the_person "Ugh, just get on with it already! I'm not getting any younger... And I need to get pregnant soon. I want to feel your cock inside me, to feel your love and your passion."
            "She rolls her eyes, her expression playful and teasing as she invites you to enter her."
    return


label breeder_anal_sex_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 75:
        the_person "Oh, come on! Don't tease me like that. I can see the hunger in your eyes, and I know you're dying to breed me... In every hole."
        "She winks, her eyes sparkling with excitement as she invites you to take her anally."
        mc.name "You're right, I do want to breed you... And I want to make sure you're comfortable with it."
        the_person "Comfortable? Ha! I'm a breeder, not some delicate flower. I can take it rough, and I want it rough."
        "She bends over, her ass presented to you as she gazes back at you with a sultry expression."

    elif the_person.love >= 60:
        the_person "Are you sure you want to do this? I'm not exactly the most experienced person when it comes to anal... But I'm willing to try for you."
        mc.name "I'll be gentle, don't worry. I just want to make sure you're happy and satisfied."
        the_person "Alright, but if it hurts too much, I'm stopping... And I'll make sure you know it."
        "She smiles, her eyes sparkling with amusement as she invites you to take her anally."

    else:
        if the_person.has_taboo("vaginal_sex"):
            the_person "Wait, are you sure you want to do this? My ass might be too tight for your cock... But I'm willing to try if you are."
            mc.name "I'll make it fit, but you might feel a little sore afterward... And I'll make sure to take care of you."
            the_person "Oh, great. Just what I needed... A good hard fucking in the ass."
        else:
            the_person "Come on, [mc.name]. Let's just get this over with. I don't know what's gotten into me today... But I think I need to be bred, and I need it now."
            mc.name "Are you sure you're okay with this? You seem a little... nervous."
            the_person "Of course, I'm just... anxious. And a little embarrassed. But let's just do this already! I need to feel your cock inside me, and I need it now."
            "She blushes and looks away, her face flushing with excitement and anticipation."
            mc.name "Alright, let's get started then... And see where this takes us."
            the_person "Hurry up, I'm ready when you are... And I'm not going to wait much longer."
    return

label breeder_condomless_sex_taboo_break(the_person):
    if the_person.knows_pregnant:
        the_person "Ah, you want to breed me without protection? Well, I suppose it's a little late for that now... But don't say I didn't warn you, I'm a fertile female after all, and I'm ready to take your cum deep inside my womb."
        if the_person.wants_creampie:
            the_person "If you're going to cum inside me, make sure it's a good one... I want to feel your seed splashing against my cervix, and know that I've been thoroughly bred like the fertile female I am."
        else:
            the_person "Just make sure to cover me with your cum... I want to feel it dripping down my thighs, and know that I've been marked as your breeding vessel."
        "She spreads her legs, inviting you to take her without protection as she gazes up at you with a sultry expression."

    elif the_person.opinion.bareback_sex > 0:
        the_person "Whatever, you want to do it bareback, huh? Well, I'm not going to stop you... But don't say I didn't warn you, I'm a breeder after all, and I'm ready to take your cum deep inside my womb."
        if the_person.on_birth_control:
            the_person "I'm on the pill, so you don't have to worry about getting me pregnant... But I have to admit, the thought of it is kind of exciting, and I'm tempted to see what would happen if we took a chance."
            $ the_person.update_birth_control_knowledge()
        elif the_person.wants_creampie:
            the_person "But if you're going to cum inside me, you'd better make it worth my while... I want to feel your seed splashing against my cervix, and know that I've been thoroughly bred like the fertile female I am."
        elif the_person.opinion.creampies < 0:
            the_person "Just don't get me pregnant, okay? That would be a huge pain... But at the same time, it's kind of tempting to see what would happen if we took a chance, and I felt your cum deep inside my womb."
        else:
            the_person "Alright, just make sure you pull out this time... But I have to admit, the thought of you cumming inside me is kind of exciting, and I'm tempted to see what would happen if we took a chance."
        "She smiles, her eyes sparkling with amusement as she invites you to take her without protection, and explore the possibilities of breeding her."

    elif the_person.love > 60:
        if the_person.on_birth_control:
            the_person "Fine, I'll admit it... I'm on the pill. But don't think that means you can just cum inside me without making it worth my while... I want to feel your cock deep inside my pussy, and know that you're serious about breeding me."
            $ the_person.update_birth_control_knowledge()
            "She smiles, her eyes sparkling with amusement as she invites you to take her without protection."
        elif the_person.wants_creampie:
            the_person "You're always pushing me to my limits, aren't you? Fine, if we're going to do this, make it a good one... I want to feel your seed splashing against my cervix, and know that I've been thoroughly bred like the fertile female I am."
            mc.name "Are you on the pill?"
            "She rolls her eyes, a sly smile spreading across her face."
            the_person "No, I'm not. But if you're going to cum inside me, you'd better make it worth it... I want to feel your cum dripping down my thighs, and know that I've been marked as your breeding vessel."
            $ the_person.update_birth_control_knowledge()
        elif the_person.opinion.creampies < 0:
            the_person "You're always trying to make me do stupid things, aren't you? Fine, just don't get me pregnant... I'm not ready for that kind of responsibility again, at least not yet. But I do want to feel your cock inside me, and know that you're serious about breeding me."
            "She looks up at you, her eyes serious as she warns you to be careful."
        else:
            the_person "You're always pushing me to my limits, aren't you? Fine, just make sure you pull out this time... I'm not ready to take on the responsibilities of motherhood just yet, but I do want to feel your cum on my skin, and know that you're still interested in breeding me."
            if the_person.kids == 0:
                the_person "I need you to pull out though... I'm not quite ready to be a mother, even with you. But I do want to feel your cum on my skin, and know that you're serious about breeding me. Maybe we can even try for a creampie next time, if you're lucky."
            elif the_person.kids == 1:
                the_person "I need you to pull out though... I've already got a kid, I don't need another one right now. But I do want to feel your cum on my skin, and know that you're still interested in breeding me. Maybe we can even try for a creampie next time, if you're lucky."
            else:
                the_person "I need you to pull out though... I've already got kids, I don't need another one right now. But I do want to feel your cum on my skin, and know that you're still committed to our breeding program. Maybe we can even try for a creampie next time, if you're lucky."
    else:
        if the_person.on_birth_control:
            the_person "Hmph, you want to breed me without protection? Well, I'm on the pill, so I guess it's fine... But don't think this means I'm going to go easy on you. I want to feel your cock deep inside my pussy, and know that you're serious about breeding me."
            $ the_person.update_birth_control_knowledge()
            "She smiles, her eyes sparkling with amusement as she invites you to take her without protection."

        elif the_person.has_taboo("vaginal_sex"):
            the_person "You're really not going to use a condom? I'm not on the pill, so we could end up with a little surprise... Like a baby bump, for instance. And I have to admit, the thought of it is kind of exciting."
            $ the_person.update_birth_control_knowledge()
            the_person "Or is this your sneaky plan to put a baby in me? To breed me like a fertile female and fill me up with your seed? Because if it is, I have to admit, I'm a little tempted."
            mc.name "I swear I'll pull out. I want our first time to be memorable, and I don't want to rush into anything we're not ready for... But I do want to feel your pussy wrapped around my cock, and know that you're serious about breeding with me."
            "She crosses her arms and gives a half-hearted sigh, her expression playful and teasing."
            the_person "Ugh, fine. But you better pull out, or you'll regret it... I'm not ready to be a mother just yet, but I do want to feel your cum on my skin, and know that you're serious about breeding me."

        else:
            the_person "You're really not going to use a condom? I'm not on the pill, so we could end up with a little surprise... Like a baby bump, for instance. And I have to admit, the thought of it is kind of exciting."
            $ the_person.update_birth_control_knowledge()
            the_person "Or is this your sneaky plan to put a baby in me? To breed me like a fertile female and fill me up with your seed? Because if it is, I have to admit, I'm a little tempted... And I want to feel your cock deep inside my pussy, and know that you're serious about breeding me."
            mc.name "I promise I'll pull out. It'll feel so much better without anything between us, and I want to make sure you're comfortable and happy... And I want to feel your pussy wrapped around my cock."
            the_person "God, I know. I'm trying to be rational here, not some lust-driven animal... But it's hard when you're looking at me like that, like you want to devour me whole... And I have to admit, I want to be devoured. I want to feel your cum on my skin, and know that you're serious about breeding me."
            "She huffs and puffs, her face flushing with excitement and anticipation."
            the_person "Fine, no condom. Just remember to pull out, got it? Good... And don't think this means I'm going to go easy on you. I want to feel your cum on my skin, and know that you're serious about breeding me. And maybe, just maybe, we'll make a baby out of this."
    return

label breeder_underwear_nudity_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > 30 - (the_person.opinion.skimpy_outfits * 5):
        the_person "You want to see me in my underwear, huh? It's about time you asked... I've been waiting for you to make a move and claim me as your breeding vessel. I'm ready to be filled with your cum and produce high-quality offspring."
        "She smiles, her eyes sparkling with amusement as she invites you to take off her clothes and explore her fertile body."
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "What are we waiting for then, let's get this off of you... And see what's underneath. I want to examine my breeding stock and make sure you're worthy of carrying my seed. I want to see your tits, your pussy, and your entire fertile body."
            the_person "Oh, you're eager, aren't you? Well, I suppose I can indulge you... This time. But don't think this means I'm going to go easy on you. I'm a breeder, and I expect to be treated as such. I want to be bred hard and filled with your cum."
        else:
            mc.name "Yeah, yeah. We've been over this. You're not exactly subtle about it... You've been teasing me for weeks, and I'm ready to take you to the next level. I want to fuck you hard and fill you up with my cum."
            the_person "Shut up! I just don't want you to get the wrong idea... But I suppose it's too late for that now. You've already seen me in my breeding attire, and I can tell you're ready to take me to the next level. I'm ready to be bred and filled with your seed."
            mc.name "Wrong idea? Like how you're not wearing anything under this skirt? Or how you're just begging to be bred and filled with my cum?"
            the_person "Ugh, fine. But don't say I didn't warn you... I'm not responsible for what happens next. You've been warned, and now it's time to take me and make me yours. I'm ready to be bred and filled with your seed."

    elif the_person.love > 15:
        the_person "You want me to strip down a little? It's about time, I was wondering why you were taking things so slow... Don't you want to see what's underneath and explore my fertile body? I'm ready to be bred and filled with your seed."
        "She smiles, her eyes sparkling with amusement as she invites you to take off her clothes and examine her breeding stock."
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "Oh, don't give me that. You know you want to show off... You've been teasing me for weeks, and now it's time to take it to the next level. I want to see your tits, your pussy, and your entire fertile body."
            the_person "Fine, but if this gets out of hand, I'm blaming you... I'm not responsible for what happens next. But I have to admit, I'm excited to see where this goes and what kind of breeding we can do together. I'm ready to be bred and filled with your seed."
            mc.name "Promise?"
            the_person "Yeah, yeah. Now get this [the_clothing.display_name] off... And let's see what happens next. I'm ready to take our breeding to the next level and make some babies."
        else:
            mc.name "Yeah, I know. You've been teasing me for weeks... And I'm not going to take it anymore. It's time to take you and make you mine, and start our breeding program together. I want to fuck you hard and fill you up with my cum."
            the_person "Teasing? I'm just being friendly... But I suppose it's too late for that now. You've already seen me in my breeding attire, and I can tell you're ready to take me to the next level. I'm ready to be bred and filled with your seed."
            mc.name "Right. Now let's get you out of these clothes... And see what's underneath. I want to examine my breeding stock and make sure you're worthy of carrying my seed. I want to see your tits, your pussy, and your entire fertile body."
            the_person "Ugh, fine. But don't think this means I'm going easy on you... I'm still in control here, and I expect to be treated as a breeder and a fertile female. I want to be bred hard and filled with your cum."

    else:
        the_person "You really want to see me like this? Fine, but don't say I didn't warn you... I'm not responsible for what happens next. You've been warned, and now it's time to take me and make me yours. I'm ready to be bred and filled with your seed."
        the_person "If you take my [the_clothing.display_name] I'll only have my underwear on, you know that?... And I'm not sure I'm ready for that. But I suppose it's too late for that now. You've already seen me in my breeding attire, and I can tell you're ready to take me to the next level."
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "Yeah, that's kind of the point... I want to see what's underneath and explore my breeding stock. I want to make sure you're worthy of carrying my seed and producing high-quality offspring. I want to see your tits, your pussy, and your entire fertile body."
            "She shakes her head and laughs to herself, her eyes sparkling with amusement."
            the_person "Whatever, but if you think I'm doing this because I want to... You're wrong. I'm doing it because I need to be bred and filled with your seed. I'm a breeder, and it's my duty to produce high-quality offspring."
        else:
            mc.name "Yeah, I know. You're not exactly shy... But I suppose it's too late for that now. You've already seen me in my breeding attire, and I can tell you're ready to take me to the next level. I want to fuck you hard and fill you up with my cum."
            the_person "Hey, I'm just being cautious... You can't blame a girl for being careful when it comes to breeding and producing high-quality offspring. But I suppose it's too late for that now. You've already seen me in my breeding attire, and I can tell you're ready to take me to the next level."
            mc.name "Of course not. Now let's get you out of these clothes... And see what's underneath. I want to examine my breeding stock and make sure you're worthy of carrying my seed. I want to see your tits, your pussy, and your entire fertile body."
            the_person "Fine, but don't think this means I'm going easy on you... I'm still in control here, and I expect to be treated as a breeder and a fertile female. I want to be bred hard and filled with your cum."
    return

label breeder_bare_tits_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > (40 - the_person.opinion.showing_her_tits * 5):
        the_person "Why do you want to see my tits now, all of a sudden? Like I don't already know you're checking me out and wanting to breed me."
        if the_person.has_large_tits:
            "She reluctantly shakes her chest for you, jiggling the [the_person.tits_description] hidden underneath her [the_clothing.display_name] and making you want to grab them and squeeze them hard."
        else:
            "She reluctantly shakes her chest and gives her [the_person.tits_description] a little jiggle, making you want to pinch her nipples and make her squeal."
        the_person "You're always so eager, aren't you? I guess I can show you, but don't get too excited... Yet. I want to make sure you're worthy of breeding me."
        if the_person.has_large_tits:
            mc.name "Oh, I've been looking. Now let's get those puppies out where I can enjoy them and suck on them hard."
        else:
            mc.name "Oh, I've been looking. Now let's get those cute little things out and see how sensitive they are to my touch."

    elif the_person.love > 25:
        the_person "Are you really sure you want to see my tits, [the_person.mc_title]? Are you ready to take our breeding to the next level?"
        if the_person.has_large_tits:
            "She rolls her eyes and shakes her chest, jiggling her nice [the_person.tits_description], barely restrained by her [the_clothing.display_name] and making you want to rip it off and take her right there."
        else:
            "She rolls her eyes and shakes her chest, giving her [the_person.tits_description] a little jiggle and making you want to grab her and kiss her hard."
        mc.name "Of course I am. You know I love your tits and I want to breed you so bad."
        the_person "Well, I suppose you're entitled to see them then... But don't think this means I'm going to start showing them off to everyone. I'm a breeder, not a slut."

    else:
        the_person "Wait, no! Don't look at me like that! You should at least ask a girl before you try and put her tits on full display and breed her like an animal!"
        mc.name "Come on, don't be like that. I bet your tits look great and I want to see them so bad."
        the_person "They do, but I still feel a little self-conscious about being naked around you, alright? I'm not sure I'm ready for this level of intimacy and breeding."
        mc.name "There's no need to be. Just relax and let me take your [the_clothing.display_name] off for you. I promise I'll be gentle and make it worth your while."
        the_person "Ugh, fine... But don't think this means I'm going to start showing off my body to everyone! I'm a breeder, not a slut, and I expect to be treated as such."
    return

label breeder_bare_pussy_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > (50 - the_person.opinion.showing_her_ass * 5):
        the_person "So you want to see my breeding slit, huh? Like I don't already know you're thinking about fucking me and filling me up with your seed."
        if the_person.has_taboo("touching_vagina"):
            "She reluctantly lifts her hips, allowing you to slowly remove her [the_clothing.display_name] and reveal her pussy, her juices already starting to flow in anticipation of your touch."
        else:
            "She lifts her hips, giving you a quick glimpse of her pussy before covering it back up, her eyes sparkling with amusement and invitation."
        the_person "Well, you got your wish. Don't say I didn't warn you... Now that you've seen my breeding slit, you'll have to take responsibility for what happens next."

    elif the_person.love > 35:
        the_person "You want to see my pussy, really? Are you sure you're ready for that? Are you ready to take our breeding to the next level?"
        if the_person.has_taboo("touching_vagina"):
            mc.name "I think I am. I've been wanting to see it for a while, to explore your fertile body and make you mine."
            the_person "Hmm, well... I suppose you've earned it. Just remember, you asked for this. You asked to see my breeding slit, and now you'll have to take responsibility for what happens next."
        else:
            mc.name "I've already felt it up, I thought I should see it too. I want to see the place where our babies will be made, where our love will grow."
            the_person "You really are persistent, aren't you? Fine, go on then. But don't think this means I'm going easy on you. I'm a breeder, and I expect to be treated as such."

    else:
        the_person "Hold on, you're not getting me out of my [the_clothing.display_name] that easily! You're not going to just take me and breed me like an animal, without even asking!"
        if the_person.has_taboo("touching_vagina"):
            mc.name "Come on, just let me see it. I promise I'll be gentle, I promise I'll make it worth your while."
            the_person "You're such a liar... But fine, go ahead. Just remember, you asked for this. You asked to see my breeding slit, and now you'll have to take responsibility for what happens next."
        else:
            mc.name "I've already felt your pussy up, I want to get a look at it now. I want to see the place where our babies will be made, where our love will grow."
            the_person "You're so pushy! Alright, but don't say I didn't warn you. I'm a breeder, and I expect to be treated as such. I expect to be bred hard and filled with your seed."
    return


# label breeder_facial_cum_taboo_break(the_person):

#     return

# label breeder_mouth_cum_taboo_break(the_person):

#     return

# label breeder_body_cum_taboo_break(the_person):

#     return
#==================================================================

label breeder_creampie_taboo_break(the_person):
    if the_person.wants_creampie:
        if the_person.knows_pregnant:
            the_person "You want to breed me, huh? Fine, I suppose it's about time someone filled me up with their seed and made me pregnant."
            "She sighs happily, seeming almost resigned to the idea of being a breeding vessel."

        elif the_person.on_birth_control:
            if the_person.has_significant_other:
                the_person "Oh my god, I'm such a naughty breeder! But I needed this creampie so badly, and I'm glad you could give it to me."
                the_person "Maybe if we're lucky, my [the_person.so_title] won't find out about our little breeding session."
                "She looks at you with a mischievous grin, her eyes sparkling with amusement and invitation."
            else:
                the_person "Oh my god, I needed this creampie so badly! Ah... I guess I'll just have to deal with the consequences of being a breeder and taking your seed."

        elif the_person.effective_sluttiness() > 75 or the_person.opinion.creampies > 0:
            if the_person.has_significant_other:
                the_person "You want to breed me? Fine, I suppose it's about time someone filled me up with their seed and made me pregnant."
                the_person "Maybe my [the_person.so_title] will finally notice how unhappy I am and do something about it... Or maybe they'll just get jealous of your breeding skills."

            else:
                the_person "You want to breed me? Fine, I suppose it's about time someone filled me up with their seed and made me pregnant."
                the_person "I guess I'll just have to deal with the consequences of being a breeder and taking your seed."

            "She sighs happily, but with a hint of annoyance and a desire for more breeding."
            the_person "How long until you're ready for round two? I want as much of your cum inside my pussy as possible, and I want to feel your seed growing inside me."
            the_person "Just don't expect me to be all happy and grateful about it... I'm a breeder, not a slave."

        else:
            if the_person.has_significant_other:
                the_person "Oh fuck... I'm such a terrible breeder!"
                "She sighs happily, but with a hint of guilt and a desire for more breeding."
                the_person "But that creampie felt so good... I think I might be addicted to your seed."
            else:
                the_person "Oh fuck, that was so risky... But it felt so good to have your cum inside me."
                "She sighs happily, but with a hint of annoyance and a desire for more breeding."
                the_person "I'll just have to hope you haven't knocked me up... Yet. We really shouldn't do this again, my luck is going to run out at some point."
                the_person "Besides, I'm not exactly thrilled about the idea of being tied down to a man right now... But I do love the idea of being a breeder and taking your seed."
    else:
        if the_person.knows_pregnant:
            the_person "Ugh, you're kidding me, right? You actually managed to breed me? I didn't think you had it in you."

        elif not the_person.on_birth_control:
            the_person "Seriously? You didn't even use protection? What if I get pregnant and have to carry your seed to term?"
            "She looks at you with a mix of shock and arousal, her eyes sparkling with excitement and anticipation."

            if the_person.has_significant_other:
                the_person "What if you just got me pregnant? I would be the worst [the_person.so_girl_title] of all time... But at the same time, I have to admit, the thought of being bred by you is kind of exciting."

            else:
                the_person "What if I get pregnant? I'm not ready for that kind of responsibility... But at the same time, I have to admit, the thought of being a mother and carrying your seed to term is kind of tempting."
            the_person "You'd better start taking care of me and making sure I'm happy and healthy... Because if I am pregnant, I'm going to need all the support I can get."
            the_person "Next time, we're using condoms, or we're not doing it at all... Unless you want to try to breed me again, that is."

        elif the_person.has_significant_other:
            the_person "Did you really just creampie me after I told you to pull out? You're such a naughty breeder!"
            "She sighs unhappily, but with a hint of arousal and excitement."
            the_person "God, I'm such a terrible [the_person.so_girl_title]. Maybe next time I'll make you wear a condom as punishment... Or maybe I'll just let you breed me again and see what happens."

        elif the_person.opinion.creampies < 0:
            the_person "Ugh, this is so unpleasant. Couldn't you have at least made it worth my while and given me a good orgasm?"
            "She rolls her eyes, but with a hint of arousal and excitement."
            the_person "Next time, at least have the decency to ask if I'm in the mood for a creampie... Or better yet, don't even bother if you're just going to be careless like this and not even try to make me cum."
            the_person "Next time, ask me first if I want a baby... And maybe we can even plan it out and make it a special occasion."

        else:
            the_person "Are you serious right now? You're really going to give me that attitude after you just...you know, bred me and filled me up with your seed?"
            "She huffs and crosses her arms, but with a hint of arousal and excitement."
            the_person "I swear, you're going to be the death of me... But at the same time, I have to admit, I kind of like the way you make me feel when you're inside me and breeding me."
            the_person "Fine, next time, at least have the decency to clean up after yourself... And maybe even take care of me and make sure I'm happy and healthy."
    return

label breeder_anal_creampie_taboo_break(the_person):
    if the_person.opinion.anal_creampies > 0:
        if the_person.effective_sluttiness() > 75 or the_person.opinion.anal_creampies > 1:
            if the_person.has_significant_other:
                the_person "Ugh, fine. I won't tell my [the_person.so_title] about this little breeding session. But don't think I'm enjoying this... Yet."
                "She says this while wincing in pleasure as you fill her ass with your cream, her body trembling with excitement and anticipation."
                the_person "Ugh, it's just... weirdly satisfying, I guess... To feel your cum inside my ass, and know that I'm being bred like a fertile female."
            else:
                the_person "Ugh, finally! You're actually doing this! I've been waiting for this forever... To feel your cum inside my ass, and know that I'm being bred like a fertile female."
                the_person "Okay, okay, I know it's wrong, but... it feels so good... To be filled up with your seed, and know that I'm being used for my intended purpose."
            "She bites her lip, trying to contain her excitement and anticipation, but her eyes sparkle with amusement and invitation."
            the_person "I guess it's nice... having your cum in my ass... It's like I'm being marked as your breeding vessel, and I love it."
        else:
            if the_person.has_significant_other:
                the_person "Ugh, what are you doing? My [the_person.so_title] is going to kill me if he finds out about this little breeding session..."
                "She moans softly as you continue to fill her ass, her body trembling with excitement and anticipation."
                the_person "Ugh, I can't believe I'm letting you do this... It's just so taboo, and yet so exciting... To be bred like a fertile female, and filled up with your seed."
            else:
                the_person "Ugh, promise you'll do this again? I can't believe I'm saying this, but... it's kind of hot... To be filled up with your cum, and know that I'm being used for my intended purpose."
                the_person "All that cum in my tight little ass... It's like I'm being bred like a fertile female, and I love it."

    else:
        if the_person.has_significant_other:
            the_person "Ugh, seriously? You couldn't pull out? My [the_person.so_title] is going to kill me... And yet, I have to admit, it's kind of exciting to be bred like this."
            "She starts to squirm and try to get away from you, but her eyes sparkle with amusement and invitation."
            the_person "Next time, just shoot your load on my ass, okay? I want to feel your cum on my skin, and know that I'm being used for my intended purpose."
        elif the_person.opinion.anal_creampies < -1:
            the_person "Ugh, seriously? You can't even follow simple instructions? My ass is not a creampie dispenser, but I have to admit, it's kind of exciting to be bred like this."
        else:
            the_person "Ugh, not inside! My ass is not a dirty little secret, although that sounds kind of hot... To be bred like a fertile female, and filled up with your seed."
    return

label breeder_dual_penetration_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 75:
        the_person "Ugh, you're really going to breed me like a fertile female, aren't you? Fine, but don't expect me to go easy on you... I want to feel your cocks deep inside me, and know that I'm being used for my intended purpose."
        "She spreads her legs and invites you to take her, her eyes sparkling with excitement and anticipation."
        mc.name "Don't worry, it'll be worth it. You'll be filled up with our seed, and know that you're being bred like a fertile female."
        the_person "I doubt that, but whatever. Just make sure you're gentle and don't hurt me... I want to be able to take your cocks again and again."

    elif the_person.love >= 60:
        the_person "You're really sure about this? It's going to be a tight fit... But I have to admit, the thought of being bred by two cocks at once is kind of exciting."
        mc.name "I'll make sure it fits perfectly. I want to feel your pussy wrapped around my cock, and know that you're being used for your intended purpose."
        the_person "Ugh, just be careful not to hurt me, okay? I don't want any scars... But at the same time, I want to feel your cocks deep inside me, and know that I'm being bred like a fertile female."

    else:
        if the_person.has_taboo("vaginal_sex"):
            the_person "Are you sure my pussy wouldn't be tight enough for you? I mean, I've never done this before... But I have to admit, the thought of being bred by two cocks at once is kind of exciting."
            mc.name "It's okay, I'll make it fit. Just try to relax and let us take care of you... We'll make sure you're filled up with our seed, and know that you're being bred like a fertile female."
            the_person "Ugh, this is so embarrassing... But at the same time, I want to feel your cocks deep inside me, and know that I'm being used for my intended purpose."
        else:
            the_person "Ugh, fine. I guess we're doing this, right? I mean, I can't back out now... But I have to admit, the thought of being bred by two cocks at once is kind of exciting."
            mc.name "Are you sure you're ready for this? We're going to breed you like a fertile female, and fill you up with our seed."
            the_person "Yeah, whatever. Let's just get this over with... I want to feel your cocks deep inside me, and know that I'm being used for my intended purpose."
    return

label breeder_sleepover_yourplace_response(the_person): #Invited her over to spend the night
    if the_person.love >= 70:
        the_person "Fine, I'll come over and let you breed me like a female in heat. But don't think this means I'm going to go easy on you... I want to feel your cock deep inside me, and know that I'm being used for my intended purpose."
        mc.name "I wouldn't dream of it. We'll just have a good time, and maybe even make some babies."
        the_person "Yeah, yeah. Just don't get too close, okay? I don't like cuddling or anything... But I do like being bred and filled up with your seed."

    elif the_person.sluttiness >= 80:
        the_person "Oh god, I'm so ready to be bred like a fertile female! Make sure you have everything ready, so we can have a great night of breeding and making babies."
        mc.name "I've got everything we need. I'll make sure you're filled up with my seed, and we'll have a great time doing it."

    else:
        the_person "I guess I could come over... But don't expect me to do anything I'm not comfortable with, okay? I'm not sure I'm ready for this level of intimacy and breeding."
        mc.name "Don't worry, I'll be gentle and make sure you're comfortable. We'll take it slow and see where things go."
    return

label breeder_sleepover_herplace_response(the_person): #Spending the night at her place
    if the_person.love >= 70:
        the_person "Fine, come over and stay the night, but don't think this means I'm going to go easy on you... I want to feel your cock deep inside me, and know that I'm being used for my intended purpose."
        mc.name "I wouldn't dream of it. We'll just have a good time, and maybe even make some babies."
        the_person "Yeah, yeah. Just don't get too close, okay? I don't like cuddling or anything... But I do like being bred and filled up with your seed."

    elif the_person.sluttiness >= 80:
        the_person "Oh god, I'm so ready to be bred like a fertile female! Come over and let's have a wild night of breeding and making babies."
        mc.name "I'll be right there. I'll make sure you're filled up with my seed, and we'll have a great time doing it."

    else:
        the_person "I guess you can come over... But don't expect me to do anything I'm not comfortable with, okay? I'm not sure I'm ready for this level of intimacy and breeding."
        mc.name "Don't worry, I'll be gentle and make sure you're comfortable. We'll take it slow and see where things go."
    return

label breeder_sleepover_yourplace_sex_start(the_person):
    "[the_person.title] saunters over to you, her hips swaying seductively as she moves. Her expression is a mix of annoyance and desire, but her eyes sparkle with excitement and anticipation."
    the_person "Fine, let's get this breeding session started. I'm ready to be filled up with your seed and make some babies."
    "She reaches out and grabs your cock, her hand wrapping around it tightly as she pulls you towards her."
    the_person "Don't expect me to be all lovey-dovey or anything... I just want to be bred like a fertile female in heat and feel your cum inside me."
    return

label breeder_sleepover_herplace_sex_start(the_person):
    the_person "Finally, it's time to get this breeding session started! Get over here and fill me up with your seed."
    "She smirks and spreads her legs wide, her pussy glistening with anticipation and desire."
    mc.name "Are you ready to be bred like a fertile female?"
    the_person "Hah! Like I need to be ready for this. I was born to be bred and make babies. Just get in here and do your worst."
    "She leans back on the couch, her legs spread wide in invitation as she awaits your cock."
    the_person "Hurry up, I'm not getting any younger! I need to be bred and filled up with your seed before it's too late."
    "She reaches out and grabs your cock, her hand wrapping around it tightly as she pulls you towards her."
    the_person "Come on, let's make some babies! I'm ready to be bred like a fertile female in heat and feel your cum inside me."
    return

label breeder_sleepover_impressed_response(the_person):  #If you've made her cum a lot
    the_person "Ugh, you're really good at breeding me... I have to admit, I'm impressed by your skills."
    "She rolls her eyes and smirks, trying to hide her true feelings of desire and satisfaction."
    mc.name "You want more?"
    the_person "Hmph, maybe. But don't think you've won me over or anything. I'm still a breeder, and I expect to be treated as such."
    "[the_person.title] lies down in bed, her breathing still ragged from the previous rounds of breeding."
    the_person "I might be able to go for another round... But don't get too excited, I'm not making any promises! Just make sure you're ready to fill me up with your seed again."
    return

label breeder_sleepover_good_response(the_person):  #If you've made her cum
    the_person "Ugh, fine. That wasn't too terrible, I suppose. You're actually pretty good at breeding me."
    "She rolls her eyes and smirks, trying to hide her true feelings of desire and satisfaction."
    mc.name "You want more?"
    $ the_person.draw_person(position = "missionary")
    the_person "Hmph, maybe. But don't think you've won me over or anything. I'm still a breeder, and I expect to be treated as such."
    "[the_person.title] lies down in bed, her breathing still ragged from the previous round of breeding."
    the_person "Could you give me another pounding before we go to sleep? I want to feel your cock deep inside me again, and I want to be filled up with your seed."
    return

label breeder_sleepover_bored_response(the_person):  #If she hasn't cum yet
    the_person "Ugh, is that the best you can do? I was expecting more than that from you... I want to be bred like a fertile female, not just played with."
    "She crosses her arms and looks at you with a bored expression, clearly unimpressed by your breeding skills."
    mc.name "What's wrong?"
    the_person "You know, just do better. I expect more from you than this... I want to feel your cock deep inside me, and I want to be filled up with your seed."
    "She rolls her eyes and smirks, still rubbing her pussy in anticipation of being bred."
    the_person "You'd better step it up if you want to keep me interested... I'm a breeder, and I expect to be treated as such."
    return

