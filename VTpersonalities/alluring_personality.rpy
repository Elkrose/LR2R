### PERSONALITY CHARACTERISTICS ###
# add more alluring personality, use different words, and movements.
# update all the following the_person and movements with alluring personality. Use Miss Fortune and Samira from League of Legends for ideas, keep to the structure. Movements in quotations:
### DIALOGUE ###
label alluring_introduction(the_person):
    mc.name "Well, well, well. Looks like I just stumbled upon a vision of loveliness. Care to make my day and tell me your name?"
    "She raises an eyebrow, a sly smile spreading across her face as she turns to face you, her hips swaying slightly in the process."
    the_person "Oh, I think I can spare a minute for a charming stranger such as yourself. But don't get too excited, I'm not that easy to impress."
    mc.name "I wouldn't dream of it. I just had to take a chance and see if the spark I felt when I saw you was real."
    "She chuckles, the sound husky and confident, and takes a step closer to you, her eyes locked on yours."
    $ the_person.set_title()
    $ the_person.set_possessive_title()
    the_person "I'm [the_person.title], and you are...?"
    "She trails off, her voice dripping with anticipation, as she waits for your response."
    return

label alluring_greetings(the_person):
    if the_person.love < 0:
        "She looks up at you, a hint of annoyance in her eyes, but still a sly smile on her lips."
        the_person "Well, well, well. Look what the wind blew in. What do you want this time, hmm?"
    elif the_person.happiness < 90:
        "She sighs, her shoulders rolling in a languid motion as she gazes up at you with a hint of mischief."
        the_person "Mmm, I'm having a bit of a rough day, darling. But I'm sure you're here to make it all better, aren't you?"
    else:
        if the_person.sluttiness > 60:
            if the_person.obedience > 180:
                "She basks a sultry smile on you, her voice dripping with seduction as she takes a step closer."
                the_person "Ah, [the_person.mc_title], it's so lovely to see you. I've been waiting for someone to... attend to my needs."
            else:
                "She flashes a flirtatious grin, her eyes sparkling with amusement as she leans in, her voice husky."
                the_person "Mmm, [the_person.mc_title], I hope you're here to play. I'm feeling particularly... restless today."
        else:
            if the_person.obedience > 180:
                "She offers a demure smile, her eyes cast downward in a playful gesture of submission."
                the_person "Hello, [the_person.mc_title]. It's lovely to see you, as always."
            else:
                "She raises an eyebrow, a sly smile spreading across her face as she gazes up at you with a hint of challenge."
                the_person "Hey, handsome. What brings you to my neck of the woods?"
    return

label alluring_sex_responses_foreplay(the_person):
    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] arches her back, a sultry moan escaping her lips as she presses herself against you, her eyes locked on yours with a hungry gleam."
            the_person "Mmm, you're so good at this... Don't stop, darling."
        else:
            "[the_person.possessive_title!c] lets out a soft, throaty moan, her head tilting back in pleasure as she melts into your touch, her voice barely above a whisper."
            the_person "Oh, that feels... amazing. You're really good at this, aren't you?"

    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] writhes beneath your touch, her hips bucking in anticipation as she gazes up at you with a fierce, sultry intensity."
            the_person "Oh, fuck... I adore the way you touch me. It's like you know exactly what I need."
        else:
            "[the_person.possessive_title!c] shudders, her breath catching in her throat as she clings to you, her voice trembling with desire."
            the_person "Oh... Oh, god. That feels... incredible."

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] spreads her legs wider, inviting you to explore her further as she gazes up at you with a brazen, seductive smile."
            the_person "Mmm, it feels so fucking good when you touch me like that. Don't stop, I'm just getting started."
        else:
            "[the_person.possessive_title!c] wraps her arms around you, pulling you closer as she nuzzles your neck, her voice husky with desire."
            the_person "Keep going, [the_person.mc_title]. I'm all yours, darling."

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] arches her back, her body trembling with anticipation as she gazes up at you with a wild, sultry abandon."
            the_person "Mmm, touch me all over. I'm your dirty little secret, and I'll do anything you want."
        else:
            "[the_person.possessive_title!c] clings to you, her voice barely above a whisper as she trembles with desire."
            the_person "Touch me, [the_person.mc_title]. I'm yours, all yours."

    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                "[the_person.possessive_title!c] bucks beneath your touch, her body trembling with anticipation as she gazes up at you with a fierce, sultry intensity."
                the_person "Oh, fuck... I'm going to cum soon. I can feel it building, and I know it's going to be amazing."
            else:
                "[the_person.possessive_title!c] shudders, her breath catching in her throat as she clings to you, her voice trembling with desire."
                the_person "The way you touch me is... different. It's like you know exactly what I need, and I crave it."
        else:
            "[the_person.possessive_title!c] wraps her arms around you, pulling you closer as she nuzzles your neck, her voice husky with desire."
            the_person "Don't stop, [the_person.mc_title]. I'm so close... I can feel it building, and I know it's going to be incredible."
    return

label alluring_sex_responses_oral(the_person):
    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] spreads her legs wider, a sultry smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
            the_person "Mmm, darling... Go down on me, and show me what you're working with."
        else:
            "[the_person.possessive_title!c] shudders, her breath catching in her throat as she clings to you, her voice trembling with desire."
            the_person "Oh, god... You're really going to... Oh, yes, please..."

    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] wraps her legs around your head, pulling you closer as she gazes up at you with a fierce, sultry abandon."
            the_person "Mmm, I adore a good tongue-lashing. You're so good at this, darling."
        else:
            "[the_person.possessive_title!c] arches her back, her body trembling with anticipation as she gazes up at you with a wild, sultry intensity."
            the_person "Fuck, that feels... incredible. Don't stop, darling."

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] bucks beneath your touch, her hips writhing in pleasure as she gazes up at you with a brazen, seductive smile."
            the_person "Eat me out, [the_person.mc_title]. Your tongue is absolute magic."
        else:
            "[the_person.possessive_title!c] shudders, her breath catching in her throat as she clings to you, her voice trembling with desire."
            the_person "That feels... so good. You have no idea what you're doing to me."

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] spreads her legs wider, a sultry smile spreading across her face as she gazes up at you with a fierce, sultry intensity."
            the_person "Mmm, lick that pussy! Ah, yes... just like that."
        else:
            "[the_person.possessive_title!c] arches her back, her body trembling with anticipation as she gazes up at you with a wild, sultry abandon."
            the_person "Oh, god... yes! Yes, darling, just like that."

    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                "[the_person.possessive_title!c] bucks beneath your touch, her hips writhing in pleasure as she gazes up at you with a brazen, seductive smile."
                the_person "Fuck, fuck, fuck... that's it right there, darling. Make me cum."
            else:
                "[the_person.possessive_title!c] shudders, her breath catching in her throat as she clings to you, her voice trembling with desire."
                the_person "My [the_person.so_title] never eats me out like this, [the_person.mc_title]. You're so much better than they are."
                the_person "Make me cum my brains out, and I'll forget all about them, darling."
        else:
            "[the_person.possessive_title!c] wraps her legs around your head, pulling you closer as she gazes up at you with a fierce, sultry abandon."
            the_person "Don't stop, darling! You're going to make me cum, and I don't want it to end."
    return

label alluring_sex_responses_vaginal(the_person):
    if the_person.energy < 10:
        call low_energy_sex_responses_vaginal(the_person) from alluring_call_low_energy_sex_responses_vaginal_10
        return

    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            $ play_moan_sound()
            "[the_person.possessive_title!c] arches her back, a sultry moan escaping her lips as she wraps her legs around you, pulling you deeper."
            the_person "Mmm, how does my pussy feel, darling? I hope I'm tight enough for you... for now."
        else:
            "[the_person.possessive_title!c] bites her lip, a soft, throaty moan escaping her as she gazes up at you with a hungry, sultry intensity."
            the_person "Oh... god, that feels... so good."

    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] writhes beneath you, her hips bucking in pleasure as she gazes up at you with a brazen, seductive smile."
            the_person "Oh, fuck... I never get tired of feeling you inside me, darling. You're so good at this."
        else:
            "[the_person.possessive_title!c] shudders, her breath catching in her throat as she clings to you, her voice trembling with desire."
            the_person "Oh... oh, fuck me... your cock feels... incredible."

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] spreads her legs wider, a sultry smile spreading across her face as she gazes up at you with a fierce, sultry intensity."
            the_person "Mmm, you feel so good fucking my pussy, darling. Don't stop, I'm just getting started."
        else:
            "[the_person.possessive_title!c] arches her back, her body trembling with anticipation as she gazes up at you with a wild, sultry abandon."
            the_person "Ah, fuck me... just like that, darling. Yes, yes, yes..."

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] bucks beneath you, her hips writhing in pleasure as she gazes up at you with a brazen, seductive smile."
            the_person "That's right, use me like your dirty little slut and fuck my pussy hard, darling. I love it when you take control."
        else:
            "[the_person.possessive_title!c] shudders, her breath catching in her throat as she clings to you, her voice trembling with desire."
            the_person "Oh, fuck yes... fuck yes, darling. I'm so close..."

    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                "[the_person.possessive_title!c] arches her back, a sultry moan escaping her lips as she wraps her legs around you, pulling you deeper."
                the_person "Fuck! I'm... your cock is going to make me cum, darling! I want you to make me cum, now!"
            else:
                "[the_person.possessive_title!c] shudders, her breath catching in her throat as she clings to you, her voice trembling with desire."
                the_person "Your cock is stretching me out, my [the_person.so_title] is never going to be enough for me after this, darling."
                the_person "Oh well, fuck him! Keep going and make me cum, I don't care about anything else."
        else:
            "[the_person.possessive_title!c] wraps her legs around you, pulling you deeper as she gazes up at you with a fierce, sultry intensity."
            the_person "Don't stop fucking me, darling! You're going to make me cum, I can feel it building... yes, yes, yes..."
    return

### DIALOGUE ###
label alluring_sex_responses_anal(the_person):
    if the_person.energy < 10:
        call low_energy_sex_responses_anal(the_person) from alluring_call_low_energy_sex_responses_anal_10
        return

    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] gazes up at you with a sultry, pleading expression, her voice barely above a whisper."
            the_person "Just go slowly, darling... I want to feel every inch of you inside me."
            "She seems to be savoring the moment, her eyes locked on yours with a hungry intensity."
        else:
            $ the_person.call_dialogue("surprised_exclaim")
            "[the_person.possessive_title!c] takes a deep breath, her chest heaving as she tries to compose herself, her voice trembling with desire."
            the_person "Deep breaths, [the_person.title]... deep breaths... I can do this."
            "She pants to herself, her eyes fixed on yours as she struggles to maintain control."

    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            $ the_person.call_dialogue("surprised_exclaim")
            "[the_person.possessive_title!c] arches her back, a sultry moan escaping her lips as she wraps her legs around you, pulling you deeper."
            the_person "Mmm, I love being stretched out like this, darling... it's so... liberating."
        else:
            "[the_person.possessive_title!c] shudders, her breath catching in her throat as she clings to you, her voice barely above a whisper."
            the_person "Oh... oh, fuck my ass, darling... yes, yes, yes..."

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] bucks beneath you, her hips writhing in pleasure as she gazes up at you with a brazen, seductive smile."
            the_person "Gah! Ah! Fuck, darling... you're so good at this!"
        else:
            "[the_person.possessive_title!c] bites her lip, a soft, throaty moan escaping her as she gazes up at you with a hungry, sultry intensity."
            the_person "God, I won't be able to sit for a week after this, darling... but it's so worth it."

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            if mc.condom:
                "[the_person.possessive_title!c] wraps her legs around you, pulling you deeper as she gazes up at you with a fierce, sultry intensity."
                the_person "Give it to me, darling... punish that slutty ass with your big cock!"
            else:
                "[the_person.possessive_title!c] arches her back, a sultry moan escaping her lips as she wraps her legs around you, pulling you deeper."
                the_person "Give it to me, darling... fuck my horny asshole raw!"
        else:
            "[the_person.possessive_title!c] shudders, her breath catching in her throat as she clings to you, her voice barely above a whisper."
            the_person "Ah! Why does your cock have to be so fucking big, darling?!"

    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                "[the_person.possessive_title!c] arches her back, a sultry moan escaping her lips as she wraps her legs around you, pulling you deeper."
                the_person "Fuck, darling... I think I'm going to cum from your cock up my ass!"
            else:
                "[the_person.possessive_title!c] shudders, her breath catching in her throat as she clings to you, her voice trembling with desire."
                the_person "Wreck my ass, [the_person.mc_title]... send me back to my [the_person.so_title] gaping and ruined! Ah, yes..."
                the_person "I might have a [the_person.so_title], but he doesn't drive me crazy like you do, darling... Make me cum my brains out!"
                the_person "Screw my [the_person.so_title], he's not half the man you are, darling... you're the only one I need."
        else:
            $ the_person.call_dialogue("surprised_exclaim")
            "[the_person.possessive_title!c] gazes up at you with a sultry, pleading expression, her voice barely above a whisper."
            the_person "I think I'm going to cum soon, darling... please, don't stop... I need this."
    return

label alluring_climax_responses_foreplay(the_person):
    if the_person.sluttiness > 50:
        "[the_person.possessive_title!c] arches her back, a sultry moan escaping her lips as she gazes up at you with a brazen, seductive smile."
        the_person "Oh, darling... yes... I'm going to cum! I can feel it building, and I know it's going to be amazing!"
        "She trembles with anticipation, her body tense and ready to release."
    else:
        $ the_person.call_dialogue("surprised_exclaim")
        "[the_person.possessive_title!c] bites her lip, a soft, throaty moan escaping her as she gazes up at you with a hungry, sultry intensity."
        the_person "You're going to make me cum, darling... I can feel it... oh, god..."
        "She goes silent, her body trembling with anticipation, and then lets out a shuddering moan as she reaches her climax."
    return

label alluring_climax_responses_oral(the_person):
    if the_person.sluttiness > 70:
        "[the_person.possessive_title!c] wraps her legs around your head, pulling you closer as she gazes up at you with a fierce, sultry intensity."
        the_person "Mmm, darling... yes... I'm going to cum! Make me cum, and don't stop until I'm screaming your name!"
        "She trembles with anticipation, her body tense and ready to release."
    else:
        "[the_person.possessive_title!c] arches her back, a sultry moan escaping her lips as she gazes up at you with a brazen, seductive smile."
        the_person "Oh, god... you're so good at that, darling... I'm going to... I'm going to cum, and it's all because of you..."
        "She shudders, her breath catching in her throat as she clings to you, her voice barely above a whisper."
    return

label alluring_climax_responses_vaginal(the_person):
    if the_person.sluttiness > 70:
        if the_person.arousal_perc > 120:
            "[the_person.possessive_title!c] wraps her legs around you, pulling you deeper as she gazes up at you with a fierce, sultry intensity."
            the_person "Mmm, yes... keep going, darling. Make your little slut cum, and don't stop until I'm screaming your name!"
            "She closes her eyes, her body trembling with anticipation, and lets out a sultry squeal of pleasure."
        else:
            "[the_person.possessive_title!c] arches her back, a sultry moan escaping her lips as she gazes up at you with a brazen, seductive smile."
            the_person "Ah, darling... more! I'm going to... Ah! Cum! Oh, fuck, yes!"
            "She shudders, her breath catching in her throat as she clings to you, her voice barely above a whisper."
    else:
        "[the_person.possessive_title!c] bites her lip, a soft, throaty moan escaping her as she gazes up at you with a hungry, sultry intensity."
        the_person "Oh, god... I'm going to... Oh, fuck me, darling! Ah, yes!"
        "She trembles with anticipation, her body tense and ready to release, as she whispers your name."
    return

label alluring_climax_responses_anal(the_person):
    if the_person.sluttiness > 70:
        if the_person.arousal_perc > 120:
            "[the_person.possessive_title!c] arches her back, a sultry moan escaping her lips as she gazes up at you with a brazen, seductive smile."
            the_person "Mmm, yes... shove your big cock into my slutty ass, darling. Make your little bitch cum, and don't stop until I'm screaming your name!"
            "She trembles with anticipation, her body tense and ready to release, as she whispers your name."
            the_person "Ah! Mmhmmm, darling... yes!"
        else:
            "[the_person.possessive_title!c] wraps her legs around you, pulling you deeper as she gazes up at you with a fierce, sultry intensity."
            the_person "Oh, fuck... your cock feels so huge in my ass, darling! It's going to make me cum, and I know it's going to be amazing!"
            "She shudders, her breath catching in her throat as she clings to you, her voice barely above a whisper."
            the_person "Ah! Mmhmmm, yes... darling!"
    else:
        "[the_person.possessive_title!c] bites her lip, a soft, throaty moan escaping her as she gazes up at you with a hungry, sultry intensity."
        the_person "Oh, fucking shit, darling... I think you're going to make me..."
        "She barely finishes her sentence before her body is racked with pleasure, her eyes rolling back in her head as she screams your name."
        the_person "Cum, darling... yes! Oh, god, yes!"
    return

label alluring_clothing_accept(the_person):
    if the_person.obedience > 180:
        "[the_person.possessive_title!c] gazes up at you with a sultry, submissive expression, her voice barely above a whisper."
        the_person "Mmm, you think it will look good on me, darling? I guess that's all I need to hear, then. I trust your taste completely."
        "She smiles, a seductive smile spreading across her face as she takes the clothing from you."
    else:
        "[the_person.possessive_title!c] raises an eyebrow, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
        the_person "Hey, thanks, darling. That's a good look, I like it. You have a great eye for fashion... and for me, it seems."
        "She winks, a flirtatious glint in her eye as she takes the clothing from you, her fingers brushing against yours."
    return

label alluring_clothing_reject(the_person):
    if the_person.should_wear_uniform:
        "[the_person.possessive_title!c] gazes up at you with a sultry, apologetic expression, her voice barely above a whisper."
        the_person "Mmm, darling... I guess I should get my uniform sorted out, right? One second, I'll just go change."
        "She smiles, a seductive smile spreading across her face as she turns to leave, her hips swaying slightly as she walks away."
    elif the_person.obedience > 180:
        "[the_person.possessive_title!c] looks down, a blush rising to her cheeks as she gazes up at you with a submissive, embarrassed expression."
        the_person "I don't... I'm sorry, darling... but I really don't think I could get away with wearing something like this. I appreciate the thought, though... you're always so thoughtful."
        "She smiles, a shy smile spreading across her face as she looks down, her voice barely above a whisper."
    else:
        if the_person.sluttiness > 60:
            "[the_person.possessive_title!c] raises an eyebrow, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
            the_person "Mmm, darling... you didn't leave much to the imagination, did you? I don't think I can wear this... at least, not in public."
            "She winks, a flirtatious glint in her eye as she holds up the outfit, her fingers brushing against the fabric."
        else:
            "[the_person.possessive_title!c] looks at the outfit, a mixture of surprise and amusement on her face as she gazes up at you with a teasing expression."
            the_person "There's not much of an outfit to this outfit, darling... thanks for the thought, but there's no way I could wear this. At least, not without getting into trouble."
            "She laughs, a throaty laugh escaping her lips as she shakes her head, her hair bouncing with the motion."
    return

label alluring_clothing_review(the_person):
    if the_person.outfit.cum_covered:
        if (the_person.sluttiness > 40 and the_person.opinion.being_covered_in_cum >=0) or the_person.opinion.being_covered_in_cum > 0:
            "[the_person.possessive_title!c] gazes up at you with a sultry, mischievous expression, her voice barely above a whisper."
            the_person "Mmm, darling... I guess I can't walk around covered in cum all day... although it does make for a nice accessory, don't you think?"
            "[the_person.title] starts to wipe up the biggest splashes of cum on her, her fingers brushing against her skin with a sensual touch."
        else:
            "[the_person.possessive_title!c] looks down, a blush rising to her cheeks as she gazes up at you with a embarrassed expression."
            the_person "Oh, fuck... I need to clean up all of this cum, darling! Let me know if I've missed any, okay?"
            "[the_person.title] wipes herself down, cleaning up all the cum she can find, her movements quick and efficient."

    if the_person.obedience > 180:
        "[the_person.possessive_title!c] gazes up at you with a sultry, submissive expression, her voice barely above a whisper."
        the_person "Oh, man... I'm a mess, darling. I'll be back in a moment, I'm just going to get cleaned up for you. I want to look my best for you, always."
        "She smiles, a shy smile spreading across her face as she turns to leave, her hips swaying slightly as she walks away."
    else:
        if the_person.sluttiness > 40:
            "[the_person.possessive_title!c] raises an eyebrow, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
            the_person "Mmm, darling... I don't think everyone else would appreciate me going around dressed like this as much as you would. I'll be back in a second, I just want to get cleaned up... and maybe change into something a little more... revealing."
            "She winks, a flirtatious glint in her eye as she turns to leave, her hips swaying slightly as she walks away."
        else:
            "[the_person.possessive_title!c] looks at herself, a mixture of surprise and amusement on her face as she gazes up at you with a teasing expression."
            the_person "Damn, everything's out of place after that, darling. Wait here a moment, I'm just going to find a mirror and try and look presentable... or at least, as presentable as I can after what we just did."
            "She laughs, a throaty laugh escaping her lips as she turns to leave, her hair bouncing with the motion."
    $ the_person.apply_planned_outfit(show_dress_sequence = True)
    return

label alluring_strip_reject(the_person, the_clothing, strip_type = "Full"):
    if the_person.obedience > 180:
        "[the_person.possessive_title!c] gazes up at you with a sultry, submissive expression, her voice barely above a whisper."
        the_person "Mmm, darling... could we leave my [the_clothing.display_name] on for now, please? I want to savor the moment a little longer."
        "She smiles, a shy smile spreading across her face as she looks down, her eyes cast downward in a playful gesture of submission."
    elif the_person.obedience < 70:
        "[the_person.possessive_title!c] raises an eyebrow, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
        the_person "No, no, no, darling... I'll decide what comes off and when, okay? You'll just have to wait and see."
        "She winks, a flirtatious glint in her eye as she crosses her arms, her body language playful and teasing."
    else:
        "[the_person.possessive_title!c] bites her lip, a soft, throaty moan escaping her as she gazes up at you with a hungry, sultry intensity."
        the_person "Not yet, darling... get me a little warmed up first, okay? Then maybe you can take off my [the_clothing.display_name]... and see what's underneath."
        "She smiles, a seductive smile spreading across her face as she takes a step closer to you, her body swaying slightly as she moves."
    return

label alluring_strip_obedience_accept(the_person, the_clothing, strip_type = "Full"):
    "[the_person.possessive_title!c] laughs nervously, a sultry, husky sound escaping her lips as you start to slide her [the_clothing.display_name] away, her eyes locked on yours with a hungry, sultry intensity."
    if the_person.obedience > 180:
        "[the_person.possessive_title!c] gazes up at you with a sultry, submissive expression, her voice barely above a whisper."
        the_person "Mmm, darling... I don't know if that's a good idea. Could we just leave it... for now?"
        "She smiles, a shy smile spreading across her face as she looks down, her eyes cast downward in a playful gesture of submission."
    else:
        "[the_person.possessive_title!c] raises an eyebrow, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
        the_person "Hey, darling... let's not take this too far... yet. I want to savor the moment a little longer."
        "She winks, a flirtatious glint in her eye as she leans in closer to you, her body swaying slightly as she moves."
    return

label alluring_grope_body_reject(the_person):
    if the_person.effective_sluttiness("touching_body") < 5: #Fail point for touching shoulder
        "[the_person.possessive_title!c] lets out a soft, throaty gasp as you touch her, her eyes widening in surprise."
        the_person "Ah, darling...!"
        "[the_person.title] steps back, a sultry smile spreading across her face as she laughs awkwardly, her hand rising to her chest."
        the_person "Haha, sorry... Your hand just kind of came out of nowhere, and I wasn't expecting it."
        mc.name "Sorry, I didn't mean to startle you, darling."
        the_person "Don't worry about it, just give me a little warning next time, okay? I want to be ready for your touch."
        "She seems a little uncomfortable, but you both laugh about it and try to move on, the tension between you still palpable."
    else: #Fail point for touching waist
        "[the_person.possessive_title!c] raises an eyebrow, a sly smile spreading across her face as she takes your hand and pulls it off of her waist."
        the_person "Hey, darling... could you just... keep your hands to yourself? For now, at least?"
        mc.name "Oh yeah, of course. My bad, darling."
        the_person "No problem, just don't make a habit of it... yet. Alright?"
        "She doesn't say anything else, but she still seems uncomfortable with the situation, her eyes locked on yours with a hungry, sultry intensity."
    return

label alluring_sex_accept(the_person, the_position):
    if the_person.sluttiness > 70:
        if the_person.obedience < 70:
            "[the_person.possessive_title!c] gazes up at you with a sultry, mischievous expression, her voice barely above a whisper."
            the_person "Mmm, darling... let's do it. Once you've had your fill, I have a few ideas we could try out... and I think you'll love them."
            "She smiles, a sly smile spreading across her face as she takes a step closer to you, her body swaying slightly as she moves."
        else:
            if the_position.skill_tag == "Foreplay":
                "[the_person.possessive_title!c] bites her lip, a soft, throaty moan escaping her as she gazes up at you with a hungry, sultry intensity."
                the_person "I was hoping you would suggest that, darling... just thinking about it gets me excited. I love the way you touch me."
                "She shudders, her breath catching in her throat as she clings to you, her voice barely above a whisper."
            elif the_position.skill_tag == "Oral":
                if "getting head" in the_position.opinion_tags:
                    "[the_person.possessive_title!c] raises an eyebrow, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
                    the_person "Oh, [the_person.mc_title]... get down there and make me cum my brains out, darling. I need it so badly."
                    "She winks, a flirtatious glint in her eye as she pushes you down, her hands guiding your head to her pussy."
                else:
                    "[the_person.possessive_title!c] gazes up at you with a sultry, submissive expression, her voice barely above a whisper."
                    the_person "Come here, darling... I need to suck on that lovely dick right now. I want to taste you so badly."
                    "She smiles, a shy smile spreading across her face as she takes your cock in her mouth, her lips wrapping around it with a sensual touch."
            else:
                "[the_person.possessive_title!c] arches her back, a sultry moan escaping her lips as she gazes up at you with a fierce, sultry intensity."
                the_person "Oh, yes... [the_person.mc_title], I need you to fuck me hard and deep, darling. I want to feel you inside me so badly."
                "She trembles with anticipation, her body tense and ready to release as she wraps her legs around you, pulling you deeper."
    else:
        "[the_person.possessive_title!c] gazes up at you with a sultry, inviting expression, her voice barely above a whisper."
        the_person "Come here, [the_person.mc_title]... let's do it, darling. I want to feel you inside me."
        "She smiles, a seductive smile spreading across her face as she takes a step closer to you, her body swaying slightly as she moves."
    return

label alluring_sex_obedience_accept(the_person):
    if the_person.sluttiness > 70:
        "[the_person.possessive_title!c] gazes up at you with a sultry, submissive expression, her voice barely above a whisper."
        the_person "Mmm, god... what have you done to me, darling? I should say no, but... I just want you to use me however you want, [the_person.mc_title]. I'm yours to command."
        "She shudders, her breath catching in her throat as she clings to you, her voice trembling with desire."
    else:
        if the_person.obedience > 180:
            "[the_person.possessive_title!c] looks down, a blush rising to her cheeks as she gazes up at you with a shy, submissive expression."
            the_person "If that's what you want to do, darling... then I will do what you tell me to do. I trust you completely."
            "She smiles, a soft, gentle smile spreading across her face as she nods, her eyes cast downward in a playful gesture of submission."
        else:
            "[the_person.possessive_title!c] raises an eyebrow, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
            the_person "I shouldn't, darling... but if you want to try it out, I'm game. Try everything once, right? And I have a feeling I'll love it with you."
            "She winks, a flirtatious glint in her eye as she leans in closer to you, her body swaying slightly as she moves."
    return

label alluring_sex_gentle_reject(the_person):
    if the_person.sluttiness > 50:
        "[the_person.possessive_title!c] gazes up at you with a sultry, teasing expression, her voice barely above a whisper."
        the_person "Mmm, not yet, darling... [the_person.mc_title], get me warmed up first. I want to be nice and hot for you."
        "She smiles, a sly smile spreading across her face as she takes a step closer to you, her body swaying slightly as she moves."
    else:
        "[the_person.possessive_title!c] looks up at you with a shy, hesitant expression, her voice barely above a whisper."
        the_person "Wait, darling... I just... I don't think I'm ready for this. I want to fool around, but let's keep it casual... for now, at least."
        "She bites her lip, a soft, gentle smile spreading across her face as she gazes up at you with a hungry, sultry intensity."
    return

label alluring_sex_angry_reject(the_person):
    if the_person.has_significant_other:
        "[the_person.possessive_title!c] raises an eyebrow, a fierce, sultry intensity burning in her eyes as she gazes up at you with a brazen, seductive expression."
        the_person "What, darling? I have a [the_person.so_title], so you can forget about doing anything like that. Ever. I'm taken, and I won't be swayed."
        "She glares at you, her eyes flashing with annoyance, before turning on her heel and walking away, her hips swaying slightly as she moves."
    elif the_person.sluttiness < 20:
        "[the_person.possessive_title!c] looks up at you with a shocked, offended expression, her voice rising in indignation."
        the_person "I'm sorry, what!? No, you've massively misread the situation, darling. Get the fuck away from me before I lose my temper!"
        "[the_person.title] glares at you, her eyes blazing with anger, before stepping back and crossing her arms, her body language radiating disdain."
    else:
        "[the_person.possessive_title!c] gazes up at you with a sultry, disgusted expression, her voice dripping with contempt."
        the_person "What, darling? That's fucking disgusting, I'm shocked you'd even suggest that to me. Do you really think I'm that kind of girl?"
        "[the_person.title] glares at you, her eyes flashing with annoyance, before stepping back and turning away, her hips swaying slightly as she moves."
    return

label alluring_seduction_response(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] gazes up at you with a sultry, submissive expression, her voice barely above a whisper."
            the_person "Mmm, oh, darling... I think I know what you need right now. Let me take care of you, and make you feel better."
            "She smiles, a shy smile spreading across her face as she takes a step closer to you, her body swaying slightly as she moves."
        else:
            "[the_person.possessive_title!c] looks down, a blush rising to her cheeks as she gazes up at you with a shy, hesitant expression."
            the_person "Right now, darling? Okay, lead the way, I guess. I trust you to know what's best for me."
            "She nods, a soft, gentle smile spreading across her face as she follows you, her eyes cast downward in a playful gesture of submission."
    else:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] raises an eyebrow, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
            the_person "Mmm, you're feeling as horny as me, then? Come on, darling... let's go and find some place to take care of that."
            "[the_person.title] takes your hand and leads you off to find some place out of the way, her hips swaying slightly as she moves."
        elif the_person.sluttiness > 10:
            "[the_person.possessive_title!c] gazes up at you with a sultry, teasing expression, her voice barely above a whisper."
            the_person "I know that look you're giving me, darling... I think I know what you want. And I'm happy to give it to you."
            "She smiles, a sly smile spreading across her face as she takes a step closer to you, her body swaying slightly as she moves."
        else:
            "[the_person.possessive_title!c] looks up at you with a shy, hesitant expression, her voice barely above a whisper."
            the_person "[mc.name], I know what you mean... Okay, darling, I can spare a few minutes. But just a few, I'm a busy girl."
            "She smiles, a soft, gentle smile spreading across her face as she nods, her eyes cast downward in a playful gesture of submission."
    return

label alluring_seduction_accept_crowded(the_person):
    if not the_person.has_significant_other:
        if the_person.sluttiness < 20:
            "[the_person.possessive_title!c] gazes up at you with a shy, hesitant expression, her voice barely above a whisper."
            the_person "Alright, darling... let's slip away for a few minutes and you can convince me a little more. I'm not sure I'm ready for this, but I'm willing to listen."
            "She smiles, a soft, gentle smile spreading across her face as she takes your hand, her eyes cast downward in a playful gesture of submission."
        elif the_person.sluttiness < 50:
            "[the_person.possessive_title!c] raises an eyebrow, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
            the_person "Come on, darling... I know someplace nearby where we can get a few minutes of privacy. And I think we're going to need it, don't you?"
            "She winks, a flirtatious glint in her eye as she takes your hand and leads you away, her hips swaying slightly as she moves."
        else:
            "[the_person.possessive_title!c] gazes up at you with a sultry, desperate expression, her voice barely above a whisper."
            the_person "Oh my god, darling... I hope you aren't planning on making me wait, [the_person.mc_title], because I don't know if I can! I need you so badly right now."
            "She trembles with anticipation, her body tense and ready to release as she clings to you, her eyes locked on yours with a hungry, sultry intensity."
    else:
        if the_person.sluttiness + (5*the_person.opinion.cheating_on_men) > 50:
            "[the_person.possessive_title!c] raises an eyebrow, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
            the_person "Fuck, darling... let's get this party started! I don't care about my [the_person.so_title] right now, all I care about is you and me, and what we're going to do together."
            "She laughs, a throaty, seductive sound escaping her lips as she takes your hand and leads you away, her hips swaying slightly as she moves."
        else:
            "[the_person.possessive_title!c] gazes up at you with a sultry, guilty expression, her voice barely above a whisper."
            the_person "God damn it, darling... you're bad for me, [the_person.mc_title]. Come on, we need to go somewhere quiet so my [the_person.so_title] doesn't find out about this. I don't want to get caught, but I need you so badly."
            "She bites her lip, a soft, gentle smile spreading across her face as she takes your hand, her eyes cast downward in a playful gesture of submission."
    return

label alluring_seduction_accept_alone(the_person):
    if not the_person.has_significant_other:
        if the_person.sluttiness < 20:
            "[the_person.possessive_title!c] gazes up at you with a shy, flirtatious expression, her voice barely above a whisper."
            the_person "Well, darling... I think you deserve a chance to impress me. Show me what you're working with."
            "She smiles, a soft, gentle smile spreading across her face as she takes a step closer to you, her body swaying slightly as she moves."
        elif the_person.sluttiness < 50:
            "[the_person.possessive_title!c] raises an eyebrow, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
            the_person "Mmm, well, darling... let's get this party started and see where it goes. I have a feeling it's going to be a wild ride."
            "She winks, a flirtatious glint in her eye as she takes your hand and leads you closer, her hips swaying slightly as she moves."
        else:
            "[the_person.possessive_title!c] gazes up at you with a sultry, desperate expression, her voice barely above a whisper."
            the_person "Fuck, darling... I'm glad you're as horny as I am right now. Come on, I need you inside me, and I need it now!"
            "She trembles with anticipation, her body tense and ready to release as she clings to you, her eyes locked on yours with a hungry, sultry intensity."
    else:
        if the_person.sluttiness + (5*the_person.opinion.cheating_on_men) > 50:
            "[the_person.possessive_title!c] raises an eyebrow, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
            the_person "Fuck, darling... you know how to turn me on in ways my [the_person.so_title] never can. Come here, and show me what you're working with."
            "She laughs, a throaty, seductive sound escaping her lips as she takes your hand and leads you closer, her hips swaying slightly as she moves."
        else:
            "[the_person.possessive_title!c] gazes up at you with a sultry, guilty expression, her voice barely above a whisper."
            the_person "You're such bad news, darling... [the_person.mc_title]. I have a [the_person.so_title], but all I can ever think of is you, and what we could do together."
            "She bites her lip, a soft, gentle smile spreading across her face as she takes a step closer to you, her body swaying slightly as she moves."
    return

label alluring_seduction_refuse(the_person):
    if the_person.sluttiness < 20:
        "[the_person.possessive_title!c] gazes up at you with a shy, apologetic expression, her voice barely above a whisper."
        the_person "Sorry, darling... [the_person.mc_title], I'm not really in the mood to flirt or fool around. Maybe some other time, okay?"
        "[the_person.title] shrugs unapologetically, a soft, gentle smile spreading across her face as she looks away, her eyes cast downward in a playful gesture of submission."

    elif the_person.sluttiness < 50:
        "[the_person.possessive_title!c] raises an eyebrow, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
        the_person "I'll admit it, darling... you're tempting me, but I'm not in the mood to fool around right now. Maybe some other time, though... I think we could have a lot of fun together, and I'd love to explore that."
        "She winks, a flirtatious glint in her eye as she takes a step back, her hips swaying slightly as she moves."

    else:
        "[the_person.possessive_title!c] gazes up at you with a sultry, teasing expression, her voice barely above a whisper."
        the_person "Shit, darling... that sounds like a lot of fun, [the_person.mc_title], but I'm not feeling it right now. Hang onto that thought, and we can fool around some other time... I promise it'll be worth the wait."
        "She smiles, a seductive smile spreading across her face as she takes a step closer to you, her body swaying slightly as she moves, before pulling back and walking away, her hips swaying enticingly as she goes."
    return

label alluring_compliment_response(the_person):
    mc.name "Hey, [the_person.fname]... how are you, darling? You're looking quite perky today."
    if the_person.is_at_work:
        if (the_person.is_employee or the_person.is_strip_club_employee) and the_person.is_wearing_uniform:
            call alluring_flirt_response_employee_uniform_low(the_person) from _call_alluring_flirt_response_employee_uniform_low_compliment_response
        elif the_person.is_at_job(prostitute_job):
            "[the_person.possessive_title!c] gazes up at you with a sultry, seductive expression, her voice barely above a whisper."
            the_person "I'm good, babe... how about you and me have some fun together? I think we could have a great time, don't you?"
            "She smiles, a sly smile spreading across her face as she takes a step closer to you, her body swaying slightly as she moves."
        elif the_person.sluttiness > 50:
            "[the_person.possessive_title!c] raises an eyebrow, a flirtatious glint in her eye as she gazes up at you with a brazen, seductive intensity."
            the_person "I'm doing great, darling... and you are looking quite yummy yourself. Maybe we could discuss that further, hmm?"
            "She winks, a playful smile spreading across her face as she takes a step closer to you, her hips swaying slightly as she moves."
        else:
            "[the_person.possessive_title!c] blushes, a shy smile spreading across her face as she gazes up at you with a playful, teasing expression."
            the_person "Oh, stop it, you charmer... but thanks, I'm good. You're making me blush, though."
            "She giggles, a soft, gentle sound escaping her lips as she looks away, her eyes cast downward in a playful gesture of submission."
    else:
        "[the_person.possessive_title!c] smiles, a warm, inviting smile spreading across her face as she gazes up at you with a happy, relaxed expression."
        the_person "Aww, thank you for noticing, darling... I'm doing well. It's nice to have someone to talk to."
        "You chat with [the_person.possessive_title] for a while and slip in a compliment when you can. She is enjoying all the attention, and her body language shows it, her hips swaying slightly as she moves, her eyes locked on yours with a hungry, sultry intensity."
    return

label alluring_compliment_response_girlfriend(the_person):
    mc.name "Hey, [the_person.title]... you're looking very sexy this [StringInfo.time_of_day_string], darling."
    if the_person.is_at_work:
        if (the_person.is_employee or the_person.is_strip_club_employee) and the_person.is_wearing_uniform:
            call alluring_flirt_response_employee_uniform_mid(the_person) from _call_alluring_flirt_response_employee_uniform_mid_compliment_response_girlfriend
            $ the_person.call_dialogue("flirt_response_employee_uniform_mid")
        elif the_person.sluttiness > 50:
            "[the_person.possessive_title!c] gazes up at you with a sultry, seductive expression, her voice barely above a whisper."
            the_person "Mmm, thank you, [the_person.mc_title]... darling. Wanna find out how sexy I am... in private, maybe?"
            "She winks, a flirtatious glint in her eye as she takes a step closer to you, her body swaying slightly as she moves."
        else:
            "[the_person.possessive_title!c] blushes, a shy smile spreading across her face as she gazes up at you with a playful, teasing expression."
            the_person "Ah, really, darling? Thanks, [the_person.mc_title]. You are not looking so bad yourself... maybe we can discuss that further, hmm?"
            "She giggles, a soft, gentle sound escaping her lips as she looks away, her eyes cast downward in a playful gesture of submission."
    else:
        "[the_person.possessive_title!c] smiles, a warm, inviting smile spreading across her face as she gazes up at you with a happy, relaxed expression."
        the_person "Aww, thank you, darling... I'm good. You are looking quite hot yourself... maybe we can do something about that, hmm?"
        "She raises an eyebrow, a flirtatious glint in her eye as she takes a step closer to you, her body swaying slightly as she moves, her eyes locked on yours with a hungry, sultry intensity."
    "You chat with [the_person.possessive_title] for a while, making sexy references where you can. She is quite charmed by your efforts, and her body language shows it, her hips swaying slightly as she moves, her eyes locked on yours with a hungry, sultry intensity."
    return

label alluring_compliment_response_affair(the_person):
    mc.name "Hey, [the_person.title]... you're looking absolutely gorgeous this [StringInfo.time_of_day_string], darling."
    if the_person.is_at_work:
        if (the_person.is_employee or the_person.is_strip_club_employee) and the_person.is_wearing_uniform:
            call alluring_flirt_response_employee_uniform_mid(the_person) from _call_alluring_flirt_response_employee_uniform_mid_compliment_response_affair
        elif the_person.sluttiness > 50:
            "[the_person.possessive_title!c] gazes up at you with a sultry, seductive expression, her voice barely above a whisper."
            the_person "Mmmm, thank you, [the_person.mc_title]... darling. Wanna go somewhere a little more private, so you can make me feel how gorgeous I am? I think we could have a lot of fun together."
            "She winks, a flirtatious glint in her eye as she takes a step closer to you, her body swaying slightly as she moves, her eyes locked on yours with a hungry, sultry intensity."
        else:
            "[the_person.possessive_title!c] blushes, a shy smile spreading across her face as she gazes up at you with a playful, teasing expression."
            the_person "Hush, [the_person.mc_title]!... you really like my outfit? I can show you what I'm wearing underneath... if you want, darling."
            "She giggles, a soft, gentle sound escaping her lips as she looks away, her eyes cast downward in a playful gesture of submission."
    else:
        "[the_person.possessive_title!c] smiles, a warm, inviting smile spreading across her face as she gazes up at you with a happy, relaxed expression."
        the_person "You like this, darling? Take me to dinner, and we can explore other parts... of the city, maybe. Or maybe just explore each other, hmm?"
        "She raises an eyebrow, a flirtatious glint in her eye as she takes a step closer to you, her body swaying slightly as she moves, her eyes locked on yours with a hungry, sultry intensity."
    "You keep chatting with [the_person.possessive_title] for a while, slipping in a few more compliments. She is quite enamoured by your attentiveness, and her body language shows it, her hips swaying slightly as she moves, her eyes locked on yours with a hungry, sultry intensity."
    return

label alluring_flirt_response(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] gazes up at you with a sultry, submissive expression, her voice barely above a whisper."
            the_person "You know that all you have to do is ask, darling... and it's all yours. I'm yours to command."
            "She smiles, a shy smile spreading across her face as she looks down, her eyes cast downward in a playful gesture of submission."
        else:
            "[the_person.possessive_title!c] blushes, a shy smile spreading across her face as she gazes up at you with a playful, teasing expression."
            the_person "Thank you, [the_person.mc_title]... darling. I'm glad you're enjoying the view. Maybe you'll get to see more of it later, hmm?"
            "She giggles, a soft, gentle sound escaping her lips as she looks away, her eyes cast downward in a playful gesture of submission."

    elif the_person.has_significant_other:
        if the_person.sluttiness + (the_person.opinion.cheating_on_men*5) > 50:
            "[the_person.possessive_title!c] raises an eyebrow, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
            the_person "Then why don't you do something about it, darling? Come on, we don't have to tell my [the_person.so_title] anything at all, right? It can be our little secret."
            "[the_person.title] winks and spins around, giving you a full look at her body, her hips swaying slightly as she moves, her eyes locked on yours with a hungry, sultry intensity."
        else:
            "[the_person.possessive_title!c] gazes up at you with a sultry, warning expression, her voice barely above a whisper."
            the_person "You're playing with fire, [the_person.mc_title]... darling. I've got a [the_person.so_title], and I don't think he'd appreciate you flirting with me. But I might, hmm?"
            mc.name "What about you, do you appreciate it, darling?"
            "She gives a coy smile and shrugs, her eyes locked on yours with a hungry, sultry intensity."
            the_person "Maybe I do, darling... maybe I do."

    else:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] gazes up at you with a sultry, seductive expression, her voice barely above a whisper."
            the_person "Then why don't you do something about it, darling? Come on, all you have to do is ask. I'm ready and willing, hmm?"
            "[the_person.title] smiles at you and spins around, giving you a full look at her body, her hips swaying slightly as she moves, her eyes locked on yours with a hungry, sultry intensity."
        else:
            "[the_person.possessive_title!c] raises an eyebrow, a sly smile spreading across her face as she gazes up at you with a playful, teasing expression."
            the_person "Well, thank you, darling... play your cards right and maybe you'll get to see a little bit more. But you'll have to really impress me, hmm? I have high standards, and I don't settle for anything less."
            the_person "But I think you might be up to the challenge, darling... I think you might just be the one I'm looking for."
            "She smiles, a seductive smile spreading across her face as she takes a step closer to you, her body swaying slightly as she moves, her eyes locked on yours with a hungry, sultry intensity."
    return

label alluring_flirt_response_employee_uniform_low(the_person):
    if the_person.is_wearing_forced_uniform:
        "[the_person.possessive_title!c] gazes up at you with a sultry, teasing expression, her voice barely above a whisper."
        the_person "I'm sure you like it, darling... I'm practically naked! But I have to admit, it's kind of exciting to be dressed like this for you."
        mc.name "I know you don't like it, but I needed to make a point, darling."
        the_person "I know, I know... but I'm willing to make an exception for you, hmm?"
        $ mc.change_locked_clarity(5)
        "She smiles and gives you a quick turn to either side, showing off her body, her hips swaying slightly as she moves, her eyes locked on yours with a hungry, sultry intensity."
    elif the_person.judge_outfit(the_person.outfit):
        #She's in uniform and likes how it looks.
        "[the_person.possessive_title!c] raises an eyebrow, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
        the_person "Thanks, darling! I think I look pretty cute in it too. It's nice to work somewhere where I can show off a little... and I love the way you look at me when I'm dressed like this."
        the_person "It's like you can't take your eyes off me, hmm? And I have to admit, I like the attention."
        $ mc.change_locked_clarity(5)
        "She smiles and gives you a quick turn to either side, showing off her hips, her body swaying slightly as she moves, her eyes locked on yours with a hungry, sultry intensity."

    else:
        #She's in uniform, but she thinks it's a little too slutty.
        if the_person.vagina_visible:
            # Her pussy is on display.
            "[the_person.possessive_title!c] gazes up at you with a sultry, teasing expression, her voice barely above a whisper."
            the_person "I'm sure you like it, darling... I'm practically naked! But I have to admit, it's kind of exciting to be dressed like this for you."
            mc.name "Well, you know that it's..."
            the_person "I know, I know... it's company policy, darling. But I'm not complaining, exactly. It's kind of fun to be a little naughty, hmm?"
            mc.name "Give it some time and you'll get used to it, darling."
            $ mc.change_locked_clarity(5)
            "She smiles and nods, her eyes locked on yours with a hungry, sultry intensity."
            the_person "I'm sure I will, darling... and I'm looking forward to it."

        elif the_person.tits_visible:
            # Her tits are out
            "[the_person.possessive_title!c] raises an eyebrow, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
            the_person "Thanks, darling! I'm still getting used to being so... exposed in this uniform. But at least I don't have to wear a bra, hmm? That's a definite plus."
            mc.name "You look incredible, darling... and you're comfortable. I call that a success."
            $ mc.change_locked_clarity(5)
            "She laughs and shrugs, her body swaying slightly as she moves, her eyes locked on yours with a hungry, sultry intensity."
            the_person "Sure, I guess you could call it that, darling... but I think it's more than that. I think it's a chance for us to get a little closer, hmm?"

        elif the_person.underwear_visible:
            # Her underwear is visible.
            "[the_person.possessive_title!c] gazes up at you with a sultry, teasing expression, her voice barely above a whisper."
            the_person "Thanks, darling! I probably would have picked something that kept me a little more covered, but at least our uniform is comfortable... and I have to admit, it's kind of exciting to be dressed like this for you."
            mc.name "It may be a little unconventional, darling... but you look fantastic. You've got exactly the right kind of body for it, hmm?"
            the_person "Well, that's good to know, darling... I'm glad you like it."
            $ mc.change_locked_clarity(5)
            "She smiles and gives you a quick turn to either side, showing off her body, her hips swaying slightly as she moves, her eyes locked on yours with a hungry, sultry intensity."

        else:
            # It's just generally slutty.
            "[the_person.possessive_title!c] raises an eyebrow, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
            the_person "Well, thank you, darling! Our uniforms are a little bold for my taste, but I'm glad I look good in it... and I'm glad you like it, hmm?"
            $ mc.change_locked_clarity(5)
            "She smiles and gives you a quick turn to either side, showing off her body for you, her hips swaying slightly as she moves, her eyes locked on yours with a hungry, sultry intensity."
    return

label alluring_flirt_response_employee_uniform_mid(the_person):
    if the_person.is_wearing_forced_uniform:
        $ mc.change_locked_clarity(10)
        if the_person.vagina_visible:
            "[the_person.possessive_title!c] gazes up at you with a sultry, teasing expression, her voice barely above a whisper."
            the_person "I mean, look at me, darling! I feel like you should be throwing twenties at me every time I walk away... or maybe just throwing me onto the bed, hmm?"
            "She winks and strikes a pose, her hips swaying slightly as she moves, her eyes locked on yours with a hungry, sultry intensity."
        elif the_person.tits_visible:
            "[the_person.possessive_title!c] raises an eyebrow, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
            the_person "I mean, look at me, darling! I feel like you should be tucking a twenty into my underwear every time I want to talk to you... or maybe just tucking your hand into my underwear, hmm?"
            "She winks and wiggles her shoulders, setting her boobs jiggling for you, her eyes locked on yours with a hungry, sultry intensity."
        else:
            "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
            the_person "I mean, look at it, darling! I feel like an underwear model every time I get dressed for work... and I think I'd make a great model, don't you, hmm?"
            "She smiles and strikes a pose, her hips swaying slightly as she moves, her eyes locked on yours with a hungry, sultry intensity."
        mc.name "Rules are rules, darling... and I'm afraid I have to enforce them, even if you do look good enough to eat."
        "She sighs and nods, a pouty expression on her face, but her eyes still sparkling with amusement."
        the_person "Yeah, I know, darling... at least you're having a good time. I don't mind that so much, as long as you're enjoying the view."

    elif the_person.judge_outfit(the_person.outfit):
        $ mc.change_locked_clarity(10)
        if the_person.tits_visible:
            "[the_person.possessive_title!c] raises an eyebrow, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
            the_person "Are you sure you don't mean my tits look good in this outfit, darling? Because I think they're looking particularly perky today, don't you, hmm?"
            "She winks and wiggles her shoulders, setting her boobs jiggling for you, her eyes locked on yours with a hungry, sultry intensity."
            mc.name "All of you looks good, tits included, darling. You're a vision of loveliness, as always."
            the_person "Good answer, darling! I think these uniforms are pretty hot too. You've got some good fashion sense, and I love the way you look at me when I'm dressed like this."
        else:
            "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
            the_person "Aw, thanks, darling! I think your uniforms look pretty hot on me too. You've got some good fashion sense, and I love the way you look at me when I'm dressed like this."
        the_person "Maybe I'll invite you shopping one day, darling... and you can tell me what else you want to see me in. I think that could be a lot of fun, don't you, hmm?"
        mc.name "Sounds like a good time, darling. I'd love to go shopping with you and pick out some new outfits for you to wear."

    else:
        # the_person "I think it shows off a little too much!"
        "[the_person.possessive_title!c] gazes up at you with a sultry, teasing expression, her voice barely above a whisper."
        the_person "Thanks, darling... but I think these uniforms show off just a little too much of my fabulous body, don't you, hmm? I mean, I know you like to look at me, but this is just a little too much, even for you."
        $ mc.change_locked_clarity(10)
        if the_person.vagina_visible:
            the_person "I mean, look at me, darling! I feel like you should be throwing twenties at me every time I walk away... or maybe just throwing me onto the bed, hmm?"
            "She winks and strikes a pose, her hips swaying slightly as she moves, her eyes locked on yours with a hungry, sultry intensity."
        elif the_person.tits_visible:
            the_person "I mean, look at me, darling! I feel like you should be tucking a twenty into my underwear every time I want to talk to you... or maybe just tucking your hand into my underwear, hmm?"
            "She winks and wiggles her shoulders, setting her boobs jiggling for you, her eyes locked on yours with a hungry, sultry intensity."
        else:
            the_person "I mean, look at it, darling! I feel like an underwear model every time I get dressed for work... and I think I'd make a great model, don't you, hmm?"
            "She smiles and strikes a pose, her hips swaying slightly as she moves, her eyes locked on yours with a hungry, sultry intensity."
        mc.name "I understand, darling... but I promise it's important for the business. And I have to say, you do look lovely in that uniform, even if it is a little revealing."
        "She sighs and nods, a pouty expression on her face, but her eyes still sparkling with amusement."
        the_person "Yeah, I know, darling... at least you're having a good time. I don't mind that so much, as long as you're enjoying the view."
    return

label alluring_flirt_response_low(the_person):
    #She's in her own outfit.
    "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
    the_person "Thanks, darling... it's really cute, right? I was hoping you'd like it."
    $ the_person.draw_person(position = "walking_away")
    $ mc.change_locked_clarity(5)
    "She smiles and gives you a quick spin, showing off her outfit from every angle, her hips swaying slightly as she moves, her eyes locked on yours with a hungry, sultry intensity."
    "As she spins, her skirt flares out, giving you a glimpse of her thighs, and her top clings to her curves, accentuating her breasts."
    $ the_person.draw_person()
    "She strikes a pose, her hand on her hip, her eyes sparkling with amusement, and her lips curled up in a sly smile."
    return

label alluring_flirt_response_low1(the_person):
    if the_person.has_significant_other:
        "[the_person.possessive_title!c] gazes up at you with a sultry, warning expression, her voice barely above a whisper."
        the_person "You're playing with fire, [the_person.mc_title]... darling. I've got a [the_person.so_title], and I don't think he'd appreciate you flirting with me."
        mc.name "What about you, darling... do you appreciate it?"
        "She gives a coy smile and shrugs, her eyes sparkling with amusement, and her lips curled up in a sly smile."
        the_person "Maybe I do, darling... maybe I do. But don't tell anyone, it's our little secret."
        "She winks, a flirtatious glint in her eye, as she takes a step closer to you, her body swaying slightly as she moves."

    else:
        "[the_person.possessive_title!c] raises an eyebrow, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
        the_person "Well, thank you, darling... play your cards right, and maybe you'll get to see a little bit more. But don't expect anything too easily, I like to keep things interesting."
        the_person "You'll have to really impress me, though... I have high standards, and I don't settle for anything less than perfection."
        "She takes a step closer to you, her body swaying slightly as she moves, her eyes locked on yours with a hungry, sultry intensity, as she whispers in your ear."
        the_person "But I think you might just be up to the challenge, darling... I think you might just be the one I'm looking for."
    $ mc.change_locked_clarity(5)
    return

label alluring_flirt_response_mid(the_person):
    if mc.location.person_count > 1 and the_person.effective_sluttiness("kissing") < (25 - (5*the_person.opinion.public_sex)):
        $ mc.change_locked_clarity(10)
        if the_person.tits_visible:
            "[the_person.possessive_title!c] raises an eyebrow, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
            the_person "Are you sure you don't mean my tits look good in this outfit, darling? Because I think they're looking particularly perky today, don't you?"
            "She winks and wiggles her shoulders, setting her boobs jiggling for you, her eyes locked on yours with a hungry, sultry intensity."
            mc.name "All of you looks good, tits included, darling. You're a vision of loveliness, as always."
            the_person "Good answer, darling. I knew you would like this look when I was picking it out this morning... I was thinking of you the whole time, hmm?"
        else:
            "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
            the_person "Aw, thanks, darling! I thought this was a pretty hot look when I was getting dressed this morning... and I'm glad you agree, hmm?"

        the_person "Maybe I'll invite you shopping one day, darling... so you can tell me what else you want to see me in. I think that could be a lot of fun, don't you?"
        mc.name "I can think of a few things already, darling... and I'm sure I'll come up with even more when we're shopping together."
        the_person "I'm sure you can, darling... and I'm looking forward to it, hmm?"

    else:
        "[the_person.possessive_title!c] raises an eyebrow, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
        the_person "Thanks, darling... I thought I looked pretty hot in it too. You want a better look, right? Here, how does it make my ass look?"
        $ the_person.draw_person(position = "back_peek")
        $ mc.change_locked_clarity(10)
        the_person "Good, right? I think it makes my ass look pretty amazing, if I do say so myself, hmm?"
        mc.name "Fantastic, darling... I wish I could get an even better look at it. Maybe up close and personal, hmm?"
        "[the_person.possessive_title!c] smiles and turns back to face you, her eyes locked on yours with a hungry, sultry intensity."
        $ the_person.draw_person()
        the_person "I'm sure you do, darling... take me out for a drink and maybe we can work something out. I'm game if you are, hmm?"
    return

label alluring_flirt_response_mid1(the_person):
    $ mc.change_locked_clarity(10)
    "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
    the_person "Thanks, darling... I do look amazing in this outfit, don't I? I was thinking of you when I put it on, hmm?"
    if (the_person.has_skirt or the_person.has_dress) and not the_person.has_thigh_high_socks:
        mc.name "You could change it up with some high stockings, darling... I would love to see that. I think it would really make your legs stand out, hmm?"
        "[the_person.possessive_title!c] raises an eyebrow, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
        the_person "I bet you would, you naughty boy... but I think I can make it work, hmm? For you, at least."

    mc.name "How about you and me go and grab a coffee sometime, darling? Just the two of us, hmm?"
    if the_person.has_significant_other:
        "[the_person.possessive_title!c] gazes up at you with a sultry, teasing expression, her voice barely above a whisper."
        the_person "Sure, darling... my [the_person.so_title] doesn't mind, or at least, I won't tell him, hmm? It can be our little secret."
    else:
        "[the_person.possessive_title!c] smiles, a warm, inviting smile spreading across her face as she gazes up at you with a happy, relaxed expression."
        the_person "Why not, darling? I could use a pick-me-up once in a while... and I think you might just be the one to give it to me, hmm?"
    "[the_person.possessive_title!c] leans in closer to you, her voice barely above a whisper."
    the_person "Just let me know when, darling... I would love to. I'm always up for a good time, hmm?"
    return

label alluring_flirt_response_high(the_person):
    if mc.location.person_count > 1 and the_person.effective_sluttiness() < (25 - (5*the_person.opinion.public_sex)): # There are other people here, if she's not slutty she asks if you want to find somewhere quiet
        "[the_person.possessive_title!c] gazes up at you with a sultry, teasing expression, her voice barely above a whisper."
        the_person "Driving you crazy, huh? Well... maybe we should do something about that, but not here, darling."
        "She glances around, her eyes sparkling with amusement, before smiling mischievously."
        menu:
            "Find somewhere more quiet\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                mc.name "Then let's find somewhere that isn't here, darling. I want to be alone with you."
                "[the_person.possessive_title!c] raises an eyebrow, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
                the_person "Eager, huh? Alright, let's go find somewhere, darling. I'm ready to get a little naughty with you."
                call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_alluring_flirt_response_high_2
                the_person "So... now what's your plan, darling? Are you going to make me scream with pleasure?"
                if the_person.is_willing(kissing):
                    $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
                    if the_person.has_taboo("kissing"):
                        "You step close to [the_person.title] and put your arm around her waist, pulling her close."
                        $ the_person.call_dialogue("kissing_taboo_break")
                        $ the_person.break_taboo("kissing")
                        "You kiss her. She eagerly presses her body against yours in response, her lips trembling with desire."
                    else:
                        "You step close to [the_person.title] and put your arm around her waist, pulling her close and kissing her."
                        "She responds immediately and eagerly presses her body against yours, her tongue dancing with yours."
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from vt_allure_call_fuck_person_49
                else:
                    if the_person.has_taboo("touching_body"):
                        $ the_person.call_dialogue("touching_body_taboo_break")
                        $ the_person.break_taboo("touching_body")
                        "You take her hand and pull her close against you. She looks into your eyes, her gaze burning with desire."
                    else:
                        "You answer by pulling her close against you, your bodies pressed together in a sensual dance."
                    call fuck_person(the_person, private = True, start_position = standing_grope, skip_intro = True) from _call_fuck_person_alluring_flirt_grope

                $ the_person.call_dialogue("sex_review", the_report = _return)
                call mc_restore_original_location(the_person) from _call_mc_restore_original_location_alluring_flirt_response_high_2

            "Just flirt":
                mc.name "Not here, huh? How about back at your place then, darling?"
                "[the_person.possessive_title!c] raises an eyebrow, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
                the_person "Bold, darling. I like it. Maybe if you buy me dinner, you'll get your chance to take me home and show me what you're working with."

    else:
        if mc.location.person_count == 1: #You're alone, so she just didn't meet the sluttiness threshold
            "[the_person.possessive_title!c] bites her lower lip and glances around, confirming you're alone, before gazing up at you with a sultry, teasing expression."
            the_person "Well, it's just the two of us here, so now's your chance to find out, darling. What's your plan? Are you going to make me scream with pleasure?"

        else:  # You aren't alone but she's still into it.
            "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
            the_person "Feeling bold today, huh? Well, I think your chances are pretty good, darling. I'm in the mood for something naughty."
            if the_person.has_large_tits: #Bounces her tits for you
                $ mc.change_locked_clarity(15)
                "[the_person.title] grabs her tits and jiggles them for you, her eyes locked on yours with a hungry, sultry intensity."
                the_person "Maybe I can get these girls out for you, darling. Does that sound nice? I think it would be a lot of fun."
            else: #No big tits, so she can't bounce them (as much)
                "[the_person.title] runs her hands over her hips sensually, obviously encouraging you to take things further, her eyes locked on yours with a hungry, sultry intensity."

        menu:
            "Touch her" if not the_person.is_willing(kissing):
                "You step closer to [the_person.title] and move your hands down her waist, your fingers tracing the curves of her body."
                if the_person.has_taboo("touching_body"):
                    $ the_person.call_dialogue("touching_body_taboo_break")
                    $ the_person.break_taboo("touching_body")
                    "She shudders with pleasure, her body trembling with desire."

                call fuck_person(the_person, start_position = standing_grope, private = False) from _call_fuck_person_flirt_response_alluring_touching

            "Kiss her" if the_person.is_willing(kissing):
                $ the_person.draw_person()
                if the_person.has_taboo("kissing"):
                    "You put your arm around [the_person.possessive_title] and lean in close, your lips inches from hers."
                    $ the_person.call_dialogue("kissing_taboo_break")
                    $ the_person.break_taboo("kissing")
                    "You kiss her. She returns the kiss and presses her body against you, her tongue dancing with yours."
                else:
                    "You put your arm around [the_person.possessive_title] and pull her close, leaning in to kiss her, your lips meeting in a passionate kiss."
                    "She responds immediately, pressing her body against yours and kissing you back, her tongue tracing the curves of your mouth."

                call mc_move_to_private_location(the_person) from  _call_mc_move_to_private_location_alluring_flirt_response_high
                call fuck_person(the_person, start_position = kissing, private = _return, skip_intro = True) from vt_allure_call_fuck_person_50
                $ the_person.call_dialogue("sex_review", the_report = _return)
                call mc_restore_original_location(the_person) from _call_mc_restore_original_location_alluring_flirt_response_high

            "Just flirt":
                $ the_person.draw_person()
                mc.name "Very tempting, darling... but you're going to have to contain yourself for now. I'm not ready to take things that far... yet."
                "[the_person.title] pouts melodramatically, her eyes sparkling with amusement."
                the_person "You're so cruel, darling. Maybe you can take me out to dinner to make up for it. I promise I'll be on my best behavior... or not, depending on how the night goes."
    return

label alluring_flirt_response_low_energy(the_person):
    if the_person.sluttiness > 40:
        "[the_person.possessive_title!c] gazes up at you with a sultry, tired expression, her voice barely above a whisper."
        the_person "Oh, thank you, darling... now I wish I wasn't so exhausted. I'd love to take things further, but I don't think I have the energy for it right now."
        "She smiles, a soft, gentle smile spreading across her face as she looks up at you with a hint of disappointment in her eyes."

    else:
        "[the_person.possessive_title!c] looks up at you with a shy, tired expression, her voice barely above a whisper."
        the_person "Thank you, darling... I'm a little worn out, can we pick this up later? I'm not really feeling up to flirting right now, but I promise I'll make it up to you soon."
        "She smiles, a soft, gentle smile spreading across her face as she looks up at you with a hint of apology in her eyes."
    return

label alluring_flirt_response_girlfriend(the_person):
    # Lead in: mc.name "You're so beautiful [the_person.title], I'm so lucky to have a woman like you in my life."
    if mc.location.person_count > 1:
        # There are other people around, so she'll only start making out with you if she's slutty.
        if the_person.effective_sluttiness("kissing") < (25 - (5*the_person.opinion.public_sex)):
            # Not very slutty, so she wants to find somewhere private
            "[the_person.possessive_title!c] gazes up at you with a sultry, teasing expression, her voice barely above a whisper."
            the_person "Oh my god, you're such a sap, darling... come here and show me how you really feel."
            "She pulls you against her and kisses you intensely, her lips burning with passion. She smiles when she breaks the kiss a moment later, her eyes sparkling with amusement."
            the_person "There, that's how you should show a woman how you feel, darling. With passion and fire."
            mc.name "Uh huh, I think I've got the idea, darling... but I'm not sure I can wait to get you alone."
            "You put your arms around her and kiss her back, matching her own intensity, your tongues dancing together in a sensual rhythm."
            the_person "Mmm, yeah you've got it, darling... don't get too excited though, we have to wait until we're alone to do anything more. But I promise it'll be worth the wait."
            menu:
                "Find somewhere more quiet\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                    mc.name "Why wait, darling? Come on, I'm sure we can find somewhere quiet... and private."
                    "[the_person.possessive_title!c] raises an eyebrow, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
                    the_person "That eager, huh? Alright, let's go, darling! I'm ready to get a little naughty with you."
                    "You and [the_person.possessive_title] hurry off, searching for a private spot, your hands entwined as you walk."
                    call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_alluring_flirt_response_girlfriend_2
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from vt_allure_call_fuck_person_76
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_alluring_flirt_response_girlfriend_2

                "Just flirt":
                    $ mc.change_locked_clarity(10)
                    "You reach behind [the_person.possessive_title] and grab her ass, giving it a firm squeeze, your fingers tracing the curves of her body."
                    mc.name "Alright, I'll be patient, darling... this ass is worth waiting for, and I'm going to make sure it's worth the wait."
                    "She wiggles her hips back against your hand, her eyes sparkling with amusement."
                    the_person "Damn right it is, darling... and I'm going to make sure you know it."

        else:
            "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
            the_person "Well, if I'm so beautiful, then hurry up and kiss me, hot stuff... I'm ready to get a little naughty with you."
            "You put your arm around her waist and lean close, kissing her on her lips, your tongues dancing together in a sensual rhythm."
            "When you break the kiss [the_person.possessive_title] sighs happily and leans her head against your shoulder, her eyes sparkling with amusement."
            the_person "Why did you stop, darling? I was having such a good time... and I'm not ready to stop yet."
            menu:
                "Make out":
                    "You don't say a word as you lean back and kiss her again, slowly and sensually this time, your lips burning with passion."
                    "[the_person.title] presses her body against you in response, grinding her hips against your thigh, her eyes locked on yours with a hungry, sultry intensity."

                    call mc_move_to_private_location(the_person) from  _call_mc_move_to_private_location_alluring_flirt_response_girlfriend
                    call fuck_person(the_person, start_position = kissing, private = _return, skip_intro = True) from vt_allure_call_fuck_person_77
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_alluring_flirt_response_girlfriend

                "Just flirt":
                    mc.name "I just like to tease you, darling... and make you wait for it."
                    $ mc.change_locked_clarity(10)
                    "You reach around and grab her ass, squeezing it playfully, your fingers tracing the curves of her body."
                    "She pouts melodramatically and rubs your chest, her eyes sparkling with amusement."
                    the_person "Ugh, you're the worst, darling... I was already getting turned on, and now you're just making me wait."

    else:
        # You're alone, so she's open to fooling around.
        "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
        the_person "Well, you've got me all alone, darling... so how about you show me just how lucky you feel? I'm ready to get a little naughty with you."
        "She reaches down to your waist and cups your crotch, rubbing it gently, her eyes locked on yours with a hungry, sultry intensity."
        menu:
            "Kiss her":
                if the_person.has_taboo("kissing"):
                    $ the_person.call_dialogue("kissing_taboo_break")
                    $ the_person.break_taboo("kissing")

                "You put your arms around [the_person.possessive_title]'s waist and rest your hands on her ass, pulling her close and kissing her sensually, your lips burning with passion."
                "She responds by pressing her body against you and grinding her hips against your thigh, her eyes locked on yours with a hungry, sultry intensity."
                call fuck_person(the_person, start_position = kissing, skip_intro = True) from vt_allure_call_fuck_person_78
                $ the_person.call_dialogue("sex_review", the_report = _return)
                $ the_person.review_outfit()

            "Just flirt":
                "You reach your arms around her waist and grab her ass, squeezing it playfully, your fingers tracing the curves of her body."
                mc.name "I'm sorry, darling... but I'm going to make you wait a bit for that. I just like seeing you get all worked up, and I'm not ready to stop teasing you yet."
                "She pouts melodramatically, her eyes sparkling with amusement."
                the_person "Ugh, you're the worst, darling... I was already getting so turned on, and now you're just making me wait. But I'll get you back for this, oh yes..."
    return

label alluring_flirt_response_affair(the_person):
    # Lead in: mc.name "You look so good today [the_person.title], you're making me want to do some very naughty things to you."
    if mc.location.person_count > 1: #There are other people around, she's nervous about people finding out what you're doing.
        if (the_person.opinion.cheating_on_men *15) + the_person.effective_sluttiness() > 50: #SHe's turned on by flirting in public or doesn't think anything is wrong with it
            "[the_person.possessive_title!c] bites her lower lip and looks you up and down, eyes lingering on your crotch, a sultry, teasing expression on her face."
            the_person "Yeah? Well... I've got some spare time, darling. How about we slip away and you can show me what you mean? I'm dying to find out what you have in mind."
            menu:
                "Find somewhere more quiet\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                    mc.name "Alright, let's go, darling. I have a few ideas I want to try out on you."
                    "You and [the_person.title] hurry off to find a quiet spot, your hands entwined as you walk."
                    call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_alluring_flirt_response_affair
                    $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
                    "As soon as you're alone, she pulls you into a deep and passionate kiss, her lips burning with desire."
                    $ the_person.draw_person(position = "kissing")
                    the_person "Ah... you aren't the only one having dirty thoughts, darling. You get me so fucking horny! I need you to take care of me, now."
                    "You wrap your arms around her waist and kiss her back, your tongues dancing together in a sensual rhythm."
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from vt_allure_call_fuck_person_79
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_alluring_flirt_response_affair

                "Just flirt":
                    "You slide your arm around [the_person.title]'s waist and rest your hand on her ass, rubbing it gently, your fingers tracing the curves of her body."
                    mc.name "You'll have to wait a little bit, darling... we don't have time for all the things I want to do to you right now. But I promise it'll be worth the wait."
                    $ mc.change_locked_clarity(20)
                    "She glances around and checks to make sure nobody else is watching, then she slides her hand down your waist and to your crotch, her eyes locked on yours with a hungry, sultry intensity."
                    "[the_person.possessive_title!c] massages your bulge lightly and pouts, her lips curled up in a sly smile."
                    the_person "That's a shame, darling... I can think of so many fun things to do with this. Just don't make me wait too long, okay? I barely get any action from my [the_person.so_title]."
                    "You give her ass a slap before letting go, your hand stinging her skin."
                    mc.name "It won't be too long, darling... I promise. And when it happens, it'll be worth the wait."

        else: #She's shy or nervous about being discovered
            "[the_person.possessive_title!c] laughs, then shakes her head and glances around, a nervous expression on her face."
            the_person "You're looking pretty hot too, darling... but you need to be a little more subtle. I don't want any rumours getting back to my [the_person.so_title]. That would really throw a wrench into our little affair..."
            $ mc.change_locked_clarity(15)
            "After checking again that nobody else is watching, she reaches over and cups your crotch, massaging the bulge through your pants, her eyes locked on yours with a hungry, sultry intensity."
            the_person "Just be patient, darling... I'll be all over this dick soon enough. And when I am, you'll know it."
            mc.name "Alright, darling... I think I can contain myself a little while longer. But it's not going to be easy, knowing what's waiting for me."
            "She pulls her hand back and smiles, a sly smile spreading across her face."

    else:
        # the_person "Yeah? Well there's nobody around, and I'm not going to stop you."
        "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
        the_person "Oh yeah? Well then, darling... do you want to share what all of these naughty things are? You have my attention, and I'm dying to know what you have in mind."
        menu:
            "Feel her up":
                "You put your arms around [the_person.possessive_title]'s waist and rest your hands on her ass, your fingers tracing the curves of her body."
                mc.name "Well, first I want to get my hands all over your beautiful body, darling. I want to feel every inch of you."
                "You massage her butt, and she sighs happily, leaning against your body, her eyes locked on yours with a hungry, sultry intensity."
                the_person "What next, darling? What do you want to do to me? I'm all yours."
                "You spin her around and shift your hands to her breasts, squeezing them, your fingers tracing the curves of her body."
                mc.name "No need to rush things, darling... just relax and enjoy for now. We have all the time in the world."
                call fuck_person(the_person, private = True, start_position = standing_grope, skip_intro = True) from vt_allure_call_fuck_person_80
                $ the_person.call_dialogue("sex_review", the_report = _return)
                $ the_person.review_outfit()

            "Just flirt":
                $ mc.change_locked_clarity(10)
                "You put your arms around [the_person.possessive_title]'s waist and rest your hands on her ass, your fingers tracing the curves of her body."
                mc.name "I wish I had the time, darling... you'll have to wait until later. But I promise it'll be worth the wait."
                "You massage her butt, and she sighs happily, leaning her weight against you, her eyes locked on yours with a hungry, sultry intensity."
                the_person "Aww, are you sure, darling? I was really looking forward to it."
                "You slap her ass and step back, your hand stinging her skin."
                the_person "Fine, darling... but don't make me wait too long, okay? I have needs, and my [the_person.so_title] sure as hell isn't fulfilling them."
                mc.name "I won't make you wait long, darling... I promise. And when it happens, it'll be worth the wait."
    return

label alluring_flirt_response_text(the_person):
    mc.name "Hey [the_person.title], what's up, darling? I'm bored and figured we could chat."
    "There's a brief pause, then she texts back, her words dripping with seduction."
    if the_person.is_affair:
        the_person "I'm bored too, darling... and I can think of a few things we could do together to stop being bored. Things that would be much more fun than just chatting, hmm?"
        the_person "When can we get together, darling? I'm dying to see you and feel your touch."
        mc.name "Some time soon, darling... I'll let you know. But trust me, it'll be worth the wait."

    elif the_person.is_girlfriend:
        the_person "I'm bored too, darling... we should get together and hang out. Maybe do something naughty, hmm?"
        the_person "When are you going to take me out on another date, darling? I'm going to have to do it myself at this rate... and I don't think you want that, do you?"
        mc.name "Some time soon, darling... I'll let you know. And when I do, it'll be a night to remember, I promise."

    elif the_person.love < 40:
        if the_person.effective_sluttiness() > the_person.love:
            the_person "Bored, huh, darling? Well, I'm here to entertain... and I think I can come up with a few ideas to keep you occupied, hmm?"
        else:
            the_person "That sucks, being bored is the worst, darling... but I'm here for you, so let's chat and see if we can't come up with something to liven things up."

    else:
        if the_person.effective_sluttiness() > the_person.love:
            the_person "Bored, huh, darling? Well, I'm here to entertain you, so what would you like me to do... or talk about, hmm? I'm all yours, darling."
            the_person "I mean, what would you like to talk about, darling? The possibilities are endless, and I'm game for anything, hmm?"
        else:
            the_person "Bored and you came to me, huh, darling? It must be really bad... but don't worry, I'm here for you, and I'll do my best to make it all better, hmm?"
            the_person "Alright, let's chat then, darling... what's up with you? What's been going on in that head of yours, hmm?"
    return

label alluring_condom_demand(the_person):
    if the_person.wants_creampie:
        "[the_person.possessive_title!c] gazes up at you with a sultry, teasing expression, her voice barely above a whisper."
        the_person "Oh shit, darling... you need to put on a condom before we do anything. I hate it too, but it's just a precaution, hmm?"
        the_person "I want to feel you inside me, but I also want to be safe, darling. So, let's get that condom on and get this party started, shall we?"

    else:
        "[the_person.possessive_title!c] raises an eyebrow, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
        the_person "Hey, darling... you have a condom on you, right? You need to put one on before you can fuck me, and I'm not getting any younger, hmm?"
        the_person "Don't take too long, darling... I might get cold feet, or worse, I might just have to take matters into my own hands, and I don't think you want that, do you?"
    return

### DIALOGUE ###
label alluring_condom_ask(the_person):
    if the_person.on_birth_control:
        "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
        the_person "Want a condom, darling? I'm on the pill, but I guess it's still possible something goes wrong... and I don't want to take any chances, hmm?"
        $ the_person.update_birth_control_knowledge()
        "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."

    elif the_person.wants_creampie:
        "[the_person.possessive_title!c] raises an eyebrow, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
        the_person "If you want to cum inside me, darling... you should probably put on a condom. I know it's less fun than fucking raw, but it's still better than pulling out, right?"
        the_person "I want to feel you inside me, but I also want to be safe, darling. So, let's get that condom on and get this party started, shall we?"
        $ the_person.discover_opinion("creampies")

    else:
        "[the_person.possessive_title!c] gazes up at you with a sultry, teasing expression, her voice barely above a whisper."
        the_person "Fuck, darling... I should probably tell you to put on a condom... but I don't want to ruin the moment, hmm?"
        the_person "I can trust you to pull out, right, darling? We'll need to be careful... but I'm willing to take that risk with you, hmm?"
    return

label alluring_condom_bareback_ask(the_person):
    if the_person.wants_creampie:
        if the_person.is_infertile:
            "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
            the_person "You aren't thinking of wearing a condom, are you, darling? Fuck that, I want you to paint my pussy white... and make me scream with pleasure."
            "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."

        elif the_person.on_birth_control:
            "[the_person.possessive_title!c] raises an eyebrow, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
            the_person "You aren't thinking of wearing a condom, are you, darling? Fuck that, I'm on the pill... and I'm ready to get a little naughty with you."
            the_person "You can cum right inside me, no worries, darling... and I'll make sure you know it's worth it."
            $ the_person.update_birth_control_knowledge()
            "She winks, a flirtatious glint in her eye, as she takes a step closer to you, her body swaying slightly as she moves."

        else:
            "[the_person.possessive_title!c] gazes up at you with a sultry, teasing expression, her voice barely above a whisper."
            the_person "Forget the condom, darling [the_person.mc_title]... I want you to fuck me raw, and make me feel every inch of you inside me."
            if not the_person.knows_pregnant:
                the_person "I want to feel you cum inside me, knowing I might be getting knocked up, darling... it's such a thrill, and I love the risk."
            the_person "That would be so fucking hot, darling... and I know I'd love every minute of it."
            $ the_person.discover_opinion("creampies")

    else:
        "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
        the_person "Don't bother with a condom, darling [the_person.mc_title]... I want to feel you raw, and unbridled."
        if not the_person.knows_pregnant:
            the_person "I don't care what the risks are, darling... they're worth it, just to feel you inside me, and know that I'm taking a chance with you."
        else:
            the_person "I love it, darling... when you fuck me raw, and make me feel every inch of you inside me. It's like nothing else matters, and all I can think about is you, and your cock."
    return

label alluring_condom_bareback_demand(the_person):
    if the_person.has_breeding_fetish: #Actively looking to get knocked up.
        if the_person.knows_pregnant:
            "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
            the_person "Oh, fuck that, darling... what's the point of fucking if you aren't going to fuck me raw? I need to feel you inside me, and I need it now."
            the_person "Come on, give me that cock, darling! I'm ready to take it all, and I want it all."
            "She takes a step closer to you, her body swaying slightly as she moves, her eyes locked on yours with a hungry, sultry intensity."

        elif the_person.is_infertile:
            "[the_person.possessive_title!c] raises an eyebrow, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
            the_person "Oh, fuck me already, darling! I'm infertile, so there's no risk, just pleasure... and I want it all."
            "She takes a step closer to you, her body swaying slightly as she moves, her eyes locked on yours with a hungry, sultry intensity."

        else:
            "[the_person.possessive_title!c] gazes up at you with a sultry, teasing expression, her voice barely above a whisper."
            the_person "Oh, fuck that, darling... what's the point of fucking if you aren't going to knock me up? I want to feel you inside me, and I want to know that there's a chance I'll get pregnant."
            the_person "Come on, preg me, darling! I'm ready to take the risk, and I want to feel you cum inside me."
            "She takes a step closer to you, her body swaying slightly as she moves, her eyes locked on yours with a hungry, sultry intensity."

    elif the_person.wants_creampie: #Just likes raw sex
        if the_person.is_infertile:
            "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
            the_person "Oh, fuck me already, darling! I'm infertile, so there's no risk, just pleasure... and I want it all."
            "She takes a step closer to you, her body swaying slightly as she moves, her eyes locked on yours with a hungry, sultry intensity."

        elif the_person.on_birth_control:
            "[the_person.possessive_title!c] raises an eyebrow, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
            the_person "Fuck that, darling... I'm on the pill! Fuck me raw, [the_person.mc_title], and cum inside me. I want to feel it all."
            the_person "Even better, you can fill me up, darling! I want to feel your cum inside me, and I want to know that it's all yours."
            $ the_person.update_birth_control_knowledge()
            "She winks, a flirtatious glint in her eye, as she takes a step closer to you, her body swaying slightly as she moves."

        else:
            "[the_person.possessive_title!c] gazes up at you with a sultry, teasing expression, her voice barely above a whisper."
            the_person "Fuck that, darling... they feel like shit, and I want to feel you cum inside me, not through some piece of rubber."
            the_person "So hurry up, darling... and get inside me! I'm ready to take it all, and I want it now."
            "She takes a step closer to you, her body swaying slightly as she moves, her eyes locked on yours with a hungry, sultry intensity."

    else:
        if the_person.is_infertile:
            "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
            the_person "Take me bareback, darling [the_person.mc_title]... that's how I want it, and that's how I need it."
            "She takes a step closer to you, her body swaying slightly as she moves, her eyes locked on yours with a hungry, sultry intensity."

        elif the_person.on_birth_control:
            "[the_person.possessive_title!c] raises an eyebrow, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
            the_person "Fuck that, darling... I'm on the pill! Take me bareback, [the_person.mc_title], that's how I want it!"
            the_person "I want to feel you inside me, darling... and I want to know that it's all yours."
            $ the_person.update_birth_control_knowledge()
            "She winks, a flirtatious glint in her eye, as she takes a step closer to you, her body swaying slightly as she moves."

        else:
            "[the_person.possessive_title!c] gazes up at you with a sultry, teasing expression, her voice barely above a whisper."
            the_person "Fuck that, darling... it feels so much better without one! Take me bareback, I can't wait any longer!"
            the_person "I want to feel you inside me, darling... and I want to know that it's all yours. I'm ready to take it all, and I want it now."
            "She takes a step closer to you, her body swaying slightly as she moves, her eyes locked on yours with a hungry, sultry intensity."
    return

label alluring_cum_face(the_person):
    if the_person.has_cum_fetish or the_person.obedience > 180:
        if the_person.has_cum_fetish or the_person.effective_sluttiness() > 60 or the_person.opinion.cum_facials > 0:
            "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
            the_person "What do you think, darling? Is this a good look for me? Do I look ravishing with your cum all over my face?"
            "[the_person.title] licks her lips, moving a few drops of your semen that had run down her face with her fingers to her mouth, her eyes locked on yours with a hungry, sultry intensity."
            "She smiles, a sly smile spreading across her face as she savors the taste of your cum."

        else:
            "[the_person.possessive_title!c] looks up at you with a shy, teasing expression, her voice barely above a whisper."
            the_person "I hope you had a good time, darling [the_person.mc_title]. It certainly seems like you did... and I'm glad I could be a part of it."
            "[the_person.title] runs a finger along her cheek, wiping away some of your semen, her eyes locked on yours with a soft, gentle intensity."
            "She smiles, a warm, inviting smile spreading across her face as she gazes up at you."

    else:
        if the_person.effective_sluttiness() > 80 or the_person.opinion.cum_facials > 0:
            "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
            the_person "Mmm, that's such a good feeling, darling... do you think I look cute like this? All covered in your cum?"
            "[the_person.title] runs her tongue along her lips, then smiles and laughs, her eyes sparkling with amusement."
            "She takes a step closer to you, her body swaying slightly as she moves, her eyes locked on yours with a hungry, sultry intensity."

        else:
            "[the_person.possessive_title!c] looks up at you with a sly, teasing expression, her voice barely above a whisper."
            the_person "Whew, glad you got that over with, darling... take a good look while it lasts, because I'm not sure I'm going to let you do that again anytime soon."
            "She smiles, a playful, mischievous smile spreading across her face as she gazes up at you, her eyes sparkling with amusement."
    return

label alluring_cum_mouth(the_person):
    if the_person.has_cum_fetish or the_person.obedience > 180:
        if the_person.has_cum_fetish or the_person.effective_sluttiness() > 60 or the_person.opinion.drinking_cum > 0:
            "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
            the_person "Mmm, thank you, darling [the_person.mc_title]... that was delicious. I love the way you taste."
            "She smiles, a sly smile spreading across her face as she savors the taste of your cum, her eyes locked on yours with a hungry, sultry intensity."

        else:
            "[the_person.title]'s face grimaces slightly as she tastes your cum in her mouth, but she quickly recovers, a sly smile spreading across her face."
            the_person "Ugh, darling... there, all taken care of [the_person.mc_title]. I hope that was satisfactory for you."
            "She looks up at you with a teasing expression, her eyes sparkling with amusement."

    else:
        if the_person.effective_sluttiness() > 80  or the_person.opinion.drinking_cum > 0:
            "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
            the_person "Mmm, you taste great, darling [the_person.mc_title]... was it nice to watch me take your load in my mouth? I hope you enjoyed the show."
            "She smiles, a sly smile spreading across her face as she savors the taste of your cum, her eyes locked on yours with a hungry, sultry intensity."

        else:
            "[the_person.title] looks up at you with a shy, teasing expression, her voice barely above a whisper."
            the_person "Ugh, darling... that's such a... unique taste. I'm not sure if I like it, but I'll do it for you, because I love the way you make me feel."
            "She smiles, a warm, inviting smile spreading across her face as she gazes up at you, her eyes sparkling with amusement."
    return

label alluring_cum_pullout(the_person):
    # Lead in: "I'm going to cum!"
    if mc.condom:
        if the_person.wants_creampie and not the_person.has_taboo("condomless_sex"): #TODO: FIgure out we want any more requirements for this to fire.
            if the_person.knows_pregnant:
                "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
                the_person "Oh, fuck... take that stupid condom off and cum in my pussy, darling! You already knocked me up, so who fucking cares? I just want you to fill me up!"
                "She moans desperately, her body trembling with desire."
            elif the_person.on_birth_control:
                "[the_person.possessive_title!c] raises an eyebrow, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
                the_person "Oh, fuck... I can't take it any more, take that condom off, darling [the_person.mc_title]!"
                "She moans desperately, her body trembling with desire."
                the_person "I give in, I want you to cum inside me, darling! I want to feel you fill me up!"
            else:
                "[the_person.possessive_title!c] gazes up at you with a sultry, teasing expression, her voice barely above a whisper."
                the_person "I can't... I can't think straight, darling! Fuck it! Take the condom off and cum inside me, darling [the_person.mc_title]!"
                $ the_person.update_birth_control_knowledge()
                the_person "I want you to get me pregnant and fuck my life up, darling! I want to be yours, completely and utterly."
            menu: #TODO: Add a variant of this normally so you can stealth a girl (don't do that in real life, it's super fucked up).
                "Take off the condom":
                    "You don't have much time to spare, darling. You pull out, barely clearing her pussy, and pull the condom off as quickly as you can manage."
                    $ mc.condom = False
                    $ use_condom = False  # prevent putting on a new condom next sex loop
                "Leave it on":
                    "You ignore [the_person.possessive_title]'s cum-drunk offer and keep the condom in place, darling."

        else:
            "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
            the_person "Fuck yeah, darling... I'm going to make you cum! I want to feel you explode inside me!"

    else:
        if the_person.wants_creampie:
            if the_person.knows_pregnant: #She's already knocked up, so who cares!
                "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
                the_person "Creampie me, darling [the_person.mc_title]... I want it all! Fill me up with your cum and make me scream with pleasure!"

            elif the_person.opinion.creampies > 0:
                "[the_person.possessive_title!c] moans happily, her body trembling with desire."
                if the_person.on_birth_control: #She just likes creampies.
                    the_person "Fuck yeah, fill me up with your cum, darling [the_person.mc_title]! Creampie me and make me scream with pleasure!"
                else: #Yeah, she's not on BC and asking for you to creampie her. She's looking to get pregnant.
                    $ the_person.update_birth_control_knowledge()
                    the_person "Oh, fuck... cum inside me and knock me up, darling [the_person.mc_title]! I want you to breed me like a slut and make me yours!"

            elif the_person.is_infertile:
                "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
                the_person "Cum wherever you want, darling [the_person.mc_title]... I'm infertile, so there's no risk, just pleasure!"

            elif the_person.on_birth_control: #She's on the pill, so she's probably fine
                $ the_person.update_birth_control_knowledge()
                the_person "Cum wherever you want, darling [the_person.mc_title]... I'm on the pill, so don't worry about it!"

            else: #Too distracted to care about getting pregnant or not. Oh well, what could go wrong?
                the_person "Do it, darling! Cum! I want to feel you explode inside me and make me scream with pleasure!"

        else:
            if the_person.is_infertile:
                "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
                the_person "Just pull out, darling... I don't want your cum inside me, but I do want to feel you cum all over me!"

            elif not the_person.on_birth_control: #You need to pull out, I'm not on the pill!
                $ the_person.update_birth_control_knowledge()
                the_person "Fuck, pull out, darling! I'm not on the pill, and I don't want to get pregnant... yet!"

            elif the_person.opinion.creampies < 0:
                the_person "Pull out, darling... I don't want you to cum in me, but I do want to feel you cum all over me!"

            else:
                "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
                the_person "Hell yeah, pull out and cum all over me, darling! I want to feel your cum on my skin and know that you're all mine!"
    return

label alluring_cum_condom(the_person):
    if the_person.effective_sluttiness() > 75 or the_person.opinion.creampies > 0:
        "[the_person.possessive_title!c] gazes up at you with a sultry, teasing expression, her voice barely above a whisper."
        the_person "Oh, god, darling... it's so warm. If your condom broke, it would all be inside me, and I'm not sure I'd mind that one bit."
        "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."

    else:
        "[the_person.possessive_title!c] raises an eyebrow, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
        the_person "Oh, god, darling... I hope you buy good condoms, because that's a lot of cum, and I'm not sure I'm ready for that kind of surprise."
        the_person "But then again, maybe you're dreaming of knocking me up, darling... and maybe I'm dreaming of it too."
        "She winks, a flirtatious glint in her eye, as she takes a step closer to you, her body swaying slightly as she moves."
    return

label alluring_cum_vagina(the_person):
    if the_person.has_taboo("creampie"):
        $ the_person.call_dialogue("creampie_taboo_break")
        $ the_person.break_taboo("creampie")
        return

    if the_person.wants_creampie:
        if the_person.knows_pregnant:
            "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
            the_person "It's no wonder I got knocked up, darling... I just love feeling your cum inside me so much! It's like my body was made for you."

        elif the_person.is_infertile:
            "[the_person.possessive_title!c] raises an eyebrow, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
            the_person "Fuck yes, pump that hot cum into me, darling! I want to feel it all inside me, and I want to know that it's all yours."

        elif the_person.on_birth_control:
            if the_person.has_significant_other:
                "[the_person.possessive_title!c] gazes up at you with a sultry, teasing expression, her voice barely above a whisper."
                the_person "Oh, fuck, wow, darling! My [the_person.so_title] never cums like that... there's so much of it, and I love every drop."
            else:
                if the_person.knows_pregnant:
                    the_person "Oh, fuck, that's a lot of cum, darling... good thing I'm already pregnant, because I don't think you're firing blanks, hmm?"
                elif the_person.is_infertile:
                    the_person "Oh, fuck, that's a lot of cum, darling... I'll be dripping your cum all day long, and I love the thought of it."
                else:
                    the_person "Oh, fuck, that's a lot of cum, darling... good thing I'm on the pill, because I don't think you're firing blanks, hmm?"
                $ the_person.update_birth_control_knowledge()

        elif the_person.effective_sluttiness() > 75 or the_person.opinion.creampies > 0:
            if the_person.has_significant_other:
                "[the_person.possessive_title!c] raises an eyebrow, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
                the_person "Fuck yes, pump that cum into me, darling! I don't care if I get pregnant... I'll just tell my [the_person.so_title] that it's his, and he'll never know the difference."

            else:
                the_person "Mmm, give me that baby batter, darling... pump my pussy full of it! I'll worry about being pregnant later, but for now, I just want to feel you inside me."
        else:
            if the_person.has_significant_other:
                the_person "Oh, fuck, you really filled me up, darling... you're going to send me home to my [the_person.so_title] knocked up, aren't you?"

            else:
                the_person "That was such a big load, darling... you're trying your best to knock me up, and I love the thought of it!"

    else: #She's angry
        if the_person.knows_pregnant:
            the_person "Hey, I told you to pull out, darling... well, I guess it's okay, since I'm already pregnant, but still, be more careful next time, hmm?"

        elif not the_person.on_birth_control:
            if the_person.has_significant_other:
                the_person "Oh, fuck, [the_person.mc_title], why didn’t you pull out? My [the_person.so_title] would kill me if he found out I got pregnant."
                if the_person.kids > 0:
                    the_person "... Again."
            else:
                the_person "Oh, fuck, I said to pull out, darling! I'm not on the pill, [the_person.mc_title], what happens if I get pregnant? You need to be more careful with me."
                $ the_person.update_birth_control_knowledge()
                the_person "Whatever, I guess it's already happened... maybe next time I should make you wear a condom, hmm?"

        elif the_person.is_infertile:
            the_person "Hey, I told you to pull out, darling... now look at what a mess you've made... what a fucking mess, and all for nothing, since I'm infertile anyway."

        elif the_person.has_significant_other:
            the_person "Hey, I said to pull out, darling! I have a [the_person.so_title], even if I'm on the pill, you shouldn't be creampieing me... it's not right."
            $ the_person.update_birth_control_knowledge()
            the_person "I don't want to have to make you wear a condom, darling... so be a little more careful next time, hmm?"

        elif the_person.opinion.creampies < 0:
            the_person "Hey, I told you to pull out, darling... now look at what a mess you've made... it feels like it's everywhere, and I hate it."

        else:
            the_person "I told you to pull out, darling... did you get a little too excited? Don't make a habit of it, otherwise I'll make you start wearing a condom again, and I don't think you want that, hmm?"
            the_person "Just be more careful next time, darling... I want to feel you inside me, but I also want to be safe, and I want to be in control."
    return

label alluring_cum_anal(the_person):
    if the_person.has_taboo("anal creampie"):
        $ the_person.call_dialogue("anal_creampie_taboo_break")
        $ the_person.break_taboo("anal creampie")
        return

    if the_person.sluttiness > 75 or the_person.opinion.anal_creampies > 0:
        "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
        the_person "Mmm, pump my ass full of your hot cum, darling! I want to feel it all inside me, and I want to know that it's all yours."
        "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."

    elif the_person.opinion.anal_creampies < 0:
        "[the_person.possessive_title!c] looks up at you with a shy, nervous expression, her voice barely above a whisper."
        the_person "Oh, fuck... cover my ass, darling... not inside, please. I don't think I can handle it."
        "She glances down, her eyes avoiding yours as she speaks, her voice trembling slightly."

    else:
        "[the_person.possessive_title!c] gazes up at you with a sultry, teasing expression, her voice barely above a whisper."
        the_person "Oh, fuck... fill me up, darling... oh, fuck! I don't know if I can take it, but I want to try."
        "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity, her eyes sparkling with excitement."
    return

label alluring_surprised_exclaim(the_person):
    $rando = renpy.random.choice(["Darling, oh my!","Fuck, darling!","Shit, I didn't expect that!","Oh, darling, you're a naughty one!","Ah, darling! Oh, the surprise!", "Mmm, what a pleasant surprise!", "Fucking hell, darling!", "Holy shit, darling!", "Fucking amazing!", "God, darling, you're incredible!", "Son of a... wow!", "Mother... darling, you're so bad!", "Whoah, darling!"])
    "[the_person.possessive_title!c] gazes up at you with a sultry, surprised expression, her voice barely above a whisper."
    the_person "[rando]"
    "She raises an eyebrow, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
    return

label alluring_talk_busy(the_person):
    if the_person.obedience > 120:
        "[the_person.possessive_title!c] gazes up at you with a sultry, apologetic expression, her voice barely above a whisper."
        the_person "I've got a ton of things I need to get to, darling [the_person.mc_title]... could we talk some other time? I promise I'll make it worth your while."
        "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."

    else:
        "[the_person.possessive_title!c] looks up at you with a playful, teasing expression, her voice barely above a whisper."
        the_person "Hey, darling... I'd love to chat, but I have a million things to get done right now. Maybe later, hmm? I promise I'll be worth the wait."
        "She winks, a flirtatious glint in her eye, as she takes a step closer to you, her body swaying slightly as she moves."
    return

### DIALOGUE ###
label alluring_sex_strip(the_person):
    if the_person.sluttiness < 20:
        if the_person.arousal_perc < 50:
            "[the_person.possessive_title!c] looks up at you with a shy, teasing expression, her voice barely above a whisper."
            the_person "One sec, darling... I want to take something off. Just to make things a little more... interesting."
            "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."

        else:
            "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
            the_person "Ah, I'm wearing way too much right now, darling... one sec! I want to show you what's underneath."
            "She winks, a flirtatious glint in her eye, as she takes a step closer to you, her body swaying slightly as she moves."

    elif the_person.sluttiness < 60:
        if the_person.arousal_perc < 50:
            "[the_person.possessive_title!c] raises an eyebrow, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
            the_person "Why do I bother wearing all this, darling? It's just going to get in the way of what we really want."
            "She takes a step closer to you, her body swaying slightly as she moves, her eyes locked on yours with a hungry, sultry intensity."

        else:
            "[the_person.possessive_title!c] looks up at you with a playful, teasing expression, her voice barely above a whisper."
            the_person "Wait, darling... I want to get a little more naked for you. Just to make things a little more... exciting."
            "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."

    else:
        if the_person.arousal_perc < 50:
            "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
            the_person "Give me a second, darling... I'm going to strip something off just. For. You. Because I want to show you what's underneath, and I want to make you want me."
            "She winks, a flirtatious glint in her eye, as she takes a step closer to you, her body swaying slightly as she moves."

        else:
            "[the_person.possessive_title!c] raises an eyebrow, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
            the_person "Ugh, let me get this off, darling... I want to feel you pressed against every inch of me! I want to feel your skin on mine, and I want to know that you're all mine."
            "She takes a step closer to you, her body swaying slightly as she moves, her eyes locked on yours with a hungry, sultry intensity."
    return

label alluring_sex_watch(the_person, the_sex_person, the_position):
    $ title = the_person.title if not the_person.is_stranger else "The stranger"
    if the_person.sluttiness < the_position.slut_requirement - 20:
        $ the_person.draw_person(emotion = "angry", display_transform = character_left_flipped)
        the_person "Ugh, why don't you two get a room or something, nobody wants to see this... or do they, hmm?"
        $ the_person.change_stats(obedience = -2, happiness = -1)
        "[title] looks away, trying to hide a hint of curiosity, while you and [the_sex_person.fname] [the_position.verb]."
        return False

    if the_person.sluttiness < the_position.slut_requirement - 10:
        $ the_person.draw_person(display_transform = character_left_flipped)
        the_person "Could you two at least keep it down, darling? This is fucking ridiculous... but I have to admit, it's also kind of intriguing."
        $ the_person.change_happiness(-1)
        "[title] tries to avert her gaze, but can't help sneaking a peek, while you and [the_sex_person.fname] [the_position.verb]."
        return False

    if the_person.sluttiness < the_position.slut_requirement:
        $ the_person.draw_person(display_transform = character_left_flipped)
        if not is_watching(the_person):
            the_person "You're certainly feeling bold today, [the_sex_person.fname]... and I have to admit, it's kind of turning me on."
        $ the_person.change_slut(1, 30)
        "[title] watches with growing interest while you and [the_sex_person.fname] keep [the_position.verbing]."
        return True

    if the_person.sluttiness >= the_position.slut_requirement and the_person.sluttiness < the_position.slut_cap:
        $ the_person.draw_person(display_transform = character_left_flipped)
        if not is_watching(the_person):
            the_person "Oh, wow, darling... that's hot. You don't mind if I watch, do you? I promise I'll be a good girl... or not."
        $ the_person.change_slut(1, 50)
        "[title] watches with increasing arousal while you and [the_sex_person.fname] [the_position.verb]."
        return True

    $ the_person.draw_person(emotion = "happy", display_transform = character_left_flipped)
    if renpy.random.randint(0, 1) == 0:
        the_person "Come on, darling [the_person.mc_title]... [the_sex_person.fname] is going to fall asleep at this rate! You're going to have to give her a little more than that, hmm?"
    else:
        call watcher_position_comment(the_person, the_sex_person, the_position) from _call_watcher_position_comment_alluring_sex_watch
    "[title] watches eagerly, her eyes fixed on the action, while you and [the_sex_person.fname] [the_position.verb]."
    return True

label alluring_being_watched(the_person, the_watcher, the_position):
    $ title = the_watcher.fname if not the_watcher.is_stranger else "the stranger"
    if the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #They agree you should give it to her harder
        "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
        the_person "Come on, darling [the_person.mc_title]... be rough with me. I can handle it, and I want to feel you inside me, deep and hard."
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [title] watching you and her [the_position.verb], and she's loving every minute of it."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's super slutty and doesn't care what people think.
        "[the_person.possessive_title!c] raises an eyebrow, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
        the_person "I bet she just wishes she was the one being [the_position.verb]ed by you, darling... but she's too shy to admit it."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #She's super slutty and encourages the watcher to be slutty.
        "[the_person.possessive_title!c] looks over at [title] with a sultry, inviting expression, her voice barely above a whisper."
        the_person "Oh, god, darling [title]... you need to get a little of this yourself. Come and join us, and let's make it a party!"
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [title] watching you and her [the_position.verb], and she's eager to share the experience."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #She's into it and encouraged by the slut watching her.
        "[the_person.possessive_title!c] responds to [title], her voice barely above a whisper."
        the_person "I'm giving him all I can right now, darling [title]... any more and he's going to break me, but I love the way it feels."
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [title] watching you and her [the_position.verb], and she's feeding off the energy."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's into it but shamed by the prude watching her.
        "[the_person.possessive_title!c] looks up at you with a shy, nervous expression, her voice barely above a whisper."
        the_person "Fuck, maybe we should go somewhere a little quieter, darling... I don't think [title] is comfortable with this."
        $ the_person.change_stats(arousal = -1, slut = -1)
        "[the_person.title] seems uncomfortable with [title] nearby, and she's starting to feel a little self-conscious."

    else: #the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #They're both into it but not fanatical about it.
        "[the_person.possessive_title!c] looks directly at [title] with a sultry, teasing expression, her voice barely above a whisper."
        the_person "Ah, now this is a party, darling! Maybe when he's done, you can tap in and take a turn... if you're feeling brave, that is."
        $ the_person.change_stats(arousal = 1, slut = 1, max_slut = 30)
        "[the_person.title] seems more comfortable [the_position.verbing] you with [title] around, and she's starting to get into the swing of things."
    return

label alluring_work_enter_greeting(the_person):
    if the_person.happiness < 80 or the_person.love < 0:
        "[the_person.possessive_title!c] glances up at you when you enter the room, her eyes narrowing slightly as she takes in your presence."
        "She scoffs, a hint of disdain in her voice, and turns back to her work, dismissing you."

    elif the_person.happiness > 130:
        if the_person.sluttiness > 40:
            "[the_person.possessive_title!c] looks up from her work, a sultry, confident expression spreading across her face as she gazes up at you."
            the_person "Hey, darling [the_person.mc_title]... down here for business or pleasure? I'm hoping it's the latter, hmm?"
            "The smile she gives you tells you which one she's hoping for, and it's clear she's in the mood for something more... personal."

        else:
            "[the_person.possessive_title!c] looks up from her work, a warm, inviting smile spreading across her face as she gazes up at you."
            the_person "Hey, darling [the_person.mc_title]... it's nice to have you stop by. Let me know if you need anything, and I'll do my best to help you out."
            "She leans forward, her eyes sparkling with interest, as she waits for your response."

    else:
        if the_person.sluttiness > 60:
            $ the_person.draw_person(position = "stand4")
            "[the_person.possessive_title!c] walks over to you when you come into the room, her hips swaying seductively as she moves."
            the_person "Just the person I was hoping would stop by, darling... I'm here if you need anything, and I mean anything."
            "She winks, a flirtatious glint in her eye, as she slides a hand down your chest, stomach, and finally your crotch, her touch sending shivers down your spine."
            the_person "Anything at all, darling... just let me know what you need, and I'll take care of it for you."

        else:
            "[the_person.possessive_title!c] looks up from her work, a friendly, approachable expression on her face as she gazes up at you."
            the_person "Hey, darling [the_person.mc_title]... need anything? I'm here to help, and I want to make sure you're taken care of."
    return

label alluring_date_seduction(the_person):
    if the_person.is_girlfriend:
        "[the_person.possessive_title!c] grabs your hand and pulls you around to look at her, her eyes sparkling with desire."
        the_person "Hey, darling... that was such a great time. So I was thinking..."
        $ mc.change_locked_clarity(30)
        if the_person.effective_sluttiness(["vaginal_sex", "condomless_sex"]) > 60 and the_person.wants_creampie and the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex >= 0 and the_person.opinion.creampies >= 0 and not the_person.on_birth_control and not the_person.knows_pregnant:
            if the_person.opinion.creampies > 0: #No condoms, loves creampies, she's basically asking you to knock her up. So... have her ask you to knock her up!
                the_person "Let's go back to my place and fuck until you knock me up, darling... I want to feel your cum inside me, and I want to know that I'm all yours."
                the_person "Don't you think I'd look good with huge mommy-tits, hmm? You can make it happen, darling."
            else:
                the_person "Let's go back to my place, darling... I want you to throw me on the bed and fuck me bareback. I want to feel your cock inside me, and I want to know that it's all yours."
                the_person "You can even cum inside me if you want, darling... I just want you to fuck me up with your cock, and make me scream with pleasure."

        elif the_person.effective_sluttiness(["vaginal_sex", "condomless_sex"]) > 60 and the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex > 0:
            the_person "Let's go back to my place, darling... you can fuck me any way you want, as long as you follow my one simple rule: No condoms."
            the_person "It feels so much better getting fucked bareback, darling... I just can't do it any other way, and I want to feel your cock inside me, skin to skin."

        elif the_person.effective_sluttiness(["vaginal_sex"]) > 50 and the_person.opinion.vaginal_sex > 0:
            the_person "Let's go back to my place, alright, darling? I want to get my little pussy pounded, and you're the guy for the job."
            the_person "Do you think you can do that, darling? Can you come fuck me up with that big cock of yours, and make me scream with pleasure?"

        elif the_person.effective_sluttiness(["anal_sex"]) > 60 and the_person.opinion.anal_sex > 0:
            the_person "Let's go back to my place, alright, darling? I want to get my ass stretched out tonight, and you've got the cock that I love."
            the_person "Doesn't that sound like a fun way to end our night together, darling? Just the two of us, and your cock in my ass."

        elif the_person.effective_sluttiness(["sucking_cock"]) > 40 and the_person.opinion.giving_blowjobs > 0:
            the_person "Let's go back to my place, darling... I want to reward you for giving me such a wonderful night."
            the_person "How does a nice long, sloppy blowjob sound, hmm? I think it sounds pretty fun, and I want to taste your cum in my mouth."

        elif the_person.effective_sluttiness() > 40 and the_person.opinion.being_covered_in_cum > 0:
            the_person "Let's go back to my place, darling... we can have some fun, and I can end this night in my favourite way..."
            "She licks her lips playfully, her eyes sparkling with desire."
            the_person "Covered in your hot cum, darling... sound like fun to you, hmm?"

        elif the_person.effective_sluttiness(["touching_body"]) > 40 and the_person.opinion.giving_tit_fucks > 0 and the_person.has_large_tits:
            the_person "Let's go back to my place, then I can repay you for this wonderful night, darling."
            the_person "I'll slide that big cock of yours between my tits and fuck it until you cum, hmm? How does that sound, darling?"

        else: #She's not very slutty, so she leaves the invitation open to interpretation
            the_person "It doesn't have to be over yet, does it, darling? Let's go back to my place and we can keep the fun going, hmm?"
            "She bites her lower lip playfully, her eyes sparkling with desire."

    elif the_person.is_affair:
        the_person "So my [the_person.so_title] won't be home tonight, darling... I was thinking..."
        "She reaches down and cups your crotch, rubbing it gently through your pants, her eyes locked on yours with a hungry, sultry intensity."
        $ mc.change_locked_clarity(40)
        if the_person.wants_creampie and the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex >= 0 and the_person.opinion.creampies >= 0 and not the_person.on_birth_control and not the_person.knows_pregnant:
            if the_person.opinion.creampies > 0: #No condoms, loves creampies, she's basically asking you to knock her up. So... have her ask you to knock her up!
                the_person "Let's go back to my place so you can pin me to the bed and creampie me all night long, darling... I want to feel your cum inside me, and I want to know that I'm all yours."
                the_person "All that cum in my unprotected pussy and I'm sure to get knocked up, darling... just thinking about it is making me wet!"

            else:
                the_person "Let's go back to my place, darling... you can pin me to the bed and fuck me bareback all night long. I want to feel your cock inside me, and I want to know that it's all yours."
                the_person "Cum inside me, over my face, whatever, darling... I just want you to fuck me up with your cock, and make me scream with pleasure."

        elif the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex > 0:
            the_person "Let's go back to my place, darling... you can fuck me all night, any way you want, as long as you follow one simple rule: No condoms."
            the_person "If you're fucking me, you're doing it bareback, darling... I want to feel your cock inside me, skin to skin, and I want to know that it's all yours."

        elif the_person.opinion.vaginal_sex > 0:
            the_person "Let's go back to my place and you can pound my tight fucking pussy until I'm just a quivering, cum-covered wreck, darling."
            the_person "How does that sound, hmm? Do I have your attention, darling?"

        elif the_person.opinion.anal_sex > 0:
            the_person "Let's go back to my place so you can stretch out my tight little asshole with that monster cock of yours, darling."
            the_person "I want to feel your cock in my ass, and I want to know that it's all yours, darling."

        elif the_person.opinion.giving_blowjobs > 0:
            the_person "Let's go back to my place, and you can choke me out on that monster cock of yours, darling."
            the_person "I want to throat it so fucking deep, darling... I want to feel your balls against my chin when you cum, and I want to taste your cum in my mouth."

        elif the_person.opinion.being_covered_in_cum > 0:
            the_person "Let's go back to my place, and you can spend all night glazing me like a slutty donut, darling."
            the_person "I want to be absolutely covered in your sperm, head to toe, darling... sound like fun to you, hmm?"

        elif the_person.opinion.giving_tit_fucks > 0 and the_person.has_large_tits:
            the_person "Let's go back to my place so I can wrap these big fucking tits around your big fucking cock, darling."
            the_person "Then I'll fuck that thing until you explode, darling... sound like fun to you, hmm?"

        elif the_person.opinion.cheating_on_men > 0:
            the_person "Let's go back to my place, and you can do all the fucked up things I tell my husband I hate, darling."
            the_person "He tries to treat me like a lady, but all I want to be is your cock drunk slut, darling."

        else:
            the_person "Let's go back to my place and make him really regret leaving me alone for the night, darling."
            the_person "I want to feel your cock inside me, and I want to know that it's all yours, darling."

    elif not the_person.has_significant_other:
        $ mc.change_locked_clarity(20)
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                the_person "I've had a blast, darling [the_person.mc_title]... but there are a few more things I'd like to do with you. Want to come back to my place and find out what they are, hmm?"
                the_person "I promise it will be worth your while, darling... I want to feel your cock inside me, and I want to know that it's all yours."

            else:
                the_person "You've been a blast, darling [the_person.mc_title]... want to come back to my place, have a few drinks, and see where things lead, hmm?"
                the_person "I want to get to know you better, darling... and I want to feel your cock inside me, skin to skin."

        else:
            if the_person.love > 40:
                the_person "Tonight's been amazing, darling [the_person.mc_title]... I just don't want to say goodbye, hmm?"
                the_person "Do you want to come back to my place and have a few drinks, darling? I want to spend more time with you, and I want to feel your cock inside me."

            else:
                the_person "This might be crazy, darling... but I had a great time tonight, and you make me a little crazy, hmm?"
                the_person "Do you want to come back to my place and see where things go, darling? I want to feel your cock inside me, and I want to know that it's all yours."

    else:
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                $ mc.change_locked_clarity(20)
                the_person "I've had a blast, darling [the_person.mc_title]... but I'm not done with you yet, hmm?"
                the_person "Want to come back to my place, darling? My [the_person.so_title] won't be home until morning, so we would have plenty of time to play."

            else:
                $ mc.change_locked_clarity(20)
                the_person "This might be crazy, darling... but do you want to come back to have another drink with me, hmm?"
                the_person "My [the_person.so_title] is stuck at work, and I don't want to be left all alone, darling... I want to feel your cock inside me, and I want to know that it's all yours."

        else:
            if the_person.love > 40:
                $ mc.change_locked_clarity(20)
                the_person "You're making me feel crazy, darling [the_person.mc_title]... do you want to come have a drink at my place, hmm?"
                the_person "My [the_person.so_title] won't be home until morning, and we have a big bed you could help me warm up, darling... I want to feel your cock inside me, and I want to know that it's all yours."

            else:
                $ mc.change_locked_clarity(20)
                the_person "This is crazy, darling... but would you want to have one last drink at my place, hmm?"
                the_person "My [the_person.so_title] won't be home until morning, and I want to spend more time with you, darling... I want to feel your cock inside me, and I want to know that it's all yours."
    return

label alluring_sex_end_early(the_person):
    if the_person.sluttiness > 50:
        if the_person.love > 40:
            if the_person.arousal_perc > 60:
                "[the_person.possessive_title!c] gazes up at you with a sultry, disappointed expression, her voice barely above a whisper."
                the_person "You're really done, darling? Fuck [the_person.mc_title], I'm still so horny... I was hoping for a little more, hmm?"
                "She pouts, her lips curling into a sultry, inviting smile as she gazes up at you with a brazen, seductive intensity."

            else:
                "[the_person.possessive_title!c] raises an eyebrow, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
                the_person "That's all you wanted, darling? I was prepared to do so much more to you... and I was hoping you'd do more to me, hmm?"
                "She winks, a flirtatious glint in her eye, as she takes a step closer to you, her body swaying slightly as she moves."

        else:
            if the_person.arousal_perc > 60:
                "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
                the_person "Fuck, I'm so horny, darling... you're sure you're finished? I was just getting started, hmm?"
                "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."

            else:
                "[the_person.possessive_title!c] looks up at you with a playful, teasing expression, her voice barely above a whisper."
                the_person "That was a little bit of fun, I suppose, darling... but I was hoping for more, hmm?"
                "She pouts, her lips curling into a sultry, inviting smile as she gazes up at you with a brazen, seductive intensity."

    else:
        if the_person.love > 40:
            if the_person.arousal_perc > 60:
                "[the_person.possessive_title!c] gazes up at you with a shy, nervous expression, her voice barely above a whisper."
                the_person "[the_person.mc_title], you got me so turned on, darling... I didn't expect that, hmm?"
                "She blushes, her cheeks flushing with excitement as she gazes up at you with a soft, gentle intensity."

            else:
                "[the_person.possessive_title!c] looks up at you with a warm, inviting smile, her voice barely above a whisper."
                the_person "I hope you had a good time, darling... I wanted to make sure you were satisfied, hmm?"
                "She smiles, a gentle, loving smile as she gazes up at you with a soft, gentle intensity."

        else:
            if the_person.arousal_perc > 60:
                "[the_person.possessive_title!c] gazes up at you with a sultry, surprised expression, her voice barely above a whisper."
                the_person "Oh, god, that was intense, darling... I didn't expect it to be so... good, hmm?"
                "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."

            else:
                "[the_person.possessive_title!c] looks up at you with a playful, teasing expression, her voice barely above a whisper."
                the_person "Done? Good, nice and quick, darling... just the way I like it, hmm?"
                "She winks, a flirtatious glint in her eye, as she takes a step closer to you, her body swaying slightly as she moves."
    return

label alluring_sex_take_control(the_person):
    if the_person.arousal_perc > 60:
        "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
        the_person "Oh, hell no, darling... you can't just get me wet and then walk away! I'm not done with you yet, hmm?"
        "She reaches out and grabs your arm, pulling you back towards her with a sly, seductive smile."

    else:
        "[the_person.possessive_title!c] looks up at you with a playful, teasing expression, her voice barely above a whisper."
        the_person "Are you getting bored already, darling? Get back here, we aren't done yet! I've just gotten started, hmm?"
        "She winks, a flirtatious glint in her eye, as she takes a step closer to you, her body swaying slightly as she moves."
    return

label alluring_sex_beg_finish(the_person):
    "[the_person.possessive_title!c] gazes up at you with a sultry, desperate expression, her voice barely above a whisper."
    the_person "Wait, darling [the_person.mc_title]... I'm going to cum soon, and I just really need this... I'll do anything for you, just let me cum, hmm?"
    "She arches her back, her body trembling with anticipation as she begs for release, her eyes locked on yours with a hungry, sultry intensity."
    "Her voice drops to a whisper, her words dripping with desire as she pleads with you to let her cum."
    return

### DIALOGUE ###
label alluring_sex_review(the_person, the_report):
    $ comment_position = the_person.pick_position_comment(the_report)
    if comment_position is None:
        return #You didn't actually do anything, no need to comment.

    $ used_obedience = the_report.get("obedience_used", False) #True if a girl only tried a position because you ordered her to.
    $ the_person.draw_person()  # make sure she stands up for talking with you

    #She's worried about her SO finding out because it was in public
    if the_report.get("was_public", False) and the_person.has_significant_other and the_person.opinion.cheating_on_men <= 0: #It was public and she cares.
        if the_person.is_affair: #Dialogue about her being into it, but you can't do this in case she gets caught.
            "[the_person.possessive_title!c] gazes up at you with a sultry, worried expression, her voice barely above a whisper."
            the_person "Whew, that got a little crazy, darling! We, uh, should probably be more careful next time though, okay?"
            the_person "Somebody might tip off my [the_person.so_title], and this whole thing is going to be hard to explain, hmm?"
            "She bites her lower lip, her eyes locked on yours with a hungry, sultry intensity."

        elif used_obedience:
            "[the_person.possessive_title!c] looks up at you with a shy, nervous expression, her voice barely above a whisper."
            the_person "Everyone is watching... Fuck, what if someone tells my [the_person.so_title], darling?"
            mc.name "Don't worry, nobody really cares what we're doing, darling. They aren't going to tell your [the_person.so_title]."
            the_person "I hope you're right, this is going to be really hard to explain, hmm?"

        else:
            $ the_person.call_dialogue("surprised_exclaim")
            "[the_person.possessive_title!c] gazes up at you with a sultry, surprised expression, her voice barely above a whisper."
            the_person "Everyone's watching us, darling... I hope my [the_person.so_title] doesn't hear about this, hmm?"
            mc.name "Don't worry, nobody here really cares what we do together, darling. Nobody's going to tell him."
            the_person "I hope you're right, this would be really hard to explain, hmm?"

    #She's single, but worried that you did in public.
    elif the_report.get("was_public", False) and (the_person.effective_sluttiness()+10*the_person.opinion.public_sex < comment_position.slut_cap):
        if used_obedience:
            "[the_person.possessive_title!c] looks up at you with a shy, nervous expression, her voice barely above a whisper."
            the_person "Fuck, everyone is watching us, darling [the_person.mc_title]."
            the_person "They're all going to think I'm some sort of huge slut after this, hmm?"
            "She blushes, her cheeks flushing with excitement as she gazes up at you with a soft, gentle intensity."

        else:
            "[the_person.possessive_title!c] gazes up at you with a sultry, worried expression, her voice barely above a whisper."
            the_person "Oh fuck, everyone's watching us, darling [the_person.mc_title]."
            mc.name "Don't worry, nobody really cares what we're doing, darling."
            the_person "I hope you're right, or I'm going to end up with a reputation for this sort of thing, hmm?"

    elif the_report.get("girl orgasms", 0) > 2:
        if used_obedience:
            "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
            the_person "Oh fuck... baby... I loved what you did to me, darling."
            mc.name "I do enjoy when you keep begging me to make you cum again, darling."
            "[the_person.possessive_title!c] smiles at you, her eyes sparkling with desire as she gazes up at you with a brazen, seductive intensity."

        else:
            "[the_person.possessive_title!c] looks up at you with a shy, nervous expression, her voice barely above a whisper."
            the_person "I have never... cum that hard, darling... It was just amazing, hmm?"
            "She seems dazed by her orgasm as she tries to form coherent sentences, her eyes locked on yours with a hungry, sultry intensity."
            the_person "You really... know how to give a girl a good time, darling... just gimme a second, hmm?"

        call sex_review_trance(the_person) from _call_sex_review_trance_alluring_sex_review

    #No special conditions, just respond based on how orgasmed and how slutty the position was.
    elif the_report.get("girl orgasms", 0) > 0 and the_report.get("guy orgasms", 0) > 0: #You both came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position cap, it was tame
            "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
            the_person "Ah, that was fucking nice, darling... But I think we could go even further next time, hmm?"
            the_person "Doesn't that sound like fun, darling? I'm getting wet just thinking about it, hmm?"
            "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            "[the_person.possessive_title!c] looks up at you with a playful, teasing expression, her voice barely above a whisper."
            the_person "Ah, that was just what I needed, darling! I think we're very compatible, [the_person.mc_title]."
            the_person "Let's do it again some time soon, okay, darling? I promise it will be worth your while, hmm?"
            "She winks, a flirtatious glint in her eye, as she takes a step closer to you, her body swaying slightly as she moves."

        elif used_obedience: #She only did it because she was commanded
            "[the_person.possessive_title!c] looks up at you with a shy, nervous expression, her voice barely above a whisper."
            the_person "Fuck, I... I didn't think I was going to cum like that, darling."
            mc.name "Aren't you going to thank me, darling? You obviously had a good time, hmm?"
            "She rolls her eyes and looks away, trying to hide her embarrassment, but a hint of a smile plays on her lips."

        else: # She's surprised she even tried that.
            "[the_person.possessive_title!c] gazes up at you with a sultry, surprised expression, her voice barely above a whisper."
            the_person "Oh fuck, that was intense, darling! I didn't think I was going to take it so far, but it just felt right, you know, hmm?"
            the_person "Don't think that's going to happen every time though, alright, darling? I'm not a slut, hmm?"
            "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."

    elif the_report.get("girl orgasms", 0) > 0: #Only she came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
            the_person "Done already, darling? Well, that's just not right, hmm? Next time I'm going to make sure we both cum, hmm?"
            the_person "I've got a few ideas that are going to blow you away, darling... just you wait and see, hmm?"
            "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            "[the_person.possessive_title!c] looks up at you with a playful, teasing expression, her voice barely above a whisper."
            the_person "You're all done, darling? Well, that was fucking hot either way, hmm?"
            the_person "I'll repay the favour next time, alright, darling? I promise it will be worth your while, hmm?"
            "She winks, a flirtatious glint in her eye, as she takes a step closer to you, her body swaying slightly as she moves."

        elif used_obedience: #She only did it because she was commanded
            "[the_person.possessive_title!c] looks up at you with a shy, nervous expression, her voice barely above a whisper."
            the_person "That's it, darling? I mean, not like I wanted to do anything more, I just thought you were going to finish, hmm?"
            mc.name "Some other time, darling. I just wanted to see what you look like when you cum, hmm?"
            the_person "I... Fuck, well, I guess you got what you wanted, darling."
            the_person "It could have been worse, I guess, hmm?"

        else: # She's surprised she even tried that.
            "[the_person.possessive_title!c] gazes up at you with a sultry, surprised expression, her voice barely above a whisper."
            the_person "Oh fuck, that was intense, darling! You really know how to make a girl feel good, hmm?"
            the_person "You're probably tired after all that work, darling... I promise I'll repay the favour next time, okay, hmm?"
            "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."

    elif the_report.get("guy orgasms", 0) > 0: #Only you came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
            the_person "All tired out, darling? Well, that's a little disappointing, hmm?"
            mc.name "Sorry, darling. I'll make it up to you next time, hmm?"
            the_person "You better, darling. I've got some ideas that should have both of us cumming our brains out, hmm?"
            "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            "[the_person.possessive_title!c] looks up at you with a playful, teasing expression, her voice barely above a whisper."
            the_person "Tired out already, darling? Well someone's being a little selfish today, hmm?"
            mc.name "Sorry, darling. I'll make it up to you next time, hmm?"
            the_person "You better, darling... or you won't get many more \"next times\", hmm?"
            "She winks, a flirtatious glint in her eye, as she takes a step closer to you, her body swaying slightly as she moves."

        elif used_obedience: #She only did it because she was commanded
            "[the_person.possessive_title!c] looks up at you with a shy, nervous expression, her voice barely above a whisper."
            the_person "I expect you're tired after all of that, darling. We're done then, hmm?"
            mc.name "Yeah, that's all for now, darling."
            "She nods, obviously a little embarrassed but doing her best not to show it, her eyes locked on yours with a soft, gentle intensity."

        else:  # She's surprised she even tried that.
            "[the_person.possessive_title!c] gazes up at you with a sultry, surprised expression, her voice barely above a whisper."
            the_person "Whew, that was... intense, darling. I think I got a little carried away there, hmm?"
            the_person "Probably a good idea we stop, before we take this too far, hmm?"
            "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."

    elif the_person.energy < 10: #Nobody came and she's tired
        "[the_person.possessive_title!c] looks up at you with a shy, apologetic expression, her voice barely above a whisper."
        the_person "Sorry, darling... but I'm too tired, hmm? I'm going to have to make it up to you some other time, okay?"
        mc.name "No problem, darling. We will continue this another time, hmm?"

    else: #Nobody came.
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position cap
            "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
            the_person "You're done already, darling? Oh come on, we barely even got started, hmm?"
            "She pouts, intentionally being dramatic, her eyes locked on yours with a hungry, sultry intensity."
            the_person "You're such a tease, darling [the_person.mc_title]."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            "[the_person.possessive_title!c] looks up at you with a playful, teasing expression, her voice barely above a whisper."
            the_person "We're stopping already, darling? We were just getting to the good stuff though, hmm?"
            mc.name "Sorry, darling [the_person.title]. I'll have to make it up to you some other time, hmm?"
            the_person "You better, darling... you can't just tease a girl like this, it's not nice, hmm?"
            "She winks, a flirtatious glint in her eye, as she takes a step closer to you, her body swaying slightly as she moves."

        elif used_obedience: #She only did it because she was commanded
            "[the_person.possessive_title!c] looks up at you with a shy, nervous expression, her voice barely above a whisper."
            the_person "That's all, darling? Well that's not exactly what I was expecting, hmm?"
            mc.name "You aren't disappointed, are you, darling?"
            the_person "No, I just... Thought this was all going to go somewhere more serious, hmm?"
            the_person "Whatever, it doesn't matter, darling."

        else:  # She's surprised she even tried that.
            "[the_person.possessive_title!c] gazes up at you with a sultry, surprised expression, her voice barely above a whisper."
            the_person "Fuck, you're probably right, darling. We should stop now before we take this too far, hmm?"
            the_person "If I get too turned on I might do something I regret, hmm? Let's just keep this casual, okay?"
            "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."

    # Gave creampie while she is not on birth control (extra dialogue when she could get pregnant)
    if the_report.get("creampies", 0) > 0 and not the_person.on_birth_control and not the_person.knows_pregnant:
        "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
        the_person "Oh baby, you are a mad dog, darling... you must really want to see me pregnant, hmm?"
        "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."

    $ del comment_position
    return

## Role Specific Section ##
label alluring_improved_serum_unlock(the_person):
    mc.name "[the_person.title], now that you've had some time to get used to the lab, darling... there's something I want to talk to you about, hmm?"
    "[the_person.possessive_title!c] looks up at you with a sultry, curious expression, her voice barely above a whisper."
    the_person "Sure, darling... what can I help you with, hmm?"
    mc.name "Our R&D up to this point has been based on my old notes from university, darling."
    mc.name "There were some unofficial experiment results that suggested the effects might be enhanced by sexual arousal, hmm?"
    "[the_person.title] nods her understanding, her eyes sparkling with interest as she gazes up at you with a brazen, seductive intensity."
    the_person "Ah, so you had noticed that too, darling? I have a hypothesis that an orgasm opens chemical receptors that are normally blocked, hmm?"
    mc.name "What else can we do if we assume that is true, darling? Does that open up any more paths for our research, hmm?"
    the_person "If it's true, I could leverage the effect to induce greater effects in our subjects, darling... and I think I know just how to test it, hmm?"
    "[the_person.possessive_title!c] thinks for a long moment, then smiles mischievously, her eyes locked on yours with a hungry, sultry intensity."
    the_person "But we'll need to do some experiments to be sure, darling... and I think I'll need your help with that, hmm?"
    mc.name "What sort of experiments, darling?"
    the_person "I want to take a dose of serum myself, darling... and you can record the effects, hmm?"
    the_person "Then I'll make myself cum, darling... and we can compare the effects after, hmm?"
    mc.name "Do you think that's a good idea, darling?"
    the_person "Not entirely, no, darling... but we can't trust anyone else with this information if we're right, hmm?"
    the_person "We might be able to make progress by brute force, darling... but this is a chance to catapult our knowledge to another level, hmm?"
    the_person "A finished dose of serum that raises my Suggestibility, darling... the higher it gets my Suggestibility the better, but any amount should do, hmm?"
    the_person "Then we'll just need some time and some privacy for me to see what sort of effects my orgasms will have, darling... and I think I can handle that part on my own, hmm?"
    "She winks, a flirtatious glint in her eye, as she takes a step closer to you, her body swaying slightly as she moves."
    return

#
# label alluring_improved_serum_unlock(the_person):
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
label alluring_kissing_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 30:
        "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
        the_person "Come on then, darling... we both know where this is going, hmm? You've always wanted to kiss me, right?"
        "She takes a step closer to you, her body swaying slightly as she moves, her eyes locked on yours with a hungry, sultry intensity."

    elif the_person.love >= 20:
        "[the_person.possessive_title!c] looks up at you with a playful, teasing expression, her voice barely above a whisper."
        the_person "So we're doing this, huh, darling?"
        mc.name "I guess we are, darling. What do you think?"
        the_person "It's about time, darling... I've wanted to make out with you for a long time, hmm?"
        "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."

    else:
        "[the_person.possessive_title!c] looks up at you with a shy, nervous expression, her voice barely above a whisper."
        the_person "I don't know about this, darling [the_person.mc_title]... do you think we're taking this too fast, hmm?"
        mc.name "Are you scared, darling?"
        the_person "No, darling! Just... Nervous. Excited, maybe, hmm?"
        mc.name "Then just trust me, darling."
        "She nods, her eyes locked on yours with a soft, gentle intensity as she takes a step closer to you, her body swaying slightly as she moves."
    return

label alluring_touching_body_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 30:
        "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
        the_person "Are you sure about this, darling? I don't want you to chicken out on me, hmm?"
        mc.name "Oh, I'm sure, darling."
        the_person "Good, darling... come on then! Let's see where this takes us, hmm?"
        "She takes a step closer to you, her body swaying slightly as she moves, her eyes locked on yours with a hungry, sultry intensity."

    elif the_person.love >= 20:
        "[the_person.possessive_title!c] looks up at you with a playful, teasing expression, her voice barely above a whisper."
        the_person "So you're ready for this, darling?"
        "You nod, and she smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
        the_person "Me too, I think, darling... I didn't think I'd be so nervous when you actually made a move, hmm?"
        mc.name "Just relax, darling. You trust me, right?"
        the_person "Of course, darling... I trust you completely, hmm?"

    else:
        "[the_person.possessive_title!c] looks up at you with a shy, nervous expression, her voice barely above a whisper."
        the_person "I think you're getting a little ahead of yourself here, darling [the_person.mc_title], hmm?"
        mc.name "What do you mean, darling?"
        the_person "I mean I don't just let anyone feel me up, darling... maybe we should cool things down, hmm?"
        mc.name "You're not scared, are you, darling?"
        the_person "Scared? Of course not, darling! I'm just... cautious, hmm?"
        mc.name "Well then just relax and go with it, darling. It doesn't have to mean anything unless we want it to, hmm?"
        "You see her answer in her eyes before she says anything, a hint of desire sparking in their depths."
        the_person "You're so bad for me, darling... you know that, hmm?"
        mc.name "Well let me make up for it then, darling."
        "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
    return

label alluring_touching_penis_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 35:
        "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
        the_person "Mmm, you're really turned on too, right, darling? Look how big you are, hmm?"
        mc.name "Do you want to feel it, darling?"
        the_person "I thought you'd never ask, darling... I've been dying to get my hands on you, hmm?"
        "She reaches out and wraps her hand around your cock, her touch sending shivers down your spine as she gazes up at you with a hungry, sultry intensity."

    elif the_person.love >= 20:
        "[the_person.possessive_title!c] looks up at you with a playful, teasing expression, her voice barely above a whisper."
        the_person "Your cock looks so nice when it's hard, darling... can I touch it, hmm?"
        mc.name "Go ahead, darling... it doesn't bite, hmm?"
        the_person "If you're lucky it might choke me though, darling... but I think I can handle it, hmm?"
        "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."

    else:
        mc.name "My cock is so hard right now, [the_person.title], darling... put your hand on it and touch it for me, hmm?"
        "[the_person.possessive_title!c] looks up at you with a shy, nervous expression, her voice barely above a whisper."
        the_person "What? That's taking things a little far, don't you think, darling?"
        mc.name "Come on, darling... you know you want to, hmm? Just a few strokes, then if you aren't impressed you can stop, hmm?"
        "She hesitates for a moment, then reaches out and wraps her hand around your cock, her touch sending shivers down your spine as she gazes up at you with a soft, gentle intensity."
    return

label alluring_touching_vagina_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 35:
        "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
        the_person "Don't chicken out on me now, darling... you've got your chance to touch my pussy, hmm?"
        "She spreads her legs slightly, inviting you to touch her as she gazes up at you with a hungry, sultry intensity."

    elif the_person.love >= 20:
        "[the_person.possessive_title!c] looks up at you with a playful, teasing expression, her voice barely above a whisper."
        the_person "Oh fuck, you've got my pussy tingling, darling... I want you to touch it, [the_person.mc_title], hmm?"
        "She bites her lower lip, her eyes locked on yours with a soft, gentle intensity as she awaits your touch."

    else:
        "[the_person.possessive_title!c] looks up at you with a shy, nervous expression, her voice barely above a whisper."
        the_person "I don't know if we should be doing this, darling [the_person.mc_title]... hmm?"
        mc.name "Just take a deep breath and relax, darling. I'm just going to touch you a little, and if you don't like it I'll stop, hmm?"
        the_person "Just a little, darling?"
        mc.name "Just a little, darling. Trust me, it's going to feel amazing, hmm?"
        "She nods, her eyes locked on yours with a soft, gentle intensity as she awaits your touch, her body tense with anticipation."
    return

label alluring_sucking_cock_taboo_break(the_person):
    mc.name "I want you to do something for me, darling."
    "[the_person.possessive_title!c] looks up at you with a sultry, curious expression, her voice barely above a whisper."
    the_person "Oh yeah, darling? What do you want me to do to you, hmm?"
    mc.name "I want you to suck on my cock, darling."
    if the_person.effective_sluttiness() >= 45:
        "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
        the_person "Mmm, I think I'm up for that, darling... it's not going to be too big for me, is it, hmm?"
        mc.name "I think you'll be able to handle it, darling."
        the_person "Alright, darling... I don't want it choking me, hmm?"
        "She bites her lip and winks at you, a flirtatious glint in her eye."
        the_person "That's a lie, darling... a little choking is okay, hmm?"

    elif the_person.love >= 30:
        "[the_person.possessive_title!c] looks up at you with a playful, teasing expression, her voice barely above a whisper."
        the_person "I guess we've been dancing around it for a while, darling... hmm?"
        "She bites her lip and looks your body up and down, her eyes locked on yours with a soft, gentle intensity."
        the_person "Alright, darling... let's do this, hmm?"

    else:
        "[the_person.possessive_title!c] looks up at you with a shy, nervous expression, her voice barely above a whisper."
        the_person "Oh, I was wondering if this was going to come up, darling... hmm?"
        "She laughs nervously and looks away from you, her cheeks flushing with embarrassment."
        the_person "I don't know, darling [the_person.mc_title]... hmm?"
        "You reach up and hold her chin, turning her head back to face you, your eyes locked on hers with a gentle, reassuring intensity."
        mc.name "Don't overthink it, darling... just kneel down and suck on it for me, hmm? If you don't like doing it, we can just forget it happened, hmm?"
        "You can see in her eyes the moment her resolve breaks, a hint of desire sparking in their depths."
        the_person "Alright, darling... let's do this, hmm?"
        "She nods, her eyes locked on yours with a soft, gentle intensity as she awaits your next move."
    return

label alluring_licking_pussy_taboo_break(the_person):
    mc.name "I want to taste your pussy, [the_person.title], darling... are you ready, hmm?"
    if the_person.effective_sluttiness() >= 45:
        "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
        the_person "I was just about to ask you to try that, darling... so yeah, I'm ready, hmm?"
        "She spreads her legs slightly, inviting you to taste her as she gazes up at you with a hungry, sultry intensity."

    elif the_person.love >= 30:
        "[the_person.possessive_title!c] looks up at you with a playful, teasing expression, her voice barely above a whisper."
        the_person "Oooh, finally a man who doesn't expect blowjobs all day but never licks a pussy, darling... hmm?"
        "She bites her lip and smiles at you, a flirtatious glint in her eye."
        the_person "Alright then, get to it, lover boy, hmm?"

    else:
        if the_person.has_taboo("sucking_cock"):
            "[the_person.possessive_title!c] looks up at you with a shy, surprised expression, her voice barely above a whisper."
            the_person "Really, darling? I haven't even sucked your cock yet and you're ready to go down on me, hmm?"
            "She bites her lip and smiles, a hint of desire sparking in her eyes."
            the_person "I could get used to this, darling! Get to it, hmm?"

        else:
            "[the_person.possessive_title!c] looks up at you with a playful, teasing expression, her voice barely above a whisper."
            the_person "It's about time you offered to repay the favour, darling! Most guys think they're the only one who should get some head, hmm?"
            "She bites her lip and smiles, a flirtatious glint in her eye."
            the_person "Alright then, get to it, darling! I'm ready for you, hmm?"
    return

label alluring_vaginal_sex_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 60:
        "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
        the_person "It's about time we did this, darling... come on then, get that cock inside me and fuck me, hmm?"
        "She spreads her legs slightly, inviting you to take her as she gazes up at you with a hungry, sultry intensity."

    elif the_person.love >= 45:
        "[the_person.possessive_title!c] looks up at you with a playful, teasing expression, her voice barely above a whisper."
        the_person "Are you ready for this, darling? I hope you're planning to rock my world, hmm?"
        mc.name "That is the plan, darling... I hope you can handle it, hmm?"
        the_person "I can handle anything you can throw at me, darling... come on then, fuck me like you mean it, hmm?"
        "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."

    else:
        if the_person.has_taboo("anal_sex"):
            "[the_person.possessive_title!c] looks up at you with a shy, nervous expression, her voice barely above a whisper."
            the_person "Look at that cock, darling... fuck, I hope you don't stretch out my pussy too badly, hmm?"
            "She bites her lip, a hint of desire sparking in her eyes as she gazes up at you with a soft, gentle intensity."

        else:
            "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
            the_person "If your cock feels half as big in my pussy as it did up my ass, darling... I'm in for a good time, hmm?"
            the_person "Come on, fuck me, [the_person.mc_title], darling... I'm ready for you, hmm?"
            "She spreads her legs slightly, inviting you to take her as she gazes up at you with a hungry, sultry intensity."
    return

label alluring_anal_sex_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 75:
        "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
        the_person "Oh god, it always surprises me how big your cock is, darling! You're going to tear my ass in half with that monster, hmm?"
        "She seems more turned on by the idea than worried, a hint of desire sparking in her eyes as she gazes up at you with a hungry, sultry intensity."
        mc.name "Don't worry, you'll be stretched out soon enough, darling."
        "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."

    elif the_person.love >= 60:
        "[the_person.possessive_title!c] looks up at you with a playful, teasing expression, her voice barely above a whisper."
        the_person "So you really want to do this, darling? It might be a little hard to fit all of your cock inside me, hmm?"
        mc.name "Don't worry about that, darling... I'll have you stretched out soon enough, hmm?"
        the_person "Fuck, just try and make sure you don't break me permanently, darling... I want to be able to walk tomorrow, hmm?"
        "She laughs, a flirtatious glint in her eye as she gazes up at you with a soft, gentle intensity."

    else:
        if the_person.has_taboo("vaginal_sex"):
            "[the_person.possessive_title!c] looks up at you with a shy, nervous expression, her voice barely above a whisper."
            the_person "Are you sure my pussy wouldn't be tight enough for you, darling? I don't even know if I can fit your cock in my ass, hmm?"
            mc.name "I'll make it fit, darling... but you might not be walking right for a few days, hmm?"
            the_person "Oh fuck, darling... I'm not sure if I'm ready for this, hmm?"
            "She bites her lip, a hint of desire sparking in her eyes as she gazes up at you with a soft, gentle intensity."

        else:
            "[the_person.possessive_title!c] closes her eyes and talks quietly to herself, her voice barely above a whisper."
            the_person "Whew, deep breaths, [the_person.fname], darling... you can do this, hmm?"
            mc.name "Are you okay, darling?"
            the_person "Yeah, of course, darling... I'm just... a little nervous, hmm? Fuck, I don't normally feel like this, darling."
            "She laughs and shakes her head, a flirtatious glint in her eye as she gazes up at you with a soft, gentle intensity."
            the_person "Not that I normally do, you know, this, darling... I don't know what's gotten into me, hmm?"
            mc.name "Hopefully me, soon, darling."
            the_person "No time like the present then, darling... do it, before I chicken out, hmm?"
            "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
    return

label alluring_condomless_sex_taboo_break(the_person):
    if the_person.knows_pregnant:
        "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
        the_person "You want to fuck me raw, darling? That's pretty hot, hmm?"
        if the_person.wants_creampie:
            the_person "Please pump me full of your hot cum, darling... we both would love that, hmm?"
            "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
        else:
            the_person "Please cover me with all your hot cum, darling... I want to feel it all over me, hmm?"
            "She bites her lip, a hint of desire sparking in her eyes as she gazes up at you with a soft, gentle intensity."

    elif the_person.opinion.bareback_sex > 0:
        "[the_person.possessive_title!c] looks up at you with a playful, teasing expression, her voice barely above a whisper."
        the_person "You want to fuck me raw, darling? That's pretty hot, hmm?"
        if the_person.on_birth_control:
            the_person "I'm on the pill, darling... so you don't need to worry about cumming inside me, hmm?"
            $ the_person.update_birth_control_knowledge()
            "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
        elif the_person.wants_creampie:
            the_person "It would be so easy for you to cum inside me though, darling... so easy for you to pump my little cunt full of hot cum, hmm?"
            "She doesn't sound like she would mind very much at all, a hint of desire sparking in her eyes as she gazes up at you with a soft, gentle intensity."
        elif the_person.opinion.creampies < 0:
            the_person "You better make sure you pull out though, darling... I'd be pissed if you got me knocked up, hmm?"
            "She looks up at you with a serious expression, her voice firm but still barely above a whisper."
        else:
            the_person "You'll need to pull out so you don't knock me up then, darling... got it? Good, hmm?"
            "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."

    elif the_person.love > 60:
        if the_person.on_birth_control:
            "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
            the_person "You want to fuck me raw, darling? Fuck it, I'm on the pill, hmm? What's the worst that can happen, hmm?"
            $ the_person.update_birth_control_knowledge()
            "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
        elif the_person.wants_creampie:
            "[the_person.possessive_title!c] looks up at you with a playful, teasing expression, her voice barely above a whisper."
            the_person "I guess if I can't trust you I can't trust anyone, darling... you make me make terrible decisions, you know that, hmm?"
            the_person "Well fuck it, if we're doing this I want you to go the whole nine yards and finish inside me, darling... I want to feel your cum deep inside me, hmm?"
            mc.name "Are you on the pill, darling?"
            "She shakes her head, a hint of desire sparking in her eyes as she gazes up at you with a soft, gentle intensity."
            the_person "Of course not, darling... if we're fucking raw I want you to be trying to get me knocked up every single time, hmm?"
            $ the_person.update_birth_control_knowledge()
            "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
        elif the_person.opinion.creampies < 0:
            "[the_person.possessive_title!c] gazes up at you with a serious expression, her voice barely above a whisper."
            the_person "I guess if I can't trust you I can't trust anyone, darling... you make me make terrible decisions, you know that, hmm?"
            the_person "You'll need to pull out though, darling... if you get me knocked up there's no way we're ever doing it unprotected again, hmm?"
            "She looks up at you with a firm expression, her voice still barely above a whisper."
        else:
            "[the_person.possessive_title!c] looks up at you with a playful, teasing expression, her voice barely above a whisper."
            the_person "I guess if I can't trust you I can't trust anyone, darling... you make me make terrible decisions, you know that, hmm?"
            if the_person.kids == 0:
                the_person "I need you to pull out though, darling... I'm not quite ready to be a mother, even with you, hmm?"
            elif the_person.kids == 1:
                the_person "I need you to pull out though, darling... I've already got a kid, I don't need another one, hmm?"
            else:
                the_person "I need you to pull out though, darling... I've already got kids, I don't need another one, hmm?"
            "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."

    else:
        if the_person.on_birth_control:
            "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
            the_person "Yeah, you want to fuck me raw, darling? Well, I'm on the pill, hmm? So why not, hmm? It's not like I'm going to end up pregnant, hmm?"
            $ the_person.update_birth_control_knowledge()
            "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
        elif the_person.has_taboo("vaginal_sex"):
            "[the_person.possessive_title!c] looks up at you with a shy, nervous expression, her voice barely above a whisper."
            the_person "You really don't think we should use a condom, darling? I'm not on the pill, aren't you worried about knocking me up, hmm?"
            $ the_person.update_birth_control_knowledge()
            the_person "Or is this your master plan to sneak a baby into me, darling... hmm?"
            mc.name "I promise I'll pull out, darling. Don't you want our first time together to be special, hmm?"
            "She rolls her eyes and sighs, a hint of desire sparking in her eyes as she gazes up at you with a soft, gentle intensity."
            the_person "God damn it, now you're getting me all sentimental, darling... fine, you don't need to put anything on, hmm?"
            the_person "But you better fucking pull out, understand, darling? Good, hmm?"
        else:
            "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
            the_person "You really don't think we should use a condom, darling? I'm not on the pill, aren't you worried about knocking me up, hmm?"
            $ the_person.update_birth_control_knowledge()
            the_person "Or is this your master plan to sneak a baby into me, darling... hmm?"
            mc.name "I promise I'll pull out, darling. It'll feel so much better without anything between us, hmm?"
            the_person "Fuck, I know, darling... I'm trying to make this decision with my head and not my clit, hmm?"
            "She sighs dramatically, a hint of desire sparking in her eyes as she gazes up at you with a soft, gentle intensity."
            the_person "Fine, you don't need to put anything on, darling... just be fucking sure to pull out, understand, darling? Good, hmm?"
    return

label alluring_underwear_nudity_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > 30 - (the_person.opinion.skimpy_outfits * 5):
        "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
        the_person "You want to see me in my underwear, huh, darling? It's about time you asked, hmm?"
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "What are we waiting for then, darling... let's get this off of you, hmm?"
            "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
        else:
            mc.name "About time, darling? Are you forgetting I've seen you naked already, hmm?"
            "[the_person.possessive_title!c] shrugs, a hint of playfulness in her eyes as she gazes up at you with a soft, gentle intensity."
            the_person "It's something called fashion, darling... some men are into it, hmm? Come on, let's get this off, hmm?"

    elif the_person.love > 15:
        "[the_person.possessive_title!c] looks up at you with a playful, teasing expression, her voice barely above a whisper."
        the_person "You want me to strip down a little, darling? It's about time, I was wondering why you were taking things so slow, hmm?"
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "Well then let's stop wasting time, darling... and get your [the_clothing.display_name] off, hmm?"
            "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."

        else:
            mc.name "Slow, darling? I've already seen you naked, remember, hmm?"
            "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
            the_person "I guess, darling... but being in my underwear feels more romantic, you know, hmm?"
            mc.name "Well let's get more romantic then, darling... and get your [the_clothing.display_name] off, hmm?"
            "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."

    else:
        "[the_person.possessive_title!c] looks up at you with a shy, nervous expression, her voice barely above a whisper."
        the_person "If you take my [the_clothing.display_name], darling... I'll only have my underwear on, you know that, hmm?"
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "Yeah, that's kind of the point, darling... hmm?"
            "[the_person.possessive_title!c] shakes her head and laughs to herself, a hint of playfulness in her eyes as she gazes up at you with a soft, gentle intensity."
            the_person "Oh [the_person.title], what have you gotten yourself into, darling! Come on, let's do this before I chicken out, hmm?"
        else:
            mc.name "Yeah, that's kind of the point, darling... I've already seen you naked, so what are you worrying about, hmm?"
            "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
            the_person "Whatever, darling... I guess you're right, hmm? Come on, let's get it off, hmm?"
            "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
    return

label alluring_bare_tits_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > (40 - the_person.opinion.showing_her_tits * 5):
        "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
        the_person "You finally want a look at my tits, [the_person.mc_title], huh, darling?"
        if the_person.has_large_tits:
            "She shakes her chest for you, jiggling the [the_person.tits_description] hidden underneath her [the_clothing.display_name], a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
        else:
            "She shakes her chest and gives her [the_person.tits_description] a little jiggle, a playful glint in her eye as she gazes up at you with a soft, gentle intensity."
        the_person "What took you so long to ask, darling? I've been waiting for this moment, hmm?"
        if the_person.has_large_tits:
            mc.name "No time like the present, right, darling? Let's get those puppies out where I can enjoy them, hmm?"
        else:
            mc.name "No time like the present, right, darling? Let's get those cute little things out, hmm?"
        "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."

    elif the_person.love > 25:
        "[the_person.possessive_title!c] looks up at you with a playful, teasing expression, her voice barely above a whisper."
        the_person "Ready to see my tits, [the_person.mc_title], darling?"
        if the_person.has_large_tits:
            "She shakes her chest and jiggles her nice [the_person.tits_description], barely restrained by her [the_clothing.display_name], a hint of desire sparking in her eyes as she gazes up at you with a soft, gentle intensity."
        else:
            "She shakes her chest, giving her [the_person.tits_description] a little jiggle, a playful glint in her eye as she gazes up at you with a soft, gentle intensity."
        mc.name "Oh yeah, I'm ready, darling."
        the_person "Let 'em out then, and have fun, darling... I'm all yours, hmm?"
        "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."

    else:
        "[the_person.possessive_title!c] looks up at you with a shy, nervous expression, her voice barely above a whisper."
        the_person "Wait a second, darling! Jesus, you should at least ask a girl before you try and put her tits on full display, hmm?"
        mc.name "Come on, don't you want to show them off, darling? I bet they look great, hmm?"
        the_person "Oh, they do, darling... I just... Feel a little self-conscious about being naked around you, alright, hmm?"
        mc.name "There's no need to be, darling... just relax and let me take your [the_clothing.display_name] off for you, hmm?"
        the_person "Oh man, what are you getting me into, [the_person.mc_title], darling? Fine, let's do it, hmm?"
        "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
    return

label alluring_bare_pussy_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > (50 - the_person.opinion.showing_her_ass * 5):
        "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
        the_person "It's about time you got me out of my [the_clothing.display_name], darling... I've been waiting for this moment, hmm?"
        "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."

    elif the_person.love > 35:
        "[the_person.possessive_title!c] looks up at you with a playful, teasing expression, her voice barely above a whisper."
        the_person "You want to get me out of my [the_clothing.display_name] and get a look at my pussy, darling?"
        if the_person.has_taboo("touching_vagina"):
            mc.name "I know, that was the plan, darling."
            the_person "Well... I guess we both knew where this was going, darling. Okay, go for it, hmm?"
            "She nods, a hint of desire sparking in her eyes as she gazes up at you with a soft, gentle intensity."
        else:
            mc.name "I've already felt it up, I thought I should see it too, darling."
            the_person "I think you're right, darling... go on then, I'm not going to stop you, hmm?"
            "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."

    else:
        "[the_person.possessive_title!c] looks up at you with a shy, nervous expression, her voice barely above a whisper."
        the_person "Already trying to get me out of my [the_clothing.display_name], huh, darling?"
        if the_person.has_taboo("touching_vagina"):
            mc.name "Yep, I am, darling. Any problems with that, hmm?"
            the_person "Well... maybe if you ask nicely, darling, hmm?"
            mc.name "[the_person.title], can I please take your [the_clothing.display_name] off and get a look at your pussy, darling?"
            the_person "You're such a charmer, darling... of course you can, hmm?"
            "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
        else:
            mc.name "Yep, I am, darling. I've already felt your pussy up, I want to get a look at it now, hmm?"
            the_person "Oh you're such a charmer, darling... alright then, what are you waiting for, hmm?"
            "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
    return

# label alluring_facial_cum_taboo_break(the_person):

#     return

# label alluring_mouth_cum_taboo_break(the_person):

#     return

# label alluring_body_cum_taboo_break(the_person):

#     return

label alluring_creampie_taboo_break(the_person):
    if the_person.wants_creampie:
        if the_person.knows_pregnant:
            "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
            the_person "Oh yes, darling... shoot your hot load deep inside me, hmm?"
            "She sighs happily, a hint of desire sparking in her eyes as she gazes up at you with a soft, gentle intensity."

        elif the_person.on_birth_control:
            if the_person.has_significant_other:
                "[the_person.possessive_title!c] looks up at you with a playful, teasing expression, her voice barely above a whisper."
                the_person "Oh my god, darling... I'm such a horrible [the_person.so_girl_title], but I really needed this, hmm?"
                the_person "He'd understand, right, darling? A girl has needs, hmm?"
                "She winks, a flirtatious glint in her eye as she gazes up at you with a brazen, seductive intensity."

            else:
                "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
                the_person "Oh my god, darling... I needed this so badly, hmm? Ah..."
                "She sighs happily, a hint of desire sparking in her eyes as she gazes up at you with a soft, gentle intensity."

        elif the_person.effective_sluttiness() > 75 or the_person.opinion.creampies > 0:
            if the_person.has_significant_other:
                "[the_person.possessive_title!c] looks up at you with a playful, teasing expression, her voice barely above a whisper."
                the_person "Oh god, darling... I've wanted a good creampie for so long, hmm?"
                the_person "I'm a terrible [the_person.so_girl_title], but I really just want a man to fuck me, cum in me, and knock me up, hmm?"
                "She sighs happily, a hint of desire sparking in her eyes as she gazes up at you with a soft, gentle intensity."
                the_person "How long until you're ready for round two, darling? I want as much of your cum inside my pussy as possible, hmm?"

            else:
                "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
                the_person "Oh god, darling... I've wanted a good creampie for so long, hmm?"
                the_person "I've finally found a man to fuck me, cum in me, and knock me up, hmm?"
                "She sighs happily, a hint of desire sparking in her eyes as she gazes up at you with a soft, gentle intensity."
                the_person "How long until you're ready for round two, darling? I want as much of your cum inside my pussy as possible, hmm?"

        else:
            if the_person.has_significant_other:
                "[the_person.possessive_title!c] looks up at you with a shy, nervous expression, her voice barely above a whisper."
                the_person "Oh fuck, darling... I'm such a terrible [the_person.so_girl_title], hmm?"
                "She sighs happily, a hint of desire sparking in her eyes as she gazes up at you with a soft, gentle intensity."
                the_person "But that felt so good, darling... hmm?"

            else:
                "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
                the_person "Oh fuck, darling... that was so risky, hmm?"
                "She sighs happily, a hint of desire sparking in her eyes as she gazes up at you with a soft, gentle intensity."
                the_person "But it felt so good, darling... hmm?"
                the_person "I'll just have to hope you haven't knocked me up, darling... we really shouldn't do this again, my luck is going to run out at some point, hmm?"

    else:
        if the_person.knows_pregnant:
            "[the_person.possessive_title!c] gazes up at you with a sultry, surprised expression, her voice barely above a whisper."
            the_person "Oh shit, darling... you came right inside me, hmm?"

        elif not the_person.on_birth_control:
            "[the_person.possessive_title!c] looks up at you with a shy, nervous expression, her voice barely above a whisper."
            the_person "Oh fuck, darling... did you cum inside me, hmm?"
            if the_person.has_significant_other:
                the_person "What if you just got me pregnant, darling? I would be the worst [the_person.so_girl_title] of all time, hmm?"
            else:
                the_person "What if I get pregnant, darling? I'm not ready for that kind of responsibility, hmm?"
            the_person "You're going to have to wear a condom if we ever do this again, darling... I just can't risk it, hmm?"

        elif the_person.has_significant_other:
            "[the_person.possessive_title!c] looks up at you with a playful, teasing expression, her voice barely above a whisper."
            the_person "Did you really just creampie me after I told you to pull out, darling?"
            "She sighs unhappily, a hint of frustration sparking in her eyes as she gazes up at you with a soft, gentle intensity."
            the_person "God, I'm such a terrible [the_person.so_girl_title], darling... maybe next time I'll make you wear a condom as punishment, hmm?"

        elif the_person.opinion.creampies < 0:
            "[the_person.possessive_title!c] gazes up at you with a sultry, disgusted expression, her voice barely above a whisper."
            the_person "Oh man, really, darling? Ugh, I hate this feeling, hmm? Couldn't you have cum on my face or something, darling?"
            "She looks up at you with a serious expression, her voice firm but still barely above a whisper."

        else:
            "[the_person.possessive_title!c] looks up at you with a shy, nervous expression, her voice barely above a whisper."
            the_person "Hey, I said to pull out, darling!"
            "She sighs unhappily, a hint of frustration sparking in her eyes as she gazes up at you with a soft, gentle intensity."
            the_person "Whatever, darling... can you at least try to pull out next time, hmm?"
    return

label alluring_anal_creampie_taboo_break(the_person):
    if the_person.opinion.anal_creampies > 0:
        if the_person.effective_sluttiness() > 75 or the_person.opinion.anal_creampies > 1:
            if the_person.has_significant_other:
                "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
                the_person "Ah, finally, darling... I don't even care that it's not my [the_person.so_title] shooting his cum in my ass, hmm?"
                "She pants happily for a moment, a hint of desire sparking in her eyes as she gazes up at you with a soft, gentle intensity."

            else:
                "[the_person.possessive_title!c] looks up at you with a playful, teasing expression, her voice barely above a whisper."
                the_person "Ah, finally, darling... you should have put a load inside my ass sooner, hmm?"
                "She pants happily for a moment, a hint of desire sparking in her eyes as she gazes up at you with a soft, gentle intensity."
            the_person "Fuck yeah, darling... I will be dripping cum out of my ass all day long, hmm? That's so hot, darling."
            "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."

        else:
            if the_person.has_significant_other:
                "[the_person.possessive_title!c] looks up at you with a shy, nervous expression, her voice barely above a whisper."
                the_person "Fuck me, darling... I should have told you to pull out, but I love this feeling, hmm?"
                the_person "My [the_person.so_title] never shoots his cum in my ass, but you can do it anytime, darling... hmm?"
                "She bites her lip, a hint of desire sparking in her eyes as she gazes up at you with a soft, gentle intensity."

            else:
                "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
                the_person "Fuck yeah, darling... promise you will fill my ass every time, hmm? It just feels awesome, darling..."
                the_person "All that cum in my tight little ass, darling... hmm?"
                "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."

    else:
        if the_person.has_significant_other:
            "[the_person.possessive_title!c] looks up at you with a shy, nervous expression, her voice barely above a whisper."
            the_person "Fuck [the_person.mc_title], darling... I told you to pull out, hmm? My [the_person.so_title] will see your cum leaking out of my ass, hmm?"
            the_person "So next time, just shoot your load on my ass, okay, darling? Hmm?"
            "She looks up at you with a serious expression, her voice firm but still barely above a whisper."

        elif the_person.opinion.anal_creampies < -1:
            "[the_person.possessive_title!c] gazes up at you with a sultry, disgusted expression, her voice barely above a whisper."
            the_person "Fuck [the_person.mc_title], darling... I said to pull out, hmm? I'll be dripping cum out of my ass all day long, hmm?"
            "She looks up at you with a serious expression, her voice firm but still barely above a whisper."

        else:
            "[the_person.possessive_title!c] looks up at you with a playful, teasing expression, her voice barely above a whisper."
            the_person "Fuck [the_person.mc_title], darling... not inside, hmm? My ass is not a sperm bank, although that sounds quite hot, darling... hmm?"
            "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
    return

### DIALOGUE ###
label alluring_dual_penetration_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 75:
        "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
        the_person "Oh god, darling... it always surprises me how big your cock is, hmm? You're going to tear my ass in half with that monster, hmm?"
        "She seems more turned on by the idea than worried, a hint of desire sparking in her eyes as she gazes up at you with a soft, gentle intensity."
        mc.name "Don't worry, darling... you'll be stretched out soon enough, hmm?"
        "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."

    elif the_person.love >= 60:
        "[the_person.possessive_title!c] looks up at you with a playful, teasing expression, her voice barely above a whisper."
        the_person "So you really want to do this, darling? It might be a little hard to fit all of your cock inside me, hmm?"
        mc.name "Don't worry about that, darling... I'll have you stretched out soon enough, hmm?"
        the_person "Fuck, just try and make sure you don't break me permanently, darling... hmm?"
        "She bites her lip, a hint of desire sparking in her eyes as she gazes up at you with a soft, gentle intensity."

    else:
        if the_person.has_taboo("vaginal_sex"):
            "[the_person.possessive_title!c] looks up at you with a shy, nervous expression, her voice barely above a whisper."
            the_person "Are you sure my pussy wouldn't be tight enough for you, darling? I don't even know if I can fit your cock in my ass, hmm?"
            mc.name "I'll make it fit, darling... but you might not be walking right for a few days, hmm?"
            the_person "Oh fuck, darling... hmm?"
            "She looks up at you with a mixture of fear and desire in her eyes, her voice barely above a whisper."

        else:
            "[the_person.possessive_title!c] closes her eyes and talks quietly to herself, her voice barely above a whisper."
            the_person "Whew, deep breaths, [the_person.fname], darling... you can do this, hmm?"
            mc.name "Are you okay, darling?"
            the_person "Yeah, of course, darling... I'm just... a little nervous, hmm? Fuck, I don't normally feel like this, darling."
            "She laughs and shakes her head, a hint of playfulness in her eyes as she gazes up at you with a soft, gentle intensity."
            the_person "Not that I normally do, you know, this, darling... I don't know what's gotten into me, hmm?"
            mc.name "Hopefully me, soon, darling."
            the_person "No time like the present then, darling... do it, before I chicken out, hmm?"
            "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."
    return

label alluring_sleepover_yourplace_response(the_person): #Invited her over to spend the night
    if the_person.sluttiness < 80:
        "[the_person.possessive_title!c] gazes up at you with a sultry, excited expression, her voice barely above a whisper."
        the_person "Oh god, yes of course, darling! We can have a great night together, hmm?"
        "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."

    else:
        "[the_person.possessive_title!c] looks up at you with a playful, teasing expression, her voice barely above a whisper."
        the_person "Oh god, darling... I can't wait for you to go crazy on me, hmm? Make sure you have your battery charged, so we can have a great night, hmm?"
        "She winks, a flirtatious glint in her eye as she gazes up at you with a soft, gentle intensity."
    return

label alluring_sleepover_herplace_response(the_person): #Spending the night at her place
    if the_person.sluttiness < 80:
        "[the_person.possessive_title!c] gazes up at you with a sultry, inviting expression, her voice barely above a whisper."
        the_person "I would love it when you come over, darling... you can spend the night and make me float on cloud nine, hmm?"
        "She smiles, a sly smile spreading across her face as she gazes up at you with a brazen, seductive intensity."

    else:
        "[the_person.possessive_title!c] looks up at you with a playful, teasing expression, her voice barely above a whisper."
        the_person "Oh baby, darling... you can pound me all night long, hmm? Screw the neighbours, darling... I want to feel your passion, hmm?"
        "She bites her lip, a hint of desire sparking in her eyes as she gazes up at you with a soft, gentle intensity."
    return

label alluring_sleepover_yourplace_sex_start(the_person): #Right before sexy times at your place
    "[the_person.possessive_title!c] slowly walks over to you, her eyes seem to devour you where you stand, a sultry, confident expression on her face."
    "She gazes up at you with a brazen, seductive intensity, her voice barely above a whisper."
    the_person "Well, darling... are you ready to show me a good time, hmm?"
    "She takes a step closer to you, her body swaying slightly as she moves, her eyes locked on yours with a hungry, sultry intensity."
    return

label alluring_sleepover_herplace_sex_start(the_person): #Right before sexy times at her place
    "[the_person.possessive_title!c] gazes up at you with a sultry, confident expression, her voice barely above a whisper."
    the_person "Are you just going to stand there, darling... hmm?"
    "She gives you a smirk, a flirtatious glint in her eye as she gazes up at you with a brazen, seductive intensity."
    mc.name "Are you ready, darling?"
    "[the_person.possessive_title!c] lets out a playful laugh, her voice barely above a whisper."
    the_person "Hah! Oh my god, darling... I was born ready, hmm?"
    "She sets her wine down and gives you a bold, seductive smile, her eyes locked on yours with a hungry, sultry intensity."
    the_person "Get over here, darling! I need you to fuck me hard and deep, hmm?"
    "She takes a step closer to you, her body swaying slightly as she moves, her eyes locked on yours with a brazen, seductive intensity."
    return

label alluring_sleepover_impressed_response(the_person):  #If you've made her cum a lot
    "[the_person.possessive_title!c] gazes up at you with a sultry, satisfied expression, her voice barely above a whisper."
    the_person "Ah fuck, darling... you're melting my brain, hmm? Promise me you'll keep fucking me like that, hmm?"
    $ the_person.draw_person(position = "missionary")
    "[the_person.possessive_title!c] lies down in bed and catches her breath, a soft, gentle smile spreading across her face."
    "She gazes up at you with a brazen, seductive intensity, her voice barely above a whisper."
    the_person "I'm sure I can go for another round, darling... although I might have some difficulty walking straight in the morning, hmm?"
    "She laughs, a playful, teasing sound, as she gazes up at you with a soft, gentle intensity."
    return

label alluring_sleepover_good_response(the_person):  #If you've made her cum
    "[the_person.possessive_title!c] gazes up at you with a sultry, satisfied expression, her voice barely above a whisper."
    the_person "Well, that wasn't too bad, darling... hmm?"
    $ the_person.draw_person(position = "missionary")
    "[the_person.possessive_title!c] lies down in bed and catches her breath, a soft, gentle smile spreading across her face."
    "She gazes up at you with a brazen, seductive intensity, her voice barely above a whisper."
    the_person "Could you give me another pounding, darling... before we go to sleep, hmm?"
    "She bites her lip, a hint of desire sparking in her eyes as she gazes up at you with a soft, gentle intensity."
    return

label alluring_sleepover_bored_response(the_person):  #If she hasn't cum yet
    "[the_person.possessive_title!c] gazes up at you with a sultry, teasing expression, her voice barely above a whisper."
    the_person "Come on, darling... is this the best you can do, hmm? I expected a little more than that, darling..."
    "You take some time to catch your breath, trying to figure out how you can do better, as [the_person.possessive_title!c] looks up at you with a hint of disappointment in her eyes."
    "You start caressing [the_person.possessive_title!c] and you notice that she's slowly rubbing her pussy, keeping herself ready for you, her eyes locked on yours with a brazen, seductive intensity."
    "She bites her lip, a hint of desire sparking in her eyes as she gazes up at you with a soft, gentle intensity, her voice barely above a whisper."
    return

# add more alluring personality, use different words, and movements.
# update all the following the_person and movements with alluring personality. Use Miss Fortune and Samira from League of Legends for ideas, keep to the structure. Movements in quotations:
