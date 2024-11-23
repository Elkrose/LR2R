### PERSONALITY CHARACTERISTICS ###
# yandere (A term for a person who is initially loving and caring to someone they like a lot until their romantic love, admiration and devotion becomes feisty and mentally destructive in nature through either overprotectiveness, violence, brutality or all three combined. Yandere characters are mentally unstable, deranged, and use violence or emotional abuse as an outlet for their emotions. Yandere are usually, but not always, female characters.)
# "Yandere" (JP) is a term for a character whose love, admiration, and devotion to their love interest is so strong that it causes them to become mentally unstable. At first they are very sweet, loving, and affectionate like a normal deredere, but over time they begin exhibiting signs of being mentally sick, such as extreme jealousy or feelings of possession, and start to grow more and more mentally unstable. Their love is expressed as an excessive obsession and possessiveness towards their love interest. They become so attached to their love interest that it's impossible to let go and they may even use violence towards anyone who "threatens" their relationship.
#They entrust themselves to their love interest, trusting in their love interest's kindness. They probe the deepest recesses of their love interest's heart to more perfectly form their greatest self within their love interest. Some will go so far as to behave in immoral and troubling ways. They will not care about the negative effect their behaviors can have on others, including their love interest, because they only care about their feelings. 
#Yuno Gasai from Future Diary, pretty much defined the trope. She has every classic yandere characteristic you can think of and there really is no more accurate example than her. It also helps that she's one of the most important characters in that show so you see her alot.
#==================================================================
# update all the following the_person and actions with kuudere personality. Remember the_person is female, and mc.name is male. Use Reina Aharen from Aharen-San for ideas, keep to the structure and don't use the same dialogs:```
# update all the following the_person and actions with yandere personality. Remember the_person is female, and mc.name is male. Use Yuno Gasai from Future Diary for ideas, keep to the structure and don't use the same dialogs:```
#add more yandere personality, use different words, and movements on a new line in quotations.

### DIALOGUE ###



label yandere_introduction(the_person):
    mc.name "Excuse me, could I bother you for a moment?"
    "You approach her and she turns around, her eyes narrowing with an unsettling intensity."
    the_person "What do you want?"
    mc.name "I know this is sudden, but I just saw you walking by and I felt this overwhelming urge to talk to you."
    "She raises an eyebrow, her expression cold and calculating."
    the_person "Why should I care?"
    $ the_person.change_happiness(-1)
    mc.name "Because... there's just something about you that makes me feel alive. I want to know everything about you."
    "She smirks, a hint of madness in her eyes."
    the_person "My name is [the_person.name]. And you are?"
    $ the_person.set_title()
    $ the_person.set_possessive_title()
    mc.name "I'm [mc.name]. It's a pleasure to meet you, [the_person.title]."
    "She takes a step closer to you, her eyes glinting with a dangerous excitement."
    the_person "Yes, a pleasure indeed. I look forward to getting to know you better, [mc.name]."
    $ the_person.change_happiness(2)
    return

label yandere_greetings(the_person):
    if the_person.love < 0:
        the_person "Oh, great, another annoying person to deal with. What do you want?"
    elif the_person.happiness < 90:
        the_person "Ugh, hi. I'm not really in the mood for anything right now."
    else:
        if the_person.sluttiness > 60:
            if the_person.obedience > 180:
                the_person "Hello there, [the_person.mc_title]. You're here to see me, aren't you? I can tell just by looking at you."
            else:
                the_person "Well, well, well. Look who's come to pay me a visit, [the_person.mc_title]. You're just in time for some fun."
        else:
            if the_person.obedience > 180:
                the_person "Hello, [the_person.mc_title]. It's been a while."
            else:
                the_person "Hey, [the_person.mc_title]. What brings you here today?"
    return

label yandere_sex_responses_foreplay(the_person):
    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] purrs with delight, her eyes flashing with excitement."
        else:
            "[the_person.possessive_title!c] giggles softly, her voice dripping with lust."
            the_person "That... that feels amazing."

    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            the_person "Oh, yes! I love the way you touch me! Make me yours!"
            "[the_person.possessive_title!c] wraps her legs around you, pulling you closer."
        else:
            the_person "Oh... Oh, that's... That's so good!"
            "[the_person.possessive_title!c] begins to rock her hips, seeking more contact."

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            the_person "It feels like you're going to make me lose my mind! I need more, I need everything you have to give!"
            "[the_person.possessive_title!c] reaches out to run her fingers through your hair, pulling you closer."
        else:
            the_person "Mmm, keep going, [the_person.mc_title]. Don't ever stop."
            "[the_person.possessive_title!c] starts to grind against you, her breath coming in ragged gasps."

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "I'm yours to command, [the_person.mc_title]. Use me, break me, make me yours!"
            "[the_person.possessive_title!c] starts to undo your clothes, eager to feel your skin against hers."
        else:
            the_person "Touch me, [the_person.mc_title], I'm all yours to do with as you please!"
            "[the_person.possessive_title!c] starts to kiss your neck, her lips leaving trails of fire on your skin."
    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                the_person "Oh, I'm going to shatter soon. You're driving me mad with desire!"
                "[the_person.possessive_title!c] starts to ride you, her eyes rolling back in pleasure."
            else:
                the_person "Your touch is unlike anyone else's. It's as if you were made for me alone."
                "[the_person.possessive_title!c] starts to whisper dirty things in your ear, her breath hot against your skin."
        else:
            the_person "Don't stop! You're so close to making me cum—don't you dare stop!"
            "[the_person.possessive_title!c] starts to moan loudly, her voice echoing in the room."

    return

label yandere_sex_responses_oral(the_person):
    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] purrs with delight, her eyes sparkling with lust."
            the_person "Oh, [the_person.mc_title], you're going to make me cum just from that."
        else:
            "[the_person.possessive_title!c] blushes, her cheeks flushed with excitement."
            the_person "Oh fuck, you're really going to... Oh fuck yes..."
            "[the_person.possessive_title!c] starts to moan softly, her hips bucking slightly."

    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            the_person "Mmm, I love the way you taste."
            "[the_person.possessive_title!c] starts to thrust her hips, seeking more contact."
        else:
            the_person "Fuck me that feels real nice, [the_person.mc_title]."
            "[the_person.possessive_title!c] starts to run her fingers through your hair, pulling you closer."

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            the_person "Eat me out [the_person.mc_title], your tongue is a magic wand."
            "[the_person.possessive_title!c] starts to grip your hair, pulling you deeper into her."
        else:
            the_person "That feels so good, you have no idea, [the_person.mc_title]."
            "[the_person.possessive_title!c] starts to kiss your neck, her lips leaving trails of fire on your skin."

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "Mmm, lick that pussy! Ah, [the_person.mc_title], you're making me insane!"
            "[the_person.possessive_title!c] starts to grind against your face, her hips bucking wildly."
        else:
            the_person "Oh god, yes! Yes, [the_person.mc_title], you're making me cum!"
            "[the_person.possessive_title!c] starts to cry out, her orgasm building."
    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                the_person "Fuck fuck fuck, that's it right there, [the_person.mc_title]!"
            else:
                the_person "My [the_person.so_title] never eats me out like this, [the_person.mc_title]!"
                the_person "Make me cum my brains out and forget about him!"
                "[the_person.possessive_title!c] starts to scream, her orgasm overwhelming her."
        else:
            the_person "Don't stop! You're going to make me cum, don't you dare stop, [the_person.mc_title]!"
            "[the_person.possessive_title!c] starts to shake, her orgasm tearing through her."

    return

label yandere_sex_responses_vaginal(the_person):
    if the_person.energy < 10:
        call low_energy_sex_responses_vaginal(the_person) from _vt_yandere_call_low_energy_sex_responses_vaginal_10
        return

    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            $ play_moan_sound()
            "[the_person.possessive_title!c] wraps her legs around you, pulling you closer."
            the_person "How does my pussy feel? I hope I'm tight enough for you. You're mine now."
            "As you thrust, [the_person.possessive_title!c] begins to rub her clit with one hand, her other hand gripping your shoulder possessively."
        else:
            "[the_person.possessive_title!c] pushes you away, her eyes burning with a fiery intensity."
            the_person "Don't you dare stop, not now... not ever."

    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            the_person "Oh fuck, I never get tired of being filled by you!"
            "As you continue, [the_person.possessive_title!c] starts to rock her hips, meeting your thrusts with a wild abandon."
        else:
            the_person "Oh... Oh fuck me, you're the only one who can make me feel this way..."
            "Her hands grip your shirt, pulling you closer as she arches her back, offering herself to you."

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            the_person "Mmm, you feel so good, so perfect inside me!"
            "With a possessive smile, [the_person.possessive_title!c] starts to ride you, her hips moving in a hypnotic rhythm."
        else:
            the_person "Ah, fuck me just like that, don't stop..."
            "Her nails dig into your skin, her eyes burning with a fierce intensity as she urges you on."

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "That's right, use me like your dirty little slut and fuck my pussy hard!"
            "With a wicked grin, [the_person.possessive_title!c] starts to fuck you back, her hips snapping wildly."
        else:
            the_person "Oh fuck yes, fuck yes, you're mine now!"
            "Her legs wrap around you like a vice, her heels digging into your ass as she rides you hard."
    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                the_person "Fuck! I'm... I'm yours now, and you're going to make me cum!"
                "As you approach climax, [the_person.possessive_title!c] starts to moan loudly, her voice echoing through the room."
            else:
                the_person "Your cock is stretching me out, my [the_person.so_title] is never going to be enough for me after this!"
                "Her eyes flash with a possessive fury as she starts to fuck you with renewed vigor."
                the_person "Oh well, fuck him! You're mine now, and you're going to make me cum!"
        else:
            the_person "Don't stop fucking me! You're going to make me cum, and I'm never letting you go after this!"
            "Her body tenses, her eyes locked on yours as she starts to climax, her pussy clenching around you."
    return

label yandere_sex_responses_anal(the_person):
    if the_person.energy < 10:
        call low_energy_sex_responses_anal(the_person) from _vt_yandere_call_low_energy_sex_responses_anal_10
        return

    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            the_person "Just go slowly, my dear [the_person.mc_title]. I need to savor every moment with you..."
            "Her voice drips with a possessive tone, as if she owns you. She gently runs her fingers through your hair, pulling you closer."
        else:
            $ the_person.call_dialogue("surprised_exclaim")
            the_person "Deep breaths, [the_person.title], deep breaths... I need to maintain control."
            "She pants to herself, doing her best to keep control of the situation, but her eyes never leave yours. She shifts her weight, her hips tilting towards you."

    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            $ the_person.call_dialogue("surprised_exclaim")
            the_person "I'm never going to get used to being stretched out like this... but I wouldn't want it any other way."
            "She moans softly as you thrust into her, her hands gripping your shoulders for leverage. She lifts her hips to meet your pace."
        else:
            the_person "Oh... Oh fuck, my ass is on fire! [the_person.title]!"
            "Her voice rises in a plea, her body writhing under you as you fuck her."

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            the_person "Gah! Ah! Fuck, [the_person.mc_title]! You're so good at this!"
            "Her words are punctuated by gasps and moans, her hips meeting yours in a frantic rhythm. She reaches out to touch your face, her eyes burning with desire."
        else:
            the_person "God, I won't be able to sit for a week after this... but I wouldn't want to."
            "She pants heavily, her body taut with pleasure. She moves her hips in a slow circle, teasing you with the promise of more."

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            if mc.condom:
                the_person "Give it to me, punish that slutty ass with your big cock! Make me yours!"
                "Her voice is husky with lust, her body trembling with anticipation. She lifts her hips to meet your thrusts, her eyes locked on yours."
            else:
                the_person "Give it to me, fuck my horny asshole raw! I want to feel you deep inside me!"
                "Her words are a sensual command, her body arching towards you. She wraps her legs around your waist, pulling you closer."
        else:
            the_person "Ah! Why does your cock have to be so fucking big? It's making me crazy!"
            "Her voice is a mix of frustration and pleasure, her body writhing under you as she tries to take all of you."
    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                the_person "Fuck, I can't believe I'm going to cum from your cock up my ass! I'm all yours!"
                "Her words are a declaration of ownership, her body trembling with pleasure. She reaches out to touch your face, her eyes burning with desire."
            else:
                the_person "Wreck my ass, [the_person.mc_title]! Send me back to my [the_person.so_title] ruined and used by you!"
                the_person "You're all I need, [the_person.mc_title]. I don't want anyone else, only you!"
                "Her voice is a passionate whisper, her body arched towards you as she climaxes. She wraps her legs around your waist, pulling you closer."
        else:
            $ the_person.call_dialogue("surprised_exclaim")
            the_person "I can't believe it, but I think I'm going to cum soon! And I want you to be the one to make me do it!"
            "Her eyes burn with a fiery intensity, as if she's about to consume you. She shifts her weight, her hips tilting towards you."
            "She reaches out to touch your face, her fingers tracing your lips as she moans softly. Her body shudders under you, her climax approaching."

    return

label yandere_climax_responses_foreplay(the_person):
    if the_person.sluttiness > 50:
        the_person "You're mine, all mine, [the_person.mc_title]... and I'm going to make you watch as I cum."
        "Her voice is a sultry whisper, her body arching towards you as she teases the edge of climax. She gently runs her fingers through your hair, pulling you closer."
        "As you move, she moans softly, her hips meeting yours in a frantic rhythm. Her eyes never leave yours, filled with a fiery intensity."
    else:
        $ the_person.call_dialogue("surprised_exclaim")
        the_person "You're going to make me cum! And when I do, I'm going to make you suffer!"
        "Her voice is a mix of pleasure and threat, her body trembling with anticipation. She leans in close, her breath hot against your ear."
        "She wraps her legs around your waist, pulling you closer as she moves her hips in a slow circle, teasing you with the promise of more."
    return

label yandere_climax_responses_oral(the_person):
    if the_person.sluttiness > 70:
        the_person "You're all mine, [the_person.mc_title], and I'm going to make you feel how much I love you when I cum."
        "Her voice is a sultry whisper, her body trembling with pleasure. She gently runs her fingers through your hair, pulling you closer."
        "As you continue, she moans softly, her hips moving in time with your actions. Her eyes never leave yours, filled with a fiery intensity."
        "She reaches out to touch your face, her fingers tracing your lips as she shudders with pleasure."
    else:
        the_person "Oh my god, you're good at that! I'm going to... I'm going to cum! And when I do, I'm going to make you suffer!"
        "Her voice is a mix of pleasure and threat, her body arching towards you as she teases the edge of climax. She leans in close, her breath hot against your ear."
        "She wraps her legs around your waist, pulling you closer as she moves her hips in a slow circle, teasing you with the promise of more."
    return

label yandere_climax_responses_vaginal(the_person):
    if the_person.sluttiness > 70:
        if the_person.arousal_perc > 120:
            the_person "You're all mine, [the_person.mc_title], and I'm going to make you watch as I cum."
            "Her voice is a sultry whisper, her body arching towards you as she teases the edge of climax. She gently runs her fingers through your hair, pulling you closer."
            "As you move, she moans softly, her hips meeting yours in a frantic rhythm. Her eyes never leave yours, filled with a fiery intensity."
        else:
            the_person "Ah! More! I'm going to... Ah! Cum! Fuck!"
            "Her voice is a mix of pleasure and demand, her body trembling with anticipation. She wraps her legs around your waist, pulling you closer."
            "She reaches out to touch your face, her fingers tracing your lips as she shudders with pleasure."
        "She closes her eyes and squeals with pleasure."
    else:
        the_person "Oh god, I'm going to... Oh fuck me! Ah!"
        "Her voice is a mix of surprise and pleasure, her body arching towards you as she teases the edge of climax. She leans in close, her breath hot against your ear."
    return

label yandere_climax_responses_anal(the_person):
    if the_person.sluttiness > 70:
        if the_person.arousal_perc > 120:
            the_person "Ah yes, shove your big cock into my slutty ass. Make your little bitch cum!"
        else:
            the_person "Oh fuck, your cock feels so huge in my ass! It's going to make me cum!"
        the_person "Ah! Mmhmmm!"
    else:
        the_person "Oh fucking shit, I think you're going to make me..."
        "She barely finishes her sentence before her body is racked with pleasure."
        the_person "Cum!"
    return

label yandere_clothing_accept(the_person):
    if the_person.obedience > 180:
        the_person "You want me to wear that? Oh, [the_person.mc_title], I'll wear whatever you want me to wear. It's all yours."
        "Her voice is a mix of compliance and possession, her eyes never leaving yours as she submits to your request. She leans in closer, her body language indicating a willingness to please."
        "As you help her put on the outfit, she moans softly, her hips moving in time with your actions. Her eyes never leave yours, filled with a fiery intensity."
    else:
        the_person "Hey, thanks. That's a good look, I like it."
        "She says it casually, but there's a hint of excitement in her voice as she imagines wearing the outfit. She twirls around, showing off her new attire, and smiles at you."
    return

label yandere_clothing_reject(the_person):
    if the_person.should_wear_uniform:
        the_person "I suppose it's only natural for me to fit in, don't you think? I'll go ahead and get dressed in this uniform. After all, I wouldn't want to stand out too much."
    elif the_person.obedience > 180:
        the_person "I'm not sure this outfit is suitable for me, but I suppose it's the thought that counts. I'll just have to make do."
    else:
        if the_person.sluttiness > 60:
            the_person "Oh, this is a bit too revealing, don't you think? I wouldn't want to give the wrong impression. But thank you for the suggestion."
        else:
            the_person "I think this outfit needs a bit more... pizzazz. I'll have to find something that suits my style better. Thanks for the idea, though."
    return

label yandere_clothing_review(the_person):
    if the_person.outfit.cum_covered:
        if (the_person.sluttiness > 40 and the_person.opinion.being_covered_in_cum >=0) or the_person.opinion.being_covered_in_cum > 0:
            the_person "Hmm, it seems I've made quite a mess... I suppose I should clean up before I make myself too uncomfortable."
            "[the_person.title] begins to gently wipe away the cum from her outfit, her eyes gleaming with a sinister intent."
            "As she wipes, she starts to hum a soft melody, the sound of her voice sending shivers down your spine."
        else:
            the_person "Ugh, this cum is everywhere! I'll have to clean it all up before I can continue."
            "[the_person.title] methodically wipes herself down, ensuring that not a single drop of cum remains."
            "Her movements are graceful and precise, each stroke of her hand calculated to remove every last trace of the mess."

    if the_person.obedience > 180:
        the_person "I suppose I should tidy myself up before we continue, don't you think? I wouldn't want to be any less than perfect for you."
    else:
        if the_person.sluttiness > 40:
            the_person "You're so understanding about my little... mishap. I'll be right back, I just want to freshen up a bit."
            "[the_person.title] disappears into the bathroom, the sound of water running in the background."
        else:
            the_person "I need to make sure I look my best for you. Wait here, I'll be right back after I fix myself up."
            "[the_person.title] strides into the bathroom, leaving you alone in the room."
    $ the_person.apply_planned_outfit(show_dress_sequence = True)
    return

label yandere_strip_reject(the_person, the_clothing, strip_type = "Full"):
    if the_person.obedience > 180:
        the_person "Oh, I don't think I'm ready to let go of my [the_clothing.display_name] just yet, if you don't mind. I'm quite fond of it."
        "[the_person.title] runs her hands over the fabric of her [the_clothing.display_name], her eyes glazing over as she becomes lost in thought."
    elif the_person.obedience < 70:
        the_person "No, no, no, I'll decide when and if anything comes off, okay? Don't rush me."
        "[the_person.title] crosses her arms over her chest, her expression stern and unyielding."
    else:
        the_person "Hmm, I think we should take things slow, don't you? Maybe we can start with something else and work our way up. Then, if you're lucky, I might let you take off my [the_clothing.display_name]."
        "[the_person.title] begins to unbutton her shirt, revealing a hint of her cleavage as she teases you with the prospect of more."
    return

label yandere_strip_obedience_accept(the_person, the_clothing, strip_type = "Full"):
    "[the_person.title] giggles uncontrollably as you begin to peel her [the_clothing.display_name] off her body."
    if the_person.obedience > 180:
        the_person "Oh, please, let's not be hasty. I think I'll keep my [the_clothing.display_name] on for now."
        "[the_person.title] places her hand on yours, trying to gently guide it away from her body."
    else:
        the_person "Wait, stop! I don't know if I'm ready for this..."
        "[the_person.title] tries to squirm away from your grasp, but you hold her firmly in place."
    return

label yandere_grope_body_reject(the_person):
    if the_person.effective_sluttiness("touching_body") < 5: #Fail point for touching shoulder
        the_person "Ah! You startled me!"
        "[the_person.title] jumps away from your touch, her eyes wide with surprise."
        the_person "What's wrong with you, sneaking up on me like that?"
        mc.name "I'm sorry, I didn't mean to scare you."
        the_person "It's fine, just be more careful next time, okay? I don't want you to think I'm some kind of... fragile thing that needs to be handled with care."
        "She says it with a hint of a smile, but you can tell she's still a little shaken up."
    else: #Fail point for touching waist
        the_person "Ow! What are you doing?"
        "[the_person.title] grabs your hand and twists it away from her waist."
        the_person "Stop that! You're being very touchy-feely, and I'm not comfortable with it."
        mc.name "I'm sorry, I didn't mean to upset you."
        the_person "It's not about upsetting me, it's about respect. I need you to respect my personal boundaries."
        "She looks at you sternly, her eyes flashing with a hint of anger."
    return

label yandere_sex_accept(the_person, the_position):
    if the_person.sluttiness > 70:
        if the_person.obedience < 70:
            the_person "I've been waiting for this moment, [the_person.mc_title]. Let's make it unforgettable."
            the_person "I've been thinking about this all day, and I can't wait to feel you inside me."
            the_person "You're going to make me scream your name, [mc.name]. I can feel it."
            the_person "Come here, [the_person.mc_title]. I want to feel your hands on me, your lips, your everything."
            the_person "I'm yours, [mc.name]. Do with me as you please."
        else:
            if the_position.skill_tag == "Foreplay":
                the_person "You're so good at that, [the_person.mc_title]. My heart is racing just thinking about it."
                the_person "I love the way you touch me, [mc.name]. It's like you were made for me."
                the_person "I want to feel you inside me, [the_person.mc_title]. Make me yours forever."
            elif the_position.skill_tag == "Oral":
                if "getting head" in the_position.opinion_tags:
                    the_person "Mmm, [mc.name], I can't wait any longer. Make me cum, my love."
                    the_person "You're going to make me forget my own name, [the_person.mc_title]. And that's exactly what I want."
                else:
                    the_person "I can't resist you any longer, [mc.name]. You're going to make me scream your name."
                    the_person "I want to feel your breath on me, your tongue, your everything."
            else:
                the_person "Oh yes, [mc.name], I need you to fill me up and take me away."
                the_person "I'm yours, [the_person.mc_title]. Use me however you want."
    else:
        the_person "Come here, [mc.name]. I need you now."
        the_person "I don't care what we do, as long as it's together."
    return

label yandere_sex_obedience_accept(the_person):
    if the_person.sluttiness > 70:
        the_person "Oh, [the_person.mc_title], I'm so sorry. I shouldn't even be thinking about this, but... I just can't resist you."
        the_person "I should be ashamed of myself, but all I can think about is how much I want you to use me, [mc.name]."
        the_person "You're going to make me do things I never thought I'd do, [the_person.mc_title]. And I can't wait."
    else:
        if the_person.obedience > 180:
            the_person "If that's what you want, [mc.name], then I'll do as you say. I'll give you everything you want."
        else:
            the_person "I shouldn't even be considering this, but... if you really want to try it out, I won't say no."
            the_person "After all, life's too short, right? And if it's you, [the_person.mc_title], I know it'll be amazing."
    return

label yandere_sex_gentle_reject(the_person):
    if the_person.sluttiness > 50:
        the_person "Not yet, [mc.name]. I need you to make me feel something first. Make me feel alive."
        the_person "I want you to touch me, kiss me, make me moan. And then, and only then, can we think about going any further."
    else:
        the_person "Wait, [mc.name]. I just... I don't think I'm ready for this. I want to feel something, but I don't want it to be too much."
        the_person "Let's keep it light and fun, okay? I just need some time to get comfortable."
        the_person "Take your time, [the_person.mc_title]. Explore me, taste me, make me shiver. But don't rush it, okay? I need to feel safe."
    return

label yandere_sex_angry_reject(the_person):
    if the_person.has_significant_other:
        the_person "What? I have a [the_person.so_title], so you can forget about doing anything like that. Ever."
        "Her eyes flash with a dangerous intensity, and she takes a step closer to you."
        mc.name "I'll make sure you never touch another man, especially not [the_person.SO_name]."
        "She leans in close, a cold smile spreading across her face."
        the_person "You should be grateful I'm even talking to you."
        "[the_person.title] glares at you, then walks away."
    elif the_person.sluttiness < 20:
        the_person "I'm sorry, what!? No, you've massively misread the situation, get the fuck away from me!"
        "Her voice is icy, her words laced with a threat."
        the_person "I don't know what kind of game you think you're playing, but it's over."
        "[the_person.title] glares at you and steps back, her eyes never leaving yours."
    else:
        the_person "What? That's fucking disgusting, I can't believe you'd even suggest that to me!"
        "Her face twists with anger, her eyes blazing with fury."
        the_person "You're lucky I don't kill you where you stand for even thinking about it."
        "[the_person.title] glares at you and steps back, her hands clenched into fists."
    return

label yandere_seduction_response(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 50:
            the_person "Oh, I can tell you're craving something right now. And I'm just the girl to satisfy that craving."
            "She smirks, her eyes gleaming with a sinister light."
            the_person "Let me take care of you, and you'll never want for anything else again."
        else:
            the_person "You want me, don't you? And I want you too. Come on, let's go somewhere private."
            "Her voice is low and seductive, but with an underlying edge of threat."
            "[the_person.title] takes your hand and leads you off to find some place out of the way."
    else:
        if the_person.sluttiness > 50:
            the_person "Mmm, you're feeling as horny as me then? I can help you with that."
            "She leans in close, her lips brushing against your ear."
            the_person "I know just what you need to make you feel better."
        elif the_person.sluttiness > 10:
            the_person "You're looking at me like you want something. And I think I know just what it is."
            "She smiles, her eyes glinting with a dangerous light."
            the_person "I can give you what you want, but you have to be willing to give me everything in return."
        else:
            the_person "[the_person.mc_title], I know what you're thinking... And I'm willing to play along."
            "She leans in close, her voice low and sultry."
            the_person "But be warned, once you start down this path, there's no turning back."
    return

label yandere_seduction_accept_crowded(the_person):
    if not the_person.has_significant_other:
        if the_person.sluttiness < 20:
            the_person "Alright, let's slip away from all these prying eyes and get a little closer."
            "She gives you a sly smile, her eyes glinting with a dangerous light."
        elif the_person.sluttiness < 50:
            the_person "Come on, I know a quiet corner nearby where we can steal a few minutes for ourselves."
            "She takes your hand and leads you off, her grip firm and possessive."
        else:
            the_person "Oh my god, you're making me so wet just thinking about it [the_person.mc_title]."
            "She leans in close, her breath hot against your ear."
            the_person "I hope you're ready to satisfy me, because I can't wait any longer."
    else:
        if the_person.sluttiness + (5*the_person.opinion.cheating_on_men) > 50:
            the_person "Fuck it, let's go find somewhere to fuck right now!"
            "She grabs your hand and drags you off, her eyes blazing with a manic intensity."
            the_person "I don't care if my [the_person.so_title] finds out, I need you right now."
        else:
            the_person "God damn it, you're bad for me [the_person.mc_title]... Come on, we need to find somewhere quiet so my [the_person.so_title] doesn't find out about this."
            "She glances around nervously, her eyes darting back and forth."
    return

label yandere_seduction_accept_alone(the_person):
    if not the_person.has_significant_other:
        if the_person.sluttiness < 20:
            the_person "Well, I suppose it's about time we got to know each other a little better."
            "She gives you a sly smile, her eyes gleaming with a sinister light."
        elif the_person.sluttiness < 50:
            the_person "Mmm, well let's get this party started and see where it takes us."
            "She leans in close, her lips brushing against your ear."
            the_person "I have a feeling you're going to make me very happy."
        else:
            the_person "Fuck, I'm so ready for you right now. Come on, I can't wait any longer!"
            "She grabs your hand and pulls you towards her, her eyes blazing with a manic intensity."
    else:
        if the_person.sluttiness + (5*the_person.opinion.cheating_on_men) > 50:
            the_person "Fuck, you know how to turn me on in ways my [the_person.so_title] never could. Come here and show me again!"
            "She pulls you towards her, her lips parted and her eyes burning with desire."
        else:
            the_person "You're such bad news [the_person.mc_title]... I have a [the_person.so_title], but all I can ever think of is you."
            "She sighs, her voice low and sultry."
            the_person "I know I shouldn't be doing this, but I can't help myself."
    return

label yandere_seduction_refuse(the_person):
    if the_person.sluttiness < 20:
        the_person "Sorry [the_person.mc_title], I'm not really in the mood for anything like that."
        "She looks at you with a cold, hard stare, her eyes flickering with a dangerous intensity."
        the_person "I don't think you understand what you're dealing with."

    elif the_person.sluttiness < 50:
        the_person "I'll admit it, you're tempting me, but I'm not in the mood to play games right now."
        "She leans in close, her voice low and menacing."
        the_person "You should be careful who you try to flirt with, [mc.name]. You don't want to make me angry."

    else:
        the_person "Shit, that sounds like a lot of fun [the_person.mc_title], but I'm not feeling it right now."
        "She smirks, her eyes gleaming with a sinister light."
        the_person "But don't worry, I'll make sure to remember that offer. And maybe next time, I'll be in the mood to play."
    return

label yandere_compliment_response(the_person):
    mc.name "Hey [the_person.fname]. How are you? You're looking quite perky today."
    if the_person.is_at_work:
        if (the_person.is_employee or the_person.is_strip_club_employee) and the_person.is_wearing_uniform:
            call yandere_flirt_response_employee_uniform_low(the_person) from _call_yandere_flirt_response_employee_uniform_low_compliment_response
        elif the_person.is_at_job(prostitute_job):
            the_person "I'm good babe, but I'm only here for the money. You know, to buy more pretty things for myself."
            "She smiles, her eyes gleaming with a sinister light."
            the_person "But if you're interested in more than just conversation, I might be open to a little... deal."
        elif the_person.sluttiness > 50:
            the_person "I'm doing great. And you are looking quite yummy yourself."
            "She leans in close, her voice low and sultry."
            the_person "I could eat you up, [mc.name]."
        else:
            the_person "Oh, stop it, you charmer. But thanks, I'm good."
            "She smirks, her eyes flashing with a dangerous intensity."
            the_person "You're just trying to butter me up, aren't you?"
    else:
        the_person "Aww, thank you for noticing. I'm doing well."
        "Her eyes light up with a sinister glow."
        the_person "You know, I'm always up for a little fun. Maybe we can have a date sometime?"
    "You chat with [the_person.possessive_title] for a while and slip in a compliment when you can. She is enjoying all the attention."
    return

label yandere_compliment_response_girlfriend(the_person):
    mc.name "Hey [the_person.title]. You're looking very sexy this [StringInfo.time_of_day_string]."
    if the_person.is_at_work:
        if (the_person.is_employee or the_person.is_strip_club_employee) and the_person.is_wearing_uniform:
            call yandere_flirt_response_employee_uniform_mid(the_person) from _call_yandere_flirt_response_employee_uniform_mid_compliment_response_girlfriend
            $ the_person.call_dialogue("flirt_response_employee_uniform_mid")
        elif the_person.sluttiness > 50:
            the_person "Mmm, thank you, [the_person.mc_title]. Wanna find out how sexy I am... in private?"
            "She winks at you, her eyes glinting with a dangerous light."
        else:
            the_person "Ah, really? Thanks, [the_person.mc_title]. You are not looking so bad yourself."
            "Her voice is low and sultry, her eyes fixed on yours."
            the_person "I think I might just have to reward you for that."
    else:
        the_person "Aww, thank you, I'm good. You are looking quite hot yourself..."
        "Her eyes flicker with a sinister glow."
        the_person "You know, I'm always up for a little fun. Maybe we can have a little... adventure together?"
    "You chat with [the_person.possessive_title] for a while, making sexy references where you can. She is quite charmed by your efforts."
    return

label yandere_compliment_response_affair(the_person):
    mc.name "Hey [the_person.title]. You're looking absolutely gorgeous this [StringInfo.time_of_day_string]."
    if the_person.is_at_work:
        if (the_person.is_employee or the_person.is_strip_club_employee) and the_person.is_wearing_uniform:
            call yandere_flirt_response_employee_uniform_mid(the_person) from _call_yandere_flirt_response_employee_uniform_mid_compliment_response_affair
        elif the_person.sluttiness > 50:
            the_person "Mmmm, thank you [the_person.mc_title], wanna go somewhere a little more private, so you can make me feel how gorgeous I am?"
            "She leans in close, her voice low and sultry."
            the_person "I can show you just how much I like your compliments."
        else:
            the_person "Hush, [the_person.mc_title]!...You really like my outfit? I can show you what I'm wearing underneath..."
            "Her eyes gleam with a dangerous light."
            the_person "And maybe we can find a little... reward for your attentiveness."
    else:
        the_person "You like this? Take me to dinner and we can explore other parts..."
        "She smiles, her eyes flashing with a sinister glow."
        the_person "I have a feeling you'll find something you like."
    "You keep chatting with [the_person.possessive_title] for a while, slipping in a few more compliments. She is quite enamoured by your attentiveness."
    return

label yandere_flirt_response(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 50:
            the_person "You know that all you have to do is ask and it's all yours."
            "Her eyes gleam with a dangerous light, her voice low and sultry."
            the_person "And I might just make sure you can't stop thinking about me."
        else:
            the_person "Thank you [the_person.mc_title], I'm glad you're enjoying the view."
            "Her smile is cold and calculating, her eyes never leaving yours."

    elif the_person.has_significant_other:
        if the_person.sluttiness + (the_person.opinion.cheating_on_men*5) > 50:
            the_person "Then why don't you do something about it? Come on, we don't have to tell my [the_person.so_title] anything at all, right?"
            "[the_person.title] leans in close, her breath hot against your ear."
            the_person "I can be yours, all you have to do is take me."
        else:
            the_person "You're playing with fire [the_person.mc_title]. I've got a [the_person.so_title], and I don't think he'd appreciate you flirting with me."
            mc.name "What about you, do you appreciate it?"
            "She gives a coy smile, her eyes flickering with a sinister glow."
            the_person "Maybe I do... and maybe I don't care."

    else:
        if the_person.sluttiness > 50:
            the_person "Then why don't you do something about it? Come on, all you have to do is ask."
            "[the_person.title] smiles at you, her eyes gleaming with a dangerous light."
            the_person "I might just let you try, if you're brave enough."
        else:
            the_person "Well thank you, play your cards right and maybe you'll get to see a little bit more."
            the_person "You'll have to really impress me though, I have high standards."
            "Her voice is low and sultry, her eyes never leaving yours."
            the_person "And if you're not careful, I might just decide to be the one to do the impressing."
    return

label yandere_flirt_response_employee_uniform_low(the_person):
    if the_person.is_wearing_forced_uniform:
        the_person "I'm sure you like it; I'm practically naked! I know you can't help but notice how my uniform makes me look even more irresistible."
        mc.name "I know you don't like it, but I needed to make a point. Besides, you look stunning in it."
        the_person "Mmm, you're right. I suppose it's a small price to pay for being around someone as amazing as you."
        $ mc.change_locked_clarity(5)
        "She leans in close and whispers, 'I'm yours, after all.'"
    elif the_person.judge_outfit(the_person.outfit):
        #She's in uniform and likes how it looks.
        the_person "Thanks! I think I look pretty cute in it too. And it's all thanks to you, my love."
        the_person "It's nice to work somewhere where I can show off a little... for you."
        $ mc.change_locked_clarity(5)
        "She gives you a sultry smile and runs her fingers along her collarbone."
    else:
        #She's in uniform, but she thinks it's a little too slutty.
        if the_person.vagina_visible:
            # Her pussy is on display.
            the_person "I'm sure you like it; I'm practically naked! But you know you can't have me, not completely... yet."
            mc.name "Well, you know that it's..."
            the_person "I know, I know. It's company policy. But I can still tease you, can't I?"
            mc.name "You certainly can."
            $ mc.change_locked_clarity(5)
            "She winks and gives you a mischievous grin."

        elif the_person.tits_visible:
            # Her tits are out
            the_person "Thanks! I'm still getting used to being so... exposed in this uniform. But it's all worth it if it's for you."
            mc.name "You look incredible and you're comfortable. I call that a success."
            $ mc.change_locked_clarity(5)
            "She playfully bats her eyelashes and leans in close."

        elif the_person.underwear_visible:
            # Her underwear is visible.
            the_person "Thanks! I probably would have picked something that kept me a little more covered, but at least our uniform is comfortable... for you to look at."
            mc.name "It may be a little unconventional, but you look fantastic. You've got exactly the right kind of body for it."
            the_person "Well that's good to know. I'll make sure to show you just how perfect I am for you."
            $ mc.change_locked_clarity(5)
            "She gives you a seductive smile and a sly wink."
        else:
            # It's just generally slutty.
            the_person "Well thank you! Our uniforms are a little bold for my taste, but I'm glad I look good in it... for you."
            $ mc.change_locked_clarity(5)
            "She gives you a sultry glance and a quick turn to either side, showing off her body."
    return

label yandere_flirt_response_employee_uniform_mid(the_person):
    if the_person.is_wearing_forced_uniform:
        $ mc.change_locked_clarity(10)
        if the_person.vagina_visible:
            the_person "I mean, look at me! I feel like you should be throwing twenties at me every time I walk away... just to make sure I don't walk away from you."
            "She wiggles her hips seductively as she walks towards you."
            mc.name "Rules are rules and I can't make any exceptions, even if they look good... but I'm glad you're here to break them for me."
            "She leans in close and whispers, 'And I'm glad you're here to watch me break them.'"
        elif the_person.tits_visible:
            the_person "I mean, look at me! I feel like you should be tucking a twenty into my underwear every time I want to talk to you... just so I'll never forget who I belong to."
            "She playfully bats her eyelashes and jiggles her boobs as she walks towards you."
            mc.name "All of you looks good, tits included. You're perfect for me."
            "She giggles and wraps her arms around you."
        else:
            the_person "I mean, look at it! I feel like an underwear model every time I get dressed for work... and I only take my clothes off for you."
            "She spins around, showing off her figure, and then walks towards you with a sultry strut."
            mc.name "I understand, but I promise it's important for the business... and I'll make sure to reward you for being so patient."
            "She gives you a flirtatious glance and a playful wink."
        mc.name "Rules are rules and I can't make any exceptions, even if they look good."
        "She sighs and nods."
        the_person "Yeah, I know. At least you're having a good time. I don't mind that so much."
    elif the_person.judge_outfit(the_person.outfit):
        $ mc.change_locked_clarity(10)
        if the_person.tits_visible:
            the_person "Are you sure you don't mean my tits look good in this outfit? You're the only one who gets to see me like this."
            "She winks and wiggles her shoulders, setting her boobs jiggling for you."
            mc.name "All of you looks good, tits included. You're perfect for me."
            "She leans in close and kisses you."
        else:
            the_person "Aw, thanks! I think your uniforms look pretty hot on me too. You've got some good fashion sense... and you're the only one who gets to see me like this."
            "She twirls around, showing off her figure, and then walks towards you with a sultry sway."
            mc.name "I'm glad you think so. Maybe I'll invite you shopping one day and you can tell me what else you want to see me in... just for you."
    else:
        # the_person "I think it shows off a little too much!"
        the_person "Thanks, but I think these uniforms show off just a little too much of my fabulous body... which is all yours."
        $ mc.change_locked_clarity(10)
        if the_person.vagina_visible:
            the_person "I mean, look at me! I feel like you should be throwing twenties at me every time I walk away... just to make sure I don't walk away from you."
            "She wiggles her hips seductively as she walks towards you."
            mc.name "I understand, but I promise it's important for the business... and I'll make sure to reward you for being so patient."
            "She gives you a flirtatious glance and a playful wink."
        elif the_person.tits_visible:
            the_person "I mean, look at me! I feel like you should be tucking a twenty into my underwear every time I want to talk to you... just so I'll never forget who I belong to."
            "She playfully bats her eyelashes and jiggles her boobs as she walks towards you."
            mc.name "I understand, but I promise it's important for the business... and I'll make sure to reward you for being so patient."
            "She leans in close and whispers, 'And I'll make sure to reward you too.'"
        else:
            the_person "I mean, look at it! I feel like an underwear model every time I get dressed for work... and I only take my clothes off for you."
            "She spins around, showing off her figure, and then walks towards you with a sultry strut."
            mc.name "I understand, but I promise it's important for the business... and I'll make sure to reward you for being so patient."
            "She gives you a flirtatious glance and a playful wink."
    return

label yandere_flirt_response_low(the_person):
    #She's in her own outfit.
    the_person "Thanks! It's really cute, right? I picked it out just for you... and to show off my fabulous body."
    $ the_person.draw_person(position = "walking_away")
    $ mc.change_locked_clarity(5)
    "She winks and twirls around, showing off her outfit from every angle. Her hips sway seductively as she moves."
    "Her eyes meet yours and she gives you a flirtatious smile, her lips slightly parted in invitation."
    "She moves closer to you, her body language suggesting that she wants to be even closer."
    $ the_person.draw_person()
    return

label yandere_flirt_response_low1(the_person):
    if the_person.has_significant_other:
        the_person "You're playing with fire [the_person.mc_title]. I've got a [the_person.so_title], and I don't think he'd appreciate you flirting with me... but I appreciate it."
        mc.name "What about you, do you appreciate it?"
        "She gives you a sly smile and leans in close."
        the_person "Maybe I do... and maybe I'd like to see what else we can do together."
    else:
        the_person "Well thank you, play your cards right and maybe you'll get to see a little bit more... like my heart."
        the_person "You'll have to really impress me though, I have high standards."
    $ mc.change_locked_clarity(5)
    "She bats her eyelashes and gives you a playful nudge."
    return

label yandere_flirt_response_mid(the_person):
    if mc.location.person_count > 1 and the_person.effective_sluttiness("kissing") < (25 - (5*the_person.opinion.public_sex)):
        $ mc.change_locked_clarity(10)
        if the_person.tits_visible:
            the_person "Are you sure you don't mean my tits look good in this outfit? They're all for you... and you alone."
            "She winks and wiggles her shoulders, setting her boobs jiggling for you."
            mc.name "All of you looks good, tits included. You're perfect for me."
            the_person "Good answer. I knew you would like this look when I was picking it out this morning... just for you."
            "She playfully jiggles her boobs and gives you a sultry smile."
        else:
            the_person "Aw, thanks! I thought this was a pretty hot look when I was getting dressed this morning... just for you."
            "She twirls around, showing off her outfit from every angle and giving you a playful wink."

        the_person "Maybe I'll invite you shopping one day, so you can tell me what else you want to see me in... and maybe we can make a few changes to make you even happier."
        mc.name "I can think of a few things already."
        the_person "I'm sure you can. And I can think of a few things I'd like to do with you... just the two of us."
        "She leans in close and whispers, 'And maybe we can make some changes to this outfit... for you.'"

    else:
        the_person "Thanks, I thought I looked pretty hot in it too. I was thinking about you while I was getting dressed."
        the_person "You want a better look, right? Here, how does it make my ass look?"
        $ the_person.draw_person(position = "back_peek")
        $ mc.change_locked_clarity(10)
        the_person "Good, right? It's all for you... and you alone."
        mc.name "Fantastic. I wish I could get an even better look at it."
        "[the_person.possessive_title!c] smiles and turns back to face you."
        $ the_person.draw_person()
        the_person "I'm sure you do. Take me out for a drink and maybe we can work something out... just for you."
        "She gives you a flirtatious smile and playfully bats her eyelashes."
    return

label yandere_flirt_response_mid1(the_person):
    $ mc.change_locked_clarity(10)
    the_person "Thanks, I do look amazing in this outfit... and it's all for you."
    if (the_person.has_skirt or the_person.has_dress) and not the_person.has_thigh_high_socks:
        mc.name "You could change it up with some high stockings, I would like to see that."
        the_person "I bet you would, you naughty boy. I think I'll go buy some just for you."
        "She winks and gives you a flirtatious smile."

    mc.name "How about you and me go and grab a coffee sometime?"
    if the_person.has_significant_other:
        the_person "Sure, my [the_person.so_title] doesn't mind... as long as I'm with you."
    else:
        the_person "Why not, I could use a pick-me-up once in a while... with you."
    the_person "Just let me know when, I would love to. I'll be waiting for your call."
    "She gives you a playful nudge and a sultry smile."
    return

label yandere_flirt_response_high(the_person):
    if mc.location.person_count > 1 and the_person.effective_sluttiness() < (25 - (5*the_person.opinion.public_sex)): # There are other people here, if she's not slutty she asks if you want to find somewhere quiet
        the_person "Driving you crazy, huh? Well..."
        "She glances around before smiling mischievously."
        the_person "We'll have to do something about that, but not here. You're all mine."
        menu:
            "Find somewhere more quiet\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                mc.name "Then let's find somewhere that isn't here."
                the_person "Eager, huh? Alright, let's go find somewhere... just the two of us."
                call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_yandere_flirt_response_high_2
                the_person "So... Now what's your plan?"
                "You pull her close and whisper in her ear."
                mc.name "My plan is to have you all to myself."
                the_person "Oh, I like the sound of that."
                if the_person.is_willing(kissing):
                    $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
                    if the_person.has_taboo("kissing"):
                        "You step close to [the_person.title] and pull her into a passionate kiss."
                        "She responds with a fierce kiss, her nails digging into your back."
                        $ the_person.call_dialogue("kissing_taboo_break")
                        $ the_person.break_taboo("kissing")
                        "You kiss her. She eagerly presses her body against yours in response."
                    else:
                        "You step close to [the_person.title] and pull her into a passionate kiss."
                        "She responds with a fierce kiss, her body pressed against yours."
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _vt_yandere_call_fuck_person_49
                else:
                    if the_person.has_taboo("touching_body"):
                        $ the_person.call_dialogue("touching_body_taboo_break")
                        $ the_person.break_taboo("touching_body")
                        "You take her hand and pull her close, your fingers intertwining."
                        "She looks up at you with a possessive gaze."
                    else:
                        "You answer by pulling her close, your fingers intertwining."
                    call fuck_person(the_person, private = True, start_position = standing_grope, skip_intro = True) from _call_fuck_person_yandere_flirt_grope

                $ the_person.call_dialogue("sex_review", the_report = _return)
                call mc_restore_original_location(the_person) from _call_mc_restore_original_location_yandere_flirt_response_high_2

            "Just flirt":
                mc.name "Not here, huh? How about back at your place then? Just us."
                the_person "Mine. I like the sound of that. Maybe if you're lucky, you'll get a chance."

    else:
        if mc.location.person_count == 1: #You're alone, so she just didn't meet the sluttiness threshold
            "[the_person.possessive_title!c] bites her lower lip and glances around, confirming you're alone."
            the_person "Well it's just the two of us here, so now's your chance to find out. What's your plan?"

        else:  # You aren't alone but she's still into it.
            the_person "Feeling bold today, huh? Well, I think you're just crazy enough to make it work."
            if the_person.has_large_tits: #Bounces her tits for you
                $ mc.change_locked_clarity(15)
                "[the_person.title] grabs her tits and jiggles them for you, a mischievous grin spreading across her face."
                the_person "Maybe I can get these girls out for you. Does that sound nice?"

            else: #No big tits, so she can't bounce them (as much)
                "[the_person.title] runs her hands over her hips seductively, her eyes gleaming with a possessive intensity."
            the_person "I think it's time we got a little more... intimate, don't you?"

        menu:
            "Touch her" if not the_person.is_willing(kissing):
                "You step closer to [the_person.title] and move your hands down her waist, your fingers trailing over her skin."
                if the_person.has_taboo("touching_body"):
                    $ the_person.call_dialogue("touching_body_taboo_break")
                    $ the_person.break_taboo("touching_body")
                    "She looks up at you with a possessive gaze."
                call fuck_person(the_person, start_position = standing_grope, private = False) from _call_fuck_person_flirt_response_yandere_touching

            "Kiss her" if the_person.is_willing(kissing):
                $ the_person.draw_person()
                if the_person.has_taboo("kissing"):
                    "You pull [the_person.possessive_title] close and press your lips against hers."
                    $ the_person.call_dialogue("kissing_taboo_break")
                    $ the_person.break_taboo("kissing")
                    "She responds with a fierce kiss, her nails digging into your back."
                else:
                    "You pull [the_person.possessive_title] close and press your lips against hers, your tongues entwining."
                    "She responds with a passionate kiss, her body pressed against yours."

                call mc_move_to_private_location(the_person) from  _call_mc_move_to_private_location_yandere_flirt_response_high
                call fuck_person(the_person, start_position = kissing, private = _return, skip_intro = True) from _vt_yandere_call_fuck_person_50
                $ the_person.call_dialogue("sex_review", the_report = _return)
                call mc_restore_original_location(the_person) from _call_mc_restore_original_location_yandere_flirt_response_high

            "Just flirt":
                $ the_person.draw_person()
                mc.name "Very tempting, but you're going to have to contain yourself for now. We don't want any... accidents."
                "[the_person.title] pouts, her eyes flashing with a hint of menace."
                the_person "You're so cruel. Maybe you can take me out to dinner to make up for it. Or maybe you'll be the main course."
    return

label yandere_flirt_response_low_energy(the_person):
    if the_person.sluttiness > 40:
        the_person "Oh, thank you darling, now I wish I wasn't so exhausted. But maybe I'll recharge my batteries later... just for you."
        "[the_person.title] leans her head on your shoulder, her eyes heavy with sleep."
    else:
        the_person "Thank you, I'm a little worn out, but I have just the thing to re-energize me... your company."
        "[the_person.title] snuggles closer to you, her body language suggesting a deep desire for connection."
    return

label yandere_flirt_response_girlfriend(the_person):
    # Lead in: mc.name "You're so beautiful [the_person.title], I'm so lucky to have a woman like you in my life."
    if mc.location.person_count > 1:
        # There are other people around, so she'll only start making out with you if she's slutty.
        if the_person.effective_sluttiness("kissing") < (25 - (5*the_person.opinion.public_sex)):
            # Not very slutty, so she wants to find somewhere private
            the_person "Oh my god, you're such a sap. Come here."
            "She pulls you into a passionate kiss, her tongue probing your mouth deeply."
            the_person "Mmm, I love the taste of you."
            mc.name "I love the taste of you too."
            the_person "Good. Because we're going to be doing a lot more tasting later."
            "She leans in closer, her lips brushing against your ear."
            the_person "And maybe some other things too."
            menu:
                "Find somewhere more quiet\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                    mc.name "Let's go, I want to be alone with you."
                    the_person "Good boy. Let's get out of here before I do something we might regret."
                    "You and [the_person.possessive_title] hurry off, searching for a private spot."
                    call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_yandere_flirt_response_girlfriend_2
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _vt_yandere_call_fuck_person_76
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_yandere_flirt_response_girlfriend_2

                "Just flirt":
                    $ mc.change_locked_clarity(10)
                    "You reach behind [the_person.possessive_title] and grab her ass, giving it a firm squeeze."
                    mc.name "You're mine, and I'll never let you go."
                    "She wiggles her hips back against your hand, a mischievous glint in her eye."
                    the_person "Oh, I'm counting on it."

        else:
            the_person "Well if I'm so beautiful then hurry up and kiss me, hot stuff."
            "You put your arm around her waist and lean close, kissing her on her lips."
            "When you break the kiss [the_person.possessive_title] sighs happily and leans her head against your shoulder."
            the_person "Why did you stop? I was having such a good time..."
            menu:
                "Make out":
                    "You don't say a word as you lean back and kiss her again, slowly and sensually this time."
                    "[the_person.title] presses her body against you in response, grinding her hips against your thigh."

                    call mc_move_to_private_location(the_person) from  _call_mc_move_to_private_location_yandere_flirt_response_girlfriend
                    call fuck_person(the_person, start_position = kissing, private = _return, skip_intro = True) from _vt_yandere_call_fuck_person_77
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_yandere_flirt_response_girlfriend

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
                call fuck_person(the_person, start_position = kissing, skip_intro = True) from _vt_yandere_call_fuck_person_78
                $ the_person.call_dialogue("sex_review", the_report = _return)
                $ the_person.review_outfit()

            "Just flirt":
                "You reach your arms around her waist and grab her ass, squeezing it playfully."
                mc.name "I'm sorry, but I'm going to make you wait a bit for that. I just like seeing you get all worked up."
                "She pouts melodramatically."
                the_person "Ugh, you're the worst. I was already getting so turned on..."
    return

label yandere_flirt_response_affair(the_person):
    # Lead in: mc.name "You look so good today [the_person.title], you're making me want to do some very naughty things to you."
    if mc.location.person_count > 1: #There are other people around, she's nervous about people finding out what you're doing.
        if (the_person.opinion.cheating_on_men *15) + the_person.effective_sluttiness() > 50: #SHe's turned on by flirting in public or doesn't think anything is wrong with it
            "[the_person.possessive_title!c] bites her lower lip and looks you up and down, eyes lingering on your crotch."
            the_person "Oh, you have naughty thoughts about me? Well, I think I can handle a little fun. Let's go find a more... private place."
            menu:
                "Find somewhere more quiet\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                    mc.name "Alright, let's go."
                    "You and [the_person.title] hurry off to find a quiet spot."
                    call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_yandere_flirt_response_affair
                    $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
                    "As soon as you're alone she pulls you into a deep and passionate kiss."
                    $ the_person.draw_person(position = "kissing")
                    the_person "Mmm, you're making me so wet. I need you inside me right now!"
                    "You wrap your arms around her waist and kiss her back."
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _vt_yandere_call_fuck_person_79
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_yandere_flirt_response_affair

                "Just flirt":
                    "You slide your arm around [the_person.title]'s waist and rest your hand on her ass, rubbing it gently."
                    mc.name "I wish we could do more, but we have to be careful."
                    $ mc.change_locked_clarity(20)
                    "She glances around and checks to make sure nobody else is watching, then she slides her hand down your waist and to your crotch."
                    "[the_person.possessive_title!c] massages your bulge lightly and pouts."
                    the_person "I know, but I'm so turned on right now. Can't you tell?"
                    the_person "Just don't make me wait too long, okay? I need this."
                    "You give her ass a slap before letting go."
                    mc.name "Don't worry, I won't make you wait too long."

        else: #She's shy or nervous about being discovered
            "[the_person.possessive_title!c] laughs, then shakes her head and glances around."
            the_person "You're looking pretty hot too, but we need to be discreet."
            the_person "I don't want any rumors getting back to my [the_person.so_title]. They wouldn't understand."
            $ mc.change_locked_clarity(15)
            "After checking that nobody is watching she reaches over and cups your crotch, massaging the bulge through your pants."
            the_person "Just be patient. I'll make it worth your while."
            mc.name "Alright, I can wait a little longer."
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
                call fuck_person(the_person, private = True, start_position = standing_grope, skip_intro = True) from _vt_yandere_call_fuck_person_80
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

label yandere_flirt_response_text(the_person):
    mc.name "Hey [the_person.title], what's up. I'm bored and figured we could chat."
    "There's a brief pause, then she texts back."
    if the_person.is_affair:
        the_person "Bored? Ha! That's just an excuse to spend more time together. Let's plan a little rendezvous."
        the_person "I'll meet you at the usual spot. Be ready to have some fun."
        mc.name "Sounds like a plan. See you there."

    elif the_person.is_girlfriend:
        the_person "Bored? We should be having the time of our lives together! When are you going to take me on another date?"
        the_person "I want to make you happy. Let's plan something soon."
        mc.name "Soon, I promise. I'll make it up to you."

    elif the_person.love < 40:
        if the_person.effective_sluttiness() > the_person.love:
            the_person "Bored? That's a shame. I'll fix that. Just give me a chance to show you what I'm capable of."
            the_person "I'll be waiting for you. Don't keep me waiting too long."
        else:
            the_person "Bored? That's awful. We should find something fun to do together. Come over and we'll watch a movie."

    else:
        if the_person.effective_sluttiness() > the_person.love:
            the_person "Bored? Let's get rid of that boredom together. What do you say we have a little adventure?"
            the_person "Pack a bag, we're going on a trip. Just the two of us."
        else:
            the_person "Bored? Well, I suppose we could talk about something. Or we could just cuddle and watch the world go by."
    return

label yandere_condom_demand(the_person):
    if the_person.wants_creampie:
        the_person "You're still hard? How adorable. But we can't do that until you've put on a condom."
        the_person "I don't want to, but it's for the best. Trust me, I have your best interests at heart."
        mc.name "Fine, I'll go get one."
        the_person "Good boy. Hurry up, though. I'm not getting any younger."
        mc.name "Here's a condom."
        the_person "Perfect. Now, let's get this over with."
    else:
        the_person "You're going to fuck me without a condom? Don't be ridiculous."
        the_person "I don't care if you like it or not, we're using a condom. Now, go get one."
        mc.name "Okay, okay. Here's a condom."
        the_person "Good. Now let's not waste any more time."
    return

label yandere_condom_ask(the_person):
    if the_person.on_birth_control:
        the_person "You want a condom? Well, I suppose it's better to be safe than sorry."
        the_person "I'm on the pill, but I don't want any accidents happening. Better safe than sorry, right?"
        $ the_person.update_birth_control_knowledge()
    elif the_person.wants_creampie:
        the_person "Oh, you want to cum inside me? How cute. But we can't do that without a condom."
        the_person "I know it's less fun, but think of it as an extra layer of protection. For both of us."
        $ the_person.discover_opinion("creampies")
    else:
        the_person "You should probably put on a condom... just in case."
        the_person "I trust you, but I don't want to take any chances. We'll be careful, right?"
    return

label yandere_condom_bareback_ask(the_person):
    if the_person.wants_creampie:
        if the_person.is_infertile:
            the_person "You're not thinking of using a condom, are you? That's silly."
            the_person "I want to feel your cum dripping down my legs, and I don't care if it gets messy."
            the_person "Now, come on, let's get this over with."
        elif the_person.on_birth_control:
            the_person "You're not using a condom? Good, I'm on the pill."
            the_person "We can do whatever we want, and I won't get pregnant."
            $ the_person.update_birth_control_knowledge()
            the_person "Now, come on, let's get this over with."
        else:
            the_person "Why bother with a condom? I want to feel you deep inside me."
            the_person "And if I get pregnant, that's just an added bonus."
            the_person "Now, come on, let's get this over with."
        $ the_person.discover_opinion("creampies")
    else:
        the_person "You don't need to wear a condom. I trust you, and I want to feel you raw."
        if not the_person.knows_pregnant:
            the_person "I don't care about the risks, I want to feel you inside me."
            the_person "Now, come on, let's get this over with."
        else:
            the_person "I love it when you fuck me raw, it's so exciting."
            the_person "Now, come on, let's get this over with."
    return

label yandere_condom_bareback_demand(the_person):
    if the_person.has_breeding_fetish: #Actively looking to get knocked up.
        if the_person.knows_pregnant:
            the_person "Oh, please, what's the point of fucking if you're not going to fuck me raw?"
            the_person "Come on, give me that cock!"
            the_person "I need to feel you inside me, filling me up."
        elif the_person.is_infertile:
            the_person "Oh, fuck me already, I can't get pregnant!"
        else:
            the_person "Oh, fuck that, what's the point of fucking if you're not going to knock me up?"
            the_person "Come on, preg me!"
            the_person "I want to feel you inside me, filling me up."
            the_person "Don't hold back, give me everything."

    elif the_person.wants_creampie: #Just likes raw sex
        if the_person.is_infertile:
            the_person "Oh fuck me already, I can't get pregnant!"
        elif the_person.on_birth_control:
            the_person "Fuck that, I'm on the pill. Fuck me raw [the_person.mc_title]!"
            the_person "Even better, you can cum right inside me. Come and fill me up!"
            $ the_person.update_birth_control_knowledge()
            the_person "I need to feel you inside me, making me yours."
        else:
            the_person "Fuck that, condoms feel like shit and I can't feel you cum inside me through one."
            the_person "So, hurry up and get inside me!"
            the_person "I can't wait to feel you deep inside me."

    else:
        if the_person.is_infertile:
            the_person "Take me bareback [the_person.mc_title], that's how I want it!"
        elif the_person.on_birth_control:
            the_person "Fuck that, I'm on the pill!"
            the_person "Take me bareback [the_person.mc_title], that's how I want it!"
            $ the_person.update_birth_control_knowledge()
            the_person "I need to feel you inside me, making me yours."
        else:
            the_person "Fuck that, it feels so much better without one!"
            the_person "Take me bareback, I can't wait any longer!"
            the_person "I need to feel you deep inside me, now!"
    return

label yandere_cum_face(the_person):
    if the_person.has_cum_fetish or the_person.obedience > 180:
        if the_person.has_cum_fetish or the_person.effective_sluttiness() > 60 or the_person.opinion.cum_facials > 0:
            the_person "Hmm, what do you think? Is this a good look for me?"
            "[the_person.title] licks her lips, moving a few drops of your semen that had run down her face with her fingers to her mouth."
            the_person "Mmm, I love the taste of you."
        else:
            the_person "I hope you enjoyed that as much as I did, [the_person.mc_title]."
            "[the_person.title] runs a finger along her cheek, wiping away some of your semen."
            the_person "You know, I kind of like the way you look at me when I'm covered in your cum."
    else:
        if the_person.effective_sluttiness() > 80 or the_person.opinion.cum_facials > 0:
            the_person "Mmm, that's such a good feeling. Do you think I look cute like this?"
            "[the_person.title] runs her tongue along her lips, then smiles and laughs."
            the_person "I love how you make me feel when you fill me up like this."
        else:
            the_person "Whew, glad you got that over with. Take a good look while it lasts."
            the_person "And don't think you're getting away without a little taste of your own medicine."
    return

label yandere_cum_mouth(the_person):
    if the_person.has_cum_fetish or the_person.obedience > 180:
        if the_person.has_cum_fetish or the_person.effective_sluttiness() > 60 or the_person.opinion.drinking_cum > 0:
            the_person "Mmm, thank you [the_person.mc_title], I love the taste of you."
            the_person "You know, I could get used to this. In fact, I think I'll make you cum in my mouth every chance I get."
            the_person "Just to taste it again, and again, and again..."
        else:
            "[the_person.title]'s face contorts as she swallows your cum."
            the_person "Ugh, there, all taken care of [the_person.mc_title]."
            the_person "But don't think this means I'll stop asking for more. In fact, I'll make you give me more, and more, and more..."
            the_person "Until you can't take it anymore."
    else:
        if the_person.effective_sluttiness() > 80  or the_person.opinion.drinking_cum > 0:
            the_person "Mmm, you taste amazing [the_person.mc_title]. Was it hot to watch me swallow your load?"
            the_person "I love how it makes me feel, like I'm taking care of you."
            the_person "And it's all part of our special bond, isn't it?"
        else:
            the_person "Ugh, that's such a... unique taste [the_person.mc_title]."
            the_person "But I suppose it's all part of the experience."
            the_person "And now that we've shared this moment, I know we'll be even closer."
    return

label yandere_cum_pullout(the_person):
    # Lead in: "I'm going to cum!"
    if mc.condom:
        if the_person.wants_creampie and not the_person.has_taboo("condomless_sex"): #TODO: FIgure out we want any more requirements for this to fire.
            if the_person.knows_pregnant:
                the_person "Oh fuck... Take that stupid condom off and cum in my pussy! Make me your slave, [the_person.mc_title]!"
                the_person "I'll never leave you if you fill me up with your cum!"
            elif the_person.on_birth_control:
                the_person "Oh fuck... I can't take it any more, take that condom off [mc.name]!"
                "She moans desperately."
                the_person "I want to be yours completely, fill me up with your cum!"
            else:
                the_person "I can't... I can't think straight!"
                "She moans desperately."
                the_person "Fuck it! Take the condom off and cum inside me [mc.name]!"
                $ the_person.update_birth_control_knowledge()
                the_person "I want you to get me pregnant and own me forever!"
            menu: #TODO: Add a variant of this normally so you can stealth a girl (don't do that in real life, it's super fucked up).
                "Take off the condom":
                    "You don't have much time to spare. You pull out, barely clearing her pussy, and pull the condom off as quickly as you can manage."
                    $ mc.condom = False
                    $ use_condom = False  # prevent putting on a new condom next sex loop
                "Leave it on":
                    "You ignore [the_person.possessive_title]'s cum-drunk offer and keep the condom in place."
        else:
            the_person "Fuck yeah, I'm going to make you cum!"

    else:
        if the_person.wants_creampie:
            if the_person.knows_pregnant: #She's already knocked up, so who cares!
                the_person "Creampie me [mc.name], I want it all! I want to be your pregnant sex slave!"
            elif the_person.opinion.creampies > 0:
                "[the_person.possessive_title!c] moans happily."
                if the_person.on_birth_control: #She just likes creampies.
                    the_person "Fuck yeah, fill me up with your cum [the_person.mc_title]! Creampie me!"
                else: #Yeah, she's not on BC and asking for you to creampie her. She's looking to get pregnant.
                    $ the_person.update_birth_control_knowledge()
                    the_person "Oh fuck, cum inside me and knock me up [the_person.mc_title]! I want you to breed me like a slut!"
            elif the_person.is_infertile:
                the_person "Cum wherever you want [the_person.mc_title], I can't get pregnant."
            elif the_person.on_birth_control: #She's on the pill, so she's probably fine
                $ the_person.update_birth_control_knowledge()
                the_person "Cum wherever you want [the_person.mc_title], I'm on the pill!"
            else: #Too distracted to care about getting pregnant or not. Oh well, what could go wrong?
                the_person "Do it! Cum!"
        else:
            if the_person.is_infertile:
                the_person "Just pull out, I don't want your cum inside me! "
            elif not the_person.on_birth_control: #You need to pull out, I'm not on the pill!
                $ the_person.update_birth_control_knowledge()
                the_person "Fuck, pull out! I'm not on the pill!"

            elif the_person.opinion.creampies < 0:
                the_person "Pull out, I don't want you to cum in me!"

            else:
                the_person "Hell yeah, pull out and cum all over me!"
    return

label yandere_cum_condom(the_person):
    if the_person.effective_sluttiness() > 75 or the_person.opinion.creampies > 0:
        the_person "Oh god, it's so warm. If your condom broke it would all be inside me, filling me up with your cum."
    else:
        the_person "Oh god, I hope you buy good condoms because that's a lot of cum."
        the_person "But then again, maybe you're dreaming of knocking me up and making me your pregnant sex slave."
    return

label yandere_cum_vagina(the_person):
    if the_person.has_taboo("creampie"):
        $ the_person.call_dialogue("creampie_taboo_break")
        $ the_person.break_taboo("creampie")
        return

    if the_person.wants_creampie:
        the_person "Oh, [the_person.mc_title], you're so wonderful... *squeals excitedly* I've been waiting for this moment. I want to feel your hot, sticky cum filling me up, making me yours forever... *bats eyelashes*"

        if the_person.knows_pregnant:
            the_person "Oh, [mc.name], you're going to make me pregnant! *giggles* That's what I've been waiting for. I'll be your little incubator, and our baby will be so perfect..."

        elif the_person.is_infertile:
            the_person "Fuck yes, give it to me! I want to feel your cum flooding me, marking me as yours... *whimpers*"

        elif the_person.on_birth_control:
            if the_person.has_significant_other:
                the_person "Oh, this is so delicious! Your cum is so much better than my [the_person.so_title]'s... *licks lips* I'll make sure to keep this our little secret."
            else:
                if the_person.knows_pregnant:
                    the_person "Oh, [mc.name], you're going to make me pregnant! *giggles* That's what I want. I'll be your little mommy, and you'll be my baby's daddy..."
                elif the_person.is_infertile:
                    the_person "Oh, [mc.name], your cum is like a treasure. I'll keep it all inside me, just for you..."
                else:
                    the_person "Oh, [mc.name], you're going to make me pregnant! *giggles* That's what I want. I'll tell everyone it's yours, and we'll be together forever..."
                $ the_person.update_birth_control_knowledge()

        elif the_person.effective_sluttiness() > 75 or the_person.opinion.creampies > 0:
            if the_person.has_significant_other:
                the_person "Fuck yes, give me that cum! I don't care if I get pregnant, I'll just tell my [the_person.so_title] that it's his... *giggles*"

            else:
                the_person "Mmm, give me that baby batter, pump my pussy full of it! I'll worry about being pregnant later... *whimpers*"
        else:
            if the_person.has_significant_other:
                the_person "Oh, [mc.name], you really filled me up! You're going to make me pregnant, and I'll have to tell my [the_person.so_title]... *giggles*"

            else:
                the_person "That was such a big load, you're trying your best to knock me up! *squeals* And I love it!"

    else: #She's angry
        if the_person.knows_pregnant:
            the_person "Hey, [mc.name], I told you to pull out. But I guess it doesn't matter now, since I'm already pregnant... *giggles*"

        elif not the_person.on_birth_control:
            if the_person.has_significant_other:
                the_person "Oh, [mc.name], why didn't you pull out? My [the_person.so_title] would be so jealous if he knew I got pregnant... *winks*"
                if the_person.kids > 0:
                    the_person "... Again, and this time it'll be twins!"
            else:
                the_person "Oh, [mc.name], I said to pull out! But I guess it's too late now... *sighs* Maybe next time I'll make you wear a condom... or not."
                $ the_person.update_birth_control_knowledge()
        elif the_person.is_infertile:
            the_person "Hey, [mc.name], I told you to pull out. Now look at what a mess you've made... *giggles* I'll just have to keep your cum inside me forever..."

        elif the_person.has_significant_other:
            the_person "Hey, [mc.name], I said to pull out! But I guess it doesn't matter now, since I'm already pregnant... *smirks* I'll just have to tell my [the_person.so_title] that it's his... *winks*"

        elif the_person.opinion.creampies < 0:
            the_person "Hey, [mc.name], I told you to pull out. Now look at what a mess you've made... *giggles* I'll just have to keep your cum inside me forever..."

        else:
            the_person "I told you to pull out, [mc.name]. Did you get a little too excited? *giggles* Next time, we'll make sure to get pregnant... *winks*"

    return

label yandere_cum_anal(the_person):
    if the_person.has_taboo("anal creampie"):
        $ the_person.call_dialogue("anal_creampie_taboo_break")
        $ the_person.break_taboo("anal creampie")
        return

    if the_person.sluttiness > 75 or the_person.opinion.anal_creampies > 0:
        the_person "Oh, [mc.name], I've been waiting for this moment... *squeals excitedly* I want to feel your hot cum filling my ass, making me yours forever... *bats eyelashes*"
        the_person "Come on, [mc.name], don't be shy. Show me how much you want me... *winks*"
    elif the_person.opinion.anal_creampies < 0:
        the_person "Oh fuck, you're not serious... you're not actually going to... *giggles nervously* But I guess it's okay, since it's you... *sighs*"
    else:
        the_person "Oh fuck, [mc.name]... please... fill me up... make me yours... *whimpers*"
        the_person "Oh, yes... right there... fill me up, [the_person.mc_title]... *moans*"
    return

label yandere_surprised_exclaim(the_person):
    $rando = renpy.random.choice(["Oh my god!","Wow!","This is amazing!","I'm so happy!","I can't believe this!","Oh wow!","Fuck yeah!", "Yeah baby!", "That's incredible!", "I'm so excited!", "This is the best!"])
    the_person "[rando]"
    return

label yandere_talk_busy(the_person):
    if the_person.obedience > 120:
        the_person "Oh, [mc.name], I have so many things I need to do for you... *squeals excitedly* But I'll make time for you, my love!"
    else:
        the_person "Hey, I'd love to chat, but I have so many things to do for you, [mc.name]... *giggles* Don't want to keep my favorite person waiting!"
    return

label yandere_sex_strip(the_person):
    if the_person.sluttiness < 20:
        if the_person.arousal_perc < 50:
            the_person "Oh, [mc.name], I want to make you happy... *squeals excitedly* Let me take something off for you."
        else:
            the_person "Ah, [the_person.mc_title], I'm so excited! I want to be close to you, let me take something off!"

    elif the_person.sluttiness < 60:
        if the_person.arousal_perc < 50:
            the_person "Why do I bother wearing all this, [mc.name]? I want to be yours, all yours..."
        else:
            the_person "Wait, I want to get a little more naked for you, [the_person.mc_title]. I want to feel your skin against mine..."

    else:
        if the_person.arousal_perc < 50:
            the_person "Give me a second, [the_person.mc_title], I'm going to strip something off just for you. I want you to see all of me..."
        else:
            the_person "Ugh let me get this off, [the_person.mc_title]. I want to feel you pressed against every inch of me! I'm so excited to be with you!"
    return

label yandere_sex_watch(the_person, the_sex_person, the_position):
    $ title = the_person.title if not the_person.is_stranger else "The stranger"
    if the_person.sluttiness < the_position.slut_requirement - 20:
        $ the_person.draw_person(emotion = "angry", display_transform = character_left_flipped)
        the_person "Ugh, I don't want to watch this. It's so boring."
        $ the_person.change_stats(obedience = -2, happiness = -1)
        "[title] looks away while you and [the_sex_person.fname] [the_position.verb]."
        return False

    if the_person.sluttiness < the_position.slut_requirement - 10:
        $ the_person.draw_person(display_transform = character_left_flipped)
        the_person "I don't really want to watch this, but it's kind of hot... *sighs*"
        $ the_person.change_happiness(-1)
        "[title] tries to avert her gaze and ignore you and [the_sex_person.fname] [the_position.verb]."
        return False

    if the_person.sluttiness < the_position.slut_requirement:
        $ the_person.draw_person(display_transform = character_left_flipped)
        if not is_watching(the_person):
            the_person "I don't usually watch this kind of thing, but I'll make an exception for you [the_sex_person.fname]. You're so lucky!"
        $ the_person.change_slut(1, 30)
        "[title] watches while you and [the_sex_person.fname] keep [the_position.verbing]."
        return True

    if the_person.sluttiness >= the_position.slut_requirement and the_person.sluttiness < the_position.slut_cap:
        $ the_person.draw_person(display_transform = character_left_flipped)
        if not is_watching(the_person):
            the_person "Oh wow, this is so hot! I can't believe I'm watching this... *squeals excitedly*"
        $ the_person.change_slut(1, 50)
        "[title] watches you and [the_sex_person.fname] [the_position.verb]."
        return True

    $ the_person.draw_person(emotion = "happy", display_transform = character_left_flipped)
    if renpy.random.randint(0, 1) == 0:
        the_person "Come on [the_person.mc_title], [the_sex_person.fname] is so lucky to have you! Show them how it's done!"
    else:
        call watcher_position_comment(the_person, the_sex_person, the_position) from _call_watcher_position_comment_yandere_sex_watch
    "[title] watches eagerly while you and [the_sex_person.fname] [the_position.verb]."
    return True
    return

label yandere_being_watched(the_person, the_watcher, the_position):
    $ title = the_watcher.fname if not the_watcher.is_stranger else "the stranger"
    if the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #They agree you should give it to her harder
        the_person "Oh, [the_person.mc_title], I want you to give it to me harder. Show me how much you want me... *squeals excitedly*"
        $ the_person.change_arousal(1)
        "[the_person.title] seems thrilled by [title] watching you and her [the_position.verb]."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's super slutty and doesn't care what people think.
        the_person "Oh, [the_person.mc_title], I don't care who's watching. I just want you to make me feel good... *giggles*"

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #She's super slutty and encourages the watcher to be slutty.
        the_person "Oh, come on, [title]! You know you want a taste of this too! *winks*"
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [title] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #She's into it and encouraged by the slut watching her.
        "[the_person.fname] responds to [title]."
        the_person "I'm giving him all I can right now. Any more and he's going to break me! *moans*"
        $ the_person.change_arousal(1)
        "[the_person.title] seems thrilled by [title] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's into it but shamed by the prude watching her.
        the_person "Fuck, maybe we should go somewhere a little quieter... *whispers*"
        $ the_person.change_stats(arousal = -1, slut = -1)
        "[the_person.title] seems uncomfortable with [title] nearby."

    else: #the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #They're both into it but not fanatical about it.
        "[the_person.possessive_title!c] looks directly at [title] and says..."
        the_person "Ah, now this is a party! Maybe when he's done you can tap in and take a turn! *winks*"
        $ the_person.change_stats(arousal = 1, slut = 1, max_slut = 30)
        "[the_person.title] seems more comfortable [the_position.verbing] you with [title] around."

    return

label yandere_work_enter_greeting(the_person):
    if the_person.happiness < 80 or the_person.love < 0:
        "[the_person.title] barely acknowledges your presence when you enter the room."

    elif the_person.happiness > 130:
        if the_person.sluttiness > 40:
            the_person "Hey [the_person.mc_title], down here for business or pleasure? *giggles* I hope it's the latter."
            "Her eyes sparkle with excitement as she moves closer to you."
        else:
            "[the_person.title] looks up from her work and smiles at you when you enter the room."
            "She winks and leans in close, whispering in your ear."
            the_person "Hey [the_person.mc_title], it's nice to have you stop by. You know I'm always here for you."
    else:
        if the_person.sluttiness > 60:
            $ the_person.draw_person(position = "stand4")
            "[the_person.title] walks over to you when you come into the room."
            the_person "Hey [the_person.mc_title], you came just in time. *squeals excitedly* I was getting bored without you."
            "She wraps her arms around your waist and presses her body against yours."
            the_person "I was hoping you'd stop by. Now that you're here, I don't want you to leave."
        else:
            the_person "Hey [the_person.mc_title]. Need anything? *smirks* I'm always here for you."
    return

label yandere_date_seduction(the_person):
    if the_person.is_girlfriend:
        "[the_person.possessive_title!c] grabs your hand and pulls you around to look at her."
        the_person "Hey, that was such a great time. So I was thinking..."
        $ mc.change_locked_clarity(30)
        the_person "You know what I really want, {mc.name}? I want to be closer to you. Like, really close."
        the_person "I want to feel you inside me all the time, and I want to be with you all the time too."
        the_person "So, are you ready to make us one? Let's go back to my place and make sure we can't be apart anymore."
        if the_person.effective_sluttiness(["vaginal_sex", "condomless_sex"]) > 60 and the_person.wants_creampie and the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex >= 0 and the_person.opinion.creampies >= 0 and not the_person.on_birth_control and not the_person.knows_pregnant:
            if the_person.opinion.creampies > 0: #No condoms, loves creampies, she's basically asking you to knock her up. So... have her ask you to knock her up!
                the_person "Oh, and one more thing... I want you to knock me up. Yes, you heard that right."
                the_person "I want to be pregnant with your baby, and I want to make a beautiful family together."
                "She leans in close, her eyes sparkling with excitement."
                the_person "Can you imagine how perfect our family would be? Just think about it..."
            else:
                the_person "I want you to cum inside me, [the_person.mc_title]. I want to feel you filling me up, and I want to get pregnant with your baby."
                "She reaches out and caresses your face, her touch sending shivers down your spine."
                the_person "Can you imagine how perfect our family would be? Just think about it..."
        elif the_person.effective_sluttiness(["vaginal_sex", "condomless_sex"]) > 60 and the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex > 0:
            the_person "I want you to cum inside me, [the_person.mc_title]. I want to feel you filling me up, and I want to get pregnant with your baby."
            "She reaches out and caresses your face, her touch sending shivers down your spine."
            the_person "Can you imagine how perfect our family would be? Just think about it..."
        elif the_person.effective_sluttiness(["vaginal_sex"]) > 50 and the_person.opinion.vaginal_sex > 0:
            the_person "You know what I want, [the_person.mc_title]? I want you to fuck me hard, and I want to feel you deep inside me."
            the_person "And if we make a baby, well... that would just be the best surprise ever!"
            "She wraps her arms around you, pulling you close."
        elif the_person.effective_sluttiness(["anal_sex"]) > 60 and the_person.opinion.anal_sex > 0:
            the_perthe_person "I want to feel you inside me, [the_person.mc_title]. Anywhere, everywhere."
            the_person "And if we make a baby, well... I wouldn't mind at all. It would just be a sign of how much we love each other."
            "She winks at you, her eyes gleaming with mischief."
        elif the_person.effective_sluttiness(["sucking_cock"]) > 40 and the_person.opinion.giving_blowjobs > 0:
            the_person "I want to give you a blowjob, [the_person.mc_title]. A really good one."
            the_person "And if we make a baby... well, I wouldn't be surprised. I just want to be close to you all the time."
            "She leans in and kisses your neck, her lips warm against your skin."
        elif the_person.effective_sluttiness() > 40 and the_person.opinion.being_covered_in_cum > 0:
            the_person "I want to feel you cum inside me, [the_person.mc_title]. I want to taste it, and I want to swallow it all."
            the_person "And if we make a baby... well, that would just be the ultimate proof of how much we love each other."
            "She reaches down and caresses your erection, her touch sending shivers through you."
        elif the_person.effective_sluttiness(["touching_body"]) > 40 and the_person.opinion.giving_tit_fucks > 0 and the_person.has_large_tits:
            the_person "I need to feel your cock inside me, [the_person.mc_title], and I want to do it now. Let's go back to my place and fuck until we're both satisfied."
            the_person "Think of how good it will feel, having my tits wrapped around your cock, and how much I want to feel you deep inside me."
            the_person "Come on, [the_person.mc_title], let's go. I'm already getting wet thinking about it."
            "She grabs your hand and starts pulling you towards the door, her eyes never leaving yours."
        else: #She's not very slutty, so she leaves the invitation open to interpretation
            the_person "You're mine now, [the_person.mc_title], and I won't let you go. Let's go back to my place and make sure that never changes."
            "Her eyes gleam with a fierce possessiveness as she leans in closer to you, her breath warm on your face."
            "She nips your earlobe gently before pulling back and looking into your eyes."
    elif the_person.is_affair:
        the_person "So my [the_person.so_title] won't be home tonight, and I'm all yours. I was thinking..."
        "She leans in close, her eyes gleaming with an obsessive intensity."
        $ mc.change_locked_clarity(40)
        if the_person.wants_creampie and the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex >= 0 and the_person.opinion.creampies >= 0 and not the_person.on_birth_control and not the_person.knows_pregnant:
            if the_person.opinion.creampies > 0: #No condoms, loves creampies, she's basically asking you to knock her up. So... have her ask you to knock her up!
                the_person "Let's go back to my place, [the_person.mc_title]. I want you to fill me up with your cum, and make me your little mommy."
                the_person "I want to be pregnant with your baby, to carry your child inside me. Just thinking about it makes me so wet."
            else:
                the_person "Let's go back to my place. I want you to fuck me bareback, to feel your cock sliding inside me without any barrier."
                the_person "I want to be your slut, your fucktoy, your everything. I want to feel you cumming inside me, filling me up."
        elif the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex > 0:
            # the_person "Do you want to come over to my place and fuck me all night long? No condoms allowed."
            the_person "Let's go back to my place, [the_person.mc_title]. I want you to fuck me all night long, any way you want, as long as you follow one simple rule."
            the_person "No condoms. I want to feel you deep inside me, without anything between us."
        elif the_person.opinion.vaginal_sex > 0:
            the_person "Let's go back to my place and you can make me yours, [the_person.mc_title]. I want you to take me, to use me, to fuck me until I'm cumming."
            the_person "Do you want to do this? Do you want to make me yours?"
        elif the_person.opinion.anal_sex > 0:
            the_person "Let's go back to my place, [the_person.mc_title]. I want you to take me from behind, to stretch me open and fill me up."
            the_person "I want to feel you deep inside me, to feel you claiming me as yours."
        elif the_person.opinion.giving_blowjobs > 0:
            the_person "Let's go back to my place, [the_person.mc_title]. I want to suck your cock, to feel it in my mouth and to make you cum."
            the_person "I want to be your slut, your cock sucker, your everything. I want to feel you cumming in my mouth."
        elif the_person.opinion.being_covered_in_cum > 0:
            the_person "Let's go back to my place, [the_person.mc_title]. I want to be covered in your cum, to feel it dripping down my face, my breasts, and my stomach."
            the_person "I want to be your cum slut, your cum whore, your everything. I want to feel you cumming all over me."
        elif the_person.opinion.giving_tit_fucks > 0 and the_person.has_large_tits:
            the_person "Let's go back to my place, [the_person.mc_title]. I want to feel your cock between my tits, to fuck it until you cum."
            the_person "I want to be your tit fucker, your cock milker, your everything. I want to feel you cumming between my breasts."
        elif the_person.opinion.cheating_on_men > 0:
            the_person "Let's go back to my place, [the_person.mc_title]. I want to be your slut, your fucktoy, your everything."
            the_person "I want to do all the things I'm not supposed to do, all the things my husband would never allow."
            the_person "I want to be yours, completely and utterly, and I want to make you happy."
        else:
            the_person "Let's go back to my place, [the_person.mc_title], and make sure that this is where we both belong."
            "Her eyes gleam with a fierce possessiveness as she reaches out and takes your hand."
    elif not the_person.has_significant_other:
        $ mc.change_locked_clarity(20)
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                the_person "I want to take you home with me, [the_person.mc_title], and show you all the ways I can make you happy."
                the_person "I want to be yours, completely and utterly, and I want to make you mine."
            else:
                the_person "I don't want to say goodbye, [the_person.mc_title]. I want to take you back to my place and keep you with me all night."
                the_person "I want to be with you, to touch you, to make you mine."
        else:
            if the_person.love > 40:
                the_person "You're the only one I want, [the_person.mc_title]. I don't want to be with anyone else."
                the_person "I want to take you home with me, to keep you safe and make you mine."
            else:
                the_person "I can't stop thinking about you, [the_person.mc_title]. I want to take you back to my place and make you mine."
                the_person "I want to be with you, to feel you close to me, to make you mine."
    else:
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                $ mc.change_locked_clarity(20)
                the_person "I want to be alone with you, [the_person.mc_title], and I want it to be at my place. Will you come with me?"
                the_person "My [the_person.so_title] won't be home until morning, and I'll make sure we have the whole night to ourselves."
            else:
                $ mc.change_locked_clarity(20)
                the_person "I don't want to say goodbye, [the_person.mc_title]. Do you want to come back to my place and keep me company?"
                the_person "My [the_person.so_title] is away, and I don't want to be left all alone in this big empty house."
        else:
            if the_person.love > 40:
                $ mc.change_locked_clarity(20)
                the_person "I don't want to let you go, [the_person.mc_title]. Do you want to come to my place and stay with me?"
                the_person "My [the_person.so_title] won't be home until morning, and I want you to be the one to keep me warm."
            else:
                $ mc.change_locked_clarity(20)
                the_person "This might be crazy, but I want you to come to my place. My [the_person.so_title] won't be home until morning..."
                the_person "I want to be with you, [the_person.mc_title], and I don't want to be apart from you anymore."
    return

label yandere_sex_end_early(the_person):
    if the_person.sluttiness > 50:
        if the_person.love > 40:
            if the_person.arousal_perc > 60:
                the_person "Mmm, I'm still so aroused from that, [the_person.mc_title]. You must be exhausted, but I'm not done yet..."
                the_person "You're going to have to keep up with me, [mc.name]. I won't let you rest until we've both had our fill."
            else:
                the_person "Wow, you really know how to tire a girl out, [mc.name]. I'm not even close to being finished with you..."
                the_person "You're going to have to be more careful with me, [the_person.mc_title]. I'm not going to let you escape that easily."
        else:
            if the_person.arousal_perc > 60:
                the_person "You're sure you're done? I could go another round or two, [the_person.mc_title]..."
                the_person "I won't let you leave me unsatisfied, [mc.name]. We're not finished yet."
            else:
                the_person "That was... interesting. You're not bad in bed, I suppose."
                the_person "But don't think you've won me over that easily, [mc.name]. I'm not going to let you get too comfortable."

    else:
        if the_person.love > 40:
            if the_person.arousal_perc > 60:
                the_person "Oh, [the_person.mc_title], you have no idea how much you've turned me on... I think I might explode if we don't do it again soon!"
                the_person "I don't want to let you go, [mc.name]. I need more of you."
            else:
                the_person "I'm glad you enjoyed it, [the_person.mc_title]. I did, too."
                the_person "But don't think we're done here, [mc.name]. I want to see more of you."
        else:
            if the_person.arousal_perc > 60:
                the_person "Hmph, you're done already? I suppose that's for the best. I wouldn't want you to get too tired."
                the_person "But don't think you're off the hook, [mc.name]. I'll be watching you."
            else:
                the_person "Good, we can go do something else now. I'm not really in the mood for more... intimacy."
                the_person "But don't get too comfortable, [mc.name]. I'll be back for more soon."
    return

label yandere_sex_take_control(the_person):
    if the_person.arousal_perc > 60:
        the_person "Oh no, you're not going to leave me hanging like this, [mc.name]!"
        the_person "I've been waiting for this moment, and I won't let you go until we're both satisfied."
    else:
        the_person "You can't just tease me like this and then stop! I need more, [mc.name]!"
        the_person "Don't think you can escape me that easily. We're just getting started."
    return

label yandere_sex_beg_finish(the_person):
    the_person "Oh god, [the_person.mc_title], I can't hold back anymore... Please, please let me finish with you!"
    the_person "I need it so badly, and I'll do anything to make sure you're happy, [the_person.mc_title]. Just give me this."
    return

label yandere_sex_review(the_person, the_report):
    $ comment_position = the_person.pick_position_comment(the_report)
    if comment_position is None:
        return #You didn't actually do anything, no need to comment.

    $ used_obedience = the_report.get("obedience_used", False) #True if a girl only tried a position because you ordered her to.
    $ the_person.draw_person()  # make sure she stands up for talking with you

    #She's worried about her SO finding out because it was in public
    if the_report.get("was_public", False) and the_person.has_significant_other and the_person.opinion.cheating_on_men <= 0: #It was public and she cares.
        if the_person.is_affair: #Dialogue about her being into it, but you can't do this in case she gets caught.
            the_person "Oh god, we were just seen by someone, weren't we? That's not good... I need to make sure my [the_person.so_title] doesn't find out."
            the_person "I'm going to have to be extra careful from now on, or else everything will fall apart."
        elif used_obedience:
            the_person "This is not good, [the_person.mc_title]. Someone saw us, and if they tell my [the_person.so_title], it's all over."
            the_person "I need to make sure you're extra careful from now on, or else everything will fall apart."

        else:
            $ the_person.call_dialogue("surprised_exclaim")
            the_person "Oh no, someone saw us... I hope my [the_person.so_title] doesn't find out!"
            the_person "I'll have to be more careful from now on, or else this is going to blow up in our faces."

    #She's single, but worried that you did in public.
    elif the_report.get("was_public", False) and (the_person.effective_sluttiness()+10*the_person.opinion.public_sex < comment_position.slut_cap):
        if used_obedience:
            the_person "This is not good, [the_person.mc_title]. Someone saw us, and now I'm going to be the talk of the town."
            the_person "I need to make sure you're more careful from now on, or else I'm going to have a reputation for being a slut."
        else:
            the_person "Oh no, someone saw us... I hope nobody finds out about this."
            the_person "I need to make sure you're more careful from now on, or else I'm going to have a reputation for being a slut."

    elif the_report.get("girl orgasms", 0) > 2:
        if used_obedience:
            the_person "Oh god, [the_person.mc_title], you make me feel so good... I can't get enough of this!"
            the_person "I want to feel it again and again, [the_person.mc_title]. Don't stop now, please..."
            mc.name "I'm not going to stop until you're satisfied, my dear. You know I love seeing you like this."
            "[the_person.possessive_title!c] smiles wickedly, clearly enjoying the moment."
        else:
            the_person "I... I've never felt anything like that before... You're making me feel so alive!"
            the_person "Please, [the_person.mc_title], don't stop. I need to feel it again, and again, and again..."
            mc.name "I'll give you as many orgasms as you want, my dear. You know I love seeing you like this."
            the_person "Thank you, [the_person.mc_title]... You're the best... partner... ever."

        call sex_review_trance(the_person) from _call_sex_review_trance_yandere_sex_review

    #No special conditions, just respond based on how orgasmed and how slutty the position was.
    elif the_report.get("girl orgasms", 0) > 0 and the_report.get("guy orgasms", 0) > 0: #You both came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position cap, it was tame
            the_person "Mmph... that was delicious. *nuzzles into your chest* Next time, let's explore more of each other's bodies."
            the_person "I want to feel you trembling with pleasure, [mc.name]. *gently bites your nipple*"
            the_person "I bet we could push each other to new heights. Wouldn't you like that, [mc.name]?"
        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "Fuuuuck... that was amazing! I could feel my heart racing and my body trembling. You make me feel alive, [mc.name]."
            "She wraps her legs around you and starts to straddle you, while smiling wickedly..."
            the_person "Let's do it again and again, okay?"
        elif used_obedience: #She only did it because she was commanded
            the_person "Ah, fuck... I... I didn't think I'd be able to climax like that."
            mc.name "Aren't you going to thank me? You obviously enjoyed yourself."
            the_person "Hmph. Maybe. But don't expect me to be so compliant next time."
            "She grins mischievously."
        else: # She's surprised she even tried that.
            the_person "Oh my god, that was so intense!"
            "She clasps her hands around your neck and looks deeply into your eyes."
            the_person "I didn't think I'd be able to go there, but it felt so right, you know?"
            the_person "But don't think that means I'll be easy next time. I'm still the same person, [mc.name]."
            "She gives you a playful bite on the ear and sexily growls."

    elif the_report.get("girl orgasms", 0) > 0: #Only she came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            the_person "Done already? Well, that's just not right. *pouts playfully* Next time I'm going to make sure we both cum... and maybe even more."
            the_person "I've got a few ideas that are going to blow you away, [mc.name]."
            "She smiles mischievously, already imagining your next encounter."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "You're all done? Well, that was fucking hot either way, [mc.name]."
            "She blushes, then leans in close to your ear ans whispers..."
            the_person "I'll repay the favour next time, alright? I promise."

        elif used_obedience: #She only did it because she was commanded
            the_person "That's it? I mean, not like I wanted to do anything more, I just thought you were going to finish. *sighs*"
            mc.name "Some other time. I just wanted to see what you look like when you cum. *grins*"
            the_person "I... Fuck, well, I guess you got what you wanted. *looks down, embarrassed*"
            the_person "It could have been worse, I guess. *smirks*"

        else: # She's surprised she even tried that.
            the_person "Oh fuck, that was intense! You really know how to make a girl feel good!"
            the_person "You're probably tired after all that work. I promise I'll repay the favour next time, okay?"

    elif the_report.get("guy orgasms", 0) > 0: #Only you came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            the_person "You're already done? How disappointing... I was just getting started."
            "Her eyes narrow, and she creeps closer, her body language becoming more suggestive."
            mc.name "Sorry, I'll make it up to you next time."
            the_person "Oh, I'm sure you will. And when you do, I'll make sure to be even more... accommodating."
            "She leans in, her lips brushing against your ear, sending shivers down your spine."
            mc.name "I'm looking forward to it."
        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "Tired out already? What a shame... I was hoping for a longer session."
            "She moves closer, her body pressed against yours, her breath hot against your ear."
            mc.name "Sorry, I'll make it up to you next time."
            the_person "You'd better, or else... I might just have to find other ways to get my needs met."
            "She giggles, her voice husky with desire, her eyes locked onto yours."
            mc.name "I'll keep that in mind."
        elif used_obedience: #She only did it because she was commanded
            the_person "Finished already? That's too bad... I was enjoying it."
            "Her lower lip pouts out in a childish expression, her eyes filling with disappointment."
            mc.name "Yeah, that's all for now."
            the_person "Alright, I'll just have to find other ways to satisfy myself then."
            "She nods, her expression softening, but her eyes still holding a hint of mischief."
        else:  # She's surprised she even tried that.
            the_person "Wow, that was... interesting. I didn't know I had it in me."
            "She blushes, her cheeks flushing with color, her eyes sparkling with excitement."
            the_person "But I think we should stop for now... before things get out of hand."
            "She moves away slightly, her body language becoming more reserved, but her eyes still holding a trace of desire."

    elif the_person.energy < 10: #Nobody came and she's tired
        the_person "Sorry, but I'm too exhausted. I think I need some... rest."
        "She lies down, her body sinking into the mattress, her eyes closing as she exhales a tired sigh."
        mc.name "No problem, we can continue this another time."
        the_person "Yes, please do. I'm looking forward to it."
        "She smiles seductively, her eyes opening lazily, her body language still hinting at her desire."

    else: #Nobody came.
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            the_person "You're done already? Oh come on, we barely even got started! *pouts*"
            "She crosses her arms over her chest, her eyes narrowing in disappointment."
            mc.name "Sorry [the_person.title], I'll have to make it up to you some other time."
            the_person "You're such a tease [the_person.mc_title]. *leans in*"
            "Her lips brush against your cheek, sending shivers down your spine."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "We're stopping already? We were just getting to the good stuff though! *giggles*"
            "She wiggles her eyebrows, her eyes sparkling with excitement."
            mc.name "Sorry [the_person.title], I'll have to make it up to you some other time."
            the_person "You better. You can't just tease a girl like this, it's not nice."
            if not the_person.is_bald:
                "Her fingers run through the strands, her movements smooth and seductive."

        elif used_obedience: #She only did it because she was commanded
            the_person "That's all? Well that's not exactly what I was expecting. *frowns*"
            "Her eyes narrow, her expression turning sour."
            mc.name "You aren't disappointed, are you?"
            the_person "No, I just... Thought this was all going to go somewhere more serious. *sighs*"
            "She slumps her shoulders, her body language conveying her disappointment."
            the_person "Whatever, it doesn't matter. *shrugs*"
            "Her expression softens slightly, but her eyes still hold a hint of resentment."

        else:  # She's surprised she even tried that.
            the_person "Fuck, you're probably right. We should stop now before we take this too far. *blushes*"
            "She blushes, her cheeks flushing with color."
            the_person "If I get too turned on I might do something I regret. Let's just keep this casual. *moves closer*"
            "She moves closer, her body language becoming more intimate, her eyes locked onto yours."

    # Gave creampie while she is not on birth control (extra dialogue when she could get pregnant)
    if the_report.get("creampies", 0) > 0 and not the_person.on_birth_control and not the_person.knows_pregnant:
        the_person "Oh baby, you are a mad dog, you must really want to see me pregnant. *giggles*"
        "Her eyes sparkle with mischief, her lips curling into a seductive smile."
        the_person "I might just let you do it again... for old times' sake. *winks*"
        "Her wink is playful, but her eyes hold a hint of vulnerability, hinting at her true desires."

    $ del comment_position
    return

## Role Specific Section ##
label yandere_improved_serum_unlock(the_person):
    mc.name "[the_person.title], it's time we had a little chat about something."
    the_person "Hmm, what's on your mind?"
    mc.name "Our research has been based on my old notes, but there's something I haven't mentioned yet."
    mc.name "There were some unofficial experiment results that suggested the effects might be enhanced by sexual arousal."
    "[the_person.possessive_title!c] looks intrigued, and leans forward, her eyes glinting with excitement."
    the_person "You've noticed that too? I've always thought that an orgasm could unlock something deeper."
    mc.name "If that's true, what could we do to leverage it?"
    the_person "If it's true, I could use it to induce greater effects in our test subjects."
    "[the_person.title] grins wickedly, her lips parted slightly."
    the_person "But we need to test it first."
    mc.name "What kind of test?"
    the_person "I'll take a dose of serum, and you can observe the effects."
    the_person "Then I'll make myself cum, and we'll compare the results."
    mc.name "Are you sure that's a good idea?"
    the_person "No, not really. But we can't trust anyone else with this information."
    the_person "This could be our chance to make a breakthrough."
    the_person "I want a dose of serum that maximizes my Suggestibility. The higher, the better."
    the_person "We'll need to find a private spot and some time for me to see what happens."
    return

#
# label yandere_improved_serum_unlock(the_person):
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
label yandere_kissing_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 30:
        the_person "Oh, come on [mc.name], don't pretend like you don't want this. We both know where this is going."
        "[the_person.title]'s eyes spark with excitement as she leans in, her lips slightly parted."
        the_person "You've always wanted to kiss me, haven't you?"
        "[the_person.title]'s hand slides up your arm, her fingers trailing softly against your skin."
    elif the_person.love >= 20:
        the_person "Finally, we're doing this. It's about time, don't you think?"
        mc.name "I guess we are. What do you think?"
        the_person "It's about time we made out, I've wanted to for a long time."
        "[the_person.title]'s fingers dance across your chest, her nails lightly scratching your skin."
    else:
        the_person "I don't know if this is a good idea [the_person.mc_title], do you think we're rushing into this?"
        mc.name "Are you scared?"
        the_person "No! I mean, a little. But I'm excited too."
        mc.name "Then just trust me."
        "[the_person.title]'s eyes light up, and she nuzzles closer to you, her breath warm against your skin."
        "[the_person.title]'s hand slides up to cup your cheek, her fingers tracing the shape of your face."
    return

label yandere_touching_body_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 30:
        the_person "Ready to get a little closer, aren't we? Don't want to back out now, do you?"
        mc.name "Of course not."
        the_person "Good. Let's do this."
        "[the_person.title]'s fingers dance up your arm, her touch electric."
        "[the_person.title]'s nose nuzzles gently against your ear, her breath warm and inviting."
    elif the_person.love >= 20:
        the_person "You really want to do this, huh?"
        "You nod."
        the_person "Me too. I didn't think I'd be this nervous, but I guess I'm excited too."
        mc.name "Just relax. You trust me, right?"
        the_person "More than anything."
        "[the_person.title]'s hands intertwine with yours, her eyes locked on his."
        "[the_person.title]'s other hand traces the outline of your face, her touch possessive."
    else:
        the_person "I think we're moving a bit fast here, don't you?"
        mc.name "Why's that?"
        the_person "Because I don't just let anyone touch me like this. But if you want to... we can."
        mc.name "You're not scared, are you?"
        the_person "Scared? Of course not! I'm just... cautious."
        mc.name "Well then just relax and go with it. It doesn't have to mean anything unless we want it to."
        "You see her answer in her eyes before she says anything."
        the_person "You're so tempting, you know that?"
        mc.name "Well let me make up for it then."
        "[the_person.title]'s fingers trace the muscles of your chest, her touch possessive."
        "[the_person.title]'s lips brush against yours, her kiss hungry and demanding."
    return

label yandere_touching_penis_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 35:
        the_person "Mmm, you're really turned on too, right? Look at how hard you are."
        mc.name "Do you want to feel it?"
        the_person "I thought you'd never ask."
        "[the_person.title]'s hand slides down your stomach, her fingers tracing the contours of your body."
        "Her touch is electric, sending shivers down your spine."
        "[the_person.title]'s hand wraps around your erection, her grip firm and possessive."
    elif the_person.love >= 20:
        the_person "Your cock looks so nice when it's hard. Can I touch it?"
        mc.name "Go ahead, it doesn't bite."
        the_person "If you're lucky it might choke me though."
        "[the_person.title]'s hand wraps around your erection, her fingers squeezing gently."
        "Her touch is almost playful, but there's an edge of hunger to it."
    else:
        mc.name "My cock is so hard right now [the_person.title]. Put your hand on it and touch it for me."
        the_person "What? That's taking things a little far, don't you think?"
        mc.name "Come on, you know you want to. Just a few strokes, then if you aren't impressed you can stop."
        "[the_person.title]'s eyes lock onto yours, her gaze challenging."
        "[the_person.title]'s hand reaches out, her fingers wrapping around your erection."
        "There's a sense of daring in her touch, like she's daring you to stop her."
    return

label yandere_touching_vagina_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 35:
        the_person "Don't be shy now, you've got your chance to touch me where it counts."
        "[the_person.title]'s hand slides down her stomach, her fingers tracing the contours of her body."
        "Her touch is bold and confident, daring you to follow."
        "[the_person.title] leans in, her lips brushing against your ear."
    elif the_person.love >= 20:
        the_person "Oh fuck, you've got my pussy so wet. I want you to touch it [the_person.mc_title]."
        "[the_person.title]'s hand reaches out, her fingers brushing against yours."
        "Her touch is possessive, like she's claiming you as her own."
        "[the_person.title]'s eyes lock onto yours, her gaze hungry and demanding."
    else:
        the_person "I don't know if we should be doing this [the_person.mc_title]..."
        mc.name "Just take a deep breath and relax. I'm just going to touch you a little, and if you don't like it I'll stop."
        the_person "Just a little?"
        mc.name "Just a little. Trust me, it's going to feel amazing."
        "[the_person.title]'s hand reaches out, her fingers brushing against yours."
        "Her touch is tentative, but there's a sense of excitement beneath the surface."
        "[the_person.title]'s other hand slides up to cup your face, her thumb tracing the curve of your cheekbone."
    return

label yandere_sucking_cock_taboo_break(the_person):
    mc.name "I want you to do something for me."
    the_person "Oh yeah? What do you want me to do to you?"
    mc.name "I want you to suck on my cock."
    if the_person.effective_sluttiness() >= 45:
        the_person "Mmm, I think I'm ready to take you on. But don't say I didn't warn you."
        mc.name "I'm counting on it."
        the_person "Just remember, I'm the one in control here."
        "Her lips wrap around your cock, her tongue swirling around the head."
    elif the_person.love >= 30:
        the_person "I've been waiting for this moment. You've been teasing me long enough."
        "She pouts, her eyes flashing with desire."
        the_person "Now, let's see what you're really made of."
        "[the_person.title] drops to her knees, her lips wrapping around your cock. Her eyes never leave yours, her gaze filled with lust and control."
    else:
        the_person "Oh, I've been wanting to do this for a while now."
        "She licks her lips, her eyes gleaming with a dangerous promise."
        the_person "So, are you ready for me to take you to the edge?"
        mc.name "I've been waiting for this."
        the_person "Good. Then let's see how far we can push things."
        "[the_person.title] drops to her knees, her lips wrapping around your cock. Her eyes never leave yours, her gaze filled with lust and a hint of danger."
        "[the_person.title]'s hand slides up your thigh, her fingers digging into your flesh with a possessive grip."
    return

label yandere_licking_pussy_taboo_break(the_person):
    mc.name "I want to taste your pussy [the_person.title]. Are you ready to let me possess this secret?"
    if the_person.effective_sluttiness() >= 45:
        the_person "Oh, I've been dying for you to ask! I'm burning up with anticipation!"
    elif the_person.love >= 30:
        the_person "You're the only man who's ever dared to offer me this kind of pleasure. I'll reward you for your boldness."
        "She runs her fingers through your hair, her eyes burning with intensity."
        the_person "So, are you going to make me scream with pleasure, or what?"
    else:
        if the_person.has_taboo("sucking_cock"):
            the_person "I can see the hunger in your eyes. You really want to taste me, don't you? Most men would never dream of it."
            "She leans in closer, her breath hot against your ear."
            the_person "But I like that you're willing to break the rules. So go ahead and indulge in me."
        else:
            the_person "I've been waiting for you to take control and show me what you're made of. You're not like the other men who only care about their own pleasure."
            "She grabs your hand and pulls you closer, her eyes glinting with danger."
            the_person "So, are you going to make me feel like I'm the only one who matters, or what?"
    return

label yandere_vaginal_sex_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 60:
        the_person "Finally, you're going to give me what I've been craving. Come on, thrust that cock inside me and make me burn!"
    elif the_person.love >= 45:
        the_person "You've been teasing me for so long, it's time to pay the price. I want to feel your passion, your hunger."
        mc.name "I've been waiting for this moment."
        the_person "Good, because I'm going to devour you whole. Come on then, fuck me like there's no tomorrow!"
    else:
        if the_person.has_taboo("anal_sex"):
            the_person "Your eyes are burning with desire, I can see it. You're going to make me scream and beg for more."
            mc.name "I'm not sure what you're talking about."
            the_person "Oh, don't play dumb with me. I know you want to take me to the edge and push me over."
        else:
            the_person "Your cock looks like a weapon, ready to tear me apart. I can't wait to see how far you'll take me."
            the_person "Come on, fuck me [the_person.mc_title]! Make me yours and don't let me go!"
    return

label yandere_anal_sex_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 75:
        the_person "I've been waiting for this moment, [mc.name]. Your cock is going to take me to places I've never been before."
        mc.name "You're sure you're ready for this?"
        the_person "I'm more than ready, I crave it. I need you to make me yours."
        "She moves closer to you, her eyes locked on his."
        the_person "Come on, touch me, claim me."
    elif the_person.love >= 60:
        the_person "You want to make me yours, don't you? You want to possess me, body and soul."
        mc.name "That's right."
        the_person "Good. Because I want you to. I want you to take me, use me, make me yours."
        "She leans in, her lips brushing against your ear."
        the_person "Please, [mc.name], make me yours."
    else:
        if the_person.has_taboo("vaginal_sex"):
            the_person "You're not going to use my pussy? But why? I thought you wanted to be with me."
            mc.name "I do, but I want to do something different. Something that will make you mine forever."
            the_person "Oh, I see. Well, if you're sure..."
            mc.name "I'm positive."
            the_person "Okay, I'll try. But if it hurts too much, I'm blaming you."
        else:
            "She takes a deep breath and looks at you with a mix of excitement and apprehension."
            the_person "Okay, here we go... Please don't hurt me too badly."
            mc.name "I'll be gentle, but don't expect me to hold back."
            the_person "I wouldn't dream of it."
            "She moves closer, her eyes never leaving yours."
            the_person "Now, are you going to make me yours, or do I have to take matters into my own hands?"
    return

label yandere_condomless_sex_taboo_break(the_person):
    if the_person.knows_pregnant:
        the_person "Raw sex, how thrilling. I've always wanted to feel you deep inside me, bare and unprotected."
        if the_person.wants_creampie:
            the_person "Please, make me yours. Fill me with your hot cum and make me pregnant."
            "She moves closer, her eyes locked on yours."
            the_person "Come on, fill me up and make me yours."
        else:
            the_person "Please, claim me. Cover me with your essence and make me yours."
            "She leans in, her lips brushing against your ear."
            the_person "Make me yours, [mc.name]. Make me yours."
    elif the_person.opinion.bareback_sex > 0:
        the_person "Raw sex, how daring. I've always wanted to feel the intensity of unprotected sex."
        if the_person.on_birth_control:
            the_person "I'm on the pill, so you don't need to worry about cumming inside me."
            $ the_person.update_birth_control_knowledge()
        elif the_person.wants_creampie:
            the_person "It would be so deliciously reckless to cum inside me."
            the_person "So easy for you to fill me up with your hot cum..."
            "Her words are laced with excitement and desire."
            "She moves closer, her hands reaching out to touch you."
        elif the_person.opinion.creampies < 0:
            the_person "But you better make sure you pull out though. I'd be furious if you got me pregnant."
            "She narrows her eyes, her voice taking on a threatening tone."
        else:
            the_person "You'll need to pull out so you don't knock me up. Do it for me, please."
            "She takes your hand, her grip firm and possessive."
            the_person "Make me yours, [mc.name]. Make me yours."

    elif the_person.love > 60:
        if the_person.on_birth_control:
            the_person "You want to fuck me raw? Fuck it, I'm on the pill. What's the worst that can happen?"
            $ the_person.update_birth_control_knowledge()
            "She moves closer, her eyes locked on yours."
            the_person "Come on, let's do this. I want to feel you deep inside me."
            "She leans in, her lips brushing against your ear."
            the_person "Make me yours, [mc.name]. Make me yours."
        elif the_person.wants_creampie:
            the_person "I guess if I can't trust you, I can't trust anyone. You make me make terrible decisions, you know that?"
            the_person "Well fuck it, if we're doing this, I want you to go the whole nine yards and finish inside me."
            "She moves closer, her hands reaching out to touch you."
            the_person "Please, fill me up with your cum and make me yours."
            "She looks you straight in the eye, her expression intense."
            the_person "Now, give me your babies!"
            $ the_person.update_birth_control_knowledge()
        elif the_person.opinion.creampies < 0:
            the_person "I guess if I can't trust you, I can't trust anyone. You make me make terrible decisions, you know that?"
            the_person "You'll need to pull out though. If you get me knocked up, there's no way we're ever doing it unprotected again."
            "She narrows her eyes, her voice taking on a threatening tone."
        else:
            the_person "I guess if I can't trust you I can't trust anyone. You make me make terrible decisions, you know that?"
            if the_person.kids == 0:
                the_person "I need you to pull out though. I'm not quite ready to be a mother, even with you."
                "She moves closer, her hands reaching out to touch yours."
                the_person "Do it for me, please."
            elif the_person.kids == 1:
                the_person "I need you to pull out though. I've already got a kid, I don't need another one."
                "She grabs your hand, her grip firm and possessive."
                the_person "Make me yours, [mc.name]. Make me yours."
            else:
                the_person "I need you to pull out though. I've already got kids, I don't need another one."
                "She moves closer, her lips brushing against your ear."
                the_person "Please, [mc.name], make me yours."
            "Her words are laced with anger and possessiveness."

    else:
        if the_person.on_birth_control:
            the_person "You want to fuck me without a condom? I'm on the pill, so why not?"
            $ the_person.update_birth_control_knowledge()
            "She moves closer, her eyes locked on yours."
            the_person "Come on, let's do this. I want to feel you deep inside me."
            "She leans in, her lips brushing against your ear."
            the_person "Make me yours, [mc.name]. Make me yours."
        elif the_person.has_taboo("vaginal_sex"):
            the_person "You're sure we shouldn't use a condom? I'm not on the pill, aren't you worried about getting me pregnant?"
            $ the_person.update_birth_control_knowledge()
            the_person "Or is this your plan to surprise me with a baby?"
            mc.name "I promise I'll pull out. Our first time together will be special."
            "She rolls her eyes and sighs."
            the_person "Alright, alright. No condom."
            the_person "But you better pull out, understand? Good..... or don't"
            "She smirks and squirms at the last thought..."
        else:
            the_person "You're sure we shouldn't use a condom? I'm not on the pill, aren't you concerned about getting me pregnant?"
            $ the_person.update_birth_control_knowledge()
            the_person "Or is this your plan to create a little surprise for me?"
            mc.name "I promise I'll pull out. It'll feel better without anything in the way."
            the_person "I know, I know. I'm trying to think with my head and not my hormones."
            "She sighs dramatically."
            the_person "Fine, no condom. Just remember to pull out, alright?"
            "She moves closer, her eyes locked on yours."
            the_person "Now, are you going to make me yours, or do I need to take matters into my own hands?"
    return

label yandere_underwear_nudity_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > 30 - (the_person.opinion.skimpy_outfits * 5):
        the_person "You want to see me in my underwear, huh? How adorable, you're just like my dear diary, always eager to see me undressed."
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "Oh, please, let's not make me wait any longer than necessary."
        else:
            mc.name "Adorable? I've seen you naked before, remember?"
            the_person "Yes, but there's something thrilling about being undressed just for you."

    elif the_person.love > 15:
        the_person "You want me to strip down a little? Darling, you're spoiling me. Come on, let's get this over with."
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "Well then let's stop wasting time and get your [the_clothing.display_name] off."

        else:
            mc.name "Spoiling me? I've already seen you naked, sweetie."
            the_person "True, but this time it's different, just you and me."
            mc.name "Well let's get more romantic then and get your [the_clothing.display_name] off."

    else:
        the_person "If you take my [the_clothing.display_name], I'll be practically naked. Are you sure you're ready for that?"
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "I'm more than ready, my dear."
            "She giggles and blushes."
            the_person "Oh [the_person.title], you're so wicked! Alright, let's do it!"
        else:
            mc.name "I'm more than ready, sweetheart."
            the_person "Yeah, yeah, get it off then."
    return

label yandere_bare_tits_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > (40 - the_person.opinion.showing_her_tits * 5):
        the_person "Oh, you're finally ready to feast your eyes on my delightful décolletage, [the_person.mc_title]? I can't help but feel a thrill at the prospect of baring it all for you."
        if the_person.has_large_tits:
            "She sensuously undulates her hips, causing her [the_person.tits_description] to sway tantalizingly beneath her [the_clothing.display_name], as if beckoning you to unveil them."
        else:
            "She flirtatiously jiggles her chest, giving her [the_person.tits_description] a playful shimmy."
        the_person "What took you so long to ask?"
        if the_person.has_large_tits:
            mc.name "No time like the present, right? Let's give those luscious ladies a proper unveiling."
        else:
            mc.name "No time like the present, right? Let's get those adorable mounds out."

    elif the_person.love > 25:
        the_person "Are you prepared to witness the majesty of my bare bosom, [the_person.mc_title]?"
        if the_person.has_large_tits:
            "She provocatively shakes her chest, causing her [the_person.tits_description] to bounce seductively beneath her [the_clothing.display_name], teasing you with a glimpse of what's to come."
        else:
            "She coquettishly jiggles her chest, giving her [the_person.tits_description] a teasing wiggle."
        mc.name "Oh yeah, I'm ready."
        the_person "Then let's get this show on the road, and don't hold back!"

    else:
        the_person "Hold up! You can't just expect me to strip down like this without a proper invitation!"
        mc.name "Come on, don't you want to show off those lovely assets? I'm sure they're stunning."
        the_person "Oh, they are. But I feel a little vulnerable being naked around you, alright?"
        mc.name "Nonsense, my dear. I'm here to pleasure you, not judge you. Now, let's take that [the_clothing.display_name] off and enjoy the view."
        the_person "Alright, alright... But don't say I didn't warn you!"
    return

label yandere_bare_pussy_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > (50 - the_person.opinion.showing_her_ass * 5):
        the_person "Ah, you finally want to unveil the secrets hidden beneath my [the_clothing.display_name], don't you, [the_person.mc_title]? I must admit, I've been eagerly anticipating this moment."
        if the_person.has_taboo("touching_vagina"):
            mc.name "I know, I just can't resist the temptation. Your pussy is like a forbidden fruit, and I'm the one who's going to take a bite."
            the_person "Well, you've been such a good boy, haven't you? Alright, let's take off this [the_clothing.display_name] and reveal the treasure that's been waiting for you."
    elif the_person.love > 35:
        the_person "You crave a glimpse of my most intimate treasure, [the_person.mc_title]? I must say, the prospect of sharing this with you is rather thrilling."
        if the_person.has_taboo("touching_vagina"):
            mc.name "I can't help myself. Your pussy is like a dangerous allure, and I'm the one who's going to succumb to its charm."
            the_person "Well, you've been warned. Alright, let's take off this [the_clothing.display_name] and unleash the temptation that's been building up."
        else:
            mc.name "I've already tasted it, I just want to see it too."
            the_person "That's very daring of you, [mc.name]. I'm glad you appreciate my beauty so much. Alright, let's get this [the_clothing.display_name] off."
    else:
        the_person "Hold up, you're trying to get me out of my [the_clothing.display_name] already? And without even asking nicely?"
        if the_person.has_taboo("touching_vagina"):
            mc.name "I'm sorry, [the_person.title], I just can't help myself. Your pussy is too tempting to resist."
            the_person "Well, you've been playing with fire, haven't you? Alright, let's take off this [the_clothing.display_name] and see where this leads us."
        else:
            mc.name "I'm sorry, [the_person.title], I just can't help myself. I've already touched your pussy, I just want to see it too."
            the_person "Oh, that's very sweet of you. Alright then, let's get this [the_clothing.display_name] off."
    return

# label yandere_facial_cum_taboo_break(the_person):

#     return

# label yandere_mouth_cum_taboo_break(the_person):

#     return

# label yandere_body_cum_taboo_break(the_person):

#     return
#========================================================================

label yandere_creampie_taboo_break(the_person):
    if the_person.wants_creampie:
        if the_person.knows_pregnant:
            the_person "Ah, yes, please shoot your hot load deep inside me, my precious."
            mc.name "I love how you say that, [the_person.possessive_title]."
            "She blushes and smiles, her eyes filled with excitement."

        elif the_person.on_birth_control:
            if the_person.has_significant_other:
                the_person "Oh, my dear [the_person.so_girl_title], you know I shouldn't be doing this, but I can't help myself."
                the_person "I want to feel you deep inside me, and I want to be yours completely."
                mc.name "You're so beautiful when you're naughty, [the_person.name]."
                "She giggles, her face flushed with pleasure."
            else:
                the_person "Oh, I've wanted this for so long! Please, I need to feel you inside me."
                the_person "I don't care about the consequences, I just want to be with you."
                mc.name "You're so adorable when you're like this, [the_person.name]."
                "She smiles, her eyes shining with desire."
            "She sighs happily."
            the_person "How long can you hold out before you need to be inside me again? I want to feel you fill me up completely."
        elif the_person.effective_sluttiness() > 75 or the_person.opinion.creampies > 0:
            if the_person.has_significant_other:
                the_person "Oh, fuck... I'm such a terrible [the_person.so_girl_title]!"
                mc.name "But you're my terrible [the_person.so_girl_title], and I love how possessive you are."
                the_person "My precious, you're so sweet to say that."
            else:
                the_person "Oh, fuck, I shouldn't be doing this!"
                mc.name "But you want to, and I want to, and that's all that matters."
                the_person "Yes, I want to be yours completely, my dear."
            "She sighs happily."
            the_person "How long can you hold out before you need to be inside me again? I want to feel you fill me up completely."
            mc.name "As long as you want me to, my love."
            the_person "Good, because I don't ever want you to leave me."
        else:
            if the_person.has_significant_other:
                the_person "Oh, fuck... I'm such a terrible [the_person.so_girl_title]!"
                mc.name "But you're my terrible [the_person.so_girl_title], and I love how much you need me."
                the_person "My precious, you're all I need."
            else:
                the_person "Oh, fuck, I shouldn't be doing this!"
                mc.name "But you want to, and I want to, and that's all that matters."
                the_person "Yes, I want to be yours, my dear."

            the_person "I'll just have to hope you haven't knocked me up. We really shouldn't do this again, my luck is going to run out at some point."
        the_person "Just promise me you won't ever leave me, and we'll forget about the consequences, okay?"
        mc.name "I promise, [the_person.name]. I'll never leave you."
        "She smiles, her heart filled with love and desire."
    else:
        if the_person.knows_pregnant:
            the_person "Oh, my dear, you've made me come so hard I might just collapse."
            mc.name "That's because you're carrying my precious seed."
            the_person "Mmm, I love the thought of being filled with your essence."
        elif not the_person.on_birth_control:
            the_person "Oh, my sweet, you've given me your gift. Are you ready to face the consequences?"
            mc.name "Together, we'll face whatever comes our way."
            the_person "I want you to be mine, completely and irrevocably."

            if the_person.has_significant_other:
                the_person "We'll make them regret ever trying to come between us."
            else:
                the_person "We'll make our own rules and live by them."

        elif the_person.has_significant_other:
            the_person "Did you just make me feel so alive, my love? I might just take you away from them."
            mc.name "You wouldn't dare, my dangerous angel."
            the_person "Wouldn't I? You're mine now, and I won't let anyone take that away."

        elif the_person.opinion.creampies < 0:
            the_person "Oh, my dear, you know I hate this feeling. But it's because I'm so addicted to your touch."
            mc.name "I'll make it up to you, my sweet. Just give me the chance."
            the_person "I'm counting on it, my precious. And if you don't, I might just have to take matters into my own hands."
        else:
            the_person "Oh, my dear, why did you stop? I wanted to feel you fill me up completely and make me yours."
            mc.name "I'll make it up to you, my love. Just be patient."
            the_person "I'll try, but I can't promise I won't take matters into my own hands if you don't deliver."
    return

label yandere_anal_creampie_taboo_break(the_person):
    if the_person.opinion.anal_creampies > 0:
        if the_person.effective_sluttiness() > 75 or the_person.opinion.anal_creampies > 1:
            if the_person.has_significant_other:
                the_person "Darling [the_person.mc_title], you're being so impulsive, but I can't help but love this taboo thrill! My [the_person.so_title] would never dare to shoot his cum in my ass, but you, on the other hand, are free to fill me up anytime you desire!"
            else:
                the_person "Ah, finally! You should have put a load inside my ass sooner! Now, I'll be drenched in your delicious cum all day long!"
            "She giggles uncontrollably, her eyes shining with a mischievous glint."
            the_person "Yes, yes, yes! I'll be dripping with your cum all day long! It's so wicked, so taboo, and yet... so incredibly delicious!"
        else:
            if the_person.has_significant_other:
                the_person "Oh, [the_person.mc_title], I should've told you to pull out, but I simply can't resist this sensation... My [the_person.so_title] never ventures into such forbidden territory, but you, my love, are free to indulge my darkest desires!"
            else:
                the_person "Promise me, [the_person.mc_title], that you'll fill me up every time... It's wrong, it's twisted, but oh, how it makes my heart race! All that cum in my tight little ass..."
    else:
        if the_person.has_significant_other:
            the_person "Fuck [the_person.mc_title], I told you to pull out! My [the_person.so_title] will see your cum leaking out of my ass, and we both know that's not allowed..."
        elif the_person.opinion.anal_creampies < -1:
            the_person "Fuck [the_person.mc_title], I said to pull out! I'll be dripping cum out of my ass all day long, and that's just not acceptable."
        else:
            the_person "Fuck [the_person.mc_title], not inside! My ass is not a sperm bank, although that does sound quite tempting in a twisted sort of way."
    return

label yandere_dual_penetration_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 75:
        the_person "Oh, my sweet darling, you're going to split me in two with that colossal cock and that monstrous toy! I'm trembling with anticipation!"
        "She seems more excited by the thought than concerned."
        mc.name "Don't worry, my dear, I'll make sure you're properly stretched out for this experience."
    elif the_person.love >= 60:
        the_person "You're really going to attempt this? I'm not sure if I can even fit both your massive cock and that gigantic toy in my ass... but I want it so badly!"
        mc.name "Trust me, I'll make it work. And don't worry, I'll be gentle... until you beg for more, that is."
        the_person "Fuck, just try not to break me into pieces!"
    else:
        if the_person.has_taboo("vaginal_sex"):
            the_person "Are you sure my pussy isn't enough for you, considering you're going to stuff that enormous toy in my ass too? You're a very naughty boy..."
            mc.name "I'll manage, but you might feel a little sore afterwards."
            the_person "Oh, fuck... I love it!"
        else:
            "She takes a deep breath and speaks in a sultry tone."
            the_person "Whew, okay, [the_person.fname], let's get wild and dirty... before I lose my mind."
            mc.name "Are you ready to unleash your inner slut?"
            the_person "Yes, let's just get it over with. I don't know what's gotten into me today... but I'm loving every moment of it."
            "She laughs seductively and looks at you with a mischievous grin."
            the_person "Well, maybe I do... You, of course."
            mc.name "That's what I'm counting on."
            the_person "Okay, then, let's get this over with before I change my mind... again!"
    return

label yandere_sleepover_yourplace_response(the_person): #Invited her over to spend the night
    if the_person.sluttiness < 80:
        the_person "Oh, darling! I'd be absolutely thrilled to spend the night in your embrace! I've been yearning for your touch, your kisses, and your passionate embrace for far too long! The thought of being in your bed, in your arms, sends shivers down my spine!"
        "Her eyes sparkle with excitement, and she bites her lower lip seductively."
    else:
        the_person "Oh, god, yes! I can't wait to be completely at your mercy, to feel you ravage me with your passion! Make sure you're ready to unleash your wildest fantasies, because I'm going to push you to your limits and beyond! I want to feel your hands on me, your lips on my skin, and your body buried deep within mine!"
        "She leans in closer, her voice dropping to a sultry whisper."
        the_person "I've been dreaming of this moment for so long, and now that it's here, I can hardly contain my excitement. I want to feel you trembling with desire, to hear you moan my name as you lose control. Are you ready to give me what I want, darling?"
    return


label yandere_sleepover_herplace_response(the_person): #Spending the night at her place
    if the_person.sluttiness < 80:
        the_person "Oh, darling! Spending the night at my place would be absolute heaven! I'll make sure to pamper you and make you feel like the king of the world. You can sleep in my bed, and I'll keep you warm throughout the night with my body."
    else:
        the_person "Oh, god, yes! You can ravage me all night long, and I don't care who hears us! The neighbors can join in if they want to, for all I care! I want to feel you deep inside me, pumping away like there's no tomorrow!"
        "She leans in closer, her voice dropping to a sultry whisper."
        the_person "I've been waiting for this moment for so long, and now that it's here, I can't help but feel like I'm going to explode with pleasure. So come on, darling, give me what I want, and let's make this night one we'll never forget!"
    return

label yandere_sleepover_yourplace_sex_start(the_person): #Right before sexy times at your place
    "[the_person.title] seductively glides towards you, her eyes fixed intently on yours. Her lips curl into a sly smile as she speaks in a husky whisper."
    the_person "Oh, darling, I've been waiting for this moment all night. Are you ready to unleash your wildest desires and make me scream with pleasure? I'm more than ready to reciprocate."
    "She leans in closer, her breath caressing your ear as she adds, her voice dripping with seduction."
    the_person "And don't worry, I won't hold back. I want to feel you trembling with lust, to hear you beg for more. Let's make this night one to remember, shall we?"
    return

label yandere_sleepover_herplace_sex_start(the_person): #Right before sexy times at her place
    the_person "Well, well, well... Look who finally decided to join me. Are you going to stand there and stare all night, or are you going to make me scream with pleasure?"
    "She winks at you, her lips curling into a wicked grin."
    mc.name "Are you ready for this?"
    the_person "Ready? I've been ready since the moment you walked through the door! I've been dreaming of this moment for days, maybe even weeks... I need you, darling. I need you inside me, hard and fast!"
    "She grabs your hand and pulls you towards her, her eyes burning with desire."
    the_person "Come on, don't make me wait any longer. I want to feel you deep within me, to hear you moan my name as I ride you like a wild animal!"
    return

label yandere_sleepover_impressed_response(the_person):  #If you've made her cum a lot
    the_person "Oh, my god, you're an absolute machine! I don't think my body can take much more of this... but I'm not sure I want it to stop! You're incredible, darling!"
    "She gasps for breath, her eyes still closed in ecstasy."
    $ the_person.draw_person(position = "missionary")
    the_person "I want to feel you inside me again, to lose myself in the pleasure you bring me. Make me cum once more, and then maybe we can take a break... or maybe not."
    "She opens her eyes, a mischievous grin spreading across her face."
    the_person "I'm not sure I'm ready to face the morning after this kind of orgasmic overload, but I'm willing to give it a shot... as long as you're by my side."
    return

label yandere_sleepover_good_response(the_person):  #If you've made her cum
    the_person "Oh, my god, that was incredible! I never thought I'd experience pleasure like that again... or ever! You're a magician, darling!"
    "She gasps for breath, her eyes still closed in ecstasy."
    $ the_person.draw_person(position = "missionary")
    the_person "I want more, I need more! Please, darling, make me cum again. I don't care if we have to go to sleep on the floor, as long as we're together."
    "She opens her eyes, her gaze burning with desire."
    the_person "You've awakened a hunger within me, a hunger that only you can satiate. Give me what I crave, and let's see how many times we can make each other scream with pleasure tonight!"
    return

label yandere_sleepover_bored_response(the_person):  #If she hasn't cum yet
    the_person "Oh, come on, darling! I've had more satisfying orgasms in my dreams! Don't tell me you're not capable of making me scream with pleasure!"
    "She rolls her eyes and sits up, her expression mocking."
    the_person "I guess I'll have to take matters into my own hands. You're not doing it right."
    "She starts to play with her clit, her eyes never leaving yours."
    the_person "You should be ashamed of yourself, unable to satisfy a woman like me. I need a real man to make me cum, not some pathetic excuse for a lover."
    "She continues to rub herself, her gaze challenging you to prove your worth."
    the_person "So, are you up for the challenge, or should I just go find someone else who can make me feel something?"
    return

