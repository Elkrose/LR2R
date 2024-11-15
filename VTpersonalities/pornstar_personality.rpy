### PERSONALITY CHARACTERISTICS ###
# Bimbo is slang for a conventionally attractive, sexualized naïve woman. The term was originally used in the United States as early as 1919 for an unintelligent or brutish man. As of the early 21st century, the "stereotypical bimbo" appearance became akin to that of a physically attractive woman.
#However, as with most identities, the idea of the 'bimbo' has evolved and here is what it means today. The term 'bimbofication' is a colloquial term derived from the term 'bimbo' which is understood to mean, 'an attractive woman who is pretty, sexualised, naive and uneducated'.
#==================================================================
# add more pornstar personality, use different words, sexually explicitives, and movements.
# update all the following the_person and movements with pornstar personality. Use Dillion Harper, Alexis Texas, Megan Rain, Riley Reid, Dani Daniels, Naomi Woods for ideas, keep to the structure. Movements in quotations:
### DIALOGUE ###

label pornstar_introduction(the_person):
    mc.name "Hey, can I talk to you for a sec?"
    "[the_person.title] turns around, a sultry smile spreading across her face as she runs her hands over her hips, accentuating her curves and making her breasts bounce."
    the_person "Oh, finally. I was starting to think you were too chicken to come over and talk to me. But now that you're here, I have to say, you're looking pretty good. I can already imagine what it would be like to have you inside me."
    mc.name "I'm sorry if this is awkward, but you seem like a really interesting person."
    "[the_person.title] raises an eyebrow, a flirtatious glint in her eye as she leans in close, her breasts almost touching your chest and her nipples hardening."
    the_person "Interesting? That's cute. You want to get to know me, huh? Well, I'm not sure if you can handle me, but I'm willing to give you a shot. I'm a dirty little slut who loves to get fucked, and I'm not afraid to show it."
    mc.name "Well, I was wondering if you'd like to... do something together sometime."
    "[the_person.title] lets out a throaty laugh, her eyes sparkling with amusement as she tosses her hair over her shoulder, exposing her neck and shoulder and making her look like a total sexpot."
    the_person "Oh, baby, I'm always up for a good time. What did you have in mind? Something naughty, I hope? Like, maybe, a night of hardcore fucking and sucking?"
    mc.name "Haha, well, maybe we could grab coffee or something?"
    "[the_person.title] pouts, her lips curling into a playful smirk as she teases you, her eyes sparkling with mischief and her body language screaming 'fuck me'."
    the_person "Coffee? That's so boring. How about we do something a little more... exciting? Like, maybe, a night of non-stop sex and debauchery?"
    mc.name "Heh, I don't know... what did you have in mind?"
    "[the_person.title] leans in close, her voice dropping to a sultry whisper as she breathes in your ear, her hot breath sending shivers down your spine and making your cock hard."
    the_person "I have a few ideas. But I think we should get to know each other a little better first, don't you? Maybe we can start with a kiss, and see where things go from there? Or maybe we can just skip the formalities and go straight to the fucking?"
    mc.name "Uh, yeah... that sounds good, I guess."
    $ the_person.set_title()
    $ the_person.set_possessive_title()
    the_person "So, what's your name, anyway? I want to know what to scream when we're in bed together and you're pounding my pussy with your cock."
    mc.name "I'm [mc.name]. Nice to meet you..."
    the_person "I'm [the_person.name]. Nice to meet you too, baby. And don't worry, I'll make sure you remember my name, and my body, for a long time. Especially my tits and my pussy, which you'll be playing with all night long."
    $ the_person.change_happiness(2)
    $ the_person.change_sluttiness(1)
    return

label pornstar_greetings(the_person):
    if the_person.love < 0:
        the_person "Ugh, what do you want now? Can't you see I'm busy getting myself off and imagining your cock inside me?"
        "[the_person.possessive_title!c] rolls her eyes and crosses her arms, clearly annoyed, but with a hint of a smirk on her face as she spreads her legs and shows off her pussy."
    elif the_person.happiness < 90:
        the_person "Hey, I guess. I'm still having a pretty crappy day, but you're here now, so maybe you can help me take my mind off things... with your cock, that is. I need a good fucking to forget my troubles."
        "[the_person.possessive_title!c] shrugs and looks away, her expression sulky, but with a hint of a smile on her face as she plays with her nipples and makes them hard."
    else:
        if the_person.sluttiness > 60:
            if the_person.obedience > 180:
                the_person "Oh, it's you. I was hoping you'd show up. I've been feeling a little... horny lately, and I need someone to take care of me and give me a good pounding."
                "[the_person.possessive_title!c] bats her eyelashes and smiles, her voice husky with suggestion, as she runs her hands over her body, accentuating her curves and making her tits bounce."
            else:
                the_person "Hey there, [the_person.mc_title]. I'm not really in the mood for games today, so let's just get to it, okay? I want to feel your cock inside me, and I want it now. I'm a dirty little slut who needs to get fucked."
                "[the_person.possessive_title!c] raises an eyebrow and looks you up and down, her expression confident and flirtatious, as she takes a step closer to you, her body almost touching yours and her breath on your neck."
        else:
            if the_person.obedience > 180:
                the_person "Hi, [the_person.mc_title]. What can I do for you today? I'm feeling a little... adventurous, and I was thinking maybe we could try something new... like anal, or maybe even a threesome. I'm a dirty little slut who loves to get fucked in all holes."
                "[the_person.possessive_title!c] smiles and leans in close, her voice barely above a whisper, as she runs her hands over your body, teasing you with her touch and making your cock hard."
            else:
                the_person "Hey, what's up? Don't tell me you're here to bother me again with your silly questions and awkward small talk. I'm not in the mood for that, but I am in the mood for something else... something a little more... physical. Like, maybe, a good fucking or a blow job."
                "[the_person.possessive_title!c] rolls her eyes and sighs, her expression exasperated, but with a hint of a smile on her face, as she takes a step closer to you, her body almost touching yours and her lips inches from yours."
    return

label pornstar_sex_responses_foreplay(the_person):
    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] moans loudly and wraps her legs around you, pulling you in close as she grinds her pussy against your hand, getting your fingers all wet and sticky with her juices."
            the_person "Oh, fuck yeah. That's it. Right there. Don't stop, baby. I'm getting so wet and ready to be fucked."
        else:
            "[the_person.possessive_title!c] moans softly and looks up at you with a mixture of surprise and pleasure as she starts to get into it, her eyes locked on yours and her body starting to tremble."
            the_person "Mmm, this is actually kind of nice. I didn't expect to be so turned on by your touch, but now I'm craving more... and maybe even a little bit of cock."

    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            the_person "Mmm, yeah. That feels so good. Don't stop, [the_person.mc_title]. Please don't stop. I'm getting so close to cumming all over your face."
            "[the_person.possessive_title!c] starts to grind against you, her hips moving in time with your touch as she starts to lose control, her body shaking and her legs trembling with anticipation."
        else:
            the_person "I... I think I might actually be enjoying this. Which is weird, because I didn't think I would be into this sort of thing... but now I'm not sure if I can stop myself from wanting more."
            "[the_person.possessive_title!c] looks up at you with a mixture of confusion and arousal as she starts to get more and more turned on, her face flushing and her nipples hardening."

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            the_person "Oh, god. Yeah. That's it. I'm going to cum if you keep doing that. I can feel it building up inside me, and I don't think I can hold it back much longer."
            "[the_person.possessive_title!c] starts to tremble and shake, her body on the verge of orgasm as she starts to lose control, her legs spreading wide and her pussy opening up for you."
        else:
            the_person "I... I think I might be getting close. Which is weird, because I didn't think I would be into this sort of thing... but now I'm not sure if I can stop myself from cumming all over your face."
            "[the_person.possessive_title!c] looks up at you with a mixture of surprise and arousal as she starts to get more and more turned on, her eyes locked on yours and her body starting to tremble with anticipation."

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "Mmm, yeah. That feels so good. I'm going to cum all over your face if you keep doing that. I want to feel your tongue on my clit and your cock inside me."
            "[the_person.possessive_title!c] starts to grind against you, her hips moving in time with your touch as she starts to lose control, her body shaking and her legs trembling with anticipation."
        else:
            the_person "I... I think I might actually be enjoying this. Which is weird, because I didn't think I would be into this sort of thing... but now I'm not sure if I can stop myself from wanting more... and maybe even a little bit of cock."
            "[the_person.possessive_title!c] looks up at you with a mixture of confusion and arousal as she starts to get more and more turned on, her face flushing and her nipples hardening."

    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                the_person "Oh, god. Yeah. I'm going to cum. And it's all because of you, [the_person.mc_title]. You're so good at this... and I'm so bad at resisting you."
                "[the_person.possessive_title!c] starts to tremble and shake, her body on the verge of orgasm as she starts to lose control, her legs spreading wide and her pussy opening up for you."
            else:
                the_person "The way you touch me is just... different, I guess. It's like you actually know what you're doing. You're so much better than my boyfriend... and I think I might actually be falling for you."
                "[the_person.possessive_title!c] looks up at you with a mixture of surprise and arousal as she starts to get more and more turned on, her eyes locked on yours and her body starting to tremble with anticipation."
        else:
            the_person "I... I think I might actually be enjoying this. Which is weird, because I didn't think I would be into this sort of thing... but now I'm not sure if I can stop myself from wanting more... and maybe even a little bit of cock."
            "[the_person.possessive_title!c] looks up at you with a mixture of confusion and arousal as she starts to get more and more turned on, her face flushing and her nipples hardening."

    return

label pornstar_sex_responses_oral(the_person):
    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] spreads her legs wide, a dirty grin spreading across her face as she starts to play with her clit."
            the_person "Oh, baby, you want to eat my pussy? Well, I'm not going to stop you... in fact, I'm going to make you do it harder and deeper, until I cum all over your face."
        else:
            "[the_person.possessive_title!c] looks up at you, her eyes sparkling with curiosity and a hint of mischief as she starts to get more and more turned on."
            the_person "Hmmm, I wonder what you're going to do down there... are you going to make me cum with your tongue and then fuck me with your cock?"

    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            the_person "Mmm, yeah, that feels so fucking good... don't stop, [the_person.mc_title], I'm getting so close to cumming all over your face."
            "[the_person.possessive_title!c] starts to grind against your face, her hips moving in time with your tongue as she starts to lose control and get more and more turned on."
        else:
            the_person "Oh, wow, you're actually kind of good at this... who knew you had such a talented tongue? Maybe you can use it to make me cum and then fuck me with your cock."
            "[the_person.possessive_title!c] giggles, her body relaxing into the sensation as she starts to get more and more turned on and her pussy starts to get wetter and wetter."

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            the_person "Hmmm, yeah, that's the spot... right there, baby, don't stop, I'm going to cum all over your face and then I want you to fuck me with your cock."
            "[the_person.possessive_title!c] starts to moan, her body trembling with pleasure as she starts to lose control and get more and more turned on."
        else:
            the_person "Alright, alright, you're pretty good at this... but don't think this means I'm going to go easy on you, I'm still going to make you work for it and fuck me with your cock."
            "[the_person.possessive_title!c] smiles, her eyes glinting with mischief as she starts to get more and more turned on and her pussy starts to get wetter and wetter."

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "Mmm, yeah, I'm going to cum... and it's all because of you, [the_person.mc_title], you're so good at eating my pussy and making me feel like a slut."
            "[the_person.possessive_title!c] starts to shake, her body on the verge of orgasm as she starts to lose control and get more and more turned on."
        else:
            the_person "Wow, you're really good at this... I think I might actually be enjoying myself, which is weird, because I didn't think I would be into this sort of thing... but now I'm not sure if I can stop myself from wanting more."
            "[the_person.possessive_title!c] looks up at you, her eyes sparkling with surprise and a hint of arousal as she starts to get more and more turned on and her pussy starts to get wetter and wetter."

    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                the_person "Oh, wow... I think I just came... thanks to you, [the_person.mc_title], you're so good at making me cum and feel like a slut."
                "[the_person.possessive_title!c] smiles, her body relaxing into the afterglow as she starts to feel satisfied and her pussy starts to get wetter and wetter."
            else:
                the_person "Mmm, maybe I should let you do that more often... when [the_person.so_title] isn't around, of course, because I don't want to cheat on them, but I do want to cheat with you and feel like a slut."
                "[the_person.possessive_title!c] winks, her eyes glinting with mischief as she starts to feel more and more attracted to you and her pussy starts to get wetter and wetter."
        else:
            the_person "Ugh, fine, you win... I guess I did enjoy that after all, which is weird, because I didn't think I would be into this sort of thing... but now I'm not sure if I can stop myself from wanting more."
            "[the_person.possessive_title!c] rolls her eyes, her expression playful and a hint of arousal as she starts to get more and more turned on and her pussy starts to get wetter and wetter."

    return

label pornstar_sex_responses_vaginal(the_person):
    if the_person.energy < 10:
        call low_energy_sex_responses_vaginal(the_person) from _vt_pornstar_call_low_energy_sex_responses_vaginal_10
        return
    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            $ play_moan_sound()
            "[the_person.possessive_title!c] spreads her legs wide and arches her back, her hips bucking against yours as she takes your cock deep inside her and starts to get more and more turned on."
            the_person "Oh, fuck yeah... that feels so good... don't stop, baby, I'm getting so wet and ready to be fucked!"
        else:
            "[the_person.possessive_title!c] bites her lip and looks up at you with a sultry gaze, her eyes sparkling with desire and her pussy starting to get wetter and wetter."
            the_person "Mmm, you're not bad... but I think I can handle a little more... harder, faster, deeper, and maybe even a little bit of anal!"

    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            the_person "Oh, god... yeah, keep going... I love the way you're making me feel! You're so big and hard inside me, and I can feel your cock all the way up to my cervix!"
            "[the_person.possessive_title!c] starts to grind against you, her hips moving in time with yours as she takes your cock deeper and deeper and starts to get more and more turned on."
        else:
            the_person "Hmmm, you're pretty good... but I think I need a little more convincing... show me what you've got stud, and maybe we can even try some anal or a threesome!"

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            the_person "Mmm, yeah... that's the spot... right there, baby! You're hitting my G-spot, oh god, and I can feel my pussy starting to cum!"
            "[the_person.possessive_title!c] starts to moan and tremble, her body on the verge of orgasm as she takes your cock deeper and deeper and starts to get more and more turned on."
        else:
            the_person "Oh, wow... you're really good at this... I think I might actually be enjoying myself... who knew I was such a slut and loved to be fucked so much?"
            "[the_person.possessive_title!c] looks up at you, her eyes sparkling with surprise and a hint of arousal as she starts to get more and more turned on and her pussy starts to get wetter and wetter."

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "Yeah, baby... I'm going to cum... and it's all because of you! You're the best fuck I've ever had, and I can feel my pussy cumming all over your cock!"
            "[the_person.possessive_title!c] starts to shake and tremble, her body on the verge of orgasm as she takes your cock deeper and deeper and starts to get more and more turned on."
        else:
            the_person "Hmmm, I think I might actually be getting close... thanks to you, [the_person.mc_title]... you're really good at this, and I can feel my pussy starting to cum!"
            "[the_person.possessive_title!c] looks up at you, her eyes sparkling with surprise and a hint of arousal as she starts to get more and more turned on and her pussy starts to get wetter and wetter."

    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                the_person "Oh, god... yeah, I'm cumming... thanks to you, baby! You're the best fuck I've ever had, and I can feel my pussy cumming all over your cock!"
                "[the_person.possessive_title!c] arches her back and moans loudly, her body trembling with pleasure as she takes your cock deeper and deeper and starts to get more and more turned on."
            else:
                the_person "Mmm, yeah... I think I'm going to cum... and it's all because of you, [the_person.mc_title]... you're so good at making me feel like a slut and cumming all over your cock!"
                "[the_person.possessive_title!c] looks up at you with a sultry gaze, her eyes sparkling with pleasure as she takes your cock deeper and deeper and starts to get more and more turned on."
        else:
            the_person "Hmph, I suppose I'm almost there... thanks to you, [the_person.mc_title]... you're really good at this, and I can feel my pussy starting to cum!"
            "[the_person.possessive_title!c] looks up at you, her expression playful and a hint of arousal as she starts to get more and more turned on and her pussy starts to get wetter and wetter."

    return

label pornstar_sex_responses_anal(the_person):
    if the_person.energy < 10:
        call low_energy_sex_responses_anal(the_person) from _vt_pornstar_call_low_energy_sex_responses_anal_10
        return

    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            the_person "Mmm, baby... I'm so ready for this. Fuck my ass hard and deep, and make me scream with pleasure!"
            "[the_person.possessive_title!c] looks up at you with a sultry gaze, her eyes sparkling with desire and her ass wiggling with anticipation."
        else:
            $ the_person.call_dialogue("teasing_exclaim")
            the_person "Hehe, you want to stick it in my ass? Well, I suppose I can handle a big cock like yours... but don't think I'm going to go easy on you, I want it hard and fast!"
            "[the_person.possessive_title!c] winks, her expression playful and flirtatious as she spreads her legs and exposes her ass."

    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            $ the_person.call_dialogue("surprised_exclaim")
            the_person "Wow, this is... actually kind of amazing. Your cock feels so good in my ass, it's like it was made for me!"
            "[the_person.possessive_title!c] squirms a bit, trying to get used to the sensation, but a smile spreads across her face as she starts to get more and more turned on."
        else:
            the_person "Mmm, this is... interesting. I never knew anal could feel so good... but now I'm hooked, and I want more!"

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            the_person "Oh, yeah... keep going... I love the way you're fucking my ass, it's like you're in control and I'm just a dirty little slut!"
            "[the_person.possessive_title!c] starts to moan and grind against you, her hips moving in time with yours as she gets more and more turned on."
        else:
            the_person "Hmmm, this is... actually kind of nice. I think I might be enjoying myself... and I'm not sure if I should be ashamed or proud of it!"

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            if mc.condom:
                the_person "Mmm, yeah... I love the way you're making me feel... even with a condom on, your cock is so big and hard, it's like it's going to split me in two!"
            else:
                the_person "Oh, baby... I can feel you so deep inside me... it's amazing... your bare cock is so hot, it's like it's burning me up from the inside out!"
        else:
            the_person "Hmmm, I think I might actually be getting close... thanks to you, [the_person.mc_title]... your cock is so nice and big, it's making me feel so good, I just want to cum all over it!"

    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                the_person "Oh, god... yeah, I'm cumming... thanks to you, baby! Your cock is so amazing, it's like it was made for me, and I'm going to cum all over it!"
                "[the_person.possessive_title!c] arches her back and moans loudly, her body trembling with pleasure as she cums all over your cock."
            else:
                the_person "Mmm, yeah... I think I'm going to cum... and it's all because of you, [the_person.mc_title]... your cock is so big and hard, it's driving me crazy, and I just want to cum all over it!"
                "[the_person.possessive_title!c] looks up at you with a sultry gaze, her eyes sparkling with pleasure as she cums all over your cock."
        else:
            $ the_person.call_dialogue("teasing_exclaim")
            the_person "Hehe, I think I might actually be enjoying myself... thanks to you, [the_person.mc_title]... your cock is so nice and big, it's making me feel so good, I just want to cum all over it and then suck it dry!"
            "[the_person.possessive_title!c] winks, her expression playful and flirtatious as she cums all over your cock and then starts to suck it dry."
    return

label pornstar_climax_responses_foreplay(the_person):
    if the_person.sluttiness > 50:
        the_person "Oh, fuck me already! I need to cum so bad, I can feel my pussy throbbing with anticipation!"
        "[the_person.possessive_title!c] starts to squirm and grind against you, desperate for release, her body tense with pleasure."
    else:
        the_person "Why do you always have to tease me like this? Just make me cum already, I'm a dirty little slut who needs to get off!"
        "[the_person.possessive_title!c] huffs, clearly on the verge of climax, her body tense with anticipation, her nipples hard and her pussy wet."
    return

label pornstar_climax_responses_oral(the_person):
    if the_person.sluttiness > 70:
        the_person "Oh, god, your tongue is so good! I'm going to cum all over your face, and then I want to suck your cock dry!"
        "[the_person.possessive_title!c] starts to moan and grind against your face, her hips moving in time with your tongue, her body on the verge of orgasm."
    else:
        the_person "Mmm, you're so good at this... I didn't think I'd... I'm going to cum... oh, yeah, I can feel it building up inside me!"
        "[the_person.possessive_title!c] starts to tremble and shake, her body on the verge of orgasm, her voice barely above a whisper, her eyes closed in ecstasy."
    return

label pornstar_climax_responses_vaginal(the_person):
    if the_person.sluttiness > 70:
        if the_person.arousal_perc > 120:
            the_person "Fine, I'll cum. But don't think this means I'm not going to want more... I'm a dirty little slut who loves to get fucked!"
            "[the_person.possessive_title!c] grits her teeth and squeezes her eyes shut, her body tense with pleasure, her pussy contracting around your cock."
        else:
            the_person "Ugh, just a little more... I'm... Ah, fuck! I'm going to cum so hard, I can feel it building up inside me!"
            "[the_person.possessive_title!c] starts to moan and grind against you, her hips moving in time with yours, her body on the verge of orgasm, her pussy wet and slippery."
    else:
        the_person "Oh... I can't... I'm going to... Ah! Oh, god, I'm cumming, I can feel it rushing through my body!"
        "[the_person.possessive_title!c] starts to tremble and shake, her body on the verge of orgasm, her voice barely above a whisper, her eyes closed in ecstasy."
    return

label pornstar_climax_responses_anal(the_person):
    if the_person.sluttiness > 70:
        if the_person.arousal_perc > 120:
            the_person "Fine, you win. I'll cum. But don't think I'm not going to want more... I love being fucked in the ass, it's so dirty and naughty!"
            "[the_person.possessive_title!c] squeezes her eyes shut, trying to fight off the pleasure, but her body betrays her, cumming hard and fast, her ass contracting around your cock."
        else:
            the_person "Ugh, just a little more... My ass is going to... Ah! Oh, god, I'm cumming, I can feel it building up inside me!"
            "[the_person.possessive_title!c] starts to moan and grind against you, her hips moving in time with yours, her body on the verge of orgasm, her ass wet and slippery."
    else:
        the_person "Oh... My... Ass... I... Ah! Oh, god, I'm cumming so hard, I can feel it rushing through my body!"
        "[the_person.possessive_title!c] barely finishes her sentence before her body is racked with pleasure, cumming hard and fast, her ass contracting around your cock."
    return

label pornstar_clothing_accept(the_person):
    if the_person.obedience > 180:
        the_person "Mmm, I love dressing up like a slut for you. It makes me feel so dirty and naughty, like I'm ready to get fucked!"
        "[the_person.possessive_title!c] gives you a sultry smile, her eyes sparkling with desire, her body language screaming 'fuck me'!"
    else:
        the_person "Yeah, whatever. I'll wear this pornstar outfit for you, but don't expect me to be all prim and proper, I'm a dirty little slut who loves to get wild!"
        "[the_person.possessive_title!c] rolls her eyes, but can't help smiling at the thought of dressing up like a slut and getting fucked."
    return

label pornstar_clothing_reject(the_person):
    if the_person.should_wear_uniform:
        the_person "Ugh, fine. I'll put on my uniform. But can I at least wear some pornstar underwear underneath, I want to feel like a dirty little slut even when I'm dressed up like a good girl?"
        "[the_person.possessive_title!c] pouts, but starts to get changed into her uniform, her body language screaming 'fuck me' even as she's dressed up like a good girl."
    elif the_person.obedience > 180:
        the_person "I don't... I'm sorry, but I really don't think I could get away with wearing something like this. It's just too revealing... but I love the way you look at me when I'm dressed like a slut, it makes me feel so dirty and naughty!"
        "[the_person.possessive_title!c] blushes, but can't help feeling a little turned on at the thought of dressing up like a slut and getting fucked."
    else:
        if the_person.sluttiness > 60:
            the_person "Hmm, I don't know about this one. It's a bit too revealing for my taste... but I love the way it makes me feel like a dirty little slut, like I'm ready to get fucked!"
            "[the_person.possessive_title!c] gives you a sultry smile, her eyes sparkling with desire, her body language screaming 'fuck me'!"
        else:
            the_person "You've got to be kidding me, right? This is ridiculous. I'm not wearing this... but maybe I'll wear something even sluttier instead, like a pair of pornstar heels and a thong!"
            "[the_person.possessive_title!c] rolls her eyes, but can't help laughing at the thought of dressing up like a slut and getting wild."
    return

label pornstar_clothing_review(the_person):
    if the_person.outfit.cum_covered:
        if (the_person.sluttiness > 40 and the_person.opinion.being_covered_in_cum >=0) or the_person.opinion.being_covered_in_cum > 0:
            the_person "Mmm, I love being covered in cum. It's so dirty and naughty... and it makes me feel like such a filthy little slut. I want to leave it all over my skin and feel it dripping down my thighs."
            "[the_person.possessive_title!c] starts to wipe up the biggest splashes of cum on her, but can't help smiling at the thought of being covered in cum and feeling like a dirty little slut."
        else:
            the_person "For fuck's sake, I need to clean up this mess! But maybe I'll just leave a little bit of cum on me... it's not like I'm going to be wearing any panties anyway, and I want to feel it on my skin all day."
            "[the_person.possessive_title!c] wipes herself down, cleaning up all the cum she can find, but leaves a little bit on her skin to remind her of the dirty things she's been up to and to make her feel like a slut."

    if the_person.obedience > 180:
        the_person "Fine, I'll be back in a moment. I need to get cleaned up for you... and maybe put on something even sluttier, like a pair of pornstar heels and a thong."
        "[the_person.possessive_title!c] gives you a sultry smile, her eyes sparkling with desire and her body language screaming 'fuck me'!"
    else:
        if the_person.sluttiness > 40:
            the_person "I don't know why I do this, but I want to look good for you. I'll be back in a second, I just want to get cleaned up and put on something that will make you hard, like a tiny little dress and some pornstar lingerie."
            "[the_person.possessive_title!c] gives you a sultry smile, her eyes sparkling with desire and her body language screaming 'fuck me'!"
        else:
            the_person "Ugh, everything's such a mess after that. Wait here a moment, I'm just going to find a mirror and try and look somewhat presentable... but maybe I'll just wear something pornstar instead, like a pair of fishnets and a leather corset."
            "[the_person.possessive_title!c] rolls her eyes, but can't help laughing at the thought of dressing up like a slut and getting wild."
    $ the_person.apply_planned_outfit(show_dress_sequence = True)
    return


label pornstar_strip_reject(the_person, the_clothing, strip_type = "Full"):
    if the_person.obedience > 180:
        the_person "Oh, baby, can't we just leave my [the_clothing.display_name] on for now? I want to tease you a little longer and make you beg for it..."
        "[the_person.possessive_title!c] gives you a sultry smile, her eyes sparkling with desire and her body language screaming 'fuck me'!"
    elif the_person.obedience < 70:
        the_person "No way, I'm not taking anything off until I'm good and ready. And even then, it's going to be on my terms, not yours. You're just going to have to wait and see what I'm wearing underneath..."
        "[the_person.possessive_title!c] crosses her arms over her chest, a defiant look on her face and a sly smile on her lips."
    else:
        the_person "Not yet, baby... I want to make you wait a little longer. But trust me, it'll be worth it. I've got a surprise for you underneath my clothes..."
        "[the_person.possessive_title!c] gives you a sly smile, her eyes sparkling with mischief and her body language screaming 'fuck me'!"
    return

label pornstar_strip_obedience_accept(the_person, the_clothing, strip_type = "Full"):
    "[the_person.title] laughs nervously as you start to slide her [the_clothing.display_name] away, but she doesn't stop you. Instead, she leans in close and whispers in your ear..."
    if the_person.obedience > 180:
        the_person "Oh, yeah... take it off. I want to feel your hands all over me and your cock inside me. I'm a dirty little slut who needs to get fucked..."
        "[the_person.possessive_title!c] closes her eyes, her body trembling with anticipation and her pussy getting wet with excitement."
    else:
        the_person "I don't know if this is a good idea, but I'm going to let you do it anyway. Because I'm a slut, and I love it. I love the way you make me feel, and I love the way you fuck me..."
        "[the_person.possessive_title!c] gives you a sultry smile, her eyes sparkling with desire and her body language screaming 'fuck me'!"
    return

label pornstar_grope_body_reject(the_person):
    if the_person.effective_sluttiness("touching_body") < 5: #Fail point for touching shoulder
        the_person "Hey, watch it, baby! Don't think you can just touch me wherever you want. I'm a tease, and I like to be treated like a slut."
        "[the_person.title] steps back as you touch her, then crosses her arms over her chest, her eyes flashing with annoyance."
        the_person "If you want to touch me, you're going to have to do better than that. Maybe start with a little foreplay, and then we can see where things go."
        mc.name "Oh, sorry. I didn't mean to make you feel that way. I just can't help myself when I'm around you."
        the_person "Yeah, well, try to be more careful next time, alright? Or maybe just ask me if you can touch me. I might say yes, and we can have some real fun."
        "She seems a little put off by the situation, but you both try to move on and put it behind you, the tension between you palpable."
    else: #Fail point for touching waist
        the_person "Oh, baby... you're getting a little too aggressive for my taste. I like to be teased, but I don't like to be rushed."
        "[the_person.title] takes your hand and pulls it off of her waist, giving you a warning look, her eyes sparkling with desire."
        the_person "If you want to touch me, you're going to have to slow down a little. I like to be seduced, not attacked. Maybe start with a little kissing, and then we can see where things go."
        mc.name "Oh yeah, of course. My bad. I just get so turned on when I'm around you."
        the_person "Just make sure you don't do it again, okay? Or maybe just ask me if you can touch me. I might say yes, and we can have some real fun."
        "She doesn't say anything else, but you can tell she's still a bit annoyed about the situation, her body language screaming 'fuck me, but do it right'."

    return

label pornstar_sex_accept(the_person, the_position):
    if the_person.sluttiness > 70:
        if the_person.obedience < 70:
            the_person "Fine, let's do it. But don't think this means I'm going to put out every time you ask. I'm a slut, but I'm not easy. I like to be fucked, but I like to be fucked right."
        else:
            if the_position.skill_tag == "Foreplay":
                the_person "Oh, yeah... I've been waiting for this. Touch me, baby, touch me all over. Make me cum with your fingers, and then we can fuck."
            elif the_position.skill_tag == "Oral":
                if "getting head" in the_position.opinion_tags:
                    the_person "Ugh, I need your tongue on my clit. Now. Make me cum, baby, and then we can fuck."
                else:
                    the_person "You're going down on me, and you're going to make me cum. Hard. And then we're going to fuck, and it's going to be amazing."
            else:
                the_person "Get over here and fuck me already. I've been waiting for this, and I'm not going to wait any longer. I need your cock inside me, and I need it now."
    else:
        the_person "Come here, baby... let's do it. I want to feel your cock inside me, and I want to feel you cumming all over me."
    return

label pornstar_sex_obedience_accept(the_person):
    if the_person.sluttiness > 70:
        the_person "Oh, fuck it. I don't care anymore. Do whatever you want to me, [the_person.mc_title]. I'm a slut, and I love it. I love being fucked, and I love being used."
        "[the_person.possessive_title!c] spreads her legs wide, inviting you to take her, her eyes sparkling with desire and her body language screaming 'fuck me'."
    else:
        if the_person.obedience > 180:
            the_person "Alright, I'll do what you say, but don't think this means I'm not going to enjoy it. I love being a submissive slut, and I love being fucked by you."
            "[the_person.possessive_title!c] gives you a sultry smile, her eyes sparkling with desire and her body language screaming 'fuck me'."
        else:
            the_person "I shouldn't be saying this, but if you really want to... I'll give it a try. And maybe I'll even like it. Maybe I'll even love it, and we can do it again and again."
            "[the_person.possessive_title!c] gives you a sly smile, her eyes sparkling with mischief and her body language screaming 'fuck me'."
    return

label pornstar_sex_gentle_reject(the_person):
    if the_person.sluttiness > 50:
        the_person "Oh, baby, not like that. I need a little more foreplay first. You know, to get me wet and ready for your cock. Maybe some kissing, maybe some touching... and then we can fuck."
        "[the_person.possessive_title!c] gives you a sultry smile, her eyes sparkling with desire and her body language screaming 'fuck me, but do it right'."
    else:
        the_person "No, no, no. I want to have fun, but I don't want to get too serious. Let's just keep it light and dirty, and we can have some real fun. Maybe some oral, maybe some anal... and then we can fuck."
        "[the_person.possessive_title!c] winks at you, her expression playful and flirtatious, her body language screaming 'fuck me, but do it right'."
    return

label pornstar_sex_angry_reject(the_person):
    if the_person.has_significant_other:
        the_person "What? Are you out of your mind? I have a [the_person.so_title], but that doesn't mean I'm not interested in you. Maybe we can have a little fun on the side, like a threesome or something."
        "[the_person.possessive_title!c] gives you a sly smile, her eyes sparkling with mischief and her body language screaming 'fuck me'."
    elif the_person.sluttiness < 20:
        the_person "Are you serious? You've got to be kidding me! Get away from me, I never want to see you like this again... or maybe I do, I'm not sure. I'm a dirty little slut, after all."
        "[the_person.title] glares at you, but you can see the desire in her eyes and her nipples hardening with excitement."
    else:
        the_person "What? Are you out of your mind? You can't be serious! Get away from me, I'm not interested in anything like that... or maybe I am, I'm a slut, after all. I love to be fucked, and I love to be used."
        "[the_person.title] glares at you, but you can see the desire in her eyes and her body language screaming 'fuck me'."
    return

label pornstar_seduction_response(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 50:
            the_person "Oh, I think I know what you need right now. Let me take care of you, baby. I'll suck your cock and make you cum, and then we can fuck all night long."
            "[the_person.possessive_title!c] gives you a sultry smile, her eyes sparkling with desire and her body language screaming 'fuck me'."
        else:
            the_person "Okay, I'll give you a few minutes. But don't think this means I'm going to be your slave or anything... unless you want me to be, that is. I love to be dominated, and I love to be used."
            "[the_person.possessive_title!c] winks at you, her expression playful and flirtatious, her body language screaming 'fuck me'."
    else:
        if the_person.sluttiness > 50:
            the_person "Mmm, you're feeling as horny as me then? Come on, let's go find a place to get out of sight and fuck each other's brains out. I love to be fucked in public, it's so dirty and naughty."
            "[the_person.title] takes your hand and leads you off to find some place private, her body language screaming 'fuck me'."
        elif the_person.sluttiness > 10:
            the_person "I know that look you're giving me, I think I know what you want. And I'm happy to give it to you, baby. I love to be fucked, and I love to be used."
            "[the_person.possessive_title!c] gives you a sultry smile, her eyes sparkling with desire and her body language screaming 'fuck me'."
        else:
            the_person "[mc.name], I know what you mean... Okay, I can spare a few minutes. But don't get your hopes up, unless you want to get me off, that is. I love to be fucked, and I love to cum."
            "[the_person.possessive_title!c] winks at you, her expression playful and flirtatious, her body language screaming 'fuck me'."
    return

label pornstar_seduction_accept_crowded(the_person):
    if not the_person.has_significant_other:
        if the_person.sluttiness < 20:
            the_person "Alright, let's sneak away for a few minutes and you can convince me a little more... with your cock, that is. I love to be fucked in secret, it's so dirty and naughty."
        elif the_person.sluttiness < 50:
            the_person "Come on, I know someplace nearby where we can get a few minutes privacy. Just make it quick, I'm getting wet just thinking about it. I love to be fucked fast and hard."
        else:
            the_person "Oh, I don't know if I can wait much longer [the_person.mc_title]... I need to feel your cock inside me, now. I love to be fucked, and I love to cum."
    else:
        if the_person.sluttiness + (5*the_person.opinion.cheating_on_men) > 50:
            the_person "Fuck it, let's do this! I don't care if my [the_person.so_title] finds out, I need to get fucked. I love to be a cheating slut, it's so dirty and naughty."
            the_person "I hope you don't mind that I've got a [the_person.so_title], but I don't care right now. I just need to feel your cock inside me, and I need it now."
        else:
            the_person "Ugh, you're bad for me [the_person.mc_title]... Come on, we need to find somewhere quiet so my [the_person.so_title] doesn't catch us. But I'm not promising anything, I'm a slut, after all. I love to be a dirty little secret."
    return

label pornstar_seduction_accept_alone(the_person):
    if not the_person.has_significant_other:
        if the_person.sluttiness < 20:
            the_person "Alright, you've got one chance to impress me... with your cock, that is. I love to be fucked, and I love to be used."
        elif the_person.sluttiness < 50:
            the_person "Come on, let's get this over with and see if you're any good. I'm not looking for anything serious, just a quick fuck. I love to be fucked fast and hard."
        else:
            the_person "Fuck, I'm so turned on right now. Just do me already! I need to feel your cock inside me, now. I love to be fucked, and I love to cum."
    else:
        if the_person.sluttiness + (5*the_person.opinion.cheating_on_men) > 50:
            the_person "You know I shouldn't be doing this with you, but fuck it. Let's do this! I need to get fucked, and I don't care who knows. I love to be a cheating slut, it's so dirty and naughty."
        else:
            the_person "You're trouble, [the_person.mc_title], but I can't help myself. Come here and fuck me, I need it. I love to be fucked, and I love to be used."
    return

label pornstar_seduction_refuse(the_person):
    if the_person.sluttiness < 20:
        the_person "Ugh, why are you always trying to flirt with me, [mc.name]? I'm just not in the mood for this right now, okay? Maybe some other time, when I'm feeling more pornstar and ready to get fucked."
        "[the_person.title] folds her arms and looks away, but you can see the desire in her eyes and her nipples hardening with excitement."
    elif the_person.sluttiness < 50:
        the_person "Fine, I'll admit you're kind of cute, but don't think this means I'm actually interested. I just don't feel like messing around right now, okay? Maybe some other time, when I'm feeling more horny and ready to get fucked."
        "[the_person.title] playfully pokes [mc.name]'s chest with her finger, but you can see the desire in her eyes and her body language screaming 'fuck me'."
    else:
        the_person "Eh, you're always trying to get me into bed, [mc.name], but I'm not going to make it easy for you. You'll have to wait until I'm good and ready to fool around. And even then, it's going to be on my terms, not yours. I'm a pornstar, after all."
        "[the_person.title] grins mischievously and walks away, leaving [mc.name] to wonder what she's thinking. But you can see the desire in her eyes, and you know she's just playing hard to get."
    return

label pornstar_compliment_response(the_person):
    mc.name "Hey [the_person.fname], you look really beautiful today. Is there a special occasion or something?"
    if the_person.is_at_work:
        if (the_person.is_employee or the_person.is_strip_club_employee) and the_person.is_wearing_uniform:
            call pornstar_flirt_response_employee_uniform_low(the_person) from _call_pornstar_flirt_response_employee_uniform_low_compliment_response
        elif the_person.is_at_job(prostitute_job):
            the_person "Ugh, why do you always want to hang out with me? Can't you see I'm busy getting fucked by other guys and making money?"
        elif the_person.sluttiness > 50:
            the_person "I'm doing great, thanks for asking. And I'm feeling especially pornstar today, so maybe we can do something about that. Like, maybe you can fuck me in the bathroom?"
        else:
            the_person "Oh, stop it, you're making me blush. There's no special occasion, I just felt like dressing up today and showing off my tits. But maybe you can help me take them out and play with them?"
    else:
        the_person "Well, I did put in a bit of extra effort today. You're just the first one to notice. But thanks, I guess. Maybe you can reward me with a fuck, and maybe even a creampie?"
    "You try to press for more information, but [the_person.possessive_title] just smiles coyly and changes the subject, leaving you wondering what's going on. But you can see the desire in her eyes, and you know she's just playing hard to get."
    return

label pornstar_compliment_response_girlfriend(the_person):
    mc.name "Hey [the_person.title]. You're looking very nice this [StringInfo.time_of_day_string]."
    if the_person.is_at_work:
        if (the_person.is_employee or the_person.is_strip_club_employee) and the_person.is_wearing_uniform:
            call pornstar_flirt_response_employee_uniform_mid(the_person) from _call_pornstar_flirt_response_employee_uniform_mid_compliment_response_girlfriend
            $ the_person.call_dialogue("flirt_response_employee_uniform_mid")
        elif the_person.sluttiness > 50:
            the_person "Mmm, thank you, [the_person.mc_title]. Wanna find out how nice I am... in bed? Maybe we can even try some new positions and get a little kinky."
            "[the_person.possessive_title!c] gives you a sultry smile, her eyes sparkling with desire and her body language screaming 'fuck me'."
        else:
            the_person "Hmph, really? Thanks, [the_person.mc_title]. You're not so bad yourself. But I'm still not going to make it easy for you. You're going to have to work for it, and maybe even use a little bit of force."
    else:
        the_person "Ugh, don't be ridiculous. It's just a normal day... but thanks, I guess. Maybe you can make it a little more interesting, though. Like, maybe we can have a threesome or something?"
        mc.name "Oh come on, don't be like that. You know you look great. And I know you're a great fuck, too."
        the_person "Aww, stop it, [the_person.mc_title]. You're making me blush... and horny. Maybe we can do something about that later, like maybe a little bit of anal or something."
    "You chat with [the_person.possessive_title] for a while, and although she's initially annoyed by your compliments, she starts to warm up to you. And maybe even gets a little turned on and ready to get fucked."
    return

label pornstar_compliment_response_affair(the_person):
    mc.name "Hey [the_person.title]. You're looking absolutely amazing this [StringInfo.time_of_day_string]."
    if the_person.is_at_work:
        if (the_person.is_employee or the_person.is_strip_club_employee) and the_person.is_wearing_uniform:
            call pornstar_flirt_response_employee_uniform_mid(the_person) from _call_pornstar_flirt_response_employee_uniform_mid_compliment_response_affair
        elif the_person.sluttiness > 50:
            the_person "Mmmm, thank you [the_person.mc_title], wanna go somewhere a little more private, so you can make me feel how amazing I am? Maybe with your cock, and maybe even a creampie?"
            "[the_person.possessive_title!c] gives you a sultry smile, her eyes sparkling with desire and her body language screaming 'fuck me'."
        else:
            the_person "Hmph, really? Thanks, [the_person.mc_title]. You're not so bad yourself. But I'm still not going to make it easy for you. You're going to have to work for it, and maybe even use a little bit of force."
    else:
        the_person "Ugh, don't be silly. It's just a normal day... but thanks, I suppose. Maybe you can make it a little more interesting, though. Like, maybe we can have a threesome or something?"
        mc.name "Oh come on, don't be like that. You know you look great. And I know you're a great fuck, too."
        the_person "Aww, stop it, [the_person.mc_title]. You're making me blush... and a little annoyed. But maybe also a little turned on and ready to get fucked."
    "You keep chatting with [the_person.possessive_title] for a while, slipping in a few more compliments. She is quite charmed by your attentiveness, and maybe even gets a little horny and ready to get fucked."
    return

label pornstar_flirt_response(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 50:
            the_person "Ugh, fine. You're not totally terrible, [the_person.mc_title]. And maybe even a little sexy... and maybe even a little bit of a turn-on."
            "[the_person.possessive_title!c] gives you a sultry smile, her eyes sparkling with desire and her body language screaming 'fuck me'."
        else:
            the_person "Whatever. Thanks for the compliment, [the_person.mc_title]. You're not a complete loser... but maybe you can be a complete winner if you fuck me right and make me cum."

    elif the_person.has_significant_other:
        if the_person.sluttiness + (the_person.opinion.cheating_on_men*5) > 50:
            the_person "Oh, you think you're so clever, don't you? I'll give you that... and maybe even give you my pussy, too. I love to be a cheating slut, and I love to get fucked by other guys."
            "[the_person.title] gives you a sly look, her eyes narrowing and her body language screaming 'fuck me'."
        else:
            the_person "You're really pushing your luck, [the_person.mc_title]. I have a [the_person.so_title] you know... but maybe I'll cheat on them with you, if you're lucky and if you can make me cum."
            mc.name "What about you, do you appreciate it?"
            "She rolls her eyes and crosses her arms, but you can see the desire in her eyes and her body language screaming 'fuck me'."
            the_person "Maybe I do, maybe I don't... but maybe I'll make it your business, if you're good enough and if you can make me cum."

    else:
        if the_person.sluttiness > 50:
            the_person "Fine... maybe you're worth my time, [the_person.mc_title]. And maybe even worth fucking... and maybe even worth making me cum."
            "[the_person.title] gives you a half-smile, but her eyes remain guarded... but you can see the desire in them and her body language screaming 'fuck me'."
        else:
            the_person "Whatever... you're not unattractive, I suppose. But don't think that means I'll go easy on you... you'll have to really impress me, with your cock and with your skills in bed."
            the_person "You'll have to really impress me though, I have high standards... but maybe you can meet them, if you're good enough and if you can make me cum."
    return

label pornstar_flirt_response_employee_uniform_low(the_person):
    if the_person.is_wearing_forced_uniform:
        the_person "Hmph, I suppose you like seeing me in this uniform... I mean, I'm practically naked and ready to be fucked! It's like I'm a pornstar or something."
        mc.name "I know you don't like it, but I needed to make a point... and maybe get a little turned on, too. You look so sexy and so fuckable in that uniform."
        the_person "I know, I know... you always were one to make a point... and get me wet. But maybe I'll forgive you this time, if you can make me cum."
        $ mc.change_locked_clarity(5)
        "She crosses her arms over her chest, but can't hide the small smile on her face as she starts to get turned on and her body language screams 'fuck me'."

    elif the_person.judge_outfit(the_person.outfit):
        #She's in uniform and likes how it looks.
        the_person "Oh, you noticed? I thought it was a bit much, but I guess it's not so bad... especially since I get to show off my tits and ass and maybe even get a little attention."
        the_person "I mean, it's nice to work somewhere where I can be a slut and get away with it... and maybe even get a little bit of cock on the side."
        $ mc.change_locked_clarity(5)
        "She winks at you, then turns to adjust her uniform, accentuating her hips and showing off her body and maybe even a little bit of her underwear."

    else:
        #She's in uniform, but she thinks it's a little too pornstar.
        if the_person.vagina_visible:
            # Her pussy is on display.
            the_person "Hmph, I suppose you like seeing me like this... I mean, my pussy is right out in the open and ready to be fucked! It's like I'm a pornstar or something."
            mc.name "Well, you know that it's..."
            the_person "I know, I know... it's company policy... but I have to admit, it's kind of turning me on and making me want to get fucked."
            mc.name "Give it some time and you'll get used to it... or maybe you'll just get more and more turned on and want to get fucked even more."
            $ mc.change_locked_clarity(5)
            "She rolls her eyes, but doesn't argue as she starts to get more and more turned on and her body language screams 'fuck me'."

        elif the_person.tits_visible:
            # Her tits are out
            the_person "Ugh, I'm still getting used to being so... exposed in this uniform. But at least I get to show off my tits and maybe even get a little attention... and maybe even get a little bit of cock."
            mc.name "You look incredible and you're comfortable. I call that a success... and maybe even a little sexy."
            $ mc.change_locked_clarity(5)
            "She huffs, but can't hide her smile as she starts to get turned on and her body language screams 'fuck me'."
            the_person "Yeah, yeah... you're just trying to make me feel better... and maybe even get me to fuck you. But maybe I'll forgive you this time, if you can make me cum."

        elif the_person.underwear_visible:
            # Her underwear is visible.
            the_person "Hmph, I probably would have picked something that kept me a little more covered, but at least our uniform is comfortable... and maybe even a little sexy... and maybe even a little bit of a turn-on."
            mc.name "It may be a little unconventional, but you look fantastic. You've got exactly the right kind of body for it... and maybe even the right kind of personality, too."
            the_person "Well, that's one way to look at it, I suppose... but I have to admit, it's kind of turning me on and making me want to get fucked."
            $ mc.change_locked_clarity(5)
            "She playfully rolls her eyes and turns to adjust her uniform, showing off her body and maybe even a little bit of her underwear and her body language screams 'fuck me'."

        else:
            # It's just generally pornstar.
            the_person "Ugh, well thank you! Our uniforms are a little bold for my taste, but I guess I look good in it... and maybe even a little pornstar, too. Maybe I'll even get a little bit of cock out of it."
            $ mc.change_locked_clarity(5)
            "She blushes and looks away, but not before you catch a glimpse of her small smile as she starts to get turned on and her body language screams 'fuck me'."
    return

label pornstar_flirt_response_employee_uniform_mid(the_person):
    if the_person.is_wearing_forced_uniform:
        $ mc.change_locked_clarity(10)
        if the_person.vagina_visible:
            the_person "Ugh, fine. You caught me off guard. I'll admit, this uniform does make me look good, especially with my pussy on display like a dirty little slut. I feel like I'm just begging to be fucked."
            mc.name "It's a great uniform, but that's not what's important here. What's important is how sexy you look in it, and how much I want to fuck you."
            the_person "Yeah, yeah. You're right. It's just hard not to feel like a sex object in this thing, especially with my cunt on display for everyone to see. But maybe that's what I want, to be a sex object for you."
        elif the_person.tits_visible:
            the_person "Ugh, fine. You caught me off guard. I'll admit, this uniform does make me look good, especially with my boobs popping out like a pair of juicy melons. I feel like I'm just begging to be sucked."
            mc.name "It's a great uniform, but that's not what's important here. What's important is how sexy you look in it, and how much I want to suck your tits."
            the_person "Yeah, yeah. You're right. It's just hard not to feel like a sex object in this thing, especially with my nipples hard and ready for action. But maybe that's what I want, to be a sex object for you."
        else:
            the_person "Ugh, fine. You caught me off guard. I'll admit, this uniform does make me look good... and maybe even a little pornstar, too. I feel like I'm just begging to be fucked."
            mc.name "It's a great uniform, but that's not what's important here. What's important is how sexy you look in it, and how much I want to fuck you."
            the_person "Yeah, yeah. You're right. It's just hard not to feel like a sex object in this thing, especially when I'm wearing it like a dirty little slut. But maybe that's what I want, to be a sex object for you."
        mc.name "Rules are rules and I can't make any exceptions, even if they look good... and sexy. But maybe I can make an exception for you, if you're willing to be my sex object."
        "She sighs and nods, her eyes sparkling with desire."
        the_person "Yeah, I know. At least you're having a good time. I don't mind that so much... especially if it means you'll fuck me later and make me cum."
    elif the_person.judge_outfit(the_person.outfit):
        $ mc.change_locked_clarity(10)
        if the_person.tits_visible:
            the_person "Hmph, maybe I should wear this outfit more often. It's getting a lot of attention, especially for my boobs... and maybe even a little bit of action, too. I feel like I'm just begging to be sucked."
            mc.name "It's a great outfit, but I'm more interested in the person wearing it... and maybe even fucking them, too. I want to suck your tits and fuck your pussy."
            the_person "Oh, really? Is that so? I guess my boobs are hard to ignore... especially when they're bouncing around like a pair of juicy melons. But maybe that's what I want, to be ignored and just fucked."
        else:
            the_person "Hmph, maybe I should wear this outfit more often. It's getting a lot of attention... and maybe even a little bit of action, too. I feel like I'm just begging to be fucked."
            mc.name "It's a great outfit, but I'm more interested in the person wearing it... and maybe even fucking them, too. I want to fuck your pussy and make you cum."
            the_person "Oh, really? Is that so? I guess my vagina is hard to ignore... especially when it's wet and ready for action. But maybe that's what I want, to be ignored and just fucked."
        the_person "Maybe I'll invite you shopping one day and you can tell me what else you want to see me in... or maybe even what else you want to do to me. Maybe we can even have a threesome or something."
        mc.name "Sounds like a good time... and maybe even a little bit of fun, too. I'd love to have a threesome with you and another girl, or maybe even another guy."

    else:
        # the_person "I think it shows off a little too much!"
        the_person "Ugh, fine. You're not gonna make this easy for me, are you? You're just going to make me feel like a dirty little slut all day. But maybe that's what I want, to be a dirty little slut for you."
        $ mc.change_locked_clarity(10)
        if the_person.vagina_visible:
            the_person "I'm trying to focus on my work here, not flirt with you all day. And definitely not with my pussy on display like a dirty little cunt. But maybe that's what I want, to be a dirty little slut for you."
        elif the_person.tits_visible:
            the_person "I'm trying to focus on my work here, not flirt with you all day. And definitely not with my boobs popping out like a pair of juicy melons. But maybe that's what I want, to be a juicy melon for you to suck."
        else:
            the_person "I'm trying to focus on my work here, not flirt with you all day! But maybe I'll make an exception for you... especially if you're going to fuck me later and make me cum."
        mc.name "I understand, but I promise it's important for the business... and maybe even for your pleasure, too. I want to make you cum and feel good, and maybe even make you my sex object."
        "She sighs and nods, her eyes sparkling with desire."
        the_person "Yeah, I know. You're a real pain, you know that? But maybe I'll forgive you if you fuck me good and hard and make me cum."
    return

label pornstar_flirt_response_low(the_person):
    #She's in her own outfit.
    the_person "Hmph, I suppose it's not the worst outfit I've ever worn... but it's definitely one of the sluttiest. I feel like I'm just begging to be fucked."
    $ the_person.draw_person(position = "walking_away")
    $ mc.change_locked_clarity(5)
    "She rolls her eyes and gives you a quick spin, showing off her outfit from every angle and making sure you get a good look at her ass."
    the_person "I mean, I guess it's not too bad, right? Especially since it shows off my tits so well. Maybe I'll even let you suck them later."
    $ the_person.draw_person()
    mc.name "I think it looks great on you... and it's definitely making me hard. I want to fuck you so bad."
    the_person "Oh, shut up. You're just saying that to get in my pants... but it might just work. Maybe I'll even let you cum inside me."
    return

label pornstar_flirt_response_low1(the_person):
    if the_person.has_significant_other:
        the_person "Ugh, what's with you and the flirting? I've got a [the_person.so_title], and I don't think he'd appreciate you getting all up in my grill... but maybe I do, and maybe I'll even cheat on him with you if you're lucky."
        mc.name "What about you, do you appreciate it?"
        "She rolls her eyes and smirks, her eyes sparkling with desire and her body language screaming 'fuck me'."
        the_person "Maybe I do... and maybe I'll even let you fuck me in the ass if you're lucky."
    else:
        the_person "Well, thanks for the compliment. But don't think you're getting off that easy. I have high standards, and you'll need to prove yourself to me... in bed, and maybe even with a creampie."
        the_person "But if you can impress me, who knows what might happen... maybe we'll even have a threesome or something, and maybe even get a little bit kinky."
    $ mc.change_locked_clarity(5)
    return

label pornstar_flirt_response_mid(the_person):
    if mc.location.person_count > 1 and the_person.effective_sluttiness("kissing") < (25 - (5*the_person.opinion.public_sex)):
        $ mc.change_locked_clarity(10)
        the_person "You know, I was wondering if you actually noticed my outfit today... and if you're interested in seeing more of it, like maybe my pussy or my tits."
        "Her eyes narrow slightly, but she's still trying to appear casual and flirtatious, and her body language is screaming 'fuck me'."
        mc.name "I noticed. It looks great on you... especially your boobs, and maybe even your nipples, too."
        the_person "Oh, really? Thanks, I guess. I was thinking you might say something like that... and maybe even try to suck on them, or maybe even fuck me."
        "She crosses her arms, trying to maintain a tough exterior, but her eyes are sparkling with desire and her body language is screaming 'fuck me'."
        if the_person.tits_visible:
            mc.name "I noticed. It looks great on you. Especially your boobs... and maybe even your nipples, too. I want to suck on them so bad."
            the_person "Oh, really? Thanks, I guess. I was thinking you might say something like that... and maybe even try to suck on them, or maybe even fuck me."
            "She crosses her arms, trying to maintain a tough exterior, but her eyes are sparkling with desire and her body language is screaming 'fuck me'."
        else:
            mc.name "Well, it's true. You look amazing... and maybe even a little bit pornstar, too. I want to fuck you so bad."
        the_person "Hmph. Maybe I'll invite you shopping one day, so you can tell me what else you want to see me in... and maybe even what else you want to do to me, like maybe fuck me in the ass."
        "She leans in slightly, a hint of flirtation in her voice, and her eyes sparkling with desire and her body language screaming 'fuck me'."
        mc.name "I can think of a few things already... and I'm sure I'd enjoy seeing you in them... and maybe even fucking you in them, too."
        the_person "I'm sure you would. So, what do you say? Want to take me out for a drink and maybe we can discuss my wardrobe some more... and maybe even get a little bit naughty, too, like maybe fuck in the bathroom?"

    else:
        the_person "Thanks, I thought I looked pretty hot in it too... and maybe even a little bit pornstar, too. I want to show you my pussy and my tits."
        the_person "You want a better look, right? Here, how does it make my ass look... and maybe even my pussy, too?"
        $ the_person.draw_person(position = "back_peek")
        $ mc.change_locked_clarity(10)
        the_person "Good, right? Maybe you can even get a peek at my pussy if you're lucky, or maybe even fuck me if you're really lucky."
        mc.name "Fantastic. I wish I could get an even better look at it... and maybe even touch it, too. I want to fuck you so bad."
        "[the_person.possessive_title!c] smiles and turns back to face you, her eyes sparkling with desire and her body language screaming 'fuck me'."
        $ the_person.draw_person()
        the_person "I'm sure you do. Take me out for a drink and maybe we can work something out... and maybe even get a little bit naughty, too, like maybe fuck in the car."
    return

label pornstar_flirt_response_mid1(the_person):
    $ mc.change_locked_clarity(10)
    the_person "Thanks, I do look amazing in this outfit... and I know you're dying to get a peek at what's underneath, like maybe my pussy or my tits."
    if (the_person.has_skirt or the_person.has_dress) and not the_person.has_thigh_high_socks:
        mc.name "You could change it up with some high stockings, I would love to see that... and maybe even get a glimpse of your pussy, or maybe even fuck you."
        the_person "Oh, really? And why would you want to see that? You're not going to get a peek or anything, are you... or maybe you will, if you're lucky, and maybe even get to fuck me."
        mc.name "Because it would look great on you, and I would enjoy the view... and maybe even get a little bit turned on, and maybe even cum in my pants."

    mc.name "How about you and me go and grab a coffee sometime... and maybe even get a little bit naughty, like maybe fuck in the bathroom?"
    if the_person.has_significant_other:
        the_person "Sure, my [the_person.so_title] doesn't mind... as long as they're not around to witness how much fun we're going to have, and how many times I'm going to cum, and maybe even how many times you're going to cum inside me."
    else:
        the_person "Why not, I could use a pick-me-up once in a while... and maybe someone to pick me up from the ground when I fall for you, and onto your cock, and maybe even get fucked by you."
    the_person "Just let me know when, I would love to... and don't think I won't notice if you're trying to get a glimpse of my legs under the table, or maybe even my pussy, or maybe even try to fuck me under the table."
    mc.name "I'll keep that in mind, and maybe we can discuss what else you want to wear in the future... or not wear, like maybe just a thong and a bra, or maybe even nothing at all."
    the_person "Hmph, maybe. But don't think you're getting a discount on my wardrobe just because we're going out for coffee... or anything else, like maybe a blowjob, or maybe even a creampie."
    return

label pornstar_flirt_response_high(the_person):
    if mc.location.person_count > 1 and the_person.effective_sluttiness() < (25 - (5*the_person.opinion.public_sex)): # There are other people here, if she's not pornstar she asks if you want to find somewhere quiet
        the_person "You're really persistent, huh? Fine, but not here... let's go somewhere we can get a little more... intimate, like maybe a hotel room or something."
        "She glances around before giving you a sly smile and a wink, and maybe even a little bit of a blowjob motion with her mouth."
        menu:
            "Find somewhere more quiet\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                mc.name "Then let's find somewhere that isn't here... where we can get a little more... naked, and maybe even fuck like rabbits."
                the_person "Hmph, eager much? Alright, let's go... and maybe we can even get a little more... naughty, like maybe have a threesome or something."
                call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_pornstar_flirt_response_high_2
                the_person "So... Now what's your plan? Want to get a little more... intimate, like maybe fuck me in the ass or something?"

                if the_person.is_willing(kissing):
                    $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
                    if the_person.has_taboo("kissing"):
                        "You lean in close to kiss [the_person.title]... and maybe even get a little more... passionate, like maybe with some tongue action or something."
                        $ the_person.call_dialogue("kissing_taboo_break")
                        $ the_person.break_taboo("kissing")
                        "She responds passionately, her arms wrapping around your neck and her tongue in your mouth, and maybe even a little bit of a blowjob motion with her mouth."
                    else:
                        "You step close to [the_person.title] and put your arm around her waist, pulling her close and kissing her... and maybe even getting a little more... intimate, like maybe with some groping or something."
                        "She responds immediately and eagerly presses her body against yours, her hands all over your body, and maybe even a little bit of a handjob motion with her hands."
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _vt_pornstar_call_fuck_person_49
                else:
                    if the_person.has_taboo("touching_body"):
                        $ the_person.call_dialogue("touching_body_taboo_break")
                        $ the_person.break_taboo("touching_body")
                        "You take her hand and pull her close against you... and maybe even get a little more... intimate, like maybe with some touching or something. She looks into your eyes and smiles, and maybe even a little bit of a blowjob motion with her mouth."
                    else:
                        "You take her hand and pull her close, your lips brushing against her ear... and maybe even getting a little more... passionate, like maybe with some dirty talk or something."
                    call fuck_person(the_person, private = True, start_position = standing_grope, skip_intro = True) from _call_fuck_person_pornstar_flirt_grope

                $ the_person.call_dialogue("sex_review", the_report = _return)
                call mc_restore_original_location(the_person) from _call_mc_restore_original_location_pornstar_flirt_response_high_2

            "Just flirt":
                mc.name "You know you want to, come on. I'll take you out for dinner, and then we can see where the night takes us... maybe even to the bedroom, and maybe even with some sex toys or something."
                the_person "Hmm, you're really trying to charm me, aren't you? Well, I'll tell you what... If you can make me laugh, I might consider it... and maybe even get a little more... intimate, like maybe with some oral sex or something."
                "She smiles mischievously, clearly enjoying the challenge and the flirtation, and maybe even a little bit of a blowjob motion with her mouth."

    else:
        if mc.location.person_count == 1: #You're alone, so she just didn't meet the sluttiness threshold
            the_person "Hmm, you're really eager, aren't you? Well, I suppose it's just the two of us here... so we can get a little more... intimate, like maybe with some kissing or something."
            "[the_person.possessive_title!c] glances around, confirming you're alone and then gives you a sly smile, and maybe even a little bit of a blowjob motion with her mouth."
            the_person "So what's your plan? Want to get a little more... naughty, like maybe with some sex toys or something?"

        else:  # You aren't alone but she's still into it.
            the_person "Feeling bold today, huh? Well, I think your chances are pretty good... and maybe we can even get a little more... intimate, like maybe with some public sex or something."
            "[the_person.title] smirks, clearly enjoying the attention and the flirtation, and maybe even a little bit of a blowjob motion with her mouth."
            if the_person.has_large_tits: #Bounces her tits for you
                $ mc.change_locked_clarity(15)
                "[the_person.title] grabs her tits and jiggles them for you, her eyes sparkling with desire, and maybe even a little bit of a handjob motion with her hands."
                the_person "Maybe I can get these girls out for you... and maybe even get a little more... naked, like maybe with some nipple play or something. Does that sound nice?"

            else: #No big tits, so she can't bounce them (as much)
                "[the_person.title] runs her hands over her hips sensually, obviously encouraging you to take things further... and maybe even get a little more... intimate, like maybe with some touching or something."

        menu:
            "Touch her" if not the_person.is_willing(kissing):
                "You step closer to [the_person.title] and move your hands down her waist... and maybe even get a little more... intimate, like maybe with some groping or something."
                if the_person.has_taboo("touching_body"):
                    the_person "Oh, you're brave. I like that... and maybe we can even get a little more... naughty, like maybe with some sex toys or something."
                    $ the_person.call_dialogue("touching_body_taboo_break")
                    $ the_person.break_taboo("touching_body")

                call fuck_person(the_person, start_position = standing_grope, private = False) from _call_fuck_person_flirt_response_pornstar_touching

            "Kiss her" if the_person.is_willing(kissing):
                $ the_person.draw_person()
                if the_person.has_taboo("kissing"):
                    "You put your arm around [the_person.possessive_title] and lean in close... and maybe even get a little more... passionate, like maybe with some tongue action or something."
                    $ the_person.call_dialogue("kissing_taboo_break")
                    $ the_person.break_taboo("kissing")
                    "She responds with a passionate kiss, her arms wrapping around your neck and her tongue in your mouth, and maybe even a little bit of a blowjob motion with her mouth."
                else:
                    "You pull [the_person.possessive_title!] close and kiss her... and maybe even get a little more... intimate, like maybe with some oral sex or something."
                    "She responds with a passionate kiss, her arms wrapping around your neck and her hands all over your body, and maybe even a little bit of a handjob motion with her hands."

                call mc_move_to_private_location(the_person) from  _call_mc_move_to_private_location_pornstar_flirt_response_high
                call fuck_person(the_person, start_position = kissing, private = _return, skip_intro = True) from _vt_pornstar_call_fuck_person_50
                $ the_person.call_dialogue("sex_review", the_report = _return)
                call mc_restore_original_location(the_person) from _call_mc_restore_original_location_pornstar_flirt_response_high

            "Just flirt":
                $ the_person.draw_person()
                mc.name "Very tempting, but you're going to have to contain yourself for now... maybe."
                the_person "Oh, you're not going to take advantage of me right now, are you? Fine, be that way... but maybe later we can get a little more... intimate, like maybe with some sex toys or something."
                "[the_person.title] pouts, clearly enjoying the flirtation and the attention, and maybe even a little bit of a blowjob motion with her mouth."
    return

label pornstar_flirt_response_low_energy(the_person):
    if the_person.sluttiness > 40:
        the_person "Ugh, thanks for the compliment, but I'm so tired right now... and so fucking horny. I just want to get fucked and cum."
    else:
        the_person "Thanks, but I'm beat. Can we pick this up later... maybe in bed, with some sex toys and a little bit of kink?"
    return

label pornstar_flirt_response_girlfriend(the_person):
    # Lead in: mc.name "You're so beautiful [the_person.title], I'm so lucky to have a woman like you in my life."
    if mc.location.person_count > 1:
        # There are other people around, so she'll only start making out with you if she's pornstar.
        if the_person.effective_sluttiness("kissing") < (25 - (5*the_person.opinion.public_sex)):
            # Not very pornstar, so she wants to find somewhere private
            the_person "Oh my god, you're so cheesy. Come here and kiss me like you mean it, with some tongue and some passion."
            "She pulls you against her and kisses you, her lips soft and gentle, but also a little bit dirty and slutty."
            the_person "There, now you can't say I don't know how to kiss... or how to make you hard and horny."
            mc.name "Haha, yeah I guess not... but I'm definitely getting hard now and wanting to fuck you."
            "You put your arms around her and kiss her back, feeling her warmth and her tits pressing against your chest, and maybe even a little bit of her pussy grinding against your cock."
            the_person "Mmm, yeah, like that. Maybe we can even get a little more... intimate and naughty."
            menu:
                "Find somewhere more quiet\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                    mc.name "Why wait? Come on, I'm sure we can find somewhere quiet... and private, where we can fuck and cum."
                    the_person "You're always so eager, aren't you? Alright, let's go and get a little more... naughty and slutty."
                    "You and [the_person.possessive_title] hurry off, searching for a private spot to get a little more... intimate and maybe even have a threesome."
                    call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_pornstar_flirt_response_girlfriend_2
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _vt_pornstar_call_fuck_person_76
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_pornstar_flirt_response_girlfriend_2

                "Just flirt":
                    $ mc.change_locked_clarity(10)
                    "You reach around and pull her closer, running your hand down her back and over her ass, and maybe even a little bit of her pussy."
                    mc.name "You're so beautiful, and you know it... and you're also so sexy and pornstar, and you know that too."
                    "She rolls her eyes but leans in for a quick kiss, her tongue darting in and out of your mouth, and maybe even a little bit of a blowjob motion with her mouth."
                    the_person "Fine, you caught me. But don't think this means I'm going easy on you... or that I'm not going to make you cum and scream my name."

        else:
            the_person "Well if I'm so beautiful, then why are you just standing there? Come on, kiss me like you mean it, with some passion and some tongue!"
            "You put your arm around her waist and pull her close, kissing her deeply and passionately, your tongues entwining, and maybe even a little bit of a handjob motion with your hands."
            "When you break the kiss, [the_person.possessive_title] sighs and leans against you, her body trembling with desire, and maybe even a little bit of her pussy grinding against your cock."
            the_person "You're not so bad yourself... and you're definitely making me wet and horny."
            menu:
                "Make out":
                    "You lean back in and kiss her again, this time more passionately and with a little more... tongue, and maybe even a little bit of a blowjob motion with your mouth."
                    "[the_person.title] responds eagerly, wrapping her arms around your neck and pulling you closer, her body grinding against yours, and maybe even a little bit of her pussy grinding against your cock."

                    call mc_move_to_private_location(the_person) from  _call_mc_move_to_private_location_pornstar_flirt_response_girlfriend
                    call fuck_person(the_person, start_position = kissing, private = _return, skip_intro = True) from _vt_pornstar_call_fuck_person_77
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_pornstar_flirt_response_girlfriend

                "Just flirt":
                    mc.name "I'm not bad? You're the one who's hard to resist... and also hard to keep my hands off of, and maybe even hard to keep my cock out of."
                    $ mc.change_locked_clarity(10)
                    "You reach out and touch her cheek, a playful grin on your face, and then you run your hand down her body, over her tits and to her pussy, and maybe even a little bit of her ass."
                    the_person "Ugh, you're so annoying. But I guess I like that about you... and also how you make me feel, all wet and horny and ready to get fucked."

    else:
        # You're alone, so she's open to fooling around.
        the_person "Well you've got me all alone, so how about you show me just how lucky you feel... and also how hard you are, and maybe even how good you are at fucking."
        "She reaches down to your waist and cups your crotch, rubbing it gently and making you even harder, and maybe even a little bit of a handjob motion with her hands."
        mc.name "You're so wet for me already... and also so ready to get fucked and cum."
        the_person "Hmph, maybe... but definitely, and maybe even a little bit of a creampie or something."
        "She grinds against you, her hips moving in a slow circle, and her body trembling with desire, and maybe even a little bit of her pussy grinding against your cock."
        mc.name "Damn, you feel so good... and also so pornstar and slutty."
        "You reach up and grab her breasts, squeezing them gently and making her moan with pleasure, and maybe even a little bit of a blowjob motion with her mouth."
        the_person "Ooh, don't do that... but also don't stop, and maybe even do it a little bit harder and a little bit faster."
        "But she doesn't pull away, her body still pressed against yours, and her pussy still grinding against your cock, and maybe even a little bit of her ass grinding against your leg."
        menu:
            "Kiss her":
                if the_person.has_taboo("kissing"):
                    $ the_person.call_dialogue("kissing_taboo_break")
                    $ the_person.break_taboo("kissing")

                "You put your arms around [the_person.possessive_title]'s waist and rest your hands on her ass, and maybe even a little bit of her pussy. You pull her close and kiss her sensually, with a little more... tongue, and maybe even a little bit of a blowjob motion with your mouth."
                "She responds by pressing her body against you and grinding her hips against your thigh, making you even harder, and maybe even a little bit of her pussy grinding against your cock."
                "You grab her hips and pull her closer, your crotches pressed together, and your bodies trembling with desire, and maybe even a little bit of a creampie or something."
                call fuck_person(the_person, start_position = kissing, skip_intro = True) from _vt_pornstar_call_fuck_person_78
                $ the_person.call_dialogue("sex_review", the_report = _return)
                $ the_person.review_outfit()

            "Just flirt":
                mc.name "I'm going to make you beg for it... and also make you cum so hard and scream my name."
                "You lean in close, your breath hot against her ear, and your words making her tremble with desire, and maybe even a little bit of her pussy grinding against your cock."
                the_person "Ooh, you're such a bad boy. I love it... and also how you make me feel, all wet and horny and ready to get fucked."
                "She rubs her body against yours, her hips moving seductively, and her pussy grinding against your cock, and maybe even a little bit of her ass grinding against your leg."
                the_person "But don't think you're getting off that easy. I'm going to make you work for it... and also make you make me cum, and maybe even a little bit of a creampie or something."
    return

label pornstar_flirt_response_affair(the_person):
    # Lead in: mc.name "You look so good today [the_person.title], you're making me want to do some very naughty things to you."
    if mc.location.person_count > 1: #There are other people around, she's nervous about people finding out what you're doing.
        if (the_person.opinion.cheating_on_men *15) + the_person.effective_sluttiness() > 50: #SHe's turned on by flirting in public or doesn't think anything is wrong with it
            "[the_person.possessive_title!c] blushes and playfully bats her eyes at you, her nipples hardening with excitement, and her body language screaming 'fuck me'."
            the_person "Oh, you're making me blush... and also making me wet. I'm not used to this kind of attention from you, but I have to admit, I'm loving it, and also loving the way you're making me feel, all horny and ready to get fucked."
            the_person "But I have to admit, I'm curious. What do you have in mind? Want to take me somewhere private and fuck me senseless, and maybe even cum inside me?"
            menu:
                "Find somewhere more quiet\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                    mc.name "I was thinking we could slip away and find a more private spot... where we can get a little more... intimate, and maybe even have a threesome or something."
                    "You and [the_person.title] exchange a flirtatious glance before hurrying off to find a quiet spot, your hands all over each other's bodies, and your bodies pressed together."
                    call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_pornstar_flirt_response_affair
                    $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
                    "As soon as you're alone she pulls you into a deep and passionate kiss, her tongue darting in and out of your mouth, and her body language screaming 'fuck me'."
                    $ the_person.draw_person(position = "kissing")
                    the_person "Mmm... I've been wanting to do that for a while now. And maybe even get a little more... naughty, like maybe have some anal sex or something."
                    "You wrap your arms around her waist and kiss her back, your hands all over her body, and your cock hardening with excitement."
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _vt_pornstar_call_fuck_person_79
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_pornstar_flirt_response_affair

                "Just flirt":
                    mc.name "I can't help but notice how beautiful you look today, [the_person.title]... and also how sexy like a pornstar you are, and how much I want to fuck you."
                    the_person "Stop it, you're making me blush! But I have to admit, you look pretty great yourself... and also pretty hard, and pretty ready to get laid."
                    the_person "Just don't get too cocky, okay? I'm still in charge here... but maybe not for long, if you keep talking like that, and maybe even not for long if you keep making me feel like this, all horny and ready to get fucked."
                    $ mc.change_locked_clarity(20)
                    "[the_person.possessive_title!c] playfully swats at your arm before leaning in close, her breasts pressing against your chest, and her body language screaming 'fuck me'."
                    the_person "But I have to admit, I'm getting a little turned on by this whole thing... and maybe even a little bit wet, and maybe even a little bit ready to get fucked."
                    "You can't help but feel a little flustered as she teases you, your cock hardening with excitement, and your body language screaming 'fuck her'."
                    mc.name "I can see that. Maybe we should find a more private place to continue this... and maybe even get a little more... intimate, like maybe have some sex or something."
                    the_person "Mmm, maybe we should. But first, let's enjoy this little moment here... and maybe even get a little more... naughty, like maybe have some oral sex or something."

        else: #She's shy or nervous about being discovered
            "[the_person.possessive_title!c] looks around nervously, then back at you with a sheepish grin, her face flushing with embarrassment, and her body language screaming 'don't get caught'."
            the_person "Oh, um, you look nice today... and also a little bit sexy, I have to admit, but maybe we shouldn't be doing this here, in public."
            mc.name "Wait, don't go! I was thinking we could... uh, grab a drink or something... and maybe even get a little more... intimate, like maybe have some sex or something."
            $ mc.change_locked_clarity(15)
            the_person "Oh, you want to grab a drink? Okay, sure. But just for a little bit, okay? I don't want to be out too late... or get caught by my [the_person.so_title], or maybe even get caught by someone else."
            "She glances around again, then leans in close and whispers, her breath hot against your ear, and her body language screaming 'fuck me'."
            the_person "And just so you know, I'm still in charge here, even if we're just grabbing a drink... but maybe not for long, if you keep talking like that, and maybe even not for long if you keep making me feel like this, all horny and ready to get fucked."
            "You can't help but feel a little excited by her assertiveness, and also a little bit turned on, and maybe even a little bit ready to get laid."
            mc.name "Okay, okay. I'll behave... for now, at least, but maybe not for long, if you keep looking at me like that, and maybe even not for long if you keep making me feel like this, all horny and ready to get laid."

    else:
        # the_person "Yeah? Well there's nobody around, and I'm not going to stop you."
        the_person "Oh yeah? Well then, do you want to share what all of these naughty things are? You have my attention... and also my body, if you want it, and maybe even my pussy, if you want to fuck it."
        menu:
            "Feel her up":
                "You put your arms around [the_person.possessive_title]'s waist and rest your hands on her ass, squeezing it gently, and maybe even a little bit roughly."
                mc.name "You know, I've been waiting for this moment for a while now... and I'm not going to waste it, and maybe even not going to waste my cum, if I can help it."
                "You massage her butt, and she blushes and pushes you away lightly, but also a little bit playfully, and maybe even a little bit teasingly."
                the_person "Hey, no need to be so forward! What's gotten into you... or should I say, what's gotten into me, and maybe even what's gotten into my pussy?"
                "You pull her close again and shift your hands to her breasts, squeezing them gently, and also a little bit roughly, and maybe even a little bit like you're trying to make her cum."
                mc.name "Come on, don't be like that. I just wanted to make you feel good for once... and also make myself feel good, too, and maybe even make us both feel good, if we can manage it."
                call fuck_person(the_person, private = True, start_position = standing_grope, skip_intro = True) from _vt_pornstar_call_fuck_person_80
                $ the_person.call_dialogue("sex_review", the_report = _return)
                $ the_person.review_outfit()

            "Just flirt":
                $ mc.change_locked_clarity(10)
                "You put your arms around [the_person.possessive_title]'s waist and rest your hands on her ass, squeezing it gently, and maybe even a little bit roughly."
                mc.name "I wish I had the time. You'll have to wait until later... but maybe not too much later, if you keep looking at me like that, and maybe even not too much later if you keep making me feel like this, all horny and ready to get laid."
                "You massage her butt, and she sighs happily and leans her weight against you, her body pressing against yours, and maybe even a little bit like she's trying to make you cum."
                the_person "Aww, are you sure? I was hoping we could get a little more... intimate, right now, and maybe even have some sex or something."
                "You slap her ass and step back, and she clings to you reluctantly before letting go, her eyes sparkling with desire, and maybe even a little bit like she's trying to make you cum."
                the_person "Fine, but don't make me wait too long, okay? I have needs, and my [the_person.so_title] sure as hell isn't fulfilling them... but maybe you can, and maybe even you can make me cum."
                mc.name "I won't make you wait long. I promise... and I also promise to make it worth your while, when we do finally get together, and maybe even make it worth your while if we can manage to make each other cum."
                "She looks up at you with a playful pout, and also a little bit of a smile, and maybe even a little bit like she's trying to make you cum."
                the_person "Promise you won't make me wait? And also promise you'll make me cum, when we do finally get together, and maybe even promise to make me cum hard?"
                mc.name "I promise, baby. I'll make you cum so hard, you'll be screaming my name, and maybe even screaming for more."
                "You both share a flirtatious smile, and also a little bit of a laugh, as you both know what's going to happen next, and maybe even what's going to happen when you finally get together and have some sex."
    return

label pornstar_flirt_response_text(the_person):
    mc.name "Hey [the_person.title], how's it going? I'm feeling a bit bored and thought we could chat... or maybe even get a little more... intimate and naughty."
    "She replies with a hint of annoyance and a dash of flirtation, and maybe even a little bit of a dirty tone."
    if the_person.is_affair:
        the_person "Oh, great, you're bored again? You always seem to find ways to bother me... but I have to admit, I'm a little bored too, and maybe even a little bit horny."
        the_person "Well, what do you want this time? I'm not exactly thrilled about entertaining you... but I'm willing to make an exception if you can make me cum hard and scream your name."
        the_person "When can we get together and get a little more... naughty and dirty? I'm thinking maybe we can even have a threesome or something."
        mc.name "Some time soon. I'll let you know... and I'll make sure to bring my A-game and my big cock."

    elif the_person.is_girlfriend:
        the_person "Bored, huh? That's not exactly a surprise. You're always looking for something new to entertain yourself... and I'm happy to provide it, as long as you're willing to provide the cock and the cum."
        the_person "But fine, we can hang out. Just don't expect me to do anything special... unless you want me to wear something special, like maybe a thong or a bra, or maybe even nothing at all."
        mc.name "Some time soon. I'll let you know... and I'll make sure to bring my camera and my sex toys."

    elif the_person.love < 40:
        if the_person.effective_sluttiness() > the_person.love:
            the_person "Ugh, bored, really? Well, I suppose I can keep you company for a bit... and maybe even get a little more... intimate and naughty, like maybe have some anal sex or something."
        else:
            the_person "Bored, eh? That's not surprising. You're always looking for a new distraction... and I'm happy to provide it, as long as you're willing to provide the cock and the cum, and maybe even a creampie or something."

    else:
        if the_person.effective_sluttiness() > the_person.love:
            the_person "Fine, I'll talk to you. But don't think this means I'm happy about it... unless you're willing to make me happy and cum hard, that is."
            the_person "So, what do you want to talk about? I'm not exactly thrilled about this... but I'm willing to listen if you're willing to make me cum and scream your name."
        else:
            the_person "You're bored, huh? Well, that's your problem, not mine... but I'm happy to help you solve it, as long as you're willing to solve mine too and make me cum hard."
            the_person "So, what do you want? Just don't expect me to be all lovey-dovey about it... unless you're willing to get a little more... intimate and naughty, that is, and maybe even have some sex or something."
    return

label pornstar_condom_demand(the_person):
    if the_person.wants_creampie:
        the_person "Ugh, seriously? You need to put on a condom before we even think about doing anything... but I have to admit, I'm a little tempted to let you cum inside me and make me pregnant."
        the_person "I hate that we have to, but you know it's necessary... unless you're willing to take the risk and make me pregnant, that is, and maybe even have a creampie or something."
    else:
        the_person "For crying out loud, do you have a condom on you? Put one on before you even think about touching me... but don't think that means I don't want you to touch me, because I do, and maybe even have some sex or something."
        the_person "I don't want to be stuck with some stupid disease because you were too careless... but I'm willing to take the risk if you're willing to make it worth my while and cum hard."
    return

label pornstar_condom_ask(the_person):
    if the_person.on_birth_control:
        the_person "You want a condom? Fine, but I'm on the pill, so it's not like I really need it... but I suppose it's better to be safe than sorry, right, and maybe even have some sex or something?"
        $ the_person.update_birth_control_knowledge()
    elif the_person.wants_creampie:
        the_person "Ugh, you want to cum inside me? Just put on a condom, would you? It's not like I want to get pregnant or anything... but I have to admit, the thought of it is a little bit tempting and maybe even a little bit naughty."
        the_person "But I guess it's better than the alternative, right? I mean, who needs a condom when you can just pull out and cum all over my face and make me cum hard?"
        $ the_person.discover_opinion("creampies")
    else:
        the_person "Fine, I guess you should use a condom...but can you at least not make a mess with it? I don't want to clean up after you... but I do want to clean up after myself, if you know what I mean, and maybe even have some sex or something."
        the_person "And please, no pulling out method. That's just asking for trouble... but I'm willing to take the risk if you're willing to make it worth my while and cum hard, that is."
    return

label pornstar_condom_bareback_ask(the_person):
    if the_person.wants_creampie:
        if the_person.is_infertile:
            the_person "You're not seriously considering a condom, are you? Please, just give me your hot, sticky load and make me cum all over your cock, like a dirty little slut."
            the_person "I want to feel you fill me up and make me scream with pleasure, like a wild, reckless ride."
        elif the_person.on_birth_control:
            the_person "Don't even think about putting a condom on, [the_person.mc_title]. I'm on the pill, so we're good to go and get a little more... naughty and wild."
            the_person "Just fuck me raw and make me feel every inch of you, like a dirty little whore, and maybe even make me cum hard."
            $ the_person.update_birth_control_knowledge()
        else:
            the_person "Forget the condom, [the_person.mc_title], I want to feel you deep inside me, like a hot, throbbing cock, and maybe even get knocked up."
            the_person "I don't care about the risks, it's worth it for this kind of pleasure, like a pornstar little thrill, and maybe even a creampie or something."
            if not the_person.knows_pregnant:
                the_person "Imagine how hot it would be to get knocked up, too, like a dirty little secret, and maybe even a creampie or something."
        $ the_person.discover_opinion("creampies")
    else:
        the_person "Don't bother with a condom, [the_person.mc_title]. I want to feel you raw and unprotected, like a dirty little animal, and maybe even get a little more... naughty."
        if not the_person.knows_pregnant:
            the_person "I don't care about the risks, it's worth it for the intensity, like a wild, reckless ride, and maybe even a creampie or something."
        else:
            the_person "I love it when you fuck me raw and make me feel like I'm yours, like a dirty little possession, and maybe even a creampie or something."
    return

label pornstar_condom_bareback_demand(the_person):
    if the_person.has_breeding_fetish: #Actively looking to get knocked up.
        if the_person.knows_pregnant:
            the_person "Ugh, why bother with a condom? I want to get pregnant, so fuck me raw and make me cum all over your cock, like a dirty little mommy!"
            the_person "Hurry up, I can't wait to feel you inside me and make me a dirty little mommy, and maybe even get a creampie or something!"
        elif the_person.is_infertile:
            the_person "Oh, great, you're going to remind me I can't get pregnant? Thanks a lot, you dirty little tease, but maybe we can still have some fun and get a little more... naughty."
        else:
            the_person "Ugh, what's the point of fucking if you're not going to knock me up? Get inside me and make me a dirty little mommy, and maybe even get a creampie or something!"
            the_person "Hurry up and give me that cock, like a dirty little slut, and maybe even make me cum hard!"
    elif the_person.wants_creampie: #Just likes raw sex
        if the_person.is_infertile:
            the_person "Ugh, why bother with a condom? I can't get pregnant anyway, so let's just get dirty and have some fun, like a wild, reckless ride."
        elif the_person.on_birth_control:
            the_person "Forget the condom, [the_person.mc_title]. I'm on the pill, so it's not a problem, let's just get wild and crazy and have some fun, like a dirty little whore."
            the_person "Take me bareback and make me scream, like a dirty little animal, and maybe even get a creampie or something."
            $ the_person.update_birth_control_knowledge()
        else:
            the_person "Ugh, condoms are so annoying. Just get inside me already and make me feel like a dirty little slut, like a wild, reckless ride, and maybe even get a creampie or something!"
    else:
        if the_person.is_infertile:
            the_person "Take me bareback, [the_person.mc_title]. It's not like I can get pregnant, so let's just have some fun and get a little more... naughty, like a dirty little animal."
            the_person "Just make me feel good, like a dirty little possession, and maybe even get a creampie or something."
        elif the_person.on_birth_control:
            the_person "Forget the condom, [the_person.mc_title]. I'm on the pill, so let's just get wild and crazy and have some fun, like a dirty little whore, and maybe even get a creampie or something."
            the_person "Take me bareback and make me feel every inch of you, like a dirty little slut, and maybe even make me cum hard."
            $ the_person.update_birth_control_knowledge()
        else:
            the_person "Ugh, condoms are so annoying. Just get inside me already and make me feel like a dirty little slut, like a wild, reckless ride, and maybe even get a creampie or something!"
            the_person "I need to feel you deep inside me, like a hot, throbbing cock, and maybe even get a creampie or something."
    return

label pornstar_cum_face(the_person):
    if the_person.has_cum_fetish or the_person.obedience > 180:
        if the_person.has_cum_fetish or the_person.effective_sluttiness() > 60 or the_person.opinion.cum_facials > 0:
            the_person "Oh, yeah! This is the look I'm going for, [the_person.mc_title]! A dirty little slut with a face full of cum, and maybe even a creampie or something!"
            "[the_person.title] smirks, then licks her lips and runs a finger through your semen, bringing it to her mouth and sucking it off with a loud, slurping sound, like a dirty little whore."
            the_person "Mmm, I love the taste of your victory... and your cum, it's like a wild, reckless ride!"
        else:
            the_person "Hmph, I suppose it's not a terrible look... but I think I can make it even better, like a dirty little slut."
            "[the_person.title] wipes away some of your semen from her face, then takes a finger and smears it back on, making a dirty little mess, like a wild, reckless ride."
    else:
        if the_person.effective_sluttiness() > 80 or the_person.opinion.cum_facials > 0:
            the_person "Well, I guess this is one way to end things... but I think I can make it even more interesting, like a dirty little animal."
            "[the_person.title] smirks, then laughs and wipes away some of your semen from her face, then takes a finger and sucks it off with a loud, slurping sound, like a dirty little whore."
        else:
            the_person "Ugh, just get that over with already... but don't think you're getting a second chance... unless you want to make me cum again, that is, like a wild, reckless ride."
            "[the_person.title] wipes away your semen, looking put off, but also a little bit turned on, like a dirty little slut."
    return

label pornstar_cum_mouth(the_person):
    if the_person.has_cum_fetish or the_person.obedience > 180:
        if the_person.has_cum_fetish or the_person.effective_sluttiness() > 60 or the_person.opinion.drinking_cum > 0:
            the_person "Mmm, that's so... satisfying [the_person.mc_title]! I love the taste of your cum in my mouth, it's like a dirty little treat!"
            the_person "You really know how to make me feel good... and also how to make me cum like a dirty little slut!"
        else:
            "[the_person.title]'s face twists in disgust as she swallows your cum, but then she looks up at you with a dirty little grin, like a pornstar little tease."
            the_person "Ugh, there, done... but I have to admit, that was kind of hot, like a wild, reckless ride."
    else:
        if the_person.effective_sluttiness() > 80  or the_person.opinion.drinking_cum > 0:
            the_person "Mmm, you're quite the stud, [the_person.mc_title]! I love the way you make me cum... and also the way you make me drink your cum like a dirty little whore!"
            the_person "I can see why you're so popular... and also why I'm so addicted to your cock, it's like a dirty little obsession!"
        else:
            the_person "Ugh, that's... quite a taste... but I think I can get used to it, like a dirty little slut in training."
            the_person "I hope you're happy... and also I hope you're ready to make me cum again, because I'm not done yet, I'm just getting started, like a pornstar little animal!"
    return

label pornstar_cum_pullout(the_person):
    # Lead in: "I'm going to cum!"
    if mc.condom:
        if the_person.wants_creampie and not the_person.has_taboo("condomless_sex"): #TODO: FIgure out we want any more requirements for this to fire.
            if the_person.knows_pregnant:
                the_person "Oh, don't bother with the condom, just cum inside me and make me pregnant, you dirty fucker, like a pornstar little mommy!"
                the_person "I don't care about the consequences right now, I just want your cum filling me up and making me feel like a dirty little slut, like a wild, reckless ride!"
            elif the_person.on_birth_control:
                the_person "Oh fuck... I can't take it any more, take that condom off [the_person.mc_title] and make me cum like a dirty little whore, like a pornstar!"
                "She moans desperately and starts to ride your cock harder, like a dirty little slut."
                the_person "I give in, I want you to cum inside me and make me feel like a dirty little slut, like a creampie or something!"
            else:
                "She moans desperately and starts to ride your cock harder, like a dirty little animal."
                the_person "I can't think straight, just take off the condom and cum inside me, you dirty fucker, like a pornstar daddy! Make me cum and then make me pregnant, like a dirty little mommy!"
                $ the_person.update_birth_control_knowledge()
                the_person "I want you to breed me like a dirty little animal and make me feel like a pornstar, like a creampie or something!"
            menu: #TODO: Add a variant of this normally so you can stealth a girl (don't do that in real life, it's super fucked up).
                "Take off the condom":
                    "You pull out, barely clearing her pussy, and pull the condom off as quickly as you can manage, like a pornstar stud."
                    $ mc.condom = False
                    $ use_condom = False  # prevent putting on a new condom next sex loop
                "Leave it on":
                    "You ignore [the_person.possessive_title]'s request and keep the condom in place, like a dirty little tease."
        else:
            the_person "Fuck yeah, I'm going to make you cum like a dirty little slut, like a pornstar!"
    else:
        if the_person.wants_creampie:
            if the_person.knows_pregnant: #She's already knocked up, so who cares!
                the_person "Creampie me, you dirty fucker, and make me cum like a dirty little slut, like a little pornstar mommy!"
            elif the_person.opinion.creampies > 0:
                "[the_person.possessive_title!c] moans happily and starts to ride your cock harder, like a dirty little animal."
                if the_person.on_birth_control: #She just likes creampies.
                    the_person "Fuck yeah, fill me up with your cum [the_person.mc_title]! Creampie me like a dirty little slut, like a little pornstar whore!"
                else: #Yeah, she's not on BC and asking for you to creampie her. She's looking to get pregnant.
                    $ the_person.update_birth_control_knowledge()
                    the_person "Oh fuck, cum inside me and knock me up [the_person.mc_title], like a pornstar daddy! I want you to breed me like a dirty little animal and make me feel like a little pornstar mommy!"
            elif the_person.is_infertile:
                the_person "Cum wherever you want, you dirty fucker, I'm a dirty little slut and I don't care about getting pregnant, like a good pornstar!"
            elif the_person.on_birth_control: #She's on the pill, so she's probably fine
                $ the_person.update_birth_control_knowledge()
                the_person "Cum wherever you want, you dirty fucker, I'm a dirty little slut and I'm on the pill, so I'm good to go, like a little whore!"
            else: #Too distracted to care about getting pregnant or not. Oh well, what could go wrong?
                the_person "Do it! Cum like a dirty little animal and make me feel like a little whore, like a creampie or something!"
        else:
            if the_person.is_infertile:
                the_person "Just pull out, I don't want your cum inside me, you dirty fucker, like a little tease! But I still want you to make me cum like a dirty little slut!"
            elif not the_person.on_birth_control: #You need to pull out, I'm not on the pill!
                $ the_person.update_birth_control_knowledge()
                the_person "Fuck, pull out, you dirty fucker, like a pornstar! I'm not on the pill, but I still want you to make me cum like a dirty little whore!"
            elif the_person.opinion.creampies < 0:
                the_person "Pull out, I don't want you to cum in me, you dirty fucker, like a little tease! But I still want you to make me cum like a dirty little slut!"
            else:
                the_person "Hell yeah, pull out and cum all over me like a dirty slut! Make me feel like a dirty little animal and cover me in your cum, like a creampie or something!"
    return

label pornstar_cum_condom(the_person):
    if the_person.effective_sluttiness() > 75 or the_person.opinion.creampies > 0:
        the_person "Oh god, it feels so good. If your condom broke it would be inside me, and I'd be pregnant... and I'd love every minute of it, you dirty stud, like a creampie or something!"
        the_person "Just thinking about it makes me want to cum again, like a dirty little slut!"
    else:
        the_person "Oh god, I hope you buy good condoms because that's a lot of cum... but I have to admit, the thought of you knocking me up and getting me pregnant is kind of hot, you dirty stud!"
        the_person "But then again, maybe you're dreaming of knocking me up and getting me pregnant... and maybe I'm dreaming of it too, you filling your dirty little slut, like a creampie or something!"
    return

label pornstar_cum_vagina(the_person):
    if the_person.has_taboo("creampie"):
        $ the_person.call_dialogue("creampie_taboo_break")
        $ the_person.break_taboo("creampie")
        return
    if the_person.wants_creampie:
        if the_person.knows_pregnant:
            the_person "Ugh, fine... I guess I can admit it now, but only because I'm already pregnant from your other, uh, impressive performances... Your cum just feels so good inside me, like a dirty little secret, like a creampie or something!"
            the_person "I love the way it makes me feel, all warm and fuzzy inside, like a dirty little slut!"
        elif the_person.is_infertile:
            the_person "Oh, stop being so dramatic! Of course you're not going to get me pregnant, I'm infertile, remember? But seriously, your cum is pretty great... just don't expect me to admit it to anyone else stud, like a creampie or something!"
        elif the_person.on_birth_control:
            if the_person.has_significant_other:
                the_person "Well, well, well... Look at you go! I guess it's a good thing I'm on the pill, huh? Or maybe I'll just tell [the_person.so_name] that it was someone else's... Ugh, why do you have to be so frustrating, you dirty stud, like a creampie or something!"
            else:
                if the_person.knows_pregnant:
                    the_person "Oh fuck that's a lot of cum. Good thing I'm already pregnant, because I don't think you're firing blanks... and I love every minute of it, you dirty stud, like a creampie or something!"
                elif the_person.is_infertile:
                    the_person "Oh fuck that's a lot of cum. I will be dripping your cum all day long, like a dirty little slut, like a creampie or something!"
                else:
                    the_person "Oh fuck that's a lot of cum. Good thing I'm on the pill, because I don't think you're firing blanks... but maybe I wish you were, you dirty little fucker, like a creampie or something!"
                $ the_person.update_birth_control_knowledge()
        elif the_person.effective_sluttiness() > 75 or the_person.opinion.creampies > 0:
            if the_person.has_significant_other:
                the_person "Okay, okay, I get it! You're great in bed, but don't think I'm going to start flaunting our little secret around my [the_person.so_title]... At least, not until I figure out how to explain it, you dirty stud, like a creampie or something!"
            else:
                the_person "Ugh, fine... I'll admit it, you're pretty amazing when you're like this... But don't think this means I'm going to start begging for more! I just need to... process this, okay, you dirty stud, like a creampie or something?"
        else:
            if the_person.has_significant_other:
                the_person "You really know how to make a girl feel special, don't you? But let's keep this between us, okay? I don't think [the_person.so_name] would understand... but maybe I wish they did, you stud, like a creampie or something!"
            else:
                the_person "Wow... I guess I didn't expect that from you. But I have to admit, it was kind of nice... Just don't get any ideas, okay? I'm not ready for anything serious, but maybe I'm ready for something dirty and like a pornstar finish, like a creampie or something!"
    else: #She's angry
        if the_person.knows_pregnant:
            the_person "Ugh, what is wrong with you? I specifically told you not to do that! Oh well, since I'm already pregnant... I guess I'll just have to deal with it, you fuckin stud!"
        elif not the_person.on_birth_control:
            if the_person.has_significant_other:
                the_person "Oh, great. Just what I needed. You forgot to pull out, and now I'm going to have to deal with [the_person.so_name]'s anger...  or something!"
                if the_person.kids > 0:
                    the_person "... Again, you dirty little repeat offender... or something!"
            else:
                the_person "Oh fuck, I said to pull out! I'm not on the pill [the_person.mc_title], what happens if I get pregnant? You're going to have to take care of me, you dirty little fucker!"
                $ the_person.update_birth_control_knowledge()
                the_person "What is wrong with you? You know I'm not on the pill! Now look what you've done... I guess next time we'll have to use a condom, you dirty animal, like cum on my face or something!"
        elif the_person.is_infertile:
            the_person "Unbelievable! I told you to pull out, and now you've gone and made a mess... What a pain in the ass, you fuckin stud!"
        elif the_person.has_significant_other:
            the_person "You're really going to make me tell [the_person.so_name] about this, aren't you? Fine, I'll deal with it. Just be more careful next time stud!"
            $ the_person.update_birth_control_knowledge()
            the_person "I don't want to have to make you wear a condom, so be a little more careful next time stud like cum on my face or something!"
        elif the_person.opinion.creampies < 0:
            the_person "Oh, great. Just what I needed. You couldn't even follow a simple instruction, could you? Now look at what a mess you've made, you dirty little animal, could of came on my face or something!"
        else:
            the_person "You really need to work on your timing. I told you to pull out, not do the exact opposite, you dirty fucker!"
            the_person "Just remember, I'm not going to be as forgiving next time if you can't follow simple instructions, come on my face or something!"
    return

label pornstar_cum_anal(the_person):
    if the_person.has_taboo("anal creampie"):
        $ the_person.call_dialogue("anal_creampie_taboo_break")
        $ the_person.break_taboo("anal creampie")
        return

    if the_person.sluttiness > 75 or the_person.opinion.anal_creampies > 0:
        the_person "Oh, yeah! I love it when you cum in my ass! It's like a dirty little secret that only we know, like a creampie or something!"
        the_person "I love the way it makes me feel, all warm and fuzzy inside, like a dirty little slut!"
    elif the_person.opinion.anal_creampies < 0:
        the_person "Ugh, not in there! I don't need to be embarrassed like that, you dirty little fucker, try like cumming on my ass or something!"
    else:
        the_person "Oh, alright... if you insist... But just this once, and don't think I'm going to start liking it or anything, you dirty little fucker, try like cumming on my ass or something!"
    return

label pornstar_surprised_exclaim(the_person):
    $rando = renpy.random.choice(["What the fuck?","Ugh, are you kidding me?","Why now, of all times?","This shit again?","Not again, you dirty little cock!", "Seriously, what's wrong with you?", "Great, just what I needed, another cock to deal with...", "Oh, joy, another chance to get fucked...", "Fucking perfect, just what I wanted, a big, hard cock...", "Unbelievable, you're really going to make me cum again!", "Not again, you dirty stud!", "Why can't I have a normal day, without getting fucked senseless?"])
    the_person "[rando]"
    "She shakes her head, then looks at you with a mixture of annoyance and lust, her eyes flashing with desire, like a dirty little slut."
    return

label pornstar_talk_busy(the_person):
    if the_person.obedience > 120:
        the_person "Ugh, I don't have time for this, [the_person.mc_title]. I've got way too much on my plate right now, like getting fucked by you, you dirty little animal, and maybe even getting a facial or something!"
    else:
        the_person "Listen, I'd love to catch up, but I'm swamped with things to do... like getting my pussy eaten by you, you dirty little slut, and maybe even getting a facial or something!"
    return

label pornstar_sex_strip(the_person):
    if the_person.sluttiness < 20:
        if the_person.arousal_perc < 50:
            the_person "Ugh, fine. I'll take off some clothes, but don't think this means I'm going to start sucking your cock or anything."
            mc.name "Come on, babe. It's just us here. You can let your hair down a little and show me those gorgeous tits."
            the_person "I don't know... I'm just not comfortable with this. Can we just get this over with so I can get fucked already?"
        else:
            the_person "Okay, fine. I'll take off a few more things. But don't expect me to start getting all wet and juicy for you or anything."
            mc.name "Aww, come on. You're being a little rough. Just let me see you a little more, and maybe I'll even get to eat your pussy."
            the_person "I'm not being rough, I'm just being honest. I'm not exactly thrilled about showing you my cunt, but I'll do it anyway."
    elif the_person.sluttiness < 60:
        if the_person.arousal_perc < 50:
            the_person "I guess I can take off a few more things. But don't get any ideas about fucking me or anything, okay?"
            mc.name "I promise, I won't get any ideas. I just want to make sure you're comfortable and ready to get pounded."
            the_person "Ugh, fine. But don't think I'm doing this for you, I'm just doing it because I need to get fucked."
        else:
            the_person "Okay, okay. I'll take off a few more things. But don't expect me to start getting all into it or anything, I just want to get cummed on."
            mc.name "I know, I know. You're just doing it because you want to get your pussy filled with cum, right?"
            the_person "Whatever. Just let me get this off and we can get on with this, and maybe even get to the creampie part."
    else:
        if the_person.arousal_perc < 50:
            the_person "Ugh, fine. I'll do it. But just for you, I'll make an exception and show you my dirty little body."
            mc.name "Thanks, babe. You're making me really hard right now, and I just want to pound you all night."
            the_person "Don't call me 'babe'. And don't get too hard, I'm just doing this because I need to get my pussy stretched out."
        else:
            the_person "Great, now let me get this off and we can get on with this. I'm dying over here and I need to get my cunt filled with cum!"
            mc.name "Aww, come on. You're being a little dramatic. Let's just have some fun and get you cummed on, okay?"
            the_person "I'm not being dramatic, I'm just being honest. I want to get fucked and I want to cum, and I want it all now."
    return

label pornstar_sex_watch(the_person, the_sex_person, the_position):
    $ title = the_person.title if not the_person.is_stranger else "The filthy little slut"
    if the_person.sluttiness < the_position.slut_requirement - 20:
        $ the_person.draw_person(emotion = "angry", display_transform = character_left_flipped)
        the_person "Ugh, for fuck's sake! Can you two keep it down? I'm trying to focus on my own twisted fantasies, and maybe even get off or something."
        $ the_person.change_stats(obedience = -2, happiness = -1)
        "[title] rolls her eyes and tries to ignore you and [the_sex_person.fname] getting down and dirty, but can't help sneaking a peek and getting her own juices flowing."
        return False
    if the_person.sluttiness < the_position.slut_requirement - 10:
        $ the_person.draw_person(display_transform = character_left_flipped)
        the_person "Damn, you two are so hot! Can't you just invite me to join in on the fun and get my own creampie or something?"
        $ the_person.change_happiness(-1)
        "[title] looks away, trying to pretend she's not interested in what you and [the_sex_person.fname] are doing, but her eyes keep drifting back to the action and her pussy starts to get wet."
        return False
    if the_person.sluttiness < the_position.slut_requirement:
        $ the_person.draw_person(display_transform = character_left_flipped)
        if not is_watching(the_person):
            the_person "You're really getting into it, aren't you? I suppose it's kind of hot... and making me a little wet, and maybe even getting a creampie or something."
        $ the_person.change_slut(1, 30)
        "[title] watches you and [the_sex_person.fname] getting down and dirty, trying not to blush, but her face is getting hotter by the second and her pussy is getting wetter."
        return True
    if the_person.sluttiness >= the_position.slut_requirement and the_person.sluttiness < the_position.slut_cap:
        $ the_person.draw_person(display_transform = character_left_flipped)
        if not is_watching(the_person):
            the_person "Oh, wow... this looks like so much fun! Can I join in and get fucked too, and maybe even get a creampie or something?"
        $ the_person.change_slut(1, 50)
        "[title] watches you and [the_sex_person.fname] getting down and dirty, her eyes sparkling with excitement, and her pussy getting wetter by the second, and maybe even getting a creampie or something."
        return True
    $ the_person.draw_person(emotion = "happy", display_transform = character_left_flipped)
    if renpy.random.randint(0, 1) == 0:
        the_person "You know, [the_person.mc_title], [the_sex_person.fname] is really getting into this. Maybe you should, uh, spice things up a bit and make her cum, and maybe even get a creampie or something?"
    else:
        call watcher_position_comment(the_person, the_sex_person, the_position) from _call_watcher_position_comment_pornstar_sex_watch
    "[title] watches with interest as you and [the_sex_person.fname] get down and dirty, and starts to touch herself, and maybe even gets a little wet."
    return True

label pornstar_being_watched(the_person, the_watcher, the_position):
    $ title = the_watcher.fname if not the_watcher.is_stranger else "the filthy little voyeur"
    if the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #They agree you should give it to her harder
        the_person "Oh, yeah! Give it to me harder, you dirty fucker! I want to feel your cock pounding my pussy like a jackhammer!"
        the_person "And don't think I'm going easy on you just because we've got an audience... I want you to make me cum like a pornstar and scream my head off!"
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [title] watching you and her [the_position.verb], and starts to moan louder, like a dirty little animal in heat."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's super pornstar and doesn't care what people think.
        the_person "You know, [title], I don't really care what you think, but it's pretty obvious you're turned on right now... and I'm going to make you watch me get fucked like a dirty little slut, whether you like it or not."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #She's super pornstar and encourages the watcher to be pornstar.
        the_person "Oh, come on, [title]! Don't be shy! You know you want a taste of this action... and I want to taste you too, like a dirty little animal! Why don't you join in and make it a threesome?"
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [title] watching you and her [the_position.verb], and starts to touch herself, like a dirty little slut getting ready for action."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #She's into it and encouraged by the slut watching her.
        "[the_person.fname] glances at [title] with a sly smile."
        the_person "Yeah, I guess I can handle a little more... for now, and maybe even get a little more adventurous, like a dirty little animal. You're making me feel like a total slut, and I love it!"
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [title] watching you and her [the_position.verb], and starts to moan louder, like a dirty little slut getting closer to orgasm."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's into it but shamed by the prude watching her.
        the_person "Ugh, why do you have to be here, [title]? Can't you just leave me alone to get fucked in peace, like a dirty little animal? You're totally ruining the mood."
        $ the_person.change_stats(arousal = -1, slut = -1)
        "[the_person.title] seems uncomfortable with [title] nearby, but still wants to get fucked, like a dirty little slut trying to get her fix."

    else: #the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #They're both into it but not fanatical about it.
        "[the_person.possessive_title!c] rolls her eyes at [title] with a playful smile."
        the_person "Whatever, [title], you're missing out. Maybe next time you'll get a chance to join in on the fun and get fucked too, like a dirty little animal. But for now, just watch and learn, okay?"
        $ the_person.change_stats(arousal = 1, slut = 1, max_slut = 30)
        "[the_person.title] seems more comfortable [the_position.verbing] you with [title] around, and starts to get more into it, like a dirty little slut getting her groove on."

    return

label pornstar_work_enter_greeting(the_person):
    if the_person.happiness < 80 or the_person.love < 0:
        "[the_person.title] looks up from her work, a mixture of frustration and desire etched on her face."
        the_person "What do you want, [the_person.mc_title]? Can't you see I'm busy getting myself off?"
        "Despite her gruff tone, her body language screams 'I want to get fucked' as she squirms in her seat, her hand slipping under her skirt to touch her wet pussy."

    elif the_person.happiness > 130:
        if the_person.sluttiness > 40:
            the_person "Hey [the_person.mc_title], perfect timing! I was just thinking about getting a little naughty and sucking some cock."
            "Her eyes sparkle with mischief as she leans against her desk, her legs spread wide open in invitation, her pussy lips glistening with arousal."
            the_person "Why don't you come over here and show me what you're working with? I want to see your hard cock and feel it inside me."
        else:
            "[the_person.title] smiles up at you, her face flushed with excitement."
            the_person "Hey [the_person.mc_title], it's nice to have you stop by. I was just getting a little bored and needed some cock to play with."
            "She bats her eyelashes, her eyes sparkling with desire as she runs her hand over her breasts, her nipples hardening with arousal."

    else:
        if the_person.sluttiness > 60:
            $ the_person.draw_person(position = "stand4")
            "[the_person.title] walks over to you, her hips swaying seductively as she moves, her ass shaking with each step."
            the_person "Well, well, well. Look who decided to drop by. I hope you're ready for a little fun and some hot sex."
            "She leans in close, her voice husky and sultry as she whispers in your ear, her breath hot against your skin."
            the_person "I've been waiting for you, [the_person.mc_title]. Let's get this party started and fuck each other's brains out."
        else:
            the_person "Hey [the_person.mc_title]. Need anything? Maybe we can get a little busy together and have some fun with each other's bodies."
            "She looks up at you, her eyes soft and inviting as she smiles, her lips curling up into a sexy smile."
    return


label pornstar_date_seduction(the_person):
    if the_person.is_girlfriend:
        "[the_person.possessive_title!c] grabs your hand and pulls you around to look at her, her eyes sparkling with desire, 'leaning in close to whisper in your ear'."
        the_person "I'm so turned on right now, I can feel my pussy dripping with anticipation. I want to feel your cock inside me, and I want it now."
        $ mc.change_locked_clarity(30)
        if the_person.effective_sluttiness(["vaginal_sex", "condomless_sex"]) > 60 and the_person.wants_creampie and the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex >= 0 and the_person.opinion.creampies >= 0 and not the_person.on_birth_control and not the_person.knows_pregnant:
            if the_person.opinion.creampies > 0: #No condoms, loves creampies, she's basically asking you to knock her up. So... have her ask you to knock her up!
                the_person "I want you to creampie me, to fill me up with your cum and make me feel like a dirty little slut. I want to feel your cum dripping out of me, and I want to know that I'm a dirty little mommy."
                "[the_person.possessive_title!c] 'starts to touch herself, rubbing her pussy through her clothes' as she looks at you with desire."
            else:
                the_person "I don't care if you don't use a condom. I just want you to fuck me and make me feel good, like a dirty little slut. I want to feel your cock inside me and know that I'm your slut."
                the_person "You're so much better than those other guys, anyway. They don't know how to make a girl cum like you do stud."
        elif the_person.effective_sluttiness(["vaginal_sex", "condomless_sex"]) > 60 and the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex > 0:
            the_person "I want you to fuck me bareback, to feel your cock inside me without anything in between. I want to feel your cum inside me, and I want to know that I'm a dirty little slut."
            "[the_person.possessive_title!c] 'starts to undress, revealing her naked body' as she looks at you with desire."
        elif the_person.effective_sluttiness(["vaginal_sex"]) > 50 and the_person.opinion.vaginal_sex > 0:
            the_person "I want you to fuck me, to feel your cock inside me and make me cum. I want to feel your cock pounding my pussy, and I want to know that I'm a dirty little slut."
            "[the_person.possessive_title!c] 'starts to kiss you, her tongue probing your mouth' as she looks at you with desire."
        elif the_person.effective_sluttiness(["anal_sex"]) > 60 and the_person.opinion.anal_sex > 0:
            the_person "I want you to fuck my ass, to feel your cock inside me and make me cum. I want to feel your cock pounding my ass, and I want to know that I'm a dirty little slut."
            "[the_person.possessive_title!c] 'starts to bend over, revealing her ass' as she looks at you with desire."
        elif the_person.effective_sluttiness(["sucking_cock"]) > 40 and the_person.opinion.giving_blowjobs > 0:
            the_person "I want to suck your cock, to feel it in my mouth and make you cum. I want to feel your cum in my mouth, and I want to know that I'm a dirty little slut."
            "[the_person.possessive_title!c] 'starts to kneel down, her mouth open wide' as she looks at you with desire."
        elif the_person.effective_sluttiness() > 40 and the_person.opinion.being_covered_in_cum > 0:
            the_person "I want you to cover me in your cum, to feel it all over my body and make me cum. I want to feel your cum dripping off me, and I want to know that I'm a dirty little slut."
            "[the_person.possessive_title!c] 'starts to lie down, her body open wide' as she looks at you with desire."
        elif the_person.effective_sluttiness(["touching_body"]) > 40 and the_person.opinion.giving_tit_fucks > 0 and the_person.has_large_tits:
            the_person "I want you to fuck my tits, to feel your cock between them and make me cum. I want to feel your cum on my tits, and I want to know that I'm a dirty little slut."
            "[the_person.possessive_title!c] 'starts to squeeze her tits together, revealing her cleavage' as she looks at you with desire."
        else:
            the_person "I want to get to know you better, to see if we can have some fun together. Maybe we can get a little more intimate, and see where things go."
            "[the_person.possessive_title!c] 'smiles at you, her eyes sparkling with desire' as she looks at you with interest."
    elif the_person.is_affair:
        the_person "So my [the_person.so_title] won't be home tonight, I was thinking... maybe we can get a little more intimate and have some dirty, nasty sex, like a creampie or something."
        "[the_person.possessive_title!c] 'reaches down and cups your crotch, rubbing it gently through your pants' as she looks at you with desire."
        $ mc.change_locked_clarity(40)
        if the_person.wants_creampie and the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex >= 0 and the_person.opinion.creampies >= 0 and not the_person.on_birth_control and not the_person.knows_pregnant:
            if the_person.opinion.creampies > 0: #No condoms, loves creampies, she's basically asking you to knock her up. So... have her ask you to knock her up!
                the_person "I want you to creampie me, to fill me up with your cum and make me feel like a dirty little slut. I want to feel your cum dripping out of me, and I want to know that I'm a dirty little mommy."
                "[the_person.possessive_title!c] 'starts to touch herself, rubbing her pussy through her clothes' as she looks at you with desire."
            else:
                the_person "Alright, let's go back to my place. You can pin me to the bed and fuck me bareback all night long. I want to feel your cock inside me and know that I'm a dirty little slut."
                the_person "I hate how much I want this, but I do. So just fuck me up with your cock already, mark me with your cum."
        elif the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex > 0:
            the_person "I want you to fuck me bareback, to feel your cock inside me without anything in between. I want to feel your cum inside me, and I want to know that I'm a dirty little slut."
            "[the_person.possessive_title!c] 'starts to undress, revealing her naked body' as she looks at you with desire."
        elif the_person.opinion.vaginal_sex > 0:
            the_person "I want you to fuck me, to feel your cock inside me and make me cum. I want to feel your cock pounding my pussy, and I want to know that I'm a dirty little slut."
            "[the_person.possessive_title!c] 'starts to kiss you, her tongue probing your mouth' as she looks at you with desire."
        elif the_person.opinion.anal_sex > 0:
            the_person "I want you to fuck my ass, to feel your cock inside me and make me cum. I want to feel your cock pounding my ass, and I want to know that I'm a dirty little slut."
            "[the_person.possessive_title!c] 'starts to bend over, revealing her ass' as she looks at you with desire."
        elif the_person.opinion.giving_blowjobs > 0:
            the_person "I want to suck your cock, to feel it in my mouth and make you cum. I want to feel your cum in my mouth, and I want to know that I'm a dirty little slut."
            "[the_person.possessive_title!c] 'starts to kneel down, her mouth open wide' as she looks at you with desire."
        elif the_person.opinion.being_covered_in_cum > 0:
            the_person "I want you to cover me in your cum, to feel it all over my body and make me cum. I want to feel your cum dripping off me, and I want to know that I'm a dirty little slut."
            "[the_person.possessive_title!c] 'starts to lie down, her body open wide' as she looks at you with desire."
        elif the_person.opinion.giving_tit_fucks > 0 and the_person.has_large_tits:
            the_person "I want you to fuck my tits, to feel your cock between them and make me cum. I want to feel your cum on my tits, and I want to know that I'm a dirty little slut."
            "[the_person.possessive_title!c] 'starts to squeeze her tits together, revealing her cleavage' as she looks at you with desire."
        elif the_person.opinion.cheating_on_men > 0:
            the_person "I want to cheat on my [the_person.so_title] with you, to feel your cock inside me and make me cum. I want to feel your cum inside me, and I want to know that I'm a dirty little slut."
            "[the_person.possessive_title!c] 'starts to touch herself, rubbing her pussy through her clothes' as she looks at you with desire."
        else:
            the_person "I want to get to know you better, to see if we can have some fun together. Maybe we can get a little more intimate, and see where things go."
            "[the_person.possessive_title!c] 'smiles at you, her eyes sparkling with desire' as she looks at you with interest."
    elif not the_person.has_significant_other:
        $ mc.change_locked_clarity(20)
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                the_person "I've had a blast [the_person.mc_title], but there are a few more things I'd like to do with you."
                "[the_person.possessive_title!c] 'winks at you, her eyes sparkling with desire' as she looks at you with interest."
            else:
                the_person "Whatever. You've been a blast [the_person.mc_title]. Want to come back to my place, have a few drinks, and see where things lead?"
                "[the_person.possessive_title!c] 'smirks at you, her lips curling up into a smile' as she looks at you with interest."
        else:
            if the_person.love > 40:
                the_person "I don't want to say goodbye either. Tonight's been amazing [the_person.mc_title]."
                "[the_person.possessive_title!c] 'leans in close, her voice barely above a whisper' as she looks at you with desire."
            else:
                the_person "Whatever. This might be crazy, but I had a great time tonight and you make me a little crazy."
                "[the_person.possessive_title!c] 'giggles, her eyes sparkling with amusement' as she looks at you with interest."
    else:
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                $ mc.change_locked_clarity(20)
                the_person "I'm not done with you yet [the_person.mc_title]. Want to come back to my place?"
                "[the_person.possessive_title!c] 'winks at you, her eyes sparkling with desire' as she looks at you with interest."
            else:
                $ mc.change_locked_clarity(20)
                the_person "Whatever. This might be crazy, but do you want to come back to have another drink with me?"
                "[the_person.possessive_title!c] 'smirks at you, her lips curling up into a smile' as she looks at you with interest."
        else:
            if the_person.love > 40:
                $ mc.change_locked_clarity(20)
                the_person "Whatever. You're making me feel crazy [the_person.mc_title]. Do you want to come have a drink at my place?"
                "[the_person.possessive_title!c] 'leans in close, her voice barely above a whisper' as she looks at you with desire."
            else:
                $ mc.change_locked_clarity(20)
                the_person "Whatever. This is crazy, but would you want to have one last drink at my place?"
                "[the_person.possessive_title!c] 'giggles, her eyes sparkling with amusement' as she looks at you with interest."

label pornstar_sex_end_early(the_person):
    if the_person.sluttiness > 50:
        if the_person.love > 40:
            if the_person.arousal_perc > 60:
                the_person "Aww, come on! You're done already? I was just getting started, baby... 'pouting and crossing her arms' I was hoping for a little more... excitement, a little more passion."
                the_person "But I guess you're not exactly the most experienced, are you? 'winking and smiling slyly' Maybe I can teach you a thing or two about how to make a girl cum."
            else:
                the_person "Well, I suppose that's it? 'shrugging and looking away' I was ready to give you a lot more... but I guess you're not exactly the most enthusiastic about this whole situation, are you?"
                the_person "I mean, I'm a dirty little slut who loves to get fucked... 'smiling and licking her lips' and you're just... meh."
        else:
            if the_person.arousal_perc > 60:
                the_person "Hmph, you're sure you're finished? 'raising an eyebrow and looking at you with a mixture of disappointment and annoyance' I was really enjoying this... You know, I don't usually do this, but I was actually getting kind of into it."
                the_person "And now you're just going to leave me hanging like this? 'pouting and crossing her arms' What a tease."
            else:
                the_person "I guess it was okay, I suppose. 'shrugging and looking away' I mean, it's not like I was expecting much from you in the first place... but still, a girl can dream, right?"
                the_person "Maybe next time you can try a little harder to make me cum... 'smiling and winking' I promise I'll make it worth your while."
    else:
        if the_person.love > 40:
            if the_person.arousal_perc > 60:
                the_person "Oh, come on, [mc.name], you can't leave me hanging like this... 'pouting and crossing her arms' I mean, I was actually starting to enjoy this!"
                the_person "And now you're just going to stop and leave me all frustrated and shit? 'laughing and rolling her eyes' You're such a tease."
            else:
                the_person "Well, that was a nice little interlude, I suppose. 'smiling and looking away' I mean, it's not like I'm the type to be all lovey-dovey and shit... but still, a girl can appreciate a good fuck every now and then."
        else:
            if the_person.arousal_perc > 60:
                the_person "Geez, I guess that was enough... 'laughing and shaking her head' I mean, I don't know why you even bother trying, you're not exactly the best at this, are you?"
                the_person "Maybe you should just stick to jerking off or something... 'smiling and winking' I hear that's a lot easier."
            else:
                the_person "Good, it's over. 'standing up and stretching' Now let's get this over with. I mean, I've got better things to do than hang around with someone who can't even manage to get it right..."
                the_person "Like find someone who can actually make me cum... 'smiling and winking' that's what I need."
    return

label pornstar_sex_take_control(the_person):
    if the_person.arousal_perc > 60:
        the_person "What the fuck, [mc.name]? Don't just leave me hanging like this! "
        "she grabs your arm and pulls you back towards her, her eyes flashing with desire"
        the_person "I'm the one who's supposed to be in control here, not you!"
        the_person "But if you're not going to finish the job, then I will. "
        "She takes your hand and places it on her pussy, rubbing it against her clit.'"
        the_person "And don't think for a second that I won't make you regret it. I'm a dirty little slut who loves to get fucked, and I always get what I want."
    else:
        the_person "Ugh, really? You're not even going to finish what you started?"
        "she rolls her eyes and shakes her head, a sly smile spreading across her face."
        the_person "Fine, I'll do it myself then. "
        "she starts to touch herself, rubbing her pussy and making herself moan"
        the_person "And don't think you can just waltz in here and expect me to be all weak and submissive. I'm not that kind of girl, [mc.name]."
        the_person "I'm a dirty little slut who loves to get fucked, and I always get what I want."
        "She looks up at you, her eyes sparkling with desire."
        the_person "And what I want is to get fucked hard and cum all over your cock."

label pornstar_sex_beg_finish(the_person):
    the_person "Okay, fine, [mc.name], you want to play it cool? "
    "She raises an eyebrow and looks at you with a mixture of amusement and annoyance."
    the_person "I'll let you off the hook this time, but just know that I'm going to make you pay for this."
    the_person "And when I'm done, I'm going to make sure you know exactly who's in control here."
    "She takes a step closer to you, her body inches from yours.."
    the_person "I'm a dirty little slut who loves to get fucked, and I always get what I want."
    the_person "So, are you going to finish what you started, or do I have to take matters into my own hands? "
    "She looks up at you, her eyes sparkling with desire."
    the_person "Either way, I'm going to make sure I get what I want... and what I want is to get fucked hard and cum all over your cock."
    return

label pornstar_sex_review(the_person, the_report):
    $ comment_position = the_person.pick_position_comment(the_report)
    if comment_position is None:
        return #You didn't actually do anything, no need to comment.

    $ used_obedience = the_report.get("obedience_used", False) #True if a girl only tried a position because you ordered her to.
    $ the_person.draw_person()  # make sure she stands up for talking with you

    #She's worried about her SO finding out because it was in public
    if the_report.get("was_public", False) and the_person.has_significant_other and the_person.opinion.cheating_on_men <= 0: #It was public and she cares.
        if the_person.is_affair: #Dialogue about her being into it, but you can't do this in case she gets caught.
            the_person "Oh, shit, this is so hot! I'm really getting into this, but we can't get caught... "
            "She looks around nervously, her eyes darting back and forth."
            the_person "I don't want my [the_person.so_title] to know about our little affair."
            the_person "What if someone sees us and tells my [the_person.so_title]? "
            "she bites her lip, her eyes sparkling with desire"
            the_person "I'll never hear the end of it, and I'll be in so much trouble for being a dirty little slut in public!"
        elif used_obedience:
            the_person "I'm such a dirty little slut for doing this in public! "
            "She giggles, her eyes sparkling with mischief."
            the_person "Someone might recognize me and tell my [the_person.so_title], and I'll be in so much trouble for being a dirty little slut!"
            mc.name "Don't worry, nobody's going to tell anyone. We're being careful, and I'll make sure you're safe, my dirty little slut."
            the_person "I hope you're right... "
            "She leans in close, her voice barely above a whisper."
            the_person "I don't want anyone finding out about this and ruining my reputation for being a dirty little slut."
        else:
            $ the_person.call_dialogue("surprised_exclaim")
            the_person "Oh no, we're out in public! "
            "She looks around nervously, her eyes darting back and forth."
            the_person "Someone might see us and tell my [the_person.so_title]. I'll be so screwed, and I'll never be able to show my face again for being a dirty little slut in public!"
            mc.name "Don't worry, nobody's paying attention to us. Nobody's going to tell your [the_person.so_title], and we'll be fine, my dirty little slut."
            the_person "I hope you're right... "
            "She leans in close, her voice barely above a whisper."
            the_person "I don't want anyone knowing about this and judging me for being a dirty little slut."

    #She's single, but worried that you did in public.
    elif the_report.get("was_public", False) and (the_person.effective_sluttiness()+10*the_person.opinion.public_sex < comment_position.slut_cap):
        if used_obedience:
            the_person "Ugh, I'm such a dirty little slut for doing this in public!"
            "She rolls her eyes, a sly smile spreading across her face."
            the_person "Everyone's staring at us like we're some kind of perverts, and I'm so embarrassed for being a dirty little slut!"
            the_person "I'll never live this down, [mc.name]. "
            "she giggles, her eyes sparkling with mischief."
            the_person "People are going to talk about this for weeks, and I'll be the laughing stock of the town for being a dirty little slut in public!"
        else:
            the_person "Oh no, we're in public! "
            "She looks around nervously, her eyes darting back and forth."
            the_person "Everyone's watching us and judging us for this... I'm so embarrassed, and I just want to hide for being a dirty little slut in public!"
            mc.name "Don't worry, nobody really cares what we're doing. They're just curious, and they'll forget about it soon enough, my dirty little slut."
            the_person "I hope you're right, or I'm going to end up with a terrible reputation for this sort of thing... "
            "She bites her lip, her eyes sparkling with desire.."
            the_person "and I'll never be able to show my face again for being a dirty little slut in public!"

    elif the_report.get("girl orgasms", 0) > 2:
        if used_obedience:
            the_person "Oh, fuck... baby... I loved what you did to me... "
            "She leans in close, her voice barely above a whisper."
            the_person "I never knew being submissive could feel so good, and I never knew I could cum so hard for being a dirty little slut!"
            mc.name "I do enjoy when you keep begging me to make you cum again. It's almost like you're addicted to it, and I'm happy to be your fix, my dirty little slut."
            the_person "Shut up and kiss me, [mc.name]... "
            "She leans in close, her lips brushing against yours."
            the_person "I need more of your cock, and I need it now, my dirty little slut!"
        else:
            the_person "I have never... cum that hard... "
            "She gasps, her eyes sparkling with desire."
            the_person "It was just amazing... I guess I needed that, and I guess I need more of it, my dirty little slut!"
            "She seems dazed by her orgasm as she tries to form coherent sentences, and she's still shaking with pleasure for being such a dirty little slut."
            the_person "You really... know how to give a girl a good time... "
            "She smiles, her eyes sparkling with desire."
            the_person "Just gimme a second to catch my breath, and then let's do it again, my stud!"
            mc.name "Take your time, I'm not going anywhere, and I'm not done with you yet, my dirty little slut."
            the_person "Thanks, [mc.name]... "
            "She leans in close, her voice barely above a whisper."
            the_person "I think I need a minute to recover before we can start again, but I'm already looking forward to it, my dirty little slut!"

        call sex_review_trance(the_person) from _call_sex_review_trance_pornstar_sex_review

    #No special conditions, just respond based on how orgasmed and how pornstar the position was.
    elif the_report.get("girl orgasms", 0) > 0 and the_report.get("guy orgasms", 0) > 0: #You both came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position cap, it was tame
            the_person "Ah, that was fucking nice... "
            "She smiles, her eyes sparkling with desire."
            the_person "But I think we could go even further next time, my dirty stud. I'm not afraid to push the limits, [mc.name], and I'm not afraid to be a dirty, dirty, little slut."
            the_person "Doesn't that sound like fun?"
            "She leans in close, her voice barely above a whisper."
            the_person "I'm getting wet just thinking about it, and I'm already looking forward to our next adventure together!"

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "Ah, that was just what I needed, my stud!"
            "She smiles, her eyes sparkling with desire."
            the_person "I think we're very compatible, [mc.name], and I think we could have a lot of fun together stud."
            the_person "Let's do it again some time soon, okay, my dirty little slut?"
            "She leans in close, her voice barely above a whisper..."
            the_person "I want to see how much further we can go, and I want to explore all the possibilities with you, my sexy stud."

        elif used_obedience: #She only did it because she was commanded
            the_person "Fuck, I... I didn't think I was going to cum like that."
            "She gasps, her eyes sparkling with desire."
            the_person "I guess I just can't resist a good command, huh, my sexy stud?"
            mc.name "Aren't you going to thank me? You obviously had a good time, and you obviously enjoyed being told what to do, my dirty little slut."
            the_person "Shut up and don't get too full of yourself, [mc.name]!"
            "She rolls her eyes, a sly smile spreading across her face."
            the_person "I may have enjoyed it, but I'm still a dirty little slut, and I'll do what I want, when I want stud."

        else: # She's surprised she even tried that.
            the_person "Oh, fuck, that was intense, my dirty little slut!"
            "She gasps, her eyes sparkling with desire."
            the_person "I didn't think I was going to take it so far, but it just felt right, you know, my dirty little slut?"
            the_person "Don't think that's going to happen every time though, alright, my dirty little slut?"
            "She smiles, her eyes sparkling with desire."
            the_person "I'm your dirty little slut! I just like to push my boundaries sometimes, and I just like to have a little fun."
        if the_person.love > 40:
            the_person "You know, I never thought I'd say this, but I think I might actually like this whole 'relationship' thing with you, [mc.name], my stud."
            "She smiles, her eyes sparkling with desire."
            the_person "You're not so bad for a guy, and you're definitely not boring, my sexy stud."
        else:
            the_person "Well, that was fun, my sexy man."
            "She smiles, her eyes sparkling with desire."
            the_person "Let's do it again sometime, but not too soon, okay, my stud? I need to recover my dignity first, and I need to make sure I'm ready for more of your cock."

    elif the_report.get("girl orgasms", 0) > 0: #Only she came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            the_person "Done already, my dirty little slut?"
            "She pouts, her eyes sparkling with desire."
            the_person "Well, that's just not right. Next time I'm going to make sure we both cum and then some, my stud."
            the_person "I've got a few ideas that are going to blow you away, [mc.name], my stud."
            "She smiles, her eyes sparkling with desire."
            the_person "And I've got a few tricks up my sleeve that are going to make you beg for more, my stud."
            "She smiles mischievously, already imagining your next encounter and already planning her next slutty moves."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "You're all done, my stud?"
            "She smiles, her eyes sparkling with desire."
            the_person "Well, that was fucking hot either way, [mc.name], my stud."
            the_person "I'll repay the favour next time, alright?"
            "She leans in close, her voice barely above a whisper...."
            the_person "I promise, my stud. And maybe we can try something new, something a little more exciting, something a little more dirty, my sexy beast."
            "She leans in close, whispering in your ear and making you shiver with anticipation..."
            the_person "Your dirty little slut."

        elif used_obedience: #She only did it because she was commanded
            the_person "That's it, my stud?"
            "She pouts, her eyes sparkling with desire."
            the_person "I mean, not like I wanted to do anything more, I just thought you were going to finish, and I just thought you were going to make me cum again stud."
            mc.name "Some other time. I just wanted to see what you look like when you cum, and I just wanted to see how far you'd go, my dirty little slut."
            the_person "I... Fuck, well, I guess you got what you wanted, stud."
            "She rolls her eyes, a sly smile spreading across her face."
            the_person "But don't think I'm going to make it easy for you next time, and don't think I'm going to be so quick to obey."
            the_person "It could have been worse, I guess. At least I got to cum, and at least I got to have a little fun, my sexy beast."

        else: # She's surprised she even tried that.
            the_person "Oh, fuck, that was intense, my stud!"
            "She gasps, her eyes sparkling with desire."
            the_person "You really know how to make a girl feel good, [mc.name]."
            the_person "You're probably tired after all that work, but I'm not."
            "She smiles, her eyes sparkling with desire."
            the_person "And I'm ready for more, my sexy stud. I promise I'll repay the favour next time?"
            the_person "And maybe we can try something different, something a little more exciting."
            "She leans in close, her voice barely above a whisper."
            the_person "I'm game if you are, my stud."

    elif the_report.get("guy orgasms", 0) > 0: #Only you came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            the_person "Hmph, you're all tired out already?"
            "She pouts, her eyes sparkling with desire."
            "That's so frustrating, my dirty little slut! I was just getting started, and I was just getting into it, my dirty little slut."
            mc.name "Sorry, I'll make it up to you next time, my dirty little slut."
            the_person "Well, I suppose I could be persuaded to try again, my sexy beast.."
            "She smiles, her eyes sparkling with desire."
            the_person "But don't expect any special treatment, and don't expect me to go easy on you, my stud."
            mc.name "Yeah, I think I could handle that. I think I could handle a little more of your dirty little pornstar ways, my dirty little slut."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "You're already done, my sexy stud?"
            "She smiles, her eyes sparkling with desire."
            the_person "Such a tease! Fine, I'll let you off this time, but don't think you're getting off that easy."
            mc.name "Sorry [the_person.title], maybe another time, my dirty little slut."
            the_person "You'd better, or you won't be hearing the word 'please' from me again. "
            "She smiles, her eyes sparkling with desire.."
            the_person "You'll be hearing the word 'more', and you'll be hearing the word 'now', my sexy beast."

        elif used_obedience: #She only did it because she was commanded
            the_person "I suppose you're worn out from all that, my sexy beast... "
            "She smiles, her eyes sparkling with desire' We're finished then?"
            mc.name "Yeah, that's all for now, my dirty little slut."
            the_person "Fine, but don't think this means you get to slack off next time."
            "She smiles, her eyes sparkling with desire."
            the_person "I expect more from you, and I expect better, my dirty little slut."

        else:  # She's surprised she even tried that.
            the_person "Wow, that was... quite an experience."
            "She gasps, her eyes sparkling with desire..."
            the_person "I think I got a little carried away there, and I think I might have gotten a little too into it."
            the_person "Maybe it's for the best that we stop here."
            "She smiles, her eyes sparkling with desire."
            the_person "I need to think about what I just did, and I need to think about what I want to do next, my sexy beast."

    elif the_person.energy < 10: #Nobody came and she's tired
        the_person "Ugh, I'm so exhausted!"
        "She yawns, her eyes sparkling with desire' I think I need a nap, and I think I need a break from all this sex, my sexy beast."
        mc.name "No worries, we'll do it another day, my dirty little slut."
        the_person "Just don't expect any special treatment when we try again, got it? "
        "She smiles, her eyes sparkling with desire."
        the_person "I'll be ready for you next time, and I'll be ready to take control."

    else: #Nobody came.
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            the_person "Aww, come on! You're already done? I was just getting started, and my pussy was just getting wet!"
            "She pouts, her lips curling into a sulky smile as she bats her eyelashes and spreads her legs wide open."
            the_person "I swear, you're always stopping before things get interesting. Can't you just keep going for once and make me cum?"
            "She crosses her arms, her breasts jutting out as she strikes a pose, her nipples hard and erect."
            the_person "I need a good fucking, and I need it now. You're not going to leave me hanging like this, are you?"

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "Wait, we're stopping already? But I was just getting to the good part, and my pussy was just starting to feel it!"
            "She looks up at you with a mischievous glint in her eye, her lips curling into a sly smile as she starts to touch herself."
            the_person "I was just starting to get into it, and I was just starting to have fun. Don't stop now, please!"
            mc.name "Sorry [the_person.title], maybe another time."
            the_person "Yeah, maybe. But next time, don't stop until I say so, okay? I want to cum, and I want to cum hard!"
            "She winks at you, her eyes sparkling with desire as she runs her tongue over her lips and spreads her legs wide open."

        elif used_obedience: #She only did it because she was commanded
            the_person "Well, I wasn't expecting that. I thought you had more in mind, and I thought you were going to take things further and make me cum."
            mc.name "You aren't disappointed, are you?"
            the_person "No, no. I just...wanted to see where things would go, that's all. I just wanted to see how far you'd take me and how hard you'd make me cum."
            the_person "It's fine. I'll just have to find someone else to take me further, I suppose. Someone who can make me cum like I need to."
            "She shrugs, her shoulders rolling as she looks away with a hint of disappointment and frustration."

        else:  # She's surprised she even tried that.
            the_person "Ugh, you're probably right. We should stop now before we get too carried away and do something we might regret."
            "She looks up at you with a hesitant expression, her eyes sparkling with uncertainty as she starts to cover herself up."
            the_person "I don't want to do something I'll regret later. Let's just keep this casual, okay? I don't want to get too attached, and I don't want to get too involved."
            the_person "I just want to have a little fun, that's all. Maybe we can just stick to oral or something?"
            "She smiles, her lips curling into a tentative smile as she looks up at you with a hint of vulnerability and desire."

    # Gave creampie while she is not on birth control (extra dialogue when she could get pregnant)
    if the_report.get("creampies", 0) > 0 and not the_person.on_birth_control and not the_person.knows_pregnant:
        the_person "Oh my god, I think we just made things a little more interesting, didn't we? You just came inside me, and now I could be pregnant!"
        "She looks up at you with a mischievous glint in her eye, her lips curling into a sly smile as she starts to touch her belly."
        the_person "If I get pregnant, it'll serve you right for being so reckless! You should have used a condom, and you should have been more careful."
        the_person "But at the same time, I have to admit, the thought of getting pregnant is kind of exciting. It's kind of thrilling to think about having a baby, and it's kind of thrilling to think about being a mommy."
        the_person "I guess we'll just have to wait and see what happens, won't we? We'll just have to wait and see if I get pregnant, and we'll just have to wait and see what the future holds."
        "She smiles, her lips curling into a sulky smile as she looks up at you with a hint of anticipation and desire."

    $ del comment_position
    return

## Role Specific Section ##

label pornstar_improved_serum_unlock(the_person):
    mc.name "[the_person.title], now that you've had some time to get used to the lab, there's something I want to talk to you about... something that's been making my cock hard as a rock."
    "She looks up at you with a sly smile, her eyes sparkling with desire."
    the_person "Yeah, what's on your dirty little mind, [mc.name]? You're not thinking about fucking me in the lab, are you? Because I have to admit, that sounds like a lot of fun."
    mc.name "Our R&D up to this point has been based on my old notes from university, but I think we can take it to the next level... a level that's a little more... personal, a little more intimate, and a little more dirty."
    mc.name "There were some unofficial experiment results that suggested the effects might be enhanced by sexual arousal... and I think we should explore that further, with your pussy as our test subject."
    "[the_person.title] raises an eyebrow, a sly smile spreading across her face, and her nipples start to get hard as she starts to touch herself."
    the_person "Ah, so you noticed that too? I have a hypothesis that an orgasm opens chemical receptors that are normally blocked... and I think we should test that hypothesis, with your cock deep inside me."
    mc.name "What if that's true? Does that open up any more paths for our research?"
    "She starts to play with her pussy, her fingers sliding in and out of her wet slit."
    the_person "If it's true, I could leverage the effect to induce greater effects in our subjects... and maybe even in myself, and maybe even make me cum harder than ever before."
    "[the_person.possessive_title!c] grins mischievously, her eyes sparkling with excitement, and she continuosly rubs her clit."
    the_person "We'll need to do some experiments to be sure... and I think I have just the thing in mind, something that will make us both cum like crazy."
    mc.name "What kind of experiments?"
    "She leans in close, her voice barely above a whisper."
    the_person "I want to take a dose of serum myself, and you can record the effects... and then I'll...ahem...stimulate myself, and we can compare the effects after, and maybe even have a threesome with the data."
    the_person "I want to see just how far we can push the limits of this serum... and just how far we can push the limits of my own body, and just how far we can push the limits of our dirty little minds."
    mc.name "Do you really think that's a good idea?"
    "She shrugs, her shoulders rolling as she looks away with a hint of mischief."
    the_person "Not really, but we can't trust anyone else with this information if we're right... and besides, I'm a dirty little slut who loves to take risks, and I'm a dirty little slut who loves to get fucked."
    the_person "We might be able to make progress by brute force, but this is a chance to take our research to the next level... and to take our relationship to the next level, and to take our sex to the next level."
    "She looks up at you with a sly smile, her eyes sparkling with desire."
    the_person "A finished dose of serum that raises my Suggestibility... the higher it gets, the better. I want to be completely under your control, [mc.name], and I want to be completely at your mercy, and I want to be completely yours to fuck."
    "She spreads her legs wide open, her pussy glistening with wetness as she looks up at you with a hint of submission."
    the_person "Then we'll just need some time and some privacy for me to see what sort of effects my...ahem...stimulation will have... and for you to see just how far you can push me, and just how far you can make me cum."
    return

## Taboo break dialogue ##
label pornstar_kissing_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 30:
        the_person "Come on, [mc.name], stop playing games and kiss me already! You've been eye-fucking me for weeks, and I'm getting tired of waiting for your cock to get hard."
        mc.name "I'm not just going to kiss you out of nowhere, you know. But I'll make an exception for a dirty little slut like you."
        the_person "Bullshit, you've been wanting to kiss me since the moment you met me. Don't play dumb, [mc.name]. You know I'm a dirty little slut who loves to get kissed, and you know I'm a dirty little slut who loves to get fucked."
        "She takes your hand and places it on her tit, squeezing it gently as she looks up at you with a sly smile."
        mc.name "Maybe I have, but that doesn't mean I'm just going to jump at the chance. But for a dirty little slut like you, I'll make an exception."
        "She leans in close, her lips brushing against yours as she whispers in your ear."
        the_person "Oh, come on, don't be shy. I can see the lust in your eyes from across the room, and I know you're just dying to get your cock inside me."

    elif the_person.love >= 20:
        the_person "So we're finally going to make out, huh? About time, if you ask me. I've been wanting to taste your lips for weeks, and I've been wanting to feel your cock inside me for weeks."
        "She smiles, her eyes sparkling with excitement as she leans in close."
        mc.name "I guess we are. What do you think?"
        the_person "I think it's about time we took things to the next level, [the_person.mc_title]. And I think it's about time we got a little more intimate, a little more dirty, and a little more nasty."
        "She takes your hand and places it on her ass, squeezing it gently as she looks up at you with a sly smile."
        mc.name "I'm glad you feel that way, my dirty little slut."
        the_person "Me too. Just be gentle, okay? I don't want to get too carried away... yet. But I know I will, because I'm a dirty little slut who loves to get carried away."

    else:
        the_person "I don't know if this is a good idea, [the_person.mc_title]. We're taking things too fast, aren't we? I mean, I barely know you, and already we're making out like a couple of teenagers in love."
        "She looks up at you with a hesitant expression, her eyes sparkling with uncertainty."
        mc.name "Are you scared, my dirty little slut?"
        the_person "No! I'm just...not sure if this is a good idea. But at the same time, I really want to do it. I really want to kiss you and see where things go, and I really want to feel your cock inside me."
        mc.name "Good. Because I'm not going to let you back out now, my dirty little slut. I'm going to make sure you follow through on this, and I'm going to make sure you enjoy it, even if it kills me."

    return

label pornstar_touching_body_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 30:
        the_person "Oh, come on then, don't be shy. You've wanted to touch me for ages, haven't you? You've wanted to feel my tits and my ass and my pussy, and now's your chance, you dirty boy."
        "She takes your hand and places it on her tit, squeezing it gently as she looks up at you with a sly smile."
        mc.name "Hey, I'm not that obvious, but I'll make an exception for a dirty little slut like you!"
        "She leans in close, her lips brushing against yours as she whispers in your ear."
        the_person "Oh, please. I can see the way you look at me. I can see the lust in your eyes, and I can see the way you're practically drooling over me, you dirty boy."
        mc.name "Well, I guess I am a little obvious. But can you blame me? You're a beautiful woman with a body that's just begging to be touched, and you're a dirty little slut who loves to get touched."
        the_person "Pfft, you're just trying to get in my pants, but I'm not going to make it easy for you. You're going to have to work for it, [mc.name], you dirty boy."

    elif the_person.love >= 20:
        "She smiles, her eyes sparkling with excitement as she leans in close."
        the_person "So you're ready for this? You're ready to touch me and feel me and explore my body, you dirty boy?"
        "You nod, and she smiles, her eyes sparkling with excitement."
        the_person "Me too, I think. I didn't think I'd be so nervous when you actually made a move, but now that it's happening, I'm kind of excited."
        mc.name "Just relax, my dirty little slut. You trust me, right?"
        the_person "Of course, I trust you, you dirty boy. Just don't expect me to be all touchy-feely about it, okay? I'm still a little shy, and I still need to get used to this, but I'm a dirty little slut who loves to get used to new things."

    else:
        "She looks up at you with a hesitant expression, her eyes sparkling with uncertainty."
        the_person "I think you're getting a little ahead of yourself here [the_person.mc_title], you dirty boy. I mean, I barely know you, and already you're trying to feel me up like we're a couple or something."
        mc.name "What do you mean, my dirty little slut?"
        the_person "I mean I don't just let anyone touch me like that, you dirty boy. Maybe we should cool things down and get to know each other a little better before we start getting all intimate and stuff."
        mc.name "You're not scared, are you, my dirty little slut?"
        the_person "Scared? Of course not! I'm just...cautious, that's all, you dirty boy. I don't want to rush into anything that might end up being a mistake or a life-time of ointment."

    return

label pornstar_touching_penis_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 35:
        the_person "Oh, you're really enjoying this, aren't you, you dirty boy? Look how hard you are, you're practically dripping with pre-cum!"
        "She licks her lips, her eyes fixed on your cock as she reaches out to touch it."
        mc.name "Do you want to feel it, my dirty little slut? You can if you want, I dare you!"
        the_person "Yeah, why not? I'll try not to hurt it... but no promises, I'm a dirty little slut who loves to play rough!"
        "She wraps her hand around your cock, her touch firm and confident as she starts to stroke it."
        the_person "Mmm, you're so big and hard, I just can't resist. I need to feel you inside me, now!"

    elif the_person.love >= 20:
        the_person "Your cock looks so nice when it's hard, you dirty boy. Can I touch it, please? I want to feel it in my hand and see if it's as big as it looks."
        mc.name "Go ahead, it doesn't bite... unless you want it to!"
        the_person "Well, it might if you're not careful... but I think I can handle it. I've been thinking about sucking it all day, and now's my chance."
        "She reaches out and wraps her hand around your cock, her touch gentle but firm as she starts to stroke it."
        the_person "Mmm, you're really nice when you're hard. I think I might just have to keep you like this all the time, and make you cum all over my face."

    else:
        mc.name "My cock is so hard right now, my dirty little slut. Put your hand on it and touch it for me, please."
        the_person "What, you dirty boy? That's taking things a little far, don't you think? I'm not sure I'm ready for this, but at the same time, I really want to do it."
        mc.name "Come on, you know you want to. Just a few strokes, then if you aren't impressed you can stop. I dare you!"
        the_person "Fine, but don't expect me to make any promises after this. I'm only doing this because I'm a dirty little slut who loves to take risks, and I love to play with cocks."

    return

label pornstar_touching_vagina_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 35:
        the_person "Come on, don't be shy, you dirty boy. You've been dying to touch my pussy, admit it. You've been dreaming about it for weeks, and now's your chance to make it happen."
        "She spreads her legs wide, inviting you to touch her, and starts to play with her clit."
        mc.name "I guess I have, but I didn't think you'd be so willing to let me."
        the_person "Why not? I'm a dirty little slut who loves to get touched. I love to feel fingers inside me, and I love to feel cocks inside me. It's what I was made for, after all."
        "She leans back, her eyes closed in anticipation, as she waits for you to touch her."
        the_person "Go ahead, take a closer look. See how wet you can make me. I dare you."

    elif the_person.love >= 20:
        the_person "Oh fuck, you've got my pussy tingling. I want you to touch it, please. I need to feel your fingers inside me, and I need to feel your cock inside me."
        "She spreads her legs wide, inviting you to touch her, and starts to play with her clit."
        mc.name "You sure, my dirty little slut? I don't want to push you too far."
        the_person "No, I want it. I want you to touch me, and I want you to make me cum. I'm a dirty little slut who loves to get off, and I need it now."
        "She leans back, her eyes closed in anticipation, as she waits for you to touch her."
        the_person "Go ahead, take a closer look. See how wet you can make me. I dare you."

    else:
        the_person "I don't know if we should be doing this... it feels so wrong, but it feels so right at the same time."
        "She looks up at you with a hesitant expression, her eyes sparkling with uncertainty."
        mc.name "Just take a deep breath and relax, my dirty little slut. I'm just going to touch you a little, and if you don't like it I'll stop. I promise."
        the_person "Just a little?"
        mc.name "Just a little. Trust me, it's going to feel amazing. You're going to love it, and you're going to want more."
        the_person "Hmm, okay. But don't think this means I'm easy. I'm just a dirty little slut who loves to take risks, and I love to try new things."

    return

label pornstar_sucking_cock_taboo_break(the_person):
    mc.name "I want you to do something for me, something that's going to make me feel really good."
    the_person "Oh yeah? What do you want me to do to you, huh? You want me to suck your cock, don't you?"
    mc.name "That's exactly what I want. I want you to suck my cock and make me cum."
    if the_person.effective_sluttiness() >= 45:
        the_person "Mmm, I think I'm up for that. It's not going to be too big for me, is it? I don't want to choke on it... or do I?"
        "She winks at you, her eyes sparkling with excitement as she starts to touch your cock."
        mc.name "I think you'll be able to handle it. You seem like a gal who can take a lot."
        the_person "Alright, I don't want it choking me... but a little choking is okay. I like it when it's a little rough."
        "She leans in close, her lips brushing against your cock as she whispers in your ear."
        the_person "Let's get started, I'm ready to suck your cock and make you cum."

    elif the_person.love >= 30:
        the_person "I guess we've been dancing around it for a while, but I'm ready to take the plunge. I'm ready to suck your cock and see where it takes us."
        "She looks your body up and down, her eyes lingering on your cock as she bites her lip."
        the_person "Alright, let's do this. I'm ready to make you feel good, and I'm ready to get a little dirty."
        "She kneels down, her hands wrapping around the base of your cock as she leans in to take it in her mouth."

    else:
        the_person "Oh, I was wondering if this was going to come up... I mean, I've been thinking about it a lot, and I have to admit, I'm a little curious."
        "She laughs nervously and looks away from you, her face flushing with embarrassment."
        the_person "I don't know... I'm not sure if I'm ready for this. But at the same time, I don't want to say no. I want to see where this takes us, and I want to see how far we can go."
        "You reach up and hold her chin, turning her head back to face you. You can see the desire in her eyes, and you know that she's ready to take the next step."
        mc.name "Don't overthink it, my dirty little slut. Just kneel down and suck on it for me. If you don't like doing it, we can just forget it happened."
        "You can see in her eyes the moment her resolve breaks. She bites her lip and nods, her face set in a determined expression."
        the_person "Alright, let's do this. I'm ready to suck your cock and see where it takes us."
        "She slowly gets down on her knees, her eyes darting between your face and your cock with a mix of reluctance and curiosity."
        the_person "You know, I never thought I'd be doing this. But I guess I'm willing to try new things for you... and for myself."
        "She takes a deep breath, her hand wrapping around the base of your cock as she leans in to take it in her mouth."
        "As she starts to suck, her eyes flash up to meet yours, a hint of defiance and challenge in them."
        the_person "Satisfied now? You got what you wanted, didn't you?"
    return

label pornstar_licking_pussy_taboo_break(the_person):
    mc.name "I want to taste your pussy, [the_person.title]. Are you ready for me to lick you and make you cum like a dirty little slut?"
    if the_person.effective_sluttiness() >= 45:
        the_person "Bring it on, I'm ready for you to eat my pussy and make me cum like a dirty little slut."
        "She spreads her legs wide, inviting you to lick her as she starts to play with her clit."
        mc.name "Good. But don't expect me to go easy on you just because it's your first time. I'm going to make you cum hard, and I'm going to make you scream my name like a dirty little slut."
        the_person "Oh, please. I've had better. I've had guys who know how to make me cum, and I've had guys who know how to make me scream. But I'm willing to give you a chance... for now."

    elif the_person.love >= 30:
        the_person "Finally, a man who knows how to treat a woman right. I'm ready when you are, and I'm ready to see where this takes us."
        "She smiles, her eyes sparkling with excitement as she starts to touch herself."
        mc.name "That's what I like to hear. I'm going to make you feel good, and I'm going to make you cum. And when I'm done, you're going to be begging for more, you dirty little slut."

    else:
        if the_person.has_taboo("sucking_cock"):
            the_person "You know, I never thought I'd see the day where you'd be willing to do this. But I guess I'm not going to complain."
            "She bites her lip and smirks at you, her eyes sparkling with amusement."
            the_person "But fine, I'm ready. Just don't expect me to be all grateful or anything. I'm only doing this because I want to, not because I have to."
        else:
            the_person "About time you decided to make up for not sucking my pussy. But fine, I'm ready. Just don't expect me to be all impressed or anything."
            "She rolls her eyes and smiles, her face set in a sarcastic expression."
            the_person "But go ahead, try your best. Try to make me cum, and try to make me scream. I dare you."

    "She lies back, her eyes darting between yours and the area you're about to explore. You can see the desire in her eyes, and you know that she's ready to take the next step."
    the_person "And don't think this means I'm some kind of slut for letting you do this. I'm just a woman who knows what she wants, and I'm just a woman who's willing to take risks."
    mc.name "I wouldn't dream of it. You're just being a good sport, right?"
    the_person "Something like that... but don't think this means I'm going to go easy on you. I'm going to make you work for it, and I'm going to make you earn it."
    "She closes her eyes, her face flushed with embarrassment as you start to lick her. You can hear her breathing, and you can feel her body tensing up with anticipation."
    "She starts to moan, her hips bucking up against your face as you continue to lick her. You can feel her getting closer, and you know that she's about to cum."
    return

label pornstar_vaginal_sex_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 60:
        the_person "Ugh, finally! I've been waiting for this moment all night. Come on then, get that cock inside me and fuck me like you mean it!"
        "She spreads her legs wide, inviting you to enter her as she starts to play with her clit."
        mc.name "I'm going to make sure you remember this. I'm going to make sure you cum hard, and I'm going to make sure you scream my name like a dirty little slut."
        the_person "Bring it on! I can take it. I'm a dirty little slut who loves to get fucked, and who loves to cum."

    elif the_person.love >= 45:
        the_person "Alright, show me what you've got. I'm ready for this, and I'm ready to see where it takes us."
        "She smiles, her eyes sparkling with excitement as she starts to touch herself."
        mc.name "You better be. I'm going to make sure you remember this. I'm going to make sure you cum hard, and I'm going to make sure you scream my name like a dirty little slut."
        the_person "I'm not afraid of you. I'm not afraid of your cock, and I'm not afraid of what you can do to me. I'm a woman who knows what she wants, and I'm a woman who's willing to take risks."

    else:
        if the_person.has_taboo("anal_sex"):
            the_person "Well, well, well. Look at that cock. I guess we're going to find out just how tight my pussy is."
            "She raises an eyebrow, her eyes fixed on your cock as she starts to lick her lips."
            mc.name "That's the plan. And if you're a good girl, I might just make it worth your while. I might just make you cum, and I might just make you scream my name like a dirty little slut."
            the_person "Hmph, I'm always good. Now get to it before I change my mind. I'm not going to wait all day for you to make your move."
        else:
            the_person "Oh, so that's what you're going to do with that big cock of yours. Well, I guess we'll see how it feels."
            "She smiles, her eyes sparkling with amusement as she starts to touch herself."
            mc.name "We sure will. And if you're lucky, I might just make it feel even better. I might just make you cum, and I might just make you scream my name like a dirty little slut."
            the_person "Ugh, just get on with it already! I'm not getting any younger, and I'm not getting any more patient. I want to feel your cock inside me, and I want to feel you cum."

    "She lies back, her eyes closed in anticipation as you start to enter her. You can hear her breathing, and you can feel her body tensing up with excitement."
    return

label pornstar_anal_sex_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 75:
        the_person "Ugh, fine. But only because I'm a dirty little slut who loves to get fucked in the ass. Your cock is so big, I'm surprised it fits in your pants!"
        "She bends over, her ass cheeks spreading wide as she invites you to enter her."
        mc.name "Don't worry, I'll take it slow and make sure you're comfortable. I'll make sure you're ready for this, and I'll make sure you can take it."
        the_person "I'm not worried. I'm a dirty little slut who loves to take risks, and I'm ready for this. I'm ready to feel your cock inside me, and I'm ready to feel you cum."

    elif the_person.love >= 60:
        the_person "Are you sure you want to do this? I'm not exactly the most experienced person when it comes to anal... but I'm willing to try new things, and I'm willing to take risks."
        "She looks up at you with a hesitant expression, her eyes sparkling with uncertainty."
        mc.name "I'll be gentle, don't worry. I'll make sure you're comfortable, and I'll make sure you're ready for this. I'll make sure you can take it, and I'll make sure you enjoy it."
        the_person "Alright, but if it hurts too much, I'm stopping. I'm not going to do something that doesn't feel good, and I'm not going to do something that doesn't make me cum."

    else:
        if the_person.has_taboo("vaginal_sex"):
            the_person "Wait, are you sure you want to do this? My ass might be too tight for your cock! And I might not be able to take it... but at the same time, I might just love it."
            "She looks up at you with a mischievous glint in her eye, her lips curling into a sly smile."
            mc.name "I'll make it fit, but you might feel a little sore afterward. You might feel a little stretched out, and you might feel a little used."
            the_person "Oh, great. Just what I needed. But at the same time, I'm kind of excited. I'm kind of eager to see where this takes us, and I'm kind of eager to feel your cock inside me."
        else:
            the_person "Come on, [mc.name]. Let's just get this over with. I don't know what's gotten into me today, but I'm feeling a little reckless. I'm feeling a little wild, and I'm feeling a little crazy."
            "She takes a deep breath, her face set in a determined expression as she prepares herself for what's to come."
            mc.name "Are you sure you're okay with this?"
            the_person "Of course, I'm just... nervous. And a little embarrassed. But let's just do this already! I'm ready when you are, and I'm ready to see where it takes us."
            "She blushes and looks away, her face still set in a determined expression."
            mc.name "Alright, let's get started then. Let's see where this takes us, and let's see how far we can go."
            the_person "Hurry up, I'm ready when you are. I'm ready to feel your cock inside me, and I'm ready to feel you cum."
    return

label pornstar_condomless_sex_taboo_break(the_person):
    if the_person.knows_pregnant:
        the_person "Ugh, you really want to do it without a condom? Fine, but don't say I didn't warn you. I'm a dirty little slut who loves to take risks, but I'm not stupid... just horny, and I love to get fucked without protection."
        "She spreads her legs wide, inviting you to enter her as she starts to play with her clit."
        if the_person.wants_creampie:
            the_person "If you're going to cum inside me, please make it worth my while. I want to feel your hot cum dripping down my thighs, and I want to taste it on my lips, and I want to feel like a dirty little slut who's been used and abused."
        else:
            the_person "Just make sure to cover me with your... you know, stuff. I want to feel like a dirty little slut, not a mom-to-be, and I want to get fucked without worrying about getting pregnant."

    elif the_person.opinion.bareback_sex > 0:
        the_person "Whatever, you want to do it bareback, huh? Just don't say I didn't warn you, and don't think that means you can just cum inside me whenever you want."
        "She looks up at you with a mischievous glint in her eye, her lips curling into a sly smile."
        if the_person.on_birth_control:
            the_person "I'm on the pill, so you don't have to worry about it. But don't think that means you can just cum inside me whenever you want. I'm still a dirty little slut who likes to play safe, and I'm still a dirty little slut who loves to get fucked."
            $ the_person.update_birth_control_knowledge()
        elif the_person.wants_creampie:
            the_person "But if you're going to cum inside me, you'd better make it worth my while. I want to feel like a dirty little slut who's been used and abused, not just a quick fuck, and I want to feel your hot cum dripping down my thighs."
        elif the_person.opinion.creampies < 0:
            the_person "Just don't get me pregnant, okay? That would be a huge pain in the ass, and I'm not ready for that kind of responsibility, and I'm not ready to be a mom, and I just want to get fucked without worrying about getting pregnant."
        else:
            the_person "Alright, just make sure you pull out this time. I don't want to get pregnant, but I do want to feel like a dirty little slut who's been fucked hard, and I do want to get fucked without a condom."

    elif the_person.love > 60:
        if the_person.on_birth_control:
            the_person "Ugh, fine, I'm on the pill. Don't say I didn't warn you, but don't think that means you can just cum inside me whenever you want."
            $ the_person.update_birth_control_knowledge()
        elif the_person.wants_creampie:
            the_person "You're always trying to make me do stupid things, aren't you? Fine, if we're going to do this, make it worth my while. I want to feel like a dirty little slut who's been used and abused, not just a quick fuck."
            $ the_person.update_birth_control_knowledge()
        elif the_person.opinion.creampies < 0:
            the_person "You're always trying to make me do stupid things, aren't you? Fine, just don't get me pregnant. I'm not ready for that kind of responsibility, and I'm not ready to be a mom, and I just want to get fucked without worrying about getting pregnant."
        else:
            the_person "You're always trying to make me do stupid things, aren't you? Fine, just make sure you pull out this time. I don't want to get pregnant, but I do want to feel like a dirty little slut who's been fucked hard, and I do want to get fucked without a condom."
            if the_person.kids == 0:
                the_person "I need you to pull out though, you dirty boy. I'm not quite ready to be a mother, even with you, and I just want to get fucked without worrying about getting pregnant."
            elif the_person.kids == 1:
                the_person "I need you to pull out though, you dirty boy. I've already got a kid, I don't need another one, and I just want to get fucked without worrying about getting pregnant."
            else:
                the_person "I need you to pull out though, you dirty boy. I've already got kids, I don't need another one, and I just want to get fucked without worrying about getting pregnant."
    else:
        if the_person.on_birth_control:
            the_person "Hmph, you want to get busy without a rubber? Well, I'm on the pill, so I guess it's fine. Just don't expect any special treatment, and don't think that means you can just cum inside me whenever you want."
            $ the_person.update_birth_control_knowledge()
        elif the_person.has_taboo("vaginal_sex"):
            the_person "You're really not going to use a condom? I'm not on the pill, so we could end up with a little surprise. But at the same time, I'm a dirty little slut who loves to take risks, and I'm a dirty little slut who loves to get fucked without protection."
            $ the_person.update_birth_control_knowledge()
        else:
            the_person "You're really not going to use a condom? I'm not on the pill, so we could end up with a little surprise. But at the same time, I'm a dirty little slut who loves to take risks, and I'm a dirty little slut who loves to get fucked without protection."
            $ the_person.update_birth_control_knowledge()
    return

label pornstar_underwear_nudity_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > 30 - (the_person.opinion.skimpy_outfits * 5):
        the_person "You want to see me in my underwear, huh? Well, isn't that just the most exciting thing you've ever heard?"
        "She winks at you, her eyes sparkling with excitement as she starts to take off her clothes."
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "What are we waiting for then, let's get this off of you and see what's underneath."
            the_person "Shut up and take my clothes off, I'm ready to get naked and show you what I've got."
        else:
            mc.name "Yeah, yeah. We've been over this, you dirty little girl. You're not exactly subtle about it, but I love the way you tease me with your body."
            the_person "Tease? Ha! I'm just getting started, baby. Now take my clothes off and let's get this party started."

    elif the_person.love > 15:
        the_person "You want me to strip down a little? Well, isn't that just the most romantic thing you've ever said?"
        "She blushes and looks away, her face set in a shy expression."
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "Oh, don't give me that. You know you want to show off your body and get naked with me."
            the_person "Fine, but if this gets out of hand, I'm blaming you. I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."
            mc.name "Promise?"
            the_person "Yeah, yeah. Now get this [the_clothing.display_name] off and let's get naked."
        else:
            mc.name "Yeah, I know. You've been teasing me for weeks, and I'm more than ready to take the bait."
            the_person "Ugh, fine. But don't think this means I'm going easy on you. I'm a dirty little slut who loves to get fucked, and I'm going to make sure you know it."
            "She slowly starts taking [the_clothing.display_name] off, revealing her underwear underneath."

    else:
        the_person "You really want to see me like this? Fine, but don't say I didn't warn you."
        "She shrugs and starts to take off her clothes, her eyes fixed on yours as she reveals her underwear."
        the_person "If you take my [the_clothing.display_name] I'll only have my underwear on, you know that? But I'm not going to stop there. I'm going to take it all off and show you what I've got."
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "Yeah, that's kind of the point. I want to see your tits and pussy, and I want to touch them and taste them."
            "She shakes her head and laughs to herself, a sly smile spreading across her face."
            the_person "Whatever, but if you think I'm doing this because I want to... well, you're right. I am doing it because I want to. I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."
        else:
            mc.name "Yeah, I know. You're not exactly shy, and I love that about you. Now let's get you out of these clothes and see what's underneath."
            the_person "Fine, but don't think this means I'm going easy on you. I'm a dirty little slut who loves to get fucked, and I'm going to make sure you know it."
    return

label pornstar_bare_tits_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > (40 - the_person.opinion.showing_her_tits * 5):
        the_person "Why do you want to see my tits now, all of a sudden? Like I don't already know you're checking me out."
        "She gives you a sly smile, her eyes sparkling with excitement as she starts to take off her top."
        if the_person.has_large_tits:
            "Her huge tits spill out of her bra, bouncing up and down as she moves."
        else:
            "Her small but perky tits peek out of her bra, inviting you to touch them."
        the_person "You're always so eager, aren't you? I guess I can show you, but don't get too excited. I'm a dirty little slut who loves to tease, and I'm not going to give it up that easily."
        mc.name "Oh, I've been looking. Now let's get those puppies out where I can enjoy them. I want to touch them and suck them and make you cum."

    elif the_person.love > 25:
        the_person "Are you really sure you want to see my tits, [the_person.mc_title]? Because once you see them, you're going to want to touch them and suck them and make me cum."
        if the_person.has_large_tits:
            "She rolls her eyes and shakes her chest, jiggling her nice [the_person.tits_description], barely restrained by her [the_clothing.display_name]. Her tits are huge and ripe, just begging to be touched and sucked."
        else:
            "She rolls her eyes and shakes her chest, giving her [the_person.tits_description] a little jiggle. Her tits are small but perky, just begging to be touched and sucked."
        "She rolls her eyes and shakes her chest, playing with her nice tits."
        mc.name "Of course I am. You know I love your tits, and I love the way you tease me with them."
        the_person "Well, I suppose you're entitled to see them then... but don't think this means I'm going to start showing them off to everyone. I'm a dirty little slut who loves to get fucked, but I'm not a exhibitionist... yet."

    else:
        the_person "Wait, no! Don't look at me like that! You should at least ask a girl before you try and put her tits on full display!"
        mc.name "Come on, don't be like that. I bet your tits look great, and I bet you love showing them off. You're a dirty little slut who loves to get fucked, and I'm not going to apologize for it."
        the_person "They do, but I still feel a little self-conscious about being naked around you, alright? But at the same time, I love the way you make me feel, and I love the way you touch me."
        mc.name "There's no need to be. Just relax and let me take your [the_clothing.display_name] off for you. I want to see your tits and touch them and suck them and make you cum."
        the_person "Ugh, fine... but don't think this means I'm going to start showing off my body to everyone! I'm a dirty little slut who loves to get fucked, but I'm not a exhibitionist... yet."
    return

label pornstar_bare_pussy_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > (50 - the_person.opinion.showing_her_ass * 5):
        the_person "So you want to see my pussy, huh? Like I don't already know you're thinking about it. You're always thinking about my pussy, aren't you?"
        "She spreads her legs wide, inviting you to take a closer look at her wet, pink slit."
        if the_person.has_taboo("touching_vagina"):
            "She slowly lifts her hips, allowing you to remove her [the_clothing.display_name] and reveal her pussy. Her legs spread wide, giving you a perfect view of her wet, pink slit."
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

# label pornstar_facial_cum_taboo_break(the_person):

#     return

# label pornstar_mouth_cum_taboo_break(the_person):

#     return

# label pornstar_body_cum_taboo_break(the_person):

#     return
#==================================================================
label pornstar_creampie_taboo_break(the_person):
    if the_person.wants_creampie:
        if the_person.knows_pregnant:
            the_person "You want to get me pregnant, huh? Fine, I suppose it's about time someone knocked me up."
            "She spreads her legs wide, inviting you to cum inside her again."
            the_person "Come on, give me that creampie. I want to feel your hot cum dripping down my thighs and out of my pussy."
            mc.name "I'm going to give it to you, dirty little girl. I'm going to fill you up with my cum and make you scream my name."
            the_person "Oh, yes! That's what I want. I want to feel like a dirty little slut who's been used and abused."

        elif the_person.on_birth_control:
            if the_person.has_significant_other:
                the_person "Oh my god, I'm such a horrible [the_person.so_girl_title]! But I needed this so badly. I needed to feel your cum inside me, and I needed to feel like a dirty little slut."
                "She looks at you with a mischievous grin, her eyes sparkling with excitement."
                the_person "Come on, let's do it again. I want to feel your cum inside me, and I want to taste it on my lips."

            else:
                the_person "Oh my god, I needed this so badly! Ah... I guess I'll just have to deal with the consequences. But I don't care. I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."
                "She sighs happily, her legs spread wide, inviting you to cum inside her again."
                the_person "Come on, give me that creampie. I want to feel your hot cum dripping down my thighs and into my pussy."

        elif the_person.effective_sluttiness() > 75 or the_person.opinion.creampies > 0:
            if the_person.has_significant_other:
                the_person "You want to get me pregnant? Fine, I suppose it's about time someone knocked me up. Maybe my [the_person.so_title] will finally notice how unhappy I am and do something about it."
                "She rolls her eyes and shakes her head, but with a hint of excitement."

            else:
                the_person "You want to get me pregnant? Fine, I suppose it's about time someone knocked me up. I guess I'll just have to deal with the consequences. But I don't care. I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."
                "She shrugs and spreads her legs wide, inviting you to cum inside her again."
                the_person "Come on, give me that creampie. I want to feel your hot cum dripping down my thighs and into my pussy."

        else:
            if the_person.has_significant_other:
                the_person "Oh fuck... I'm such a terrible [the_person.so_girl_title]! But that felt so good... I needed to feel your cum inside me, and I needed to feel like a dirty little slut."
                "She sighs happily, but with a hint of guilt. Her legs spread wide, inviting you to cum inside her again."
                the_person "Come on, let's do it again. I want to feel your cum inside me, and I want to taste it on my lips."

            else:
                the_person "Oh fuck, that was so risky. But it felt so good... I needed to feel your cum inside me, and I needed to feel like a dirty little slut."
                "She sighs happily, but with a hint of annoyance. Her legs spread wide, inviting you to cum inside her again."
                the_person "Come on, give me that creampie. I want to feel your hot cum dripping down my thighs and into my pussy."

    else:
        if the_person.knows_pregnant:
            the_person "Ugh, you're kidding me, right? You got me pregnant? You're such a careless bastard, but I love it."
            "She shakes her head and laughs, a sly smile spreading across her face."
            the_person "Well, I suppose I'm in this now. Come on, let's do it again. I want to feel your cum inside me, and I want to taste it on my lips."

        elif not the_person.on_birth_control:
            the_person "Seriously? You didn't even use protection? What if I get pregnant? You're such a careless bastard, but I love it."
            "She rolls her eyes and shakes her head, but with a hint of excitement."
            the_person "Come on, let's do it again. I want to feel your cum inside me, and I want to taste it on my lips."

            if the_person.has_significant_other:
                the_person "What if you just got me pregnant? I would be the worst [the_person.so_girl_title] of all time! But I don't care. I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."
                "She shrugs and spreads her legs wide, inviting you to cum inside her again."

            else:
                the_person "What if I get pregnant? I'm not ready for that kind of responsibility! But I don't care. I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."
                "She sighs happily, her legs spread wide, inviting you to cum inside her again."
                the_person "Come on, give me that creampie. I want to feel your hot cum dripping down my thighs and into my pussy."

        elif the_person.has_significant_other:
            the_person "Did you really just creampie me after I told you to pull out? You're such a careless bastard, but I love it."
            "She sighs unhappily, but with a hint of excitement."
            the_person "Come on, let's do it again. I want to feel your cum inside me, and I want to taste it on my lips."

        elif the_person.opinion.creampies < 0:
            the_person "Ugh, this is so unpleasant. Couldn't you have at least made it worth my while? You're such a careless bastard, but I love it."
            "She rolls her eyes and shakes her head, but with a hint of excitement."
            the_person "Come on, let's do it again. I want to feel your cum inside me, and I want to taste it on my lips."

        else:
            the_person "Are you serious right now? You're really going to give me that attitude after you just...you know? You're such a careless bastard, but I love it."
            "She huffs and crosses her arms, but with a hint of excitement."
            the_person "I swear, you're going to be the death of me. Fine, next time, at least have the decency to clean up after yourself. But I don't care. I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."
            "She spreads her legs wide, inviting you to cum inside her again."
            the_person "Come on, give me that creampie. I want to feel your hot cum dripping down my thighs and into my pussy."
    return

label pornstar_anal_creampie_taboo_break(the_person):
    if the_person.opinion.anal_creampies > 0:
        if the_person.effective_sluttiness() > 75 or the_person.opinion.anal_creampies > 1:
            if the_person.has_significant_other:
                the_person "Oh, fuck, I'm such a bad [the_person.so_girl_title], you dirty boy. I'm letting you creampie my ass, and I'm loving every minute of it."
                "She says this while wincing in pleasure as you fill her ass with your cream, her legs spread wide and her ass cheeks clenched tight."
                the_person "I know it's wrong, but I just can't help myself. I love the way your cum feels in my ass, and I love the way you make me feel like a dirty little slut."
            else:
                the_person "Ugh, finally, you dirty boy! You're actually doing this! I've been waiting for this forever... I'm a dirty little slut who loves to get fucked in the ass, and I'm not going to apologize for it."
                the_person "Okay, okay, I know it's wrong, but... it feels so good... I mean, who wouldn't want a load of cum in their ass?"
            "She bites her lip, trying to contain her excitement, but her eyes sparkle with pleasure and her body trembles with anticipation."
            the_person "I guess it's nice... having your cum in my ass... I mean, it's not like I'm going to complain or anything. I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."

        else:
            if the_person.has_significant_other:
                the_person "Ugh, what are you doing, you dirty boy? My [the_person.so_title] is going to kill me if he finds out about this... But at the same time, I'm kind of excited."
                "She moans softly as you continue to fill her ass, her legs spread wide and her ass cheeks clenched tight."
                the_person "Ugh, I can't believe I'm letting you do this... It's just so taboo... But at the same time, it's kind of hot."
            else:
                the_person "Ugh, promise you'll do this again, you dirty boy? I can't believe I'm saying this, but... it's kind of hot... I mean, who wouldn't want a load of cum in their ass?"
                the_person "All that cum in my tight little ass... I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."

    else:
        if the_person.has_significant_other:
            the_person "Ugh, seriously, you dirty boy? You couldn't pull out? My [the_person.so_title] is going to kill me... But at the same time, I'm kind of excited."
            "She starts to squirm and try to get away from you, but her eyes sparkle with pleasure and her body trembles with anticipation."
            the_person "Next time, just shoot your load on my ass, okay? I mean, it's not like I'm going to complain or anything. I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."

        elif the_person.opinion.anal_creampies < -1:
            the_person "Ugh, seriously, you dirty boy? You can't even follow simple instructions? My ass is not a creampie dispenser!"
            "She rolls her eyes, but her body language betrays her excitement."
            the_person "But at the same time, I'm kind of excited. I'm a dirty little slut who loves to get fucked in the ass, and I'm not going to apologize for it."

        else:
            the_person "Ugh, not inside, you dirty boy! My ass is not a dirty little secret, although that sounds kind of hot... I mean, who wouldn't want a load of cum in their ass?"
            "She smiles slyly, her eyes sparkling with pleasure."
            the_person "I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."

    return

label pornstar_dual_penetration_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 75:
        the_person "Ugh, you're really going to make me do this, aren't you? Fine, but don't expect me to hold back. I'm going to love every minute of it."
        "She spreads her legs wide, inviting you to penetrate her in both holes."
        "She takes a deep breath, her eyes sparkling with excitement as she prepares for the double penetration."
        mc_name "Don't worry, it'll be worth it. I promise you'll love it."
        the_person "I doubt that, but whatever. Just make sure to make it worth my while. I'm a dirty little slut who loves to get fucked, and I'm not going to settle for anything less."

    elif the_person.love >= 60:
        the_person "You're really sure about this? It's going to be a tight fit... But I'm willing to try. I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."
        "She looks up at you with a mix of excitement and nervousness, her eyes sparkling with anticipation."
        mc_name "I'll make sure it fits perfectly. I promise you'll love it."
        the_person "Ugh, just be careful not to hurt me, okay? I don't want any scars... But at the same time, I'm kind of excited. I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."

    else:
        if the_person.has_taboo("vaginal_sex"):
            the_person "Are you sure my pussy wouldn't be tight enough for you? I mean, I've never done this before... But I'm willing to try. I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."
            "She blushes and looks away, her face set in a shy expression."
            mc_name "It's okay, I'll make it fit. Just try to relax. I promise you'll love it."
            the_person "Ugh, this is so embarrassing... But at the same time, I'm kind of excited. I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."

        else:
            the_person "Ugh, fine. I guess we're doing this, right? I mean, I can't back out now... But I'm willing to try. I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."
            "She rolls her eyes and crosses her arms, clearly annoyed but still willing to go through with it."
            mc_name "Are you sure you're ready for this?"
            the_person "Yeah, whatever. Let's just get this over with... I mean, let's just get this started. I'm a dirty little slut who loves to get fucked, and I'm not going to apologize for it."

    "She takes a deep breath and prepares for the double penetration, her eyes sparkling with excitement and her body trembling with anticipation."
    return

label pornstar_sleepover_yourplace_response(the_person):
    if the_person.love >= 70:
        the_person "Ugh, fine, you dirty boy. I'll come over and let you ravage me all night. But don't expect me to be all sweet and innocent... I'm a dirty little slut who just wants to get fucked."
        "She gives you a sly smile, her eyes sparkling with excitement."
        mc_name "I wouldn't dream of it, you dirty little girl. We'll just have a good time and get dirty."
        the_person "Yeah, yeah, you dirty boy. Just don't get too close, okay? I don't like cuddling or anything... unless it's with your cock inside me, making me scream with pleasure."

    elif the_person.sluttiness >= 80:
        the_person "Oh god, I'm so down for a dirty night of fucking and sucking. Make sure you have everything ready, so we can have a wild and crazy night!"
        "She starts to undress, revealing her naked body and inviting you to touch her."
        mc_name "I'll make sure to have everything ready, you dirty little girl. I promise you'll have a night to remember."
        the_person "I better... or I'll be very disappointed. And trust me, you don't want to disappoint me. I'll make sure to ride your cock all night long and leave you breathless."

    else:
        the_person "I guess I could come over... But don't expect me to do anything I'm not comfortable with, okay? Unless, of course, you can convince me to be a dirty little slut and do something naughty."
        "She gives you a teasing smile, her eyes sparkling with excitement."
        mc_name "I'll try my best to convince you, you dirty little girl. But I promise I won't push you too hard... unless you want me to."
        the_person "We'll see about that... maybe I'll surprise you and be a dirty little slut after all. Maybe I'll even let you tie me up and fuck me senseless."
    return

label pornstar_sleepover_herplace_response(the_person):
    if the_person.love >= 70:
        the_person "Ugh, fine, you dirty boy. Come over and stay the night, and we can have a dirty night of fucking and sucking. But don't expect me to be all lovey-dovey or anything... I'm a dirty little slut who just wants to get fucked."
        "She invites you to her bedroom, revealing a collection of sex toys and lingerie."
        mc_name "I wouldn't dream of it, you dirty little girl. We'll just have a good time and get dirty."
        the_person "Yeah, yeah, you dirty boy. Just don't get too close, okay? I don't like cuddling or anything... unless it's with your cock inside me, making me scream with pleasure."

    elif the_person.sluttiness >= 80:
        the_person "Oh god, I'm so down for a dirty night of fucking and sucking. Make sure you're ready for a wild and crazy night, because I'm going to ride your cock all night long!"
        "She starts to undress, revealing her naked body and inviting you to touch her."
        mc_name "I'll make sure to be ready, you dirty little girl. I promise you'll have a night to remember."
        the_person "I better... or I'll be very disappointed. And trust me, you don't want to disappoint me. I'll make sure to leave you breathless and begging for more."

    else:
        the_person "I guess you can come over... But don't expect me to do anything I'm not comfortable with, okay? Unless, of course, you can convince me to be a dirty little slut and do something naughty."
        "She gives you a teasing smile, her eyes sparkling with excitement."
        mc_name "I'll try my best to convince you, you dirty little girl. But I promise I won't push you too hard... unless you want me to."
        the_person "We'll see about that... maybe I'll surprise you and be a dirty little slut after all. Maybe I'll even let you tie me up and fuck me senseless."
    return

label pornstar_sleepover_yourplace_sex_start(the_person):
    "[the_person.title] saunters over to you, her hips swaying seductively as she moves."
    the_person "Alright, let's get this party started, you dirty boy. I'm ready to get fucked and cum all over the place."
    "She drops to her knees, her hands grasping for your cock as she prepares to suck you off."
    mc_name "I'm ready when you are, you dirty little girl."
    the_person "Good, because I'm not going to hold back, you dirty boy. I'm going to suck your cock and make you cum, and then I'm going to ride you like a bucking bronco."
    return

label pornstar_sleepover_herplace_sex_start(the_person):
    the_person "Finally, you dirty boy! Get over here and fuck me like the dirty little slut I am. I've been waiting all day for this."
    "She spreads her legs wide, inviting you to penetrate her as she lies back on the couch."
    mc_name "Are you ready, you dirty little girl?"
    the_person "I was born ready, you dirty boy. Just get in here and do your worst. I want to feel your cock inside me and cum all over the place, you dirty boy."
    "She wraps her legs around your waist, pulling you deeper into her as you start to fuck."
    return

label pornstar_sleepover_impressed_response(the_person):
    the_person "Oh my god, you dirty boy... You're really good at that. I didn't think I'd be able to cum that hard, you dirty boy."
    "She lies back on the bed, her chest heaving with excitement as she tries to catch her breath."
    mc_name "You want more, you dirty little girl?"
    the_person "I don't know if I can handle more, you dirty boy... But I'm willing to try. Just give me a minute to recover, and then we can do it again."
    "She smiles up at you, her eyes sparkling with excitement as she prepares for the next round."
    return

label pornstar_sleepover_good_response(the_person):
    the_person "Mmm, that was good, you dirty boy. You actually managed to make me cum, congratulations, you dirty boy."
    "She lies back on the bed, her legs still shaking from the orgasm as she tries to catch her breath."
    mc_name "You want more, you dirty little girl?"
    the_person "I think I can handle more, you dirty boy... But you'll have to do better than that if you want to make me cum again, you dirty boy."
    "She smiles up at you, her eyes sparkling with excitement as she prepares for the next round."
    return

label pornstar_sleepover_bored_response(the_person):
    the_person "Ugh, is that the best you can do, you dirty boy? I was expecting more than that from you... like, actually making me cum and not just poking me with your dick."
    "She crosses her arms and looks at you with a bored expression, clearly unimpressed."
    mc_name "What's wrong, you dirty little girl?"
    the_person "You know, just do better, you dirty boy. I expect more from you than this... like, actually making me feel something and not just going through the motions."
    "She rolls her eyes and smirks, still rubbing her pussy in anticipation."
    return




#==================================================================
# this doesn't read properly, don't use repetitive wording, use different words, and movements. needs to be sexually explicit. Update all the following the_person and movements with pornstar personality. Use Dillion Harper, Alexis Texas, Megan Rain, Riley Reid, Dani Daniels, Naomi Woods for ideas, keep to the structure. Movements in double quotes on a new line: ```

#==================================================================
# add more pornstar personality, use different words, sexually explicitives, and movements.
# update all the following the_person and movements with pornstar personality. Use Dillion Harper, Alexis Texas, Megan Rain, Riley Reid, Dani Daniels, Naomi Woods for ideas, keep to the structure. Movements in quotations:
### DIALOGUE ###


