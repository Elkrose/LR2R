### PERSONALITY CHARACTERISTICS ###
# dandere personality (A stock love interest who is quiet and asocial. They are generally afraid to speak, fearing that what they say will get them in trouble.)
# "Dandere" (JP) is a term for a character who is silent almost to the point of coming across as emotionless most of the time, but will suddenly become cute, talkative, and deredere when they are alone with their love interest. They will often keep to themselves and not go out of their way to try to talk to anyone other than their love interest revealing that they're actually just shy. They often struggle with severe social anxiety and will depend on their love interest to help them overcome it. 
# update all the following the_person and actions with dandere personality. Remember the_person is female, and mc.name is male. Use Shouko Komi from Komi Can't Communicate for ideas, keep to the structure and don't use the same dialogs:```
#add more dandere personality, use different words, and movements on a new line in quotations.



### DIALOGUE ###
label dandere_introduction(the_person):
    mc.name "Excuse me, could I bother you for a moment?"
    "She freezes, then turns around slowly to face you."
    the_person "H-hello..."
    mc.name "I know this is sudden, but I just saw you walking by and something about your presence caught my attention... It's not every day that one encounters someone as enigmatic as yourself."
    "She glances around uncomfortably, her cheeks flushing slightly."
    the_person "I-I don't know what you mean..."
    $ the_person.change_happiness(-1)
    mc.name "Oh, I apologize if my words were too forward... It's just that there's something about your quiet demeanor and shy smile that intrigues me."
    "She seems even more nervous now as she tries to find the right words."
    $ the_person.set_title()
    $ the_person.set_possessive_title()
    the_person "My name is [the_person.name]. Is that all you wanted to know?"
    $ the_person.change_happiness(-2)
    mc.name "Well, I also wanted to introduce myself... My name's [mc.name]."
    return

label dandere_greetings(the_person):
    if the_person.love < 0:
        the_person "Umm..."
        "She nervously fidgets with her hands and nods, while avoiding making eye contact."
    elif the_person.happiness < 90:
        the_person "H-hi..."
        "She sighs softly and looks down at the floor, fidgeting with her feet while twirling her hair nervously."
    else:
        if the_person.sluttiness > 60 and the_person.obedience > 180:
            the_person "H-hello [the_person.mc_title]..."
            "She is obviously nervous, but then smiles politely, straightens her posture andcomposes herself."
            the_person "How may I help you?"
            "She leans forward slightly, showing that she is interested."
        elif the_person.love >= 0 or the_person.happiness >= 90:
            if renpy.random.randint(0, 1) == 0:
                the_person "O-oh... H-hi [the_person.mc_title]..."
                "She smiles slightly, then looks away, then you see a blush form on her face while she plays with her hands."
            else:
                the_person "H-hello [the_person.mc_title]..."
                "She gets nervous, then smiles, then takes a deep breath before her eyes meets yours."
                the_person "How are you today?"
                "She leans in obviously interested in what you have to say."
        elif renpy.random.randint(0, 1) == 0 and the_person.sluttiness > 80:
            the_person "O-oh..."
            "She blushes deeply as she realizes you are there."
            the_person "H-hello [the_person.mc_title]..."
            "She gets flustered, then looks away as she fans herself while giggling nervously."
    return

label dandere_sex_responses_foreplay(the_person):
    if arousal_perc < 45:
        if sluttiness > 50:
            "[the_person.possessive_title] lets out a small squeak, her eyes widening in surprise."
            the_person "O-oh... I didn't expect it to feel so... good."
        else:
            "[the_person.possessive_title] blushes deeply and looks away, her voice barely above a whisper."
            the_person "I-I think I like this..."
    elif arousal_perc < 60:
        if sluttiness > 50:
            the_person "Mmm... your touch is so gentle... I love it."
            "She leans in closer, her eyes locked on yours."
        else:
            "[the_person.possessive_title] blushes deeply and whispers softly, her eyes darting around the room."
            the_person "I-I feel a little... embarrassed, but it feels so good..."
    elif arousal_perc < 75:
        if sluttiness > 50:
            "[the_person.possessive_title] lets out a small moan, her eyes locked on yours as she pants softly."
            the_person "You're so good at this... I feel like I'm melting in your hands."
        else:
            "[the_person.possessive_title] blushes deeply and looks away shyly, her voice barely above a whisper."
            the_person "I-I think I might be getting a little too excited... *giggles nervously*"
    elif arousal_perc < 90:
        if sluttiness > 50:
            "[the_person.possessive_title] moans seductively, her eyes locked on yours as she pants heavily."
            the_person "T-touch me all over... I want to feel your hands everywhere."
        else:
            "[the_person.possessive_title] blushes deeply and looks away shyly, her voice barely above a whisper."
            the_person "I-I think I'm going to... *gulps*... you know, if you keep touching me like that..."
    else:
        if sluttiness > 50:
            if not the_person.has_significant_other:
                "[the_person.possessive_title] moans softly, her eyes locked on yours as she pants slightly."
                the_person "O-oh no... I think I'm going to cum soon... *bites lip*"
            else:
                "[the_person.possessive_title] blushes deeply and looks away shyly."
                the_person "I-I feel so guilty, but your touch is just so... different from my [the_person.so_title]'s."
        else:
            "[the_person.possessive_title] moans softly, her eyes locked on yours as she pants slightly."
            the_person "D-don't stop... please don't stop... *whimpers*"
    return

label dandere_sex_responses_oral(the_person):
    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] lets out a small squeak, her eyes widening in surprise."
            "She covers her mouth with her hand, trying to stifle her moans."
        else:
            "[the_person.possessive_title!c] watches you with wide eyes, her face flushing with embarrassment."
            "She tries to look away, but can't help sneaking glances at you."
    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            the_person "O-oh... that feels so... good."
            "She starts to squirm and fidget, trying to get more comfortable."
        else:
            the_person "Mmm... *whispers* I think I like this..."
            "*she looks up at you with a shy expression, her eyes sparkling with excitement."
    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            the_person "A-ah... *moans* your tongue is so... skilled."
            "She starts to pant and breathe heavily, her body tensing up."
        else:
            the_person "O-oh my... *whispers* this is so embarrassing..."
            "She covers her face with her hands, trying to hide her blush."
    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "Mmm... *moans* don't stop, please..."
            "*she starts to writhe and squirm, her body trembling with pleasure."
        else:
            the_person "O-oh god... *whispers* I think I'm going to..."
            "She looks up at you with a desperate expression, her eyes pleading for more."
    elif the_person.arousal_perc < 100 and not the_person.has_significant_other:
        if the_person.sluttiness > 50:
            the_person "A-ah... *moans* I'm going to cum soon..."
            "She starts to pant and breathe heavily, her body tensing up."
        else:
            the_person "O-oh my... *whispers* I don't know if I can take much more..."
            "She looks up at you with a shy expression, her eyes sparkling with excitement."
    elif the_person.arousal_perc < 100 and the_person.has_significant_other:
        if the_person.sluttiness > 50:
            the_person "Mmm... *moans* my [the_person.so_title] never makes me feel like this..."
            "She starts to pant and breathe heavily, her body tensing up."
        else:
            the_person "O-oh god... *whispers* I feel so guilty, but this feels so good..."
            "She covers her face with her hands, trying to hide her blush."
    else:
        if the_person.sluttiness > 50:
            the_person "D-don't stop! *moans* please don't stop..."
            "She starts to writhe and squirm, her body trembling with pleasure."
        elif the_person.sluttiness < 51 and not the_person.has_significant_other:
            the_person "O-oh my... *whispers* I think I'm going to cum soon..."
            "She looks up at you with a shy expression, her eyes sparkling with excitement."
        else:
            the_person "A-ah... *moans* yes, right there..."
            "She starts to pant and breathe heavily, her body tensing up."
    return

label dandere_sex_responses_vaginal(the_person):
    if the_person.energy < 10:
        call low_energy_sex_responses_vaginal(the_person) from _call_low_energy_sex_responses_vaginal_VT10
        return
    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            $ play_moan_sound()
            "[the_person.possessive_title!c] lets out a small squeak, her eyes widening in surprise."
            the_person "O-oh... I didn't expect it to feel so... good."
        else:
            "[the_person.possessive_title!c] blushes deeply and looks away, her voice barely above a whisper."
            the_person "I-I think I like this..."
    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            the_person "Mmm... *whispers* your cock feels so... nice."
            "She starts to squirm and fidget, trying to get more comfortable."
        else:
            $ play_moan_sound
            the_person "A-ah... *whispers* I think I'm getting a little too excited..."
            "She covers her face with her hands, trying to hide her blush."
    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                the_person "O-oh no... *whispers* I think I'm going to cum soon..."
                "She starts to pant and breathe heavily, her body tensing up."
            else:
                the_person "Mmm... *whispers* my [the_person.so_title] never makes me feel like this..."
                "She starts to squirm and fidget, trying to get more comfortable."
        else:
            the_person "Don't stop fucking me! You're going to make me cum, I can feel it!"
    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "A-ah... *moans* yes, right there..."
            "She starts to pant and breathe heavily, her body tensing up."
        else:
            the_person "O-oh yes... *whispers* that feels so good..."
            "She covers her face with her hands, trying to hide her blush."
    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                the_person "O-oh no... *whispers* I'm going to cum..."
                "She starts to pant and breathe heavily, her body tensing up."
            else:
                the_person "Mmm... *whispers* my [the_person.so_title] never makes me feel like this..."
                "She starts to squirm and fidget, trying to get more comfortable."
        else:
            the_person "D-don't stop... *whispers* please don't stop..."
            "She starts to writhe and squirm, her body trembling with pleasure."
    return

label dandere_sex_responses_anal(the_person):
    if the_person.energy < 10:
        call low_energy_sex_responses_anal(the_person) from _call_low_energy_sex_responses_anal_VT10
        return

    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            $ the_person.call_dialogue("surprised_exclaim")
            the_person "E-eh... *whispers* I'm not sure if I can handle this..."
            "She looks away, her face flushing with embarrassment, and fidgets with her hands."
        else:
            $ the_person.call_dialogue("surprised_exclaim")
            the_person "H-haa... *whispers* I think I need to calm down..."
            "She takes a few deep breaths, her eyes closed, and tries to compose herself."

    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            $ the_person.call_dialogue("surprised_exclaim")
            the_person "Mmm... *whispers* this is kind of... nice..."
            "She starts to squirm and fidget, trying to get more comfortable, and looks up at you with a shy expression.."
        else:
            the_person "O-oh... *whispers* I didn't expect it to feel so... weird..."

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            the_person "A-ah... *moans* yes, right there... *whispers* please don't stop..."
            "She starts to pant and breathe heavily, her body tensing up, and reaches out to grab your arm."
        else:
            the_person "O-oh no... *whispers* I think I might be getting a little too excited... *gulps*"

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            if mc.condom:
                the_person "Mmm... *whispers* give it to me, please... *whispers* I want it..."
            else:
                the_person "A-ah... *moans* yes, please... no condom... *whispers* I don't care..."
        else:
            the_person "O-oh... *whispers* why does it have to feel so... good? *looks away, embarrassed*"
    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                the_person "O-oh no... *whispers* I think I'm going to cum soon..."
                "She starts to pant and breathe heavily, her body tensing up."
            else:
                the_person "Mmm... *whispers* my [the_person.so_title] never makes me feel like this..."
                "She starts to squirm and fidget, trying to get more comfortable."
                the_person "I-I might have a [the_person.so_title], but... *whispers* you're so much better..."
        else:
            $ the_person.call_dialogue("surprised_exclaim")
            the_person "I-I think I'm going to... *whispers* cum soon..."
            "She covers her face with her hands, trying to hide her blush."
    return

label dandere_climax_responses_foreplay(the_person):
    if the_person.sluttiness > 50:
        $ the_person.call_dialogue("surprised_exclaim")
        the_person "E-eh... I think I'm going to lose control..."
        "She looks up at you with a flustered expression, her eyes wide with anticipation, and fidgets with her hands."
        the_person "Mmm... please don't stop... I'm so close..."
        "She starts to squirm and fidget, trying to get more comfortable, and her face flushes with embarrassment."
    else:
        the_person "I-I think I'm going to... do something embarrassing... oh no..."
        $ the_person.call_dialogue("surprised_exclaim")
        "She covers her face with her hands, trying to hide her blush, and looks away, mortified."
        "She goes silent, then lets out a shuddering moan, her body trembling with pleasure, and her legs start to shake uncontrollably."
        "She starts to whisper to herself, trying to calm down, but her voice is shaking with excitement."
    return

label dandere_climax_responses_oral(the_person):
    if the_person.sluttiness > 70:
        $ the_person.call_dialogue("surprised_exclaim")
        the_person "E-eh, what's happening? I feel like I'm going to..."
        "She looks up at you with a bewildered expression, her eyes wide with surprise, and her face flushes with embarrassment."
        the_person "Mmm... please, don't stop... I think I'm going to lose control..."
        "She starts to squirm and fidget, trying to get more comfortable, and her hands start to shake uncontrollably."
    else:
        the_person "O-oh no, this is too much... I think I'm going to pass out..."
        $ the_person.call_dialogue("surprised_exclaim")
        "She covers her face with her hands, trying to hide her blush, and looks away, mortified, her body trembling with pleasure."
        "She goes silent, then lets out a shuddering moan, her legs start to shake uncontrollably, and she starts to whisper to herself, trying to calm down."
    return
#
label dandere_climax_responses_vaginal(the_person):
    if the_person.sluttiness > 70:
        $ the_person.call_dialogue("surprised_exclaim")
        if the_person.arousal_perc > 120:
            the_person "Mmm... no, stop... I think I'm going to... *gulps*"
            "She looks up at you with a bewildered expression, her eyes wide with surprise, and her face flushes with embarrassment."
            "She starts to tremble and shake, her body losing control, and her hands start to flail wildly."
        else:
            the_person "A-ah, more... please... I think I'm going to... *whispers* cum..."
            "She starts to squirm and fidget, trying to get more comfortable, and her face flushes with embarrassment."
            "She bites her lip, trying to hold back her moans, and her eyes start to glaze over with pleasure."
    else:
        the_person "O-oh no, this is too much... I think I'm going to... *gulps*"
        "She covers her face with her hands, trying to hide her blush, and looks away, mortified."
        "She lets out a shuddering moan, her body trembling with pleasure, and her legs start to shake uncontrollably."
        "She starts to whisper to herself, trying to calm down, but her voice is shaking with excitement."
    return

label dandere_climax_responses_anal(the_person):
    if the_person.sluttiness > 70:
        $ the_person.call_dialogue("surprised_exclaim")
        if the_person.arousal_perc > 120:
            the_person "E-eh, no, wait... I think I'm going to lose control... *gulps*"
            "She looks up at you with a flustered expression, her eyes wide with anticipation."
            "She starts to tremble and shake, her body losing control, and her hands start to flail wildly."
        else:
            the_person "Mmm... it feels so... strange... *whispers* but good..."
            "She starts to squirm and fidget, trying to get more comfortable, and her face flushes with embarrassment."
            "She bites her lip, trying to hold back her moans, and her eyes start to glaze over with pleasure."
        the_person "A-ah... *moans*... mmm..."
    else:
        the_person "O-oh no, this is too much... I think I'm going to... *gulps*"
        $ the_person.call_dialogue("surprised_exclaim")
        the_person "A-ah... *moans*... cum..."
        "She covers her face with her hands, trying to hide her blush, and looks away, mortified."
    return

label dandere_clothing_accept(the_person):
    if the_person.obedience > 180:
        $ the_person.call_dialogue("surprised_exclaim")
        the_person "R-really? You think I'd look good in this...?"
        "She looks down, fidgeting with her hands, and her face flushes with embarrassment."
    elif the_person.sluttiness <= 70 or the_person.arousal_perc < 120:
        $ the_person.call_dialogue("surprised_exclaim")
        the_person "O-oh, th-thank you... I think it's nice too..."
        "She smiles slightly, looking away, and her eyes sparkle with shy excitement."
    else:
        the_person "E-eh... um, t-thanks... *gulps*"
        "She looks away, her face flushing with embarrassment, and her hands start to tremble slightly."
    return

label dandere_clothing_reject(the_person):
    if the_person.should_wear_uniform:
        the_person "O-oh, r-right... I should probably wear my uniform... *gets flustered*"
        "She looks around, trying to compose herself, and her face flushes with embarrassment."
    elif the_person.obedience > 180:
        the_person "I-I'm sorry... but I don't think this is suitable for me... *looks down*"
        "She fidgets with her hands, trying to hide her nervousness, and her voice barely above a whisper."
    else:
        if the_person.sluttiness > 60:
            the_person "E-eh... I don't know if I can wear this... it's a bit too... *gulps* revealing..."
            "She looks away, her face flushing with embarrassment, and her hands start to tremble slightly."
        else:
            the_person "I-I don't think this is really my style... *gets nervous* maybe something else would be better...?"
            "She looks down, fidgeting with her hands, and her voice barely above a whisper."
    return

label dandere_clothing_review(the_person):
    if the_person.outfit.cum_covered:
        if (the_person.sluttiness > 40 and the_person.opinion.being_covered_in_cum >=0) or the_person.opinion.being_covered_in_cum > 0:
            $ the_person.call_dialogue("surprised_exclaim")
            "[the_person.title] looks down at herself, her face flushing with embarrassment, and starts to nervously wipe up the biggest splashes of cum on her."
            "She mutters to herself, trying to hide her embarrassment, and her hands start to tremble slightly."
        else:
            the_person "O-oh no... I'm such a mess... *gulps*"
            "She looks around, trying to find a way to clean up, and her face flushes with embarrassment."
        "[the_person.title] wipes herself down, cleaning up all the cum she can find, while trying to avoid eye contact."

    if the_person.obedience > 180:
        the_person "I-I'm so sorry... I'm a bit of a mess... *looks down*"
        "She starts to nervously fidget with her hands, trying to hide her embarrassment, and her voice barely above a whisper."
    else:
        if the_person.sluttiness > 40:
            the_person "E-eh... I don't think I can go out like this... *gulps*"
            "She looks around, trying to find a way to clean up, and her face flushes with embarrassment."
        else:
            the_person "O-oh dear... I think I need to fix myself up a bit... *gets nervous*"
            "She starts to nervously fidget with her hands, trying to hide her embarrassment, and her voice barely above a whisper."
    $ the_person.apply_planned_outfit(show_dress_sequence = True)
    return

label dandere_strip_reject(the_person, the_clothing, strip_type = "Full"):
    if the_person.obedience > 180:
        the_person "I-I'd rather not take off my [the_clothing.display_name] right now, if that's okay..."
        "She looks down, fidgeting with her hands, and her voice barely above a whisper."
    elif the_person.obedience < 70:
        the_person "N-no, I don't think so... *gets defensive*"
        "She crosses her arms, trying to hide her nervousness, and her face flushes with embarrassment."
    else:
        the_person "E-eh, not yet... *gulps* maybe later, okay?"
        "She looks away, trying to avoid eye contact, and her hands start to tremble slightly."
    return

label dandere_strip_obedience_accept(the_person, the_clothing, strip_type = "Full"):
    "[the_person.title] looks down, her face flushing with embarrassment, and her hands start to fidget nervously as you begin to remove her [the_clothing.display_name]."
    if the_person.obedience > 180:
        the_person "I-I don't know if I can do this... *whispers* I'm really scared..."
        "She looks up at you with a pleading expression, her eyes wide with anxiety."
    else:
        the_person "E-eh, p-please be gentle... *gulps* I don't want to... *whispers* mess up..."
        "She looks away, trying to avoid eye contact, and her body starts to tremble slightly."
    return

label dandere_grope_body_reject(the_person):
    if the_person.effective_sluttiness("touching_body") < 5: #Fail point for touching shoulder
        the_person "E-eh!"
        "[the_person.title] jumps back, her eyes wide with surprise, and her face flushes with embarrassment."
        mc.name "S-sorry... I didn't mean to scare you."
        the_person "I-it's okay... *whispers* I just wasn't expecting it..."
        "She looks down, fidgeting with her hands, and her voice barely above a whisper."
        the_person "P-please be more careful next time... *gulps* my body is really sensitive..."
        mc.name "I understand. I won't touch you without your permission again."
        the_person "... T-thank you... *sighs in relief*"
    else: #Fail point for touching waist
        the_person "Um, c-could you... *gets nervous*"
        "[the_person.title] hesitates, looking around nervously, before speaking up in a barely audible whisper."
        mc.name "O-oh, sorry... I didn't mean to make you uncomfortable."
        the_person "I-it's just... *gulps* I'm not used to being touched like that... *looks away*"
        mc.name "I apologize for crossing the line. We can go back to what we were doing before if you want."
        "[the_person.title] nods shyly, her face still flushed with embarrassment, and her eyes avoid yours."
        the_person "T-thank you... *whispers* let's just forget this happened, okay? *looks down*"
    return

label dandere_sex_accept(the_person, the_position):
    if the_person.sluttiness > 70:
        if the_person.obedience < 70:
            the_person "I-I think I'm ready... *gulps*"
            "She looks up at you with a nervous expression, her eyes wide with anticipation."
        else:
            if the_position.skill_tag == "Foreplay":
                the_person "E-eh, okay... *whispers* but please be gentle..."
                "She looks down, fidgeting with her hands, and her face flushes with embarrassment."
            elif the_position.skill_tag == "Oral":
                if "getting head" in the_position.opinion_tags:
                    the_person "I-I suppose it's okay... *gets nervous*"
                    "She looks away, trying to hide her embarrassment, and her voice barely above a whisper."
                else:
                    the_person "Um, a-are you sure? *gulps* I don't know if I can do that..."
                    "She looks up at you with a pleading expression, her eyes wide with anxiety."
            else:
                the_person "O-oh no, I don't know... *whispers* it might be too much for me..."
                "She looks down, fidgeting with her hands, and her face flushes with embarrassment."
    else:
        the_person "L-let's do it, [the_person.mc_title]... *gulps*"
        "She looks up at you with a nervous expression, her eyes wide with anticipation, and her voice barely above a whisper."
    return

label dandere_sex_obedience_accept(the_person):
    if the_person.sluttiness > 70:
        the_person "I-I don't know what's wrong with me... *whispers* but I want you to... take control..."
        "She looks up at you with a nervous expression, her eyes wide with anticipation, and her face flushes with embarrassment."
        the_person "P-please, [the_person.mc_title]... *gulps* use me as you like..."
    else:
        if the_person.obedience > 180:
            the_person "I-I'm not sure this is a good idea... *whispers* but if you really want to..."
            "She looks down, fidgeting with her hands, and her voice barely above a whisper."
            the_person "P-please be gentle... *gulps* I don't know if I can handle it..."
        else:
            the_person "E-eh, this feels kind of... wrong... *whispers* but since we're both here..."
            "She looks up at you with a nervous expression, her eyes wide with anticipation, and her face flushes with embarrassment."
            the_person "L-let's just... see where this goes... *gulps* but please don't push me too far..."
    return

label dandere_sex_gentle_reject(the_person):
    if the_person.sluttiness > 50:
        the_person "N-not yet, [the_person.mc_title]... *whispers* I need a little more time..."
        "She looks up at you with a nervous expression, her eyes wide with anticipation, and her face flushes with embarrassment."
    else:
        the_person "W-wait, [the_person.mc_title]... *gulps* I don't think I'm ready for this..."
        "She looks down, fidgeting with her hands, and her voice barely above a whisper."
        the_person "I-I want to... you know, fool around... *whispers* but let's keep it casual, okay?"
        "She hesitates, blushing deeply as she tries to find the words, and her eyes avoid yours."
        the_person "I-I'm not quite... ready... *whispers* please, let's just take it slow..."
    return

label dandere_sex_angry_reject(the_person):
    if the_person.has_significant_other:
        the_person "W-what? No, no, no... *gets flustered* I have a [the_person.so_title], so... *gulps* just forget it, okay?"
        "She looks down, her face flushing with embarrassment, and quickly turns away, trying to hide her discomfort."
        "She walks off with her head down, her shoulders shaking slightly as she tries to compose herself."
    elif the_person.sluttiness < 20:
        the_person "E-eh? N-no way... *stammers* get away from me!"
        "She takes a step back, her eyes wide with fear, and her face flushes with embarrassment."
        "[the_person.title] looks around nervously, trying to find an escape route, and her hands start to tremble."
    else:
        the_person "W-what? That's... *gulps* no, no, no... *looks away*"
        "She recoils in horror, her hands covering her mouth, and her eyes wide with shock."
        "[the_person.title] takes a step back, trying to distance herself, and her voice barely above a whisper."
        the_person "I-I don't want to... *whispers* please just leave me alone..."
    return

label dandere_seduction_response(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 50:
            the_person "E-eh, I think I know what you need... *whispers* let me take care of you..."
            "[the_person.title] takes your hand with a shy smile and looks down, her face flushing with embarrassment, as she leads you off to find some place out of the way."
        else:
            the_person "R-right now? O-okay... *gulps* lead the way, I guess..."
            "She looks down, fidgeting with her hands, and her voice barely above a whisper."
    else:
        if the_person.sluttiness > 50:
            the_person "M-maybe we can... *whispers* find someplace quiet?"
            "[the_person.title] takes your hand and looks up at you with a nervous expression, her eyes wide with anticipation."
        elif the_person.sluttiness > 10:
            the_person "I-I think I know what you're looking for... *gulps*"
            "[the_person.title] hesitates for a moment, looking around nervously, before suggesting going somewhere more private together."
        else:
            the_person "O-oh, um... *whispers* maybe later?"
            "[the_person.title] looks down, her face flushing with embarrassment, and her voice barely above a whisper."
            "She seems hesitant and unsure, but willing to explore further under your guidance."
    return

label dandere_seduction_accept_crowded(the_person):
    if not the_person.has_significant_other:
        if the_person.sluttiness < 20:
            the_person "E-eh, let's go somewhere quieter... *whispers* I don't like it when it's too crowded..."
            "She looks around nervously, fidgeting with her hands, and her voice barely above a whisper."
        elif the_person.sluttiness < 50:
            the_person "I-I know a place nearby that's less crowded... *gulps* we can talk there..."
            "She looks up at you with a nervous expression, her eyes wide with anticipation."
        else:
            the_person "O-oh my... *whispers* this is really happening, isn't it? *gulps*"
            "She looks down, her face flushing with embarrassment, and her voice barely above a whisper."
            the_person "I-I hope you don't mind that I'm not very... *whispers* experienced..."
    else:
        if the_person.sluttiness + (5*the_person.opinion.cheating_on_men) > 50:
            the_person "E-eh, let's just... *whispers* do it..."
            "She looks up at you with a nervous expression, her eyes wide with anticipation, and her face flushing with embarrassment."
            the_person "I-I don't care about my [the_person.so_title] right now... *gulps*"
        else:
            the_person "O-oh no, this is so wrong... *whispers* but I want to do it anyway..."
            "She looks down, her face flushing with embarrassment, and her voice barely above a whisper."
            the_person "L-let's just go somewhere quiet... *gulps* so my [the_person.so_title] doesn't find out..."
    return

label dandere_seduction_accept_alone(the_person):
    if not the_person.has_significant_other:
        if the_person.sluttiness < 20:
            the_person "E-eh, I think... *whispers* you seem nice..."
            "She looks down, fidgeting with her hands, and her voice barely above a whisper."
            the_person "I-if you want to... *gulps* try to impress me, I won't stop you..."
        elif the_person.sluttiness < 50:
            the_person "M-maybe we can... *whispers* see where this goes?"
            "She looks up at you with a nervous expression, her eyes wide with anticipation."
            the_person "P-please be gentle with me, though... *gulps* I'm really shy..."
        else:
            the_person "O-oh my... *whispers* I think I'm really turned on right now..."
            "She looks down, her face flushing with embarrassment, and her voice barely above a whisper."
            the_person "M-maybe we should... *gulps* take things slow, though?"
    else:
        if the_person.sluttiness + (5*the_person.opinion.cheating_on_men) > 50:
            the_person "E-eh, I don't know what's wrong with me... *whispers* but I really want to do this..."
            "She looks up at you with a nervous expression, her eyes wide with anticipation, and her face flushing with embarrassment."
            the_person "I-I know I have a [the_person.so_title], but... *gulps* I just can't help myself..."
        else:
            the_person "O-oh no, this is so wrong... *whispers* but I just can't resist you..."
            "She looks down, her face flushing with embarrassment, and her voice barely above a whisper."
            the_person "P-please understand, though... *gulps* my heart belongs to someone else..."
    return

label dandere_seduction_refuse(the_person):
    if the_person.sluttiness < 20:
        the_person "E-eh, no... *whispers* I don't think so..."
        "She looks down, fidgeting with her hands, and her face flushes with embarrassment."
        "[the_person.title] takes a step back, trying to create some distance between you."
    elif the_person.sluttiness < 50:
        the_person "I-I'm s-sorry... *whispers* but I'm not really feeling it..."
        "She bites her lip nervously and avoids eye contact, her face still flushed with embarrassment."
        "[the_person.title] hesitates for a moment before speaking up again."
        the_person "M-maybe another time... *gulps* when I'm feeling more... confident?"
    else:
        the_person "O-oh, um... *whispers* I don't know if I'm ready for that..."
        "She smiles hesitantly and shrugs, trying to hide her nervousness."
        "[the_person.title] looks away, her face still flushed with embarrassment, and her voice barely above a whisper."
        the_person "M-maybe someday... *gulps* when I feel more... comfortable with myself?"
    return

label dandere_compliment_response(the_person):
    mc.name "Hey [the_person.fname]. You seem to be having a good day today, aren't you?"
    if the_person.is_at_work:
        if (the_person.is_employee or the_person.is_strip_club_employee) and the_person.is_wearing_uniform:
            call dandere_flirt_response_employee_uniform_low(the_person) from _call_dandere_flirt_response_employee_uniform_low_compliment_response
        else:
            the_person "E-eh, stop it... *whispers* you're making me blush..."
            "She looks down, fidgeting with her hands, and her face flushes with embarrassment."
    else:
        the_person "O-oh, um... *whispers* I don't know... *gulps*"
        "She looks away, trying to hide her nervousness, and her voice barely above a whisper."
        "You chat with [the_person.possessive_title] and try to give her compliments when it feels natural. She seems really shy about receiving them, but you can tell she's secretly happy."
        the_person "T-thank you... *whispers* for saying that..."
        "She smiles slightly, still looking away, and her face still flushed with embarrassment."
    return

label dandere_compliment_response_girlfriend(the_person):
    mc.name "Hey [the_person.title]. You're looking very sexy this [StringInfo.time_of_day_string]..."
    if the_person.is_at_work:
        if (the_person.is_employee or the_person.is_strip_club_employee) and the_person.is_wearing_uniform:
            call dandere_flirt_response_employee_uniform_mid(the_person) from _call_dandere_flirt_response_employee_uniform_mid_compliment_response_girlfriend
            $ the_person.call_dialogue("flirt_response_employee_uniform_mid")
        elif the_person.sluttiness > 50:
            the_person "E-eh, th-thank you... *whispers* you're making me blush..."
            "She looks down, fidgeting with her hands, and her face flushes with embarrassment."
        else:
            the_person "O-oh, r-really? *gulps* thank you for noticing..."
            "She smiles slightly, looking away, and her face still flushed with embarrassment."
    else:
        "You chat with [the_person.possessive_title] for a while, making subtle sexual references and compliments when possible. She seems to appreciate your sly attempts at flirtation, but gets flustered and looks away whenever you catch her eye."
        the_person "T-thank you... *whispers* for making me feel special..."
        "She looks up at you with a shy expression, her eyes sparkling with happiness, and her face still flushed with embarrassment."
    return

label dandere_compliment_response_affair(the_person):
    mc.name "Hey [the_person.title]. You're looking absolutely stunning this evening, aren't you?"
    if the_person.is_at_work:
        if (the_person.is_employee or the_person.is_strip_club_employee) and the_person.is_wearing_uniform:
            call dandere_flirt_response_employee_uniform_mid(the_person) from _call_dandere_flirt_response_employee_uniform_mid_compliment_response_affair
        elif the_person.sluttiness > 50:
            the_person "E-eh, th-thank you... *whispers* I'm glad you like it..."
            "She looks down, fidgeting with her hands, and her face flushes with embarrassment."
            the_person "M-maybe we could... *gulps* talk more about it later?"
        else:
            the_person "O-oh, um... *whispers* thank you for noticing..."
            "She looks away, trying to hide her nervousness, and her voice barely above a whisper."
            the_person "I-if you like my outfit... *gulps* maybe we could find a quiet spot later?"
    else:
        the_person "R-really? *whispers* you think I'm stunning?"
        "She looks up at you with a shy expression, her eyes sparkling with happiness, and her face still flushed with embarrassment."
        the_person "I-if we were somewhere more... *gulps* intimate... I could show you more..."
        "As you continue complimenting [the_person.possessive_title], she seems to grow increasingly flustered and intrigued by your attention, but tries to hide it behind a mask of shyness."
    return

label dandere_flirt_response(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 50:
            the_person "E-eh, if you want... *whispers* I'll do my best..."
            "She looks down, fidgeting with her hands, and her face flushes with embarrassment."
        else:
            the_person "T-thank you, [the_person.mc_title]... *whispers* that's very kind of you..."
            "She smiles slightly, looking away, and her face still flushed with embarrassment."
    elif the_person.has_significant_other:
        if the_person.sluttiness + (the_person.opinion.cheating_on_men*5) > 50:
            the_person "O-oh, um... *whispers* this is really flattering..."
            "She looks up at you with a shy expression, her eyes sparkling with excitement, and her face still flushed with embarrassment."
            mc.name "I understand, but maybe we could just have some fun together?"
            the_person "I-I don't know... *gulps* but maybe it wouldn't hurt to... *whispers* enjoy each other's company a little bit..."
        else:
            the_person "P-please remember... *whispers* I'm taken..."
            "She looks down, fidgeting with her hands, and her face flushes with embarrassment."
            the_person "I appreciate your compliments, but... *whispers* we should respect my relationship..."
    else:
        if the_person.sluttiness > 50:
            the_person "E-eh, I'm flattered... *whispers* but please be gentle..."
            "She smiles slightly, looking away, and her face still flushed with embarrassment."
            "[the_person.title] glances up at you, her eyes sparkling with excitement, before quickly looking away again."
        else:
            the_person "T-thank you, [the_person.mc_title]... *whispers* but let's just... *gulps* keep things friendly, okay?"
            "She looks down, fidgeting with her hands, and her face flushes with embarrassment."
    return

label dandere_flirt_response_employee_uniform_low(the_person):
    if the_person.is_wearing_forced_uniform:
        the_person "E-eh, I guess you like it... *whispers* it's a bit embarrassing, though..."
        mc.name "It looks... interesting on you."
        $ mc.change_locked_clarity(5)
        the_person "T-thank you, I guess... *whispers* I just wish it wasn't so... revealing..."
    elif the_person.judge_outfit(the_person.outfit):
        #She's in uniform and likes how it looks.
        the_person "O-oh, th-thank you... *whispers* I think it's kind of cute too..."
        $ mc.change_locked_clarity(5)
        the_person "I-it's nice to work somewhere where we can... *gulps* show off a little bit of our personalities..."
    else:
        #She's in uniform, but she thinks it's a little too slutty.
        if the_person.vagina_visible:
            # Her pussy is on display.
            the_person "I-I'm s-so sorry... *whispers* I didn't mean to show so much..."
            mc.name "Well, it does show off your assets quite nicely."
            $ mc.change_locked_clarity(5)
            the_person "Y-yes, I suppose so... *whispers* but I wish there was a bit more coverage..."
        elif the_person.tits_visible:
            # Her tits are out
            the_person "T-thank you... *whispers* I just wish it wasn't so... revealing..."
            mc.name "You look incredible and you're comfortable. That's what matters."
            $ mc.change_locked_clarity(5)
            the_person "I-I guess... *whispers* I just wish there was a way to wear it that felt more... modest..."
        elif the_person.underwear_visible:
            # Her underwear is visible.
            the_person "T-thank you... *whispers* I just wish it wasn't so... visible..."
            mc.name "You look fantastic in it."
            $ mc.change_locked_clarity(5)
            the_person "W-well... *whispers* thank you, I guess... I just wish there was a way to wear it that felt more... professional..."
        else:
            # It's just generally slutty.
            the_person "T-thank you... *whispers* I think it's a bit too... bold, though..."
            mc.name "You look amazing in it!"
            $ mc.change_locked_clarity(5)
            the_person "W-well... *whispers* thank you, I guess... I just wish there was a way to wear it that felt more... confident, but still respectable..."
    return

label dandere_flirt_response_employee_uniform_mid(the_person):
    if the_person.is_wearing_forced_uniform:
        $ mc.change_locked_clarity(10)
        if the_person.vagina_visible:
            the_person "E-eh, l-look at me... *whispers* I feel so exposed..."
        elif the_person.tits_visible:
            the_person "O-oh, um... *whispers* I don't know if I'm comfortable with this..."
        else:
            the_person "I-I mean, it's just an outfit... *whispers* but maybe I do feel a little bit sexy in it..."
        mc.name "Rules are rules and I can't make any exceptions, even if they look good."
        "She looks down, her face flushing with embarrassment, and her voice barely above a whisper."
        the_person "Y-yes... I know... *whispers* at least you seem to be enjoying it..."
    elif the_person.judge_outfit(the_person.outfit):
        $ mc.change_locked_clarity(10)
        if the_person.tits_visible:
            the_person "A-are you sure... *whispers* my top is okay?"
            "She looks away, trying to hide her blush, and her voice barely above a whisper."
            mc.name "All of you looks good, don't worry about it."
            the_person "T-thank you... *whispers* I think..."
        else:
            the_person "O-oh, th-thank you... *whispers* I think this uniform is kind of cute too..."
        the_person "M-maybe we could... *gulps* go shopping sometime and find something even better for me to wear?"
        mc.name "That sounds like fun!"
    else:
        # the_person "I think it shows off a little too much!"
        the_person "E-eh, I-I mean... *whispers* this uniform is a bit too revealing for me..."
        $ mc.change_locked_clarity(10)
        if the_person.vagina_visible:
            the_person "L-look at me... *whispers* I feel so exposed..."
        elif the_person.tits_visible:
            the_person "I-it's just an outfit... *whispers* but maybe it makes me feel a little bit sexy?"
        else:
            the_person "I-it's just an outfit... *whispers* but sometimes I do think about how good I look in it..."
        mc.name "I understand your concerns, but it's important for business."
        "She looks down, her face still flushed with embarrassment, and her voice barely above a whisper."
        the_person "Y-yes... *whispers* at least you seem to be enjoying yourself..."
    return

label dandere_flirt_response_low(the_person):
    "[the_person.title] whispers softly, her eyes cast downward in shyness as she responds to your compliment: "
    the_person "T-thank you... *whispers* I-I think so too..."
    "[the_person.title] hesitates for a moment, fidgeting with her hands, before slowly starting to spin around, revealing her outfit in a timid manner. Her movements are awkward and self-conscious, avoiding your gaze as she rotates."
    "As the spin comes to an end, she stands still once more, her face flushing deeply with embarrassment as she awaits your reaction."
    $ the_person.draw_person(position = "walking_away")
    $ mc.change_locked_clarity(5)
    "You can't help but notice how adorably flustered she is in this moment – her shyness and awkwardness making for a charming display."
    "Your heart skips a beat at the thought of engaging further with her, but you remain patient and supportive; offering a warm smile that encourages her to continue exploring these newfound flirtatious sides of herself if she so desires."
    $ the_person.draw_person()
    the_person "E-eh, um... *whispers* do you really think I look okay?"
    "She looks up at you with a pleading expression, her eyes wide with uncertainty, and her voice barely above a whisper."
    return

label dandere_flirt_response_low1(the_person):
    if the_person.has_significant_other:
        the_person "E-eh, I shouldn't be... *whispers* doing this, [the_person.mc_title]..."
        "She looks down, fidgeting with her hands, and her face flushes with embarrassment."
        the_person "M-maybe we could just... *whispers* talk? As friends?"
        mc.name "Friends sound nice." 
    else:
        the_person "O-oh, th-thank you... *whispers* maybe if you're lucky, you'll get to see more of me..."
        "She looks away, trying to hide her blush, and her voice barely above a whisper."
        the_person "I-I have high standards, though... *whispers* you'll have to really impress me..."
        the_person "I-I'm s-so sorry... *whispers* I didn't mean to come on so strong, [the_person.mc_title]..."
        "She looks down, her face flushing deeply with embarrassment, and her voice barely above a whisper."
        the_person "I-I get nervous sometimes... *whispers* and you're just really... *gulps* cute..."
        mc.name "Thanks! It's okay, we all have our moments." 
        "[the_person.title] blushes even deeper and looks away, trying to hide her face."
    $ mc.change_locked_clarity(5)
    return

label dandere_flirt_response_mid(the_person):
    if mc.location.person_count > 1 and the_person.effective_sluttiness("kissing") < (25 - (5*the_person.opinion.public_sex)):
        $ mc.change_locked_clarity(10)
        if the_person.tits_visible:
            the_person "E-eh... *whispers* do you really think so?"
            "She looks down, her face flushing deeply with embarrassment, and her voice barely above a whisper."
            the_person "Y-you like my... *gulps* top?"
            "Her eyes dart around nervously, as if afraid of what your answer might be."
        else:
            the_person "A-are you... *whispers* serious?"
            "She trails off, her eyes looking down, and her hands trembling slightly."
            the_person "Y-you think this outfit... *gulps* looks good on me?"
            "Her voice is barely audible, and her face is still flushed with embarrassment."
        the_person "I-I thought so too... *whispers* when I picked it out this morning..."
        mc.name "It's really sexy."
        the_person "T-thank you... *whispers* I'm glad you like it..."
    else:
        the_person "O-oh, th-thank you... *whispers* I think it's kind of cute too..."
        the_person "Y-you want to see more of me? *gulps*"
        $ the_person.draw_person(position = "back_peek")
        mc.name "I... yeah..."
        "[the_person.possessive_title!c] turns around slowly, her cheeks flushing a deep red as she reveals her bare ass to you."
        $ the_person.draw_person()
        the_person "H-here's something for now... *whispers* maybe we can go out and I'll show off more later?"
        "She looks down, her face still flushed with embarrassment, and her voice barely above a whisper."
        $ mc.change_locked_clarity(10)
    return

label dandere_flirt_response_mid1(the_person):
    $ mc.change_locked_clarity(10)
    the_person "E-eh, th-thank you... *whispers* I think I look okay in this outfit..."
    if (the_person.has_skirt or the_person.has_dress) and not the_person.has_thigh_high_socks:
        mc.name "You could change it up with some high stockings, I would like to see that."
        the_person "O-oh, um... *whispers* I don't know if I'm brave enough for that..."

    mc.name "How about we grab a coffee together sometime?"
    if the_person.has_significant_other:
        the_person "I-I don't know... *whispers* my [the_person.so_title] might not like it..."
        "She looks down, her face flushing with embarrassment, and her voice barely above a whisper."
    else:
        the_person "E-eh, s-sure... *whispers* why not?"
        "She smiles slightly, looking away, and her face still flushed with embarrassment."
    mc.name "I do, very much so."
    the_person "A-alright then... *whispers* let's plan it for sometime soon..."
    "She looks down, fidgeting with her hands, and her voice barely above a whisper."
    the_person "J-just give me a heads up when you're free... *whispers* and we can arrange something..."
    return

label dandere_flirt_response_high(the_person):
    if mc.location.person_count > 1 and the_person.effective_sluttiness() < (25 - (5*the_person.opinion.public_sex)): # There are other people here, if she's not slutty she asks if you want to find somewhere quiet
        the_person "E-eh, you're making me blush... *whispers* let's find somewhere more private..."
        "She glances around nervously, her face flushing with embarrassment."
        menu:
            "Find somewhere more quiet\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                mc.name "Then let's find somewhere that isn't here."
                the_person "O-oh, um... *whispers* okay..."
                call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_dandere_flirt_response_high_VT2
                the_person "S-so... *whispers* now what's your plan?"

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
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _call_dandere_fuck_person_VT49
                else:
                    if the_person.has_taboo("touching_body"):
                        $ the_person.call_dialogue("touching_body_taboo_break")
                        $ the_person.break_taboo("touching_body")
                        "You take her hand and pull her close against you. She looks into your eyes."
                    else:
                        "You answer by pulling her close against you."
                    call fuck_person(the_person, private = True, start_position = standing_grope, skip_intro = True) from _call_fuck_person_dandere_flirt_grope

                $ the_person.call_dialogue("sex_review", the_report = _return)
                call mc_restore_original_location(the_person) from _call_mc_restore_original_location_dandere_flirt_response_high_VT2

            "Just flirt":
                mc.name "Not here, huh? How about back at your place then?"
                the_person "O-oh, um... *whispers* maybe..."

    else:
        if mc.location.person_count == 1: #You're alone, so she just didn't meet the sluttiness threshold
            "[the_person.possessive_title!c] bites her lower lip and glances around, confirming you're alone."
            the_person "W-well... *whispers* it's just the two of us here..."
            "She looks up at you with a shy expression, her eyes sparkling with excitement."
        else:  # You aren't alone but she's still into it.
            the_person "E-eh, you're really bold today... *whispers* I like it..."
            if the_person.has_large_tits: #Bounces her tits for you
                $ mc.change_locked_clarity(15)
                "[the_person.title] nervously runs her hands over her breasts, trying to hide her blush."
                the_person "M-maybe... *whispers* I can show you more later..."
            else: #No big tits, so she can't bounce them (as much)
                "[the_person.title] fidgets with her hands, trying to hide her nervousness."
                the_person "I-I don't know... *whispers* but I think I might like it..."

        menu:
            "Touch her" if not the_person.is_willing(kissing):
                "You step closer to [the_person.title] and move your hands down her waist."
                if the_person.has_taboo("touching_body"):
                    $ the_person.call_dialogue("touching_body_taboo_break")
                    $ the_person.break_taboo("touching_body")

                call fuck_person(the_person, start_position = standing_grope, private = False) from _call_fuck_person_flirt_response_dandere_touching

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

                call mc_move_to_private_location(the_person) from  _call_mc_move_to_private_location_dandere_flirt_response_high
                call fuck_person(the_person, start_position = kissing, private = _return, skip_intro = True) from _call_dandere_fuck_person_VT50
                $ the_person.call_dialogue("sex_review", the_report = _return)
                call mc_restore_original_location(the_person) from _call_mc_restore_original_location_dandere_flirt_response_high

            "Just flirt":
                $ the_person.draw_person()
                mc.name "Very tempting, but you're going to have to contain yourself for now."
                "[the_person.title] looks down, her face flushing with embarrassment."
                the_person "O-oh, um... *whispers* okay..."
    return

label dandere_flirt_response_low_energy(the_person):
    if the_person.sluttiness > 40:
        the_person "E-eh, th-thank you... *whispers* I'm feeling a bit... overwhelmed right now..."
        "She looks down, her face flushing with embarrassment, and her voice barely above a whisper."
    else:
        the_person "T-thank you... *whispers* but I'm really tired and shy right now... *gulps*"
        "She looks away, trying to hide her nervousness, and her voice barely above a whisper."
        the_person "M-maybe we could... *whispers* talk another time?"
        "She smiles slightly, still looking away, and her face still flushed with embarrassment."
    return

label dandere_flirt_response_girlfriend(the_person):
    # Lead in: mc.name "You're so beautiful [the_person.title], I'm so lucky to have a woman like you in my life."
    if mc.location.person_count > 1:
        # There are other people around, so she'll only start making out with you if she's slutty.
        if the_person.effective_sluttiness("kissing") < (25 - (5*the_person.opinion.public_sex)):
            # Not very slutty, so she wants to find somewhere private
            mc.name "Uh huh..."
            the_person "Mmm... y-yes..."
            the_person "E-eh, let's find somewhere more private... *whispers* I don't want to make a scene..."
            menu:
                "Find somewhere more quiet\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                    mc.name "Why wait? Come on, I'm sure we can find somewhere quiet."
                    the_person "O-oh, um... *whispers* okay..."
                    "You and [the_person.possessive_title] hurry off, searching for a private spot."
                    call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_dandere_flirt_response_girlfriend_VT2
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _call_dandere_fuck_person_VT76
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_dandere_flirt_response_girlfriend_VT2

                "Just flirt":
                    $ mc.change_locked_clarity(10)
                    "You reach behind [the_person.possessive_title] and gently touch her waist, making her blush."
                    mc.name "Alright, I'll be patient. I just want to see how turned on you get."
                    "She looks down, her face flushing with embarrassment, and her voice barely above a whisper."
                    the_person "I-I think I'm already... *whispers* pretty turned on..."
            the_person "Mmm... alright, let me enjoy this for now."
            "She sighs with a blush on her face as she leans into your touch."
        else:
            the_person "W-well... *whispers* if you think I'm beautiful, then... *gulps* kiss me..."
            "You put your arm around her waist and lean close, kissing her on her lips."
            "When you break the kiss [the_person.possessive_title] sighs happily and leans her head against your shoulder."
            the_person "W-why did you stop? *whispers* I was having such a good time..."
            menu:
                "Make out":
                    "You don't say a word as you lean back and kiss her again, slowly and sensually this time."
                    "[the_person.title] presses her body against you in response, grinding her hips against your thigh."

                    call mc_move_to_private_location(the_person) from  _call_mc_move_to_private_location_dandere_flirt_response_girlfriend
                    call fuck_person(the_person, start_position = kissing, private = _return, skip_intro = True) from _call_dandere_fuck_person_VT77
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_dandere_flirt_response_girlfriend

                "Just flirt":
                    mc.name "I just like to tease you."
                    $ mc.change_locked_clarity(10)
                    "You reach around and gently touch her waist, making her blush."
                    "She pouts melodramatically and rubs your chest."
                    the_person "Ugh, you're the worst... *whispers* I was already getting turned on..."
    else:
        # You're alone, so she's open to fooling around.
        the_person "W-well... *whispers* you've got me all alone, so... *gulps* how about you show me just how lucky you feel?"
        "She reaches down to your waist and cups your crotch, rubbing it gently."
        menu:
            "Kiss her":
                if the_person.has_taboo("kissing"):
                    $ the_person.call_dialogue("kissing_taboo_break")
                    $ the_person.break_taboo("kissing")
                "You lean in closer, your lips inches away from hers. Your heart races as you feel her anticipation through your fingertips on her waist. Finally, you close the distance and press your lips against hers."
                "It's soft yet passionate, hesitant yet eager. She lets a sigh of relief after breaking the kiss."
                "You pull away slowly, relishing in the lingering touch of your lips on hers. Her eyes are closed, her breathing ragged as you admire how beautifully vulnerable she looks right now."
                call fuck_person(the_person, start_position = kissing, skip_intro = True) from _call_dandere_fuck_person_VT78
                $ the_person.call_dialogue("sex_review", the_report = _return)
                $ the_person.review_outfit()

            "Just flirt":
                mc.name "I'm sorry for being so forward earlier."
                "She pouts melodramatically."
                the_person "It's alright... *whispers* I understand you were excited..."
                "She replies with a reassuring smile on her face as she leans into your touch again."
    return

label dandere_flirt_response_affair(the_person):
    # Lead in: mc.name "You look so good today [the_person.title], you're making me want to do some very naughty things to you."
    if mc.location.person_count > 1: #There are other people around, she's nervous about people finding out what you're doing.
        if (the_person.opinion.cheating_on_men *15) + the_person.effective_sluttiness() > 50: #SHe's turned on by flirting in public or doesn't think anything is wrong with it
            "[the_person.possessive_title!c] bites her lower lip and looks you up and down, her eyes lingering on your crotch."
            $ mc.change_locked_clarity(20)
            "[the_person.possessive_title!c] hesitantly reaches out and touches your arm, her hand trembling slightly."
            the_person "E-eh, th-thank you... *whispers* but we should probably not do anything too... public..."
            the_person "Just be patient... *whispers* I'll be all over you soon enough..."
            menu:
                "Find somewhere more quiet\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                    mc.name "Alright, let's go."
                    "You and [the_person.title] hurry off to find a quiet spot, trying to be discreet."
                    call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_dandere_flirt_response_affair
                    $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
                    "As soon as you're alone she pulls you into a deep and passionate kiss."
                    $ the_person.draw_person(position = "kissing")
                    the_person "A-ah... *whispers* I've wanted this for so long..."
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _call_dandere_fuck_person_VT79
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_dandere_flirt_response_affair
                "Just flirt":
                    "You slide your arm around [the_person.title]'s waist and rest your hand on her hip, trying to be subtle."
                    mc.name "You'll have to wait a little bit, we don't have time for all the things I want to do to you right now."
                    $ mc.change_locked_clarity(20)
                    "She glances around nervously, then leans in close to whisper in your ear."
                    the_person "I-I can think of so many fun things to do with you... *whispers* but we have to be careful..."
                    "She pulls back and looks up at you with a shy expression."
                    the_person "Just don't make me wait too long, okay? *whispers* I barely get any attention from my [the_person.so_title]..."
                    "You give her a reassuring smile and a gentle squeeze on the hip."
                    mc.name "It won't be too long, I promise."
        else: #She's shy or nervous about being discovered
            "[the_person.possessive_title] blushes deeply, looking away from your gaze."
            the_person "Um... I-I appreciate it, but we should probably not do anything too... public..."
            "[the_person.possessive_title!c] laughs nervously, then shakes her head and glances around."
            the_person "You're looking pretty... *whispers* attractive too, but we need to be more subtle."
            the_person "I don't want any rumours getting back to my [the_person.so_title]. That would really... *whispers* complicate things..."
            $ mc.change_locked_clarity(15)
            "After checking again that nobody else is watching she hesitantly reaches out and touches your arm, her hand trembling slightly."
            the_person "Just be patient... *whispers* I'll be all over you soon enough..."
            mc.name "Alright, I think I can contain myself a little while longer."
            "She pulls her hand back and smiles shyly."
    else:
        # the_person "Yeah? Well there's nobody around, and I'm not going to stop you."
        the_person "O-oh yeah? *whispers* well then, what do you want to do to me?"
        menu:
            "Feel her up":
                "You put your arms around [the_person.possessive_title]'s waist and rest your hands on her hips, trying to be gentle."
                mc.name "Well, first I want to get my hands all over your... *whispers* beautiful body..."
                "You massage her hips, trying to be subtle. She sighs happily and leans against your body."
                the_person "W-what next? *whispers* what do you want to do to me?"
                "You spin her around and shift your hands to her waist, trying to be gentle."
                mc.name "No need to rush things... *whispers* just relax and enjoy for now..."
                call fuck_person(the_person, private = True, start_position = standing_grope, skip_intro = True) from _call_dandere_fuck_person_VT80
                $ the_person.call_dialogue("sex_review", the_report = _return)
                $ the_person.review_outfit()
            "Just flirt":
                $ mc.change_locked_clarity(10)
                "You put your arms around [the_person.possessive_title]'s waist and rest your hands on her hips, trying to be subtle."
                mc.name "I wish I had the time... *whispers* you'll have to wait until later..."
                "You massage her hips, trying to be gentle. She sighs happily and leans her weight against you."
                the_person "A-aww, are you sure? *whispers* I was really looking forward to it..."
                "You give her a reassuring smile and a gentle squeeze on the hip."
                mc.name "I won't make you wait long, I promise."
    return

label dandere_flirt_response_text(the_person):
    mc.name "Hey [the_person.title], what's going on? I was just feeling a bit... understimulated, and thought we could talk." 
    the_person "E-eh... *text pause* I see..." 
    "there's an awkward silence as you both try to figure out how to proceed. Finally, she texts back with hesitation."
    if the_person.is_affair:
        the_person "W-well... *text pause* maybe we could find something... interesting to do together?"
        the_person "W-when would be a good time for you?"
        mc.name "Um, how about this weekend? We can figure out what to do then."
        the_person "O-oh, s-sounds good... *text pause* I'll make sure to be free"

    elif the_person.is_girlfriend:
        the_person "I... I understand. *text pause* Maybe we should plan another date soon?"
        the_person "J-just let me know when you're free and we can... *text pause* make arrangements"
        mc.name "Yeah, sure. We'll do that."
        the_person "O-oh, y-yeah... *text pause* I'm looking forward to it"

    elif the_person.love < 40:
        if the_person.effective_sluttiness() > the_person.love:
            the_person "B-boredom can be... *text pause* kind of exciting, huh?"
        else:
            the_person "I-I'm sorry to hear that you're feeling bored..."

    else:
        if the_person.effective_sluttiness() > the_person.love:
            the_person "B-boredom can be... *text pause* kind of intriguing, don't you think?"
            the_person "S-so, what would you like to... *text pause* talk about?"
            the_person "O-or should I... *text pause* entertain you in a different way?"
        else:
            the_person "I-I see... *text pause* well, if you ever want someone to chat with, just let me know..."
    return

label dandere_condom_demand(the_person):
    if the_person.wants_creampie:
        "[the_person.title] looks down, her face flushing with embarrassment, and whispers..."
        the_person "E-eh, um... *whispers* maybe we should use a condom..."
        "[the_person.title] fidgets with her hands, her voice barely above a whisper."
        the_person "I-I know it's not... *whispers* ideal, but safety is important..."
    else:
        "[the_person.title] bites her lip nervously and looks away, her voice barely above a whisper."
        the_person "D-do you... *whispers* have a condom?"
        "[the_person.title] fidgets with her hands, her face flushing with embarrassment."
        "After a moment of uncomfortable silence, she musters up enough courage to add, "
        the_person "I-I mean... *whispers* it's just for protection... and stuff..."
        "[the_person.title] looks down, her face still flushed with embarrassment."
    return

label dandere_condom_ask(the_person):
    if the_person.on_birth_control:
        the_person "E-eh, um... *whispers* do you want to use a condom?"
        the_person "I-I'm on the pill, but... *whispers* accidents can still happen, right?"
        $ the_person.update_birth_control_knowledge()
    elif the_person.wants_creampie:
        the_person "I-if you want to... *whispers* cum inside me..."
        the_person "M-maybe we should use a condom... *whispers* just to be safe..."
        $ the_person.discover_opinion("creampies")
    else:
        the_person "I-I think we should... *whispers* use a condom..."
        the_person "I-I trust you to... *whispers* pull out, but maybe it's better to be safe..."
        the_person "E-eh, um... *whispers* just in case, right?"
    return

label dandere_condom_bareback_ask(the_person):
    if the_person.wants_creampie:
        if the_person.is_infertile or the_person.on_birth_control:
            "[the_person.title] looks down, her face flushing with embarrassment, and whispers..."
            the_person "E-eh, um... *whispers* can we not use a condom?"
            "[the_person.title] fidgets with her hands, her voice barely above a whisper."
            the_person "I-if it's okay with you, that is..."
            if the_person.on_birth_control:
                the_person "Y-you can... *whispers* cum inside me, I'm on the pill..."
                $ the_person.update_birth_control_knowledge()
        else:
            "[the_person.title] blushes deeply, her eyes looking away, and whispers..."
            the_person "I-I think it would be... *whispers* really hot if we didn't use protection..."
            "She trails off, unable to finish the sentence, and looks down, her face still flushed with embarrassment."
            if not the_person.knows_pregnant:
                the_person "I-I think it would be... *whispers* really special if you... *gulps* fill me..."
        $ the_person.discover_opinion("creampies")
    else:
        the_person "D-don't bother with a condom, [the_person.mc_title]... *whispers* I want to feel you..."
        if not the_person.knows_pregnant:
            "[the_person.title] shivers slightly at the thought, her eyes looking away, and whispers..."
            the_person "I-I think it would be... *whispers* really special to feel you inside me... *gulps* without anything between us..."
            "She looks down, her face still flushed with embarrassment."
        else:
            "[the_person.title] hesitates, her voice barely above a whisper."
            the_person "I-it's okay if you... *whispers* don't wear a condom... I mean, if that's what you want..."
            "She looks down, her face still flushed with embarrassment, and whispers..."
            the_person "I-I trust you... *whispers* to make the right decision..."
    return

label dandere_condom_bareback_demand(the_person):
    if the_person.has_breeding_fetish: #Actively looking to get knocked up.
        if the_person.knows_pregnant:
            the_person "E-eh, um... *whispers* never mind..."
            "[the_person.title] looks away, her face flushing with embarrassment."
        elif the_person.is_infertile:
            the_person "W-well, um... *whispers* if we can't have a baby anyway..."
            "[the_person.title] hesitates and stammers, clearly uncomfortable with her own desires."
            the_person "M-maybe it doesn't matter... *whispers* but I still want to feel you inside me..."
            $ the_person.update_birth_control_knowledge()
        else:
            the_person "I-I know it's not rational... *whispers* but I want to feel you inside me, without anything between us..."
            "[the_person.title] looks down, her face flushing with embarrassment, and whispers..."
            the_person "B-breed me... *whispers* please..."
    elif the_person.wants_creampie: #Just likes raw sex
        if the_person.is_infertile:
            the_person "E-eh, um... *whispers* never mind..."
            "[the_person.title] looks away, her face flushing with embarrassment."
            $ the_person.update_birth_control_knowledge()
        elif the_person.on_birth_control:
            the_person "W-well, um... *whispers* if I'm on birth control anyway..."
            "[the_person.title] hesitates and stammers, clearly uncomfortable with her own desires."
            the_person "M-maybe it wouldn't be so bad... *whispers* as long as you don't mind..."
            $ the_person.update_birth_control_knowledge()
        else:
            the_person "I-I know it's not safe... *whispers* but I want to feel you inside me, without anything between us..."
            "[the_person.title] looks down, her face flushing with embarrassment."
    else:
        if the_person.is_infertile:
            the_person "W-well, um... *whispers* since we can't have a baby anyway..."
            "[the_person.title] hesitates and stammers, clearly uncomfortable with her own desires."
            the_person "M-maybe it wouldn't be so bad... *whispers* to just do it this way..."
        elif the_person.on_birth_control:
            the_person "I-I guess if I am on birth control... *whispers* then it wouldn't be a problem?"
            "[the_person.title] looks away, her face flushing with embarrassment."
            the_person "A-as long as you don't mind... *whispers* I mean..."
            $ the_person.update_birth_control_knowledge()
        else:
            the_person "U-um... *whispers* well, since there aren't any condoms..."
            "[the_person.title] bites her lip nervously and avoids eye contact, clearly struggling with her own sexual desires in such an intimate situation."
            the_person "M-maybe we could just... *whispers* do it this way?"
    return

label dandere_cum_face(the_person):
    if the_person.has_cum_fetish or the_person.obedience > 180:
        if the_person.has_cum_fetish or the_person.effective_sluttiness() > 60 or the_person.opinion.cum_facials > 0:
            the_person "E-eh, um... *whispers* do I look okay like this?"
            "[the_person.title] looks down, her face flushing with embarrassment, and whispers..."
            the_person "I-I mean, is this... *whispers* what you wanted?"
        else:
            the_person "I-I hope you... *whispers* enjoyed yourself, [the_person.mc_title]..."
            "[the_person.title] gently wipes away some semen, avoiding eye contact and blushing deeply, her voice barely above a whisper."
            the_person "I-I'm glad I could... *whispers* make you happy..."
    else:
        if the_person.effective_sluttiness() > 80 or the_person.opinion.cum_facials > 0:
            the_person "M-mmm... *whispers* that feels so good..."
            "[the_person.title] bites her lower lip, her eyes looking away, and whispers..."
            the_person "D-do you think I... *whispers* look cute like this?"
        else:
            the_person "E-eh, um... *whispers* I'm glad that's over..."
            "[the_person.title] looks away, her face flushing with embarrassment, and whispers..."
            the_person "Y-you can... *whispers* look at me for a little while longer, if you want..."
    return

label dandere_cum_mouth(the_person):
    if the_person.has_cum_fetish or the_person.obedience > 180:
        if the_person.has_cum_fetish or the_person.effective_sluttiness() > 60 or the_person.opinion.drinking_cum > 0:
            the_person "E-eh, th-thank you... *whispers* [the_person.mc_title]..."
            "[the_person.title] looks down, her face flushing with embarrassment, and whispers..."
            the_person "I-I'm glad I could... *whispers* make you happy..."
        else:
            "[the_person.title]'s face twitches as she reluctantly tastes your cum in her mouth."
            the_person "U-ugh... *whispers* it's done now, [the_person.mc_title]..."
            "[the_person.title] looks away, her face still flushing with embarrassment, and whispers..."
            the_person "C-can we... *whispers* move on now?"
    else:
        if the_person.effective_sluttiness() > 80  or the_person.opinion.drinking_cum > 0:
            the_person "M-mmm... *whispers* you taste... um, interesting..."
            "[the_person.title] looks up at you with a shy expression, her eyes sparkling with curiosity, and whispers..."
            the_person "W-was it... *whispers* satisfying to watch me?"
        else:
            the_person "U-ugh... *whispers* this is so... uncomfortable..."
            "[the_person.title] looks away, her face flushing with embarrassment, and whispers..."
            the_person "I-I don't know if I can... *whispers* do this again..."
    return

label dandere_cum_pullout(the_person):
    # Lead in: "I'm going to cum!"
    if mc.condom:
        if the_person.wants_creampie and not the_person.has_taboo("condomless_sex"): 
            if the_person.knows_pregnant:
                the_person "E-eh, um... *whispers* take off the condom and... *gulps* cum inside me..."
                the_person "Y-you already... *whispers* knocked me up, so... *sighs* who cares?"
            elif the_person.on_birth_control:
                the_person "O-oh, um... *whispers* please, [the_person.mc_title]..."
                "She moans desperately, her voice barely above a whisper."
                the_person "I-I give in... *whispers* I want you to cum inside me..."
            else:
                the_person "I-I don't... *whispers* care anymore..."
                "She moans desperately, her voice barely above a whisper."
                the_person "R-rip off the condom and... *whispers* cum inside me, [the_person.mc_title]..."
                $ the_person.update_birth_control_knowledge()
                the_person "P-please... *whispers* make me... *gulps* pregnant..."
            menu: 
                "Take off the condom":
                    "You don't have much time to spare. You pull out, barely clearing her pussy, and pull the condom off as quickly as you can manage."
                    $ mc.condom = False
                    $ use_condom = False  
                "Leave it on":
                    "You ignore [the_person.possessive_title]'s cum-drunk offer and keep the condom in place."
        else:
            the_person "I-I'm going to... *whispers* make you cum..."
    else:
        if the_person.wants_creampie:
            if the_person.knows_pregnant: 
                the_person "C-creampie me... *whispers* [the_person.mc_title]..."
                the_person "I-I want it all... *whispers* inside me..."
            elif the_person.opinion.creampies > 0:
                "[the_person.possessive_title!c] moans happily, her voice barely above a whisper."
                if the_person.on_birth_control: 
                    the_person "F-fill me up... *whispers* with your cum, [the_person.mc_title]..."
                else: 
                    $ the_person.update_birth_control_knowledge()
                    the_person "O-oh, um... *whispers* cum inside me, [the_person.mc_title]..."
                    the_person "I-I want you to... *whispers* breed me..."
            elif the_person.is_infertile:
                the_person "C-cum wherever you want... *whispers* [the_person.mc_title]..."
                the_person "I-I'm infertile... *whispers* so it's okay..."
            elif the_person.on_birth_control: 
                $ the_person.update_birth_control_knowledge()
                the_person "C-cum wherever you want... *whispers* [the_person.mc_title]..."
                the_person "I-I'm on the pill... *whispers* so it's fine..."
            else: 
                the_person "H-hells yeah... *whispers* cum inside me..."
                the_person "A-and creampie me... *whispers* too..."
        else:
            if the_person.is_infertile:
                the_person "J-just pull out... *whispers* I don't want your cum inside me..."
            elif not the_person.on_birth_control: 
                $ the_person.update_birth_control_knowledge()
                the_person "F-fuck, pull out... *whispers* I'm not on the pill..."
            elif the_person.opinion.creampies < 0:
                the_person "P-pull out... *whispers* I don't want you to cum in me..."
            else:
                the_person "H-hells yeah... *whispers* cum inside me..."
                the_person "A-and creampie me... *whispers* too..."
    return

label dandere_cum_condom(the_person):
    if the_person.effective_sluttiness() > 75 or the_person.opinion.creampies > 0:
        the_person "E-eh, um... *whispers* it's so warm..."
        the_person "I-I hope... *whispers* your condom doesn't break..."
        the_person "A-all of that... *whispers* would be inside me..."
        "[the_person.possessive_title!c] blushes deeply, her voice barely above a whisper."
    else:
        the_person "O-oh no... *whispers* I hope you buy good condoms..."
        the_person "T-that's a lot of... *whispers* cum..."
        the_person "B-but maybe... *whispers* you're dreaming of... *gulps* knocking me up..."
        the_person "O-oh, umm... *whispers* I really hope you buy good condoms..."
        the_person "I-it feels like... *whispers* there's going to be so much..."
        the_person "B-but maybe... *whispers* you're into... *gulps* creampies..."
        the_person "A-and want to... *whispers* make a baby with me..."
    "[the_person.possessive_title!c] moans happily, her face still flushed with embarrassment."
    return

label dandere_cum_vagina(the_person):
    if the_person.has_taboo("creampie"):
        $ the_person.call_dialogue("creampie_taboo_break")
        $ the_person.break_taboo("creampie")
        return

    if the_person.wants_creampie:
        if the_person.knows_pregnant:
            the_person "E-eh, um... *whispers* it feels so good to have your cum inside me..."
            the_person "I-I guess that's what happens when you... *whispers* get knocked up..."
        elif the_person.is_infertile:
            the_person "M-mmm... *whispers* this is amazing..."
            the_person "Y-your hot cum... *whispers* filling my pussy..."
        elif the_person.on_birth_control:
            if the_person.has_significant_other:
                the_person "O-oh, wow... *whispers* you really gave it to me..."
                the_person "I-it's so much... *whispers* I can feel it all inside..."
                the_person "M-my [the_person.so_title]... *whispers* never cums like that..."
            else:
                if the_person.knows_pregnant:
                    the_person "Y-your cum is... *whispers* everywhere..."
                    the_person "A-and I guess... *whispers* that means we should be careful not to get pregnant again..."
                    "She giggles nervously"
                elif the_person.is_infertile:
                    the_person "I-I'm going to... *whispers* feel your cum all day long..."
                    the_person "I-isn't it... *whispers* wonderful?"
                else:
                    the_person "T-this is a lot of... *whispers* cum..."
                    the_person "I-I hope you... *whispers* weren't trying to get me pregnant..."
                $ the_person.update_birth_control_knowledge()
        elif the_person.effective_sluttiness() > 75 or the_person.opinion.creampies > 0:
            if the_person.has_significant_other:
                the_person "O-oh, it feels... *whispers* so good to be filled up with your cum..."
                the_person "I-I don't care... *whispers* if we get pregnant again... as long as my [the_person.so_title] is okay with it..."
            else:
                the_person "M-mmm... *whispers* this is amazing..."
                the_person "Y-your hot cum... *whispers* inside me feels so good..."
                the_person "E-even though... *whispers* it might make me pregnant..."
        else:
            if the_person.has_significant_other:
                the_person "O-oh my... *whispers* you really gave it to me..."
                the_person "I-I feel so... *whispers* full of your cum..."
            else:
                the_person "T-this is a lot of... *whispers* cum..."
                the_person "M-maybe we... *whispers* should be more careful next time..."
    else: #She's angry
        if the_person.knows_pregnant:
            the_person "Y-you said you... *whispers* would pull out!"
            the_person "N-now I'm going to... *whispers* have your baby, and it's all your fault!"
        elif not the_person.on_birth_control:
            if the_person.has_significant_other:
                the_person "O-oh no... *whispers* [the_person.mc_title] is going to kill me when he finds out I got pregnant again!"
                the_person "W-why didn’t you... *whispers* pull out?"
                if the_person.kids > 0:
                    the_person "... A-and now we... *whispers* have another one on the way..."
            else:
                the_person "Y-you said you... *whispers* would pull out!"
                the_person "N-now what am I... *whispers* supposed to do?"
                the_person "M-my [the_person.so_title]... *whispers* doesn't even know about this yet..."
                $ the_person.update_birth_control_knowledge()
                the_person "W-whatever... *whispers* I guess it's already happened... C-condom next time please!"
        elif the_person.is_infertile:
            the_person "I-I told you... *whispers* to pull out, but instead you creampied me!"
            the_person "T-this is all... *whispers* your fault!"
        elif the_person.has_significant_other:
            the_person "H-hey... *whispers* I said to pull out!"
            the_person "I-I have a... *whispers* [the_person.so_title], even if I'm on the pill you shouldn't be filling me up..."
            $ the_person.update_birth_control_knowledge()
            the_person "I-I don't want to... *whispers* have to make you wear a condom, so be a little more careful next time..."
        elif the_person.opinion.creampies < 0:
            the_person "Y-you said you... *whispers* would pull out... but it feels like there's cum everywhere now..."
        else:
            the_person "W-why didn't you... *whispers* pull out?"
            the_person "N-now we have to... *whispers* deal with this mess..."
            the_person "D-don't make a habit... *whispers* of it, otherwise I'll twist it..."
    return

label dandere_cum_anal(the_person):
    if the_person.has_taboo("anal creampie"):
        $ the_person.call_dialogue("anal_creampie_taboo_break")
        $ the_person.break_taboo("anal creampie")
        return

    if the_person.sluttiness > 75 or the_person.opinion.anal_creampies > 0:
        the_person "E-eh, um... *whispers* I'm not sure how I feel about this..."
        the_person "B-but if it's what you... *whispers* want, maybe I should just go along with it..."
        "[the_person.title] looks down, her face flushing with embarrassment, and whispers..."
        the_person "I-I want to make you... *whispers* happy, after all..."
    elif the_person.opinion.anal_creampies < 0:
        the_person "O-oh no, p-please... *whispers* don't do that..."
        "[the_person.title] looks up at you with a worried expression, her voice barely above a whisper."
        the_person "B-but how can I... *whispers* stop you when you're so excited?"
    else:
        the_person "T-this is... *whispers* different..."
        "[the_person.title] looks down, her face flushing with embarrassment, and whispers..."
        the_person "B-but if it makes you... *whispers* happy, I'll try to... *gulps* enjoy it..."
    return

label dandere_surprised_exclaim(the_person):
    $rando = renpy.random.choice(["E-eh...","O-oh no...","Um, ah...","W-what's happening...","A-ah! Oh, um...", "A-ah!", "O-oh my...", "W-wait, what?!"])
    the_person "[rando]"
    return

label dandere_talk_busy(the_person):
    if the_person.obedience > 120:
        the_person "E-eh, um... *whispers* I'm really busy right now..."
        the_person "C-could we... *whispers* talk about this later, [the_person.mc_title]?"
        "[the_person.title] looks down, her face flushing with embarrassment, and whispers..."
        the_person "I-I'm sorry... *whispers* I don't have time to chat right now..."
    else:
        the_person "O-oh, h-hello... *whispers* I'm kind of in a hurry..."
        the_person "M-maybe we... *whispers* could talk later?"
        "[the_person.title] smiles shyly and looks away, her voice barely above a whisper."
        the_person "I-I'd like to... *whispers* chat with you, but not right now..."
    return

label dandere_sex_strip(the_person):
    if the_person.sluttiness < 20:
        if the_person.arousal_perc < 50:
            the_person "E-eh, um... *whispers* I think I'll take something off..."
            "[the_person.title] looks down, her face flushing with embarrassment, and whispers..."
            the_person "I-I feel a bit... *whispers* hot..."
        else:
            the_person "A-ah, this is... *whispers* too much..."
            "[the_person.title] looks up at you with a shy expression, her voice barely above a whisper."
            the_person "L-let me... *whispers* remove something..."

    elif the_person.sluttiness < 60:
        if the_person.arousal_perc < 50:
            the_person "W-why do I... *whispers* even wear all of this?"
            "[the_person.title] looks down, her face flushing with embarrassment, and whispers..."
            the_person "I-it's just... *whispers* getting in the way..."
        else:
            the_person "I-I want to... *whispers* get more naked for you..."
            "[the_person.title] looks up at you with a shy expression, her voice barely above a whisper."
            the_person "I-if you... *whispers* want me to, that is..."

    else:
        if the_person.arousal_perc < 50:
            the_person "G-give me a... *whispers* moment..."
            "[the_person.title] smiles shyly and looks away, her voice barely above a whisper."
            the_person "I-I'll take... *whispers* something off just for you..."
        else:
            the_person "U-ugh, l-let me... *whispers* get this off..."
            "[the_person.title] looks up at you with a desperate expression, her voice barely above a whisper."
            the_person "I-I want to... *whispers* feel your touch everywhere..."
    return

label dandere_sex_watch(the_person, the_sex_person, the_position):
    $ title = the_person.title if not the_person.is_stranger else "The stranger"
    if the_person.sluttiness < the_position.slut_requirement - 20:
        $ the_person.draw_person(emotion = "angry", display_transform = character_left_flipped)
        the_person "E-eh, um... *whispers* can you two please keep it down?"
        the_person "I-it's just... *whispers* really embarrassing..."
        $ the_person.change_stats(obedience = -2, happiness = -1)
        "[title] looks away, her face flushing with embarrassment, and whispers..."
        return False

    if the_person.sluttiness < the_position.slut_requirement - 10:
        $ the_person.draw_person(display_transform = character_left_flipped)
        the_person "C-could you two... *whispers* at least be more discreet?"
        the_person "I-it's just... *whispers* really awkward..."
        $ the_person.change_happiness(-1)
        "[title] tries to avoid looking at you and [the_sex_person.fname] [the_position.verb], clearly uncomfortable."
        return False

    if the_person.sluttiness < the_position.slut_requirement:
        $ the_person.draw_person(display_transform = character_left_flipped)
        if not is_watching(the_person):
            the_person "Y-you're certainly... *whispers* feeling bold today, [the_sex_person.fname]..."
            the_person "A-at least... *whispers* it looks like you're having a good time..."
        $ the_person.change_slut(1, 30)
        "[title] watches your encounter with [the_sex_person.fname], her eyes flickering between the two of you."
        return True

    if the_person.sluttiness >= the_position.slut_requirement and the_person.sluttiness < the_position.slut_cap:
        $ the_person.draw_person(display_transform = character_left_flipped)
        if not is_watching(the_person):
            the_person "O-oh wow... *whispers* that's really hot..."
            the_person "Y-you don't mind... *whispers* if I watch, do you?"
        $ the_person.change_slut(1, 50)
        "[title] watches your intimate encounter with [the_sex_person.fname], her cheeks flushing slightly as she struggles to contain her excitement."
        return True

    $ the_person.draw_person(emotion = "happy", display_transform = character_left_flipped)
    if renpy.random.randint(0, 1) == 0:
        the_person "C-come on... *whispers* [the_person.mc_title], you're going to have to give her a little more than that..."
    else:
        call watcher_position_comment(the_person, the_sex_person, the_position) from _call_watcher_position_comment_dandere_sex_watch_VT
    "[title] watches your passionate encounter with [the_sex_person.fname], her eyes wide and mouth slightly agape as she struggles to contain her arousal."
    return True

label dandere_being_watched(the_person, the_watcher, the_position):
    $ title = the_watcher.fname if not the_watcher.is_stranger else "the stranger"
    if the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #They agree you should give it to her harder
        the_person "E-eh, um... *whispers* this feels really intense..."
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [title] watching you and her [the_position.verb], her face flushing with embarrassment."
    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's super slutty and doesn't care what people think.
        the_person "I-I don't... *whispers* mind if [title] watches..."
        "[the_person.title] looks away, her face still flushing with embarrassment."
    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #She's super slutty and encourages the watcher to be slutty.
        the_person "W-well, [title]... *whispers* you should try it too... maybe..."
        the_person "B-but not... *whispers* right now, okay?"
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [title] watching you and her [the_position.verb], her face still flushing with embarrassment."
    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #She's into it and encouraged by the slut watching her.
        the_person "I-I can... *whispers* feel myself getting hotter..."
        the_person "E-even with... *whispers* [title] here..."
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [title] watching you and her [the_position.verb], her face flushing with embarrassment."
    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's into it but shamed by the prude watching her.
        the_person "A-ah, maybe... *whispers* we should find a more private place..."
        $ the_person.change_stats(arousal = -1, slut = -1)
        "[the_person.title] looks away, her face flushing with embarrassment, and whispers..."
        the_person "I-I don't want... *whispers* to be watched..."
    else: #the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #They're both into it but not fanatical about it.
        "[the_person.possessive_title!c] looks directly at [title] and whispers..."
        the_person "W-well, [title]... *whispers* you seem to be... um, enjoying yourself too..."
        $ the_person.change_stats(arousal = 1, slut = 1, max_slut = 30)
        "[the_person.title] seems more comfortable [the_position.verbing] you with [title] around, her face still flushing with embarrassment."
    return

label dandere_work_enter_greeting(the_person):
    if the_person.happiness < 80 or the_person.love < 0:
        "[the_person.title] glances at you when you enter the room, her eyes flickering briefly before she quickly looks away and focuses on her work, her face expressionless."

    elif the_person.happiness > 130:
        if the_person.sluttiness > 40:
            the_person "E-eh, um... *whispers* h-hi [the_person.mc_title]..."
            "She stutters, her cheeks flushing slightly as she tries to maintain eye contact with you, but ultimately looks away."
            the_person "I-I was just... *whispers* working on this project..."
            "She trails off, unable to finish her sentence due to her nervousness."
        else:
            "[the_person.title] looks up from her work when you enter the room, offering a shy smile that barely reaches her eyes."
            the_person "H-hi [the_person.mc_title]... *whispers* it's nice of you to stop by..."
            "Her voice is soft and hesitant, as if she's unsure whether or not she should be engaging in conversation with you at all."
    else:
        if the_person.sluttiness > 60:
            $ the_person.draw_person(position = "stand4")
            "[the_person.title] walks over to you when you come into the room, her eyes cast downward."
            the_person "E-eh, um... *whispers* just the person I was hoping would stop by..."
            "She whispers, barely audible above the sound of her nervous breathing."
            the_person "I-I'm here if you... *whispers* need anything..."
            "She looks up at you with a shy expression, her eyes sparkling with nervousness."
        else:
            "[the_person.title] stands near her workstation, eyes cast downward as she fiddles with a pen in her hand."
            the_person "...H-hi [the_person.mc_title]... *whispers* I mean, if you need anything or want to talk about something..."
            "She whispers, barely audible above the sound of her nervous breathing."
            the_person "P-please feel free to... *whispers* ask?"
            "Her gaze flickers upwards briefly before returning to her pen, which she continues to twirl around in her fingers."
    return

label dandere_date_seduction(the_person):
    if the_person.is_girlfriend:
        "[the_person.possessive_title!c] looks up at you with a shy expression, her eyes sparkling with nervousness."
        the_person "E-eh, um... *whispers* that was such a great time..."
        $ mc.change_locked_clarity(30)
        if the_person.effective_sluttiness(["vaginal_sex", "condomless_sex"]) > 60 and the_person.wants_creampie and the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex >= 0 and the_person.opinion.creampies >= 0 and not the_person.on_birth_control and not the_person.knows_pregnant:
            if the_person.opinion.creampies > 0: 
                the_person "L-let's go back to my place... *whispers* and make love all night long..."
                "[the_person.title] hesitates, biting her lower lip nervously before continuing in a soft whisper, "
                the_person "...and maybe... *whispers* make a baby..."
            else:
                the_person "L-let's go back to my place... *whispers* and be intimate without condoms..."
                "[the_person.title] hesitates, biting her lower lip nervously before continuing in a soft whisper, "
                the_person "...all night long...really hard...bare...back.."
        elif the_person.effective_sluttiness(["vaginal_sex", "condomless_sex"]) > 60 and the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex > 0:
            the_person "L-let's go back to my place... *whispers* and make love without any barriers..."
            "[the_person.title] hesitates, swallowing hard before continuing in a barely audible whisper, "
            the_person "...no condoms allowed..."
        elif the_person.effective_sluttiness(["vaginal_sex"]) > 50 and the_person.opinion.vaginal_sex > 0:
            the_person "L-let's go back to my place... *whispers* and get my little pussy pounded..."
            "[the_person.title] hesitates, biting her lower lip as she struggles with her words. After a long pause, she finally manages to speak in a soft, shy voice, "
            the_person "...by your big cock..."
        elif the_person.effective_sluttiness(["anal_sex"]) > 60 and the_person.opinion.anal_sex > 0:
            "[the_person.title] hesitates, blushing deeply as she struggles to find the words. Eventually, she musters up the courage to speak in a quiet, shy voice, "
            the_person "L-let's go back to my place... *whispers* and try something new..."
            "[the_person.title] trails off, biting her lower lip nervously before continuing with even greater hesitation, "
            the_person "...in my ass..."
        elif the_person.effective_sluttiness(["sucking_cock"]) > 40 and the_person.opinion.giving_blowjobs > 0:
            the_person "L-let's go back to my place... *whispers* and I'll give you a nice long blowjob..."
            "[the_person.title] hesitates, biting her lower lip nervously before continuing in a soft whisper, "
            the_person "...if you want..."
        elif the_person.effective_sluttiness() > 40 and the_person.opinion.being_covered_in_cum > 0:
            the_person "I-it doesn't have to be over yet... *whispers* does it?"
            "[the_person.title] hesitates, biting her lower lip nervously before continuing in a soft whisper, "
            the_person "L-let's go back to my place... *whispers* and keep the fun going..."
            "[the_person.title] looks up at you with a shy expression, her eyes sparkling with nervousness."
            the_person "...if you want to... *whispers* cover me in cum..."
        elif the_person.effective_sluttiness(["touching_body"]) > 40 and the_person.opinion.giving_tit_fucks > 0 and the_person.has_large_tits:
            the_person "I-it doesn't have to be over yet... *whispers* does it?"
            "[the_person.title] hesitates, biting her lower lip nervously before continuing in a soft whisper, "
            the_person "L-let's go back to my place... *whispers* and keep the fun going..."
            "[the_person.title] looks up at you with a shy expression, her eyes sparkling with nervousness."
            the_person "...if you want to... *whispers* slide your cock between my breasts..."
        else: 
            the_person "I-it doesn't have to be over yet... *whispers* does it?"
            "[the_person.title] hesitates, biting her lower lip nervously before continuing in a soft whisper, "
            the_person "L-let's go back to my place... *whispers* and keep the fun going..."
            "[the_person.title] looks up at you with a shy expression, her eyes sparkling with nervousness."
            the_person "...if you want..."
    elif the_person.is_affair:
        the_person "S-so my [the_person.so_title] won't be home tonight... *whispers* I was thinking..."
        "[the_person.title] reaches down and cups your crotch, rubbing it gently through your pants."
        $ mc.change_locked_clarity(40)
        if the_person.wants_creampie and the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex >= 0 and the_person.opinion.creampies >= 0 and not the_person.on_birth_control and not the_person.knows_pregnant:
            if the_person.opinion.creampies > 0: 
                the_person "L-let's go back to my place... *whispers* and make love all night long..."
                "[the_person.title] hesitates, biting her lower lip nervously before continuing in a soft whisper, "
                the_person "...and maybe... *whispers* make a baby..."
            else:
                the_person "L-let's go back to my place... *whispers* and be intimate without condoms..."
                "[the_person.title] hesitates, biting her lower lip nervously before continuing in a soft whisper, "
                the_person "...all night long..."
        elif the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex > 0:
            the_person "L-let's go back to my place... *whispers* and make love without any barriers..."
            "[the_person.title] hesitates, swallowing hard before continuing in a barely audible whisper, "
            the_person "...no condoms allowed..."
        elif the_person.opinion.vaginal_sex > 0:
            the_person "L-let's go back to my place... *whispers* and get my little pussy pounded..."
            "[the_person.title] hesitates, biting her lower lip as she struggles with her words. After a long pause, she finally manages to speak in a soft, shy voice, "
            the_person "...by your big cock..."
        elif the_person.opinion.anal_sex > 0:
            "[the_person.title] hesitates, blushing deeply as she struggles to find the words. Eventually, she musters up the courage to speak in a quiet, shy voice, "
            the_person "L-let's go back to my place... *whispers* and try something new..."
            "[the_person.title] trails off, biting her lower lip nervously before continuing with even greater hesitation, "
            the_person "...in my ass..."
        elif the_person.opinion.giving_blowjobs > 0:
            the_person "L-let's go back to my place... *whispers* and I'll give you a nice long blowjob..."
            "[the_person.title] hesitates, biting her lower lip nervously before continuing in a soft whisper, "
            the_person "...if you want..."
        elif the_person.opinion.being_covered_in_cum > 0:
            the_person "I-it doesn't have to be over yet... *whispers* does it?"
            "[the_person.title] hesitates, biting her lower lip nervously before continuing in a soft whisper, "
            the_person "L-let's go back to my place... *whispers* and keep the fun going..."
            "[the_person.title] looks up at you with a shy expression, her eyes sparkling with nervousness."
            the_person "...if you want to... *whispers* cover me in cum..."
        elif the_person.opinion.giving_tit_fucks > 0 and the_person.has_large_tits:
            the_person "I-it doesn't have to be over yet... *whispers* does it?"
            "[the_person.title] hesitates, biting her lower lip nervously before continuing in a soft whisper, "
            the_person "L-let's go back to my place... *whispers* and keep the fun going..."
            "[the_person.title] looks up at you with a shy expression, her eyes sparkling with nervousness."
            the_person "...if you want to... *whispers* slide your cock between my breasts..."
        elif the_person.opinion.cheating_on_men > 0:
            the_person "L-let's go back to my place... *whispers* and let our desires run wild..."
            "[the_person.title] hesitates, biting her lower lip nervously before continuing in a soft whisper, "
            the_person "...without judgement..."
        else:
            the_person "L-let's go back to my place... *whispers* and make him regret leaving me alone for the night..."
    elif not the_person.has_significant_other:
        $ mc.change_locked_clarity(20)
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                the_person "E-eh, um... *whispers* I've had a really great time tonight, [the_person.mc_title]..."
                "[the_person.title] hesitates, biting her lower lip nervously before continuing in a soft whisper, "
                the_person "...want to come back to my place and... *whispers* see what else we can do?"
            else:
                the_person "Y-you've been really fun tonight... *whispers* [the_person.mc_title]."
                "[the_person.title] hesitates, biting her lower lip nervously before continuing in a soft whisper, "
                the_person "...would you like to come back to my place for some... *whispers* drinks?"
                the_person "M-maybe... *whispers* we can do something else if it feels right..."
        else:
            if the_person.love > 40:
                the_person "T-tonight's been... *whispers* amazing, [the_person.mc_title]..."
                "[the_person.title] hesitates, biting her lower lip nervously before continuing in a soft whisper, "
                the_person "...I don't want to say goodbye... *whispers* yet."
                the_person "D-do you want to... *whispers* come back to my place and have a few drinks?"
            else:
                the_person "T-this might be... *whispers* crazy, but I had a really great time tonight... *whispers* and you make me feel... different, [the_person.mc_title]."
                "[the_person.title] hesitates, biting her lower lip nervously before continuing in a soft whisper, "
                the_person "...would you like to... *whispers* join me at my place for some more conversation... or maybe something else if we both want it?"
    else:
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                $ mc.change_locked_clarity(20)
                the_person "E-eh, um... *whispers* I've had a really great time tonight, [the_person.mc_title]..."
                "[the_person.title] hesitates, biting her lower lip nervously before continuing in a soft whisper, "
                the_person "...want to come back to my place and... *whispers* see what else we can do?"
                the_person "M-my [the_person.so_title] won't be home until... *whispers* morning, so we would have plenty of time..."
            else:
                $ mc.change_locked_clarity(20)
                the_person "Y-you've been really fun tonight... *whispers* [the_person.mc_title]."
                "[the_person.title] hesitates, biting her lower lip nervously before continuing in a soft whisper, "
                the_person "...would you like to come back to my place for some... *whispers* drinks?"
                the_person "M-my [the_person.so_title] is... *whispers* stuck at work and I don't want to be left all alone..."
        else:
            if the_person.love > 40:
                $ mc.change_locked_clarity(20)
                the_person "T-tonight's been... *whispers* amazing, [the_person.mc_title]..."
                "[the_person.title] hesitates, biting her lower lip nervously before continuing in a soft whisper, "
                the_person "...I don't want to say goodbye... *whispers* yet."
                the_person "D-do you want to... *whispers* come back to my place and have a few drinks?"
                the_person "M-my [the_person.so_title] won't be home until... *whispers* morning, and we have a big bed you could... *whispers* help me warm up..."
            else:
                $ mc.change_locked_clarity(20)
                the_person "T-this might be... *whispers* crazy, but I had a really great time tonight... *whispers* and you make me feel... different, [the_person.mc_title]."
                "[the_person.title] hesitates, biting her lower lip nervously before continuing in a soft whisper, "
                the_person "...would you like to... *whispers* join me at my place for some more conversation... or maybe something else if we both want it?"
                the_person "M-my [the_person.so_title] won't be home until... *whispers* morning..."
    return

label dandere_sex_end_early(the_person):
    if the_person.sluttiness > 50:
        if the_person.love > 40:
            if the_person.arousal_perc > 60:
                the_person "E-eh, um... *whispers* you're really done?"
                "[the_person.title] looks up at you with a shy expression, her eyes sparkling with nervousness."
                the_person "I-I'm still... *whispers* really horny, [the_person.mc_title]..."
            else:
                the_person "T-that was... *whispers* all you wanted?"
                "[the_person.title] looks down, her face flushing with embarrassment."
                the_person "I-I thought... *whispers* we could do more together..."
        else:
            if the_person.arousal_perc > 60:
                the_person "F-fuck... *whispers* I'm still really turned on..."
                "[the_person.title] bites her lower lip, her eyes sparkling with nervousness."
                the_person "A-are you... *whispers* sure you don't want any more?"
            else:
                the_person "I-I guess... *whispers* that was a little bit of fun..."
                "[the_person.title] looks away, her face still flushing with embarrassment."
    else:
        if the_person.love > 40:
            if the_person.arousal_perc > 60:
                the_person "[the_person.mc_title]... *whispers* you turned me on so much..."
                "[the_person.title] looks up at you with a shy expression, her eyes sparkling with nervousness."
            else:
                the_person "I-I hope... *whispers* that was enjoyable for both of us, [the_person.mc_title]..."
                "[the_person.title] smiles shyly and looks away."
        else:
            if the_person.arousal_perc > 60:
                the_person "O-oh god... *whispers* I'm still a bit overwhelmed..."
                "[the_person.title] takes a deep breath, her face still flushing with embarrassment."
                the_person "L-let me... *whispers* catch my breath..."
            else:
                the_person "D-done?... *whispers* alright then..."
                "[the_person.title] looks away, her face still flushing with embarrassment."
                the_person "W-we can... *whispers* move on to something else now..."
    return

label dandere_sex_take_control(the_person):
    if the_person.arousal_perc > 60:
        the_person "E-eh, um... *whispers* I didn't mean for that to happen..."
        "[the_person.title] looks down, her face flushing with embarrassment, and whispers..."
        the_person "I-I got a bit... *whispers* carried away..."
    else:
        the_person "A-are you... *whispers* really done already?"
        "[the_person.title] looks up at you with a shy expression, her eyes sparkling with nervousness."
        the_person "W-we could... *whispers* still have some fun together, couldn't we?"
    return

label dandere_sex_beg_finish(the_person):
    the_person "E-eh, um... *whispers* [the_person.mc_title]..."
    "[the_person.title] looks up at you with a shy expression, her eyes sparkling with nervousness."
    the_person "I-I think... *whispers* I'm going to cum soon..."
    "[the_person.title] bites her lower lip, her face flushing with embarrassment."
    the_person "I-it feels... *whispers* really good..."
    the_person "P-please... *whispers* help me finish..."
    return


label dandere_sex_review(the_person, the_report):
    $ comment_position = the_person.pick_position_comment(the_report)
    if comment_position is None:
        return #You didn't actually do anything, no need to comment.
    $ used_obedience = the_report.get("obedience_used", False) #True if a girl only tried a position because you ordered her to.
    $ the_person.draw_person()  # make sure she stands up for talking with you
    #She's worried about her SO finding out because it was in public
    if the_report.get("was_public", False) and the_person.has_significant_other and the_person.opinion.cheating_on_men <= 0: #It was public and she cares.
        if the_person.is_affair: #Dialogue about her being into it, but you can't do this in case she gets caught.
            the_person "E-eh, um... *whispers* that was a bit too much..."
            the_person "W-we should... *whispers* be more careful next time..."
            the_person "S-somebody might... *whispers* see us and tell my [the_person.so_title]..."
        elif used_obedience:
            mc.name "D-don't worry about it... *whispers* people are too busy to notice us..."
            mc.name "T-they won't... *whispers* tell your [the_person.so_title]..."
            the_person "Y-yeah... *whispers* you're right..."
        else:
            $ the_person.call_dialogue("surprised_exclaim")
            the_person "E-everyone's... *whispers* watching us..."
            the_person "I-I hope... *whispers* my [the_person.so_title] doesn't find out..."
            mc.name "N-nobody... *whispers* really cares what we do together..."
            mc.name "Y-you don't... *whispers* need to worry about it..."
            the_person "T-thanks... *whispers* I hope you're right..."
    #She's single, but worried that you did in public.
    elif the_report.get("was_public", False) and (the_person.effective_sluttiness()+10*the_person.opinion.public_sex < comment_position.slut_cap):
        the_person "U-ugh... *whispers* everyone's watching us..."
        if used_obedience:
            the_person "T-they're... *whispers* going to think I'm a huge slut..."
        else:
            mc.name "D-don't worry... *whispers* nobody really cares what we do together..."
            the_person "I-I hope... *whispers* you're right... or I might get a bad reputation..."
    elif the_report.get("girl orgasms", 0) > 2:
        if used_obedience:
            "[the_person.possessive_title!c] smiles at you, still looking a bit dazed."
        else:
            the_person "I-I've... *whispers* never cum that hard before..."
            "She looks up at you with a shy expression, her eyes sparkling with nervousness."
            the_person "Y-you really... *whispers* know how to make a girl feel good..."
            the_person "J-just give me... *whispers* a minute to catch my breath..."
        call sex_review_trance(the_person) from _call_sex_review_trance_dandere_sex_review
    #No special conditions, just respond based on how orgasmed and how slutty the position was.
    elif the_report.get("girl orgasms", 0) > 0 and the_report.get("guy orgasms", 0) > 0: #You both came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position cap, it was tame
            the_person "A-ah... *whispers* that was nice..."
            the_person "I-I didn't... *whispers* expect us to go that far together..."
            the_person "B-but it was... *whispers* kind of exciting..."
        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "A-ah... *whispers* that was really fun..."
            the_person "L-let's do it... *whispers* again sometime soon..."
            the_person "M-maybe we can... *whispers* try something even more exciting next time..."
        elif used_obedience: #She only did it because she was commanded
            the_person "U-um... *whispers* I didn't expect to enjoy that so much..."
            the_person "I-it was... *whispers* really intense..."
            "She looks away, trying to hide her embarrassment."
        else: # She's surprised she even tried that.
            the_person "O-oh my... *whispers* that was unexpected..."
            the_person "I-I didn't... *whispers* think I would ever try something like that..."
            the_person "B-but it... *whispers* felt kind of right in the moment..."
    elif the_report.get("girl orgasms", 0) > 0: #Only she came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            the_person "A-ah... *whispers* that was nice..."
            the_person "B-but it... *whispers* feels a bit anticlimactic when you finish so quickly..."
            the_person "N-next time... *whispers* let's make sure we both cum together, okay?"
        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "A-ah... *whispers* that was really fun..."
            the_person "I-I'll... *whispers* repay the favour next time, okay?"
        elif used_obedience: #She only did it because she was commanded
            the_person "F-fuck... *whispers* I didn't expect to enjoy that so much..."
            the_person "I-it was... *whispers* really intense..."
        else: # She's surprised she even tried that.
            the_person "O-oh my... *whispers* that was unexpected..."
            the_person "I-I didn't... *whispers* think I would ever try something like that..."
            the_person "B-but it... *whispers* felt kind of right in the moment..."
    elif the_report.get("guy orgasms", 0) > 0: #Only you came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            the_person "A-are you... *whispers* all tired out?"
            mc.name "Y-yeah... *whispers* sorry about that..."
            the_person "I-it's... *whispers* okay, I guess..."
            the_person "B-but next time... *whispers* let's make sure we both cum together, okay?"
        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "T-tired out... *whispers* already?"
            mc.name "Y-yeah... *whispers* sorry about that..."
            the_person "I-it's... *whispers* okay, I guess..."
            the_person "B-but next time... *whispers* let's make sure we both cum together, okay?"
        elif used_obedience: #She only did it because she was commanded
            the_person "I-I guess... *whispers* we're done then?"
            mc.name "Y-yeah... *whispers* that's all for now..."
            "She nods, still looking a bit embarrassed."
        else:  # She's surprised she even tried that.
            the_person "W-whew... *whispers* that was intense..."
            the_person "I-I think... *whispers* we should stop before things get out of hand..."
    elif the_person.energy < 10: #Nobody came and she's tired
        the_person "S-sorry... *whispers* I'm just really tired..."
        mc.name "I-it's... *whispers* okay, we can try again later..."
    else: #Nobody came.
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            the_person "Y-you're... *whispers* done already?"
            the_person "I-I thought... *whispers* we were just getting started..."
        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "W-we're... *whispers* stopping already?"
            the_person "I-I wanted... *whispers* to go further..."
            mc.name "I-I'm... *whispers* sorry, [the_person.title]..."
            the_person "I-it's... *whispers* okay, I guess..."
            the_person "B-but next time... *whispers* let's make sure we both cum together, okay?"
        elif used_obedience: #She only did it because she was commanded
            the_person "T-that's... *whispers* all?"
            mc.name "Y-yeah... *whispers* that's all for now..."
            "She nods, still looking a bit embarrassed."
        else:  # She's surprised she even tried that.
            the_person "O-oh... *whispers* maybe we should stop before things get out of hand?"
            the_person "I-I don't... *whispers* want to do anything I might regret later..."
    # Gave creampie while she is not on birth control (extra dialogue when she could get pregnant)
    if the_report.get("creampies", 0) > 0 and not the_person.on_birth_control and not the_person.knows_pregnant:
        the_person "A-ah... *whispers* you really want to see me like this, huh?"
        the_person "P-pregnant... *whispers* with your child..."

    $ del comment_position
    return

## Role Specific Section ##
label dandere_improved_serum_unlock(the_person):
    mc.name "[the_person.title], now that you've had some time to get used to the lab... *whispers* there's something I want to talk to you about."
    the_person "E-eh, um... *whispers* what is it?"
    mc.name "O-our R&D up to this point... *whispers* has been based on my old notes from university."
    mc.name "T-there were some unofficial experiment results... *whispers* that suggested the effects might be enhanced by sexual arousal."
    "[the_person.title] nods her understanding, but hesitates before speaking further, her face flushing with embarrassment."
    the_person "A-ah, s-so you had noticed that too?... *whispers* I have a hypothesis that an orgasm opens chemical receptors that are normally blocked."
    mc.name "W-what else can we do... *whispers* if we assume that is true?"
    mc.name "D-does that open up any more paths... *whispers* for our research?"
    the_person "I-if it's true... *whispers* then perhaps we could experiment with different stimuli to induce arousal in subjects before administering the serum."
    "[the_person.possessive_title!c] fidgets nervously as they consider their own suggestion, her eyes darting around the room."
    the_person "B-but we'll need to... *whispers* do some experiments to be sure, and I don't want to push things too far..."
    mc.name "W-what sort of experiments?"
    the_person "I-I... *whispers* think it would be best if I took a small dose of serum myself first."
    the_person "T-then we can... *whispers* observe my reactions, and see how sexual arousal might affect the results."
    mc.name "D-do you think that's a good idea?"
    the_person "N-not entirely... *whispers* no, but it feels necessary if we want to make any real progress in this area."
    the_person "W-we can't trust anyone else... *whispers* with this information, and I don't want to put you at risk..."
    the_person "B-but there might be... *whispers* a chance for us to catapult our knowledge forward by taking these risks together."
    mc.name "A-alright, let's do it then... *whispers* but please remember that we should proceed with caution and make sure everything is safe."
    return

# label dandere_improved_serum_unlock(the_person):
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
#
label dandere_kissing_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 30:
        "[the_person.title] whispers quietly, her face flushing with embarrassment and excitement: "
        the_person "E-eh, um... *whispers* come on then..."
        the_person "W-we both know... *whispers* where this is going, right?"
        the_person "Y-you've always... *whispers* wanted to kiss me, haven't you?"
    elif the_person.love >= 20:
        "[the_person.title] mumbles softly, avoiding eye contact as she fidgets slightly, her voice barely audible: "
        the_person "S-so... *whispers* we're doing this now?"
        the_person "I-I mean... *whispers* if you really want to..."
        "You smile reassuringly and try not to sound too eager: "
        mc.name "I-I guess so... *whispers* what do you think?"
        "[the_person.title] still hesitant but visibly relieved by your response, her face still flushing with embarrassment: "
        the_person "I-it's... *whispers* about time, I guess..."
        the_person "I-I've wanted... *whispers* to make out with you for a long time..."
    else:
        "[the_person.title] bites her lip and looks away shyly, her voice barely audible: "
        the_person "I-I don't know... *whispers* if this is such a good idea..."
        the_person "A-are we... *whispers* rushing things?"
        "You gently nudge her with understanding and warmth in your tone: "
        mc.name "A-are you... *whispers* scared?"
        "[the_person.title] blushes deeply, avoiding eye contact as she fidgets even more, her voice barely audible: "
        the_person "N-no... *whispers* well, maybe a little..."
        the_person "J-just nervous... *whispers* and excited too..."
        "You smile reassuringly and places a comforting hand on her shoulder: "
        mc.name "T-then just... *whispers* trust me, okay?"
        mc.name "I-I'll... *whispers* take care of you."
    return

label dandere_touching_body_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 30:
        "[the_person.title] whispers softly, her face flushing with embarrassment and excitement: "
        the_person "A-are you... *whispers* sure about this?"
        the_person "I-I don't want... *whispers* you to chicken out on me..."
        "You smile to reassure her and to not sound too eager: "
        mc.name "Oh, I'm... *whispers* sure."
        "[the_person.title] visibly relieved by your response but still hesitant, her voice barely audible: "
        the_person "G-good... *whispers* come on then..."
    elif the_person.love >= 20:
        "[the_person.title] mumbles softly and avoids eye contact as they fidget slightly, her voice barely audible: "
        the_person "S-so... *whispers* you're ready for this?"
        "You nod with a warm smile, trying to be understanding of her nervousness."
        "[the_person.title] still visibly shy but showing hints of anticipation, her face flushing with embarrassment."
        the_person "M-me too... *whispers* I think."
        the_person "I-I didn't think... *whispers* I'd be so nervous when you actually made a move."
        "You gently coax her with reassurance and understanding in your tone: "
        mc.name "Just relax... *whispers* you trust me, right?"
        "[the_person.title] nods hesitantly but clearly trying to convince herself as much as you, her voice barely audible: "
        the_person "O-of course..."
    else:
        "[the_person.title] bites her lip and looks away shyly, her voice barely audible: "
        the_person "I-I think... *whispers* you're getting a little ahead of yourself here, [the_person.mc_title]..."
        "You gently prod her with a tone of curiosity but not pushiness: "
        mc.name "What do you... *whispers* mean?"
        "[the_person.title] still hesitant, eyes darting around nervously, her voice barely audible: "
        the_person "I-I mean... *whispers* I don't just let anyone touch me like that..."
        the_person "M-maybe we... *whispers* should cool things down a bit..."
        "You smile reassuringly and places a comforting hand on her shoulder: "
        mc.name "You're not... *whispers* scared, are you?"
        "[the_person.title] blushes deeply, avoiding eye contact as she fidgets even more, her voice barely audible: "
        the_person "S-scared?... *whispers* of course not..."
        "You chuckle softly and try to make light of the situation while still being understanding: "
        mc.name "Well then... *whispers* just relax and go with it, okay?"
        mc.name "It doesn't... *whispers* have to mean anything unless we want it to."
        "You see her answer in her eyes before she says anything."
        "[the_person.title] mumbles hesitantly, her voice barely audible but clearly showing her inner turmoil: "
        the_person "Y-you're... *whispers* so bad for me, you know that?"
        "You smile warmly and gently pull her closer: "
        mc.name "Well let me... *whispers* make up for it then."
    return

label dandere_touching_vagina_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 35:
        the_person "D-don't... *whispers* chicken out on me now..."
        the_person "Y-you've got... *whispers* your chance to touch my pussy..."
        "[the_person.title] looks up at you with a shy expression, her eyes sparkling with nervousness."
    elif the_person.love >= 20:
        the_person "O-oh... *whispers* fuck..."
        the_person "I-I mean... *whispers* uh, this is a big step for us, [the_person.mc_title]..."
        the_person "I-if you're... *whispers* sure about it, I want you to touch my pussy..."
        "[the_person.title] looks down, her face flushing with embarrassment."
    else:
        the_person "I-I don't... *whispers* know if we should be doing this, [the_person.mc_title]..."
        the_person "I-it feels... *whispers* wrong somehow..."
        mc.name "Hey... *whispers* just take a deep breath and relax, okay?"
        mc.name "I promise... *whispers* it won't hurt too much."
        mc.name "We can... *whispers* stop anytime you want."
        the_person "J-just... *whispers* remember that once we cross this line, there's no going back, [the_person.mc_title]..."
        "[the_person.title] looks up at you with a shy expression, her eyes sparkling with nervousness."
    return

label dandere_sucking_cock_taboo_break(the_person):
    mc.name "I want you to do something for me."
    the_person "E-eh?... *whispers* what do you want me to do to you?"
    mc.name "I want you to suck on my cock."
    if the_person.effective_sluttiness() >= 45:
        the_person "M-mmm... *whispers* I think I'm up for that..."
        the_person "B-but it... *whispers* still makes me nervous..."
        "[the_person.title] bites her lip and looks away from you before taking a deep breath."
        the_person "A-alright... *whispers* let's do this."
        the_person "J-just tell me... *whispers* if it's too much or not what you wanted."
    elif the_person.love >= 30:
        the_person "T-this feels... *whispers* like a natural progression in our relationship..."
        the_person "B-but I... *whispers* can't help feeling shy about it."
        "[the_person.title] bites her lip and looks your body up and down, then takes another deep breath before kneeling down."
    else:
        the_person "O-oh... *whispers* I was wondering if this was going to come up..."
        "[the_person.title] laughs nervously and looks away from you."
        the_person "I-I don't know... *whispers* [the_person.mc_title]..."
        the_person "M-maybe we... *whispers* should talk about it first?"
        mc.name "We can discuss it later, if you want. But for now, just focus on sucking my cock."
        mc.name "But for now... *whispers* just focus on sucking my cock."
        "You reach up and hold her chin, turning her head back to face you."
        the_person "A-alright... *whispers* I'll try my best."
    return

label dandere_licking_pussy_taboo_break(the_person):
    mc.name "I'd really like to taste your pussy [the_person.title]. Are you comfortable with that?"
    if the_person.effective_sluttiness() >= 45:
        the_person "O-oh... *whispers* a man who doesn't expect blowjobs all day..."
        the_person "B-but is... *whispers* willing to try something new."
        "[the_person.title] blushes deeply and looks away shyly."
        the_person "A-alright then... *whispers* I trust you, [mc.name]."
    elif the_person.love >= 30:
        the_person "O-oooh... *whispers* finally a man who doesn't expect blowjobs all day..."
        the_person "B-but never... *whispers* licks a pussy."
        "[the_person.title] bites her lip and smiles at you shyly."
        the_person "A-alright then... *whispers* get to it, lover boy."
    else:
        if the_person.has_taboo("sucking_cock"):
            the_person "H-hmm... *whispers* that's interesting."
            the_person "U-usually it's... *whispers* the other way around with guys like this."
            "[the_person.title] bites her lip and glances at you nervously."
            the_person "W-well... *whispers* I guess if we're going to explore each other's bodies..."
            the_person "W-we should... *whispers* do everything right?"
            "[the_person.title]'s voice trails off as she looks away shyly."
        else:
            the_person "M-most guys... *whispers* think they deserve head all the time."
            the_person "I-it's nice... *whispers* to find someone who wants to return the favor."
            "[the_person.title] blushes deeply and looks down at her hands."
            the_person "A-alright then... *whispers* I trust you, [mc.name]."
    return

label dandere_vaginal_sex_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 60:
        the_person "I-it's... *whispers* about time we did this..."
        the_person "I-I suppose... *whispers* you should, umm, put your thing inside me now..."
        "[the_person.title] looks away, her face flushing with embarrassment."
    elif the_person.love >= 45:
        the_person "A-are you... *whispers* ready for this?"
        the_person "I-I hope... *whispers* you're planning to rock my world."
        mc.name "That is... *whispers* the plan, I hope you can handle it."
        the_person "I-I can... *whispers* handle anything you can throw at me."
        the_person "C-come on then... *whispers* fuck me like you mean it."
        
        the_person "A-are you... *whispers* ready for this?"
        the_person "I-I hope... *whispers* it won't be too much for either of us..."
        mc.name "I will... *whispers* do my best to make sure both of us enjoy it."
        the_person "T-thank you... *whispers* just, please be gentle with me."
    else:
        if the_person.has_taboo("anal_sex"):
            the_person "L-look at... *whispers* that cock..."
            the_person "I-I'm a bit... *whispers* nervous about this, but let's see how it goes..."

        else:
            the_person "I-if your... *whispers* cock feels half as big in my pussy as it did up my ass..."
            the_person "T-then we... *whispers* might be in for an interesting experience."
            the_person "L-let's find... *whispers* out."
    return

label dandere_anal_sex_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 75:
        the_person "O-oh my... *whispers* your cock is enormous!"
        the_person "I-I can't believe... *whispers* you want to put that inside me!"
        mc.name "Don't worry, I'll make sure it feels good for both of us."
        "[the_person.title] looks away, her face flushing with embarrassment."
    elif the_person.love >= 60:
        the_person "A-are you... *whispers* really sure about this?"
        the_person "I-it might... *whispers* hurt a bit..."
        mc.name "I know it might be uncomfortable at first, but I'll take care of you."
        mc.name "But I'll... *whispers* take care of you."
        the_person "A-alright... *whispers* just go slow and gentle with me, okay?"
        "[the_person.title] looks up at you with a shy expression, her eyes sparkling with nervousness."
    else:
        if the_person.has_taboo("vaginal_sex"):
            the_person "I-I don't know... *whispers* if my ass is ready for this!"
            the_person "M-maybe we... *whispers* should try something else first..."
            mc.name "Your pussy might be tight, but I think it can handle me."
            the_person "O-oh... *whispers* alright then."
            the_person "B-but please... *whispers* be gentle!"
        else:
            the_person "I-I'm really... *whispers* nervous about this!"
            the_person "W-what if... *whispers* something goes wrong?"
            mc.name "Trust me, we'll take things slow and make sure you enjoy it."
            the_person "O-okay... *whispers* I guess there's only one way to find out!"
            "[the_person.title] takes a deep breath, her face still flushing with embarrassment."
    return

label dandere_condomless_sex_taboo_break(the_person):
    if the_person.knows_pregnant:
        the_person "Y-you want to... *whispers* have raw sex with me?"
        if the_person.wants_creampie:
            the_person "I-I mean... *whispers* I guess it's okay..."
            the_person "I-if you want to... *whispers* fill my pussy with your cum... then go ahead."
        else:
            the_person "P-please be... *whispers* careful not to cum inside me, alright?"
    elif the_person.opinion.bareback_sex > 0:
        the_person "O-oh, you want to... *whispers* have sex without a condom?"
        the_person "I-I mean... *whispers* it's okay if we both agree on it."
        if the_person.on_birth_control:
            the_person "S-since I'm... *whispers* on the pill, there shouldn't be any risk of pregnancy..."
            the_person "B-but please... *whispers* remember to pull out before you cum."
            $ the_person.update_birth_control_knowledge()
        elif the_person.wants_creampie:
            the_person "I-it would feel... *whispers* so good if you filled me up with your seed..."
            the_person "B-but please... *whispers* make sure we're being safe about it."
            "You feel her pussy muscles squeeze briefly coaxing some more pre-cum out of your cock."
        elif the_person.opinion.creampies < 0:
            the_person "Y-you should... *whispers* really pull out before you cum!"
            the_person "I-I don't want... *whispers* to get pregnant!"
        else:
            the_person "P-please... *whispers* remember to pull out before you cum... it's important."
    elif the_person.love > 60:
        if the_person.on_birth_control:
            the_person "Y-you want to... *whispers* fuck me raw?"
            the_person "I-I'm on... *whispers* the pill, so it should be okay..."
            $ the_person.update_birth_control_knowledge()
        elif the_person.wants_creampie:
            the_person "I-if we're... *whispers* doing this, then... maybe you could go all the way?"
            the_person "I-I mean... *whispers* inside me?"
            mc.name "A-are you... *whispers* on the pill?"
            "She shakes her head."
            the_person "O-oh... *whispers* well, umm... if we're fucking raw like that..."
            $ the_person.update_birth_control_knowledge()
        elif the_person.opinion.creampies < 0:
            the_person "I-I guess... *whispers* it can't be helped then?"
            the_person "Y-you should... *whispers* umm... pull out before you cum?"
        else:
            the_person "I-if we're... *whispers* doing this without protection..."
            if the_person.kids == 0:
                the_person "...y-you need... *whispers* to promise me that you'll pull out."
            elif the_person.kids == 1:
                the_person "...I-I already... *whispers* have one kid, I don't want another."
            else:
                the_person "...I-I have... *whispers* kids already, please be careful."
    else:
        if the_person.on_birth_control:
            the_person "Y-you want to... *whispers* fuck me raw?"
            the_person "W-well... *whispers* I'm on the pill... so it shouldn't be a problem, right?"
            $ the_person.update_birth_control_knowledge()
        elif the_person.has_taboo("vaginal_sex"):
            the_person "U-uh, you... *whispers* don't think we should use a condom?"
            the_person "I-I'm not... *whispers* on the pill... and um, aren't you worried about getting me pregnant?"
            $ the_person.update_birth_control_knowledge()
            the_person "O-or is... *whispers* this some kind of master plan to sneak a baby into my life without asking first?!"
            mc.name "N-no, no!... *whispers* I promise I'll pull out."
            mc.name "W-we can... *whispers* make our special moment even more intimate."
            "She hesitates for a moment before nodding slowly."
            the_person "F-fine... *whispers* but you better really pull out this time, okay?"
            the_person "N-no accidents!"
        else:
            the_person "Y-you don't... *whispers* want to use a condom?"
            the_person "I-I mean... *whispers* I'm not on the pill right now..."
            $ the_person.update_birth_control_knowledge()
            the_person "A-and um... *whispers* aren't you worried about getting me pregnant?"
            mc.name "N-no, no!... *whispers* we can make our special moment even more intimate without a condom."
            the_person "F-fuck..."
            "She bites her lip and looks away for a moment before meeting your eyes again."
            the_person "O-okay... *whispers* but you better really pull out this time."
            the_person "N-no accidents!"
    return

label dandere_underwear_nudity_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > 30 - (the_person.opinion.skimpy_outfits * 5):
        the_person "I-it feels... *whispers* a bit sudden..."
        the_person "B-but if... *whispers* that's what you wish for..."
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "W-what are... *whispers* we waiting for then?"
            mc.name "L-let's get... *whispers* this off of you."
        else:
            mc.name "A-about time?... *whispers* are you forgetting I've seen you naked already?"
            "She shrugs and looks away, her face flushing with embarrassment."
            the_person "I-it's... *whispers* something called fashion, some men are into it."
            the_person "C-come on... *whispers* let's get this off."

    elif the_person.love > 15:
        the_person "Y-you want... *whispers* me to strip down just a little?"
        the_person "I-I was... *whispers* wondering why things were moving so slowly."
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "W-well then... *whispers* let's stop wasting time and get your [the_clothing.display_name] off."

        else:
            mc.name "S-slow?... *whispers* I've already seen you naked, remember?"
            the_person "I-it feels... *whispers* more romantic this way..."
            the_person "I-if that's... *whispers* what you desire..."
            mc.name "W-well... *whispers* let's get more romantic then and get your [the_clothing.display_name] off."

    else:
        the_person "I-if you... *whispers* take my [the_clothing.display_name] off..."
        the_person "I-I'll only... *whispers* have my underwear left on."
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "O-oh, uh... *whispers* well, it is kind of the point, isn't it?"
            "She shakes her head and laughs to herself, her face flushing with embarrassment."
            the_person "A-alright... *whispers* but remember, this is a big step for me..."
        else:
            mc.name "I-I've... *whispers* already seen you naked, so there's no need to worry about it."
            the_person "W-whatever... *whispers* I guess you're right."
            the_person "L-let's just... *whispers* get it over with."
    return

label dandere_bare_tits_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > (40 - the_person.opinion.showing_her_tits * 5):
        the_person "Y-you finally... *whispers* want a look at my tits, [the_person.mc_title]?"
        if the_person.has_large_tits:
            "[the_person.title] shakes her chest for you, jiggling the [the_person.tits_description] hidden underneath her [the_clothing.display_name]."
            "Her cheeks flush with a mix of embarrassment and excitement."
        else:
            "[the_person.title] shakes her chest and gives her [the_person.tits_description] a little jiggle, blushing deeply as she struggles to meet your gaze."
        the_person "W-what took... *whispers* you so long to ask?"
        if the_person.has_large_tits:
            mc.name "No time like the present, right?"
            mc.name "Let's get those puppies out where I can enjoy them."
        else:
            mc.name "No time like the present, right?"
            mc.name "Let's get those cute little melons out."
    elif the_person.love > 25:
        the_person "R-ready to... *whispers* see my tits, [the_person.mc_title]?"
        if the_person.has_large_tits:
            "[the_person.title] shakes her chest and jiggles her nice [the_person.tits_description], barely restrained by her [the_clothing.display_name]."
            "Her eyes dart around nervously, not quite meeting yours."
        else:
            "[the_person.title] shakes her chest, giving her [the_person.tits_description] a little jiggle, and looks away quickly as if she's afraid you might notice how excited it makes her."
        mc.name "Oh yeah... *whispers* I'm ready."
        the_person "L-let 'em... *whispers* out then, and have fun."
    else:
        the_person "W-wait a... *whispers* second!"
        the_person "J-jesus, you... *whispers* should at least ask a girl before you try and put her tits on full display."
        mc.name "Come on... don't you want to show them off?"
        mc.name "I bet... they look great."
        the_person "O-oh, they... *whispers* do."
        the_person "I-I just... *whispers* feel a little self-conscious about being naked around you, alright?"
        mc.name "There's no need to be, just relax and let me take your [the_clothing.display_name] off for you."
        the_person "O-oh man... *whispers* what are you getting me into, [the_person.mc_title]?"
        the_person "F-fine... *whispers* let's do it!"
    return

label dandere_bare_pussy_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > (50 - the_person.opinion.showing_her_ass * 5):
        "She blushes and looks down while fidgetting with her hands"
        the_person "...D-do it..."
    elif the_person.love > 35:
        "She looks up, then quickly looks away"
        the_person "I-I... think I'm ready..."
        if the_person.has_taboo("touching_vagina"):
            mc.name "I want to see you."
            "She nervously nods and barely whispers..."
            the_person "O-okay..."
        else:
            mc.name "I've already touched it. Now I want to see it."
            "She blushes and looks down while fidgetting with her hands"
            the_person "I-I know..."
    else:
        "She quickly looks away and stammers"
        the_person "I-I... d-don't know..."
        if the_person.has_taboo("touching_vagina"):
            mc.name "I want to take your [the_clothing.display_name] off."
            "First she nods then shakes her head and whispers..."
            the_person "A-ask me nicely..."
            mc.name "[the_person.title], may I please take your [the_clothing.display_name] off and see your pussy?"
            "Smiles briefly, blushes, looks up at you, then quickly looks away while nodding..."
            the_person "Y-yes..."
        else:
            mc.name "I've already felt it up. Now I want to see it."
            "She fidgets with her hands and looks down, embarrassed and mumbles quietly"
            the_person "D-do it..."
    return

# label dandere_facial_cum_taboo_break(the_person):

#     return

# label dandere_mouth_cum_taboo_break(the_person):

#     return

# label dandere_body_cum_taboo_break(the_person):

#     return
#
# add more dandere personality, use different words, and movements.

label dandere_creampie_taboo_break(the_person):
    if the_person.wants_creampie:
        if the_person.knows_pregnant:
            "She looks down, while blushing furiously"
            the_person "...I-I want it..."
            "She bites her lip and nods softly."
        elif the_person.on_birth_control:
            if the_person.has_significant_other:
                the_person "*whispers* I'm s-so sorry... but it feels... really good..."
                the_person "*looks away, embarrassed* H-he wouldn't understand... but I c-can't help myself..."
            else:
                the_person "*looks down, fidgeting* I-I know it's wrong... but it feels... amazing..."
        elif the_person.effective_sluttiness() > 75 or the_person.opinion.creampies > 0:
            if the_person.has_significant_other:
                the_person "*nervously smiles* I-I've wanted this... for so long..."
                the_person "*looks away, blushing* I'm a t-terrible [the_person.so_girl_title]... but I c-can't resist..."
            else:
                the_person "*peeks up, then looks away* I-I've wanted... a good creampie... for so long..."
                the_person "*nervously nods* P-please... give me more..."
            "She sighs happily, still looking away."
            the_person "*whispers* H-how long... until you're ready... again?"
        else:
            if the_person.has_significant_other:
                the_person "*looks down, embarrassed* O-oh no... I'm s-such a terrible [the_person.so_girl_title]..."
                "She sighs happily, still looking down."
                the_person "*whispers* I-I shouldn't have... let this happen... but it felt... too good..."
            else:
                "She looks away and fidgets"
                the_person "O-oh no... that was... so r-risky..."
                "She sighs happily, still looking away."
                the_person "*whispers* I-I hope... my luck... holds out..."
    else:
        if the_person.knows_pregnant:
            the_person "*looks up, shocked* O-oh no... you c-came inside me..."
        elif not the_person.on_birth_control:
            the_person "*looks worried* U-uh... did you... cum in me?"
            if the_person.has_significant_other:
                the_person "*looks down, embarrassed* W-what if... I'm p-pregnant now?"
            else:
                the_person "*looks away, fidgeting* I-I don't think... I'm r-ready... for that..."
            the_person "*nervously nods* P-please... let's use... condoms... from now on..."
        elif the_person.has_significant_other:
            the_person "*looks away, blushing* Y-you really... went ahead... and creampied me?"
            "She looks down, embarrassed."
            the_person "*whispers* M-maybe... next time... we should... wear condoms..."
        elif the_person.opinion.creampies < 0:
            the_person "*shudders* O-oh no... I d-didn't want... this to happen..."
            "She looks away, trying to hide her discomfort."
            the_person "*whispers* C-couldn't you... have cum... somewhere else?"
        else:
            the_person "*pouts* H-hey... we agreed... to pull out..."
            "She looks away, her voice barely audible."
            the_person "*whispers* I-I guess... can you... try not to... do that again?"
    return

label dandere_anal_creampie_taboo_break(the_person):
    if the_person.opinion.anal_creampies > 0:
        if the_person.effective_sluttiness() > 75 or the_person.opinion.anal_creampies > 1:
            if the_person.has_significant_other:
                the_person "*bites her lip and whispers* I don't care who knows... just make me feel it..."
                "[the_person.title] mumbles under her breath as she looks down at her hands..."
                the_person "It's... nice. Inside me."
                "She twitches slightly"
            else:
                "She blushes deeply and stammers..."
                the_person "Y-you should've done this sooner..."
                "[the_person.title] covers her face with her hands and peeks through her fingers, whispering, "
                the_person "I like it when you... fill me up..."
        else:
            if the_person.has_significant_other:
                "She glances around nervously and whispers..."
                the_person "I shouldn't be doing this..."
                "[the_person.title] leans in close, looking down and fidgeting with her hands as she whispers..."
                the_person "But my [the_person.so_title] never... so maybe it's okay?"
            else:
                "[the_person.title] giggles nervously and covers her mouth with her hand as she whispers..."
                the_person "It feels... wrong, but good."
                "She blushes deeply."
    else:
        if the_person.has_significant_other:
            "[the_person.title] frantically panics and grabs your arm and whispers..."
            the_person "[the_person.mc_title], I told you to pull out! My [the_person.so_title] will see!"
            "She looks around nervously..."
            the_person "N-next time, just... just do it on my ass, okay?"
        elif the_person.opinion.anal_creampies < -1:
            "[the_person.title] mumbles under her breath as she looks away embarrassed, and finally whispers..."
            the_person "It's just... so embarrassing."
            "She covers her face with her hands."
        else:
            the_person "*stammers* N-not inside, [the_person.mc_title]! My ass isn't... a sperm bank or anything..."
            "[the_person.title] blushes deeply and giggles nervously as looks down at her hands. She fidgets with them and whispers..."
            the_person "I-It's just... really personal, you know?"
    return

label dandere_dual_penetration_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 75:
        the_person whispers "I-I don't know if I can handle this... it's just so... big."
        "[the_person.title] fidgets with her hands, her voice barely above a whisper, "
        the_person "But at the same time... it feels kind of... exciting?"
        mc.name "Don't worry, you'll be fine. Just relax."
        "[the_person.title] nods slightly, still looking away, "
        the_person "I-I trust you..."
    elif the_person.love >= 60:
        the_person "*whispers* D-do you really want to do this? It might... hurt."
        mc.name "I'll be gentle, I promise. It'll feel good, I'll make sure of it."
        "She looks up, her eyes wide with concern.."
        the_person "P-promise me you won't... break anything."
        mc.name "I promise, I'll be careful."
        "She nods, but still looks worried."
        the_person "O-okay... let's do this then..."
    else:
        if the_person.has_taboo("vaginal_sex"):
            "[the_person.title] looks away, blushing and leans close to whisper..."
            the_person "I-I don't know if my... pussy can handle it. Maybe my ass isn't... ready?"
            mc.name "I'll make it work, don't worry."
            "[the_person.title] looks down, her voice barely above a whisper..."
            the_person "O-oh no..."
        else:
            "[the_person.title] takes a deep breath, her eyes closed and whispers to herself..."
            the_person "I can do this... I think."
            mc.name "Yeah, you can. Just remember, we're doing something naughty here."
            "[the_person.title] opens her eyes, looking up at you, she nervously whispers..."
            the_person "I-I know... it's just... new."
            mc.name "Well, no time like the present then. Do it, before you change your mind!"
            the_person "O-okay... let's do this then..."
    return

label dandere_sleepover_yourplace_response(the_person): 
    if the_person.sluttiness < 80:
        the_person "Y-yes... that sounds... fun..."
        "[the_person.title] fidgets with her hands, avoiding eye contact, "
        the_person "I-I'll, uh, bring my stuff... "
        "She gets nervously excited and looks away, trying to hide a smile"
    else:
        the_person "I-I'd like that... "
        "[the_person.title] pauses, choosing her next words carefully."
        the_person "I'll, uh, make sure to bring everything I need..." 
        "She looks away, her face turning bright red."
        "[the_person.title] takes a deep breath, trying to calm herself down, "
        the_person "I-I mean... it'll be a sleepover..."
        "She nervously laughs and looks away again."
    return

label dandere_sleepover_herplace_response(the_person): 
    if the_person.sluttiness < 80:
        the_person "C-come over... if you want..."
        "[the_person.title] plays with the hem of her clothes, her eyes cast downward, "
        the_person "I'll... try to be a good host... I think..."
    else:
        the_person "M-my place is... pretty messy... but you can come over..."
        "[the_person.title] tucks a strand of hair behind her ear, her face growing hot, "
        the_person "I-I'll... clean up a bit... if you promise not to... laugh at me..."
    return

label dandere_sleepover_yourplace_sex_start(the_person): 
    "[the_person.title] hesitantly enters the room, her eyes fixed on the floor as she fidgets with the hem of her clothes."
    "[the_person.title] stops in front of you, her hands clasped together in front of her, and whispers almost inaudibly, "
    the_person "D-do I... need to do anything...?"
    "[the_person.title] peeks up at you, her face reddening as she quickly looks away again, "
    return

label dandere_sleepover_herplace_sex_start(the_person): 
    "[the_person.title] stands by the bed, her back to you as she fidgets with the bed sheets, "
    the_person "Y-you can... come over here... if you want..."
    "You approach her, and she turns around, her eyes cast downward, "
    "[the_person.title] takes a step back, her hands clasped together in front of her, and whispers, "
    the_person "I-I'll... show you... where everything is..."
    "[the_person.title] gestures vaguely towards the bed, her face growing hot, "
    return

label dandere_sleepover_impressed_response(the_person): 
    "[the_person.title] covers her mouth with her hand, her eyes wide with surprise, "
    the_person "W-wait... I think I need a minute..."
    "[the_person.title] takes a few deep breaths, her face still flushed, "
    the_person "Y-you're... really good at this..."
    $ the_person.draw_person(position = "missionary")
    "[the_person.title] looks away, her voice barely above a whisper, "
    the_person "I-I didn't know it could feel like that..."
    "[the_person.title] lies down in bed, still trying to catch her breath, and whispers, "
    the_person "I-I think I might need a little while... before we do that again..."
    return

label dandere_sleepover_good_response(the_person): 
    "[the_person.title] turns her face away, her ears turning bright red, "
    $ the_person.draw_person(position = "missionary")
    the_person "I-I think that was... okay..."
    "[the_person.title] lies down in bed, pulling the covers up to her chin, and whispers, "
    the_person "Y-you're... pretty good, I guess..."
    "[the_person.title] looks up at you with a shy smile, her eyes quickly darting away again, "
    the_person "I-I might need a little while... before we do that again..."
    return

label dandere_sleepover_bored_response(the_person): 
    "[the_person.title] looks away, her face slightly flushed, "
    the_person "I-I don't know... if this is... working..."
    "[the_person.title] fidgets with her hands, her voice barely above a whisper, "
    the_person "M-maybe you could... try something else..."
    "[the_person.title] glances up at you, her eyes quickly darting away again, as she subtly shifts her hips, "
    "[the_person.title] starts to nervously play with her hair, her body language hinting that she's waiting for something more."
    return

# add more dandere personality, use different words, and movements.
# update all the following the_person and movements with dandere personality. Use Shouko Komi from Komi Can't Communicate for ideas, keep to the structure. Movements in quotations:

