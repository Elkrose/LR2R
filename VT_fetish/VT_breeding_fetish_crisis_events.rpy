#Update all the following the_person and movements with breeding personality. Use Hitomi Takami from Ane Haramix or Momoko Kuzuryu from Sumomomo, Momomo: The Strongest Bride on Earth, for ideas, keep to the structure. Movements in quotations:

label VT_breeding_fetish_high_fertility_crisis_label():
    $ the_person = VT_get_highly_fertile_breeder()
    if the_person is None:
        return

    $ update_breeding_fetish_state(the_person)
    if the_person == mom or the_person == lily:
        "You hear a knock on your door."
        mc.name "It's open!"
        $ the_person.draw_person()
        "It's [the_person.possessive_title]. She steps into your room, closes your door, and locks it... her eyes fixed on you with a hungry gleam."
        mc.name "Something you need tonight [the_person.title]?"
        the_person "I've been tracking my cycles, and today's the day! I'm at peak fertility, and I need you to fill me up... I need your seed to make me whole."
        "She takes a step closer, her hands on her hips, her body language screaming 'fuck me'."
    else:
        $ mc.start_text_convo(the_person)
        the_person "Hey, I need your help with something. I'm on my way over. I've got a bit of a situation... I'm so horny and I need you to fix it."
        "Hmm, she's inviting herself over?"
        mc.name "Ok, text me when you get here."
        "A few minutes later, she texts you again."
        the_person "I'm here! Let me in! I'm feeling a little... desperate. I need your cock inside me."
        $ mc.end_text_convo()
        "You go out to your front door and open it."
        $ the_person.draw_person()
        the_person "Hey! Let's go to your room. I need to talk to you about something... and then I need you to fuck me."
        mc.name "Okay... this is a little weird..."
        the_person "I'll explain when we get there... but let's just say I've got a bit of a problem, and I need your help to solve it. I need your seed to make me pregnant."
        "You quickly lead her back to your room. When you walk in, she closes the bedroom door and locks it... then she turns to you and starts to strip down."
    the_person "I've been following my cycles on this app... Today it gave me a notification that I am highly fertile! I can feel it in my body, and I know I need to get pregnant tonight... I need your cock to make it happen."
    "She comes closer, wrapping her arms around you, her body pressed against yours."
    the_person "You need to cum inside me tonight... I'm not taking no for an answer! I need your seed to make me whole... to make me a mother."
    $ mc.change_locked_clarity(30)
    if the_person.is_dominant:
        "She pushes you back onto your bed. She seems pretty intent on taking what she wants from you... and what she wants is your cock inside her."
        "You watch as she starts to strip down, her eyes fixed on you with a hungry gleam... then she climbs up on top of you, positioning your cock at her entrance."
        $ the_person.strip_outfit()
        $ the_person.change_arousal(10)
        "She runs a hand down her belly, to her mound and across her slit. You can see moisture already starting to collect there... she's so wet and ready for you."
        $ the_person.draw_person(position = "cowgirl")
        $ mc.change_locked_clarity(30)
        "[the_person.possessive_title!c] reaches down and pulls your pants off and then climbs up on top of you, positioning your cock at her entrance... then she slowly starts to sink down onto you, her eyes fixed on yours."
        the_person "Oh god... this is it. I can feel it! Tonight's the night you finally knock me up... and make me a mother."
        "She gasps when your dick parts her labia... then she starts to rock her hips, riding you like a pro."
        $ the_person.break_taboo("condomless_sex")
        $ the_person.break_taboo("vaginal_sex")
        the_person "Yes! Oh [the_person.mc_title]... fill me up! Make me pregnant!"
        "She descends slowly, but finally bottoms out with a sigh. She takes a moment to adjust to your girth before she starts to rock her hips some... then she starts to pick up speed, riding you harder and faster."
        the_person "Oh god... here we go! Make me pregnant!"
        call get_fucked(the_person, the_goal = "vaginal creampie", start_position = cowgirl, private = True, skip_intro = True, allow_continue = False) from _call_get_fucked_VT_breeding_fetish_high_fertility_crisis_01
        if the_person.has_creampie_cum:
            the_person "It's inside me! It worked! Don't ask me how I know... I can just feel it! I'm going to be a mother!"
            "She rubs her belly and sighs... then she looks up at you with a smile."
            $ become_pregnant(the_person, mc_father = True, breeder_announce = True) #Guaranteed to knock her up
        else:
            "Too tired to continue, [the_person.possessive_title] lifts off of you a little frustrated."
            the_person "I can't believe it... just... let's make sure we try again soon okay? I need to get pregnant."
            $ VT_fetish_timer_reset(the_person, "breeding", 1, False)
    else:
        mc.name "One knocked up cum slut, coming right up! I'll make sure to fill you up good."
        "You reach down and start to pull her bottoms off... then you pick her up and throw her down on your bed."
        $ the_person.strip_outfit(exclude_upper = True)
        $ mc.change_locked_clarity(50)
        "You pull out your cock and slowly crawl up her body... then you position your cock at her entrance and start to push inside as you whisper into her ear..."
        $ the_person.draw_person(position = "missionary")
        mc.name "Are you ready for this? Once I knock you up, there's no going back... you'll be a mother."
        $ the_person.break_taboo("condomless_sex")
        $ the_person.break_taboo("vaginal_sex")
        "She moans and bucks her hips... then she wraps her legs around you, locking them and pulling you down deeper inside her forcefully with her legs."
        $ play_moan_sound()
        mc.name "Mmm, fuck I guess so! You want it that bad, huh?"
        "You start to piston your hips, savouring the highly fertile, bare pussy that is wrapped around you... then you start to pick up speed, fucking her harder and faster."
        the_person "Give it to me [the_person.mc_title]! Give me a fucking I'll never forget and pour your seed deep! Make me pregnant!"
        call fuck_person(the_person, start_position = breeding_missionary, start_object = make_bed(), private = True, skip_intro = True, skip_condom = True, position_locked = True) from VT_breeding_fetish_high_fertility_crisis_02
        if the_person.has_creampie_cum:
            the_person "It's inside me! I'm pregnant! Don't ask me how I know... I can just feel it! You've made me a mother!"
            "She rubs her belly and sighs... then she looks up at you with a smile."
            $ become_pregnant(the_person, mc_father = True, breeder_announce = True) #Guaranteed to knock her up
        else:
            "Too tired to continue, [the_person.possessive_title] looks up at you a little frustrated."
            the_person "I can't believe it... just... let's make sure we try again soon okay? I need to get pregnant."
            $ VT_fetish_timer_reset(the_person, "breeding", 1, False)
        "Finished for now, [the_person.title] excuses herself... but not before giving you a kiss on the cheek."
    the_person "I'd better get going... but I'll be back for more. I need to make sure I get pregnant."
    if the_person.has_creampie_cum:
        the_person "It'll be a few days before a test shows a definite positive... but I'm almost positive we just made a baby! You've made me so happy."
    else:
        the_person "I'm still going to be fertile for a few days... please try again? Okay? I don't want to wait anymore, I want your baby inside me... I need to be a mother."
    $ the_person.review_outfit()
    $ the_person.draw_person(position = "walking_away")
    return

label VT_breeding_fetish_happy_breeder_crisis_label():
    $ the_person = VT_get_pregnant_breeder()
    if the_person is None:
        return

    $ update_breeding_fetish_state(the_person)
    if the_person == mom or the_person == lily:
        "You hear a knock on your door."
        "You stand up and open your door. It's [the_person.title], dressed very nicely... and looking very horny."
        $ set_special_fetish_outfit(the_person)
        $ the_person.draw_person()
        $ mc.change_locked_clarity(20)
        "She steps into your room, closes your door, and locks it... then she turns to you with a hungry look in her eyes."
        mc.name "Something you need tonight [the_person.title]?"
        the_person "Yeah... something like that! I need your cock inside me, and I need it now."
    else:
        "*Ding Dong*"
        "You're roused from your bed by the loud ring of your doorbell."
        $ mc.change_location(hall)
        "You head to your front door and see [the_person.possessive_title] standing there... outside... in a very provocative outfit."
        $ set_special_fetish_outfit(the_person)
        $ the_person.draw_person()
        $ mc.change_locked_clarity(20)
        "You quickly open the door and invite her inside."
        "To avoid any situations with [mom.possessive_title] or [lily.possessive_title], you quickly invite her to your room."
        $ mc.change_location(bedroom)
        "You walk into your room, close the door and lock it... then you turn to [the_person.title] and see the hunger in her eyes."

    $ the_person.draw_person(position="kissing")
    "[the_person.possessive_title!c] quickly turns and embraces you... her body pressed against yours, her lips on yours."
    the_person "Oh, [the_person.mc_title], I'm sorry to just come over without asking like this... but I need you, I need your cock inside me."
    the_person "I was in bed trying to sleep but I kept thinking about the baby growing inside me and I started getting all worked up... I need you to make me feel better."
    "She stumbles over her words for a second, her eyes fixed on yours."
    the_person "Oh geez... I just couldn't stop thinking about how good it feels when you fuck me! I need you to do it again, and again, and again."
    "You are hardly surprised. [the_person.possessive_title!c]'s breeding fetish makes her a cum-starved slut... and you're happy to oblige."
    the_person "I just couldn't help it... will you please let me stay here tonight? I promise I'll be good, I'll do anything you want."
    $ mc.change_locked_clarity(30)
    "[the_person.possessive_title!c] looks at you with hopeful eyes, her body language screaming 'fuck me'."
    menu:
        "Accept":  #This begins the sex scene
            "[the_person.possessive_title!c] walks over to the windows and looks out of it. You see her hips move side to side for a second, and then she peeks back at you."
            $ the_person.draw_person(position = "back_peek")
            the_person "It's so pretty out tonight... Why don't you come over here and take me from behind?"
            "You walk over and stand behind [the_person.possessive_title] as she looks out the window... then you reach out and grab her hips, pulling her back against you."
            "You put your hands on her hips, feeling her soft skin... then you line yourself up and gently push your cock inside her."
            $ the_person.break_taboo("condomless_sex")
            $ the_person.break_taboo("vaginal_sex")
            call fuck_person(the_person, start_position = facing_window, start_object = make_window(), skip_intro = True, skip_condom = True) from _call_fuck_VT_breeding_fetish_happy_breeder_crisis_01
            "[the_person.possessive_title!c] walks over to your bed and lays down on her back and takes off any remaining clothing."
            $ the_person.strip_outfit(exclude_feet = False, position = "missionary")
            $ the_person.draw_person(position = "missionary")
            "You join her on the bed. She raises her arm, and you lay your head down on her breast... feeling her soft skin, her warmth."
            "You both catch your breath and just enjoy the warmth of each other's bodies... then you start to get hard again, thinking about her body, her pussy."
            if the_person.is_lactating:
                "When you squeeze her nipple, some of her milk begins to come out... and you can't resist the temptation to taste it."
                the_person "Oh god, my nipples are so sensitive now that my milk is coming in... do you want to taste it?"
                "You turn your head and begin to lick and suck her nipple... feeling her milk flow into your mouth, tasting her sweetness."
                if the_person.lactation_sources > 3: #Lots of milk
                    "After a few moments, her milk really begins to flow. There is now a thin but steady stream of the creamy fluid flowing into your mouth."
                    the_person "Ah! Oh baby that's it! aahhhhh..."
                    $ the_person.change_arousal(30)
                    $ mc.change_locked_clarity(30)
                    "Her cream is sweet and plentiful... and you can't get enough of it."
                    the_person "ohhh, [the_person.mc_title] that felt so good. Can you, you know, do the other one too?"
                    mc.name "Mmm, certainly."
                    "You switch sides and begin to suckle again... feeling her milk flow into your mouth, tasting her sweetness."
                    the_person "Ahh! Oh my god..."
                    $ the_person.change_arousal(30)
                    "Her cream just keeps flowing... and you drink it in, feeling her warmth, her love."
                    $ mc.change_energy(50)
                    $ the_person.change_energy(50)
                else:
                    "Her milk comes out in small amounts as you suckle... her breathing catches with each pull."
                    the_person "Ahhhh... oh [the_person.mc_title] that feels so good..."
                    $ the_person.change_arousal(30)
                    $ mc.change_locked_clarity(20)
                    "You manage to squeeze a bit of her cream out... and you drink it in. It's a delicious treat that restores some of your energy."
                    $ mc.change_energy(40)
                    $ the_person.change_energy(40)
            else:
                $ play_moan_sound()
                "[the_person.possessive_title!c] moans and runs her hands through your hair... then she pulls you down, kissing you, her lips on yours."
                "You turn your head and begin to lick and suck her nipple... feeling her soft skin, her warmth."
                $ the_person.change_arousal(20)
                $ mc.change_locked_clarity(10)
                the_person "That feels so good [the_person.mc_title]... I love it when you touch me like that."
                $ mc.change_energy(30)
                $ the_person.change_energy(30)
                "Soon you are getting hard again... thinking about her body, her pussy."
            "You roll over on top of [the_person.possessive_title]. She wraps her arms around you as you slowly sink your cock into her moist cunt."
            call fuck_person(the_person, start_position = breeding_missionary, start_object = make_bed(), skip_intro = True, skip_condom = True) from _call_fuck_person_VT_breeding_fetish_happy_breeder_crisis_02

            the_person "Oh god [the_person.mc_title], tonight has been incredible... excuse me for a second."
            $ the_person.draw_person(position = "walking_away")
            "[the_person.possessive_title!c] excuses herself to your restroom. After a few minutes she comes back. She sits down on the side of the bed."
            $ the_person.draw_person(position = "sitting")
            the_person "Why don't... why don't you come sit on the side of the bed? I know you're tired but... I could really go for one more round..."
            "You sit up and move to the side of the bed... then you see [the_person.title] looking at you with hungry eyes."
            "[the_person.possessive_title!c] smiles and gets down on her knees below you."
            $ the_person.draw_person(position = "blowjob")
            the_person "I'm sorry [the_person.mc_title]... I just can't help it. It feels so good inside me... and I need it again."
            "[the_person.possessive_title!c] reaches down and starts to stroke your mostly soft cock... then she looks up at you with big eyes."
            "Her hands feel good, but you can tell it's going to take a little more to get you aroused again after cumming twice already."
            ###IF girl has big tits, ask for a tit fuck
            if the_person.has_large_tits:
                mc.name "Why don't you put it between your tits for a while?"
                "[the_person.possessive_title!c] smiles up at you."
                the_person "Anything for you, [the_person.mc_title]."
                "[the_person.possessive_title!c] looks up at you while she scoots closer to you, until her body is up against yours. She uses her hand to point your cock straight up while she moves it in position between her amazingly soft tits."
                "Once in position, she uses her hands to push her [the_person.tits_description] together, squashing your prick in her heavenly soft tit-flesh."
                $ mc.change_locked_clarity(30)
                "[the_person.possessive_title!c] starts to move up and down. Now and then when her tits are at the base of your dick she licks the sensitive tip."
                "The view of [the_person.possessive_title] on her knees before you, happy with you between her tits is extremely arousing. It isn't long until you are fully erect."

            else:
                mc.name "Why don't you put it in your mouth for a while?"
                "[the_person.possessive_title!c] smiles up at you."
                the_person "Anything for you, [the_person.mc_title]."
                "[the_person.possessive_title!c] looks up at you while she scoots closer to you, then lowers her head down and begins to lick up and down your groin."
                $ mc.change_locked_clarity(30)
                "She moves her head to the tip and slowly moves her head up and down your shaft a few times. She pulls off for a second then looks up at you."
                the_person "Mmm, I can taste the remnants of earlier... I love it when you cum inside me."
                "[the_person.possessive_title!c] resumes blowing you with vigour."
                "The view of [the_person.possessive_title] on her knees before you, happy with your cock in her mouth is extremely arousing. It isn't long until you are fully erect."

            mc.name "Okay [the_person.title], I'm ready. Now bend over and get ready for another round."
            "[the_person.possessive_title!c] obediently does as you ask and bends over your bed as you stand up and get behind her."
            $ the_person.draw_person(position = "standing_doggy")
            $ mc.change_locked_clarity(50)
            the_person "Come and get it, [the_person.mc_title]... it's yours for the taking!"
            "You line yourself up with her soaking wet slit and push yourself in."
            ###Sex Doggy Style###
            call fuck_person(the_person, start_position = bent_over_breeding, start_object = make_floor(), skip_intro = True, skip_condom = True) from _call_fuck_person_VT_breeding_fetish_happy_breeder_crisis_03

            "Exhausted from your night with [the_person.possessive_title], you get back up into your bed. [the_person.possessive_title!c] joins you and you quickly fall asleep, cuddling together."
            "That night, you have many pleasant dreams involving [the_person.possessive_title] and sex in all kinds of crazy positions."
        "Refuse":       # allow for player to decide if he wants to induce fetish
            mc.name "I'm sorry [the_person.title], I really need to get some sleep."
            $ the_person.change_stats(happiness = -10, obedience = -10)
            the_person "Oh! I'm sorry... Maybe tomorrow then?"
            "[the_person.possessive_title!c] quickly sulks off."
            $ VT_fetish_timer_reset(the_person, "breeding", 2, False)
            return # EXIT
        "Too Tired" if mc.energy < 30:
            "[the_person.possessive_title!c] is surprised by your answer."
            $ the_person.change_stats(happiness = -5, obedience = -5)
            the_person "Oh! I'm sorry... I didn't think about that. Maybe tomorrow then?"
            "[the_person.possessive_title!c] quickly sulks off."
            $ VT_fetish_timer_reset(the_person, "breeding", 1, False)           
            return  # EXIT

    call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_VT_breeding_fetish_happy_breeder_crisis_02
    call VT_breeder_cowgirl_wakeup_label(the_person) from _call_breeder_overnight_cowgirl_wakeup_VT_breeding_fetish_happy_breeder_crisis01
    return "Advance Time"

label VT_breeding_fetish_family_sleep_crisis_label():
    $ the_person = VT_get_family_breeder()
    if the_person is None:
        return

    $ update_breeding_fetish_state(the_person)
    if the_person == lily:
        "Before going to bed, you hear a knock on your door. You hear [the_person.possessive_title] from the other side of the door, her voice husky with desire."
        the_person "Hey [the_person.mc_title], you still up? I was just wondering if I could come in for a bit... I need you."
        "You invite her in, and she enters wearing a provocative outfit that showcases her curves."
        $ set_special_fetish_blue_outfit(the_person)
        $ the_person.draw_person()
        $ mc.change_locked_clarity(30)
        the_person "So... I was wondering... is it okay if I sleep in here with you again tonight? I promise I'll be good... and I'll make it worth your while."
        menu:
            "Not tonight" if mc.lust_tier < 3:
                mc.name "Sorry [the_person.title]... I had a long day and I'm pretty worn out... maybe tomorrow?"
                "She pouts, her face falling in disappointment."
                the_person "Whatever [the_person.mc_title]... see you in the morning I guess?"
                "You head for bed, looking forward to a restful night's sleep... but you can't shake the feeling that you're missing out on something special."
                $ the_person.change_stats(happiness = -5, obedience = -2)
                $ VT_fetish_timer_reset(the_person, "breeding", 1, False)
                return
            "Not tonight\n{menu_red}Too much Lust to say No{/menu_red} (disabled)" if mc.lust_tier > 2:
                pass
            "Strip first":
                mc.name "That sounds good [the_person.title]... why don't you give me a show before we go to bed? I want to see your body, feel your heat."
                "[the_person.possessive_title!c] smiles at you, her eyes sparkling with desire."
                the_person "Aww, does my [the_person.mc_title] wanna see his [the_person.title] get naked for him? What a pervert! I love it."
                "[the_person.possessive_title!c] winks at you before beginning her routine, her movements slow and sensual."
                call strip_tease(the_person, for_pay = False) from _free_strip_scene_VT_breeding_fetish_family_sleep_crisis_01
                $ mc.change_locked_clarity(50)
                mc.name "Damn [the_person.title], you are really getting good at that. You're making me so hard."
                "[the_person.possessive_title!c] bites her lip, glancing down at your bulge. Her cheeks are flushed and rosy, her eyes shining with desire."
                the_person "Hey... if you want to I could... you know... take care of that tent you are sporting there [the_person.mc_title]. I want to feel you inside me, to taste your cum."
                "You stand up and embrace her, your dick straining against your clothes, eager to begin another incestuous tryst with [the_person.possessive_title]."

        "You kiss [the_person.possessive_title] along her neck and ear, your lips tracing the curve of her jaw. She shivers at the sensation and then whispers in your ear."
        $ the_person.change_arousal(20)
        the_person "Throw me down on your bed, [the_person.mc_title]. I want to feel your weight on top of me while you fuck my brains out! I want to be yours, to be your breeding stock."
        "You roughly pick up [the_person.possessive_title] and carry her over to the bed. You throw her down and quickly jump on top of her, your body covering hers."
        if not the_person.vagina_available:
            $ the_person.strip_to_vagina(position = "missionary", prefer_half_off = True)
        "[the_person.possessive_title!c] spreads her legs wide, giving you easy access. She sighs as you sink your cock into her greedy cunt, her body arching up to meet yours."

    elif the_person == mom:
        "You are just drifting off to sleep when you hear your bedroom door squeak open. You look up to see [the_person.possessive_title] walking in, her eyes fixed on you with a hungry gleam."
        $ set_special_fetish_outfit(the_person)
        $ the_person.draw_person()
        $ mc.change_locked_clarity(30)
        mc.name "[the_person.title]?"
        the_person "Hi honey... I was feeling lonely over in my room, I thought maybe you might like some company tonight... and maybe a little something more."
        $ the_person.draw_person(position = "sitting")
        "[the_person.possessive_title!c] sits on the edge of your bed, her body language screaming 'fuck me'."
        menu:
            "Not tonight" if mc.lust_tier < 3 or mc.energy < 80:
                mc.name "Sorry [the_person.title]... I had a long day and I'm pretty worn out... maybe tomorrow?"
                "She pouts, her face falling in disappointment."
                the_person "I understand [the_person.mc_title]... see you in the morning I guess?"
                "You roll over while she leaves the room and quickly fall asleep... but you can't shake the feeling that you're missing out on something special."
                $ the_person.change_stats(happiness = -5, obedience = -2)
                $ VT_fetish_timer_reset(the_person, "breeding", 1, False)
                return
            "Not tonight\n{menu_red}Too much Lust to say No{/menu_red} (disabled)" if mc.lust_tier > 2 and mc.energy > 80:
                pass
            "Let Her":
                "You pull her onto the bed, eager to begin another incestuous tryst with [the_person.possessive_title]. You want to feel her body, to taste her skin."

    else: # aunt or cousin
        "You are just drifting off to sleep when you hear your bedroom door squeak open. You look up to see [the_person.possessive_title] walking in, her eyes fixed on you with a hungry gleam."
        $ set_special_fetish_outfit(the_person)
        $ the_person.draw_person()
        $ mc.change_locked_clarity(30)
        mc.name "What are you doing here [the_person.title]?"
        if the_person == aunt:
            the_person "Hi [the_person.mc_title], I need your help. I need you to fuck me, to make me feel like a woman again."
        else:
            the_person "Be quiet [the_person.mc_title], you need to help me right now. I need your cock, your cum, your seed."
        $ the_person.draw_person(position = "sitting")
        "[the_person.possessive_title!c] sits on the edge of your bed, her body language screaming 'fuck me'."
        menu:
            "Not tonight" if mc.lust_tier < 3 or mc.energy < 80:
                mc.name "Sorry [the_person.title]... I had a long day and I'm pretty worn out... maybe tomorrow?"
                "She pouts, her face falling in disappointment."
                $ VT_fetish_timer_reset(the_person, "breeding", 1, False)
                if the_person == aunt:
                    the_person "Ah, yes... well... maybe another time."
                else:
                    the_person "Whatever."
                "You roll over while she leaves the room and quickly fall asleep... but you can't shake the feeling that you're missing out on something special."
                $ the_person.change_stats(happiness = -5, obedience = -2)
                return
            "Not tonight\n{menu_red}Too much Lust to say No{/menu_red} (disabled)" if mc.lust_tier > 2 and mc.energy > 80:
                pass
            "Help Her":
                "You quickly push her down on the bed, eager to give [the_person.possessive_title] what she needs. You want to feel her body, to taste her skin, to make her cum."

    $ the_person.break_taboo("condomless_sex")
    $ the_person.break_taboo("vaginal_sex")
    call fuck_person(the_person, start_position = breeding_missionary, private = True, start_object = make_bed(), skip_intro = True, skip_condom = True) from _call_fuck_person_VT_breeding_fetish_family_sleep_crisis_01
    "After you finish your rutting, you and [the_person.possessive_title] get under the covers of your bed, your bodies entwined, your skin touching."
    "Spooning behind [the_person.possessive_title], you drift off to a wonderful night's sleep, her body heat and the feeling of her naked skin against yours giving you very pleasant dreams."
    call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_VT_breeding_fetish_family_sleep_crisis
    call VT_breeder_cowgirl_wakeup_label(the_person) from _call_breeder_overnight_cowgirl_wakeup_VT_breeding_fetish_family_sleep_crisis
    return "Advance Time"

label VT_breeding_fetish_employee_high_fertility_crisis_label():
    $ the_person = VT_get_highly_fertile_employee_breeder()
    if the_person is None:
        return

    $ update_breeding_fetish_state(the_person)
    $ set_special_fetish_outfit(the_person)
    "As you are working, you get a text on your phone."
    $ mc.start_text_convo(the_person)
    the_person "Hey, can you help me with something? I'll be in your office... and I need it now."
    mc.name "Sure, I'll be right there."
    $ mc.end_text_convo()
    $ mc.change_location(ceo_office)
    "You step into your office, and you're immediately hit with the sight of [the_person.possessive_title] bending over your desk, her ass in the air."
    mc.name "I swear if this is about taxes..."
    $ the_person.draw_person(position = "standing_doggy")
    $ mc.change_locked_clarity(50)
    the_person "Nope! This is definitely not about taxes... it's about getting me pregnant."
    "You close your office door and lock it, your heart racing with anticipation."
    the_person "Though what happens here might become a happy little tax break in 9 months... if you know what I mean."
    "As you start walking over to her, she moves her hips back and forth a little, her body language screaming 'fuck me'."
    the_person "I know you're busy, so I wanted to make this as easy as possible. I'm fertile, and I need your seed inside me."
    "You walk up behind her and put your hands on her hips, feeling her soft skin and curvy body."
    the_person "It's easy... just stick it in, and make sure to push deep when you finish... I want to feel your cum inside me."
    "You give her ass a playful spank, and she moans in response, her body arching up to meet yours."
    mc.name "God you are such a good little slut. Presenting me your wet little pussy to fuck so I can knock you up."
    $ the_person.change_arousal(5)
    the_person "Yeah [the_person.mc_title]! I want it so bad... I need it so bad."
    "You give her ass another spank, and she cries out in pleasure, her body trembling with desire."
    mc.name "Beg for it."
    "She doesn't hesitate, her voice husky with desire."
    the_person "Fuck me [the_person.mc_title]! Fuck me raw and don't stop fucking me until your cock pulses and blows your seed inside me! I want to be your breeding stock, your cumdump."
    $ mc.change_locked_clarity(50)
    "You start to pull out your cock, your body aching with desire, and [the_person.possessive_title] is so wet you slide in easily."
    $ the_person.break_taboo("condomless_sex")
    $ the_person.break_taboo("vaginal_sex")
    the_person "Yes! Oh [the_person.mc_title], fuck me good! Paint my cervix with your seed!"
    call fuck_person(the_person, start_position = bent_over_breeding, start_object = make_desk(), skip_intro = True, position_locked = True, skip_condom = True, private = True) from _call_VT_breeding_fetish_employee_high_fertility_crisis
    if the_person.has_creampie_cum:
        $ the_person.draw_person(position = "standing_doggy")
        "[the_person.possessive_title!c] is still bent over your desk, but has her hands between her legs, trying to hold your cum in, a look of pure ecstasy on her face."
        "It is beginning to run down the inside of her thighs, a sign that your seed is taking root inside her."
        the_person "Oh god... it's so deep... I can feel it inside me, spreading its warmth, looking for my egg to impregnate me."
        $ become_pregnant(the_person, mc_father = True, breeder_announce = True) #Guaranteed to knock her up
        $ the_person.change_stats(happiness = 10, obedience = 10)
        "[the_person.title] is euphoric, having taken your load she so desperately wanted, her body glowing with a newfound sense of purpose."
        $ the_person.draw_person(position = "missionary")
        "She rolls over onto her back on your desk, lifting her hips to try and keep your cum inside her, a look of pure satisfaction on her face."
        the_person "Is it okay if I just lay like this for a bit? I read that it can help... the sperm reach the egg."
        mc.name "That's fine. I'll lock the door behind me."
        the_person "Okay. Thank you [the_person.mc_title]."
        $ mc.change_location(lobby)
    else:
        $ the_person.draw_person(position = "stand3")
        the_person "That's it?... I thought you'd be able to give me more... to make me pregnant."
        mc.name "I'm sorry, I'm just too tired right now."
        the_person "Okay... just... try again soon, okay? I need it, I need your seed inside me."
        $ the_person.change_happiness(-15)
        "You can tell she is really disappointed, her body language screaming 'I need more'."
        $ VT_fetish_timer_reset(the_person, "breeding", 1, False)
    $ clear_scene()
    return

label VT_breeder_cowgirl_wakeup_label(the_person):
    "All night long, you have sexy dreams centred around [the_person.possessive_title], your mind filled with visions of her body, her curves, her fertile womb."
    "She's on her knees, sucking you off expertly, her lips wrapped around your cock, her tongue dancing across your skin. Later, she's on her back while you pin her to the bed, your body covering hers, your cock deep inside her. Sometime later, she's on her hands and knees, taking your cock from behind like a pro, her body arching up to meet yours."
    "When morning comes, you feel a stirring in your loins again as you start to slowly wake up. This time, however, there are some very pleasant sensations coming from your crotch, a warm, wet feeling that can only mean one thing."
    $ mc.change_locked_clarity(50)
    $ the_person.apply_outfit(Outfit("Nude"))
    $ the_person.draw_person(position = "cowgirl")
    $ the_person.change_arousal(35)
    "You slowly open your eyes and discover that [the_person.possessive_title] is on top of you, riding you in the cowgirl position, her body moving up and down, her hips swaying back and forth."
    "You reach up and grab her amazing ass cheeks, feeling her soft skin, her curves. [the_person.possessive_title!c] looks in your eyes when she feels your hands on her, a smile spreading across her face."
    the_person "Good morning [the_person.mc_title]... Sorry but when I woke up I noticed you were hard so... I figured you wouldn't mind if I hopped on for a bit... I needed it, I needed your cock inside me."
    $ play_moan_sound()
    "[the_person.possessive_title!c] moans during one slow stroke, her body trembling with pleasure, her eyes locked on yours."
    "You decide to lay back and enjoy the ride, feeling her body, her heat, her wetness."
    call get_fucked(the_person, the_goal = "vaginal creampie", start_position = cowgirl, start_object = make_bed(), skip_intro = True, allow_continue = False) from _call_get_fucked_VT_breeder_cowgirl_wakeup_label_01
    mc.name "Oh god what a wakeup. I think I'm gonna go back to sleep for a bit. Thanks, [the_person.title]... you're the best."
    if the_person == mom:
        "[the_person.possessive_title!c] looks at you and smiles, her eyes shining with love, her face glowing with satisfaction."
        the_person "Oh, anything for you [the_person.mc_title]. Well, I'd better go get ready for the day! I have a feeling it's going to be a great day."
    elif the_person == lily:
        "[the_person.possessive_title!c] gives you a peck on the cheeks, her lips soft, her touch gentle."
        if had_family_threesome():
            the_person "Oh, anything for my big brother, just make sure mom doesn't find out... yet."
        elif day%7 < 5:
            if the_person.is_employee:
                the_person "You're welcome big brother, but I'd better go and get ready for work! I have a lot to do today."
            else:
                the_person "You're welcome big brother, but I'd better go and get ready for school! I don't want to be late."
        else:
            the_person "Anytime big bro, but I got to go, I'm meeting some friends in town. Maybe I'll see you later?"
    elif the_person == starbuck:
        "[the_person.possessive_title!c] giggles for a second then says goodbye, her eyes sparkling with mischief."
        the_person "Yeah well, just don't tell my other customers about this, I can't make house calls for everyone... or can I?"
    else:
        "[the_person.title] looks at you and winks, her eyes shining with satisfaction, her face glowing with pleasure."
        the_person "Anytime [the_person.mc_title]! I'd better go get ready! I have a feeling it's going to be a great day."
    $ the_person.apply_planned_outfit(show_dress_sequence = True)
    $ the_person.draw_person(position = "stand3")
    "You fall back asleep, feeling satisfied, feeling happy. When you wake up, [the_person.possessive_title] has left, but you can still feel her presence, her heat, her love."
    $ clear_scene()
    "Looks like you slept in! But it was worth it, wasn't it?"
    return