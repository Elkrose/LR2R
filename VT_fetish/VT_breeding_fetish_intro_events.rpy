
#Fetish Intro Labels
label VT_breeding_fetish_employee_intro_label(the_person):
    "You are finishing up the last of your work today and closing up. All your employees should be gone for the day."
    "However, you are surprised when you are interrupted by someone."
    $ the_person.draw_person()
    the_person "Ah! [the_person.mc_title]... I was hoping to catch you alone. I need to talk to you about something."
    mc.name "Good evening [the_person.title]. What can I do for you?"
    the_person "Ah... more like... what can you do to me..."
    "Did you hear that right?"
    mc.name "Oh?"
    the_person "I umm... I mean... sorry."
    "She looks a bit flustered for a second, but quickly gathers her thoughts and starts to talk to you."
    if the_person.age < 35:
        the_person "Well, you know sir, I'm still pretty young, and lately I've been dealing with some pretty intense biological... urges..."
    else:
        the_person "Well, you know sir, I'm starting to get a bit older, and as my biological clock is ticking I've been getting some pretty intense... urges..."
    the_person "I'm not sure why, but lately I've been having these fantasies about having sex, raw, over and over, and getting filled with cum!"
    "Lately, you've been slipping her the Vitamin D so much, it increased her drive to reproduce. Unsurprisingly, it sounds like she has developed a breeding fetish."
    if the_person.knows_pregnant:
        the_person "Obviously I'm already pregnant, but umm, I've really been craving your cock inside me, twitching and pulsing your loads deep, over and over..."
    else:
        the_person "I don't know how to say this but, I've been craving you, and your cock, twitching and pulsing load after load deep inside me! Knocking me up!"
    $ mc.change_locked_clarity(20)
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
    mc.name "... and didn't stop until I dump my cum deep inside your wet breeding hole?"
    the_person "Oh god! Yes do it! Oh fuck!"
    "Still holding her hands down, you start to thrust rapidly. It's time to give this horny slut a creampie!"
    call fuck_person(the_person, start_position = breeding_missionary, start_object = make_desk(), private = True, skip_intro = True, position_locked = True, skip_condom = True) from _VT_breeding_fetish_employee_intro_01
    if the_person.has_creampie_cum:
        the_person "Oh god! It's so deep! Oh thank you so much [the_person.mc_title]!"
    else:
        the_person "Oh god, so deep and it isn't leaking out!"
        pass
    $ VT_add_breeding_fetish(the_person)
    if the_person.knows_pregnant:
        the_person "I don't care if I am already pregnant... Please do that again! My body was made to take your cum like that!"
    else:
        the_person "I hope that did it, but you'd better cum inside me again and again anyway!"
    "You slowly back away from [the_person.title], allowing her to get up."
    $ the_person.draw_person()
    "[the_person.possessive_title!c] slowly stands up, her legs are a little unsteady."
    mc.name "I need to get a few more things done before I close up the office. From now on, you are my breeding stock. Be ready to take my cum whenever I tell you to!"
    the_person "Yes! Yes sir! I'll be ready, don't worry!"
    $ the_person.draw_person()
    "You say goodbye to [the_person.title]."
    "[the_person.possessive_title!c] now has a fetish to get bred by you!"
    return #Needs testing

label VT_breeding_fetish_family_intro_label(the_person):
    $ mc.change_location(the_person.home)
    $ the_person.draw_person(position = "back_peek")
    "You walk into [the_person.possessive_title]'s bedroom. She is looking at herself in the mirror, but turns to look when she hears you walk in."
    the_person "Oh hey [the_person.mc_title]. I was just getting ready to head for bed."
    "She takes one last look at herself in the mirror, then turns around."
    $ the_person.draw_person()
    the_person "Do you want to cuddle with me for a little bit?"
    mc.name "Sounds nice."
    $ the_person.draw_person(position = "missionary")
    $ mc.change_locked_clarity(15)
    "You lay down next to [the_person.possessive_title] as she lays down on her back. You rest your head on her chest and put your arm across her."
    "For a while you simply enjoy the heat of each other's bodies. She is the first to break the silence."
    if the_person.knows_pregnant:
        the_person "Do you think it's weird, if I say I love this feeling? Being pregnant, making babies. It's like my body was made to do this, over and over again."
        the_person "I'm already looking forward to making another one, and this one isn't even here yet!"
    elif the_person.age > 35:
        the_person "Do you think I'm too old to have a baby? My hormones are in overdrive lately..."
        mc.name "No way. With modern medical science, women are having babies older and older, into their late forties even."
    else:
        the_person "My hormones are being crazy lately... would it be weird if I told you I... want to get knocked up?"
        mc.name "I'd imagine that's a pretty normal thing. We don't survive as a species if we don't have a drive to reproduce, right?"
        the_person "I suppose so."
    "You move your hand to her belly and begin to rub it. You can tell by her arousal that she's really ready to be fucked proper."
    "You wonder if she is on the verge of developing a fetish. Do you want to try and push her over the edge?"
    #if the_person.is_unique:
    #    "Warning, this character is unique, and may have unique fetish dialogue. If you continue, you may miss this dialogue!"
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
            $ VT_fetish_timer_reset(the_person, "breeding") 
            $ clear_scene()
            return
    "You decide it's time to train [the_person.possessive_title] to be your own personal breeding stock."
    "You push yourself up and on top of [the_person.title]. She puts her arms around you as your body begins to press against hers."
    mc.name "Honestly, I think it's pretty normal to have desires like that."
    the_person "Yeah..."
    "You start to kiss her along her neck and then whisper in her ear."
    mc.name "To have a man pin you down, fuck you senseless, then dump his risky load deep inside you, over and over."
    $ the_person.change_arousal(20)
    $ mc.change_locked_clarity(20)
    the_person "Ah, that does sound nice..."
    mc.name "It sounds more than nice though, doesn't it? It's what you NEED. A bull, who fucks you and knocks you up, over and over. Like some kind of livestock."
    the_person "Ahhh, yeah! Oh god..."
    $ the_person.change_arousal(20)
    "You reach down and start to pull your cock out."
    the_person "But... we're... you know... family..."
    mc.name "Shhh, it's okay. You can trust me, right? We're both consenting adults, who just happen to be related."
    "She bites her lip. It's clear from the look in her eyes that she wants it badly, but is afraid to take the leap."
    mc.name "Tell you what, let's go a little farther, and if it feels wrong we can stop."
    $ the_person.add_situational_slut("situation",20, "I can stop if I want to...")
    "She nods her head in agreement."
    if the_person.vagina_available:
        "You finish pulling your cock out and begin to rub it along her slit."
    else:
        "As you finish pulling your cock out, [the_person.possessive_title] reaches down and starts pulling her bottoms off."
        $ the_person.strip_to_vagina(prefer_half_off = True, position = "missionary")
    $ mc.change_locked_clarity(50)
    $ the_person.change_arousal(10)
    if the_person.love < 0:
        the_person "I can't believe I'm saying this, and with you of all people..."
        the_person "But I'm ready! Just... just put it in me! Raw!"
    else:
        the_person "My brain says this is wrong, but my body keeps saying it's so right!"
        the_person "Fuck me [the_person.mc_title], I want you to fill me with your cum!"
    $ the_person.break_taboo("condomless_sex")
    $ the_person.break_taboo("vaginal_sex")
    "You run your cock along her slit a couple more times, then start to push it inside."
    $ play_moan_sound()
    "She moans as you bottom out inside her and start to fuck."
    call fuck_person(the_person, start_position = breeding_missionary, start_object = make_bed(), private = True, skip_intro = True, position_locked = True, skip_condom = True) from _VT_breeding_fetish_family_intro_01
    $ VT_add_breeding_fetish(the_person)
    $ the_person.draw_person(position = "missionary")
    if the_person.knows_pregnant:
        the_person "I know I'm already pregnant... but that was so good. Even after this one comes, I want to keep doing this!"
    else:
        the_person "Oh god, you're right. It feels so right getting seeded by you."
    "You slowly roll off of [the_person.title] and lie beside her."
    mc.name "Make sure you lay like this for a while. Keep those swimmers as deep as you can."
    "You get up and start to get dressed."
    the_person "Do you... want to stay with me tonight?"
    mc.name "I can't stay tonight, but from now on, you are my breeding stock. Be ready to take my cum whenever I tell you to."
    the_person "Yes! Yes sir! I'll be ready, don't worry!"
    "You say goodbye to [the_person.title]."
    "[the_person.possessive_title!c] now has a fetish to get bred by you!"
    $ the_person.clear_situational_slut("situation")
    return #Needs testing

label VT_breeding_fetish_generic_intro_label(the_person): #This function to be used for generic non employee, non unique girls
    $ the_person.arousal = 40
    "As you walk into [mc.location.formal_name], you notice [the_person.title]. She notices you also and approaches."
    $ the_person.draw_person()
    the_person "Hello [the_person.mc_title]! It's good to see you!"
    if the_person.tits_visible:
        "You take a moment to look at her. Her cheeks are flushed, and her exposed nipples look hard as diamonds. She is definitely aroused."
    else:
        "You take a moment to look at her. Her cheeks seem flushed... Her nipples are poking against the fabric of her outfit. Is she... Aroused?"
    mc.name "It's good to see you also."
    the_person "Hey, I was just thinking about texting you. Are you busy right now?"
    mc.name "Probably not."
    "She leans forward and talks quietly in your ear."
    the_person "My place is right around the corner... want a tour of my bedroom?"
    $ mc.change_locked_clarity(20)
    "Lately, you've been slipping her the Vitamin D so much, it seems to have increased her drive to reproduce."
    "It's possible she might be on the verge of developing a fetish. If you go back to her place, you can push her over the edge into having a breeding fetish!"
    #if the_person.is_unique:
    #    "Warning, this character is unique, and may have unique fetish dialogue. If you continue, you may miss this dialogue!"
    menu:
        "Go to her place" if mc.energy > 40:
            mc.name "A tour would be nice. Lead the way."
        "Too tired" if mc.energy <= 40:
            pass
            #TODO re add the event for this person for the next day.
            $ VT_fetish_timer_reset(the_person, "breeding")
            $ clear_scene()
            return
        "Not now":
            mc.name "I'm sorry [the_person.title], I've got errands to accomplish. Maybe another time."
            $ the_person.change_stats(happiness = -5, love = -2)
            the_person "Ah, okay. I see."
            $ VT_fetish_timer_reset(the_person, "breeding", 2) 
            return False

    "[the_person.title] takes your hand and you step away with her. After a few minutes of walking, you find yourself at her place."
    "She quickly unlocks the front door and pulls you inside."
    $ the_person.learn_home()
    $ mc.change_location(the_person.home)
    $ the_person.draw_person(position = "kissing")
    "She throws her arms around you and you start to make out. Your hands drop to her ass and you start to grope her aggressively."
    the_person "Oh god, I'm not sure I can make it to the bedroom."
    $ the_person.draw_person(position = "against_wall")
    $ the_person.change_arousal(10) #50
    $ mc.change_locked_clarity(30)
    "You pick her up and carry her to her bedroom. She is grinding against you the whole way."
    "Knowing the reason she is so aroused, you start to talk dirty with her."
    mc.name "Are you on birth control, [the_person.title]?"
    the_person "You know I'm not..."
    mc.name "Good. When we get to your bed, I'm going to throw you down on it, pin you down, and fuck you until I cum deep inside you."
    if the_person.knows_pregnant:
        the_person "Do it! I'm already pregnant, but I want to feel your seed deep inside me!"
    else:
        the_person "Oh fuck, but I could... I could get..."
        mc.name "Pregnant? You're right."
    $ the_person.draw_person(position = "missionary")
    mc.name "That's what you want, isn't it? For me to pin you down and breed you, over and over, like the little slut you are."
    the_person "Oh [the_person.mc_title], I really do!"
    if the_person.vagina_available:
        "You pull your cock out and begin to rub it along her inviting slit."
    else:
        "As you pull your cock out, [the_person.possessive_title] pulls her bottoms off."
        $ the_person.strip_outfit(exclude_upper = True, position = "missionary")
        "When she finishes you run your cock all along her inviting slit."
    $ the_person.change_arousal(10) #60
    $ mc.change_locked_clarity(50)
    the_person "Just shove it in! I'm ready!"
    $ the_person.break_taboo("condomless_sex")
    $ the_person.break_taboo("vaginal_sex")
    "You decide to give her what she wants, for now. You grab her hips and then push yourself inside her sopping wet cunt."
    call fuck_person(the_person, start_position = breeding_missionary, start_object = make_bed(), private = True, skip_intro = True, position_locked = True, skip_condom = True) from _VT_breeding_fetish_generic_intro_01
    $ VT_add_breeding_fetish(the_person)
    $ the_person.draw_person(position = "missionary")
    "When you finish, she lays back, just rubbing her hand along her belly."
    if the_person.knows_pregnant:
        the_person "I know I'm already pregnant... but that was so good. Even after this one comes, I want to keep doing this!"
    else:
        the_person "Oh god, that was amazing. I hope... I hope that did it!"
    "You slowly roll off of [the_person.title] and lie beside her."
    mc.name "Make sure you lay like this for a while. Keep my semen as deep as you can."
    "You get up and start to get dressed."
    the_person "Can we do this again soon?"
    mc.name "I plan to. Keep your cunt ready for me, anytime I want to dump my load inside you."
    the_person "Yes! Don't worry, I'll be ready!"
    "You say goodbye to [the_person.title]."
    "[the_person.possessive_title!c] now has a fetish to get bred by you!"
    return

label VT_breeding_fetish_mom_intro_label(): # Needs testing
    $ the_person = mom
    $ the_person.on_birth_control = False
    $ the_person.event_triggers_dict["Mom_forced_off_bc"] = False
    $ the_person.outfit.strip_to_vagina()
    "You're woken up by your bed shifting under you and a sudden weight around your waist."
    "You feel a tug on your clothing, and you are slowly opening your eyes when you feel your morning wood spring free."
    $ the_person.draw_person(position = "cowgirl", emotion = "happy")
    $ mc.change_locked_clarity(50)
    "You open your eyes to see [the_person.possessive_title] lining you up with her pussy, before slowly sliding down on top of you."
    $ the_person.break_taboo("condomless_sex")
    $ the_person.break_taboo("vaginal_sex")
    mc.name "Ooohh... good morning [the_person.title]."
    the_person "Ohhh... good morning honey! Mommy needs your seed inside her this morning... and I'm not taking no for an answer!"
    "Lately, you've been slipping her the Vitamin D so much, it increased her drive to reproduce. Unsurprisingly, it sounds like she has developed a breeding fetish."
    the_person "I had such vivid dreams last night... you were fucking me and kept cumming inside me over and over and over!"
    the_person "My belly started to get bigger and my tits started to leak milk and I loved it so much..."
    "Ahh, you've been fucking her so much, she can't seem to get enough. Looks like you have finally driven her over the edge and given her a breeding fetish!"
    $ the_person.change_arousal (30)
    $ mc.change_locked_clarity(50)
    "She starts to rock her hips back and forth. You reach up and start to fondle her tits as they sway back and forth."
    mc.name "Mmmm, I can't wait to drink milk from your tits again, [the_person.title]."
    if the_person.knows_pregnant: #She already knows she's pregnant
        the_person "Oh god I know I'm already pregnant, but I just want you to fuck your cum into me over and over!"
    else:
        the_person "Oh god, can we really do this? Will you fuck your cum into me over and over until I'm pregnant? I want that so bad!"
    mc.name "Of course I'll give you my cum. From now on, you'll be my own personal mare. I'll breed you every chance I get."
    $ the_person.change_arousal(15)
    the_person "Oh [the_person.mc_title], that's so hot... I want it now! I'm going to ride the cum out of you now!"
    call get_fucked(the_person, the_goal = "vaginal creampie", start_position = cowgirl, private = True, skip_intro = True, allow_continue = False) from _call_get_fucked_VT_breeding_fetish_mom_intro_01
    if the_person.has_creampie_cum:
        the_person "Oh god... I need to keep it all in..."
        "[the_person.title] reaches her hand down, trying to keep your cum inside her, but failing, as your cum drips down the inside of her thighs."
    else:
        the_person "Oh god! It's so deep! Oh thank you so much [the_person.mc_title]!"
        pass
    mc.name "Don't worry, I'll give you more soon."
    "She chuckles, then smiles at you."
    the_person "You better... Every day! Even if I am pregnant..."
    $ VT_add_breeding_fetish(the_person)
    the_person "It's good for the baby, I think! It knows when mommy is getting taken care of... How happy you make her..."
    $ the_person.draw_person(position = "missionary")
    "[the_person.title] lays down beside you for a while. Soon though, it is time to get up and ready for the day."
    the_person "Have a good day. Don't forget, try to be home for dinner tonight! You need to keep your energy up!"
    "You can hardly believe it. Your own mother now has a fetish to get bred by you!"
    $ mc.change_locked_clarity(10)
    return #Needs testing

label VT_breeding_fetish_lily_intro_label(the_person): #NEeds testing, evening room entry event
    $ the_person = lily
    "Note: This scene was written assuming that eventually you fuck [the_person.title] on a live stream, but so far Vren has not written this step."
    $ mc.change_location(the_person.home)
    "You step into [the_person.possessive_title]'s room. She is standing next to her mirror playing with her [the_person.hair_description], but looks over at you and smiles when she hears the door."
    $ the_person.draw_person()
    the_person "Oh hey [the_person.mc_title]! I was wondering if you were going to be around tonight. Want to stream with me tonight?"
    "Your sister's job, over the last few months, has slowly evolved. From taking sexy snaps, to streaming sex with you live. Having sex with your sister, {i}and{/i} getting paid for it? It's amazing."
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
    "You notice she hesitates a bit. She bites her lower lip before continuing."
    the_person "So umm, I've been getting some requests recently..."
    mc.name "Oh? What are the thirsty anonymous internet guys wanting?"
    "She chuckles a second, but you sense a nervous tone."
    the_person "Well... they've been asking to see us take things one step farther... For you to finish inside me!"
    if the_person.knows_pregnant:
        "[the_person.title] is already pregnant, so it doesn't necessarily make the act risky."
        mc.name "You're already pregnant... but is that what they want? To act like you could get pregnant?"
    else:
        "You knew [the_person.title] wasn't on birth control."
        mc.name "That could be risky. What if you got pregnant? Or is that the point?"
    "Recently, you've been fucking her alot, possibly triggering her urge to reproduce... you wonder if there's even been any requests, or if she is just using that as an excuse."
    mc.name "Maybe I should message them. Find out more about what they want to see..."
    "She quickly interrupts you."
    the_person "No! You don't need to do that... I'm sure that's what it is! To watch as I pretend to get knocked up!"
    "She gives a tell-tale sign. As she says that, she looks away from you and to the side. She is lying to you."
    mc.name "That's what they want? Are you sure? Or is that what YOU want?"
    "[the_person.possessive_title!c] begins to blush heavily."
    the_person "Oh me? Want to get knocked up? By my brother? That's... I mean that's CRAZY!... right?"
    $ mc.change_locked_clarity(20)
    "She is struggling to give a reasonable explanation. It is pretty clear now that she is just fishing for an excuse to fuck you raw, and to get filled with your potent seed."
    mc.name "Yeah, I mean, wouldn't that be crazy? For a woman to want to get fucked? To have a man dominate her and do what he wants with her, then fill her up with his seed, consequences be damned?"
    $ the_person.change_arousal(10)
    the_person "Well yeah I mean obviously that sounds hot but you're my brother..."
    mc.name "Right, who happens to be a man? Someone you know and trust."
    "She sighs. She resigns herself and opens up."
    the_person "I can't explain it... The way things between us have progressed... But I just can't stop thinking about it!"
    the_person "My body wants it so bad, for you to pin me down and fuck me anywhere you want, cumming inside me over and over..."
    $ mc.change_locked_clarity(50)
    "She pauses for a second..."
    if the_person.knows_pregnant:
        the_person "I know this is crazy... I'm already pregnant!... but I don't want to stop now! I want you to breed me over and over, like your personal breeding slave!"
    else:
        the_person "I know this is crazy... I want you to knock me up! And not just once! I want you to breed me over and over, like your personal breeding slave!"
    "She seems to have acquired a breeding fetish!"
    mc.name "Ok... from now on, you are my personal cum dumpster. I'll use you like you want!"
    the_person "Oh god... this is amazing! Let's do it!"
    "Suddenly she remembers."
    the_person "Can we... can we do it on stream? No one on there believes we are actually siblings. They think it's all just for show!"
    mc.name "Go ahead, set it up."
    $ the_person.draw_person(position = "sitting")
    "[the_person.possessive_title!c] walks over to her laptop. You give her a few minutes to get everything set up."
    the_person "Okay... I promised all the viewers a crazy show! Oh god, I can't believe it..."
    "She stands up."
    $ the_person.draw_person()
    the_person "Just one more thing to do..."
    $ the_person.strip_outfit()
    "[the_person.title] gets naked, and you quickly follow suit."
    mc.name "How do you think we should do this?"
    the_person "I was thinking... you could just lay back and hold the camera. I'll ride you reverse cowgirl, then when you finish you'll be able to uhhh, you know, see it."
    $ mc.change_locked_clarity(20)
    mc.name "Mmm... that sounds amazing... for the viewers too!"
    "She punches your arm half-heartedly and laughs."
    "You walk over to her bed and lay down on it. After a minute she brings you the camera."
    "She goes back over to the computer, and after a moment, she gives a countdown."
    the_person "Okay, we are streaming in 5, 4, 3..."
    "As she goes past three stops counting and instead starts to walk over to you. She starts to talk into the camera."
    the_person "Hey everyone... just as promised, I have a naughty stream set up tonight!"
    the_person "Tonight is the night. I'm going to fuck my brother and let him cum in my pussy!"
    "You can hear a few replies go through on the computer, but from where you are you can't see them. [the_person.title] also hears them."
    the_person "I'm sorry, tonight I won't be able to take requests during. Just sit back and enjoy the show!"
    $ the_person.draw_person(position = "doggy")
    $ mc.change_locked_clarity(50)
    "With that, she turns her back to you and swings one leg over your body, her ass now pointed back at you."
    "She reaches down and gives your bare cock a few strokes, then points it up at her cunt."
    $ the_person.increase_vaginal_sex()
    "Her pussy is moist and she easily starts to slide down on it, your bare cock enveloped by her steamy flesh."
    the_person "Oh fuck bro, you fill me up so good..."
    "She's playing it up for the stream, but you know she is also having fun, fucking her brother."
    $ the_person.change_arousal(20)
    $ mc.change_locked_clarity(20)
    "You lay back on the bed while [the_person.possessive_title] works your cock in and out of her. You make sure to keep her ass in the frame of the camera."
    "[the_person.possessive_title!c] gives you a few quick, shallow dips then pull off you almost completely, leaving just your tip inside her."
    "She swirls her hips a couple times then impales herself on your again. [the_person.title] works her hips relentlessly on top of you as she pleases herself on your erection."
    $ the_person.change_arousal(30)
    $ mc.change_arousal(30)
    "She is putting on an incredible show for the camera! Her skill at working dick is extraordinary."
    the_person "Oh god bro, I'm so full! I want you to cum inside me!"
    "Her dirty words are matched by her actions as she works your cock aggressively. Her sexual expertise is incredibly pleasing for both of you."
    mc.name "Do it sis, your ass is amazing!"
    "You play along for the stream, and while no one online actually believes it, you legitimately fuck your sister."
    $ the_person.change_arousal(30)
    $ mc.change_locked_clarity(20)
    "[the_person.possessive_title!c] wiggles back and forth a few more times, then looks back at you and smiles."
    the_person "Do you like that, bro? Ah! That is so good..."
    "[the_person.possessive_title!c] reaches back between her legs and cups your balls."
    the_person "Mmm, you feel so full... I want you to fill me up! I can't wait to milk all that cum out of you!"
    $ the_person.change_arousal(30)
    $ mc.change_locked_clarity(20)
    "Her dirty talking is having its desired effect, and the taboo of doing this while anyone in the world can watch is just too much."
    "[the_person.possessive_title!c]'s sweet cunt milks your cock, the wet friction pushes you past the point of no return."
    mc.name "Ah, I'm going to cum!"
    the_person "Oh god me too! Oh fuck bro I'm cumming! Fill me up I need your cum too!"
    "She slams her hips down. As deep as your cock can go, you start to cum, filling [the_person.possessive_title]."
    $ the_person.have_orgasm()
    "Her hole is quivering as she cums at the same time, milking your cock for every last drop of seed."
    $ the_person.cum_in_vagina()
    $ the_person.draw_person(position = "doggy")
    $ ClimaxController.manual_clarity_release(climax_type = "pussy", person = the_person)
    "Eventually the twitching stops, for both of you. You did it. You dumped your seed into your sister's unprotected, fertile snatch."
    "When she slowly pulls off you, your seed immediately begins to leak out of her and down her legs. You make sure to get the whole thing in frame."
    $ mc.reset_arousal()
    $ the_person.reset_arousal()
    the_person "Oh god... I wonder if I got pregnant..."
    "[the_person.possessive_title!c] slowly recovers and gets up. She turns around and sits on the side of the bed, facing you."
    $ the_person.draw_person(position = "sitting")
    the_person "Well... I hope everyone enjoyed watching my brother try and knock me up... I know I enjoyed it."
    the_person "Time for the stream to end! Goodbye everyone!"
    $ the_person.draw_person(position = "walking_away")
    "[the_person.title] walks over to the computer, ending the live stream. Your seed still running down the inside of her legs."
    $ the_person.draw_person()
    the_person "Well... I think that went well!"
    mc.name "Me too... want to have another round?"
    the_person "Oh god... my body says yes... but I think I need to rest."
    "She bites her lip as she looks down at you."
    the_person "I meant it earlier though... I want you to breed me. Anytime, anywhere!"
    mc.name "Don't worry, I'll give you more soon."
    "She chuckles, then smiles at you."
    the_person "You better... Every day! Even if I am pregnant..."
    $ VT_add_breeding_fetish(the_person)
    "You quietly get up and get dressed. You sneak out of her room, being careful so your mother doesn't hear you."
    "You can hardly believe it. Your own sister now has a fetish to get bred by you!"
    return

label VT_breeding_fetish_rebecca_intro_label():
    "Rebecca doesn't have a breeding fetish written yet"
    return

label VT_breeding_fetish_gabrielle_intro_label():
    "Gabrielle doesn't have a breeding fetish written yet"
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
            the_person "Heyyyyyyy [the_person.mc_title]! I need your cock! Meet in your office?"
            mc.name "Sure, I'll meet you there."
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
            the_person "Basically, this guy with a monster cock bent his secretary over his desk and fucked her over and over until she was knocked up and full of cum!"
            the_person "I was dreaming about it all night. Can we do it please please please pleeeeeaaaassseee???"
            "Sounds like [the_person.title] has started to develop a breeding fetish from all the fuckery. You suppose you should indulge her with this as well."
            mc.name "Sounds good. Get over here."
            the_person "Oh! Yes sir. What are you going to do to me?"
            call VT_breeding_fetish_stephanie_bimbo_label(the_person) from _VT_breeding_fetish_stephanie_intro_bimbo_02
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
            the_person "Well, recently I've started having a new set of... well... breeding fantasies. Serum related I'm sure."
            the_person "I just wanted to make sure that we still have an understanding, right?"
            mc.name "Certainly. I'll always be here to help you with your needs."
            call breeding_fetish_stephanie_normal_label(the_person) from _VT_breeding_fetish_stephanie_intro_normal_02

    $ clear_scene()
    $ scene_manager.clear_scene()
    $ the_person.apply_planned_outfit()
    return #Needs testing

label VT_breeding_fetish_stephanie_bimbo_label(the_person):
    "You begin to walk towards her."
    mc.name "That's right. You were going to bend over my desk for a minute. And if everything goes well, I have a present for you."
    the_person "Oh! A present! I do love presents! Especially the ones I tend to get when I'm bent over. I wonder what it could be!"
    $ scene_manager.update_actor(the_person, position = "standing_doggy")
    $ mc.change_locked_clarity(50)
    "[the_person.possessive_title!c] turns around and bends over. Your hands immediately get to work."
    $ scene_manager.strip_to_vagina(person = the_person)
    "She wiggles her ass back and forth in front of you as you pull your dick out."
    the_person "Stick it in [the_person.mc_title]! I want to earn my special present!"
    $ the_person.break_taboo("condomless_sex")
    $ the_person.break_taboo("vaginal_sex")
    "Without any hesitation you slide your cock into her cunt."
    call fuck_person(the_person, start_position = bent_over_breeding, start_object = make_desk(), skip_intro = True, position_locked = True, skip_condom = True) from _call_VT_breeding_fetish_stephanie_bimbo_01
    $ VT_add_breeding_fetish(the_person)
    the_person "Oh god, it's so warm. It's like I can feel the little sperm wriggling inside me..."
    $ scene_manager.update_actor(the_person, position = "stand2")
    the_person "Mmm, thanks for that mister! I know this is kinda crazy but... I'm totally getting the urge for another round. Normally one time is enough but..."
    mc.name "I'm sorry, you'll have to be patient if you want another round."
    the_person "Ah... I see."
    the_person "Fine! I'll just go back to... whatever it was I was doing. What do I do here again?"
    mc.name "It doesn't matter, you can take the rest of the day off."
    the_person "Oh? That eager to get rid of me? Guess I'll just go find someone else to play with for a while. Your loss mister!"
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "You say goodbye, and [the_person.possessive_title] turns and walks out of your office. Your seed is dribbling down her leg."
    "Looks like [the_person.title] has a breeding fetish now! But she is also a bimbo."
    if the_person == mc.business.head_researcher:
        "You are guessing she is probably not particularly fit for her job in research. Maybe you can move her somewhere else in the company?"
    return

label VT_breeding_fetish_stephanie_normal_label(the_person):
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person, position = "stand4")
    "[the_person.possessive_title!c] stands up."
    if not the_person.vagina_available:
        "She starts to strip down."
        $ scene_manager.strip_to_vagina(person = the_person)
    "She looks at you expectantly."
    the_person "Well? Why are you still wearing clothes? You said you would help!"
    # call fuck_person(the_person, start_position = anal_cowgirl, start_object = make_desk(), girl_in_charge = True, position_locked = True) from _call_sex_description_SBA093
    call get_fucked(the_person, the_goal = "vaginal creampie", start_position = cowgirl, start_object = make_desk(), allow_continue = False) from _call_get_fucked_VT_breeding_fetish_stephanie_normal_cowgirl_01
    $ VT_add_breeding_fetish(the_person)
    the_person "Oh god... It's even better than I dreamed about last night."
    "[the_person.possessive_title!c] takes a minute to recover before standing up. She rubs her belly."
    $ scene_manager.update_actor(the_person, position = "stand2")
    the_person "Okay. I hope you realise the serums also greatly increase libido."
    mc.name "Don't worry. If the urges ever get too strong, just come find me, anywhere I am I'll bend you over, even here in the lab."
    the_person "Ah... that sounds... acceptable. Okay, let's give this a shot I guess."
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "You say goodbye, and [the_person.possessive_title] turns and walks out of your office, your cum running down the inside of her legs."
    "Looks like [the_person.title] has a breeding fetish now!"
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

label VT_breeding_fetish_starbuck_intro_label():  #Needs TEsting
    $ the_person = starbuck
    $ mc.start_text_convo(the_person)
    the_person "Hey, do you think you could help me close up the shop tonight? I have a few things I need help with."
    "You consider it. You don't have much else going on right now, so you decide to agree."
    mc.name "Sure, I'll be over shortly."
    $ mc.end_text_convo()
    "You make your way over to the sex shop."
    $ mc.change_location(sex_store)
    $ the_person.draw_person()
    "When you get to the store, you look around. It seems like the store is already pretty clean."
    mc.name "Good evening [the_person.title]. Still need help? Things look pretty good around here to me..."
    the_person "Hey [the_person.mc_title]! Thanks for coming. I'm almost done, but thought maybe we could just hang out for a bit."
    "Hmm, so she has ulterior motives for asking you here."
    mc.name "Certainly."
    "[the_person.possessive_title!c] locks the front door. She gets you a beer from her fridge and she grabs one for herself."
    "You make small talk for a bit. Finally, [the_person.title] starts to talk to you about why she asked you over."
    the_person "So... you are probably wondering why you are here. Today, something happened to me while I was working."
    the_person "This young couple came in, looking for some new lingerie. They needed new ones because the woman had umm... grown out of her clothing."
    the_person "She was... shall we say VERY pregnant. I think she was ready to pop any day!"
    if the_person.knows_pregnant:
        the_person "I know I'm already pregnant but... it was so hot! It made me realise how amazing it is to get bred."
    else:
        the_person "There was something about them though. They were practically glowing! And the way they looked at each other. I... I can't believe this, but it made me so jealous!"
        the_person "I've never had it quite this bad before... but it gave me this ITCH. I can't explain it, but I've been daydreaming all day about... you know... being like that."
    if the_person.is_girlfriend:
        the_person "I know our relationship is kind of... unique... with how much older I am. But I don't think I've ever been so sure of something."
    else:
        the_person "I know it's kind of weird, with how much older I am. But I don't think I've ever been more sure of something."
    the_person "Would you be my bull? Cum inside me... over and over... breed me like it's your job!"
    $ mc.change_locked_clarity(30)
    the_person "I want to feel your seed inside me, every second of every day!"
    "Your cock is already hard, listening to [the_person.possessive_title] talk like this. You've been cumming in her lots, and it looks like you finally given her a breeding fetish."
    "It's time to seal the deal. If you give her what she wants now, she'll be begging you for creampies every chance she gets."
    mc.name "Okay. I'll give you my cum. Now turn around, I want to take you over the counter."
    $ the_person.change_arousal(8)
    the_person "Oh god, yes!"
    $ the_person.draw_person(position = "standing_doggy")
    "She turns around and bends over the counter, as you asked her to. You step close behind her."
    if the_person.vagina_available:
        "With her pussy already out and ready to be used, you waste no time getting your pants off. When your cock springs free, you use it to smack her ass a couple times."
    else:
        "As you start to pull your cock out, [the_person.possessive_title] reaches back and starts to pull off the clothing covering her ass."
        $ the_person.strip_outfit(exclude_upper = True, position = "standing_doggy")
        "You give her ass a couple smacks with your cock."
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(50)
    "She wiggles her hips back and forth a bit, teasing you."
    the_person "Stick it in [the_person.mc_title]! Fuck me hard and cum as deep as you can!"
    "You grab her hips to stop the wiggling. You line yourself up with her thirsty cunt and push into her. She gasps when you bottom out."
    $ the_person.break_taboo("condomless_sex")
    $ the_person.break_taboo("vaginal_sex")
    the_person "Oh yes! Give it to me good!"
    call fuck_person(the_person, start_position = bent_over_breeding, start_object = make_counter(), private = True, skip_intro = True, position_locked = True, skip_condom = True) from _VT_breeding_fetish_starbuck_intro_01
    if the_person.has_creampie_cum:
        the_person "Oh god! Baby making sex is so hot, I can't believe it..."
        "[the_person.title] reaches her hand back, trying to keep your cum inside her, but failing, as your cum drips down the inside of her thighs."
        if the_person.knows_pregnant:
            the_person "I don't care if I am already pregnant... Please do that again! My body was made to take your cum like that!"
        else:
            the_person "I hope that did it, but you'd better cum inside me again and again anyway!"
    else:
        the_person "Please, [the_person.mc_title], next time, fill my little pussy with all that cum."
        mc.name "If you like it that much, I will give you everything I got, next time."
        "She smiles, with a definite sparkle in her eyes."
    $ VT_add_breeding_fetish(the_person)
    $ the_person.draw_person()
    "[the_person.possessive_title!c] slowly stands up and turns to you."
    the_person "Wow... I'm glad I finished closing up before you got here..."
    $ the_person.draw_person(position = "kissing")
    "She draws you into a hug, then whispers in your ear."
    the_person "You can bend me over like that anytime... I don't even care if there are customers here when you do it..."
    $ the_person.draw_person()
    the_person "You go ahead, I have a couple more things to do before I go."
    "You say goodbye to [the_person.title]."
    "You can hardly believe it. The sex store owner [the_person.title] now has a fetish to get bred by you!"
    return #Needs testing

label VT_breeding_fetish_sarah_intro_label():   #Needs Testing
    $ the_person = sarah
    $ mc.change_location(bedroom)
    $ scene_manager = Scene()
    $ mc.start_text_convo(the_person)
    the_person "Hey, can I come over tonight? I had something I wanted to talk to you about."
    mc.name "Sure. Want to spend the night?"
    the_person "Hell yeah! I'll bring some stuff over."
    "About 20 minutes later she texts you."
    the_person "Hey, I'm here! Come let me in!"
    $ mc.end_text_convo()
    "You head to your front door and open it."
    "For once, you manage to get her back to your room while avoiding [mom.possessive_title] and [lily.title]."
    $ scene_manager.add_actor(the_person, position = "sitting")
    "She walks over and sits on your bed."
    mc.name "So... what did you want to talk about?"
    "She clears her throat. You can tell she is a little nervous."
    if the_person.knows_pregnant:
        the_person "I know I'm already pregnant... and it is amazing really."
        the_person "But even after you got me pregnant, every time you finish inside me, I find myself craving it, more and more."
        the_person "The itch is getting so bad! I just want you to fill me up, over and over!"
        the_person "Even after the baby comes... I want your seed planted deep in me as much as possible!"
        "This is quite a twist! You know you most likely started giving her pregnancy urges due to all the cum you pumped into her."
        mc.name "I'll do it. From now on, you are my personal mare! I'll breed you over and over, just like you want."
    else:
        the_person "Well, this is kind of hard to talk about. But... we've been having a lot of unprotected sex lately..."
        mc.name "Oh my god, are you pregnant?"
        the_person "No! No, not yet... that I know of anyway..."
        mc.name "Not... yet?"
        the_person "Well, [the_person.mc_title], it's been like a dream, having you back in my life like this. Things are amazing, being with you."
        the_person "I've been, well, tracking my cycles recently and, well, basically, I'm fertile right now."
        "You can feel your cock twitch in your pants. You imagine [the_person.possessive_title], knocked up, her tits swelling with milk and her belly growing..."
        the_person "Every time you finish inside me, I find myself thinking about it, more and more, what it would be like to get pregnant and have a baby with you."
        the_person "Look, you don't have to answer me right now, but, I thought maybe we could try and have a baby. Together?"
        the_person "I know this is crazy... but lately I've just had this almost overwhelming itch! I want you to knock me up and fill me over and over!"
        "This is quite a twist! You know you most likely started giving her pregnancy urges due to all the cum you pumped into her."
        mc.name "Honestly, I didn't realise this was something you were thinking about. But I would love to make a baby with you!"
    $ the_person.change_stats(happiness = 15, obedience = 10)
    $ mc.change_locked_clarity(50)
    the_person "Oh! Wow, I honestly... I thought you were gonna say no! This is... I can't believe it."
    "She looks up at you, and you can see the changes in her facial expression. She goes from surprised, to happy, to sultry."
    the_person "So umm, what are you doing right now?"
    mc.name "I think we should get naked."
    the_person "Yes sir!"
    $ scene_manager.strip_full_outfit(person = the_person)
    $ mc.change_locked_clarity(50)
    "You get naked with [the_person.possessive_title]. She rolls on her back and spreads her legs."
    the_person "Come fill me up, [the_person.mc_title]!"
    call fuck_person(the_person, start_position = breeding_missionary, start_object = bedroom.get_object_with_name("bed"), skip_intro = False, girl_in_charge = False, position_locked = True, skip_condom = True) from _VT_breeding_fetish_sarah_intro_05
    if the_person.has_creampie_cum:
        the_person "Oh my god... we actually did it..."
        "She grabs an extra pillow and puts it under her butt so her hips are elevated."
        the_person "I'm just going to lay her like this for a bit, you know. Keep that seed nice and deep."
    else:
        mc.name "I'm sorry, I really want to, I'm just really tired."
        "You can tell she is a little disappointed."
        the_person "That's okay. Maybe in the morning?"
    "You snuggle up with [the_person.possessive_title]. Your have turned her into your personal breeding mare."
    $ VT_add_breeding_fetish(the_person)
    call Sarah_spend_the_night() from VT_breeding_fetish_sarah_intro_overnight_15

    return #Needs testing

label VT_breeding_fetish_ophelia_intro_label():
    "Ophelia doesn't have a breeding fetish written yet"
    return

label VT_breeding_fetish_erica_intro_label():
    $ the_person = erica
    $ the_person.fertility_percent = 20.0
    $ mc.start_text_convo(the_person)
    if the_person.is_girlfriend:
        the_person "Hey! Can you come over? It's supposed to be cold out and it would be nice to have you help keep my bed warm... Plus I kinda want to talk to you about something!"
    else:
        the_person "Hey... Can you come over tonight? I have something I need to talk to you about..."
    "You don't really have anything going on..."
    mc.name "Sure, I'm on my way over."
    $ mc.end_text_convo()
    $ mc.change_location(the_person.home)
    "You swing by [the_person.possessive_title]'s. You knock on the door and soon she opens it."
    $ the_person.draw_person()
    the_person "Hi! Come in..."
    "You follow her inside. She motions you to her table, so you sit down."
    the_person "Can I get you anything? Coffee?"
    mc.name "Am I going to need the caffeine?"
    "You answer, making your flirting tone obvious. She gives you a shy smile."
    the_person "Hopefully! I'm hoping this will be a long and productive night..."
    mc.name "Coffee sounds great."
    "You can already smell it, so she must already have a pot brewed."
    $ the_person.draw_person(position = "back_peek")
    "[the_person.possessive_title!c] turns to the counter and grabs a couple of cups. She pours two, then turns and sits down across from you, setting your cup in front of you."
    $ the_person.draw_person(position = "sitting")
    "[the_person.title] looks nervous. Whatever it is she wants to talk about, you can tell it's making her anxious. You take a sip of your coffee."
    mc.name "So... What's eating you? I mean, besides me later..."
    "She gives a nervous sigh."
    the_person "Okay... So... I've kind of... Been thinking about something..."
    "Her purse is sitting on the table next to her. She opens it up and starts to go through it. She pulls out a package of birth control pills, and a package of plan B."
    the_person "A while back I had my IUD removed due to a medical complication and switched to regular birth control."
    mc.name "I hope you are okay?"
    the_person "Yes, I'm fine, but I stopped taking them too lately..."
    the_person "I told myself it was just for the thrill of the risk, but if anything ever actually happened, I had plan B ready, and if that ever didn't work, you know... I was gonna get it taken care of."
    the_person "I love running track and field. But if I ever got pregnant..."
    the_person "I know they can't legally kick me off the team, but the coach is a real bitch!"
    the_person "Last time a girl got knocked up, they kicked her off for 'scholastic misconduct' to get around the law."
    the_person "I didn't want that to be me, you know? So I did what I had to..."
    if the_person.is_girlfriend:
        the_person "But [the_person.mc_title], I just love you so much! The urge to just let go of all that, and just submit myself to you over and over, taking your seed! It's so so strong!"
    else:
        the_person "But lately, when I'm with you... And even when I'm not, I can't stop fantasizing about you cumming inside me. Over and over, not letting me take my pills and knocking me up!"
    "It's been a while since you started dosing [the_person.possessive_title] with Reproduction Proclivity Nanobots. It seems they have taken hold of her."
    the_person "I knew that when girls get to about my age they could get baby fever... But I never imagined the urge would be so strong! [the_person.mc_title]... I don't care about the track team anymore! Please knock me up! Will you please?"
    "There is some significant urgency in her voice. [the_person.possessive_title!c] is willing to give up her sports team, just to have your babies! This is a total no-brainer."
    "You reach over the table, and pick up her birth control. You stand up, take it to the trash can, and throw it away. She observes your movements closely."
    the_person "You just... Does that mean?"
    mc.name "Lie down on the table, [erica.fname]."
    the_person "Oh! Oh my god..."
    $ the_person.draw_person(position = "missionary")
    if the_person.vagina_available:
        "You reach down and pull your cock out from your pants."
    else:
        "As you start to pull your cock out, [the_person.possessive_title] reaches down and starts pulling her bottoms off."
        $ the_person.strip_to_vagina(prefer_half_off = True, position = "missionary")
    "You grab her hands and force them down at her sides. She looks at you longingly as your bare cock nears her cunt."
    "You don't say a word, you just push forward, sliding yourself into her fertile young pussy."
    $ the_person.change_arousal (20)
    $ mc.change_locked_clarity(50)
    $ the_person.break_taboo("condomless_sex")
    $ the_person.break_taboo("vaginal_sex")
    the_person "Oh god! Yes! Make me cum and fill me up [the_person.mc_title]."
    "Still holding her hands down, you start to thrust rapidly. It's time to give this horny slut a creampie!"
    call fuck_person(the_person, start_position = breeding_missionary, start_object = make_table(), private = True, skip_intro = True, position_locked = True, skip_condom = True) from _VT_breeding_fetish_erica_intro_01
    $ the_person.draw_person(position = "missionary")
    if the_person.has_creampie_cum:
        $ become_pregnant(the_person, breeder_announce = True)
        the_person "Oh god! It's amazing. I think you did it. I don't know how I know... I can just feel it."
        "She rubs her belly happily."
        the_person "I mean... I'll take a test in a few days to be sure but..."
    else:
        the_person "That's... you didn't finish?"
        mc.name "I'm sorry [the_person.title]. It's been a long day, and I'm just too tired."
        the_person "Seriously? After all our training and everything..."
        $ the_person.change_love(-5)
        the_person "I think you should go."
        mc.name "I'm sorry, we can try again..."
        the_person "Damn right we'll try again! But tonight I just need to be mad. Now get out!"
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
    "[the_person.title] stands up and smiles at you."
    the_person "I'll let you know when I find out for sure... daddy!"
    "You say goodnight and head home. It seems that you have given [the_person.possessive_title] a breeding fetish! You look forward to many creampies in your future together."
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
    "As you slowly start to wake up, you feel the weight on your bed shift a little bit."
    if mom.sluttiness > 60:
        "You assume it's probably [mom.title], coming in to give you another pleasant wake-up call, but as your brain slowly engages, you realise the weight of the person is different."
    else:
        "Thinking you are probably still dreaming, your brain is slow to engage and register what is going on."
    "Your pants slide off, exposing your morning wood. You feel a weight around your hips as someone gets on top of you. You slowly open your eyes."
    $ the_person.draw_person(position = "cowgirl")
    "It's... [the_person.possessive_title]!?!"
    mc.name "Wha? [the_person.title]?"
    the_person "Shhh, don't want to wake your family..."
    "She slowly slides herself down onto you, taking your full length inside her. You can't help but moan at the sudden sensation."
    $ the_person.break_taboo("condomless_sex")
    $ the_person.break_taboo("vaginal_sex")
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(50)
    mc.name "What are you doing here?"
    the_person "I've been tracking my cycles and I am soooo fertile right now. I understand you were too tired last night, but I need your cum ASAP."
    "[the_person.possessive_title!c] starts to work her hips. You know you should be concerned about how she even got in here, but right now you decide to just lie back and enjoy."
    call get_fucked(the_person, the_goal = "vaginal creampie", start_position = cowgirl, private = True, skip_intro = True, allow_continue = False) from _call_get_fucked_VT_breeding_fetish_erica_unsuccessful_followup_02
    "When you finish, she rolls off you and lies beside you on your bed."
    $ the_person.draw_person(position = "missionary")
    $ VT_add_breeding_fetish(the_person)
    $ become_pregnant(the_person, breeder_announce = True)
    the_person "Oh god! It's amazing. I think you did it. I don't know how I know... I can just feel it."
    "She rubs her belly happily."
    the_person "I mean... I'll take a test in a few days to be sure but..."
    "She lies beside you for a minute, but then quietly gets up. She puts on some clothes you didn't even realise she had with her."
    $ the_person.apply_planned_outfit(show_dress_sequence = True)
    the_person "I'll let you know when I find out for sure... daddy!"
    "She seems positively glowing."
    "Quietly, she leaves your room."
    "Did that just happen? You feel groggy. Looking down, you see your limp cock, still slick from her juices. Huh, that must have happened."
    "How did she even get in? You have so many questions, but for now, you just get up and start your regular morning routine."
    $ the_person.add_unique_on_room_enter_event(
        Action("Erica knocked up followup", VT_erica_breeding_fetish_followup_requirement, "erica_breeding_fetish_followup_label")
    )
    return


label VT_breeding_fetish_candace_intro_label(the_person): #This is going to be two intros, depending on if candace is still a bimbo or not NEeds Testing
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
    "You feel your phone go off when you get a notification. It's a message from [the_person.possessive_title]."
    $ mc.start_text_convo(the_person)
    the_person "Hey, can you PLEASE come to the café tonight? It'll be worth it... I promise!"
    mc.name "Oh? What do you need?"
    the_person "It involves The Sims. It'll be worth it, just cum!"
    "You can't help but notice her spelling."
    mc.name "Alright, I'm on my way."
    $ mc.end_text_convo()
    $ mc.change_location(gaming_cafe)
    $ the_person.apply_outfit(Outfit("Nude"))
    "When you get to the gaming café, you find it unlocked. You let yourself in, then lock the door."
    if myra_lewd_cafe_open():
        "You head to the back and into the adults–only section."
    else:
        "You head to the back where you've played a lewd version of The Sims with [the_person.title]"
    $ the_person.draw_person()
    the_person "Hey! You came!"
    mc.name "Of course. And I can see I am a bit overdressed. Are we playing The Sims tonight?"
    "You start to undress."
    the_person "Yeah! I don't know why, but I'm feeling pretty lucky about the way the game finishes tonight..."
    "[the_person.possessive_title!c] is definitely acting a bit odd. She is pretty forward about things, so you shouldn't be surprised she called you here this late."
    "However, you can't help shake the feeling that she has rigged this somehow."
    "You've been dosing her with Vitamin D alot recently. Maybe she is developing a breeding fetish?"
    "You step out of the last of your clothes and look up. [the_person.possessive_title!c] is looking at your hungrily."
    the_person "Fuck you look so... virile... let's get this going!"
    call myra_sex_roulette_session_label(the_person, breeding_fetish_intro = True) from _call_VT_breeding_fetish_myra_intro
    "When you finish, she just stands there, running her hands over her belly."
    "She obviously intended for you to cum inside her from the moment she texted you."
    if the_person.knows_pregnant:
        the_person "No wonder I'm pregnant... there is nothing as amazing as taking a hot load of cum."
    else:
        the_person "Oh god, that was fucking amazing. Do you think... maybe it really knocked me up?"
    "It seems obvious now. After giving her multiple serums, [the_person.possessive_title] has developed a breeding fetish."
    "Even now you see her looking at your cock, trying to decide if she can milk another load from it."
    mc.name "You love it, don't you? You want to be by personal cum dumpster, to take my loads anytime and anywhere I want you to?"
    the_person "Oh god yes..."
    mc.name "You're going to love it, aren't you? When you show up for a tournament, your belly round, your big tits leaking milk. Everyone there is gonna know what a needy cunt you have."
    the_person "Yes!"
    mc.name "Everyone there is going to know you are a hopeless, thirsty slut. You long for your master's cum sloshing around in your fertile womb all day long."
    "[the_person.possessive_title!c]'s knees start to buckle for a second."
    the_person "Yes please! Breed me again PLEASE?"
    mc.name "I plan to. Keep your cunt ready for me, anytime I want to dump my load inside you."
    the_person "Yes! Don't worry, I'll be ready!"
    "You say goodbye to [the_person.title]."
    "[the_person.possessive_title!c] now has a fetish to get bred by you!"
    "If you re-enact a scene from The Sims in the future, she may also decide to force you to cum inside her too..."
    $ VT_add_breeding_fetish(the_person)
    $ mc.change_location(bedroom)
    "You walk home and collapse into your bed. You can't wait to fill [the_person.possessive_title]'s needy cunt with your cum, over and over again."
    return

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
