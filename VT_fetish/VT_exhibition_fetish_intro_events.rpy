# Fetish Labels
label VT_exhibition_fetish_employee_intro_label(the_person):
    "You are finishing up the last of your work today and closing up. All your employees should be gone for the day."
    $ mc.change_location(lobby)
    "You massage your neck pondering over tomorrows tasks as you approach the lobby and hear dance music bouncing around the room."
    "You blink a few times to make sure you are seeing what your seeing, but your vision is perfectly fine..."
    $ the_person.apply_outfit(Outfit("Nude"))
    $ the_person.draw_person()
    "You watch as [the_person.mc_title] is happily dancing to her dance music in her birthday suit! You chuckle... and she notices!"
    the_person "Ah! [the_person.mc_title]... I was hoping to catch you alone. I need to talk to you about something."
    mc.name "Good evening [the_person.title]. What can I do for you?"
    the_person "Ah... more like... what can you do to me..."
    "Did you hear that right?"
    mc.name "Oh?"
    the_person "I umm... I mean... sorry."
    "She looks a bit flustered for a second, but quickly gathers her thoughts and starts to talk to you."
    "She seems perfectly oblivious that she's naked in the lobby, and quickly realizes the music still blaring and turns it off."
    "She puts on some 'S&M' by Rihanna, and starts dancing to it. You like where this is going..."
    "She dances quite provocatively, the way she slides her hands down to her ass and gives it nice squeeze and slap."
    "Sliding her hands back up her sides to grope her breast to squeeze and winks at you."
    the_person "Na-na-na, come on, come on, come on..."
    $ the_person.change_arousal (50)
    $ mc.change_locked_clarity(50)
    "Her hormones must really be effecting her, for her to be this forward with you. You decide to take advantage of the situation... and of her."
    "You get close to her. She wraps her arms around you as you get close."
    $ the_person.draw_person(position = "kissing")
    mc.name "So what you are saying is..."
    "You grab her ass and grope it, pushing into her."
    mc.name "... You wouldn't mind it if..."
    $ the_person.draw_person(position = "against_wall")
    "You roughly pick her up and slowly move her backwards."
    mc.name "... I just pushed you back..."
    "You keep her backing up until her ass runs into the edge of someone's desk."
    mc.name "... Onto this desk..."
    $ the_person.draw_person(position = "missionary")
    "You force her down onto her back."
    the_person "Oh my god..."
    if the_person.vagina_available:
        "You reach down and pull your cock out from your pants."
    else:
        "As you start to pull your cock out, [the_person.possessive_title] reaches down and starts pulling her clothes off."
        $ the_person.strip_to_vagina(prefer_half_off = True, position = "missionary")
    $ the_person.change_arousal (15)
    $ mc.change_locked_clarity(50)
    mc.name "... and pinned you down..."
    "You grab her hands and force them down at her sides. She has a wild look in her eye as your raw cock nears her cunt."
    mc.name "... and fucked your brains out..."
    "As you finish those words, you push yourself inside her."
    $ play_moan_sound()
    "She moans as it goes in."
    $ the_person.change_arousal (20)
    $ mc.change_locked_clarity(50)
    $ the_person.break_taboo("condomless_sex")
    $ the_person.break_taboo("vaginal_sex")
    mc.name "... and didn't stop until I mark your body with my cum?"
    the_person "Oh god! Yes do it! Oh fuck!"
    "Still holding her hands down, you start to thrust rapidly. It's time to mark this horny slut!"
    call fuck_person(the_person, start_position = breeding_missionary, start_object = make_desk(), private = False, skip_intro = True, position_locked = True, skip_condom = True) from _VT_exhibition_fetish_employee_intro_01

    # if the_person.has_creampie_cum:
        # the_person "Oh god! It's so deep! Oh thank you so much [the_person.mc_title]!"
    # else:
        # the_person "Oh god, so deep and it isn't leaking out!"
        # pass
    $ VT_add_exhibition_fetish(the_person)
    # if the_person.knows_pregnant:
        # the_person "I don't care if I am already pregnant... Please do that again! My body was made to take your cum like that!"
    # else:
        # the_person "I hope that did it, but you'd better cum inside me again and again anyway!"
    "You slowly back away from [the_person.title], admiring your cum covered slut."
    "She purrs and grin proudly as she rubs your cum to soak into her skin."
    $ the_person.draw_person()
    "[the_person.possessive_title!c] slowly stands up, her legs are a little unsteady."
    mc.name "I need to get a few more things done before I close up the office. From now on, you are my slut. Be ready to take my cum whenever I tell you to!"
    the_person "Yes! Yes sir! I'll be ready, don't worry!"
    $ the_person.draw_person()
    "You say goodbye to [the_person.title]."
    "[the_person.possessive_title!c] now has an exhibition fetish to get fucked by you in public spaces!"
    return #Needs testing

label VT_exhibition_fetish_family_intro_label(the_person):
    $ mc.change_location(bedroom)
    $ the_person.arousal = 40
    $ towel_outfit = Outfit("Towel")
    $ towel_outfit.add_dress(towel.get_copy())
    "Noticing the door is open, you walk up to [the_person.possessive_title]'s bedroom door. As you approach, you hear noises coming from inside."
    the_person "Oh... mmm... oh fuck yeah... That's it baby..."
    "As you sneak closer, you look in and see [the_person.title], face down ass up on her bed with her fingers between her legs."
    $ the_person.apply_outfit(Outfit("Nude"))
    $ the_person.draw_person(position = "doggy")
    $ mc.change_locked_clarity(25)
    $ play_moan_sound()
    "Her moans are soft. She's getting into it, but probably hasn't been going at it for long yet."
    $ the_person.change_arousal(10) #50
    "She's running two fingers in a circle around her clit for a bit, then plunges them inside herself."
    the_person "Oh god! That's it [the_person.mc_title]... Fuck me yeah..."
    "Damn! She's fantasizing about you! You lean in and listen closer."
    $ the_person.change_arousal (10) #60
    $ play_moan_sound()
    the_person "Ooohhhh, yes... Yeah I want you to pull out and cover my ass in your cum... oh fuck yes..."
    $ mc.change_arousal(25)
    "Your pants are getting tight. This is very sexy. It sounds like she is fantasizing about you cumming all over her."
    "You've both been fooling around a lot lately, so it is not surprise she might be developing a bit of a fetish."
    the_person "Fuck me [the_person.mc_title]... I know we're related... I don't care... oh yessss!"
    $ the_person.change_arousal(10) #70
    $ mc.change_locked_clarity(50)
    "She's clearly getting off on this. You wonder if you should make your presence known? You could fuck her, then pull out and cum all over her ass, just how she is fantasizing."
    # if the_person in get_cum_fetish_unique_dialogue_list():
        # "Warning, this character is unique, and may have unique fetish dialogue. If you continue, you may miss this dialogue!"
    menu:
        "Train her to be a exhibitionist" if mc.energy > 40:
            pass
        "Too tired" if mc.energy <= 40:
            pass
            #TODO re add the event for this person for the next day.
            $ VT_fetish_timer_reset(the_person, "exhibition")
            $ clear_scene()
            return
        "Lave her alone":
            "You decide to leave her alone for now. You might revisit this decision at a later date."
            $ VT_fetish_timer_reset(the_person, "exhibition", 2)
            $ clear_scene()
            return False
    "This is it, time to be bold. You step into the room and say casually"
    mc.name "So ready for the mall?"
    $ the_person.draw_person(position = "sitting")
    the_person "Oh fuck! [the_person.mc_title]? What are... how long have you been there?"
    "[the_person.possessive_title!c] quickly sits up, she grabs a sheet and tries to cover herself."
    $ the_person.apply_outfit(towel_outfit)
    $ the_person.draw_person(position = "sitting")
    mc.name "Long enough. It's okay [the_person.title]. You don't have to be ashamed of anything."
    the_person "It's... I'm not, I just didn't realise the door was open... wait.. what do you mean 'Ready for the mall'?"
    "You step closer to the bed with a michevious smile dances on your lips"
    mc.name "I got really turned on hearing you talk about what you want. I decided I wanted to give it to you."
    "[the_person.possessive_title!c] begins to ramble excuses, but the look on her face as you approach isn't dismay, but more like hope."
    the_person "You don't... I mean... that would be crazy... but you could?"
    mc.name "I want to. Now put that silly sheet down."
    $ the_person.apply_outfit(Outfit("Nude"))
    $ the_person.draw_person(position = "sitting")
    "[the_person.title] gives in and drops the sheet. You get closer until you are standing right in front of her."
    mc.name "That's it. Now, you're already all warmed up. Why don't you give me a kiss and help me catch up a little."
    "Still sitting on the edge of the bed, [the_person.possessive_title] looks up at you as you bring your cock up to her face."
    if the_person.is_bald:
        "You run your hand over her smooth head, as she begins to lick around the tip of your dick."
    else:
        "You run your hand through her [the_person.hair_description] a couple times, as she begins to lick around the tip of your dick."
    "She licks up some of your precum."
    "So, I was thinking, maybe we should break in the mall bathroom and changing rooms..."
    the_person "Mmm... o..h my god, that would be so hot. But its so risky!"
    mc.name "Look how turned on you are. Your nips are like pins!"
    the_person "Yeah, I suppose. mmms"
    "She opens her mouth and then takes you in. Her sultry lips feel amazing as they descend your cock, then slowly pull back off."
    $ mc.change_locked_clarity(30)
    "[the_person.possessive_title!c] gives you a couple slow strokes then pulls off for a breath."
    the_person "Mmm, I can't believe how hot your cock is [the_person.mc_title]..."
    "[the_person.title] opens up and starts to go at it. Her lips smack against each other each time she pulls back."
    "[the_person.possessive_title!c] is reaching down with her free hand and has begin to play with herself. Her moans around your erection feel amazing."
    $ the_person.change_arousal(10) #80
    $ mc.change_locked_clarity(50)
    "She starts getting carried away with sucking you off, so you stop her. Grabbing her by the hair you pull her head back."
    mc.name "Imagine us at the mall fucking, with the risk of getting caught. Get on your hands and knees. I have a fantasy to fulfil now."
    $ the_person.draw_person(position = "doggy")
    "When she gets in to position, you get behind her. With hands on her hips, you push yourself inside her."
    #TODO break vaginal taboo if required
    "[the_person.possessive_title!c]'s cunt is soaked and you slide in easily. The warm grip feels great when you bottom out."
    the_person "Go ahead [the_person.mc_title]... I'm so wet, give it to me good!"
    "You grab onto [the_person.title] by her hips and settle into a steady rhythm, pumping your cock in and out of her tight pussy."
    $ the_person.call_dialogue("sex_responses_vaginal")
    "The sounds of slapping echo all around the room as you give it to her. Soon, her moans begin to increase in intensity and pace."
    $ the_person.change_arousal(30) #110
    $ mc.change_locked_clarity(50)
    the_person "Oh god [the_person.mc_title] I'm cumming... I'm cumming!"
    "You keep up your pace while [the_person.possessive_title] cums. You think you can feel her pussy twitch around your cock."
    $ the_person.have_orgasm() #55
    $ mc.change_arousal(25) # 80
    "You don't let up at all. You keep pounding [the_person.title] as you are getting close to your own orgasm now."
    mc.name "God [the_person.title] your pussy is so good."
    the_person "On my ass... I want you to mark my body with your cum!!"
    $ the_person.change_arousal(30) #85
    $ mc.change_locked_clarity(50)
    "You pump your hips as hard as you can for as long as you can, but right when you are about to cum you pull out."
    "You stroke yourself as you pump your load all over her body, coating it in your cum."
    $ the_person.cum_on_ass()
    $ the_person.draw_person(position = "doggy")
    $ ClimaxController.manual_clarity_release(climax_type = "body", person = the_person)
    $ mc.reset_arousal()
    the_person "Oh fuck! It feels so good! Cover me [the_person.mc_title]!"
    "You unload everything you have. Her ass and up her back, covered in sperm, is a work of art."
    "However, you want to push things a little further and make sure you really make [the_person.possessive_title] your cumslut."
    mc.name "That was hot. Your ass is covered! I bet you wish you could taste it huh?"
    the_person "Ahhh, yeah that would be nice..."
    mc.name "Here, let me help."
    "You use two fingers and scoop up some of your cum, then lean forward and reach around her head, putting it up to her mouth."
    mc.name "Go ahead, open up."
    "[the_person.title] opens her mouth and eagerly starts to suck on your fingers. She moans when she gets a good taste of your cum."
    $ the_person.cum_in_mouth()
    $ mc.change_locked_clarity(20)
    mc.name "That's it. Here, I bet you could even cum again doing this."
    "You bring your hand back and scoop up a little more. This time as you bring it back to her mouth she already has her mouth open and eagerly starts to suck on your fingers."
    "With your other hand, you rub some of your cum on her ass, then bring your fingers down to her pussy."
    "Your slick cum spreads easily across her labia. With a little bit left on the tip of your fingers, you push them into her steaming cunt."
    "She moans but keeps sucking on your fingers, as you finger-fuck her with your other hand."
    mc.name "Imagine me fucking you in the mall bathroom, or the changing room... the risk of.. getting caught.."
    $ the_person.change_arousal(30)
    $ mc.change_locked_clarity(20)
    "Soon she is moaning and bucking her hips back against you hand."
    "[the_person.title]'s cries are muffled by your fingers as she cums again, her body trembling in pleasure."
    $ the_person.have_orgasm(half_arousal = False)
    "When she finishes, you slowly withdraw your fingers and start to get up."
    $ VT_add_exhibition_fetish(the_person)
    the_person "[the_person.mc_title]... that was amazing... but we can't tell anyone... okay?"
    mc.name "I know [the_person.title]. It's okay. You can be my secret cumslut."
    $ the_person.draw_person()
    "[the_person.possessive_title!c] slowly stands up and turns to you. You can see a tiny bit of your cum dribbling down her lip."
    mc.name "I need to get going. Take care [the_person.title]. Remember... the mall!"
    "You hear her slightly moan when you say mall, and left her with lots of possibilities in her head."
    "You say goodbye to [the_person.possessive_title] then leave her room. As you walk away, you can't help but smile."
    $ clear_scene()
    "Your have turned her into your cumslut. Now to see if you can push her into more at the mall."
    $ the_person.apply_planned_outfit()
    return True 

label VT_exhibition_fetish_generic_intro_label(the_person):
    "Sighing as you play solitare while enjoying your mini break, your phone buzzes with a text."
    "Having nothing better to do at the moment you pick it up and see what is the matter."
    $ mc.phone.add_non_convo_message(the_person, "Hey, are you available?")
    $ mc.phone.add_non_convo_message(the_person, "I want to see you right now. I so horny!")
    $ mc.phone.add_non_convo_message(the_person, "I really need to fuck! Want to fuck me?")
    $ mc.phone.add_non_convo_message(the_person, "Want to meet me at the mall PLEASE!")
    "[the_person.title] has been texting you. She's sent you several messages, with the last ending:"
    $ mc.start_text_convo(the_person)
    mc.name "Sure, I'll see you there"
    the_person "I'm can't wait till you get here! Text me when you are here!"
    $ mc.end_text_convo()
    "Strange, but more interesting than Solitare, which you flick off as you get your ass out of your office."
    $ mc.change_location(mall)
    $ mc.start_text_convo(the_person)
    mc.name "I'm here, where are you?"
    the_person "Heyyyyyyy [the_person.mc_title]! I need your cock! Meet in the clothing store?"
    mc.name "Sure, I'll see you there."
    $ mc.end_text_convo()
    $ the_person.arousal = 40
    $ mc.change_location(clothing_store)
    "[the_person.title] is no where to be found, so you start browsing the clothing as a customer."
    "As you look up, you see [the_person.title]'s face pop out of one of the changing rooms and she mouths 'come here'"
    "You chuckle and look around to make sure no one notices as you approach the changing rooms."
    "Her hand snatches you and pulls you into her changing room quickly"
    $ the_person.arousal = 61
    $ mc.change_location(changing_room)
    $ the_person.apply_outfit(Outfit("Nude"))
    $ the_person.draw_person(position = "sitting")
    the_person "Omg, my heart is pounding! I've been wanting to do this with you for awhile now!"
    $ mc.change_locked_clarity(50)
    $ the_person.draw_person(emotion = "happy")
    the_person "Oh [the_person.mc_title], I just keep on thinking about your nice cock and its sweet nectar, you need to help me!"
    "Even before you have time to respond, she drops to her knees and pulls out your flaccid member."
    $ the_person.draw_person(position = "blowjob")
    menu:
        "Ok, go ahead, make my day":
            mc.name "Ok, go ahead, but make it quick, its risky here."
            $ mc.change_locked_clarity(50)
            "She quickly takes you in her mouth, slowly making your cock hard as a rock."
            $ the_person.break_taboo("sucking_cock")
            the_person "Mmh, I love it when I can feel it grow in my mouth."
            "[the_person.possessive_title!c] begins bobbing her head up and down eagerly, hungry for your delicious cum."
            # call fuck_person(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = True, position_locked = True) from _call_fuck_person_SBC10B
            call get_fucked(the_person, goal="get mc off", start_position = blowjob, start_object = make_floor(), private=False, skip_intro = True, allow_continue = False) from _call_get_fucked_VT_exhibition_fetish_generic_intro_01
            $ VT_add_exhibition_fetish(the_person)

            "[the_person.possessive_title!c] is moaning ecstatically."
            if the_person.has_face_cum:
                "Glancing down, you see [the_person.possessive_title] running her hands along her face, rubbing your cum into her skin."
                the_person "Mmm... it feels so good! That first splash is always the best..."
            else:
                "Glancing down, you see [the_person.possessive_title] licking her fingers. There isn't a trace of your cum anywhere, she has swallowed every drop."
                the_person "Mmm... your taste is so unique, I love it!"
            "[the_person.possessive_title!c] stands up."
            $ the_person.draw_person(emotion = "happy")
            the_person "Wow, that was amazing, [the_person.mc_title]. I don't know what has been coming over me lately..."
            "[the_person.possessive_title!c] blushes and pauses..."
            mc.name "Did you get what you were hoping for?"
            the_person "Oh, I think I'm good for today... but I'm sure it won't be long until I need your come again..."
            if the_person.is_bald:
                "[the_person.possessive_title!c] runs her fingers over her lips and smiles at you."
            else:
                "[the_person.possessive_title!c] runs her hand through her [the_person.hair_description]. She licks her lips and smiles at you."
            $ the_person.apply_planned_outfit(show_dress_sequence = True)
            the_person "Thanks again, [the_person.mc_title]. We should do this again... and soon."
            $ the_person.draw_person(position = "walking_away", emotion = "happy")
            "You wave goodbye to [the_person.possessive_title] and quickly put away your cock as you poke your head out the change room."
            "Coast is clear, so you step out of the change room and head back to the office."
        "Not today":
            mc.name "I'm sorry, [the_person.title], but I can't right now."
            $ the_person.draw_person(emotion = "angry")
            the_person "Really?! I'm so stupid, thinking you would be brave enough for this."
            $ the_person.draw_person(position = "walking_away", emotion = "angry")
            "You watch her, slip out of the changing room, while you put away your dick. You sigh and head back to the office."
            $ VT_fetish_timer_reset(the_person, "exhibition", 2)
    $ the_person.apply_planned_outfit()
    $ mc.change_location(lobby)
    $ clear_scene()
    return

label VT_exhibition_fetish_mom_intro_label():
    return False

label VT_exhibition_fetish_lily_intro_label():
    return False

label VT_exhibition_fetish_rebecca_intro_label():
    return False

label VT_exhibition_fetish_gabrielle_intro_label():
    return False

label VT_exhibition_fetish_stephanie_intro_label():
    return False

label VT_exhibition_fetish_alex_intro_label():
    return False

label VT_exhibition_fetish_nora_intro_label():
    return False

label VT_exhibition_fetish_emily_intro_label():
    return False

label VT_exhibition_fetish_christina_intro_label():
    return False

label VT_exhibition_fetish_starbuck_intro_label():
    return False

label VT_exhibition_fetish_sarah_intro_label():
    $ the_person = sarah
    "It's another Wednesday morning. The girls are starting to arrive for work and getting set up for the day."
    "You always enjoy when the girls get there in the morning. You check out some of their outfits, not so subtly, as they arrive."
    "You are just starting to think about calling one to the office for a quickie when someone interrupts your thoughts..."
    the_person "Ahem..."
    $ the_person.draw_person()
    mc.name "Ah, good morning [the_person.title]."
    the_person "Good morning. I umm, noticed you were checking out some of the employees..."
    mc.name "Ah, yes I was."
    the_person "I try to take care of your urges for you at the Monday meetings..."
    mc.name "Well, maybe..."
    the_person "Do you need me to take care of you again? I know it's hump day... I could do it right here?"
    "You look around. Several girls have already sat down at their desks and begun their work."
    "You look back at [the_person.possessive_title]. Is she blushing?"
    "You've been testing Social Sexual Proclivity Nanobots quite a bit on her lately. Is she doing this {i}because{/i} all the other girls are here?"
    "You reply to her in a voice that is louder than necessary, making sure all the girls around you hear it."
    mc.name "Yes [the_person.title]. Why don't you get on your knees and take care of it for me."
    $ the_person.change_happiness(3)
    the_person "Yes sir!"
    $ the_person.draw_person(position = "blowjob")
    "[the_person.possessive_title!c] gleefully gets down on her knees and pulls down your zipper. After pulling your cock out, she smiles up at you, then licks the tip."
    "You can hear murmurs from some of the girls around you, but it doesn't seem to phase her. If anything, she seems to be emboldened..."

    return

label VT_exhibition_fetish_ophelia_intro_label():
    return False

label VT_exhibition_fetish_candace_intro_label():
    return False

label VT_exhibition_fetish_dawn_intro_label():
    return False

label VT_exhibition_fetish_erica_intro_label():
    return False

label VT_exhibition_fetish_ashley_intro_label():
    return False

