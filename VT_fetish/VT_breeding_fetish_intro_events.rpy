
#Fetish Intro Labels
label VT_breeding_fetish_employee_intro_label(the_person):
    "You are finishing up the last of your work today and closing up. All your employees should be gone for the day."
    "However, you are surprised when you are interrupted by someone, a look of desire in their eyes."
    $ the_person.draw_person()
    the_person "Ah! [the_person.mc_title]... I was hoping to catch you alone. I need to talk to you about something... something important."
    mc.name "Good evening [the_person.title]. What can I do for you?"
    the_person "Ah... more like... what can you do to me... I've been having these thoughts, these feelings... and I need your help to satisfy them."
    "Did you hear that right? Is she really asking for what you think she is?"
    mc.name "Oh?"
    the_person "I umm... I mean... sorry. It's just that lately, I've been feeling this intense desire to be bred, to be filled with your cum and made pregnant."
    "She looks a bit flustered for a second, but quickly gathers her thoughts and starts to talk to you, her words spilling out in a rush."
    if the_person.age < 35:
        the_person "Well, you know sir, I'm still pretty young, and lately I've been dealing with some pretty intense biological... urges. I feel like my body is screaming for me to get pregnant, to be bred and made whole."
    else:
        the_person "Well, you know sir, I'm starting to get a bit older, and as my biological clock is ticking I've been getting some pretty intense... urges. I feel like I'm running out of time, and I need to be bred before it's too late."
    the_person "I'm not sure why, but lately I've been having these fantasies about having sex, raw, over and over, and getting filled with cum! I want to feel your cock inside me, twitching and pulsing your loads deep, over and over..."
    "Lately, you've been slipping her the Vitamin D so much, it increased her drive to reproduce. Unsurprisingly, it sounds like she has developed a breeding fetish, a desire to be bred and made pregnant."
    if the_person.knows_pregnant:
        the_person "Obviously I'm already pregnant, but umm, I've really been craving your cock inside me, twitching and pulsing your loads deep, over and over... I want to feel like I'm being bred, like I'm being made whole."
    else:
        the_person "I don't know how to say this but, I've been craving you, and your cock, twitching and pulsing load after load deep inside me! I want to be knocked up, to be made pregnant and feel like a real woman."
    $ mc.change_locked_clarity(20)
    "Her hormones must really be effecting her, for her to be this forward with you. You decide to take advantage of the situation... and of her, to give her what she's been craving."
    "You get close to her, your body inches from hers. She wraps her arms around you, pulling you in close."
    $ the_person.draw_person(position = "kissing")
    mc.name "So what you are saying is... you want to be bred, to be made pregnant and feel like a real woman?"
    "You grab her ass and grope it, pushing into her, feeling her soft skin and curves."
    mc.name "... You want me to take you, to make you mine and fill you with my cum?"
    $ the_person.draw_person(position = "against_wall")
    "You roughly pick her up and slowly move her backwards, your body covering hers."
    mc.name "... You want me to pin you down and fuck your brains out, to make you scream with pleasure and beg for more?"
    "You keep her backing up until her ass runs into the edge of someone's desk, then you force her down onto her back, your body on top of hers."
    $ the_person.draw_person(position = "missionary")
    the_person "Oh my god... yes, that's exactly what I want. I want to be bred, to be made pregnant and feel like a real woman."
    if the_person.vagina_available:
        "You reach down and pull your cock out from your pants, feeling your desire, your need to breed her."
    else:
        "As you start to pull your cock out, [the_person.possessive_title] reaches down and starts pulling her clothes off, revealing her body, her curves."
        $ the_person.strip_to_vagina(prefer_half_off = True, position = "missionary")
    $ the_person.change_arousal (15)
    $ mc.change_locked_clarity(50)
    mc.name "... and I'm going to pin you down and I'm going to breed you and make you mine."
    "You grab her hands and force them down at her sides. She has a wild look in her eye as your raw cock nears her cunt."
    mc.name "... and fucked your brains out..."
    "As you finish those words, you push yourself inside her."
    $ play_moan_sound()
    "She moans as it goes in."
    $ the_person.change_arousal (20)
    $ mc.change_locked_clarity(50)
    $ the_person.break_taboo("condomless_sex")
    $ the_person.break_taboo("vaginal_sex")
    mc.name "... and didn't stop until I dump my cum deep inside your wet breeding hole?"
    the_person "Oh god! Yes do it! Oh fuck!"
    "Still holding her hands down, you start to thrust rapidly, feeling your desire, your need to breed her. It's time to give this horny slut a creampie, to make her pregnant and feel like a real woman."
    call fuck_person(the_person, start_position = breeding_missionary, start_object = make_desk(), private = True, skip_intro = True, position_locked = True, skip_condom = True) from _VT_breeding_fetish_employee_intro_01
    if the_person.has_creampie_cum:
        the_person "Oh god! It's so deep! Oh thank you so much [the_person.mc_title]! I feel like I've been made whole, like I've been bred and made pregnant."
    else:
        the_person "Oh god, so deep and it isn't leaking out! I feel like I've been made whole, like I've been bred and made pregnant."
        pass
    $ VT_add_breeding_fetish(the_person)
    if the_person.knows_pregnant:
        the_person "I don't care if I am already pregnant... Please do that again! My body was made to take your cum like that, to be bred and made whole."
    else:
        the_person "I hope that did it, but you'd better cum inside me again and again anyway! I want to be made pregnant, to feel like a real woman."
    "You slowly back away from [the_person.title], allowing her to get up, feeling your desire, your need to breed her again."
    $ the_person.draw_person()
    "[the_person.possessive_title!c] slowly stands up, her legs are a little unsteady, but she's smiling, she's happy."
    mc.name "I need to get a few more things done before I close up the office. From now on, you are my breeding stock, my cumdump. Be ready to take my cum whenever I tell you to, to be bred and made pregnant."
    the_person "Yes! Yes sir! I'll be ready, don't worry! I'll be your breeding stock, your cumdump, your pregnant slut."
    $ the_person.draw_person()
    "You say goodbye to [the_person.title], feeling your desire, your need to breed her again."
    "[the_person.possessive_title!c] now has a fetish to get bred by you, to be made your personal breeding stock."
    return #Needs testing

label VT_breeding_fetish_family_intro_label(the_person):
    $ mc.change_location(the_person.home)
    $ the_person.draw_person(position = "back_peek")
    "You walk into [the_person.possessive_title]'s bedroom, and you're immediately hit with the sight of her curves, her body.  She is looking at herself in the mirror, but turns to look when she hears you walk in."
    the_person "Oh hey [the_person.mc_title]. I was just getting ready to head for bed... but I'm glad you're here."
    "She takes one last look at herself in the mirror, then turns around, her eyes locked on yours."
    $ the_person.draw_person()
    the_person "Do you want to cuddle with me for a little bit? I love feeling your body against mine."
    mc.name "Sounds nice."
    $ the_person.draw_person(position = "missionary")
    $ mc.change_locked_clarity(15)
    "You lay down next to [the_person.possessive_title] as she lays down on her back. You rest your head on her chest and put your arm across her, feeling her soft skin, her curves."
    "For a while you simply enjoy the heat of each other's bodies. She is the first to break the silence, her voice husky with desire."
    if the_person.knows_pregnant:
        the_person "Do you think it's weird, if I say I love this feeling? Being pregnant, making babies. It's like my body was made to do this, over and over again."
        the_person "I'm already looking forward to making another one, and this one isn't even here yet! I want to be your breeding stock, your cumdump."
    elif the_person.age > 35:
        the_person "Do you think I'm too old to have a baby? My hormones are in overdrive lately... I feel like I'm going crazy with desire."
        mc.name "No way. With modern medical science, women are having babies older and older, into their late forties even. And I'm happy to help you with that."
    else:
        the_person "My hormones are being crazy lately... would it be weird if I told you I... want to get knocked up? I want to feel your cum inside me, to be bred and made pregnant."
        mc.name "I'd imagine that's a pretty normal thing. We don't survive as a species if we don't have a drive to reproduce, right? And I'm happy to help you with that."
        the_person "I suppose so... but it feels so dirty, so wrong. But at the same time, it feels so right, so natural."
    "You move your hand to her belly and begin to rub it, feeling her soft skin, her curves. You can tell by her arousal that she's really ready to be fucked proper."
    "You wonder if she is on the verge of developing a fetish. Do you want to try and push her over the edge?"
    menu:
        "Attempt to train her breeding fetish" if mc.energy > 40:
            pass
        "Too tired" if mc.energy <= 40:
            pass
            #TODO re add the event for this person for the next day.
            $ VT_fetish_timer_reset(the_person, "breeding", 1) 
            $ clear_scene()
            return
        "Too risky, leave her alone":
            pass
            $ VT_fetish_timer_reset(the_person, "breeding", 1) 
            $ clear_scene()
            return
    "You decide it's time to train [the_person.possessive_title] to be your own personal breeding stock, your cumdump."
    "You push yourself up and on top of [the_person.title]. She puts her arms around you as your body begins to press against hers, feeling her soft skin, her curves."
    mc.name "Honestly, I think it's pretty normal to have desires like that. To want to be bred, to want to be made pregnant."
    the_person "Yeah... I guess you're right. But it's still so dirty, so wrong."
    "You start to kiss her along her neck and then whisper in her ear, your breath hot against her skin."
    mc.name "To have a man pin you down, fuck you senseless, then dump his risky load deep inside you, over and over. That's what you need, that's what you want."
    $ the_person.change_arousal(20)
    $ mc.change_locked_clarity(20)
    the_person "Ah, that does sound nice... so dirty, so wrong, but so nice."
    mc.name "It sounds more than nice though, doesn't it? It's what you NEED. A bull, who fucks you and knocks you up, over and over. Like some kind of livestock."
    the_person "Ahhh, yeah! Oh god... that's exactly what I need, what I want."
    $ the_person.change_arousal(20)
    "You reach down and start to pull your cock out, feeling your desire, your need to breed her."
    the_person "But... we're... you know... family..."
    mc.name "Shhh, it's okay. You can trust me, right? We're both consenting adults, who just happen to be related. And I'm going to make you feel so good, so right."
    "She bites her lip, her eyes locked on yours. It's clear from the look in her eyes that she wants it badly, but is afraid to take the leap."
    mc.name "Tell you what, let's go a little farther, and if it feels wrong we can stop. But I don't think it will, I think it will feel so right, so natural."
    $ the_person.add_situational_slut("situation",20, "I can stop if I want to...")
    "She nods her head in agreement, her eyes still locked on yours."
    if the_person.vagina_available:
        "You finish pulling your cock out and begin to rub it along her slit, feeling her soft skin, her curves."
    else:
        "As you finish pulling your cock out, [the_person.possessive_title] reaches down and starts pulling her bottoms off, revealing her body, her curves."
        $ the_person.strip_to_vagina(prefer_half_off = True, position = "missionary")
    $ mc.change_locked_clarity(50)
    $ the_person.change_arousal(10)
    if the_person.love < 0:
        the_person "I can't believe I'm saying this, and with you of all people... but I'm ready! Just... just put it in me! Raw!"
    else:
        the_person "My brain says this is wrong, but my body keeps saying it's so right! Fuck me [the_person.mc_title], I want you to fill me with your cum!"
    $ the_person.break_taboo("condomless_sex")
    $ the_person.break_taboo("vaginal_sex")
    "You run your cock along her slit a couple more times, then start to push it inside, feeling her soft skin, her curves."
    $ play_moan_sound()
    "She moans as you bottom out inside her and start to fuck, your body moving in and out of hers."
    call fuck_person(the_person, start_position = breeding_missionary, start_object = make_bed(), private = True, skip_intro = True, position_locked = True, skip_condom = True) from _VT_breeding_fetish_family_intro_01
    $ VT_add_breeding_fetish(the_person)
    $ the_person.draw_person(position = "missionary")
    if the_person.knows_pregnant:
        the_person "I know I'm already pregnant... but that was so good. Even after this one comes, I want to keep doing this, to keep being your breeding stock, your cumdump."
    else:
        the_person "Oh god, you're right. It feels so right getting seeded by you, being your breeding stock, your cumdump."
    "You slowly roll off of [the_person.title] and lie beside her, feeling your desire, your need to breed her again."
    mc.name "Make sure you lay like this for a while. Keep those swimmers as deep as you can, and maybe we'll make another baby."
    "You get up and start to get dressed, feeling your desire, your need to breed her again."
    the_person "Do you... want to stay with me tonight?"
    mc.name "I can't stay tonight, but from now on, you are my breeding stock, my cumdump. Be ready to take my cum whenever I tell you to, to be bred and made pregnant."
    the_person "Yes! Yes sir! I'll be ready, don't worry! I'll be your breeding stock, your cumdump, your pregnant slut."
    "You say goodbye to [the_person.title], feeling your desire, your need to breed her again."
    "[the_person.possessive_title!c] now has a fetish to get bred by you, to be your breeding stock, your cumdump."
    $ the_person.clear_situational_slut("situation")
    return

#This function to be used for generic non employee, non unique girls
label VT_breeding_fetish_generic_intro_label(the_person): 
    $ the_person.arousal = 40
    "As you walk into [mc.location.formal_name], you notice [the_person.title]. She notices you also and approaches, her eyes locked on yours with a hungry gaze."
    $ the_person.draw_person()
    the_person "Hello [the_person.mc_title]... I've been thinking about you all day. I need to talk to you about something."
    if the_person.tits_visible:
        "You take a moment to look at her. Her cheeks are flushed, and her exposed nipples look hard as diamonds. She is definitely aroused, and it's clear she's been thinking about you in a very naughty way."
    else:
        "You take a moment to look at her. Her cheeks seem flushed... Her nipples are poking against the fabric of her outfit. Is she... Aroused? It's clear she's been thinking about you, and it's not just innocent thoughts."
    mc.name "What's on your mind?"
    the_person "I... I don't know how to say this, but I've been feeling really... fertile lately. I need a man to take care of me, to breed me."
    mc.name "I see. And you think I'm the man for the job?"
    the_person "Yes... I do. I need your cum inside me, to feel your seed taking root. I need to be bred, to be made pregnant."
    $ mc.change_locked_clarity(20)
    "Lately, you've been slipping her the Vitamin D so much, it seems to have increased her drive to reproduce. She's been thinking about you, and it's clear she wants to take things to the next level."
    "It's possible she might be on the verge of developing a fetish. If you go back to her place, you can push her over the edge into having a breeding fetish! The thought of it is making you hard."
    menu:
        "Go to her place" if mc.energy > 40:
            mc.name "Let's go back to your place and take care of that need of yours."
        "Too tired" if mc.energy <= 40:
            pass
            $ VT_fetish_timer_reset(the_person, "breeding", 1)
            $ clear_scene()
            return
        "Not now":
            mc.name "I'm sorry [the_person.title], I've got errands to accomplish. Maybe another time."
            $ the_person.change_stats(happiness = -5, love = -2)
            the_person "Ah, okay. I see. Maybe next time then."
            $ VT_fetish_timer_reset(the_person, "breeding", 2) 
            return False

    "[the_person.title] takes your hand and you step away with her. After a few minutes of walking, you find yourself at her place."
    "She quickly unlocks the front door and pulls you inside, her body pressed against yours."
    $ the_person.learn_home()
    $ mc.change_location(the_person.home)
    $ the_person.draw_person(position = "kissing")
    "She throws her arms around you and you start to make out, your lips locked in a passionate kiss. Your hands drop to her ass and you start to grope her aggressively, feeling her soft skin, her curves."
    the_person "Oh god, I'm so wet. I need you inside me now."
    $ the_person.draw_person(position = "against_wall")
    $ the_person.change_arousal(10) 
    $ mc.change_locked_clarity(30)
    "You pick her up and carry her to her bedroom, her body wrapped around yours. She is grinding against you the whole way, her hips moving in time with yours."
    "You throw her down on the bed and start to undress her, revealing her naked body. She is so wet, so ready for you."
    mc.name "Are you on birth control, [the_person.title]? Because I'm not going to hold back. I'm going to give you everything I've got."
    if the_person.knows_pregnant:
        the_person "Do it! I'm already pregnant, but I want to feel your seed deep inside me, to be bred like the little slut I am."
    else:
        the_person "You know I'm not... and I don't want you to hold back. I want to feel your cum deep inside me, to be bred like the little slut I am."
        mc.name "You're so beautiful, so fertile. I'm going to breed you, flood your womb full of my seed."
        the_person "Yes... please. I need your cum inside me, to feel your seed taking root."
    $ the_person.strip_outfit(position = "missionary")
    $ the_person.change_arousal(10) #60
    $ mc.change_locked_clarity(50)
    if the_person.vagina_available:
        "You pull your cock out and begin to rub it along her inviting slit, feeling her soft skin, her curves."
    else:
        "As you pull your cock out, [the_person.possessive_title] pulls her bottoms off, revealing her body, her curves."
        $ the_person.strip_outfit(exclude_upper = True, position = "missionary")
        "When she finishes you run your cock all along her inviting slit, feeling her soft skin, her curves."
    $ the_person.break_taboo("condomless_sex")
    $ the_person.break_taboo("vaginal_sex")
    "You climb on top of her and start to fuck her, your cock sliding in and out of her wet cunt. She is moaning, her body trembling with pleasure."
    call fuck_person(the_person, start_position = breeding_missionary, start_object = make_bed(), private = True, skip_intro = True, position_locked = True, skip_condom = True) from _VT_breeding_fetish_generic_intro_01
    $ VT_add_breeding_fetish(the_person)
    $ the_person.draw_person(position = "missionary")
    "When you finish, she lays back, just rubbing her hand along her belly, a look of satisfaction on her face."
    if the_person.knows_pregnant:
        the_person "I know I'm already pregnant... but that was so good. Even after this one comes, I want to keep doing this, to keep being your breeding stock, your cumdump."
    else:
        the_person "That was so good... I feel so full, so fertile! I hope I'm pregnant, that I'm going to be a mom."
    "You slowly roll off of [the_person.title] and lie beside her, feeling your desire, your need to breed her again."
    mc.name "Make sure you lay like this for a while. Keep my semen as deep as you can, and maybe we'll make another baby."
    "You get up and start to get dressed, feeling your desire, your need to breed her again."
    the_person "Can we do this again soon? I want to feel your cum deep inside me again, to be bred like the little slut I am."
    mc.name "I plan to. Keep your cunt ready for me, anytime I want to dump my load inside you. You're my breeding stock, my cumdump, and I'll use you whenever I want."
    the_person "Yes! Don't worry, I'll be ready! I'll be your slut, your cumdump, your breeding stock, whenever you want."
    "You say goodbye to [the_person.title], feeling your desire, your need to breed her again."
    "[the_person.possessive_title!c] now has a fetish to get bred by you, to be your breeding stock, your cumdump."
    return
    
label VT_breeding_fetish_mom_intro_label():
    $ the_person = mom
    $ the_person.on_birth_control = False
    $ the_person.event_triggers_dict["Mom_forced_off_bc"] = False
    $ the_person.outfit.strip_to_vagina()
    "You're woken up by your bed shifting under you and a sudden weight around your waist, a warm body pressed against yours."
    "You feel a tug on your clothing, and you are slowly opening your eyes when you feel your morning wood spring free, your cock hard and ready."
    $ the_person.draw_person(position = "cowgirl", emotion = "happy")
    $ mc.change_locked_clarity(50)
    "You open your eyes to see [the_person.possessive_title] lining you up with her pussy, before slowly sliding down on top of you, her body moving in a slow, sensual motion."
    $ the_person.break_taboo("condomless_sex")
    $ the_person.break_taboo("vaginal_sex")
    mc.name "Ooohh... good morning [the_person.title]. You're looking particularly beautiful today."
    the_person "Ohhh... good morning honey! Mommy needs your seed inside her this morning... and I'm not taking no for an answer! I've been dreaming about this all night, about feeling your cum deep inside me."
    "Lately, you've been slipping her the Vitamin D so much, it increased her drive to reproduce. Unsurprisingly, it seems like she has developed a breeding fetish, a desire to be bred and made pregnant by you."
    the_person "I had such vivid dreams last night... you were fucking me and kept cumming inside me over and over and over, filling me up with your seed. My belly started to get bigger and my tits started to leak milk and I loved it so much..."
    "Ahh, you've been fucking her so much, she can't seem to get enough. Looks like you have finally driven her over the edge and given her a breeding fetish, a desire to be your personal mare, your breeding stock."
    $ the_person.change_arousal (30)
    $ mc.change_locked_clarity(50)
    "She starts to rock her hips back and forth, her body moving in a slow, sensual motion. You reach up and start to fondle her tits as they sway back and forth, feeling her soft skin, her curves."
    mc.name "Mmmm, I love your tits, [the_person.title]. I love the way they feel, the way they taste. I'll never get tired of them."
    if the_person.knows_pregnant: #She already knows she's pregnant
        the_person "Oh god I know I'm already pregnant, but I just want you to fuck your cum into me over and over, to fill me up with your seed and make me feel like a real woman."
    else:
        the_person "Oh god, can we really do this? Will you fuck your cum into me over and over until I'm pregnant? I want that so bad, to feel your seed taking root inside me and growing into a new life."
    mc.name "Of course I'll give you my cum. From now on, you'll be my own personal mare, my breeding stock. I'll breed you every chance I get, and you'll love every minute of it."
    $ the_person.change_arousal(15)
    the_person "Oh [the_person.mc_title], that's so hot... I want it now! I'm going to ride the cum out of you now, to feel your seed deep inside me and make me feel like a real woman."
    call get_fucked(the_person, the_goal = "vaginal creampie", start_position = cowgirl, private = True, skip_intro = True, allow_continue = False) from _call_get_fucked_VT_breeding_fetish_mom_intro_01
    if the_person.has_creampie_cum:
        the_person "Oh god... I need to keep it all in, to feel your seed taking root inside me and growing into a new life."
        "[the_person.title] reaches her hand down, trying to keep your cum inside her, but failing, as your cum drips down the inside of her thighs, a sign of your successful breeding."
    else:
        the_person "Oh god! It's so deep! Oh thank you so much [the_person.mc_title]! I feel like a real woman now, like I've been bred and made whole."
        pass
    mc.name "Don't worry, I'll give you more soon. I'll breed you again and again, until you're pregnant and happy."
    "She chuckles, then smiles at you, her eyes shining with happiness and desire."
    the_person "You better... Every day! Even if I am pregnant, I'll still want your cum inside me, to feel your seed taking root and growing into a new life."
    $ VT_add_breeding_fetish(the_person)
    the_person "It's good for the baby, I think! It knows when mommy is getting taken care of, when she's feeling happy and fulfilled. And it makes me feel so good, so alive."
    $ the_person.draw_person(position = "missionary")
    "[the_person.title] lays down beside you for a while, her body pressed against yours, her eyes shining with happiness and desire. Soon though, it is time to get up and ready for the day."
    the_person "Have a good day. Don't forget, try to be home for dinner tonight! You need to keep your energy up, to breed me again and again."
    "You can hardly believe it. Your own mother now has a fetish to get bred by you, to be your personal mare, your breeding stock. And you're happy to oblige, to give her what she wants and needs."
    $ mc.change_locked_clarity(10)
    return #Needs testing

label VT_breeding_fetish_lily_intro_label(lily): 
    $ the_person = lily
    "Note: This scene was written assuming that eventually you fuck [the_person.title] on a live stream, but so far Vren has not written this step."
    $ mc.change_location(the_person.home)
    "You step into [the_person.possessive_title]'s room, and you're immediately hit with the sight of her curves, her body."
    "She is standing next to her mirror playing with her [the_person.hair_description], but looks over at you and smiles when she hears the door."
    $ the_person.draw_person()
    the_person "Oh hey [the_person.mc_title]! I was wondering if you were going to be around tonight. Want to stream with me tonight?"
    "Your sister's job, over the last few months, has slowly evolved. From taking sexy snaps, to streaming sex with you. Having sex with your sister, {i}and{/i} getting paid for it? It's amazing."
    "You think about it. Do you want to do another stream tonight?"
    menu:
        "Hell yeah!" if mc.energy > 60:
            pass
        "Too Tired " if mc.energy <= 60:
            pass
            #TODO re add the event for this person for the next day.
            $ VT_fetish_timer_reset(the_person, "breeding")
            $ clear_scene()
            return
        "Not tonight":
            $ VT_fetish_timer_reset(the_person, "breeding", 2)
            return

    the_person "Great! I'll get it set up..."
    "You notice she hesitates a bit. She bites her lower lip before continuing, her eyes locked on yours with a hungry gaze."
    the_person "So umm, I've been getting some requests recently... for us to take things to the next level."
    mc.name "Oh? What are the thirsty anonymous internet guys wanting?"
    "She chuckles a second, but you sense a nervous tone, a hint of desire in her voice."
    the_person "Well... they've been asking to see us do it raw... for you to cum inside me, to breed me like a little slut."
    if the_person.knows_pregnant:
        "[the_person.title] is already pregnant, so it doesn't necessarily make the act risky, but it's clear she wants to take things to the next level, to be bred and made pregnant again."
        mc.name "You're already pregnant... but is that what they want? To act like you could get pregnant again?"
    else:
        "You knew [the_person.title] wasn't on birth control, and it's clear she wants to take things to the next level, to be bred."
        mc.name "That could be risky. What if you got pregnant? Or is that the point?"
    "Recently, you've been fucking her a lot, possibly triggering her urge to reproduce... you wonder if there's even been any requests, or if she is just using that as an excuse to get what she wants."
    mc.name "Maybe I should message them. Find out more about what they want to see..."
    "She quickly interrupts you, her voice filled with desire, her eyes locked on yours."
    the_person "No! You don't need to do that... I'm sure that's what it is! To watch as I pretend to get knocked up, to be bred like a little slut."
    "She gives a tell-tale sign. As she says that, she looks away from you and to the side, her cheeks flushing with desire. She is lying to you, but it's clear she wants to be bred, to be made pregnant."
    mc.name "That's what they want? Are you sure? Or is that what YOU want?"
    "[the_person.possessive_title!c] begins to blush heavily, her eyes locked on yours with a hungry gaze."
    the_person "Oh me? Want to get knocked up? By my brother? That's... I mean that's CRAZY!... right?"
    $ mc.change_locked_clarity(20)
    "She is struggling to give a reasonable explanation, but it's clear she wants to be bred, to be made pregnant. She wants to feel your cum deep inside her, to be filled with your seed."
    mc.name "Yeah, I mean, wouldn't that be crazy? For a woman to want to get fucked? To have a man dominate her and do what he wants with her, then fill her up with his seed, consequences be damned?"
    $ the_person.change_arousal(10)
    the_person "Well yeah I mean obviously that sounds hot but you're my brother..."
    mc.name "Right, who happens to be a man? Someone you know and trust, someone who can give you what you want, what you need."
    "She sighs, her body language screaming with desire. She resigns herself and opens up, her eyes locked on yours with a hungry gaze."
    the_person "I don't know... The way things between us have progressed... But I just can't stop thinking about it, about being bred, carrying my big bro's babies."
    the_person "My body wants it so bad, for you to pin me down and fuck me anywhere you want, cumming inside me over and over, filling me up with your seed."
    $ mc.change_locked_clarity(50)
    "She pauses for a second, her eyes locked on yours with a hungry gaze..."
    if the_person.knows_pregnant:
        the_person "I know this is crazy... I'm already pregnant!... but I don't want to stop now! I want you to breed me over and over, like your personal breeding slave, your cumdump."
    else:
        the_person "I know this is crazy... I want you to knock me up! And not just once! I want you to breed me over and over, like your personal breeding slave, your cumdump."
    "She seems to have acquired a breeding fetish, a desire to be bred and made pregnant, to be filled with your seed."
    mc.name "Ok... from now on, you are my personal cum dumpster, my breeding stock. I'll use you like you want, whenever I want."
    the_person "Oh god... this is amazing! Let's do it, let's make a baby, or two, or three..."
    "Suddenly she remembers, her eyes lighting up with excitement."
    the_person "Can we... can we do it on stream? No one on there believes we are actually siblings. They think it's all just for show, but I want to show them the truth, I want to show them how much I love being bred, being made pregnant."
    mc.name "Go ahead, set it up. I'll give them a show they'll never forget."
    $ the_person.draw_person(position = "sitting")
    "[the_person.possessive_title!c] walks over to her laptop, her body language screaming with desire. You give her a few minutes to get everything set up."
    the_person "Okay... I promised all the viewers a crazy show! Oh god, I'm so excited, I'm so ready to be bred, to be made pregnant."
    "She stands up, her eyes locked on yours with a hungry gaze."
    $ the_person.draw_person()
    the_person "Just one more thing to do..."
    $ the_person.strip_outfit()
    "[the_person.title] gets naked, and you quickly follow suit, your cock hard and ready to breed her, to make her pregnant."
    mc.name "How do you think we should do this? Do you want to be on top, or do you want me to take control?"
    the_person "I was thinking... you could just lay back and hold the camera. I'll ride you reverse cowgirl, then when you finish you'll be able to uhhh, you know, see it, see your cum dripping out of me."
    $ mc.change_locked_clarity(20)
    mc.name "Mmm... that sounds amazing... for the viewers too, but mostly for me, for my own pleasure."
    "She punches your arm half-heartedly and laughs, her eyes sparkling with desire."
    "You walk over to her bed and lay down on it. After a minute she brings you the camera, her body language screaming with desire."
    "She goes back over to the computer, and after a moment, she gives a countdown, her voice filled with excitement."
    the_person "Okay, we are streaming in 5, 4, 3..."
    "As she goes past three stops counting and instead starts to walk over to you, her eyes locked on yours with a hungry gaze."
    the_person "Hey everyone... just as promised, I have a naughty stream set up tonight, and it's going to be a wild ride, a breeding fest."
    the_person "Tonight is the night. I'm going to fuck my brother and let him cum in my pussy, and I'm going to love every minute of it, every second of it."
    "You can hear a few replies go through on the computer, but from where you are you can't see them. [the_person.title] also hears them, and she smiles, her eyes sparkling with desire."
    the_person "I'm sorry, tonight I won't be able to take requests during. Just sit back and enjoy the show, enjoy the breeding, the making of a new life."
    $ the_person.draw_person(position = "doggy")
    $ mc.change_locked_clarity(50)
    "With that, she turns her back to you and swings one leg over your body, her ass now pointed back at you, her pussy open and ready to be bred."
    "She reaches down and gives your bare cock a few strokes, then points it up at her cunt, her body language screaming with desire."
    $ the_person.increase_vaginal_sex()
    "Her pussy is moist and she easily starts to slide down on it, your bare cock enveloped by her steamy flesh, her body wrapping around yours like a glove."
    $ the_person.break_taboo("condomless_sex")
    $ the_person.break_taboo("vaginal_sex")
    the_person "Oh fuck bro, you fill me up so good, so completely. I love being bred, being made pregnant."
    "She's playing it up for the stream, but you know she is also having fun, fucking her brother, being bred and made pregnant."
    $ the_person.change_arousal(20)
    $ mc.change_locked_clarity(20)
    "You lay back on the bed while [the_person.possessive_title] works your cock in and out of her, her body moving in a slow, sensual motion, her pussy milking your cock for all it's worth."
    "[the_person.possessive_title!c] gives you a few quick, shallow dips then pull off you almost completely, leaving just your tip inside her, teasing you, teasing the viewers."
    "She swirls her hips a couple times then impales herself on your again, her body wrapping around yours like a glove, her pussy milking your cock for all it's worth."
    $ the_person.change_arousal(30)
    $ mc.change_arousal(30)
    "She is putting on an incredible show for the camera, for the viewers, but mostly for you, for your own pleasure. Her skill at working dick is extraordinary, her body made for breeding, for being made pregnant."
    the_person "Oh god bro, I'm so full! I want you to cum inside me, to breed me, to make me pregnant!"
    "Her dirty words are matched by her actions as she works your cock aggressively, her body moving in a slow, sensual motion, her pussy milking your cock for all it's worth."
    mc.name "Do it sis, your ass is amazing, your pussy is incredible. I love being inside you, I love breeding you, making you pregnant."
    "You play along for the stream, but you know you're not just playing, you're living your fantasy, your desire to breed your sister, to make her pregnant."
    $ the_person.change_arousal(30)
    $ mc.change_locked_clarity(20)
    "[the_person.possessive_title!c] wiggles back and forth a few more times, then looks back at you and smiles, her eyes sparkling with desire."
    the_person "Do you like that, bro? Ah! That is so good, so amazing. I love being bred by my big bro."
    "[the_person.possessive_title!c] reaches back between her legs and cups your balls, her body language screaming with desire."
    the_person "Mmm, you feel so full... I want you to fill me up, to breed me, to make me pregnant. I want to feel your cum deep inside me, to know that I'm being made pregnant."
    $ the_person.change_arousal(30)
    $ mc.change_locked_clarity(20)
    "Her dirty talking is having its desired effect, and the taboo of doing this while anyone in the world can watch is just too much, too exciting, too arousing."
    "[the_person.possessive_title!c]'s sweet cunt milks your cock, the wet friction pushes you past the point of no return, and you start to cum, to breed her, to make her pregnant."
    mc.name "Ah, I'm going to cum, sis! I'm going to breed you, to make you pregnant!"
    the_person "Oh god me too! Oh fuck bro I'm cumming! Fill me up, breed me, make me pregnant!"
    "She slams her hips down, as deep as your cock can go, and you start to cum, to breed her, to make her pregnant, your seed filling her up, making her whole."
    $ the_person.have_orgasm()
    "Her hole is quivering as she cums at the same time, milking your cock for every last drop of seed, every last drop of cum."
    $ the_person.cum_in_vagina()
    $ the_person.draw_person(position = "doggy")
    $ ClimaxController.manual_clarity_release(climax_type = "pussy", person = the_person)
    "Eventually the twitching stops, for both of you. You did it, you bred your sister, you made her pregnant, and it was amazing, incredible, life-changing."
    "When she slowly pulls off you, your seed immediately begins to leak out of her and down her legs, a sign of your successful breeding, a sign of your love, your desire for each other."
    $ mc.reset_arousal()
    $ the_person.reset_arousal()
    the_person "Oh god... I wonder if I got pregnant... I hope I did, I hope I'm going to be a mom, a mom to your child, your seed."
    "[the_person.possessive_title!c] slowly recovers and gets up, her body language screaming with desire, her eyes sparkling with excitement."
    $ the_person.draw_person(position = "sitting")
    the_person "Well... I hope everyone enjoyed watching my brother try and knock me up... I know I enjoyed it, I loved every minute of it, every second of it."
    the_person "Time for the stream to end! Goodbye everyone, goodbye, and thank you for watching us, for watching us breed, for watching us make a new life."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.title] walks over to the computer, ending the live stream, her body language screaming with desire, her eyes sparkling with excitement."
    $ the_person.draw_person()
    the_person "Well... I think that went well, don't you, bro? I think we made a great team, a great breeding team."
    mc.name "Me too, sis... want to have another round?"
    the_person "Oh god... my body says yes... but I think I need to rest, I need to recover from that amazing breeding session."
    "She bites her lip as she looks down at you, her eyes sparkling with desire, her body language screaming with need."
    the_person "I meant it earlier though... I want you to breed me, to make me pregnant, anytime, anywhere. I want to be your cumdump, your breeding stock, your slut."
    mc.name "Don't worry, sis, I'll give you more soon. I'll breed you again and again, until you're pregnant, until you're a mom, a mom to my child, my seed."
    "She chuckles, then smiles at you, her eyes sparkling with desire, her body language screaming with need."
    the_person "You better... Every day! Even if I am pregnant, I'll still want your cum inside me, I'll still want to be bred, to be made pregnant again and again."
    $ VT_add_breeding_fetish(the_person)
    "You quietly get up and get dressed, your mind reeling with the implications of what just happened, of what you just did, of what you just bred."
    "You can hardly believe it. Your own sister now has a fetish to get bred by you, to be your cumdump, your breeding stock, your slut."
    return

label VT_breeding_fetish_rebecca_intro_label(aunt): #NEeds testing, evening room entry event
    $ the_person = aunt
    "You step into [the_person.possessive_title]'s room, and you're immediately struck by the sight of her curves, her body. She's sitting at her desk, surrounded by books and papers, but her eyes are fixed on you, and you can see the desire burning in them."
    $ the_person.draw_person()
    the_person "Ah, [the_person.mc_title]... welcome to my study session. I've been thinking about you all day."
    "She's trying to sound casual, but you can hear the huskiness in her voice, the underlying tone of desire. She's been wanting you for a long time, and it's clear that she's not going to hide it anymore."
    mc.name "Hey, [the_person.title]. What's with the books? You're really getting into your studies, huh?"
    the_person "Oh, yeah... I'm just trying to get ahead, you know? But it's hard to focus when all I can think about is you."
    "She looks at you, her eyes locked on yours, and you can see the hunger in them. She's not just talking about her studies, she's talking about her desire for you."
    mc.name "[the_person.title], I... I don't know what to say. This is all so... sudden."
    the_person "Don't say anything, [the_person.mc_title]. Just come to me. Let's forget about the books, forget about everything else. Let's just be together."
    "She gets up from her chair, her body moving towards you with a slow, sensual motion. You can see the curves of her body, the way her clothes hug her in all the right places."
    $ the_person.draw_person(position = "kissing")
    "You kiss her, the passion igniting between you like a wildfire. You feel like you're losing yourself in her, in the desire that's been building between you for so long."
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(30)
    "You start to undress her, the clothes falling away from her body like a revelation. You see the curves of her breasts, the softness of her skin, and you know that you're in heaven."
    $ the_person.strip_outfit()
    "[the_person.title] is naked, her body glowing in the dim light of the room. She's like a goddess, a creature of beauty and desire."
    mc.name "[the_person.title], you're so... beautiful. So sexy."
    the_person "Take me, [the_person.mc_title]. Take me and make me yours."
    $ the_person.draw_person(position = "missionary")
    "You take her, the passion igniting between you like a wildfire. You feel like you're losing yourself in her, in the desire that's been building between you for so long."
    call fuck_person(the_person, start_position = breeding_missionary, start_object = make_bed(), private = True, skip_intro = True, position_locked = True, skip_condom = True) from _call_fuck_person_VT_breeding_fetish_rebecca_intro_01
    $ VT_add_breeding_fetish(the_person)
    "When you finish, [the_person.title] is lying beneath you, her body glowing with a soft, ethereal light. She's like a goddess, a creature of beauty and desire."
    the_person "Ah, [the_person.mc_title]... that was... incredible. I feel like I've been transformed, like I've been reborn."
    mc.name "[the_person.title], you're so... beautiful. So sexy."
    the_person "I know, [the_person.mc_title]. I feel it too. I feel like I've found my true self, my true passion."
    "You look at her, and you see a sexy [the_person.title], a creature of beauty and desire. You know that you'll never forget this moment, this feeling of passion and desire."
    return

label VT_breeding_fetish_gabrielle_intro_label(): #NEeds testing, evening room entry event
    $ the_person = cousin
    "You step into [the_person.possessive_title]'s room, and you're immediately enveloped in the dark, moody atmosphere. The walls are adorned with Gothic-inspired artwork, and the air is thick with the scent of incense."
    $ the_person.draw_person()
    the_person "Ah, [the_person.mc_title]... welcome to my lair. I've been expecting you."
    "She's sitting on her bed, surrounded by candles and listening to a hauntingly beautiful Gothic melody. Her eyes are closed, and her body is swaying gently to the music."
    mc.name "Hey, cuz. What's with the music? It's pretty intense."
    the_person "Oh, it's just my favorite band, Lacuna Coil. Their music speaks to my soul."
    "She opens her eyes and looks at you, her gaze piercing and intense."
    the_person "I've been feeling really... restless lately. Like there's something inside me, waiting to be unleashed."
    mc.name "Unleashed? What do you mean?"
    the_person "I don't know... it's just this feeling of... hunger. Like I need something more, something deeper."
    "She pauses, her eyes locked on yours."
    the_person "I think I need you, [the_person.mc_title]. I need you to fill me up, to make me whole."
    $ mc.change_locked_clarity(20)
    "You can feel the tension in the air, the electricity between you and your cousin. It's like the music is fueling your desire, your need for each other."
    mc.name "Cuz, I... I don't know what to say. This is all so... intense."
    the_person "Don't say anything, [the_person.mc_title]. Just come to me. Let's let the music take us away."
    "She reaches out and takes your hand, pulling you towards her. You feel like you're being drawn into a dark, Gothic world, a world of passion and desire."
    $ the_person.draw_person(position = "kissing")
    "You kiss her, the music swirling around you like a vortex. You feel like you're losing yourself in her, in the darkness and the passion."
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(30)
    "You start to undress her, the music building to a crescendo. You feel like you're unleashing a wild animal, a creature of passion and desire."
    $ the_person.strip_outfit()
    "[the_person.title] is naked, her body glowing in the candlelight. She's like a Gothic goddess, a creature of darkness and beauty."
    mc.name "Cuz, you're so... beautiful. So wild and free."
    the_person "Take me, [the_person.mc_title]. Take me and make me yours."
    $ the_person.draw_person(position = "missionary")
    "You take her, the music swirling around you like a vortex. You feel like you're losing yourself in her, in the darkness and the passion."
    $ the_person.break_taboo("condomless_sex")
    $ the_person.break_taboo("vaginal_sex")
    call fuck_person(the_person, start_position = breeding_missionary, start_object = make_bed(), private = True, skip_intro = True, position_locked = True, skip_condom = True) from _call_fuck_person_VT_breeding_fetish_gabrielle_intro_01
    $ VT_add_breeding_fetish(the_person)
    "When you finish, [the_person.title] is lying beneath you, her body glowing with a soft, ethereal light. She's like a Gothic angel, a creature of beauty and desire."
    the_person "Ah, [the_person.mc_title]... that was... incredible. I feel like I've been transformed, like I've been reborn."
    mc.name "Cuz, you're so... beautiful. So wild and free."
    the_person "I know, [the_person.mc_title]. I feel it too. I feel like I've found my true self, my true passion."
    "You look at her, and you see a Gothic goddess, a creature of darkness and beauty. You know that you'll never forget this moment, this feeling of passion and desire."
    return

label VT_breeding_fetish_stephanie_intro_label():  #Needs Testing
    $ the_person = stephanie
    if stephanie.fetish_count == 0:
        call VT_fetish_stephanie_first_fetish_label(the_person) from __VT_breeding_fetish_stephanie_intro_bimbo_choice_01
        if the_person.personality == bimbo_personality:
            call VT_breeding_fetish_stephanie_bimbo_label(the_person) from _VT_breeding_fetish_stephanie_intro_bimbo_01
        else:
            call VT_breeding_fetish_stephanie_normal_label(the_person) from _VT_breeding_fetish_stephanie_intro_normal_01
    else:
        if the_person.personality == bimbo_personality:
            $ mc.start_text_convo(the_person)
            the_person "Heyyyyyyy [the_person.mc_title]! I need your cock so bad! Meet in your office?"
            mc.name "Sure, I'll meet you there. I'll give you what you need."
            $ mc.change_locked_clarity(20)
            $ mc.end_text_convo()
            $ mc.change_location(ceo_office)
            $ scene_manager = Scene()
            $ scene_manager.add_actor(the_person)
            the_person "Oh hey! You're here! I'm so ready for you!"
            mc.name "Of course. Can you lock the door? We don't want anyone to disturb us."
            the_person "Oh! Right right right... I don't want anyone to see us, to see what we're doing."
            "[the_person.possessive_title!c] turns and locks your office door, her body language screaming with desire."
            the_person "So... I saw this crazy video last night, and I thought maybe we could re-create it! It was so hot, so sexy!"
            mc.name "Oh yeah? What was it about? Tell me more."
            the_person "Basically, this guy with a monster cock bent his secretary over his desk and fucked her over and over until she was knocked up and full of cum! It was so amazing, so incredible!"
            the_person "I was dreaming about it all night. Can we do it please please please pleeeeeaaaassseee??? I want to feel your cum deep inside me, to be bred like a little slut."
            "Sounds like [the_person.title] has started to develop a breeding fetish from all the fuckery. You suppose you should indulge her with this as well, give her what she wants, what she needs."
            mc.name "Sounds good. Get over here, bend over my desk. I'll give you what you want, what you need."
            the_person "Oh! Yes sir. What are you going to do to me? Are you going to breed me, to make me pregnant?"
            call VT_breeding_fetish_stephanie_bimbo_label(the_person) from _VT_breeding_fetish_stephanie_intro_bimbo_02
        else:
            if mc.location == mc.business.r_div: #Already in research
                "Suddenly, [the_person.possessive_title] looks up from her work and speaks up, her voice filled with desire."
                the_person "Hey [the_person.mc_title], I need to talk to you about something. Can we go somewhere private? I don't want anyone to hear us, to know what we're doing."
                mc.name "Sure, follow me to my office. We can talk there, in private."
            else:
                $ mc.start_text_convo(the_person)
                the_person "Hey [the_person.mc_title], I need to talk to you about something. Can we meet somewhere private? I have something important to tell you, something I want to share with you."
                mc.name "Sure, meet me in my office. We can talk there, in private."
                $ mc.end_text_convo()

            $ mc.change_location(ceo_office)
            $ scene_manager = Scene()
            $ scene_manager.add_actor(the_person)
            "You walk with [the_person.possessive_title]. When you get there, she locks the door, her body language screaming with desire. You sit down at your desk, and she sits down across from you, her eyes locked on yours."
            mc.name "What can I do for you [the_person.title]? What's on your mind?"
            the_person "Well, recently I've started having a new set of... well... breeding fantasies. I just can't stop thinking about it, about being bred, about being made pregnant."
            the_person "I just wanted to make sure that we still have an understanding, right? That you'll still give me what I need, what I want."
            mc.name "Certainly. I'll always be here to help you with your needs, to give you what you want, what you need. You're my slut, my breeding stock, and I'll use you whenever I want."
            call breeding_fetish_stephanie_normal_label(the_person) from _VT_breeding_fetish_stephanie_intro_normal_02

    $ clear_scene()
    $ scene_manager.clear_scene()
    $ the_person.apply_planned_outfit()
    return #Needs testing

label VT_breeding_fetish_stephanie_bimbo_label(the_person):
    "You begin to walk towards her, and she looks up at you with a bubbly smile."
    mc.name "That's right. You were going to bend over my desk for a minute, and if everything goes well, I have a special surprise for you, a present that will make you scream with pleasure."
    the_person "Oh my god, like, I'm so excited! I love presents, especially the ones that make me feel like a dirty little slut. I wonder what it could be, what kind of naughty thing you have in store for me."
    $ scene_manager.update_actor(the_person, position = "standing_doggy")
    $ mc.change_locked_clarity(50)
    "[the_person.possessive_title!c] turns around and bends over, her ass wiggling back and forth in front of you like a tantalizing treat. Your hands immediately get to work, stripping her down to her bare essentials."
    $ scene_manager.strip_to_vagina(person = the_person)
    "She moans with pleasure as you expose her, her body trembling with anticipation. You can see the desire in her eyes, the need to be bred, vulnerable to your cock."
    the_person "Stick it in [the_person.mc_title]! I want to earn my special present, I want to feel your cum deep inside me, to be bred like a little slut."
    $ the_person.break_taboo("condomless_sex")
    $ the_person.break_taboo("vaginal_sex")
    "Without any hesitation, you slide your cock into her cunt, feeling her warm, wet flesh envelop you like a glove. She's so tight, so ready to be bred, vulnerable to your seed."
    call fuck_person(the_person, start_position = bent_over_breeding, start_object = make_desk(), skip_intro = True, position_locked = True, skip_condom = True) from _call_VT_breeding_fetish_stephanie_bimbo_01
    $ VT_add_breeding_fetish(the_person)
    the_person "Oh my god, like, that was so amazing! I can feel your cum deep inside me, your seed taking root. It's like I'm being reborn, like I'm becoming a new person."
    $ scene_manager.update_actor(the_person, position = "stand2")
    the_person "Mmm, thanks for that mister! I know this is kinda crazy, but... I'm totally getting the urge for another round. Normally one time is enough, but with you, I just can't get enough, I need more, I need to be bred again and again."
    mc.name "I'm sorry, you'll have to be patient if you want another round. But don't worry, I'll give you what you need, what you want. You're my slut, my breeding stock, and I'll use you whenever I want."
    the_person "Ah... I see. Well, in that case, I'll just have to wait, to anticipate the next time we can be together, the next time you can breed me, make me pregnant."
    the_person "Fine! I'll just go back to... whatever it was I was doing. But don't think you've seen the last of me, mister. I'll be back, and next time, I won't be so easy to get rid of."
    mc.name "It doesn't matter, you can take the rest of the day off. But don't think you're off the hook that easily. I'll be calling you again soon, and next time, you'll be ready, you'll be eager to be bred, to be made pregnant."
    the_person "Oh? That eager to get rid of me? Guess I'll just go find someone else to play with for a while. But don't worry, mister, I'll be back, and next time, I'll be ready, I'll be eager to be bred, to be made pregnant."
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "You say goodbye, and [the_person.possessive_title] turns and walks out of your office, your seed dribbling down her leg like a badge of honor. She's a dirty little slut, and she knows it, and she loves it."
    return

label VT_breeding_fetish_stephanie_normal_label(the_person):
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person, position = "stand4")
    "[the_person.possessive_title!c] rises from her seat, a sultry smile spreading across her face as she gazes at you with an unmistakable hunger in her eyes."
    if not the_person.vagina_available:
        "With a flirtatious flick of her wrist, she begins to strip down, her clothes falling away to reveal the soft, inviting curves of her body."
        $ scene_manager.strip_to_vagina(person = the_person)
    "Her eyes never leave yours as she strikes a pose, her hips cocked to one side in a tantalizing invitation."
    the_person "Well? Why are you still dressed? You promised to help me, and I'm not going anywhere until you do."
    # call fuck_person(the_person, start_position = anal_cowgirl, start_object = make_desk(), girl_in_charge = True, position_locked = True) from _call_sex_description_SBA093
    $ the_person.break_taboo("condomless_sex")
    $ the_person.break_taboo("vaginal_sex")
    call get_fucked(the_person, the_goal = "vaginal creampie", start_position = cowgirl, start_object = make_desk(), allow_continue = False) from _call_get_fucked_VT_breeding_fetish_stephanie_normal_cowgirl_01
    $ VT_add_breeding_fetish(the_person)
    the_person "Mmm... Oh god, it's even better than I fantasized about last night. Your cum feels so warm and delicious inside me."
    "[the_person.possessive_title!c] takes a moment to catch her breath, her chest heaving with pleasure, before she stands up and rubs her belly with a satisfied smile."
    $ scene_manager.update_actor(the_person, position = "stand2")
    the_person "You know, the serums don't just increase fertility... they also amplify libido. I can already feel it coursing through my veins, making me want to fuck you all over again."
    mc.name "Don't worry, I'll be here to take care of you whenever the urge strikes. Just come find me, and I'll bend you over wherever we are – even right here in the lab."
    the_person "Mmm... that sounds like a promise I can get behind. Or in front of. Or on top of..."
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "With a flirtatious wink, [the_person.possessive_title] turns and walks out of your office, the evidence of your encounter trickling down the inside of her thighs."
    "It looks like [the_person.title] has developed a breeding fetish, and you can't wait to see where this new desire takes her – and you."
    return

label VT_breeding_fetish_emily_intro_label():
    "Emily doesn't have a breeding fetish written yet"
    return

label VT_breeding_fetish_christina_intro_label():
    "Christina doesn't have a breeding fetish written yet"
    return

label VT_breeding_fetish_alex_intro_label():
    "Alexia doesn't have a breeding fetish written yet"
    return

label VT_breeding_fetish_nora_intro_label():
    "Nora doesn't have a breeding fetish written yet"
    return

label VT_breeding_fetish_starbuck_intro_label(): 
    $ the_person = starbuck
    $ mc.start_text_convo(the_person)
    the_person "Hey, I need a favor. Can you swing by the shop tonight and help me close up? I've got a few things I need to take care of."
    "You consider it for a moment before agreeing. You don't have anything else going on, and it's always nice to spend time with [the_person.title]."
    mc.name "Sure thing, I'll be right over."
    $ mc.end_text_convo()
    "You make your way to the sex shop, wondering what [the_person.title] needs help with."
    $ mc.change_location(sex_store)
    $ the_person.draw_person()
    "When you arrive, you're greeted by [the_person.title]'s warm smile. The shop is already spotless, but she seems to be lingering, waiting for you to arrive."
    mc.name "Hey [the_person.title], everything looks great in here. What do you need help with?"
    the_person "Oh, just a few things. But first, let's grab a drink and catch up. I've got a beer in the fridge with your name on it."
    "She locks the front door and heads to the back, returning with two cold beers. You sit down together, making small talk as you sip your drinks."
    the_person "So, I had an interesting customer come in today. A young couple, looking for some new lingerie. The woman was... quite pregnant, to say the least."
    if the_person.knows_pregnant:
        the_person "I know I'm already pregnant, but seeing them together... it was just so hot. It made me realize how amazing it feels to be bred, to have a man's cum inside me."
    else:
        the_person "There was something about them, though. They were glowing, and the way they looked at each other... it was like they were in their own little world. I couldn't help but feel a pang of jealousy."
        the_person "I've never felt this way before, but it's like I've got an itch I just can't scratch. I've been daydreaming all day about... you know, being like that. Being bred, feeling a man's cum inside me."
    if the_person.is_girlfriend:
        the_person "I know our relationship is a little unconventional, but I've never been more sure of anything in my life. I want you to be my bull, to cum inside me over and over again."
    else:
        the_person "I know it's a little weird, given our age difference, but I just can't shake this feeling. I want you to be my bull, to breed me like it's your job."
    the_person "I want to feel your seed inside me every second of every day. I want to be your little cum dumpster, your breeding slut."
    $ mc.change_locked_clarity(30)
    "Your cock is already hard, listening to [the_person.title] talk like this. You can tell she's been thinking about this a lot, and it's clear she's not going to take no for an answer."
    mc.name "Okay, I'll give you what you want. But first, turn around and bend over the counter. I want to take you from behind."
    $ the_person.change_arousal(8)
    the_person "Oh god, yes! Please, fuck me hard and cum deep inside me!"
    $ the_person.draw_person(position = "standing_doggy")
    "She turns around and bends over the counter, her ass wiggling back and forth as she waits for you to take her."
    if the_person.vagina_available:
        "You step up behind her, your cock springing free as you prepare to take her. You give her ass a few smacks with your cock, just to get her ready."
    else:
        "As you start to pull your cock out, [the_person.title] reaches back and starts to pull off her pants. You give her ass a few smacks with your cock, just to get her ready."
        $ the_person.strip_outfit(exclude_upper = True, position = "standing_doggy")
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(50)
    "She gasps as you push into her, your cock filling her cunt to the brim. You start to fuck her hard, pounding into her as she begs for more."
    $ the_person.break_taboo("condomless_sex")
    $ the_person.break_taboo("vaginal_sex")
    call fuck_person(the_person, start_position = bent_over_breeding, start_object = make_counter(), private = True, skip_intro = True, position_locked = True, skip_condom = True) from _VT_breeding_fetish_starbuck_intro_01
    if the_person.has_creampie_cum:
        the_person "Oh god, baby making sex is so hot! I can feel your cum dripping down my thighs, and I just can't get enough!"
        "[the_person.title] reaches back, trying to keep your cum inside her, but it's no use. Your cum drips down her thighs, a sticky reminder of what you've just done."
        if the_person.knows_pregnant:
            the_person "I don't care if I'm already pregnant, please do that again! My body was made to take your cum like that!"
        else:
            the_person "I hope that did it, but you'd better cum inside me again and again anyway! I want to be your little breeding slut, your cum dumpster!"
    else:
        the_person "Please, [the_person.mc_title], next time, fill my little pussy with all that cum. I want to feel your seed inside me, and I want it to stay there."
        mc.name "If you like it that much, I'll give you everything I've got, next time. You can count on it."
        "She smiles, a sparkle in her eye. You can tell she's already thinking about the next time you'll breed her."
    $ VT_add_breeding_fetish(the_person)
    $ the_person.draw_person()
    "[the_person.title] slowly stands up, turning to face you with a satisfied smile on her face."
    the_person "Wow, I'm glad I finished closing up before you got here. I don't think I could have handled any customers after that."
    $ the_person.draw_person(position = "kissing")
    "She draws you into a hug, whispering in your ear."
    the_person "You can bend me over like that anytime, [the_person.mc_title]. I don't even care if there are customers here when you do it. I just want to be your little breeding slut, your cum dumpster."
    $ the_person.draw_person()
    the_person "You go ahead, I've got a few more things to take care of before I go. But don't worry, I'll be thinking about you, and what you did to me."
    "You say goodbye to [the_person.title], still trying to wrap your head around what just happened. The sex store owner [the_person.title] now has a fetish to get bred by you, and you can't wait to see where this new development takes you."
    return


label VT_breeding_fetish_sarah_intro_label():
    $ the_person = sarah
    $ mc.change_location(bedroom)
    $ scene_manager = Scene()
    $ mc.start_text_convo(the_person)
    the_person "Hey, can I come over tonight? I've got something on my mind that I want to talk to you about."
    mc.name "Of course, baby. Want to spend the night?"
    the_person "Hell yeah! I'll bring some stuff over. Can't wait to see you!"
    "About 20 minutes later, she texts you again."
    the_person "Hey, I'm here! Come let me in, I'm dying to see you!"
    $ mc.end_text_convo()
    "You head to your front door and open it, revealing [the_person.title] standing there with a sultry smile on her face."
    "For once, you manage to get her back to your room without running into [mom.possessive_title] or [lily.title]."
    $ scene_manager.add_actor(the_person, position = "sitting")
    "She walks over and sits on your bed, her eyes locked on yours with a hungry intensity."
    mc.name "So... what's on your mind, baby?"
    "She clears her throat, a hint of nervousness in her voice."
    if the_person.knows_pregnant:
        the_person "I know I'm already pregnant... and it's amazing, really. But every time you finish inside me, I find myself craving it more and more."
        the_person "The itch is getting so bad! I just want you to fill me up, over and over, and never stop."
        the_person "Even after the baby comes... I want your seed planted deep in me as much as possible. I want to be your breeding mare, your cum dumpster."
        "This is quite a twist! You realize that you've probably been giving her pregnancy urges due to all the cum you've been pumping into her."
        mc.name "I'll do it, baby. From now on, you're my personal mare. I'll breed you over and over, just like you want."
    else:
        the_person "Well, this is kind of hard to talk about... but we've been having a lot of unprotected sex lately, and I've been thinking..."
        mc.name "Oh my god, are you pregnant?"
        the_person "No! No, not yet... that I know of, anyway..."
        mc.name "Not... yet?"
        the_person "Well, [the_person.mc_title], it's been like a dream having you back in my life like this. Things are amazing, being with you."
        the_person "I've been tracking my cycles recently, and... well, basically, I'm fertile right now."
        "You can feel your cock twitch in your pants as you imagine [the_person.possessive_title] knocked up, her tits swelling with milk and her belly growing..."
        the_person "Every time you finish inside me, I find myself thinking about it more and more... what it would be like to get pregnant and have a baby with you."
        the_person "Look, you don't have to answer me right now, but... I thought maybe we could try and have a baby. Together?"
        the_person "I know this is crazy... but lately, I've just had this almost overwhelming itch! I want you to knock me up and fill me over and over!"
        "This is quite a twist! You realize that you've probably been giving her pregnancy urges due to all the cum you've been pumping into her."
        mc.name "Honestly, I didn't realize this was something you were thinking about... but I would love to make a baby with you, baby."
    $ the_person.change_stats(happiness = 15, obedience = 10)
    $ mc.change_locked_clarity(50)
    the_person "Oh! Wow, I honestly... I thought you were gonna say no! This is... I don't know what to say."
    "She looks up at you, her facial expression changing from surprise to happiness to sultry desire."
    the_person "So... umm... what are you doing right now?"
    mc.name "I think we should get naked, don't you?"
    the_person "Yes, sir! I'm all yours."
    $ scene_manager.strip_full_outfit(person = the_person)
    $ mc.change_locked_clarity(50)
    "You get naked with [the_person.possessive_title], and she rolls onto her back, spreading her legs wide open for you."
    the_person "Come fill me up, [the_person.mc_title]! Make me your breeding mare!"
    call fuck_person(the_person, start_position = breeding_missionary, start_object = bedroom.get_object_with_name("bed"), skip_intro = False, girl_in_charge = False, position_locked = True, skip_condom = True) from _VT_breeding_fetish_sarah_intro_05
    if the_person.has_creampie_cum:
        the_person "Oh my god... we actually did it... I can feel your cum dripping down my thighs."
        "She grabs an extra pillow and puts it under her butt, elevating her hips to keep your seed deep inside her."
        the_person "I'm just going to lay here like this for a bit... keep that seed nice and deep."
    else:
        mc.name "I'm sorry, baby... I really want to, I'm just really tired."
        "You can tell she's a little disappointed, but she smiles and snuggles up close to you."
        the_person "That's okay... maybe in the morning?"
    "You snuggle up with [the_person.possessive_title], feeling a sense of pride and ownership over your new breeding mare."
    $ VT_add_breeding_fetish(the_person)
    call Sarah_spend_the_night() from VT_breeding_fetish_sarah_intro_overnight_15

    return 

label VT_breeding_fetish_ophelia_intro_label():
    "Ophelia doesn't have a breeding fetish written yet"
    return

label VT_breeding_fetish_erica_intro_label():
    $ the_person = erica
    $ the_person.fertility_percent = 20.0
    $ mc.start_text_convo(the_person)
    if the_person.is_girlfriend:
        the_person "Hey, baby! Can you come over tonight? It's supposed to be cold out, and I could use some company... plus, I want to talk to you about something."
    else:
        the_person "Hey... can you come over tonight? I need to talk to you about something."
    "You don't have anything else going on, so you agree to head over."
    mc.name "Sure, I'm on my way."
    $ mc.end_text_convo()
    $ mc.change_location(the_person.home)
    "You arrive at [the_person.possessive_title]'s place and knock on the door. She answers, looking a bit nervous."
    $ the_person.draw_person()
    the_person "Hi! Come in..."
    "You follow her inside, and she motions for you to sit down at the table."
    the_person "Can I get you anything? Coffee, maybe?"
    mc.name "Am I going to need the caffeine?"
    "You ask, flirting shamelessly. She gives you a shy smile."
    the_person "Hopefully! I'm hoping this will be a long and... productive night."
    mc.name "Coffee sounds great, then."
    "You can already smell the coffee brewing, so she must have had a pot ready."
    $ the_person.draw_person(position = "back_peek")
    "[the_person.possessive_title!c] turns to the counter and grabs a couple of cups. She pours two, then turns and sits down across from you, setting your cup in front of you."
    $ the_person.draw_person(position = "sitting")
    "[the_person.title] looks nervous, fidgeting with her hands. Whatever it is she wants to talk about, it's clearly making her anxious."
    mc.name "So... what's on your mind? Besides me, later, that is."
    "She gives a nervous sigh and opens her purse, pulling out a package of birth control pills and a package of Plan B."
    the_person "Okay... so... I've been thinking about something. A while back, I had to get my IUD removed due to a medical complication, and I switched to regular birth control."
    mc.name "I hope you're okay?"
    the_person "Yeah, I'm fine... but I stopped taking the pills lately. I told myself it was just for the thrill of the risk, but if anything ever actually happened, I had Plan B ready, and if that didn't work... well, I was prepared to take care of it."
    the_person "But the thing is... I love running track and field. And if I ever got pregnant... I know they can't kick me off the team, but the coach is a real bitch. Last time a girl got knocked up, they kicked her off for 'scholastic misconduct' to get around the law."
    the_person "I didn't want that to be me, so I did what I had to... but lately, when I'm with you... and even when I'm not... I just can't stop fantasizing about you cumming inside me. Over and over, not letting me take my pills and knocking me up!"
    "It's clear that all the cumming inside her have taken hold of her and given her serious breeding fetish urges."
    the_person "I knew that girls my age could get baby fever... but I never imagined the urge would be so strong! [the_person.mc_title]... I don't care about the track team anymore! Please knock me up! Will you please?"
    "There's a desperate edge to her voice. [the_person.possessive_title!c] is willing to give up her sports team just to have your babies. This is a no-brainer."
    "You reach over the table and pick up her birth control. You stand up, take it to the trash can, and throw it away. She watches your every move, her eyes wide with excitement."
    the_person "You just... does that mean?"
    mc.name "Lie down on the table, [erica.fname]."
    the_person "Oh! Oh my god..."
    $ the_person.draw_person(position = "missionary")
    if the_person.vagina_available:
        "You reach down and pull your cock out of your pants, ready to give her the creampie she's been begging for."
    else:
        "As you start to pull your cock out, [the_person.possessive_title] reaches down and starts pulling her bottoms off."
        $ the_person.strip_to_vagina(prefer_half_off = True, position = "missionary")
    "You grab her hands and force them down at her sides. She looks up at you with a mixture of excitement and nervousness as your bare cock nears her cunt."
    "You don't say a word, you just push forward, sliding yourself into her fertile young pussy."
    $ the_person.change_arousal (20)
    $ mc.change_locked_clarity(50)
    $ the_person.break_taboo("condomless_sex")
    $ the_person.break_taboo("vaginal_sex")
    the_person "Oh god! Yes! Make me cum and fill me up [the_person.mc_title]!"
    "Still holding her hands down, you start to thrust rapidly. It's time to give this horny slut a creampie!"
    call fuck_person(the_person, start_position = breeding_missionary, start_object = make_table(), private = True, skip_intro = True, position_locked = True, skip_condom = True) from _VT_breeding_fetish_erica_intro_01
    $ the_person.draw_person(position = "missionary")
    if the_person.has_creampie_cum:
        $ become_pregnant(the_person, breeder_announce = True)
        the_person "Oh god! It's amazing. I think you did it. I don't know how I know... I can just feel it."
        "She rubs her belly happily, a satisfied smile on her face."
        the_person "I mean... I'll take a test in a few days to be sure, but..."
    else:
        the_person "That's... you didn't finish?"
        mc.name "I'm sorry [the_person.title]. It's been a long day, and I'm just too tired."
        the_person "Seriously? After all our training and everything..."
        $ the_person.change_love(-5)
        the_person "I think you should go."
        mc.name "I'm sorry, we can try again..."
        the_person "Damn right we'll try again! But tonight, I just need to be mad. Now get out!"
        $ clear_scene()
        "You quickly vacate [the_person.possessive_title]'s apartment and head home."
        $ mc.business.add_mandatory_morning_crisis(
            Fetish_Action("Erica surprises you", VT_breeding_fetish_erica_unsuccessful_followup_requirement, "VT_breeding_fetish_erica_unsuccessful_followup_label", fetish_type = "breeding")
        )
        return
    $ VT_add_breeding_fetish(the_person)
    "[the_person.possessive_title!c] is positively glowing. She seems pretty confident that did the trick."
    the_person "I'm sorry to say this, but I have to get up early in the morning."
    mc.name "It's okay, get some rest."
    $ the_person.draw_person(position = "stand3")
    "[the_person.title] stands up and smiles at you, her eyes sparkling with excitement."
    the_person "I'll let you know when I find out for sure... daddy!"
    "You say goodnight and head home, looking forward to many more creampies in your future together."
    $ mc.change_location(bedroom)
    $ the_person.add_unique_on_room_enter_event(
        Action("Erica knocked up followup", VT_erica_breeding_fetish_followup_requirement, "erica_breeding_fetish_followup_label")
    )
    return

label VT_breeding_fetish_erica_unsuccessful_followup_label():
    $ the_person = erica
    $ erica.arousal = 50
    $ erica.apply_outfit(Outfit("Nude"))
    $ mc.change_energy(mc.max_energy)
    "As you slowly start to wake up, you feel the weight on your bed shift, and a gentle warmth spreads across your skin."
    if mom.sluttiness > 60:
        "You assume it's probably [mom.title], coming in to give you another pleasant wake-up call, but as your brain slowly engages, you realize the weight of the person is different, and the touch is more... urgent."
    else:
        "Thinking you're probably still dreaming, your brain is slow to engage and register what's going on, but the sensation of skin on skin is unmistakable."
    "Your pants slide off, exposing your morning wood, and you feel a weight around your hips as someone gets on top of you. You slowly open your eyes to find [the_person.possessive_title] straddling you, her eyes locked on yours with a fierce intensity."
    $ the_person.draw_person(position = "cowgirl")
    mc.name "Wha? [the_person.title]?"
    the_person "Shhh, don't want to wake your family... I need this, and I need it now."
    "She slowly slides herself down onto you, taking your full length inside her. You can't help but moan at the sudden sensation, and she responds with a soft gasp of pleasure."
    $ the_person.break_taboo("condomless_sex")
    $ the_person.break_taboo("vaginal_sex")
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(50)
    mc.name "What are you doing here?"
    the_person "I've been tracking my cycles, and I'm so fertile right now... I need your cum, and I need it ASAP. I couldn't wait any longer."
    "[the_person.possessive_title!c] starts to work her hips, her movements slow and deliberate at first, but growing more urgent and insistent as she builds towards her climax."
    call get_fucked(the_person, the_goal = "vaginal creampie", start_position = cowgirl, private = True, skip_intro = True, allow_continue = False) from _call_get_fucked_VT_breeding_fetish_erica_unsuccessful_followup_02
    "When you finish, she rolls off you and lies beside you on your bed, a look of satisfied exhaustion on her face."
    $ the_person.draw_person(position = "missionary")
    $ VT_add_breeding_fetish(the_person)
    $ become_pregnant(the_person, breeder_announce = True)
    the_person "Oh god... it's amazing. I think you did it. I don't know how I know... I can just feel it."
    "She rubs her belly happily, a soft smile spreading across her face."
    the_person "I mean... I'll take a test in a few days to be sure, but..."
    "She lies beside you for a minute, basking in the afterglow, before quietly getting up and dressing in the clothes she had brought with her."
    $ the_person.apply_planned_outfit(show_dress_sequence = True)
    the_person "I'll let you know when I find out for sure... daddy!"
    "She seems positively glowing, her eyes shining with a newfound sense of purpose and belonging."
    "Quietly, she leaves your room, leaving you to wonder how she had gotten in, and what other surprises she might have in store for you."
    "You look down at your limp cock, still slick from her juices, and can't help but smile at the memory of their encounter."
    "How did she even get in? You have so many questions, but for now, you just get up and start your regular morning routine, feeling a sense of excitement and anticipation for what the future might hold."
    $ the_person.add_unique_on_room_enter_event(
        Action("Erica knocked up followup", VT_erica_breeding_fetish_followup_requirement, "erica_breeding_fetish_followup_label")
    )
    return

label VT_breeding_fetish_candace_intro_label(the_person): 
    $ the_person = candace
    "As you step into the office, you see [the_person.possessive_title] looking over at you. She stands up and waves you over to her desk."
    $ the_person.draw_person()
    "You walk over to her."
    if the_person.personality == bimbo_personality: #She is a bimbo.
        mc.name "Hello [the_person.title]. Something I can help you with?"
        the_person "Yeah boss! I'm having trouble concentrating on my work this morning. Could you help me?"
        mc.name "Possibly, what seems to be distracting you?"
        the_person "Last night, I was like, totally watching porn, but I couldn't get off to the usual stuff. I was starting to get frustrated, until I finally found something that worked!"
        the_person "I found this video where like, the first half of it is this hottie getting railed and the guy cums in her, and then in the second half she's like 8 months pregnant!"
        the_person "You could totally tell it was her too because like, she had the same tattoo and everything!"
        the_person "I went back and watched the first half again and came so hard, thinking about how that was when she got knocked up!"
        mc.name "That... sounds like a great a video, but I'm not sure what I can help you with."
        if the_person.knows_pregnant:
            the_person "I know that like, I'm already knocked up, OBVIOUSLY. But like, maybe we could make a video like that too?"
            the_person "You could just like, keep fucking babies into me non-stop and every time you cum inside me, it's like, this could be the time!"
            mc.name "You want me to keep getting you pregnant?"
            the_person "Like, over and over! That sounds so hot!"
        else:
            the_person "I was thinking like, maybe we could do that! Take a video of you cumming inside me and knocking me up!"
            mc.name "You want me to get you pregnant?"
            the_person "Fuck yeah! That's like, so hot! And can you imagine having that on video? Holy fuck!"
        "Lately, you've been slipping her the Vitamin D so much, it increased her drive to reproduce. Unsurprisingly, it sounds like she has developed a breeding fetish."
        mc.name "Okay. I'll give you my cum. Now turn around, I'm going to take you over your desk."
        $ camera_person = get_random_from_list(known_people_at_location(mc.location, excluded_people = [the_person]))
        if not camera_person:
            "You look around the room, but no one else is around to record it, so you set up your phone to record and prop it up on a nearby desk as best you can."
        else:
            "You look around the room. You notice that another employee has overheard the conversation and is looking at you with some interest."
            mc.name "[camera_person.title], come here."
            $ camera_person.draw_person()
            camera_person "Yes?"
            mc.name "Take this, I need you to take a video for me."
            camera_person "Oh wow... you're really going to...? Right here?"
            "You nod and hand her your phone, with it set to video mode."
        "You turn back to [the_person.possessive_title]."
        $ the_person.draw_person(position = "standing_doggy")
        if the_person.vagina_available:
            "With her pussy already out and ready to be used, you waste no time getting your pants off. When your cock springs free, you use it to smack her ass a couple times."
        else:
            "As you start to pull your cock out, [the_person.possessive_title] reaches back and starts to pull off the clothing covering her ass."
            $ the_person.strip_outfit(exclude_upper = True, position = "standing_doggy")
            "You give her ass a couple smacks with your cock."
        $ the_person.change_arousal(10)
        $ mc.change_locked_clarity(50)
        mc.name "Are you ready to get bred, bitch?"
        "[the_person.title] keeps trying to back herself up onto you, but you move your dick around, frustrating her."
        the_person "Just, like, put it in me already!"
        mc.name "I want to hear you beg."
        the_person "PUT IT IN AND FUCK ME AND BREED ME AND CUM OVER AND OVER DEEP MAKE ME YOUR CUM DUMPSTER PLEASE PLEASE PLEASE!!!"
        $ mc.change_locked_clarity(50)
        "Wow, that didn't take much encouragement. You grab her hips, line yourself up and push yourself in deep."
        $ the_person.break_taboo("condomless_sex")
        $ the_person.break_taboo("vaginal_sex")
        the_person "Yes!!!"
        call fuck_person(the_person, start_position = bent_over_breeding, start_object = make_desk(), private = False, skip_intro = True, position_locked = True, skip_condom = True) from _VT_breeding_fetish_candace_intro_01
        if the_person.has_creampie_cum:
            "[the_person.title] reaches her hand back, rubbing the cum that has started to drip out of her all around her slit, playing with it."
        else:
            the_person "Oh god! It's so deep! Oh thank you so much [the_person.mc_title]!"
            pass
        if camera_person is None:
            "You grab your phone off the desk and stop the video. You quickly put it in an email to [the_person.title] so she can have a copy of it."
        else:
            camera_person "Wow..."
            "You grab your phone from [camera_person.title] and thank her for her help. You quickly put the video in an email to [the_person.title] so she can have a copy of it."
        $ del camera_person
        if the_person.knows_pregnant:
            the_person "I don't care if I am already pregnant... Please do that again! My body was made to take your cum like that!"
        else:
            the_person "I hope that did it, but you'd better cum inside me again and again anyway!"
        $ the_person.draw_person()
        "[the_person.possessive_title!c] slowly stands up and turns to you."
        the_person "Did you, like... get the video?"
        mc.name "A copy should be in your email shortly."
        if the_person.knows_pregnant:
            the_person "We'll have to like, make more! You know, when you are ACTUALLY knocking me up, not just practising!"
        else:
            the_person "Don't forget, I want another like, when my belly is all big and my titties are spraying milk everywhere!"
        mc.name "I'll make sure it happens. Do you think you can concentrate on your work now?"
        the_person "Yes sir! I'll get back to work!"
        $ VT_add_breeding_fetish(the_person)
        "You step away from her desk, letting her get back to her work. You notice her humming a happy tune as you walk away."
        "You can hardly believe it. [the_person.possessive_title!c] now has a fetish to get bred by you!"
        return
    else:
        the_person "[the_person.mc_title], I've been thinking about something, and I needed to make you aware of it."
        mc.name "Okay, what would that be?"
        the_person "Well, as you know, you and I both have very good... shall we say, genetics?"
        the_person "We are both very talented, go getters, with good genes."
        the_person "We owe it to the world to make offspring. As many, and as often as we can."
        if the_person.knows_pregnant:
            mc.name "We've been doing pretty good at that so far."
            "[the_person.title] rubs her pregnant belly."
            the_person "I agree."
        the_person "It's important that you cum inside me on a regular basis... As often as possible, really."
        "Lately, you've been slipping her the Vitamin D so much, it increased her drive to reproduce. Unsurprisingly, it sounds like she has developed a breeding fetish."
        mc.name "Are you saying you want to be my personal breeding mare?"
        the_person "The comparison to livestock is crude... but fitting. Yes, [the_person.mc_title], I want you to breed me over and over as much and as often as possible!"
        $ the_person.draw_person(position = "standing_doggy")
        $ mc.change_locked_clarity(50)
        "[the_person.title] stands up and bends over her desk."
        the_person "You should start right now. It's okay, I'll count it as my 5 minute break."
        if the_person.vagina_available:
            "With her pussy already out and ready to be used, you waste no time getting your pants off. When your cock springs free, you use it to smack her ass a couple times."
        else:
            "As you start to pull your cock out, [the_person.possessive_title] reaches back and starts to pull off the clothing covering her ass."
            $ the_person.strip_outfit(exclude_upper = True, position = "standing_doggy")
            "You give her ass a couple smacks with your cock."
        $ the_person.change_arousal(10)
        $ mc.change_locked_clarity(50)
        mc.name "Are you ready to get bred, bitch?"
        "[the_person.title] keeps trying to back herself up onto you, but you move your dick around, frustrating her."
        the_person "[the_person.mc_title], it's not appropriate to tease a lady like this."
        mc.name "I want to hear you beg."
        the_person "PUT IT IN AND FUCK ME AND BREED ME AND CUM OVER AND OVER DEEP MAKE ME YOUR CUM DUMPSTER PLEASE PLEASE PLEASE!!!"
        "Wow, that didn't take much encouragement. You grab her hips, line yourself up and push yourself in deep."
        $ the_person.break_taboo("condomless_sex")
        $ the_person.break_taboo("vaginal_sex")
        the_person "Yes!!!"

        call fuck_person(the_person, start_position = bent_over_breeding, start_object = make_desk(), private = False, skip_intro = True, position_locked = True, skip_condom = True) from _VT_breeding_fetish_candace_intro_02
        if the_person.has_creampie_cum:
            "[the_person.title] reaches her hand back, rubbing the cum that has started to drip out of her all around her slit, playing with it."
            if the_person.knows_pregnant:
                the_person "Mmm... I think I felt the baby kick when you came inside me!"
            else:
                the_person "The odds aren't great from just one creampie. Make sure you cum inside me again soon!"
        else:
            the_person "You're... you're done already?"
            mc.name "Sorry... I'll have to cum inside you another time."
        $ the_person.draw_person(position = "stand2")
        "[the_person.possessive_title!c] slowly stands up and turns to you."
        the_person "Thank you [the_person.mc_title]. Please cum inside me anytime you need a little relief from now on."
        $ VT_add_breeding_fetish(the_person)
        "You step away from her desk, letting her get back to her work. You notice her humming a happy tune as you walk away."
        "You can hardly believe it. [the_person.possessive_title!c] now has a fetish to get bred by you!"
    return #Needs testing #Needs testing

label VT_breeding_fetish_myra_intro_label():
    $ the_person = myra
    $ the_person.arousal = 40
    "Your phone buzzes with a notification from [the_person.possessive_title]."
    $ mc.start_text_convo(the_person)
    the_person "Hey, can you PLEASE come to the café tonight? I promise it'll be worth it... I've got a special surprise waiting for you."
    mc.name "Oh? What's the surprise?"
    the_person "It involves The Sims... and a whole lot of cum. Just come, okay?"
    "You can't help but notice the suggestive tone in her message."
    mc.name "Alright, I'm on my way."
    $ mc.end_text_convo()
    $ mc.change_location(gaming_cafe)
    $ the_person.apply_outfit(Outfit("Nude"))
    "When you arrive at the gaming café, you find it unlocked. You let yourself in and lock the door behind you."
    if myra_lewd_cafe_open():
        "You head to the back and into the adults-only section, where [the_person.title] is waiting for you."
    else:
        "You head to the back where you've played a lewd version of The Sims with [the_person.title] before."
    $ the_person.draw_person()
    the_person "Hey! You came! And I see you're a bit overdressed... let's fix that."
    mc.name "I guess I am. Are we playing The Sims tonight?"
    "You start to undress, and [the_person.title] watches with a hungry gaze."
    the_person "Yeah! I don't know why, but I'm feeling pretty lucky about the way the game finishes tonight... and I think it's going to involve a lot of cum."
    "[the_person.possessive_title!c] is definitely acting strange, but you can't help but be drawn in by her enthusiasm."
    "You've been dosing her with Vitamin D a lot recently... maybe she's developing a breeding fetish?"
    "You step out of the last of your clothes and look up to see [the_person.title] staring at you with a look of pure lust."
    the_person "Fuck, you look so... virile... let's get this going!"
    $ the_person.break_taboo("condomless_sex")
    $ the_person.break_taboo("vaginal_sex")
    call myra_sex_roulette_session_label(the_person, breeding_fetish_intro = True) from _call_VT_breeding_fetish_myra_intro
    "When you finish, she just stands there, running her hands over her belly with a look of satisfaction."
    "It's clear that she intended for you to cum inside her from the moment she texted you."
    if the_person.knows_pregnant:
        the_person "No wonder I'm pregnant... there's nothing as amazing as taking a hot load of cum."
    else:
        the_person "Oh god, that was fucking amazing. Do you think... maybe it really knocked me up?"
    "It's obvious now that [the_person.possessive_title] has developed a breeding fetish after all the loads of cum you've given her."
    "Even now, you can see her looking at your cock, trying to decide if she can milk another load from it."
    mc.name "You love it, don't you? You want to be my personal cum dumpster, to take my loads anytime and anywhere I want you to?"
    the_person "Oh god yes... I'll do anything to feel your cum inside me."
    mc.name "You're going to love it, aren't you? When you show up for a tournament, your belly round, your big tits leaking milk... everyone there is going to know what a needy cunt you have."
    the_person "Yes! I want everyone to know that I'm your breeding slut, that I'm always ready to take your cum."
    mc.name "Everyone there is going to know that you're a hopeless, thirsty slut... that you long for your master's cum sloshing around in your fertile womb all day long."
    "[the_person.possessive_title!c]'s knees start to buckle for a second, and she looks up at you with a pleading expression."
    the_person "Yes please! Breed me again, PLEASE?"
    mc.name "I plan to. Keep your cunt ready for me, anytime I want to dump my load inside you."
    the_person "Yes! Don't worry, I'll be ready... always."
    "You say goodbye to [the_person.title], knowing that she's now your breeding slut."
    "[the_person.possessive_title!c] now has a fetish to get bred by you, and you can't wait to fill her needy cunt with your cum over and over again."
    $ VT_add_breeding_fetish(the_person)
    $ mc.change_location(bedroom)
    "You walk home and collapse into your bed, already thinking about the next time you'll breed [the_person.title]."
    return


# this doesn't read properly, don't use repetitive wording, use different words, and movements. Update all the following the_person and movements with natural raw breeding personality. Use Hitomi Takami from Ane Haramix or Momoko Kuzuryu from Sumomomo, Momomo: The Strongest Bride on Earth, for ideas, keep to the structure. More sexual breeding personality and sexually explicit movements.
### DIALOGUE ###

label VT_breeding_fetish_ashley_intro_label():
    "Ashley doesn't have a breeding fetish written yet"
    return

label VT_breeding_fetish_dawn_intro_label():
    "Dawn doesn't have a breeding fetish written yet"
    return

label VT_breeding_fetish_kaya_intro_label():
    return False

label VT_breeding_fetish_ellie_intro_label():
    return False

label VT_breeding_fetish_camila_intro_label():
    return False

label VT_breeding_fetish_sakari_intro_label():
    return False
