### PERSONALITY CHARACTERISTICS ###
# Bimbo is slang for a conventionally attractive, sexualized naïve woman. The term was originally used in the United States as early as 1919 for an unintelligent or brutish man. As of the early 21st century, the "stereotypical bimbo" appearance became akin to that of a physically attractive woman.
#However, as with most identities, the idea of the 'bimbo' has evolved and here is what it means today. The term 'bimbofication' is a colloquial term derived from the term 'bimbo' which is understood to mean, 'an attractive woman who is pretty, sexualised, naive and uneducated'.
#==================================================================
# add more slutty personality, use different words, and movements.
# update all the following the_person and movements with slutty personality. Use Panty Anarchy from Panty & Stocking with Garterbelt or Naruko Yokoshima from Seitokai Yakuindomo, for ideas, keep to the structure. Movements in quotations:
### DIALOGUE ###
# Anna Nishikinomiya from Shimoneta
# Kyousuke Yaguchi from Yarichin Bitch Club
# Ayame Kajou - Blue Snow

label slutty_introduction(the_person):
    mc.name "Hey, can I talk to you for a sec?"
    "[the_person.title] turns around, a sultry smile spreading across her face as she runs her hands over her hips, accentuating her curves."
    the_person "Oh, finally. I was starting to think you were too chicken to come over and talk to me. But now that you're here, I have to say, you're looking pretty good."
    mc.name "I'm sorry if this is awkward, but you seem like a really interesting person."
    "[the_person.title] raises an eyebrow, a flirtatious glint in her eye as she leans in close, her breasts almost touching your chest."
    the_person "Interesting? That's cute. You want to get to know me, huh? Well, I'm not sure if you can handle me, but I'm willing to give you a shot."
    mc.name "Well, I was wondering if you'd like to... do something together sometime."
    "[the_person.title] lets out a throaty laugh, her eyes sparkling with amusement as she tosses her hair over her shoulder, exposing her neck and shoulder."
    the_person "Oh, baby, I'm always up for a good time. What did you have in mind? Something naughty, I hope?"
    mc.name "Haha, well, maybe we could grab coffee or something?"
    "[the_person.title] pouts, her lips curling into a playful smirk as she teases you, her eyes sparkling with mischief."
    the_person "Coffee? That's so boring. How about we do something a little more... exciting? Like, maybe, a night in bed together?"
    mc.name "Heh, I don't know... what did you have in mind?"
    "[the_person.title] leans in close, her voice dropping to a sultry whisper as she breathes in your ear, her hot breath sending shivers down your spine."
    the_person "I have a few ideas. But I think we should get to know each other a little better first, don't you? Maybe we can start with a kiss, and see where things go from there?"
    mc.name "Uh, yeah... that sounds good, I guess."
    $ the_person.set_title()
    $ the_person.set_possessive_title()
    the_person "So, what's your name, anyway? I want to know what to scream when we're in bed together."
    mc.name "I'm [mc.name]. Nice to meet you..."
    the_person "I'm [the_person.name]. Nice to meet you too, baby. And don't worry, I'll make sure you remember my name, and my body, for a long time."
    $ the_person.change_happiness(2)
    return

label slutty_greetings(the_person):
    if the_person.love < 0:
        the_person "Ugh, what do you want now? Can't you see I'm busy getting myself off?"
        "[the_person.possessive_title!c] rolls her eyes and crosses her arms, clearly annoyed, but with a hint of a smirk on her face."
    elif the_person.happiness < 90:
        the_person "Hey, I guess. I'm still having a pretty crappy day, but you're here now, so maybe you can help me take my mind off things... with your cock, that is."
        "[the_person.possessive_title!c] shrugs and looks away, her expression sulky, but with a hint of a smile on her face."
    else:
        if the_person.sluttiness > 60:
            if the_person.obedience > 180:
                the_person "Oh, it's you. I was hoping you'd show up. I've been feeling a little... horny lately, and I need someone to take care of me."
                "[the_person.possessive_title!c] bats her eyelashes and smiles, her voice husky with suggestion, as she runs her hands over her body, accentuating her curves."
            else:
                the_person "Hey there, [the_person.mc_title]. I'm not really in the mood for games today, so let's just get to it, okay? I want to feel your cock inside me, and I want it now."
                "[the_person.possessive_title!c] raises an eyebrow and looks you up and down, her expression confident and flirtatious, as she takes a step closer to you, her body almost touching yours."
        else:
            if the_person.obedience > 180:
                the_person "Hi, [the_person.mc_title]. What can I do for you today? I'm feeling a little... adventurous, and I was thinking maybe we could try something new... like anal, or maybe even a threesome."
                "[the_person.possessive_title!c] smiles and leans in close, her voice barely above a whisper, as she runs her hands over your body, teasing you with her touch."
            else:
                the_person "Hey, what's up? Don't tell me you're here to bother me again with your silly questions and awkward small talk. I'm not in the mood for that, but I am in the mood for something else... something a little more... physical."
                "[the_person.possessive_title!c] rolls her eyes and sighs, her expression exasperated, but with a hint of a smile on her face, as she takes a step closer to you, her body almost touching yours."
    return

label slutty_sex_responses_foreplay(the_person):
    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] moans loudly and wraps her legs around you, pulling you in close as she grinds her pussy against your hand."
            the_person "Oh, fuck yeah. That's it. Right there. Don't stop, baby. I'm getting so wet."
        else:
            "[the_person.possessive_title!c] moans softly and looks up at you with a mixture of surprise and pleasure as she starts to get into it."
            the_person "Mmm, this is actually kind of nice. I didn't expect to be so turned on by your touch."

    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            the_person "Mmm, yeah. That feels so good. Don't stop, [the_person.mc_title]. Please don't stop. I'm getting so close to cumming."
            "[the_person.possessive_title!c] starts to grind against you, her hips moving in time with your touch as she starts to lose control."
        else:
            the_person "I... I think I might actually be enjoying this. Which is weird, because I didn't think I would be into this sort of thing."
            "[the_person.possessive_title!c] looks up at you with a mixture of confusion and arousal as she starts to get more and more turned on."

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            the_person "Oh, god. Yeah. That's it. I'm going to cum if you keep doing that. I can feel it building up inside me."
            "[the_person.possessive_title!c] starts to tremble and shake, her body on the verge of orgasm as she starts to lose control."
        else:
            the_person "I... I think I might be getting close. Which is weird, because I didn't think I would be into this sort of thing."
            "[the_person.possessive_title!c] looks up at you with a mixture of surprise and arousal as she starts to get more and more turned on."

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "Mmm, yeah. That feels so good. I'm going to cum all over your face if you keep doing that. I want to feel your tongue on my clit."
            "[the_person.possessive_title!c] starts to grind against you, her hips moving in time with your touch as she starts to lose control."
        else:
            the_person "I... I think I might actually be enjoying this. Which is weird, because I didn't think I would be into this sort of thing."
            "[the_person.possessive_title!c] looks up at you with a mixture of confusion and arousal as she starts to get more and more turned on."

    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                the_person "Oh, god. Yeah. I'm going to cum. And it's all because of you, [the_person.mc_title]. You're so good at this."
                "[the_person.possessive_title!c] starts to tremble and shake, her body on the verge of orgasm as she starts to lose control."
            else:
                the_person "The way you touch me is just... different, I guess. It's like you actually know what you're doing. You're so much better than my boyfriend."
                "[the_person.possessive_title!c] looks up at you with a mixture of surprise and arousal as she starts to get more and more turned on."
        else:
            the_person "I... I think I might actually be enjoying this. Which is weird, because I didn't think I would be into this sort of thing."
            "[the_person.possessive_title!c] looks up at you with a mixture of confusion and arousal as she starts to get more and more turned on."

    return

label slutty_sex_responses_oral(the_person):
    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] spreads her legs wide, a dirty grin spreading across her face."
            the_person "Oh, baby, you want to eat my pussy? Well, I'm not going to stop you... in fact, I'm going to make you do it harder."
        else:
            "[the_person.possessive_title!c] looks up at you, her eyes sparkling with curiosity and a hint of mischief."
            the_person "Hmmm, I wonder what you're going to do down there... are you going to make me cum with your tongue?"

    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            the_person "Mmm, yeah, that feels so fucking good... don't stop, [the_person.mc_title], I'm getting so close to cumming."
            "[the_person.possessive_title!c] starts to grind against your face, her hips moving in time with your tongue as she starts to lose control."
        else:
            the_person "Oh, wow, you're actually kind of good at this... who knew you had such a talented tongue?"
            "[the_person.possessive_title!c] giggles, her body relaxing into the sensation as she starts to get more and more turned on."

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            the_person "Hmmm, yeah, that's the spot... right there, baby, don't stop, I'm going to cum all over your face."
            "[the_person.possessive_title!c] starts to moan, her body trembling with pleasure as she starts to lose control."
        else:
            the_person "Alright, alright, you're pretty good at this... but don't think this means I'm going to go easy on you, I'm still going to make you work for it."
            "[the_person.possessive_title!c] smiles, her eyes glinting with mischief as she starts to get more and more turned on."

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "Mmm, yeah, I'm going to cum... and it's all because of you, [the_person.mc_title], you're so good at eating my pussy."
            "[the_person.possessive_title!c] starts to shake, her body on the verge of orgasm as she starts to lose control."
        else:
            the_person "Wow, you're really good at this... I think I might actually be enjoying myself, which is weird, because I didn't think I would be into this sort of thing."
            "[the_person.possessive_title!c] looks up at you, her eyes sparkling with surprise and a hint of arousal."

    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                the_person "Oh, wow... I think I just came... thanks to you, [the_person.mc_title], you're so good at making me cum."
                "[the_person.possessive_title!c] smiles, her body relaxing into the afterglow as she starts to feel satisfied."
            else:
                the_person "Mmm, maybe I should let you do that more often... when [the_person.so_title] isn't around, of course, because I don't want to cheat on them, but I do want to cheat with you."
                "[the_person.possessive_title!c] winks, her eyes glinting with mischief as she starts to feel more and more attracted to you."
        else:
            the_person "Ugh, fine, you win... I guess I did enjoy that after all, which is weird, because I didn't think I would be into this sort of thing."
            "[the_person.possessive_title!c] rolls her eyes, her expression playful and a hint of arousal."

    return

label slutty_sex_responses_vaginal(the_person):
    if the_person.energy < 10:
        call low_energy_sex_responses_vaginal(the_person) from _vt_slutty_call_low_energy_sex_responses_vaginal_10
        return
    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            $ play_moan_sound()
            "[the_person.possessive_title!c] spreads her legs wide and arches her back, her hips bucking against yours as she takes your cock deep inside her."
            the_person "Oh, fuck yeah... that feels so good... don't stop, baby, I'm getting so wet!"
        else:
            "[the_person.possessive_title!c] bites her lip and looks up at you with a sultry gaze, her eyes sparkling with desire."
            the_person "Mmm, you're not bad... but I think I can handle a little more... harder, faster, deeper!"

    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            the_person "Oh, god... yeah, keep going... I love the way you're making me feel! You're so big and hard inside me!"
            "[the_person.possessive_title!c] starts to grind against you, her hips moving in time with yours as she takes your cock deeper and deeper."
        else:
            the_person "Hmmm, you're pretty good... but I think I need a little more convincing... show me what you've got, baby!"

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            the_person "Mmm, yeah... that's the spot... right there, baby! You're hitting my G-spot, oh god!"
            "[the_person.possessive_title!c] starts to moan and tremble, her body on the verge of orgasm as she takes your cock deeper and deeper."
        else:
            the_person "Oh, wow... you're really good at this... I think I might actually be enjoying myself... who knew I was such a slut?"

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "Yeah, baby... I'm going to cum... and it's all because of you! You're the best fuck I've ever had!"
            "[the_person.possessive_title!c] starts to shake and tremble, her body on the verge of orgasm as she takes your cock deeper and deeper."
        else:
            the_person "Hmmm, I think I might actually be getting close... thanks to you, [the_person.mc_title]... you're really good at this."

    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                the_person "Oh, god... yeah, I'm cumming... thanks to you, baby! You're the best fuck I've ever had!"
                "[the_person.possessive_title!c] arches her back and moans loudly, her body trembling with pleasure as she takes your cock deeper and deeper."
            else:
                the_person "Mmm, yeah... I think I'm going to cum... and it's all because of you, [the_person.mc_title]... you're so good at making me feel like a slut."
                "[the_person.possessive_title!c] looks up at you with a sultry gaze, her eyes sparkling with pleasure as she takes your cock deeper and deeper."
        else:
            the_person "Hmph, I suppose I'm almost there... thanks to you, [the_person.mc_title]... you're really good at this, I have to admit."
            "[the_person.possessive_title!c] looks up at you with a mixture of surprise and pleasure, her eyes sparkling with desire."
    return

label slutty_sex_responses_anal(the_person):
    if the_person.energy < 10:
        call low_energy_sex_responses_anal(the_person) from _vt_slutty_call_low_energy_sex_responses_anal_10
        return

    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            the_person "Mmm, baby... I'm so ready for this. Fuck my ass hard and deep!"
            "[the_person.possessive_title!c] looks up at you with a sultry gaze, her eyes sparkling with desire."
        else:
            $ the_person.call_dialogue("teasing_exclaim")
            the_person "Hehe, you want to stick it in my ass? Well, I suppose I can handle a big cock like yours..."
            "[the_person.possessive_title!c] winks, her expression playful and flirtatious."

    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            $ the_person.call_dialogue("surprised_exclaim")
            the_person "Wow, this is... actually kind of nice. Your cock feels so good in my ass!"
            "[the_person.possessive_title!c] squirms a bit, trying to get used to the sensation, but a smile spreads across her face."
        else:
            the_person "Mmm, this is... interesting. I never knew anal could feel so good..."

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            the_person "Oh, yeah... keep going... I love the way you're fucking my ass!"
            "[the_person.possessive_title!c] starts to moan and grind against you, her hips moving in time with yours."
        else:
            the_person "Hmmm, this is... actually kind of nice. I think I might be enjoying myself..."

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            if mc.condom:
                the_person "Mmm, yeah... I love the way you're making me feel... even with a condom on, your cock is so big and hard!"
            else:
                the_person "Oh, baby... I can feel you so deep inside me... it's amazing... your bare cock is so hot!"
        else:
            the_person "Hmmm, I think I might actually be getting close... thanks to you, [the_person.mc_title]..."

    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                the_person "Oh, god... yeah, I'm cumming... thanks to you, baby! Your cock is so amazing!"
                "[the_person.possessive_title!c] arches her back and moans loudly, her body trembling with pleasure."
            else:
                the_person "Mmm, yeah... I think I'm going to cum... and it's all because of you, [the_person.mc_title]... your cock is so big and hard, it's driving me crazy!"
                "[the_person.possessive_title!c] looks up at you with a sultry gaze, her eyes sparkling with pleasure."
        else:
            $ the_person.call_dialogue("teasing_exclaim")
            the_person "Hehe, I think I might actually be enjoying myself... thanks to you, [the_person.mc_title]... your cock is so nice and big, it's making me feel so good!"
            "[the_person.possessive_title!c] winks, her expression playful and flirtatious."

    return

label slutty_climax_responses_foreplay(the_person):
    if the_person.sluttiness > 50:
        the_person "Oh, fuck me already! I need to cum so bad!"
        "[the_person.possessive_title!c] starts to squirm and grind against you, desperate for release."
    else:
        the_person "Why do you always have to tease me like this? Just make me cum already!"
        "[the_person.possessive_title!c] huffs, clearly on the verge of climax, her body tense with anticipation."
    return

label slutty_climax_responses_oral(the_person):
    if the_person.sluttiness > 70:
        the_person "Oh, god, your tongue is so good! I'm going to cum all over your face!"
        "[the_person.possessive_title!c] starts to moan and grind against your face, her hips moving in time with your tongue."
    else:
        the_person "Mmm, you're so good at this... I didn't think I'd... I'm going to cum... oh, yeah!"
        "[the_person.possessive_title!c] starts to tremble and shake, her body on the verge of orgasm, her voice barely above a whisper."
    return

label slutty_climax_responses_vaginal(the_person):
    if the_person.sluttiness > 70:
        if the_person.arousal_perc > 120:
            the_person "Fine, I'll cum. But don't think this means I'm not going to want more... I'm a slut, after all!"
            "[the_person.possessive_title!c] grits her teeth and squeezes her eyes shut, her body tense with pleasure."
        else:
            the_person "Ugh, just a little more... I'm... Ah, fuck! I'm going to cum so hard!"
            "[the_person.possessive_title!c] starts to moan and grind against you, her hips moving in time with yours, her body on the verge of orgasm."
    else:
        the_person "Oh... I can't... I'm going to... Ah! Oh, god, I'm cumming!"
        "[the_person.possessive_title!c] starts to tremble and shake, her body on the verge of orgasm, her voice barely above a whisper."
    return

label slutty_climax_responses_anal(the_person):
    if the_person.sluttiness > 70:
        if the_person.arousal_perc > 120:
            the_person "Fine, you win. I'll cum. But don't think I'm not going to want more... I love being fucked in the ass!"
            "[the_person.possessive_title!c] squeezes her eyes shut, trying to fight off the pleasure, but her body betrays her, cumming hard."
        else:
            the_person "Ugh, just a little more... My ass is going to... Ah! Oh, god, I'm cumming!"
            "[the_person.possessive_title!c] starts to moan and grind against you, her hips moving in time with yours, her body on the verge of orgasm."
    else:
        the_person "Oh... My... Ass... I... Ah! Oh, god, I'm cumming so hard!"
        "[the_person.possessive_title!c] barely finishes her sentence before her body is racked with pleasure, cumming hard and fast."
    return

label slutty_clothing_accept(the_person):
    if the_person.obedience > 180:
        the_person "Mmm, I love dressing up like a slut for you. It makes me feel so dirty and naughty."
        "[the_person.possessive_title!c] gives you a sultry smile, her eyes sparkling with desire."
    else:
        the_person "Yeah, whatever. I'll wear this slutty outfit for you, but don't expect me to be all prim and proper."
        "[the_person.possessive_title!c] rolls her eyes, but can't help smiling at the thought of dressing up like a slut."
    return

label slutty_clothing_reject(the_person):
    if the_person.should_wear_uniform:
        the_person "Ugh, fine. I'll put on my uniform. But can I at least wear some slutty underwear underneath?"
        "[the_person.possessive_title!c] pouts, but starts to get changed into her uniform."
    elif the_person.obedience > 180:
        the_person "I don't... I'm sorry, but I really don't think I could get away with wearing something like this. It's just too revealing... but I love the way you look at me when I'm dressed like a slut."
        "[the_person.possessive_title!c] blushes, but can't help feeling a little turned on at the thought of dressing up like a slut."
    else:
        if the_person.sluttiness > 60:
            the_person "Hmm, I don't know about this one. It's a bit too revealing for my taste... but I love the way it makes me feel like a dirty little slut."
            "[the_person.possessive_title!c] gives you a sultry smile, her eyes sparkling with desire."
        else:
            the_person "You've got to be kidding me, right? This is ridiculous. I'm not wearing this... but maybe I'll wear something even sluttier instead."
            "[the_person.possessive_title!c] rolls her eyes, but can't help laughing at the thought of dressing up like a slut."
    return

label slutty_clothing_review(the_person):
    if the_person.outfit.cum_covered:
        if (the_person.sluttiness > 40 and the_person.opinion.being_covered_in_cum >=0) or the_person.opinion.being_covered_in_cum > 0:
            the_person "Mmm, I love being covered in cum. It's so dirty and naughty... and it makes me feel like such a slut."
            "[the_person.possessive_title!c] starts to wipe up the biggest splashes of cum on her, but can't help smiling at the thought of being covered in cum."
        else:
            the_person "For fuck's sake, I need to clean up this mess! But maybe I'll just leave a little bit of cum on me... it's not like I'm going to be wearing any panties anyway."
            "[the_person.possessive_title!c] wipes herself down, cleaning up all the cum she can find, but leaves a little bit on her skin to remind her of the dirty things she's been up to."

    if the_person.obedience > 180:
        the_person "Fine, I'll be back in a moment. I need to get cleaned up for you... and maybe put on something even sluttier."
        "[the_person.possessive_title!c] gives you a sultry smile, her eyes sparkling with desire."
    else:
        if the_person.sluttiness > 40:
            the_person "I don't know why I do this, but I want to look good for you. I'll be back in a second, I just want to get cleaned up and put on something that will make you hard."
            "[the_person.possessive_title!c] gives you a sultry smile, her eyes sparkling with desire."
        else:
            the_person "Ugh, everything's such a mess after that. Wait here a moment, I'm just going to find a mirror and try and look somewhat presentable... but maybe I'll just wear something slutty instead."
            "[the_person.possessive_title!c] rolls her eyes, but can't help laughing at the thought of dressing up like a slut."
    $ the_person.apply_planned_outfit(show_dress_sequence = True)
    return

label slutty_strip_reject(the_person, the_clothing, strip_type = "Full"):
    if the_person.obedience > 180:
        the_person "Oh, baby, can't we just leave my [the_clothing.display_name] on for now? I want to tease you a little longer..."
        "[the_person.possessive_title!c] gives you a sultry smile, her eyes sparkling with desire."
    elif the_person.obedience < 70:
        the_person "No way, I'm not taking anything off until I'm good and ready. And even then, it's going to be on my terms, not yours."
        "[the_person.possessive_title!c] crosses her arms over her chest, a defiant look on her face."
    else:
        the_person "Not yet, baby... I want to make you wait a little longer. But trust me, it'll be worth it."
        "[the_person.possessive_title!c] gives you a sly smile, her eyes sparkling with mischief."
    return

label slutty_strip_obedience_accept(the_person, the_clothing, strip_type = "Full"):
    "[the_person.title] laughs nervously as you start to slide her [the_clothing.display_name] away, but she doesn't stop you."
    if the_person.obedience > 180:
        the_person "Oh, yeah... take it off. I want to feel your hands all over me."
        "[the_person.possessive_title!c] closes her eyes, her body trembling with anticipation."
    else:
        the_person "I don't know if this is a good idea, but I'm going to let you do it anyway. Because I'm a slut, and I love it."
        "[the_person.possessive_title!c] gives you a sultry smile, her eyes sparkling with desire."
    return

label slutty_grope_body_reject(the_person):
    if the_person.effective_sluttiness("touching_body") < 5: #Fail point for touching shoulder
        the_person "Hey, watch it! Don't think you can just touch me wherever you want."
        "[the_person.title] steps back as you touch her, then crosses her arms over her chest."
        the_person "If you want to touch me, you're going to have to do better than that."
        mc.name "Oh, sorry. I didn't mean to make you feel that way."
        the_person "Yeah, well, try to be more careful next time, alright? Or maybe just ask me if you can touch me. I might say yes."
        "She seems a little put off by the situation, but you both try to move on and put it behind you."
    else: #Fail point for touching waist
        the_person "Oh, baby... you're getting a little too aggressive for my taste."
        "[the_person.title] takes your hand and pulls it off of her waist, giving you a warning look."
        the_person "If you want to touch me, you're going to have to slow down a little. I like to be teased."
        mc.name "Oh yeah, of course. My bad."
        the_person "Just make sure you don't do it again, okay? Or maybe just ask me if you can touch me. I might say yes."
        "She doesn't say anything else, but you can tell she's still a bit annoyed about the situation."
    return

label slutty_sex_accept(the_person, the_position):
    if the_person.sluttiness > 70:
        if the_person.obedience < 70:
            the_person "Fine, let's do it. But don't think this means I'm going to put out every time you ask. I'm a slut, but I'm not easy."
        else:
            if the_position.skill_tag == "Foreplay":
                the_person "Oh, yeah... I've been waiting for this. Touch me, baby, touch me all over."
            elif the_position.skill_tag == "Oral":
                if "getting head" in the_position.opinion_tags:
                    the_person "Ugh, I need your tongue on my clit. Now."
                else:
                    the_person "You're going down on me, and you're going to make me cum. Hard."
            else:
                the_person "Get over here and fuck me already. I've been waiting for this, and I'm not going to wait any longer."
    else:
        the_person "Come here, baby... let's do it. I want to feel your cock inside me."
    return

label slutty_sex_obedience_accept(the_person):
    if the_person.sluttiness > 70:
        the_person "Oh, fuck it. I don't care anymore. Do whatever you want to me, [the_person.mc_title]. I'm a slut, and I love it."
        "[the_person.possessive_title!c] spreads her legs wide, inviting you to take her."
    else:
        if the_person.obedience > 180:
            the_person "Alright, I'll do what you say, but don't think this means I'm not going to enjoy it. I love being a submissive slut."
            "[the_person.possessive_title!c] gives you a sultry smile, her eyes sparkling with desire."
        else:
            the_person "I shouldn't be saying this, but if you really want to... I'll give it a try. And maybe I'll even like it."
            "[the_person.possessive_title!c] gives you a sly smile, her eyes sparkling with mischief."
    return

label slutty_sex_gentle_reject(the_person):
    if the_person.sluttiness > 50:
        the_person "Oh, baby, not like that. I need a little more foreplay first. You know, to get me wet and ready for your cock."
        "[the_person.possessive_title!c] gives you a sultry smile, her eyes sparkling with desire."
    else:
        the_person "No, no, no. I want to have fun, but I don't want to get too serious. Let's just keep it light and dirty."
        "[the_person.possessive_title!c] winks at you, her expression playful and flirtatious."
    return

label slutty_sex_angry_reject(the_person):
    if the_person.has_significant_other:
        the_person "What? Are you out of your mind? I have a [the_person.so_title], but that doesn't mean I'm not interested in you. Maybe we can have a little fun on the side."
        "[the_person.possessive_title!c] gives you a sly smile, her eyes sparkling with mischief."
    elif the_person.sluttiness < 20:
        the_person "Are you serious? You've got to be kidding me! Get away from me, I never want to see you like this again... or maybe I do, I'm not sure."
        "[the_person.title] glares at you, but you can see the desire in her eyes."
    else:
        the_person "What? Are you out of your mind? You can't be serious! Get away from me, I'm not interested in anything like that... or maybe I am, I'm a slut, after all."
        "[the_person.title] glares at you, but you can see the desire in her eyes."
    return

label slutty_seduction_response(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 50:
            the_person "Oh, I think I know what you need right now. Let me take care of you, baby. I'll suck your cock and make you cum."
            "[the_person.possessive_title!c] gives you a sultry smile, her eyes sparkling with desire."
        else:
            the_person "Okay, I'll give you a few minutes. But don't think this means I'm going to be your slave or anything... unless you want me to be, that is."
            "[the_person.possessive_title!c] winks at you, her expression playful and flirtatious."
    else:
        if the_person.sluttiness > 50:
            the_person "Mmm, you're feeling as horny as me then? Come on, let's go find a place to get out of sight and fuck each other's brains out."
            "[the_person.title] takes your hand and leads you off to find some place private."
        elif the_person.sluttiness > 10:
            the_person "I know that look you're giving me, I think I know what you want. And I'm happy to give it to you, baby."
            "[the_person.possessive_title!c] gives you a sultry smile, her eyes sparkling with desire."
        else:
            the_person "[mc.name], I know what you mean... Okay, I can spare a few minutes. But don't get your hopes up, unless you want to get me off, that is."
            "[the_person.possessive_title!c] winks at you, her expression playful and flirtatious."
    return

label slutty_seduction_accept_crowded(the_person):
    if not the_person.has_significant_other:
        if the_person.sluttiness < 20:
            the_person "Alright, let's sneak away for a few minutes and you can convince me a little more... with your cock, that is."
        elif the_person.sluttiness < 50:
            the_person "Come on, I know someplace nearby where we can get a few minutes privacy. Just make it quick, I'm getting wet just thinking about it."
        else:
            the_person "Oh, I don't know if I can wait much longer [the_person.mc_title]... I need to feel your cock inside me, now."
    else:
        if the_person.sluttiness + (5*the_person.opinion.cheating_on_men) > 50:
            the_person "Fuck it, let's do this! I don't care if my [the_person.so_title] finds out, I need to get fucked."
            the_person "I hope you don't mind that I've got a [the_person.so_title], but I don't care right now. I just need to feel your cock inside me."
        else:
            the_person "Ugh, you're bad for me [the_person.mc_title]... Come on, we need to find somewhere quiet so my [the_person.so_title] doesn't catch us. But I'm not promising anything, I'm a slut, after all."
    return

label slutty_seduction_accept_alone(the_person):
    if not the_person.has_significant_other:
        if the_person.sluttiness < 20:
            the_person "Alright, you've got one chance to impress me... with your cock, that is."
        elif the_person.sluttiness < 50:
            the_person "Come on, let's get this over with and see if you're any good. I'm not looking for anything serious, just a quick fuck."
        else:
            the_person "Fuck, I'm so turned on right now. Just do me already! I need to feel your cock inside me, now."
    else:
        if the_person.sluttiness + (5*the_person.opinion.cheating_on_men) > 50:
            the_person "You know I shouldn't be doing this with you, but fuck it. Let's do this! I need to get fucked, and I don't care who knows."
        else:
            the_person "You're trouble, [the_person.mc_title], but I can't help myself. Come here and fuck me, I need it."
    return

label slutty_seduction_refuse(the_person):
    if the_person.sluttiness < 20:
        the_person "Ugh, why are you always trying to flirt with me, [mc.name]? I'm just not in the mood for this right now, okay? Maybe some other time, when I'm feeling more slutty."
        "[the_person.title] folds her arms and looks away, but you can see the desire in her eyes."
    elif the_person.sluttiness < 50:
        the_person "Fine, I'll admit you're kind of cute, but don't think this means I'm actually interested. I just don't feel like messing around right now, okay? Maybe some other time, when I'm feeling more horny."
        "[the_person.title] playfully pokes [mc.name]'s chest with her finger, but you can see the desire in her eyes."
    else:
        the_person "Eh, you're always trying to get me into bed, [mc.name], but I'm not going to make it easy for you. You'll have to wait until I'm good and ready to fool around. And even then, it's going to be on my terms, not yours."
        "[the_person.title] grins mischievously and walks away, leaving [mc.name] to wonder what she's thinking. But you can see the desire in her eyes, and you know she's just playing hard to get."
    return

label slutty_compliment_response(the_person):
    mc.name "Hey [the_person.fname], you look really beautiful today. Is there a special occasion or something?"
    if the_person.is_at_work:
        if (the_person.is_employee or the_person.is_strip_club_employee) and the_person.is_wearing_uniform:
            call slutty_flirt_response_employee_uniform_low(the_person) from _call_slutty_flirt_response_employee_uniform_low_compliment_response
        elif the_person.is_at_job(prostitute_job):
            the_person "Ugh, why do you always want to hang out with me? Can't you see I'm busy getting fucked by other guys?"
        elif the_person.sluttiness > 50:
            the_person "I'm doing great, thanks for asking. And I'm feeling especially slutty today, so maybe we can do something about that."
        else:
            the_person "Oh, stop it, you're making me blush. There's no special occasion, I just felt like dressing up today and showing off my tits."
    else:
        the_person "Well, I did put in a bit of extra effort today. You're just the first one to notice. But thanks, I guess. Maybe you can reward me with a fuck?"
    "You try to press for more information, but [the_person.possessive_title!c] just smiles coyly and changes the subject, leaving you wondering what's going on. But you can see the desire in her eyes, and you know she's just playing hard to get."
    return

label slutty_compliment_response_girlfriend(the_person):
    mc.name "Hey [the_person.title]. You're looking very nice this [StringInfo.time_of_day_string]."
    if the_person.is_at_work:
        if (the_person.is_employee or the_person.is_strip_club_employee) and the_person.is_wearing_uniform:
            call slutty_flirt_response_employee_uniform_mid(the_person) from _call_slutty_flirt_response_employee_uniform_mid_compliment_response_girlfriend
            $ the_person.call_dialogue("flirt_response_employee_uniform_mid")
        elif the_person.sluttiness > 50:
            the_person "Mmm, thank you, [the_person.mc_title]. Wanna find out how nice I am... in bed?"
            "[the_person.possessive_title!c] gives you a sultry smile, her eyes sparkling with desire."
        else:
            the_person "Hmph, really? Thanks, [the_person.mc_title]. You're not so bad yourself. But I'm still not going to make it easy for you."
    else:
        the_person "Ugh, don't be ridiculous. It's just a normal day... but thanks, I guess. Maybe you can make it a little more interesting, though."
        mc.name "Oh come on, don't be like that. You know you look great. And I know you're a great fuck, too."
        the_person "Aww, stop it, [the_person.mc_title]. You're making me blush... and horny. Maybe we can do something about that later."
    "You chat with [the_person.possessive_title!c] for a while, and although she's initially annoyed by your compliments, she starts to warm up to you. And maybe even gets a little turned on."
    return

label slutty_compliment_response_affair(the_person):
    mc.name "Hey [the_person.title]. You're looking absolutely amazing this [StringInfo.time_of_day_string]."
    if the_person.is_at_work:
        if (the_person.is_employee or the_person.is_strip_club_employee) and the_person.is_wearing_uniform:
            call slutty_flirt_response_employee_uniform_mid(the_person) from _call_slutty_flirt_response_employee_uniform_mid_compliment_response_affair
        elif the_person.sluttiness > 50:
            the_person "Mmmm, thank you [the_person.mc_title], wanna go somewhere a little more private, so you can make me feel how amazing I am? Maybe with your cock?"
            "[the_person.possessive_title!c] gives you a sultry smile, her eyes sparkling with desire."
        else:
            the_person "Hmph, really? Thanks, [the_person.mc_title]. You're not so bad yourself. But I'm still not going to make it easy for you."
    else:
        the_person "Ugh, don't be silly. It's just a normal day... but thanks, I suppose. Maybe you can make it a little more interesting, though."
        mc.name "Oh come on, don't be like that. You know you look great. And I know you're a great fuck, too."
        the_person "Aww, stop it, [the_person.mc_title]. You're making me blush... and a little annoyed. But maybe also a little turned on."
    "You keep chatting with [the_person.possessive_title!c] for a while, slipping in a few more compliments. She is quite charmed by your attentiveness, and maybe even gets a little horny."
    return

label slutty_flirt_response(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 50:
            the_person "Ugh, fine. You're not totally terrible, [the_person.mc_title]. And maybe even a little sexy."
            "[the_person.possessive_title!c] gives you a sultry smile, her eyes sparkling with desire."
        else:
            the_person "Whatever. Thanks for the compliment, [the_person.mc_title]. You're not a complete loser. But maybe you can be a complete winner if you fuck me right."

    elif the_person.has_significant_other:
        if the_person.sluttiness + (the_person.opinion.cheating_on_men*5) > 50:
            the_person "Oh, you think you're so clever, don't you? I'll give you that. And maybe even give you my pussy, too."
            "[the_person.title] gives you a sly look, her eyes narrowing."
        else:
            the_person "You're really pushing your luck, [the_person.mc_title]. I have a [the_person.so_title] you know. But maybe I'll cheat on them with you, if you're lucky."
            mc.name "What about you, do you appreciate it?"
            "She rolls her eyes and crosses her arms, but you can see the desire in her eyes."
            the_person "Maybe I do, maybe I don't. It's none of your business. But maybe I'll make it your business, if you're good enough."

    else:
        if the_person.sluttiness > 50:
            the_person "Fine. Maybe you're worth my time, [the_person.mc_title]. And maybe even worth fucking."
            "[the_person.title] gives you a half-smile, but her eyes remain guarded. But you can see the desire in them."
        else:
            the_person "Whatever. You're not unattractive, I suppose. But don't think that means I'll go easy on you. You'll have to really impress me, with your cock."
            the_person "You'll have to really impress me though, I have high standards. But maybe you can meet them, if you're good enough."
    return

label slutty_flirt_response_employee_uniform_low(the_person):
    if the_person.is_wearing_forced_uniform:
        the_person "Hmph, I suppose you like seeing me in this uniform... I mean, I'm practically naked and ready to be fucked!"
        mc.name "I know you don't like it, but I needed to make a point... and maybe get a little turned on, too."
        the_person "I know, I know. You always were one to make a point... and get me wet."
        $ mc.change_locked_clarity(5)
        "She crosses her arms over her chest, but can't hide the small smile on her face as she starts to get turned on."

    elif the_person.judge_outfit(the_person.outfit):
        the_person "Oh, you noticed? I thought it was a bit much, but I guess it's not so bad... especially since I get to show off my tits and ass."
        the_person "I mean, it's nice to work somewhere where I can be a slut and get away with it."
        $ mc.change_locked_clarity(5)
        "She winks at you, then turns to adjust her uniform, accentuating her hips and showing off her body."

    else:
        if the_person.vagina_visible:
            the_person "Hmph, I suppose you like seeing me like this... I mean, my pussy is right out in the open and ready to be fucked!"
            mc.name "Well, you know that it's..."
            the_person "I know, I know. It's company policy... but I have to admit, it's kind of turning me on."
            mc.name "Give it some time and you'll get used to it... or maybe you'll just get more and more turned on."
            $ mc.change_locked_clarity(5)
            "She rolls her eyes, but doesn't argue as she starts to get more and more turned on."

        elif the_person.tits_visible:
            the_person "Ugh, I'm still getting used to being so... exposed in this uniform. But at least I get to show off my tits and maybe even get a little attention."
            mc.name "You look incredible and you're comfortable. I call that a success... and maybe even a little sexy."
            $ mc.change_locked_clarity(5)
            "She huffs, but can't hide her smile as she starts to get turned on."
            the_person "Yeah, yeah. You're just trying to make me feel better... and maybe even get me to fuck you."

        elif the_person.underwear_visible:
            the_person "Hmph, I probably would have picked something that kept me a little more covered, but at least our uniform is comfortable... and maybe even a little sexy."
            mc.name "It may be a little unconventional, but you look fantastic. You've got exactly the right kind of body for it... and maybe even the right kind of personality, too."
            the_person "Well, that's one way to look at it, I suppose... but I have to admit, it's kind of turning me on."
            $ mc.change_locked_clarity(5)
            "She playfully rolls her eyes and turns to adjust her uniform, showing off her body and maybe even a little bit of her underwear."

        else:
            the_person "Ugh, well thank you! Our uniforms are a little bold for my taste, but I guess I look good in it... and maybe even a little slutty, too."
            $ mc.change_locked_clarity(5)
            "She blushes and looks away, but not before you catch a glimpse of her small smile as she starts to get turned on."
    return

label slutty_flirt_response_employee_uniform_mid(the_person):
    if the_person.is_wearing_forced_uniform:
        $ mc.change_locked_clarity(10)
        if the_person.vagina_visible:
            the_person "Ugh, fine. You caught me off guard. I'll admit, this uniform does make me look good, especially with my pussy on display like a dirty little slut."
            mc.name "It's a great uniform, but that's not what's important here. What's important is how sexy you look in it."
            the_person "Yeah, yeah. You're right. It's just hard not to feel like a sex object in this thing, especially with my cunt on display for everyone to see."
        elif the_person.tits_visible:
            the_person "Ugh, fine. You caught me off guard. I'll admit, this uniform does make me look good, especially with my boobs popping out like a pair of juicy melons."
            mc.name "It's a great uniform, but that's not what's important here. What's important is how sexy you look in it."
            the_person "Yeah, yeah. You're right. It's just hard not to feel like a sex object in this thing, especially with my nipples hard and ready for action."
        else:
            the_person "Ugh, fine. You caught me off guard. I'll admit, this uniform does make me look good... and maybe even a little slutty, too."
            mc.name "It's a great uniform, but that's not what's important here. What's important is how sexy you look in it."
            the_person "Yeah, yeah. You're right. It's just hard not to feel like a sex object in this thing, especially when I'm wearing it like a dirty little slut."
        mc.name "Rules are rules and I can't make any exceptions, even if they look good... and sexy."
        "She sighs and nods, her eyes sparkling with desire."
        the_person "Yeah, I know. At least you're having a good time. I don't mind that so much... especially if it means you'll fuck me later."
    elif the_person.judge_outfit(the_person.outfit):
        $ mc.change_locked_clarity(10)
        if the_person.tits_visible:
            the_person "Hmph, maybe I should wear this outfit more often. It's getting a lot of attention, especially for my boobs... and maybe even a little bit of action, too."
            mc.name "It's a great outfit, but I'm more interested in the person wearing it... and maybe even fucking them, too."
            the_person "Oh, really? Is that so? I guess my boobs are hard to ignore... especially when they're bouncing around like a pair of juicy melons."
        else:
            the_person "Hmph, maybe I should wear this outfit more often. It's getting a lot of attention... and maybe even a little bit of action, too."
            mc.name "It's a great outfit, but I'm more interested in the person wearing it... and maybe even fucking them, too."
            the_person "Oh, really? Is that so? I guess my vagina is hard to ignore... especially when it's wet and ready for action."
        the_person "Maybe I'll invite you shopping one day and you can tell me what else you want to see me in... or maybe even what else you want to do to me."
        mc.name "Sounds like a good time... and maybe even a little bit of fun, too."

    else:
        # the_person "I think it shows off a little too much!"
        the_person "Ugh, fine. You're not gonna make this easy for me, are you? You're just going to make me feel like a dirty little slut all day."
        $ mc.change_locked_clarity(10)
        if the_person.vagina_visible:
            the_person "I'm trying to focus on my work here, not flirt with you all day. And definitely not with my pussy on display like a dirty little cunt."
        elif the_person.tits_visible:
            the_person "I'm trying to focus on my work here, not flirt with you all day. And definitely not with my boobs popping out like a pair of juicy melons."
        else:
            the_person "I'm trying to focus on my work here, not flirt with you all day! But maybe I'll make an exception for you... especially if you're going to fuck me later."
        mc.name "I understand, but I promise it's important for the business... and maybe even for your pleasure, too."
        "She sighs and nods, her eyes sparkling with desire."
        the_person "Yeah, I know. You're a real pain, you know that? But maybe I'll forgive you if you fuck me good and hard."
    return

label slutty_flirt_response_low(the_person):
    #She's in her own outfit.
    the_person "Hmph, I suppose it's not the worst outfit I've ever worn... but it's definitely one of the sluttiest."
    $ the_person.draw_person(position = "walking_away")
    $ mc.change_locked_clarity(5)
    "She rolls her eyes and gives you a quick spin, showing off her outfit from every angle and making sure you get a good look at her ass."
    the_person "I mean, I guess it's not too bad, right? Especially since it shows off my tits so well."
    $ the_person.draw_person()
    mc.name "I think it looks great on you... and it's definitely making me hard."
    the_person "Oh, shut up. You're just saying that to get in my pants... but it might just work."
    return

label slutty_flirt_response_low1(the_person):
    if the_person.has_significant_other:
        the_person "Ugh, what's with you and the flirting? I've got a [the_person.so_title], and I don't think he'd appreciate you getting all up in my grill... but maybe I do."
        mc.name "What about you, do you appreciate it?"
        "She rolls her eyes and smirks, her eyes sparkling with desire."
        the_person "Maybe I do... and maybe I'll even cheat on my [the_person.so_title] with you if you're lucky."
    else:
        the_person "Well, thanks for the compliment. But don't think you're getting off that easy. I have high standards, and you'll need to prove yourself to me... in bed."
        the_person "But if you can impress me, who knows what might happen... maybe we'll even have a threesome or something."
    $ mc.change_locked_clarity(5)
    return

label slutty_flirt_response_mid(the_person):
    if mc.location.person_count > 1 and the_person.effective_sluttiness("kissing") < (25 - (5*the_person.opinion.public_sex)):
        $ mc.change_locked_clarity(10)
        the_person "You know, I was wondering if you actually noticed my outfit today... and if you're interested in seeing more of it."
        "Her eyes narrow slightly, but she's still trying to appear casual and flirtatious."
        mc.name "I noticed. It looks great on you... especially your boobs."
        the_person "Oh, really? Thanks, I guess. I was thinking you might say something like that... and maybe even try to get a peek at my pussy."
        "She crosses her arms, trying to maintain a tough exterior, but her eyes are sparkling with desire."
        if the_person.tits_visible:
            mc.name "I noticed. It looks great on you. Especially your boobs... and maybe even your nipples, too."
            the_person "Oh, really? Thanks, I guess. I was thinking you might say something like that... and maybe even try to suck on them."
            "She crosses her arms, trying to maintain a tough exterior, but her eyes are sparkling with desire."
        else:
            mc.name "Well, it's true. You look amazing... and maybe even a little bit slutty, too."
        the_person "Hmph. Maybe I'll invite you shopping one day, so you can tell me what else you want to see me in... and maybe even what else you want to do to me."
        "She leans in slightly, a hint of flirtation in her voice, and her eyes sparkling with desire."
        mc.name "I can think of a few things already... and I'm sure I'd enjoy seeing you in them... and maybe even fucking you in them, too."
        the_person "I'm sure you would. So, what do you say? Want to take me out for a drink and maybe we can discuss my wardrobe some more... and maybe even get a little bit naughty, too?"

    else:
        the_person "Thanks, I thought I looked pretty hot in it too... and maybe even a little bit slutty, too."
        the_person "You want a better look, right? Here, how does it make my ass look... and maybe even my pussy, too?"
        $ the_person.draw_person(position = "back_peek")
        $ mc.change_locked_clarity(10)
        the_person "Good, right? Maybe you can even get a peek at my pussy if you're lucky."
        mc.name "Fantastic. I wish I could get an even better look at it... and maybe even touch it, too."
        "[the_person.possessive_title!c] smiles and turns back to face you, her eyes sparkling with desire."
        $ the_person.draw_person()
        the_person "I'm sure you do. Take me out for a drink and maybe we can work something out... and maybe even get a little bit naughty, too."
    return

label slutty_flirt_response_mid1(the_person):
    $ mc.change_locked_clarity(10)
    the_person "Thanks, I do look amazing in this outfit... and I know you're dying to get a peek at what's underneath."
    if (the_person.has_skirt or the_person.has_dress) and not the_person.has_thigh_high_socks:
        mc.name "You could change it up with some high stockings, I would love to see that... and maybe even get a glimpse of your pussy."
        the_person "Oh, really? And why would you want to see that? You're not going to get a peek or anything, are you... or maybe you will, if you're lucky."
        mc.name "Because it would look great on you, and I would enjoy the view... and maybe even get a little bit turned on."

    mc.name "How about you and me go and grab a coffee sometime... and maybe even get a little bit naughty?"
    if the_person.has_significant_other:
        the_person "Sure, my [the_person.so_title] doesn't mind... as long as they're not around to witness how much fun we're going to have, and how many times I'm going to cum."
    else:
        the_person "Why not, I could use a pick-me-up once in a while... and maybe someone to pick me up from the ground when I fall for you, and onto your cock."
    the_person "Just let me know when, I would love to... and don't think I won't notice if you're trying to get a glimpse of my legs under the table, or maybe even my pussy."
    mc.name "I'll keep that in mind, and maybe we can discuss what else you want to wear in the future... or not wear, like maybe just a thong and a bra."
    the_person "Hmph, maybe. But don't think you're getting a discount on my wardrobe just because we're going out for coffee... or anything else, like maybe a blowjob."
    return

label slutty_flirt_response_high(the_person):
    if mc.location.person_count > 1 and the_person.effective_sluttiness() < (25 - (5*the_person.opinion.public_sex)):
        the_person "You're really persistent, huh? Fine, but not here... let's go somewhere we can get a little more... intimate."
        "She glances around before giving you a sly smile and a wink."

        menu:
            "Find somewhere more quiet\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                mc.name "Then let's find somewhere that isn't here... where we can get a little more... naked."
                the_person "Hmph, eager much? Alright, let's go... and maybe we can even get a little more... naughty."
                call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_slutty_flirt_response_high_2
                the_person "So... Now what's your plan? Want to get a little more... intimate?"

                if the_person.is_willing(kissing):
                    $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
                    if the_person.has_taboo("kissing"):
                        "You lean in close to kiss [the_person.title]... and maybe even get a little more... passionate."
                        $ the_person.call_dialogue("kissing_taboo_break")
                        $ the_person.break_taboo("kissing")
                        "She responds passionately, her arms wrapping around your neck and her tongue in your mouth."
                    else:
                        "You step close to [the_person.title] and put your arm around her waist, pulling her close and kissing her... and maybe even getting a little more... intimate."
                        "She responds immediately and eagerly presses her body against yours, her hands all over your body."
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _vt_slutty_call_fuck_person_49
                else:
                    if the_person.has_taboo("touching_body"):
                        $ the_person.call_dialogue("touching_body_taboo_break")
                        $ the_person.break_taboo("touching_body")
                        "You take her hand and pull her close against you... and maybe even get a little more... intimate. She looks into your eyes and smiles."
                    else:
                        "You take her hand and pull her close, your lips brushing against her ear... and maybe even getting a little more... passionate."
                    call fuck_person(the_person, private = True, start_position = standing_grope, skip_intro = True) from _call_fuck_person_slutty_flirt_grope

                $ the_person.call_dialogue("sex_review", the_report = _return)
                call mc_restore_original_location(the_person) from _call_mc_restore_original_location_slutty_flirt_response_high_2

            "Just flirt":
                mc.name "You know you want to, come on. I'll take you out for dinner, and then we can see where the night takes us... maybe even to the bedroom."
                the_person "Hmm, you're really trying to charm me, aren't you? Well, I'll tell you what... If you can make me laugh, I might consider it... and maybe even get a little more... intimate."
                "She smiles mischievously, clearly enjoying the challenge and the flirtation."

    else:
        if mc.location.person_count == 1:
            the_person "Hmm, you're really eager, aren't you? Well, I suppose it's just the two of us here... so we can get a little more... intimate."
            "[the_person.possessive_title!c] glances around, confirming you're alone and then gives you a sly smile."
            the_person "So what's your plan? Want to get a little more... naughty?"

        else:
            the_person "Feeling bold today, huh? Well, I think your chances are pretty good... and maybe we can even get a little more... intimate."
            "[the_person.title] smirks, clearly enjoying the attention and the flirtation."
            if the_person.has_large_tits:
                $ mc.change_locked_clarity(15)
                "[the_person.title] grabs her tits and jiggles them for you, her eyes sparkling with desire."
                the_person "Maybe I can get these girls out for you... and maybe even get a little more... naked. Does that sound nice?"
            else:
                "[the_person.title] runs her hands over her hips sensually, obviously encouraging you to take things further... and maybe even get a little more... intimate."

        menu:
            "Touch her" if not the_person.is_willing(kissing):
                "You step closer to [the_person.title] and move your hands down her waist... and maybe even get a little more... intimate."
                if the_person.has_taboo("touching_body"):
                    the_person "Oh, you're brave. I like that... and maybe we can even get a little more... naughty."
                    $ the_person.call_dialogue("touching_body_taboo_break")
                    $ the_person.break_taboo("touching_body")

                call fuck_person(the_person, start_position = standing_grope, private = False) from _call_fuck_person_flirt_response_slutty_touching

            "Kiss her" if the_person.is_willing(kissing):
                $ the_person.draw_person()
                if the_person.has_taboo("kissing"):
                    "You put your arm around [the_person.possessive_title!c] and lean in close... and maybe even get a little more... passionate."
                    $ the_person.call_dialogue("kissing_taboo_break")
                    $ the_person.break_taboo("kissing")
                    "She responds with a passionate kiss, her arms wrapping around your neck and her tongue in your mouth."
                else:
                    "You pull [the_person.possessive_title!c] close and kiss her... and maybe even get a little more... intimate."
                    "She responds with a passionate kiss, her arms wrapping around your neck and her hands all over your body."

                call mc_move_to_private_location(the_person) from  _call_mc_move_to_private_location_slutty_flirt_response_high
                call fuck_person(the_person, start_position = kissing, private = _return, skip_intro = True) from _vt_slutty_call_fuck_person_50
                $ the_person.call_dialogue("sex_review", the_report = _return)
                call mc_restore_original_location(the_person) from _call_mc_restore_original_location_slutty_flirt_response_high

            "Just flirt":
                $ the_person.draw_person()
                mc.name "Very tempting, but you're going to have to contain yourself for now... maybe."
                the_person "Oh, you're not going to take advantage of me right now, are you? Fine, be that way... but maybe later we can get a little more... intimate."
                "[the_person.title] pouts, clearly enjoying the flirtation and the attention."
    return

label slutty_flirt_response_low_energy(the_person):
    if the_person.sluttiness > 40:
        the_person "Ugh, thanks for the compliment, but I'm so tired right now... and so horny."
    else:
        the_person "Thanks, but I'm beat. Can we pick this up later... maybe in bed?"
    return

label slutty_flirt_response_girlfriend(the_person):
    # Lead in: mc.name "You're so beautiful [the_person.title], I'm so lucky to have a woman like you in my life."
    if mc.location.person_count > 1:
        # There are other people around, so she'll only start making out with you if she's slutty.
        if the_person.effective_sluttiness("kissing") < (25 - (5*the_person.opinion.public_sex)):
            # Not very slutty, so she wants to find somewhere private
            the_person "Oh my god, you're so cheesy. Come here and kiss me like you mean it."
            "She pulls you against her and kisses you, her lips soft and gentle, but also a little bit dirty."
            the_person "There, now you can't say I don't know how to kiss... or how to make you hard."
            mc.name "Haha, yeah I guess not... but I'm definitely getting hard now."
            "You put your arms around her and kiss her back, feeling her warmth and her tits pressing against your chest."
            the_person "Mmm, yeah, like that. Maybe we can even get a little more... intimate."
            menu:
                "Find somewhere more quiet\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                    mc.name "Why wait? Come on, I'm sure we can find somewhere quiet... and private."
                    the_person "You're always so eager, aren't you? Alright, let's go and get a little more... naughty."
                    "You and [the_person.possessive_title!c] hurry off, searching for a private spot to get a little more... intimate."
                    call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_slutty_flirt_response_girlfriend_2
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _vt_slutty_call_fuck_person_76
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_slutty_flirt_response_girlfriend_2

                "Just flirt":
                    $ mc.change_locked_clarity(10)
                    "You reach around and pull her closer, running your hand down her back and over her ass."
                    mc.name "You're so beautiful, and you know it... and you're also so sexy and slutty."
                    "She rolls her eyes but leans in for a quick kiss, her tongue darting in and out of your mouth."
                    the_person "Fine, you caught me. But don't think this means I'm going easy on you... or that I'm not going to make you cum."

        else:
            the_person "Well if I'm so beautiful, then why are you just standing there? Come on, kiss me like you mean it!"
            "You put your arm around her waist and pull her close, kissing her deeply and passionately, your tongues entwining."
            "When you break the kiss, [the_person.possessive_title!c] sighs and leans against you, her body trembling with desire."
            the_person "You're not so bad yourself... and you're definitely making me wet."
            menu:
                "Make out":
                    "You lean back in and kiss her again, this time more passionately and with a little more... tongue."
                    "[the_person.title] responds eagerly, wrapping her arms around your neck and pulling you closer, her body grinding against yours."

                    call mc_move_to_private_location(the_person) from  _call_mc_move_to_private_location_slutty_flirt_response_girlfriend
                    call fuck_person(the_person, start_position = kissing, private = _return, skip_intro = True) from _vt_slutty_call_fuck_person_77
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_slutty_flirt_response_girlfriend

                "Just flirt":
                    mc.name "I'm not bad? You're the one who's hard to resist... and also hard to keep my hands off of."
                    $ mc.change_locked_clarity(10)
                    "You reach out and touch her cheek, a playful grin on your face, and then you run your hand down her body, over her tits and to her pussy."
                    the_person "Ugh, you're so annoying. But I guess I like that about you... and also how you make me feel, all wet and horny."

    else:
        # You're alone, so she's open to fooling around.
        the_person "Well you've got me all alone, so how about you show me just how lucky you feel... and also how hard you are."
        "She reaches down to your waist and cups your crotch, rubbing it gently and making you even harder."
        mc.name "You're so wet for me already... and also so ready to get fucked."
        the_person "Hmph, maybe... but definitely."
        "She grinds against you, her hips moving in a slow circle, and her body trembling with desire."
        mc.name "Damn, you feel so good... and also so slutty."
        "You reach up and grab her breasts, squeezing them gently and making her moan with pleasure."
        the_person "Ooh, don't do that... but also don't stop."
        "But she doesn't pull away, her body still pressed against yours, and her pussy still grinding against your cock."
        menu:
            "Kiss her":
                if the_person.has_taboo("kissing"):
                    $ the_person.call_dialogue("kissing_taboo_break")
                    $ the_person.break_taboo("kissing")

                "You put your arms around [the_person.possessive_title!c]'s waist and rest your hands on her ass. You pull her close and kiss her sensually, with a little more... tongue."
                "She responds by pressing her body against you and grinding her hips against your thigh, making you even harder."
                "You grab her hips and pull her closer, your crotches pressed together, and your bodies trembling with desire."
                call fuck_person(the_person, start_position = kissing, skip_intro = True) from _vt_slutty_call_fuck_person_78
                $ the_person.call_dialogue("sex_review", the_report = _return)
                $ the_person.review_outfit()

            "Just flirt":
                mc.name "I'm going to make you beg for it... and also make you cum so hard."
                "You lean in close, your breath hot against her ear, and your words making her tremble with desire."
                the_person "Ooh, you're such a bad boy. I love it... and also how you make me feel, all wet and horny."
                "She rubs her body against yours, her hips moving seductively, and her pussy grinding against your cock."
                the_person "But don't think you're getting off that easy. I'm going to make you work for it... and also make you make me cum."
    return

label slutty_flirt_response_affair(the_person):
    # Lead in: mc.name "You look so good today [the_person.title], you're making me want to do some very naughty things to you."
    if mc.location.person_count > 1: #There are other people around, she's nervous about people finding out what you're doing.
        if (the_person.opinion.cheating_on_men *15) + the_person.effective_sluttiness() > 50: #SHe's turned on by flirting in public or doesn't think anything is wrong with it
            "[the_person.possessive_title!c] blushes and playfully bats her eyes at you, her nipples hardening with excitement."
            the_person "Oh, you're making me blush... and also making me wet. I'm not used to this kind of attention from you, but I have to admit, I'm loving it."
            the_person "But I have to admit, I'm curious. What do you have in mind? Want to take me somewhere private and fuck me senseless?"
            menu:
                "Find somewhere more quiet\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                    mc.name "I was thinking we could slip away and find a more private spot... where we can get a little more... intimate."
                    "You and [the_person.title] exchange a flirtatious glance before hurrying off to find a quiet spot, your hands all over each other's bodies."
                    call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_slutty_flirt_response_affair
                    $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
                    "As soon as you're alone she pulls you into a deep and passionate kiss, her tongue darting in and out of your mouth."
                    $ the_person.draw_person(position = "kissing")
                    the_person "Mmm... I've been wanting to do that for a while now. And maybe even get a little more... naughty."
                    "You wrap your arms around her waist and kiss her back, your hands all over her body, and your cock hardening with excitement."
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _vt_slutty_call_fuck_person_79
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_slutty_flirt_response_affair

                "Just flirt":
                    mc.name "I can't help but notice how beautiful you look today, [the_person.title]... and also how sexy and slutty you are."
                    the_person "Stop it, you're making me blush! But I have to admit, you look pretty great yourself... and also pretty hard."
                    the_person "Just don't get too cocky, okay? I'm still in charge here... but maybe not for long, if you keep talking like that."
                    $ mc.change_locked_clarity(20)
                    "[the_person.possessive_title!c] playfully swats at your arm before leaning in close, her breasts pressing against your chest."
                    the_person "But I have to admit, I'm getting a little turned on by this whole thing... and maybe even a little bit wet."
                    "You can't help but feel a little flustered as she teases you, your cock hardening with excitement."
                    mc.name "I can see that. Maybe we should find a more private place to continue this... and maybe even get a little more... intimate."
                    the_person "Mmm, maybe we should. But first, let's enjoy this little moment here... and maybe even get a little more... naughty."

        else: #She's shy or nervous about being discovered
            "[the_person.possessive_title!c] looks around nervously, then back at you with a sheepish grin, her face flushing with embarrassment."
            the_person "Oh, um, you look nice today... and also a little bit sexy, I have to admit."
            mc.name "Wait, don't go! I was thinking we could... uh, grab a drink or something... and maybe even get a little more... intimate."
            $ mc.change_locked_clarity(15)
            the_person "Oh, you want to grab a drink? Okay, sure. But just for a little bit, okay? I don't want to be out too late... or get caught by my [the_person.so_title]."
            "She glances around again, then leans in close and whispers, her breath hot against your ear."
            the_person "And just so you know, I'm still in charge here, even if we're just grabbing a drink... but maybe not for long, if you keep talking like that."
            "You can't help but feel a little excited by her assertiveness, and also a little bit turned on."
            mc.name "Okay, okay. I'll behave... for now, at least."

    else:
        # the_person "Yeah? Well there's nobody around, and I'm not going to stop you."
        the_person "Oh yeah? Well then, do you want to share what all of these naughty things are? You have my attention... and also my body, if you want it."
        menu:
            "Feel her up":
                "You put your arms around [the_person.possessive_title!c]'s waist and rest your hands on her ass, squeezing it gently."
                mc.name "You know, I've been waiting for this moment for a while now... and I'm not going to waste it."
                "You massage her butt, and she blushes and pushes you away lightly, but also a little bit playfully."
                the_person "Hey, no need to be so forward! What's gotten into you... or should I say, what's gotten into me?"
                "You pull her close again and shift your hands to her breasts, squeezing them gently, and also a little bit roughly."
                mc.name "Come on, don't be like that. I just wanted to make you feel good for once... and also make myself feel good, too."
                call fuck_person(the_person, private = True, start_position = standing_grope, skip_intro = True) from _vt_slutty_call_fuck_person_80
                $ the_person.call_dialogue("sex_review", the_report = _return)
                $ the_person.review_outfit()

            "Just flirt":
                $ mc.change_locked_clarity(10)
                "You put your arms around [the_person.possessive_title!c]'s waist and rest your hands on her ass, squeezing it gently."
                mc.name "I wish I had the time. You'll have to wait until later... but maybe not too much later, if you keep looking at me like that."
                "You massage her butt, and she sighs happily and leans her weight against you, her body pressing against yours."
                the_person "Aww, are you sure? I was hoping we could get a little more... intimate, right now."
                "You slap her ass and step back, and she clings to you reluctantly before letting go, her eyes sparkling with desire."
                the_person "Fine, but don't make me wait too long, okay? I have needs, and my [the_person.so_title] sure as hell isn't fulfilling them... but maybe you can."
                mc.name "I won't make you wait long. I promise... and I also promise to make it worth your while, when we do finally get together."
                "She looks up at you with a playful pout, and also a little bit of a smile."
                the_person "Promise you won't make me wait? And also promise you'll make me cum, when we do finally get together?"
                mc.name "I promise, baby. I'll make you cum so hard, you'll be screaming my name."
                "You both share a flirtatious smile, and also a little bit of a laugh, as you both know what's going to happen next."
    return

label slutty_flirt_response_text(the_person):
    mc.name "Hey [the_person.title], how's it going? I'm feeling a bit bored and thought we could chat... or maybe even get a little more... intimate."
    "She replies with a hint of annoyance and a dash of flirtation."
    if the_person.is_affair:
        the_person "Oh, great, you're bored again? You always seem to find ways to bother me... but I have to admit, I'm a little bored too."
        the_person "Well, what do you want this time? I'm not exactly thrilled about entertaining you... but I'm willing to make an exception if you can make me cum."
        the_person "When can we get together and get a little more... naughty?"
        mc.name "Some time soon. I'll let you know... and I'll make sure to bring my A-game."

    elif the_person.is_girlfriend:
        the_person "Bored, huh? That's not exactly a surprise. You're always looking for something new to entertain yourself... and I'm happy to provide it."
        the_person "But fine, we can hang out. Just don't expect me to do anything special... unless you want me to wear something special, that is."
        mc.name "Some time soon. I'll let you know... and I'll make sure to bring my camera."

    elif the_person.love < 40:
        if the_person.effective_sluttiness() > the_person.love:
            the_person "Ugh, bored, really? Well, I suppose I can keep you company for a bit... and maybe even get a little more... intimate."
        else:
            the_person "Bored, eh? That's not surprising. You're always looking for a new distraction... and I'm happy to provide it, as long as you're willing to provide the cock."

    else:
        if the_person.effective_sluttiness() > the_person.love:
            the_person "Fine, I'll talk to you. But don't think this means I'm happy about it... unless you're willing to make me happy, that is."
            the_person "So, what do you want to talk about? I'm not exactly thrilled about this... but I'm willing to listen if you're willing to make me cum."
        else:
            the_person "You're bored, huh? Well, that's your problem, not mine... but I'm happy to help you solve it, as long as you're willing to solve mine too."
            the_person "So, what do you want? Just don't expect me to be all lovey-dovey about it... unless you're willing to get a little more... intimate, that is."
    return

label slutty_condom_demand(the_person):
    if the_person.wants_creampie:
        the_person "Ugh, seriously? You need to put on a condom before we even think about doing anything... but I have to admit, I'm a little tempted to let you cum inside me."
        the_person "I hate that we have to, but you know it's necessary... unless you're willing to take the risk and make me pregnant, that is."
    else:
        the_person "For crying out loud, do you have a condom on you? Put one on before you even think about touching me... but don't think that means I don't want you to touch me, because I do."
        the_person "I don't want to be stuck with some stupid disease because you were too careless... but I'm willing to take the risk if you're willing to make it worth my while."
    return

label slutty_condom_ask(the_person):
    if the_person.on_birth_control:
        the_person "You want a condom? Fine, but I'm on the pill, so it's not like I really need it... but I suppose it's better to be safe than sorry, right?"
        $ the_person.update_birth_control_knowledge()
    elif the_person.wants_creampie:
        the_person "Ugh, you want to cum inside me? Just put on a condom, would you? It's not like I want to get pregnant or anything... but I have to admit, the thought of it is a little bit tempting."
        the_person "But I guess it's better than the alternative, right? I mean, who needs a condom when you can just pull out and cum all over my face?"
        $ the_person.discover_opinion("creampies")
    else:
        the_person "Fine, I guess you should use a condom...but can you at least not make a mess with it? I don't want to clean up after you... but I do want to clean up after myself, if you know what I mean."
        the_person "And please, no pulling out method. That's just asking for trouble... but I'm willing to take the risk if you're willing to make it worth my while, that is."
    return

label slutty_condom_bareback_ask(the_person):
    if the_person.wants_creampie:
        if the_person.is_infertile:
            the_person "You're not seriously considering a condom, are you? Please, just give me your hot, sticky load and make me cum all over your cock."
            the_person "I want to feel you fill me up and make me scream with pleasure, like a dirty little slut."
        elif the_person.on_birth_control:
            the_person "Don't even think about putting a condom on, [the_person.mc_title]. I'm on the pill, so we're good to go and get a little more... naughty."
            the_person "Just fuck me raw and make me feel every inch of you, like a dirty little whore."
            $ the_person.update_birth_control_knowledge()
        else:
            the_person "Forget the condom, [the_person.mc_title], I want to feel you deep inside me, like a hot, throbbing cock."
            the_person "I don't care about the risks, it's worth it for this kind of pleasure, like a slutty little thrill."
            if not the_person.knows_pregnant:
                the_person "Imagine how hot it would be to get knocked up, too, like a dirty little secret."
        $ the_person.discover_opinion("creampies")
    else:
        the_person "Don't bother with a condom, [the_person.mc_title]. I want to feel you raw and unprotected, like a dirty little animal."
        if not the_person.knows_pregnant:
            the_person "I don't care about the risks, it's worth it for the intensity, like a wild, reckless ride."
        else:
            the_person "I love it when you fuck me raw and make me feel like I'm yours, like a dirty little possession."
    return

label slutty_condom_bareback_demand(the_person):
    if the_person.has_breeding_fetish: #Actively looking to get knocked up.
        if the_person.knows_pregnant:
            the_person "Ugh, why bother with a condom? I want to get pregnant, so fuck me raw and make me cum all over your cock!"
            the_person "Hurry up, I can't wait to feel you inside me and make me a dirty little mommy."
        elif the_person.is_infertile:
            the_person "Oh, great, you're going to remind me I can't get pregnant? Thanks a lot, you dirty little tease."
        else:
            the_person "Ugh, what's the point of fucking if you're not going to knock me up? Get inside me and make me a dirty little mommy!"
            the_person "Hurry up and give me that cock, like a dirty little slut!"
    elif the_person.wants_creampie: #Just likes raw sex
        if the_person.is_infertile:
            the_person "Ugh, why bother with a condom? I can't get pregnant anyway, so let's just get dirty and have some fun."
        elif the_person.on_birth_control:
            the_person "Forget the condom, [the_person.mc_title]. I'm on the pill, so it's not a problem, let's just get wild and crazy."
            the_person "Take me bareback and make me scream, like a dirty little whore."
            $ the_person.update_birth_control_knowledge()
        else:
            the_person "Ugh, condoms are so annoying. Just get inside me already and make me feel like a dirty little slut!"
    else:
        if the_person.is_infertile:
            the_person "Take me bareback, [the_person.mc_title]. It's not like I can get pregnant, so let's just have some fun and get a little more... naughty."
            the_person "Just make me feel good, like a dirty little animal."
        elif the_person.on_birth_control:
            the_person "Forget the condom, [the_person.mc_title]. I'm on the pill, so let's just get wild and crazy and have some fun."
            the_person "Take me bareback and make me feel every inch of you, like a dirty little possession."
            $ the_person.update_birth_control_knowledge()
        else:
            the_person "Ugh, condoms are so annoying. Just get inside me already and make me feel like a dirty little slut, like a wild, reckless ride."
            the_person "I need to feel you deep inside me, like a hot, throbbing cock."
    return

label slutty_cum_face(the_person):
    if the_person.has_cum_fetish or the_person.obedience > 180:
        if the_person.has_cum_fetish or the_person.effective_sluttiness() > 60 or the_person.opinion.cum_facials > 0:
            the_person "Oh, yeah! This is the look I'm going for, [the_person.mc_title]! A dirty little slut with a face full of cum!"
            "[the_person.title] smirks, then licks her lips and runs a finger through your semen, bringing it to her mouth and sucking it off with a loud, slurping sound."
            the_person "Mmm, I love the taste of your victory... and your cum!"
        else:
            the_person "Hmph, I suppose it's not a terrible look... but I think I can make it even better."
            "[the_person.title] wipes away some of your semen from her face, then takes a finger and smears it back on, making a dirty little mess."
    else:
        if the_person.effective_sluttiness() > 80 or the_person.opinion.cum_facials > 0:
            the_person "Well, I guess this is one way to end things... but I think I can make it even more interesting."
            "[the_person.title] smirks, then laughs and wipes away some of your semen from her face, then takes a finger and sucks it off with a loud, slurping sound."
        else:
            the_person "Ugh, just get that over with already... but don't think you're getting a second chance... unless you want to make me cum again, that is."
            "[the_person.title] wipes away your semen, looking put off, but also a little bit turned on."
    return

label slutty_cum_mouth(the_person):
    if the_person.has_cum_fetish or the_person.obedience > 180:
        if the_person.has_cum_fetish or the_person.effective_sluttiness() > 60 or the_person.opinion.drinking_cum > 0:
            the_person "Mmm, that's so... satisfying [the_person.mc_title]! I love the taste of your cum in my mouth!"
            the_person "You really know how to make me feel good... and also how to make me cum!"
        else:
            "[the_person.title]'s face twists in disgust as she swallows your cum, but then she looks up at you with a dirty little grin."
            the_person "Ugh, there, done... but I have to admit, that was kind of hot."
    else:
        if the_person.effective_sluttiness() > 80  or the_person.opinion.drinking_cum > 0:
            the_person "Mmm, you're quite the stud, [the_person.mc_title]! I love the way you make me cum... and also the way you make me drink your cum!"
            the_person "I can see why you're so popular... and also why I'm so addicted to your cock!"
        else:
            the_person "Ugh, that's... quite a taste... but I think I can get used to it."
            the_person "I hope you're happy... and also I hope you're ready to make me cum again, because I'm not done yet!"
    return

label slutty_cum_pullout(the_person):
    # Lead in: "I'm going to cum!"
    if mc.condom:
        if the_person.wants_creampie and not the_person.has_taboo("condomless_sex"): #TODO: FIgure out we want any more requirements for this to fire.
            if the_person.knows_pregnant:
                the_person "Oh, don't bother with the condom, just cum inside me and make me pregnant, you dirty fucker!"
                the_person "I don't care about the consequences right now, I just want your cum filling me up and making me feel like a dirty little slut!"
            elif the_person.on_birth_control:
                the_person "Oh fuck... I can't take it any more, take that condom off [the_person.mc_title] and make me cum like a dirty little whore!"
                "She moans desperately and starts to ride your cock harder."
                the_person "I give in, I want you to cum inside me and make me feel like a dirty little slut!"
            else:
                "She moans desperately and starts to ride your cock harder."
                the_person "I can't think straight, just take off the condom and cum inside me, you dirty fucker! Make me cum and then make me pregnant, like a dirty little slut!"
                $ the_person.update_birth_control_knowledge()
                the_person "I want you to breed me like a dirty little animal and make me feel like a slutty little mommy!"
            menu:
                "Take off the condom":
                    "You pull out, barely clearing her pussy, and pull the condom off as quickly as you can manage, like a dirty little slut."
                    $ mc.condom = False
                    $ use_condom = False
                "Leave it on":
                    "You ignore [the_person.possessive_title!c]'s request and keep the condom in place, like a dirty little tease."
        else:
            the_person "Fuck yeah, I'm going to make you cum like a dirty little slut!"
    else:
        if the_person.wants_creampie:
            if the_person.knows_pregnant: #She's already knocked up, so who cares!
                the_person "Creampie me, you dirty fucker, and make me cum like a dirty little slut!"
            elif the_person.opinion.creampies > 0:
                "[the_person.possessive_title!c] moans happily and starts to ride your cock harder."
                if the_person.on_birth_control: #She just likes creampies.
                    the_person "Fuck yeah, fill me up with your cum [the_person.mc_title]! Creampie me like a dirty little slut!"
                else: #Yeah, she's not on BC and asking for you to creampie her. She's looking to get pregnant.
                    $ the_person.update_birth_control_knowledge()
                    the_person "Oh fuck, cum inside me and knock me up [the_person.mc_title]! I want you to breed me like a dirty little animal and make me feel like a slutty little mommy!"
            elif the_person.is_infertile:
                the_person "Cum wherever you want, you dirty fucker, I'm a dirty little slut and I don't care about getting pregnant!"
            elif the_person.on_birth_control: #She's on the pill, so she's probably fine
                $ the_person.update_birth_control_knowledge()
                the_person "Cum wherever you want, you dirty fucker, I'm a dirty little slut and I'm on the pill, so I'm good to go!"
            else: #Too distracted to care about getting pregnant or not. Oh well, what could go wrong?
                the_person "Do it! Cum like a dirty little animal and make me feel like a slutty little whore!"
        else:
            if the_person.is_infertile:
                the_person "Just pull out, I don't want your cum inside me, you dirty fucker! But I still want you to make me cum like a dirty little slut!"
            elif not the_person.on_birth_control: #You need to pull out, I'm not on the pill!
                $ the_person.update_birth_control_knowledge()
                the_person "Fuck, pull out, you dirty fucker! I'm not on the pill, but I still want you to make me cum like a dirty little whore!"
            elif the_person.opinion.creampies < 0:
                the_person "Pull out, I don't want you to cum in me, you dirty fucker! But I still want you to make me cum like a dirty little slut!"
            else:
                the_person "Hell yeah, pull out and cum all over me like a dirty slut! Make me feel like a dirty little animal and cover me in your cum!"
    return


label slutty_cum_condom(the_person):
    if the_person.effective_sluttiness() > 75 or the_person.opinion.creampies > 0:
        the_person "Oh god, it feels so good. If your condom broke it would be inside me, and I'd be pregnant... and I'd love every minute of it, you dirty fucker!"
    else:
        the_person "Oh god, I hope you buy good condoms because that's a lot of cum... but I have to admit, the thought of you knocking me up and getting me pregnant is kind of hot, you dirty little slut!"
        the_person "But then again, maybe you're dreaming of knocking me up and getting me pregnant... and maybe I'm dreaming of it too, you dirty little animal!"
    return

label slutty_cum_vagina(the_person):
    if the_person.has_taboo("creampie"):
        $ the_person.call_dialogue("creampie_taboo_break")
        $ the_person.break_taboo("creampie")
        return
    if the_person.wants_creampie:
        if the_person.knows_pregnant:
            the_person "Ugh, fine... I guess I can admit it now, but only because I'm already pregnant from your other, uh, impressive performances... Your cum just feels so good inside me, like a dirty little secret!"
        elif the_person.is_infertile:
            the_person "Oh, stop being so dramatic! Of course you're not going to get me pregnant, I'm infertile, remember? But seriously, your cum is pretty great... just don't expect me to admit it to anyone else, you dirty little slut!"
        elif the_person.on_birth_control:
            if the_person.has_significant_other:
                the_person "Well, well, well... Look at you go! I guess it's a good thing I'm on the pill, huh? Or maybe I'll just tell [the_person.SO_name] that it was someone else's... Ugh, why do you have to be so frustrating, you dirty little tease?"
            else:
                if the_person.knows_pregnant:
                    the_person "Oh fuck that's a lot of cum. Good thing I'm already pregnant, because I don't think you're firing blanks... and I love every minute of it, you dirty little animal!"
                elif the_person.is_infertile:
                    the_person "Oh fuck that's a lot of cum. I will be dripping your cum all day long, like a dirty little slut!"
                else:
                    the_person "Oh fuck that's a lot of cum. Good thing I'm on the pill, because I don't think you're firing blanks... but maybe I wish you were, you dirty little fucker!"
                $ the_person.update_birth_control_knowledge()
        elif the_person.effective_sluttiness() > 75 or the_person.opinion.creampies > 0:
            if the_person.has_significant_other:
                the_person "Okay, okay, I get it! You're great in bed, but don't think I'm going to start flaunting our little secret around my [the_person.so_title]... At least, not until I figure out how to explain it, you dirty little slut!"
            else:
                the_person "Ugh, fine... I'll admit it, you're pretty amazing when you're like this... But don't think this means I'm going to start begging for more! I just need to... process this, okay, you dirty little animal?"
        else:
            if the_person.has_significant_other:
                the_person "You really know how to make a girl feel special, don't you? But let's keep this between us, okay? I don't think [the_person.SO_name] would understand... but maybe I wish they did, you dirty little tease!"
            else:
                the_person "Wow... I guess I didn't expect that from you. But I have to admit, it was kind of nice... Just don't get any ideas, okay? I'm not ready for anything serious, but maybe I'm ready for something dirty and slutty!"
    else:
        if the_person.knows_pregnant:
            the_person "Ugh, what is wrong with you? I specifically told you not to do that! Oh well, since I'm already pregnant... I guess I'll just have to deal with it, you dirty little fucker!"
        elif not the_person.on_birth_control:
            if the_person.has_significant_other:
                the_person "Oh, great. Just what I needed. You forgot to pull out, and now I'm going to have to deal with [the_person.SO_name]'s anger... and maybe even my own anger, you dirty little slut!"
                if the_person.kids > 0:
                    the_person "... Again, you dirty little repeat offender!"
            else:
                the_person "Oh fuck, I said to pull out! I'm not on the pill [the_person.mc_title], what happens if I get pregnant? You're going to have to take care of me, you dirty little fucker!"
                $ the_person.update_birth_control_knowledge()
                the_person "What is wrong with you? You know I'm not on the pill! Now look what you've done... I guess next time we'll have to use a condom, you dirty little animal!"
        elif the_person.is_infertile:
            the_person "Unbelievable! I told you to pull out, and now you've gone and made a mess... What a pain in the ass, you dirty little slut!"
        elif the_person.has_significant_other:
            the_person "You're really going to make me tell [the_person.SO_name] about this, aren't you? Fine, I'll deal with it. Just be more careful next time, you dirty little tease!"
            $ the_person.update_birth_control_knowledge()
            the_person "I don't want to have to make you wear a condom, so be a little more careful next time, you dirty little fucker!"
        elif the_person.opinion.creampies < 0:
            the_person "Oh, great. Just what I needed. You couldn't even follow a simple instruction, could you? Now look at what a mess you've made, you dirty little animal!"
        else:
            the_person "You really need to work on your timing. I told you to pull out, not do the exact opposite, you dirty little slut!"
            the_person "Just remember, I'm not going to be as forgiving next time if you can't follow simple instructions, you dirty little fucker!"
    return

label slutty_cum_anal(the_person):
    if the_person.has_taboo("anal creampie"):
        $ the_person.call_dialogue("anal_creampie_taboo_break")
        $ the_person.break_taboo("anal creampie")
        return

    if the_person.sluttiness > 75 or the_person.opinion.anal_creampies > 0:
        the_person "Oh, yeah! I love it when you cum in my ass! It's like a dirty little secret that only we know."
    elif the_person.opinion.anal_creampies < 0:
        the_person "Ugh, not in there! I don't need to be embarrassed like that, you dirty little fucker!"
    else:
        the_person "Oh, alright... if you insist... But just this once, and don't think I'm going to start liking it or anything, you dirty little fucker!"
    return

label slutty_surprised_exclaim(the_person):
    $rando = renpy.random.choice(["What the fuck?","Ugh, are you kidding me?","Why now, of all times?","This shit again?","Not again, you dirty little cock!", "Seriously, what's wrong with you?", "Great, just what I needed, another cock to deal with...", "Oh, joy, another chance to get fucked...", "Fucking perfect, just what I wanted, a big, hard cock...", "Unbelievable, you're really going to make me cum again!", "Not again, you dirty little animal!", "Why can't I have a normal day, without getting fucked senseless?"])
    the_person "[rando]"
    "She shakes her head, then looks at you with a mixture of annoyance and lust, her eyes flashing with desire."
    return

label slutty_talk_busy(the_person):
    if the_person.obedience > 120:
        the_person "Ugh, I don't have time for this, [the_person.mc_title]. I've got way too much on my plate right now, like getting fucked by you, you dirty little animal!"
    else:
        the_person "Listen, I'd love to catch up, but I'm swamped with things to do... like getting my pussy eaten by you, you dirty little slut!"
    return

label slutty_sex_strip(the_person):
    if the_person.sluttiness < 20:
        if the_person.arousal_perc < 50:
            the_person "Ugh, fine. I'll take off some clothes, but don't think I'm doing this because I like you or anything, you dirty little fucker. I just need to get comfortable, that's all."
            mc.name "Come on, babe. It's just us here. You can relax and show me your dirty little body."
            the_person "I don't care! I'm still not comfortable. And don't call me 'babe', you dirty little animal. That's weird."
            mc.name "Okay, okay. I'll stop. Just take your time, okay, and let me see your dirty little pussy?"
        else:
            the_person "Alright, alright. I'll take off a few things, but don't expect me to be impressed by your reaction, you dirty little slut. I'm just taking off some clothes, big deal."
            mc.name "Aww, come on. You're being a little rough. Just let me see you a little more, okay, and maybe I'll even get to fuck you?"
            the_person "Fine, but only because you asked nicely, you dirty little fucker. And don't think this means I like you or anything, I just want to get fucked."
    elif the_person.sluttiness < 60:
        if the_person.arousal_perc < 50:
            the_person "Fine, I'll make an exception and get a little more comfortable, but don't get any ideas, okay, you dirty little animal?"
            mc.name "I promise, I won't get any ideas. I just want to make sure you're comfortable and ready to get fucked."
            the_person "Ugh, fine. But don't think I'm doing this for you, I just need to get a little more comfortable and show you my dirty little body."
            mc.name "I understand. Just take your time and let me know if you need anything, like a good hard fuck."
        else:
            the_person "Okay, okay. I'll take off a few more things if it'll make you happy, you dirty little slut. But don't think I'm doing this because I'm into you or anything, I just want to get fucked."
            mc.name "I know, I know. You're just doing it because you want to, right, you dirty little animal?"
            the_person "Whatever. Just let me get this off and we can get on with this, and maybe even get to the fucking part."
    else:
        if the_person.arousal_perc < 50:
            the_person "Ugh, fine. I'll do it, but just for you, I'll make an exception, you dirty little fucker. And don't think I'm doing this because I like you or anything, I just want to get fucked."
            mc.name "Thanks, babe. You're making me really happy right now, and I promise to make you happy too, with my cock."
            the_person "Don't call me 'babe', you dirty little animal. And don't get too happy, I'm just doing this because I have to, and because I want to get fucked."
        else:
            the_person "Great, now let me get this off and we can get on with this, I'm dying over here! But don't expect me to be all happy about it or anything, I just want to get fucked and cum."
            mc.name "Aww, come on. You're being a little grumpy. Let's just have some fun, okay, and maybe even get a little dirty?"
            the_person "Fine. But don't expect me to start smiling and laughing or anything, I just want to get fucked and feel like a dirty little slut."
    return

label slutty_sex_watch(the_person, the_sex_person, the_position):
    $ title = the_person.title if not the_person.is_stranger else "The dirty little stranger"
    if the_person.sluttiness < the_position.slut_requirement - 20:
        $ the_person.draw_person(emotion = "angry", display_transform = character_left_flipped)
        the_person "Ugh, seriously? Can you two keep it down? I'm trying to concentrate on my own dirty little fantasies."
        $ the_person.change_stats(obedience = -2, happiness = -1)
        "[title] rolls her eyes and tries to ignore you and [the_sex_person.fname] [the_position.verb], but can't help sneaking a peek."
        return False
    if the_person.sluttiness < the_position.slut_requirement - 10:
        $ the_person.draw_person(display_transform = character_left_flipped)
        the_person "Honestly, you two are so hot. Can't you just invite me to join in on the fun?"
        $ the_person.change_happiness(-1)
        "[title] looks away, trying to pretend she's not interested in what you and [the_sex_person.fname] are doing, but her eyes keep drifting back to the action."
        return False
    if the_person.sluttiness < the_position.slut_requirement:
        $ the_person.draw_person(display_transform = character_left_flipped)
        if not is_watching(the_person):
            the_person "You're really getting into it, aren't you? I suppose it's kind of hot... and making me a little wet."
        $ the_person.change_slut(1, 30)
        "[title] watches you and [the_sex_person.fname] [the_position.verb], trying not to blush, but her face is getting hotter by the second."
        return True
    if the_person.sluttiness >= the_position.slut_requirement and the_person.sluttiness < the_position.slut_cap:
        $ the_person.draw_person(display_transform = character_left_flipped)
        if not is_watching(the_person):
            the_person "Oh, wow... this looks like so much fun. Can I join in and get fucked too?"
        $ the_person.change_slut(1, 50)
        "[title] watches you and [the_sex_person.fname] [the_position.verb], her eyes sparkling with excitement, and her pussy getting wetter by the second."
        return True
    $ the_person.draw_person(emotion = "happy", display_transform = character_left_flipped)
    if renpy.random.randint(0, 1) == 0:
        the_person "You know, [the_person.mc_title], [the_sex_person.fname] is really getting into this. Maybe you should, uh, spice things up a bit and make her cum?"
    else:
        call watcher_position_comment(the_person, the_sex_person, the_position) from _call_watcher_position_comment_slutty_sex_watch
    "[title] watches with interest as you and [the_sex_person.fname] [the_position.verb], and starts to touch herself."
    return True

label slutty_being_watched(the_person, the_watcher, the_position):
    $ title = the_watcher.fname if not the_watcher.is_stranger else "the dirty little stranger"

    if the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        the_person "Hmph, I guess you're right, [the_person.mc_title]."
        the_person "But don't think I'm going easy on you just because there's an audience... I want you to fuck me harder and make me cum!"
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [title] watching you and her [the_position.verb], and starts to moan louder."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        the_person "You know, [title], I don't really care what you think, but it's pretty obvious you're turned on right now... and I'm going to make you watch me get fucked."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        the_person "Oh, come on, [title]! Don't be shy! You know you want a taste of this action... and I want to taste you too!"
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [title] watching you and her [the_position.verb], and starts to touch herself."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        "[the_person.fname] glances at [title]."
        the_person "Yeah, I guess I can handle a little more... for now, and maybe even get a little more adventurous."
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [title] watching you and her [the_position.verb], and starts to moan louder."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        the_person "Ugh, why do you have to be here, [title]? Can't you just leave me alone to get fucked in peace?"
        $ the_person.change_stats(arousal = -1, slut = -1)
        "[the_person.title] seems uncomfortable with [title] nearby, but still wants to get fucked."

    else:
        "[the_person.possessive_title!c] rolls her eyes at [title]."
        the_person "Whatever, [title], you're missing out. Maybe next time you'll get a chance to join in on the fun and get fucked too."
        $ the_person.change_stats(arousal = 1, slut = 1, max_slut = 30)
        "[the_person.title] seems more comfortable [the_position.verbing] you with [title] around, and starts to get more into it."

    return

label slutty_work_enter_greeting(the_person):
    if the_person.happiness < 80 or the_person.love < 0:
        "[the_person.title] glances at you when you enter the room, her expression a mixture of annoyance and lust."
        the_person "What do you want, [the_person.mc_title]? I'm in the middle of something... but I can always make time for a quick fuck."
        "She goes back to her work, not looking up again, but her body language screams 'I want to get fucked'."

    elif the_person.happiness > 130:
        if the_person.sluttiness > 40:
            the_person "Hey [the_person.mc_title], just the person I was hoping to see... and fuck."
            "Her eyes sparkle with mischief as she leans against her desk, her legs spread wide open."
            the_person "You know what they say: all work and no play makes for a dull girl... but I'm not dull, I'm a dirty little slut."
            "She winks, inviting you to join her in some 'play'... or rather, some hot, sweaty sex."
        else:
            "[the_person.title] looks up from her work and smiles at you when you enter the room, her face flushed with excitement."
            the_person "Hey [the_person.mc_title], it's nice to have you stop by... and maybe even get a little naughty."
            "She blushes slightly, looking away before quickly glancing back at you, her eyes sparkling with desire."
    else:
        if the_person.sluttiness > 60:
            $ the_person.draw_person(position = "stand4")
            "[the_person.title] walks over to you when you come into the room, her hips swaying seductively, her ass shaking like a leaf."
            the_person "Well, well, well. Look who decided to drop by... and maybe even get a little lucky."
            "She leans in close, her voice husky and sultry, her breath hot against your ear."
            the_person "I've been waiting for you, [the_person.mc_title]. You know, just to catch up... and maybe even get caught up in a little passion."
            "She brushes her fingers against your arm, sending shivers down your spine, and making your cock hard as a rock."
        else:
            the_person "Hey [the_person.mc_title]. Need anything? I mean, if you're not too busy... maybe we can get a little busy together."
            "She looks up at you, her eyes soft and inviting, her lips curled up into a sexy little smile."
    return

label slutty_date_seduction(the_person):
    if the_person.is_girlfriend:
        "[the_person.possessive_title!c] grabs your hand and pulls you around to look at her, her eyes sparkling with desire."
        the_person "Hey, that was such a great time. So I was thinking... maybe we can make it an even better time by getting a little more intimate."
        $ mc.change_locked_clarity(30)
        if the_person.effective_sluttiness(["vaginal_sex", "condomless_sex"]) > 60 and the_person.wants_creampie and the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex >= 0 and the_person.opinion.creampies >= 0 and not the_person.on_birth_control and not the_person.knows_pregnant:
            if the_person.opinion.creampies > 0:
                the_person "You're probably just going to say no, but I really want to get knocked up by someone like you. I want to feel your cum inside me and know that I'm going to be a dirty little mommy."
                the_person "So, are you going to make me pregnant or what? I bet you could give me some amazing kids, and I could give you some amazing sex."
            else:
                the_person "I don't care if you don't use a condom. I just want you to fuck me and make me feel good. I want to feel your cock inside me and know that I'm a dirty little slut."
                the_person "You're so much better than those other guys, anyway. They don't know how to make a girl cum like you do."
        elif the_person.effective_sluttiness(["vaginal_sex", "condomless_sex"]) > 60 and the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex > 0:
            the_person "Ugh, fine. If you really want to know, I'd rather not use a condom. I want to feel your cock inside me and know that I'm a dirty little slut."
            the_person "But don't think I'm doing it for you or anything. It just feels better that way, and I'm a dirty little slut who loves to get fucked."
        elif the_person.effective_sluttiness(["vaginal_sex"]) > 50 and the_person.opinion.vaginal_sex > 0:
            the_person "You know, I didn't really want to go home with someone like you. But you're kind of growing on me, and I think I want to get fucked by you."
            the_person "So, do you want to fuck me or what? I'm a dirty little slut who loves to get fucked, and I think you're the perfect guy to do it."
        elif the_person.effective_sluttiness(["anal_sex"]) > 60 and the_person.opinion.anal_sex > 0:
            the_person "I don't know why I'm even bothering to ask you this, but... do you want to fuck my ass? I want to feel your cock inside me and know that I'm a dirty little slut."
            the_person "It's not like I'm asking for much, but you're probably just going to say no anyway. But I'm a dirty little slut who loves to get fucked in the ass, so I'm going to ask anyway."
        elif the_person.effective_sluttiness(["sucking_cock"]) > 40 and the_person.opinion.giving_blowjobs > 0:
            the_person "You know, I'm not really in the mood to do this, but... you're kind of cute when you're all worked up. And I love sucking cock, so I'm going to do it anyway."
            the_person "So, do you want a blowjob or what? I'm a dirty little slut who loves to suck cock, and I think you're the perfect guy to do it for."
        elif the_person.effective_sluttiness() > 40 and the_person.opinion.being_covered_in_cum > 0:
            the_person "Ugh, fine. If you really want to know, I'd be okay with getting covered in your cum. I want to feel your cum all over me and know that I'm a dirty little slut."
            the_person "But don't expect me to be all happy about it or anything. I'm just a dirty little slut who loves to get covered in cum, that's all."
        elif the_person.effective_sluttiness(["touching_body"]) > 40 and the_person.opinion.giving_tit_fucks > 0 and the_person.has_large_tits:
            the_person "I don't know why I'm even telling you this, but... I'd be okay with sucking you off between my tits. I want to feel your cock between my tits and know that I'm a dirty little slut."
            the_person "But don't think I'm doing it because I like you or anything. I'm just a dirty little slut who loves to get fucked, that's all."
        else:
            the_person "You know, I don't really feel like going home with you or anything... but I guess I could be persuaded if you do something really good. Like, maybe you could fuck me and make me cum?"
            the_person "She smirks, leaving the invitation open-ended and making you wonder what she really wants."
    elif the_person.is_affair:
        the_person "So my [the_person.so_title] won't be home tonight, I was thinking... maybe we can get a little more intimate and have some fun."
        "She reaches down and cups your crotch, rubbing it gently through your pants and making you hard."
        $ mc.change_locked_clarity(40)
        if the_person.wants_creampie and the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex >= 0 and the_person.opinion.creampies >= 0 and not the_person.on_birth_control and not the_person.knows_pregnant:
            if the_person.opinion.creampies > 0:
                the_person "Fine, let's go back to my place so you can pin me to the bed and creampie me all night long. I want to feel your cum inside me and know that I'm going to be a dirty little mommy."
                the_person "I swear, just the thought of your cum inside me is making me want to puke and yet... I'm getting wet."
            else:
                the_person "Alright, let's go back to my place. You can pin me to the bed and fuck me bareback all night long. I want to feel your cock inside me and know that I'm a dirty little slut."
                the_person "I hate how much I want this, but I do. So just fuck me up with your cock already."
        elif the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex > 0:
            the_person "Ugh, fine. Let's go back to my place and fuck all night. No condoms, just your cock inside me and making me cum."
            the_person "I don't want to admit it, but I'm really looking forward to this. I'm a dirty little slut who loves to get fucked, and I think you're the perfect guy to do it."
        elif the_person.opinion.vaginal_sex > 0:
            the_person "Fine, let's go back to my place and you can pound my tight fucking pussy until I'm a wreck. I want to feel your cock inside me and know that I'm a dirty little slut."
            the_person "I hate how much I enjoy this, but... I do. So do it, and make me cum like a dirty little slut."
        elif the_person.opinion.anal_sex > 0:
            the_person "Ugh, alright. Let's go back to my place so you can... you know. I want to feel your cock in my ass and know that I'm a dirty little slut."
            the_person "I don't want to admit it, but my ass is really excited for this. I'm a dirty little slut who loves to get fucked in the ass, and I think you're the perfect guy to do it."
        elif the_person.opinion.giving_blowjobs > 0:
            the_person "Fine, let's go back to my place and you can choke me out with your cock. I want to feel your cock in my mouth and know that I'm a dirty little slut."
            the_person "I hate how much I want this, but I do. So just do it already, and make me cum like a dirty little slut."
        elif the_person.opinion.being_covered_in_cum > 0:
            the_person "Ugh, alright. Let's go back to my place, and you can cover me in your sperm all night. I want to feel your cum all over me and know that I'm a dirty little slut."
            the_person "I hate how much I enjoy this, but... I do. So just do it, and make me cum like a dirty little slut."
        elif the_person.opinion.giving_tit_fucks > 0 and the_person.has_large_tits:
            the_person "Fine, let's go back to my place so I can... you know. I want to feel your cock between my tits and know that I'm a dirty little slut."
            the_person "I hate how much I enjoy this, but I do. So just do it already, and make me cum like a dirty little slut."
        elif the_person.opinion.cheating_on_men > 0:
            the_person "Ugh, fine. Let's go back to my place, and you can do all the things I tell my [the_person.so_title] I hate. I want to feel your cock inside me and know that I'm a dirty little slut."
            the_person "I don't want to admit it, but I'm really looking forward to this. I'm a dirty little slut who loves to get fucked, and I think you're the perfect guy to do it."
        else:
            the_person "Ugh, let's go back to my place and make him really regret leaving me alone for the night. I want to feel your cock inside me and know that I'm a dirty little slut."
    elif not the_person.has_significant_other:
        $ mc.change_locked_clarity(20)
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                the_person "Ugh, fine. I've had a blast [the_person.mc_title], but there are a few more things I'd like to do with you. Want to come back to my place and find out what they are? Maybe we can get a little more intimate and have some fun."
            else:
                the_person "Whatever. You've been a blast [the_person.mc_title]. Want to come back to my place, have a few drinks, and see where things lead? I suppose I'm a dirty little slut who loves to get fucked, and I think you're the perfect guy to do it."
        else:
            if the_person.love > 40:
                the_person "Fine, I don't want to say goodbye either. Tonight's been amazing [the_person.mc_title]. Do you want to come back to my place and have a few drinks? Maybe we can get a little more intimate and have some fun."
            else:
                the_person "Whatever. This might be crazy, but I had a great time tonight and you make me a little crazy. Do you want to come back to my place and see where things go? I don't know why I'm even asking, but I'm a dirty little slut who loves to get fucked, and I think you're the perfect guy to do it."
    else:
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                $ mc.change_locked_clarity(20)
                the_person "Ugh, fine. I'm not done with you yet [the_person.mc_title]. Want to come back to my place? But don't think you're getting away with anything, I'm a dirty little slut who loves to get fucked, and I think you're the perfect guy to do it."
                the_person "My [the_person.so_title] won't be home until morning, so we would have plenty of time to get a little more intimate and have some fun."
            else:
                $ mc.change_locked_clarity(20)
                the_person "Whatever. This might be crazy, but do you want to come back to have another drink with me? I suppose I'm a dirty little slut who loves to get fucked, and I think you're the perfect guy to do it."
                the_person "My [the_person.so_title] is stuck at work and I don't want to be left all alone, so maybe we can get a little more intimate and have some fun."
        else:
            if the_person.love > 40:
                $ mc.change_locked_clarity(20)
                the_person "Whatever. You're making me feel crazy [the_person.mc_title]. Do you want to come have a drink at my place? But don't think this means anything, I'm a dirty little slut who loves to get fucked, and I think you're the perfect guy to do it."
                the_person "My [the_person.so_title] won't be home until morning, and we have a big bed you could help me warm up. Maybe we can get a little more intimate and have some fun."
            else:
                $ mc.change_locked_clarity(20)
                the_person "Whatever. This is crazy, but would you want to have one last drink at my place? My [the_person.so_title] won't be home until morning... I suppose I'm a dirty little slut who loves to get fucked, and I think you're the perfect guy to do it."
    return

label slutty_sex_end_early(the_person):
    if the_person.sluttiness > 50:
        if the_person.love > 40:
            if the_person.arousal_perc > 60:
                the_person "Ugh, really? You're done already? I was just getting into it, [mc.name]... I mean, you're not exactly the most energetic partner I've ever had, but I was hoping for a little more... excitement."
                the_person "But hey, I'll give you credit, you did try your best. Or at least, as best as you could with that tiny little cock of yours."
            else:
                the_person "Well, I suppose that's it? I was ready to give you a lot more... But I guess you're not exactly the most enthusiastic about this whole situation, are you? I mean, I'm a dirty little slut who loves to get fucked, and you're just... meh."
        else:
            if the_person.arousal_perc > 60:
                the_person "Hmph, you're sure you're finished? I was really enjoying this... You know, I don't usually do this, but I was actually getting kind of into it. And now you're just going to leave me hanging like this? What a tease!"
                the_person "But I guess you're not exactly the most experienced, are you? I mean, it's not like I'm the one who needs to learn how to do this properly... but maybe you should take a few lessons from a real slut like me."
            else:
                the_person "I guess it was okay, I suppose. I mean, it's not like I was expecting much from you in the first place... but still, a girl can dream, right? Maybe next time you can try a little harder to make me cum."
    else:
        if the_person.love > 40:
            if the_person.arousal_perc > 60:
                the_person "Oh, come on, [mc.name], you can't leave me hanging like this... I mean, I was actually starting to enjoy this! And now you're just going to stop and leave me all frustrated and shit?"
                the_person "But hey, I guess you're not exactly the most romantic guy out there, are you? I mean, I'm a dirty little slut who loves to get fucked, and you're just... not."
            else:
                the_person "Well, that was a nice little interlude, I suppose. I mean, it's not like I'm the type to be all lovey-dovey and shit... but still, a girl can appreciate a good fuck every now and then."
        else:
            if the_person.arousal_perc > 60:
                the_person "Geez, I guess that was enough... I mean, I don't know why you even bother trying, you're not exactly the best at this, are you? Maybe you should just stick to jerking off or something."
            else:
                the_person "Good, it's over. Now let's get this over with. I mean, I've got better things to do than hang around with someone who can't even manage to get it right... like find someone who can actually make me cum."
    return

label slutty_sex_take_control(the_person):
    if the_person.arousal_perc > 60:
        the_person "What do you think you're doing, [mc.name]? Don't just leave me hanging like this! I mean, I'm the one who's supposed to be in control here, not you! And now you're just going to stop and leave me all frustrated and shit?"
        the_person "But hey, if you're not going to finish the job, then I will. And don't think for a second that I won't make you regret it. I'm a dirty little slut who loves to get fucked, and I always get what I want."
    else:
        the_person "Ugh, really? You're not even going to finish what you started? Fine, I'll do it myself then! And don't think you can just waltz in here and expect me to be all weak and submissive. I'm not that kind of girl, [mc.name]. I'm a dirty little slut who loves to get fucked, and I always get what I want."
    return

label slutty_sex_beg_finish(the_person):
    the_person "Okay, fine, [mc.name], you want to play it cool? I'll let you off the hook this time, but just know that I'm going to make you pay for this. And when I'm done, I'm going to make sure you know exactly who's in control here. I'm a dirty little slut who loves to get fucked, and I always get what I want."
    the_person "So, are you going to finish what you started, or do I have to take matters into my own hands? Either way, I'm going to make sure I get what I want... and what I want is to get fucked hard and cum all over your cock."
    return

label slutty_sex_review(the_person, the_report):
    $ comment_position = the_person.pick_position_comment(the_report)
    if comment_position is None:
        return #You didn't actually do anything, no need to comment.

    $ used_obedience = the_report.get("obedience_used", False) #True if a girl only tried a position because you ordered her to.
    $ the_person.draw_person()  # make sure she stands up for talking with you

    #She's worried about her SO finding out because it was in public
    if the_report.get("was_public", False) and the_person.has_significant_other and the_person.opinion.cheating_on_men <= 0: #It was public and she cares.
        if the_person.is_affair: #Dialogue about her being into it, but you can't do this in case she gets caught.
            the_person "Oh, fuck, this is so dirty! I'm really getting into this, but we can't get caught... I don't want my [the_person.so_title] to know about our little affair."
            the_person "What if someone sees us and tells my [the_person.so_title]? I'll never hear the end of it, and I'll be in so much trouble!"
        elif used_obedience:
            the_person "I'm such a dirty little slut for doing this in public! Someone might recognize me and tell my [the_person.so_title]."
            mc.name "Don't worry, nobody's going to tell anyone. We're being careful, and I'll make sure you're safe."
            the_person "I hope you're right... I don't want anyone finding out about this and ruining my reputation."
        else:
            $ the_person.call_dialogue("surprised_exclaim")
            the_person "Oh no, we're out in public! Someone might see us and tell my [the_person.so_title]. I'll be so screwed, and I'll never be able to show my face again!"
            mc.name "Don't worry, nobody's paying attention to us. Nobody's going to tell your [the_person.so_title], and we'll be fine."
            the_person "I hope you're right... I don't want anyone knowing about this and judging me for being a dirty little slut."

    #She's single, but worried that you did in public.
    elif the_report.get("was_public", False) and (the_person.effective_sluttiness()+10*the_person.opinion.public_sex < comment_position.slut_cap):
        if used_obedience:
            the_person "Ugh, I'm such a dirty little slut for doing this in public! Everyone's staring at us like we're some kind of perverts..."
            the_person "I'll never live this down, [mc.name]. People are going to talk about this for weeks, and I'll be the laughing stock of the town!"
        else:
            the_person "Oh no, we're in public! Everyone's watching us and judging us for this... I'm so embarrassed, and I just want to hide!"
            mc.name "Don't worry, nobody really cares what we're doing. They're just curious, and they'll forget about it soon enough."
            the_person "I hope you're right, or I'm going to end up with a terrible reputation for this sort of thing... and I'll never be able to show my face again!"

    elif the_report.get("girl orgasms", 0) > 2:
        if used_obedience:
            the_person "Oh, fuck... baby... I loved what you did to me... I never knew being submissive could feel so good, and I never knew I could cum so hard!"
            mc.name "I do enjoy when you keep begging me to make you cum again. It's almost like you're addicted to it, and I'm happy to be your fix."
            the_person "Shut up and kiss me, [mc.name]... I need more of your cock, and I need it now!"
        else:
            the_person "I have never... cum that hard... It was just amazing... I guess I needed that, and I guess I need more of it!"
            "She seems dazed by her orgasm as she tries to form coherent sentences, and she's still shaking with pleasure."
            the_person "You really... know how to give a girl a good time... just gimme a second to catch my breath, and then let's do it again!"
            mc.name "Take your time, I'm not going anywhere, and I'm not done with you yet."
            the_person "Thanks, [mc.name]... I think I need a minute to recover before we can start again, but I'm already looking forward to it!"

        call sex_review_trance(the_person) from _call_sex_review_trance_slutty_sex_review

    #No special conditions, just respond based on how orgasmed and how slutty the position was.
    elif the_report.get("girl orgasms", 0) > 0 and the_report.get("guy orgasms", 0) > 0: #You both came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position cap, it was tame
            the_person "Ah, that was fucking nice... But I think we could go even further next time. I'm not afraid to push the limits, [mc.name], and I'm not afraid to get a little dirty."
            the_person "Doesn't that sound like fun? I'm getting wet just thinking about it, and I'm already looking forward to our next adventure together!"

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "Ah, that was just what I needed! I think we're very compatible, [mc.name], and I think we could have a lot of fun together."
            the_person "Let's do it again some time soon, okay? I want to see how much further we can go, and I want to explore all the possibilities with you."

        elif used_obedience: #She only did it because she was commanded
            the_person "Fuck, I... I didn't think I was going to cum like that. I guess I just can't resist a good command, huh?"
            mc.name "Aren't you going to thank me? You obviously had a good time, and you obviously enjoyed being told what to do."
            the_person "Shut up and don't get too full of yourself, [mc.name]. I may have enjoyed it, but I'm still a dirty little slut, and I'll do what I want, when I want."

        else: # She's surprised she even tried that.
            the_person "Oh, fuck, that was intense! I didn't think I was going to take it so far, but it just felt right, you know?"
            the_person "Don't think that's going to happen every time though, alright? I'm not a slut! I just like to push my boundaries sometimes, and I just like to have a little fun."
        if the_person.love > 40:
            the_person "You know, I never thought I'd say this, but I think I might actually like this whole 'relationship' thing with you, [mc.name]. You're not so bad for a guy, and you're definitely not boring."
        else:
            the_person "Well, that was fun. Let's do it again sometime, but not too soon, okay? I need to recover my dignity first, and I need to make sure I'm ready for more of your cock."

    elif the_report.get("girl orgasms", 0) > 0: #Only she came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            the_person "Done already? Well, that's just not right. Next time I'm going to make sure we both cum and then some, and next time I'm going to make sure you're not so quick to finish."
            the_person "I've got a few ideas that are going to blow you away, [mc.name], and I've got a few tricks up my sleeve that are going to make you beg for more."
            "She smiles mischievously, already imagining your next encounter and already planning her next move."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "You're all done? Well, that was fucking hot either way, [mc.name]."
            the_person "I'll repay the favour next time, alright? I promise. And maybe we can try something new, something a little more exciting, something a little more dirty."
            "She leans in close, whispering in your ear and making you shiver with anticipation."

        elif used_obedience: #She only did it because she was commanded
            the_person "That's it? I mean, not like I wanted to do anything more, I just thought you were going to finish, and I just thought you were going to make me cum again."
            mc.name "Some other time. I just wanted to see what you look like when you cum, and I just wanted to see how far you'd go."
            the_person "I... Fuck, well, I guess you got what you wanted. But don't think I'm going to make it easy for you next time, and don't think I'm going to be so quick to obey."
            the_person "It could have been worse, I guess. At least I got to cum, and at least I got to have a little fun."

        else: # She's surprised she even tried that.
            the_person "Oh, fuck, that was intense! You really know how to make a girl feel good, [mc.name], and you really know how to make me cum."
            the_person "You're probably tired after all that work, but I'm not, and I'm ready for more. I promise I'll repay the favour next time, okay? And maybe we can try something different, something a little more exciting."
            "She smiles, already looking forward to your next encounter and already planning her next move."

    elif the_report.get("guy orgasms", 0) > 0: #Only you came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            the_person "Hmph, you're all tired out already? That's so frustrating! I was just getting started, and I was just getting into it."
            mc.name "Sorry, I'll make it up to you next time."
            the_person "Well, I suppose I could be persuaded to try again. But don't expect any special treatment, and don't expect me to go easy on you."
            mc.name "Yeah, I think I could handle that. I think I could handle a little more of your dirty little slutty ways."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "You're already done? Such a tease! Fine, I'll let you off this time, but don't think you're getting off that easy."
            mc.name "Sorry, I'll make it up to you next time."
            the_person "You'd better, or you won't be hearing the word 'please' from me again. You'll be hearing the word 'more', and you'll be hearing the word 'now'."

        elif used_obedience: #She only did it because she was commanded
            the_person "I suppose you're worn out from all that... We're finished then?"
            mc.name "Yeah, that's all for now."
            the_person "Fine, but don't think this means you get to slack off next time. I expect more from you, and I expect better."

        else:  # She's surprised she even tried that.
            the_person "Wow, that was... quite an experience. I think I got a little carried away there, and I think I might have gotten a little too into it."
            the_person "Maybe it's for the best that we stop here. I need to think about what I just did, and I need to think about what I want to do next."

    elif the_person.energy < 10: #Nobody came and she's tired
        the_person "Ugh, I'm so exhausted! I think I need a nap, and I think I need a break from all this sex."
        mc.name "No worries, we'll do it another day."
        the_person "Just don't expect any special treatment when we try again, got it? I'll be ready for you next time, and I'll be ready to take control."

    else: #Nobody came.
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            the_person "Hmph, you're already done? What's the rush? We could've had more fun, and we could've gone further."
            "She crosses her arms, pretending to be upset, but you can tell she's just teasing."
            the_person "You're such a spoilsport [the_person.mc_title]. You're always stopping before things get interesting."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "We're stopping? But we were just getting to the good stuff! I was just starting to get into it, and I was just starting to have fun."
            mc.name "Sorry [the_person.title], maybe another time."
            the_person "Yeah, maybe. You can't just leave a girl hanging like that, you know. You have to finish what you started."

        elif used_obedience: #She only did it because she was commanded
            the_person "Well, I wasn't expecting that. I thought you had more in mind, and I thought you were going to take things further."
            mc.name "You aren't disappointed, are you?"
            the_person "No, no. I just...wanted to see where things would go, that's all. I just wanted to see how far you'd take me."
            the_person "It's fine. I'll just have to find someone else to take me further, I suppose."

        else:  # She's surprised she even tried that.
            the_person "Ugh, you're probably right. We should stop now before we get too carried away. I don't want to do something I'll regret later."
            the_person "Let's just keep this casual, okay? I don't want to get too attached, and I don't want to get too involved."

    # Gave creampie while she is not on birth control (extra dialogue when she could get pregnant)
    if the_report.get("creampies", 0) > 0 and not the_person.on_birth_control and not the_person.knows_pregnant:
        the_person "Well, I guess we just made things a little more interesting, didn't we?"
        the_person "If I get pregnant, it'll serve you right for being so reckless! You should have used a condom, and you should have been more careful."
        the_person "But at the same time, I have to admit, the thought of getting pregnant is kind of exciting. It's kind of thrilling to think about having a baby, and it's kind of thrilling to think about being a mommy."
        the_person "I guess we'll just have to wait and see what happens, won't we? We'll just have to wait and see if I get pregnant, and we'll just have to wait and see what the future holds."

    $ del comment_position
    return

## Role Specific Section ##

label slutty_improved_serum_unlock(the_person):
    mc.name "[the_person.title], now that you've had some time to get used to the lab, there's something I want to talk to you about... something that's been on my mind for a while now."
    the_person "Yeah, what's on your dirty little mind, [mc.name]?"
    mc.name "Our R&D up to this point has been based on my old notes from university, but I think we can take it to the next level... a level that's a little more... personal."
    mc.name "There were some unofficial experiment results that suggested the effects might be enhanced by sexual arousal... and I think we should explore that further."
    "[the_person.title] raises an eyebrow, a sly smile spreading across her face."
    the_person "Ah, so you noticed that too? I have a hypothesis that an orgasm opens chemical receptors that are normally blocked... and I think we should test that hypothesis."
    mc.name "What if that's true? Does that open up any more paths for our research?"
    the_person "If it's true, I could leverage the effect to induce greater effects in our subjects... and maybe even in myself."
    "[the_person.possessive_title!c] grins mischievously, her eyes sparkling with excitement."
    the_person "We'll need to do some experiments to be sure... and I think I have just the thing in mind."
    mc.name "What kind of experiments?"
    the_person "I want to take a dose of serum myself, and you can record the effects... and then I'll...ahem...stimulate myself, and we can compare the effects after."
    the_person "I want to see just how far we can push the limits of this serum... and just how far we can push the limits of my own body."
    mc.name "Do you really think that's a good idea?"
    the_person "Not really, but we can't trust anyone else with this information if we're right... and besides, I'm a dirty little slut who loves to take risks."
    the_person "We might be able to make progress by brute force, but this is a chance to take our research to the next level... and to take our relationship to the next level."
    the_person "A finished dose of serum that raises my Suggestibility... the higher it gets, the better. I want to be completely under your control, [mc.name]."
    the_person "Then we'll just need some time and some privacy for me to see what sort of effects my...ahem...stimulation will have... and for you to see just how far you can push me."
    return

## Taboo break dialogue ##

label slutty_kissing_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 30:
        the_person "Oh, for fuck's sake, just kiss me already! You've been eye-fucking me for weeks, and I'm getting tired of waiting."
        mc.name "I'm not just going to kiss you out of nowhere, you know."
        the_person "Bullshit, you've been wanting to kiss me since the moment you met me. Don't play dumb, [mc.name]."
        mc.name "Maybe I have, but that doesn't mean I'm just going to jump at the chance."
        the_person "Oh, come on, don't be shy. I can see the lust in your eyes from across the room."
        mc.name "Alright, alright. But don't say I didn't warn you."
        the_person " Warn me? Ha! I'm a dirty little slut who loves to get kissed, and I'm not afraid of anything."
    elif the_person.love >= 20:
        the_person "So we're finally going to make out, huh? About time, if you ask me. I've been wanting to taste your lips for weeks."
        mc.name "I guess we are. What do you think?"
        the_person "I think it's about time we took things to the next level, [the_person.mc_title]. And I think it's about time we got a little more intimate."
        mc.name "I'm glad you feel that way."
        the_person "Me too. Just be gentle, okay? I don't want to get too carried away... yet."
        mc.name "I will. But don't worry, I'll make sure you get carried away eventually."
    else:
        the_person "I don't know if this is a good idea, [the_person.mc_title]. We're taking things too fast, aren't we? I mean, I barely know you, and already we're making out like a couple of teenagers."
        mc.name "Are you scared?"
        the_person "No! I'm just...not sure if this is a good idea. But at the same time, I really want to do it. I really want to kiss you and see where things go."
        mc.name "Good. Because I'm not going to let you back out now. I'm going to make sure you follow through on this, and I'm going to make sure you enjoy it."
        the_person "Hmph. Fine. But if this is a mistake, it's on you. And if I end up getting hurt, I'm blaming you."
        mc.name "It'll be worth it, I promise. And I'll make sure you don't get hurt... unless you want me to, that is."
    return

label slutty_touching_body_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 30:
        the_person "Oh, come on then, don't be shy. You've wanted to touch me for ages, haven't you? You've wanted to feel my tits and my ass and my pussy, and now's your chance."
        mc.name "Hey, I'm not that obvious!"
        the_person "Oh, please. I can see the way you look at me. I can see the lust in your eyes, and I can see the way you're practically drooling over me."
        mc.name "Well, I guess I am a little obvious. But can you blame me? You're a beautiful woman with a body that's just begging to be touched."
        the_person "Pfft, you're just trying to get in my pants. But I'm not going to make it easy for you. You're going to have to work for it, [mc.name]."
    elif the_person.love >= 20:
        the_person "So you're ready for this? You're ready to touch me and feel me and explore my body?"
        "You nod, and she smiles."
        the_person "Me too, I think. I didn't think I'd be so nervous when you actually made a move, but now that it's happening, I'm kind of excited."
        mc.name "Just relax. You trust me, right?"
        the_person "Of course. Just don't expect me to be all touchy-feely about it. I'm still a little shy, and I still need to get used to this."
        mc.name "I will. But don't worry, I'll make sure you get used to it eventually. I'll make sure you start to crave my touch, and I'll make sure you start to love the way I make you feel."
    else:
        the_person "I think you're getting a little ahead of yourself here [the_person.mc_title]. I mean, I barely know you, and already you're trying to feel me up like we're a couple or something."
        mc.name "What do you mean?"
        the_person "I mean I don't just let anyone touch me like that. Maybe we should cool things down and get to know each other a little better before we start getting all intimate and stuff."
        mc.name "You're not scared, are you?"
        the_person "Scared? Of course not! I'm just...cautious, that's all. I don't want to rush into anything that might end up being a mistake."
        mc.name "Well then just relax and go with it. It doesn't have to mean anything unless we want it to, and we can always stop if you start to feel uncomfortable."
        "You see her answer in her eyes before she says anything, and you know that she's already made up her mind."
        the_person "You're so bad for me, you know that? You're like a corrupting influence or something, always trying to get me to do things that I know I shouldn't be doing."
        mc.name "Well let me make up for it then. Let me show you that I'm not all bad, and that I can be good for you too."
        the_person "Hmm, maybe I'll let you. But don't think that this means anything, okay? I'm still not committing to anything, and I'm still not promising you anything."
    return

label slutty_touching_penis_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 35:
        the_person "Oh, you're really enjoying this, aren't you? Look how hard you are, you dirty little boy."
        mc.name "Do you want to feel it? You can if you want, I dare you."
        the_person "Yeah, why not? I'll try not to hurt it... but no promises, I'm a dirty little slut who loves to play rough."
        "She reaches out and wraps her hand around your cock, her touch firm and confident."
        the_person "Mmm, you're so big and hard, I just can't resist."
        mc.name "Go ahead, take a closer look. See how hard you can make me."
        the_person "Oh, I think I can make you a lot harder than this... with just a few strokes of my hand."

    elif the_person.love >= 20:
        the_person "Your cock looks so nice when it's hard. Can I touch it, please? I want to feel it in my hand."
        mc.name "Go ahead, it doesn't bite... unless you want it to."
        the_person "Well, it might if you're not careful... but I think I can handle it."
        "She reaches out and wraps her hand around your cock, her touch gentle but firm."
        the_person "Mmm, you're really nice when you're hard. I think I might just have to keep you like this all the time."

    else:
        mc.name "My cock is so hard right now [the_person.title]. Put your hand on it and touch it for me, please."
        the_person "What? That's taking things a little far, don't you think? I'm not sure I'm ready for this."
        mc.name "Come on, you know you want to. Just a few strokes, then if you aren't impressed you can stop. I dare you."
        the_person "Fine, but don't expect me to make any promises after this. I'm only doing this because I'm a dirty little slut who loves to take risks."
        mc.name "I wouldn't dream of it. I just want to see how far you'll go."
        the_person "Hmm, okay then. I'll give it a try... but don't say I didn't warn you."
    "She reaches out and wraps her hand around your cock, her touch gentle but firm."
    "You feel a surge of pleasure as she starts to stroke you, and you know that this is just the beginning."
    the_person "Mmm, you're really nice when you're hard. I think I might just have to keep you like this all the time."
    return

label slutty_touching_vagina_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 35:
        the_person "Come on, don't be shy. You've been dying to touch my pussy, admit it. You've been dreaming about it for weeks."
        mc.name "I guess I have. But I didn't think you'd be so willing to let me."
        the_person "Why not? I'm a dirty little slut who loves to get touched. I love to feel fingers inside me, and I love to feel cocks inside me."
        "She spreads her legs wide, inviting you to touch her."
        the_person "Go ahead, take a closer look. See how wet you can make me."

    elif the_person.love >= 20:
        the_person "Oh fuck, you've got my pussy tingling. I want you to touch it [the_person.mc_title], please."
        mc.name "You sure? I don't want to push you too far."
        the_person "No, I want it. I want you to touch me, and I want you to make me cum. I'm a dirty little slut who loves to get off."
        "She spreads her legs wide, inviting you to touch her."
        the_person "Go ahead, take a closer look. See how wet you can make me."

    else:
        the_person "I don't know if we should be doing this [the_person.mc_title]... it feels so wrong, but it feels so right at the same time."
        mc.name "Just take a deep breath and relax. I'm just going to touch you a little, and if you don't like it I'll stop. I promise."
        the_person "Just a little?"
        mc.name "Just a little. Trust me, it's going to feel amazing. You're going to love it."
        the_person "Hmm, okay. But don't think this means I'm easy. I'm just a dirty little slut who loves to take risks."
        mc.name "I wouldn't dream of it. I just want to see how far you'll go."
    return

label slutty_sucking_cock_taboo_break(the_person):
    mc.name "I want you to do something for me, something that's going to make me feel really good."
    the_person "Oh yeah? What do you want me to do to you, huh? You want me to suck your cock, don't you?"
    mc.name "That's exactly what I want. I want you to suck on my cock and make me cum."
    if the_person.effective_sluttiness() >= 45:
        the_person "Mmm, I think I'm up for that. It's not going to be too big for me, is it? I don't want to choke on it... or do I?"
        mc.name "I think you'll be able to handle it. You seem like a gal who can take a lot."
        the_person "Alright, I don't want it choking me... but a little choking is okay. I like it when it's a little rough."
        "She bites her lip and winks at you, her eyes sparkling with excitement."
        the_person "Let's get started, I'm ready to suck your cock and make you cum."

    elif the_person.love >= 30:
        the_person "I guess we've been dancing around it for a while, but I'm ready to take the plunge. I'm ready to suck your cock and see where it takes us."
        "She bites her lip and looks your body up and down, her eyes lingering on your cock."
        the_person "Alright, let's do this. I'm ready to make you feel good, and I'm ready to get a little dirty."

    else:
        the_person "Oh, I was wondering if this was going to come up... I mean, I've been thinking about it a lot, and I have to admit, I'm a little curious."
        "She laughs nervously and looks away from you, her face flushing with embarrassment."
        the_person "I don't know [the_person.mc_title]... I'm not sure if I'm ready for this. But at the same time, I don't want to say no. I want to see where this takes us, and I want to see how far we can go."
        "You reach up and hold her chin, turning her head back to face you. You can see the desire in her eyes, and you know that she's ready to take the next step."
        mc.name "Don't overthink it. Just kneel down and suck on it for me. If you don't like doing it, we can just forget it happened."
        "You can see in her eyes the moment her resolve breaks. She bites her lip and nods, her face set in a determined expression."
        the_person "Alright, let's do this. I'm ready to suck your cock and see where it takes us."
        "She slowly gets down on her knees, her eyes darting between your face and your cock with a mix of reluctance and curiosity."
        the_person "You know, I never thought I'd be doing this. But I guess I'm willing to try new things for you... and for myself."
        "She takes a deep breath, her hand wrapping around the base of your cock as she leans in to take it in her mouth."
        "As she starts to suck, her eyes flash up to meet yours, a hint of defiance and challenge in them."
        the_person "Satisfied now? You got what you wanted, didn't you?"

    return

label slutty_licking_pussy_taboo_break(the_person):
    mc.name "I want to taste your pussy [the_person.title]. Are you ready for me to lick you and make you cum?"
    if the_person.effective_sluttiness() >= 45:
        the_person "Hmph, I don't need your permission or anything, but fine. I'm ready for you to lick my pussy and make me cum."
        mc.name "Good. But don't expect me to go easy on you just because it's your first time. I'm going to make you cum hard, and I'm going to make you scream my name."
        the_person "Oh, please. I've had better. I've had guys who know how to make me cum, and I've had guys who know how to make me scream. But I'm willing to give you a chance... for now."

    elif the_person.love >= 30:
        the_person "Finally, a man who knows how to treat a woman right. I'm ready when you are, and I'm ready to see where this takes us."
        mc.name "That's what I like to hear. I'm going to make you feel good, and I'm going to make you cum. And when I'm done, you're going to be begging for more."

    else:
        if the_person.has_taboo("sucking_cock"):
            the_person "You know, I never thought I'd see the day where you'd be willing to do this. But I guess I'm not going to complain. Just don't expect me to be all grateful or anything."
            "She bites her lip and smirks at you, her eyes sparkling with amusement."
            the_person "But fine, I'm ready. Just don't expect me to be all appreciative or anything. I'm only doing this because I want to, not because I have to."
        else:
            the_person "About time you decided to make up for not sucking my cock. But fine, I'm ready. Just don't expect me to be all impressed or anything. I've had better, and I've had worse."
            "She rolls her eyes and smiles, her face set in a sarcastic expression."
            the_person "But go ahead, try your best. Try to make me cum, and try to make me scream. I dare you."

    "She lies back, her eyes darting between yours and the area you're about to explore. You can see the desire in her eyes, and you know that she's ready to take the next step."
    the_person "And don't think this means I'm some kind of slut for letting you do this. I'm just a woman who knows what she wants, and I'm just a woman who's willing to take risks."
    mc.name "I wouldn't dream of it. You're just being a good sport, right?"
    the_person "Something like that... but don't think this means I'm going to go easy on you. I'm going to make you work for it, and I'm going to make you earn it."
    "She closes her eyes, her face flushed with embarrassment as you start to lick her. You can hear her breathing, and you can feel her body tensing up with anticipation."
    return

label slutty_vaginal_sex_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 60:
        the_person "Ugh, finally! I've been waiting for this moment all night. Come on then, get that cock inside me and fuck me like you mean it! I'm ready to take it, and I'm ready to cum."
        mc.name "I'm going to make sure you remember this. I'm going to make sure you cum hard, and I'm going to make sure you scream my name."
        the_person "Bring it on! I can take it. I'm a dirty little slut who loves to get fucked, and I'm a dirty little slut who loves to cum."

    elif the_person.love >= 45:
        the_person "Alright, show me what you've got. I'm ready for this, and I'm ready to see where it takes us. I'm ready to feel your cock inside me, and I'm ready to feel you cum."
        mc.name "You better be. I'm going to make sure you remember this. I'm going to make sure you cum hard, and I'm going to make sure you scream my name."
        the_person "I'm not afraid of you. I'm not afraid of your cock, and I'm not afraid of what you can do to me. I'm a woman who knows what she wants, and I'm a woman who's willing to take risks."

    else:
        if the_person.has_taboo("anal_sex"):
            the_person "Well, well, well. Look at that cock. I guess we're going to find out just how tight my pussy is. And I guess we're going to find out just how much I can take."
            mc.name "That's the plan. And if you're a good girl, I might just make it worth your while. I might just make you cum, and I might just make you scream my name."
            the_person "Hmph, I'm always good. Now get to it before I change my mind. I'm not going to wait all day for you to make your move."
        else:
            the_person "Oh, so that's what you're going to do with that big cock of yours. Well, I guess we'll see how it feels. And I guess we'll see how much I can take."
            mc.name "We sure will. And if you're lucky, I might just make it feel even better. I might just make you cum, and I might just make you scream my name."
            the_person "Ugh, just get on with it already! I'm not getting any younger, and I'm not getting any more patient. I want to feel your cock inside me, and I want to feel you cum."

    return

label slutty_anal_sex_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 75:
        the_person "Ugh, fine. But only because I can't resist you. Your cock is so big, I'm surprised it fits in your pants! And I'm surprised you can even walk with that thing."
        "She seems more excited by the prospect than intimidated, and she seems more eager to get started than hesitant."
        mc.name "Don't worry, I'll take it slow and make sure you're comfortable. I'll make sure you're ready for this, and I'll make sure you can take it."
        the_person "I'm not worried. I'm a dirty little slut who loves to get fucked, and I'm a dirty little slut who loves to take risks. I'm ready for this, and I'm ready to see where it takes us."

    elif the_person.love >= 60:
        the_person "Are you sure you want to do this? I'm not exactly the most experienced person when it comes to anal... but I'm willing to try new things, and I'm willing to take risks."
        mc.name "I'll be gentle, don't worry. I'll make sure you're comfortable, and I'll make sure you're ready for this. I'll make sure you can take it, and I'll make sure you enjoy it."
        the_person "Alright, but if it hurts too much, I'm stopping. I'm not going to do something that doesn't feel good, and I'm not going to do something that doesn't make me cum."

    else:
        if the_person.has_taboo("vaginal_sex"):
            the_person "Wait, are you sure you want to do this? My ass might be too tight for your cock! And I might not be able to take it... but at the same time, I might just love it."
            mc.name "I'll make it fit, but you might feel a little sore afterward. You might feel a little stretched out, and you might feel a little used."
            the_person "Oh, great. Just what I needed. But at the same time, I'm kind of excited. I'm kind of eager to see where this takes us, and I'm kind of eager to feel your cock inside me."
        else:
            the_person "Come on, [mc.name]. Let's just get this over with. I don't know what's gotten into me today, but I'm feeling a little reckless. I'm feeling a little wild, and I'm feeling a little crazy."
            mc.name "Are you sure you're okay with this?"
            the_person "Of course, I'm just... nervous. And a little embarrassed. But let's just do this already! I'm ready when you are, and I'm ready to see where it takes us."
            "She blushes and looks away, her face set in a determined expression."
            mc.name "Alright, let's get started then. Let's see where this takes us, and let's see how far we can go."
            the_person "Hurry up, I'm ready when you are. I'm ready to feel your cock inside me, and I'm ready to feel you cum."
    return

label slutty_condomless_sex_taboo_break(the_person):
    if the_person.knows_pregnant:
        the_person "Ugh, you really want to do it without a condom? Fine, but don't say I didn't warn you. I'm a dirty little slut who loves to take risks, but I'm not stupid... just horny."
        if the_person.wants_creampie:
            the_person "If you're going to cum inside me, please make it worth my while. I want to feel your hot cum dripping down my thighs, and I want to taste it on my lips."
        else:
            the_person "Just make sure to cover me with your... you know, stuff. I want to feel like a dirty little slut, not a mom-to-be."

    elif the_person.opinion.bareback_sex > 0:
        the_person "Whatever, you want to do it bareback, huh? Just don't say I didn't warn you. I'm a dirty little slut who loves to get fucked, but I'm not a fool."
        if the_person.on_birth_control:
            the_person "I'm on the pill, so you don't have to worry about it. But don't think that means you can just cum inside me whenever you want. I'm still a dirty little slut who likes to play safe."
            $ the_person.update_birth_control_knowledge()
        elif the_person.wants_creampie:
            the_person "But if you're going to cum inside me, you'd better make it worth my while. I want to feel like a dirty little slut who's been used and abused, not just a quick fuck."
        elif the_person.opinion.creampies < 0:
            the_person "Just don't get me pregnant, okay? That would be a huge pain in the ass, and I'm not ready for that kind of responsibility. I'm a dirty little slut, not a mom."
        else:
            the_person "Alright, just make sure you pull out this time. I don't want to get pregnant, but I do want to feel like a dirty little slut who's been fucked hard."

    elif the_person.love > 60:
        if the_person.on_birth_control:
            the_person "Ugh, fine, I'm on the pill. Don't say I didn't warn you. But don't think that means you can just cum inside me whenever you want. I'm still a dirty little slut who likes to play safe."
            $ the_person.update_birth_control_knowledge()
        elif the_person.wants_creampie:
            the_person "You're always trying to make me do stupid things, aren't you? Fine, if we're going to do this, make it worth my while. I want to feel like a dirty little slut who's been used and abused, not just a quick fuck."
            mc.name "Are you on the pill?"
            "She rolls her eyes."
            the_person "No, I'm not. But if you're going to cum inside me, you'd better make it worth it. I want to feel like a dirty little slut who's been fucked hard, not just a quick screw."
            $ the_person.update_birth_control_knowledge()
        elif the_person.opinion.creampies < 0:
            the_person "You're always trying to make me do stupid things, aren't you? Fine, just don't get me pregnant. I'm not ready for that kind of responsibility, and I'm not ready to be a mom."
            the_person "I'm a dirty little slut who loves to get fucked, but I'm not a fool. I know what I want, and I know what I don't want."
        else:
            the_person "You're always trying to make me do stupid things, aren't you? Fine, just make sure you pull out this time. I don't want to get pregnant, but I do want to feel like a dirty little slut who's been fucked hard."
            if the_person.kids == 0:
                the_person "I need you to pull out though. I'm not quite ready to be a mother, even with you. I'm a dirty little slut who loves to get fucked, but I'm not ready for that kind of responsibility."
            elif the_person.kids == 1:
                the_person "I need you to pull out though. I've already got a kid, I don't need another one. I'm a dirty little slut who loves to get fucked, but I'm not ready for that kind of responsibility again."
            else:
                the_person "I need you to pull out though. I've already got kids, I don't need another one. I'm a dirty little slut who loves to get fucked, but I'm not ready for that kind of responsibility again."

    else:
        if the_person.on_birth_control:
            the_person "Hmph, you want to get busy without a rubber? Well, I'm on the pill, so I guess it's fine. Just don't expect any special treatment, and don't think that means you can just cum inside me whenever you want."
            $ the_person.update_birth_control_knowledge()
        elif the_person.has_taboo("vaginal_sex"):
            the_person "You're really not going to use a condom? I'm not on the pill, so we could end up with a little surprise. But at the same time, I'm a dirty little slut who loves to take risks, and I'm a dirty little slut who loves to get fucked."
            $ the_person.update_birth_control_knowledge()
            the_person "Or is this your sneaky plan to make a baby out of me? Because if it is, I'm not interested. I'm a dirty little slut who loves to get fucked, but I'm not ready to be a mom."
            mc.name "I swear I'll pull out. I want our first time to be memorable, and I want you to feel like a dirty little slut who's been used and abused."
            "She crosses her arms and gives a half-hearted sigh."
            the_person "Ugh, fine. But you better pull out, or you'll regret it. I'm a dirty little slut who loves to get fucked, but I'm not a fool."
        else:
            the_person "You're really not going to use a condom? I'm not on the pill, so we could end up with a little surprise. But at the same time, I'm a dirty little slut who loves to take risks, and I'm a dirty little slut who loves to get fucked."
            $ the_person.update_birth_control_knowledge()
            the_person "Or is this your sneaky plan to make a baby out of me? Because if it is, I'm not interested. I'm a dirty little slut who loves to get fucked, but I'm not ready to be a mom."
            mc.name "I promise I'll pull out. It'll feel so much better without anything between us, and you'll feel like a dirty little slut who's been used and abused."
            the_person "God, I know. I'm trying to be rational here, not some lust-driven animal. But at the same time, I'm a dirty little slut who loves to get fucked, and I'm a dirty little slut who loves to take risks."
            "She huffs and puffs."
            the_person "Fine, no condom. Just remember to pull out, got it? Good. I'm a dirty little slut who loves to get fucked, but I'm not a fool."
    return

label slutty_underwear_nudity_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > 30 - (the_person.opinion.skimpy_outfits * 5):
        the_person "You want to see me in my underwear, huh? Well, isn't that just the most exciting thing you've ever heard? I'm a dirty little slut who loves to show off her body, and I'm more than happy to oblige."
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "What are we waiting for then, let's get this off of you and see what's underneath. I bet you're just dying to show me your tits and pussy."
            the_person "Shut up and take my clothes off, I'm ready to get naked and show you what I've got."
        else:
            mc.name "Yeah, yeah. We've been over this. You're not exactly subtle about it, but I love the way you tease me with your body."
            the_person "Tease? Ha! I'm just getting started, baby. Now take my clothes off and let's get this party started."
    elif the_person.love > 15:
        the_person "You want me to strip down a little? Well, isn't that just the most romantic thing you've ever said? I'm a dirty little slut who loves to get naked and show off her body, and I'm more than happy to oblige."
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "Oh, don't give me that. You know you want to show off your body and get naked with me. I can see it in your eyes, and I can feel it in your touch."
            the_person "Fine, but if this gets out of hand, I'm blaming you. I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."
            mc.name "Promise?"
            the_person "Yeah, yeah. Now get this [the_clothing.display_name] off and let's get naked."
        else:
            mc.name "Yeah, I know. You've been teasing me for weeks, and I'm more than ready to take the bait. Now let's get you out of these clothes and see what's underneath."
            the_person "Ugh, fine. But don't think this means I'm going easy on you. I'm a dirty little slut who loves to get fucked, and I'm going to make sure you know it."
            "She slowly starts taking [the_clothing.display_name] off, revealing her underwear underneath."

    else:
        the_person "You really want to see me like this? Fine, but don't say I didn't warn you. I'm a dirty little slut who loves to get naked and show off her body, and I'm not going to apologize for it."
        the_person "If you take my [the_clothing.display_name] I'll only have my underwear on, you know that? But I'm not going to stop there. I'm going to take it all off and show you what I've got."
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "Yeah, that's kind of the point. I want to see your tits and pussy, and I want to touch them and taste them."
            "She shakes her head and laughs to herself, a sly smile spreading across her face."
            the_person "Whatever, but if you think I'm doing this because I want to... well, you're right. I am doing it because I want to. I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."
        else:
            mc.name "Yeah, I know. You're not exactly shy, and I love that about you. Now let's get you out of these clothes and see what's underneath."
            the_person "Fine, but don't think this means I'm going easy on you. I'm a dirty little slut who loves to get fucked, and I'm going to make sure you know it."
    return

label slutty_bare_tits_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > (40 - the_person.opinion.showing_her_tits * 5):
        the_person "Why do you want to see my tits now, all of a sudden? Like I don't already know you're checking me out. You're always staring at my chest, and I love it."
        if the_person.has_large_tits:
            "She reluctantly shakes her chest for you, jiggling the [the_person.tits_description] hidden underneath her [the_clothing.display_name]. Her tits are huge and ripe, just begging to be touched and sucked."
        else:
            "She reluctantly shakes her chest and gives her [the_person.tits_description] a little jiggle. Her tits are small but perky, just begging to be touched and sucked."
        the_person "You're always so eager, aren't you? I guess I can show you, but don't get too excited. I'm a dirty little slut who loves to tease, and I'm not going to give it up that easily."
        if the_person.has_large_tits:
            mc.name "Oh, I've been looking. Now let's get those puppies out where I can enjoy them. I want to touch them and suck them and make you cum."
        else:
            mc.name "Oh, I've been looking. Now let's get those cute little things out. I want to touch them and suck them and make you cum."

    elif the_person.love > 25:
        the_person "Are you really sure you want to see my tits, [the_person.mc_title]? Because once you see them, you're going to want to touch them and suck them and make me cum."
        if the_person.has_large_tits:
            "She rolls her eyes and shakes her chest, jiggling her nice [the_person.tits_description], barely restrained by her [the_clothing.display_name]. Her tits are huge and ripe, just begging to be touched and sucked."
        else:
            "She rolls her eyes and shakes her chest, giving her [the_person.tits_description] a little jiggle. Her tits are small but perky, just begging to be touched and sucked."
        mc.name "Of course I am. You know I love your tits, and I love the way you tease me with them."
        the_person "Well, I suppose you're entitled to see them then... but don't think this means I'm going to start showing them off to everyone. I'm a dirty little slut who loves to get fucked, but I'm not a exhibitionist... yet."

    else:
        the_person "Wait, no! Don't look at me like that! You should at least ask a girl before you try and put her tits on full display! But at the same time, I love the way you look at me, and I love the way you make me feel."
        mc.name "Come on, don't be like that. I bet your tits look great, and I bet you love showing them off. You're a dirty little slut who loves to get fucked, and I'm not going to apologize for it."
        the_person "They do, but I still feel a little self-conscious about being naked around you, alright? But at the same time, I love the way you make me feel, and I love the way you touch me."
        mc.name "There's no need to be. Just relax and let me take your [the_clothing.display_name] off for you. I want to see your tits and touch them and suck them and make you cum."
        the_person "Ugh, fine... but don't think this means I'm going to start showing off my body to everyone! I'm a dirty little slut who loves to get fucked, but I'm not a exhibitionist... yet."
    return

label slutty_bare_pussy_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > (50 - the_person.opinion.showing_her_ass * 5):
        the_person "So you want to see my pussy, huh? Like I don't already know you're thinking about it. You're always thinking about my pussy, aren't you?"
        if the_person.has_taboo("touching_vagina"):
            "She reluctantly lifts her hips, allowing you to slowly remove her [the_clothing.display_name] and reveal her pussy. Her legs spread wide, giving you a perfect view of her wet, pink slit."
        else:
            "She lifts her hips, giving you a quick glimpse of her pussy before covering it back up. But you can tell she's just teasing you, and she's ready to show you more."
        the_person "Well, you got your wish. Don't say I didn't warn you. My pussy is hot and wet, and it's all yours to play with."

    elif the_person.love > 35:
        the_person "You want to see my pussy, really? Are you sure you're ready for that? Because once you see it, you're going to want to touch it and taste it and make me cum."
        if the_person.has_taboo("touching_vagina"):
            mc.name "I think I am. I've been wanting to see it for a while. I've been dreaming about your pussy, and I need to see it for myself."
            the_person "Hmm, well... I suppose you've earned it. Just remember, you asked for this. My pussy is not for the faint of heart."
        else:
            mc.name "I've already felt it up, I thought I should see it too. I need to see your pussy, and I need to touch it and taste it."
            the_person "You really are persistent, aren't you? Fine, go on then. But don't say I didn't warn you. My pussy is hot and wet, and it's all yours to play with."

    else:
        the_person "Hold on, you're not getting me out of my [the_clothing.display_name] that easily! But at the same time, I'm kind of excited to show you my pussy. I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."
        if the_person.has_taboo("touching_vagina"):
            mc.name "Come on, just let me see it. I promise I'll be gentle. I'll touch it and taste it and make you cum, but I'll be gentle."
            the_person "You're such a liar... But fine, go ahead. I'm a dirty little slut who loves to get fucked, and I'm not going to say no to you."
        else:
            mc.name "I've already felt your pussy up, I want to get a look at it now. I need to see your pussy, and I need to touch it and taste it."
            the_person "You're so pushy! Alright, but don't say I didn't warn you. My pussy is hot and wet, and it's all yours to play with. But don't think this means I'm going to go easy on you. I'm a dirty little slut who loves to get fucked, and I'm going to make sure you know it."
    return

# label slutty_facial_cum_taboo_break(the_person):

#     return

# label slutty_mouth_cum_taboo_break(the_person):

#     return

# label slutty_body_cum_taboo_break(the_person):

#     return
#==================================================================

label slutty_creampie_taboo_break(the_person):
    if the_person.wants_creampie:
        if the_person.knows_pregnant:
            the_person "You want to get me pregnant, huh? Fine, I suppose it's about time someone knocked me up. I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."
            "She sighs happily, seeming almost resigned to the idea. Her legs spread wide, inviting you to cum inside her again."

        elif the_person.on_birth_control:
            if the_person.has_significant_other:
                the_person "Oh my god, I'm such a horrible [the_person.so_girl_title]! But I needed this so badly. I needed to feel your cum inside me, and I needed to feel like a dirty little slut."
                the_person "Maybe if we're lucky, my [the_person.SO_name] won't find out. But even if they do, I don't care. I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."
                "She looks at you with a mischievous grin, her eyes sparkling with excitement."

            else:
                the_person "Oh my god, I needed this so badly! Ah... I guess I'll just have to deal with the consequences. But I don't care. I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."
                "She sighs happily, her legs spread wide, inviting you to cum inside her again."

        elif the_person.effective_sluttiness() > 75 or the_person.opinion.creampies > 0:
            if the_person.has_significant_other:
                the_person "You want to get me pregnant? Fine, I suppose it's about time someone knocked me up. I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."
                the_person "Maybe my [the_person.SO_name] will finally notice how unhappy I am and do something about it. But even if they don't, I don't care. I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."

            else:
                the_person "You want to get me pregnant? Fine, I suppose it's about time someone knocked me up. I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."
                the_person "I guess I'll just have to deal with the consequences. But I don't care. I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."

            "She sighs happily, but with a hint of annoyance. Her legs spread wide, inviting you to cum inside her again."
            the_person "How long until you're ready for round two? I want as much of your cum inside my pussy as possible. I want to feel like a dirty little slut who's been used and abused."
            the_person "Just don't expect me to be all happy and grateful about it. I'm a dirty little slut who loves to get fucked, but I'm not going to apologize for it."

        else:
            if the_person.has_significant_other:
                the_person "Oh fuck... I'm such a terrible [the_person.so_girl_title]! But that felt so good... I needed to feel your cum inside me, and I needed to feel like a dirty little slut."
                "She sighs happily, but with a hint of guilt. Her legs spread wide, inviting you to cum inside her again."
                the_person "But I'm not going to apologize for it. I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."

            else:
                the_person "Oh fuck, that was so risky. But it felt so good... I needed to feel your cum inside me, and I needed to feel like a dirty little slut."
                "She sighs happily, but with a hint of annoyance. Her legs spread wide, inviting you to cum inside her again."
                the_person "But I'm not going to apologize for it. I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."
            the_person "I'll just have to hope you haven't knocked me up. We really shouldn't do this again, my luck is going to run out at some point. But I don't care. I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."
            the_person "Besides, I'm not exactly thrilled about the idea of being tied down to a man right now. But I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."

    else:
        if the_person.knows_pregnant:
            the_person "Ugh, you're kidding me, right? You got me pregnant? You're such a careless bastard, but I love it."

        elif not the_person.on_birth_control:
            the_person "Seriously? You didn't even use protection? What if I get pregnant? You're such a careless bastard, but I love it."

            if the_person.has_significant_other:
                the_person "What if you just got me pregnant? I would be the worst [the_person.so_girl_title] of all time! But I don't care. I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."

            else:
                the_person "What if I get pregnant? I'm not ready for that kind of responsibility! But I don't care. I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."
            the_person "You'd better start buying me chocolate and flowers to make up for this. I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."
            the_person "Next time, we're using condoms, or we're not doing it at all! You got it? But I don't care. I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."

        elif the_person.has_significant_other:
            the_person "Did you really just creampie me after I told you to pull out? You're such a careless bastard, but I love it."
            "She sighs unhappily, but with a hint of excitement."
            the_person "God, I'm such a terrible [the_person.so_girl_title]. Maybe next time I'll make you wear a condom as punishment. But I don't care. I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."

        elif the_person.opinion.creampies < 0:
            the_person "Ugh, this is so unpleasant. Couldn't you have at least made it worth my while? You're such a careless bastard, but I love it."
            "She rolls her eyes, but with a hint of excitement."
            the_person "Next time, at least have the decency to ask if I'm in the mood for a creampie. Or better yet, don't even bother if you're just going to be careless like this. But I don't care. I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."
            the_person "Next time, ask me first if I want a baby. But I don't care. I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."

        else:
            the_person "Are you serious right now? You're really going to give me that attitude after you just...you know? You're such a careless bastard, but I love it."
            "She huffs and crosses her arms, but with a hint of excitement."
            the_person "I swear, you're going to be the death of me. Fine, next time, at least have the decency to clean up after yourself. But I don't care. I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."
    return

label slutty_anal_creampie_taboo_break(the_person):
    if the_person.opinion.anal_creampies > 0:
        if the_person.effective_sluttiness() > 75 or the_person.opinion.anal_creampies > 1:
            if the_person.has_significant_other:
                the_person "Ugh, fine. I won't tell my [the_person.so_title] about this. But don't think I'm enjoying this... Oh wait, I totally am. I'm a dirty little slut who loves to get fucked in the ass."
                "She says this while wincing in pleasure as you fill her ass with your cream, her legs spread wide and her ass cheeks clenched tight."
                the_person "Ugh, it's just... weirdly satisfying, I guess... I mean, who wouldn't want a load of cum in their ass?"
            else:
                the_person "Ugh, finally! You're actually doing this! I've been waiting for this forever... I'm a dirty little slut who loves to get fucked in the ass, and I'm not going to apologize for it."
                the_person "Okay, okay, I know it's wrong, but... it feels so good... I mean, who wouldn't want a load of cum in their ass?"
            "She bites her lip, trying to contain her excitement, but her eyes sparkle with pleasure and her body trembles with anticipation."
            the_person "I guess it's nice... having your cum in my ass... I mean, it's not like I'm going to complain or anything. I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."
        else:
            if the_person.has_significant_other:
                the_person "Ugh, what are you doing? My [the_person.so_title] is going to kill me if he finds out about this... But at the same time, I'm kind of excited. I'm a dirty little slut who loves to get fucked in the ass, and I'm not going to apologize for it."
                "She moans softly as you continue to fill her ass, her legs spread wide and her ass cheeks clenched tight."
                the_person "Ugh, I can't believe I'm letting you do this... It's just so taboo... But at the same time, it's kind of hot. I mean, who wouldn't want a load of cum in their ass?"
            else:
                the_person "Ugh, promise you'll do this again? I can't believe I'm saying this, but... it's kind of hot... I mean, who wouldn't want a load of cum in their ass?"
                the_person "All that cum in my tight little ass... I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."

    else:
        if the_person.has_significant_other:
            the_person "Ugh, seriously? You couldn't pull out? My [the_person.so_title] is going to kill me... But at the same time, I'm kind of excited. I'm a dirty little slut who loves to get fucked in the ass, and I'm not going to apologize for it."
            "She starts to squirm and try to get away from you, but her eyes sparkle with pleasure and her body trembles with anticipation."
            the_person "Next time, just shoot your load on my ass, okay? I mean, it's not like I'm going to complain or anything. I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."
        elif the_person.opinion.anal_creampies < -1:
            the_person "Ugh, seriously? You can't even follow simple instructions? My ass is not a creampie dispenser! But at the same time, I'm kind of excited. I'm a dirty little slut who loves to get fucked in the ass, and I'm not going to apologize for it."
        else:
            the_person "Ugh, not inside! My ass is not a dirty little secret, although that sounds kind of hot... I mean, who wouldn't want a load of cum in their ass? I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."

    return

label slutty_dual_penetration_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 75:
        the_person "Ugh, why do you always have to push me to do this? Fine, but don't expect me to enjoy it... Just kidding, I'm going to love it. I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."
        "She rolls her eyes and crosses her arms, clearly annoyed but still willing to go through with it. Her legs spread wide, inviting you to penetrate her in both holes."
        mc.name "Don't worry, it'll be worth it. I promise you'll love it."
        the_person "I doubt that, but whatever. Just make sure to make it worth my while. I'm a dirty little slut who loves to get fucked, and I'm not going to settle for anything less."

    elif the_person.love >= 60:
        the_person "You're really sure about this? It's going to be a tight fit... But I'm willing to try. I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."
        mc.name "I'll make sure it fits perfectly. I promise you'll love it."
        the_person "Ugh, just be careful not to hurt me, okay? I don't want any scars... But at the same time, I'm kind of excited. I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."

    else:
        if the_person.has_taboo("vaginal_sex"):
            the_person "Are you sure my pussy wouldn't be tight enough for you? I mean, I've never done this before... But I'm willing to try. I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."
            mc.name "It's okay, I'll make it fit. Just try to relax. I promise you'll love it."
            the_person "Ugh, this is so embarrassing... But at the same time, I'm kind of excited. I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."

        else:
            the_person "Ugh, fine. I guess we're doing this, right? I mean, I can't back out now... But I'm willing to try. I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."
            mc.name "Are you sure you're ready for this?"
            the_person "Yeah, whatever. Let's just get this over with... I mean, let's just get this started. I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."

    return

label slutty_sleepover_yourplace_response(the_person): #Invited her over to spend the night
    if the_person.love >= 70:
        the_person "Ugh, fine. I'll come over and let you fuck me all night. But don't expect me to be all lovey-dovey or anything... I'm a dirty little slut who just wants to get fucked."
        mc.name "I wouldn't dream of it. We'll just have a good time and get dirty."
        the_person "Yeah, yeah. Just don't get too close, okay? I don't like cuddling or anything... unless it's with your cock inside me."
    elif the_person.sluttiness >= 80:
        the_person "Oh god, I'm so down for a dirty night of fucking and sucking. Make sure you have everything ready, so we can have a wild and crazy night!"
        mc.name "I'll make sure to have everything ready. I promise you'll have a night to remember."
        the_person "I better... or I'll be very disappointed. And trust me, you don't want to disappoint me."
    else:
        the_person "I guess I could come over... But don't expect me to do anything I'm not comfortable with, okay? Unless, of course, you can convince me to be a dirty little slut and do something naughty."
        mc.name "I'll try my best to convince you. But I promise I won't push you too hard... unless you want me to."
        the_person "We'll see about that... maybe I'll surprise you and be a dirty little slut after all."
    return

label slutty_sleepover_herplace_response(the_person): #Spending the night at her place
    if the_person.love >= 70:
        the_person "Ugh, fine. Come over and stay the night, and we can have a dirty night of fucking and sucking. But don't expect me to be all lovey-dovey or anything... I'm a dirty little slut who just wants to get fucked."
        mc.name "I wouldn't dream of it. We'll just have a good time and get dirty."
        the_person "Yeah, yeah. Just don't get too close, okay? I don't like cuddling or anything... unless it's with your cock inside me."
    elif the_person.sluttiness >= 80:
        the_person "Oh god, I'm so down for a dirty night of fucking and sucking. Make sure you're ready for a wild and crazy night, because I'm going to ride your cock all night long!"
        mc.name "I'll make sure to be ready. I promise you'll have a night to remember."
        the_person "I better... or I'll be very disappointed. And trust me, you don't want to disappoint me."
    else:
        the_person "I guess you can come over... But don't expect me to do anything I'm not comfortable with, okay? Unless, of course, you can convince me to be a dirty little slut and do something naughty."
        mc.name "I'll try my best to convince you. But I promise I won't push you too hard... unless you want me to."
        the_person "We'll see about that... maybe I'll surprise you and be a dirty little slut after all."
    return

label slutty_sleepover_yourplace_sex_start(the_person):
    "[the_person.title] rolls her eyes and walks over to you, her expression a mix of annoyance and desire. She's clearly a dirty little slut who wants to get fucked."
    the_person "Ugh, fine. Let's get this over with. Just don't expect me to be all lovey-dovey or anything... I just want to get fucked and cum."
    mc.name "I wouldn't dream of it. Let's just get dirty and have a good time."
    the_person "Yeah, yeah. Just don't get too close, okay? I don't like cuddling or anything... unless it's with your cock inside me."
    return

label slutty_sleepover_herplace_sex_start(the_person):
    the_person "Ugh, finally. Get over here already and fuck me. I've been waiting all day for this."
    "She smirks and crosses her arms, clearly annoyed but still eager for the action to begin. She's a dirty little slut who just wants to get fucked."
    mc.name "Are you ready?"
    the_person "Hah! Like I need to be ready for this. Just get in here and do your worst. I want to feel your cock inside me and cum all over the place."
    "She leans back on the couch, her legs spread wide in invitation. She's a dirty little slut who just wants to get fucked and cum."
    the_person "Hurry up, I'm not getting any younger! And I need to get fucked and cum before I go crazy."
    return

label slutty_sleepover_impressed_response(the_person):  #If you've made her cum a lot
    the_person "Ugh, you're really good at that... Don't expect me to admit it, but you're making me feel things... like a dirty little slut who just wants to get fucked and cum."
    "She rolls her eyes and smirks, trying to hide her true feelings. But it's clear she's a dirty little slut who loves to get fucked and cum."
    mc.name "You want more?"
    the_person "Hmph, maybe. But don't think you've won me over or anything. I can still handle more... and I want to feel your cock inside me again and cum some more."
    "[the_person.title] lies down in bed, her breathing still ragged from the previous rounds. She's a dirty little slut who just wants to get fucked and cum some more."
    the_person "I might be able to go for another round... But don't get too excited, I'm not making any promises! Unless, of course, you can convince me to be a dirty little slut and do something naughty again."
    return

label slutty_sleepover_good_response(the_person):  #If you've made her cum
    the_person "Ugh, fine. That wasn't too terrible, I suppose. You actually managed to make me cum, congratulations."
    "She rolls her eyes and smirks, trying to hide her true feelings, but her legs are still shaking from the orgasm and her pussy is still dripping with cum."
    mc.name "You want more?"
    $ the_person.draw_person(position = "missionary")
    the_person "Hmph, maybe. But don't think you've won me over or anything. I can still handle more... and I want to feel your cock inside me again, pounding me hard and making me cum some more."
    "[the_person.title] lies down in bed, her breathing still ragged from the previous round, her tits heaving with excitement and her pussy still throbbing with pleasure."
    the_person "Could you give me another pounding before we go to sleep? But don't expect me to be all lovey-dovey or anything... I just want to get fucked and cum some more, like the dirty little slut I am."
    return

label slutty_sleepover_bored_response(the_person):  #If she hasn't cum yet
    the_person "Ugh, is that the best you can do? I was expecting more than that from you... like, actually making me cum and not just poking me with your little dick."
    "She crosses her arms and looks at you with a bored expression, clearly unimpressed, her eyes rolling in frustration and her pussy still dry and unsatisfied."
    mc.name "What's wrong?"
    the_person "You know, just do better. I expect more from you than this... like, actually making me feel something and not just going through the motions."
    "She rolls her eyes and smirks, still rubbing her pussy in anticipation, her fingers slipping inside her wet slit and playing with her clit."
    the_person "You'd better step it up if you want to keep me interested... like, actually making me cum and not just boring me to tears with your mediocre sex skills."
    return

#==================================================================
# add more slutty personality, use different words, sexually explicitives, and movements.
# update all the following the_person and movements with slutty personality. Use Panty Anarchy from Panty & Stocking with Garterbelt or Naruko Yokoshima from Seitokai Yakuindomo, for ideas, keep to the structure. Movements in quotations:
### DIALOGUE ###
