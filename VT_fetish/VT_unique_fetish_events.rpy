# Use this file to store actions, crisis, and role related items that are going to be character specific or unique. May require single fetish or multiple
# Events in this file would be better added to specific roles

init -1 python:
    def VT_fetish_lily_stream_in_room_requirement(person):
        if person.fetish_count == 0:
            return False
        if mc.location != lily_bedroom:
            return "Must be in [lily.fname]'s bedroom"
        if lily_bedroom.person_count > 1:
            return "Must be alone with [lily.fname]"
        if mc.energy < 40:
            return "You are too tired."
        return True

label VT_fetish_stephanie_first_fetish_label(the_person):
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
    "[the_person.title] meets you there. You sit down and notice she closes the office door... and then locks it."
    mc.name "Have a seat. Is there something I can do for you?"
    "She sits down and immediately starts to talk to you."
    $ scene_manager.update_actor(the_person, position = "sitting")
    if the_person.love < 40 and the_person.obedience < 140:
        the_person "Look... I've been doing this for a while now. I know the real purpose of the serums you have me researching, and the effects they have on people..."
        the_person "I went along with things for a while because... well I don't know why. I guess I was just really into the science of things."
        "She shifts uncomfortably in her seat."
        $ scene_manager.update_actor(the_person, display_transform = character_right)
        the_person "Some of the things we've developed here are incredible. They can give people happiness, and expand their skills."
        the_person "The serums you've been giving out... I thought maybe you were just trying to make all the girls' lives here better."
        the_person "But... lately, I've found myself slipping further and further into these fantasies. It's making it hard to concentrate on my work!"
        the_person "I think you and I both know that this is a direct result of one of the serums we've been investigating lately... to give girls specific cravings. Fetishes even!"
        "She takes a second, she looks like she is on the verge of getting emotional. Then she straightens up and looks you straight in the eye."
        the_person "For god's sake, the thoughts I have! They aren't normal!!!"
        the_person "I'm sorry, but I can't do it anymore. You and I both know there isn't any real way to counter these effects. So, if I'm going to be a freak... I might as well enjoy it, right?"
        mc.name "I suppose so."
        $ scene_manager.update_actor(the_person, position = "stand4")
        "[the_person.possessive_title!c] pulls a serum out of her pocket."
        the_person "I don't have an antidote for this. It's the bimbo serum. I mixed it with a couple other things... might as well enjoy my new life as a freak, right?"
        "This is some dangerous territory. If you let her go through with this, you are sure her sister will be pissed! Do you try to talk her down? Or let her do it?"
        menu:
            "Try to talk her down" if mc.charisma >= 6:
                mc.name "Stop. You don't have to do that?"
                "She looks at the serum in her hand. Then back at you."
                the_person "Ummm, I don't know... I'm pretty sure I do."
                mc.name "Don't you want to know more... about the long term effects? Of the serums I mean?"
                the_person "You hardly need me to test something like that."
                mc.name "Who better to do it though? [the_person.title], you've been with me since the beginning. I'll help meet your needs. I know the cravings will be intense, but I promise I'll help!"
                "Her resolve is failing. She looks down at the serum again."
                mc.name "The science behind these chemicals is incredible. You {i}know{/i} you want to keep studying it together. With me!"
                the_person "[the_person.mc_title]... I want to. I really do. But I'm so scared right now."
                "You get up and walk around the desk."
                mc.name "It's okay. Sometimes science is a risky business. We can do this. Together. Let me have the serum."
                "She hesitates another moment. Then hands you the serum."
                the_person "Oh god... you better be right about this!"
                $ scene_manager.update_actor(the_person, position = "kissing")
                "She throws her arms around you, holding you close."
                the_person "The serums really are incredible. I do want to study them more. But first... I need to fuck! I can't think about anything else right now!"
                return True

            "Let her take it":
                mc.name "I'm sorry, [the_person.title]. I didn't want it to be this way."
                "She looks at you. Her resolve stumbles, but only for a moment."
                the_person "Don't worry, I'll be a REAL ideal employee for you soon."
                "She brings the serum to her mouth and drinks it down. She closes her eyes as it begins to take effect."
                $ permanent_bimbo_on_apply(the_person, None, add_to_log = True)    # TODO: check if second parameter can be NONE
                "It probably only takes a minute, but it feels like an eternity. Finally she opens her eyes."
                "She looks around a bit, seeming a bit confused about where she is."
                the_person "That's... we were talking about something... right?"
                "She looks at you. Her pupils are dilated and her breathing is calm."
                mc.name "We were just about done... with the talking anyway."
                the_person "That's right! We were going to do something else after though... right? I remember hoping that."
                return False

            "Try to talk her down\n{menu_red}Requires High Charisma{/menu_red} (disabled)" if mc.charisma<= 6:
                pass

    elif the_person.love < 70 and not the_person.is_girlfriend:   #She kinda trusts / loves you, but isn't fully committed and needs some convincing.
        the_person "Look... I've been doing this for a while now. I know the real purpose of the serums you have me researching, and the effects they have on people..."
        the_person "I went along with things for a while because I trust you. You've always impressed me with the way you do things."
        "She shifts uncomfortably in her seat."
        $ scene_manager.update_actor(the_person, display_transform = character_right)
        the_person "Some of the things we've developed here are incredible. They can give people happiness, and expand their skills."
        the_person "The serums you've been giving out... I thought maybe you were just trying to make all the girls' lives here better."
        the_person "But... lately, I've found myself slipping further and further into these fantasies. It's making it hard to concentrate on my work!"
        the_person "I think you and I both know that this is a direct result of one of those nanobots we've been investigating lately... to give girls specific cravings. Fetishes even!"
        "She takes a second, she looks like she is on the verge of getting emotional. Then she straightens up and looks you straight in the eye."
        the_person "For god's sake, the thoughts I have! They aren't natural!"
        the_person "I'm going to be honest here. I trust you, I'm sure you are just doing this for research or business purposes. But I'm at a tipping point here. I need you to answer this question honestly."
        mc.name "Okay, go ahead."
        the_person "Are you going to... you know... take responsibility for this? The urges are {i}so{/i} intense! You're the only guy here, I need your word that you'll help me take care of these urges!"
        "From a pocket, she pulls out a serum that it looks like she has concocted."
        the_person "If you can't, I guess I understand. But I don't think I can take it, knowing the serums gave me these urges... I need something to forget, and just move on with my life."
        the_person "I don't have an antidote for this. It's the bimbo serum. I mixed it with a couple other things... Maybe it's time for me to start a new life. I'm sure you could use me over in marketing or something, right?"
        "This is some dangerous territory. It sounds like she is looking to you to tell her what to do."
        "Become a bimbo, for real? Or, if you want her to stay the sexy, intelligent research lead, you'll have to help her with her newfound libido?"
        "If you have her take the serum, her sister will probably get very upset!"
        menu:
            "Help her":
                pass
            "Take the Serum":
                mc.name "I'm sorry, [the_person.title]. I didn't want it to be this way. I don't think I have the time to commit to something like that."
                $ scene_manager.update_actor(the_person, emotion = "sad")
                "She looks at you. You think you see a tear coming down from her eye."
                the_person "It's okay. The science is amazing. And I'm sure I'll enjoy life as... a bimbo slut."
                "She brings the serum to her mouth and drinks it down. She closes her eyes as it begins to take effect."
                $ permanent_bimbo_on_apply(the_person, None, add_to_log = True)        # TODO: check if second parameter can be NONE
                "It probably only takes a minute, but it feels like an eternity. Finally she opens her eyes."
                "She looks around a bit, seeming a bit confused about where she is."
                the_person "That's... we were talking about something... right?"
                "She looks at you. Her pupils are dilated and her breathing is calm."
                mc.name "We were just about done... with the talking anyway."
                the_person "That's right! We were going to do something else after though... right? I remember hoping that."
                return False

        "She gives a deep sigh of relief."
        the_person "You have no {i}idea{/i} how glad I am to hear that."
        "[the_person.possessive_title!c] stands up."
        the_person "I need to fuck... like now!"
        return

    else:
        the_person "Before I get started, I just want to make sure you understand. I support you completely. I'm not mad or anything, just a little concerned."
        the_person "I've been doing this for a while now. I know the real purpose of the serums you have me researching, and the effects they have on people..."
        the_person "I went along with things for a while because I trust you. Maybe even love you. You've always impressed me with the way you do things."
        the_person "Some of the things we've developed here are incredible. They can give people happiness, and expand their skills."
        the_person "The serums you've been giving out... I thought maybe you were just trying to make all the girls' lives here better."
        the_person "But... lately, I've found myself slipping further and further into these fantasies. It's making it hard to concentrate on my work!"
        the_person "I think you and I both know that this is a direct result of one of the nanobots we've been investigating lately... to give girls specific cravings. Fetishes even!"
        "She takes a second, she looks like she is on the verge of getting emotional. Then she straightens up and looks you straight in the eye."
        the_person "For god's sake, the thoughts I'm having even now... This isn't normal!"
        the_person "I trust you. It took me a while to realise what is going on, but I understand it now."
        the_person "This is the next step in our relationship. The urges are {i}so{/i} intense! You're the only guy here, I need you to help me take care of these urges!"
        the_person "I'm sure that relying on you for this can only bring us closer together."
        if the_person.has_significant_other:
            mc.name "Wait, don't you have a [the_person.so_title]?"
            the_person "So? He isn't here at work with me all day, is he? He can fuck me when I get home, but I need you to do it while I'm here!"
        "Sounds like she thinks the whole reason you gave her the serums is because... you want to take things to the next level? For now, it is probably better if you just go along with it."
        mc.name "You're right. I probably should have been more honest about it, but I thought this would help bring us closer together."
        "She gives a deep sigh of relief."
        the_person "You have no {i}idea{/i} how glad I am to hear that."
        "[the_person.possessive_title!c] stands up."
        $ scene_manager.update_actor(the_person, position = "stand4")
        the_person "Let's fuck! I need to do it right now!"
        return True

    return


label VT_fetish_mom_kitchen_label(the_person):
    $ the_person = mom

    mc.name "Hey [the_person.title], dinner sure smells good. Just keep working on it, don't mind me!"
    "[the_person.possessive_title!c] hesitates for a second, clearly realising you are up to something."
    "You pretend to look in the fridge for something as [the_person.possessive_title] resumes dinner preparations. She bends over the counter and starts to chop up some vegetables."
    $ the_person.draw_person(position = "standing_doggy")
    if the_person.vagina_available:
        "You steal a few glances over at [the_person.possessive_title]'s exposed ass. It looks soft and supple, and shakes a bit as she prepares dinner."
    else:
        "You steal a glance over at [the_person.possessive_title]'s ass as she is bent over. It looks great in her [the_person.outfit.get_lower_top_layer.display_name]."
    "Getting a naughty idea, you quietly move behind [the_person.possessive_title]."
    menu:
        "Fuck her ass" if the_person.has_anal_fetish:
            "You reach down and grope her ass aggressively."
            the_person "Hey! What are you doing? Stop that!"
            "You continue groping her. You give her ass a solid swat."
            $ the_person.slap_ass(update_stats = False)
            mc.name "Stop? But doesn't that feel good, [the_person.title]?"
            the_person "Of course it does... But your sister, she could walk in anytime..."
            if the_person.vagina_available:
                mc.name "Shhh, just be quiet. Your ass looks so amazing [the_person.title]... I should just fuck it right here..."
            else:
                mc.name "Shhh, just be quiet. Your ass looks so good in your [the_person.outfit.get_lower_top_layer.display_name]... I should just pull it down and fuck you in the ass right here..."
            $ the_person.change_arousal(10)
            "[the_person.possessive_title!c] stifles a moan, she pushes her hips back against you as you continue to stroke her."
            the_person "Mmmmmm... Okay... Do it! Just go quick! I don't want your sister to catch us."
            if the_person.vagina_visible:           #If it's available no need to strip.
                "You quickly pull your cock out and begin to rub it between her cheeks."
            else:                                              #Otherwise, strip her down.
                "You don't bother to reply, instead you begin stripping away anything between you and her supple ass."
                $ the_person.strip_to_vagina(prefer_half_off = True, position = "standing_doggy")
                "With her ass finally exposed you waste no time. You quickly pull your cock out and rub it between her cheeks."
            "[the_person.possessive_title!c] pulls some lube out of one of the kitchen drawers."
            mc.name "Wait... you keep lube in the...?"
            the_person "Shut up just fuck me before your sister notices!"
            "You rub some lube on your cock and on [the_person.title]'s asshole. You grab her by the hips and then roughly pull her back until your cock is buried inside her rump."
            $ the_person.break_taboo("anal_sex")
            call fuck_person(the_person, start_position = anal_standing, start_object = make_table(), skip_intro = True, self_strip = False, skip_condom = True) from _call_VT_fetish_mom_kitchen
            $ the_report = _return
            if the_report.get("girl orgasms", 0) > 0:
                "[the_person.possessive_title!c] is positively glowing. She knows that even while preparing dinner, you may come and fuck her ass at any time."
            else:
                "[the_person.possessive_title!c] remains silent. She knows that even while preparing dinner, you may come use her ass for your pleasure at any time."

        "Fuck her ass\n{menu_red}Requires Anal Fetish{/menu_red} (disabled)" if not the_person.has_anal_fetish:
            pass
        "Creampie her" if the_person.has_breeding_fetish:
            if the_person.vagina_available:
                "You slowly reach down and start to slowly caress her cunt."
            else:
                "You slowly reach down and start to slowly rub her pussy through her [the_person.outfit.get_lower_top_layer.display_name]."
            the_person "Hey! What are you doing? Stop that!"
            "You continue rubbing her."
            mc.name "Stop? But doesn't that feel good, [the_person.title]?"
            the_person "Of course it does... But your sister, she could walk in anytime..."
            mc.name "You know you want a pussy full of my cum. Feel it dripping out of your fertile cunt all through dinner time."
            the_person "Yes I know but..."
            if the_person.vagina_available:
                mc.name "Shhh, just be quiet. Your ass looks so amazing [the_person.title]... I should just fuck you right here..."
            else:
                mc.name "Shhh, just be quiet. Your ass looks so good in your [the_person.outfit.get_lower_top_layer.display_name]... I should just pull it down and fuck you right here..."
            $ the_person.change_arousal(10)
            "[the_person.possessive_title!c] stifles a moan, she pushes her hips back against you as you continue to stroke her."
            the_person "Mmmmmm... Okay... Do it! Just go quick! I don't want your sister to catch us."
            if the_person.vagina_visible:           #If it's available no need to strip.
                "You quickly pull your cock out and line it up with her wet slit."
            else:                                              #Otherwise, strip her down.
                "You don't bother to reply, instead you begin stripping away anything between you and her delicious pussy."
                $ the_person.strip_to_vagina(prefer_half_off = True, position = "standing_doggy")
                "With her pussy finally exposed you waste no time. You quickly pull your cock out and line it up with her wet slit."
            $ the_person.break_taboo("condomless_sex")
            $ the_person.break_taboo("vaginal_sex")
            call fuck_person(the_person, start_position = bent_over_breeding, start_object = make_table(), skip_intro = True, self_strip = False, skip_condom = True) from _call_VT_fetish_mom_kitchen_01
            $ the_report = _return
            if the_report.get("girl orgasms", 0) > 0:
                "[the_person.possessive_title!c] is positively glowing. She knows that even while preparing dinner, you may come and fuck her at any time."
            else:
                "[the_person.possessive_title!c] remains silent. She knows that even while preparing dinner, you may come use her for your pleasure at any time."

        "Creampie her\n{menu_red}Requires Breeding Fetish{/menu_red} (disabled)" if not the_person.has_breeding_fetish:
            pass
        "Give her a cum dosage" if the_person.has_cum_fetish:
            call cum_fetish_get_dosage_label(the_person) from _call_VT_cum_fetish_get_dosage_label_fetish_mom_kitchen
        "Cover her in cum\n{menu_red}Not yet written{/menu_red} (disabled)" if the_person.has_cum_fetish:
            pass #TODO
        "Cover her in cum\n{menu_red}Requires Cum Fetish{/menu_red} (disabled)" if not the_person.has_cum_fetish:
            pass
        "Fuck her loudly" if the_person.has_exhibition_fetish:
            $ the_person.slap_ass(update_stats = False)
            "You reach down and slap her ass aggressively. It makes a loud slapping noise."
            the_person "Hey! What are you doing? Stop that!"
            mc.name "Stop? But doesn't that feel good, [the_person.title]?"
            $ the_person.slap_ass(update_stats = False)
            $ the_person.slap_ass(update_stats = False)
            "You don't bother to wait for a reply. You give her multiple hard spanks. The sound of your hand slapping her buttocks echoes through the room."
            "You hear your sister call out from the living room."
            lily "You okay in there mom?"
            the_person "Yes dear! I'm just... you know... chopping some vegetables!"
            $ the_person.slap_ass(update_stats = False)
            "You give her ass another hard spank, as if to punctuate her remark. [the_person.possessive_title!c] is barely able to stifle her moan."
            $ the_person.change_arousal(15)
            "Barely whispering, [the_person.possessive_title] tries to resist, but you can tell this is really turning her on."
            the_person "Your sister, she's going to..."
            if the_person.vagina_available:
                mc.name "Shhh, just be quiet. Your ass looks so amazing [the_person.title]... I should just fuck you right here..."
            else:
                mc.name "Shhh, just be quiet. Your ass looks so good in your [the_person.outfit.get_lower_top_layer.display_name]... I should just pull it down and fuck you right here..."
            mc.name "Besides, would it really be that bad if she caught us? I bet you'd like it if she came in and watched, wouldn't you."
            $ the_person.change_arousal(15)
            $ the_person.slap_ass(update_stats = False)
            $ play_moan_sound()
            "[the_person.possessive_title!c] stifles a moan, she pushes her hips back against you so you give her another round of spanks."
            the_person "Oh god... Do it! Just go quick."
            mc.name "If I fuck you fast, it might get kinda noisy in here."
            the_person "I don't care! Just do it!"
            if the_person.vagina_visible:
                "You quickly pull your cock out and line it up with her wet slit."
            else:                                              #Otherwise, strip her down.
                "You don't bother to reply, instead you begin stripping away anything between you and her delicious pussy."
                $ the_person.strip_to_vagina(prefer_half_off = True, position = "standing_doggy")
                "With her pussy finally exposed you waste no time. You quickly pull your cock out and line it up with her wet slit."
            "You thrust yourself inside her slowly. Her pussy accepts your length easily, well lubricated from your spanking."
            $ the_person.change_arousal(15)
            $ mc.change_arousal(15)
            $ the_person.break_taboo("condomless_sex")
            $ the_person.break_taboo("vaginal_sex")
            "You don't waste anytime and being to fuck her roughly. The sound of her ass cheeks clapping with each thrust fills the room."
            lily "Are you sure you're okay mom? That doesn't sound like vegetables."
            the_person "I'm sure! I'm not chopping vegetables anymore... I'm... oh god... I'm... beating meat!"
            "You try to stifle a laugh."
            lily "Beating... meat?"
            the_person "I mean... tenderizing it! You have to really spank... I mean... smack it hard to get it tender!"
            $ the_person.slap_ass(update_stats = False)
            "You give her ass a solid spank."
            $ the_person.change_arousal(20)
            lily "You sure you don't want some help?"
            the_person "No! I mean... your brother is in here giving me a hand... there's a {i}lot{/i} of meat to tenderize... it might take us a while!"
            "Holy shit she is actually gonna sell that."
            lily "Well... okay, if you're sure."
            "You take the opportunity now to pick up the pace. You are really giving it to [the_person.possessive_title] now."
            call fuck_person(the_person, start_position = standing_doggy, start_object = make_table(), skip_intro = True, self_strip = False, skip_condom = True) from _call_sex_VT_fetish_mom_kitchen_loud_sex_01
            $ the_report = _return
        "Fuck her loudly\n{menu_red}Requires Exhibitionist Fetish{/menu_red} (disabled)" if not the_person.has_exhibition_fetish:
            pass
    "Clearly, in her current attire, it will be obvious what [the_person.possessive_title] has been up to. You look at the state of dinner. It's almost done."
    mc.name "You go clean yourself up. I'll finish preparing dinner."
    the_person "Ahhh... okay... thank you honey!"
    $ clear_scene()
    "[the_person.title] leaves the room, leaving you alone to set up dinner."
    if mc.inventory.has_serum:
        "Now you have a perfect opportunity to give everyone some serum."
        call screen serum_inventory_select_ui(mc.inventory, batch_size = (4 if aunt_living_with_mc() else 2))
        if isinstance(_return, SerumDesign):
            $ dose_dinner_with_serum(_return)
        else:
            "You decide not to add any serum to the dinner."

    "Just as you are finishing up with plating the food, when [the_person.possessive_title] walks back into the kitchen."
    $ the_person.apply_planned_outfit()
    $ the_person.draw_person()
    the_person "Thank you [the_person.mc_title]... for finishing dinner and... you know..."
    "[the_person.possessive_title!c] gives you a kiss on the cheek."
    "You bring the food out and have a nice family dinner together."
    call advance_time() from _call_advance_time_VT_fetish_mom_kitchen_02
    return

label VT_fetish_lily_stream_in_room_label(the_person): # NOTE: This scene is currently disabled. As Lily progresses, give her a scene where you can act out her fetishes on video stream

    ###ANAL STREAM OPTION###
    "You give [the_person.possessive_title] a quick proposition."
    mc.name "Hey [the_person.title]. What do you say we get out that strap-on again? I bet your viewers would love that."
    "[the_person.possessive_title!c] looks at you and smiles."
    the_person "Mmm, that sounds pretty good [the_person.mc_title]... Here, let me take a couple... precautions."
    "[the_person.possessive_title!c] walks over and closes her door and locks it. She turns on some music and turns the volume up."
    the_person "Don't want mom to find out..."
    $ the_person.draw_person(position = "standing_doggy")
    "[the_person.possessive_title!c] goes over to her dresser. She's going through a drawer looking for the toy."
    if the_person.vagina_available:
        mc.name "Mmmm, [the_person.title], your ass looks amazing. I can't wait to see that hole stretched around my cock..."
    else:
        "You step up behind [the_person.possessive_title] and start to grope her ass. She sighs as you massage it."
        "You decide to start getting her ready while she looks for the toy. You start peeling her clothes off."
        $ the_person.strip_outfit(position = "standing_doggy", exclude_upper = True)
        mc.name "Mmmm, [the_person.title], your ass looks amazing. I can't wait to see that hole stretched around my cock..."
    the_person "Ah! Here it is. I know it's hard to wait, but I need to set up the stream first, [the_person.mc_title]."
    "[the_person.possessive_title!c] goes over to her laptop and sits down."
    $ the_person.draw_person(position = "sitting")
    "It takes her a few minutes to set it up. She sets up her camera and makes sure the angle is pointed at her bed."
    the_person "Okay... I got it just about set up. Are you ready?"
    mc.name "Ready when you are."
    the_person "Alright here we go..."
    "She clicks the button on the screen to start the stream."
    the_person "Hey everyone! I have a special stream today with You-Know-Who! Today we're gonna have some fun with this toy I got!"
    $ the_person.draw_person()
    "[the_person.possessive_title!c] hands you a bottle of lube and the dildo, then gets on her bed and gets on her hands and knees with her ass in the air."
    $ the_person.draw_person(position = "doggy")
    "You put the dildo on and lube yourself up. You get behind [the_person.possessive_title] on the bed and start to line yourself up."
    the_person "Oh god, I can't wait. This feel feels amazing when it goes in..."
    "Your cock sinks easily into her greedy back passage. She is so accustomed to being fucked anally now she accommodates you easily."
    the_person "Aaaahhhhhh yes! Now fuck me good! I'm ready for it!"
    call fuck_person(the_person, start_position = doggy_anal_dildo_dp, start_object = make_bed(), skip_intro = True, skip_condom = True) from _call_VT_fetish_lily_stream_in_room_01
    #TODO orgasm dialogue to her streamers
    "[the_person.possessive_title!c] slowly gets up and walks over to her laptop."
    the_person "That's all for now everyone... thanks for watching!"
    "She ends the stream."
    #TODO earnings based on orgasms
    the_person "Anyway, thanks for streaming [the_person.mc_title]... Don't be a stranger now!"
    "You politely excuse yourself."
    $ the_person.apply_planned_outfit()
    return
