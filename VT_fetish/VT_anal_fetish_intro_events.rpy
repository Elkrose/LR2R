### Function labels

label VT_anal_fetish_employee_intro_label(the_person):
    if the_person.sluttiness < 70:
        $ VT_abort_anal_fetish_intro(the_person)
        return
    "You are just finishing up with business for the day. As you are closing up your workstation, something is bothering you."
    "You couldn't help but notice one of your employees, [the_person.title], has been acting a little bit... different."
    "She seems to be using her ass to try and get attention."
    "Even now, as you walk around the business in your closing rounds, [the_person.possessive_title] bends over her desk when she notices you are nearby."
    $ the_person.draw_person(position = "standing_doggy")
    $ mc.change_locked_clarity(10)
    "She tries to pretend like she doesn't notice you, but you notice subtle shifts in her hips, wiggling a bit as you walk by her."
    "You wonder if [the_person.possessive_title!c] is ready to awaken a new love of anal sex."
#    if the_person in get_anal_fetish_unique_dialogue_list():
#        "Warning, this character is unique, and may have unique fetish dialogue. If you continue, you may miss this dialogue!"
    menu:
        "Attempt to train her anal fetish" if mc.energy > 40:
            pass
        "Too tired" if mc.energy <= 40:
            "You are just too tired to approach her today."
            #$ VT_abort_anal_fetish_intro(the_person)
            $ VT_fetish_timer_reset(the_person, "anal")
            $ clear_scene()
            return
        "Too risky, leave her alone":
            "You decide to leave her alone for now. You might revisit this decision at a later date."
            #$ VT_abort_anal_fetish_intro(the_person)
            $ VT_fetish_timer_reset(the_person, "anal", 2)
            $ clear_scene()
            return
    mc.name "Hello [the_person.title]."
    the_person "Hey [the_person.mc_title]! It's good to see you!"
    $ the_person.draw_person()
    "She quickly stands up and turns to you. You take a deep breath. It's time to take the plunge."
    mc.name "[the_person.title], are busy you tonight? I have something I could use your help with after we close up."
    the_person "Oh! I suppose I could stay for a bit. Let me just finish this up. Want to meet in your office?"
    "It's clear from the tone of her voice she's hoping for some personal attention."
    mc.name "That sounds perfect. See you there."
    $ clear_scene()
    $ mc.change_location(ceo_office)
    "You head to your office and wait a few minutes. Shortly after you hear a knock at the door."
    $ the_person.draw_person()
    mc.name "Come in. Please have a seat."
    $ the_person.draw_person(position = "sitting")
    "As she sits down, she starts to fidget a bit."
    mc.name "First off, I want you to know that you aren't in trouble. That isn't why I asked you here."
    the_person "Okay..."
    mc.name "I've noticed you've been acting a bit different lately whenever I am around. Bending over, wiggling your hips at me."
    the_person "I... sir it's not..."
    if the_person.has_taboo("anal_sex"):
        mc.name "I was wondering if you've ever tried anal before. It's clear that it is something that is on your mind."
    else:
        mc.name "I was wondering if you have some anal cravings. It is clear to me that your ass needs some attention."
    "[the_person.title] laughs a little."
    the_person "Oh! I umm... I suppose I would be up for something like that."
    "You stand up and start to walk around the desk toward [the_person.possessive_title]."
    mc.name "You aren't fooling anyone [the_person.title]. Your body language is practically begging for it."
    mc.name "Now get up and bend over the desk so I can get a good look."
    the_person "Oh my god..."
    $ the_person.draw_person(position = "standing_doggy")
    $ mc.change_locked_clarity(50)
    if the_person.vagina_available:
        $ the_person.slap_ass()
        "You give her ass a smack, admiring the way her cheeks wobble."
    else:
        mc.name "Let's get this out of the way first."
        $ the_person.strip_to_vagina(position = "standing_doggy")
        $ the_person.slap_ass()
        "Once you've got her clothing out of the way, you give her ass a smack, admiring the way her cheeks wobble."
    $ the_person.change_arousal(15)
    the_person "Mmm... like the view?"
    mc.name "I love it."
    $ play_moan_sound()
    "[the_person.title] moans as you firmly knead her ass for a bit."
    $ the_person.change_arousal(15)
    $ mc.change_locked_clarity(30)
    "You slide your fingers down between her cheeks and find her cunt just starting to leak a bit of moisture."
    mc.name "Wow, you really like this kind of attention don't you."
    "[the_person.possessive_title!c] can only moan as you slide two fingers inside her cunt. With your other hand you give her another spank."
    $ the_person.change_arousal(10)
    mc.name "There, that should be good."
    "You remove your fingers briefly, then bring them up slightly. She sighs as you wiggle them around her puckered hole."
    "You push against her. Your fingers easily begin to slip into [the_person.possessive_title]'s back door."
    $ the_person.change_arousal(20)
    $ mc.change_locked_clarity(30)
    the_person "Oh fuck..."
    "[the_person.title]'s knees buckle a bit as you begin to work your fingers in and out of her."
    mc.name "Do you like it?"
    the_person "God yes... keep going!"
    $ the_person.change_arousal(15)
    "[the_person.possessive_title!c]'s breathing is getting erratic as you finger-fuck her asshole for a minute or two."
    the_person "I didn't know... I didn't know it could be this good!"
    $ the_person.change_arousal(15)
    $ mc.change_locked_clarity(30)
    "[the_person.title]'s arousal is beginning to run down the inside of her thighs. She is {i}really{/i} getting off on this!"
    "You double your efforts in an attempt to get her to cum from just your fingers."
    the_person "Oh... OH! Don't stop!"
    $ the_person.change_arousal(20)
    "[the_person.possessive_title!c]'s whole body quivers as she orgasms. You push your fingers as deep as you can get them, feeling her body clench them rhythmically."
    $ the_person.have_orgasm()
    $ mc.change_locked_clarity(50)
    mc.name "Damn, that was hot. I could feel you cumming, gripping my fingers. I can't wait to feel you do that around my cock."
    "You start to pull your cock out. Still recovering, [the_person.title] takes a moment to register your words."
    the_person "Ah... yeah... on your... what?"
    "Once you pull it out, you smack her ass cheeks back and forth with it a couple times."
    the_person "Oh! Yeah but... [the_person.mc_title], it's so big... I'm not sure..."
    mc.name "Shhh. Don't worry, I'll give you some time to adjust before I fuck your backdoor raw."
    "[the_person.title] submissively whimpers, but doesn't protest any further. Instead, she leans forward a little farther, preparing herself to get fucked."
    "When you're ready you push forward. Her back passage slowly accepts your erection, eliciting a satisfied sigh from [the_person.possessive_title]."
    $ the_person.break_taboo("anal_sex")
    ###Anal Scene, standing variant###
    call fuck_person(the_person, start_position = anal_standing, start_object = make_desk(), skip_intro = True, skip_condom = True) from _call_fuck_person_VT_anal_fetish_employee_intro_01
    #$ the_person.SB_fetish = "anal sex"
    $ the_person.max_opinion_score("anal sex")
    $ the_person.max_opinion_score("anal creampies")
    "[the_person.possessive_title!c] takes a few minutes to recover, then turns to you."
    $ the_person.draw_person()
    the_person "Wow, that was amazing, [the_person.mc_title]. I don't know what has been coming over me lately... I just can't stop thinking about you bending me over..."
    "[the_person.possessive_title!c] blushes and pauses..."
    mc.name "... And doing what, [the_person.title]?"
    "You tease her."
    the_person "I can't stop thinking about how full it feels... it feels so right when you push into my ass. It gets me so hot imagining it..."
    $ VT_add_anal_fetish(the_person)
    mc.name "Here, I have something that might help."
    "You reach into your desk. Inside is a pink glass anal plug that you would normally use for discipline. Her eyes light up a bit when she sees it."
    mc.name "Take this. Anytime you start getting the urge and it's distracting you from work, play with it a bit. I'm sure it will help."
    "[the_person.possessive_title!c] takes her butt plug. She slowly pushes it into her ass."
    $ mc.change_locked_clarity(20)
    the_person "Thank you so much [the_person.mc_title]. We should do this again... and soon."
    $ the_person.draw_person(position = "walking_away")
    "You wave goodbye to [the_person.possessive_title] and get ready to head home for the night."
    $ the_person.apply_planned_outfit()
    $ clear_scene()
    return True

label VT_anal_fetish_family_intro_label(the_person):
    if the_person.sluttiness < 70:
        #$ VT_abort_anal_fetish_intro(the_person)
        $ VT_fetish_timer_reset(the_person, "anal")
        return
    $ mc.change_location(the_person.home)
    $ the_person.arousal = 30
    $ the_person.draw_person(position = "standing_doggy")
    "As you walk into the room, you notice [the_person.possessive_title]. She is bent over and appears to be reading something on her phone."
    mc.name "Hey [the_person.title]."
    $ the_person.draw_person(position = "back_peek")
    "She quickly looks back at you."
    the_person "Oh hey, [the_person.mc_title]."
    $ the_person.draw_person(position = "standing_doggy")
    $ mc.change_locked_clarity(20)
    "She turns back to her phone. As you start to walk over to her, you notice she appears to be moving her hips back and forth a bit..."
    mc.name "Looking at something interesting?"
    the_person "You could say that."
    "As you walk closer to her, you begin to hear some of the audio her phone is playing. You hear some moaning and the sounds of skin against skin."
    "When you are right behind her, you can hear enough. She is watching some kind of porn."
    "You put your hands on her hips. With gentle force, you push your hips against hers. She starts to wiggle her ass up against you."
    mc.name "Watching something good I take it. Anything you'd like to try?"
    if the_person.has_taboo("anal_sex"):
        the_person "Actually yeah... something we haven't really tried before."
    else:
        the_person "Ah, well, we've tried it before, but I've been thinking about it a lot lately."
    "You keep rubbing yourself up against her as she watches her video."
    $ play_moan_sound()
    "She moans as your cock gets hard and presses against her."
    $ the_person.change_arousal (10) # 40
    $ mc.change_locked_clarity(30)
    if the_person.has_breeding_fetish: #She likes getting pregnant
        the_person "You know I love it when we fuck and you cum deep inside me... but I was thinking maybe we could have a change of pace."
    elif the_person.has_taboo("condomless_sex") and not the_person.has_taboo("vaginal_sex"): #you'be fucked but not bare
        the_person "You know... what if we had sex... bare... and you could cum inside me. Without having to worry about getting me pregnant!"
        the_person "I know we are related, but I think I know how we could get around that."
    elif the_person.has_taboo("vaginal_sex") and not the_person.has_taboo("anal_sex"): #You've taken her ass before but not her pussy
        the_person "I know we've done it this way before, but I think I've really started to enjoy it this way."
    elif the_person.has_taboo("anal_sex") and the_person.has_taboo("vaginal_sex"): # You haven't fucked at all
        the_person "I umm... I'm not ready to go all the way with you... but I think I have an idea for something that we {i}could{/i} do..."
    else:
        the_person "What can I say, the video reminded me of you a little bit..."
    "She holds her phone up. On the screen is a woman, bent over with her panties pulled down, getting fucked in the ass."
    $ the_person.add_situational_slut("situation",20, "I want to recreate the video!")
    "As you study [the_person.possessive_title!c]'s ass, you ponder if she is ready to awaken a new love of anal sex."
#    if the_person in get_anal_fetish_unique_dialogue_list():
#        "Warning, this character is unique, and may have unique fetish dialogue. If you continue, you may miss this dialogue!"
    menu:
        "Attempt to train her anal fetish" if mc.energy > 40:
            pass
        "Too tired" if mc.energy <= 40:
            #$ VT_abort_anal_fetish_intro(the_person)
            $ VT_fetish_timer_reset(the_person, "anal")
            $ clear_scene()
            return
        "Not right now":
            "You decide to leave her alone for now. You might revisit this decision at a later date."
            #$ VT_abort_anal_fetish_intro(the_person)
            $ VT_fetish_timer_reset(the_person, "anal", 2)
            $ clear_scene()
            return
    mc.name "God you are so naughty. You want me to fuck you in your ass right here, don't you?"
    the_person "Of course not. It doesn't have to be right here."
    mc.name "You'd like that though, wouldn't you? My cute little [the_person.title], getting her ass taken anytime I feel like it. Anytime, anywhere."
    $ the_person.change_arousal(15) #55
    $ mc.change_locked_clarity(30)
    the_person "You make it sound bad..."
    mc.name "It sounds to me like you are being awfully naughty. I think you need a good spanking."
    if the_person.vagina_available:
        $ the_person.slap_ass()
        "You give her ass a smack, admiring the way her cheeks wobble."
    else:
        mc.name "Let's get this out of the way first."
        $ the_person.strip_to_vagina(position = "standing_doggy")
        $ the_person.slap_ass()
        "Once you've got her clothing out of the way, you give her ass a smack, admiring the way her cheeks wobble."
    $ the_person.change_arousal(10) #65
    $ the_person.slap_ass(update_stats = False)
    "You give her another spank. Her cheeks are starting to redden a bit, but it's obvious from her arousal that she loves it."
    if the_person.has_taboo("anal_sex"):
        mc.name "I can't believe you want me to stick it in your ass. You are such a naughty little slut."
        "She stays quiet for now, but her ass wiggles a bit, making an enticing target."
        $ the_person.slap_ass(update_stats = False)
        "You give her another spank."
        the_person "Ah! Oh fuck..."
        $ the_person.change_arousal(5) # 70
    else:
        mc.name "It's clear to me you've got a little bit of an obsession going. Can't get enough dick in your ass, even if it's a family member?"
        "She stays quiet for now, but her ass wiggles a bit, making an enticing target."
        $ the_person.slap_ass(update_stats = False)
        "You give her another spank."
        $ the_person.change_arousal(5) # 70
    $ mc.change_locked_clarity(30)
    mc.name "Fine, it's clear what you really want. Don't worry, I'll give it to you."
    "You pull out your cock. You grab her hand and bring it to your mouth where you spit a big glob of saliva, then make her stroke you a couple times, getting you lubricated."
    $ mc.change_arousal(5)
    "When you're ready, you point it at her puckered hole and begin to push. It takes several seconds, but you feel her sphincter give way and part for you."
    "With sweet, delicious pressure, your erection slowly buries itself in [the_person.possessive_title]'s bowel."
    $ the_person.change_arousal(15) #85
    $ mc.change_locked_clarity(50)
    $ the_person.break_taboo("anal_sex")
    the_person "Oh god... why does it... feel so good!!!"
    "[the_person.possessive_title!c]'s ass feels amazing as you start to fuck it. It's time to show her just how good you can make her feel this way."
    call fuck_person(the_person, start_position = anal_standing, start_object = make_bed(), skip_intro = True, skip_condom = True) from _call_fuck_person_VT_anal_fetish_family_intro_01
    $ the_person.max_opinion_score("anal sex")
    $ the_person.max_opinion_score("anal creampies")
    "[the_person.possessive_title!c] slowly stands up."
    $ the_person.draw_person()
    the_person "That was amazing, [the_person.mc_title]."
    the_person "I... I think I need to get some new toys... something a little more purpose-made for anal use..."
    "You think about it for a minute."
    if starbuck_is_business_partner():
        mc.name "I have a friend who runs a sex shop over at the mall. Head over there sometime and tell her I sent you."
        mc.name "I'll text her to let her know you are coming. She can set you up with some special toys."
    else:
        mc.name "Hey, maybe you should go to the mall. I heard they have a sex shop there."
        mc.name "Maybe they have something there that would be good for you if I'm not around to fuck that ass."
    the_person "You know, I think I'll do that. Thank you [the_person.mc_title]. My ass is yours if you want to do this again sometime..."
    mc.name "A tempting offer to be sure."
    "You part ways with [the_person.title], confident that her newfound anal fetish will bring you a lot of pleasure in the future."
    $ VT_add_anal_fetish(the_person)
    $ the_person.clear_situational_slut("situation")
    $ clear_scene() #TODO does this leave you talking to the girl? If so figure out how to part ways cleanly here.
    return True

label VT_anal_fetish_generic_intro_label(the_person):
    # Concept, spank her while fingering her ass so she can discover her new submissive, anal loving side.
    if the_person.sluttiness < 70:
        #$ VT_abort_anal_fetish_intro(the_person)
        $ VT_fetish_timer_reset(the_person, "anal")
        return
    $ the_person.arousal = 40
    $ the_person.draw_person()
    "You walk up to [the_person.title] to say hello. However, something about her demeanour seems a little off."
    mc.name "Hello [the_person.title]. How are you doing today?"
    the_person "Hello [the_person.mc_title]! It's good to see you..."
    if the_person.tits_visible:
        "You take a moment to look at her. Her cheeks are flushed, and her exposed nipples look hard as diamonds. She is definitely aroused."
    else:
        "You take a moment to look at her. Her cheeks seem flushed... Her nipples are poking against the fabric of her outfit. Is she... Aroused?"
    the_person "... Actually... I do have something you could help me with."
    "She leans forward and talks quietly in your ear."
    the_person "I woke up super horny this morning, but none of my usual masturbation techniques seemed to work... Can you help me out?"
    $ mc.change_locked_clarity(20)
    "Hmm, very interesting, maybe that's why she's having trouble getting off?"
    "Helping her might develop her anal interest into a fetish!"
#    if the_person in get_anal_fetish_unique_dialogue_list():
#        "Warning, this character is unique, and may have unique fetish dialogue. If you continue, you may miss it!"
    menu:
        "Help her":
            mc.name "Let's find somewhere private first."
        "Too busy":
            mc.name "I'm sorry [the_person.title], but I just wanted to talk about something."
            $ the_person.change_stats(happiness = -5, love = -2)
            the_person "Ah, okay. I see."
            #$ VT_abort_anal_fetish_intro(the_person)
            $ VT_fetish_timer_reset(the_person, "anal", 2)
            return False
    "[the_person.title] takes your hand. You take a few minutes to find somewhere private where you won't be interrupted."
    $ the_person.draw_person(position = "kissing")
    "She throws her arms around you and you start to make out. Your hands drop to her ass and you start to grope her aggressively."
    the_person "Mmm... that feels nice..."
    $ play_spank_sound()
    "You give her ass a rough spank."
    $ the_person.change_arousal(5) #45
    $ mc.change_locked_clarity(20)
    $ play_moan_sound()
    the_person "Oh! Mmm~ I've been bad, haven't I..."
    $ play_spank_sound()
    "You give her a couple more spanks. She moans appreciatively."
    $ the_person.change_arousal(5) # 50
    mc.name "You really have been bad. Turn around, I need to punish you more appropriately."
    "[the_person.possessive_title!c] doesn't say a word, but submissively turns around and bends over for you."
    $ the_person.draw_person(position = "standing_doggy")
    $ mc.change_locked_clarity(50)
    if the_person.vagina_available:
        $ the_person.slap_ass()
        "You give her ass a smack, admiring the way her cheeks wobble."
    else:
        mc.name "Let's get this out of the way first."
        $ the_person.strip_to_vagina(position = "standing_doggy")
        $ the_person.slap_ass()
        "Once you've got her clothing out of the way, you give her ass a smack, admiring the way her cheeks wobble."
    $ the_person.change_arousal (15) # 65
    mc.name "You've got an amazing ass [the_person.title]..."
    $ the_person.slap_ass(update_stats = False)
    "You give her another spank. Her cheeks are starting to redden a bit, but it's obvious from her arousal that she loves it."
    if the_person.has_taboo("anal_sex"):
        mc.name "Have you ever tried taking it in your ass? I think it's clear that your ass needs some attention."
        the_person "Oh? I umm... not exactly... I'm not that kind of girl..."
        $ the_person.slap_ass(update_stats = False)
        "You give her another spank."
        the_person "Ah! Oh fuck..."
        $ the_person.change_arousal(5) # 70
    else:
        mc.name "It is clear to me that your ass needs some attention. I'm going to spank you until it's red and then fuck it."
        the_person "I... I'm not like... usually that kind of girl..."
        $ the_person.slap_ass(update_stats = False)
        "You give her another spank."
        $ the_person.change_arousal(5) # 70
    $ mc.change_locked_clarity(30)
    mc.name "Are you sure? You certainly seem to be enjoying this so far."
    "Another spank. You notice goosebumps growing all down her body."
    $ the_person.change_arousal(10) # 80
    the_person "I... I can't believe I'm saying this but... my body is telling me to!"
    mc.name "I'm sorry, what exactly is your body telling you?"
    $ the_person.slap_ass(update_stats = False)
    the_person "Ah! It's telling me it wants you to fuck my ass! Push it in and fuck me raw! Oh god, it sounds so good!"
    $ the_person.slap_ass(update_stats = False)
    $ the_person.slap_ass(update_stats = False)
    "You give her ass two more final spanks."
    $ the_person.change_arousal(10) # 90
    $ mc.change_locked_clarity(50)
    mc.name "Alright. First, get on your knees. I want my cock nice and lubed up so it goes in easy."
    $ the_person.draw_person(position = "blowjob")
    "[the_person.possessive_title!c] immediately drops to her knees without a word. You quickly pull your cock out."
    "She wastes no time and begins slobbering all over your erection. Her tongue runs up and down your full length, multiple times."
    $ mc.change_arousal(10)
    mc.name "Good girl. Now get ready for me, I'm going to fuck your ass, just the way you want it."
    the_person "Oh god..."
    $ the_person.draw_person(position = "standing_doggy")
    "[the_person.possessive_title!c] turns and points her ass at you, bending over. You grab her hip in one hand and your cock in the other."
    "You run the tip of your saliva soaked meat all around her puckered hole, then start to push. She mewls as you start to push it in."
    "Slow and steady, you push yourself in until you are completely bottomed out in her bottom."
    $ the_person.change_arousal (15) #105
    the_person "Oh my god... it's so big! Oh [the_person.mc_title], it's so good!"
    $ the_person.have_orgasm()
    "[the_person.possessive_title!c]'s ass is twitching wildly all around you as she orgasms. You hold her hips tight and in place with both hands as her body quivers."
    "It feels amazing to have her body gripping you as she cums."
    $ mc.change_locked_clarity(50)
    mc.name "See? You just needed something in your ass so you could cum."
    the_person "I... I think you might be right... I..."
    $ the_person.break_taboo("anal_sex")
    "She stops mid-sentence as you give her a quick thrust."
    mc.name "It's okay to admit you are a buttslut. Now, let's just make sure your needs are sated before we part ways."
    "[the_person.possessive_title!c] is unable to reply as you begin to fuck her ass. It's time to show her just how good you can make her feel that way."
    call fuck_person(the_person, start_position = anal_standing, start_object = make_wall(), skip_intro = True, skip_condom = True) from _call_fuck_person_VT_anal_fetish_generic_intro_01
    #$ the_person.SB_fetish = "anal sex"
    $ the_person.max_opinion_score("anal sex")
    $ the_person.max_opinion_score("anal creampies")
    $ the_person.draw_person(position = "doggy")
    "After you finish with her, [the_person.possessive_title] drops to her knees as she tries to recover."
    $ the_person.draw_person()
    the_person "That was amazing, [the_person.mc_title]."
    the_person "I can't stop thinking about how full it felt, when your cock pushed into my ass..."
    if starbuck_is_business_partner():
        mc.name "Hey, I have a friend who runs a sex shop over at the mall. Head over there sometime and tell her I sent you."
        mc.name "I'll text her to let her know you are coming. She can set you up with some masturbation toys that can help you if you find yourself in this position again."
    else:
        mc.name "Hey, maybe you should go to the mall. I heard they have a sex shop there."
        mc.name "Maybe they have something that would help you out, with masturbating, if you find yourself in this position again."
    the_person "You know, I think I'll do that. Thank you [the_person.mc_title]. My ass is yours if you want to do this again sometime..."
    mc.name "A tempting offer to be sure."
    "You part ways with [the_person.title], confident that her newfound anal fetish will bring you a lot of pleasure in the future."
    $ VT_add_anal_fetish(the_person)
    $ clear_scene() #TODO does this leave you talking to the girl? If so figure out how to part ways cleanly here.
    return True

label VT_anal_fetish_mom_intro_label():
    $ mc.change_location(bedroom)
    $ the_person = mom
    "Playing around on your phone for a bit before bed, you hear a knock on your door."
    mc.name "It's open."
    $ the_person.draw_person()
    "[the_person.possessive_title!c] opens the door."
    the_person "Hey... I'm watching a movie tonight, would you join me?"
    "You consider her offer. You are pretty tired, but movie night with [the_person.title] could definitely be fun. Recently they've been getting very interesting."
    the_person "I umm... really want you to. I have something special in mind..."
    $ mc.change_locked_clarity(10)
    "You raise an eyebrow. You've been pushing your limits with [the_person.title] lately, this could be interesting indeed."
    menu:
        "Watch a Movie":
            pass
        "Too Tired":
            mc.name "Sorry [the_person.title], I really need some sleep tonight."
            the_person "That's okay dear. Maybe another night."
            #$ VT_abort_anal_fetish_intro(the_person)
            $ VT_fetish_timer_reset(the_person, "anal")
            return
    mc.name "A movie would be fun. I'll be right out."
    the_person "Great! I've got one picked out on Netflix. Make yourself comfortable on the couch, I'm just going to change into something more comfortable!"
    mc.name "Sure thing [the_person.title]."
    $ clear_scene()
    $ mc.change_location(hall)
    "You grab a soda from the kitchen then head to the living room and sit down on the couch. You take a look at the movie that [the_person.possessive_title] has picked out."
    "Murmur of the Heart? Hmm, sounds like a lame chick flick... you back out for a second to read the description. Hmm..."
    "... an open–minded teenage boy finds himself torn between a rebellious urge to discover love, and the ever-present, almost dominating affection of his beloved mother..."
    "Oh geez. She is definitely planning an interesting night! You quickly click back into the movie and pause it when you hear her bedroom door open."
    "You try to act nonchalant as you hear [the_person.title] walk into the living room. You purposefully avoid looking at her until you hear her clear her throat."
    the_person "Ah, want to get a little more comfortable with me tonight?"
    $ set_special_fetish_outfit(the_person, opinion_color = the_person.favourite_colour)
    $ the_person.draw_person()
    $ mc.change_locked_clarity(50)
    "When you look up, you are stunned at the outfit that [the_person.possessive_title] is wearing."
    mc.name "[the_person.title]... wow! But... but what about..."
    the_person "[lily.fname] is out for the night, spending it at a friend's house. We have the house to ourselves for the night..."
    "[the_person.title] slowly walks over to you. Her hips and body are mesmerizing."
    the_person "Here... let me help..."
    $ the_person.draw_person (position = "kneeling1")
    "[the_person.possessive_title!c] gets down on her knees in front of you. She undoes your pants, grasps the waistband and begins to pull them off you. You arch your back a bit to make it easier."
    "Having stripped you from the waist down, [the_person.title] looks up at you."
    the_person "Can you get your shirt?"
    mc.name "Ahhh... Oh! Right..."
    $ the_person.draw_person(position = "blowjob")
    "You start to lift your shirt over your head. As you do, you feel [the_person.possessive_title] lean forward and run her tongue up and down your cock."
    $ the_person.draw_person(position = "blowjob", special_modifier = "blowjob")
    "Her mouth opens and her soft lips slowly descend onto your erection as you finish pulling your shirt off. When you look, she has her eyes closed, just enjoying servicing her son's erection."
    $ mc.change_locked_clarity(50)
    if the_person.is_bald:
        "You run your hands over her bald head. She doesn't stroke you at all, but you feel her tongue roaming all over the tip. It feels great. Eventually she pulls off."
    else:
        "You run your hands through her [the_person.hair_description]. She doesn't stroke you at all, but you feel her tongue roaming all over the tip. It feels great. Eventually she pulls off."
    $ the_person.draw_person(position = "kneeling1")
    the_person "Mmm, sorry, I needed a taste. Ready to start the movie?"
    mc.name "Ugghhh, yeah..."
    $ the_person.draw_person("standing_doggy")
    "[the_person.possessive_title!c] stands up, turns and bends over, grabbing the remote off the ottoman."
    "She takes her time pointing the remote at the TV and hitting play. Her hips appear to be swaying when the movie intro screen starts."
    the_person "I ummm, heard good things about this movie. If it's too boring though, we can always turn it off."
    $ the_person.draw_person(position = "sitting")
    "Instead of sitting next to you, [the_person.title] sits on your lap. Your cock nestles nicely between her ass cheeks as she leans back against you."
    "As the movie begins, you simply enjoy the heat and softness of her skin against yours."
    "You can't really even see the movie, but to be honest, you don't care. Soon though, the constant pressure of her ass against your groin has you aching for more."
    "You put your hands on [the_person.possessive_title]'s hips. She sighs as you start moving her hips up and down against you."
    "[the_person.title] starts moving her hips now on her own, your cock still hot dogging between her cheeks. You reach down and start to slide your fingers along her slit."
    the_person "Oooohhhh, [the_person.mc_title], my beautiful son..."
    $ the_person.change_arousal(15) #15
    $ mc.change_locked_clarity(50)
    "She turns her head to you and comes in for a kiss. Your lips meet, followed by tongues, as she begins to hungrily explore your mouth."
    "[the_person.title] gasps when you slip two fingers inside her, moving slow and exploring every inch of her cunt."
    $ the_person.change_arousal(15) #30
    $ mc.change_arousal(10) #40
    "You make out for a while with [the_person.possessive_title], the heat and passion between the two of you growing constantly. Finally, she breaks the kiss."
    the_person "Oh [the_person.mc_title]... let your mother take care of you tonight, okay?"
    mc.name "Okay [the_person.title]."
    if the_person.has_breeding_fetish: #She likes getting pregnant
        the_person "I know we normally do this more traditionally... but tonight I want to do things a little bit differently."
    elif the_person.has_taboo("condomless_sex") and not the_person.has_taboo("vaginal_sex"): #you'be fucked but not bare
        the_person "You know... what if we had sex... bare... and you could cum inside me. Without having to worry about getting me pregnant!"
        the_person "I know I'm your mother, but I think I know how we could get around that."
    elif the_person.has_taboo("vaginal_sex") and not the_person.has_taboo("anal_sex"): #You've taken her ass before but not her pussy
        the_person "I know we've done it this way before, but I think I've really started to enjoy it this way."
    elif the_person.has_taboo("anal_sex") and the_person.has_taboo("vaginal_sex"): # You haven't fucked at all
        the_person "I umm... I'm not ready to go all the way with you... but I think I have an idea for something that we {i}could{/i} do..."
    else:
        the_person "You know I would do anything for you, but tonight I was thinking we could do things a little different."
    $ the_person.draw_person(position = "standing_doggy")
    $ mc.change_locked_clarity(50)
    "[the_person.possessive_title!c] stands up for a second, leans forward and pulls the lid off the ottoman. She pulls out a bottle of lubricant and hands it to you."
    the_person "Would you do the honours, dear? I need my ass to be good and ready for you..."
    "As you study [the_person.possessive_title!c]'s ass, you ponder if she is ready to awaken the love for anal sex."
    mc.name "Of course [the_person.title]."
    "You quickly squirt some lubricant onto your fingers and begin rubbing them around [the_person.title]'s backdoor."
    the_person "Mmmm, a little more, and make sure you get some inside too..."
    "You follow her instructions, squirting some directly on her ass, then using a finger to try and push some inside her. Her sphincter yields easily and she gasps at the penetration."
    $ the_person.change_arousal(15) #45
    "After spending some time getting her good and ready, you set the lubricant to the side. [the_person.possessive_title!c] slowly starts to sit down on your lap again."
    the_person "God you have such a monster. I can't wait to feel it..."
    $ the_person.draw_person(position = "sitting")
    "She takes your cock in hand, points it at her puckered hole, then slowly backs up onto it. It takes several seconds, but eventually her ass rests on your lap, fully impaled on your shaft."
    $ the_person.break_taboo("anal_sex")
    "It takes her a few moments, but eventually she starts to move her hips."
    the_person "Okay... don't hold back! Mommy wants your cum baby!"
    call get_fucked(the_person, the_goal = "anal creampie", start_position = anal_on_lap, start_object = make_couch(), skip_intro = True, allow_continue = False) from _call_get_fucked_VT_anal_fetish_mom_intro_01
    $ the_person.draw_person(position = "sitting")
    $ VT_add_anal_fetish(the_person)
    the_person "Oh my god... [the_person.mc_title] that was so good."
    $ the_person.draw_person()
    "[the_person.possessive_title!c] slowly stands up. She turns the TV off and turns to you."
    the_person "Can... can we move to your bedroom? That was so good, I need to feel that again!"
    mc.name "Sure. Tell you what, you go clean up a bit, I'll make some coffee."
    the_person "Okay... take a five minute break!"
    $ clear_scene()
    $ mc.change_location(kitchen)
    "You head to the kitchen and start a pot of coffee while [the_person.possessive_title] goes to the restroom. It takes a few minutes, but soon it's done."
    $ the_person.apply_outfit(Outfit("Nude"))
    $ the_person.draw_person()
    $ mc.change_locked_clarity(30)
    "Soon, she appears in the kitchen, completely nude. She makes herself a cup of coffee and you just chat for a little bit while you drink."
    $ the_person.change_energy(50)
    $ mc.change_energy(50)
    "After coffee you feel reinvigorated. It's time for round two!"
    mc.name "Ready for round two?"
    the_person "I am... lead the way!"
    $ mc.change_location(bedroom)
    "[the_person.possessive_title!c] follows you to your room."
    the_person "Oh god, I need this so bad honey. You just lay back and let momma take care of you now."
    mc.name "But you already did earlier?"
    the_person "I know, but that's how I want things to go tonight, okay? Just let mommy show you how much she loves you."
    "[the_person.possessive_title!c] reaches into your nightstand and grabs some lotion. She hands it to you."
    the_person "Here! Get me ready again."
    $ the_person.draw_person(position = "back_peek")
    $ mc.change_locked_clarity(50)
    "[the_person.possessive_title!c] turns away from you. You squirt a liberal amount of lotion onto your hand and then reach up between her supple ass cheeks and spread it around her tight asshole."
    "You start to work one finger into her."
    $ play_moan_sound()
    "She moans and starts to push back against you. When you push a second finger into her she gasps."
    $ the_person.change_arousal(15)
    the_person "Oh [the_person.mc_title]... I can't believe how good it feels this way now... I don't know what has been coming over me!"
    $ the_person.draw_person(position = "cowgirl")
    the_person "Now, just let [the_person.title] take care of you. I'm gonna stick it into my most intimate hole now..."
    "[the_person.possessive_title!c] goes slow, but steadily slides down, impaling her sphincter on your throbbing erection."
    $ play_moan_sound()
    "She bottoms out and moans loudly."
    # call fuck_person(the_person, start_position = anal_cowgirl, start_object = make_bed(), skip_intro = True, girl_in_charge = True, position_locked = True) from _call_sex_description_SBA41
    call get_fucked(the_person, the_goal = "anal creampie", private= True, start_position = anal_cowgirl, start_object = make_bed(), skip_intro = True, allow_continue = False) from _call_get_fucked_VT_anal_fetish_mom_intro_02
    $ the_report = _return
    if the_report.get("girl orgasms", 0) > 0:
        the_person "Oh god, I came so hard..."
        $ the_person.draw_person(position = "missionary")
        "[the_person.possessive_title!c] collapses onto the bed next to you, exhausted from her anal cowgirl ride."
    else:
        the_person "Mmm, that was so good, thank you [the_person.mc_title]..."
        $ the_person.draw_person(position = "missionary")
        "[the_person.possessive_title!c] rolls off you and lays down on the bed next to you."
    the_person "Can I just sleep in here tonight [the_person.mc_title]? It feels so good to be next to you."
    mc.name "Of course [the_person.title]. You can sleep in here anytime."
    "You get comfortable. Soon [the_person.possessive_title] has fallen fast asleep. You can hear her murmuring in her dreams about taking stuff in her ass."
    "You cuddle up behind her and enjoy the heat of her soft flesh as you slowly drift off to sleep."
    $ mc.change_locked_clarity(30)
    $ clear_scene()
    call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_VT_anal_fetish_mom_intro
    $ the_person.apply_outfit(Outfit("Nude"))
    "The next morning, you slowly wake up. The bed next to you is cold. You look around and see [the_person.possessive_title] getting ready for the day in the bathroom."
    $ mc.change_location(home_shower)
    $ the_person.draw_person(position = "walking_away")
    "You walk up behind [the_person.possessive_title] and wrap your arms around her. She arches her back against you as your hands roam across her chest."
    $ mc.change_locked_clarity(30)
    the_person "Good morning sleepy head..."
    "[the_person.possessive_title!c] starts to tremble at your touch."
    the_person "Last night was amazing. I just want you to know that, anytime you want it, you can take mommy's ass! I'll keep it ready for you!"
    "[the_person.title] begins to grind her hips up against you, nestling your now quickly hardening dick between her ass cheeks."
    "You grab her hips and start to grind against her. Her breathing starts to get a bit heavier."
    the_person "[the_person.mc_title], last night [the_person.title] took care of you. Do you think this morning, you could take care of me?"
    "You smile to yourself."
    mc.name "Are you asking me to fuck you in your ass?"
    the_person "Yes... Please! Please [the_person.mc_title]!"
    $ mc.change_location(bedroom)
    $ the_person.draw_person(position = "doggy")
    "You pick her up from behind and take her back to the bed. You throw her on the bed. She quickly gets on her hands and knees and starts wiggling her ass at you."
    $ mc.change_locked_clarity(50)
    "You grab the lotion leftover from the night before. You quickly apply another glob to [the_person.title]'s back side. You apply some more to your cock until it is good and slick."
    "You get yourself lined up with your mom's back passage. You slowly begin your anal penetration."
    the_person "That's it [the_person.mc_title]! Fuck me good!"
    call fuck_person(the_person, start_position = doggy_anal, start_object = make_bed(), skip_intro = True, skip_condom = True) from _VT_anal_fetish_mom_intro_03
    $ the_report = _return
    $ the_person.draw_person(position = "missionary")
    if the_report.get("girl orgasms", 0) > 0:
        "[the_person.possessive_title!c] lies there on the bed, speechless from your anal plundering."
    else:
        "[the_person.possessive_title!c] lies there on the bed."
    mc.name "So... anytime I want? I'll remember that."
    "You can see [the_person.possessive_title]'s body quiver slightly at your words. She meekly responds."
    the_person "Yes [the_person.mc_title]. It's all yours. Take my ass whenever you want. I'll be ready!"
    return

label VT_anal_fetish_lily_intro_label():
    $ the_person = lily # make sure we use lily for the event
    if the_person.sluttiness < 70:
        #$ VT_abort_anal_fetish_intro(the_person)
        $ VT_fetish_timer_reset(the_person, "anal")
        return
    $ mc.start_text_convo(the_person)
    the_person "Hey [the_person.mc_title]! Can you do me a favour? Meet me at the mall when you get off work. I need your help with something..."
    mc.name "Okay, I'll be there."
    $ mc.end_text_convo()
    "You quickly finish up with your work and head over to the mall."

    $ mc.change_location(mall)
    $ scene_manager = Scene()
    "When you get to the mall, you look around for a minute, then spot [the_person.title]. She waves to you then comes running over to you, giving you a big hug."
    $ scene_manager.add_actor(the_person, position = "stand4")
    the_person "Hey! Thanks for coming with me! I need your help with something!"
    "You are a little hesitant. She wants you to go shopping with her?"
    mc.name "Are you sure you need me for this?"
    "She gives you a mischievous smile."
    the_person "Definitely! Don't worry, you'll be glad you came when you see where we are going."
    the_person "I have had some special requests on my InstaPic channel. I need you because I don't want to go by myself and get creeped on!"
    "[the_person.title] grabs you by the hand and leads you into the mall. It seems any inhibition she might have previously had being seen with her [the_person.mc_title] has vanished after being corrupted by you."
    "You are almost surprised when she leads you into the sex shop."
    $ mc.change_location(sex_store)
    "The owner greets you as you walk in."
    $ scene_manager.add_actor(starbuck, emotion = "happy")
    if starbuck.sluttiness > 50 or starbuck.love > 30 or starbuck_is_business_partner():
        starbuck "Hello! Welcome to... Oh hey, [starbuck.mc_title]! Good to see you! Oh and you brought a partner! Hi, I'm [starbuck.title]!"
    else:
        starbuck "Hello! Welcome to Starbuck's Sex Shop! It's so great to see a couple come in."
    starbuck "Is there anything I can help you find?"
    "[the_person.possessive_title!c] takes the lead."
    the_person "Yeah so, I was wondering, do you sell a special type of strap-on that can be used to... umm... strap on to a guy so he can fuck your pussy and ass at the same time?"
    "You can barely believe your ears. You knew that the you have been corrupting your [the_person.title], but you had no idea she was ready for something like this."
    "And for her InstaPic channel? It's almost too good to be true."
    $ mc.change_locked_clarity(30)
    starbuck "Oh! I've got just the thing! Follow me!"
    $ scene_manager.update_actor(starbuck, position = "walking_away")
    $ scene_manager.update_actor(the_person, position = "walking_away")
    if perk_system.has_item_perk("Male Strapon"):
        "As you are following, remembering you already have something similar, you show [the_person.title] what you have in your backpack."
        mc.name "Hey... I already kinda have something like that..."
        $ scene_manager.update_actor(the_person, position = "back_peek")
        "She looks at what you've got and her eyes get bright."
        the_person "Ah! Bro! Why didn't you tell me you had one of these?"
        $ scene_manager.update_actor(starbuck, position = "default")
        "[starbuck.possessive_title!c] turns to you as you reach a selection of dildos."
        $ scene_manager.update_actor(the_person, position = "default")
        the_person "Just pretend like we are looking then, that will totally work!"
    else:
        $ scene_manager.update_actor(starbuck, position = "default")
        $ scene_manager.update_actor(the_person, position = "default")
        "[starbuck.possessive_title!c] leads you over to a selection of dildos. They have special straps that go around the man so that they are secured, just below the penis, and can be used for double penetration."
    the_person "Hmm... I don't know, what do you think about this one?"
    "[the_person.title] picks up one. It has an extra little vibrating unit."
    mc.name "That looks pretty good, actually."
    "[the_person.title] takes it up to the counter."
    $ scene_manager.update_actor(starbuck, position = "stand2")
    starbuck "Great! This one is actually on sale, but I hadn't gotten around to marking it yet. It's only $200!"
    "You decide to offer to pay for it."
    mc.name "Here, let me just put this on the company card..."
    $ mc.business.change_funds(-200, stat = "Shopping")
    if perk_system.has_item_perk("Male Strapon"):
        "Well, now you have an extra, in case anything ever happens to your other one..."
    starbuck "Okay! You're all set! Do you two want to try it out? I have a special room in the back, sometimes people just can't WAIT to get home before trying out a purchase!"
    $ mc.change_locked_clarity(30)
    "[the_person.title] hesitates and looks at you."
    mc.name "I think that would be a good idea, don't you [the_person.title]?"
    the_person "Oh yeah, of course!"
    $ scene_manager.update_actor(the_person, position = "walking_away")
    $ scene_manager.hide_actor(starbuck)
    "[the_person.possessive_title!c] grabs your hand and you follow her to the backroom. It has a familiar smell of body fluids and sweat."
    $ scene_manager.update_actor(the_person, position = "stand4")
    $ the_person.add_situational_slut("situation",20, "I want to try this thing out!")
    the_person "Come on [the_person.mc_title], I can't wait to feel you fuck me with this thing on..."
    "[the_person.possessive_title!c] quickly strips, eager to get started."
    $ scene_manager.strip_full_outfit(the_person)
    "You get yourself naked as well. On a nearby shelf you spot a bulk size bottle of intimate lube."
    "[the_person.possessive_title!c] gets down on her knees and starts to secure the toy to your cock."
    $ mc.change_locked_clarity(50)
    $ scene_manager.update_actor(the_person, position = "blowjob")
    mc.name "Mmm, you look amazing on your knees [the_person.title]."
    "[the_person.possessive_title!c] looks up at you."
    the_person "Yeah, you like it anytime I'm near your dick. Trust me, I'd love to blow you, but I've got something else in mind..."
    $ scene_manager.update_actor(the_person, position = "doggy")
    "[the_person.possessive_title!c] turns over and gets on her hands and knees in front of you on the floor. She lifts her hips and starts waving her ass in the air."
    "You grab a few squirts of the lube and get your cock and the dildo all lubed up. You grab another squirt and start working it in her rear entry."
    the_person "Mmm... that is so good... I don't know why, lately I just haven't been able to stop thinking about your cock fucking me back there..."
    "It sounds like she might be developing an anal fetish!"
    "You push two fingers into her tight rump. It grips and squeezes at your fingers."
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(50)
    the_person "Oh! That feels good... but I'm ready for you. Let me have it [the_person.mc_title]!"
    "You use your hand to line your cock up with her puckered hole. She reaches down and grabs the dildo and lines it up with her pussy."
    "With one slow, smooth motion, you push your cock past her well lubed sphincter. It goes in with a small pop, and then you continue with a slow thrust until your cock is buried in her ass."
    $ the_person.break_taboo("anal_sex")
    the_person "Fuck! Holy hell... [the_person.mc_title] that is intense! I've never felt... I'm so full!!!"
    "Going tantalizingly slow, you pull yourself mostly out, then back into her buttery smooth back door."
    the_person "Okay... Go slow... but I'm ready!"
    call fuck_person(the_person, start_position = doggy_anal_dildo_dp, start_object = make_floor(), skip_intro = True, skip_condom = True) from _VT_anal_fetish_lily_intro_01
    $ the_report = _return
    $ the_person.clear_situational_slut("situation")
    $ scene_manager.update_actor(the_person, position = "doggy")
    if the_report.get("girl orgasms", 0) > 1:
        "[the_person.possessive_title!c] is a sweaty, heaving mess. You know she had multiple orgasms from the intense sensations of the double penetration."
        "She looks back at you in awe."
    elif the_report.get("girl orgasms", 0) > 0:
        "[the_person.possessive_title!c] is laying on the floor, exhausted from the intensity of the double penetration."
        "She looks back at you and smiles."
    $ scene_manager.update_actor(the_person, position = "default")
    if had_family_threesome():
        the_person "[the_person.mc_title]... That felt amazing. What do you think... should we try this with mom too? I think she would also enjoy being fucked in both holes like that..."
        "You give her a knowing smile."
        mc.name "Don't worry [the_person.title], I think she'll love it."
    else:
        the_person "[the_person.mc_title]... That felt amazing. I'm not sure though... are we going to be able to keep this from mom? I don't think I can stay quiet enough when I'm getting fucked in both holes like that..."
        "You give her a reassuring smile."
        mc.name "Don't worry [the_person.title], we'll be careful."
    the_person "Good... because lately I've just been craving you so bad. We don't have to always use the strap-on. But just thinking about you fucking my ass makes me so horny."
    $ VT_add_anal_fetish(the_person)
    "It is pretty clear from the way she got off while you were fucking her and the way she was talking afterwards, you're convinced [the_person.possessive_title] has developed an anal fetish!"
    $ scene_manager.apply_outfits()
    $ mc.change_location(sex_store)
    "After you both clean up, you leave the back room of the sex shop."
    $ scene_manager.show_actor(starbuck)
    starbuck "Have a good day! Thank you for shopping at Starbuck's sex shop!"
    if starbuck.sluttiness > 50:
        "You wave goodbye to [starbuck.possessive_title]. You note some telltale signs of arousal, flushed cheeks, and you can see her nipples are erect."
        "Was she watching you somehow? Oh well, you decide to head out."
    else:
        "You wave goodbye to [starbuck.possessive_title] and head out."
    $ scene_manager.clear_scene()
    $ male_strapon_unlock()
    $ mc.change_location(mall)
    return

label VT_anal_fetish_rebecca_intro_label():
    "Rebecca's anal fetish scene has not yet been written."
    return False

label VT_anal_fetish_gabrielle_intro_label():
    "Gabrielle's anal fetish scene has not yet been written."
    return False

label VT_anal_fetish_stephanie_intro_label():
    $ the_person = stephanie
    if stephanie.fetish_count == 0:
        call fetish_stephanie_first_fetish_label(the_person) from _VT_anal_fetish_stephanie_intro_bimbo_choice_01
        if the_person.personality == bimbo_personality:
            call VT_anal_fetish_stephanie_bimbo_label(the_person) from _VT_anal_fetish_stephanie_intro_steph_bimbo_01
        else:
            call VT_anal_fetish_stephanie_normal_label(the_person) from _VT_anal_fetish_stephanie_intro_steph_normal_01
    else:
        if the_person.personality == bimbo_personality:
            $ mc.start_text_convo(the_person)
            the_person "Heyyyyyyy [the_person.mc_title]! I need your cock! Meet in your office?"
            mc.name "Sure, I'll see you there."
            $ mc.change_locked_clarity(20)
            $ mc.end_text_convo()
            $ mc.change_location(ceo_office)
            $ scene_manager = Scene()
            $ scene_manager.add_actor(the_person)
            the_person "Oh hey! You're here!"
            mc.name "Of course. Can you lock the door?"
            the_person "Oh! Right right right..."
            "[the_person.possessive_title!c] turns and locks your office door."
            the_person "So... I saw this crazy video last night, and I thought maybe we could re-create it!"
            mc.name "Oh yeah? What was it about?"
            the_person "Basically, this guy with a monster cock bent his secretary over his desk and fucked her in the ass!"
            the_person "I was dreaming about it all night. Can we do it please please please pleeeeeaaaassseee???"
            "Sounds like [the_person.title] has started to develop an anal fetish from the all the researching into anal serums. You suppose you should indulge her curiousity with this as well."
            mc.name "Sounds good. Get over here."
            the_person "Oh! Yes sir. What are you going to do to me?"
            call VT_anal_fetish_stephanie_bimbo_label(the_person) from _VT_anal_fetish_stephanie_intro_steph_bimbo_02
        else:
            if mc.location == mc.business.r_div: #Already in research
                "Suddenly, [the_person.possessive_title] looks up from her work and speaks up."
                the_person "Hey [the_person.mc_title], I need to talk to you about something. Can we go somewhere private?"
                mc.name "Sure, follow me to my office."
            else:
                $ mc.start_text_convo(the_person)
                the_person "Hey [the_person.mc_title], I need to talk to you about something. Can we meet somewhere private?"
                mc.name "Sure, meet me in my office."
                $ mc.end_text_convo()
            $ mc.change_location(ceo_office)
            $ scene_manager = Scene()
            $ scene_manager.add_actor(the_person)
            "You walk with [the_person.possessive_title]. When you get there, she locks the door. You sit down at your desk."
            mc.name "What can I do for you [the_person.title]."
            the_person "Well, recently I've started having a new set of... well... anal fantasies. All the research into anal related serums has my curiousity peaked!"
            the_person "I just wanted to make sure that we still have an understanding, right?"
            mc.name "Certainly. I'll always be here to help you with your needs."
            call VT_anal_fetish_stephanie_normal_label(the_person) from _VT_anal_fetish_stephanie_intro_steph_normal_02

    $ the_person.apply_planned_outfit()
    $ clear_scene()
    return True

label VT_anal_fetish_stephanie_bimbo_label(the_person):
    "She begins to walk around the desk toward you."
    mc.name "That's right. You were going to bend over my desk for a minute. And if everything goes well, I have a present for you."
    the_person "Oh! A present! I do love presents! Especially the ones I tend to get when I'm bent over. I wonder what it could be!"
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person, position = "standing_doggy")
    $ mc.change_locked_clarity(50)
    "[the_person.possessive_title!c] turns around and bends over. Your hands immediately get to work."
    $ scene_manager.strip_to_vagina(person = the_person)
    "She wiggles her ass back and forth in front of you as you pull your dick out."
    the_person "Stick it in [the_person.mc_title]! I want to earn my special present!"
    "Without any hesitation you slide your cock into her tight hole."
    $ the_person.break_taboo("anal_sex")
    call fuck_person(the_person, start_position = anal_standing, start_object = make_desk(), skip_intro = True, skip_condom = True, position_locked = True) from _call_VT_anal_fetish_stephanie_bimbo_01
    $ VT_add_anal_fetish(the_person)
    the_person "That's it! That's just what I was hoping for."
    $ scene_manager.update_actor(the_person, position = "stand2")
    the_person "Mmm, thanks for that mister! I know this is kinda crazy but... I'm totally getting the urge for another round. Normally one time is enough but..."
    mc.name "Don't worry. I have something that can help with that."
    "You reach inside the bottom drawer of your desk. You pull out a pink glass anal plug and hand it to her. Her eyes are transfixed on the plug."
    mc.name "This is your present. If you can't find a nice dick to fuck your asshole and you are getting too horny, play with this for a while."
    the_person "Oh! I thought the present was... but this looks great! Would you do the honours, mister?"
    $ scene_manager.update_actor(the_person, position = "standing_doggy")
    "She bends over and presents her recently used ass to you. You have no problem pushing it in, with her ass being lubed up from your prior fucking."
    the_person "Ahh! That's the spot! Could you umm... you know... move it in and out a few times? Make sure it's reeeaaaallllyyyyy in there good."
    "You grab the base and pull it out. You can feel her clenching it as you try to pull on it. When you get it out a few {height_system}, you let it go. Her ass clenches and pulls it back in until it's deep again."
    $ mc.change_locked_clarity(20)
    the_person "Mmmm... that's it. Keep going!"
    mc.name "I'm sorry, but I have to go."
    the_person "Nnnnoooooo."
    $ scene_manager.update_actor(the_person, position = "stand4")
    "She stands up and turns to you."
    the_person "Fine! I'll just go back to... whatever it was I was doing. What do I do here again?"
    mc.name "It doesn't matter, you can take the rest of the day off."
    the_person "Oh? That eager to get rid of me? Guess I'll just go find someone else to play with for a while. Your loss mister!"
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "You say goodbye, and [the_person.possessive_title] turns and walks out of your office, her plug just peeking out between her rosy ass cheeks."
    "Looks like [the_person.title] has an anal fetish now! But she is also a bimbo."
    if the_person == mc.business.head_researcher:
        "You are guessing she is probably not particularly fit for her job in research. Maybe you can move her somewhere else in the company?"
    $ scene_manager.clear_scene()
    return

label VT_anal_fetish_stephanie_normal_label(the_person):
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person, position = "stand4")
    if not the_person.vagina_visible:
        "She starts to strip down."
        $ scene_manager.strip_to_vagina(person = the_person)
    "She looks at you expectantly."
    the_person "Well? Why are you still wearing clothes? You said you would help!"
    # call fuck_person(the_person, start_position = anal_cowgirl, start_object = make_desk(), girl_in_charge = True, position_locked = True) from _call_sex_description_SBA093
    call get_fucked(the_person, the_goal = "anal creampie", start_position = anal_cowgirl, start_object = make_desk(), allow_continue = False) from _call_get_fucked_VT_anal_fetish_stephanie_normal_01
    $ VT_add_anal_fetish(the_person)
    the_person "Oh god... It's even better than I dreamed about last night."
    "[the_person.possessive_title!c] takes a minute to recover before standing up."
    $ scene_manager.update_actor(the_person, position = "stand2")
    the_person "Okay. I hope you realise the serums also greatly increase libido."
    mc.name "Don't worry. I have something that can help with that."
    "You reach inside the bottom drawer of your desk. You pull out a pink glass anal plug and hand it to her. Her eyes are transfixed on the plug."
    mc.name "If the urges get crazy strong, and I'm not available to satisfy you, use this."
    the_person "Oh! Okay! I think I'll try it out now..."
    "You see her reach behind herself and easily slide it in, her body still lubed up from your prior fucking."
    $ mc.change_locked_clarity(20)
    the_person "Ah! Mmm, I feel full. That's really nice. Not as good as you, but I guess in a pinch I could use it as a substitute."
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "You say goodbye, and [the_person.possessive_title] turns and walks out of your office, her plug just peeking out between her rosy ass cheeks."
    "Looks like [the_person.title] has an anal fetish now!"
    $ scene_manager.clear_scene()
    return

label VT_anal_fetish_alex_intro_label():
    "Alexia's anal fetish scene has not yet been written."
    return False

label VT_anal_fetish_nora_intro_label():
    "Nora's anal fetish scene has not yet been written."
    return False

label VT_anal_fetish_emily_intro_label():
    "Emily's anal fetish scene has not yet been written."
    return False

label VT_anal_fetish_christina_intro_label():
    "Christina's anal fetish scene has not yet been written."
    return False

label VT_anal_fetish_starbuck_intro_label():
    $ the_person = starbuck
    if the_person.sluttiness < 70:
        #$ VT_abort_anal_fetish_intro(the_person)
        $ VT_fetish_timer_reset(the_person, "anal")
        return
    $ mc.start_text_convo(the_person)
    the_person "Hey partner! I was just closing up the shop, butt craving something a little more real than this... want to swing by?"
    $ the_person.apply_outfit(Outfit("Nude"))
    $ the_person.draw_person(position = get_random_ass_position())
    $ mc.change_locked_clarity(30)
    "She attached a picture. It looks like she is bending over her counter. Between her ass cheeks you spy a good-sized glass butt plug!"
    "You decide this is too good of an opportunity to pass up. You head over to the sex shop."
    mc.name "Sure, I'll be there in 10 minutes."
    $ mc.end_text_convo()
    $ mc.change_location(sex_store)
    "The door is locked so you give it a knock. [the_person.possessive_title!c] appears in the glass and quickly opens it for you."
    the_person "[the_person.mc_title]! You came!"
    "She gives you a quick wink."
    the_person "Hopefully that's not the last time I say that tonight..."
    "You share a quick laugh."
    the_person "So... I take it you got my picture? We just got that plug in stock. As soon as I saw it I knew I had to try it."
    mc.name "Yeah... still got it in?"
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title!c] turns and begins to slowly walk away from you."
    the_person "Maybe..."
    "She slowly bends over the counter. The dark glass butt plug appears as her cheeks spread."
    $ the_person.draw_person(position = "standing_doggy")
    $ mc.change_locked_clarity(50)
    the_person "I've had it in all day... but all I've been able to think about is your amazing cock, ramming up inside me, filling me up!"
    "You walk up behind her and begin to run your hands along her delicious hips. You can see goosebumps break out along her skin."
    mc.name "Thinking of getting fucked in the ass? My my, [the_person.title], you seem to have quite the affinity for anal these days."
    "[the_person.title] looks back at you."
    the_person "It's true... I don't understand why, but lately I just find myself constantly daydreaming about taking it in the ass. I can't even masturbate anymore without some kind of plug back there!"
    "Sounds like [the_person.title] has developed an anal fetish!"
    "You reach down and start to slowly play with her plug. Her body stiffens as she feels it begin to slowly work in and out of her. She lets out a long, low moan."
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(30)
    the_person "Oh thank god... Oh [the_person.mc_title]."
    mc.name "Don't worry, [the_person.title]. I'm just the man to help you with all these urges you've been dealing with."
    "You slowly pull the plug out and take a look. She's already got a lot of lube worked in and around her asshole."
    "You push the plug back up against [the_person.possessive_title]'s pucker. It gives way easily and slides right in."
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(30)
    the_person "Mmm, that feels good [the_person.mc_title], but you don't have to tease me!"
    "You decide to oblige her. You leave the plug in as you quickly undress yourself. Your cock aches in anticipation, ready for another plunge into [the_person.possessive_title]'s backdoor."
    "With her plug still in, you slide your cock up and down a few times between her cheeks. She pushes herself back against you, grinding her hips against yours."
    "Her soft, pliant cheeks feel great pushed up against your hips. You reach down and slowly pull out her plug and set it on the counter."
    "With her hip in one hand and your dick in the other, you line yourself up and slowly push into [the_person.possessive_title]'s tender behind."
    $ mc.change_locked_clarity(50)
    $ the_person.break_taboo("anal_sex")
    "You lean forward and whisper into her ear."
    mc.name "Hey [the_person.title]. I'm about to fuck your ass now, just the way you like."
    "Her body shudders from your dirty talk. She wiggles her ass back up against you."
    the_person "It's about fucking time! Give it to me good, [the_person.mc_title], you know I can take it!"
    call fuck_person(the_person, start_position = doggy_anal, start_object = make_bed(), skip_intro = True, skip_condom = True) from _call_sex_VT_anal_fetish_starbuck_intro_01
    $ VT_add_anal_fetish(the_person)
    "It's pretty clear, from her sexual performance and the way she talks to you, that [the_person.title] has developed an anal fetish."
    "[the_person.title] takes a few minutes to recover. She eventually stands up and turns to you."
    $ the_person.draw_person(position = "stand4")
    the_person "Hey so, what you said earlier about, you know, being the man to help me with all these urges I've been dealing with lately... were you being serious?"
    mc.name "Of course. We've already been through so much together, you know I'd be glad to help you out!"
    "She thinks for a moment."
    the_person "Ok, stay right here! I'm going to go get something..."
    $ the_person.draw_person(position = "walking_away")
    "You watch [the_person.possessive_title]'s shapely bottom as she walks away."
    "You are definitely looking forward to fucking that ass as much as possible."
    "She is gone for several minutes, but [the_person.title] soon comes back."
    $ the_person.draw_person(position = "stand2")
    "She hands you a small card that has a username and password on it, and a logo for some company at the top that advertises being the best in teledildonics."
    mc.name "Thanks? I'm not sure what this is..."
    the_person "Well, that would be the sign in info for you to control, remotely from your phone, the vibrating plug I have in my ass right now..."
    $ mc.change_locked_clarity(20)
    "Wow! This should be interesting!"
    "[the_person.title] helps you download the app and sign in. When you finish signing in you can see all kinds of information about the plug."
    "Apparently it has some kind of heat sensor, so it can tell whether it is inserted or not and how long it's been in."
    "There's an icon for making the plug vibrate, and it can even tell when it is moving in and out rapidly so you can see when she is masturbating with it!"
    "You tap the little vibrate icon. [the_person.title] jumps."
    the_person "Mmm! That felt good! I guess we got it working!"
    $ the_person.change_arousal(7)
    "This should allow for some... unique experiences!"
    the_person "Well, I'd better get home. Feel free to uh, check in on me whenever you want [the_person.mc_title]!"
    "You say goodbye and head out so she can finish locking up the sex shop."
    $ the_person.apply_planned_outfit()
    $ clear_scene()
    return True

label VT_anal_fetish_sarah_intro_label():
    "Sarah's anal fetish scene has not yet been written."
    return False

label VT_anal_fetish_ophelia_intro_label():
    "Ophelia's anal fetish scene has not yet been written."
    return False

label VT_anal_fetish_candace_intro_label():
    "Candace's anal fetish scene has not yet been written."
    return False

label VT_anal_fetish_dawn_intro_label():
    "Dawn's anal fetish scene has not yet been written."
    return False

label VT_anal_fetish_erica_intro_label():
    $ the_person = erica
    $ mc.location.turn_lights_off()
    "You hear the door to your room slowly open, waking you up."
    $ the_person.draw_person()
    "A figure appears in your door. It's [the_person.possessive_title] again. She tip-toes over to your bed."
    $ the_person.strip_outfit(position = "stand4")
    "Did she just get naked? You decide to feign being asleep while you wait and see what she does."
    $ the_person.draw_person(position = "sitting")
    "You feel a weight on the side of your bed as she sits down. Slowly you feel the blankets being pulled down off of you."
    the_person "Oh god... I've been dreaming about this all night..."
    "You feel your shorts getting slowly pulled down now. Your morning wood springs free."
    the_person "Holy... what a monster... god help me fit this..."
    $ the_person.draw_person(position = "cowgirl")
    "[the_person.title]'s weight settles on your mid-section. You feel a hand grasp your cock and guide it as she starts to sit on it."
    "However, when you feel contact with her skin, there is an unexpected resistance. You hear her sigh."
    the_person "Okay... here we go..."
    "A tight, smooth sensation begins to envelop the end of your dick. You realise [the_person.possessive_title] is sliding you into her ass."
    mc.name "Oooohhhh..."
    "You can't help but moan at the sensation, making it obvious you are awake."
    the_person "Ahh, good morning [the_person.mc_title]."
    $ the_person.change_arousal(30)
    $ mc.change_locked_clarity(50)
    "[the_person.title] finishes sliding herself down, your morning wood now plunged completely into her well lubed backside."
    "She must have walked in the room completely ready for this."
    the_person "Oh my god... I swear I was thinking about this all night long."
    the_person "[lily.fname] and I, we had these outfits that really accentuated the ass, and all I could think about was wishing you would just rip them off and violate me!"
    "Staring at [the_person.possessive_title!c] ass, you ponder if she is ready to awaken a new love of anal sex."
    mc.name "And now, you got it. Is it as good as you hoped? Filling your slutty ass with my cock?"
    $ the_person.change_arousal(10)
    the_person "Oh god yes... It's even better, somehow!"
    "[the_person.title] begins to rock her hips forward and backward a bit, adjusting herself to your girth."
    $ the_person.change_arousal(15)
    $ mc.change_locked_clarity(50)
    "You put your hands on her hips and start to guide her movements. She moans in pleasure."
    $ play_moan_sound()
    the_person "Ohhhhhh! Fuck you feel so hot..."
    "[the_person.possessive_title!c] leans forward and whispers in your ear."
    the_person "I want you to cum in my ass... okay?"
    mc.name "Mmm, okay, let's see what you can do."
    call get_fucked(the_person, the_goal = "anal creampie", start_position = anal_cowgirl, start_object = make_bed(), skip_intro = True, allow_continue = False) from _call_get_fucked_VT_anal_fetish_erica_intro_01
    $ VT_add_anal_fetish(the_person)
    $ the_person.arousal = 60
    "When you finish, you quickly get up."
    mc.name "Bend over, show me your ass."
    the_person "Oh god... okay..."
    $ the_person.draw_person(position = "standing_doggy")
    "[the_person.possessive_title!c] leans over your bed, presenting her ass to you. A little bit of your cum has dribbled down between her legs, but most of it is still buried in her bowel."
    mc.name "Hmm, a little bit came out. Here, let's fix that..."
    "You wipe up some of your cum with your finger, then push it into her ass."
    $ the_person.change_arousal(10)
    $ play_moan_sound()
    the_person "Ah! Oh yes..."
    "You push your finger in and out of her ass a couple times. When you do, more of your cum starts to leak out."
    mc.name "Hey, you're supposed to hold it in."
    "With your other hand, you give her ass a hard spank."
    $ the_person.slap_ass(update_stats = False)
    $ the_person.change_arousal(10)
    the_person "AH! Yes sir!"
    "You feel her sphincter clench around your finger. The small dribble of cum stops."
    mc.name "There we go, now let me fix that real quick."
    "You pull out your finger. Now you take two fingers and scoop up the cum that has escaped, and push it back into her butt."
    $ the_person.change_arousal(10)
    the_person "Ah! Oh fuck yes..."
    "[the_person.possessive_title!c] practically growls. Her hips are pushing back against your fingers and it seems like she is going to cum again."
    "You start to fuck her slutty backdoor with your two fingers as she moans."
    $ the_person.change_arousal(20)
    the_person "Fuck! Oh fuck my poor little hole... OH!"
    "You can feel her back door clench around your fingers as she cums. She is cumming hard, purely from anal penetration."
    $ the_person.have_orgasm(half_arousal = False)
    "Large amounts of cum start to leak from her hole as she orgasms. You decide to let her clean it up herself this time."
    "When she finishes, [the_person.title] just leans forward on your bed, your fingers still lodged inside her."
    the_person "[the_person.mc_title], I'm sorry, I never thought of myself as an anal person, but holy fuck, we have to do this again soon..."
    if the_person.has_breeding_fetish and the_person.has_cum_fetish:
        the_person "I guess I should have known by now that you have the right to claim every hole of mine, but it took me until now to really learn it."
    elif the_person.has_breeding_fetish:
        the_person "Just make sure you keep fucking me in my other hole too... I need your cum in both!"
    else:
        the_person "I almost think I like it better than regular sex... crazy huh?"
    "After taking a minute to recover, [the_person.title] stands up."
    $ the_person.draw_person()
    the_person "Ha, I was going to go for a run this morning, but I'm not sure I can now. You left me pretty sore, but in a good way."
    "[the_person.possessive_title!c] slowly starts to get ready, putting her outfit on."
    $ the_person.apply_planned_outfit(show_dress_sequence = True)
    $ the_person.draw_person(position = "kissing")
    "Before she leaves, she gives you a hug. One hand trails down your body and gives your dick a couple strokes."
    the_person "Take care [the_person.mc_title]."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.title] quietly leaves your room."
    $ clear_scene()
    "From her actions this morning, it is clear that [the_person.possessive_title] has developed an anal fetish."
    $ mc.location.turn_lights_on()
    $ add_erica_wakeup_option("anal cowgirl")
    return True

label VT_anal_fetish_ashley_intro_label():
    "Ashley's anal fetish scene has not yet been written."
    return False

label VT_anal_fetish_kaya_intro_label():
    return False

label VT_anal_fetish_ellie_intro_label():
    return False

label VT_anal_fetish_camila_intro_label():
    return False

label VT_anal_fetish_sakari_intro_label():
    return False

