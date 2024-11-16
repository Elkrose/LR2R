### PERSONALITY CHARACTERISTICS ###
# add more wild personality, use different words, and movements.
# update all the following the_person and movements with wild personality. Use Rangiku Matsumoto from Bleach or Nami from One Piece, for ideas, keep to the structure. Movements in quotations:

### DIALOGUE ###
label vt_wild_introduction(the_person):
    mc.name "Hey, gorgeous! Mind if I join you for a sec?"
    "She turns around and looks you up and down, a hint of amusement in her eyes."
    the_person "Hmm, what's the plan here, handsome? Trying to pick me up with a cheesy line?"
    mc.name "Hey, no cheesy lines here! I just saw you and thought, 'Wow, I need to meet that girl!'"
    "She laughs and crosses her arms, a playful smile spreading across her face."
    $ the_person.set_title()
    $ the_person.set_possessive_title()
    the_person "Alright, alright! I like the confidence, even if it is a little crazy. My name's [the_person.name]."
    the_person "And you are...?"
    "She raises an eyebrow, her eyes sparkling with curiosity."
    return

label vt_wild_greetings(the_person):
    if the_person.love < 0:
        "[the_person.possessive_title] looks up at you with a scowl, her voice dripping with annoyance."
        the_person "Ugh, what now? Can't you see I'm busy?"

    elif the_person.happiness < 90:
        "[the_person.possessive_title] sighs and looks up at you with a hint of frustration."
        the_person "Hey, handsome. Just peachy. Just what I needed, another distraction from my crappy day."

    else:
        if the_person.sluttiness > 60:
            if the_person.obedience > 180:
                "[the_person.possessive_title] gives you a sultry smile, her voice dripping with seduction."
                the_person "Hello there, [the_person.mc_title]. I hope you're here to give me a good time... I've been feeling a little restless lately."
            else:
                "[the_person.possessive_title] winks at you, her voice playful and flirtatious."
                the_person "Hey there, [the_person.mc_title]! I hope you're here for some fun... I'm feeling a little wild today."

        else:
            if the_person.obedience > 180:
                "[the_person.possessive_title] gives you a polite smile, her voice friendly but reserved."
                the_person "Hello, [the_person.mc_title]. It's nice to see you."
            else:
                "[the_person.possessive_title] grins at you, her voice casual and laid-back."
                the_person "Hey, what's up? Just hanging out, having a good time."
    return

label vt_wild_sex_responses_foreplay(the_person):
    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] moans enthusiastically, clearly enjoying herself already, her body writhing with pleasure."
            the_person "Mmm, yeah... that's the spot, handsome!"
        else:
            "[the_person.possessive_title!c] moans happily to herself, her eyes fluttering closed in ecstasy."
            the_person "That's, uh... that's pretty good, [the_person.mc_title]. You're really getting me going!"

    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            the_person "Oh fuck, I love the way you touch me, [the_person.mc_title]! You're so rough and gentle at the same time!"
        else:
            the_person "Oh... oh fuck that feels nice! Don't stop, [the_person.mc_title], please don't stop!"

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            the_person "It feels so fucking good when you touch me like that, [the_person.mc_title]! I'm on fire!"
        else:
            the_person "Mmm, keep going [the_person.mc_title]. Just keep going and don't stop, I'm loving this!"

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "Mmm, touch me all over, [the_person.mc_title]! I'm your dirty slut and you can do anything you want with me, I'm all yours!"
        else:
            the_person "Touch me, [the_person.mc_title], I'm all yours! Take me, use me, make me cum!"

    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                the_person "Oh fuck, I'm going to cum soon, [the_person.mc_title]! I can feel it happening, you're getting me so close, I'm going to explode!"
            else:
                the_person "The way you feel is so different from my [the_person.so_title], [the_person.mc_title]. For some reason your touch is the one that drives me crazy, makes me want to scream and cum all over you!"
        else:
            the_person "Don't stop, [the_person.mc_title]! You're going to make me cum—don't you dare stop, I'm so close, I can feel it, oh fuck, yes, yes, yes!"
    return

label vt_wild_sex_responses_oral(the_person):
    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] giggles with excitement, her eyes sparkling with mischief."
            the_person "Go down on me, [the_person.mc_title]... you know how I want it, rough and wild!"
        else:
            "[the_person.possessive_title!c] giggles with excitement, her face flushing with pleasure."
            the_person "Oh fuck, you're really going to... Oh fuck yes, please don't stop!"

    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            the_person "Mmm, I love getting some good head, [the_person.mc_title]... you're so good at this!"
        else:
            the_person "Fuck me, that feels real nice... don't stop, [the_person.mc_title], please don't stop!"

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            the_person "Eat me out, [the_person.mc_title]... your tongue feels amazing, like a little piece of heaven!"
        else:
            the_person "That feels so good, you have no idea... I'm melting, [the_person.mc_title], I'm melting!"

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "Mmm, lick that pussy, [the_person.mc_title]! Ah, yes, yes, yes!"
        else:
            the_person "Oh god, yes! Yes, [the_person.mc_title], yes... don't stop, please don't stop!"

    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                the_person "Fuck fuck fuck, that's it right there, [the_person.mc_title]! I'm going to cum, I'm going to cum so hard!"
            else:
                the_person "My [the_person.so_title] never eats me out like this, [the_person.mc_title]... you're so much better than him!"
                the_person "Make me cum my brains out and forget about him, [the_person.mc_title]... make me yours!"
        else:
            the_person "Don't stop, [the_person.mc_title]! You're going to make me cum, don't you dare stop... I'm so close, I can feel it!"
    return

label vt_wild_sex_responses_vaginal(the_person):
    if the_person.energy < 10:
        call low_energy_sex_responses_vaginal(the_person) from _vt_wild_call_low_energy_sex_responses_vaginal_10
        return

    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            $ play_moan_sound()
            "[the_person.possessive_title!c] moans and wiggles her hips with your cock inside her, her eyes sparkling with pleasure."
            the_person "Mmm, how does my pussy feel, [the_person.mc_title]? I hope I'm tight enough for you, handsome."
        else:
            "[the_person.possessive_title!c] bites her lip and stifles a moan, her face flushing with desire."

    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            the_person "Oh fuck, I never get tired of feeling you inside me, [the_person.mc_title]! You're so big and hard, it's like you were made for me!"
        else:
            the_person "Oh... Oh fuck me, your cock feels nice, [the_person.mc_title]. Don't stop, please don't stop!"

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            the_person "Mmm, you feel so good fucking my pussy, [the_person.mc_title]! I love the way you move, the way you make me feel!"
        else:
            the_person "Ah, fuck me just like that, [the_person.mc_title]! Yes, yes, yes, don't stop!"

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "That's right, use me like your dirty little slut and fuck my pussy hard, [the_person.mc_title]! I love it when you're rough and wild!"
        else:
            the_person "Oh fuck yes, fuck yes, [the_person.mc_title]! I'm so close, I can feel it, don't stop!"

    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                the_person "Fuck! I'm... Your cock is going to make me cum, [the_person.mc_title]! I want you to make me cum, I need it!"
            else:
                the_person "Your cock is stretching me out, my [the_person.so_title] is never going to be enough for me after this, [the_person.mc_title]!"
                the_person "Oh well, fuck him! Keep going and make me cum, [the_person.mc_title]! I'm all yours!"

        else:
            the_person "Don't stop fucking me, [the_person.mc_title]! You're going to make me cum, I can feel it, don't stop, please don't stop!"
    return

label vt_wild_sex_responses_anal(the_person):
    if the_person.energy < 10:
        call low_energy_sex_responses_anal(the_person) from vt_wild_call_low_energy_sex_responses_anal_10
        return

    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] looks up at you with a mixture of excitement and nervousness, her voice barely above a whisper."
            the_person "Just go slowly, handsome... and I should be okay, hmm?"
            "She doesn't seem so sure of that, but she's willing to try, her eyes sparkling with desire."
        else:
            $ the_person.call_dialogue("surprised_exclaim")
            "[the_person.possessive_title!c] takes a deep breath, trying to calm herself down, her voice shaking slightly."
            the_person "Deep breaths, [the_person.title]... deep breaths, hmm?"
            "She pants to herself, doing her best to keep control of the situation, her face flushing with pleasure."

    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            $ the_person.call_dialogue("surprised_exclaim")
            "[the_person.possessive_title!c] looks up at you with a sultry, seductive expression, her voice barely above a whisper."
            the_person "I'm never going to get used to being stretched out like this, handsome... but I love it, hmm?"
        else:
            "[the_person.possessive_title!c] moans, her voice filled with pleasure and surprise."
            the_person "Oh... Oh fuck my ass, [the_person.mc_title]! This feels so good, hmm?"

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] screams with pleasure, her voice echoing through the room."
            the_person "Gah! Ah! Fuck, [the_person.mc_title]! This is amazing, hmm?"
        else:
            "[the_person.possessive_title!c] looks up at you with a mixture of pain and pleasure, her voice barely above a whisper."
            the_person "God, I won't be able to sit for a week after this, [the_person.mc_title]... but it's worth it, hmm?"

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            if mc.condom:
                "[the_person.possessive_title!c] looks up at you with a sultry, seductive expression, her voice barely above a whisper."
                the_person "Give it to me, handsome... punish that slutty ass with your big cock, hmm?"
            else:
                "[the_person.possessive_title!c] screams with pleasure, her voice echoing through the room."
                the_person "Give it to me, fuck my horny asshole raw, [the_person.mc_title]! I love it, hmm?"
        else:
            "[the_person.possessive_title!c] looks up at you with a mixture of surprise and pleasure, her voice barely above a whisper."
            the_person "Ah! Why does your cock have to be so fucking big, [the_person.mc_title]?! This is insane, hmm?"

    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                "[the_person.possessive_title!c] screams with pleasure, her voice echoing through the room."
                the_person "Fuck, I'm going to cum from your cock up my ass, [the_person.mc_title]! This is amazing, hmm?"
            else:
                "[the_person.possessive_title!c] looks up at you with a sultry, seductive expression, her voice barely above a whisper."
                the_person "Wreck my ass, [the_person.mc_title]... send me back to my [the_person.so_title] gaping and ruined, hmm?"
                "[the_person.possessive_title!c] smiles, a sly smile spreading across her face."
                the_person "I might have a [the_person.so_title], but he doesn't drive me crazy like you do, [the_person.mc_title]... make me cum my brains out, hmm?"
                "[the_person.possessive_title!c] laughs, a playful, teasing sound."
                the_person "Screw my [the_person.so_title], he's not half the man you are, [the_person.mc_title]... I'm all yours, hmm?"
        else:
            $ the_person.call_dialogue("surprised_exclaim")
            "[the_person.possessive_title!c] looks up at you with a mixture of surprise and pleasure, her voice barely above a whisper."
            the_person "I think I'm going to cum soon, [the_person.mc_title]... this is amazing, hmm?"
    return

label vt_wild_climax_responses_foreplay(the_person):
    if the_person.sluttiness > 50:
        "[the_person.possessive_title!c] screams with pleasure, her voice echoing through the room."
        the_person "Oh fuck yes, I'm going to cum, [the_person.mc_title]! I'm cumming, hmm?!"
        "She arches her back, her body shaking with pleasure as she reaches her climax."

    else:
        $ the_person.call_dialogue("surprised_exclaim")
        "[the_person.possessive_title!c] looks up at you with a mixture of surprise and pleasure, her voice barely above a whisper."
        the_person "You're going to make me cum, [the_person.mc_title]! Fuck, this is amazing, hmm?"
        "She goes silent, her eyes rolling back in her head as she reaches her climax, then lets out a shuddering moan."
        "[the_person.possessive_title!c] shakes and trembles, her body wracked with pleasure as she cums, her voice echoing through the room."
    return

label vt_wild_climax_responses_oral(the_person):
    if the_person.sluttiness > 70:
        "[the_person.possessive_title!c] screams with pleasure, her voice echoing through the room."
        the_person "Fuck yes, I'm going to cum, [the_person.mc_title]! Make me cum, hmm?!"
        "She grabs your head, pulling you closer as she reaches her climax, her body shaking with pleasure."

    else:
        "[the_person.possessive_title!c] looks up at you with a mixture of surprise and pleasure, her voice barely above a whisper."
        the_person "Oh my god, you're good at that, [the_person.mc_title]! I'm going to... I'm going to cum, hmm?"
        "She arches her back, her body trembling with pleasure as she reaches her climax, her voice rising to a crescendo."
        "[the_person.possessive_title!c] lets out a shuddering moan, her body wracked with pleasure as she cums, her voice echoing through the room."
    return

label vt_wild_climax_responses_vaginal(the_person):
    if the_person.sluttiness > 70:
        if the_person.arousal_perc > 120:
            "[the_person.possessive_title!c] screams with pleasure, her voice echoing through the room."
            the_person "Yes, [the_person.mc_title]! Keep going, make your little slut cum, hmm?!"
            "She grabs your hips, pulling you deeper into her as she reaches her climax, her body shaking with pleasure."
        else:
            "[the_person.possessive_title!c] looks up at you with a mixture of surprise and pleasure, her voice barely above a whisper."
            the_person "Ah, [the_person.mc_title]! More! I'm going to... Ah! Cum! Fuck, hmm?!"
            "She closes her eyes and squeals with pleasure, her body trembling with pleasure as she reaches her climax."
            "[the_person.possessive_title!c] lets out a shuddering moan, her body wracked with pleasure as she cums, her voice echoing through the room."

    else:
        "[the_person.possessive_title!c] looks up at you with a mixture of surprise and pleasure, her voice barely above a whisper."
        the_person "Oh god, I'm going to... Oh fuck me, [the_person.mc_title]! Ah, hmm?!"
        "She arches her back, her body trembling with pleasure as she reaches her climax, her voice rising to a crescendo."
        "[the_person.possessive_title!c] lets out a shuddering moan, her body wracked with pleasure as she cums, her voice echoing through the room."
    return

label vt_wild_climax_responses_anal(the_person):
    if the_person.sluttiness > 70:
        if the_person.arousal_perc > 120:
            "[the_person.possessive_title!c] screams with pleasure, her voice echoing through the room."
            the_person "Ah yes, [the_person.mc_title]... shove your big cock into my slutty ass, hmm? Make your little bitch cum, yeah!"
            "She grabs your hips, pulling you deeper into her as she reaches her climax, her body shaking with pleasure."
            the_person "Ah! Mmhmmm, [the_person.mc_title]... this is amazing, hmm?"
        else:
            "[the_person.possessive_title!c] looks up at you with a mixture of surprise and pleasure, her voice barely above a whisper."
            the_person "Oh fuck, [the_person.mc_title]... your cock feels so huge in my ass, hmm? It's going to make me cum, yeah!"
            "She arches her back, her body trembling with pleasure as she reaches her climax, her voice rising to a crescendo."
            the_person "Ah! Mmhmmm, [the_person.mc_title]... this is so good, hmm?"

    else:
        "[the_person.possessive_title!c] looks up at you with a mixture of surprise and pleasure, her voice barely above a whisper."
        the_person "Oh fucking shit, [the_person.mc_title]... I think you're going to make me, hmm?"
        "She barely finishes her sentence before her body is racked with pleasure, her eyes rolling back in her head."
        the_person "Cum, [the_person.mc_title]... oh god, I'm cumming, hmm?"
        "She lets out a shuddering moan, her body wracked with pleasure as she cums, her voice echoing through the room."
    return

label vt_wild_clothing_accept(the_person):
    if the_person.obedience > 180:
        "[the_person.possessive_title!c] gives you a sultry smile, her voice barely above a whisper."
        the_person "You think it will look good on me, [the_person.mc_title]? I guess that's all I need to hear then, hmm?"
        "She takes the clothing from you, her eyes sparkling with excitement as she examines it."

    else:
        "[the_person.possessive_title!c] looks at the clothing with a critical eye, then nods in approval."
        the_person "Hey, thanks [the_person.mc_title]. That's a good look, I like it, hmm?"
        "She takes the clothing from you, a playful smile spreading across her face as she starts to put it on."
    return

### DIALOGUE ###
label vt_wild_clothing_reject(the_person):
    if the_person.should_wear_uniform:
        "[the_person.possessive_title!c] rolls her eyes, a playful smile spreading across her face."
        the_person "Hey, I guess I should get my uniform sorted out, right? One second, [the_person.mc_title]."
        "She winks at you, her eyes sparkling with mischief as she heads off to change."

    elif the_person.obedience > 180:
        "[the_person.possessive_title!c] looks at the clothing with a hesitant expression, her voice barely above a whisper."
        the_person "I don't... I'm sorry, [the_person.mc_title], but I really don't think I could get away with wearing something like this, hmm?"
        "She looks up at you with a pleading expression, her eyes sparkling with uncertainty."
        the_person "I appreciate the thought, though, [the_person.mc_title]. You're always so sweet to me."

    else:
        if the_person.sluttiness > 60:
            "[the_person.possessive_title!c] laughs, a playful, teasing sound."
            the_person "Jesus, [the_person.mc_title], you didn't leave much to the imagination, did you? I don't think I can wear this, hmm?"
            "She winks at you, her eyes sparkling with mischief as she holds up the clothing."

        else:
            "[the_person.possessive_title!c] blushes, her face flushing with embarrassment."
            the_person "There's not much of an outfit to this outfit, [the_person.mc_title], hmm? Thanks for the thought, but there's no way I could wear this."
            "She looks up at you with a shy expression, her eyes sparkling with uncertainty."
    return

label vt_wild_clothing_review(the_person):
    if the_person.outfit.cum_covered:
        if (the_person.sluttiness > 40 and the_person.opinion.being_covered_in_cum >=0) or the_person.opinion.being_covered_in_cum > 0:
            "[the_person.possessive_title!c] giggles, a playful, teasing sound."
            the_person "I guess I can't walk around covered in cum all day, [the_person.mc_title]... that would be a little too wild, hmm?"
            "[the_person.possessive_title!c] starts to wipe up the biggest splashes of cum on her, her eyes sparkling with mischief."

        else:
            "[the_person.possessive_title!c] looks down at herself with a mixture of disgust and embarrassment."
            the_person "Fuck, [the_person.mc_title]... I need to clean up all of this cum! Let me know if I've missed any, okay?"
            "[the_person.possessive_title!c] wipes herself down, cleaning up all the cum she can find, her face flushing with embarrassment."

    if the_person.obedience > 180:
        "[the_person.possessive_title!c] looks up at you with a sultry, seductive expression."
        the_person "Oh man, [the_person.mc_title]... I'm a mess. I'll be back in a moment, I'm just going to get cleaned up for you, hmm?"
        "She winks at you, her eyes sparkling with mischief as she heads off to change."

    else:
        if the_person.sluttiness > 40:
            "[the_person.possessive_title!c] laughs, a playful, teasing sound."
            the_person "I don't think everyone else would appreciate me going around dressed like this as much as you would, [the_person.mc_title], hmm?"
            "She winks at you, her eyes sparkling with mischief as she heads off to change."
            the_person "I'll be back in a second, [the_person.mc_title]... I just want to get cleaned up and look presentable for you."

        else:
            "[the_person.possessive_title!c] looks down at herself with a mixture of frustration and embarrassment."
            the_person "Damn, [the_person.mc_title]... everything's out of place after that. Wait here a moment, I'm just going to find a mirror and try and look presentable, hmm?"
            "She heads off to change, her face flushing with embarrassment as she tries to compose herself."
    $ the_person.apply_planned_outfit(show_dress_sequence = True)
    return

label vt_wild_strip_reject(the_person, the_clothing, strip_type = "Full"):
    if the_person.obedience > 180:
        "[the_person.possessive_title!c] looks up at you with a sultry, seductive expression, her voice barely above a whisper."
        the_person "Could we leave my [the_clothing.display_name] on for now, please, [the_person.mc_title]? I want to savor the moment, hmm?"
        "She bites her lip, her eyes sparkling with desire as she gazes up at you."

    elif the_person.obedience < 70:
        "[the_person.possessive_title!c] tosses her head, a fiery look in her eyes, her voice firm and commanding."
        the_person "No, no, no, [the_person.mc_title]! I'll decide what comes off and when, okay? Don't think you can just strip me down without a fight, hmm?"
        "She puts her hands on her hips, her body language daring you to try and take control."

    else:
        "[the_person.possessive_title!c] smiles, a playful, teasing smile spreading across her face."
        the_person "Not yet, [the_person.mc_title]... get me a little warmed up first, okay? Then maybe you can take off my [the_clothing.display_name] and see what's underneath, hmm?"
        "She winks at you, her eyes sparkling with mischief as she invites you to play along."
    return

label vt_wild_strip_obedience_accept(the_person, the_clothing, strip_type = "Full"):
    "[the_person.possessive_title!c] laughs nervously as you start to slide her [the_clothing.display_name] away, her eyes sparkling with a mix of excitement and hesitation."
    if the_person.obedience > 180:
        "[the_person.possessive_title!c] looks up at you with a sultry, seductive expression, her voice barely above a whisper."
        the_person "Hey, [the_person.mc_title]... I don't know if that's a good idea, hmm? Could we just leave it for now?"
        "She bites her lip, her eyes sparkling with desire as she gazes up at you, her body language inviting you to take control."

    else:
        "[the_person.possessive_title!c] raises an eyebrow, a playful, teasing glint in her eye, her voice husky and seductive."
        the_person "Hey, [the_person.mc_title]... let's not take this too far, hmm? At least, not yet, okay?"
        "She smiles, a sly, mischievous smile spreading across her face as she invites you to play along, her body language daring you to take the next step."
    return

label vt_wild_grope_body_reject(the_person):
    if the_person.effective_sluttiness("touching_body") < 5: #Fail point for touching shoulder
        "[the_person.possessive_title!c] lets out a startled yelp as you touch her, then laughs awkwardly, her eyes sparkling with surprise."
        the_person "Ah, [the_person.mc_title]! You scared me, hmm?"
        "[the_person.possessive_title!c] steps back, her hands on her hips, a playful, teasing glint in her eye."
        the_person "Haha, sorry... Your hand just kind of came out of nowhere, didn't it?"
        mc.name "Sorry, I didn't mean to startle you."
        "[the_person.possessive_title!c] smiles, a sultry, seductive smile spreading across her face."
        the_person "Don't worry about it, just give me a little warning next time, okay? I like to be prepared, hmm?"
        "She winks at you, her eyes sparkling with mischief as she invites you to play along."

    else: #Fail point for touching waist
        "[the_person.possessive_title!c] raises an eyebrow, a hint of annoyance in her voice, her eyes flashing with warning."
        the_person "Hey, [the_person.mc_title]... could you just..."
        "[the_person.possessive_title!c] takes your hand and pulls it off of her waist, her movements firm but playful."
        the_person "... Keep your hands to yourself? Thanks, hmm?"
        mc.name "Oh yeah, of course. My bad."
        "[the_person.possessive_title!c] smiles, a sly, mischievous smile spreading across her face."
        the_person "No problem, just don't make a habit of it, okay? I like to be in control, hmm?"
        "She winks at you, her eyes sparkling with teasing as she asserts her dominance."
    return

label vt_wild_sex_accept(the_person, the_position):
    if the_person.sluttiness > 70:
        if the_person.obedience < 70:
            "[the_person.possessive_title!c] gives you a sultry, seductive smile, her eyes sparkling with mischief."
            the_person "Let's do it, [the_person.mc_title]. Once you've had your fill, I have a few ideas we could try out, hmm?"
            "She winks at you, her body language inviting you to take control."
        else:
            if the_position.skill_tag == "Foreplay":
                "[the_person.possessive_title!c] looks up at you with a playful, teasing expression, her voice barely above a whisper."
                the_person "I was hoping you would suggest that, [the_person.mc_title]... just thinking about it gets me excited, hmm?"
                "She bites her lip, her eyes sparkling with desire as she gazes up at you."
            elif the_position.skill_tag == "Oral":
                if "getting head" in the_position.opinion_tags:
                    "[the_person.possessive_title!c] screams with excitement, her voice echoing through the room."
                    the_person "Oh [the_person.mc_title], get down there and make me cum my brains out, hmm? I need it, I need it now!"
                else:
                    "[the_person.possessive_title!c] drops to her knees, her eyes locked on your crotch, her voice husky and seductive."
                    the_person "Come here, [the_person.mc_title]... I need to suck on that lovely dick right now, hmm? I'm starving for it!"
            else:
                "[the_person.possessive_title!c] looks up at you with a sultry, seductive expression, her voice barely above a whisper."
                the_person "Oh yes, [the_person.mc_title]... I need you to fuck me hard and deep, hmm? I need to feel you inside me, filling me up!"
    else:
        "[the_person.possessive_title!c] smiles, a playful, teasing smile spreading across her face."
        the_person "Come here [the_person.mc_title], let's do it, hmm? I'm ready for you, I'm ready to feel you inside me."
        "She opens her arms, inviting you to take her, her body language screaming with desire."
    return

label vt_wild_sex_obedience_accept(the_person):
    if the_person.sluttiness > 70:
        "[the_person.possessive_title!c] looks up at you with a sultry, seductive expression, her voice barely above a whisper."
        the_person "God, what have you done to me, [the_person.mc_title]? I should say no, but... I just want you to use me however you want, hmm?"
        "She bites her lip, her eyes sparkling with desire as she gazes up at you, her body language screaming with submission."
    else:
        if the_person.obedience > 180:
            "[the_person.possessive_title!c] looks up at you with a demure, submissive expression, her voice soft and obedient."
            the_person "If that's what you want to do, [the_person.mc_title], then I will do what you tell me to do, hmm?"
            "She bows her head, her eyes cast downward in submission, her body language screaming with obedience."
        else:
            "[the_person.possessive_title!c] grins, a playful, teasing smile spreading across her face."
            the_person "I shouldn't... but if you want to try it out, [the_person.mc_title], I'm game, hmm? Try everything once, right?"
            "She winks at you, her eyes sparkling with mischief as she invites you to take control, her body language daring you to try something new."
    return

label vt_wild_sex_gentle_reject(the_person):
    if the_person.sluttiness > 50:
        "[the_person.possessive_title!c] looks up at you with a sultry, seductive expression, her voice barely above a whisper."
        the_person "Not yet, [the_person.mc_title]... get me warmed up first, hmm? I want to feel the heat, the passion, the excitement..."
        "She bites her lip, her eyes sparkling with desire as she gazes up at you, her body language screaming with anticipation."
    else:
        "[the_person.possessive_title!c] looks up at you with a hesitant, uncertain expression, her voice soft and cautious."
        the_person "Wait, [the_person.mc_title]... I just... I don't think I'm ready for this, hmm? I want to fool around, but let's keep it casual, okay?"
        "She takes a step back, her eyes darting around the room as she tries to process her feelings, her body language screaming with nervousness."
        "[the_person.possessive_title!c] looks up at you with a pleading expression, her voice barely above a whisper."
        the_person "Let's just take it slow, okay? I want to have fun, but I don't want to rush into anything, hmm?"
    return

label vt_wild_sex_angry_reject(the_person):
    if the_person.has_significant_other:
        "[the_person.possessive_title!c] looks up at you with a fierce, angry expression, her voice firm and commanding."
        the_person "What? I have a [the_person.so_title], so you can forget about doing anything like that, [the_person.mc_title]. Ever, hmm?"
        "She glares at you, her eyes flashing with anger and possessiveness, then turns and walks away, her body language screaming with rejection."
    elif the_person.sluttiness < 20:
        "[the_person.possessive_title!c] looks up at you with a shocked, outraged expression, her voice rising to a scream."
        the_person "I'm sorry, what!? No, you've massively misread the situation, [the_person.mc_title]! Get the fuck away from me, hmm?"
        "[the_person.possessive_title!c] glares at you, her eyes blazing with anger and indignation, then steps back, her body language screaming with revulsion."
    else:
        "[the_person.possessive_title!c] looks up at you with a disgusted, appalled expression, her voice dripping with contempt."
        the_person "What? That's fucking disgusting, [the_person.mc_title]! I can't believe you'd even suggest that to me, hmm?"
        "[the_person.possessive_title!c] glares at you, her eyes flashing with anger and disgust, then steps back, her body language screaming with rejection and disgust."
    return

label vt_wild_seduction_response(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] gives you a sultry, seductive smile, her voice barely above a whisper."
            the_person "Oh, [the_person.mc_title]... I think I know what you need right now, hmm? Let me take care of you, I'll make sure you're satisfied."
            "She bats her eyelashes at you, her eyes sparkling with desire as she invites you to indulge in your desires."
        else:
            "[the_person.possessive_title!c] looks up at you with a hesitant, uncertain expression, her voice soft and cautious."
            the_person "Right now, [the_person.mc_title]? Okay, lead the way, I guess... I'm not sure what to expect, but I'll follow you."
            "She takes a step back, her eyes darting around the room as she tries to process her feelings, her body language screaming with nervousness."
    else:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] gives you a playful, teasing smile, her voice husky and seductive."
            the_person "Mmm, [the_person.mc_title]... you're feeling as horny as me then? Come on, let's go, hmm? I know just the place to satisfy our desires."
            "[the_person.possessive_title!c] takes your hand and leads you off to find some place out of the way, her body language screaming with excitement and anticipation."
        elif the_person.sluttiness > 10:
            "[the_person.possessive_title!c] raises an eyebrow, a hint of mischief in her voice, her eyes sparkling with teasing."
            the_person "I know that look you're giving me, [the_person.mc_title]... I think I know what you want, hmm? And I'm not sure if I'm going to give it to you... yet."
        else:
            "[the_person.possessive_title!c] sighs, a hint of resignation in her voice, her eyes rolling in exasperation."
            the_person "[mc.name], I know what you mean... Okay, I can spare a few minutes, hmm? But don't expect me to go all out, I'm not in the mood for games."
    return

label vt_wild_seduction_accept_crowded(the_person):
    if not the_person.has_significant_other:
        if the_person.sluttiness < 20:
            "[the_person.possessive_title!c] looks around nervously, her voice barely above a whisper."
            the_person "Alright, [the_person.mc_title]... let's slip away for a few minutes and you can convince me a little more, hmm?"
            "She glances around the room, her eyes darting towards the exit as she searches for a way to escape the crowd."
        elif the_person.sluttiness < 50:
            "[the_person.possessive_title!c] smiles mischievously, her voice husky and seductive."
            the_person "Come on, [the_person.mc_title]... I know someplace nearby where we can get a few minutes privacy, hmm?"
            "She winks at you, her eyes sparkling with teasing as she invites you to follow her."
        else:
            "[the_person.possessive_title!c] screams with excitement, her voice echoing through the room."
            the_person "Oh my god, [the_person.mc_title]! I hope you aren't planning on making me wait, because I don't know if I can, hmm?"
            "She grabs your arm, her eyes blazing with desire as she pulls you towards her, her body language screaming with urgency."
    else:
        if the_person.sluttiness + (5*the_person.opinion.cheating_on_men) > 50:
            "[the_person.possessive_title!c] laughs, a wild, reckless sound, her voice husky and seductive."
            the_person "Fuck, [the_person.mc_title]... let's get this party started, hmm?"
            "She grabs your hand, her eyes sparkling with mischief as she pulls you towards her, her body language screaming with excitement."
            the_person "I hope you don't mind that I've got a [the_person.so_title], because I sure as hell don't right now, hmm?"
        else:
            "[the_person.possessive_title!c] looks around nervously, her voice barely above a whisper."
            the_person "God damn it, [the_person.mc_title]... you're bad for me, hmm? Come on, we need to go somewhere quiet so my [the_person.so_title] doesn't find out about this."
            "She glances around the room, her eyes darting towards the exit as she searches for a way to escape the crowd, her body language screaming with guilt and anxiety."
    return

label vt_wild_seduction_accept_alone(the_person):
    if not the_person.has_significant_other:
        if the_person.sluttiness < 20:
            "[the_person.possessive_title!c] smiles, a sly, mischievous smile spreading across her face."
            the_person "Well, [the_person.mc_title]... I think you deserve a chance to impress me, hmm?"
            "She raises an eyebrow, her eyes sparkling with teasing as she invites you to try and win her over."
        elif the_person.sluttiness < 50:
            "[the_person.possessive_title!c] laughs, a playful, flirtatious sound, her voice husky and seductive."
            the_person "Mmm, [the_person.mc_title]... well let's get this party started and see where it goes, hmm?"
            "She winks at you, her eyes sparkling with mischief as she invites you to join her in a night of fun and adventure."
        else:
            "[the_person.possessive_title!c] screams with excitement, her voice echoing through the room."
            the_person "Fuck, [the_person.mc_title]! I'm glad you're as horny as I am right now, hmm? Come on, I can't wait any more!"
            "She grabs your arm, her eyes blazing with desire as she pulls you towards her, her body language screaming with urgency and need."
    else:
        if the_person.sluttiness + (5*the_person.opinion.cheating_on_men) > 50:
            "[the_person.possessive_title!c] laughs, a wild, reckless sound, her voice husky and seductive."
            the_person "Fuck, [the_person.mc_title]... you know how to turn me on in ways my [the_person.so_title] never can, hmm? Come here!"
            "She grabs your hand, her eyes sparkling with mischief as she pulls you towards her, her body language screaming with excitement and desire."
        else:
            "[the_person.possessive_title!c] looks up at you with a guilty, conflicted expression, her voice barely above a whisper."
            the_person "You're such bad news, [the_person.mc_title]... I have a [the_person.so_title], but all I can ever think of is you, hmm?"
            "She bites her lip, her eyes sparkling with desire and guilt as she struggles with her feelings, her body language screaming with tension and anxiety."
    return

label vt_wild_seduction_refuse(the_person):
    if the_person.sluttiness < 20:
        "[the_person.possessive_title!c] looks up at you with a dismissive, uninterested expression, her voice firm and unyielding."
        the_person "Sorry [the_person.mc_title], I'm not really in the mood to flirt or fool around, hmm? Don't take it personally."
        "[the_person.possessive_title!c] shrugs unapologetically, her eyes flashing with a hint of annoyance as she turns away from you."

    elif the_person.sluttiness < 50:
        "[the_person.possessive_title!c] smiles, a sly, teasing smile spreading across her face."
        the_person "I'll admit it, [the_person.mc_title]... you're tempting me, but I'm not in the mood to fool around right now, hmm? Maybe some other time though, I think we could have a lot of fun together."
        "She winks at you, her eyes sparkling with mischief as she invites you to try again another time."

    else:
        "[the_person.possessive_title!c] laughs, a wild, flirtatious sound, her voice husky and seductive."
        the_person "Shit, [the_person.mc_title]... that sounds like a lot of fun, but I'm not feeling it right now, hmm? Hang onto that thought and we can fool around some other time, okay?"
        "She blows you a kiss, her eyes sparkling with teasing as she turns away from you, her body language screaming with confidence and seduction."
    return

label vt_wild_compliment_response(the_person):
    mc.name "Hey [the_person.fname]. How are you? You're looking quite perky today."
    if the_person.is_at_work:
        if (the_person.is_employee or the_person.is_strip_club_employee) and the_person.is_wearing_uniform:
            call vt_wild_flirt_response_employee_uniform_low(the_person) from _call_vt_wild_flirt_response_employee_uniform_low_compliment_response
        elif the_person.is_at_job(prostitute_job):
            "[the_person.possessive_title!c] gives you a sultry, seductive smile, her voice husky and inviting."
            the_person "I'm good babe, how about you and me have some fun together, hmm? I'm always up for a good time."
            "She winks at you, her eyes sparkling with mischief as she invites you to indulge in her services."
        elif the_person.sluttiness > 50:
            "[the_person.possessive_title!c] laughs, a playful, flirtatious sound, her voice husky and seductive."
            the_person "I'm doing great, [the_person.mc_title]. And you are looking quite yummy yourself, hmm? Maybe we can grab lunch together and see where things go?"
            "She bats her eyelashes at you, her eyes sparkling with teasing as she invites you to join her for a meal."
        else:
            "[the_person.possessive_title!c] blushes, her face flushing with embarrassment, her voice soft and demure."
            the_person "Oh, stop it, you charmer, hmm? But thanks, I'm good. Just trying to get through my shift without too much trouble."
            "She smiles, a shy, hesitant smile spreading across her face as she tries to deflect your attention."
    else:
        "[the_person.possessive_title!c] smiles, a warm, friendly smile spreading across her face."
        the_person "Aww, thank you for noticing, [the_person.mc_title]. I'm doing well, just enjoying my day and trying to stay out of trouble, hmm?"
        "She laughs, a playful, carefree sound, her eyes sparkling with amusement as she chats with you."
    "You chat with [the_person.possessive_title] for a while and slip in a compliment when you can. She is enjoying all the attention, her body language screaming with confidence and pleasure."
    return

label vt_wild_compliment_response_girlfriend(the_person):
    mc.name "Hey [the_person.title]. You're looking very sexy this [StringInfo.time_of_day_string]."
    if the_person.is_at_work:
        if (the_person.is_employee or the_person.is_strip_club_employee) and the_person.is_wearing_uniform:
            call vt_wild_flirt_response_employee_uniform_mid(the_person) from _call_vt_wild_flirt_response_employee_uniform_mid_compliment_response_girlfriend
            $ the_person.call_dialogue("flirt_response_employee_uniform_mid")
        elif the_person.sluttiness > 50:
            "[the_person.possessive_title!c] gives you a sultry, seductive smile, her voice husky and inviting."
            the_person "Mmm, thank you, [the_person.mc_title]... Wanna find out how sexy I am, hmm? Maybe we can sneak away and I'll show you."
            "She winks at you, her eyes sparkling with mischief as she invites you to indulge in a little workplace romance."
        else:
            "[the_person.possessive_title!c] blushes, her face flushing with embarrassment, her voice soft and demure."
            the_person "Ah, really, [the_person.mc_title]? Thanks, I guess I'm just trying to get through my shift without too much trouble, hmm? You are not looking so bad yourself, though."
            "She smiles, a shy, hesitant smile spreading across her face as she tries to deflect your attention."
    else:
        "[the_person.possessive_title!c] smiles, a warm, flirtatious smile spreading across her face."
        the_person "Aww, thank you, [the_person.mc_title]... I'm good. You are looking quite hot yourself, hmm? Maybe we can do something about that later."
        "She winks at you, her eyes sparkling with teasing as she invites you to join her for a little fun and games."
    "You chat with [the_person.possessive_title] for a while, making sexy references where you can. She is quite charmed by your efforts, her body language screaming with confidence and pleasure."
    return

label vt_wild_compliment_response_affair(the_person):
    mc.name "Hey [the_person.title]. You're looking absolutely gorgeous this [StringInfo.time_of_day_string]."
    if the_person.is_at_work:
        if (the_person.is_employee or the_person.is_strip_club_employee) and the_person.is_wearing_uniform:
            call vt_wild_flirt_response_employee_uniform_mid(the_person) from _call_vt_wild_flirt_response_employee_uniform_mid_compliment_response_affair
        elif the_person.sluttiness > 50:
            "[the_person.possessive_title!c] gives you a sultry, seductive smile, her voice husky and inviting."
            the_person "Mmmm, thank you [the_person.mc_title]... wanna go somewhere a little more private, so you can make me feel how gorgeous I am, hmm?"
            "She winks at you, her eyes sparkling with mischief as she invites you to indulge in a little workplace romance, her body language screaming with desire and anticipation."
        else:
            "[the_person.possessive_title!c] blushes, her face flushing with embarrassment, her voice soft and demure."
            the_person "Hush, [the_person.mc_title]!...You really like my outfit, hmm? I can show you what I'm wearing underneath... but you have to promise not to tell anyone, okay?"
            "She looks around nervously, her eyes darting towards the exit as she tries to gauge the risk of getting caught, her body language screaming with excitement and nervousness."
    else:
        "[the_person.possessive_title!c] smiles, a warm, flirtatious smile spreading across her face."
        the_person "You like this, [the_person.mc_title]? Take me to dinner and we can explore other parts... of the city, hmm?"
        "She winks at you, her eyes sparkling with teasing as she invites you to join her for a night out on the town, her body language screaming with confidence and seduction."
    "You keep chatting with [the_person.possessive_title] for a while, slipping in a few more compliments. She is quite enamoured by your attentiveness, her body language screaming with pleasure and desire."
    return

label vt_wild_flirt_response(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] gives you a sultry, seductive smile, her voice husky and inviting."
            the_person "You know that all you have to do is ask, [the_person.mc_title]... and it's all yours, hmm?"
            "She leans in close to you, her hot breath sending shivers down your spine as she teases you with her words."
        else:
            "[the_person.possessive_title!c] blushes, her face flushing with embarrassment, her voice soft and demure."
            the_person "Thank you, [the_person.mc_title]... I'm glad you're enjoying the view, hmm?"
            "She looks up at you with a shy, hesitant expression, her eyes sparkling with pleasure as she tries to play it cool."
    elif the_person.has_significant_other:
        if the_person.sluttiness + (the_person.opinion.cheating_on_men*5) > 50:
            "[the_person.possessive_title!c] winks at you, her eyes sparkling with mischief as she spins around, giving you a full look at her body."
            the_person "Then why don't you do something about it, [the_person.mc_title]? Come on, we don't have to tell my [the_person.so_title] anything at all, right, hmm?"
            "She laughs, a playful, flirtatious sound, as she invites you to indulge in a little secret affair."
        else:
            "[the_person.possessive_title!c] looks up at you with a warning expression, her voice firm and cautionary."
            the_person "You're playing with fire, [the_person.mc_title]... I've got a [the_person.so_title], and I don't think he'd appreciate you flirting with me, hmm?"
            mc.name "What about you, do you appreciate it?"
            "[the_person.possessive_title!c] gives a coy smile and shrugs, her eyes sparkling with teasing."
            the_person "Maybe I do, [the_person.mc_title]... maybe I do."
    else:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] smiles at you, her eyes sparkling with invitation as she spins around, giving you a full look at her body."
            the_person "Then why don't you do something about it, [the_person.mc_title]? Come on, all you have to do is ask, hmm?"
            "She winks at you, her eyes sparkling with mischief as she invites you to take the next step."
        else:
            "[the_person.possessive_title!c] looks up at you with a playful, teasing expression, her voice husky and seductive."
            the_person "Well thank you, [the_person.mc_title]... play your cards right and maybe you'll get to see a little bit more, hmm?"
            the_person "You'll have to really impress me though, I have high standards... but I think you might just be up to the challenge, hmm?"
            "She smiles, a sly, flirtatious smile, as she invites you to try and win her over."
    return

label vt_wild_flirt_response_employee_uniform_low(the_person):
    if the_person.is_wearing_forced_uniform:
        "[the_person.possessive_title!c] looks up at you with a hint of annoyance, her voice husky and seductive."
        the_person "I'm sure you like it, [the_person.mc_title]... I'm practically naked, hmm?"
        mc.name "I know you don't like it, but I needed to make a point."
        "[the_person.possessive_title!c] rolls her eyes, a playful, teasing glint in her eye."
        the_person "I know, I know... you're the boss, after all."
        $ mc.change_locked_clarity(5)
        "She smiles and gives you a quick turn to either side, showing off her body, her movements fluid and seductive."
    elif the_person.judge_outfit(the_person.outfit):
        #She's in uniform and likes how it looks.
        "[the_person.possessive_title!c] beams with pride, her voice bubbly and enthusiastic."
        the_person "Thanks, [the_person.mc_title]! I think I look pretty cute in it too, hmm?"
        the_person "It's nice to work somewhere where I can show off a little... and get appreciated for it, too."
        $ mc.change_locked_clarity(5)
        "She smiles and gives you a quick turn to either side, showing off her hips, her body language screaming with confidence and seduction."
    else:
        #She's in uniform, but she thinks it's a little too slutty.
        if the_person.vagina_visible:
            # Her pussy is on display.
            "[the_person.possessive_title!c] looks up at you with a hint of embarrassment, her voice barely above a whisper."
            the_person "I'm sure you like it, [the_person.mc_title]... I'm practically naked, hmm?"
            mc.name "Well, you know that it's..."
            "[the_person.possessive_title!c] interrupts, her voice husky and seductive."
            the_person "I know, I know... it's company policy, hmm? I'm not complaining, exactly... it's kind of fun, actually."
            mc.name "Give it some time and you'll get used to it."
            $ mc.change_locked_clarity(5)
            "She smiles and nods, her eyes sparkling with mischief."
        elif the_person.tits_visible:
            # Her tits are out
            "[the_person.possessive_title!c] laughs, a playful, flirtatious sound, her voice husky and seductive."
            the_person "Thanks, [the_person.mc_title]! I'm still getting used to being so... exposed in this uniform, hmm? At least I don't have to wear a bra, right?"
            mc.name "You look incredible and you're comfortable. I call that a success."
            $ mc.change_locked_clarity(5)
            "She shrugs, her shoulders barely rising off her body, her eyes sparkling with teasing."
        elif the_person.underwear_visible:
            # Her underwear is visible.
            "[the_person.possessive_title!c] smiles, a sly, flirtatious smile spreading across her face."
            the_person "Thanks, [the_person.mc_title]! I probably would have picked something that kept me a little more covered, but at least our uniform is comfortable, hmm?"
            mc.name "It may be a little unconventional, but you look fantastic. You've got exactly the right kind of body for it."
            "[the_person.possessive_title!c] raises an eyebrow, a hint of surprise in her voice."
            the_person "Well that's good to know, [the_person.mc_title]... I guess I'll just have to get used to being a little more... exposed, hmm?"
            $ mc.change_locked_clarity(5)
            "She smiles and gives you a quick turn to either side, showing off her body, her movements fluid and seductive."
        else:
            # It's just generally slutty.
            "[the_person.possessive_title!c] smiles, a warm, flirtatious smile spreading across her face."
            the_person "Well thank you, [the_person.mc_title]! Our uniforms are a little bold for my taste, but I'm glad I look good in it, hmm?"
            $ mc.change_locked_clarity(5)
            "She smiles and gives you a quick turn to either side, showing off her body for you, her body language screaming with confidence and seduction."
    return

label vt_wild_flirt_response_employee_uniform_mid(the_person):
    if the_person.is_wearing_forced_uniform:
        $ mc.change_locked_clarity(10)
        if the_person.vagina_visible:
            "[the_person.possessive_title!c] strikes a pose, her voice husky and seductive."
            the_person "I mean, look at me, [the_person.mc_title]! I feel like you should be throwing twenties at me every time I walk away, hmm?"
            "She winks at you, her eyes sparkling with mischief as she shows off her body."
        elif the_person.tits_visible:
            "[the_person.possessive_title!c] laughs, a playful, flirtatious sound, her voice husky and seductive."
            the_person "I mean, look at me, [the_person.mc_title]! I feel like you should be tucking a twenty into my underwear every time I want to talk to you, hmm?"
            "She winks at you, her eyes sparkling with teasing as she jiggles her breasts for your attention."
        else:
            "[the_person.possessive_title!c] smiles, a sly, flirtatious smile spreading across her face."
            the_person "I mean, look at it, [the_person.mc_title]! I feel like an underwear model every time I get dressed for work, hmm?"
            "She strikes a pose, her body language screaming with confidence and seduction as she shows off her outfit."
        mc.name "Rules are rules and I can't make any exceptions, even if they look good."
        "[the_person.possessive_title!c] sighs and nods, her eyes sparkling with mischief."
        the_person "Yeah, I know, [the_person.mc_title]. At least you're having a good time. I don't mind that so much, hmm?"
        "She winks at you, her eyes sparkling with teasing as she invites you to enjoy the view."
    elif the_person.judge_outfit(the_person.outfit):
        $ mc.change_locked_clarity(10)
        if the_person.tits_visible:
            "[the_person.possessive_title!c] raises an eyebrow, a hint of teasing in her voice."
            the_person "Are you sure you don't mean my tits look good in this outfit, [the_person.mc_title]?"
            "She winks and wiggles her shoulders, setting her boobs jiggling for you, her eyes sparkling with mischief."
            mc.name "All of you looks good, tits included."
            "[the_person.possessive_title!c] laughs, a playful, flirtatious sound, her voice husky and seductive."
            the_person "Good answer, [the_person.mc_title]. I think these uniforms are pretty hot too. You've got some good fashion sense, hmm?"
            "She smiles, a sly, flirtatious smile spreading across her face as she invites you to admire her outfit."
        else:
            "[the_person.possessive_title!c] beams with pride, her voice bubbly and enthusiastic."
            the_person "Aw, thanks, [the_person.mc_title]! I think your uniforms look pretty hot on me too. You've got some good fashion sense, hmm?"
            "She twirls around, her skirt flying up as she shows off her outfit, her body language screaming with confidence and seduction."
        the_person "Maybe I'll invite you shopping one day and you can tell me what else you want to see me in, hmm?"
        mc.name "Sounds like a good time."
        "[the_person.possessive_title!c] smiles, a warm, flirtatious smile spreading across her face."
        the_person "I thought you'd say that, [the_person.mc_title]. I'll have to make sure to wear something extra special, just for you, hmm?"
    else:
        "[the_person.possessive_title!c] smiles, a sly, flirtatious smile spreading across her face."
        the_person "Thanks, but I think these uniforms show off just a little too much of my fabulous body, hmm?"
        $ mc.change_locked_clarity(10)
        if the_person.vagina_visible:
            "[the_person.possessive_title!c] strikes a pose, her voice husky and seductive."
            the_person "I mean, look at me, [the_person.mc_title]! I feel like you should be throwing twenties at me every time I walk away, hmm?"
            "She winks at you, her eyes sparkling with mischief as she shows off her body."
        elif the_person.tits_visible:
            "[the_person.possessive_title!c] laughs, a playful, flirtatious sound, her voice husky and seductive."
            the_person "I mean, look at me, [the_person.mc_title]! I feel like you should be tucking a twenty into my underwear every time I want to talk to you, hmm?"
            "She winks at you, her eyes sparkling with teasing as she jiggles her breasts for your attention."
        else:
            "[the_person.possessive_title!c] smiles, a sly, flirtatious smile spreading across her face."
            the_person "I mean, look at it, [the_person.mc_title]! I feel like an underwear model every time I get dressed for work, hmm?"
            "She strikes a pose, her body language screaming with confidence and seduction as she shows off her outfit."
        mc.name "I understand, but I promise it's important for the business."
        "[the_person.possessive_title!c] sighs and nods, her eyes sparkling with mischief."
        the_person "Yeah, I know, [the_person.mc_title]. At least you're having a good time. I don't mind that so much, hmm?"
        "She winks at you, her eyes sparkling with teasing as she invites you to enjoy the view."
    return

label vt_wild_flirt_response_low(the_person):
    #She's in her own outfit.
    "[the_person.possessive_title!c] beams with pride, her voice bubbly and enthusiastic."
    the_person "Thanks, [the_person.mc_title]! It's really cute, right? I just got it yesterday and I couldn't wait to wear it out."
    $ the_person.draw_person(position = "walking_away")
    $ mc.change_locked_clarity(5)
    "She strikes a pose, 'striking a pose and giving you a sassy smile' as she shows off her outfit from every angle, her hips swaying seductively as she walks away."
    $ the_person.draw_person()
    "[the_person.possessive_title!c] turns back to you, her eyes sparkling with mischief as she invites you to admire her outfit."
    the_person "So, what do you think? Does it make me look good, hmm?"
    return

label vt_wild_flirt_response_low1(the_person):
    if the_person.has_significant_other:
        "[the_person.possessive_title!c] looks up at you with a warning expression, her voice firm and cautionary."
        the_person "You're playing with fire, [the_person.mc_title]... I've got a [the_person.so_title], and I don't think he'd appreciate you flirting with me, hmm?"
        mc.name "What about you, do you appreciate it?"
        "[the_person.possessive_title!c] gives a coy smile and shrugs, her eyes sparkling with teasing."
        the_person "Maybe I do, [the_person.mc_title]... maybe I do."
        "She leans in close to you, her voice barely above a whisper."
        the_person "But don't think for a second that I'm going to make it easy for you, hmm? You'll have to work hard to impress me."

    else:
        "[the_person.possessive_title!c] smiles, a sly, flirtatious smile spreading across her face."
        the_person "Well thank you, [the_person.mc_title]... play your cards right and maybe you'll get to see a little bit more, hmm?"
        the_person "You'll have to really impress me though, I have high standards... but I think you might just be up to the challenge, hmm?"
        "She winks at you, her eyes sparkling with mischief as she invites you to try and win her over."
    $ mc.change_locked_clarity(5)
    return

label vt_wild_flirt_response_mid(the_person):
    if mc.location.person_count > 1 and the_person.effective_sluttiness("kissing") < (25 - (5*the_person.opinion.public_sex)):
        $ mc.change_locked_clarity(10)
        if the_person.tits_visible:
            "[the_person.possessive_title!c] raises an eyebrow, a hint of teasing in her voice."
            the_person "Are you sure you don't mean my tits look good in this outfit, [the_person.mc_title]?"
            "She winks and wiggles her shoulders, setting her boobs jiggling for you, her eyes sparkling with mischief."
            mc.name "All of you looks good, tits included."
            "[the_person.possessive_title!c] laughs, a playful, flirtatious sound, her voice husky and seductive."
            the_person "Good answer, [the_person.mc_title]. I knew you would like this look when I was picking it out this morning, hmm?"
            "She smiles, a sly, flirtatious smile spreading across her face as she invites you to admire her outfit."
        else:
            "[the_person.possessive_title!c] beams with pride, her voice bubbly and enthusiastic."
            the_person "Aw, thanks, [the_person.mc_title]! I thought this was a pretty hot look when I was getting dressed this morning, hmm?"
            "She twirls around, her skirt flying up as she shows off her outfit, her body language screaming with confidence and seduction."
        the_person "Maybe I'll invite you shopping one day, so you can tell me what else you want to see me in, hmm?"
        mc.name "I can think of a few things already."
        "[the_person.possessive_title!c] winks at you, her eyes sparkling with teasing."
        the_person "I'm sure you can, [the_person.mc_title]... I'm sure you can."
    else:
        "[the_person.possessive_title!c] smiles, a sly, flirtatious smile spreading across her face."
        the_person "Thanks, [the_person.mc_title]... I thought I looked pretty hot in it too, hmm?"
        the_person "You want a better look, right? Here, how does it make my ass look?"
        $ the_person.draw_person(position = "back_peek")
        $ mc.change_locked_clarity(10)
        "[the_person.possessive_title!c] looks back at you over her shoulder, her eyes sparkling with mischief."
        the_person "Good, right?"
        mc.name "Fantastic. I wish I could get an even better look at it."
        "[the_person.possessive_title!c] smiles and turns back to face you, her body language screaming with confidence and seduction."
        $ the_person.draw_person()
        the_person "I'm sure you do, [the_person.mc_title]... Take me out for a drink and maybe we can work something out, hmm?"
        "She winks at you, her eyes sparkling with teasing as she invites you to take her out on a date."
    return

label vt_wild_flirt_response_mid1(the_person):
    $ mc.change_locked_clarity(10)
    "[the_person.possessive_title!c] beams with pride, her voice bubbly and enthusiastic."
    the_person "Thanks, [the_person.mc_title]... I do look amazing in this outfit, hmm?"
    "She strikes a pose, her body language screaming with confidence and seduction as she shows off her outfit."
    if (the_person.has_skirt or the_person.has_dress) and not the_person.has_thigh_high_socks:
        mc.name "You could change it up with some high stockings, I would like to see that."
        "[the_person.possessive_title!c] raises an eyebrow, a hint of teasing in her voice."
        the_person "I bet you would, [the_person.mc_title]... you naughty boy, hmm?"
        "She winks at you, her eyes sparkling with mischief as she teases you with her words."
    mc.name "How about you and me go and grab a coffee sometime?"
    if the_person.has_significant_other:
        "[the_person.possessive_title!c] smiles, a sly, flirtatious smile spreading across her face."
        the_person "Sure, [the_person.mc_title]... my [the_person.so_title] doesn't mind, hmm?"
        "She leans in close to you, her voice barely above a whisper."
        the_person "But don't think for a second that I'm going to make it easy for you, hmm? You'll have to work hard to impress me."
    else:
        "[the_person.possessive_title!c] laughs, a playful, flirtatious sound, her voice husky and seductive."
        the_person "Why not, [the_person.mc_title]... I could use a pick-me-up once in a while, hmm?"
        "She smiles, a warm, inviting smile spreading across her face as she invites you to spend time with her."
    the_person "Just let me know when, [the_person.mc_title]... I would love to, hmm?"
    "She winks at you, her eyes sparkling with teasing as she invites you to take her out on a date."
    return

label vt_wild_flirt_response_high(the_person):
    if mc.location.person_count > 1 and the_person.effective_sluttiness() < (25 - (5*the_person.opinion.public_sex)): # There are other people here, if she's not slutty she asks if you want to find somewhere quiet
        "[the_person.possessive_title!c] smiles mischievously, her voice husky and seductive."
        the_person "Driving you crazy, huh? Well..."
        "She glances around, her eyes sparkling with mischief as she checks to see if anyone is watching."
        the_person "We'll have to do something about that, but not here, hmm?"
        menu:
            "Find somewhere more quiet\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                mc.name "Then let's find somewhere that isn't here."
                "[the_person.possessive_title!c] laughs, a playful, flirtatious sound, her voice husky and seductive."
                the_person "Eager, huh? Alright, let's go find somewhere, hmm?"
                call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_vt_wild_flirt_response_high_2
                "[the_person.possessive_title!c] looks up at you with a sly, flirtatious smile, her voice barely above a whisper."
                the_person "So... Now what's your plan, hmm?"

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
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from vt_wild_call_fuck_person_49
                else:
                    if the_person.has_taboo("touching_body"):
                        $ the_person.call_dialogue("touching_body_taboo_break")
                        $ the_person.break_taboo("touching_body")
                        "You take her hand and pull her close against you. She looks into your eyes."
                    else:
                        "You answer by pulling her close against you."
                    call fuck_person(the_person, private = True, start_position = standing_grope, skip_intro = True) from _call_fuck_person_vt_wild_flirt_grope

                $ the_person.call_dialogue("sex_review", the_report = _return)
                call mc_restore_original_location(the_person) from _call_mc_restore_original_location_vt_wild_flirt_response_high_2

            "Just flirt":
                mc.name "Not here, huh? How about back at your place then?"
                "[the_person.possessive_title!c] raises an eyebrow, a hint of teasing in her voice."
                the_person "Bold. I like it. Maybe if you buy me dinner you'll get your chance, hmm?"
                "She winks at you, her eyes sparkling with mischief as she invites you to take her out on a date."

    else:
        if mc.location.person_count == 1: #You're alone, so she just didn't meet the sluttiness threshold
            "[the_person.possessive_title!c] bites her lower lip and glances around, confirming you're alone."
            the_person "Well it's just the two of us here, so now's your chance to find out. What's your plan, hmm?"
            "She looks up at you with a sly, flirtatious smile, her voice barely above a whisper."

        else:  # You aren't alone but she's still into it.
            "[the_person.possessive_title!c] smiles, a sly, flirtatious smile spreading across her face."
            the_person "Feeling bold today, huh? Well I think your chances are pretty good, hmm?"
            if the_person.has_large_tits: #Bounces her tits for you
                $ mc.change_locked_clarity(15)
                "[the_person.title] grabs her tits and jiggles them for you, her eyes sparkling with mischief."
                the_person "Maybe I can get these girls out for you. Does that sound nice, hmm?"
                "She winks at you, her body language screaming with confidence and seduction."

            else: #No big tits, so she can't bounce them (as much)
                "[the_person.title] runs her hands over her hips sensually, obviously encouraging you to take things further."
                "She looks up at you with a sly, flirtatious smile, her voice barely above a whisper."

        menu:
            "Touch her" if not the_person.is_willing(kissing):
                "You step closer to [the_person.title] and move your hands down her waist."
                if the_person.has_taboo("touching_body"):
                    $ the_person.call_dialogue("touching_body_taboo_break")
                    $ the_person.break_taboo("touching_body")

                call fuck_person(the_person, start_position = standing_grope, private = False) from _call_fuck_person_flirt_response_vt_wild_touching

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

                call mc_move_to_private_location(the_person) from  _call_mc_move_to_private_location_vt_wild_flirt_response_high
                call fuck_person(the_person, start_position = kissing, private = _return, skip_intro = True) from vt_wild_call_fuck_person_50
                $ the_person.call_dialogue("sex_review", the_report = _return)
                call mc_restore_original_location(the_person) from _call_mc_restore_original_location_vt_wild_flirt_response_high

            "Just flirt":
                $ the_person.draw_person()
                mc.name "Very tempting, but you're going to have to contain yourself for now."
                "[the_person.title] pouts melodramatically, her lips jutting out in a playful expression."
                the_person "You're so cruel, [the_person.mc_title]. Maybe you can take me out to dinner to make up for it, hmm?"
                "She winks at you, her eyes sparkling with mischief as she invites you to take her out on a date."
    return

label vt_wild_flirt_response_low_energy(the_person):
    if the_person.sluttiness > 40:
        "[the_person.possessive_title!c] smiles, a sly, flirtatious smile spreading across her face, despite her exhaustion."
        the_person "Oh, thank you, darling... now I wish I wasn't so exhausted, hmm?"
        "She stretches, arching her back and extending her arms above her head, her body language screaming with seduction even in her tired state."

    else:
        "[the_person.possessive_title!c] looks up at you with a hint of apology, her voice soft and demure."
        the_person "Thank you, [the_person.mc_title]... I'm a little worn out, can we pick this up later, hmm?"
        "She yawns, covering her mouth with her hand, her eyes sparkling with mischief even in her exhaustion."
    return

label vt_wild_flirt_response_girlfriend(the_person):
    # Lead in: mc.name "You're so beautiful [the_person.title], I'm so lucky to have a woman like you in my life."
    if mc.location.person_count > 1:
        # There are other people around, so she'll only start making out with you if she's slutty.
        if the_person.effective_sluttiness("kissing") < (25 - (5*the_person.opinion.public_sex)):
            # Not very slutty, so she wants to find somewhere private
            "[the_person.possessive_title!c] smiles, a sly, flirtatious smile spreading across her face."
            the_person "Oh my god, you're such a sap, [the_person.mc_title]. Come here."
            "She pulls you against her and kisses you intensely, her lips pressing against yours with a fierce passion."
            "She smiles when she breaks the kiss a moment later, her eyes sparkling with mischief."
            the_person "There, that's how you should show a woman how you feel, hmm?"
            mc.name "Uh huh, I think I've got the idea..."
            "You put your arms around her and kiss her back, matching her own intensity, your bodies pressed together in a passionate embrace."
            the_person "Mmm, yeah you've got it, [the_person.mc_title]. Don't get too excited though, we have to wait until we're alone to do anything more, hmm?"
            menu:
                "Find somewhere more quiet\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                    mc.name "Why wait? Come on, I'm sure we can find somewhere quiet."
                    "[the_person.possessive_title!c] laughs, a playful, flirtatious sound, her voice husky and seductive."
                    the_person "That eager, huh? Alright, let's go, hot stuff!"
                    "You and [the_person.possessive_title] hurry off, searching for a private spot, your hands still wrapped around each other's waists."
                    call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_vt_wild_flirt_response_girlfriend_2
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from vt_wild_call_fuck_person_76
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_vt_wild_flirt_response_girlfriend_2

                "Just flirt":
                    $ mc.change_locked_clarity(10)
                    "You reach behind [the_person.possessive_title] and grab her ass, giving it a firm squeeze, your fingers digging into her flesh."
                    mc.name "Alright, I'll be patient, [the_person.title]. This ass is worth waiting for, hmm?"
                    "She wiggles her hips back against your hand, her eyes sparkling with mischief."
                    the_person "Damn right it is, [the_person.mc_title]... you're going to have to wait a bit longer to get your hands on it, though."

        else:
            "[the_person.possessive_title!c] smiles, a sly, flirtatious smile spreading across her face."
            the_person "Well if I'm so beautiful then hurry up and kiss me, hot stuff, hmm?"
            "You put your arm around her waist and lean close, kissing her on her lips, your bodies pressed together in a passionate embrace."
            "When you break the kiss [the_person.possessive_title] sighs happily and leans her head against your shoulder, her eyes sparkling with pleasure."
            the_person "Why did you stop, [the_person.mc_title]? I was having such a good time, hmm?"
            menu:
                "Make out":
                    "You don't say a word as you lean back and kiss her again, slowly and sensually this time, your lips exploring hers with a fierce passion."
                    "[the_person.title] presses her body against you in response, grinding her hips against your thigh, her eyes sparkling with desire."

                    call mc_move_to_private_location(the_person) from  _call_mc_move_to_private_location_vt_wild_flirt_response_girlfriend
                    call fuck_person(the_person, start_position = kissing, private = _return, skip_intro = True) from vt_wild_call_fuck_person_77
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_vt_wild_flirt_response_girlfriend

                "Just flirt":
                    mc.name "I just like to tease you, [the_person.title]."
                    $ mc.change_locked_clarity(10)
                    "You reach around and grab her ass, squeezing it playfully, your fingers digging into her flesh."
                    "She pouts melodramatically and rubs your chest, her eyes sparkling with mischief."
                    the_person "Ugh, you're the worst, [the_person.mc_title]. I was already getting turned on, hmm?"

    else:
        # You're alone, so she's open to fooling around.
        "[the_person.possessive_title!c] smiles, a sly, flirtatious smile spreading across her face."
        the_person "Well you've got me all alone, [the_person.mc_title]... so how about you show me just how lucky you feel, hmm?"
        "She reaches down to your waist and cups your crotch, rubbing it gently, her eyes sparkling with desire."
        menu:
            "Kiss her":
                if the_person.has_taboo("kissing"):
                    $ the_person.call_dialogue("kissing_taboo_break")
                    $ the_person.break_taboo("kissing")

                "You put your arms around [the_person.possessive_title]'s waist and rest your hands on her ass. You pull her close and kiss her sensually, your lips exploring hers with a fierce passion."
                "She responds by pressing her body against you and grinding her hips against your thigh, her eyes sparkling with desire."
                call fuck_person(the_person, start_position = kissing, skip_intro = True) from vt_wild_call_fuck_person_78
                $ the_person.call_dialogue("sex_review", the_report = _return)
                $ the_person.review_outfit()

            "Just flirt":
                "You reach your arms around her waist and grab her ass, squeezing it playfully, your fingers digging into her flesh."
                mc.name "I'm sorry, but I'm going to make you wait a bit for that, [the_person.title]. I just like seeing you get all worked up, hmm?"
                "She pouts melodramatically, her eyes sparkling with mischief."
                the_person "Ugh, you're the worst, [the_person.mc_title]. I was already getting so turned on, hmm?"
    return

label vt_wild_flirt_response_affair(the_person):
    # Lead in: mc.name "You look so good today [the_person.title], you're making me want to do some very naughty things to you."
    if mc.location.person_count > 1: #There are other people around, she's nervous about people finding out what you're doing.
        if (the_person.opinion.cheating_on_men *15) + the_person.effective_sluttiness() > 50: #SHe's turned on by flirting in public or doesn't think anything is wrong with it
            "[the_person.possessive_title!c] bites her lower lip and looks you up and down, her eyes lingering on your crotch with a hungry gaze."
            the_person "Yeah? Well... I've got some spare time, [the_person.mc_title]. How about we slip away and you can show me what you mean, hmm?"
            menu:
                "Find somewhere more quiet\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                    mc.name "Alright, let's go."
                    "You and [the_person.title] hurry off to find a quiet spot, your hands wrapped around each other's waists as you move through the crowd."
                    call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_vt_wild_flirt_response_affair
                    $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
                    "As soon as you're alone she pulls you into a deep and passionate kiss, her lips pressing against yours with a fierce hunger."
                    $ the_person.draw_person(position = "kissing")
                    the_person "Ah... You aren't the only one having dirty thoughts, [the_person.mc_title]. You get me so fucking horny!"
                    "You wrap your arms around her waist and kiss her back, your bodies pressed together in a passionate embrace."
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from vt_wild_call_fuck_person_79
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_vt_wild_flirt_response_affair

                "Just flirt":
                    "You slide your arm around [the_person.title]'s waist and rest your hand on her ass, rubbing it gently, your fingers digging into her flesh."
                    mc.name "You'll have to wait a little bit, [the_person.title]. We don't have time for all the things I want to do to you right now, hmm?"
                    $ mc.change_locked_clarity(20)
                    "She glances around and checks to make sure nobody else is watching, then she slides her hand down your waist and to your crotch, her eyes sparkling with mischief."
                    "[the_person.possessive_title!c] massages your bulge lightly and pouts, her lips jutting out in a playful expression."
                    the_person "That's a shame, [the_person.mc_title]. I can think of so many fun things to do with this... Just don't make me wait too long, okay?"
                    the_person "I barely get any action from my [the_person.so_title], and I'm starting to feel like I'm going to explode, hmm?"
                    "You give her ass a slap before letting go, the sound echoing through the air as you tease her."
                    mc.name "It won't be too long, I promise."

        else: #She's shy or nervous about being discovered
            "[the_person.possessive_title!c] laughs, then shakes her head and glances around, her eyes darting towards the crowd with a nervous energy."
            the_person "You're looking pretty hot too, [the_person.mc_title]... but you need to be a little more subtle, hmm?"
            the_person "I don't want any rumours getting back to my [the_person.so_title]. That would really throw a wrench into our little affair... and I don't think I could handle the drama, okay?"
            $ mc.change_locked_clarity(15)
            "After checking again that nobody else is watching she reaches over and cups your crotch, massaging the bulge through your pants, her eyes sparkling with desire."
            the_person "Just be patient, [the_person.mc_title]. I'll be all over this dick soon enough, hmm?"
            mc.name "Alright, I think I can contain myself a little while longer."
            "She pulls her hand back and smiles, her eyes sparkling with mischief as she teases you."

    else:
        # the_person "Yeah? Well there's nobody around, and I'm not going to stop you."
        "[the_person.possessive_title!c] smiles, a sly, flirtatious smile spreading across her face."
        the_person "Oh yeah? Well then, do you want to share what all of these naughty things are, [the_person.mc_title]? You have my attention, hmm?"
        menu:
            "Feel her up":
                "You put your arms around [the_person.possessive_title]'s waist and rest your hands on her ass, your fingers digging into her flesh."
                mc.name "Well, first I want to get my hands all over your beautiful body, [the_person.title]."
                "You massage her butt, your hands moving in slow, sensual circles as you tease her."
                "She sighs happily and leans against your body, her eyes sparkling with pleasure as she relaxes into your touch."
                the_person "What next, [the_person.mc_title]? What do you want to do to me, hmm?"
                "You spin her around and shift your hands to her breasts, squeezing them gently, your fingers tracing the curves of her body."
                mc.name "No need to rush things, [the_person.title]. Just relax and enjoy for now, hmm?"
                call fuck_person(the_person, private = True, start_position = standing_grope, skip_intro = True) from vt_wild_call_fuck_person_80
                $ the_person.call_dialogue("sex_review", the_report = _return)
                $ the_person.review_outfit()

            "Just flirt":
                $ mc.change_locked_clarity(10)
                "You put your arms around [the_person.possessive_title]'s waist and rest your hands on her ass, your fingers digging into her flesh."
                mc.name "I wish I had the time, [the_person.title]. You'll have to wait until later, hmm?"
                "You massage her butt, your hands moving in slow, sensual circles as you tease her."
                "She sighs happily and leans her weight against you, her eyes sparkling with pleasure as she relaxes into your touch."
                the_person "Aww, are you sure, [the_person.mc_title]?"
                "You slap her ass and step back, the sound echoing through the air as you tease her."
                "She clings to you reluctantly before letting go, her eyes sparkling with mischief as she teases you."
                the_person "Fine, but don't make me wait too long, okay? I have needs, and my [the_person.so_title] sure as hell isn't fulfilling them, hmm?"
                mc.name "I won't make you wait long, I promise."
    return

label vt_wild_flirt_response_text(the_person):
    mc.name "Hey [the_person.title], what's up. I'm bored and figured we could chat."
    "There's a brief pause, then she texts back, her words popping up on the screen with a playful, flirtatious tone."
    if the_person.is_affair:
        "[the_person.possessive_title!c]'s response is immediate and flirtatious, her words dripping with seduction."
        the_person "I'm bored too, [the_person.mc_title]. I can think of a few things we could do together to stop being bored... and they all involve getting naked, hmm?"
        the_person "When can we get together and make some magic happen?"
        mc.name "Some time soon. I'll let you know."
    elif the_person.is_girlfriend:
        "[the_person.possessive_title!c]'s response is playful and teasing, her words poking fun at your lack of initiative."
        the_person "I'm bored too, [the_person.mc_title]. We should get together and hang out... but only if you promise to take me out on a real date, hmm?"
        the_person "When are you going to take me out on another date? I'm going to have to do it myself at this rate, and I don't think you want that, do you?"
        mc.name "Some time soon. I'll let you know."
    elif the_person.love < 40:
        if the_person.effective_sluttiness() > the_person.love:
            "[the_person.possessive_title!c]'s response is flirtatious and playful, her words hinting at a deeper connection."
            the_person "Bored, huh? Well I'm here to entertain, [the_person.mc_title]... and maybe a little more, hmm?"
        else:
            "[the_person.possessive_title!c]'s response is sympathetic and friendly, her words offering a listening ear."
            the_person "That sucks, being bored is the worst. Want to talk about it, [the_person.mc_title]?"
    else:
        if the_person.effective_sluttiness() > the_person.love:
            "[the_person.possessive_title!c]'s response is flirtatious and playful, her words teasing you with possibilities."
            the_person "Bored, huh? Well I'm here to entertain you, [the_person.mc_title]... so what would you like me to do, hmm?"
            the_person "I mean talk about, of course. What would you like to talk about, [the_person.mc_title]?"
        else:
            "[the_person.possessive_title!c]'s response is playful and teasing, her words poking fun at your boredom."
            the_person "Bored and you came to me, huh? It must be really bad, [the_person.mc_title]."
            the_person "Alright, let's chat then. What's up with you, hmm?"
    return

label vt_wild_condom_demand(the_person):
    if the_person.wants_creampie:
        "[the_person.possessive_title!c] looks up at you with a hint of concern, her voice husky and seductive."
        the_person "Oh shit, [the_person.mc_title]... you need to put on a condom before we do anything, hmm?"
        the_person "I hate it too, but it's important, [the_person.mc_title]. I don't want to get pregnant... at least, not yet, hmm?"
        "She winks at you, her eyes sparkling with mischief as she teases you with the possibility of a future pregnancy."

    else:
        "[the_person.possessive_title!c] looks up at you with a sly, flirtatious smile, her voice husky and seductive."
        the_person "Hey, [the_person.mc_title]... you have a condom on you, right? You need to put one on before you can fuck me, hmm?"
        the_person "Don't take too long, [the_person.mc_title]... I might get cold feet, and I don't think you want that, do you?"
        "She raises an eyebrow, a hint of teasing in her voice as she invites you to hurry up and get ready for sex."
    return

label vt_wild_condom_ask(the_person):
    if the_person.on_birth_control:
        "[the_person.possessive_title!c] looks up at you with a sly, flirtatious smile, her voice husky and seductive."
        the_person "Want a condom, [the_person.mc_title]? I'm on the pill, but I guess it's still possible something goes wrong, hmm?"
        "She shrugs, her shoulders barely rising off her body as she invites you to consider the risks."
        $ the_person.update_birth_control_knowledge()

    elif the_person.wants_creampie:
        "[the_person.possessive_title!c] looks up at you with a hint of mischief, her voice husky and seductive."
        the_person "If you want to cum inside me, [the_person.mc_title]... you should put on a condom, hmm?"
        the_person "I know it's less fun than fucking raw, but it's still better than pulling out, right? At least this way we can still feel each other, hmm?"
        "She winks at you, her eyes sparkling with desire as she invites you to consider the possibilities."
        $ the_person.discover_opinion("creampies")

    else:
        "[the_person.possessive_title!c] looks up at you with a hint of concern, her voice husky and seductive."
        the_person "Fuck, [the_person.mc_title]... I should probably tell you to put on a condom, hmm?"
        the_person "I can trust you to pull out, right? We'll need to be careful, but I don't want to ruin the mood, hmm?"
        "She looks up at you with a sly, flirtatious smile, her eyes sparkling with desire as she invites you to take the risk."
    return

label vt_wild_condom_bareback_ask(the_person):
    if the_person.wants_creampie:
        if the_person.is_infertile:
            "[the_person.possessive_title!c] looks up at you with a sly, flirtatious smile, her voice husky and seductive."
            the_person "You aren't thinking of wearing a condom, are you, [the_person.mc_title]? Fuck that, I want you to paint my pussy white, hmm?"
            "She winks at you, her eyes sparkling with desire as she invites you to take her raw."
        elif the_person.on_birth_control:
            "[the_person.possessive_title!c] looks up at you with a hint of mischief, her voice husky and seductive."
            the_person "You aren't thinking of wearing a condom, are you, [the_person.mc_title]? Fuck that, I'm on the pill, hmm?"
            the_person "You can cum right inside me, no worries, [the_person.mc_title]. I want to feel you fill me up, hmm?"
            "She smiles, a sly, flirtatious smile spreading across her face as she invites you to take her raw."
            $ the_person.update_birth_control_knowledge()
        else:
            "[the_person.possessive_title!c] looks up at you with a hint of excitement, her voice husky and seductive."
            the_person "Forget the condom, [the_person.mc_title]... I want you to fuck me raw, hmm?"
            if not the_person.knows_pregnant:
                the_person "I want to feel you cum inside me, knowing I might be getting knocked up, hmm? The thought of it is making me so wet!"
            the_person "That would be so fucking hot, [the_person.mc_title]! I can already imagine it, hmm?"
            "She winks at you, her eyes sparkling with desire as she invites you to take the risk."
        $ the_person.discover_opinion("creampies")
    else:
        "[the_person.possessive_title!c] looks up at you with a sly, flirtatious smile, her voice husky and seductive."
        the_person "Don't bother with a condom, [the_person.mc_title]... I want to feel you raw, hmm?"
        if not the_person.knows_pregnant:
            the_person "I don't care what the risks are, [the_person.mc_title]... they're worth it, hmm? I want to feel you inside me, no matter what."
        else:
            the_person "I love it, [the_person.mc_title]... when you fuck me raw, hmm? It's like our bodies were made for each other."
        "She smiles, a sly, flirtatious smile spreading across her face as she invites you to take her raw."
    return

label vt_wild_condom_bareback_demand(the_person):
    if the_person.has_breeding_fetish: #Actively looking to get knocked up.
        if the_person.knows_pregnant:
            "[the_person.possessive_title!c] looks up at you with a fierce, hungry gaze, her voice husky and seductive."
            the_person "Oh fuck that, [the_person.mc_title]... what's the point of fucking if you aren't going to fuck me raw, hmm?"
            the_person "Come on, give me that cock! I want to feel you inside me, filling me up with your cum, hmm?"
            "She reaches out and grabs your hips, pulling you towards her with a fierce passion."
        elif the_person.is_infertile:
            "[the_person.possessive_title!c] looks up at you with a sly, flirtatious smile, her voice husky and seductive."
            the_person "Oh fuck me already, [the_person.mc_title]... I can't get pregnant, so what's the hold up, hmm?"
            "She winks at you, her eyes sparkling with desire as she invites you to take her raw."
        else:
            "[the_person.possessive_title!c] looks up at you with a fierce, hungry gaze, her voice husky and seductive."
            the_person "Oh fuck that, [the_person.mc_title]... what's the point of fucking if you aren't going to knock me up, hmm?"
            the_person "Come on, preg me! I want to feel your cum inside me, making me pregnant, hmm?"
            "She reaches out and grabs your hips, pulling you towards her with a fierce passion."
    elif the_person.wants_creampie: #Just likes raw sex
        if the_person.is_infertile:
            "[the_person.possessive_title!c] looks up at you with a sly, flirtatious smile, her voice husky and seductive."
            the_person "Oh fuck me already, [the_person.mc_title]... I can't get pregnant, so what's the hold up, hmm?"
            "She winks at you, her eyes sparkling with desire as she invites you to take her raw."
        elif the_person.on_birth_control:
            "[the_person.possessive_title!c] looks up at you with a hint of mischief, her voice husky and seductive."
            the_person "Fuck that, [the_person.mc_title]... I'm on the pill, so we don't have to worry about anything, hmm?"
            the_person "Even better, you can cum right inside me. Come and fill me up, [the_person.mc_title]!"
            "She smiles, a sly, flirtatious smile spreading across her face as she invites you to take her raw."
            $ the_person.update_birth_control_knowledge()
        else:
            "[the_person.possessive_title!c] looks up at you with a hint of frustration, her voice husky and seductive."
            the_person "Fuck that, [the_person.mc_title]... they feel like shit and I can't feel you cum inside me through one, hmm?"
            the_person "So hurry up and get inside me! I want to feel you raw, with nothing between us, hmm?"
            "She reaches out and grabs your hips, pulling you towards her with a fierce passion."
    else:
        if the_person.is_infertile:
            "[the_person.possessive_title!c] looks up at you with a sly, flirtatious smile, her voice husky and seductive."
            the_person "Take me bareback, [the_person.mc_title]... that's how I want it, hmm?"
            "She winks at you, her eyes sparkling with desire as she invites you to take her raw."
        elif the_person.on_birth_control:
            "[the_person.possessive_title!c] looks up at you with a hint of mischief, her voice husky and seductive."
            the_person "Fuck that, [the_person.mc_title]... I'm on the pill, so we don't have to worry about anything, hmm?"
            the_person "Take me bareback, [the_person.mc_title]... that's how I want it, hmm?"
            "She smiles, a sly, flirtatious smile spreading across her face as she invites you to take her raw."
            $ the_person.update_birth_control_knowledge()
        else:
            "[the_person.possessive_title!c] looks up at you with a hint of desire, her voice husky and seductive."
            the_person "Fuck that, [the_person.mc_title]... it feels so much better without one, hmm?"
            the_person "Take me bareback, [the_person.mc_title]... I can't wait any longer, hmm?"
            "She reaches out and grabs your hips, pulling you towards her with a fierce passion."
    return

label vt_wild_cum_face(the_person):
    if the_person.has_cum_fetish or the_person.obedience > 180:
        if the_person.has_cum_fetish or the_person.effective_sluttiness() > 60 or the_person.opinion.cum_facials > 0:
            "[the_person.possessive_title!c] looks up at you with a sly, flirtatious smile, her voice husky and seductive."
            the_person "What do you think, [the_person.mc_title]? Is this a good look for me, hmm?"
            "[the_person.title] licks her lips, moving a few drops of your semen that had run down her face with her fingers to her mouth, her eyes sparkling with mischief."
            "She savors the taste, her expression a mix of pleasure and desire."
        else:
            "[the_person.possessive_title!c] looks up at you with a hint of amusement, her voice playful and teasing."
            the_person "I hope you had a good time, [the_person.mc_title]. It certainly seems like you did, hmm?"
            "[the_person.title] runs a finger along her cheek, wiping away some of your semen, her eyes sparkling with mischief."
            "She smiles, a sly, flirtatious smile spreading across her face as she teases you with her words."
    else:
        if the_person.effective_sluttiness() > 80 or the_person.opinion.cum_facials > 0:
            "[the_person.possessive_title!c] looks up at you with a sly, flirtatious smile, her voice husky and seductive."
            the_person "Mmm, that's such a good feeling, [the_person.mc_title]. Do you think I look cute like this, hmm?"
            "[the_person.title] runs her tongue along her lips, then smiles and laughs, her eyes sparkling with mischief."
            "She seems to be enjoying the sensation of your cum on her face, her expression a mix of pleasure and desire."
        else:
            "[the_person.possessive_title!c] looks up at you with a hint of annoyance, her voice playful and teasing."
            the_person "Whew, glad you got that over with, [the_person.mc_title]. Take a good look while it lasts, hmm?"
            "She rolls her eyes, a playful, flirtatious smile spreading across her face as she teases you with her words."
    return

label vt_wild_cum_mouth(the_person):
    if the_person.has_cum_fetish or the_person.obedience > 180:
        if the_person.has_cum_fetish or the_person.effective_sluttiness() > 60 or the_person.opinion.drinking_cum > 0:
            "[the_person.possessive_title!c] looks up at you with a sly, flirtatious smile, her voice husky and seductive."
            the_person "Mmm, thank you, [the_person.mc_title]... that was delicious, hmm?"
            "She licks her lips, savoring the taste of your cum, her eyes sparkling with mischief."
        else:
            "[the_person.possessive_title!c] makes a face, her expression a mix of distaste and amusement."
            "[the_person.title]'s face grimaces as she tastes your cum in her mouth, her eyes narrowing in a playful, flirtatious way."
            the_person "Ugh... There, all taken care of, [the_person.mc_title]. I hope you enjoyed the show, hmm?"
            "She winks at you, her eyes sparkling with mischief as she teases you with her words."
    else:
        if the_person.effective_sluttiness() > 80  or the_person.opinion.drinking_cum > 0:
            "[the_person.possessive_title!c] looks up at you with a sly, flirtatious smile, her voice husky and seductive."
            the_person "Mmm, you taste great, [the_person.mc_title]... Was it nice to watch me take your load in my mouth, hmm?"
            "She runs her tongue along her lips, savoring the taste of your cum, her eyes sparkling with mischief."
        else:
            "[the_person.possessive_title!c] makes a face, her expression a mix of distaste and amusement."
            the_person "Ugh, that's such a... unique taste, [the_person.mc_title]. I'm not sure if I love it or hate it, hmm?"
            "She laughs, a playful, flirtatious sound, her eyes sparkling with mischief as she teases you with her words."
    return

label vt_wild_cum_pullout(the_person):
    # Lead in: "I'm going to cum!"
    if mc.condom:
        if the_person.wants_creampie and not the_person.has_taboo("condomless_sex"): #TODO: FIgure out we want any more requirements for this to fire.
            if the_person.knows_pregnant:
                "[the_person.possessive_title!c] looks up at you with a fierce, hungry gaze, her voice husky and seductive."
                the_person "Oh fuck... Take that stupid condom off and cum in my pussy, [the_person.mc_title]!"
                the_person "You already knocked me up, so who fucking cares? I just want you to fill me up and make me feel like a slut, hmm?"
                "She moans desperately, her body writhing with pleasure as she begs you to take her raw."
            elif the_person.on_birth_control:
                "[the_person.possessive_title!c] looks up at you with a sly, flirtatious smile, her voice husky and seductive."
                the_person "Oh fuck... I can't take it any more, take that condom off, [the_person.mc_title]!"
                "She moans desperately, her body writhing with pleasure as she begs you to take her raw."
                the_person "I give in, I want you to cum inside me and make me feel like a slut, hmm?"
            else:
                "[the_person.possessive_title!c] looks up at you with a fierce, hungry gaze, her voice husky and seductive."
                the_person "I can't... I can't think straight, [the_person.mc_title]!"
                "She moans desperately, her body writhing with pleasure as she begs you to take her raw."
                the_person "Fuck it! Take the condom off and cum inside me, [the_person.mc_title]! I want you to get me pregnant and fuck my life up, hmm?"
                $ the_person.update_birth_control_knowledge()
                "She looks up at you with a sly, flirtatious smile, her eyes sparkling with mischief as she invites you to take the risk."
            menu: #TODO: Add a variant of this normally so you can stealth a girl (don't do that in real life, it's super fucked up).
                "Take off the condom":
                    "You don't have much time to spare. You pull out, barely clearing her pussy, and pull the condom off as quickly as you can manage."
                    $ mc.condom = False
                    $ use_condom = False  # prevent putting on a new condom next sex loop
                "Leave it on":
                    "You ignore [the_person.possessive_title]'s cum-drunk offer and keep the condom in place."
        else:
            "[the_person.possessive_title!c] looks up at you with a sly, flirtatious smile, her voice husky and seductive."
            the_person "Fuck yeah, I'm going to make you cum, [the_person.mc_title]! Let it all out and show me what you're working with, hmm?"
            "She winks at you, her eyes sparkling with mischief as she invites you to cum."
    else:
        if the_person.wants_creampie:
            if the_person.knows_pregnant: #She's already knocked up, so who cares!
                "[the_person.possessive_title!c] looks up at you with a fierce, hungry gaze, her voice husky and seductive."
                the_person "Creampie me, [the_person.mc_title]... I want it all, hmm? Fill me up with your cum and make me feel like a slut!"
                "She moans desperately, her body writhing with pleasure as she begs you to creampie her."
            elif the_person.opinion.creampies > 0:
                "[the_person.possessive_title!c] moans happily, her body writhing with pleasure as she begs you to creampie her."
                if the_person.on_birth_control: #She just likes creampies.
                    the_person "Fuck yeah, fill me up with your cum, [the_person.mc_title]! Creampie me and make me feel like a slut, hmm?"
                else: #Yeah, she's not on BC and asking for you to creampie her. She's looking to get pregnant.
                    $ the_person.update_birth_control_knowledge()
                    the_person "Oh fuck, cum inside me and knock me up, [the_person.mc_title]! I want you to breed me like a slut and make me feel like a dirty little whore, hmm?"
                "She looks up at you with a sly, flirtatious smile, her eyes sparkling with mischief as she invites you to take the risk."
            elif the_person.is_infertile:
                "[the_person.possessive_title!c] looks up at you with a sly, flirtatious smile, her voice husky and seductive."
                the_person "Cum wherever you want, [the_person.mc_title]... I'm infertile, so who cares, hmm?"
                "She winks at you, her eyes sparkling with mischief as she invites you to cum wherever you want."
            elif the_person.on_birth_control: #She's on the pill, so she's probably fine
                $ the_person.update_birth_control_knowledge()
                "[the_person.possessive_title!c] looks up at you with a sly, flirtatious smile, her voice husky and seductive."
                the_person "Cum wherever you want, [the_person.mc_title]... I'm on the pill, so we're good to go, hmm?"
                "She winks at you, her eyes sparkling with mischief as she invites you to cum wherever you want."
            else: #Too distracted to care about getting pregnant or not. Oh well, what could go wrong?
                "[the_person.possessive_title!c] looks up at you with a fierce, hungry gaze, her voice husky and seductive."
                the_person "Do it! Cum inside me and make me feel like a slut, [the_person.mc_title]! I don't care about anything else, just make me cum, hmm?"
                "She moans desperately, her body writhing with pleasure as she begs you to creampie her."
        else:
            if the_person.is_infertile:
                "[the_person.possessive_title!c] looks up at you with a sly, flirtatious smile, her voice husky and seductive."
                the_person "Just pull out, [the_person.mc_title]... I don't want your cum inside me, hmm?"
                "She winks at you, her eyes sparkling with mischief as she invites you to pull out."
            elif not the_person.on_birth_control: #You need to pull out, I'm not on the pill!
                $ the_person.update_birth_control_knowledge()
                "[the_person.possessive_title!c] looks up at you with a hint of concern, her voice husky and seductive."
                the_person "Fuck, pull out, [the_person.mc_title]! I'm not on the pill, so we can't take any chances, hmm?"
                "She looks up at you with a serious expression, her eyes sparkling with concern as she invites you to pull out."
            elif the_person.opinion.creampies < 0:
                "[the_person.possessive_title!c] looks up at you with a hint of distaste, her voice husky and seductive."
                the_person "Pull out, [the_person.mc_title]... I don't want you to cum in me, hmm?"
                "She looks up at you with a serious expression, her eyes sparkling with distaste as she invites you to pull out."
            else:
                "[the_person.possessive_title!c] looks up at you with a sly, flirtatious smile, her voice husky and seductive."
                the_person "Hell yeah, pull out and cum all over me, [the_person.mc_title]! I want to feel your cum on my skin and taste it on my lips, hmm?"
                "She winks at you, her eyes sparkling with mischief as she invites you to cum all over her."
    return

label vt_wild_cum_condom(the_person):
    if the_person.effective_sluttiness() > 75 or the_person.opinion.creampies > 0:
        "[the_person.possessive_title!c] looks up at you with a sly, flirtatious smile, her voice husky and seductive."
        the_person "Oh god, it's so warm... If your condom broke, it would all be inside me, hmm?"
        "She bites her lower lip, her eyes sparkling with desire as she imagines the possibility of a creampie."
        "Her body language screams with seduction, inviting you to take the risk and go bareback."
    else:
        "[the_person.possessive_title!c] looks up at you with a hint of amusement, her voice playful and teasing."
        the_person "Oh god, I hope you buy good condoms, [the_person.mc_title]... because that's a lot of cum, hmm?"
        the_person "But then again, maybe you're dreaming of knocking me up, [the_person.mc_title]... and making me a mommy, hmm?"
        "She winks at you, her eyes sparkling with mischief as she teases you with the possibility of getting her pregnant."
    return

label vt_wild_cum_vagina(the_person):
    if the_person.has_taboo("creampie"):
        $ the_person.call_dialogue("creampie_taboo_break")
        $ the_person.break_taboo("creampie")
        return

    if the_person.wants_creampie:
        if the_person.knows_pregnant:
            "[the_person.possessive_title!c] throws her head back, laughing maniacally as she wraps her legs around you."
            the_person "Ha! Looks like I'm already knocked up, so go ahead and give me that creampie, baby!"

        elif the_person.is_infertile:
            "[the_person.title] starts to ride you, her hips bucking wildly as she screams with pleasure."
            the_person "Oh, yeah! Fill me up, baby! I want to feel that hot cum inside me all day long!"

        elif the_person.on_birth_control:
            if the_person.has_significant_other:
                "[the_person.title] winks at you, her eyes sparkling with mischief as she whispers in your ear."
                the_person "Mwahahaha, my [the_person.so_title] has no idea what I'm doing right now... and I'm loving every minute of it!"
            else:
                if the_person.knows_pregnant:
                    "[the_person.title] shrugs, a wicked grin spreading across her face."
                    the_person "Who cares about getting pregnant? I'm already there, so let's just enjoy the ride!"
                elif the_person.is_infertile:
                    "[the_person.title] starts to laugh, her body shaking with pleasure as she rocks back and forth."
                    the_person "I'm not worried about getting pregnant, so go ahead and cum inside me all you want!"
                else:
                    "[the_person.title] leans in close, her breath hot against your ear."
                    the_person "I'm on the pill, but that's not going to stop me from having fun! Fill me up, baby!"
                $ the_person.update_birth_control_knowledge()

        elif the_person.effective_sluttiness() > 75 or the_person.opinion.creampies > 0:
            if the_person.has_significant_other:
                "[the_person.title] starts to giggle, her eyes sparkling with mischief as she whispers in your ear."
                the_person "Hehe, my [the_person.so_title] thinks I'm a good girl, but little does he know... I'm a creampie-loving slut!"

            else:
                "[the_person.title] starts to scream with pleasure, her body shaking with orgasm as she rocks back and forth."
                the_person "Cum inside me, baby! I want to feel that hot sperm filling me up and making me whole!"
        else:
            if the_person.has_significant_other:
                "[the_person.title] winks at you, her eyes sparkling with mischief as she whispers in your ear."
                the_person "Oh, this is going to be fun! My [the_person.so_title] is going to be so surprised when I come home with a big belly!"

            else:
                "[the_person.title] starts to laugh, her body shaking with pleasure as she rocks back and forth."
                the_person "Haha, you're really trying to knock me up, aren't you? Well, I'm not going to stop you!"

    else: #She's angry
        if the_person.knows_pregnant:
            "[the_person.title] slaps your chest, her face twisted in anger."
            the_person "Ugh, you idiot! I told you to pull out, but I guess it's too late now..."

        elif not the_person.on_birth_control:
            if the_person.has_significant_other:
                "[the_person.title] starts to yell, her voice echoing off the walls as she points at you accusingly."
                the_person "What the hell, [the_person.mc_title]! My [the_person.so_title] is going to kill me if I get pregnant again!"
                if the_person.kids > 0:
                    "[the_person.title] throws up her hands, her face twisted in frustration."
                    the_person "... And I'm not even kidding this time."
            else:
                "[the_person.title] looks at you in horror, her eyes wide with shock."
                the_person "Are you kidding me?! I'm not on the pill, and you just creampieed me! What am I supposed to do now?"
                $ the_person.update_birth_control_knowledge()
                "[the_person.title] crosses her arms, her face twisted in anger."
                the_person "You're going to have to start wearing a condom from now on, because I'm not dealing with this crap again."
        elif the_person.is_infertile:
            "[the_person.title] rolls her eyes, her face twisted in disgust."
            the_person "Ugh, you're such a mess! Look at what you've done now... I'm covered in your cum!"

        elif the_person.has_significant_other:
            "[the_person.title] starts to yell, her voice echoing off the walls as she points at you accusingly."
            the_person "What the hell, [the_person.mc_title]! I have a [the_person.so_title], and you're creampieing me like I'm some kind of slut!"
            $ the_person.update_birth_control_knowledge()
            "[the_person.title] throws up her hands, her face twisted in frustration."
            the_person "You need to be more careful next time, or I'll make you wear a condom for sure."

        elif the_person.opinion.creampies < 0:
            "[the_person.title] looks at you in disgust, her face twisted in revulsion."
            the_person "Ugh, this is disgusting! You're covered in your own cum, and now I am too..."

        else:
            "[the_person.title] shakes her head, her face twisted in disappointment."
            the_person "What's wrong with you, [the_person.mc_title]? Can't you just pull out like a normal person?"
            "[the_person.title] sighs, her shoulders slumping in frustration."
            the_person "Don't make me have to start wearing a condom again, because I'm not going to deal with this nonsense."

    return

label vt_wild_cum_anal(the_person):
    if the_person.has_taboo("anal creampie"):
        $ the_person.call_dialogue("anal_creampie_taboo_break")
        $ the_person.break_taboo("anal creampie")
        return

    if the_person.sluttiness > 75 or the_person.opinion.anal_creampies > 0:
        "[the_person.title] starts to moan loudly, her hips bucking wildly as she reaches back to grab your hips."
        the_person "Ahh, yes! Fill my ass up with that hot cum! I want to feel it dripping out of me all day!"
    elif the_person.opinion.anal_creampies < 0:
        "[the_person.title] looks back at you with a mixture of shock and disgust, her eyes wide with alarm."
        the_person "Oh no, no, no! Not inside my ass! Pull out, pull out!"
    else:
        "[the_person.title] starts to scream with pleasure, her body shaking with orgasm as she rocks back and forth."
        the_person "Oh my god, yes! Fill me up! I want to feel that hot cum inside me, making me whole!"
    return

label vt_wild_surprised_exclaim(the_person):
    $rando = renpy.random.choice(["Ahh, yessss!","Oh my god!","Fuck yeah!","Shit, yeah!","Whoa, baby!","Holy fuck!","Fucking hell, yeah!", "God damn, that's good!", "Son of a...!", "Mother...!", "What the...!", "Fucking... wow!"])
    "[the_person.title] throws her head back, her eyes wide with surprise and excitement."
    the_person "[rando]"
    "[the_person.title] takes a deep breath, her chest heaving with anticipation."
    return

label vt_wild_talk_busy(the_person):
    if the_person.obedience > 120:
        "[the_person.title] flashes you a flirtatious smile as she rushes by, her hair flying behind her."
        the_person "Sorry, sweetie, I'm slammed right now! Maybe we can catch up later, hmm?"
    else:
        "[the_person.title] gives you a playful wink as she juggles multiple tasks at once, her eyes sparkling with energy."
        the_person "Hey, lover! I'd love to chat, but I'm up to my eyeballs in work right now. Rain check, okay?"
    return

label vt_wild_sex_strip(the_person):
    if the_person.sluttiness < 20:
        if the_person.arousal_perc < 50:
            "[the_person.title] gives you a sly smile as she reaches for the hem of her clothes."
            the_person "Just a sec, baby... I want to show you something."
        else:
            "[the_person.title] laughs playfully as she starts to peel off her clothes, her eyes sparkling with excitement."
            the_person "Oh, this is getting in the way! Time to get a little more... intimate."
    elif the_person.sluttiness < 60:
        if the_person.arousal_perc < 50:
            "[the_person.title] rolls her eyes good-naturedly as she starts to strip, her movements fluid and confident."
            the_person "Why bother with all these clothes, anyway?"
        else:
            "[the_person.title] winks at you as she slowly reveals more skin, her voice husky with desire."
            the_person "I think it's time I showed you what's underneath... don't you?"
    else:
        if the_person.arousal_perc < 50:
            "[the_person.title] gives you a sultry smile as she starts to peel off her clothes, her movements deliberate and sensual."
            the_person "Just for you, baby... I'm going to show you everything."
        else:
            "[the_person.title] moans with frustration as she rips off her clothes, her eyes blazing with desire."
            the_person "Ugh, get this off me! I want to feel your skin against mine, now!"
    return

label vt_wild_sex_watch(the_person, the_sex_person, the_position):
    $ title = the_person.title if not the_person.is_stranger else "The stranger"
    if the_person.sluttiness < the_position.slut_requirement - 20:
        $ the_person.draw_person(emotion = "angry", display_transform = character_left_flipped)
        "[the_person.title] crosses her arms, her eyes flashing with annoyance."
        the_person "Ugh, can you two just get a room already? This is ridiculous."
        $ the_person.change_stats(obedience = -2, happiness = -1)
        "[title] turns her back on you and [the_sex_person.fname], clearly uninterested in the scene unfolding before her."
        return False

    if the_person.sluttiness < the_position.slut_requirement - 10:
        $ the_person.draw_person(display_transform = character_left_flipped)
        "[the_person.title] raises an eyebrow, her voice dripping with sarcasm."
        the_person "Wow, you two are really going at it. Could you at least try to keep it down?"
        $ the_person.change_happiness(-1)
        "[title] rolls her eyes and tries to ignore you and [the_sex_person.fname] [the_position.verb]."
        return False

    if the_person.sluttiness < the_position.slut_requirement:
        $ the_person.draw_person(display_transform = character_left_flipped)
        if not is_watching(the_person):
            "[the_person.title] leans in, her voice barely above a whisper."
            the_person "You're really getting into this, aren't you [the_sex_person.fname]? I have to admit, it's kind of hot..."
        $ the_person.change_slut(1, 30)
        "[title] watches with growing interest as you and [the_sex_person.fname] continue [the_position.verbing]."
        return True

    if the_person.sluttiness >= the_position.slut_requirement and the_person.sluttiness < the_position.slut_cap:
        $ the_person.draw_person(display_transform = character_left_flipped)
        if not is_watching(the_person):
            "[the_person.title] grins mischievously, her eyes sparkling with excitement."
            the_person "Oh, this is getting good! Mind if I join the party?"
        $ the_person.change_slut(1, 50)
        "[title] watches with rapt attention as you and [the_sex_person.fname] [the_position.verb]."
        return True

    $ the_person.draw_person(emotion = "happy", display_transform = character_left_flipped)
    if renpy.random.randint(0, 1) == 0:
        "[title] cheers you on, her voice husky with desire."
        the_person "That's it, [the_person.mc_title]! Give it to her good! Make her scream!"
    else:
        call watcher_position_comment(the_person, the_sex_person, the_position) from _call_watcher_position_comment_vt_wild_sex_watch
    "[title] watches with unbridled enthusiasm as you and [the_sex_person.fname] [the_position.verb]."
    return True

label vt_wild_being_watched(the_person, the_watcher, the_position):
    $ title = the_watcher.fname if not the_watcher.is_stranger else "the stranger"
    if the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #They agree you should give it to her harder
        "[the_person.title] looks back at [title] with a wicked grin, her eyes sparkling with excitement."
        the_person "Come on, [the_person.mc_title], show her what you're working with! Give it to me harder!"
        $ the_person.change_arousal(1)
        "[the_person.title] seems to be feeding off [title]'s energy, getting more and more turned on by the minute."
    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's super slutty and doesn't care what people think.
        "[the_person.title] tosses a flirtatious glance back at [title], her voice dripping with sarcasm."
        the_person "Oh, I'm sure she's just dying to be in my shoes right now. Who wouldn't want to be getting [the_position.verb]ed by you?"
    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #She's super slutty and encourages the watcher to be slutty.
        "[the_person.title] reaches out and grabs [title]'s hand, pulling her closer to the action."
        the_person "Come on, [title], join the party! We can make this a threesome and really get things going!"
        $ the_person.change_arousal(1)
        "[the_person.title] seems to be enjoying the attention from [title], and is getting more and more turned on by the minute."
    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #She's into it and encouraged by the slut watching her.
        "[the_person.title] looks back at [title] with a mixture of excitement and nervousness, her voice barely above a whisper."
        the_person "I-I'm not sure how much more of this I can take... but I'm loving every minute of it!"
        $ the_person.change_arousal(1)
        "[the_person.title] seems to be feeding off [title]'s energy, getting more and more turned on by the minute."
    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's into it but shamed by the prude watching her.
        "[the_person.title] looks back at [title] with a mixture of embarrassment and annoyance, her voice laced with frustration."
        the_person "Ugh, can we please just go somewhere else? This is really killing the mood..."
        $ the_person.change_stats(arousal = -1, slut = -1)
        "[the_person.title] seems uncomfortable with [title] nearby, and is having trouble getting back into the mood."
    else: #the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #They're both into it but not fanatical about it.
        "[the_person.title] grins mischievously at [title], her eyes sparkling with excitement."
        the_person "Hey, [title], why don't you come join us? We can make this a party and really get things going!"
        $ the_person.change_stats(arousal = 1, slut = 1, max_slut = 30)
        "[the_person.title] seems more comfortable [the_position.verbing] you with [title] around, and is enjoying the attention from both of you."
    return

label vt_wild_work_enter_greeting(the_person):
    if the_person.happiness < 80 or the_person.love < 0:
        "[the_person.title] barely acknowledges your presence, her eyes flashing with annoyance as she mutters under her breath."
        the_person "Great, just what I needed. Another distraction."
    elif the_person.happiness > 130:
        if the_person.sluttiness > 40:
            "[the_person.title] looks up from her work, a sultry smile spreading across her face as she eyes you up and down."
            the_person "Well, well, well. Look what we have here. Come to see me, or just to brighten up my day?"
            "She winks, her eyes sparkling with mischief as she leans back in her chair, her legs crossed seductively."
        else:
            "[the_person.title] beams at you, her face lighting up with a warm smile as she waves you over."
            the_person "Hey, [the_person.mc_title]! Come on over, I'm so glad you stopped by. What brings you here today?"
    else:
        if the_person.sluttiness > 60:
            $ the_person.draw_person(position = "stand4")
            "[the_person.title] sashays over to you, her hips swaying seductively as she runs her hands over your chest, her eyes locked on yours."
            the_person "Mmm, just the person I was hoping to see. I've got a little something that needs... attention."
            "She winks, her voice dripping with innuendo as she leans in close, her breath hot against your ear."
        else:
            "[the_person.title] looks up from her work, a friendly smile on her face as she greets you."
            the_person "Hey, [the_person.mc_title]! Need anything? I'm all ears... or whatever else you might need."
    return

label vt_wild_date_seduction(the_person):
    if the_person.is_girlfriend:
        "[the_person.possessive_title!c] grabs your hand and pulls you around to look at her, a mischievous glint in her eye."
        the_person "Hey, that was such a great time. So I was thinking... why don't we take things to the next level?"
        $ mc.change_locked_clarity(30)
        if the_person.effective_sluttiness(["vaginal_sex", "condomless_sex"]) > 60 and the_person.wants_creampie and the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex >= 0 and the_person.opinion.creampies >= 0 and not the_person.on_birth_control and not the_person.knows_pregnant:
            if the_person.opinion.creampies > 0: 
                the_person "Let's go back to my place and get crazy. I want you to knock me up, [the_person.mc_title]!"
                the_person "Can you imagine it? Me, with a big belly, and you, being the one who put that baby inside me?"
            else:
                the_person "Let's go back to my place and get wild. I want you to fuck me bareback, and cum inside me."
                the_person "I love the way it feels, and I know you do too. So what do you say?"
        elif the_person.effective_sluttiness(["vaginal_sex", "condomless_sex"]) > 60 and the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex > 0:
            the_person "Let's go back to my place, and get naked. I want you to fuck me all night, no condoms allowed."
            the_person "I love the way it feels, and I know you do too. So what do you say?"
        elif the_person.effective_sluttiness(["vaginal_sex"]) > 50 and the_person.opinion.vaginal_sex > 0:
            the_person "Let's go back to my place, and get crazy. I want you to pound my little pussy all night long."
            the_person "I love the way it feels, and I know you do too. So what do you say?"
        elif the_person.effective_sluttiness(["anal_sex"]) > 60 and the_person.opinion.anal_sex > 0:
            the_person "Let's go back to my place, and get wild. I want you to stretch out my tight little asshole all night long."
            the_person "I love the way it feels, and I know you do too. So what do you say?"
        elif the_person.effective_sluttiness(["sucking_cock"]) > 40 and the_person.opinion.giving_blowjobs > 0:
            the_person "Let's go back to my place, and get crazy. I want to suck your cock all night long."
            the_person "I love the way it feels, and I know you do too. So what do you say?"
        elif the_person.effective_sluttiness() > 40 and the_person.opinion.being_covered_in_cum > 0:
            the_person "Let's go back to my place, and get wild. I want you to cover me in your cum all night long."
            the_person "I love the way it feels, and I know you do too. So what do you say?"
        elif the_person.effective_sluttiness(["touching_body"]) > 40 and the_person.opinion.giving_tit_fucks > 0 and the_person.has_large_tits:
            the_person "Let's go back to my place, and get crazy. I want you to fuck my tits all night long."
            the_person "I love the way it feels, and I know you do too. So what do you say?"
        else: 
            the_person "It doesn't have to be over yet, does it? Let's go back to my place, and see where things go."
            "She bites her lower lip playfully, and winks at you."

    elif the_person.is_affair:
        the_person "So my [the_person.so_title] won't be home tonight, I was thinking... why don't we have some fun?"
        "She reaches down and cups your crotch, rubbing it gently through your pants."
        $ mc.change_locked_clarity(40)
        if the_person.wants_creampie and the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex >= 0 and the_person.opinion.creampies >= 0 and not the_person.on_birth_control and not the_person.knows_pregnant:
            if the_person.opinion.creampies > 0: 
                the_person "Let's go back to my place, and get crazy. I want you to creampie me all night long."
                the_person "All that cum in my unprotected pussy and I'm sure to get knocked up. Just thinking about it is making me wet!"
            else:
                the_person "Let's go back to my place, and get wild. I want you to fuck me bareback all night long."
                the_person "Cum inside me, over my face, whatever. I just want you to fuck me up with your cock."
        elif the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex > 0:
            the_person "Let's go back to my place, and get naked. I want you to fuck me all night, no condoms allowed."
            the_person "If you're fucking me you're doing it bareback. I love the way it feels, and I know you do too. So what do you say?"
        elif the_person.opinion.vaginal_sex > 0:
            the_person "Let's go back to my place, and get crazy. I want you to pound my tight fucking pussy all night long."
            the_person "I love the way it feels, and I know you do too. So what do you say?"
        elif the_person.opinion.anal_sex > 0:
            the_person "Let's go back to my place, and get wild. I want you to stretch out my tight little asshole all night long."
            the_person "I love the way it feels, and I know you do too. So what do you say?"
        elif the_person.opinion.giving_blowjobs > 0:
            the_person "Let's go back to my place, and get crazy. I want to suck your cock all night long."
            the_person "I love the way it feels, and I know you do too. So what do you say?"
        elif the_person.opinion.being_covered_in_cum > 0:
            the_person "Let's go back to my place, and get wild. I want you to cover me in your cum all night long."
            the_person "I love the way it feels, and I know you do too. So what do you say?"
        elif the_person.opinion.giving_tit_fucks > 0 and the_person.has_large_tits:
            the_person "Let's go back to my place, and get crazy. I want you to fuck my tits all night long."
            the_person "I love the way it feels, and I know you do too. So what do you say?"
        elif the_person.opinion.cheating_on_men > 0:
            the_person "Let's go back to my place, and get wild. I want to do all the things my husband thinks I hate."
            the_person "I love the way it feels, and I know you do too. So what do you say?"
        else:
            the_person "Let's go back to my place, and make him really regret leaving me alone for the night."
    elif not the_person.has_significant_other:
        $ mc.change_locked_clarity(20)
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                the_person "I've had a blast [the_person.mc_title], but there are a few more things I'd like to do with you. Want to come back to my place and find out what they are?"
                "She winks at you, and bites her lower lip playfully."
            else:
                the_person "You've been a blast [the_person.mc_title]. Want to come back to my place, have a few drinks, and see where things lead?"
                "She smiles at you, and raises an eyebrow."
        else:
            if the_person.love > 40:
                the_person "Tonight's been amazing [the_person.mc_title], I just don't want to say goodbye. Do you want to come back to my place and have a few drinks?"
                "She smiles at you, and takes your hand."
            else:
                the_person "This might be crazy, but I had a great time tonight and you make me a little crazy. Do you want to come back to my place and see where things go?"
                "She looks up at you, her eyes sparkling with excitement."
    else:
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                $ mc.change_locked_clarity(20)
                the_person "I've had a blast [the_person.mc_title], but I'm not done with you yet. Want to come back to my place?"
                the_person "My [the_person.so_title] won't be home until morning, so we would have plenty of time."
                "She winks at you, and bites her lower lip playfully."
            else:
                $ mc.change_locked_clarity(20)
                the_person "This might be crazy, but do you want to come back to have another drink with me?"
                the_person "My [the_person.so_title] is stuck at work and I don't want to be left all alone."
                "She smiles at you, and raises an eyebrow."
        else:
            if the_person.love > 40:
                $ mc.change_locked_clarity(20)
                the_person "You're making me feel crazy [the_person.mc_title]. Do you want to come have a drink at my place?"
                the_person "My [the_person.so_title] won't be home until morning, and we have a big bed you could help me warm up."
                "She smiles at you, and takes your hand."
            else:
                $ mc.change_locked_clarity(20)
                the_person "This is crazy, but would you want to have one last drink at my place? My [the_person.so_title] won't be home until morning..."
                "She looks up at you, her eyes sparkling with excitement."
    return

label vt_wild_sex_end_early(the_person):
    if the_person.sluttiness > 50:
        if the_person.love > 40:
            if the_person.arousal_perc > 60:
                "[the_person.title] pouts, her face twisted in a mixture of disappointment and desire."
                the_person "You're really done? Fuck [the_person.mc_title], I'm still so horny... I was just getting started!"
            else:
                "[the_person.title] raises an eyebrow, a sly smile spreading across her face."
                the_person "That's all you wanted? I was prepared to do so much more to you... and have you do so much more to me."
        else:
            if the_person.arousal_perc > 60:
                "[the_person.title] looks at you with a hungry gaze, her eyes flashing with desire."
                the_person "Fuck, I'm so horny... you're sure you're finished? I'm just getting warmed up!"
            else:
                "[the_person.title] shrugs, a nonchalant expression on her face."
                the_person "That was a little bit of fun, I suppose. But I'm not done yet... are you sure you are?"
    else:
        if the_person.love > 40:
            if the_person.arousal_perc > 60:
                "[the_person.title] blushes, her face flushed with excitement."
                the_person "[the_person.mc_title], you got me so turned on... I didn't expect that to happen so fast!"
            else:
                "[the_person.title] smiles, a gentle expression on her face."
                the_person "I hope you had a good time. I know I did... even if it was a little short."
        else:
            if the_person.arousal_perc > 60:
                "[the_person.title] gasps, her eyes wide with surprise."
                the_person "Oh god, that was intense... I didn't expect it to be so good!"
            else:
                "[the_person.title] nods, a matter-of-fact expression on her face."
                the_person "Done? Good, nice and quick. Just what I needed."
    return

label vt_wild_sex_take_control(the_person):
    if the_person.arousal_perc > 60:
        "[the_person.title] grabs your arm, her eyes blazing with desire as she pulls you back into the action."
        the_person "Oh hell no, you can't just get me wet and then walk away! Finish what you started, damn it!"
    else:
        "[the_person.title] pouts, her face twisted in a mixture of disappointment and frustration as she reaches out to grab you."
        the_person "Are you getting bored already? Get back here, we aren't done yet! I'm just getting started!"
    return

label vt_wild_sex_beg_finish(the_person):
    "[the_person.title] looks up at you with pleading eyes, her voice husky with desire as she wraps her legs around you."
    the_person "Oh, [the_person.mc_title], please... don't stop now! I'm so close... I'll do anything, just let me cum!"
    "[the_person.title] arches her back, her body trembling with anticipation as she begs for release."
    return

label vt_wild_sex_review(the_person, the_report):
    $ comment_position = the_person.pick_position_comment(the_report)
    if comment_position is None:
        return #You didn't actually do anything, no need to comment.

    $ used_obedience = the_report.get("obedience_used", False) #True if a girl only tried a position because you ordered her to.
    $ the_person.draw_person()  # make sure she stands up for talking with you

    #She's worried about her SO finding out because it was in public
    if the_report.get("was_public", False) and the_person.has_significant_other and the_person.opinion.cheating_on_men <= 0: #It was public and she cares.
        if the_person.is_affair: #Dialogue about her being into it, but you can't do this in case she gets caught.
            "[the_person.title] looks around nervously, her voice barely above a whisper."
            the_person "Whew, that got a little crazy! We, uh, should probably be more careful next time though, okay?"
            the_person "Somebody might tip off my [the_person.so_title], and this whole thing is going to be hard to explain... not that I'm not worth it, of course."
        elif used_obedience:
            "[the_person.title] looks around nervously, her eyes darting back and forth."
            the_person "Everyone is watching... Fuck, what if someone tells my [the_person.so_title]?"
            mc.name "Don't worry, nobody really cares what we're doing. They aren't going to tell your [the_person.so_title]."
            the_person "I hope you're right, this is going to be really hard to explain... and I don't want to have to deal with the drama."

        else:
            "[the_person.title] gasps, her eyes wide with surprise."
            the_person "Everyone's watching us. I hope my [the_person.so_title] doesn't hear about this..."
            mc.name "Don't worry, nobody here really cares what we do together. Nobody's going to tell him."
            the_person "I hope you're right, this would be really hard to explain... and I don't want to have to deal with the fallout."

    #She's single, but worried that you did in public.
    elif the_report.get("was_public", False) and (the_person.effective_sluttiness()+10*the_person.opinion.public_sex < comment_position.slut_cap):
        if used_obedience:
            "[the_person.title] looks around nervously, her face twisted in a mixture of embarrassment and arousal."
            the_person "Fuck, everyone is watching us [the_person.mc_title]."
            the_person "They're all going to think I'm some sort of huge slut after this... which, I mean, I guess I am."

        else:
            "[the_person.title] gasps, her eyes wide with surprise."
            the_person "Oh fuck, everyone's watching us [the_person.mc_title]."
            mc.name "Don't worry, nobody really cares what we're doing."
            the_person "I hope you're right, or I'm going to end up with a reputation for this sort of thing... which, I mean, could be kind of fun."

    elif the_report.get("girl orgasms", 0) > 2:
        if used_obedience:
            "[the_person.title] smiles up at you, her eyes sparkling with pleasure."
            the_person "Oh fuck... baby... I loved what you did to me... you're so good at making me cum."
            mc.name "I do enjoy when you keep begging me to make you cum again."
            "[the_person.possessive_title!c] winks at you, her face still flushed with arousal."

        else:
            "[the_person.title] gasps, her eyes wide with surprise."
            the_person "I have never... cum that hard... It was just amazing... you're so good at this."
            "She seems dazed by her orgasm as she tries to form coherent sentences."
            the_person "You really... know how to give a girl a good time... just gimme a second, I need to catch my breath."

        call sex_review_trance(the_person) from _call_sex_review_trance_vt_wild_sex_review

    #No special conditions, just respond based on how orgasmed and how slutty the position was.
    elif the_report.get("girl orgasms", 0) > 0 and the_report.get("guy orgasms", 0) > 0: #You both came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position cap, it was tame
            "[the_person.title] pouts, her face twisted in a mixture of disappointment and arousal."
            the_person "Ah, that was fucking nice... But I think we could go even further next time. You're not even close to my limits yet."
            the_person "Doesn't that sound like fun? I'm getting wet just thinking about it... again."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            "[the_person.title] smiles, her eyes sparkling with pleasure."
            the_person "Ah, that was just what I needed! I think we're very compatible [the_person.mc_title]."
            the_person "Let's do it again some time soon, okay? Maybe we can even try something new... and naughty."

        elif used_obedience: #She only did it because she was commanded
            "[the_person.title] looks away, her face twisted in a mixture of embarrassment and arousal."
            the_person "Fuck, I... I didn't think I was going to cum like that. You're really good at this... I guess."
            mc.name "Aren't you going to thank me? You obviously had a good time."
            "She rolls her eyes and looks away, trying to hide her embarrassment."

        else: # She's surprised she even tried that.
            "[the_person.title] gasps, her eyes wide with surprise."
            the_person "Oh fuck, that was intense! I didn't think I was going to take it so far, but it just felt right, you know?"
            the_person "Don't think that's going to happen every time though, alright? I'm not a slut... or at least, I don't think I am... yet."

    elif the_report.get("girl orgasms", 0) > 0: #Only she came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            "[the_person.title] pouts, her face twisted in a mixture of disappointment and arousal."
            the_person "Done already? Well, that's just not right. Next time I'm going to make sure we both cum... multiple times."
            the_person "I've got a few ideas that are going to blow you away... and make you cum like crazy."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            "[the_person.title] smiles, her eyes sparkling with pleasure."
            the_person "You're all done? Well, that was fucking hot either way."
            the_person "I'll repay the favour next time, alright? I promise... and I always keep my promises."

        elif used_obedience: #She only did it because she was commanded
            "[the_person.title] looks away, her face twisted in a mixture of embarrassment and arousal."
            the_person "That's it? I mean, not like I wanted to do anything more, I just thought you were going to finish."
            mc.name "Some other time. I just wanted to see what you look like when you cum."
            the_person "I... Fuck, well, I guess you got what you wanted... you always do, don't you?"

        else: # She's surprised she even tried that.
            "[the_person.title] gasps, her eyes wide with surprise."
            the_person "Oh fuck, that was intense! You really know how to make a girl feel good... and cum like crazy."
            the_person "You're probably tired after all that work. I promise I'll repay the favour next time, okay? Maybe we can even try something new... and naughty."

    elif the_report.get("guy orgasms", 0) > 0: #Only you came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            "[the_person.title] pouts, her face twisted in a mixture of disappointment and arousal."
            the_person "All tired out? Well, that's a little disappointing... but I guess I can forgive you this time."
            mc.name "Sorry, I'll make it up to you next time."
            the_person "You better. I've got some ideas that should have both of us cumming our brains out. Sound like fun?"

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            "[the_person.title] smiles, her eyes sparkling with pleasure."
            the_person "Tired out already? Well someone's being a little selfish today... but I guess I can forgive you this time."
            mc.name "Sorry, I'll make it up to you next time."
            the_person "You better, or you won't get many more \"next times\"... and I think you want more \"next times\", don't you?"

        elif used_obedience: #She only did it because she was commanded
            "[the_person.title] looks away, her face twisted in a mixture of embarrassment and arousal."
            the_person "I expect you're tired after all of that. We're done then?"
            mc.name "Yeah, that's all for now."
            "She nods, obviously a little embarrassed but doing her best not to show it... but you can tell she's still turned on."

        else:  # She's surprised she even tried that.
            "[the_person.title] gasps, her eyes wide with surprise."
            the_person "Whew, that was... intense. I think I got a little carried away there... but it was fun, wasn't it?"
            the_person "Probably a good idea we stop, before we take this too far... but I think I want to take it further next time, don't you?"

    elif the_person.energy < 10: #Nobody came and she's tired
        "[the_person.title] yawns, her eyes drooping with exhaustion."
        the_person "Sorry, but I'm too tired. I'm going to have to make it up to you some other time... maybe after a nap."
        mc.name "No problem, we will continue this another time... when you're feeling more energized."

    else: #Nobody came.
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            "[the_person.title] pouts, her face twisted in a mixture of disappointment and arousal."
            the_person "You're done already? Oh come on, we barely even got started! I was just getting warmed up."
            "She winks at you, her eyes sparkling with mischief."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            "[the_person.title] smiles, her eyes sparkling with pleasure."
            the_person "We're stopping already? We were just getting to the good stuff though! I was having so much fun."
            mc.name "Sorry [the_person.title], I'll have to make it up to you some other time."
            the_person "You better. You can't just tease a girl like this, it's not nice... but I think I like it when you're a little mean."

        elif used_obedience: #She only did it because she was commanded
            "[the_person.title] looks away, her face twisted in a mixture of embarrassment and arousal."
            the_person "That's all? Well that's not exactly what I was expecting... but I guess it was still kind of fun."
            mc.name "You aren't disappointed, are you?"
            the_person "No, I just... Thought this was all going to go somewhere more serious... but I guess I was wrong."

        else:  # She's surprised she even tried that.
            "[the_person.title] gasps, her eyes wide with surprise."
            the_person "Fuck, you're probably right. We should stop now before we take this too far... but I think I want to take it further next time, don't you?"
            the_person "If I get too turned on I might do something I regret... but I think I want to regret it, don't you?"

    # Gave creampie while she is not on birth control (extra dialogue when she could get pregnant)
    if the_report.get("creampies", 0) > 0 and not the_person.on_birth_control and not the_person.knows_pregnant:
        "[the_person.title] smiles up at you, her eyes sparkling with mischief."
        the_person "Oh baby, you are a mad dog, you must really want to see me pregnant... and I think I want to see that too."

    $ del comment_position
    return

## Role Specific Section ##
label vt_wild_improved_serum_unlock(the_person):
    mc.name "[the_person.title], now that you've had some time to get used to the lab there is something I want to talk to you about."
    "[the_person.title] looks up from her work, a curious expression on her face."
    the_person "Ooh, what's on your mind? Something juicy, I hope?"
    mc.name "Our R&D up to this point has been based on my old notes from university."
    mc.name "There were some unofficial experiment results that suggested the effects might be enhanced by sexual arousal."
    "[the_person.title] raises an eyebrow, a sly smile spreading across her face."
    the_person "Ah, you're talking about the old 'sex makes everything better' theory? I've got some thoughts on that myself."
    mc.name "What else can we do if we assume that is true? Does that open up any more paths for our research?"
    "[the_person.title] leans in, a conspiratorial look on her face."
    the_person "If it's true, I think we could be onto something huge. I could leverage the effect to induce greater effects in our subjects... and maybe even in ourselves."
    "[the_person.possessive_title!c] winks at you, her eyes sparkling with mischief."
    the_person "But we'll need to do some experiments to be sure. And I've got just the thing in mind."
    mc.name "What sort of experiments?"
    "[the_person.title] leans back in her chair, a sly smile still plastered on her face."
    the_person "I want to take a dose of serum myself, and you can record the effects. Then I'll make myself cum, and we can compare the effects after."
    mc.name "Do you think that's a good idea?"
    the_person "Not entirely, no. But we can't trust anyone else with this information if we're right. And I'm willing to take the risk if it means we can make some real progress."
    the_person "We might be able to make progress by brute force, but this is a chance to catapult our knowledge to another level. And I'm not going to let a little thing like caution hold me back."
    the_person "A finished dose of serum that raises my Suggestibility. The higher it gets my Suggestibility the better, but any amount should do."
    the_person "Then we'll just need some time and some privacy for me to see what sort of effects my orgasms will have. And maybe, just maybe, we'll stumble upon something amazing."
    return

#
# label vt_wild_improved_serum_unlock(the_person):
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
label vt_wild_kissing_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 30:
        "[the_person.title] looks up at you with a flirtatious smile, her eyes sparkling with excitement."
        the_person "Come on then, we both know where this is going. You've always wanted to kiss me, right? And I've always wanted you to."
        "[the_person.title] takes a step closer, her body language inviting you to make a move."

    elif the_person.love >= 20:
        "[the_person.title] looks up at you with a sly smile, her eyes flashing with anticipation."
        the_person "So we're doing this, huh? Finally."
        mc.name "I guess we are. What do you think?"
        "[the_person.title] leans in, her voice barely above a whisper."
        the_person "It's about time, I've wanted to make out with you for a long time. And I think I'm going to enjoy it."

    else:
        "[the_person.title] looks up at you with a nervous expression, her eyes darting back and forth."
        the_person "I don't know about this [the_person.mc_title], do you think we're taking this too fast?"
        mc.name "Are you scared?"
        "[the_person.title] shakes her head, her hair flying back and forth."
        the_person "No! Just... Nervous. Excited, maybe. I don't know what's going to happen next."
        mc.name "Then just trust me."
        "[the_person.title] nods, her eyes locked on yours as she waits for you to make a move."
    return

label vt_wild_touching_body_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 30:
        "[the_person.title] looks up at you with a sly smile, her eyes sparkling with mischief."
        the_person "Are you sure about this? I don't want you to chicken out on me... I'm ready to take things to the next level."
        mc.name "Oh, I'm sure."
        "[the_person.title] nods, her face lighting up with excitement."
        the_person "Good. Come on then! Let's see where this takes us."
    elif the_person.love >= 20:
        "[the_person.title] looks up at you with a nervous smile, her eyes darting back and forth."
        the_person "So you're ready for this?"
        "You nod, and [the_person.title] takes a deep breath."
        the_person "Me too, I think. I didn't think I'd be so nervous when you actually made a move... but I'm glad you did."
        mc.name "Just relax. You trust me, right."
        "[the_person.title] nods, her eyes locked on yours."
        the_person "Of course. I trust you completely."
    else:
        "[the_person.title] looks up at you with a hesitant expression, her eyes flashing with uncertainty."
        the_person "I think you're getting a little ahead of yourself here [the_person.mc_title]."
        mc.name "What do you mean?"
        "[the_person.title] takes a step back, her hands on her hips."
        the_person "I mean I don't just let anyone feel me up. Maybe we should cool things down... before things get out of hand."
        mc.name "You're not scared, are you?"
        "[the_person.title] rolls her eyes, a smile playing on her lips."
        the_person "Scared? Of course not! I'm just... cautious. Yeah, that's it."
        mc.name "Well then just relax and go with it. It doesn't have to mean anything unless we want it to."
        "[the_person.title] looks up at you, her eyes sparkling with mischief."
        the_person "You're so bad for me, you know that? But I think I like it."
        mc.name "Well let me make up for it then."
        "[the_person.title] nods, her face lighting up with excitement."
    return

label vt_wild_touching_penis_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 35:
        "[the_person.title] looks down at your crotch, her eyes widening with excitement."
        the_person "Mmm, you're really turned on too, right? Look how big you are... I can already imagine what it would be like to have that inside me."
        mc.name "Do you want to feel it?"
        "[the_person.title] nods eagerly, her hands reaching out to grab your cock."
        the_person "I thought you'd never ask... I've been dying to get my hands on that thing."

    elif the_person.love >= 20:
        "[the_person.title] looks up at you with a sly smile, her eyes sparkling with mischief."
        the_person "Your cock looks so nice when it's hard. Can I touch it? I promise I'll be gentle... or not, depending on what you like."
        mc.name "Go ahead, it doesn't bite."
        "[the_person.title] giggles, her hands reaching out to grab your cock."
        the_person "If you're lucky it might choke me though... but I think I'd like that."

    else:
        mc.name "My cock is so hard right now [the_person.title]. Put your hand on it and touch it for me."
        "[the_person.title] looks up at you with a hesitant expression, her eyes flashing with uncertainty."
        the_person "What? That's taking things a little far, don't you think? I'm not sure I'm ready for that... but at the same time, I'm really curious."
        mc.name "Come on, you know you want to. Just a few strokes, then if you aren't impressed you can stop."
        "[the_person.title] looks down at your crotch, her eyes fixed on your cock as she considers your request."
    return

label vt_wild_touching_vagina_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 35:
        "[the_person.title] looks up at you with a daring smile, her eyes sparkling with excitement."
        the_person "Don't chicken out on me now, you've got your chance to touch my pussy... and I'm not going to let you get away that easily."
        "[the_person.title] spreads her legs, inviting you to touch her."

    elif the_person.love >= 20:
        "[the_person.title] looks up at you with a sultry smile, her eyes flashing with desire."
        the_person "Oh fuck, you've got my pussy tingling. I want you to touch it [the_person.mc_title]... I need you to touch it."
        "[the_person.title] takes your hand, guiding it to her pussy."

    else:
        "[the_person.title] looks up at you with a nervous expression, her eyes darting back and forth."
        the_person "I don't know if we should be doing this [the_person.mc_title]... it feels so wrong, but at the same time, it feels so right."
        mc.name "Just take a deep breath and relax. I'm just going to touch you a little, and if you don't like it I'll stop."
        "[the_person.title] hesitates, her eyes fixed on yours as she considers your request."
        the_person "Just a little?"
        mc.name "Just a little. Trust me, it's going to feel amazing."
        "[the_person.title] nods, her face set in a determined expression."
        the_person "Okay... but if I don't like it, I'm blaming you."
    return

label vt_wild_sucking_cock_taboo_break(the_person):
    mc.name "I want you to do something for me."
    "[the_person.title] looks up at you with a sly smile, her eyes sparkling with curiosity."
    the_person "Oh yeah? What do you want me to do to you? Something naughty, I hope?"
    mc.name "I want you to suck on my cock."
    if the_person.effective_sluttiness() >= 45:
        "[the_person.title] grins, her eyes flashing with excitement."
        the_person "Mmm, I think I'm up for that. It's not going to be too big for me, is it?"
        mc.name "I think you'll be able to handle it."
        "[the_person.title] winks at you, her tongue darting out to lick her lips."
        the_person "Alright, I don't want it choking me... but at the same time, I kind of do."
        "She bites her lip and leans in, her eyes locked on your cock."

    elif the_person.love >= 30:
        "[the_person.title] looks up at you with a sultry smile, her eyes flashing with desire."
        the_person "I guess we've been dancing around it for a while... but I think I'm ready to take the leap."
        "She bites her lip and looks your body up and down, her eyes lingering on your cock."
        the_person "Alright, let's do this. I want to taste you."

    else:
        "[the_person.title] looks up at you with a nervous expression, her eyes darting back and forth."
        the_person "Oh, I was wondering if this was going to come up... I'm not sure if I'm ready for this."
        "She laughs nervously and looks away from you, her face flushing with embarrassment."
        the_person "I don't know [the_person.mc_title]... this is all so new to me."
        "You reach up and hold her chin, turning her head back to face you. She looks up at you with a mixture of fear and desire in her eyes."
        mc.name "Don't overthink it. Just kneel down and suck on it for me. If you don't like doing it, we can just forget it happened."
        "You can see in her eyes the moment her resolve breaks. She bites her lip and nods, a determined look on her face."
        the_person "Alright, let's do this. I'll try anything once... or twice... or maybe more."
    return

label vt_wild_licking_pussy_taboo_break(the_person):
    mc.name "I want to taste your pussy [the_person.title]. Are you ready?"
    if the_person.effective_sluttiness() >= 45:
        "[the_person.title] grins, her eyes flashing with excitement."
        the_person "I was just about to ask you to try that. So yeah, I'm ready! I've been waiting for this moment for a long time."
        "She spreads her legs, inviting you to taste her pussy."

    elif the_person.love >= 30:
        "[the_person.title] looks up at you with a sultry smile, her eyes sparkling with desire."
        the_person "Oooh, finally a man who doesn't expect blowjobs all day but never licks a pussy. You're a true gentleman... or at least, a true lover."
        "She bites her lip and smiles at you, her face flushing with excitement."
        the_person "Alright then, get to it lover boy. Show me what you're working with."

    else:
        if the_person.has_taboo("sucking_cock"):
            "[the_person.title] looks up at you with a surprised expression, her eyes wide with excitement."
            the_person "Really? I haven't even sucked your cock yet and you're ready to go down on me? You're a bold one, I like that."
            "She bites her lip and smiles, her face flushing with desire."
            the_person "I could get used to this! Get to it, and don't hold back."

        else:
            "[the_person.title] looks up at you with a sly smile, her eyes sparkling with mischief."
            the_person "It's about time you offered to repay the favour! Most guys think they're the only one who should get some head... but not you, you're different."
            "She bites her lip and smiles, her face flushing with excitement."
            the_person "Alright then, get to it! Show me what you're working with, and don't disappoint me."
    return

label vt_wild_vaginal_sex_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 60:
        "[the_person.title] looks up at you with a fierce expression, her eyes blazing with desire."
        the_person "It's about time we did this. Come on then, get that cock inside me and fuck me like you mean it! I'm ready to take it all in."
        "She spreads her legs wide, inviting you to enter her."

    elif the_person.love >= 45:
        "[the_person.title] looks up at you with a sly smile, her eyes sparkling with excitement."
        the_person "Are you ready for this? I hope you're planning to rock my world... because I'm ready to rock yours."
        mc.name "That is the plan, I hope you can handle it."
        "She nods, her face set in a determined expression."
        the_person "I can handle anything you can throw at me. Come on then, fuck me like you mean it! I want to feel you deep inside me."

    else:
        if the_person.has_taboo("anal_sex"):
            "[the_person.title] looks down at your cock, her eyes widening with a mix of fear and excitement."
            the_person "Look at that cock... Fuck, I hope you don't stretch out my pussy too badly. But at the same time, I kind of hope you do."
            "She looks up at you, her eyes sparkling with mischief."

        else:
            "[the_person.title] looks up at you with a sly smile, her eyes sparkling with excitement."
            the_person "If your cock feels half as big in my pussy as it did up my ass I'm in for a good time... and I think I'm going to love it."
            the_person "Come on, fuck me [the_person.mc_title]! I want to feel you inside me, and I want it now."
            "She spreads her legs wide, inviting you to enter her."
    return

label vt_wild_anal_sex_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 75:
        "[the_person.title] looks down at your cock, her eyes widening with a mix of excitement and anticipation."
        the_person "Oh god, it always surprises me how big your cock is! You're going to tear my ass in half with that monster... and I'm going to love every minute of it!"
        "She seems more turned on by the idea than worried, her body language screaming 'fuck me' as she spreads her legs wide."
        mc.name "Don't worry, you'll be stretched out soon enough."
        "She nods, her eyes sparkling with mischief as she prepares for the ride of her life."

    elif the_person.love >= 60:
        "[the_person.title] looks up at you with a sly smile, her eyes sparkling with excitement."
        the_person "So you really want to do this? It might be a little hard to fit all of your cock inside me... but I'm willing to try if you are."
        mc.name "Don't worry about that, I'll have you stretched out soon enough."
        "She giggles, her face lighting up with anticipation."
        the_person "Fuck, just try and make sure you don't break me permanently! I want to be able to walk tomorrow."

    else:
        if the_person.has_taboo("vaginal_sex"):
            "[the_person.title] looks down at your cock, her eyes widening with a mix of fear and excitement."
            the_person "Are you sure my pussy wouldn't be tight enough for you, I don't even know if I can fit your cock in my ass! You're so big..."
            mc.name "I'll make it fit, but you might not be walking right for a few days."
            "She gasps, her eyes sparkling with a mix of fear and anticipation."
            the_person "Oh fuck... I think I'm in trouble."

        else:
            "[the_person.title] closes her eyes and takes a deep breath, her body language screaming 'I'm ready for this'."
            the_person "Whew, deep breaths [the_person.fname]. You can do this... just relax and let him in."
            mc.name "Are you okay?"
            "[the_person.title] opens her eyes, her expression set in determination."
            the_person "Yeah, of course. I'm just... a little nervous. Fuck, I don't normally feel like this... but I think I like it."
            "She laughs and shakes her head, her eyes sparkling with mischief."
            the_person "Not that I normally do, you know, this. I don't know what's gotten into me... but I think I'm going to enjoy it."
            mc.name "Hopefully me, soon."
            "She nods, her face lighting up with anticipation."
            the_person "No time like the present then. Do it, before I chicken out! I'm ready for you."
    return

label vt_wild_condomless_sex_taboo_break(the_person):
    if the_person.knows_pregnant:
        "[the_person.title] smiles slyly, her eyes sparkling with mischief."
        the_person "You want to fuck me raw? That's pretty hot... and I'm already pregnant, so what's the worst that could happen?"
        if the_person.wants_creampie:
            "[the_person.title] leans in, her voice barely above a whisper."
            the_person "Please pump me full of your hot cum, we both would love that... and who knows, maybe we'll even get lucky and have twins."
        else:
            "[the_person.title] winks at you, her eyes sparkling with excitement."
            the_person "Please cover me with all your hot cum... I want to feel it dripping down my thighs."
    elif the_person.opinion.bareback_sex > 0:
        "[the_person.title] grins mischievously, her eyes sparkling with excitement."
        the_person "You want to fuck me raw? That's pretty hot... and I'm always up for a little risk."
        if the_person.on_birth_control:
            "[the_person.title] shrugs, her expression nonchalant."
            the_person "I'm on the pill, so you don't need to worry about cumming inside me... but where's the fun in that?"
            $ the_person.update_birth_control_knowledge()
        elif the_person.wants_creampie:
            "[the_person.title] leans in, her voice barely above a whisper."
            the_person "It would be so easy for you to cum inside me though... and I think I'd love every minute of it."
            "[the_person.title] doesn't sound like she would mind very much at all."
        elif the_person.opinion.creampies < 0:
            "[the_person.title] frowns, her expression serious."
            the_person "You better make sure you pull out though. I'd be pissed if you got me knocked up... and I think you would be too."
        else:
            "[the_person.title] shrugs, her expression nonchalant."
            the_person "You'll need to pull out so you don't knock me up then. Got it? Good... but don't think this means I'm not going to enjoy every minute of it."
    elif the_person.love > 60:
        if the_person.on_birth_control:
            "[the_person.title] smiles slyly, her eyes sparkling with mischief."
            the_person "You want to fuck me raw? Fuck it, I'm on the pill. What's the worst that can happen... besides us having the best sex of our lives?"
            $ the_person.update_birth_control_knowledge()
        elif the_person.wants_creampie:
            "[the_person.title] leans in, her voice barely above a whisper."
            the_person "I guess if I can't trust you I can't trust anyone. You make me make terrible decisions, you know that?"
            "[the_person.title] winks at you, her eyes sparkling with excitement."
            the_person "Well fuck it, if we're doing this I want you to go the whole nine yards and finish inside me... and maybe even get me pregnant."
            mc.name "Are you on the pill?"
            "[the_person.title] shakes her head, her expression serious."
            the_person "Of course not. If we're fucking raw I want you to be trying to get me knocked up every single time... and I think I'd love every minute of it."
            $ the_person.update_birth_control_knowledge()
        elif the_person.opinion.creampies < 0:
            "[the_person.title] frowns, her expression serious."
            the_person "I guess if I can't trust you I can't trust anyone. You make me make terrible decisions, you know that?"
            "[the_person.title] looks up at you, her eyes sparkling with a mix of fear and excitement."
            the_person "You'll need to pull out though. If you get me knocked up there's no way we're ever doing it unprotected again... and I think I'd actually be pretty okay with that."
        else:
            "[the_person.title] smiles slyly, her eyes sparkling with mischief."
            the_person "I guess if I can't trust you I can't trust anyone. You make me make terrible decisions, you know that?"
            if the_person.kids == 0:
                "[the_person.title] leans in, her voice barely above a whisper."
                the_person "I need you to pull out though. I'm not quite ready to be a mother, even with you... but maybe someday soon."
            elif the_person.kids == 1:
                "[the_person.title] shrugs, her expression nonchalant."
                the_person "I need you to pull out though. I've already got a kid, I don't need another one... but maybe someday we can have another one together."
            else:
                "[the_person.title] rolls her eyes, her expression playful."
                the_person "I need you to pull out though. I've already got kids, I don't need another one... but maybe someday we can have a whole soccer team together."
    else:
        if the_person.on_birth_control:
            "[the_person.title] shrugs, her expression nonchalant."
            the_person "Yeah, you want to fuck me raw? Well, I'm on the pill, so why not? It's not like I'm going to end up pregnant... but maybe that would be kind of fun."
            $ the_person.update_birth_control_knowledge()
        elif the_person.has_taboo("vaginal_sex"):
            "[the_person.title] looks up at you, her eyes sparkling with a mix of fear and excitement."
            the_person "You really don't think we should use a condom? I'm not on the pill, aren't you worried about knocking me up?"
            $ the_person.update_birth_control_knowledge()
            "[the_person.title] winks at you, her eyes sparkling with mischief."
            the_person "Or is this your master plan to sneak a baby into me? Because if it is, I have to admit, it's kind of working."
            mc.name "I promise I'll pull out. Don't you want our first time together to be special?"
            "[the_person.title] rolls her eyes and sighs, her expression playful."
            the_person "God damn it, now you're getting me all sentimental. Fine, you don't need to put anything on."
            "[the_person.title] looks up at you, her eyes sparkling with a mix of fear and excitement."
            the_person "But you better fucking pull out, understand? Good... because I don't think I'm ready for a baby just yet."
        else:
            "[the_person.title] looks up at you, her eyes sparkling with a mix of fear and excitement."
            the_person "You really don't think we should use a condom? I'm not on the pill, aren't you worried about knocking me up?"
            $ the_person.update_birth_control_knowledge()
            "[the_person.title] shrugs, her expression nonchalant."
            the_person "Or is this your master plan to sneak a baby into me? Because if it is, I have to admit, it's kind of tempting."
            mc.name "I promise I'll pull out. It'll feel so much better without anything between us."
            "[the_person.title] sighs dramatically, her expression playful."
            the_person "Fuck, I know. I'm trying to make this decision with my head and not my clit... but my clit is winning."
            "[the_person.title] winks at you, her eyes sparkling with mischief."
            the_person "Fine, you don't need to put anything on. Just be fucking sure to pull out, understand? Good... because I don't think I'm ready for a baby just yet."
    return

label vt_wild_underwear_nudity_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > 30 - (the_person.opinion.skimpy_outfits * 5):
        "[the_person.title] looks up at you with a sly smile, her eyes sparkling with mischief."
        the_person "You want to see me in my underwear, huh? It's about time you asked... I was starting to think you were too shy."
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "What are we waiting for then, let's get this off of you."
            "[the_person.title] giggles and nods, her hands already reaching for the hem of her [the_clothing.display_name]."
        else:
            mc.name "About time? Are you forgetting I've seen you naked already?"
            "[the_person.title] shrugs, her expression nonchalant."
            the_person "It's something called fashion, some men are into it. Come on, let's get this off... and see if you can handle the real me."

    elif the_person.love > 15:
        "[the_person.title] looks up at you with a flirtatious smile, her eyes sparkling with excitement."
        the_person "You want me to strip me down a little? It's about time, I was wondering why you were taking things so slow... I thought you were more of a wild one."
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "Well then let's stop wasting time and get your [the_clothing.display_name] off."
            "[the_person.title] nods, her face lighting up with anticipation."

        else:
            mc.name "Slow? I've already seen you naked, remember?"
            "[the_person.title] giggles and nods, her eyes sparkling with mischief."
            the_person "I guess, but being in my underwear feels more romantic, you know? It's like we're sharing a secret."
            mc.name "Well let's get more romantic then and get your [the_clothing.display_name] off."
            "[the_person.title] nods, her hands already reaching for the hem of her [the_clothing.display_name]."

    else:
        "[the_person.title] looks up at you with a hesitant expression, her eyes flashing with uncertainty."
        the_person "If you take my [the_clothing.display_name] I'll only have my underwear on, you know that?"
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "Yeah, that's kind of the point."
            "[the_person.title] shakes her head and laughs to herself, her expression a mix of excitement and nervousness."
            the_person "Oh [the_person.title], what have you gotten yourself into! Come on, let's do this before I chicken out... and see where things go."
        else:
            mc.name "Yeah, that's kind of the point. I've already seen you naked, so what are you worrying about?"
            "[the_person.title] rolls her eyes, her expression playful."
            the_person "Whatever, I guess you're right. Come on, let's get it off... and see what kind of trouble we can get into."
    return

label vt_wild_bare_tits_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > (40 - the_person.opinion.showing_her_tits * 5):
        "[the_person.title] looks up at you with a sly smile, her eyes sparkling with mischief."
        the_person "You finally want a look at my tits [the_person.mc_title], huh? It's about time, I was starting to think you were too shy."
        if the_person.has_large_tits:
            "She shakes her chest for you, jiggling the [the_person.tits_description] hidden underneath her [the_clothing.display_name]."
            "Her breasts bounce and sway, drawing your attention to the generous cleavage on display."
        else:
            "She shakes her chest and gives her [the_person.tits_description] a little jiggle, her eyes sparkling with playfulness."
        the_person "What took you so long to ask? I've been waiting for this moment for a while now."
        if the_person.has_large_tits:
            mc.name "No time like the present, right? Let's get those puppies out where I can enjoy them."
            "[the_person.title] giggles and nods, her hands already reaching for the hem of her [the_clothing.display_name]."
        else:
            mc.name "No time like the present, right? Let's get those cute little things out."
            "[the_person.title] smiles and nods, her eyes sparkling with excitement."

    elif the_person.love > 25:
        "[the_person.title] looks up at you with a flirtatious smile, her eyes sparkling with excitement."
        the_person "Ready to see my tits [the_person.mc_title]?"
        if the_person.has_large_tits:
            "She shakes her chest and jiggles her nice [the_person.tits_description], barely restrained by her [the_clothing.display_name]."
            "Her breasts bounce and sway, drawing your attention to the generous cleavage on display."
        else:
            "She shakes her chest, giving her [the_person.tits_description] a little jiggle, her eyes sparkling with playfulness."
        mc.name "Oh yeah, I'm ready."
        "[the_person.title] nods, her face lighting up with anticipation."
        the_person "Let 'em out then, and have fun... I want to see the look on your face when you see my tits for the first time."

    else:
        "[the_person.title] looks up at you with a hesitant expression, her eyes flashing with uncertainty."
        the_person "Wait a second! Jesus, you should at least ask a girl before you try and put her tits on full display... don't you think?"
        mc.name "Come on, don't you want to show them off? I bet they look great."
        "[the_person.title] blushes, her face lighting up with embarrassment."
        the_person "Oh, they do. I just... Feel a little self-conscious about being naked around you, alright? You're kind of intimidating."
        mc.name "There's no need to be, just relax and let me take your [the_clothing.display_name] off for you."
        "[the_person.title] nods, her eyes sparkling with a mix of excitement and nervousness."
        the_person "Oh man, what are you getting me into [the_person.mc_title]? Fine, let's do it... and see where things go."
    return

label vt_wild_bare_pussy_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > (50 - the_person.opinion.showing_her_ass * 5):
        "[the_person.title] looks up at you with a sly smile, her eyes sparkling with mischief."
        the_person "It's about time you got me out of my [the_clothing.display_name]! I've been waiting for this moment for a while now."
        "She spreads her legs wide, inviting you to take a closer look."

    elif the_person.love > 35:
        "[the_person.title] looks up at you with a flirtatious smile, her eyes sparkling with excitement."
        the_person "You want to get me out of my [the_clothing.display_name] and get a look at my pussy?"
        if the_person.has_taboo("touching_vagina"):
            mc.name "I know, that was the plan."
            "[the_person.title] nods, her face lighting up with anticipation."
            the_person "Well... I guess we both knew where this was going. Okay, go for it... but be gentle, I'm a little nervous."
        else:
            mc.name "I've already felt it up, I thought I should see it too."
            "[the_person.title] giggles and nods, her eyes sparkling with mischief."
            the_person "I think you're right. Go on then, I'm not going to stop you... but don't think you're getting off that easy, I want to see some action."

    else:
        "[the_person.title] looks up at you with a hesitant expression, her eyes flashing with uncertainty."
        the_person "Already trying to get me out of my [the_clothing.display_name], huh? You're a little forward, aren't you?"
        if the_person.has_taboo("touching_vagina"):
            mc.name "Yep, I am. Any problems with that?"
            "[the_person.title] blushes, her face lighting up with embarrassment."
            the_person "Well... Maybe if you ask nicely... and promise to be gentle."
            mc.name "[the_person.title], can I please take your [the_clothing.display_name] off and get a look at your pussy?"
            "[the_person.title] nods, her eyes sparkling with a mix of excitement and nervousness."
            the_person "You're such a charmer. Of course you can... but don't think this means I'm going to let you do whatever you want."
        else:
            mc.name "Yep, I am. I've already felt your pussy up, I want to get a look at it now."
            "[the_person.title] rolls her eyes, her expression playful.]"
            the_person "Oh you're such a charmer. Alright then, what are you waiting for? Get to it, and don't disappoint me."
    return

# label vt_wild_facial_cum_taboo_break(the_person):

#     return

# label vt_wild_mouth_cum_taboo_break(the_person):

#     return

# label vt_wild_body_cum_taboo_break(the_person):

#     return

label vt_wild_creampie_taboo_break(the_person):
    if the_person.wants_creampie:
        if the_person.knows_pregnant:
            "[the_person.title] looks up at you with a radiant smile, her eyes sparkling with joy."
            the_person "Oh yes, shoot your hot load deep inside me... I can already imagine the possibilities."
            "She sighs happily, her body language screaming 'I'm in heaven'."

        elif the_person.on_birth_control:
            if the_person.has_significant_other:
                "[the_person.title] looks up at you with a sly smile, her eyes sparkling with mischief."
                the_person "Oh my god, I'm such a horrible [the_person.so_girl_title], but I really needed this... and I'm not sorry about it at all."
                the_person "He'd understand, right? A girl has needs... and I need to get fucked like this more often."

            else:
                "[the_person.title] looks up at you with a flirtatious smile, her eyes sparkling with excitement."
                the_person "Oh my god, I needed this so badly! Ah... that feels so much better."

        elif the_person.effective_sluttiness() > 75 or the_person.opinion.creampies > 0:
            if the_person.has_significant_other:
                "[the_person.title] looks up at you with a fierce expression, her eyes blazing with desire."
                the_person "Oh god, I've wanted a good creampie for so long! And now I've finally found someone who can give it to me."
                the_person "I'm a terrible [the_person.so_girl_title], but I really just want a man to fuck me, cum in me, and knock me up... and I don't care who knows it!"

            else:
                "[the_person.title] looks up at you with a wild expression, her eyes sparkling with excitement."
                the_person "Oh god, I've wanted a good creampie for so long! And now I've finally found someone who can give it to me."
                the_person "I've finally found a man to fuck me, cum in me, and knock me up... and I'm not going to let him go!"

            "She sighs happily, her body language screaming 'I'm in heaven'."
            the_person "How long until you're ready for round two? I want as much of your cum inside my pussy as possible... and I'm not going to stop until I get it."

        else:
            if the_person.has_significant_other:
                "[the_person.title] looks up at you with a guilty expression, her eyes flashing with uncertainty."
                the_person "Oh fuck... I'm such a terrible [the_person.so_girl_title]! But that felt so good... and I'm not sorry about it at all."
                "She sighs happily, her body language screaming 'I'm in heaven'."

            else:
                "[the_person.title] looks up at you with a worried expression, her eyes flashing with concern."
                the_person "Oh fuck, that was so risky... but it felt so good! I guess I'll just have to hope for the best."
                "She sighs happily, her body language screaming 'I'm in heaven'."
            the_person "I'll just have to hope you haven't knocked me up. We really shouldn't do this again, my luck is going to run out at some point... but I'm not going to stop until it does."

    else:
        if the_person.knows_pregnant:
            "[the_person.title] looks up at you with a shocked expression, her eyes wide with surprise."
            the_person "Oh shit, you came right inside me... I didn't expect that at all."

        elif not the_person.on_birth_control:
            "[the_person.title] looks up at you with a worried expression, her eyes flashing with concern."
            the_person "Oh fuck, did you cum inside me? What if I get pregnant? I'm not ready for that kind of responsibility... and I don't think you are either."
            if the_person.has_significant_other:
                the_person "What if you just got me pregnant? I would be the worst [the_person.so_girl_title] of all time... and I don't think I could handle the guilt."
            else:
                the_person "What if I get pregnant? I'm not ready for that kind of responsibility... and I don't think I could handle it on my own."
            the_person "You're going to have to wear a condom if we ever do this again, I just can't risk it... and I don't think you can either."

        elif the_person.has_significant_other:
            "[the_person.title] looks up at you with a stern expression, her eyes flashing with anger."
            the_person "Did you really just creampie me after I told you to pull out? God, I'm such a terrible [the_person.so_girl_title]... and you're not much better."
            "[She sighs unhappily, her body language screaming 'I'm not happy about this'.]"
            the_person "Maybe next time I'll make you wear a condom as punishment... and maybe next time you'll actually listen to me."

        elif the_person.opinion.creampies < 0:
            "[the_person.title] looks up at you with a disgusted expression, her eyes flashing with annoyance."
            the_person "Oh man, really? Ugh, I hate this feeling... it's so messy and gross. Couldn't you have cum on my face or something instead?"

        else:
            "[the_person.title] looks up at you with a frustrated expression, her eyes flashing with irritation."
            the_person "Hey, I said to pull out! What's wrong with you, can't you even follow simple instructions?"
            "[She sighs unhappily, her body language screaming 'I'm not happy about this'.]"
            the_person "Whatever, can you at least try to pull out next time? I don't want to have to deal with this again... and I don't think you do either."
    return

label vt_wild_anal_creampie_taboo_break(the_person):
    if the_person.opinion.anal_creampies > 0:
        if the_person.effective_sluttiness() > 75 or the_person.opinion.anal_creampies > 1:
            if the_person.has_significant_other:
                "[the_person.title] looks up at you with a sly smile, her eyes sparkling with mischief."
                the_person "Ah, finally! I don't even care that it's not my [the_person.so_title] shooting his cum in my ass... you're so much better at it anyway."
                "She winks at you, her expression playful."

            else:
                "[the_person.title] looks up at you with a wild expression, her eyes blazing with desire."
                the_person "Ah, finally! You should have put a load inside my ass sooner... I've been waiting for this moment for so long."
                "She pants happily for a moment, her chest heaving with excitement."

            the_person "Fuck yeah, I will be dripping cum out of my ass all day long! That's so hot... and I'm so turned on right now."
            "She looks up at you with a flirtatious smile, her eyes sparkling with mischief."

        else:
            if the_person.has_significant_other:
                "[the_person.title] looks up at you with a guilty expression, her eyes flashing with uncertainty."
                the_person "Fuck me, I should have told you to pull out, but I love this feeling... it's so wrong, but it feels so right."
                the_person "My [the_person.so_title] never shoots his cum in my ass, but you can do it anytime... just don't tell him, okay?"

            else:
                "[the_person.title] looks up at you with a sly smile, her eyes sparkling with mischief."
                the_person "Fuck yeah, promise you will fill my ass every time... it just feels awesome... and I love the way it makes me feel."
                the_person "All that cum in my tight little ass... it's like a dream come true."

    else:
        if the_person.has_significant_other:
            "[the_person.title] looks up at you with a stern expression, her eyes flashing with anger."
            the_person "Fuck [the_person.mc_title], I told you to pull out. My [the_person.so_title] will see your cum leaking out of my ass... and I don't think he'll be happy about it."
            the_person "So next time, just shoot your load on my ass, okay? I don't want to have to deal with the drama."

        elif the_person.opinion.anal_creampies < -1:
            "[the_person.title] looks up at you with a disgusted expression, her eyes flashing with annoyance."
            the_person "Fuck [the_person.mc_title], I said to pull out! I'll be dripping cum out of my ass all day long... and I hate the way it feels."

        else:
            "[the_person.title] looks up at you with a playful expression, her eyes sparkling with mischief."
            the_person "Fuck [the_person.mc_title], not inside! My ass is not a sperm bank, although that sounds quite hot... maybe we can try that next time."
            "She winks at you, her expression flirtatious."
    return

label vt_wild_dual_penetration_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 75:
        "[the_person.title] looks up at you with a wild expression, her eyes blazing with desire."
        the_person "Oh god, it always surprises me how big your cock is! You're going to tear my ass in half with that monster... and I'm going to love every minute of it!"
        "She spreads her legs wide, inviting you to take a closer look."
        mc.name "Don't worry, you'll be stretched out soon enough."
        "[the_person.title] nods, her face lighting up with anticipation."

    elif the_person.love >= 60:
        "[the_person.title] looks up at you with a flirtatious smile, her eyes sparkling with excitement."
        the_person "So you really want to do this? It might be a little hard to fit all of your cock inside me... but I'm willing to try if you are."
        mc.name "Don't worry about that, I'll have you stretched out soon enough."
        "[the_person.title] giggles, her face lighting up with anticipation."
        the_person "Fuck, just try and make sure you don't break me permanently... but I think I can handle it."

    else:
        if the_person.has_taboo("vaginal_sex"):
            "[the_person.title] looks up at you with a hesitant expression, her eyes flashing with uncertainty."
            the_person "Are you sure my pussy wouldn't be tight enough for you, I don't even know if I can fit your cock in my ass... it's a little intimidating."
            mc.name "I'll make it fit, but you might not be walking right for a few days."
            "[the_person.title] gasps, her eyes wide with surprise."
            the_person "Oh fuck... I don't know if I'm ready for this."

        else:
            "[the_person.title] closes her eyes and takes a deep breath, her body language screaming 'I'm ready for this'."
            the_person "Whew, deep breathes [the_person.fname]. You can do this... just relax and let him in."
            mc.name "Are you okay?"
            "[the_person.title] opens her eyes, her expression set in determination."
            the_person "Yeah, of course. I'm just... a little nervous. Fuck, I don't normally feel like this... but I think I like it."
            "She laughs and shakes her head, her eyes sparkling with mischief."
            the_person "Not that I normally do, you know, this. I don't know what's gotten into me... but I think I'm going to enjoy it."
            mc.name "Hopefully me, soon."
            "[the_person.title] nods, her face lighting up with anticipation."
            the_person "No time like the present then. Do it, before I chicken out... and let's see where things go."
    return

label vt_wild_sleepover_yourplace_response(the_person): #Invited her over to spend the night
    if the_person.sluttiness < 80:
        "[the_person.title] squeals with excitement, her eyes sparkling with anticipation."
        the_person "Oh god, yes of course! We can have a great night together! I'll bring my favorite PJs... or maybe not, who needs those anyway?"
        "[the_person.title] winks at you, her face lighting up with a mischievous grin."

    else:
        "[the_person.title] looks up at you with a sultry smile, her eyes flashing with desire."
        the_person "Oh god, I can't wait for you to go crazy on me. Make sure you have your battery charged, so we can have a great night... and by great night, I mean a night of non-stop sex and debauchery."
        "[the_person.title] leans in, her voice barely above a whisper."
        the_person "I'm ready to be ravished, and I know you're the man to do it."
    return

label vt_wild_sleepover_herplace_response(the_person): #Spending the night at her place
    if the_person.sluttiness < 80:
        "[the_person.title] smiles sweetly, her eyes sparkling with excitement as she bounces up and down."
        the_person "I would love it when you come over, you can spend the night and make me float on cloud nine... or maybe even higher than that!"
        "[the_person.title] winks at you, her face lighting up with a playful grin as she blows you a kiss."
        the_person "I'll make sure to clear my schedule, so we can have a night to remember... and maybe even make some noise that the neighbors will never forget!"

    else:
        "[the_person.title] looks up at you with a sultry smile, her eyes flashing with desire as she licks her lips."
        the_person "Oh baby, you can pound me all night long, screw the neighbours... I'm sure they'll just be jealous of the noise we're making... and the fact that I'm getting fucked by a stud like you!"
        "[the_person.title] leans in, her voice barely above a whisper as she whispers in your ear."
        the_person "I want to feel you deep inside me, all night long... and I don't care who hears us. I want to scream your name at the top of my lungs and make the whole neighborhood know that I'm yours."
        "[the_person.title] takes your hand, pulling you towards her with a seductive smile as she leads you to her bedroom."
    return

label vt_wild_sleepover_yourplace_sex_start(the_person): #Right before sexy times at your place
    "[the_person.title] saunters over to you, her hips swaying seductively as she moves."
    "She gives you a sly smile, her eyes sparkling with mischief as she looks you up and down."
    the_person "Well, are you ready to show me a good time? I hope you're not planning on getting any sleep tonight, because I'm just getting started."
    "[the_person.title] takes a step closer, her voice dropping to a sultry whisper as she leans in close to you."
    return

label vt_wild_sleepover_herplace_sex_start(the_person): #Right before sexy times at her place
    "[the_person.title] looks up at you with a sultry smile, her eyes sparkling with desire."
    the_person "Are you just going to stand there, or are you going to come and take what's yours?"
    "She raises an eyebrow, her smirk growing wider as she teases you."
    mc.name "Are you ready?"
    "[the_person.title] lets out a throaty laugh, her body language screaming 'fuck me' as she sets her wine down."
    the_person "Hah! Oh my god, I was born ready... and I've been waiting for this moment for far too long."
    "She gives you a bold smile, her eyes flashing with excitement as she crooks her finger at you."
    the_person "Get over here! I need you to fuck me hard and deep, and make me scream your name at the top of my lungs!"
    "[the_person.title] leans back on the couch, her legs spreading wide as she invites you to take her."
    return

label vt_wild_sleepover_impressed_response(the_person):  #If you've made her cum a lot
    "[the_person.title] looks up at you with a dazed expression, her eyes sparkling with pleasure."
    the_person "Ah fuck, you're melting my brain... promise me you keep fucking me like that, and I'll be your sex slave forever!"
    $ the_person.draw_person(position = "missionary")
    "[the_person.title] lies down in bed, her body trembling with aftershocks as she catches her breath."
    "She looks up at you with a sly smile, her eyes flashing with mischief."
    the_person "I'm sure I can go for another round... although I might have some difficulty walking straight in the morning! But who needs to walk when you can just carry me around and fuck me wherever you want?"
    "[the_person.title] giggles, her body language screaming 'fuck me again' as she spreads her legs wide."
    return

label vt_wild_sleepover_good_response(the_person):  #If you've made her cum
    "[the_person.title] looks up at you with a sly smile, her eyes sparkling with pleasure."
    the_person "Well, that wasn't too bad... but I think you can do better than that, don't you?"
    $ the_person.draw_person(position = "missionary")
    "[the_person.title] lies down in bed, her body trembling with aftershocks as she catches her breath."
    "She looks up at you with a flirtatious gaze, her eyes flashing with desire."
    the_person "Could you give me another pounding before we go to sleep? I'm not quite satisfied yet... and I think you owe me a few more orgasms."
    "[the_person.title] winks at you, her body language screaming 'fuck me again' as she spreads her legs wide."
    return

label vt_wild_sleepover_bored_response(the_person):  #If she hasn't cum yet
    "[the_person.title] looks up at you with a pouty expression, her eyes flashing with disappointment."
    the_person "Come on! Is this the best you can do? I expected a little more than that... I thought you were supposed to be some kind of sex god or something."
    "She rolls her eyes and sighs, her body language screaming 'try harder' as she shifts her hips."
    "You take some time to catch your breath, trying to figure out how you can do better."
    "[the_person.title] starts to get impatient, her hands drifting down to her pussy as she begins to rub herself, keeping herself ready for you."
    "She looks up at you with a sultry smile, her eyes sparkling with mischief."
    the_person "You'd better step up your game, or I'll have to take matters into my own hands... and trust me, you don't want that."
    return
# update all the following the_person and movements with wild personality. Use Rangiku Matsumoto from Bleach or Nami from One Piece, for ideas, keep to the structure. Movements in quotations:
## DIALOGUE ##

