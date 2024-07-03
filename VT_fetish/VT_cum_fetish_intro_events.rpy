### Function labels

label VT_cum_fetish_employee_intro_label(the_person):
    $ the_person.arousal = 40
    "It's the end of the day, and you and your employees are packing up to head out. However, one of your employees is acting a little suspicious and milling around."
    "The rest of the girls in her department pack up and head out, while she clearly is wasting time. You decide to ask her if she's okay."
    $ the_person.draw_person()
    "You walk up to her."
    mc.name "Hey [the_person.title]. You doing okay? Everyone else has left for the day."
    the_person "Oh! Hi [the_person.mc_title]."
    "She looks around the room, noting that it's empty."
    the_person "I know it's... time to leave but..."
    "As you step closer to her, she suddenly rushes at you and wraps her arms around you."
    $ the_person.draw_person(position = "kissing")
    the_person "I'm sorry! I'm not ready to go home yet! I wanted to get your attention but I just couldn't do it with everyone around..."
    "She starts to kiss your neck. Her hand reaches down and starts to stroke your cock through your clothes."
    $ mc.change_locked_clarity(20)
    the_person "I know this is really forward, but can I ask you for a favour?"
    mc.name "I'd say you are in a good position to do that."
    the_person "I just wanted to know if I could suck you off. I'm not sure why, but lately every time I think about your cock, my mouth starts to water and it sounds so good..."
    "Wow, sounds like [the_person.title] is really hungry for your Vitamin dick. You wonder if she might be developing a fetish."
    "Do you want to try and train her into a cumslut?"
#    if the_person in get_cum_fetish_unique_dialogue_list():
#        "Warning, this character is unique, and may have unique fetish dialogue. If you continue, you may miss this dialogue!"
    menu:
        "Train her to be a cumslut" if mc.energy > 40:
            pass
        "Too tired" if mc.energy <= 40:
            pass
            #TODO re add the event for this person for the next day.
            $ VT_fetish_timer_reset(the_person, "cum")
            $ clear_scene()
            return
        "Refuse":
            "You decide to leave her alone for now. You might revisit this decision at a later date."
            $ VT_fetish_timer_reset(the_person, "cum", 2)
            $ clear_scene()
            return
    mc.name "I'll let you do that, but only if you do as I say when I finish."
    the_person "Oh? That sounds fun..."
    $ the_person.draw_person(position = "blowjob")
    "[the_person.possessive_title!c] drops to her knees and unzips your pants, then pulls your cock out."
    the_person "Mmm, it looks so tasty."
    "She opens her mouth and slowly licks some of your precum from the tip. You watch as she works her tongue around her mouth, savouring the taste."
    $ mc.change_arousal(15)
    $ mc.change_locked_clarity(50)
    if the_person.tits_available:
        "As she takes you in her mouth, she runs her fingers along her breasts, pinching and pulling at her nipples."
    else:
        mc.name "Get your tits out. I want something nice to look at."
        the_person "Mmm, okay."
        $ the_person.strip_outfit(exclude_upper = False, exclude_lower = True)
        "When she finishes, she takes you back in her mouth, she runs her fingers along her breasts, pinching and pulling at her nipples."
    call fuck_person(the_person, start_position = cum_fetish_blowjob, start_object = make_floor(), skip_intro = True, position_locked = True) from _call_fuck_VT_cum_fetish_employee_intro_01
    mc.name "Damn that was good. You really got off on that, didn't you?"
    the_person "Mmm... yeah..."
    mc.name "I want you to wipe some cum on your fingers, and rub it into your tits."
    the_person "Oh? That's... oh god that sounds hot..."
    "She takes her hand and wipes a bit of your cum off her face, then brings them down to her breasts..."
    $ the_person.cum_on_tits()
    $ the_person.draw_person(position = "kneeling1")
    $ the_person.change_arousal(20)
    $ mc.change_locked_clarity(30)
    mc.name "That's it. Feels good, doesn't it?"
    the_person "Your cum feels so good on my skin... it's electric!"
    mc.name "Good girl. Keeping going, rub some on your stomach..."
    the_person "Oh my god..."
    $ the_person.cum_on_stomach()
    $ the_person.draw_person(position = "kneeling1")
    "Taking what she can, [the_person.possessive_title] goes further, rubbing your cum onto her belly."
    $ the_person.change_arousal(20)
    $ mc.change_locked_clarity(30)
    "[the_person.title] is breathing rapidly now. When she looks up at you, her pupils are actually a little dilated. She is {i}really{/i} getting off on this!"
    mc.name "That's a good cumslut. You know what's coming next, right?"
    the_person "Oh god, probably me soon!"
    mc.name "Do it. Rub some cum around your cunt and get yourself off for me."
    the_person "Oh fuck yes!"
    $ the_person.draw_person(position = "kneeling1")
    $ the_person.change_arousal (25)
    $ mc.change_locked_clarity(50)
    "[the_person.possessive_title!c] immediately begins to finger herself rapidly. Once in a while she will wipe a bit of cum off her face, rub it in circles around her slit, then keep going."
    the_person "Oh god! [the_person.mc_title] I'm cumming!"
    $ the_person.have_orgasm()
    "[the_person.title] cries out as she cums. Her body convulses in waves as a strong orgasm overtakes her."
    "It takes several seconds for her to catch her breath."
    $ VT_add_cum_fetish(the_person)
    the_person "That... was amazing..."
    "You put your cock back in your pants and grab your stuff."
    $ the_person.draw_person()
    mc.name "You are such a good cum slut. I'll make sure to make use of your mouth again soon. Goodnight [the_person.title]."
    the_person "Good night [the_person.mc_title]!"
    $ clear_scene()
    $ mc.change_location(lobby)
    "You leave the office, setting the doors to lock automatically after [the_person.title] leaves. She definitely seems to have developed a fetish for your cum!"
    $ the_person.apply_planned_outfit()
    return True

label VT_cum_fetish_family_intro_label(the_person):
    $ mc.change_location(bedroom)
    $ the_person.arousal = 40
    $ towel_outfit = Outfit("Towel")
    $ towel_outfit.add_dress(towel.get_copy())
    "Noticing the door cracked, you walk up to [the_person.possessive_title]'s bedroom door. As you approach, you hear noises coming from inside."
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
    "You've been feeding her your cum a lot lately, so it is not surprise she might be developing a bit of a fetish."
    the_person "Fuck me [the_person.mc_title]... I know we're related... I don't care... oh yessss!"
    $ the_person.change_arousal(10) #70
    $ mc.change_locked_clarity(50)
    "She's clearly getting off on this. You wonder if you should make your presence known? You could fuck her, then pull out and cum all over her ass, just how she is fantasizing."
    #if the_person in get_cum_fetish_unique_dialogue_list():
    #    "Warning, this character is unique, and may have unique fetish dialogue. If you continue, you may miss this dialogue!"
    menu:
        "Train her to be a cumslut" if mc.energy > 40:
            pass
        "Too tired" if mc.energy <= 40:
            pass
            #TODO re add the event for this person for the next day.
            $ VT_fetish_timer_reset(the_person, "cum")
            $ clear_scene()
            return
        "Lave her alone":
            "You decide to leave her alone for now. You might revisit this decision at a later date."
            $ VT_fetish_timer_reset(the_person, "cum", 2)
            $ clear_scene()
            return False
    "This is it. It's time to be bold. You quietly step into the room. You quietly slip out of your clothes before she notices you."
    mc.name "Cum all over your ass? Is that what you want [the_person.title]?"
    $ the_person.draw_person(position = "sitting")
    the_person "Oh fuck! [the_person.mc_title]? What are... how long have you been there?"
    "[the_person.possessive_title!c] quickly sits up, she grabs a sheet and tries to cover herself."
    $ the_person.apply_outfit(towel_outfit)
    $ the_person.draw_person(position = "sitting")
    mc.name "Long enough. It's okay [the_person.title]. You don't have to be ashamed of anything."
    the_person "It's... I'm not, I just didn't realise the door was open... wait where are your clothes?"
    "You step closer to the bed."
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
    the_person "Mmm... that tastes so... good? It's funny... I'd never thought of cum as tasting so good before."
    mc.name "It's because of how turned on you are."
    the_person "Yeah, I suppose."
    "She opens her mouth and then takes you in. Her sultry lips feel amazing as they descend your cock, then slowly pull back off."
    $ mc.change_locked_clarity(30)
    "[the_person.possessive_title!c] gives you a couple slow strokes then pulls off for a breath."
    the_person "Mmm, I can't believe how hot your cock is [the_person.mc_title]..."
    "[the_person.title] opens up and starts to go at it. Her lips smack against each other each time she pulls back."
    "[the_person.possessive_title!c] is reaching down with her free hand and has begin to play with herself. Her moans around your erection feel amazing."
    $ the_person.change_arousal(10) #80
    $ mc.change_locked_clarity(50)
    "She starts getting carried away with sucking you off, so you stop her. Grabbing her by the hair you pull her head back."
    mc.name "Easy. I'd say I'm all warmed up now too. Get on your hands and knees. I have a fantasy to fulfil now."
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
    the_person "On my ass... I want you to finish on my ass!"
    $ the_person.change_arousal(30) #85
    $ mc.change_locked_clarity(50)
    "You pump your hips as hard as you can for as long as you can, but right when you are about to cum you pull out."
    "You stroke yourself as you pump your load all over her ass, coating it in your cum."
    $ the_person.cum_on_ass()
    $ the_person.draw_person(position = "doggy")
    $ ClimaxController.manual_clarity_release(climax_type = "body", person = the_person)
    $ mc.reset_arousal()
    the_person "Oh fuck! It feels so good! Cover me [the_person.mc_title]!"
    "You unload everything you have. The ass in front of you, covered in sperm, is a work of art."
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
    $ the_person.change_arousal(30)
    $ mc.change_locked_clarity(20)
    "Soon she is moaning and bucking her hips back against you hand."
    "[the_person.title]'s cries are muffled by your fingers as she cums again, her body trembling in pleasure."
    $ the_person.have_orgasm(half_arousal = False)
    "When she finishes, you slowly withdraw your fingers and start to get up."
    $ VT_add_cum_fetish(the_person)
    the_person "[the_person.mc_title]... that was amazing... but we can't tell anyone... okay?"
    mc.name "I know [the_person.title]. It's okay. You can be my secret cumslut."
    $ the_person.draw_person()
    "[the_person.possessive_title!c] slowly stands up and turns to you. You can see a tiny bit of your cum dribbling down her lip."
    mc.name "I need to get going. Take care [the_person.title]."
    "You say goodbye to [the_person.possessive_title] then leave her room. As you walk away, you can't help but smile."
    $ clear_scene()
    "Your have turned her into your cumslut."
    $ the_person.apply_planned_outfit()
    return True

label VT_cum_fetish_generic_intro_label(the_person):
    $ mc.change_location(bedroom)
    "Some time late in the night, you're awoken by the buzz of your phone getting a text. You roll over and ignore it."
    "A few minutes later it buzzes again, then again. You're forced to wake up and see what is the matter."
    $ mc.phone.add_non_convo_message(the_person, "Hey, are you awake?")
    $ mc.phone.add_non_convo_message(the_person, "I want to see you tonight. Can I come over?")
    $ mc.phone.add_non_convo_message(the_person, "I really need to fuck! Want to fuck me?")
    $ mc.phone.add_non_convo_message(the_person, "Oh my god, never mind. I shouldn't have sent that. I'm drunk.")
    $ mc.phone.add_non_convo_message(the_person, "I'm going to come over so I can apologise.")
    "[the_person.title] has been texting you. She's sent you several messages, with the last ending:"
    $ mc.start_text_convo(the_person)
    the_person "I'm here... Should I just knock on the door?"
    $ mc.end_text_convo()
    $ her_hallway.show_background()
    "You drag yourself out of bed and stumble out to the front hall. You move to a window and peek out at your front door."
    $ the_person.draw_person(emotion = "happy")
    "You see [the_person.title] standing outside. You open the door before she goes to knock."
    mc.name "[the_person.title], what are you doing here? It's the middle of the night."
    "[the_person.possessive_title!c] takes a step towards you, running a hand down your chest. You guide her outside so she won't wake up your mother or sister."
    the_person "Oh [the_person.mc_title], I just keep on thinking about your nice cock and its sweet nectar, you need to help me!"
    "Even before you have time to respond, she drops to her knees and pulls out your flaccid member."
    $ the_person.draw_person(position = "blowjob")
    menu:
        "Ok, go ahead":
            mc.name "Ok, go ahead, but make it quick, I don't want to disturb the neighbours."
            $ mc.change_locked_clarity(50)
            "She quickly takes you in her mouth, slowly making your cock hard as a rock."
            $ the_person.break_taboo("sucking_cock")
            the_person "Mmh, I love it when I can feel it grow in my mouth."
            "[the_person.possessive_title!c] begins bobbing her head up and down eagerly, hungry for your delicious cum."
            # call fuck_person(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = True, position_locked = True) from _call_fuck_person_SBC10B
            call get_fucked(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, allow_continue = False) from _call_get_fucked_VT_cum_fetish_generic_intro_01
            $ VT_add_cum_fetish(the_person)

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
            the_person "Oh, I think I'm good for today... but I'm sure it won't be long until I get hungry again..."
            if the_person.is_bald:
                "[the_person.possessive_title!c] runs her fingers over her lips and smiles at you."
            else:
                "[the_person.possessive_title!c] runs her hand through her [the_person.hair_description]. She licks her lips and smiles at you."
            $ the_person.apply_planned_outfit(show_dress_sequence = True)
            the_person "Thanks again, [the_person.mc_title]. We should do this again... and soon."
            $ the_person.draw_person(position = "walking_away", emotion = "happy")
            "You wave goodbye to [the_person.possessive_title] and quickly put away your cock. You turn around and go to bed."
        "Not tonight":
            mc.name "I'm sorry, [the_person.title], but I can't right now."
            $ the_person.draw_person(emotion = "angry")
            the_person "Really?! I'm so stupid, thinking you would help me out."
            $ the_person.draw_person(position = "walking_away", emotion = "angry")
            "You watch her walk away while you put away your dick. You turn around and go to bed."
            $ VT_fetish_timer_reset(the_person, "cum")
    $ the_person.apply_planned_outfit()
    $ mc.change_location(bedroom)
    $ clear_scene()
    return

label VT_cum_fetish_mom_intro_label():
    $ the_person = mom
    $ mc.change_location(bedroom)
    "Tired from a long day, you quickly fall asleep."
    "You are having some very pleasant dreams. [the_person.possessive_title!c] is posing for you in some sexy lingerie, then gets down on her knees..."
    $ the_person.increase_blowjobs()
    "Her velvet soft mouth wraps around your cock, and she begins to bob her head eagerly up and down your erection."
    "[the_person.possessive_title!c]'s skilled tongue teases and strokes you. The pleasure is so intense you slowly start to awaken from your naughty dream."
    "However, as you awaken, the pleasure you are experiencing continues."
    $ the_person.draw_person(position = "blowjob")
    "You look down and discover that [the_person.possessive_title] is between your legs. She has pulled your underwear down and is sucking you off."
    $ the_person.break_taboo("sucking_cock")
    $ mc.change_locked_clarity(50)
    mc.name "[the_person.title]? What are you..."
    "[the_person.possessive_title!c] interrupts you."
    the_person "Shhh, just lay back. I need your cum right now. I couldn't sleep, I was craving you so bad."
    "You lay back, [the_person.possessive_title] continues to suck you off."
    "Your mind is racing. You've been giving her your cum for a while now. Maybe she has developed a fetish, for your cum?"
    "[the_person.possessive_title!c] keeps her mouth open wide and bobs her head back and forth to slide your cock in and out. The feeling of her soft, warm mouth sends shivers up your spine."
    "She moans slightly as she strokes you with her soft, velvet lips. She pulls off for a second and looks at you."
    the_person "[the_person.mc_title]... I want you to cum wherever you want, okay? Just do it in me or on me somewhere..."
    "She opens her mouth and goes back to work. Her skilled mouth is quickly bringing you to an orgasm!"
    menu:
        "Cum in her mouth":
            "You rest your hand on her head, guiding her as she sucks you off."
            "With a little encouragement, you pull [the_person.possessive_title]'s head down a little further with each stroke."
            mc.name "That's it [the_person.title]. I'm going to cum in your mouth and I want you to swallow every drop."
            "[the_person.possessive_title!c] moans. She is ready for her prize."
            mc.name "Fuck, here I come!"
            "[the_person.possessive_title!c] moans and looks you in the eyes. She pulls off until just the tip of your cock is in her mouth and she begins to stroke you off eagerly."
            $ play_swallow_sound()
            "You erupt in orgasm into her greedy mouth. [the_person.possessive_title!c] is swallowing rapidly as you fill her mouth with your cum."
            $ play_moan_sound()
            "[the_person.possessive_title!c] is moaning uncontrollably around your twitching cock."
            $ the_person.cum_in_mouth()
            $ the_person.draw_person(position = "blowjob")
            $ ClimaxController.manual_clarity_release(climax_type = "mouth", person = the_person)
            $ VT_add_cum_fetish(the_person)
            "You look down and see [the_person.possessive_title]. She uses her finger to wipe up a bit of cum that leaked out of her mouth and licks it clean."
        "Cum on her face":
            if the_person.is_bald:
                "You rest your hand on her shiny head."
                mc.name "That's it [the_person.title]. I'm going to cum all over that pretty little face and head of yours."
            else:
                "You rest your hand on her head, slowly gathering her hair up."
                mc.name "That's it [the_person.title]. I'm going to cum all over that pretty little face of yours."
            "[the_person.possessive_title!c] moans. She is ready for her prize."
            mc.name "Fuck, here I come!"
            "[the_person.possessive_title!c] moans and looks you in the eyes. She pulls off your cock and strokes you eagerly, waiting for the first splash across her face."
            $ the_person.cum_on_face()
            $ the_person.draw_person(position = "kneeling1")
            $ ClimaxController.manual_clarity_release(climax_type = "face", person = the_person)
            "You erupt in orgasm and shoot your load across her glowing face. Her pupils dilate as her cum-addicted brain registers the presence of your cum on her skin."
            "[the_person.possessive_title!c] moans uncontrollably with every spurt."
            $ VT_add_cum_fetish(the_person)
            "Slowly recovering, you look at [the_person.possessive_title]'s cum-covered face. Her eyes are closed and she is absentmindedly playing with some of the cum that is starting to run down her neck."
    the_person "Oh... I needed that so bad... you have no idea."
    $ the_person.reset_arousal()
    "[the_person.possessive_title!c] slowly crawls up the bed and lays down next to you. You put your arm around her."
    $ the_person.draw_person(position = "missionary")
    "Completely satisfied, she quickly falls asleep."
    "Wow! [the_person.possessive_title] just woke you up, in the middle of the night, with an amazing blowjob, took your load, then cuddled up and fell asleep with you."
    "You have a feeling that this is only the beginning of things between you and her."
    $ clear_scene()
    "You slowly fall asleep, enjoying the warmth of her body."
    $ mc.change_locked_clarity(30)
    call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_VT_cum_fetish_mom_intro_01
    "When morning comes, you feel a stirring in your loins again as you start to slowly wake up. The now familiar feeling of [the_person.possessive_title]'s mouth feels amazing."
    $ the_person.apply_outfit(Outfit("Nude"))
    $ the_person.draw_person(position = "blowjob")
    $ mc.change_locked_clarity(50)
    "She senses that you are beginning to awaken."
    the_person "Good morning, [the_person.mc_title]. It's a new day... and I need another load of your cum..."
    "Last night she sucked you off. Maybe this morning you should repay the favour?"
    mc.name "Good morning. Why don't you get on top of me? I wanna eat your pussy for breakfast."
    the_person "Oh! That sounds good. As long as you promise to cum for me..."
    mc.name "Don't worry, I promise."
    $ the_person.draw_person(position = sixty_nine.position_tag)
    "[the_person.possessive_title!c] repositions and swings a leg over your body, presenting her pussy right in front of your face. You waste no time and start to flick your tongue around her slit."
    the_person "Mmm, that feels good [the_person.mc_title]... and your cock... it looks so good... I wanna swallow it whole!"
    "[the_person.possessive_title!c] begins to please you in return. Taking you into her mouth, she begins sucking you off."
    call fuck_person(the_person, start_position = sixty_nine, start_object = make_bed(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_fuck_VT_cum_fetish_mom_intro_03
    $ the_report = _return
    if the_report.get("girl orgasms", 0) > 0:
        "[the_person.possessive_title!c] lies on top of you for a little longer, recovering. She idly licks your rapidly softening cock and nuzzles it for a bit."
    $ the_person.draw_person(position = "stand5")
    "[the_person.possessive_title!c] stands up."
    the_person "Okay... I think I'm good for now. It's time to get up! Why don't you hop in the shower while I go make some breakfast?"
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title!c] leaves your room. Wow! What a night! She definitely has a fetish for your cum now."
    $ clear_scene()
    "You grab some clothes and head for the shower."
    python:
        the_person.apply_planned_outfit()
        mc.location.show_background()
    return "Advance Time"

label VT_cum_fetish_lily_intro_label():
    $ the_person = lily
    $ mc.change_location(bedroom)
    "You wake up a little groggy. Your head kinda hurts, so you grab some clothes and head towards the bathroom to take a hot shower. Hopefully the steam will help you feel better."
    $ mc.change_location(home_shower)
    "You stand in the shower, enjoying the hot water for several minutes. The steam is beginning to cloud up the bathroom."
    "You are surprised when the shower door opens. You see [the_person.possessive_title] getting in the shower with you."
    $ the_person.apply_outfit(Outfit("Nude"))
    $ the_person.draw_person()
    $ mc.change_locked_clarity(50)
    the_person "Good morning [the_person.mc_title]. Mind if I join you?"
    "You are surprised. She hasn't been this direct with you before. You quickly invite her in."
    the_person "Thanks! You were taking forever, and I got tired of waiting. This will be more fun than showering by myself, anyway."
    "[the_person.possessive_title!c] grabs some soap and begins soaping up her body. You watch her as she works the soap into her skin."
    the_person "Hey, can you get my back?"
    mc.name "Sure."
    $ the_person.draw_person(position = "back_peek")
    "[the_person.possessive_title!c] hands you her bath sponge. You give her back a good scrubbing."
    "When you finish you hand her the bath sponge back, but she doesn't turn around. Instead, she slowly leans back until she is up against you."
    "Her body now completely up against yours, your cock is rapidly hardening, resting in the crack of her ass. She starts to slowly move her hips back and forth, grinding against you."
    "[the_person.possessive_title!c] moans as she grinds against you. She turns around and wraps her arms around you."
    $ the_person.draw_person(position = "kissing")
    the_person "[the_person.mc_title]... it feels so good against me. I want to taste it!"
    "You are a little bit surprised."
    mc.name "Are you sure you want that? Or do you want me to fuck you?"
    "[the_person.possessive_title!c] shakes her head."
    the_person "No... I'm not sure what is going on with me lately, but I've just been craving your cum so bad..."
    $ the_person.draw_person(position = "blowjob")
    $ mc.change_locked_clarity(50)
    "[the_person.possessive_title!c] gets down on her knees in front of you."
    the_person "I feel like I'm going crazy... but I can't stop thinking about you. About swallowing your cum, or you cumming all over my face, or my body..."
    "You see [the_person.possessive_title] reaches down with one hand and start to touch herself. She runs her tongue up and down your shaft a few times."
    the_person "It's like I'm thirsty... but no amount of water I drink makes my thirst go away... Only when I think about drinking your sweet cum do I feel any better..."
    "[the_person.possessive_title!c] opens her mouth and starts to suck you off. You feel her soft, velvet mouth wrapped around you."
    $ the_person.break_taboo("sucking_cock")
    "[the_person.possessive_title!c] begins bobbing her head up and down eagerly, hungry for your delicious cum."
    # call fuck_person(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = True, position_locked = True) from _call_fuck_person_SBC40
    call get_fucked(the_person, sex_path = build_blowjob_path(the_person), start_object = make_floor(), skip_intro = True, allow_continue = False) from _call_get_fucked_VT_cum_fetish_lily_intro_01
    $ VT_add_cum_fetish(the_person)
    "[the_person.possessive_title!c] is moaning ecstatically. You start to worry that [mom.possessive_title] might hear."
    $ the_person.draw_person(position = "kissing")
    "[the_person.possessive_title!c] stands up and hugs you."
    the_person "Wow, that was amazing, [the_person.mc_title]. I don't know what has been coming over me lately..."
    "You hold her close."
    the_person "That was exactly what I've been craving."
    "She sighs happily."
    the_person "But... I can already feel the thirst. It's going to come back isn't it?"
    "Her body shivers slightly."
    the_person "I guess maybe it's those serums I've been testing for you. You'll help me, right? I'm going to need your cum again... and soon I think!"
    mc.name "Of course, [the_person.title]. I'll always be here for you."
    "[the_person.possessive_title!c]'s body melts into yours as she hears your words."
    the_person "Okay... I'm going to hop out of the shower now."
    $ clear_scene()
    $ mc.change_location(bedroom)
    "[the_person.possessive_title!c] gets out. You finish up with your shower, balls empty and ready for the day!"
    "She definitely seems to have developed a fetish for your cum."
    $ the_person.apply_planned_outfit()
    return

label VT_cum_fetish_rebecca_intro_label(the_person):
    $ scene_manager = Scene()  #Clean Scene
    $ scene_manager.add_actor(the_person, position = "sitting")
    $ the_person.arousal = 40
    if mc.energy < 100:
        $ mc.energy = 100
    "As you walk into [the_person.possessive_title]'s apartment, you see her sitting on the couch, watching some TV."
    the_person "Oh hey [the_person.mc_title]! Good to see you!"
    "She pats the couch next to her."
    the_person "I was just watching a show, but it's kind of dumb. Why don't you join me for a bit?"
    mc.name "That sounds good [the_person.title]. Want me to grab some wine first?"
    the_person "Nah, I'm not really in the mood for a drink tonight. Thanks though!"
    "Definitely unusual for [the_person.possessive_title]. She is usually ready for a glass anytime. You walk over to her and sit down."
    "When you sit down, she scoots over close to you. You raise your arm up and put it around her as she lays her head on your shoulder."
    "You feel her hand on your leg, rubbing your thigh. It slowly starts to creep higher until she is eventually rubbing your crotch."
    the_person "You know... [cousin.fname] won't be home for hours... she's always out so late these days."
    the_person "Want to have some fun on the couch? I'm not in the mood for wine, but I would love to have a drink of something else..."
    $ mc.change_locked_clarity(20)
    "Your pants are getting tight. Sounds like your sexy aunt wants to taste your cum!"
    "You've been dosing her with your cum a lot lately, so it is not surprising she might be developing a bit of a fetish."
    "You decide it's time to train her to be a proper cum slut."
    mc.name "You love cum, don't you?"
    the_person "I love {i}your{/i} cum..."
    mc.name "That's fair. If you want a drink, that's fine. If you do a good job, maybe we could even have a round two and I'll cover your ass in it too."
    $ the_person.change_arousal(15)
    $ mc.change_locked_clarity(30)
    the_person "Oh fuck... that sounds amazing..."
    "[the_person.title] starts pulling on your zipper, eager to get your cock out. As soon as it's out, she starts to go down on you."
    $ scene_manager.update_actor(the_person, position = "blowjob")
    if the_person.event_triggers_dict.get("has_blowjob_lesson", False):
        $ play_gag_sound()
        "The blowjob lessons she has received from [salon_manager.title] have really paid off. In no time she has your cock down her throat and is swallowing you like a pro."
    else:
        "With enthusiasm, [the_person.title] takes your cock in her mouth and goes to work."
    $ the_person.add_situational_slut("Thirsty", 20, "Needs your cum")
    call fuck_person(the_person, start_position = cum_fetish_blowjob, start_object = make_floor(), skip_intro = True, position_locked = True) from _call_fuck_VT_cum_fetish_rebecca_intro_01
    $ the_person.clear_situational_slut("Thirsty")
    $ scene_manager.update_actor(the_person, position = "kneeling1")
    $ VT_add_cum_fetish(the_person)
    "[the_person.possessive_title!c] is moaning ecstatically."
    if the_person.has_face_cum:
        "Glancing down, you see [the_person.possessive_title] running her hands along her face, rubbing your cum into her skin."
        the_person "Mmm... it feels so good! That first splash is always the best..."
    else:
        $ play_swallow_sound()
        "Glancing down, you see [the_person.possessive_title] licking her fingers. There isn't a trace of your cum anywhere, she has swallowed every drop."
        the_person "Mmm... you taste so good, I just can't get enough!"
    mc.name "God that was amazing. From now on, you're my little cumslut. Be ready to take a load anytime, and anywhere I tell you to."
    the_person "Yes... I'll be your cumslut!"
    mc.name "Good. Now get up and bend over the couch. I want to fuck another one of your holes tonight."
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(50)
    the_person "Yes [the_person.mc_title]! My holes are for you to use!"
    $ scene_manager.update_actor(the_person, position = "standing_doggy")
    if the_person.vagina_available:
        "As she bends over, her holes are on display for you. You run your hand along her slit a few times, the moisture immediately soaking your fingers."
    else:
        $ scene_manager.strip_to_vagina(person = the_person)
        "She wiggles her hips as you pull her clothes off. When you finish, her holes are on wonderful display for you."
    $ play_spank_sound()
    "The eagerness of [the_person.possessive_title] and her body on display soon has your cock hardening again. You give her ass a couple smacks with it and she moans."
    $ play_spank_sound()
    $ the_person.change_arousal(20)
    $ mc.change_locked_clarity(50)
    if the_person.has_anal_fetish:
        the_person "You can stick it in my ass if you want..."
        mc.name "I know. We've already established that your ass is always mine for the taking when I want it. But tonight I'm gonna take your pussy."
    if the_person.has_breeding_fetish:
        the_person "You can cum inside me if you want..."
        mc.name "I know. We've already established that I can seed your fertile cunt anytime I want to, but tonight I'm going to cover you with it instead."
    "You rub the tip of your cock against [the_person.possessive_title]'s cunt, feeling how nice and wet she is already. She moans, anticipating your penetration."
    "You continue to rub your dick against her pussy and gather more of her juices. She is already so wet you are soon slick with her secretions."
    "When you are ready, you push yourself inside her. You bottom out easily in one smooth stroke."
    "The heat and moisture of [the_person.title]'s cunt wrapped around your cock is exquisite. You take a moment and just enjoy being inside her."
    "Soon though, you get the urge to really give it to her. You grab her hips with both hands and start to fuck her vigorously."
    "You push yourself in as deep as you can go. [the_person.possessive_title!c] moans as you fill her completely."
    $ scene_manager.update_actor(the_person, position = "back_peek")
    $ mc.change_locked_clarity(50)
    "You push her down, face-first into the couch. You use your body weight to pin her prone to the couch. She turns her head and looks back at you as you keep fucking her."
    the_person "Give it to me! Oh fuck [the_person.mc_title] cum! I want you to cum all over me!"
    "[the_person.title] is trying to push her ass back against you with each thrust but lying prone, she has no leverage. You continue to relentlessly fuck her."
    the_person "It's so good... I'm gonna cum... I'm cumming!!!"
    $ the_person.have_orgasm()
    "[the_person.possessive_title!c]'s pussy spasming around you and her cries drive you over the edge. You pull out at the last second."
    $ the_person.cum_on_ass()
    $ ClimaxController.manual_clarity_release(climax_type = "body", person = the_person)
    $ scene_manager.update_actor(the_person, position = "back_peek")
    "Your cum erupts in long ropes, covering her ass and lower back. One particularly intense pulse erupts, going up her back and actually hitting the couch cushion next to her head."
    "She hears it hit the cushion and in her orgasm induced bliss she turns and starts licking your cum off the couch. When she finishes, she sighs."
    the_person "Not a drop goes to waste... that cum belongs to ME!"
    "You slowly get up. [the_person.possessive_title!c] is a sticky mess, and she is loving it. She slowly stands as well, being careful not to get any more on the furniture."
    $ scene_manager.update_actor(the_person, position = "default")
    the_person "[the_person.mc_title]... I don't know why, I just can't stop craving your cum. You'll give me more soon... right?"
    mc.name "Of course, [the_person.title]. I'll always be here for you."
    "[the_person.possessive_title!c]'s body melts into yours as she hears your words."
    $ scene_manager.update_actor(the_person, position = "kissing")
    "You hold her for a while. She starts to giggle."
    the_person "I can feel your cum running down between my cheeks... it's nice."
    $ scene_manager.update_actor(the_person, position = "default")
    mc.name "I need to get going. Take care [the_person.title]."
    $ scene_manager.clear_scene()
    "You say goodbye to [the_person.possessive_title] then leave her apartment. As you walk away, you can't help but smile."
    "Your have turned her into your cumslut."
    python:
        the_person.apply_planned_outfit()
        clear_scene()
    return True

label VT_cum_fetish_gabrielle_intro_label():
    return False

label VT_cum_fetish_stephanie_intro_label():
    return False

label VT_cum_fetish_alex_intro_label():
    return False

label VT_cum_fetish_nora_intro_label():
    return False

label VT_cum_fetish_emily_intro_label():
    return False

label VT_cum_fetish_christina_intro_label():
    return False

label VT_cum_fetish_starbuck_intro_label():
    return False

label VT_cum_fetish_sarah_intro_label():
    $ the_person = sarah
    "You are just finishing up with some work before you get ready for lunch. You hear a friendly voice greet you as you pull your packed lunch from the desk."
    the_person "Hey [the_person.mc_title]! That sure looks good!"
    $ the_person.draw_person()
    "You give her a quick wave as she walks up to you. You assumed she was talking about your lunch, but quickly notice she is looking at your crotch."
    the_person "So, I forgot to pack a lunch today, and I'm pretty hungry, so I was wondering if, you know..."
    "Her hand travels down to your crotch. She begins to stroke you as she continues..."
    the_person "... if maybe while you were eating your lunch, I could bother you for a salty snack."
    $ mc.change_locked_clarity(20)
    "[the_person.possessive_title!c] looks at you with hopeful eyes."
    the_person "I could get down under your desk! If anyone walks by they won't even know!"
    menu:
        "Help yourself":  #This begins the sex scene
            mc.name "I suppose I could help you out with that. Are you sure you don't want to share any of my lunch?"
            the_person "Oh! That's okay, [the_person.mc_title]."
            "[the_person.possessive_title!c] lowers her voice and whispers huskily in your ear."
            the_person "I'm not sure what is going on with me but... lately... I've just been craving your cum so bad..."
            "You aren't surprised, it's been a while since you started giving her the Vitamin D."
            the_person "I feel like I'm going crazy..."
            if the_person.tits_available:
                "You check out [the_person.possessive_title]. Her delicious looking tits are on full display."
            else:
                "You check out [the_person.possessive_title]. You decide it might be easier to get off if you have a little more skin to look at while she sucks you."
                mc.name "Hey, before you get under the desk, why don't you get your tits out? It'd be great to have something to look at..."
                "[the_person.possessive_title!c] smiles wide."
                the_person "Of course! Let me get this off for you..."
                $ the_person.strip_outfit(exclude_lower = True)
            $ mc.change_locked_clarity(50)
            "[the_person.possessive_title!c] gropes her breasts with both hands, looking for your approval."
            mc.name "Mmm, that looks great. I think I'll eat my lunch now..."
            "[the_person.possessive_title!c] giggles."
            the_person "Mmm... me too!"
            "[the_person.possessive_title!c] quickly gets down underneath your desk, before you sit down."
            $ the_person.draw_person(position = "blowjob")
            "She immediately gets to work, pulling your dick out of your pants. You feel her soft, velvet mouth wrapped around you."
            $ the_person.break_taboo("sucking_cock")
            "[the_person.possessive_title!c] begins bobbing her head up and down eagerly, hungry for your delicious cum."
            call get_fucked(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, allow_continue = False) from _call_get_fucked_VT_cum_fetish_sarah_intro_01
            $ VT_add_cum_fetish(the_person)
            "[the_person.possessive_title!c] is moaning ecstatically below your desk."
            if the_person.has_mouth_cum:
                "Glancing down, you see [the_person.possessive_title] running her hands along her face, then down to her chest. She is rubbing your cum into her skin."
                the_person "Mmm... it feels so good! That first splash is always the best..."
            elif the_person.has_face_cum:
                $ play_swallow_sound()
                "Glancing down, you see [the_person.possessive_title] licking her fingers. There isn't a trace of your cum anywhere, she has swallowed every drop."
                the_person "Mmm... that was so... good..."
            "[the_person.possessive_title!c] stands up."
            $ the_person.draw_person()
            the_person "Wow, that was amazing, [the_person.mc_title]. I don't know what has been coming over me lately..."
            "[the_person.possessive_title!c] blushes and pauses..."
            mc.name "Did you get what you were hoping for?"
            "You tease her."
            the_person "Oh, I think I'm good for today... but I'm sure it won't be long until I get hungry again..."
            "She's been under the influence of your cock for a while now. She has definitely developed a cum fetish."
            if the_person.is_bald:
                "[the_person.possessive_title!c] runs her fingers over her lips and smiles at you."
            else:
                "[the_person.possessive_title!c] runs her hand through her [the_person.hair_description]. She licks her lips and smiles at you."
            $ the_person.apply_planned_outfit(show_dress_sequence = True)
            the_person "Thanks again, [the_person.mc_title]. We should do this again... and soon."
            $ the_person.draw_person(position = "walking_away")
            "You wave goodbye to [the_person.possessive_title] and finish eating your lunch."
        "Refuse":
            the_person "I'm sorry to hear that..." #TODO finish this
            $ VT_fetish_timer_reset(the_person, "cum", 2)

    $ the_person.apply_planned_outfit()
    $ mc.location.show_background()
    $ clear_scene()
    return True

label VT_cum_fetish_ophelia_intro_label():
    return False

label VT_cum_fetish_candace_intro_label():
    return False

label VT_cum_fetish_dawn_intro_label():
    return False

label VT_cum_fetish_erica_intro_label(the_person):
    $ the_person = erica
    "It's time to hit the gym. You step into the locker room to get changed into workout clothes."
    "As you are changing, you feel someone tap on your shoulder. You turn around."
    $ the_person.draw_person()
    mc.name "Uhhh... [the_person.title]? Are you supposed to be in the men's locker room?"
    erica "Shhh!"
    "[the_person.possessive_title!c] shushes you, then grabs your hand."
    $ the_person.draw_person(position = "walking_away")
    "She leads you into one of the shower stalls. You close it off behind you."
    $ the_person.draw_person(position = "kissing")
    "[the_person.title] pulls you close then whispers in your ear."
    erica "Hey, I saw you walk in here, and I was just getting ready to work out too..."
    erica "I thought today instead of a protein shake, I could just have some vitamin D."
    $ the_person.draw_person(position = "blowjob")
    "[the_person.title] gets down on her knees. She looks up at you and smiles."
    "It's been a while since you started giving her the Vitamin D."
    "Being a fitness enthusiast, it doesn't surprise you she has linked her urge for your cum with health benefits."
    "You nod, and she immediately gets to work, pulling your dick out of your underwear. You feel her soft, velvet mouth wrapped around you."
    $ the_person.break_taboo("sucking_cock")
    "[the_person.possessive_title!c] begins bobbing her head up and down eagerly, hungry for your delicious cum."
    call get_fucked(the_person, start_position = blowjob, the_goal = "oral creampie", start_object = make_floor(), skip_intro = True, allow_continue = False) from _call_get_fucked_VT_cum_fetish_erica_intro_01
    $ VT_add_cum_fetish(the_person)
    "After you finish, [the_person.possessive_title] continues to lick her fingers, desperate for a little more of your cum."
    if the_person.is_bald:
        "[the_person.possessive_title!c] runs her fingers over her lips and smiles at you."
    else:
        "[the_person.possessive_title!c] runs her hand through her [the_person.hair_description]. She licks her lips and smiles at you."
    the_person "That was great. I think I'm ready to make some serious gains today!"
    mc.name "I'm sure you are..."
    "She's been under the influence of your cock for a while now. She has definitely developed a cum fetish."
    $ the_person.draw_person()
    the_person "Alright... I'm gonna sneak out of here... see you later!"
    $ the_person.apply_planned_outfit()
    $ mc.location.show_background()
    $ clear_scene()
    "You finish changing into your workout gear, then leave the locker room."
    return True

label VT_cum_fetish_ashley_intro_label():
    return False

label VT_cum_fetish_kaya_intro_label():
    return False

label VT_cum_fetish_ellie_intro_label():
    return False

label VT_cum_fetish_camila_intro_label():
    return False

label VT_cum_fetish_sakari_intro_label():
    return False


# label SB_fetish_stephanie_cum_label():
#     $ the_person = stephanie
#     if mc.location == mc.business.r_div: #Already in research
#         "Suddenly, [the_person.possessive_title] looks up from her work and speaks up."
#         the_person "Hey [the_person.mc_title], I need to talk to you about something. Can we go somewhere private?"
#     else:
#         "You get a text message from [the_person.possessive_title]."
#         the_person "Hey [the_person.mc_title], I need to talk to you about something. Can we meet somewhere private?"
#         "You text her back."
#     mc.name "Sure, meet me in my office."
#     $ mc.change_location(ceo_office)
#     $ scene_manager = Scene()
#     $ scene_manager.add_actor(the_person)
#     "[the_person.title] meets you there. You sit down and notice she closes the office door... and then locks it."
#     mc.name "Have a seat. Is there something I can do for you?"
#     "She sits down and immediately starts to talk to you."
#     $ scene_manager.update_actor(the_person, position = "sitting")
#     if the_person.love < 40 and the_person.obedience < 140:
#         the_person "Look... I've been doing this for a while now. I know the real purpose of the serums you have me researching, and the effects they have on people..."
#         the_person "I went along with things for a while because... well I don't know why. I guess I was just really into the science of things."
#         "She shifts uncomfortably in her seat."
#         $ scene_manager.update_actor(the_person, display_transform = character_right_flipped)
#         the_person "Some of the things we've developed here are incredible. They can give people happiness, and expand their skills."
#         the_person "The serums you've been giving out... I thought maybe you were just trying to make all the girls' lives here better."
#         the_person "But... lately, I've found myself slipping further and further into these fantasies. It's making it hard to concentrate on my work!"
#         the_person "I think you and I both know that this is a direct result of one of the serums we've been investigating lately... to give girls specific cravings. Fetishes even!"
#         "She takes a second, she looks like she is on the verge of getting emotional. Then she straightens up and looks you straight in the eye."
#         the_person "For god's sake, last night I had a dream that I was getting gangbanged and twelve guys came on, or in me, at the same time!"
#         the_person "I'm sorry, but I can't do it anymore. You and I both know there isn't any real way to counter these effects. So, if I'm going to be a cum slut... I might as well enjoy it, right?"
#         mc.name "I suppose so."
#         $ scene_manager.update_actor(the_person, position = "stand4")
#         "[the_person.possessive_title!c] pulls a serum out of her pocket."
#         the_person "I don't have an antidote for this. It's the bimbo serum. I mixed it with a couple other things..."
#         "This is some dangerous territory. If you let her go through with this, you are sure her sister will be pissed! Do you try to talk her down? Or let her do it?"
#         menu:
#             "Try to talk her down" if mc.charisma > 6:
#                 mc.name "Stop. You don't have to do that?"
#                 "She looks at the serum in her hand. Then back at you."
#                 the_person "Ummm, I don't know... I'm pretty sure I do."
#                 mc.name "Don't you want to know more... about the long term effects? Of the serums I mean?"
#                 the_person "You hardly need me to test something like that."
#                 mc.name "Who better to do it though? [the_person.title], you've been with me since the beginning. I'll help meet your needs. I know the cravings will be intense, but I promise I'll help!"
#                 "Her resolve is failing. She looks down at the serum again."
#                 mc.name "The science behind these chemicals is incredible. You {i}know{/i} you want to keep studying it together. With me!"
#                 the_person "[the_person.mc_title]... I want to. I really do. But I'm so scared right now."
#                 "You get up and walk around the desk."
#                 mc.name "It's okay. Sometimes science is a risky business. We can do this. Together. Let me have the serum."
#                 "She hesitates another moment. Then hands you the serum."
#                 the_person "Oh god... you better be right about this!"
#                 $ scene_manager.update_actor(the_person, position = "kissing")
#                 "She throws her arms around you, holding you close."
#                 the_person "The serums really are incredible. I do want to study them more. But first... I need your cum so bad! I can't think about anything else right now!"
#                 $ scene_manager.update_actor(the_person, position = "blowjob")
#                 "[the_person.possessive_title!c] gets on her knees and starts to pull down your trousers. It isn't long until she has your dick out and is stroking it eagerly."
#                 the_person "Come on [the_person.mc_title], you know what I need!"
#                 "She enthusiastically opens her mouth and sucks your hard cock into her mouth. She is desperate for your seed!"
#                 $ the_person.break_taboo("sucking_cock")
#                 "You should consider carefully where you cum, it might change where she prefers to take cum from now on."
#                 call fuck_person(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_fuck_person_SBC060
#                 $ VT_add_cum_fetish(the_person)
#                 the_person "Oh god... It's even better than I dreamed about last night."
#                 "[the_person.possessive_title!c] takes a minute to recover before standing up."
#                 $ scene_manager.update_actor(the_person, position = "stand2")
#                 the_person "Okay. We can do this. Together! I hope you realise the serums also greatly increase libido."
#                 mc.name "Don't worry."
#                 the_person "Well, I'll get back to work for now then. But I might swing by your office again later... you know... if I get hungry!"
#                 $ scene_manager.update_actor(the_person, position = "walking_away")
#                 "You say goodbye, and [the_person.possessive_title] turns and walks out of your office."
#                 "Looks like [the_person.title] has a cum fetish now!"
#             "Let her take it":
#                 mc.name "I'm sorry, [the_person.title]. I didn't want it to be this way."
#                 "She looks at you. Her resolve stumbles, but only for a moment."
#                 the_person "Don't worry, I'll be the bimbo cum slut you've always wanted!"
#                 "She brings the serum to her mouth and drinks it down. She closes her eyes as it begins to take effect."
#                 $ permanent_bimbo_on_apply(the_person, add_to_log = True)
#                 "It probably only takes a minute, but it feels like an eternity. Finally she opens her eyes."
#                 "She looks around a bit, seeming a bit confused about where she is."
#                 the_person "That's... we were talking about something... right?"
#                 "She looks at you. Her pupils are dilated and her breathing is calm."
#                 mc.name "We were just about done... with the talking anyway."
#                 the_person "That's right! We were going to do something else after though... right? I remember hoping that."
#                 "She begins to walk around the desk toward you."
#                 mc.name "That's right. You were going to get on your knees. And if everything goes well, I have a present for you."
#                 the_person "Oh! A present! I do love presents! Especially the ones I tend to get when I'm on my knees. I wonder what it could be!"
#                 $ scene_manager.update_actor(the_person, position = "blowjob")
#                 "[the_person.possessive_title!c] gets on her knees and skilfully removes your pants and underwear."
#                 "She gives your hard-on a few eager strokes."
#                 the_person "Mmm [the_person.mc_title]! You look so yummy!"
#                 "She enthusiastically opens her mouth and sucks your hard cock into her mouth. She is desperate for your seed!"
#                 $ the_person.break_taboo("sucking_cock")
#                 "You should consider carefully where you cum, it might change where she prefers to take cum from now on."
#                 call fuck_person(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_fuck_person_SBC061
#                 $ VT_add_cum_fetish(the_person)
#                 the_person "Your cum is amazing!"
#                 $ scene_manager.update_actor(the_person, position = "stand2")
#                 the_person "Mmm, thanks for that mister! I know this is kinda crazy but... I'm totally getting the urge for another load. Is there any more in those lonely looking balls for me?"
#                 mc.name "I'm sorry, but I have to get going."
#                 the_person "Awww! Okay. I hope you're around later though. I have a feeling I'm going to get hungry."
#                 $ scene_manager.update_actor(the_person, position = "stand4")
#                 the_person "I'll just go back to... whatever it was I was doing. What do I do here again?"
#                 mc.name "It doesn't matter, you can take the rest of the day off."
#                 the_person "Oh? Guess I'll just go find someone else to play with for a while. Your loss mister!"
#                 $ scene_manager.update_actor(the_person, position = "walking_away")
#                 "You say goodbye, and [the_person.possessive_title] turns and walks out of your office."
#                 "Looks like [the_person.title] has a cum fetish now! But she is also a bimbo."
#                 "You are guessing she is probably not particularly fit for her job in research. Maybe you can move her somewhere else in the company?"
#
#             "Try to talk her down \n{menu_red}Requires High Charisma{/menu_red} (disabled)" if mc.charisma <= 6:
#                 pass
#
#     elif the_person.love < 70 and not the_person.is_girlfriend:   #She kinda trusts / loves you, but isn't fully committed and needs some convincing.
#         the_person "Look... I've been doing this for a while now. I know the real purpose of the serums you have me researching, and the effects they have on people..."
#         the_person "I went along with things for a while because I trust you. You've always impressed me with the way you do things."
#         "She shifts uncomfortably in her seat."
#         $ scene_manager.update_actor(the_person, display_transform = character_right_flipped)
#         the_person "Some of the things we've developed here are incredible. They can give people happiness, and expand their skills."
#         the_person "The serums you've been giving out... I thought maybe you were just trying to make all the girls' lives here better."
#         the_person "But... lately, I've found myself slipping further and further into these fantasies. It's making it hard to concentrate on my work!"
#         the_person "I think you and I both know that this is a direct result of one of the serums we've been investigating lately... to give girls specific cravings. Fetishes even!"
#         "She takes a second, she looks like she is on the verge of getting emotional. Then she straightens up and looks you straight in the eye."
#         the_person "For god's sake, last night I went to the bar and sucked off three different guys! In one night! That isn't normal!"
#         the_person "I'm going to be honest here. I trust you, I'm sure you are just doing this for research or business purposes. But I'm at a tipping point here. I need you to answer this question honestly."
#         mc.name "Okay, go ahead."
#         the_person "Are you going to... you know... take responsibility for this? The urges are {i}so{/i} intense! You're the only guy here, I need your word that you'll help me take care of these urges!"
#         "From a pocket, she pulls out a serum that it looks like she has concocted."
#         the_person "If you can't, I understand. But I don't think I can take it, knowing the serums gave me these urges... I need something to forget the research, and just move on with my life."
#         the_person "I don't have an antidote for this. It's the bimbo serum. I mixed it with a couple other things... Maybe it's time for me to start a new life. I'm sure you could use me over in marketing or something, right?"
#         "This is some dangerous territory. It sounds like she is looking to you to tell her what to do."
#         "Become a bimbo, for real? Or, if you want her to stay the sexy, intelligent research lead, you'll have to help her with her newfound libido?"
#         "If you have her take the serum, her sister will probably get very upset!"
#         menu:
#             "Help her":
#                 pass
#             "Take the Serum":
#                 mc.name "I'm sorry, [the_person.title]. I didn't want it to be this way. I don't think I have the time to commit to something like that."
#                 $ scene_manager.update_actor(the_person, emotion = "sad")
#                 "She looks at you. You think you see a tear coming down from her eye."
#                 the_person "It's okay. The science is amazing. And I'm sure I'll enjoy life as... a bimbo butt slut."
#                 "She brings the serum to her mouth and drinks it down. She closes her eyes as it begins to take effect."
#                 $ permanent_bimbo_on_apply(the_person, add_to_log = True)
#                 "It probably only takes a minute, but it feels like an eternity. Finally she opens her eyes."
#                 "She looks around a bit, seeming a bit confused about where she is."
#                 the_person "That's... we were talking about something... right?"
#                 "She looks at you. Her pupils are dilated and her breathing is calm."
#                 mc.name "We were just about done... with the talking anyway."
#                 the_person "That's right! We were going to do something else after though... right? I remember hoping that."
#                 $ scene_manager.update_actor(the_person, position = "stand2")
#                 "She begins to walk around the desk toward you."
#                 mc.name "That's right. You were going to get on your knees. And if everything goes well, I have a present for you."
#                 the_person "Oh! A present! I do love presents! Especially the ones I tend to get when I'm on my knees. I wonder what it could be!"
#                 $ scene_manager.update_actor(the_person, position = "blowjob")
#                 "[the_person.possessive_title!c] gets on her knees and skilfully removes your pants and underwear."
#                 "She gives your hard-on a few eager strokes."
#                 the_person "Mmm [the_person.mc_title]! You look so yummy!"
#                 "She enthusiastically opens her mouth and sucks your hard cock into her mouth. She is desperate for your seed!"
#                 $ the_person.break_taboo("sucking_cock")
#                 "You should consider carefully where you cum, it might change where she prefers to take cum from now on."
#                 call fuck_person(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_fuck_person_SBC062
#                 $ VT_add_cum_fetish(the_person)
#                 the_person "Your cum is amazing!"
#                 $ scene_manager.update_actor(the_person, position = "stand2")
#                 the_person "Mmm, thanks for that mister! I know this is kinda crazy but... I'm totally getting the urge for another load. Is there any more in those lonely looking balls for me?"
#                 mc.name "I'm sorry, but I have to get going."
#                 the_person "Awww! Okay. I hope you're around later though. I have a feeling I'm going to get hungry."
#                 $ scene_manager.update_actor(the_person, position = "stand4")
#                 the_person "I'll just go back to... whatever it was I was doing. What do I do here again?"
#                 mc.name "It doesn't matter, you can take the rest of the day off."
#                 the_person "Oh? Guess I'll just go find someone else to play with for a while. Your loss mister!"
#                 $ scene_manager.update_actor(the_person, position = "walking_away")
#                 "You say goodbye, and [the_person.possessive_title] turns and walks out of your office."
#                 "Looks like [the_person.title] has a cum fetish now! But she is also a bimbo."
#                 "You are guessing she is probably not particularly fit for her job in research. Maybe you can move her somewhere else in the company?"
#                 $ the_person.apply_planned_outfit()
#                 $ clear_scene()
#                 return
#         "She gives a deep sigh of relief."
#         the_person "You have NO idea how glad I am to hear that."
#         $ scene_manager.update_actor(the_person, position = "blowjob")
#         "She comes around the desk then gets on her knees next to your chair. She looks up at you expectantly."
#         the_person "Well? Why isn't your cock out? You said you would help!"
#         mc.name "Oh. Right!"
#         "You quickly pull down your zipper. She reaches in your trousers and pulls out your erection."
#         "She enthusiastically opens her mouth and sucks your hard cock into her mouth. She is desperate for your seed!"
#         $ the_person.break_taboo("sucking_cock")
#         "You should consider carefully where you cum, it might change where she prefers to take cum from now on."
#         call fuck_person(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_fuck_person_SBC063
#         $ VT_add_cum_fetish(the_person)
#         the_person "Oh god... Every load just feels so good!"
#         "[the_person.possessive_title!c] takes a minute to recover before standing up."
#         $ scene_manager.update_actor(the_person, position = "stand2")
#         the_person "Okay. We can do this. Together! I hope you realise the serums also greatly increase libido."
#         mc.name "Don't worry. I'm definitely aware."
#         the_person "Well, I'll get back to work for now then. But I might swing by your office again later... you know... if I get hungry!"
#         $ scene_manager.update_actor(the_person, position = "walking_away")
#         "You say goodbye, and [the_person.possessive_title] turns and walks out of your office."
#         "Looks like [the_person.title] has a cum fetish now!"
#     else:
#         the_person "Before I get started, I just want to make sure you understand. I support you completely. I'm not mad or anything, just a little concerned."
#         the_person "I've been doing this for a while now. I know the real purpose of the serums you have me researching, and the effects they have on people..."
#         the_person "I went along with things for a while because I trust you. Maybe even love you. You've always impressed me with the way you do things."
#         the_person "Some of the things we've developed here are incredible. They can give people happiness, and expand their skills."
#         the_person "The serums you've been giving out... I thought maybe you were just trying to make all the girls' lives here better."
#         the_person "But... lately, I've found myself slipping further and further into these fantasies. It's making it hard to concentrate on my work!"
#         the_person "I think you and I both know that this is a direct result of one of the serums we've been investigating lately... to give girls specific cravings. Fetishes even!"
#         "She takes a second, she looks like she is on the verge of getting emotional. Then she straightens up and looks you straight in the eye."
#         the_person "For god's sake, all I can think about is your cock blowing load after load all over me, in me, anywhere you want!"
#         the_person "I trust you. It took me a while to realise what is going on, but I understand it now."
#         the_person "This is the next step in our relationship. The urges are {i}so{/i} intense! You're the only guy here, I need you to help me take care of these urges!"
#         the_person "I'm sure that relying on you for this can only bring us closer together."
#         if the_person.has_significant_other:
#             mc.name "Wait, don't you have a [the_person.so_title]?"
#             the_person "So? He isn't here at work with me all day, is he? He can cum for me when I get home, but I need you to do it while I'm here!"
#         "Sounds like she thinks the whole reason you gave her the serums is because... you want to take things to the next level? For now, it is probably better if you just go along with it."
#         mc.name "You're right. I probably should have been more honest about it, but I thought this would help bring us closer together."
#         "She gives a deep sigh of relief."
#         the_person "You have NO idea how glad I am to hear that."
#         "[the_person.possessive_title!c] walks around your desk then gets on her knees."
#         $ scene_manager.update_actor(the_person, position = "blowjob")
#
#         the_person "Well? Why isn't your cock out? You said you would help!"
#         mc.name "Oh. Right!"
#         "You quickly pull down your zipper. She reaches in your trousers and pulls out your erection."
#         "She enthusiastically opens her mouth and sucks your hard cock into her mouth. She is desperate for your seed!"
#         $ the_person.break_taboo("sucking_cock")
#         "You should consider carefully where you cum, it might change where she prefers to take cum from now on."
#         call fuck_person(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_fuck_person_SBC064
#         $ VT_add_cum_fetish(the_person)
#         the_person "Oh god... I can't get enough of your cock! It tastes so good."
#         "[the_person.possessive_title!c] takes a minute to recover before standing up."
#         $ scene_manager.update_actor(the_person, position = "stand2")
#         the_person "Okay. I can already feel the urge to get another load from you, but I know you are a busy guy."
#         the_person "I'll be back later, okay? I have a feeling I'm going to be hungry for more!"
#         $ scene_manager.update_actor(the_person, position = "walking_away")
#         "You say goodbye, and [the_person.possessive_title] turns and walks out of your office."
#         "Looks like [the_person.title] has a cum fetish now!"
#
#     $ scene_manager.clear_scene()
#     $ the_person.apply_planned_outfit()
#     $ clear_scene()
#     return
