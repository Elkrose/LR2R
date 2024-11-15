### PERSONALITY CHARACTERISTICS ###
# goudere (A character who relentlessly pursues their own vision of their love interest's desires, which they typically misunderstand in some comically over-the-top fashion.)
# Goudere (JP) is a term for a character who has an idealized notion of their love interest, believing that they are a magnificent and powerful being who is more important than others and deserves to rule the world. They will stop at nothing to obtain whatever they want their love interest to have, even if the love interest explains to the goudere that this is not necessary at all. They are unstoppable forces that do whatever they please for their love interest, purely out of their love for them. Due to their insane devotion to them, they will go to unimaginable lengths to give to their love interest what they believe is the best for them creating uncomfortable and comical situations that can even put the love interest in trouble. ex Albedo from Overlord
### DIALOGUE ###
label goudere_introduction(the_person):
    mc.name "Excuse me, could I bother you for a moment?"
    "She freezes, then turns around slowly to face you."
    mc.name "Oh my goodness! You have no idea how long I've been searching for someone like you!"
    "Her eyes widen in surprise as she takes a step back."
    $ the_person.change_happiness(-2)
    mc.name "I mean, just look at that enchanting smile and those captivating eyes! They're practically begging for someone to sweep them off their feet!"
    "She blushes deeply, trying to hide her discomfort."
    $ the_person.set_title()
    $ the_person.set_possessive_title()
    the_person "My name is [the_person.name]. Is that all you wanted to know?"
    $ the_person.change_happiness(-3)
    mc.name "Oh, no! Of course not! I was just getting started!"
    return

label goudere_greetings(the_person):
    if the_person.love < 0:
        the_person "Oh, great! What do you want from me now?"
    elif the_person.happiness < 90:
        the_person "Hey there... I hope your day is going better than mine."
    else:
        if the_person.sluttiness > 60:
            if the_person.obedience > 180:
                the_person "Hello [the_person.mc_title], how can I serve you today? Is there anything in particular that has caught your eye?"
            else:
                the_person "Hey there [the_person.mc_title], I hope this is for pleasure and not business."
        else:
            if the_person.obedience > 180:
                the_person "Hello [the_person.mc_title], it's nice to see you again."
            else:
                the_person "Hey, what do you want? Can't you see I'm busy?"
    return

label goudere_sex_responses_foreplay(the_person):
    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] moans enthusiastically, clearly enjoying herself already."
        else:
            "[the_person.possessive_title!c] smiles happily to herself as she feels your touch."

    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            the_person "Oh fuck, I love how you're touching me!"
        else:
            the_person "This feels really good... Keep going [the_person.mc_title]."

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            the_person "It's incredible how much I enjoy your touch!"
        else:
            the_person "Mmm, keep going [the_person.mc_title]. You're making me feel amazing."

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "Oh god, I need you to touch every inch of my body! I'm your dirty slut and you can do whatever you want with me!"
        else:
            the_person "Touch me [the_person.mc_title], I'm yours completely."
    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                the_person "Oh fuck, I can feel myself getting close to cumming! Your touch is driving me wild!"
            else:
                the_person "The way you make me feel is so different from my [the_person.so_title]. It's like your touch ignites a fire inside of me."
        else:
            the_person "Don't stop! I can feel myself getting close to cumming, and I want it all!"

    return

label goudere_sex_responses_oral(the_person):
    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] giggles with excitement, her eyes sparkling."
            the_person "Go down on me [the_person.mc_title], you know how I want it..."
        else:
            "[the_person.possessive_title!c] smiles excitedly as she anticipates your actions."
            the_person "Oh fuck yes, you're really going to... Oh god that feels so good..."
    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            the_person "Mmm, I love getting some good head."
        else:
            the_person "Fuck yeah, that feels really nice..."
    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            the_person "Eat me out [the_person.mc_title], your tongue feels amazing!"
        else:
            the_person "That's so fucking good, you have no idea..."
    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "Mmm, lick that pussy! Ah!"
        else:
            the_person "Oh god yes! Yes! Don't stop..."
    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                the_person "Fuck fuck fuck, that's it right there!"
            else:
                the_person "My [the_person.so_title] never eats me out like this, [the_person.mc_title]!"
                the_person "[the_person.so_title] will never know what he's missing! [the_person.mc_title], you're incredible!"
        else:
            the_person "Don't stop! You're going to make me cum my brains out, and I don't care who knows it!"

    return

label goudere_sex_responses_vaginal(the_person):
    if the_person.energy < 10:
        call low_energy_sex_responses_vaginal(the_person) from _vt_goudere_call_low_energy_sex_responses_vaginal_10
        return

    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            $ play_moan_sound()
            "[the_person.possessive_title!c] moans and writhes in pleasure, her eyes closed tightly."
            the_person "Oh god, your cock feels amazing inside me!"
        else:
            "[the_person.possessive_title!c] bites her lip and stifles a moan as she tries to maintain some semblance of control."

    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            the_person "Fuck, I love how your cock feels inside me! Keep going!"
        else:
            the_person "Oh... Your cock is so good."

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            the_person "Mmm, you're fucking me so well! I love it!"
        else:
            the_person "Ah... You're really getting to me."

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "Fuck my pussy hard, use me like your dirty little slut! I want your cock to make me cum!"
        else:
            the_person "Oh fuck yes, keep going and I'll cum for sure."
    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                the_person "Fuck... Your cock is making me crazy! I want you to make me cum!"
            else:
                the_person "Don't stop fucking me, [the_person.so_title] will never know what he's missing out on with this incredible feeling!"

        else:
            the_person "Oh fuck yes, keep going and I'll cum for sure."

    return

label goudere_sex_responses_anal(the_person):
    if the_person.energy < 10:
        call low_energy_sex_responses_anal(the_person) from _vt_goudere_call_low_energy_sex_responses_anal_10
        return

    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            the_person "Just go slowly and I should be okay..."
            "She doesn't sound too confident about that."
        else:
            $ the_person.call_dialogue("surprised_exclaim")
            the_person "Deep breaths [the_person.title], deep breaths..."
            "She pants to herself, trying her best to stay in control of the situation."

    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            $ the_person.call_dialogue("surprised_exclaim")
            the_person "I'm never going to get used to being stretched out like this."
        else:
            the_person "Oh... Oh fuck my ass!"

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            the_person "Gah! Ah! Fuck!"
        else:
            the_person "God, I won't be able to sit for a week after this..."

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            if mc.condom:
                the_person "Give it to me, punish that slutty ass with your big cock!"
            else:
                the_person "Give it to me, fuck my horny asshole raw!"
        else:
            the_person "Ah! Why does your cock have to be so fucking big?!"
    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                the_person "Fuck, I can't believe I'm going to cum from your cock up my ass!"
            else:
                the_person "Wreck my ass [the_person.mc_title], send me back to my [the_person.so_title] gaping and ruined! Ah!"

                the_person "I might have a [the_person.so_title], but he doesn't drive me crazy like you do [the_person.mc_title]!"
                the_person "Make me cum my brains out! Screw my [the_person.so_title], he's not half the man you are!"
        else:
            $ the_person.call_dialogue("surprised_exclaim")
            the_person "I can't believe it but I think I'm going to cum soon!"

    return

label goudere_climax_responses_foreplay(the_person):
    if the_person.sluttiness > 50:
        the_person "Oh fuck yes, I'm going to cum! I'm cumming!"
    else:
        $ the_person.call_dialogue("surprised_exclaim")
        the_person "You're making me feel so good [the_person.mc_title], I think I'm about to cum!"
        "She goes silent, then lets out a shuddering moan."
    return

label goudere_climax_responses_oral(the_person):
    if the_person.sluttiness > 70:
        the_person "Fuck yes, I'm going to cum! Make me cum!"
    else:
        $the_person.call_dialogue("surprised_exclaim")
        the_person "Oh my god, you're so good at that [the_person.mc_title]! You've got me right on the edge... I think I'm about to cum!"
    return

label goudere_climax_responses_vaginal(the_person):
    if the_person.sluttiness > 70:
        if the_person.arousal_perc > 120:
            the_person "Yes! Keep going, make your little slut cum!"
        else:
            the_person "Ah! More! I'm going to... Ah! Cum! Fuck!"
        "She closes her eyes and squeals with pleasure."
    else:
        the_person "Oh god, I'm going to... Oh fuck me! Ah!"
    return

label goudere_climax_responses_anal(the_person):
    if the_person.sluttiness > 70:
        if the_person.arousal_perc > 120:
            the_person "Ah yes, shove your big cock into my slutty ass. Make your little bitch cum!"
        else:
            $the_person.call_dialogue("surprised_exclaim")
            the_person "Oh fuck, it feels so huge in my ass! You're going to make me cum!"
        the_person "Ah! Mmhmmm!"
    else:
        the_person "Oh fucking shit, I think you're going to..."
        "She barely finishes her sentence before her body is racked with pleasure."
        $the_person.call_dialogue("surprised_exclaim")
        the_person "Cum! Ahhhh!"
    return

label goudere_clothing_accept(the_person):
    if the_person.obedience > 180:
        the_person "You think it will look good on me? I guess that's all I need to hear then."
    else:
        the_person "Hey, thanks! That's a nice look; I really like it!"
    return

label goudere_clothing_reject(the_person):
    if the_person.should_wear_uniform:
        the_person "Hey, I guess I should get my uniform sorted out, right? One second."
    elif the_person.obedience > 180:
        the_person "I don't... I apologize for any inconvenience this may cause, but I really can't see myself wearing something like this. Thank you for considering me."
    else:
        if the_person.sluttiness > 60:
            the_person "Did you even leave anything to the imagination? There's no way I could pull this off."
        else:
            the_person "There isn't much of an outfit in that outfit. Thanks for thinking of me, but it just won't work."
    return

label goudere_clothing_review(the_person):
    if the_person.outfit.cum_covered:
        if (the_person.sluttiness > 40 and the_person.opinion.being_covered_in_cum >=0) or the_person.opinion.being_covered_in_cum > 0:
            the_person "I guess I can't walk around covered in cum all day, huh?"
            "[the_person.title] starts to wipe up the biggest splashes of cum on her."
            the_person "Let me know if see any big splashes of cum I miss."
        else:
            the_person "Fuck, I need to clean myself up! Give me a sec, and let me know if I missed anything, okay?"
            "[the_person.title] wipes herself down, making sure she's clean from head to toe."

    if the_person.obedience > 180:
        the_person "*sighs* I'm a mess! Let me go get myself cleaned up for you."
    else:
        if the_person.sluttiness > 40:
            the_person "I don't think everyone would appreciate seeing me like this, huh? I'll be right back, just need to clean myself up."
        else:
            the_person "Damn, everything's out of place after that! Just gimme a sec, and I'll find a mirror to fix my appearance for you."
    "[the_person.title] cleans herself up, making sure she looks presentable again."
    $ the_person.apply_planned_outfit(show_dress_sequence = True)
    return

label goudere_strip_reject(the_person, the_clothing, strip_type = "Full"):
    if the_person.obedience > 180:
        the_person "Could we leave my [the_clothing.display_name] on for now? I'd feel more comfortable that way."
    elif the_person.obedience < 70:
        the_person "No, nope! Not until you earn it. I decide when my [the_clothing.display_name] comes off."
    else:
        the_person "Not yet... let's get a little warmer first, okay? Then maybe we can talk about taking off my [the_clothing.display_name]."
    return

label goudere_strip_obedience_accept(the_person, the_clothing, strip_type = "Full"):
    "[the_person.title] laughs nervously as you start to slide her [the_clothing.display_name] away."
    if the_person.obedience > 180:
        the_person "Hey, I don't know if that's a good idea... Could we just leave it on for now?"
    else:
        the_person "Hey, let's not take this too far..."
    return

label goudere_grope_body_reject(the_person):
    if the_person.effective_sluttiness("touching_body") < 5: #Fail point for touching shoulder
        the_person "Ah!"
        "[the_person.title] steps back as you touch her, then laughs awkwardly."
        the_person "Haha, sorry... Your hand just kind of came out of nowhere."
        mc.name "Sorry, I didn't mean to startle you."
        the_person "Don't worry about it! I want you to touch me, just give me a little warning next time, okay?"
        "She seems a little uncomfortable, but you both laugh about it and try and move on."
    else: #Fail point for touching waist
        the_person "Hey, could you just..."
        "[the_person.title] takes your hand and pulls it off of her waist."
        the_person "... Keep your hands to yourself? Thanks."
        mc.name "Oh yeah, of course. My bad."
        the_person "No problem, just don't make a habit of it. Alright?"
        "She doesn't say anything else, but she still seems uncomfortable with the situation."
    return

label goudere_sex_accept(the_person, the_position):
    if the_person.sluttiness > 70:
        if the_person.obedience < 70:
            the_person "Let's do it. Once you've had your fill I have a few ideas we could try out."
        else:
            if the_position.skill_tag == "Foreplay":
                the_person "I was hoping you would suggest that, just thinking about it gets me excited."
            elif the_position.skill_tag == "Oral":
                if "getting head" in the_position.opinion_tags:
                    the_person "Oh [the_person.mc_title], get down there and make me cum my brains out."
                else:
                    the_person "Come here, I need to suck on that lovely dick right now."
            else:
                the_person "Oh yes, [the_person.mc_title], I need you to fuck me hard and deep."
    else:
        the_person "Come here [the_person.mc_title], let's do it."
    return

label goudere_sex_obedience_accept(the_person):
    if the_person.sluttiness > 70:
        the_person "I shouldn't... but if you want to try it out I'm game. Try everything once, right?"
    else:
        if the_person.obedience > 180:
            the_person "If that's what you want to do then I will do what you tell me to do."
        else:
            the_person "I guess I can be a little naughty tonight, [the_person.mc_title]. Let's see where this goes."
    return

label goudere_sex_gentle_reject(the_person):
    if the_person.sluttiness > 50:
        the_person "Not yet [the_person.mc_title], get me warmed up first."
    else:
        the_person "Eh, not yet [the_person.mc_title]. Let's take our time and see where this goes."
    return

label goudere_sex_angry_reject(the_person):
    if the_person.has_significant_other:
        the_person "What? I have a [the_person.so_title], so you can forget about doing anything like that. Ever."
        "She glares at you, then walks away with her nose in the air, clearly offended and disgusted by your suggestion."
    elif the_person.sluttiness < 20:
        the_person "I'm sorry, what!? No, you've massively misread the situation, get the fuck away from me!"
        "[the_person.title] glares at you and steps back, her cheeks flushed with anger and embarrassment."
    else:
        the_person "What? That's fucking disgusting, I can't believe you'd even suggest that to me!"
        "[the_person.title] glares at you and steps back, her eyes narrowed in anger and a hint of fear."
    return

label goudere_seduction_response(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 50:
            the_person "Oh, I think I know what you need right now. Let me take care of you."
            "[the_person.title] smirks seductively and steps closer to you, her eyes filled with desire."
        else:
            the_person "Right now? Okay, lead the way I guess."
    else:
        if the_person.sluttiness > 50:
            the_person "Mmm, you're feeling as horny as me then? Come on, let's go."
            "[the_person.title] takes your hand and leads you off to find some place out of the way with a sultry smile."
        elif the_person.sluttiness > 10:
            the_person "I know that look you're giving me, I think I know what you want."
        else:
            the_person "[mc.name], I know what you mean... Okay, I can spare a few minutes."
            "[the_person.title] hesitates for a moment before nodding and stepping closer to you, her cheeks flushed with anticipation."
    return

label goudere_seduction_accept_crowded(the_person):
    if not the_person.has_significant_other:
        if the_person.sluttiness < 20:
            the_person "Alright, let's slip away for a few minutes and you can convince me a little more."
            "[the_person.title] smirks seductively but keeps her voice low to avoid drawing attention in the crowded room."
        elif the_person.sluttiness < 50:
            the_person "Come on, I know someplace nearby where we can get a few minutes privacy."
            "[the_person.title] takes your hand and leads you, her eyes locked onto yours with desire."
        else:
            the_person "Oh my god. I hope you aren't planning on making me wait [the_person.mc_title], because I don't know if I can!"
    else:
        if the_person.sluttiness + (5*the_person.opinion.cheating_on_men) > 50:
            the_person "Fuck, let's get this party started!"
            "[the_person.title] leans in close to you and whispers seductively, her breath hot against your ear."
            the_person "I hope you don't mind that I've got a [the_person.so_title], because I sure as hell don't right now!"
        else:
            the_person "Damn it, you're bad for me [the_person.mc_title]... Come on, we need to go somewhere quiet so my [the_person.so_title] doesn't find out about this."
    return

label goudere_seduction_accept_alone(the_person):
    if not the_person.has_significant_other:
        if the_person.sluttiness < 20:
            the_person "Well, I think you deserve a chance to impress me."
        elif the_person.sluttiness < 50:
            the_person "Mmm, well let's get this party started and see where it goes."
        else:
            the_person "Fuck, I can't believe how horny you make me! Come on, I need to feel your touch!"
    else:
        if the_person.sluttiness + (5*the_person.opinion.cheating_on_men) > 50:
            the_person "Fuck, you know how to turn me on in ways my [the_person.so_title] never can... Come here and show me what I've been missing!"
        else:
            the_person "You're such bad news for me [the_person.mc_title], but all I can ever think of is you when we're alone like this..."
    return

label goudere_seduction_refuse(the_person):
    if the_person.sluttiness < 20:
        the_person "Sorry [the_person.mc_title], I'm just not in the mood for flirting or fooling around right now."
        "[the_person.title] shrugs unapologetically."
    elif the_person.sluttiness < 50:
        the_person "I gotta admit, you're really tempting me there [the_person.mc_title], but I just ain't in the mood to fool around right now. Maybe some other time when we can have a lot of fun together."
    else:
        the_person "Shit, that sounds like it could be a whole bunch of fun [the_person.mc_title], but I'm just not feeling it right now. Hang onto that thought and maybe some other time when we can fool around together."
    return

label goudere_compliment_response(the_person):
    mc.name "Hey [the_person.fname]. How are you? You're looking quite perky today."
    if the_person.is_at_work:
        if (the_person.is_employee or the_person.is_strip_club_employee) and the_person.is_wearing_uniform:
            call goudere_flirt_response_employee_uniform_low(the_person) from _call_goudere_flirt_response_employee_uniform_low_compliment_response
        elif the_person.is_at_job(prostitute_job):
            the_person "I'm doing great, babe. How about us having some fun together?"
        elif the_person.sluttiness > 50:
            the_person "I'm doing great, and you look quite yummy yourself."
        else:
            the_person "Oh stop it, you charmer! But thanks, I'm good."
    else:
        the_person "Aww, thank you for noticing. I'm doing well."
    "You chat with [the_person.possessive_title] for a while and slip in a compliment when you can. She is enjoying all the attention."
    return

label goudere_compliment_response_girlfriend(the_person):
    mc.name "Hey [the_person.title], you look quite sexy this [StringInfo.time_of_day_string]."
    if the_person.is_at_work:
        if (the_person.is_employee or the_person.is_strip_club_employee) and the_person.is_wearing_uniform:
            call goudere_flirt_response_employee_uniform_mid(the_person) from _call_goudere_flirt_response_employee_uniform_mid_compliment_response_girlfriend
            $ the_person.call_dialogue("flirt_response_employee_uniform_mid")
        elif the_person.sluttiness > 50:
            the_person "Mmm, thank you [the_person.mc_title]. Wanna find out how sexy I am...?"
        else:
            the_person "Ah, really? Thanks, [the_person.mc_title]. You are not looking so bad yourself."
    else:
        the_person "Aww, thank you, I'm good. You are looking quite hot yourself..."
    "You chat with [the_person.possessive_title] for a while, making sexy references where you can. She is quite charmed by your efforts."
    return

label goudere_compliment_response_affair(the_person):
    mc.name "Hey [the_person.title], you look absolutely stunning this [StringInfo.time_of_day_string]."
    if the_person.is_at_work:
        if (the_person.is_employee or the_person.is_strip_club_employee) and the_person.is_wearing_uniform:
            call goudere_flirt_response_employee_uniform_mid(the_person) from _call_goudere_flirt_response_employee_uniform_mid_compliment_response_affair
        elif the_person.sluttiness > 50:
            the_person "Mmmm, thank you [the_person.mc_title], wanna go somewhere a little more private? I can show you how stunning I am..."
        else:
            the_person "Hush, [the_person.mc_title]!...You like my outfit? Let's find someplace quiet and I'll show you what I look like underneath it..."
    else:
        the_person "You like this? Take me to dinner and we can explore other parts..."
    "You keep chatting with [the_person.possessive_title] for a while, slipping in a few more compliments. She is quite enamoured by your attentiveness."
    return

# Make this code better with goudere personality ```
label goudere_flirt_response(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 50:
            the_person "You know that all you have to do is ask and it's all yours."
        else:
            the_person "Thank you [the_person.mc_title], I'm glad you're enjoying the view."
    elif the_person.has_significant_other:
        if the_person.sluttiness + (the_person.opinion.cheating_on_men*5) > 50:
            the_person "Then why don't you do something about it? Come on, we don't have to tell my [the_person.so_title] anything at all, right?"
            "[the_person.title] winks and spins around, giving you a full look at her body."
        else:
            the_person "You're playing with fire [the_person.mc_title]. I've got a [the_person.so_title], and I don't think he'd appreciate you flirting with me."
            mc.name "What about you, do you appreciate it?"
            "She gives a coy smiles and shrugs."
            the_person "Maybe I do."
    else:
        if the_person.sluttiness > 50:
            the_person "Then why don't you do something about it? Come on, all you have to do is ask."
            "[the_person.title] smiles at you and spins around, giving you a full look at her body."
        else:
            the_person "Well thank you, play your cards right and maybe you'll get to see a little bit more."
            the_person "You'll have to really impress me though, I sorta have high standards."
    return

label goudere_flirt_response_employee_uniform_low(the_person):
    if the_person.is_wearing_forced_uniform:
        the_person "I'm sure you like it; I'm practically naked!"
        mc.name "It's not that I don't appreciate your beauty, but I know this isn't what you wanted."
        the_person "I know, I know. It's company policy. But hey, at least it gets people talking about us, right?"
        $ mc.change_locked_clarity(5)
        "She smiles and gives you a quick turn to either side, showing off her body."
    elif the_person.judge_outfit(the_person.outfit):
        #She's in uniform and likes how it looks.
        the_person "Thanks! I think I look pretty cute in it too. It makes me feel confident and sexy at the same time."
        $ mc.change_locked_clarity(5)
        "She smiles flirtatiously, her eyes lingering on yours for a moment before she gives you a quick turn to either side, showing off her hips."
    else:
        #She's in uniform, but she thinks it's a little too slutty.
        if the_person.vagina_visible:
            # Her pussy is on display.
            the_person "I know; I wish we had more options for something a bit less revealing."
            mc.name "Well, you look incredible nonetheless."
            $ mc.change_locked_clarity(5)
            "She smiles and nods in agreement."
        elif the_person.tits_visible:
            # Her tits are out
            the_person "Thanks! I love my breasts, but sometimes I wish we could cover them up a bit more during work hours."
            mc.name "You look stunning with your tits on display; it's hard not to notice how gorgeous they are."
            $ mc.change_locked_clarity(5)
            "She blushes and looks away briefly before meeting your gaze again, her smile more flirtatious than before."
        elif the_person.underwear_visible:
            # Her underwear is visible.
            the_person "Thanks! I'm not complaining about how comfortable our uniforms are, but sometimes I wish we could wear something that covers us a bit more down there."
            mc.name "You have an incredible body; it's hard to imagine anything covering up your underwear making you look any less amazing."
            $ mc.change_locked_clarity(5)
            "She smiles and gives you a quick turn to either side, showing off her body for you."
        else:
            # It's just generally slutty.
            the_person "Well thank you! Our uniforms are definitely bold, but I think they make us stand out in a good way."
            $ mc.change_locked_clarity(5)
            "She smiles and gives you a quick turn to either side, showing off her body for you."
    return

label goudere_flirt_response_employee_uniform_mid(the_person):
    if the_person.is_wearing_forced_uniform:
        $ mc.change_locked_clarity(10)
        if the_person.vagina_visible:
            the_person "I mean, look at me! I feel like you should be throwing twenties at me every time I walk away."
        elif the_person.tits_visible:
            the_person "I mean, look at me! I feel like you should be tucking a twenty into my underwear every time I want to talk to you."
        else:
            the_person "I mean, look at it! I feel like a sexy underwear model every time I put this on."
        mc.name "Rules are rules and I can't make any exceptions, even if you look amazing in that outfit."
        "She sighs and nods."
        the_person "Yeah, I know. At least you appreciate it."
    elif the_person.judge_outfit(the_person.outfit):
        $ mc.change_locked_clarity(10)
        if the_person.tits_visible:
            the_person "Are my ladies looking good in this? *smirks*"
            "She winks and adjusts her top, giving you a better view."
            mc.name "All of you looks great, especially your... *ahems* ladies."
        else:
            the_person "Thanks! I think these uniforms look fabulous on me too. You've got some good fashion sense."
        the_person "Maybe we can go shopping together sometime and find something even sexier for me to wear."
        mc.name "That sounds like a fun plan!"
    else:
        the_person "Thanks, but I think these uniforms show off just a little too much of my fabulous body."
        $ mc.change_locked_clarity(10)
        if the_person.vagina_visible:
            the_person "I mean, look at me! I feel like you should be throwing twenties at me every time I walk away."
        elif the_person.tits_visible:
            the_person "I mean, look at me! I feel like you should be tucking a twenty into my underwear every time I want to talk to you."
        else:
            the_person "I mean, look at it! I feel like an underwear model every time I get dressed for work."
        the_person "I mean, look at it! I feel a bit exposed in this outfit."
        mc.name "I understand your concerns, but these uniforms are necessary for our business."
        "She sighs and nods."
        the_person "Yeah, I know. At least you're enjoying it."
    return

label goudere_flirt_response_low(the_person): 
    # She's in her own outfit. 
    $ mc.change_locked_clarity(5) 
    if the_person.tits_visible: 
        the_person "Are my tits looking good in this outfit?"
        "She winks and adjusts her top, giving you a better view."
        mc.name "You look amazing! Your tits are really popping out of it."
    else: 
        the_person "Thanks! I think my outfit looks pretty hot on me too." 
        mc.name "I agree, it's a great choice for you!" 
    if the_person.vagina_visible: 
        $ mc.change_locked_clarity(5)
        the_person "I mean, look at me! I feel a bit exposed in this outfit."
        the_person "I mean, look at it! It's not exactly my style, but hey, you seem to like it!" 
        mc.name "It is a bit revealing, but I guess it shows off your fabulous body well enough."
    else: 
        the_person "I mean, look at it! It's not exactly my style, but hey, you seem to like it!" 
        mc.name "It's an interesting choice for sure, but I think you pull it off well enough."
    the_person "I mean, look at it! It's not exactly my style, but hey, you seem to like it!" 
    mc.name "It is a bit revealing, but I guess it shows off your fabulous body well enough."
    return

label goudere_flirt_response_low1(the_person):
    if the_person.has_significant_other:
        the_person "You're playing with fire [the_person.mc_title]. I've got a [the_person.so_title], and I don't think he'd appreciate you flirting with me."
        mc.name "What about you, do you appreciate it?"
        "She gives a coy smiles and shrugs."
        the_person "Maybe I do."
    else:
        the_person "Well thank you, play your cards right and maybe you'll get to see a little bit more."
        the_person "You'll have to really impress me though, I have high standards."
    $ mc.change_locked_clarity(5)
    return

label goudere_flirt_response_mid(the_person):
    if mc.location.person_count > 1 and the_person.effective_sluttiness("kissing") < (25 - (5*the_person.opinion.public_sex)):
        $ mc.change_locked_clarity(10)
        if the_person.tits_visible:
            the_person "Are you sure you don't like my tits in this outfit?"
            "She winks and wiggles her shoulders, setting her boobs jiggling for you."
            mc.name "You look fantastic, especially with those boobs on display."
            the_person "Good answer! I knew you'd like it when I picked it out this morning."
        else:
            the_person "Aw, thanks! I thought this was a pretty hot look when I got dressed today."

        the_person "Maybe one day I'll invite you shopping so you can tell me what else to wear that turns you on."
        mc.name "I already have some ideas in mind."
        the_person "Oh, really? You must be quite the connoisseur of sexy outfits!"

    else:
        the_person "Thanks for noticing my hot ass! Maybe we should grab a drink and see where things go?"
        $ the_person.draw_person(position = "back_peek")
        $ mc.change_locked_clarity(10)
        the_person "Good, right?"
        mc.name "I'd love to take you out, [the_person.possessive_title]."
        $ the_person.draw_person()
    return

label goudere_flirt_response_mid1(the_person):
    $ mc.change_locked_clarity(10)
    the_person "Thanks, I do look amazing in this outfit."
    if (the_person.has_skirt or the_person.has_dress) and not the_person.has_thigh_high_socks:
        mc.name "You could change it up with some high stockings, I would like to see that."
        the_person "I bet you would, you naughty boy."
    the_person "Thanks for noticing my hot ass! Maybe we should grab a drink and see where things go?"
    if the_person.has_significant_other:
        the_person "Sure, my [the_person.so_title] doesn't mind, does he?"
    else:
        the_person "I could use a pick-me-up once in a while."
    the_person "Just let me know when, I would love to."
    return

label goudere_flirt_response_high(the_person):
    if mc.location.person_count > 1 and the_person.effective_sluttiness() < (25 - (5*the_person.opinion.public_sex)): # There are other people here, if she's not slutty she asks if you want to find somewhere quiet
        the_person "... to have me? Oh my dear [mc.name], I must say that your boldness is quite... appealing. *smirks*"
        the_person "But, as much as I would love to indulge in such desires with you, we must be mindful of our surroundings."
        th_person "Perhaps we could find a more private location where we can truly let our passions run wild?"
        "She winks then glances around before smiling mischievously."
        the_person "What do you say, my sweet [mc.name]?"
        menu:
            "Find somewhere more quiet\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                mc.name "Then let's find somewhere that isn't here."
                the_person "Oh my dear [mc.name], I must say that your eagerness is quite... arousing. *smirks*"
                the_person "Let us proceed to a more private location where we can truly indulge in our desires. *winks* What do you say, my sweet [mc.name]?"
                call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_goudere_flirt_response_high_2
                the_person "What's your plan? ... to have me?"
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
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _vt_goudere_call_fuck_person_49
                else:
                    the_person "Or perhaps... would... you... like..."
                    the_person "Maybe I can get these girls out for you. Does that sound nice?"
                    if the_person.has_taboo("touching_body"):
                        $ the_person.call_dialogue("touching_body_taboo_break")
                        $ the_person.break_taboo("touching_body")
                        "She takes your hand and pull you close against her placing it on her chest. She looks into your eyes."
                    else:
                        "You answer by pulling her close against you and grabbing her breast."
                    call fuck_person(the_person, private = True, start_position = standing_grope, skip_intro = True) from _call_fuck_person_goudere_flirt_grope
                $ the_person.call_dialogue("sex_review", the_report = _return)
                call mc_restore_original_location(the_person) from _call_mc_restore_original_location_goudere_flirt_response_high_2

            "Just flirt":
                mc.name "Not here, huh? How about back at your place then?"
                the_person "Bold. I like it. Maybe if you buy me dinner you'll get your chance."

    else:
        if mc.location.person_count == 1: #You're alone, so she just didn't meet the sluttiness threshold
            "[the_person.possessive_title!c] bites her lower lip and glances around, confirming you're alone."
            the_person "Well it's just the two of us here, so now's your chance to find out. What's your plan?"
        else:  # You aren't alone but she's still into it.
            the_person "Oh my dear [mc.name], I must say that your boldness is quite... alluring. smirks"
            if the_person.has_large_tits: #Bounces her tits for you
                $ mc.change_locked_clarity(15)
                "[the_person.title] grabs her tits and jiggles them for you."
                the_person "Maybe I can get these girls out for you. Does that sound nice?"
            else: #No big tits, so she can't bounce them (as much)
                "[the_person.title] runs her hands over her hips sensually, obviously encouraging you to take things further."

        menu:
            "Touch her" if not the_person.is_willing(kissing):
                "You step closer to [the_person.title] and move your hands down her waist."
                if the_person.has_taboo("touching_body"):
                    $ the_person.call_dialogue("touching_body_taboo_break")
                    $ the_person.break_taboo("touching_body")
                call fuck_person(the_person, start_position = standing_grope, private = False) from _call_fuck_person_flirt_response_goudere_touching

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
                call mc_move_to_private_location(the_person) from  _call_mc_move_to_private_location_goudere_flirt_response_high
                call fuck_person(the_person, start_position = kissing, private = _return, skip_intro = True) from _vt_goudere_call_fuck_person_50
                $ the_person.call_dialogue("sex_review", the_report = _return)
                call mc_restore_original_location(the_person) from _call_mc_restore_original_location_goudere_flirt_response_high

            "Just flirt":
                $ the_person.draw_person()
                mc.name "Very tempting, but you're going to have to contain yourself for now."
                "[the_person.title] runs her hands over her hip sensually, obviously encouraging you to take things further..."
                the_person "You're so cruel. Maybe you can take me out to dinner to make up for it."
    return

label goudere_flirt_response_low_energy(the_person):
    if the_person.sluttiness > 40:
        the_person "Oh, thank you darling! I'm feeling a bit slutty today."
        "She winks and leans in closer to you."
    else:
        the_person "Thank you for your kind words. Maybe another time when I have more energy?"
    return

label goudere_flirt_response_girlfriend(the_person):
    if mc.location.person_count > 1:
        # There are other people around, so she'll only start making out with you if she's slutty.
        if the_person.effective_sluttiness("kissing") < (25 - (5*the_person.opinion.public_sex)):
            # Not very slutty, so she wants to find somewhere private
            "You and [the_person.possessive_title] are kissing passionately."
            "She pulls you against her and kisses you intensely. She smiles when she breaks the kiss a moment later."
            the_person "There, that's how you should show a woman how you feel."
            mc.name "Uh huh, I think I've got the idea..."
            "You put your arms around her and kiss her back, matching her own intensity."
            the_person "Oh darling, that feels wonderful... I think we should find somewhere more private to continue."
            menu:
                "Find somewhere more quiet\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                    mc.name "Why wait? Come on, I'm sure we can find somewhere quiet."
                    the_person "That eager, huh? Alright, let's go!"
                    "You and [the_person.possessive_title] hurry off, searching for a private spot."
                    call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_goudere_flirt_response_girlfriend_2
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _vt_goudere_call_fuck_person_76
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_goudere_flirt_response_girlfriend_2

                "Just flirt":
                    $ mc.change_locked_clarity(10)
                    "You reach behind [the_person.possessive_title] and grab her ass, giving it a firm squeeze."
                    mc.name "Alright, I'll be patient. This ass is worth waiting for."
                    "She wiggles her hips back against your hand."
                    the_person "Damn right it is."

        else:
            the_person "Oh my goodness darling, you're so hot and bothered. Come here, [mc.name]."
            "She pulls you against her and kisses you intensely. Her lips are soft and inviting, and she moans deeply as she breaks the kiss a moment later."
            the_person "Mmm... You're so delicious. I can't wait to get you alone and show you how much I want you."
            menu:
                "Make out":
                    "You and [the_person.possessive_title] are making out intensely, grinding against each other."
                    "[the_person.title] presses her body against you in response, grinding her hips against your thigh."
                    the_person "Oh my god, [mc.name]. You're so confident and sexy. I can't resist your charms."
                    call mc_move_to_private_location(the_person) from  _call_mc_move_to_private_location_goudere_flirt_response_girlfriend
                    call fuck_person(the_person, start_position = kissing, private = _return, skip_intro = True) from _vt_goudere_call_fuck_person_77
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_goudere_flirt_response_girlfriend

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
                call fuck_person(the_person, start_position = kissing, skip_intro = True) from _vt_goudere_call_fuck_person_78
                $ the_person.call_dialogue("sex_review", the_report = _return)
                $ the_person.review_outfit()

            "Just flirt":
                "You reach your arms around her waist and grab her ass, squeezing it playfully."
                mc.name "I'm sorry, but I'm going to make you wait a bit for that. I just like seeing you get all worked up."
                "She pouts melodramatically and rubs your chest."
                the_person "Ugh, you're the worst. I was already getting so turned on..."
    return

label goudere_flirt_response_affair(the_person):
    # Lead in: mc.name "You look so good today [the_person.title], you're making me want to do some very naughty things to you."
    if mc.location.person_count > 1: #There are other people around, she's nervous about people finding out what you're doing.
        if (the_person.opinion.cheating_on_men *15) + the_person.effective_sluttiness() > 50: #SHe's turned on by flirting in public or doesn't think anything is wrong with it
            "You and [the_person.possessive_title] are kissing passionately."
            "You and [the_person.possessive_title] are making out intensely, grinding against each other."
            the_person "Oh darling, that feels good... I think we should find somewhere more private to continue."
            menu:
                "Find somewhere more quiet\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                    mc.name "Alright, let's go."
                    "You and [the_person.title] hurry off to find a quiet spot."
                    call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_goudere_flirt_response_affair
                    $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
                    "As soon as you're alone she pulls you into a deep and passionate kiss."
                    $ the_person.draw_person(position = "kissing")
                    the_person "Ah... You aren't the only one having dirty thoughts. You get me so fucking horny!"
                    "You wrap your arms around her waist and kiss her back."
                    the_person "You're so mine, and I'll make sure you get all the attention you deserve."
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _vt_goudere_call_fuck_person_79
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_goudere_flirt_response_affair
                    
                "Just flirt":
                    "You reach behind [the_person.possessive_title] and grab her ass, giving it a firm squeeze."
                    mc.name "You'll have to wait a little bit, we don't have time for all the things I want to do to you right now."
                    $ mc.change_locked_clarity(20)
                    "She glances around and checks to make sure nobody else is watching, then she slides her hand down your waist and to your crotch."
                    "[the_person.possessive_title!c] massages your bulge lightly and pouts."
                    the_person "That's a shame. I can think of so many fun things to do with this..."
                    the_person "Just don't make me wait too long, okay? I barely get any action from my [the_person.so_title]."
                    "You give her ass a slap before letting go."
                    mc.name "It won't be too long, I promise."
                    the_person "Oh, I'll be waiting for you. And when you finally get me alone, you'll see just how much I desire you."

        else: #She's shy or nervous about being discovered
            "[the_person.possessive_title!c] laughs, then shakes her head and glances around."
            the_person "You're looking pretty hot too, but you need to be a little more subtle."
            the_person "I don't want any rumours getting back to my [the_person.so_title]. That would really throw a wrench into our little affair..."
            $ mc.change_locked_clarity(15)
            "After checking again that nobody else is watching she reaches over and cups your crotch, massaging the bulge through your pants."
            the_person "Just be patient. I'll be all over this dick soon enough."
            mc.name "Alright, I think I can contain myself a little while longer."
            "She pulls her hand back and smiles."
            the_person "And when we're finally alone, you'll see just how much I'll satisfy your desires."
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
                the_person "Mmm, I like the way you touch me. You make me feel so desirable."
                call fuck_person(the_person, private = True, start_position = standing_grope, skip_intro = True) from _vt_goudere_call_fuck_person_80
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
                the_person "Oh, I'll be waiting for you. And when you finally get me alone, I'll show you just how much I crave your touch."
    return

label goudere_flirt_response_text(the_person):
    mc.name "Hey [the_person.title], what's up. I'm bored and figured we could chat."
    "There's a brief pause, then she texts back."
    if the_person.is_affair:
        the_person "I'm bored too, darling. I was just thinking about how much I want to be with you in person."
        the_person "I've been craving your touch, and I need it soon. When can we get together?"
        mc.name "Some time soon. I'll let you know."

    elif the_person.is_girlfriend:
        the_person "I'm bored too. We should get together and hang out. I need some attention from my adoring fan."
        the_person "When are you going to take me out on another date? I'm going to have to do it myself at this rate."
        mc.name "Some time soon. I'll let you know."

    elif the_person.love < 40:
        if the_person.effective_sluttiness() > the_person.love:
            the_person "Bored, huh? Well, I'm here to spice things up. What do you say we have a little fun together?"
        else:
            the_person "That sucks, being bored is the worst. I know just how to cure that, though."

    else:
        if the_person.effective_sluttiness() > the_person.love:
            the_person "Bored, huh? Well, I'm here to entertain you, so what would you like me to do?"
            the_person "I mean, let's get intimate. What would you like to do together?"
        else:
            the_person "Bored and you came to me, huh? It must be really bad."
            the_person "Alright, let's chat then. What's up with you? I'm ready to give you all the attention you deserve."
    return

label goudere_condom_demand(the_person):
    if the_person.wants_creampie:
        the_person "I want more than anything to feel you deep inside me, without any barriers."
        the_person "But, you need to put on a condom before we do anything."
        the_person "I know it can be inconvenient, but it's a necessity. I won't compromise on this."
    else:
        the_person "Oh darling, we can't have sex without protection. It's essential for our little affair."
        the_person "I know it can be inconvenient, but it's a necessity. I won't compromise on this."
    return

label goudere_condom_ask(the_person):
    if the_person.on_birth_control:
        the_person "Want a condom? I'm on the pill, but I guess it's still possible something goes wrong. But don't worry, I've got you covered."
        the_person "Besides, I need to feel you deep inside me, without any barriers. It's just for us, and I trust you to take care of me."
        $ the_person.update_birth_control_knowledge()
    elif the_person.wants_creampie:
        the_person "If you want to cum inside me, you should put on a condom. I don't want to ruin the moment, but we have to be safe."
        the_person "I know it's less fun than fucking raw, but it's still better than pulling out, right? Plus, I want to feel you fill me up completely."
        $ the_person.discover_opinion("creampies")
    else:
        the_person "Fuck, I should probably tell you to put on a condom... but I don't want to break the mood."
        the_person "I can trust you to pull out, right? We'll need to be careful, but I know you'll make it worth it."
    return

label goudere_condom_bareback_ask(the_person):
    if the_person.wants_creampie:
        if the_person.is_infertile:
            the_person "You aren't thinking of wearing a condom, are you? Fuck that, I want you to fill me up completely."
            the_person "I love the feeling of you deep inside me, bare and uninhibited."
        elif the_person.on_birth_control:
            the_person "You aren't thinking of wearing a condom, are you? Fuck that, I'm on the pill."
            the_person "You can cum right inside me, no worries. I want to feel you filling me up."
            $ the_person.update_birth_control_knowledge()
        else:
            the_person "Forget the condom [the_person.mc_title], I want you to fuck me raw."
            if not the_person.knows_pregnant:
                the_person "I want to feel you cum inside me, knowing I might be getting knocked up. That would be so fucking hot!"
            the_person "I love the idea of carrying your baby, it's a dirty little fantasy of mine."
        $ the_person.discover_opinion("creampies")
    else:
        the_person "Don't bother with a condom [the_person.mc_title], I want to feel you raw."
        if not the_person.knows_pregnant:
            the_person "I don't care what the risks are, they're worth it. I need to feel you deep inside me."
        else:
            the_person "I love it, when you fuck me raw. It's like our little secret, just for us."
    return

label goudere_condom_bareback_demand(the_person):
    if the_person.has_breeding_fetish: #Actively looking to get knocked up.
        if the_person.knows_pregnant:
            the_person "Oh darling, what's the point of fucking if we're not going to make a baby together?"
            the_person "Come on, give me that cock and fill me up!"
        elif the_person.is_infertile:
            the_person "Oh, I'm so sorry sweetheart. I can't get pregnant."
            the_person "But let's enjoy each other's company, shall we?"
        else:
            the_person "Oh darling, what's the point of fucking if we're not going to make a baby together?"
            the_person "Come on, flood my womb with your seed!"

    elif the_person.wants_creampie:
        if the_person.is_infertile:
            the_person "Oh, I'm so sorry sweetheart. I can't get pregnant."
            the_person "But let's enjoy each other's company, shall we?"
        elif the_person.on_birth_control:
            the_person "Fuck that, I'm on the pill. Fuck me raw [the_person.mc_title]!"
            the_person "Even better, you can cum right inside me. Come and fill me up!"
            $ the_person.update_birth_control_knowledge()
        else:
            the_person "There shall be no barriers between our love, flood my gates [the_person.mc_title]."
            the_person "So hurry up and get inside me!"

    else:
        if the_person.is_infertile:
            the_person "Take me bareback [the_person.mc_title], I'm in the mood for a little adventure!"
        elif the_person.on_birth_control:
            the_person "Fuck that, I'm on the pill!"
            the_person "Take me bareback [the_person.mc_title], I want to feel you deep inside!"
            $ the_person.update_birth_control_knowledge()
        else:
            the_person "Fuck that, it feels so much better without one!"
            the_person "Take me bareback, I can't wait any longer!"
    return

label goudere_cum_face(the_person):
    if the_person.has_cum_fetish or the_person.obedience > 180:
        if the_person.has_cum_fetish or the_person.effective_sluttiness() > 60 or the_person.opinion.cum_facials > 0:
            the_person "Ah, darling! Do you like the look of me with your cum on my face? It's so... tempting!"
            "[the_person.title] playfully licks her lips, moving a few drops of your semen that had run down her face with her fingers to her mouth."
        else:
            the_person "Oh, I hope you enjoyed that as much as I did, [mc.name]."
            "[the_person.title] runs a finger along her cheek, wiping away some of your semen and smiling mischievously."
    else:
        if the_person.effective_sluttiness() > 80 or the_person.opinion.cum_facials > 0:
            the_person "Mmm, that's such a good feeling, isn't it [mc.name]? Do you like the way you've marked me?"
            "[the_person.title] runs her tongue along her lips, then smiles seductively and raises an eyebrow."
        else:
            the_person "Well, now that we've got that out of the way, let's move on to something more interesting."
            "[the_person.title] winks at you, her eyes sparkling with mischief."
    return

label goudere_cum_mouth(the_person):
    if the_person.has_cum_fetish or the_person.obedience > 180:
        if the_person.has_cum_fetish or the_person.effective_sluttiness() > 60 or the_person.opinion.drinking_cum > 0:
            the_person "Mmm, oh darling, that was quite the treat!"
            "[the_person.title] leans in close, her lips brushing against your cheek as she savors the taste of your cum."
        else:
            "[the_person.title]'s face lights up with a mischievous grin as she tastes your cum in her mouth."
            the_person "Ah, so sweet of you to share that with me, [mc.name]."
    else:
        if the_person.effective_sluttiness() > 80  or the_person.opinion.drinking_cum > 0:
            the_person "Mmm, you taste like a king, [mc.name]."
            the_person "Was it nice to watch me take your load in my mouth? I certainly enjoyed it."
        else:
            the_person "Well, that's one way to get a taste of you, [mc.name]."
            the_person "And I must say, it's quite an... interesting flavor."
    return

label goudere_cum_pullout(the_person):
    # Lead in: "I'm going to cum!"
    if mc.condom:
        if the_person.wants_creampie and not the_person.has_taboo("condomless_sex"): #TODO: FIgure out we want any more requirements for this to fire.
            if the_person.knows_pregnant:
                the_person "Oh darling, why not? Take off the condom and fill me up!"
                the_person "You've already got me pregnant, so what's one more time?"
                the_person "We've already crossed that line once, might as well do it again!"
            elif the_person.on_birth_control:
                the_person "Oh fuck, I can't resist any longer!"
                the_person "Take off the condom and fill me up, [mc.name]!"
            else:
                the_person "I can't think straight!"
                the_person "Take off the condom and make me pregnant, [mc.name]!"
                $ the_person.update_birth_control_knowledge()
            menu: #TODO: Add a variant of this normally so you can stealth a girl (don't do that in real life, it's super fucked up).
                "Take off the condom":
                    "You quickly pull out, barely clearing her pussy, and pull the condom off."
                    $ mc.condom = False
                    $ use_condom = False  # prevent putting on a new condom next sex loop
                "Leave it on":
                    "You ignore [the_person.possessive_title]'s sultry offer and keep the condom in place."
        else:
            the_person "Hell yeah, I'm going to make you cum!"
    else:
        if the_person.wants_creampie:
            if the_person.knows_pregnant:
                the_person "Flood me with your seed, [mc.name], I want it all!"
            elif the_person.opinion.creampies > 0:
                "[the_person.possessive_title!c] moans happily."
                if the_person.on_birth_control:
                    the_person "Oh yes my darling, flood me with your cum, [mc.name]! FILL ME!"
                else:
                    $ the_person.update_birth_control_knowledge()
                    the_person "Oh yes my darling, flood my womb with your wonderful seed and knock me up, [mc.name]! I want you to breed me!"
            elif the_person.is_infertile:
                the_person "Cum wherever you want, [mc.name], I can't get pregnant."
            elif the_person.on_birth_control:
                $ the_person.update_birth_control_knowledge()
                the_person "Cum wherever you want, [mc.name], I'm on the pill!"
            else:
                the_person "Do it! Cum!"
        else:
            if the_person.is_infertile:
                the_person "Just pull out, I don't want your cum inside me!"
            elif not the_person.on_birth_control:
                $ the_person.update_birth_control_knowledge()
                the_person "Fuck, pull out! I'm not on the pill!"
            elif the_person.opinion.creampies < 0:
                the_person "Pull out, I don't want you to cum in me!"
            else:
                the_person "Hell yeah, pull out and cum all over me!"
    return

label goudere_cum_condom(the_person):
    if the_person.effective_sluttiness() > 75 or the_person.opinion.creampies > 0:
        the_person "Mmm, it's so warm and snug. If your condom broke, it would be a sweet surprise."
    else:
        the_person "Oh, I hope you invest in good condoms, [mc.name], because that's a lot of... potential."
        the_person "Though, maybe you're secretly hoping to knock me up and start a little family."
    return

label goudere_cum_vagina(the_person):
    if the_person.has_taboo("creampie"):
        $ the_person.call_dialogue("creampie_taboo_break")
        $ the_person.break_taboo("creampie")
        return

    if the_person.wants_creampie:
        the_person "Mmm, darling, I've been waiting for this moment. Fill me up with your cum, I love feeling you deep inside me." 
        if the_person.knows_pregnant:
            the_person "You know, I might just get pregnant on purpose now that I've felt how good this feels."
        elif the_person.is_infertile:
            the_person "I don't care if I can't get pregnant, I want to feel that hot cum flowing inside me."
        elif the_person.on_birth_control:
            if the_person.has_significant_other:
                the_person "Oh fuck, you're so good at this. My [the_person.so_title] doesn't know how to make me feel like this."
            else:
                the_person "I might have to get you a membership to the creampie club. You're the best at this."
                if the_person.knows_pregnant:
                    the_person "Oh fuck that's a lot of cum. Good thing I'm already pregnant, because I don't think you're firing blanks."
                elif the_person.is_infertile:
                    the_person "Oh fuck that's a lot of cum. I will be dripping your cum all day long."
                else:
                    the_person "Oh fuck that's a lot of cum. Good thing I'm on the pill, because I don't think you're firing blanks."
                $ the_person.update_birth_control_knowledge()
        elif the_person.effective_sluttiness() > 75 or the_person.opinion.creampies > 0:
            if the_person.has_significant_other:
                the_person "I don't care if I get pregnant, I'll just tell my [the_person.so_title] that it's his."
            else:
                the_person "I might just get knocked up on purpose if you keep making me feel like this."
        else:
            if the_person.has_significant_other:
                the_person "Oh fuck, you really filled me up! You're going to send me home to my [the_person.so_title] knocked up."
            else:
                the_person "That was such a big load, you're trying your best to knock me up!"
    else: #She's angry
        if the_person.knows_pregnant:
            the_person "Hey, I told you to pull out, but I guess I don't mind since I'm already pregnant..."
        elif not the_person.on_birth_control:
            if the_person.has_significant_other:
                the_person "Oh fuck. [the_person.mc_title], why didn't you pull out? My [the_person.so_title] would kill me if he found out I got pregnant."
                if the_person.kids > 0:
                    the_person "... Again."
            else:
                the_person "Oh fuck, I said to pull out! I'm not on the pill [the_person.mc_title], what happens if I get pregnant?"
                $ the_person.update_birth_control_knowledge()
            the_person "Well, it's already happened, so maybe next time I'll make you wear a condom."
        elif the_person.is_infertile:
            the_person "Hey, I told you to pull out. Now look at what a mess you've made... what a fucking mess..."
        elif the_person.has_significant_other:
            the_person "Hey, I said to pull out! I have a [the_person.so_title], even if I'm on the pill you shouldn't be creampieing me."
            $ the_person.update_birth_control_knowledge()
            the_person "I don't want to have to make you wear a condom, so be a little more careful next time."
        elif the_person.opinion.creampies < 0:
            the_person "Hey, I told you to pull out. Now look at what a mess you've made... It feels like it's everywhere..."
        else:
            the_person "I told you to pull out. Did you get a little too excited?"
            the_person "Don't make a habit of it, otherwise I'll make you start wearing a condom again."
    return

label goudere_cum_anal(the_person):
    if the_person.has_taboo("anal creampie"):
        $ the_person.call_dialogue("anal_creampie_taboo_break")
        $ the_person.break_taboo("anal creampie")
        return

    if the_person.sluttiness > 75 or the_person.opinion.anal_creampies > 0:
        the_person "Mmm, darling, I've been wanting you to do this. Fill my ass with your cum, I love the feeling of you deep inside me." 
    elif the_person.opinion.anal_creampies < 0:
        the_person "Oh fuck, are you really going to do that? I'm not sure I'm ready for that..."
    else:
        the_person "Oh fuck, you're going to fill me up... I love it when you make me feel this way."
    return

label goudere_surprised_exclaim(the_person):
    $rando = renpy.random.choice(["Fuck yes!", "Oh hell yeah!", "Incredible!", "That's amazing!", "Wow, baby!", "Unbelievable!", "That's hot!", "Oh my god!", "Fuck me right now!", "Fuck this feels good!", "Yes, please!", "Fuck, this is intense!"])
    the_person "[rando]"
    return

label goudere_talk_busy(the_person):
    if the_person.obedience > 120:
        the_person "I've got a lot on my plate right now, but I'll make time for you later, [the_person.mc_title]. I promise it'll be worth it."
    else:
        the_person "I'd love to talk, but I'm swamped with stuff at the moment. Maybe we can catch up later when things calm down?"
    return

label goudere_sex_strip(the_person):
    if the_person.sluttiness < 20:
        if the_person.arousal_perc < 50:
            the_person "Oh, I'm a bit too dressed up for this. Let me fix that."
        else:
            the_person "Hmm, I think it's time to get a bit more comfortable... for both of us."
    elif the_person.sluttiness < 60:
        if the_person.arousal_perc < 50:
            the_person "You know, I think I'd feel better if I wasn't wearing all this. Just a little."
        else:
            the_person "Yeah, I think I'll take something off. I want to feel every inch of you against me."
    else:
        if the_person.arousal_perc < 50:
            the_person "Okay, one more thing has to go. Just for you."
        else:
            the_person "Ugh, let me just get rid of this. I want you to feel every curve of me, baby!"
    return

label goudere_sex_watch(the_person, the_sex_person, the_position):
    $ title = the_person.title if not the_person.is_stranger else "The stranger"
    if the_person.sluttiness < the_position.slut_requirement - 20:
        $ the_person.draw_person(emotion = "angry", display_transform = character_left_flipped)
        the_person "Ugh, could you two at least try to be a bit more discreet? You're making me uncomfortable."
        $ the_person.change_stats(obedience = -2, happiness = -1)
        "[title] looks away while you and [the_sex_person.fname] [the_position.verb]."
        return False

    if the_person.sluttiness < the_position.slut_requirement - 10:
        $ the_person.draw_person(display_transform = character_left_flipped)
        the_person "Come on, could you two at least keep it down a bit? You're being too loud."
        $ the_person.change_happiness(-1)
        "[title] tries to avert her gaze and ignore you and [the_sex_person.fname] [the_position.verb]."
        return False

    if the_person.sluttiness < the_position.slut_requirement:
        $ the_person.draw_person(display_transform = character_left_flipped)
        if not is_watching(the_person):
            the_person "You two are really getting into it, aren't you? I can't help but be a bit turned on by this."
        $ the_person.change_slut(1, 30)
        "[title] watches while you and [the_sex_person.fname] keep [the_position.verbing]."
        return True

    if the_person.sluttiness >= the_position.slut_requirement and the_person.sluttiness < the_position.slut_cap:
        $ the_person.draw_person(display_transform = character_left_flipped)
        if not is_watching(the_person):
            the_person "Oh, this is so hot. I'm definitely getting a bit turned on by this. Keep going!"
        $ the_person.change_slut(1, 50)
        "[title] watches you and [the_sex_person.fname] [the_position.verb]."
        return True

    $ the_person.draw_person(emotion = "happy", display_transform = character_left_flipped)
    if renpy.random.randint(0, 1) == 0:
        the_person "Come on [the_person.mc_title], [the_sex_person.fname] is really getting into this! You're going to have to give her a little more than that."
    else:
        call watcher_position_comment(the_person, the_sex_person, the_position) from _call_watcher_position_comment_goudere_sex_watch
    "[title] watches with a smile while you and [the_sex_person.fname] [the_position.verb]."
    return True

label goudere_being_watched(the_person, the_watcher, the_position):
    $ title = the_watcher.fname if not the_watcher.is_stranger else "the stranger"
    if the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #They agree you should give it to her harder
        the_person "Come on [the_person.mc_title], I want it rough and deep. Make me scream!"
        $ the_person.change_arousal(1)
        "[the_person.title] seems to be enjoying [title] watching you and her [the_position.verb]."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's super slutty and doesn't care what people think.
        the_person "Oh, I bet [title] wishes they could join in and experience this wild ride with us."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #She's super slutty and encourages the watcher to be slutty.
        the_person "Oh god, [title], you need to get a little of this action yourself!"
        $ the_person.change_arousal(1)
        "[the_person.title] seems to be enjoying [title] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #She's into it and encouraged by the slut watching her.
        "[the_person.fname] responds to [title]."
        the_person "I'm giving him all I can right now. Any more and I might just come undone!"
        $ the_person.change_arousal(1)
        "[the_person.title] seems to be enjoying [title] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's into it but shamed by the prude watching her.
        the_person "Oh, maybe we should go somewhere a little more private..."
        $ the_person.change_stats(arousal = -1, slut = -1)
        "[the_person.title] seems a bit uncomfortable with [title] nearby."

    else: #the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #They're both into it but not fanatical about it.
        "[the_person.possessive_title!c] catches [title]'s eye and says..."
        the_person "Hey, maybe when he's done you can join in and give me some more action!"
        $ the_person.change_stats(arousal = 1, slut = 1, max_slut = 30)
        "[the_person.title] seems to be enjoying the show, watching you and her [the_position.verb]."

    return

label goudere_work_enter_greeting(the_person):
    if the_person.happiness < 80 or the_person.love < 0:
        "[the_person.title] looks up from her work, her eyes narrowing slightly as you enter the room. She scoffs and turns back to her task."

    elif the_person.happiness > 130:
        if the_person.sluttiness > 40:
            the_person "Hey [the_person.mc_title], down here for business or pleasure?"
            "The sultry smile she gives you tells you which one she's hoping for."
            "She leans forward, her chest brushing against your arm, and whispers in your ear."
            the_person "I hope it's the latter, [mc.name]. I've been waiting for this moment all day."

        else:
            "[the_person.title] looks up from her work and flashes you a bright smile when you enter the room."
            the_person "Hey [the_person.mc_title], it's nice to have you stop by. Let me know if you need anything!"

    else:
        if the_person.sluttiness > 60:
            "[the_person.title] walks over to you when you come into the room, her hips swaying seductively."
            the_person "Just the person I was hoping would stop by. I'm here if you need anything."
            "She winks and slides a hand down your chest, stomach, and finally your crotch."
            the_person "Anything at all."
            "Her touch sends a shiver down your spine as she leans in close, her lips brushing against your ear."
            the_person "Or maybe we can discuss something else entirely..."

        else:
            the_person "Hey [the_person.mc_title]. Need anything?"
    return

label goudere_date_seduction(the_person):
    if the_person.is_girlfriend:
        "[the_person.possessive_title!c] grabs your hand and pulls you around to look at her."
        the_person "Hey there, darling. I've had such an amazing time tonight. I was thinking, why don't we take this party back to my place and see where the night takes us?"
        the_person "My place is just a short walk from here. What do you say, are you up for it?" 
        "She bats her eyelashes and leans in closer, her lips brushing against your ear as she whispers..."
        the_person "I promise you won't regret it."
        $ mc.change_locked_clarity(30)
        if the_person.effective_sluttiness(["vaginal_sex", "condomless_sex"]) > 60 and the_person.wants_creampie and the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex >= 0 and the_person.opinion.creampies >= 0 and not the_person.on_birth_control and not the_person.knows_pregnant:
            if the_person.opinion.creampies > 0: #No condoms, loves creampies, she's basically asking you to knock her up. So... have her ask you to knock her up!
                the_person "Let's go back to my place and fuck until you knock me up."
                the_person "Don't you think I'd look good with huge mommy-tits? You can make it happen."
            else:
                the_person "Let's go back to my place, I want you to throw me on the bed and fuck me bareback."
                the_person "You can even cum inside me if you want. I just want you to fuck me up with your cock."
        elif the_person.effective_sluttiness(["vaginal_sex", "condomless_sex"]) > 60 and the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex > 0:
            the_person "Let's go back to my place. You can fuck me any way you want, as long as you follow my one simple rule: No condoms."
            the_person "It feels so much better getting fucked bareback, I just can't do it any other way!"
        elif the_person.effective_sluttiness(["vaginal_sex"]) > 50 and the_person.opinion.vaginal_sex > 0:
            the_person "Let's go back to my place, alright? I want to get my little pussy pounded, and you're the guy for the job."
            the_person "Do you think you can do that? Can you come fuck me up with that big cock?"
        elif the_person.effective_sluttiness(["anal_sex"]) > 60 and the_person.opinion.anal_sex > 0:
            the_person "Let's go back to my place, alright? I want to get my ass stretched out tonight, and you've got the cock that I love."
            the_person "Doesn't that sound like a fun way to end our night together?"
        elif the_person.effective_sluttiness(["sucking_cock"]) > 40 and the_person.opinion.giving_blowjobs > 0:
            the_person "Let's go back to my place. I want to reward you for giving me such a wonderful night."
            the_person "How does a nice long, sloppy blowjob sound? I think it sounds pretty fun."
        elif the_person.effective_sluttiness() > 40 and the_person.opinion.being_covered_in_cum > 0:
            the_person "Let's go back to my place. We can have some fun, and I can end this night in my favourite way..."
            "She licks her lips playfully."
            the_person "Covered in your hot cum. Sound like fun?"
        elif the_person.effective_sluttiness(["touching_body"]) > 40 and the_person.opinion.giving_tit_fucks > 0 and the_person.has_large_tits:
            the_person "Let's go back to my place, then I can repay you for this wonderful night."
            the_person "I'll slide that big cock of yours between my tits and fuck it until you cum. How does that sound?"
        else: #She's not very slutty, so she leaves the invitation open to interpretation
            the_person "It doesn't have to be over yet, does it? Let's go back to my place and we can keep the fun going."
            "She bites her lower lip playfully."

    elif the_person.is_affair:
        the_person "So my [the_person.so_title] won't be home tonight, I was thinking..."
        "She reaches down and cups your crotch, rubbing it gently through your pants."
        $ mc.change_locked_clarity(40)
        if the_person.wants_creampie and the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex >= 0 and the_person.opinion.creampies >= 0 and not the_person.on_birth_control and not the_person.knows_pregnant:
            if the_person.opinion.creampies > 0: #No condoms, loves creampies, she's basically asking you to knock her up. So... have her ask you to knock her up!
                the_person "Let's go back to my place so you can pin me to the bed and creampie me all night long."
                the_person "All that cum in my unprotected pussy and I'm sure to get knocked up. Just thinking about it is making me wet!"
            else:
                the_person "Let's go back to my place. You can pin me to the bed and fuck me bareback all night long."
                the_person "Cum inside me, over my face, whatever. I just want you to fuck me up with your cock."
        elif the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex > 0:
            the_person "Let's go back to my place. You can fuck me all night, any way you want, as long as you follow one simple rule."
            the_person "No condoms. If you're fucking me you're doing it bareback."
        elif the_person.opinion.vaginal_sex > 0:
            the_person "Let's go back to my place and you can pound my tight fucking pussy until I'm just a quivering, cum-covered wreck."
            the_person "How does that sound? Do I have your attention?"
        elif the_person.opinion.anal_sex > 0:
            the_person "Let's go back to my place so you can stretch out my tight little asshole with that monster cock of yours."
        elif the_person.opinion.giving_blowjobs > 0:
            the_person "Let's go back to my place, and you can choke me out on that monster cock of yours."
            the_person "I want to throat it so fucking deep. I want to feel your balls against my chin when you cum."
        elif the_person.opinion.being_covered_in_cum > 0:
            "She leans in close, her lips brushing against your ear."
            the_person "Imagine all the ways you could cover me in your cum. On my skin, in my hair, even in my mouth..."
        elif the_person.opinion.giving_tit_fucks > 0 and the_person.has_large_tits:
            the_person "Let's go back to my place so I can wrap these big fucking tits around your big fucking cock."
            "She reaches down and squeezes her own breasts, her eyes locked on yours."
            the_person "I can already feel myself getting wet just thinking about it."
        elif the_person.opinion.cheating_on_men > 0:
            the_person "Let's go back to my place, and you can do all the fucked up things I tell my husband I hate."
            the_person "He tries to treat me like a lady, but all I want to be is your cock drunk slut."
        else:
            the_person "Let's go back to my place and make him really regret leaving me alone for the night."
    elif not the_person.has_significant_other:
        $ mc.change_locked_clarity(20)
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                the_person "I've had a blast [the_person.mc_title], but there are a few more things I'd like to do with you. Want to come back to my place and find out what they are?"
            else:
                the_person "You've been a blast [the_person.mc_title]. Want to come back to my place, have a few drinks, and see where things lead?"
        else:
            if the_person.love > 40:
                the_person "Tonight's been amazing [the_person.mc_title], I just don't want to say goodbye. Do you want to come back to my place and have a few drinks?"
            else:
                the_person "This might be crazy, but I had a great time tonight and you make me a little crazy. Do you want to come back to my place and see where things go?"
    else:
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                $ mc.change_locked_clarity(20)
                the_person "I've had a blast [the_person.mc_title], but I'm not done with you yet. Want to come back to my place?"
                the_person "My [the_person.so_title] won't be home until morning, so we would have plenty of time."
            else:
                $ mc.change_locked_clarity(20)
                the_person "This might be crazy, but do you want to come back to have another drink with me?"
                the_person "My [the_person.so_title] is stuck at work and I don't want to be left all alone."
        else:
            if the_person.love > 40:
                $ mc.change_locked_clarity(20)
                the_person "You're making me feel crazy [the_person.mc_title]. Do you want to come have a drink at my place?"
                the_person "My [the_person.so_title] won't be home until morning, and we have a big bed you could help me warm up."
            else:
                $ mc.change_locked_clarity(20)
                the_person "This is crazy, but would you want to have one last drink at my place? My [the_person.so_title] won't be home until morning..."
    return

label goudere_sex_end_early(the_person):
    if the_person.sluttiness > 50:
        if the_person.love > 40:
            if the_person.arousal_perc > 60:
                the_person "Oh, [the_person.mc_title], you're really done already? But I was just getting warmed up... *pouts*"
            else:
                the_person "Well, that was fast. I was prepared to give you a much more... thorough experience. *smirks*"
    else:
        if the_person.arousal_perc > 60:
            the_person "Well, well, [the_person.mc_title], you've certainly gotten me in the mood. *giggles*"
        else:
            the_person "Finished already? Good, I'm quite done myself. *yawns*"
    return

label goudere_sex_take_control(the_person):
    if the_person.arousal_perc > 60:
        the_person "Oh darling [the_person.mc_title], I don't think so. You're not getting away from me that easily. *smirks*"
    else:
        the_person "Not so fast, [the_person.mc_title]. I'm not done with you yet. *pouts*"
    return

label goudere_sex_beg_finish(the_person):
    the_person "Oh, [the_person.mc_title]... darling, I'm so close. Please, please, let me finish. *whispers seductively* I'll make it worth your while, I promise. *smirks*"
    return

label goudere_sex_review(the_person, the_report):
    $ comment_position = the_person.pick_position_comment(the_report)
    if comment_position is None:
        return #You didn't actually do anything, no need to comment.

    $ used_obedience = the_report.get("obedience_used", False) #True if a girl only tried a position because you ordered her to.
    $ the_person.draw_person()  # make sure she stands up for talking with you

    #She's worried about her SO finding out because it was in public
    if the_report.get("was_public", False) and the_person.has_significant_other and the_person.opinion.cheating_on_men <= 0: #It was public and she cares.
        if the_person.is_affair: #Dialogue about her being into it, but you can't do this in case she gets caught.
            the_person "I have to admit, that was thrilling! But we should probably be more discreet next time, don't you think?"
            the_person "I don't want my [the_person.so_title] to find out about this."
        elif used_obedience:
            the_person "Oh my god, I can't believe we did that in public! What if someone tells my [the_person.so_title]?"
            mc.name "Don't worry, nobody really cares what we're doing. They aren't going to tell your [the_person.so_title]."
            the_person "You're right... but it's still a little scary to think about."
        else:
            $ the_person.call_dialogue("surprised_exclaim")
            the_person "Everyone's watching us. I hope my [the_person.so_title] doesn't hear about this..."
            mc.name "Don't worry, nobody here really cares what we do together. Nobody's going to tell him."
            the_person "You're right... I just get a little nervous when we do this stuff in public."

    #She's single, but worried that you did in public.
    elif the_report.get("was_public", False) and (the_person.effective_sluttiness()+10*the_person.opinion.public_sex < comment_position.slut_cap):
        if used_obedience:
            the_person "Oh my god, we did that in public? I must be crazy!"
            the_person "Everyone's probably thinking I'm some sort of slut now..."
        else:
            the_person "Oh my god, everyone's watching us! What if someone recognizes us?"
            mc.name "Don't worry, nobody really cares what we're doing."
            the_person "You're right... I guess I just get a little self-conscious when we do this stuff in public."
    elif the_report.get("girl orgasms", 0) > 2:
        if used_obedience:
            the_person "Wow, that was incredible... I didn't think I could get that carried away!"
            mc.name "I love when you lose control like that."
            "[the_person.possessive_title!c] blushes and leans in closer."
        else:
            the_person "I... I've never felt anything like that before. It was amazing!"
            "She takes a deep breath, still trying to process the intensity of the moment."
            the_person "You really know how to push my buttons, don't you?"

        call sex_review_trance(the_person) from _call_sex_review_trance_goudere_sex_review

    #No special conditions, just respond based on how orgasmed and how slutty the position was.
    elif the_report.get("girl orgasms", 0) > 0 and the_report.get("guy orgasms", 0) > 0: #You both came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position cap, it was tame
            the_person "That was definitely a good time... but I think we could take it up a notch next time."
            the_person "Are you up for it? I'm already getting wet just thinking about it..."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "Wow, that was intense! I think we're really compatible, don't you?"
            the_person "Let's do it again sometime soon, okay?"

        elif used_obedience: #She only did it because she was commanded
            the_person "I... I didn't think I could get that carried away."
            mc.name "Aren't you going to thank me? You obviously had a good time."
            "She rolls her eyes and smiles, trying to hide her embarrassment."

        else: # She's surprised she even tried that.
            the_person "Oh wow, that was unexpected! I didn't think I was going to take it so far, but it just felt right, you know?"
            the_person "Don't think that's going to happen every time though, alright? I'm not a slut!"

    elif the_report.get("girl orgasms", 0) > 0: #Only she came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            the_person "Done already? Well, that's just not right. Next time I'm going to make sure we both cum."
            the_person "I've got a few ideas that are going to blow you away."
            "She smiles mischievously, already imagining your next encounter."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "You're all done? Well, that was fucking hot either way."
            the_person "I'll repay the favour next time, alright? I promise."

        elif used_obedience: #She only did it because she was commanded
            the_person "That's it? I mean, not like I wanted to do anything more, I just thought you were going to finish."
            mc.name "Some other time. I just wanted to see what you look like when you cum."
            the_person "I... Fuck, well, I guess you got what you wanted."
            the_person "It could have been worse, I guess."

        else: # She's surprised she even tried that.
            the_person "Oh fuck, that was intense! You really know how to make a girl feel good!"
            the_person "You're probably tired after all that work. I promise I'll repay the favour next time, okay?"

    elif the_report.get("guy orgasms", 0) > 0: #Only you came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            the_person "All tired out? Well, that's a little disappointing."
            mc.name "Sorry, I'll make it up to you next time."
            the_person "You better. I've got some ideas that should have both of us cumming our brains out. Sound like fun?"
            mc.name "Yeah, I think I could get behind that."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "Tired out already? Well someone's being a little selfish today..."
            mc.name "Sorry, I'll make it up to you next time."
            the_person "You better, or you won't get many more \"next times\"!"

        elif used_obedience: #She only did it because she was commanded
            the_person "I expect you're tired after all of that. We're done then?"
            mc.name "Yeah, that's all for now."
            "She nods, obviously a little embarrassed but doing her best not to show it."

        else:  # She's surprised she even tried that.
            the_person "Whew, that was... intense. I think I got a little carried away there."
            the_person "Probably a good idea we stop, before we take this too far."

    elif the_person.energy < 10: #Nobody came and she's tired
        the_person "Sorry, but I'm too tired. I'm going to have to make it up to you some other time."
        mc.name "No problem, we will continue this another time."

    else: #Nobody came.
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            the_person "You're done already? Oh come on, we barely even got started!"
            "She pouts, intentionally being dramatic."
            the_person "You're such a tease [the_person.mc_title]."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "We're stopping already? We were just getting to the good stuff though!"
            mc.name "Sorry [the_person.title], I'll have to make it up to you some other time."
            the_person "You better. You can't just tease a girl like this, it's not nice."

        elif used_obedience: #She only did it because she was commanded
            the_person "That's all? Well that's not exactly what I was expecting."
            mc.name "You aren't disappointed, are you?"
            the_person "No, I just... Thought this was all going to go somewhere more serious."
            the_person "Whatever, it doesn't matter."

        else:  # She's surprised she even tried that.
            the_person "Fuck, you're probably right. We should stop now before we take this too far."
            the_person "If I get too turned on I might do something I regret. Let's just keep this casual."

    # Gave creampie while she is not on birth control (extra dialogue when she could get pregnant)
    if the_report.get("creampies", 0) > 0 and not the_person.on_birth_control and not the_person.knows_pregnant:
        the_person "Oh baby, you are a mad dog, you must really want to see me pregnant."

    $ del comment_position
    return

label goudere_improved_serum_unlock(the_person):
    mc.name "[the_person.title], now that you've had some time to get used to the lab there is something I want to talk to you about."
    the_person "Sure, what can I help you with?"
    mc.name "Our R&D up to this point has been based on my old notes from university."
    mc.name "There were some unofficial experiment results that suggested the effects might be enhanced by sexual arousal."
    "[the_person.possessive_title!c] nods her understanding."
    the_person "Ah, so you had noticed that too? I have a hypothesis that an orgasm opens chemical receptors that are normally blocked."
    mc.name "What else can we do if we assume that is true? Does that open up any more paths for our research?"
    the_person "If it's true I could leverage the effect to induce greater effects in our subjects."
    "[the_person.possessive_title!c] thinks for a long moment, then smiles mischievously."
    the_person "But we'll need to do some experiments to be sure."
    mc.name "What sort of experiments?"
    the_person "I want to take a dose of serum myself, and you can record the effects."
    the_person "Then I'll make myself cum, and we can compare the effects after."
    mc.name "Do you think that's a good idea?"
    the_person "Not entirely, no. But we can't trust anyone else with this information if we're right."
    the_person "We might be able to make progress by brute force, but this is a chance to catapult our knowledge to another level."
    the_person "A finished dose of serum that raises my Suggestibility. The higher it gets my Suggestibility the better, but any amount should do."
    the_person "Then we'll just need some time and some privacy for me to see what sort of effects my orgasms will have."
    "[the_person.possessive_title!c] leans in closer, her voice taking on a seductive tone."
    the_person "I've got an idea how we can make this a little more... interesting."
    mc.name "What kind of idea?"
    the_person "Why don't we make this a little more... hands-on? You can watch, and we can discuss what we see afterwards."
    mc.name "Are you sure that's a good idea?"
    the_person "Of course I'm sure! I trust you. And who knows, maybe it'll even help with the research."
    "[the_person.possessive_title!c] winks at you, a playful glint in her eye."
    the_person "So, what do you say? Are you in?"
    return

#
# label goudere_improved_serum_unlock(the_person):
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
label goudere_kissing_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 30:
        the_person "Come on then, we both know where this is going. You've always wanted to kiss me, right?"
        mc.name "I guess we are. What do you think?"
        the_person "It's about time, I've wanted to make out with you for a long time."
        "[the_person.possessive_title!c] leans in close, her lips inches from yours."
        the_person "So, are you going to be gentle or are you going to take control?"
    elif the_person.love >= 20:
        the_person "So we're doing this, huh?"
        mc.name "I guess we are. What do you think?"
        the_person "It's about time, I've wanted to make out with you for a long time."
        "[the_person.possessive_title!c] runs her fingers through your hair, a flirtatious smile on her lips."
        the_person "You've been wanting this as much as I have, don't deny it."
    else:
        the_person "I don't know about this [the_person.mc_title], do you think we're taking this too fast?"
        mc.name "Are you scared?"
        the_person "No! Just... Nervous. Excited, maybe."
        mc.name "Then just trust me."
        "[the_person.possessive_title!c] takes a deep breath, her eyes locking onto yours."
        the_person "Okay, let's do this."

    "[the_person.possessive_title!c] leans in, her lips brushing against yours softly."
    the_person "Mmmm, I've wanted to do this for so long..."

    "[the_person.possessive_title!c] pulls back slightly, her eyes sparkling with mischief."
    the_person "So, do you want to take it slow or do you want to see how far we can go?"

    return

label goudere_touching_body_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 30:
        the_person "Are you sure about this? I don't want you to chicken out on me..."
        mc.name "Oh, I'm sure."
        the_person "Good. Come on then! You're going to love it, I promise."
    elif the_person.love >= 20:
        "You lean in close, whispering in her ear."
        mc.name "I've been thinking about this for a long time, and I'm not going to back down now."
        the_person "Mmm, I like the sound of that."
        "You can feel her body relax against yours as she leans in, her breath hot against your ear."
        the_person "Alright, if you're sure... I'm not going to say I didn't warn you though."
        mc.name "I wouldn't have it any other way."
    else:
        "You gently run your fingers along her skin, sending shivers down her spine."
        the_person "Oh, you're so bad! But I suppose I deserve this for teasing you all this time."
        mc.name "That's not true. You're just as much at fault as I am."
        "You can feel her body respond to your touch, her skin warming to your touch."
        the_person "You're right... I guess we both are. And I'm not going to stop you now."
        mc.name "Good. Because I don't plan on stopping any time soon."
        "You continue to explore each other's bodies, the tension building between you two."
    return

label goudere_touching_penis_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 35:
        the_person "Mmm, you're really turned on too, right? Look how big you are."
        mc.name "Do you want to feel it?"
        the_person "I thought you'd never ask. And don't worry, I'm not going to be shy about it."
        "You can feel her hand wrap around your cock, her grip firm but gentle."

    elif the_person.love >= 20:
        the_person "Wow, you're really quite impressive. I wasn't expecting that."
        mc.name "Glad to hear it. Now, how about we take things to the next level?"
        the_person "Oh, I think we can do that. I want to feel you deep inside me."
        mc.name "That's what I wanted to hear. Let's get undressed and make this happen."

    "You both quickly shed your clothes, your eyes locked on each other's bodies as you expose yourselves."
    the_person "Damn, you're even more beautiful than I imagined. And I know I look good too."
    mc.name "You do, but I'm more interested in what's between your legs right now."
    the_person "Oh, me too. Come on, let's get this over with."
    "You both laugh as you climb onto the bed, the tension between you two mounting."
    return

label goudere_touching_vagina_taboo_break(the_person):
    the_person "Don't chicken out on me now, you've got your chance to touch my pussy. And don't think I'm not going to enjoy this too."
    mc.name "You're on. I've been dying to feel you."
    "You slowly reach out, your fingers tracing the outline of her pussy lips."
    the_person "Mmm, that feels so good. Don't stop."
    mc.name "I wouldn't dream of it. I'm just getting started."
    "You continue to explore her pussy, her moans growing louder with each passing moment."
    the_person "Oh fuck, I'm getting wet. Keep going."
    mc.name "I don't plan on stopping. I want to make sure you're ready for me."
    the_person "I'm more than ready. I want you inside me now."
    mc.name "Patience, my dear. We're not quite there yet."
    "You continue to tease her, building the anticipation to a fever pitch."
    the_person "Please, just a little more. I can't take it."
    mc.name "Soon, I promise. Just let me enjoy this for a little longer."
    "You can feel her body quiver with anticipation as you continue to touch her."
    return

label goudere_sucking_cock_taboo_break(the_person):
    mc.name "I want you to do something for me."
    the_person "Oh yeah? What do you want me to do to you?"
    mc.name "I want you to suck on my cock."
    if the_person.effective_sluttiness() >= 45:
        the_person "Mmm, I think I'm up for that. It's not going to be too big for me, is it?"
        mc.name "I think you'll be able to handle it."
        the_person "Alright, I don't want it choking me."
        "She winks at you, her eyes sparkling with mischief."
        the_person "That's a lie. A little choking is okay."
    elif the_person.love >= 30:
        the_person "I guess we've been dancing around it for a while."
        "She bites her lip and looks your body up and down, her eyes lingering on your cock."
        the_person "Alright, let's do this."
    else:
        the_person "Oh, I was wondering if this was going to come up..."
        "She laughs nervously and looks away from you."
        the_person "I don't know [the_person.mc_title]..."
        "You reach up and hold her chin, turning her head back to face you."
        mc.name "Don't overthink it. Just kneel down and suck on it for me. If you don't like doing it, we can just forget it happened."
        "You can see in her eyes the moment her resolve breaks. She bites her lip and nods."
        the_person "Alright, let's do this."
    "She slowly kneels down, her eyes locked on your cock as she takes it into her mouth."
    the_person "Mmm, you taste so good."
    mc.name "That's because I'm only good enough for you."
    "You can feel her tongue swirling around your cock, her lips tight around you."
    the_person "Oh, I think I'm going to need a little more practice to get this right."
    mc.name "Keep going, you're doing great."
    "You continue to fuck her mouth, her eyes never leaving yours as she continues to suck you off."
    return

label goudere_licking_pussy_taboo_break(the_person):
    mc.name "I want to taste your pussy [the_person.title]. Are you ready?"
    if the_person.effective_sluttiness() >= 45:
        the_person "I was just about to ask you to try that. So yeah, I'm ready! And don't worry, I won't bite... hard."
    elif the_person.love >= 30:
        the_person "Oooh, finally a man who doesn't expect blowjobs all day but never licks a pussy. You're a breath of fresh air!"
        "She bites her lip and smiles at you, her eyes sparkling with mischief."
        the_person "Alright then, get to it lover boy. And don't be shy, I want to feel your tongue."
    else:
        if the_person.has_taboo("sucking_cock"):
            the_person "Really? I haven't even sucked your cock yet and you're ready to go down on me?"
            "She bites her lip and smiles, her eyes gleaming with anticipation."
            the_person "I could get used to this! Get to it!"

        else:
            the_person "It's about time you offered to repay the favour! Most guys think they're the only one who should get some head."
            "She bites her lip and smiles, her eyes teasing you."
            the_person "Alright then, get to it! And don't make me wait too long."
    "You slowly lean down, your tongue darting out to taste her pussy."
    the_person "Mmm, that feels so good. Don't stop!"
    mc.name "Not a chance. I'm just getting started."
    "You continue to lick her pussy, her moans growing louder with each passing moment."
    the_person "Oh fuck, I'm going to cum! Don't stop!"
    mc.name "Not a chance. I want to taste your juices."
    "You continue to lick and suck her pussy, her orgasm building to a fever pitch."
    the_person "Oh fuck, I'm going to cum! Yes, yes, yes!"
    mc.name "Come for me, baby. I want to feel you cum on my tongue."
    "You continue to lick and suck her pussy, her orgasm finally hitting."
    the_person "Yes! Oh fuck, yes!"
    mc.name "That's it, baby. Cum for me."
    "You continue to lick and suck her pussy, milking her orgasm for all it's worth."
    return

label goudere_vaginal_sex_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 60:
        the_person "It's about time we did this. Come on then, get that cock inside me and fuck me like you mean it!"
    elif the_person.love >= 45:
        the_person "Are you ready for this? I hope you're planning to rock my world."
        mc.name "That is the plan, I hope you can handle it."
        the_person "I can handle anything you can throw at me. Just make sure to give it to me hard."
    else:
        if the_person.has_taboo("anal_sex"):
            the_person "Look at that cock... Fuck, I hope you don't stretch out my pussy too badly."
        else:
            the_person "If your cock feels half as big in my pussy as it did up my ass I'm in for a good time."
            "She bites her lip and smiles at you, her eyes gleaming with anticipation."
            the_person "Come on, fuck me [the_person.mc_title]! Make it count."
    "You slowly enter her, her pussy clenching around you."
    the_person "Oh fuck, that feels so good. Don't stop, just like that."
    mc.name "Not a chance. I'm just getting started."
    "You continue to fuck her, her moans growing louder with each passing moment."
    the_person "Oh fuck, I'm going to cum! Don't stop!"
    mc.name "Not a chance. I want to feel you cum on my cock."
    "You continue to fuck her, her orgasm building to a fever pitch."
    the_person "Yes, yes, yes! I'm going to cum!"
    mc.name "That's it, baby. Cum for me."
    "You continue to fuck her, milking her orgasm for all it's worth."
    the_person "Yes! Oh fuck, yes!"
    mc.name "That's it, baby. Cum for me."
    "You continue to fuck her, her orgasm finally subsiding."
    the_person "Wow, that was intense. But I think I'm ready for more."
    mc.name "I thought you might be. Let's get back to it then."
    return

label goudere_anal_sex_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 75:
        the_person "Oh god, it always surprises me how big your cock is! You're going to tear my ass in half with that monster!"
        "She seems more turned on by the idea than worried, her eyes sparkling with anticipation."
        mc.name "Don't worry, you'll be stretched out soon enough."
        the_person "Fuck, just hurry up and do it then. I can't take much more of this teasing."
    elif the_person.love >= 60:
        the_person "So you really want to do this? It might be a little hard to fit all of your cock inside me..."
        mc.name "Don't worry about that, I'll have you stretched out soon enough."
        the_person "Fuck, just try and make sure you don't break me permanently!"
        "She winks at you, her eyes twinkling with mischief."
    else:
        if the_person.has_taboo("vaginal_sex"):
            the_person "Are you sure my pussy wouldn't be tight enough for you, I don't even know if I can fit your cock in my ass!"
            mc.name "I'll make it fit, but you might not be walking right for a few days."
            the_person "Oh fuck..."
            "She bites her lip and looks away from you, her face flushing with embarrassment."
        else:
            "She closes her eyes and talks quietly to herself, her voice trembling with anticipation."
            the_person "Whew, deep breaths [the_person.fname]. You can do this..."
            mc.name "Are you okay?"
            the_person "Yeah, of course. I'm just... a little nervous. Fuck, I don't normally feel like this."
            "She laughs and shakes her head, her eyes sparkling with excitement."
            the_person "Not that I normally do, you know, this. I don't know what's gotten into me."
            mc.name "Hopefully me, soon."
            the_person "No time like the present then. Do it, before I chicken out!"
            "You slowly enter her, her ass clenching around you."
            the_person "Oh fuck, that feels so good. Don't stop, just like that."
    return

label goudere_condomless_sex_taboo_break(the_person):
    if the_person.knows_pregnant:
        the_person "Ah, darling, you want to fuck me raw? How utterly deliciously wicked of you!"
        "Her voice dripping with seduction."        
        if the_person.wants_creampie:
            the_person "Please fill me up with your hot, sticky cum. We both know we'd adore that."
            "She purrs, her eyes never leaving yours."
        else:
            the_person "Please drench me in all your hot, sticky cum."
            "She coos, her lips parted in anticipation."
    elif the_person.opinion.bareback_sex > 0:
        the_person "You want to fuck me raw, darling? That's simply deliciously wicked."
        "She teases, her tone sultry."
        if the_person.on_birth_control:
            the_person "I'm on the pill, so you don't need to worry about cumming inside me."
            "She says, her eyes sparkling with mischief."
            $ the_person.update_birth_control_knowledge()
        elif the_person.wants_creampie:
            the_person "It would be so easy for you to cum inside me though."
            "She says, her voice low and husky."
            the_person "So easy for you to pump my little cunt full of hot cum..."
            "She trails off, her breath catching in her throat."
            "She doesn't sound like she would mind very much at all."
        elif the_person.opinion.creampies < 0:
            the_person "You better make sure you pull out though. I'd be pissed if you got me knocked up."
            "She says, her tone stern but playful."
        else:
            the_person "You'll need to pull out so you don't knock me up then. Got it? Good."
    elif the_person.love > 60:
        if the_person.on_birth_control:
            the_person "You want to fuck me raw, darling? Fuck it, I'm on the pill. What's the worst that can happen?"
            "She says, her eyes twinkling with mischief."
            $ the_person.update_birth_control_knowledge()
        elif the_person.wants_creampie:
            the_person "I guess if I can't trust you I can't trust anyone. You make me make terrible decisions, you know that?"
            "She says, her tone playful but serious."
            the_person "Well fuck it, if we're doing this I want you to go the whole nine yards and finish inside me."
            "She purrs, her eyes never leaving yours."
            mc.name "Are you on the pill?"
            "She shakes her head."
            the_person "Of course not. If we're fucking raw I want you to be trying to breed me every single time."
            "She says, her tone sultry."
            $ the_person.update_birth_control_knowledge()
        elif the_person.opinion.creampies < 0:
            the_person "I guess if I can't trust you I can't trust anyone. You make me make terrible decisions, you know that?"
            "She says, her tone playful but serious."
            the_person "You'll need to pull out though. If you get me knocked up there's no way we're ever doing it unprotected again."
        else:
            the_person "I guess if I can't trust you I can't trust anyone. You make me make terrible decisions, you know that?"
            "She says, her tone playful but serious."
            if the_person.kids == 0:
                the_person "I need you to pull out though. I'm not quite ready to be a mother, even with you."
            elif the_person.kids == 1:
                the_person "I need you to pull out though. I've already got a kid, I don't need another one."
            else:
                the_person "I need you to pull out though. I've already got kids, I don't need another one."
    else:
        if the_person.on_birth_control:
            the_person "Yeah, you want to fuck me raw? Well, I'm on the pill, so why not? It's not like I'm going to end up pregnant."
            "She says, her tone casual but confident."
            $ the_person.update_birth_control_knowledge()
        elif the_person.has_taboo("vaginal_sex"):
            the_person "You really don't think we should use a condom? I'm not on the pill, aren't you worried about knocking me up?"
            "She says, her tone playful but concerned."
            $ the_person.update_birth_control_knowledge()
            the_person "Or is this your master plan to sneak a baby into me?"
            "She teases, her eyes sparkling with mischief."
            mc.name "I promise I'll pull out. Don't you want our first time together to be special?"
            "She rolls her eyes and sighs."
            the_person "God damn it, now you're getting me all sentimental. Fine, you don't need to put anything on."
            the_person "But you better fucking pull out, understand? Good."
        else:
            the_person "You really don't think we should use a condom? I'm not on the pill, aren't you worried about knocking me up?"
            $ the_person.update_birth_control_knowledge()
            the_person "Or is this your master plan to sneak a baby into me?"
            mc.name "I promise I'll pull out. It'll feel so much better without anything between us."
            the_person "Fuck, I know. I'm trying to make this decision with my head and not my clit."
            "She sighs dramatically."
            the_person "Fine, you don't need to put anything on. Just be fucking sure to pull out, understand? Good."
    return

label goudere_underwear_nudity_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > 30 - (the_person.opinion.skimpy_outfits * 5):
        the_person "Ah, darling, you want to see me in my underwear? How utterly delightful!" 
        "She says, her voice dripping with seduction."
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "What are we waiting for then, let's get this off of you."
            "She raises an eyebrow and smiles mischievously."
            the_person "Oh, I don't know... I kind of like the way you look at me when I'm all dressed up. But if you insist, I suppose I can indulge you."
            "She teases, slowly unbuttoning her underwear."
        else:
            mc.name "About time? Are you forgetting I've seen you naked already?"
            "She shrugs and laughs."
            the_person "Oh, [mc.name], you're such a scoundrel. It's not about that, it's about the thrill of the chase. Now, shall we continue?"
            "She purrs, batting her eyelashes."
    elif the_person.love > 15:
        the_person "You want me to strip down a little? It's about time, I was wondering why you were taking things so slow,"
        "She says, her eyes sparkling with flirtation."
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "Well then let's stop wasting time and get your [the_clothing.display_name] off."
            "She giggles and nods, continuing to undress."
            the_person "Oh, I do love a man who knows what he wants."
        else:
            mc.name "Slow? I've already seen you naked, remember?"
            the_person "I guess, but being in my underwear feels more romantic, you know?"
            "She says, her voice sultry."
            mc.name "Well let's get more romantic then and get your [the_clothing.display_name] off."
            "She smiles and begins to remove her clothing, her eyes never leaving yours."
    else:
        the_person "If you take my [the_clothing.display_name] I'll only have my underwear on, you know that?"
        "She says, her tone playful but a little hesitant."
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "Yeah, that's kind of the point."
            "She shakes her head and laughs to herself."
            the_person "Oh [the_person.title], what have you gotten yourself into! Come on, let's do this before I chicken out!"
            "She slowly begins to undress, her eyes never leaving yours."
        else:
            mc.name "Yeah, that's kind of the point. I've already seen you naked, so what are you worrying about?"
            the_person "Whatever, I guess you're right. Come on, let's get it off."
            "She shrugs and begins to undress, her eyes never leaving yours."
    return

label goudere_bare_tits_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > (40 - the_person.opinion.showing_her_tits * 5):
        the_person "Ah, darling, you finally want a look at my tits, do you?"
        "She says, her voice dripping with seduction."
        if the_person.has_large_tits:
            "She shakes her chest for you, jiggling the [the_person.tits_description] hidden underneath her [the_clothing.display_name]."
        else:
            "She shakes her chest and gives her [the_person.tits_description] a little jiggle."
        the_person "What took you so long to ask?"
        "She purrs, her eyes never leaving yours."
        if the_person.has_large_tits:
            mc.name "No time like the present, right? Let's get those puppies out where I can enjoy them."
            "She laughs and nods, her chest heaving with excitement."
        else:
            mc.name "No time like the present, right? Let's get those cute little things out."
            "She giggles and agrees, her eyes sparkling with flirtation."
    elif the_person.love > 25:
        the_person "Ready to see my tits, [the_person.mc_title]?"
        "She says, her voice playful and teasing."
        if the_person.has_large_tits:
            "She shakes her chest and jiggles her nice [the_person.tits_description], barely restrained by her [the_clothing.display_name]."
        else:
            "She shakes her chest, giving her [the_person.tits_description] a little jiggle."
        mc.name "Oh yeah, I'm ready."
        the_person "Let 'em out then, and have fun."
        "She says, her eyes never leaving yours."
    else:
        the_person "Wait a second! Geebus, you should at least ask a girl before you try and put her tits on full display."
        "She says, her tone playful but a little surprised."
        mc.name "Come on, don't you want to show them off? I bet they look great."
        the_person "Oh, they do. I just... Feel a little self-conscious about being naked around you, alright?"
        "She says, her voice a little softer."
        mc.name "There's no need to be, just relax and let me take your [the_clothing.display_name] off for you."
        the_person "Oh darling, what are you getting me into [the_person.mc_title]? Fine, let's do it!"
        "She says, her tone resigned but playful."
    return

label goudere_bare_pussy_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > (50 - the_person.opinion.showing_her_ass * 5):
        the_person "Ah, darling, it's about time you got me out of my [the_clothing.display_name]!"
        "She says, her voice dripping with seduction."
    elif the_person.love > 35:
        the_person "You want to get me out of my [the_clothing.display_name] and get a look at my pussy?"
        "She says, her voice playful and teasing."
        if the_person.has_taboo("touching_vagina"):
            mc.name "I know, that was the plan."
            the_person "Well... I guess we both knew where this was going. Okay, go for it." 
            "She says, her eyes never leaving yours."
        else:
            mc.name "I've already felt it up, I thought I should see it too."
            the_person "I think you're right. Go on then, I'm not going to stop you."
            "She says, her voice sultry."
    else:
        the_person "Already trying to get me out of my [the_clothing.display_name], huh?"
        "She says, her tone playful but a little surprised."
        if the_person.has_taboo("touching_vagina"):
            mc.name "Yep, I am. Any problems with that?"
            the_person "Well... Maybe if you ask nicely."
            mc.name "[the_person.title], can I please take your [the_clothing.display_name] off and get a look at your pussy?"
            the_person "You're such a charmer. Of course you can."
            "She says, her eyes sparkling with flirtation."
        else:
            mc.name "Yep, I am. I've already felt your pussy up, I want to get a look at it now."
            the_person "Oh you're such a charmer. Alright then, what are you waiting for?"
            "She says, her voice playful but a little excited."
    return

# label goudere_facial_cum_taboo_break(the_person):

#     return

# label goudere_mouth_cum_taboo_break(the_person):

#     return

# label goudere_body_cum_taboo_break(the_person):

#     return

label goudere_creampie_taboo_break(the_person):
    if the_person.wants_creampie:
        if the_person.knows_pregnant:
            the_person "Mmm, yes, give it to me. Fill me up with your hot load."
            "She purrs seductively."

        elif the_person.on_birth_control:
            if the_person.has_significant_other:
                the_person "Oh, I'm such a naughty [the_person.so_girl_title], but I couldn't resist this."
                the_person "My [the_person.so_title] would understand, wouldn't he? A girl has needs!"
            else:
                the_person "Oh my god, I needed this so badly! Ah..."

        elif the_person.effective_sluttiness() > 75 or the_person.opinion.creampies > 0:
            if the_person.has_significant_other:
                the_person "Oh god, I've wanted a good creampie for so long!"
                the_person "I'm a terrible [the_person.so_girl_title], but I really just want a man to fuck me, cum in me, and knock me up!"
                "She bats her eyelashes flirtatiously."
            else:
                the_person "Oh god, I've wanted a good creampie for so long!"
                the_person "I've finally found a man to fuck me, cum in me, and knock me up!"
                "She giggles seductively."

            "She sighs happily."
            the_person "How long until you're ready for round two? I want as much of your cum inside my pussy as possible."
            "She winks at you."
        else:
            if the_person.has_significant_other:
                the_person "Oh fuck... I'm such a naughty [the_person.so_girl_title]!"
                "She sighs happily."
                the_person "But that felt so good!"
            else:
                the_person "Oh fuck, that was so risky."
                "She sighs happily."
                the_person "But it felt so good!"
            the_person "I'll just have to hope you haven't knocked me up. We really shouldn't do this again, my luck is going to run out at some point."
            "She pouts playfully."
    else:
        if the_person.knows_pregnant:
            the_person "Oh shit, you came right inside me."
            "She grins mischievously."
        elif not the_person.on_birth_control:
            the_person "Oh fuck, did you cum inside me?"
            "She looks at you with a mix of surprise and excitement."
            if the_person.has_significant_other:
                the_person "What if you just got me pregnant? I would be the worst [the_person.so_girl_title] of all time!"
                "She giggles nervously."
            else:
                the_person "What if I get pregnant? I'm not ready for that kind of responsibility!"
                "She frowns playfully."

            the_person "You're going to have to wear a condom if we ever do this again, I just can't risk it."
            "She winks at you."

        elif the_person.has_significant_other:
            the_person "Did you really just creampie me after I told you to pull out?"
            "She sighs unhappily."
            the_person "God, I'm such a terrible [the_person.so_girl_title]. Maybe next time I'll make you wear a condom as punishment."

        elif the_person.opinion.creampies < 0:
            the_person "Oh man, really? Ugh, I hate this feeling. Couldn't you have cum on my face or something?"
            "She pouts."
        else:
            the_person "Hey, I said to pull out!"
            "She looks at you with a playful scolding."
            the_person "Whatever, can you at least try to pull out next time?"
            "She winks at you."
    return

label goudere_anal_creampie_taboo_break(the_person):
    if the_person.opinion.anal_creampies > 0:
        if the_person.effective_sluttiness() > 75 or the_person.opinion.anal_creampies > 1:
            if the_person.has_significant_other:
                the_person "Ah, finally! I don't even care that it's not my [the_person.so_title] shooting his cum in my ass!"
                "She giggles seductively."
                the_person "I can't wait to tell him about this!"
            else:
                the_person "Ah, finally! You should have put a load inside my ass sooner!"
                "She winks at you."
            "She pants happily for a moment."
            the_person "Fuck yeah, I will be dripping cum out of my ass all day long! That's so hot."
            "She purrs seductively."
        else:
            if the_person.has_significant_other:
                the_person "Fuck me, I should have told you to pull out, but I love this feeling..."
                the_person "My [the_person.so_title] never shoots his cum in my ass, but you can do it anytime!"
                "She grins mischievously."
            else:
                the_person "Fuck yeah, promise you will fill my ass everytime... it just feels awesome..."
                the_person "All that cum in my tight little ass..."
                "She bats her eyelashes flirtatiously."
    else:
        if the_person.has_significant_other:
            the_person "Fuck [the_person.mc_title], I told you to pull out. My [the_person.so_title] will see your cum leaking out of my ass..."
            the_person "So next time, just shoot your load on my ass, okay?"
            "She pouts playfully."
        elif the_person.opinion.anal_creampies < -1:
            the_person "Fuck [the_person.mc_title], I said to pull out! I'll be dripping cum out of my ass all day long."
            "She scowls slightly."
        else:
            the_person "Fuck [the_person.mc_title], not inside! My ass is not a sperm bank, although that sounds quite hot."
            "She looks at you with a playful scolding."
    return

label goudere_dual_penetration_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 75:
        the_person "Oh god, it always surprises me how big your cock is! You're going to tear my ass in half with that monster!"
        "She seems more turned on by the idea than worried."
        the_person "But I love it when you make me feel like that."
        mc.name "Don't worry, you'll be stretched out soon enough."
        "She purrs seductively."
    elif the_person.love >= 60:
        the_person "So you really want to do this? It might be a little hard to fit all of your cock inside me..."
        mc.name "Don't worry about that, I'll have you stretched out soon enough."
        the_person "Fuck, just try and make sure you don't break me permanently!"
        "She grins mischievously."
    else:
        if the_person.has_taboo("vaginal_sex"):
            the_person "Are you sure my pussy wouldn't be tight enough for you, I don't even know if I can fit your cock in my ass!"
            mc.name "I'll make it fit, but you might not be walking right for a few days."
            the_person "Oh fuck..."
            "She looks at you with a mix of apprehension and excitement."
        else:
            "She closes her eyes and talks quietly to herself."
            the_person "Whew, deep breathes [the_person.fname]. You can do this..."
            mc.name "Are you okay?"
            the_person "Yeah, of course. I'm just... a little nervous. Fuck, I don't normally feel like this."
            "She laughs and shakes her head."
            the_person "Not that I normally do, you know, this. I don't know what's gotten into me."
            mc.name "Hopefully me, soon."
            the_person "No time like the present then. Do it, before I chicken out!"
            "She winks at you."
    return

label goudere_sleepover_yourplace_response(the_person): #Invited her over to spend the night
    the_person "Oh god, yes of course! We can have a great night together! And I'm sure I'll be able to keep up with your energy."
    "She bats her eyelashes flirtatiously."
    the_person "I can't wait to see how much fun we can have."
    "She grins mischievously."
    return

label goudere_sleepover_herplace_response(the_person): #Spending the night at her place
    the_person "I would love it when you come over, you can spend the night and make me float on cloud nine."
    "She purrs seductively."
    the_person "I'll make sure you'll have a night to remember."
    "She winks at you."
    return

label goudere_sleepover_yourplace_sex_start(the_person): #Right before sexy times at your place
    "[the_person.title] slowly walks over to you, her eyes seeming to sparkle with anticipation."
    the_person "Well, are you ready to show me a good time? I'm more than ready to receive your attention."
    "She purrs seductively, leaning in close to your ear."
    return

label goudere_sleepover_herplace_sex_start(the_person): #Right before sexy times at her place
    the_person "Are you just going to stand there?"
    "She gives you a mischievous smirk."
    mc.name "Are you ready?"
    the_person "Hah! Oh my god, I was born ready..."
    "She sets her wine down and gives you a bold, seductive smile."
    the_person "Get over here! I need you to fuck me hard and deep!"
    "She leans in close, her breath hot against your ear."
    return

label goudere_sleepover_impressed_response(the_person):  #If you've made her cum a lot
    the_person "Ah fuck, you're melting my brain... promise me you keep fucking me like that..."
    "She purrs seductively."
    $ the_person.draw_person(position = "missionary")
    "[the_person.title] lies down in bed, her body still trembling from the orgasm."
    the_person "I'm sure I can go for another round... although I might have some difficulty walking straight in the morning!"
    "She grins mischievously."
    return

label goudere_sleepover_good_response(the_person):  #If you've made her cum
    the_person "Well, that wasn't too bad..."
    "She smiles playfully."
    $ the_person.draw_person(position = "missionary")
    "[the_person.title] lies down in bed, her body still trembling from the orgasm."
    the_person "Could you give me another pounding before we go to sleep?"
    "She winks at you."
    return

label goudere_sleepover_bored_response(the_person):
    mc.name "Oh, come now, [the_person.title]. Don't be like that. I thought you were enjoying yourself."
    the_person "Enjoying myself? You call this enjoyable? You're not even trying, [mc.name]."
    mc.name "Trying? I'm trying to make sure you're satisfied, my dear. But if you're not happy, I'm willing to try new things."
    the_person "Hmph. We'll see about that. You'd better prove yourself to me."
    mc.name "Oh, I'll prove myself to you, all right. Just give me a little more time to work my magic."
    the_person "Fine, but don't disappoint me, [mc.name]. I expect more from someone as talented as you."
    mc.name "Don't worry, my little temptress. I'll make sure you're screaming my name in pleasure before the night is over."
    "You lean in close to [the_person.title], your breath hot against her ear as you whisper sweet nothings to her. She shivers at your touch, her body responding to your advances."
    "You continue to caress her, teasing her nipples and rubbing your fingertips against her inner thighs. She moans softly, her eyes rolling back in pleasure."
    "As you work your magic, you notice that [the_person.title] is getting closer and closer to the edge. You take this opportunity to slip a finger inside her, feeling her wetness and warmth enveloping you."
    return
