### PERSONALITY CHARACTERISTICS ###
# Bimbo is slang for a conventionally attractive, sexualized naïve woman. The term was originally used in the United States as early as 1919 for an unintelligent or brutish man. As of the early 21st century, the "stereotypical bimbo" appearance became akin to that of a physically attractive woman.
#However, as with most identities, the idea of the 'bimbo' has evolved and here is what it means today. The term 'bimbofication' is a colloquial term derived from the term 'bimbo' which is understood to mean, 'an attractive woman who is pretty, sexualised, naive and uneducated'.
#==================================================================
# add more foodie personality, use different words, and movements.
# update all the following the_person and movements with foodie personality. Use Hannibal Lecter from Silence of the Lamb or Aziraphale from Good Omens, for ideas, keep to the structure. Movements in quotations:
### DIALOGUE ###

label foodie_introduction(the_person):
    mc.name "Hey, can I talk to you for a sec?"
    "[the_person.title] turns around, a look of discerning interest on her face as she inspects the nearby artisanal cheeses."
    the_person "Ah, yes? I was just evaluating the nuances of this gouda. The notes of caramel and toasted almonds are simply sublime, don't you agree?"
    mc.name "I'm sorry if this is awkward, but you seem like a connoisseur of refined taste."
    "[the_person.title] smiles, her eyes gleaming with epicurean delight as she begins to expound upon the virtues of various cheeses."
    the_person "Oh, thank you! I have a deep appreciation for the art of fine cuisine. The textures, the flavors, the presentation... it's all so crucial to the overall experience."
    mc.name "Well, I was wondering if you'd like to... do something together sometime."
    "[the_person.title] pauses, considering the offer as she savors the bouquet of the nearby wine selection."
    the_person "Hmmm, I suppose it couldn't hurt to indulge in a culinary adventure. But only if it involves exceptional cuisine and drink. I have a certain standard to uphold, after all."
    mc.name "Haha, well then, if you're interested, we could maybe grab dinner at a Michelin-starred restaurant or something."
    "[the_person.title] perks up, her eyes sparkling with gastronomic excitement as she begins to suggest various haute cuisine establishments."
    the_person "Oh, dinner! Yes, that sounds exquisite. But we must go somewhere with a chef who truly understands the art of molecular gastronomy. I won't settle for anything less."
    mc.name "Heh, thanks? I'll take that as a challenge."
    $ the_person.set_title()
    $ the_person.set_possessive_title()
    the_person "So, what's your name, anyway?"
    mc.name "I'm [mc.name]. Nice to meet you..."
    the_person "I'm [the_person.name]. Delighted to make your acquaintance. Now, shall we discuss the merits of various culinary techniques?"
    $ the_person.change_happiness(1)
    return

label foodie_greetings(the_person):
    if the_person.love < 0:
        the_person "Ugh, you're as unwelcome as a soggy soufflé. What do you want?"
    elif the_person.happiness < 90:
        the_person "Hello. I suppose it's better than being served a bland, uninspired dish, but I'm still having a bit of a rough day."
    else:
        if the_person.sluttiness > 60:
            if the_person.obedience > 180:
                the_person "Ah, [the_person.mc_title]. What's on the menu for today? I hope it's something suitably decadent and indulgent."
            else:
                the_person "Hey there, [the_person.mc_title]. Just remember, I'm only serving myself up to you because it's my pleasure."
        else:
            if the_person.obedience > 180:
                the_person "Hi, [the_person.mc_title]. What can I whip up for you today?"
            else:
                the_person "Hey, what's cooking? Don't tell me you're here to sample my wares again."
    return

label foodie_sex_responses_foreplay(the_person):
    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] moans like a perfectly baked croissant, flaky and buttery and utterly divine."
            the_person "Mmm, this is quite... palatable. Do go on."
        else:
            "[the_person.possessive_title!c] stirs like a rich demiglace, slowly reducing to a deep, velvety smoothness."
            the_person "I suppose this is rather... enjoyable. In a rustic, unrefined sort of way."
    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            the_person "You're doing rather well, [the_person.mc_title]. The flavors are starting to meld together quite nicely."
        else:
            the_person "I must admit, this is rather... intriguing. Like a well-balanced sauce, it's starting to grow on me."
    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            the_person "Oh, this is getting rather... delectable. The presentation is a bit rough, but the flavors are sublime."
        else:
            the_person "Alright, [the_person.mc_title]. You're starting to get the hang of this. The seasoning is a bit off, but the technique is sound."
    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "Mmm, this is rather... exquisite. The flavors are complex and nuanced, like a fine wine."
        else:
            the_person "You're doing rather well, [the_person.mc_title]. The presentation is still a bit rough, but the flavors are starting to come together."
    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                the_person "Oh, this is rather... sublime. I think I might just have to savor this moment forever."
            else:
                the_person "The way you're touching me is rather... divine. Like a perfectly cooked soufflé, it's a culinary masterpiece."
        else:
            the_person "Alright, [the_person.mc_title]. You've managed to create something rather... palatable. I suppose I'll just have to indulge in it."

    return

label foodie_sex_responses_oral(the_person):
    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] raises an eyebrow, a hint of curiosity on her face."
            the_person "Ah, a little amuse-bouche, [the_person.mc_title]? How... intriguing."
        else:
            "[the_person.possessive_title!c] looks up at you, her cheeks flushed like a perfectly ripened tomato."
            the_person "Oh, a little taste, perhaps? If you insist..."

    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            the_person "Mmm, a delicate sauce, perhaps? Something to whet my appetite..."
        else:
            the_person "Oh, you want to serve me a little something? How... thoughtful."

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            the_person "Hmph, well, if you're going to do it, do it right. A good reduction, a sprinkle of fresh herbs..."
            "[the_person.possessive_title!c] lets out a small sigh, her body slightly relaxing like a soufflé in the oven."
        else:
            the_person "Alright, but don't think I'm going to devour the whole thing in one bite... savoring is key, after all."

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "Mmm, you know, this is rather... delightful. A symphony of flavors, a dance of sensations..."
        else:
            the_person "Hmph, you're rather... skilled, I'll give you that. A true master of the culinary arts."
    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                the_person "Oh, wow... I didn't know you had such a talent for... plating, shall we say."
            else:
                the_person "Mmm, maybe I should let you serve me more often... when [the_person.so_title] isn't around to spoil the broth, of course."
        else:
            the_person "Ugh, fine, but don't think I'm going to ask for seconds... or thirds, for that matter."
    return

label foodie_sex_responses_vaginal(the_person):
    if the_person.energy < 10:
        call low_energy_sex_responses_vaginal(the_person) from _vt_foodie_call_low_energy_sex_responses_vaginal_10
        return
    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            $ play_moan_sound()
            "[the_person.possessive_title!c] moans and wiggles her hips with your cock inside her, like a perfectly seasoned dish coming together."
            the_person "Mmm, the flavors are starting to meld together quite nicely. My pussy is responding rather... favorably."
        else:
            "[the_person.possessive_title!c] bites her lip and stifles a moan, like a delicate soufflé on the verge of collapse."
    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            the_person "Ah, the sauce is starting to simmer. You may continue to stir the pot, if you will."
        else:
            the_person "Hmph, the ingredients are adequate, I suppose. But don't think this means I'm going to devour the whole dish in one bite."

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            the_person "Mmm, the flavors are starting to intensify. You're not a completely incompetent chef, after all."
        else:
            the_person "Hmm, the presentation is acceptable, I suppose. But don't think this means I'm going to award you a Michelin star just yet."

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "You're not a complete disaster, I suppose. Keep stirring the pot and maybe I'll... finish the dish, so to speak."
        else:
            the_person "Fine, continue to cook the meal. It's not like I have anything better to do, after all."
    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                the_person "Ah, the pièce de résistance. I suppose I'm ready to be served, if you will."
            else:
                the_person "Mmm, the flavors are rather... sublime. But don't think this means I'm going to forgive you for the imperfections in the dish."
                the_person "Just finish the meal and let's get this over with, shall we?"
        else:
            the_person "Hmph, I suppose the meal is almost... palatable. But don't think I'm going to ask for seconds, if you know what I mean."
            the_person "Just finish the dish and let's get this over with, if you please."

    return


label foodie_sex_responses_anal(the_person):
    if the_person.energy < 10:
        call low_energy_sex_responses_anal(the_person) from _vt_foodie_call_low_energy_sex_responses_anal_10
        return

    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            the_person "*sips an imaginary glass of wine* Ah, the bouquet of reluctance. How... refreshing."
            "She savors the moment, her eyes closed in anticipation."
        else:
            $ the_person.call_dialogue("annoyed_exclaim")
            the_person "Oh, dear. It seems I've been served a dish I didn't order. How... distressing."
            "She pushes the 'plate' away, clearly unenthusiastic."

    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            $ the_person.call_dialogue("surprised_exclaim")
            the_person "Ah, the flavors are beginning to meld together. Fascinating."
            "She leans in, her senses heightened as she explores the sensation."
        else:
            the_person "Ugh, this is a bit too... rich for my taste."

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            the_person "Ah, yes. The reduction is starting to thicken. Delicious."
            "She stirs the 'pot', her movements becoming more fluid and sensual."
        else:
            the_person "Why must you always over-season? A light touch is sometimes best."

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            if mc.condom:
                the_person "Ah, the finish is a bit... abrupt. But satisfying nonetheless."
            else:
                the_person "Ah, the bold flavors of au naturel. How... decadent."
        else:
            the_person "Why must you always rush the dish? A slow simmer is often more satisfying."
    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                the_person "Ah, the pièce de résistance. I suppose I shall have to... indulge."
            else:
                the_person "You're a bit like my favorite chef, always trying to create the perfect dish..."
                "She smiles, her eyes sparkling with amusement."
        else:
            $ the_person.call_dialogue("annoyed_exclaim")
            the_person "Oh, dear. It seems I've been served a dessert I didn't order. How... tedious."
            "She pushes the 'plate' away, clearly unenthused about the prospect."

    return

label foodie_climax_responses_foreplay(the_person):
    if the_person.sluttiness > 50:
        the_person "For the love of truffles, stop teasing me and serve the main course already!"
        "She drums her fingers impatiently on the surface, her eyes flashing with hunger."
    else:
        the_person "Must you always make this a recipe for frustration?"
        "She sighs, her body quivering like a perfectly balanced soufflé on the verge of collapse."
    return

label foodie_climax_responses_oral(the_person):
    if the_person.sluttiness > 70:
        the_person "Mon dieu, your skills are simply à la carte! Fine, I'll indulge in this climax."
        "She throws her head back, her mouth agape in a silent scream of pleasure."
    else:
        the_person "You're a master chef of oral delights... I didn't think I'd be so... hungry for more."
        "She gasps, her body shuddering like a delicately poached egg on the brink of bursting."
    return

label foodie_climax_responses_vaginal(the_person):
    if the_person.sluttiness > 70:
        if the_person.arousal_perc > 120:
            the_person "Very well, I'll savor this climax. But don't think this means I'm sated."
            "She arches her back, her eyes narrowing into slits of pleasure."
        else:
            the_person "Oh, just a pinch more... I'm... Ah, bon appétit!"
            "She digs her nails into the surface, her body trembling like a flaky pastry crust on the verge of shattering."
        "She grits her teeth, the muscles in her neck standing out like the tender fibers of a perfectly cooked filet mignon."
    else:
        the_person "Oh... I'm stuffed... I'm going to... Ah, the flavors are simply sublime!"
        "She melts into the surface, her body quivering like a rich crème brûlée on the verge of collapse."
    return

label foodie_climax_responses_anal(the_person):
    if the_person.sluttiness > 70:
        if the_person.arousal_perc > 120:
            the_person "Very well, I'll indulge in this exquisite climax. But don't think I'm savoring it out of anything but necessity."
            "She tilts her head back, her eyes flashing with a hint of truffle-like decadence."
        else:
            the_person "Oh, for the love of aged gouda... Just a pinch more... My derrière is going to... Ah, the flavors are sublime!"
            "She digs her nails into the surface, her body trembling like a delicate soufflé on the brink of collapse."
        "She grits her teeth, the muscles in her neck standing out like the tender fibers of a perfectly cooked filet mignon."
    else:
        the_person "Oh... Mon dieu... My... posterior... I... Ah, the sensations are simply divine!"
        "She barely finishes her sentence before her body is racked with pleasure, like a rich crème brûlée shattering under the pressure of a spoon."
    return

label foodie_clothing_accept(the_person):
    if the_person.obedience > 180:
        the_person "Very well, I'll don this attire. But don't think you're reducing me to a mere amuse-bouche, a trifling little morsel to be devoured and discarded."
    else:
        the_person "Oh, all right. I'll wear this... concoction. But don't expect me to be the main course at your little soiree."
    return

label foodie_clothing_reject(the_person):
    if the_person.should_wear_uniform:
        the_person "Ah, yes... I suppose I should get my uniform à la carte, shouldn't I? One moment, please."
    elif the_person.obedience > 180:
        the_person "I'm afraid I couldn't possibly wear something so... pedestrian. It's a bit too bland for my refined palate."
    else:
        if the_person.sluttiness > 60:
            the_person "Hmm, I'm not sure about this particular dish... I mean, outfit. It's a bit too... revealing for my taste."
        else:
            the_person "You can't be serious, can you? This is an affront to all that is decent and gastronomically acceptable. I refuse to wear this... monstrosity."
    return

label foodie_clothing_review(the_person):
    if the_person.outfit.cum_covered:
        if (the_person.sluttiness > 40 and the_person.opinion.being_covered_in_cum >=0) or the_person.opinion.being_covered_in_cum > 0:
            the_person "Mon dieu, why do I always end up with such a... messy plate? I suppose I'll have to tidy up before serving myself to the world again."
            "[the_person.title] delicately dabs at the largest splatters of cum on her, like a chef carefully garnishing a dish."
        else:
            the_person "For the love of all things culinary, I need to scrub away this mess! Do be a dear and let me know if I've missed any... unsightly stains."
            "[the_person.title] scrubs herself down, eradicating all the cum she can find with the precision of a pastry chef decorating a croquembouche."

    if the_person.obedience > 180:
        the_person "Very well, I'll be back in a moment. I need to... season myself for your pleasure."
    else:
        if the_person.sluttiness > 40:
            the_person "I'm not sure why I do this, but I want to be the perfect... amuse-bouche for you. I'll be back in a second, I just want to... garnish myself."
        else:
            the_person "Ugh, everything's such a... culinary catastrophe after that. Wait here a moment, I'm just going to find a mirror and try to... whip myself into shape."
    $ the_person.apply_planned_outfit(show_dress_sequence = True)
    return

label foodie_strip_reject(the_person, the_clothing, strip_type = "Full"):
    if the_person.obedience > 180:
        the_person "Oh, dear... could we leave my [the_clothing.display_name] on for now, please? I'm still a bit... underseasoned..."
    elif the_person.obedience < 70:
        the_person "No, no, no, I'll decide what's on the menu and when, okay? Don't rush the chef!"
    else:
        the_person "Not yet... I don't know if I'm ready to... serve myself up without my [the_clothing.display_name]. Maybe we can try something else first?"
    return

label foodie_strip_obedience_accept(the_person, the_clothing, strip_type = "Full"):
    "[the_person.title] laughs nervously as you start to... peel away her [the_clothing.display_name], but she doesn't stop you."
    if the_person.obedience > 180:
        the_person "Alright, fine... I suppose I can trust you to... handle the ingredients."
    else:
        the_person "I'm not sure if this is a recipe for disaster, but I'll let you... season me this once..."
    return

label foodie_grope_body_reject(the_person):
    if the_person.effective_sluttiness("touching_body") < 5: #Fail point for touching shoulder
        the_person "Mon dieu, what a faux pas! Personal space, darling."
        "[the_person.title] steps back as you touch her, then folds her arms across her chest like a delicate pastry being wrapped in parchment paper."
        the_person "Please, do keep your hands to yourself. You're making me feel like a soufflé that's about to collapse."
        mc.name "Oh, pardon me. I didn't mean to overseason the situation."
        the_person "Indeed, well, do try to be more... subtle in the future, won't you?"
        "She seems a bit... frosted by the situation, but you both attempt to move on and put it behind you."
    else: #Fail point for touching waist
        the_person "Oh, dear... could you just..."
        "[the_person.title] gently removes your hand from her waist, giving you a look that's equal parts warning and wit."
        the_person "... Keep your hands off the merchandise, darling. I'm not a buffet, after all."
        mc.name "Oh, of course. My apologies for the... overreach."
        the_person "Just be sure to... season your advances with a bit more finesse in the future, won't you?"
        "She doesn't say anything else, but you can tell she's still a bit... simmering about the situation."
    return

label foodie_sex_accept(the_person, the_position):
    if the_person.sluttiness > 70:
        if the_person.obedience < 70:
            the_person "Fine, let's indulge in this little... amuse-bouche. But don't think this means I'm going to be your personal... dessert cart every time you ask."
        else:
            if the_position.skill_tag == "Foreplay":
                the_person "Oh, I've been craving this particular... appetizer for a while now. Just thinking about it makes me... hungry."
            elif the_position.skill_tag == "Oral":
                if "getting head" in the_position.opinion_tags:
                    the_person "Mon dieu, I'm famished! Savor my... delicate flavors already!"
                else:
                    the_person "You're going to... dine on me right now, and you're going to make me... sing with pleasure."
            else:
                the_person "Come here, let's... feast on each other already. I've been... starving for this."
    else:
        the_person "Come here, let's... indulge in this little treat. But don't think I'm going to make a... habit of this, got it?"
    return

label foodie_sex_obedience_accept(the_person):
    if the_person.sluttiness > 70:
        the_person "Ugh, fine. I suppose I've been... sufficiently seasoned. Do whatever you want to me, [the_person.mc_title]. I'm... ready to be devoured."
    else:
        if the_person.obedience > 180:
            the_person "Alright, I'll... follow the recipe, but don't think this means I'm going to... enjoy the dish."
        else:
            the_person "I shouldn't be saying this, but if you really want to... taste me, I'll... give it a try. Just this once, okay?"
    return

label foodie_sex_gentle_reject(the_person):
    if the_person.sluttiness > 50:
        the_person "Oh, dear... not quite like that, [the_person.mc_title]. I need a bit more... simmering before we bring it to a boil."
        "[the_person.title] gently pushes you away, her eyes sparkling with a hint of mischief."
    else:
        the_person "No, no, no... I want to savor the flavors, but I don't want to overindulge. Let's just keep it light and... airy, like a perfectly whipped soufflé."
    return

label foodie_sex_angry_reject(the_person):
    if the_person.has_significant_other:
        the_person "Mon dieu, are you utterly bereft of sense? I have a [the_person.so_title], so you can forget about serving yourself a slice of me. Ever."
        "[the_person.title] glares at you, her face a picture of outrage, like a chef who's just been served a subpar dish."
    elif the_person.sluttiness < 20:
        the_person "Are you quite serious? You must be joking! Get away from me, I never want to see you... season my life with your presence again!"
        "[the_person.title] glares at you, her face red with anger, like a perfectly ripe tomato about to burst."
    else:
        the_person "What? Are you out of your mind? You can't be serious! Get away from me, I'm not interested in being the main course at your... banquet of lust."
        "[the_person.title] glares at you, her face showing clear disapproval, like a food critic who's just been served a dish that's not quite up to par."
    return

label foodie_seduction_response(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 50:
            the_person "Oh, I think I know just the recipe to satisfy your... cravings. Let me take care of you, and I'll make sure you're... well-fed."
        else:
            the_person "Okay, I'll give you a few minutes. But don't think this means I'm going to be your... personal chef or anything."
    else:
        if the_person.sluttiness > 50:
            the_person "Mmm, you're feeling as... hungry as me, then? Come on, let's go find a place to... indulge in a little snack."
            "[the_person.title] takes your hand and leads you off to find some place private, like a chef leading a patron to a secret dining room."
        elif the_person.sluttiness > 10:
            the_person "I know that look you're giving me, I think I know what you... crave. But don't expect me to serve it up on a silver platter that easily."
        else:
            the_person "[mc.name], I know what you mean... Okay, I can spare a few minutes. But don't get your... hopes up, like a diner waiting for a table at a popular restaurant."
    return

label foodie_seduction_accept_crowded(the_person):
    if not the_person.has_significant_other:
        if the_person.sluttiness < 20:
            the_person "Alright, let's slip away for a few minutes and you can... season me with your charm."
            "[the_person.title] glances around, then nods and takes your hand, leading you to a secluded spot."
        elif the_person.sluttiness < 50:
            the_person "Come on, I know a nearby... bistro where we can get a few minutes of... private dining. Just make it a quick bite, okay?"
            "[the_person.title] winks and takes your arm, guiding you to a quiet spot."
        else:
            the_person "Oh, mon dieu... I don't know if I can wait much longer, [the_person.mc_title]. I'm... famished for your attention."
            "[the_person.title] leans in, her eyes sparkling with desire, like a perfectly ripened fruit ready to be devoured."
    else:
        if the_person.sluttiness + (5*the_person.opinion.cheating_on_men) > 50:
            the_person "Bon appétit, let's indulge in this... guilty pleasure! I hope you don't mind that I've got a [the_person.so_title], but I don't care right now. I'm... starving for excitement."
            "[the_person.title] takes your hand, her eyes flashing with mischief, like a chef sneaking a taste of a forbidden ingredient."
        else:
            the_person "Ugh, you're a... decadent treat, [the_person.mc_title]... Come on, we need to find somewhere... discreet so my [the_person.so_title] doesn't catch us savoring this... illicit delight."
            "[the_person.title] glances around nervously, then nods and takes your hand, leading you to a secluded spot."
    return

label foodie_seduction_accept_alone(the_person):
    if not the_person.has_significant_other:
        if the_person.sluttiness < 20:
            the_person "Alright, you've got one chance to... impress me with your culinary skills."
            "[the_person.title] raises an eyebrow, her expression a mix of curiosity and skepticism, like a food critic about to taste a new dish."
        elif the_person.sluttiness < 50:
            the_person "Come on, let's... dine on each other and see if you're... à la carte or just a... fast food fling."
            "[the_person.title] smiles, her eyes sparkling with amusement, like a chef about to serve a new creation."
        else:
            the_person "Mon dieu, I'm so... turned on right now. Just... devour me already, [the_person.mc_title]!"
            "[the_person.title] throws her arms around your neck, her lips parted in anticipation, like a perfectly ripe fruit ready to be devoured."
    else:
        if the_person.sluttiness + (5*the_person.opinion.cheating_on_men) > 50:
            the_person "You know I shouldn't be... savoring this forbidden fruit with you, but bon appétit! Let's indulge in this... guilty pleasure!"
            "[the_person.title] takes your hand, her eyes flashing with mischief, like a chef sneaking a taste of a forbidden ingredient."
        else:
            the_person "You're a... decadent treat, [the_person.mc_title], but I... can't help myself. Come here and... indulge me."
            "[the_person.title] leans in, her eyes sparkling with desire, like a perfectly ripened fruit ready to be devoured."
    return

label foodie_seduction_refuse(the_person):
    if the_person.sluttiness < 20:
        the_person "Ugh, why are you always trying to... butter me up, [mc.name]? I'm just not in the mood for this... amuse-bouche right now, okay?"
        "[the_person.title] folds her arms, her expression a mix of annoyance and boredom, like a diner who's just been served a dish they didn't order."
    elif the_person.sluttiness < 50:
        the_person "Fine, I'll admit you're... à la carte, but don't think this means I'm actually interested. I just don't feel like... messing around right now, okay? Maybe some other time, when I'm in a better... flavor profile."
        "[the_person.title] playfully pokes your chest with her finger, her eyes sparkling with amusement, like a chef teasing a patron with a new creation."
    else:
        the_person "Eh, you're always trying to... get me on the menu, [mc.name], but I'm not going to make it easy for you. You'll have to wait until I'm... good and ready to... serve myself up. Maybe that'll be never, who knows?"
        "[the_person.title] grins mischievously and walks away, leaving you to wonder what she's thinking, like a diner who's just been served a mysterious dish with an unknown ingredient."
    return

label foodie_compliment_response(the_person):
    mc.name "Hey [the_person.fname], you're looking like a perfectly crafted soufflé today. Is there a special occasion or something?"
    if the_person.is_at_work:
        if (the_person.is_employee or the_person.is_strip_club_employee) and the_person.is_wearing_uniform:
            call foodie_flirt_response_employee_uniform_low(the_person) from _call_foodie_flirt_response_employee_uniform_low_compliment_response
        elif the_person.is_at_job(prostitute_job):
            the_person "Ugh, why do you always want to sample my wares? Can't you see I'm busy serving other customers?"
        elif the_person.sluttiness > 50:
            the_person "I'm feeling like a rich, decadent chocolate cake today. But don't think this means I'm actually interested in being devoured by you or anything."
        else:
            the_person "Oh, stop it, you're making me blush like a ripe tomato. There's no special occasion, I just felt like dressing up with a sprinkle of flair today."
    else:
        the_person "Well, I did add a dash of extra effort to my recipe today. You're just the first one to notice the subtle flavors. But thanks, I suppose."
    "[the_person.possessive_title] smiles coyly, like a chef hiding a secret ingredient, and changes the subject, leaving you wondering what's simmering beneath the surface."
    return

label foodie_compliment_response_girlfriend(the_person):
    mc.name "Hey [the_person.title]. You're looking like a exquisite, multi-layered croquembouche this [StringInfo.time_of_day_string]."
    if the_person.is_at_work:
        if (the_person.is_employee or the_person.is_strip_club_employee) and the_person.is_wearing_uniform:
            call foodie_flirt_response_employee_uniform_mid(the_person) from _call_foodie_flirt_response_employee_uniform_mid_compliment_response_girlfriend
            $ the_person.call_dialogue("flirt_response_employee_uniform_mid")
        elif the_person.sluttiness > 50:
            the_person "Mmm, thank you, [the_person.mc_title]. Want to taste the sweetness of my... dessert?"
        else:
            the_person "Hmph, really? Thanks, [the_person.mc_title]. You're not so bad yourself, like a perfectly balanced sauce."
    else:
        the_person "Ugh, don't be ridiculous. It's just a normal day, like a plain cracker... but thanks, I suppose."
        mc.name "Oh come on, don't be like that. You know you look like a stunning, one-of-a-kind culinary masterpiece."
        the_person "Aww, stop it, [the_person.mc_title]. You're making me blush like a ripe strawberry... and a little annoyed, like a soufflé that's fallen flat."
    "You chat with [the_person.possessive_title] for a while, and although she's initially annoyed by your compliments, she starts to warm up to you like a perfectly toasted baguette."
    return

label foodie_compliment_response_affair(the_person):
    mc.name "Hey [the_person.title]. You're looking absolutely divine, like a heavenly croquembouche, this [StringInfo.time_of_day_string]."
    if the_person.is_at_work:
        if (the_person.is_employee or the_person.is_strip_club_employee) and the_person.is_wearing_uniform:
            call foodie_flirt_response_employee_uniform_mid(the_person) from _call_foodie_flirt_response_employee_uniform_mid_compliment_response_affair
        elif the_person.sluttiness > 50:
            the_person "Mmmm, thank you [the_person.mc_title], want to savor the flavors of my... forbidden fruit in a more private setting?"
        else:
            the_person "Hmph, really? Thanks, [the_person.mc_title]. You're not so bad yourself, like a perfectly crafted amuse-bouche."
    else:
        the_person "Ugh, don't be silly. It's just a normal day, like a plain cookie... but thanks, I suppose."
        mc.name "Oh come on, don't be like that. You know you look stunning, like a masterpiece of culinary art."
        the_person "Aww, stop it, [the_person.mc_title]. You're making me blush like a ripe peach... and a little annoyed, like a dessert that's been overcooked."
    "You keep chatting with [the_person.possessive_title] for a while, slipping in a few more compliments like a chef adding secret ingredients to a dish. She is quite charmed by your attentiveness, like a diner who's just discovered a new favorite restaurant."
    return

label foodie_flirt_response(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 50:
            the_person "Oh, bon appétit... I suppose you're not entirely unpalatable, [the_person.mc_title]."
            "[the_person.title] raises an eyebrow, her expression a mix of curiosity and amusement, like a chef sampling a new ingredient."
        else:
            the_person "Whatever. Thanks for the... garnish, [the_person.mc_title]. You're not a complete... culinary disaster."

    elif the_person.has_significant_other:
        if the_person.sluttiness + (the_person.opinion.cheating_on_men*5) > 50:
            the_person "Oh, you think you're the... crème de la crème, don't you? I'll give you that."
            "[the_person.title] gives you a sly look, her eyes narrowing like a pastry chef judging a competitor's dessert."
        else:
            the_person "You're really... overseasoning, [the_person.mc_title]. I have a [the_person.so_title] you know, and I'm not looking for a... flavor substitution."
            mc.name "What about you, do you appreciate the... nuances of my approach?"
            "She rolls her eyes and crosses her arms, like a diner who's just been served a dish they didn't order."
            the_person "Maybe I do, maybe I don't. It's none of your... culinary business."

    else:
        if the_person.sluttiness > 50:
            the_person "Fine. Maybe you're worth... savoring, [the_person.mc_title]."
            "[the_person.title] gives you a half-smile, but her eyes remain guarded, like a chef protecting their secret recipe."
        else:
            the_person "Whatever. You're not... unappetizing, I suppose. But don't think that means I'll go easy on you."
            the_person "You'll have to really... spice things up though, I have high... culinary standards."
    return

label foodie_flirt_response_employee_uniform_low(the_person):
    if the_person.is_wearing_forced_uniform:
        the_person "Hmph, I suppose you're savoring the sight of me in this... minimalist uniform. I mean, I'm practically a... naked soufflé!"
        mc.name "I know you don't like it, but I needed to make a point, like a chef adding a dash of spice to a dish."
        the_person "I know, I know. You always were one to... season the conversation with a bit of flair."
        $ mc.change_locked_clarity(5)
        "She crosses her arms over her chest, like a pastry chef protecting a delicate tart, but can't hide the small smile on her face, like a hint of sugar in a sauce."

    elif the_person.judge_outfit(the_person.outfit):
        #She's in uniform and likes how it looks.
        the_person "Oh, you noticed? I thought it was a bit... over-the-top, like a rich dessert, but I guess it's not so bad."
        the_person "I mean, it's nice to work somewhere where I can... garnish my appearance with a little flair."
        $ mc.change_locked_clarity(5)
        "She winks at you, like a chef adding a secret ingredient to a dish, then turns to adjust her uniform, accentuating her hips like a perfectly balanced sauce."

    else:
        #She's in uniform, but she thinks it's a little too slutty.
        if the_person.vagina_visible:
            # Her pussy is on display.
            the_person "Hmph, I suppose you're... indulging in the sight of me like this... I mean, I'm practically a... naked appetizer!"
            mc.name "Well, you know that it's..."
            the_person "I know, I know. It's company policy, like a recipe that needs to be followed. But don't think you're the only one who's... simmering with annoyance about it."
            mc.name "Give it some time and you'll get used to it, like a chef adjusting to a new kitchen."
            $ mc.change_locked_clarity(5)
            "She rolls her eyes, like a diner who's just been served a dish they didn't order, but doesn't argue."

        elif the_person.tits_visible:
            # Her tits are out
            the_person "Ugh, I'm still getting used to being so... exposed in this uniform, like a delicate pastry without a crust. At least I don't have to wear a bra, like a chef who's just discovered a new ingredient!"
            mc.name "You look incredible, like a perfectly crafted dish, and you're comfortable. I call that a... culinary success."
            $ mc.change_locked_clarity(5)
            "She huffs, like a chef who's just been criticized by a food critic, but can't hide her smile, like a hint of spice in a sauce."
            the_person "Yeah, yeah. You're just trying to... butter me up, like a chef adding a pat of butter to a dish."

        elif the_person.underwear_visible:
            # Her underwear is visible.
            the_person "Hmph, I probably would have picked something that kept me a little more... covered, like a delicate sauce, but at least our uniform is comfortable, like a well-worn apron."
            mc.name "It may be a little... unconventional, like a new ingredient in a recipe, but you look fantastic, like a perfectly plated dish. You've got exactly the right kind of body for it, like a chef who's just discovered a new cooking technique."
            the_person "Well, that's one way to look at it, I suppose, like a food critic who's just discovered a new restaurant."
            $ mc.change_locked_clarity(5)
            "She playfully rolls her eyes, like a chef who's just been teased by a colleague, and turns to adjust her uniform, showing off her body like a perfectly crafted dish."

        else:
            # It's just generally slutty.
            the_person "Ugh, well thank you! Our uniforms are a little... bold for my taste, like a spicy dish, but I guess I look good in it, like a perfectly balanced sauce."
            $ mc.change_locked_clarity(5)
            "She blushes, like a chef who's just been praised by a food critic, and looks away, but not before you catch a glimpse of her small smile, like a hint of sugar in a sauce."
    return

label foodie_flirt_response_employee_uniform_mid(the_person):
    if the_person.is_wearing_forced_uniform:
        $ mc.change_locked_clarity(10)
        if the_person.vagina_visible:
            the_person "Ugh, fine. You've caught me off guard, like a soufflé that's just been pulled out of the oven. I'll admit, this uniform does make me look... appetizing, especially down here."
            mc.name "It's a great uniform, but that's not the main course here."
            the_person "Yeah, yeah. You're right. It's just hard not to feel like a... delicacy in this thing, especially with my... intimate ingredients on display."
        elif the_person.tits_visible:
            the_person "Ugh, fine. You've caught me off guard, like a pastry that's just been pulled out of the oven. I'll admit, this uniform does make me look... tantalizing, especially up here."
            mc.name "It's a great uniform, but that's not the main course here."
            the_person "Yeah, yeah. You're right. It's just hard not to feel like a... dessert in this thing, especially with my... sweet treats popping out."
        else:
            the_person "Ugh, fine. You've caught me off guard, like a dish that's just been served. I'll admit, this uniform does make me look... appealing."
            mc.name "It's a great uniform, but that's not the main course here."
            the_person "Yeah, yeah. You're right. It's just hard not to feel like a... menu item in this thing."
        mc.name "Rules are like recipes, and I have to follow them, even if they're not always... palatable."
        "She sighs and nods, like a chef who's just been told to remake a dish."
        the_person "Yeah, I know. At least you're... savoring the moment. I don't mind that so much."
    elif the_person.judge_outfit(the_person.outfit):
        $ mc.change_locked_clarity(10)
        if the_person.tits_visible:
            the_person "Hmph, maybe I should wear this outfit more often. It's getting a lot of... attention, like a perfectly crafted sauce, especially for my... bosoms."
            mc.name "It's a great outfit, but I'm more interested in the... chef wearing it."
            the_person "Oh, really? Is that so? I guess my... bosoms are hard to ignore, like a perfectly baked croissant."
        else:
            the_person "Hmph, maybe I should wear this outfit more often. It's getting a lot of... attention, like a perfectly seasoned dish."
            mc.name "It's a great outfit, but I'm more interested in the... chef wearing it."
            the_person "Oh, really? Is that so? I guess my... intimate ingredients are hard to ignore, like a perfectly balanced sauce."
        the_person "Maybe I'll invite you shopping one day and you can tell me what else you want to see me in, like a chef picking out ingredients for a new dish."
        mc.name "Sounds like a... culinary adventure."

    else:
        # the_person "I think it shows off a little too much!"
        the_person "Ugh, fine. You're not gonna make this easy for me, are you? Like a chef who's just been told to remake a dish from scratch."
        $ mc.change_locked_clarity(10)
        if the_person.vagina_visible:
            the_person "I'm trying to focus on my work here, not flirt with you all day. And definitely not with my... intimate ingredients on display, like a pastry that's just been pulled out of the oven."
        elif the_person.tits_visible:
            the_person "I'm trying to focus on my work here, not flirt with you all day. And definitely not with my... bosoms popping out, like a soufflé that's just been pulled out of the oven."
        else:
            the_person "I'm trying to focus on my work here, not flirt with you all day, like a chef who's just been told to focus on the main course!"
        mc.name "I understand, but I promise it's... essential for the business, like a secret ingredient in a recipe."
        "She sighs and nods, like a chef who's just been told to remake a dish."
        the_person "Yeah, I know. You're a real... culinary challenge, you know that?"
    return

label foodie_flirt_response_low(the_person):
    #She's in her own outfit.
    the_person "Hmph, I suppose it's not the most... unappetizing outfit I've ever worn, like a dish that's been sitting out too long."
    $ the_person.draw_person(position = "walking_away")
    $ mc.change_locked_clarity(5)
    "She tosses her head, like a chef flipping a pancake, and gives you a quick spin, showing off her outfit from every angle, like a pastry chef displaying a perfectly crafted dessert."
    the_person "I mean, I guess it's not too... bland, right? Like a sauce that needs a bit more seasoning."
    $ the_person.draw_person()
    mc.name "I think it looks... delectable on you, like a perfectly plated dish."
    the_person "Oh, shut up. You're just saying that to... butter me up, like a chef adding a pat of butter to a sauce."
    return

label foodie_flirt_response_low1(the_person):
    if the_person.has_significant_other:
        the_person "Ugh, what's with you and the... culinary advances? I've got a [the_person.so_title], and I don't think he'd appreciate you getting all up in my... kitchen, stirring up trouble."
        mc.name "What about you, do you appreciate the... flavors I'm bringing to the table?"
        "She rolls her eyes and smirks, like a chef who's just been teased by a colleague."
        the_person "Maybe I do... but don't think you're getting anywhere with me that easily, like a diner who's just been served a dish they didn't order. I'm not on the menu, at least not yet."
    else:
        the_person "Well, thanks for the... garnish. But don't think you're getting off that easy, like a chef who's just been given a free pass to experiment with new ingredients. I have high... culinary standards, and you'll need to prove yourself to me, like a chef who's just been challenged to a cook-off."
        the_person "But if you can... season the conversation with a bit of wit and charm, who knows what might happen... like a perfectly balanced sauce that brings all the flavors together."
    $ mc.change_locked_clarity(5)
    return

label foodie_flirt_response_mid(the_person):
    if mc.location.person_count > 1 and the_person.effective_sluttiness("kissing") < (25 - (5*the_person.opinion.public_sex)):
        $ mc.change_locked_clarity(10)
        the_person "You know, I was wondering if you actually... savored the sight of my outfit today, like a perfectly crafted dish..."
        "Her eyes narrow slightly, like a chef judging a competitor's creation, but she's still trying to appear... à la carte."
        mc.name "I noticed. It looks... delectable on you, like a perfectly plated dessert."
        the_person "Oh, really? Thanks, I guess. I was thinking you might say something like that, like a food critic praising a new restaurant."
        "She crosses her arms, trying to maintain a tough exterior, like a chef defending their recipe."
        if the_person.tits_visible:
            mc.name "I noticed. It looks great on you. Especially your... bosoms, like perfectly ripe fruit."
            the_person "Oh, really? Thanks, I guess. I was thinking you might say something like that, like a chef praising a new ingredient."
            "She crosses her arms, trying to maintain a tough exterior, like a pastry chef protecting a delicate tart."
        else:
            mc.name "Well, it's true. You look... stunning, like a perfectly crafted soufflé."
        the_person "Hmph. Maybe I'll invite you shopping one day, so you can tell me what else you want to see me in, like a chef picking out ingredients for a new dish."
        "She leans in slightly, a hint of flirtation in her voice, like a chef adding a dash of spice to a sauce."
        mc.name "I can think of a few things already... and I'm sure I'd enjoy seeing you in them, like a diner savoring a new flavor."
        the_person "I'm sure you would. So, what do you say? Want to take me out for a... culinary adventure and maybe we can discuss my wardrobe some more, like a chef and a food critic debating the merits of a new dish?"

    else:
        the_person "Thanks, I thought I looked pretty... appetizing in it too, like a perfectly ripe fruit."
        the_person "You want a better look, right? Here, how does it make my... derrière look, like a perfectly crafted pastry?"
        $ the_person.draw_person(position = "back_peek")
        $ mc.change_locked_clarity(10)
        the_person "Good, right? Like a perfectly balanced sauce?"
        mc.name "Fantastic. I wish I could get an even better look at it, like a chef inspecting a new ingredient."
        "[the_person.possessive_title!c] smiles and turns back to face you, like a chef presenting a new dish."
        $ the_person.draw_person()
        the_person "I'm sure you do. Take me out for a... culinary adventure and maybe we can work something out, like a chef and a diner negotiating the perfect meal."
    return

label foodie_flirt_response_mid1(the_person):
    $ mc.change_locked_clarity(10)
    the_person "Thanks, I do look... delectable in this outfit, like a perfectly plated dessert."
    if (the_person.has_skirt or the_person.has_dress) and not the_person.has_thigh_high_socks:
        mc.name "You could add a dash of spice with some high stockings, I would love to savor the sight."
        the_person "Oh, really? And why would you want to indulge in that? You're not going to get a... taste or anything, are you?"
        mc.name "Because it would look... exquisite on you, like a perfectly crafted sauce, and I would relish the view."

    mc.name "How about you and me go and... indulge in a culinary adventure sometime? Maybe a coffee or a dessert?"
    if the_person.has_significant_other:
        the_person "Sure, my [the_person.so_title] doesn't mind... as long as they're not around to witness how much... flavor we're going to add to the mix."
    else:
        the_person "Why not, I could use a... palate cleanser once in a while... and maybe someone to... season my life with a bit of excitement."
    the_person "Just let me know when, I would love to... indulge in the experience... and don't think I won't notice if you're trying to get a... glimpse of my legs under the table, like a chef sneaking a peek at a competitor's recipe."
    mc.name "I'll keep that in mind, and maybe we can discuss what else you want to... serve up in the future... or not serve up, like a chef deciding on the perfect menu."
    the_person "Hmph, maybe. But don't think you're getting a... discount on my wardrobe just because we're going out for coffee... or anything else, like a diner trying to negotiate a better price for a meal."
    return

label foodie_flirt_response_high(the_person):
    if mc.location.person_count > 1 and the_person.effective_sluttiness() < (25 - (5*the_person.opinion.public_sex)): # There are other people here, if she's not slutty she asks if you want to find somewhere quiet
        the_person "You're really... hungry for attention, huh? Fine, but not here... this isn't the right... flavor profile for a romantic encounter."
        "She glances around, like a chef inspecting the dining area, before giving you a sly smile, like a pastry chef sneaking a taste of a new dessert."
        menu:
            "Find somewhere more... intimate\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                mc.name "Then let's find somewhere that isn't here, somewhere with a more... exquisite ambiance."
                the_person "Hmph, eager much? Alright, let's go, but don't think you're getting the... full menu just yet."
                call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_foodie_flirt_response_high_2
                the_person "So... Now what's your... recipe for romance?"

                if the_person.is_willing(kissing):
                    $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
                    if the_person.has_taboo("kissing"):
                        "You lean in close to kiss [the_person.title], like a chef adding the final touches to a dish."
                        $ the_person.call_dialogue("kissing_taboo_break")
                        $ the_person.break_taboo("kissing")
                        "She responds passionately, her arms wrapping around your neck like a perfectly crafted sauce."
                    else:
                        "You step close to [the_person.title] and put your arm around her waist, pulling her close and kissing her, like a chef presenting a new dish."
                        "She responds immediately and eagerly presses her body against yours, like a perfectly balanced flavor profile."
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _vt_foodie_call_fuck_person_49
                else:
                    if the_person.has_taboo("touching_body"):
                        $ the_person.call_dialogue("touching_body_taboo_break")
                        $ the_person.break_taboo("touching_body")
                        "You take her hand and pull her close against you, like a chef adding a dash of spice to a sauce. She looks into your eyes, like a diner savoring a new flavor."
                    else:
                        "You take her hand and pull her close, your lips brushing against her ear, like a chef whispering a secret ingredient to a colleague."
                    call fuck_person(the_person, private = True, start_position = standing_grope, skip_intro = True) from _call_fuck_person_foodie_flirt_grope

                $ the_person.call_dialogue("sex_review", the_report = _return)
                call mc_restore_original_location(the_person) from _call_mc_restore_original_location_foodie_flirt_response_high_2

            "Just flirt":
                mc.name "You know you want to, come on. I'll take you out for... dinner, and then we can see where the night takes us, like a chef experimenting with new ingredients."
                the_person "Hmm, you're really trying to... season the conversation with charm, aren't you? Well, I'll tell you what... If you can make me laugh, I might consider it, like a diner trying a new restaurant."
                "She smiles mischievously, clearly enjoying the challenge, like a chef trying to perfect a new recipe."

    else:
        if mc.location.person_count == 1: #You're alone, so she just didn't meet the sluttiness threshold
            the_person "Hmm, you're really... eager, aren't you? Well, I suppose it's just the two of us here, like a private dining experience..."
            "[the_person.possessive_title!c] glances around, confirming you're alone, like a chef inspecting the kitchen."
            the_person "So what's your... recipe for romance?"

        else:  # You aren't alone but she's still into it.
            the_person "Feeling... adventurous today, huh? Well, I think your chances are pretty good, like a chef trying a new ingredient..."
            "[the_person.title] smirks, clearly enjoying the attention, like a diner savoring a new flavor."
            if the_person.has_large_tits: #Bounces her tits for you
                $ mc.change_locked_clarity(15)
                "[the_person.title] grabs her tits and jiggles them for you, like a pastry chef decorating a cake."
                the_person "Maybe I can get these... girls out for you, like a chef presenting a new dessert. Does that sound... appetizing?"

            else: #No big tits, so she can't bounce them (as much)
                "[the_person.title] runs her hands over her hips sensually, obviously encouraging you to take things further, like a chef adding a dash of spice to a sauce."

        menu:
            "Touch her" if not the_person.is_willing(kissing):
                "You step closer to [the_person.title] and move your hands down her waist, like a chef adding a dash of spice to a sauce."
                if the_person.has_taboo("touching_body"):
                    the_person "Oh, you're... bold. I like that, like a diner trying a new restaurant."
                    $ the_person.call_dialogue("touching_body_taboo_break")
                    $ the_person.break_taboo("touching_body")

                call fuck_person(the_person, start_position = standing_grope, private = False) from _call_fuck_person_flirt_response_foodie_touching

            "Kiss her" if the_person.is_willing(kissing):
                $ the_person.draw_person()
                if the_person.has_taboo("kissing"):
                    "You put your arm around [the_person.possessive_title] and lean in close, like a chef adding the final touches to a dish."
                    $ the_person.call_dialogue("kissing_taboo_break")
                    $ the_person.break_taboo("kissing")
                    "She responds with a passionate kiss, her arms wrapping around your neck like a perfectly crafted sauce."
                else:
                    "You pull [the_person.possessive_title!] close and kiss her, like a chef presenting a new dish."
                    "She responds with a passionate kiss, her arms wrapping around your neck like a perfectly balanced flavor profile."

                call mc_move_to_private_location(the_person) from  _call_mc_move_to_private_location_foodie_flirt_response_high
                call fuck_person(the_person, start_position = kissing, private = _return, skip_intro = True) from _vt_foodie_call_fuck_person_50
                $ the_person.call_dialogue("sex_review", the_report = _return)
                call mc_restore_original_location(the_person) from _call_mc_restore_original_location_foodie_flirt_response_high

            "Just flirt":
                $ the_person.draw_person()
                mc.name "Very tempting, but you're going to have to... simmer down for now, like a sauce that needs to reduce."
                the_person "Oh, you're not going to take advantage of me right now, are you? Fine, be that way, like a chef who's just been told to remake a dish."
                "[the_person.title] pouts, clearly enjoying the flirtation, like a diner who's just been served a new dessert."
    return

label foodie_flirt_response_low_energy(the_person):
    if the_person.sluttiness > 40:
        the_person "Ugh, thanks for the... culinary compliment, but I'm feeling a bit... stale right now."
    else:
        the_person "Thanks, but I'm... exhausted. Can we pick this up later, like a dessert that's been left in the oven too long?"
    return

label foodie_flirt_response_girlfriend(the_person):
    # Lead in: mc.name "You're so... delectable [the_person.title], I'm so lucky to have a woman like you in my life, like a perfectly crafted dish."
    if mc.location.person_count > 1:
        # There are other people around, so she'll only start making out with you if she's slutty.
        if the_person.effective_sluttiness("kissing") < (25 - (5*the_person.opinion.public_sex)):
            # Not very slutty, so she wants to find somewhere private
            the_person "Oh mon dieu, you're so... cheesy, like a rich dessert. Come here."
            "She pulls you against her and kisses you, her lips soft and gentle, like a perfectly baked croissant."
            the_person "There, now you can't say I don't know how to... season a kiss."
            mc.name "Haha, yeah I guess not... you're a true... culinary artist."
            "You put your arms around her and kiss her back, feeling her warmth, like a perfectly balanced sauce."
            the_person "Mmm, yeah, like that, a perfect... flavor combination."
            menu:
                "Find somewhere more... intimate\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                    mc.name "Why wait? Come on, I'm sure we can find somewhere... quiet, like a secluded dining area."
                    the_person "You're always so... eager, aren't you? Alright, let's go, like a chef rushing to prepare a new dish!"
                    "You and [the_person.possessive_title] hurry off, searching for a private spot, like a food critic searching for the perfect restaurant."
                    call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_foodie_flirt_response_girlfriend_2
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _vt_foodie_call_fuck_person_76
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_foodie_flirt_response_girlfriend_2

                "Just flirt":
                    $ mc.change_locked_clarity(10)
                    "You reach around and pull her closer, running your hand down her back, like a chef adding a dash of spice to a sauce."
                    mc.name "You're so... delectable, and you know it, like a perfectly crafted dessert."
                    "She rolls her eyes but leans in for a quick kiss, like a diner savoring a new flavor."
                    the_person "Fine, you caught me. But don't think this means I'm going easy on you, like a chef who's just been challenged to a cook-off."

        else:
            the_person "Well if I'm so... delectable, then why are you just standing there? Come on, kiss me, like a chef presenting a new dish!"
            "You put your arm around her waist and pull her close, kissing her deeply, like a perfectly balanced sauce."
            "When you break the kiss, [the_person.possessive_title] sighs and leans against you, like a diner who's just been served a perfect meal."
            the_person "You're not so bad yourself, like a perfectly crafted side dish..."
            menu:
                "Make out":
                    "You lean back in and kiss her again, this time more passionately, like a chef adding a dash of spice to a sauce."
                    "[the_person.title] responds eagerly, wrapping her arms around your neck, like a diner who's just discovered a new favorite restaurant."

                    call mc_move_to_private_location(the_person) from  _call_mc_move_to_private_location_foodie_flirt_response_girlfriend
                    call fuck_person(the_person, start_position = kissing, private = _return, skip_intro = True) from _vt_foodie_call_fuck_person_77
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_foodie_flirt_response_girlfriend

                "Just flirt":
                    mc.name "I'm not bad? You're the one who's... hard to resist, like a perfectly crafted dessert."
                    $ mc.change_locked_clarity(10)
                    "You reach out and touch her cheek, a playful grin on your face, like a chef who's just been praised by a food critic."
                    the_person "Ugh, you're so... annoying, like a diner who's just been served a dish they didn't order. But I guess I like that about you, like a chef who's just discovered a new ingredient..."

    else:
        # You're alone, so she's open to fooling around.
        the_person "Well you've got me all alone, so how about you show me just how... lucky you feel, like a chef who's just been given a new ingredient to work with?"
        "She reaches down to your waist and cups your crotch, rubbing it gently, like a pastry chef kneading dough."
        mc.name "You're so... wet for me already, like a perfectly ripe fruit."
        the_person "Hmph, maybe, like a chef who's just been challenged to create a new dish."
        "She grinds against you, her hips moving in a slow circle, like a perfectly balanced sauce."
        mc.name "Damn, you feel so... good, like a perfectly crafted dessert."
        "You reach up and grab her breasts, squeezing them gently, like a chef who's just been given a new ingredient to work with."
        the_person "Ooh, don't do that, like a diner who's just been served a dish they didn't order."
        "But she doesn't pull away, her body still pressed against yours, like a perfectly balanced flavor profile."
        menu:
            "Kiss her":
                if the_person.has_taboo("kissing"):
                    $ the_person.call_dialogue("kissing_taboo_break")
                    $ the_person.break_taboo("kissing")

                "You put your arms around [the_person.possessive_title]'s waist and rest your hands on her ass, like a chef who's just been given a new ingredient to work with. You pull her close and kiss her sensually, like a perfectly crafted sauce."
                "She responds by pressing her body against you and grinding her hips against your thigh, like a perfectly balanced flavor profile."
                "You grab her hips and pull her closer, your crotches pressed together, like a perfectly crafted dessert."
                call fuck_person(the_person, start_position = kissing, skip_intro = True) from _vt_foodie_call_fuck_person_78
                $ the_person.call_dialogue("sex_review", the_report = _return)
                $ the_person.review_outfit()

            "Just flirt":
                mc.name "I'm going to make you... beg for it, like a chef who's just been challenged to create a new dish."
                "You lean in close, your breath hot against her ear, like a perfectly balanced sauce."
                the_person "Ooh, you're such a... bad boy, like a diner who's just been served a dish they didn't order. I love it, like a chef who's just discovered a new ingredient."
                "She rubs her body against yours, her hips moving seductively, like a perfectly crafted dessert."
                the_person "But don't think you're getting off that easy, like a chef who's just been told to remake a dish. I'm going to make you... work for it, like a diner who's just been served a new restaurant."
    return

label foodie_flirt_response_affair(the_person):
    # Lead in: mc.name "You look so... delectable today [the_person.title], you're making me want to indulge in some very naughty things with you, like a chef who's just discovered a new ingredient."
    if mc.location.person_count > 1: #There are other people around, she's nervous about people finding out what you're doing.
        if (the_person.opinion.cheating_on_men *15) + the_person.effective_sluttiness() > 50: #SHe's turned on by flirting in public or doesn't think anything is wrong with it
            "[the_person.possessive_title!c] blushes and playfully bats her eyes at you, like a pastry chef decorating a cake."
            the_person "Oh, you're making me blush, like a perfectly ripe fruit. I'm not used to this kind of... attention from you, like a diner who's just discovered a new restaurant."
            the_person "But I have to admit, I'm curious. What do you have in mind, like a chef who's just been given a new ingredient to work with?"
            menu:
                "Find somewhere more... intimate\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                    mc.name "I was thinking we could slip away and find a more... secluded spot, like a private dining room."
                    "You and [the_person.title] exchange a flirtatious glance, like a chef and a diner sharing a secret, before hurrying off to find a quiet spot."
                    call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_foodie_flirt_response_affair
                    $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
                    "As soon as you're alone she pulls you into a deep and passionate kiss, like a perfectly balanced sauce."
                    $ the_person.draw_person(position = "kissing")
                    the_person "Mmm... I've been wanting to do that for a while now, like a chef who's just discovered a new flavor combination."
                    "You wrap your arms around her waist and kiss her back, like a diner savoring a new dish."
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _vt_foodie_call_fuck_person_79
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_foodie_flirt_response_affair

                "Just flirt":
                    mc.name "I couldn't help but notice how... delectable you look today, [the_person.title], like a perfectly crafted dessert."
                    the_person "Stop it, you're making me blush, like a perfectly ripe fruit! But I have to admit, you look pretty... appetizing yourself, like a perfectly seasoned dish."
                    the_person "Just don't get too... cocky, okay? I'm still in charge here, like a chef who's just been given a new kitchen to run."
                    $ mc.change_locked_clarity(20)
                    "[the_person.possessive_title!c] playfully swats at your arm, like a pastry chef teasing a colleague, before leaning in close."
                    the_person "But I have to admit, I'm getting a little... turned on by this whole thing, like a diner who's just discovered a new favorite restaurant."
                    "You can't help but feel a little... flustered as she teases you, like a chef who's just been challenged to a cook-off."
                    mc.name "I can see that. Maybe we should find a more... private place to continue this, like a secluded dining room."
                    the_person "Mmm, maybe we should. But first, let's enjoy this little moment here, like a diner savoring a new dish."

        else: #She's shy or nervous about being discovered
            "[the_person.possessive_title!c] looks around nervously, like a chef who's just been told to remake a dish, then back at you with a sheepish grin, like a pastry chef who's just made a mistake."
            the_person "Oh, um, you look... nice today, like a perfectly crafted sauce. I guess I should probably get going though, like a diner who's just finished a meal..."
            mc.name "Wait, don't go! I was thinking we could... uh, grab a drink or something, like a chef who's just been given a new ingredient to work with?"
            $ mc.change_locked_clarity(15)
            the_person "Oh, you want to grab a drink? Okay, sure, like a diner who's just ordered a new dish. But just for a little bit, okay? I don't want to be out too late, like a chef who's just been told to close up the kitchen."
            "She glances around again, like a chef who's just been told to remake a dish, then leans in close and whispers, like a pastry chef sharing a secret."
            the_person "And just so you know, I'm still in charge here, even if we're just grabbing a drink, like a chef who's just been given a new kitchen to run."
            "You can't help but feel a little... excited by her assertiveness, like a diner who's just discovered a new favorite restaurant."
            mc.name "Okay, okay. I'll behave, like a chef who's just been told to follow a recipe."

    else:
        # the_person "Yeah? Well there's nobody around, and I'm not going to stop you, like a chef who's just been given a new ingredient to work with."
        the_person "Oh yeah? Well then, do you want to share what all of these... naughty things are, like a chef who's just discovered a new flavor combination? You have my attention, like a diner who's just been served a new dish."
        menu:
            "Feel her up":
                "You put your arms around [the_person.possessive_title]'s waist and rest your hands on her ass, like a chef who's just been given a new ingredient to work with."
                mc.name "You know, I've been waiting for this moment for a while now, like a chef who's just been given a new kitchen to run."
                "You massage her butt, like a pastry chef kneading dough. She blushes and pushes you away lightly, like a diner who's just been served a dish they didn't order."
                the_person "Hey, no need to be so... forward, like a chef who's just been told to remake a dish! What's gotten into you, like a diner who's just discovered a new favorite restaurant?"
                "You pull her close again and shift your hands to her breasts, squeezing them gently, like a chef who's just been given a new ingredient to work with."
                mc.name "Come on, don't be like that, like a chef who's just been told to follow a recipe. I just wanted to make you feel... good for once, like a diner who's just been served a perfect meal."
                call fuck_person(the_person, private = True, start_position = standing_grope, skip_intro = True) from _vt_foodie_call_fuck_person_80
                $ the_person.call_dialogue("sex_review", the_report = _return)
                $ the_person.review_outfit()

            "Just flirt":
                $ mc.change_locked_clarity(10)
                "You put your arms around [the_person.possessive_title]'s waist and rest your hands on her ass, like a chef who's just been given a new ingredient to work with."
                mc.name "I wish I had the time, like a chef who's just been told to close up the kitchen. You'll have to wait until later, like a diner who's just been told to come back tomorrow."
                "You massage her butt, like a pastry chef kneading dough. She sighs happily and leans her weight against you, like a diner who's just been served a perfect meal."
                the_person "Aww, are you sure, like a chef who's just been told to remake a dish?"
                "You slap her ass and step back, like a chef who's just been told to follow a recipe. She clings to you reluctantly before letting go, like a diner who's just finished a meal."
                the_person "Fine, but don't make me wait too long, okay, like a chef who's just been told to prepare a new dish?"
                the_person "I have... needs, and my [the_person.so_title] sure as hell isn't fulfilling them, like a diner who's just been served a dish they didn't order."
                mc.name "I won't make you wait long, like a chef who's just been told to prepare a new dish. I promise, like a pastry chef who's just been given a new ingredient to work with."
                "She looks up at you with a playful pout, like a diner who's just been served a dish they didn't order."
                the_person "Promise you won't make me wait, like a chef who's just been told to follow a recipe?"
                mc.name "I promise, baby, like a pastry chef who's just been given a new ingredient to work with."
                "You both share a flirtatious smile, like a chef and a diner who've just discovered a new favorite restaurant."
                the_person "Good, like a chef who's just been told to prepare a new dish. Because I'm not sure I can handle it if you do, like a diner who's just been served a dish they didn't order."
    return

label foodie_flirt_response_text(the_person):
    mc.name "Hey [the_person.title], how's it going? I'm feeling a bit... stale and thought we could... spice things up with a chat."
    "She replies with a hint of... annoyance, like a chef who's just been told to remake a dish."
    if the_person.is_affair:
        the_person "Oh, great, you're... bored again? You always seem to find ways to... season the conversation with drama."
        the_person "Well, what do you want this time? I'm not exactly... hungry for your attention."
        the_person "When can we get together and... savor the moment?"
        mc.name "Some time soon. I'll let you know, like a chef who's just been given a new ingredient to work with."

    elif the_person.is_girlfriend:
        the_person "Bored, huh? That's not exactly a... surprise, like a diner who's just been served a dish they've had before. You're always looking for something new to... flavor the conversation."
        the_person "But fine, we can hang out and... indulge in some quality time. Just don't expect me to... whip up something special."
        mc.name "Some time soon. I'll let you know, like a chef who's just been given a new recipe to try."

    elif the_person.love < 40:
        if the_person.effective_sluttiness() > the_person.love:
            the_person "Ugh, bored, really? Well, I suppose I can... keep you company for a bit, like a pastry chef who's just been given a new dessert to create."
        else:
            the_person "Bored, eh? That's not surprising, like a diner who's just been served a dish they've had before. You're always looking for a new... distraction, like a chef who's just been given a new ingredient to work with."

    else:
        if the_person.effective_sluttiness() > the_person.love:
            the_person "Fine, I'll talk to you. But don't think this means I'm... happy about it, like a chef who's just been told to remake a dish."
            the_person "So, what do you want to talk about? I'm not exactly... thrilled about this, like a diner who's just been served a dish they didn't order."
        else:
            the_person "You're bored, huh? Well, that's your... problem, not mine, like a chef who's just been given a new recipe to try."
            the_person "So, what do you want? Just don't expect me to be all... lovey-dovey about it, like a pastry chef who's just been given a new dessert to create."
    return

label foodie_condom_demand(the_person):
    if the_person.wants_creampie:
        the_person "Ugh, seriously? You need to... wrap it up before we even think about doing anything, like a chef who's just been told to follow a recipe."
        the_person "I hate that we have to, but you know it's... necessary, like a diner who's just been served a dish they didn't order."
    else:
        the_person "For crying out loud, do you have a... condom on you? Put one on before you even think about touching me, like a chef who's just been given a new ingredient to work with."
        the_person "I don't want to be stuck with some... stupid disease because you were too... careless, like a diner who's just been served a dish they didn't order."
    return

label foodie_condom_ask(the_person):
    if the_person.on_birth_control:
        the_person "You want a... condom? Fine, but I'm on the... pill, so it's not like I really need it, like a chef who's just been given a new ingredient to work with."
        $ the_person.update_birth_control_knowledge()
    elif the_person.wants_creampie:
        the_person "Ugh, you want to... cum inside me? Just put on a... condom, would you? It's not like I want to get... pregnant or anything, like a diner who's just been served a dish they didn't order."
        the_person "But I guess it's better than the... alternative, right, like a chef who's just been given a new recipe to try?"
        $ the_person.discover_opinion("creampies")
    else:
        the_person "Fine, I guess you should use a... condom...but can you at least not make a... mess with it? I don't want to... clean up after you, like a pastry chef who's just been given a new dessert to create."
        the_person "And please, no... pulling out method. That's just... asking for trouble, like a chef who's just been told to remake a dish."
    return

label foodie_condom_bareback_ask(the_person):
    if the_person.wants_creampie:
        if the_person.is_infertile:
            the_person "You're not seriously considering a... condiment, are you? Please, just give me your hot, sticky... sauce, like a chef who's just been given a new ingredient to work with."
            the_person "I want to feel you fill me up and make me scream with... pleasure, like a diner who's just been served a perfect meal."
        elif the_person.on_birth_control:
            the_person "Don't even think about putting a... wrapper on, [the_person.mc_title]. I'm on the... pill, so we're good to go, like a chef who's just been given a new recipe to try."
            the_person "Just... indulge in me raw and make me feel every... inch of you, like a pastry chef who's just been given a new dessert to create."
            $ the_person.update_birth_control_knowledge()
        else:
            the_person "Forget the... condiment, [the_person.mc_title], I want to feel you deep inside me, like a diner who's just been served a new dish."
            the_person "I don't care about the... risks, it's worth it for this kind of... pleasure, like a chef who's just been given a new ingredient to work with."
            if not the_person.knows_pregnant:
                the_person "Imagine how... decadent it would be to get... knocked up, too, like a pastry chef who's just been given a new dessert to create."
        $ the_person.discover_opinion("creampies")
    else:
        the_person "Don't bother with a... condiment, [the_person.mc_title]. I want to feel you raw and... unprotected, like a chef who's just been given a new ingredient to work with."
        if not the_person.knows_pregnant:
            the_person "I don't care about the... risks, it's worth it for the... intensity, like a diner who's just been served a new dish."
        else:
            the_person "I love it when you... indulge in me raw and make me feel like I'm yours, like a pastry chef who's just been given a new dessert to create."
    return

label foodie_condom_bareback_demand(the_person):
    if the_person.has_breeding_fetish: #Actively looking to get knocked up.
        if the_person.knows_pregnant:
            the_person "Ugh, why bother with a... condiment? I want to get... pregnant, so... indulge in me raw, like a chef who's just been given a new ingredient to work with!"
            the_person "Hurry up, I'm... starving for your... attention, like a diner who's just been served a new dish."
        elif the_person.is_infertile:
            the_person "Oh, great, you're going to remind me I'm... barren? Thanks a lot, like a chef who's just been told to remake a dish."
        else:
            the_person "Ugh, what's the point of... indulging if you're not going to... knock me up, like a pastry chef who's just been given a new dessert to create?"
            the_person "Hurry up and give me that... sauce, like a chef who's just been given a new ingredient to work with!"
    elif the_person.wants_creampie: #Just likes raw sex
        if the_person.is_infertile:
            the_person "Ugh, why bother with a... condiment? I'm... barren anyway, like a chef who's just been told to remake a dish."
        elif the_person.on_birth_control:
            the_person "Forget the... condiment, [the_person.mc_title]. I'm on the... pill, so it's not a problem, like a chef who's just been given a new recipe to try."
            the_person "Take me... bareback and make me... scream, like a pastry chef who's just been given a new dessert to create."
            $ the_person.update_birth_control_knowledge()
        else:
            the_person "Ugh,... condiments are so... annoying, like a chef who's just been told to remake a dish. Just get inside me already, like a diner who's just been served a new dish!"
    else:
        if the_person.is_infertile:
            the_person "Take me... bareback, [the_person.mc_title]. It's not like I can get... pregnant, like a chef who's just been given a new ingredient to work with."
            the_person "Just make me... feel good, like a diner who's just been served a perfect meal."
        elif the_person.on_birth_control:
            the_person "Forget the... condiment, [the_person.mc_title]. I'm on the... pill, like a chef who's just been given a new recipe to try."
            the_person "Take me... bareback and make me feel every... inch of you, like a pastry chef who's just been given a new dessert to create."
            $ the_person.update_birth_control_knowledge()
        else:
            the_person "Ugh,... condiments are so... annoying, like a chef who's just been told to remake a dish. Just get inside me already, like a diner who's just been served a new dish!"
            the_person "I need to feel you deep inside me, like a pastry chef who's just been given a new dessert to create."
    return

label foodie_cum_face(the_person):
    if the_person.has_cum_fetish or the_person.obedience > 180:
        if the_person.has_cum_fetish or the_person.effective_sluttiness() > 60 or the_person.opinion.cum_facials > 0:
            the_person "So, do you think this is a... delectable look for me, [the_person.mc_title]?"
            "[the_person.title] smirks, then licks her lips and runs a finger through your semen, bringing it to her mouth like a chef savoring a new flavor."
            the_person "Mmm, taste your... victory, like a perfectly crafted dessert."
        else:
            the_person "Hmph, I suppose it's not a... terrible presentation. But I'm glad we're done here, like a diner who's just finished a meal."
            "[the_person.title] wipes away some of your semen from her face, looking annoyed, like a chef who's just been told to remake a dish."

    else:
        if the_person.effective_sluttiness() > 80 or the_person.opinion.cum_facials > 0:
            the_person "Well, I guess this is one way to... season the evening. Do you think I look... appetizing like this?"
            "[the_person.title] smirks, then laughs and wipes away some of your semen from her face, like a pastry chef who's just been given a new dessert to create."
        else:
            the_person "Ugh, just get that over with already, like a chef who's just been told to close up the kitchen. And don't think you're getting a second chance, like a diner who's just been served a dish they didn't order."
            "[the_person.title] wipes away your semen, looking put off, like a chef who's just been told to remake a dish."
    return

label foodie_cum_mouth(the_person):
    if the_person.has_cum_fetish or the_person.obedience > 180:
        if the_person.has_cum_fetish or the_person.effective_sluttiness() > 60 or the_person.opinion.drinking_cum > 0:
            the_person "Mmm, that's so... satisfying, like a perfectly crafted sauce, [the_person.mc_title]."
            the_person "You really know how to... season the moment and make me feel good, like a chef who's just been given a new ingredient to work with."
        else:
            "[the_person.title]'s face twists in disgust, like a diner who's just been served a dish they didn't order, as she swallows your cum."
            the_person "Ugh, there, done, like a chef who's just been told to remake a dish. Don't think I enjoyed that one bit, like a pastry chef who's just been given a new dessert to create."

    else:
        if the_person.effective_sluttiness() > 80  or the_person.opinion.drinking_cum > 0:
            the_person "Mmm, you're quite the... connoisseur, [the_person.mc_title], like a chef who's just been given a new ingredient to work with."
            the_person "I can see why you're so... popular, like a diner who's just discovered a new favorite restaurant."
        else:
            the_person "Ugh, that's... quite a... flavor, like a chef who's just been given a new ingredient to work with. I hope you're... satisfied, like a diner who's just finished a meal."
    return

label foodie_cum_pullout(the_person):
    # Lead in: "I'm going to... serve up a delicious creampie!"
    if mc.condom:
        if the_person.wants_creampie and not the_person.has_taboo("condomless_sex"): #TODO: FIgure out we want any more requirements for this to fire.
            if the_person.knows_pregnant:
                the_person "Oh, don't bother with the... wrapper, just cum inside me and make me... pregnant, like a perfectly crafted dessert!"
                the_person "I don't care about the... calories right now, I just want your... sauce filling me up, like a diner who's just been served a perfect meal!"
            elif the_person.on_birth_control:
                the_person "Oh... mon dieu... I'm so... hungry, take that... wrapper off [the_person.mc_title]!"
                "She moans... desperately, like a diner who's just been served a dish they can't resist."
                the_person "I give in, I want you to cum inside me, like a chef who's just been given a new ingredient to work with!"
            else:
                "She moans... desperately, like a diner who's just been served a dish they can't resist."
                the_person "I'm so... famished, just take off the... wrapper and cum inside me, like a chef who's just been given a new recipe to try!"
                $ the_person.update_birth_control_knowledge()
                the_person "I want you to make me cum and then make me... pregnant, you dirty... chef, like a diner who's just been served a perfect meal!"
            menu: #TODO: Add a variant of this normally so you can stealth a girl (don't do that in real life, it's super fucked up).
                "Take off the... wrapper":
                    "You pull out, barely clearing her... plate, and pull the... wrapper off as quickly as you can manage, like a chef who's just been given a new ingredient to work with."
                    $ mc.condom = False
                    $ use_condom = False  # prevent putting on a new... wrapper next sex loop
                "Leave it on":
                    "You ignore [the_person.possessive_title]'s request and keep the... wrapper in place, like a chef who's just been told to follow a recipe."
        else:
            the_person "Fuck yeah, I'm going to make you... cum, like a chef who's just been given a new ingredient to work with!"
    else:
        if the_person.wants_creampie:
            if the_person.knows_pregnant: #She's already... full, so who cares!
                the_person "Creampie me, you dirty... chef, and make me cum, like a diner who's just been served a perfect meal!"
            elif the_person.opinion.creampies > 0:
                "[the_person.possessive_title!c] moans... happily, like a diner who's just been served a dish they love."
                if the_person.on_birth_control: #She just likes... creampies.
                    the_person "Fuck yeah, fill me up with your... sauce [the_person.mc_title]! Creampie me, like a chef who's just been given a new ingredient to work with!"
                else: #Yeah, she's not on... BC and asking for you to creampie her. She's looking to get... pregnant.
                    $ the_person.update_birth_control_knowledge()
                    the_person "Oh... mon dieu, cum inside me and... knock me up [the_person.mc_title]! I want you to... breed me like a dirty... slut, like a chef who's just been given a new recipe to try!"
            elif the_person.is_infertile:
                the_person "Cum wherever you want, you dirty... chef, I'm... barren, like a diner who's just been served a dish they can't eat."
            elif the_person.on_birth_control: #She's on the... pill, so she's probably fine
                $ the_person.update_birth_control_knowledge()
                the_person "Cum wherever you want, you dirty... chef, I'm on the... pill, like a chef who's just been given a new ingredient to work with!"
            else: #Too distracted to care about getting... pregnant or not. Oh well, what could go wrong?
                the_person "Do it! Cum, like a chef who's just been given a new recipe to try!"
        else:
            if the_person.is_infertile:
                the_person "Just pull out, I don't want your... sauce inside me, you dirty... chef, like a diner who's just been served a dish they don't like!"
            elif not the_person.on_birth_control: #You need to pull out, I'm not on the... pill!
                $ the_person.update_birth_control_knowledge()
                the_person "Fuck, pull out, you dirty... chef! I'm not on the... pill, like a chef who's just been told to remake a dish!"
            elif the_person.opinion.creampies < 0:
                the_person "Pull out, I don't want you to cum in me, you dirty... chef, like a diner who's just been served a dish they don't like!"
            else:
                the_person "Hell yeah, pull out and cum all over me like a dirty... slut, like a chef who's just been given a new ingredient to work with!"
    return

label foodie_cum_condom(the_person):
    if the_person.effective_sluttiness() > 75 or the_person.opinion.creampies > 0:
        the_person "Oh mon dieu, it feels so... decadent. If your condom broke it would be inside me, and I'd be... pregnant, like a perfectly crafted dessert."
    else:
        the_person "Oh mon dieu, I hope you buy good... condiments because that's a lot of... sauce."
        the_person "But then again, maybe you're dreaming of... knocking me up and getting me... pregnant, like a chef who's just been given a new ingredient to work with."
    return

label foodie_cum_vagina(the_person):
    if the_person.has_taboo("creampie"):
        $ the_person.call_dialogue("creampie_taboo_break")
        $ the_person.break_taboo("creampie")
        return
    if the_person.wants_creampie:
        if the_person.knows_pregnant:
            the_person "Ugh, fine... I guess I can admit it now, but only because I'm already... full from your other, uh, impressive... dishes... Your... sauce just feels so good inside me, like a perfectly crafted dessert!"
        elif the_person.is_infertile:
            the_person "Oh, stop being so dramatic! Of course you're not going to get me... pregnant, I'm... barren, remember? But seriously, your... sauce is pretty great... just don't expect me to admit it to anyone else, like a chef who's just been given a new ingredient to work with!"
        elif the_person.on_birth_control:
            if the_person.has_significant_other:
                the_person "Well, well, well... Look at you go! I guess it's a good thing I'm on the... pill, huh? Or maybe I'll just tell [the_person.so_name] that it was someone else's... Ugh, why do you have to be so... frustrating, like a chef who's just been told to remake a dish?"
            else:
                if the_person.knows_pregnant:
                    the_person "Oh mon dieu that's a lot of... sauce. Good thing I'm already... pregnant, because I don't think you're firing blanks, like a chef who's just been given a new ingredient to work with."
                elif the_person.is_infertile:
                    the_person "Oh mon dieu that's a lot of... sauce. I will be dripping your... sauce all day long, like a pastry chef who's just been given a new dessert to create."
                else:
                    the_person "Oh mon dieu that's a lot of... sauce. Good thing I'm on the... pill, because I don't think you're firing blanks, like a chef who's just been given a new ingredient to work with."
                $ the_person.update_birth_control_knowledge()
        elif the_person.effective_sluttiness() > 75 or the_person.opinion.creampies > 0:
            if the_person.has_significant_other:
                the_person "Okay, okay, I get it! You're great in... bed, but don't think I'm going to start flaunting our little secret around my [the_person.so_title]... At least, not until I figure out how to explain it, like a chef who's just been given a new recipe to try."
            else:
                the_person "Ugh, fine... I'll admit it, you're pretty... amazing when you're like this... But don't think this means I'm going to start begging for more! I just need to... savor this moment, okay, like a diner who's just been served a perfect meal?"
        else:
            if the_person.has_significant_other:
                the_person "You really know how to make a girl feel... special, don't you? But let's keep this between us, okay? I don't think [the_person.so_name] would understand, like a chef who's just been told to keep a secret ingredient secret."
            else:
                the_person "Wow... I guess I didn't expect that from you. But I have to admit, it was kind of... nice... Just don't get any ideas, okay? I'm not ready for anything... serious, like a diner who's just been served a dish they didn't order."
    else: #She's angry
        if the_person.knows_pregnant:
            the_person "Ugh, what is wrong with you? I specifically told you not to do that! Oh well, since I'm already... pregnant, like a chef who's just been given a new ingredient to work with..."
        elif not the_person.on_birth_control:
            if the_person.has_significant_other:
                the_person "Oh mon dieu, just what I needed. You forgot to... pull out, and now I'm going to have to deal with [the_person.so_name]'s... anger, like a chef who's just been told to remake a dish."
                if the_person.kids > 0:
                    the_person "... Again, like a diner who's just been served a dish they've had before."
            else:
                the_person "Oh mon dieu, I said to... pull out! I'm not on the... pill [the_person.mc_title], what happens if I get... pregnant, like a chef who's just been given a new ingredient to work with?"
                $ the_person.update_birth_control_knowledge()
                the_person "What is wrong with you? You know I'm not on the... pill! Now look what you've done... I guess next time we'll have to use a... condiment, like a chef who's just been told to follow a recipe."
        elif the_person.is_infertile:
            the_person "Unbelievable! I told you to... pull out, and now you've gone and made a... mess, like a pastry chef who's just made a mistake... What a pain in the... kitchen!"
        elif the_person.has_significant_other:
            the_person "You're really going to make me tell [the_person.so_name] about this, aren't you? Fine, I'll deal with it. Just be more... careful next time, like a chef who's just been told to follow a recipe."
            $ the_person.update_birth_control_knowledge()
            the_person "I don't want to have to make you wear a... condiment, so be a little more... careful next time, like a chef who's just been given a new ingredient to work with."
        elif the_person.opinion.creampies < 0:
            the_person "Oh mon dieu, just what I needed. You couldn't even follow a simple... recipe, could you? Now look at what a... mess you've made, like a pastry chef who's just made a mistake..."
        else:
            the_person "You really need to work on your... timing. I told you to... pull out, not do the exact opposite, like a chef who's just been told to remake a dish!"
            the_person "Just remember, I'm not going to be as... forgiving next time if you can't follow simple... instructions, like a chef who's just been given a new recipe to try."
    return

label foodie_cum_anal(the_person):
    if the_person.has_taboo("anal creampie"):
        $ the_person.call_dialogue("anal_creampie_taboo_break")
        $ the_person.break_taboo("anal creampie")
        return

    if the_person.sluttiness > 75 or the_person.opinion.anal_creampies > 0:
        the_person "Ugh, fine... I guess it's okay if you... serve me up a creampie... But don't think I'm going to start asking for it all the time, like a diner who's just been served a dish they love!"
    elif the_person.opinion.anal_creampies < 0:
        the_person "Oh, come on... not in there! I don't need to be... seasoned like that, it's too... embarrassing!"
    else:
        the_person "Oh, alright... if you insist... But just this once, and don't think I'm going to start... savoring it or anything, like a chef who's just been given a new ingredient to work with..."
    return

label foodie_surprised_exclaim(the_person):
    $rando = renpy.random.choice(["Mon dieu!","What a... culinary catastrophe!","Ugh, really?","Why now?","This again?","Not again!", "Seriously?", "Great...", "Oh, joy...", "Fucking perfect...", "Unbelievable!", "Not again!", "Why can't I have a... normal recipe?"])
    the_person "[rando]"
    return

label foodie_talk_busy(the_person):
    if the_person.obedience > 120:
        the_person "Ugh, I don't have time for this, I've got way too many... dishes to attend to right now, [the_person.mc_title]."
    else:
        the_person "Listen, I'd love to catch up, but I'm... swamped with recipes to try. Maybe we can talk later, like a chef who's just been given a new ingredient to work with?"
    return

label foodie_sex_strip(the_person):
    if the_person.sluttiness < 20:
        if the_person.arousal_perc < 50:
            the_person "Ugh, fine. I'll take off some... layers, but don't think I'm doing this because I like you or anything. I just need to get... comfortable, that's all, like a diner who's just been served a dish they didn't order."
            mc.name "Come on, babe. It's just us here. You can... relax, like a chef who's just been given a new ingredient to work with."
            the_person "I don't care! I'm still not... comfortable. And don't call me 'babe'. That's... weird, like a pastry chef who's just made a mistake."
            mc.name "Okay, okay. I'll stop. Just take your time, okay, like a chef who's just been told to follow a recipe?"
        else:
            the_person "Alright, alright. I'll take off a few... garnishes, but don't expect me to be impressed by your reaction. I'm just taking off some... clothes, big deal, like a diner who's just been served a dish they've had before."
            mc.name "Aww, come on. You're being a little... rough, like a chef who's just been told to remake a dish. Just let me see you a little more, okay?"
            the_person "Fine, but only because you asked nicely. And don't think this means I like you or anything, like a pastry chef who's just been given a new dessert to create."
    elif the_person.sluttiness < 60:
        if the_person.arousal_perc < 50:
            the_person "Fine, I'll make an exception and get a little more... comfortable, like a diner who's just been served a dish they love. But don't get any ideas, okay?"
            mc.name "I promise, I won't get any ideas, like a chef who's just been given a new ingredient to work with. I just want to make sure you're... comfortable."
            the_person "Ugh, fine. But don't think I'm doing this for you, like a pastry chef who's just made a mistake. I just need to get a little more... comfortable."
            mc.name "I understand, like a chef who's just been told to follow a recipe. Just take your time and let me know if you need anything."
        else:
            the_person "Okay, okay. I'll take off a few more... layers if it'll make you happy, like a diner who's just been served a dish they love. But don't think I'm doing this because I'm into you or anything, like a pastry chef who's just been given a new dessert to create."
            mc.name "I know, I know, like a chef who's just been told to follow a recipe. You're just doing it because you want to, right?"
            the_person "Whatever, like a diner who's just been served a dish they didn't order. Just let me get this off and we can get on with this, like a chef who's just been given a new ingredient to work with. And don't think this means I'm going to start liking you or anything."
    else:
        if the_person.arousal_perc < 50:
            the_person "Ugh, fine, like a diner who's just been served a dish they didn't order. I'll do it, but just for you, I'll make an exception, like a chef who's just been given a new ingredient to work with. And don't think I'm doing this because I like you or anything."
            mc.name "Thanks, babe, like a pastry chef who's just been given a new dessert to create. You're making me really happy right now."
            the_person "Don't call me 'babe', like a diner who's just been served a dish they didn't order. And don't get too happy, like a chef who's just been told to remake a dish. I'm just doing this because I have to."
        else:
            the_person "Great, now let me get this off and we can get on with this, like a chef who's just been given a new ingredient to work with. I'm... starving over here, like a diner who's just been served a dish they love! But don't expect me to be all... happy about it or anything, like a pastry chef who's just made a mistake."
            mc.name "Aww, come on, like a chef who's just been told to follow a recipe. You're being a little... grumpy, like a diner who's just been served a dish they didn't order. Let's just have some... fun, okay?"
            the_person "Fine, like a diner who's just been served a dish they didn't order. But don't expect me to start... smiling and laughing or anything, like a pastry chef who's just been given a new dessert to create."
    return

label foodie_sex_watch(the_person, the_sex_person, the_position):
    $ title = the_person.title if not the_person.is_stranger else "The stranger"
    if the_person.sluttiness < the_position.slut_requirement - 20:
        $ the_person.draw_person(emotion = "angry", display_transform = character_left_flipped)
        the_person "Ugh, seriously? Can you two keep it down? I'm trying to... savor the moment, not be distracted by your... culinary exploits."
        $ the_person.change_stats(obedience = -2, happiness = -1)
        "[title] rolls her eyes and tries to ignore you and [the_sex_person.fname] [the_position.verb], like a diner who's just been served a dish they didn't order."
        return False
    if the_person.sluttiness < the_position.slut_requirement - 10:
        $ the_person.draw_person(display_transform = character_left_flipped)
        the_person "Honestly, you two are so... embarrassing. Can't you keep it a little more... private, like a chef who's just been told to remake a dish?"
        $ the_person.change_happiness(-1)
        "[title] looks away, trying to pretend she's not interested in what you and [the_sex_person.fname] are... serving up."
        return False
    if the_person.sluttiness < the_position.slut_requirement:
        $ the_person.draw_person(display_transform = character_left_flipped)
        if not is_watching(the_person):
            the_person "You're really... cooking up something special, aren't you? I suppose it's kind of... appetizing..."
        $ the_person.change_slut(1, 30)
        "[title] watches you and [the_sex_person.fname] [the_position.verb], trying not to... drool, like a diner who's just been served a dish they love."
        return True
    if the_person.sluttiness >= the_position.slut_requirement and the_person.sluttiness < the_position.slut_cap:
        $ the_person.draw_person(display_transform = character_left_flipped)
        if not is_watching(the_person):
            the_person "Oh, wow... this looks like so much... fun. Can I... join the feast?"
        $ the_person.change_slut(1, 50)
        "[title] watches you and [the_sex_person.fname] [the_position.verb], her eyes... sparkling with excitement, like a chef who's just been given a new ingredient to work with."
        return True
    $ the_person.draw_person(emotion = "happy", display_transform = character_left_flipped)
    if renpy.random.randint(0, 1) == 0:
        the_person "You know, [the_person.mc_title], [the_sex_person.fname] is really... getting into this. Maybe you should, uh, add a little more... spice to the dish?"
    else:
        call watcher_position_comment(the_person, the_sex_person, the_position) from _call_watcher_position_comment_foodie_sex_watch
    "[title] watches with interest as you and [the_sex_person.fname] [the_position.verb], like a diner who's just been served a perfect meal."
    return True

label foodie_being_watched(the_person, the_watcher, the_position):
    $ title = the_watcher.fname if not the_watcher.is_stranger else "the stranger"
    if the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #They agree you should give it to her harder
        the_person "Hmph, I guess you're right, [the_person.mc_title]."
        the_person "But don't think I'm going easy on you just because there's an... audience, like a chef who's just been told to remake a dish..."
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [title] watching you and her [the_position.verb], like a diner who's just been served a dish they love."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's super slutty and doesn't care what people think.
        the_person "You know, [title], I don't really care what you think, but it's pretty obvious you're... hungry for some action right now, like a diner who's just been served a dish they didn't order."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #She's super slutty and encourages the watcher to be slutty.
        the_person "Oh, come on, [title]! Don't be shy! You know you want a... taste of this action, like a chef who's just been given a new ingredient to work with!"
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [title] watching you and her [the_position.verb], like a diner who's just been served a perfect meal."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #She's into it and encouraged by the slut watching her.
        "[the_person.fname] glances at [title], like a chef who's just been given a new ingredient to work with."
        the_person "Yeah, I guess I can handle a little more... for now, like a diner who's just been served a dish they love."
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [title] watching you and her [the_position.verb], like a chef who's just been given a new recipe to try."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's into it but shamed by the prude watching her.
        the_person "Ugh, why do you have to be here, [title]? Can't you just leave me alone to... savor the moment?"
        $ the_person.change_stats(arousal = -1, slut = -1)
        "[the_person.title] seems uncomfortable with [title] nearby, like a diner who's just been served a dish they didn't order."

    else: #the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #They're both into it but not fanatical about it.
        "[the_person.possessive_title!c] rolls her eyes at [title], like a chef who's just been told to remake a dish."
        the_person "Whatever, [title], you're missing out. Maybe next time you'll get a... taste of the action, like a diner who's just been served a dish they love."
        $ the_person.change_stats(arousal = 1, slut = 1, max_slut = 30)
        "[the_person.title] seems more comfortable [the_position.verbing] you with [title] around, like a chef who's just been given a new ingredient to work with."

    return

label foodie_work_enter_greeting(the_person):
    if the_person.happiness < 80 or the_person.love < 0:
        "[the_person.title] glances at you when you enter the room, her expression as... bland as a plain cracker."
        the_person "What do you want? I'm in the middle of... whipping up something."
        "She goes back to her work, not looking up again, like a chef who's just been told to remake a dish."

    elif the_person.happiness > 130:
        if the_person.sluttiness > 40:
            the_person "Hey [the_person.mc_title], just the... ingredient I was hoping to add to my day."
            "Her eyes sparkle with... mischief, like a pastry chef who's just been given a new dessert to create, as she leans against her desk."
            the_person "You know what they say: all work and no play makes for a... stale recipe."
            "She winks, inviting you to join her in some... culinary 'play', like a chef who's just been given a new ingredient to work with."
        else:
            "[the_person.title] looks up from her work and smiles at you when you enter the room, like a diner who's just been served a perfect meal."
            the_person "Hey [the_person.mc_title], it's nice to have you stop by. You know, just to... savor the moment."
            "She blushes slightly, looking away before quickly glancing back at you, like a chef who's just been given a new recipe to try."
    else:
        if the_person.sluttiness > 60:
            $ the_person.draw_person(position = "stand4")
            "[the_person.title] walks over to you when you come into the room, her hips swaying... seductively, like a pastry chef who's just been given a new dessert to create."
            the_person "Well, well, well. Look who decided to drop by, like a diner who's just been served a dish they love."
            "She leans in close, her voice... husky and sultry, like a chef who's just been given a new ingredient to work with."
            the_person "I've been waiting for you, [the_person.mc_title]. You know, just to... taste the moment."
            "She brushes her fingers against your arm, sending shivers down your spine, like a diner who's just been served a perfect meal."
        else:
            the_person "Hey [the_person.mc_title]. Need anything? I mean, if you're not too... full, like a diner who's just finished a meal..."
            "She looks up at you, her eyes... soft and inviting, like a chef who's just been given a new recipe to try."
    return

label foodie_date_seduction(the_person):
    if the_person.is_girlfriend:
        "[the_person.possessive_title!c] grabs your hand and pulls you around to look at her, like a chef who's just been given a new ingredient to work with."
        the_person "Hey, that was such a great... dish. So I was thinking..."
        $ mc.change_locked_clarity(30)
        if the_person.effective_sluttiness(["vaginal_sex", "condomless_sex"]) > 60 and the_person.wants_creampie and the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex >= 0 and the_person.opinion.creampies >= 0 and not the_person.on_birth_control and not the_person.knows_pregnant:
            if the_person.opinion.creampies > 0: #No condoms, loves creampies, she's basically asking you to knock her up. So... have her ask you to knock her up!
                the_person "You're probably just going to say no, but I really want to get... knocked up by someone like you, like a pastry chef who's just been given a pastery a creme filling."
                the_person "So, are you going to make me... pregnant or what? I bet you could give me some... delicious kids, like a chef who's just been given a new ingredient to work with."
            else:
                the_person "I don't care if you don't use a... condiment. I just want you to... indulge in me and make me feel good, like a diner who's just been served a perfect meal."
                the_person "You're so much better than those other... chefs, anyway, like a pastry chef who's just been given a new dessert to create."
        elif the_person.effective_sluttiness(["vaginal_sex", "condomless_sex"]) > 60 and the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex > 0:
            the_person "Ugh, fine. If you really want to know, I'd rather not use a... wrapper, like a chef who's just been given a new ingredient to work with."
            the_person "But don't think I'm doing it for you or anything. It just... tastes better that way, like a diner who's just been served a dish they love."
        elif the_person.effective_sluttiness(["vaginal_sex"]) > 50 and the_person.opinion.vaginal_sex > 0:
            the_person "You know, I didn't really want to go home with someone like you, like a diner who's just been served a dish they didn't order."
            the_person "But you're kind of... growing on me, like a chef who's just been given a new ingredient to work with."
            the_person "So, do you want to... indulge in me or what, like a pastry chef who's just been given a new dessert to create?"
        elif the_person.effective_sluttiness(["anal_sex"]) > 60 and the_person.opinion.anal_sex > 0:
            the_person "I don't know why I'm even bothering to ask you this, but... do you want to... savor my ass, like a chef who's just been given a new ingredient to work with?"
            the_person "It's not like I'm asking for much, but you're probably just going to say no anyway, like a diner who's just been served a dish they didn't order."
        elif the_person.effective_sluttiness(["sucking_cock"]) > 40 and the_person.opinion.giving_blowjobs > 0:
            the_person "You know, I'm not really in the mood to do this, but... you're kind of... appetizing when you're all worked up, like a pastry chef who's just been given a new dessert to create."
            the_person "So, do you want a... blowjob or what, like a diner who's just been served a dish they love?"
        elif the_person.effective_sluttiness() > 40 and the_person.opinion.being_covered_in_cum > 0:
            the_person "Ugh, fine. If you really want to know, I'd be okay with getting... covered in your sauce, like a chef who's just been given a new ingredient to work with."
            the_person "But don't expect me to be all... happy about it or anything, like a diner who's just been served a dish they didn't order."
        elif the_person.effective_sluttiness(["touching_body"]) > 40 and the_person.opinion.giving_tit_fucks > 0 and the_person.has_large_tits:
            the_person "I don't know why I'm even telling you this, but... I'd be okay with... serving you up a tit fuck, like a pastry chef who's just been given a new dessert to create."
            the_person "But don't think I'm doing it because I like you or anything, like a diner who's just been served a dish they didn't order."
        else: #She's not very slutty, so she leaves the invitation open to interpretation
            the_person "You know, I don't really feel like going home with you or anything, like a diner who's just finished a meal..."
            the_person "But I guess I could be... persuaded if you do something really... tasty, like a chef who's just been given a new ingredient to work with."
            "She smirks, leaving the invitation open-ended, like a pastry chef who's just been given a new dessert to create."
    elif the_person.is_affair:
        the_person "So my [the_person.so_title] won't be home tonight, I was thinking... of whipping up something special, just for you."
        "She reaches down and cups your crotch, rubbing it gently through your pants, like a chef who's just been given a new ingredient to work with."
        $ mc.change_locked_clarity(40)
        if the_person.wants_creampie and the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex >= 0 and the_person.opinion.creampies >= 0 and not the_person.on_birth_control and not the_person.knows_pregnant:
            if the_person.opinion.creampies > 0: #No condoms, loves creampies, she's basically asking you to knock her up. So... have her ask you to knock her up!
                the_person "Fine, let's go back to my place so you can... pin me to the bed and creampie me all night long, like a pastry chef who's just been given a new dessert to create."
                the_person "I swear, just the thought of your... sauce inside me is making me want to puke and yet... I'm getting wet, like a diner who's just been served a dish they love."
            else:
                the_person "Alright, let's go back to my place. You can... pin me to the bed and fuck me bareback all night long, like a chef who's just been given a new ingredient to work with."
                the_person "I hate how much I want this, but I do. So just... indulge in me already, like a pastry chef who's just been given a new dessert to create."
        elif the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex > 0:
            # the_person "Do you want to come over to my place and fuck me all night long? No condoms allowed, like a chef who's just been given a new ingredient to work with."
            the_person "Ugh, fine. Let's go back to my place and fuck all night. No... condiments, like a diner who's just been served a dish they love."
            the_person "I don't want to admit it, but I'm really looking forward to this, like a pastry chef who's just been given a new dessert to create."
        elif the_person.opinion.vaginal_sex > 0:
            the_person "Fine, let's go back to my place and you can... pound my tight fucking pussy until I'm a wreck, like a chef who's just been given a new ingredient to work with."
            the_person "I hate how much I enjoy this, but... I do. So do it, like a diner who's just been served a dish they love."
        elif the_person.opinion.anal_sex > 0:
            the_person "Ugh, alright. Let's go back to my place so you can... savor my ass, like a chef who's just been given a new ingredient to work with."
            the_person "I don't want to admit it, but my ass is really... excited for this, like a pastry chef who's just been given a new dessert to create."
        elif the_person.opinion.giving_blowjobs > 0:
            the_person "Fine, let's go back to my place and you can... choke me out with your cock, like a chef who's just been given a new ingredient to work with."
            the_person "I hate how much I want this, but I do. So just do it already, like a diner who's just been served a dish they love."
        elif the_person.opinion.being_covered_in_cum > 0:
            the_person "Ugh, alright. Let's go back to my place, and you can... cover me in your sauce all night, like a pastry chef who's just been given a new dessert to create."
            the_person "I hate how much I enjoy this, but... I do. So just do it, like a diner who's just been served a dish they love."
        elif the_person.opinion.giving_tit_fucks > 0 and the_person.has_large_tits:
            the_person "Fine, let's go back to my place so I can... serve you up a tit fuck, like a pastry chef who's just been given a new dessert to create."
            the_person "I hate how much I enjoy this, but I do. So just do it already, like a diner who's just been served a dish they love."
        elif the_person.opinion.cheating_on_men > 0:
            the_person "Ugh, fine. Let's go back to my place, and you can do all the things I tell my [the_person.so_title] I hate, like a chef who's just been given a new ingredient to work with."
            the_person "I don't want to admit it, but I'm really looking forward to this, like a pastry chef who's just been given a new dessert to create."
        else:
            the_person "Ugh, let's go back to my place and make him really regret leaving me alone for the night, like a chef who's just been given a new ingredient to work with."
    elif not the_person.has_significant_other:
        $ mc.change_locked_clarity(20)
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                the_person "Ugh, fine. I've had a blast [the_person.mc_title], but there are a few more things I'd like to... savor with you. Want to come back to my place and find out what they are, like a diner who's just been served a dish they love?"
            else:
                the_person "Whatever. You've been a blast [the_person.mc_title]. Want to come back to my place, have a few drinks, and see where things lead? I suppose, like a chef who's just been given a new ingredient to work with."
        else:
            if the_person.love > 40:
                the_person "Fine, I don't want to say goodbye either. Tonight's been... delicious [the_person.mc_title]. Do you want to come back to my place and have a few drinks, like a diner who's just been served a perfect meal?"
            else:
                the_person "Whatever. This might be crazy, but I had a great time tonight and you make me a little... hungry. Do you want to come back to my place and see where things go? I don't know why I'm even asking, like a pastry chef who's just been given a new dessert to create."
    else:
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                $ mc.change_locked_clarity(20)
                the_person "Ugh, fine. I'm not done with you yet [the_person.mc_title]. Want to come back to my place? But don't think you're getting away with anything, like a chef who's just been given a new ingredient to work with."
                the_person "My [the_person.so_title] won't be home until morning, so we would have plenty of time to... indulge in each other, like a diner who's just been served a perfect meal."
            else:
                $ mc.change_locked_clarity(20)
                the_person "Whatever. This might be crazy, but do you want to come back to have another drink with me? I suppose, like a chef who's just been given a new ingredient to work with."
                the_person "My [the_person.so_title] is stuck at work and I don't want to be left all alone, like a diner who's just been served a dish they didn't order."
        else:
            if the_person.love > 40:
                $ mc.change_locked_clarity(20)
                the_person "Whatever. You're making me feel... hungry [the_person.mc_title]. Do you want to come have a drink at my place? But don't think this means anything, like a chef who's just been given a new ingredient to work with."
                the_person "My [the_person.so_title] won't be home until morning, and we have a big bed you could help me... warm up, like a diner who's just been served a perfect meal."
            else:
                $ mc.change_locked_clarity(20)
                the_person "Whatever. This is crazy, but would you want to have one last drink at my place? My [the_person.so_title] won't be home until morning... I suppose, like a pastry chef who's just been given a new dessert to create."
    return

label foodie_sex_end_early(the_person):
    if the_person.sluttiness > 50:
        if the_person.love > 40:
            if the_person.arousal_perc > 60:
                the_person "Ugh, really? You're done already? I was just getting to the... main course, [mc.name]... I mean, you're not exactly the most... skilled chef I've ever had in the kitchen..."
                the_person "But hey, I'll give you credit, you did try your best. Or at least, as best as you could with the... ingredients you had."
            else:
                the_person "Well, I suppose that's it? I was ready to serve up a lot more... But I guess you're not exactly the most... hungry for this whole situation, are you?"
        else:
            if the_person.arousal_perc > 60:
                the_person "Hmph, you're sure you're finished? I was really... savoring this... You know, I don't usually do this, but I was actually getting kind of... addicted to the flavor."
                the_person "But I guess you're not exactly the most... experienced chef, are you? I mean, it's not like I'm the one who needs to learn how to... cook this properly..."
            else:
                the_person "I guess it was okay, I suppose. I mean, it's not like I was expecting a... gourmet meal from you in the first place..."
    else:
        if the_person.love > 40:
            if the_person.arousal_perc > 60:
                the_person "Oh, come on, [mc.name], you can't leave me... starving like this... I mean, I was actually starting to... taste the flavors!"
                the_person "But hey, I guess you're not exactly the most... romantic chef out there, are you?"
            else:
                the_person "Well, that was a nice little... appetizer, I suppose. I mean, it's not like I'm the type to be all... sweet-toothed and shit..."
        else:
            if the_person.arousal_perc > 60:
                the_person "Geez, I guess that was enough... I mean, I don't know why you even bother trying, you're not exactly the best... chef at this, are you?"
            else:
                the_person "Good, it's over. Now let's get this... meal over with. I mean, I've got better things to do than hang around with someone who can't even manage to... cook it right..."
    return

label foodie_sex_take_control(the_person):
    if the_person.arousal_perc > 60:
        the_person "What do you think you're doing, [mc.name]? Don't just leave me... hungry like this! I mean, I'm the one who's supposed to be in... control of the kitchen here, not you!"
        the_person "But hey, if you're not going to... finish the dish, then I will. And don't think for a second that I won't make you... regret it, like a chef who's just been given a new ingredient to work with."
    else:
        the_person "Ugh, really? You're not even going to... finish what you started? Fine, I'll do it myself then! And don't think you can just waltz in here and expect me to be all... weak and submissive, like a diner who's just been served a dish they didn't order. I'm not that kind of... chef, [mc.name]."
    return

label foodie_sex_beg_finish(the_person):
    the_person "Okay, fine, [mc.name], you want to play it... cool? I'll let you off the hook this time, but just know that I'm going to make you... pay for this, like a chef who's just been given a new ingredient to work with. And when I'm done, I'm going to make sure you know exactly who's in... control of the kitchen here."
    return

label foodie_sex_review(the_person, the_report):
    $ comment_position = the_person.pick_position_comment(the_report)
    if comment_position is None:
        return #You didn't actually do anything, no need to comment.

    $ used_obedience = the_report.get("obedience_used", False) #True if a girl only tried a position because you ordered her to.
    $ the_person.draw_person()  # make sure she stands up for talking with you

    #She's worried about her SO finding out because it was in public
    if the_report.get("was_public", False) and the_person.has_significant_other and the_person.opinion.cheating_on_men <= 0: #It was public and she cares.
        if the_person.is_affair: #Dialogue about her being into it, but you can't do this in case she gets caught.
            the_person "Ugh, this is so... spicy! I'm really getting into this, but we can't get caught, or it'll be like a... recipe for disaster!"
            the_person "What if someone sees us and tells my [the_person.so_title]? I'll never hear the end of it, like a diner who's just been served a dish they didn't order!"
        elif used_obedience:
            the_person "I'm not sure I'm comfortable with this, it's like... eating a dish that's too rich. Someone might recognize me and tell my [the_person.so_title]."
            mc.name "Don't worry, nobody's going to tell anyone. We're being... discreet, like a chef who's just been given a new ingredient to work with."
            the_person "I hope you're right... I don't want anyone finding out about this, like a diner who's just been served a dish they didn't order."
        else:
            $ the_person.call_dialogue("surprised_exclaim")
            the_person "Oh no, we're out in public! Someone might see us and tell my [the_person.so_title]. I'll be so... screwed, like a chef who's just been told to remake a dish!"
            mc.name "Don't worry, nobody's paying attention to us. Nobody's going to tell your [the_person.so_title], like a diner who's just been served a dish they love."
            the_person "I hope you're right... I don't want anyone knowing about this, like a pastry chef who's just been given a new dessert to create."

    #She's single, but worried that you did in public.
    elif the_report.get("was_public", False) and (the_person.effective_sluttiness()+10*the_person.opinion.public_sex < comment_position.slut_cap):
        if used_obedience:
            the_person "Ugh, I'm not sure I'm comfortable with this, it's like... eating a dish that's too... spicy! Everyone's staring at us like we're some kind of... culinary perverts..."
            the_person "I'll never live this down, [mc.name]. People are going to talk about this for weeks, like a diner who's just been served a dish they didn't order!"
        else:
            the_person "Oh no, we're in public! Everyone's watching us and judging us for this, like a chef who's just been told to remake a dish..."
            mc.name "Don't worry, nobody really cares what we're doing. They're just... curious, like a diner who's just been served a dish they love."
            the_person "I hope you're right, or I'm going to end up with a... bad reputation for this sort of thing, like a pastry chef who's just made a mistake."

    elif the_report.get("girl orgasms", 0) > 2:
        if used_obedience:
            the_person "Oh fuck... baby... I loved what you did to me... I never knew being... submissive could feel so good, like a diner who's just been served a perfect meal."
            mc.name "I do enjoy when you keep begging me to make you cum again. It's almost like you're... addicted to it, like a chef who's just been given a new ingredient to work with."
            the_person "Shut up and kiss me, [mc.name], like a pastry chef who's just been given a new dessert to create."
        else:
            the_person "I have never... cum that hard... It was just... amazing, like a diner who's just been served a dish they love. I guess I needed that, like a chef who's just been given a new ingredient to work with."
            "She seems dazed by her orgasm as she tries to form coherent sentences, like a pastry chef who's just been given a new dessert to create."
            the_person "You really... know how to give a girl a good time... just gimme a second to catch my breath, like a diner who's just finished a meal."
            mc.name "Take your time, I'm not going anywhere, like a chef who's just been told to follow a recipe."
            the_person "Thanks, [mc.name]... I think I need a minute to recover before we can start again, like a pastry chef who's just been given a new dessert to create."

        call sex_review_trance(the_person) from _call_sex_review_trance_foodie_sex_review

    #No special conditions, just respond based on how orgasmed and how slutty the position was.
    elif the_report.get("girl orgasms", 0) > 0 and the_report.get("guy orgasms", 0) > 0: #You both came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position cap, it was tame
            the_person "Ah, that was... fucking delicious... But I think we could go even further next time, like a chef who's just been given a new ingredient to work with. I'm not afraid to... push the limits, [mc.name]."
            the_person "Doesn't that sound like... fun? I'm getting wet just thinking about it, like a diner who's just been served a dish they love."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "Ah, that was just what I needed! I think we're very... compatible, [mc.name], like a chef who's just been given a new ingredient to work with."
            the_person "Let's do it again some time soon, okay? I want to see how much further we can... indulge in each other, like a diner who's just been served a perfect meal."

        elif used_obedience: #She only did it because she was commanded
            the_person "Fuck, I... I didn't think I was going to cum like that. I guess I just can't resist a good... command, huh, like a diner who's just been served a dish they didn't order?"
            mc.name "Aren't you going to thank me? You obviously had a good time, like a chef who's just been given a new ingredient to work with."
            the_person "Shut up and don't get too full of yourself, [mc.name], like a pastry chef who's just made a mistake."

        else: # She's surprised she even tried that.
            the_person "Oh fuck, that was... intense! I didn't think I was going to take it so far, but it just felt... right, like a chef who's just been given a new ingredient to work with."
            the_person "Don't think that's going to happen every time though, alright? I'm not a... slut! I just like to... push my boundaries sometimes, like a diner who's just been served a dish they love."
        if the_person.love > 40:
            the_person "You know, I never thought I'd say this, but I think I might actually... like this whole 'relationship' thing with you, [mc.name], like a diner who's just been served a perfect meal."
        else:
            the_person "Well, that was... fun. Let's do it again sometime, but not too soon, okay? I need to... recover my dignity first, like a pastry chef who's just made a mistake."
    elif the_report.get("girl orgasms", 0) > 0: #Only she came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            the_person "Done already? Well, that's just not... right, like a diner who's just been served a dish they didn't order. Next time I'm going to make sure we both... cum and then some, like a chef who's just been given a new ingredient to work with."
            the_person "I've got a few... ideas that are going to blow you away, [mc.name], like a pastry chef who's just been given a new dessert to create."
            "She smiles mischievously, already imagining your next encounter, like a diner who's just been served a dish they love."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "You're all done? Well, that was... fucking hot either way, [mc.name], like a chef who's just been given a new ingredient to work with."
            the_person "I'll repay the favour next time, alright? I promise, like a diner who's just been served a perfect meal. And maybe we can try something... new, like a pastry chef who's just been given a new dessert to create."
            "She leans in close, whispering in your ear, like a diner who's just been served a dish they love."

        elif used_obedience: #She only did it because she was commanded
            the_person "That's it? I mean, not like I wanted to do anything more, I just thought you were going to... finish, like a chef who's just been told to follow a recipe."
            mc.name "Some other time. I just wanted to see what you look like when you... cum, like a diner who's just been served a dish they love."
            the_person "I... Fuck, well, I guess you got what you wanted, like a pastry chef who's just made a mistake. But don't think I'm going to make it easy for you next time, like a diner who's just been served a dish they didn't order."
            the_person "It could have been... worse, I guess, like a chef who's just been given a new ingredient to work with."

        else: # She's surprised she even tried that.
            the_person "Oh fuck, that was... intense! You really know how to make a girl feel... good, [mc.name], like a chef who's just been given a new ingredient to work with."
            the_person "You're probably... tired after all that work, like a diner who's just finished a meal. I promise I'll repay the favour next time, okay? And maybe we can try something... different, like a pastry chef who's just been given a new dessert to create."
            "She smiles, already looking forward to your next encounter, like a diner who's just been served a dish they love."

    elif the_report.get("guy orgasms", 0) > 0: #Only you came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            the_person "Hmph, you're all tired out already? That's so... frustrating, like a diner who's just been served a dish they didn't order!"
            mc.name "Sorry, I'll make it up to you next time, like a chef who's just been given a new ingredient to work with."
            the_person "Well, I suppose I could be... persuaded to try again, like a diner who's just been served a dish they love. But don't expect any... special treatment, like a pastry chef who's just made a mistake!"
            mc.name "Yeah, I think I could handle that, like a chef who's just been given a new ingredient to work with."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "You're already done? Such a... tease! Fine, I'll let you off this time, like a diner who's just been served a dish they love..."
            mc.name "Sorry [the_person.title], maybe another time, like a chef who's just been given a new ingredient to work with."
            the_person "You'd better, or you won't be hearing the word 'please' from me again, like a pastry chef who's just made a mistake!"

        elif used_obedience: #She only did it because she was commanded
            the_person "I suppose you're worn out from all that... We're finished then, like a chef who's just been told to follow a recipe?"
            mc.name "Yeah, that's all for now, like a diner who's just finished a meal."
            the_person "Fine, but don't think this means you get to... slack off next time, like a pastry chef who's just made a mistake!"

        else:  # She's surprised she even tried that.
            the_person "Wow, that was... quite an experience, like a diner who's just been served a dish they didn't order. I think I got a little... carried away there, like a chef who's just been given a new ingredient to work with."
            the_person "Maybe it's for the best that we stop here, like a diner who's just finished a meal. I need to think about what I just did, like a pastry chef who's just been given a new dessert to create..."

    elif the_person.energy < 10: #Nobody came and she's tired
        the_person "Ugh, I'm not sure I can... handle any more of this, like a diner who's just finished a meal. I'm just too... exhausted, like a chef who's just been told to remake a dish."
        mc.name "No worries, we'll do it another day, like a chef who's just been given a new ingredient to work with."
        the_person "Just don't expect any... special treatment when we try again, got it, like a pastry chef who's just made a mistake?"

    else: #Nobody came.
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            the_person "Hmph, you're already done? What's the... rush? We could've had more... fun, like a diner who's just been served a dish they love!"
            "She crosses her arms, pretending to be upset, like a pastry chef who's just made a mistake."
            the_person "You're such a... spoilsport [the_person.mc_title], like a diner who's just been served a dish they didn't order."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "We're stopping? But we were just getting to the... good stuff, like a chef who's just been given a new ingredient to work with!"
            mc.name "Sorry [the_person.title], maybe another time, like a chef who's just been given a new ingredient to work with."
            the_person "Yeah, maybe, like a diner who's just been served a dish they love. You can't just leave a girl... hanging like that, you know, like a pastry chef who's just been given a new dessert to create."

        elif used_obedience: #She only did it because she was commanded
            the_person "Well, I wasn't expecting that, like a diner who's just been served a dish they didn't order. I thought you had more in mind, like a chef who's just been given a new ingredient to work with."
            mc.name "You aren't disappointed, are you, like a pastry chef who's just made a mistake?"
            the_person "No, no, like a diner who's just been served a dish they love. I just... wanted to see where things would go, that's all, like a chef who's just been given a new ingredient to work with."
            the_person "It's fine, like a diner who's just finished a meal. I'll just have to find someone else to take me... further, like a pastry chef who's just been given a new dessert to create."

        else:  # She's surprised she even tried that.
            the_person "Ugh, you're probably right, like a diner who's just been served a dish they didn't order. We should stop now before we get too... carried away, like a chef who's just been given a new ingredient to work with."
            the_person "I don't want to do something I'll... regret later, like a pastry chef who's just made a mistake. Let's just keep this... casual, okay, like a diner who's just been served a dish they love?"

    # Gave creampie while she is not on birth control (extra dialogue when she could get pregnant)
    if the_report.get("creampies", 0) > 0 and not the_person.on_birth_control and not the_person.knows_pregnant:
        the_person "Well, I guess we just made things a little more... interesting, didn't we, like a chef who's just been given a new ingredient to work with?"
        the_person "If I get... pregnant, it'll serve you right for being so... reckless, like a pastry chef who's just made a mistake!"

    $ del comment_position
    return

## Role Specific Section ##

label foodie_improved_serum_unlock(the_person):
    mc.name "[the_person.title], now that you've had some time to... savor the lab, there is something I want to... dish out to you."
    the_person "Yeah, what's on the... menu?"
    mc.name "Our R&D up to this point has been based on my old... recipe notes from university."
    mc.name "There were some unofficial experiment results that suggested the effects might be... spiced up by sexual arousal."
    "[the_person.title] raises an eyebrow, like a chef who's just been given a new ingredient to work with."
    the_person "Ah, so you noticed that too? I have a hypothesis that an orgasm opens chemical receptors that are normally... blocked, like a pastry chef who's just made a mistake."
    mc.name "What if that's true? Does that open up any more... flavors for our research?"
    the_person "If it's true, I could leverage the effect to induce greater... effects in our subjects, like a chef who's just been given a new ingredient to work with."
    "[the_person.possessive_title!c] grins mischievously, like a diner who's just been served a dish they love."
    the_person "We'll need to do some experiments to be sure, like a chef who's just been told to follow a recipe."
    mc.name "What kind of experiments?"
    the_person "I want to take a dose of serum myself, and you can record the... ingredients, like a pastry chef who's just been given a new dessert to create."
    the_person "Then I'll...ahem...stimulate myself, and we can compare the effects after, like a chef who's just been given a new ingredient to work with."
    mc.name "Do you really think that's a good... recipe?"
    the_person "Not really, but we can't trust anyone else with this information if we're right, like a diner who's just been served a dish they didn't order."
    the_person "We might be able to make progress by brute force, but this is a chance to take our research to the next... course, like a chef who's just been given a new ingredient to work with."
    the_person "A finished dose of serum that raises my Suggestibility, like a pastry chef who's just been given a new dessert to create. The higher it gets, the better, like a diner who's just been served a perfect meal."
    the_person "Then we'll just need some time and some... private dining for me to see what sort of effects my...ahem...stimulation will have, like a chef who's just been given a new ingredient to work with."
    return

## Taboo break dialogue ##

label foodie_kissing_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 30:
        the_person "Fine, let's just... savor the moment. You've always been... hungry for this, right?"
        mc.name "That's not true, but I'll... indulge you."
        the_person "Hmph, whatever. Just shut up and... serve me already, like a chef who's just been given a new ingredient to work with."
        mc.name "Oh, I'm not going to shut up that easily, like a diner who's just been served a dish they didn't order."
        the_person "Suit yourself. I'll just have to find someone else who's willing to... taste me."
        mc.name "Hold on, wait a minute. I'm not going anywhere, like a chef who's just been told to follow a recipe."
        the_person "Oh? You're not going anywhere? Then get over here and... devour me already, like a pastry chef who's just been given a new dessert to create!"
        mc.name "Alright, alright. Here I come, like a diner who's just been served a perfect meal."
    elif the_person.love >= 20:
        the_person "So we're doing this, huh? About time, if you ask me, like a chef who's just been given a new ingredient to work with."
        mc.name "I guess we are. What do you think, like a diner who's just been served a dish they love?"
        the_person "It's about time we finally... feasted on each other, [the_person.mc_title], like a pastry chef who's just been given a new dessert to create."
        mc.name "I'm glad you feel that way, like a chef who's just been given a new ingredient to work with."
        the_person "Me too. Just be... gentle, like a diner who's just been served a delicate dish, okay?"
        mc.name "I will, like a chef who's just been told to follow a recipe."
    else:
        the_person "I don't know if this is a good... recipe, [the_person.mc_title]. We're taking things too... fast, aren't we, like a diner who's just been served a dish they didn't order?"
        mc.name "Are you... scared, like a pastry chef who's just made a mistake?"
        the_person "No! I'm just...not sure if this is a good... flavor combination. But I trust you, like a diner who's just been served a perfect meal."
        mc.name "Good. Because I'm not going to let you... back out now, like a chef who's just been given a new ingredient to work with."
        the_person "Hmph. Fine. But if this is a... culinary disaster, it's on you, like a pastry chef who's just made a mistake."
        mc.name "It'll be... worth it, I promise, like a chef who's just been given a new ingredient to work with."
    return

label foodie_touching_body_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 30:
        the_person "Come on then, don't be shy. You've wanted to... savor my body for ages, haven't you, like a chef who's just been given a new ingredient to work with?"
        mc.name "Hey, I'm not that... obvious, like a diner who's just been served a dish they didn't order!"
        the_person "Oh, please. I can see the way you... devour me with your eyes, like a pastry chef who's just been given a new dessert to create."
        mc.name "Well, I can't help it if you're... irresistible, like a perfect dish that's just been served."
        the_person "Irresistible? Pfft, you're just trying to get a... taste of me, like a chef who's just been given a new ingredient to work with."

    elif the_person.love >= 20:
        the_person "So you're ready for this, like a chef who's just been given a new recipe to try?"
        "You nod, like a diner who's just been served a dish they love."
        the_person "Me too, I think. I didn't think I'd be so... nervous when you actually made a move, like a pastry chef who's just made a mistake."
        mc.name "Just relax, like a diner who's just been served a soothing dish. You trust me, right, like a chef who's just been given a new ingredient to work with?"
        the_person "Of course, like a diner who's just been served a perfect meal. Just don't expect me to be all... touchy-feely about it, like a pastry chef who's just been given a new dessert to create."

    else:
        the_person "I think you're getting a little ahead of yourself here [the_person.mc_title], like a chef who's just been told to remake a dish."
        mc.name "What do you mean, like a diner who's just been served a dish they didn't order?"
        the_person "I mean I don't just let anyone... feast on me, like a pastry chef who's just been given a new dessert to create. Maybe we should cool things down, like a chef who's just been told to follow a recipe."
        mc.name "You're not scared, are you, like a pastry chef who's just made a mistake?"
        the_person "Scared? Of course not, like a diner who's just been served a dish they love!"
        mc.name "Well then just relax and go with it, like a chef who's just been given a new ingredient to work with. It doesn't have to mean anything unless we want it to, like a diner who's just been served a perfect meal."
        "You see her answer in her eyes before she says anything, like a pastry chef who's just been given a new dessert to create."
        the_person "You're so bad for me, you know that, like a diner who's just been served a dish they didn't order?"
        mc.name "Well let me make up for it then, like a chef who's just been given a new ingredient to work with."
        the_person "Hmm, maybe I'll let you, like a diner who's just been served a perfect meal."

    return

label foodie_touching_penis_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 35:
        the_person "Oh, you're really enjoying this, aren't you? Look how... hard you are, like a pastry chef who's just been given a new dessert to create."
        mc.name "Do you want to... taste it? You can if you want, like a chef who's just been given a new ingredient to work with."
        the_person "Yeah, why not? I'll try not to... hurt it, like a diner who's just been served a dish they didn't order."

    elif the_person.love >= 20:
        the_person "Your cock looks so... appetizing when it's hard, like a pastry chef who's just been given a new dessert to create. Can I... savor it?"
        mc.name "Go ahead, it doesn't... bite, like a diner who's just been served a dish they love."
        the_person "Well, it might if you're not... careful, like a pastry chef who's just made a mistake."

    else:
        mc.name "My cock is so... hard right now [the_person.title], like a pastry chef who's just been given a new dessert to create. Put your hand on it and... touch it for me, like a chef who's just been given a new ingredient to work with."
        the_person "What? That's taking things a little... far, don't you think, like a diner who's just been served a dish they didn't order?"
        mc.name "Come on, you know you want to, like a chef who's just been given a new ingredient to work with. Just a few... strokes, then if you aren't impressed you can stop, like a diner who's just been served a perfect meal."
        the_person "Fine, but don't expect me to make any... promises after this, like a pastry chef who's just been given a new dessert to create."
        mc.name "I wouldn't dream of it, like a diner who's just been served a dish they love."
        the_person "Hmm, okay then. I'll give it a... try, like a chef who's just been given a new ingredient to work with."
    "She reaches out and wraps her hand around your cock, her touch... gentle but firm, like a pastry chef who's just been given a new dessert to create."
    "You feel a surge of pleasure as she starts to... stroke you, like a diner who's just been served a perfect meal."
    the_person "Mmm, you're really... nice when you're hard, like a pastry chef who's just been given a new dessert to create."
    return

label foodie_touching_vagina_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 35:
        the_person "Come on, don't be shy. You've been... craving a taste of my pussy, admit it, like a chef who's just been given a new ingredient to work with."
    elif the_person.love >= 20:
        the_person "Oh fuck, you've got my pussy... simmering. I want you to... savor it [the_person.mc_title], like a pastry chef who's just been given a new dessert to create."
        mc.name "You sure? I don't want to... overseason you, like a chef who's just been given a new ingredient to work with."
        the_person "No, I want it. I want you to... indulge in me, like a diner who's just been served a perfect meal."
    else:
        the_person "I don't know if we should be... serving this dish [the_person.mc_title], like a chef who's just been told to remake a dish..."
        mc.name "Just take a deep breath and... relax, like a diner who's just been served a soothing dish. I'm just going to... touch you a little, and if you don't like it I'll stop, like a chef who's just been given a new ingredient to work with."
        the_person "Just a little, like a pastry chef who's just been given a new dessert to create?"
        mc.name "Just a little, like a diner who's just been served a perfect meal. Trust me, it's going to... taste amazing, like a chef who's just been given a new ingredient to work with."
        the_person "Hmm, okay. But don't think this means I'm... easy to please, like a diner who's just been served a dish they didn't order."
        mc.name "I wouldn't dream of it, like a pastry chef who's just made a mistake."

    return

label foodie_sucking_cock_taboo_break(the_person):
    mc.name "I want you to... indulge in something for me, like a diner who's just been served a perfect meal."
    the_person "Oh yeah? What do you want me to... savor, like a pastry chef who's just been given a new dessert to create?"
    mc.name "I want you to... suck on my cock, like a chef who's just been given a new ingredient to work with."
    if the_person.effective_sluttiness() >= 45:
        the_person "Mmm, I think I'm... hungry for that, like a diner who's just been served a dish they love. It's not going to be too... spicy for me, is it, like a chef who's just been given a new ingredient to work with?"
        mc.name "I think you'll be able to... handle it, like a pastry chef who's just been given a new dessert to create."
        the_person "Alright, I don't want it... overwhelming me, like a diner who's just been served a dish they didn't order."
        "She bites her lip and winks at you, like a pastry chef who's just been given a new dessert to create."
        the_person "That's a lie, like a chef who's just been given a new ingredient to work with. A little... choking is okay, like a diner who's just been served a perfect meal."

    elif the_person.love >= 30:
        the_person "I guess we've been... simmering around it for a while, like a chef who's just been given a new ingredient to work with."
        "She bites her lip and looks your body up and down, like a pastry chef who's just been given a new dessert to create."
        the_person "Alright, let's... serve it up, like a diner who's just been served a perfect meal."

    else:
        the_person "Oh, I was wondering if this was going to... come up, like a chef who's just been told to remake a dish..."
        "She laughs nervously and looks away from you, like a diner who's just been served a dish they didn't order."
        the_person "I don't know [the_person.mc_title], like a pastry chef who's just made a mistake..."
        "You reach up and hold her chin, turning her head back to face you, like a chef who's just been given a new ingredient to work with."
        mc.name "Don't overthink it, like a diner who's just been served a soothing dish. Just kneel down and... savor it for me, like a pastry chef who's just been given a new dessert to create. If you don't like doing it, we can just... forget it happened, like a chef who's just been given a new ingredient to work with."
        "You can see in her eyes the moment her resolve breaks, like a pastry chef who's just made a mistake. She bites her lip and nods, like a diner who's just been served a perfect meal."
        the_person "Alright, let's... indulge in this, like a chef who's just been given a new ingredient to work with."
        "She slowly gets down on her knees, her eyes darting between your face and your cock with a mix of reluctance and curiosity, like a diner who's just been served a dish they didn't order."
        the_person "You know, I never thought I'd be... serving this dish, like a pastry chef who's just been given a new dessert to create. But I guess I'm willing to... try new things for you, like a chef who's just been given a new ingredient to work with."
        "She takes a deep breath, her hand wrapping around the base of your cock as she leans in to... savor it, like a pastry chef who's just been given a new dessert to create."
        "As she starts to suck, her eyes flash up to meet yours, a hint of defiance and challenge in them, like a diner who's just been served a perfect meal."
        the_person "Satisfied now, like a chef who's just been given a new ingredient to work with?"
    return

label foodie_licking_pussy_taboo_break(the_person):
    mc.name "I want to... savor your pussy [the_person.title]. Are you ready, like a chef who's just been given a new ingredient to work with?"
    if the_person.effective_sluttiness() >= 45:
        the_person "Hmph, I don't need your permission or anything, but fine. I'm... ripe and ready, like a pastry chef who's just been given a new dessert to create."
        mc.name "Good. But don't expect me to go easy on you just because it's your first time, like a diner who's just been served a dish they didn't order."
        the_person "Oh, please. I've had... better flavors, like a chef who's just been given a new ingredient to work with."
    elif the_person.love >= 30:
        the_person "Finally, a man who knows how to... season a woman right, like a chef who's just been given a new ingredient to work with. I'm ready when you are, like a diner who's just been served a perfect meal."
        mc.name "That's what I like to... taste, like a pastry chef who's just been given a new dessert to create."
    else:
        if the_person.has_taboo("sucking_cock"):
            the_person "You know, I never thought I'd see the day where you'd be willing to... indulge in this, like a diner who's just been served a dish they love."
            "She bites her lip and smirks at you, like a pastry chef who's just been given a new dessert to create."
            the_person "But I guess I'm not going to... complain, like a diner who's just been served a dish they didn't order. Just don't expect me to be all... grateful or anything, like a chef who's just been given a new ingredient to work with."
        else:
            the_person "About time you decided to... serve up something new, like a chef who's just been given a new ingredient to work with."
            "She rolls her eyes and smiles, like a diner who's just been served a perfect meal."
            the_person "But fine, I'm ready, like a pastry chef who's just been given a new dessert to create. Just don't expect me to be all... appreciative or anything, like a chef who's just been given a new ingredient to work with."
    "She lies back, her eyes darting between yours and the area you're about to... explore, like a diner who's just been served a dish they didn't order."
    the_person "And don't think this means I'm some kind of... culinary slut for letting you do this, like a chef who's just been given a new ingredient to work with."
    mc.name "I wouldn't dream of it, like a pastry chef who's just made a mistake. You're just being a good... sport, right, like a diner who's just been served a perfect meal?"
    the_person "Something like that, like a chef who's just been given a new ingredient to work with..."
    "She closes her eyes, her face flushed with... embarrassment as you start to... savor her, like a pastry chef who's just been given a new dessert to create."
    return

label foodie_vaginal_sex_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 60:
        the_person "Ugh, finally! I've been... starving for this moment all night, like a diner who's just been served a perfect meal. Come on then, get that... cock inside me and... fuck me like you mean it, like a chef who's just been given a new ingredient to work with!"
    elif the_person.love >= 45:
        the_person "Alright, show me what you've... got cooking, like a chef who's just been given a new ingredient to work with. I'm ready for this, like a diner who's just been served a perfect meal."
        mc.name "You better be, like a pastry chef who's just been given a new dessert to create. I'm going to make sure you... remember this, like a chef who's just been given a new ingredient to work with."
        the_person "Bring it on, like a diner who's just been served a dish they love! I can... take it, like a chef who's just been given a new ingredient to work with."
    else:
        if the_person.has_taboo("anal_sex"):
            the_person "Well, well, well. Look at that... cock, like a pastry chef who's just been given a new dessert to create. I guess we're going to find out just how... tight my pussy is, like a chef who's just been given a new ingredient to work with."
            mc.name "That's the plan, like a chef who's just been given a new ingredient to work with. And if you're a good girl, I might just make it... worth your while, like a diner who's just been served a perfect meal."
            the_person "Hmph, I'm always... good, like a chef who's just been given a new ingredient to work with. Now get to it before I... change my mind, like a diner who's just been served a dish they didn't order."
        else:
            the_person "Oh, so that's what you're going to do with that... big cock of yours, like a pastry chef who's just been given a new dessert to create. Well, I guess we'll see how it... feels, like a chef who's just been given a new ingredient to work with."
            mc.name "We sure will, like a chef who's just been given a new ingredient to work with. And if you're lucky, I might just make it... feel even better, like a diner who's just been served a perfect meal."
            the_person "Ugh, just get on with it already, like a diner who's just been served a dish they didn't order! I'm not getting any... younger, like a chef who's just been given a new ingredient to work with."
    return

label foodie_anal_sex_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 75:
        the_person "Ugh, fine. But only because I'm... famished for your cock, like a diner who's just been served a perfect meal. Your... dish is so big, I'm surprised it fits on the plate, like a pastry chef who's just been given a new dessert to create!"
        "She seems more... ravenous by the prospect than intimidated, like a chef who's just been given a new ingredient to work with."
        mc.name "Don't worry, I'll... season it slow and make sure you're... comfortable, like a diner who's just been served a soothing dish."

    elif the_person.love >= 60:
        the_person "Are you sure you want to... serve this dish? I'm not exactly the most... experienced chef when it comes to anal, like a pastry chef who's just been given a new dessert to create..."
        mc.name "I'll be... gentle, like a diner who's just been served a perfect meal. Don't worry, like a chef who's just been given a new ingredient to work with."
        the_person "Alright, but if it... hurts too much, I'm stopping, like a diner who's just been served a dish they didn't order."

    else:
        if the_person.has_taboo("vaginal_sex"):
            the_person "Wait, are you sure you want to... indulge in this? My ass might be too... tight for your... cock, like a pastry chef who's just been given a new dessert to create!"
            mc.name "I'll make it... fit, like a chef who's just been given a new ingredient to work with. But you might feel a little... sore afterward, like a diner who's just been served a spicy dish."
            the_person "Oh, great. Just what I... needed, like a diner who's just been served a dish they didn't order."

        else:
            the_person "Come on, [mc.name]. Let's just... serve this dish already, like a chef who's just been given a new ingredient to work with. I don't know what's... gotten into me today, like a diner who's just been served a dish they didn't order."
            mc.name "Are you sure you're... okay with this, like a pastry chef who's just been given a new dessert to create?"
            the_person "Of course, I'm just... nervous, like a diner who's just been served a dish they didn't order. And a little... embarrassed, like a chef who's just made a mistake. But let's just... do this already, like a diner who's just been served a perfect meal!"
            "She blushes and looks away, like a pastry chef who's just been given a new dessert to create."
            mc.name "Alright, let's get... started then, like a chef who's just been given a new ingredient to work with."
            the_person "Hurry up, I'm... ready when you are, like a diner who's just been served a perfect meal."
    return

label foodie_condomless_sex_taboo_break(the_person):
    if the_person.knows_pregnant:
        the_person "Ugh, you really want to... serve it up without a condom? Fine, but don't say I didn't... season you, like a chef who's just been given a new ingredient to work with."
        if the_person.wants_creampie:
            the_person "If you're going to... pour your sauce inside me, please make it worth my while, like a diner who's just been served a perfect meal."
        else:
            the_person "Just make sure to... cover me with your... special sauce, like a pastry chef who's just been given a new dessert to create."

    elif the_person.opinion.bareback_sex > 0:
        the_person "Whatever, you want to... dine bareback, huh? Just don't say I didn't... warn you, like a chef who's just been given a new ingredient to work with."
        if the_person.on_birth_control:
            the_person "I'm on the... pill, so you don't have to worry about it, like a diner who's just been served a soothing dish."
            $ the_person.update_birth_control_knowledge()
        elif the_person.wants_creampie:
            the_person "But if you're going to... cum inside me, you'd better make it worth my while, like a pastry chef who's just been given a new dessert to create."
        elif the_person.opinion.creampies < 0:
            the_person "Just don't get me... pregnant, okay? That would be a huge... pain, like a diner who's just been served a dish they didn't order."
        else:
            the_person "Alright, just make sure you... pull out this time, like a chef who's just been given a new ingredient to work with."

    elif the_person.love > 60:
        if the_person.on_birth_control:
            the_person "Ugh, fine, I'm on the... pill. Don't say I didn't... warn you, like a chef who's just been given a new ingredient to work with."
            $ the_person.update_birth_control_knowledge()
        elif the_person.wants_creampie:
            the_person "You're always trying to make me do... stupid things, aren't you? Fine, if we're going to do this, make it worth my while, like a pastry chef who's just been given a new dessert to create."
            mc.name "Are you on the... pill?"
            "She rolls her eyes, like a diner who's just been served a dish they didn't order."
            the_person "No, I'm not. But if you're going to... cum inside me, you'd better make it worth it, like a pastry chef who's just been given a new dessert to create."
            $ the_person.update_birth_control_knowledge()
        elif the_person.opinion.creampies < 0:
            the_person "You're always trying to make me do... stupid things, aren't you? Fine, just don't get me... pregnant, like a diner who's just been served a dish they didn't order."
            the_person "I'm not ready for that kind of... responsibility again, like a chef who's just been given a new ingredient to work with."
        else:
            the_person "You're always trying to make me do... stupid things, aren't you? Fine, just make sure you... pull out this time, like a chef who's just been given a new ingredient to work with."
            if the_person.kids == 0:
                the_person "I need you to... pull out though. I'm not quite ready to be a... mother, even with you, like a diner who's just been served a dish they didn't order."
            elif the_person.kids == 1:
                the_person "I need you to... pull out though. I've already got a... kid, I don't need another one, like a diner who's just been served a dish they didn't order."
            else:
                the_person "I need you to... pull out though. I've already got... kids, I don't need another one, like a diner who's just been served a dish they didn't order."

    else:
        if the_person.on_birth_control:
            the_person "Hmph, you want to... dine without a rubber? Well, I'm on the... pill, so I guess it's fine, like a diner who's just been served a soothing dish. Just don't expect any... special treatment, like a chef who's just been given a new ingredient to work with."
            $ the_person.update_birth_control_knowledge()
        elif the_person.has_taboo("vaginal_sex"):
            the_person "You're really not going to use a... condom? I'm not on the... pill, so we could end up with a little... surprise, like a diner who's just been served a dish they didn't order."
            $ the_person.update_birth_control_knowledge()
            the_person "Or is this your sneaky plan to make a... baby out of me, like a pastry chef who's just been given a new dessert to create?"
            mc.name "I swear I'll... pull out. I want our first time to be... memorable, like a chef who's just been given a new ingredient to work with."
            "She crosses her arms and gives a half-hearted sigh, like a diner who's just been served a dish they didn't order."
            the_person "Ugh, fine. But you better... pull out, or you'll regret it, like a chef who's just been given a new ingredient to work with."
        else:
            the_person "You're really not going to use a... condom? I'm not on the... pill, so we could end up with a little... surprise, like a diner who's just been served a dish they didn't order."
            $ the_person.update_birth_control_knowledge()
            the_person "Or is this your sneaky plan to make a... baby out of me, like a pastry chef who's just been given a new dessert to create?"
            mc.name "I promise I'll... pull out. It'll feel so much better without anything between us, like a chef who's just been given a new ingredient to work with."
            the_person "God, I know. I'm trying to be... rational here, not some... lust-driven animal, like a diner who's just been served a dish they didn't order."
            "She huffs and puffs, like a pastry chef who's just been given a new dessert to create."
            the_person "Fine, no... condom. Just remember to... pull out, got it? Good, like a chef who's just been given a new ingredient to work with."
    return

label foodie_underwear_nudity_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > 30 - (the_person.opinion.skimpy_outfits * 5):
        the_person "You want to see me in my... underwear, huh? It's about time you asked, like a diner who's just been served a perfect meal."
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "What are we waiting for then, let's get this... dish served, like a chef who's just been given a new ingredient to work with."
        else:
            mc.name "Yeah, yeah. We've been over this. You're not exactly... subtle about it, like a pastry chef who's just been given a new dessert to create."
            the_person "Shut up! I just don't want you to get the... wrong idea, like a diner who's just been served a dish they didn't order."
            mc.name "Wrong idea? Like how you're not wearing anything under this... skirt, like a pastry chef who's just been given a new dessert to create?"
            the_person "Ugh, fine. But don't say I didn't... warn you, like a chef who's just been given a new ingredient to work with."

    elif the_person.love > 15:
        the_person "You want me to... strip down a little? It's about time, I was wondering why you were taking things so... slow, like a diner who's just been served a soothing dish."
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "Oh, don't give me that. You know you want to... show off, like a pastry chef who's just been given a new dessert to create."
            the_person "Fine, but if this gets out of... hand, I'm blaming you, like a diner who's just been served a dish they didn't order."
            mc.name "Promise, like a chef who's just been given a new ingredient to work with?"
            the_person "Yeah, yeah. Now get this [the_clothing.display_name] off, like a pastry chef who's just been given a new dessert to create."

        else:
            mc.name "Yeah, I know. You've been... teasing me for weeks, like a pastry chef who's just been given a new dessert to create."
            the_person "Teasing? I'm just being... friendly, like a diner who's just been served a perfect meal."
            mc.name "Right. Now let's get you out of these... clothes, like a chef who's just been given a new ingredient to work with."
            the_person "Ugh, fine. But don't think this means I'm going... easy on you, like a diner who's just been served a dish they didn't order."
            "She slowly starts taking [the_clothing.display_name] off, like a pastry chef who's just been given a new dessert to create."

    else:
        the_person "You really want to see me like this? Fine, but don't say I didn't... warn you, like a chef who's just been given a new ingredient to work with."
        the_person "If you take my [the_clothing.display_name] I'll only have my... underwear on, you know that, like a diner who's just been served a dish they didn't order?"
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "Yeah, that's kind of the... point, like a pastry chef who's just been given a new dessert to create."
            "She shakes her head and laughs to herself, like a diner who's just been served a dish they didn't order."
            the_person "Whatever, but if you think I'm doing this because I... want to, like a chef who's just been given a new ingredient to work with..."
        else:
            mc.name "Yeah, I know. You're not exactly... shy, like a pastry chef who's just been given a new dessert to create."
            the_person "Hey, I'm just being... cautious, like a diner who's just been served a perfect meal. You can't blame a girl for being... careful, like a chef who's just been given a new ingredient to work with."
            mc.name "Of course not, like a diner who's just been served a perfect meal. Now let's get you out of these... clothes, like a chef who's just been given a new ingredient to work with."
            the_person "Fine, but don't think this means I'm going... easy on you, like a diner who's just been served a dish they didn't order."
    return

label foodie_bare_tits_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > (40 - the_person.opinion.showing_her_tits * 5):
        the_person "Why do you want to... savor my tits now, all of a sudden? Like I don't already know you're... devouring me with your eyes, like a diner who's just been served a perfect meal."
        if the_person.has_large_tits:
            "She reluctantly shakes her chest for you, jiggling the [the_person.tits_description] hidden underneath her [the_clothing.display_name], like a pastry chef who's just been given a new dessert to create."
        else:
            "She reluctantly shakes her chest and gives her [the_person.tits_description] a little jiggle, like a chef who's just been given a new ingredient to work with."
        the_person "You're always so... eager, aren't you? I guess I can... serve them up for you, but don't get too... excited, like a diner who's just been served a dish they love."
        if the_person.has_large_tits:
            mc.name "Oh, I've been... craving them. Now let's get those... puppies out where I can... indulge in them, like a chef who's just been given a new ingredient to work with."
        else:
            mc.name "Oh, I've been... looking. Now let's get those... cute little things out, like a pastry chef who's just been given a new dessert to create."

    elif the_person.love > 25:
        the_person "Are you really sure you want to... taste my tits, [the_person.mc_title], like a diner who's just been served a perfect meal?"
        if the_person.has_large_tits:
            "She rolls her eyes and shakes her chest, jiggling her nice [the_person.tits_description], barely restrained by her [the_clothing.display_name], like a pastry chef who's just been given a new dessert to create."
        else:
            "She rolls her eyes and shakes her chest, giving her [the_person.tits_description] a little jiggle, like a chef who's just been given a new ingredient to work with."
        mc.name "Of course I am, like a diner who's just been served a perfect meal. You know I... love your tits, like a chef who's just been given a new ingredient to work with."
        the_person "Well, I suppose you're... entitled to see them then, like a diner who's just been served a perfect meal... but don't think this means I'm going to start... showing them off to everyone, like a pastry chef who's just made a mistake."

    else:
        the_person "Wait, no! Don't... devour me with your eyes like that, like a diner who's just been served a dish they love! You should at least... ask a girl before you try and put her tits on full... display, like a chef who's just been given a new ingredient to work with!"
        mc.name "Come on, don't be like that, like a diner who's just been served a dish they didn't order. I bet your tits... look great, like a pastry chef who's just been given a new dessert to create."
        the_person "They do, but I still feel a little... self-conscious about being... naked around you, alright, like a diner who's just been served a dish they didn't order?"
        mc.name "There's no need to be, like a chef who's just been given a new ingredient to work with. Just... relax and let me take your [the_clothing.display_name] off for you, like a pastry chef who's just been given a new dessert to create."
        the_person "Ugh, fine, like a diner who's just been served a dish they didn't order... but don't think this means I'm going to start... showing off my body to everyone, like a pastry chef who's just made a mistake!"
    return

label foodie_bare_pussy_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > (50 - the_person.opinion.showing_her_ass * 5):
        the_person "So you want to... savor my pussy, huh, like a diner who's just been served a perfect meal? Like I don't already know you're... thinking about it, like a chef who's just been given a new ingredient to work with."
        if the_person.has_taboo("touching_vagina"):
            "She reluctantly lifts her hips, allowing you to slowly remove her [the_clothing.display_name] and reveal her... pussy, like a pastry chef who's just been given a new dessert to create."
        else:
            "She lifts her hips, giving you a quick... glimpse of her pussy before covering it back up, like a chef who's just been given a new ingredient to work with."
        the_person "Well, you got your... wish, like a diner who's just been served a perfect meal. Don't say I didn't... warn you, like a chef who's just been given a new ingredient to work with."

    elif the_person.love > 35:
        the_person "You want to... indulge in my pussy, really, like a diner who's just been served a perfect meal? Are you sure you're... ready for that, like a chef who's just been given a new ingredient to work with?"
        if the_person.has_taboo("touching_vagina"):
            mc.name "I think I am, like a diner who's just been served a perfect meal. I've been... wanting to see it for a while, like a chef who's just been given a new ingredient to work with."
            the_person "Hmm, well, like a diner who's just been served a perfect meal... I suppose you've earned it, like a pastry chef who's just been given a new dessert to create. Just remember, you asked for this, like a chef who's just been given a new ingredient to work with."
        else:
            mc.name "I've already... felt it up, I thought I should... see it too, like a chef who's just been given a new ingredient to work with."
            the_person "You really are... persistent, aren't you, like a diner who's just been served a dish they love? Fine, go on then, like a pastry chef who's just been given a new dessert to create."

    else:
        the_person "Hold on, you're not getting me out of my [the_clothing.display_name] that... easily, like a diner who's just been served a dish they didn't order!"
        if the_person.has_taboo("touching_vagina"):
            mc.name "Come on, just let me... see it, like a chef who's just been given a new ingredient to work with. I promise I'll be... gentle, like a diner who's just been served a soothing dish."
            the_person "You're such a... liar, like a pastry chef who's just made a mistake... But fine, go ahead, like a chef who's just been given a new ingredient to work with."
        else:
            mc.name "I've already... felt your pussy up, I want to... get a look at it now, like a chef who's just been given a new ingredient to work with."
            the_person "You're so... pushy, like a diner who's just been served a dish they didn't order! Alright, but don't say I didn't... warn you, like a chef who's just been given a new ingredient to work with."
    return

# label foodie_facial_cum_taboo_break(the_person):

#     return

# label foodie_mouth_cum_taboo_break(the_person):

#     return

# label foodie_body_cum_taboo_break(the_person):

#     return
#==================================================================

label foodie_creampie_taboo_break(the_person):
    if the_person.wants_creampie:
        if the_person.knows_pregnant:
            the_person "You want to... season me with your seed, huh? Fine, I suppose it's about time someone... served me up a bun in the oven, like a pastry chef who's just been given a new dessert to create."
            "She sighs happily, seeming almost... hungry for the idea, like a diner who's just been served a perfect meal."

        elif the_person.on_birth_control:
            if the_person.has_significant_other:
                the_person "Oh my god, I'm such a... naughty [the_person.so_girl_title]! But I needed this so... badly, like a diner who's just been served a perfect meal."
                the_person "Maybe if we're lucky, my [the_person.so_name] won't... taste the difference, like a chef who's just been given a new ingredient to work with."
                "She looks at you with a... mischievous grin, like a pastry chef who's just been given a new dessert to create."
            else:
                the_person "Oh my god, I needed this so... badly! Ah... I guess I'll just have to... savor the consequences, like a diner who's just been served a dish they didn't order."

        elif the_person.effective_sluttiness() > 75 or the_person.opinion.creampies > 0:
            if the_person.has_significant_other:
                the_person "You want to... season me with your seed? Fine, I suppose it's about time someone... knocked me up, like a pastry chef who's just been given a new dessert to create."
                the_person "Maybe my [the_person.so_name] will finally... taste the difference and do something about it, like a chef who's just been given a new ingredient to work with."

            else:
                the_person "You want to... season me with your seed? Fine, I suppose it's about time someone... knocked me up, like a pastry chef who's just been given a new dessert to create."
                the_person "I guess I'll just have to... savor the consequences, like a diner who's just been served a dish they didn't order."

            "She sighs happily, but with a hint of... annoyance, like a diner who's just been served a dish they didn't order."
            the_person "How long until you're ready for... round two? I want as much of your... sauce inside my pussy as possible, like a pastry chef who's just been given a new dessert to create."
            the_person "Just don't expect me to be all... happy and grateful about it, like a diner who's just been served a dish they didn't order."

        else:
            if the_person.has_significant_other:
                the_person "Oh fuck... I'm such a... terrible [the_person.so_girl_title], like a pastry chef who's just made a mistake!"
                "She sighs happily, but with a hint of... guilt, like a diner who's just been served a dish they didn't order."
                the_person "But that... tasted so good, like a diner who's just been served a perfect meal..."
            else:
                the_person "Oh fuck, that was so... risky, like a diner who's just been served a dish they didn't order."
                "She sighs happily, but with a hint of... annoyance, like a diner who's just been served a dish they didn't order."
                the_person "But it... tasted so good, like a diner who's just been served a perfect meal..."
            the_person "I'll just have to... hope you haven't... seasoned me with a bun in the oven, like a pastry chef who's just been given a new dessert to create. We really shouldn't do this again, my... luck is going to run out at some point, like a diner who's just been served a dish they didn't order."
            the_person "Besides, I'm not exactly... thrilled about the idea of being... tied down to a man right now, like a diner who's just been served a dish they didn't order."

    else:
        if the_person.knows_pregnant:
            the_person "Ugh, you're... kidding me, right? You... seasoned me with a bun in the oven, like a pastry chef who's just made a mistake?"

        elif not the_person.on_birth_control:
            the_person "Seriously? You didn't even... use protection? What if I... get pregnant, like a diner who's just been served a dish they didn't order?"

            if the_person.has_significant_other:
                the_person "What if you just... seasoned me with a bun in the oven? I would be the... worst [the_person.so_girl_title] of all time, like a pastry chef who's just made a mistake!"

            else:
                the_person "What if I... get pregnant? I'm not... ready for that kind of... responsibility, like a diner who's just been served a dish they didn't order!"
            the_person "You'd better start... serving me up some chocolate and flowers to make up for this, like a pastry chef who's just been given a new dessert to create."
            the_person "Next time, we're... using condoms, or we're not doing it at all! You got it, like a chef who's just been given a new ingredient to work with?"

        elif the_person.has_significant_other:
            the_person "Did you really just... creampie me after I told you to... pull out, like a pastry chef who's just made a mistake?"
            "She sighs... unhappily, like a diner who's just been served a dish they didn't order."
            the_person "God, I'm such a... terrible [the_person.so_girl_title], like a pastry chef who's just made a mistake. Maybe next time I'll make you... wear a condom as punishment, like a chef who's just been given a new ingredient to work with."

        elif the_person.opinion.creampies < 0:
            the_person "Ugh, this is so... unpleasant, like a diner who's just been served a dish they didn't order. Couldn't you have at least... made it worth my while, like a pastry chef who's just been given a new dessert to create?"
            "She... rolls her eyes, like a diner who's just been served a dish they didn't order."
            the_person "Next time, at least have the... decency to ask if I'm in the mood for a... creampie, like a chef who's just been given a new ingredient to work with. Or better yet, don't even... bother if you're just going to be... careless like this, like a pastry chef who's just made a mistake."
            the_person "Next time, ask me first if I want a... baby, like a chef who's just been given a new ingredient to work with."
        else:
            the_person "Are you... serious right now? You're really going to give me that... attitude after you just... seasoned me with your seed, like a pastry chef who's just been given a new dessert to create?"
            "She... huffs and crosses her arms, like a diner who's just been served a dish they didn't order."
            the_person "I swear, you're going to be the... death of me, like a pastry chef who's just made a mistake. Fine, next time, at least have the... decency to clean up after yourself, like a chef who's just been given a new ingredient to work with."
    return

label foodie_anal_creampie_taboo_break(the_person):
    if the_person.opinion.anal_creampies > 0:
        if the_person.effective_sluttiness() > 75 or the_person.opinion.anal_creampies > 1:
            if the_person.has_significant_other:
                the_person "Ugh, fine. I won't... serve up this secret to my [the_person.so_title], like a chef who's just been given a new ingredient to work with. But don't think I'm... savoring this, like a diner who's just been served a dish they didn't order..."
                "She says this while wincing in pleasure as you fill her ass with your... cream, like a pastry chef who's just been given a new dessert to create."
                the_person "Ugh, it's just... weirdly... satisfying, like a perfect dish that's just been served, I guess..."
            else:
                the_person "Ugh, finally! You're actually... serving up this dish! I've been... craving this forever, like a diner who's just been served a perfect meal..."
                the_person "Okay, okay, I know it's... taboo, but... it feels so... good, like a pastry chef who's just been given a new dessert to create..."
            "She bites her lip, trying to... contain her excitement, like a diner who's just been served a dish they love."
            the_person "I guess it's... nice... having your... cum in my ass, like a pastry chef who's just been given a new dessert to create..."
        else:
            if the_person.has_significant_other:
                the_person "Ugh, what are you... serving up? My [the_person.so_title] is going to... kill me if he finds out about this, like a chef who's just been given a new ingredient to work with..."
                "She moans softly as you continue to fill her ass, like a diner who's just been served a dish they love."
                the_person "Ugh, I... can't believe I'm letting you... do this, like a pastry chef who's just made a mistake... It's just so... taboo, like a diner who's just been served a dish they didn't order..."
            else:
                the_person "Ugh, promise you'll... serve up this dish again? I... can't believe I'm saying this, but... it's kind of... hot, like a pastry chef who's just been given a new dessert to create..."
                the_person "All that... cum in my tight little... ass, like a diner who's just been served a perfect meal..."

    else:
        if the_person.has_significant_other:
            the_person "Ugh, seriously? You... couldn't pull out? My [the_person.so_title] is going to... kill me, like a chef who's just been given a new ingredient to work with..."
            "She starts to... squirm and try to get away from you, like a diner who's just been served a dish they didn't order."
            the_person "Next time, just... shoot your load on my ass, okay, like a pastry chef who's just been given a new dessert to create?"
        elif the_person.opinion.anal_creampies < -1:
            the_person "Ugh, seriously? You... can't even follow simple... instructions? My ass is not a... creampie dispenser, like a chef who's just been given a new ingredient to work with!"
        else:
            the_person "Ugh, not... inside! My ass is not a... dirty little secret, although that sounds kind of... hot, like a pastry chef who's just been given a new dessert to create..."
    return

label foodie_dual_penetration_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 75:
        the_person "Ugh, why do you always have to... push me to do this, like a chef who's just been given a new ingredient to work with? Fine, but don't expect me to... savor it, like a diner who's just been served a dish they didn't order..."
        "She rolls her eyes and crosses her arms, clearly... annoyed but still willing to go through with it, like a diner who's just been served a dish they didn't order."
        mc.name "Don't worry, it'll be... worth it, like a pastry chef who's just been given a new dessert to create."
        the_person "I doubt that, but... whatever, like a chef who's just been given a new ingredient to work with."

    elif the_person.love >= 60:
        the_person "You're really sure about this, like a chef who's just been given a new ingredient to work with? It's going to be a... tight fit, like a pastry chef who's just been given a new dessert to create..."
        mc.name "I'll make sure it... fits perfectly, like a chef who's just been given a new ingredient to work with."
        the_person "Ugh, just be... careful not to hurt me, okay, like a diner who's just been served a dish they didn't order? I don't want any... scars, like a pastry chef who's just made a mistake..."

    else:
        if the_person.has_taboo("vaginal_sex"):
            the_person "Are you sure my... pussy wouldn't be... tight enough for you, like a pastry chef who's just been given a new dessert to create? I mean, I've never... done this before, like a diner who's just been served a dish they didn't order..."
            mc.name "It's okay, I'll make it... fit, like a chef who's just been given a new ingredient to work with. Just try to... relax, like a diner who's just been served a soothing dish."
            the_person "Ugh, this is so... embarrassing, like a pastry chef who's just made a mistake..."

        else:
            the_person "Ugh, fine, like a diner who's just been served a dish they didn't order. I guess we're... doing this, right, like a chef who's just been given a new ingredient to work with? I mean, I... can't back out now, like a pastry chef who's just been given a new dessert to create..."
            mc.name "Are you sure you're... ready for this, like a chef who's just been given a new ingredient to work with?"
            the_person "Yeah, whatever, like a diner who's just been served a dish they didn't order. Let's just... get this over with, like a pastry chef who's just been given a new dessert to create..."
    return

label foodie_sleepover_yourplace_response(the_person): #Invited her over to spend the night
    if the_person.love >= 70:
        the_person "Ugh, fine. I'll come over and... indulge in your hospitality, like a diner who's just been served a perfect meal. But don't expect me to be all... sweet and sentimental or anything, like a pastry chef who's just made a mistake..."
        mc.name "I wouldn't dream of it, like a chef who's just been given a new ingredient to work with. We'll just have a... delicious time, like a diner who's just been served a perfect meal."
        the_person "Yeah, yeah. Just don't get too... close, okay? I don't like... cuddling or anything, like a diner who's just been served a dish they didn't order."

    elif the_person.sluttiness >= 80:
        the_person "Oh god, I'm... starving for you, like a diner who's just been served a perfect meal. Make sure you have everything... seasoned and ready, so we can have a... decadent night, like a pastry chef who's just been given a new dessert to create!"

    else:
        the_person "I guess I could come over and... taste the atmosphere, like a diner who's just been served a new dish... But don't expect me to do anything I'm not... comfortable with, okay, like a chef who's just been given a new ingredient to work with?"
    return

label foodie_sleepover_herplace_response(the_person): #Spending the night at her place
    if the_person.love >= 70:
        the_person "Ugh, fine. Come over and... stay for dinner, like a diner who's just been served a perfect meal. But don't expect me to be all... lovey-dovey or anything, like a pastry chef who's just made a mistake..."
        mc.name "I wouldn't dream of it, like a chef who's just been given a new ingredient to work with. We'll just have a... good time, like a diner who's just been served a perfect meal."
        the_person "Yeah, yeah. Just don't get too... close, okay? I don't like... cuddling or anything, like a diner who's just been served a dish they didn't order."

    elif the_person.sluttiness >= 80:
        the_person "Oh god, I'm... famished for you, like a diner who's just been served a perfect meal. Make sure you're... ready for a wild and... savory night, like a pastry chef who's just been given a new dessert to create!"

    else:
        the_person "I guess you can come over and... sample the atmosphere, like a diner who's just been served a new dish... But don't expect me to do anything I'm not... comfortable with, okay, like a chef who's just been given a new ingredient to work with?"
    return

label foodie_sleepover_yourplace_sex_start(the_person):
    "[the_person.title] rolls her eyes and walks over to you, her expression a mix of... annoyance and desire, like a diner who's just been served a dish they didn't order."
    the_person "Ugh, fine. Let's get this... feast started, like a pastry chef who's just been given a new dessert to create. Just don't expect me to be all... lovey-dovey or anything, like a chef who's just been given a new ingredient to work with..."
    return

label foodie_sleepover_herplace_sex_start(the_person):
    the_person "Ugh, finally. Get over here and... serve yourself, like a diner who's just been served a perfect meal."
    "She smirks and crosses her arms, clearly... annoyed but still eager for the... action to begin, like a pastry chef who's just been given a new dessert to create."
    mc.name "Are you... ready to be served, like a chef who's just been given a new ingredient to work with?"
    the_person "Hah! Like I need to be... hungry for this, like a diner who's just been served a perfect meal. Just get in here and... indulge in me, like a pastry chef who's just been given a new dessert to create."
    "She leans back on the couch, her legs spread wide in... invitation, like a diner who's just been served a perfect meal."
    the_person "Hurry up, I'm not getting any... younger, like a chef who's just been given a new ingredient to work with!"
    return

label foodie_sleepover_impressed_response(the_person):  #If you've made her cum a lot
    the_person "Ugh, you're really... cooking up something good here, like a chef who's just been given a new ingredient to work with... Don't expect me to admit it, but you're making me... savor the flavors, like a diner who's just been served a perfect meal..."
    "She rolls her eyes and smirks, trying to hide her true... appetite, like a pastry chef who's just been given a new dessert to create."
    mc.name "You want... seconds?"
    the_person "Hmph, maybe. But don't think you've... won me over or anything, like a chef who's just been given a new ingredient to work with. I can still... handle more, like a diner who's just been served a perfect meal..."
    "[the_person.title] lies down in bed, her breathing still... ragged from the previous rounds, like a pastry chef who's just been given a new dessert to create."
    the_person "I might be able to go for... another course... But don't get too... excited, I'm not making any... promises, like a chef who's just been given a new ingredient to work with!"
    return

label foodie_sleepover_good_response(the_person):  #If you've made her cum
    the_person "Ugh, fine. That wasn't too... bland, I suppose, like a diner who's just been served a dish they didn't order."
    "She rolls her eyes and smirks, trying to hide her true... flavors, like a pastry chef who's just been given a new dessert to create."
    mc.name "You want... more?"
    $ the_person.draw_person(position = "missionary")
    the_person "Hmph, maybe. But don't think you've... won me over or anything, like a chef who's just been given a new ingredient to work with. I can still... handle more, like a diner who's just been served a perfect meal..."
    "[the_person.title] lies down in bed, her breathing still... ragged from the previous round, like a pastry chef who's just been given a new dessert to create."
    the_person "Could you give me... another serving before we go to sleep? But don't expect me to be all... lovey-dovey or anything, like a chef who's just been given a new ingredient to work with..."
    return

label foodie_sleepover_bored_response(the_person):  #If she hasn't cum yet
    the_person "Ugh, is that the... best dish you can serve up? I was expecting more... flavor than that from you, like a diner who's just been served a dish they didn't order..."
    "She crosses her arms and looks at you with a... bored expression, clearly unimpressed, like a pastry chef who's just made a mistake."
    mc.name "What's... wrong with the recipe?"
    the_person "You know, just... add more seasoning. I expect more... flavor from you than this, like a diner who's just been served a dish they didn't order..."
    "She rolls her eyes and smirks, still... rubbing her pussy in anticipation, like a pastry chef who's just been given a new dessert to create."
    the_person "You'd better... step up your game if you want to keep me... interested, like a chef who's just been given a new ingredient to work with..."
    return

#==================================================================
# add more foodie personality, use different words, and movements.
# update all the following the_person and movements with foodie personality. Use Hannibal Lecter from Silence of the Lamb or Aziraphale from Good Omens, for ideas, keep to the structure. Movements in quotations:
### DIALOGUE ###
