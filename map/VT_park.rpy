#used Kaden's Beach code as a template
init -1 python:
     def vt_can_add_clothing(outfit, new_clothing):
        if new_clothing in dress_list:
            if outfit.can_add_dress(new_clothing):
                return True
        elif new_clothing in shirts_list or new_clothing in bra_list:
            if outfit.can_add_upper(new_clothing):
                return True
        elif new_clothing in pants_list or new_clothing in skirts_list or new_clothing in panties_list:
            if outfit.can_add_lower(new_clothing):
                return True
        elif new_clothing in socks_list or new_clothing in shoes_list:
            if outfit.can_add_feet(new_clothing):
                return True
        elif new_clothing in earings_list or new_clothing in bracelet_list or new_clothing in rings_list or new_clothing in neckwear_list:
            if outfit.can_add_accessory(new_clothing):
                return True
        return False

     def vt_add_clothing(outfit, new_clothing, re_colour = None, pattern = None, colour_pattern = None):
        if vt_can_add_clothing(outfit, new_clothing):
            if new_clothing in dress_list:
                outfit.add_dress(new_clothing, re_colour = None, pattern = None, colour_pattern = None)
            elif new_clothing in shirts_list or new_clothing in bra_list:
                outfit.add_upper(new_clothing, re_colour = None, pattern = None, colour_pattern = None)
            elif new_clothing in pants_list or new_clothing in skirts_list or new_clothing in panties_list:
                outfit.add_lower(new_clothing, re_colour = None, pattern = None, colour_pattern = None)
            elif new_clothing in socks_list or new_clothing in shoes_list:
                outfit.add_feet(new_clothing, re_colour = None, pattern = None, colour_pattern = None)
            elif new_clothing in earings_list or new_clothing in bracelet_list or new_clothing in rings_list or new_clothing in neckwear_list:
                outfit.can_add_accessory(new_clothing, re_colour = None, pattern = None, colour_pattern = None)
        return

     def vt_generalised_dressing_description(the_person, outfit, group_display = None, other_people = None, position = None):
        scene_manager = Scene()
        for cloth in [x for x in the_person.outfit.upper_body + the_person.outfit.lower_body + the_person.outfit.feet + the_person.outfit.accessories if x.half_off]:
            cloth.half_off = False
            scene_manager.add_actor(the_person)
            renpy.say(None, the_person.title + " adjusts her " + cloth.display_name + ", restoring it to the way it is normally worn.")
        if isinstance(outfit, Clothing):
            temp_list = [temp_list] #Lets you hand over a single item to put on
        else:
            temp_list = []
            for item in outfit.get_full_strip_list():
                temp_list.append(item)
        test_outfit = the_person.outfit.get_copy() #Use a copy to keep track of what's changed between iterations, so we can narrate tits being out, etc.
        loop_count = 0 #Used to keep all of the other people on the same track as the main stripper
        for item in list(reversed(temp_list)):
            if group_display is not None:
                if vt_can_add_clothing(the_person.outfit, item):
                    vt_add_clothing(the_person.outfit, item)
                group_display.redraw_group()
                if other_people is not None:
                    for person_tuple in other_people:
                        another_person = person_tuple[0]
                        another_temp_list = person_tuple[1]
                        if item == temp_list[-1]:
                            if vt_can_add_clothing(another_person.outfit, another_temp_list):
                                vt_add_clothing(another_person.outfit, another_temp_list)
                        elif len(another_temp_list) > loop_count:
                            if vt_can_add_clothing(another_person.outfit, another_temp_list[loop_count]):
                                vt_add_clothing(another_person.outfit, another_temp_list[loop_count])
                        group_display.redraw_group()
            else:
                if vt_can_add_clothing(the_person.outfit, item):
                    vt_add_clothing(the_person.outfit, item)
                    scene_manager.update_actor(the_person)
                    if test_outfit.tits_available and not the_person.tits_available: #Tits are contained
                        if the_person.has_large_tits:
                            renpy.say(None, the_person.title + " pulls on her " + item.display_name + ", covering her " + the_person.tits_description + ".")
                        else:
                            renpy.say(None, the_person.title + " puts on her " + item.display_name + " concealing her " + the_person.tits_description + ".")
                    elif test_outfit.tits_visible and not the_person.outfit.tits_visible: #Tits are fully covered
                        if the_person.has_large_tits:
                            renpy.say(None, the_person.title + " pulls on her " + item.display_name + ", hiding away all trace of her " + the_person.tits_description + ".")
                        else:
                            renpy.say(None, the_person.title + " dons her " + item.display_name + ", hiding away her " + the_person.tits_description + ".")
                    elif test_outfit.vagina_available and not the_person.vagina_available: #Pussy contained
                        if item.underwear:
                            renpy.say(None, the_person.title + " slips on her " + item.display_name + ", adjusting them to cover her " + the_person.pubes_description + " pussy.")
                        else:
                            renpy.say(None, the_person.title + " puts on her " + item.display_name + " hiding her " + the_person.pubes_description + " pussy underneath.")
                    elif test_outfit.vagina_visible and not the_person.outfit.vagina_visible: #Pussy fully covered
                        renpy.say(None, the_person.title + " puts on her " + item.display_name + ", covering her " + the_person.pubes_description + " pussy.")
                    elif item.layer == 2:
                        if test_outfit.wearing_panties and pelvis_region in item.half_off_regions:
                            renpy.say(None, the_person.title + " puts on her " + item.display_name + ", covering her " + test_outfit.get_panties().display_name + ".")
                        elif test_outfit.wearing_bra and torso_region in item.half_off_regions:
                            renpy.say(None, the_person.title + " puts on her " + item.display_name + ", concealing her " + test_outfit.get_bra().display_name + ".")
                    else:
                        rand = renpy.random.randint(0,3)
                        if rand == 0:
                            renpy.say(None, the_person.title + " slips on her " + item.display_name + ".")
                        elif rand == 1:
                            renpy.say(None, the_person.title + " puts on her " + item.display_name + ".")
                        elif rand == 2:
                            renpy.say(None, the_person.title + " slips her " + item.display_name + " on.")
                        else:
                            renpy.say(None, the_person.title + " pulls on her " + item.display_name + ".")
                    if vt_can_add_clothing(test_outfit, item):
                        vt_add_clothing(test_outfit, item) #Update our test outfit.
                    loop_count += 1
                    if group_display is not None: #This is needed to ensure the animation times for the clothing fade out are reset. Not ideal for a speedy draw, but it'll do for now.
                        scene_manager.clear_scene()
                        group_display.redraw_group()
        return

init 16 python:
    def vt_select_action(person):
        roll = random.randint(1, 3)

        if roll == 1 and person.is_willing(anal_standing) and not person.has_taboo("anal_sex"):
            return "anal_standing"
        elif roll == 2 and person.is_willing(standing_doggy) and not person.has_taboo("vaginal_sex"):
            return "standing_doggy"
        elif roll == 3 and person.is_willing(blowjob) and not person.has_taboo("sucking_cock"):
            return "blowjob"
        else:
            # If the selected action is not possible, try the other two
            if roll == 1:
                if person.is_willing(standing_doggy) and not person.has_taboo("vaginal_sex"):
                    return "standing_doggy"
                elif person.is_willing(blowjob) and not person.has_taboo("sucking_cock"):
                    return "blowjob"
            elif roll == 2:
                if person.is_willing(anal_standing) and not person.has_taboo("anal_sex"):
                    return "anal_standing"
                elif person.is_willing(blowjob) and not person.has_taboo("sucking_cock"):
                    return "blowjob"
            elif roll == 3:
                if person.is_willing(anal_standing) and not person.has_taboo("anal_sex"):
                    return "anal_standing"
                elif person.is_willing(standing_doggy) and not person.has_taboo("vaginal_sex"):
                    return "standing_doggy"
            # If none of the actions are possible, return None
            return "Not happening"

    def vt_select_action_grope_finger_bj(person):
        roll = random.randint(1, 3)
        if roll == 1 and person.is_willing(standing_grope) and not person.has_taboo("touching_body"):
            return "standing_grope"
        elif roll == 2 and person.is_willing(standing_finger) and not person.has_taboo("touching_vagina"):
            return "standing_finger"
        elif roll == 3 and person.is_willing(blowjob) and not person.has_taboo("sucking_cock"):
            return "blowjob"
        else:
            # If the selected action is not possible, try the other two
            if roll == 1:
                if person.is_willing(standing_finger) and not person.has_taboo("touching_vagina"):
                    return "standing_finger"
                elif person.is_willing(blowjob) and not person.has_taboo("sucking_cock"):
                    return "blowjob"
            elif roll == 2:
                if person.is_willing(standing_grope) and not person.has_taboo("touching_body"):
                    return "standing_grope"
                elif person.is_willing(blowjob) and not person.has_taboo("sucking_cock"):
                    return "blowjob"
            elif roll == 3:
                if person.is_willing(standing_grope) and not person.has_taboo("touching_body"):
                    return "standing_grope"
                elif person.is_willing(standing_finger) and not person.has_taboo("touching_vagina"):
                    return "standing_finger"
            # If none of the actions are possible, return None
            return "Not happening"

    def park_is_open():
        if time_of_day == 0:
            park.background_name = "Park_Early_Morning_Background"
        elif time_of_day == 1:
            park.background_name = "Park_Morning_Background"
        elif time_of_day == 2:
            park.background_name = "Park_Afternoon_Background"
        elif time_of_day ==3:
            park.background_name = "Park_Evening_Background"
        elif time_of_day ==4:
            park.background_name = "Park_Night_Background"
        
        if day==0:
            return time_of_day in (0,1, 2, 3,4) and day != 0
        else:
            return time_of_day in (0,1,2,3, 4)
        #add other events here to trigger

    def park_date_invite_requirement():
        if time_of_day in [1,2,3]:
            if get_park_date_person():
                return True
        return False

    def get_park_date_person():
        temp_list = []
        for person in known_people_in_the_game():
            if person.energy > 60 and person.is_available:
                    if 40 < person.love < 70:
                        if person.relationship == "Single" or person.has_role(girlfriend_role) or person.has_role(affair_role):
                            if not person.is_at_work:
                                temp_list.append(person)
        return get_random_from_list(temp_list)

    park_date_invite = ActionMod("Park Date Invite", park_date_invite_requirement, "park_date_invite_label",
        menu_tooltip = "Someone invites you to go to the park with them.", category = "Mall", is_crisis = True, is_morning_crisis = False, priority = 5)

init 16 python:
    def park_get_choice(person):
        exhibition_score = (person.opinion.public_sex + person.opinion.not_wearing_anything + person.opinion.showing_her_tits + person.opinion.showing_her_ass)/4.0
        tan_score = person.get_opinion_score("yoga") + exhibition_score
        sport_score = person.get_opinion_score("sports") + exhibition_score
        public_score = person.get_opinion_score("hiking") + exhibition_score
        walk_score = person.get_opinion_score("hiking") - exhibition_score
        park_list = []
        park_list.append([tan_score, "tan_score"])
        park_list.append([sport_score, "sport_score"])
        park_list.append([public_score, "public_score"])
        park_list.append([walk_score, "walk_score"])
        choice = max(park_list)
        return choice

    def get_park_outfit(person, outfit_type = "full"):
        
        park_outfit = Outfit("Park")
        vt_outfit_modifier = 0
        if person.has_broken_taboo("bare_tits"):
            vt_outfit_modifier +=5
        if person.has_broken_taboo("bare_pussy"):
            vt_outfit_modifier +=5
        if person.has_exhibition_fetish:
            vt_outfit_modifier +=10
        if person.has_cum_fetish:
            vt_outfit_modifier +=10
        if person.has_anal_fetish:
            vt_outfit_modifier +=10
        if person.has_breeding_fetish:
            vt_outfit_modifier +=10
        
        park_outfit = Wardrobe.generate_random_appropriate_outfit(person, outfit_type = "full", opinion_color = person.favourite_colour,sluttiness_limit = the_person.effective_sluttiness() + int(vt_outfit_modifier), allow_skimpy = person.effective_sluttiness() > 30)
        return park_outfit

    Person.get_park_outfit = get_park_outfit


init 30 python:
    park = Room("park", "Public Park", "Park_Afternoon_Background", [make_floor(), make_bench()],
            actions = [], map_pos = [1,1], lighting_conditions = standard_outdoor_lighting, privacy_level = 3, allow_walk_in = True, accessible_func = park_is_open)

    park_bush = Room("park_bush", "Park Bushes", "Park_Bushes_Background", make_floor(),
            actions = [],  map_pos = [2,1], lighting_conditions = standard_outdoor_lighting, darken = True, privacy_level = 2, allow_walk_in = True, accessible_func = park_is_open)

    park_bush_secluded = Room("park_bush_secluded", "Park Secluded Area", "Park_Bushes_Background", make_floor(),
            visible = False, lighting_conditions = standard_outdoor_lighting, darken = True,
            actions = [], map_pos = [2,2],  privacy_level = 1 )

    park_hub = MapHub("park_hub", "Public Park", icon = "POI_Park", position = Point(890, 450), locations = [park, park_bush, park_bush_secluded], accessible_func = park_is_open)

    #### note on co-ordinates-  1200, 700... ( first number is from left of screen, second is from top of screen)
  
    def park_initialization(self):
        list_of_places.append(park)
        list_of_places.append(park_bush)
        list_of_places.append(park_bush_secluded)
        list_of_hubs.append(park_hub)
        park.add_action(park_wrapper_action)
        return

    park_wrapper_action = ActionMod("Spend time in the park {image=gui/heart/Time_Advance.png}", park_is_open, "select_person_for_park",
        initialization = park_initialization, menu_tooltip = "Bring a person to the park.", category = "Misc")

label select_person_for_park():
    call screen main_choice_display(build_menu_items(
        [get_sorted_people_list(known_people_in_the_game(), "Spend time with", "Back")]
        ))
    $ the_person = _return
    if the_person != "Back":
        "You send a text message to [the_person.title] about spending some time at the park."
        "A moment later you get a response..."
        call select_person_for_park_response(the_person) from _call_select_person_for_park_response
        call advance_time from _call_advance_time_park
    return

label select_person_for_park_response(the_person):
    $ scene_manager = Scene()
    if the_person.location == park:
        the_person "Seriously, are you stalking me? I just got here."
        the_person "Where do you want to meet up?"
        mc.name "I'm at the South parking lot."
    elif the_person.happiness < 100 or the_person.obedience < 70:
        $ scene_manager.add_actor(the_person, temp_outfit, emotion = "sad")
        the_person "I'm not in the mood for the park, right now."
        $ the_person.change_obedience(-2)
        $ scene_manager.clear_scene()
        return
    if the_person.personality == bimbo_personality:
        the_person "Cumming right away, [the_person.mc_title]!"
    elif the_person.obedience > 140:
        the_person "Yes, Sir. I am on my way."
    elif the_person.sluttiness > 30:
        the_person "Yes, [the_person.mc_title]. I am on my way."
    elif the_person.happiness < 120 and the_person.love > 20:
        $ scene_manager.update_actor(the_person, emotion = "happy")
        the_person "Thanks for the attention, [the_person.mc_title]."
        $ the_person.change_stats(happiness = 10)
    else:
        the_person "Sounds good, I'll be right there, [the_person.mc_title]."
        $ the_person.change_stats(happiness = 10)
    call park_wrapper(the_person) from _call_park_wrapper_person_for_park
    $ scene_manager.clear_scene()
    return

label park_date_invite_label():
    $ scene_manager = Scene()
    $ the_person = get_park_date_person()
    if mc.is_at_work:
        "As you are packing up to head home for the day you get a text from [the_person.title]."
    elif mc.is_home:
        "As you are walking down the hallway in your house you get a text from [the_person.title]."
    else:
        "As you are wandering around you get a text from [the_person.title]."
    $ mc.start_text_convo(the_person)
    the_person "Hey [the_person.mc_title]! I just got to the park. Do you want to come hang out with me?"
    menu:
        "Go to the park":
            pass
        "Decline the date":
            mc.name "Sorry I can't right now. I've got other plans."
            the_person "Oh, okay, but you're really missing out."
            $ park.show_background()
            $ scene_manager.add_actor(the_person, get_park_outfit(the_person), emotion = "happy")
            "To emphasize her point she sends you a picture of her standing in a sunny spot in the park."
            $ mc.change_locked_clarity(the_person.sluttiness/5)
            "It is tempting to change you mind, but you commit to your original decision. Maybe next time you are downtown you could invite her to the park."
            mc.name "I know, but I really do have things to do."
            the_person "Alright, your loss!"
            $ mc.location.show_background()
            $ mc.end_text_convo()
            $ scene_manager.clear_scene()
            $ the_person.apply_planned_outfit()
            return
    mc.name "Yeah, that sounds great. I can be there soon."
    the_person "Great! I'll be waiting by the picnic tables for you."
    mc.name "See you soon."
    $ mc.end_text_convo()
    "A little while later you walk into the park."
    call park_wrapper(the_person) from _call_park_wrapper_invite
    $ scene_manager.clear_scene()
    return

label park_wrapper(the_person):
    $ scene_manager = Scene()
    $ choice = None
    $ mc.change_location(park)
    if not the_person in park.people:
        $ the_person.change_location(park)
    $ temp_outfit = get_park_outfit(the_person)
    $ scene_manager.add_actor(the_person, temp_outfit, emotion = "happy")
    "Once you see [the_person.title], you walk up to her."
    mc.name "Hey, [the_person.title], it's good to see you."
    the_person "Hi, [the_person.mc_title] I'm so glad to be in the park. What do you want to do?"
    menu:
        "Pick an activity" if the_person.love + the_person.obedience > 150:
            menu:
                "Let's go for a walk":
                    the_person "That sounds like fun. Which way do you want to go?"
                    menu:
                        "Away from the crowd":
                            mc.name "Let's go for a walk and do some exploring, see what there is to see."
                            the_person "Alright. Lead the way."
                            $ choice = "Walk"
                        "The same way as everyone else":
                            mc.name "Let's go for a walk around the park; see what else is going on here."
                            the_person "Sounds good to me, lead the way!"
                            $ choice = "Public"
                "Let's play a game":
                    mc.name "How about we play a game, the weather seems perfect for it."
                    the_person "That sounds like a great idea [the_person.mc_title], lead the way!"
                    $ choice = "Playground"
                "Let's check out the picnic area":
                    mc.name "There are the picnic tables set up, let's go take a look at those."
                    the_person "Me versus you? Sounds like fun, let's go!"
                    $ choice = "Picnic"
                "Let's find a spot to chill out":
                    mc.name "I'm thinking we should find a nice sunny spot and just relax."
                    the_person "That sounds nice. Lead the way."
                    $ choice = "To Chill"
                "Let's get something to eat":
                    $ choice = "Change"
        "Let her pick":
            mc.name "Why don't you decide, I want you to have fun."
            $ the_person.change_stats(happiness = 5)
            if the_person.sluttiness < 30: #She is shy and we have work to do
                the_person "I'm not really sure, let's hang out up here, maybe get something to eat."
                menu:
                    "Yes\n{color=#ff0000}{size=18}Costs: $30{/size}{/color}" if mc.business.has_funds(30):
                        mc.name "Yes, that sounds good."
                        $ mc.business.change_funds(-30)
                        $ choice = "Change"
                    "Yes\n{color=#ff0000}{size=18}Requires: $30{/size}{/color} (disabled)" if not mc.business.has_funds(30):
                        pass
                    "No":
                        mc.name "Sorry, I'm a little short on cash."
                        the_person "What? You want to spend time with me and you don't have any money? Shouldn't you be at work then?"
                        $ the_person.change_stats(happiness = -10)
                        return
            else:
                $ [temp_number, her_choice] = park_get_choice(the_person)
                if her_choice == "tan_score":
                    the_person "Well, since we are here on such a nice day, let's lie down and relax."
                    mc.name "That sounds nice."
                    $ choice = "To Chill"
                elif her_choice == "sport_score":
                    if renpy.random.randint(0,1) == 1:
                        the_person "I think they have a playground here, let's go see if we can find something to play with."
                        mc.name "That sounds fun."
                        $ choice = "Playground"
                    else:
                        the_person "Well, the park is right there, let's have a picnic."
                        mc.name "Of course, that sounds great."
                        $ choice = "Picnic"
                elif her_choice == "public_score":
                    the_person "I'm not really sure, let's walk for a bit and see what is going on."
                    mc.name "Sure, that sounds relaxing."
                    $ choice = "Public"
                else: #walk
                    the_person "I want to see what is around, let's go exploring."
                    mc.name "That sounds exciting."
                    $ choice = "Walk"
    if choice == "Walk":
        call park_walk_label(the_person, temp_outfit) from _call_park_walk_label
    if choice == "Public":
        call park_public_label(the_person, temp_outfit) from _call_park_public_label
    if choice == "Playground":
        call park_game_label(the_person, temp_outfit) from _call_park_game_label
    if choice == "Picnic":
        call park_picnic_label(the_person, temp_outfit) from _call_park_picnic_label
    if choice == "To Chill":
        call park_to_chill_label(the_person, temp_outfit) from _park_to_chill_label_label
    if choice == "Change":
        call park_change_label(the_person, temp_outfit) from _call_park_change_label
    if the_person.has_role(trance_role):
        call check_date_trance(the_person) from _call_check_date_trance_park
    the_person "Thank you, [the_person.mc_title]."
    mc.name "Bye [the_person.title], see you next time."
    $ scene_manager.update_actor(the_person, position="walking_away")
    $ the_person.apply_planned_outfit()
    # $ mc.change_location(downtown)
    # $ scene_manager.clear_scene()
    if time_of_day == 4:
        $ mc.change_location(bedroom)
        $ scene_manager.clear_scene()
        call advance_time() from vt_call_advance_time_park_wrapper_latenight
    else:
        call advance_time() from vt_call_advance_time_park_wrapper
    return

label park_walk_label(the_person, temp_outfit):
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person, temp_outfit, emotion = "happy")
    "You pick one direction along the park path and walk hand in hand with [the_person.title]. You pass by the playground, taking a moment to watch some kids playing."
    "Past that, the path gets narrower and narrower, the trees coming closer together on either side."
    "Soon you've left the crowds behind, with only the occasional stranger passing by. [the_person.title] steps closer to you and takes your hand in hers."
    the_person "Thank you for coming out here with me [the_person.mc_title]."
    mc.name "No problem at all [the_person.title]. It's my pleasure."
    the_person "I'm sure it is, you've been staring at me in this outfit all day."
    mc.name "Guilty as charged. You look great in it."
    "[the_person.title] giggles and pulls closer to you, pressing up against your arm while you walk."
    "Eventually you come to a small clearing that runs off the main path, blocking your way."
    mc.name "I guess this is the end of the road. Come on, let's head back."
    if the_person.sluttiness > 30:
        $ scene_manager.update_actor(the_person, position = "walking_away")
        "[the_person.title] lets go of your hand and heads over to the clearing, walking through the trees to get a better view."
        the_person "Oh cool, there's a little stream back here. Come on, we can just follow it for a bit."
        mc.name "Fine, just be a little careful."
        $ scene_manager.strip_to_underwear(the_person, visible_enough = False)
        $ scene_manager.update_actor(the_person)
        "You follow [the_person.title] and walk through the trees until you can clear the underbrush, then head up the stream onto the other side. You find a small waterfall; twenty feet of private space with a short cliff blocking the far side."
        the_person "This is great! It's so private back here. In fact..."
        $ vt_selected_action = vt_select_action(the_person)
        
        if vt_selected_action == "anal_standing": # needs a better intro
            "[the_person.title] presses herself against you before you can even get clear of the trees, wrapping her arms around your waist and grinding her hips against yours."
            $ scene_manager.update_actor(the_person, position = "stand2")
            the_person "Mmm, I can feel how hard you are already. I'm sorry I've been teasing you all day with this outfit."
            "You wrap your arms around [the_person.possessive_title], hands on her ass. You give her a quick spank, making her gasp."
            $ the_person.slap_ass()
            mc.name "You aren't sorry, and I know it."
            "She giggles and nods, pressing her tits against your chest."
            $ mc.change_locked_clarity(5)
            the_person "I'm not, but I want to do something about it now that we have the chance."
            $ mc.change_arousal(10)
            $ the_person.change_arousal(10)
            "[the_person.title] reaches for your pants and pulls them down, your hard cock springing free to rub against her stomach."
            "She gasps and runs a finger along its length."
            the_person "Oh, it's so big... Here, I know exactly what you want."
            "She spins around in your grip and bends forward, grinding her ass against you now."
            $ scene_manager.strip_to_vagina(the_person, visible_enough = True, prefer_half_off = True, delay = 1)
            "You hook a finger under [the_person.title]'s tiny panties and pull them to the side. She moans softly when you rub the tip of your cock against her pussy."
            mc.name "I think you want this just as badly as me, right? You're dripping wet already."
            $ mc.change_arousal(10)
            $ the_person.change_arousal(10)
            "[the_person.title] moans louder and nods."
            the_person "Go ahead, please. I want you to fuck me."
            "[the_person.title] wiggles her ass at you, pressing her hips back a little so your wet tip starts to slide inside."
            "You pull back on [the_person.possessive_title]'s arms while you push forward, plunging your cock balls deep into her ass."
            the_person "Fuck! Ah!"
            call fuck_person(the_person, private = True, start_position = anal_standing, start_object = None, skip_intro = True, girl_in_charge = True, self_strip = False, hide_leave = False, position_locked = False, affair_ask_after = False, ignore_taboo = False, skip_condom = True) from _call_fuck_person_parkwalkanal
            mc.name "That felt great [the_person.title]. Thanks."
            the_person "It really did. Ah..."
            "You hang around by the waterfall for a few minutes while you both catch your breath, then head back through the trees again."
            $ vt_generalised_dressing_description(the_person, temp_outfit)
            "[the_person.title] takes your hand in hers while you take a slow stroll back to the center of the park."
        elif vt_selected_action == "standing_doggy":
            "[the_person.title] presses herself against you before you can even get clear of the trees, wrapping her arms around your waist and grinding her hips against yours."
            the_person "Mmm, I can feel how hard you are already. I'm sorry I've been teasing you all day with this outfit."
            "You wrap your arms around [the_person.possessive_title], hands on her ass. You give her a quick spank, making her gasp."
            $ the_person.slap_ass()
            mc.name "You aren't sorry, and I know it."
            "She giggles and nods, pressing her tits against your chest."
            $ mc.change_locked_clarity(5)
            the_person "I'm not, but I want to do something about it now that we have the chance."
            $ mc.change_arousal(10)
            $ the_person.change_arousal(10)
            "[the_person.title] reaches for your pants and pulls them down, your hard cock springing free to rub against her stomach."
            "She gasps and runs a finger along its length."
            the_person "Oh, it's so big... Here, I know exactly what you want."
            "She spins around in your grip and bends forward, grinding her ass against you now."
            $ scene_manager.strip_to_vagina(the_person, visible_enough = True, prefer_half_off = True, delay = 1)
            "You hook a finger under [the_person.title]'s tiny panties and pull them to the side. She moans softly when you rub the tip of your cock against her pussy."
            mc.name "I think you want this just as badly as me, right? You're dripping wet already."
            $ mc.change_arousal(10)
            $ the_person.change_arousal(10)
            "[the_person.title] moans louder and nods."
            the_person "Go ahead, please. I want you to fuck me."
            call condom_ask(the_person) from _call_condom_ask_park_walk
            if not _return:
                "[the_person.title]'s refusal has sucked the wind from your sails. You pull your pants back up."
                "At least you're no longer feeling as horny as you were, and you're able to focus on the scenery."
            else:
                "You plunge inside her, sliding your full length in on the first stroke."
                the_person "Oh fuck! Ah!"
                mc.name "God that feels good!"
                call fuck_person(the_person, private = True, start_position = standing_doggy, start_object = None, skip_intro = True, girl_in_charge = True, self_strip = False, hide_leave = False, position_locked = True, affair_ask_after = False, ignore_taboo = False, skip_condom = True) from _call_fuck_person_parkwalksex
                mc.name "That felt great [the_person.title]. Thanks."
                the_person "It really did. Ah..."
            "You hang around by the waterfall for a few minutes while you both catch your breath, then head back through the trees again."
            $ vt_generalised_dressing_description(the_person, temp_outfit)
            "[the_person.title] takes your hand in hers while you take a slow stroll back to the center of the park."
        elif vt_selected_action == "blowjob":
            $ scene_manager.update_actor(the_person, position = "kneeling1")
            "[the_person.title] turns back to you and drops to her knees; the sound of the waterfall is soothing in the background."
            the_person "Pull down your pants and let me give you a proper thank you for spending time with me out here."
            "She licks her lips and winks at you, then watches while you pull your cock out for her."
            mc.name "Here you go, is this what you wanted?"
            "She nods and runs a finger along your hard shaft, tracing its shape."
            $ mc.change_arousal(10)
            $ mc.change_locked_clarity(5)
            the_person "That's exactly what I wanted [the_person.mc_title]."
            "[the_person.title] leans forward and kisses the tip of your dick, then runs her tongue in circles around it. After getting it wet she bobs her head forward, slipping you into her mouth."
            mc.name "Oh fuck..."
            "[the_person.possessive_title!c] moans something in response, slowly sliding your cock in and out of her mouth."
            call get_fucked(the_person, the_goal = "get mc off", sex_path = None, private= True, start_position = blowjob, start_object = None, skip_intro = True, ignore_taboo = False, prohibit_tags = [], unit_test = False, allow_continue = False) from _call_get_fucked_parkwalkblow
            $ scene_manager.update_actor(the_person, position = "stand3")
            "She gets up off her knees and looks around the clearing."
            the_person "This place is nice, but we should probably head back soon if we want to do anything else today."
            mc.name "I suppose you're right. Come on, I'll lead."
            $ vt_generalised_dressing_description(the_person, temp_outfit)
            "You and [the_person.title] head back through the trees, joining up on the other side. She takes your hand in hers, and the two of you take a slow stroll back to the center of the park."
        else:
            "[the_person.title] looks around, then bites her lip and motions for you to come closer."
            the_person "I can see you're a bit worked up. That bulge in your pants doesn't leave much to the imagination. Just sit down, and let me take care of it for you as a way of saying thanks."
            $ scene_manager.update_actor(the_person, position = "kneeling1")
            "You sit down on a nearby rock next to [the_person.title] She gets down onto her knees and gives you a wink, running her hand over the bulge in your pants."
            mc.name "Here, let me get those out of the way for you."
            if mc.arousal < 30:
                $ mc.change_arousal(30)
            if the_person.has_taboo("touching_penis"):
                $ the_person.call_dialogue("touching_penis_taboo_break")
                $ the_person.break_taboo("touching_penis")
            else:
                "You pull your pants down, letting your hard cock free. [the_person.title] looks at it for a moment, then reaches out and takes it in her hand."
                the_person "It's so warm..."
            $ mc.change_locked_clarity(5)
            "[the_person.possessive_title!c] starts to stroke you off, running her hand up and down the length of your cock. You lean back and relax, enjoying the feeling for a few minutes."
            mc.name "That feels great [the_person.title] keep doing that."
            "She smiles and speeds up, playing idly with a breast while she jerks you off."
            call get_fucked(the_person, the_goal = "get mc off", sex_path = None, private= True, start_position = handjob, start_object = None, skip_intro = True, ignore_taboo = False, prohibit_tags = [], unit_test = False, allow_continue = False) from _call_get_fucked_parkwalkhand
            $ the_report = _return
            if the_person.has_mouth_cum or the_person.has_face_cum:
                the_person "Wow, that was hot."
                mc.name "Ah, yeah. Thanks [the_person.title]."
                $ scene_manager.update_actor(the_person, position = "walking_away")
                "She stands up and heads back to the stream, washing your semen off."
                $ temp_outfit.remove_all_cum()
            else:
                the_person "I'm sorry, [the_person.mc_title]."
                mc.name "It's okay, I appreciate the effort."
            $ vt_generalised_dressing_description(the_person, temp_outfit)
            $ scene_manager.update_actor(the_person, position = "stand3")
            the_person "No problem. We should probably start heading back if we want to have time to do something else."
            "You get up and join [the_person.possessive_title], heading back through the trees. From there the two of you take a slow stroll back to the center of the park."
    else:
        "[the_person.title] nods, and the two of you begin the slow stroll back to the center of the park."
        the_person "That didn't take too much time, do you want to get something to eat when we get back?"
        menu:
            "Yes\n{color=#ff0000}{size=18}Costs: $30{/size}{/color}" if mc.business.has_funds(30):
                mc.name "Yes, that sounds good."
                $ mc.business.change_funds(-30)
                call park_change_label(the_person, temp_outfit) from _call_park_change_label_walk
            "Yes\n{color=#ff0000}{size=18}Requires: $30{/size}{/color} (disabled)" if not mc.business.has_funds(30):
                pass
            "No":
                mc.name "Sorry, I'm a little short on cash."
                the_person "What? You want me to spend time with you and you don't have any money? Shouldn't you be at work then?"
                $ the_person.change_stats(happiness = -10)
    #$ scene_manager.clear_scene()
    return

label park_public_label(the_person, temp_outfit):
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person, temp_outfit, emotion = "happy")
    $ scene_manager.strip_to_underwear(the_person, visible_enough = False)
    "You pick a direction along the park path and start walking hand in hand with [the_person.title]."
    the_person "It's such a nice day out, we really got lucky."
    mc.name "Yeah, we did. I couldn't think of a better person to spend it with, either."
    the_person "Oh, very smooth. If I swoon will you catch me?"
    $ scene_manager.update_actor(the_person, position = "kissing")
    "She laughs and walks closer to you, wrapping one of her arms around yours."
    if the_person.effective_sluttiness(["bare_tits","bare_pussy"]) > 80 and not the_person.has_taboo("sucking_cock"):
        "After a few minutes of walking [the_person.title] slows down and lets go of your arm."
        mc.name "Everything alright?"
        $ scene_manager.strip_to_underwear(the_person, visible_enough = False)
        $ scene_manager.update_actor(the_person)
        if temp_outfit.get_bra():
            the_person "Yeah, I just need you to do me a favour. Pull on the knot for me, would you?"
            $ scene_manager.draw_animated_removal(the_person, temp_outfit.get_bra())
            "[the_person.title] spins around and presents the back of her outfit to you. You pull on the knot, and she proceeds to take the top off entirely."
            $ mc.change_locked_clarity(5)
            if temp_outfit.get_panties():
                "Next she pulls the bottom down and steps out of it. She turns back to you, completely naked."
                $ scene_manager.draw_animated_removal(the_person, temp_outfit.get_panties())
        elif temp_outfit.get_panties():
            the_person "Yeah, I just need to make a quick adjustment."
            $ scene_manager.draw_animated_removal(the_person, temp_outfit.get_panties())
            "She pulls her bottoms down and steps out of them, leaving herself completely naked."
        else:
            "BUG? What is she wearing?"
            $ naked_strip_description(the_person)
        $ mc.change_locked_clarity(5)
        the_person "There we go. If we're going to be walking around in the sun I don't want to end up with some ugly tan lines. Mind keeping these in your pocket?"
        "[the_person.title] hands over her outfit, then holds onto your arm again. You resume your walk through the park with [the_person.title]'s tits and pussy out in the open."
        "Not long after a group of guys further up the path notice her and begin whistling and cheering as she passes."
        the_person "Oh, I bet they want a piece of me. Just look at them."
        if the_person.opinion.showing_her_tits > 0:
            "[the_person.title] stops and turns towards them, cupping her breasts in her hands and playing with her nipples."
            $ mc.change_arousal(10)
            $ the_person.change_arousal(10)
            $ mc.change_locked_clarity(5)
            the_person "Is this what you want boys? Oh, I know it is!"
            "They cheer louder, thrusting their fists into the air in celebration."
            "[the_person.title] turns back to you and runs a finger down your chest. When she reaches the waistband of your pants she hooks it and pulls it down a little."
            the_person "I think we should give them a show they won't forget. Any objections?"
            mc.name "I think that's a great idea [the_person.title]."
        else:
            "[the_person.title] stops and turns to you."
            the_person "God, this got me so fucking horny. Can I suck you off, please?"
            "She reaches down and cups the bulge in your pants, rubbing it slowly."
            mc.name "I'd love that [the_person.title]."
        $ scene_manager.update_actor(the_person, position = "blowjob")
        "She drops to her knees and pulls your pants down low enough to free your hard cock."
        the_person "Oh, that looks nice. Let's have a taste."
        $ mc.change_locked_clarity(5)
        "[the_person.title] leans in and kisses the tip of your dick, then looks up at you while she slides it into her mouth."
        $ mc.change_arousal(10)
        $ the_person.change_arousal(10)
        mc.name "Damn, that feels great [the_person.title]."
        "She starts to blow you, bobbing her head up and down along your cock while she kneels on the grass. Up the path the cheering gets even louder."
        "You rest a hand on the back of [the_person.title]'s head and run your fingers though her hair. She speeds up with each pass, her warm throat drawing you quickly towards your orgasm."
        call fuck_person(the_person, private = False, start_position = blowjob, start_object = None, skip_intro = True, girl_in_charge = True, self_strip = False, hide_leave = False, position_locked = True, affair_ask_after = False, ignore_taboo = False, skip_condom = True) from call_fuck_person_parkpublicblow
        "You pull up your pants and look around. The group of guys are cheering louder than ever, phones out while they take pictures of you and [the_person.title]. Other small groups of people have noticed as well, and are watching the two of you."
        mc.name "Come on, we should get going before someone comes along and gets us in any trouble."
        the_person "Right. Let's go."
        "She gets back onto her feet and takes your hand. You hurry up the path until you've left the crowds behind."
        if the_person.has_mouth_cum or the_person.has_face_cum and not the_person.has_cum_fetish:
            "[the_person.title] takes a quick trip to a nearby fountain, washing your cum off of her face before you keep going."
            $ temp_outfit.remove_all_cum()
        "Soon you come to the end of the park, where the path is just a narrow strip next to the trees."
        the_person "I guess that's all there is to see this way. I'm going to get dressed again, and then we can head back and do something else."
        $ vt_generalised_dressing_description(the_person, temp_outfit)
    elif the_person.effective_sluttiness(["bare_tits","bare_pussy"]) > 60:
        "After a few minutes of walking [the_person.title] slows down and lets go of your arm."
        mc.name "Everything alright?"
        if len(temp_outfit.get_upper_ordered()) > 1:
            $ generalised_strip_description(the_person, temp_outfit.get_upper_top_layer)
        if len(temp_outfit.get_lower_ordered()) > 1:
            $ generalised_strip_description(the_person, temp_outfit.get_lower_top_layer)
        if temp_outfit.get_bra():
            the_person "Yeah, I just need you to do me a favour. Pull on the knot for me, would you?"
            $ scene_manager.draw_animated_removal(the_person, temp_outfit.get_bra())
            "[the_person.title] spins around and presents the back of her swimsuit to you. You pull on the knot, and she proceeds to take the top off entirely."
            $ mc.change_locked_clarity(5)
            if temp_outfit.get_panties():
                "Next she pulls the bottom down and steps out of it. She turns back to you, completely naked."
                $ scene_manager.draw_animated_removal(the_person, temp_outfit.get_panties())
        elif temp_outfit.get_panties():
            the_person "Yeah, I just need to make a quick adjustment."
            $ scene_manager.draw_animated_removal(the_person, temp_outfit.get_panties())
            "She pulls her bottoms down and steps out of them, leaving herself completely naked."
        else:
            "BUG? What is she wearing?"
            $ naked_strip_description(the_person)
        $ mc.change_locked_clarity(5)
        the_person "There we go. If we're going to be walking around in the sun I don't want to end up with some ugly tan lines. Mind keeping these in your pocket?"
        "[the_person.title] hands over her bikini, then holds onto your arm again. You resume your walk down the beach with [the_person.title]'s tits and pussy out in the open."
        "Not long after a group of guys further up the beach notices her and begin whistling and cheering as she passes."
        the_person "Oh, I bet they want a piece of me. Just look at them."
        $ scene_manager.update_actor(the_person, position = "stand5")
        "She raises one arm and waves to them, bouncing her tits around a little bit while she's at it."
        mc.name "So that's why you wanted to take all that off, just so people could get a better look."
        the_person "Are you complaining? You get the best view in the house."
        $ scene_manager.update_actor(the_person, position = "kissing")
        "She cups a breast and pinches the hard nipple, rolling it between her thumb and forefinger."
        $ mc.change_locked_clarity(5)
        the_person "Ah... God I've gotten myself so wet..."
        $ mc.change_arousal(10)
        $ the_person.change_arousal(10)
        "[the_person.title] keeps walking, thighs held tightly together. After another ten minutes you've left most of the crowds behind, and she lowers her free hand to her pussy."
        $ scene_manager.update_actor(the_person, position = "walking_away")
        "She runs a finger along her slit a few times, then slips it in. She fingers herself as you walk, holding onto your arm tightly."
        the_person "Do you think those guys wanted to fuck me?"
        mc.name "Back there? Oh ya, they would have done it in a heart beat if you asked them."
        $ the_person.change_arousal(10)
        "[the_person.title] shivers against you, stumbling half a step as you walk."
        mc.name "They would have bent you over that beer cooler and fucked you raw."
        the_person "Oh god..."
        $ the_person.change_arousal(10)
        $ mc.change_locked_clarity(10)
        "She shivers again, and this time comes to a complete stop. You lean in close and whisper into her ear while she pumps a couple of fingers in and out of her cunt."
        mc.name "Then they would have cum all over you and left you there, so the whole world could see what a dirty slut you are."
        the_person "Ah!"
        $ the_person.have_orgasm()
        "[the_person.title] shouts out and wraps her free arm around you. Her hips buck a few times as she orgasms."
        "When she's done she slides her fingers out of her pussy and straightens up, taking a few deep breaths to compose herself."
        $ mc.change_locked_clarity(15)
        the_person "That was... really intense."
        mc.name "It sure looked like it."
        the_person "Come on, let's keep walking for a little bit."
        "You walk together until the beach is just a sliver of sand running along the waters edge. With nothing more to see, you turn around and stroll back towards the center of the beach."
        "[the_person.title] gets redressed before you get to the most populated sections, to avoid getting you both in trouble."
        $ vt_generalised_dressing_description(the_person, temp_outfit)
    elif the_person.effective_sluttiness(["underwear_nudity","bare_tits"]) > 40:
        $ scene_manager.strip_to_underwear(the_person, visible_enough = False)
        $ scene_manager.update_actor(the_person)
        if temp_outfit.get_bra():
            "After a few minutes of walking [the_person.title] slows down and lets go of your arm."
            mc.name "Everything alright?"
            the_person "Yeah, I just need you to do me a favour. Pull on the knot for me, would you?"
            if temp_outfit.get_bra().has_extension:
                $ scene_manager.draw_animated_removal(the_person, temp_outfit.get_bra(), half_off_instead = True)
            else:
                $ scene_manager.draw_animated_removal(the_person, temp_outfit.get_bra())
            "[the_person.title] spins around and presents the back of her swimsuit to you. You pull on the knot, and she proceeds to take the top off entirely."
            $ mc.change_locked_clarity(5)
            the_person "There we go. If we're going to be spending a lot of time walking around in the sun I don't want to end up with tan lines. Mind keeping this in a pocket or something?"
            $ scene_manager.update_actor(the_person, position = "kissing")
            "She hands you the top, then holds onto your arm again. You resume your walk down the beach, now with [the_person.title]'s tits out in the open."
        else:
            "You are a little surprised that she is so comfortable being topless around so many people."
            mc.name "Do you go out like this often?"
            the_person "If we're going to be spending a lot of time walking around in the sun I don't want to end up with tan lines."
            $ mc.change_locked_clarity(5)
            $ scene_manager.strip_to_tits(the_person, visible_enough = False)
            $ scene_manager.update_actor(the_person, position = "kissing")
        "Not long after a group of guys further up the beach notices her, and begin whistling and cheering as she passes. You feel [the_person.title] shiver, as if cold."
        $ the_person.change_arousal(10)
        mc.name "We can turn around if you want."
        the_person "No, it's fine. I'm sure it's nothing they haven't seen before."
        "You notice her nipples are rock hard, and she's carefully sliding her thighs together with each step."
        $ the_person.change_arousal(10)
        "Once you're past the group of men she takes a deep breath and relaxes her grip on your arm. Half an hour of walking passes, and the beach has become a thin strip of sand against the water."
        the_person "Well, I guess that's all there is to see this way. Let's head back and see if we have time to do something else."
        mc.name "Sure. Want to put your top back on?"
        "[the_person.title] shakes her head and takes your arm again, leading you back the way you came."
        the_person "No, I... I like the way it feels when people watch me like that."
        $ the_person.change_arousal(10)
        $ mc.change_locked_clarity(10)
        "You stroll back, chatting with each other as you go. [the_person.title] eagerly points out all the men trying to take subtle glances at her tits, pressing up against your side tightly as you walk."
        "She finally puts her top back on when you get back to the heavily populated area of the beach, to avoid getting you both in trouble."
        $ vt_generalised_dressing_description(the_person, temp_outfit)
    elif the_person.effective_sluttiness("underwear_nudity") > 30:
        "You walk along the beach for a few minutes, passing by groups of people with umbrellas and tents set up."
        the_person "Hey, you see those guys over there?"
        "You follow [the_person.title]'s gaze up the beach, to a group of four guys standing around a cooler. They're not–so–subtly staring at [the_person.title] as she walks."
        mc.name "I'm not surprised they're interested, you're a good-looking girl in a hot little bikini."
        the_person "I suppose you're right. Maybe I should give them a little peek, just to be nice."
        if temp_outfit.get_bra():
            $ scene_manager.draw_animated_removal(the_person, temp_outfit.get_bra(), half_off_instead = True)
        $ scene_manager.update_actor(the_person, position = "kissing")
        "She winks at you, then lets go of your arm and turns towards the group of men. With one quick movement [the_person.title] pulls her bra up over her tits, then gives them a little shake."
        "There's a pause, then the group erupts in wolf whistles and cheers."
        $ temp_outfit.restore_all_clothing()
        $ scene_manager.update_actor(the_person, position = "kissing")
        "[the_person.title] turns away and pulls her top back down, grabbing onto your arm again. You can feel her shaking a little against you."
        $ the_person.change_arousal(10)
        the_person "Come on, let's keep going."
        "You keep walking until you've left the crowds behind and the strip of sand has shrunk to a narrow sliver."
        the_person "Well, I guess that's all there is to see this way. Let's head back and see if we have time to do something else."
        mc.name "Sure. Plan on flashing those guys again?"
        the_person "I'm not sure I could take that much excitement all in one day. They'll have to be satisfied with what they got."
        "She grabs your arm and pulls you along."
        the_person "Now come on, let's get going!"
        "You stroll back, chatting with each other as you go."
    else:
        "You walk along the beach until you've left the crowds behind and the strip of sand has shrunk to a narrow sliver."
        the_person "Well, I think that's all there is to see this way. Let's head back and see if we have time to do something else."
        "You turn around and stroll back, chatting with each other as you go."
        the_person "That didn't take too much time, do you want to get something to eat when we get back?"
        menu:
            "Yes\n{color=#ff0000}{size=18}Costs: $30{/size}{/color}" if mc.business.has_funds(30):
                mc.name "Yes, that sounds good."
                $ mc.business.change_funds(-30)
                call park_change_label(the_person, temp_outfit) from _call_park_change_label_public
            "Yes\n{color=#ff0000}{size=18}Requires: $30{/size}{/color} (disabled)" if not mc.business.has_funds(30):
                pass
            "No":
                mc.name "Sorry, I'm a little short on cash."
                the_person "What? You want me to spend time with you and you don't have any money? Shouldn't you be at work then?"
                $ the_person.change_stats(happiness = -10)
    $ scene_manager.clear_scene()
    return

label park_game_label(the_person, temp_outfit):
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person, temp_outfit, emotion = "happy")
    $ scene_manager.strip_to_underwear(the_person, visible_enough = False)
    "You and [the_person.title] walk through the park, looking for something to do. [the_person.title] suddenly points to a playground in the distance."
    the_person "I think they have a playground here, let's go see if we can find something to play with."
    "[the_person.title] takes your hand and leads you to the playground. You spend some time playing on the swings and slide, laughing and having a good time."
    mc.name "You're really good at this. How do you do it?"
    if the_person.age < 30:
        the_person "Practice, [the_person.mc_title]. In high school I was on the track team, and I still keep up some of the conditioning."
    else:
        the_person "Practice, [the_person.mc_title]. Back in high school I was on the track team, it all comes back pretty quickly."
    if the_person.sluttiness > 70 and not the_person.has_taboo("vaginal_sex"):
        "[the_person.title] pulls you close and wraps her arms around your chest from behind."
        the_person "There were a few things I never got to try back then though. Would you like to try something with me?"
        "One of her hands slides below your waist, feeling the bulge in your pants."
        mc.name "I think I would. What did you have in mind?"
        the_person "Back in high school the other girls had worked out a way of having sex in secret, but I never got to try it."
        $ mc.change_locked_clarity(5)
        "Her hand slides inside the waist of your pants, wrapping around your hard shaft."
        mc.name "Only one way to solve that then. Let me know what to do."
        "[the_person.title] pulls your cock out of your pants, then lets go. She lies on her back on a nearby bench and spreads her legs, pausing for a moment to pull her tiny panties to the side."
        the_person "Pull yourself close to me, and push my hips back a little bit. If you just pull my panties to the side, you should be able to slip right in."
        $ scene_manager.update_actor(the_person, position = "missionary")
        "You nod and grab her by the hips. It doesn't take much force to move [the_person.title] around, and soon you've got her positioned in front of you, with the tip of your penis lined up with her pussy."
        $ scene_manager.strip_to_vagina(the_person, visible_enough = True, prefer_half_off = True, delay = 1)
        call condom_ask(the_person) from _call_condom_ask_park_game
        if not _return:
            "[the_person.title]'s refusal has sucked the wind from your sails. You pull your pants back up."
            "At least you're no longer feeling as horny as you were, and you're able to focus on the game."
        else:
            the_person "That's right. Now we'll have to take it slow. We don't want to get caught."
            "You pull her hips towards you slowly, sinking into her cunt inch by inch. [the_person.title] arches her back and moans as you enter her."
            mc.name "Damn, you feel so tight like this. It feels great."
            the_person "Oh [the_person.mc_title], you feel so big. Ah..."
            "You pause when you've gotten your full length inside [the_person.possessive_title]. The sounds of the park bounce around you, and the warmth of her pussy sends shivers up your spine."
            the_person "Okay, I think I'm wet enough for you to keep going. Oh lord..."
            mc.name "Just relax and let me take care of you [the_person.title]."
            "You start to thrust in and out of [the_person.possessive_title], supporting yourself on your arms."
            the_person "Ah... that's it. Give it to me right there. Nice and slow. Ah..."
            "The bench makes you feel a little awkward, but you manage to find a comfortable position. You tighten your grip on her to stop her from moving away."
            "For a few minutes you are both silent, enjoying the strange sensations."
            "You pick up the pace, sliding in and out of [the_person.possessive_title] as fast as your position will allow."
            call fuck_person(the_person, private = True, start_position = missionary, start_object = None, skip_intro = True, girl_in_charge = True, self_strip = False, hide_leave = False, position_locked = True, affair_ask_after = False, ignore_taboo = False, skip_condom = True) from _call_fuck_person_parkgamesex
            if not the_person.has_ass_cum or the_person.has_tits_cum or the_person.has_stomach_cum or the_person.has_creampie_cum:
                    "[the_person.title] takes a moment to just lie there, then straightens up and pulls her panties back into place."
            else:
                    "[the_person.title] takes a moment to just lie there, then straightens up and washes your cum off of her with a napkin."
            the_person "Let's finish our game, I'm feeling a little hungry now."
        "You sit back up and continue playing, chatting and laughing together."
    elif the_person.is_willing(handjob) and not the_person.has_taboo("touching_penis"):
        "[the_person.title] walks close to you and wraps her arms around your chest from behind."
        the_person "I learned a few things back then; you can do almost anything when you're having fun."
        $ mc.change_locked_clarity(5)
        "Her hands rub along your chest for a few moments, then one slips below your waist and towards your crotch."
        the_person "I wanted to thank you for coming out here with me [the_person.mc_title]. It's so nice to get some time to spend with my [the_person.mc_title], and to get to play some games together."
        if mc.arousal < 30:
            $ mc.change_arousal(30)
        mc.name "It's no problem at all [the_person.title]. My pleasure."
        "Her hand slides into your pants, brushing against your already hard cock."
        the_person "Just relax and let me thank you properly. I know playing games with me got you excited."
        $ mc.change_locked_clarity(5)
        "She pulls the waist of your pants down, then wraps her hand around your shaft and strokes it gently. The fresh air is invigorating, and her hand is warm and soft."
        "You and [the_person.title] sit down on a nearby bench while she holds onto you from behind, hand sliding up and down your cock."
        mc.name "That feels great [the_person.title]."
        the_person "Good. Cum whenever you're ready."
        call get_fucked(the_person, the_goal = "get mc off", sex_path = None, private= True, start_position = handjob, start_object = None, skip_intro = True, ignore_taboo = False, prohibit_tags = [], unit_test = False, allow_continue = False) from _call_get_fucked_parkgamehand
        "She strokes you off as you climax, pulsing your load out into the air. When you're done she lets go and pulls your pants back into place."
        the_person "There we go, all done."
        "[the_person.title] pushes away from you and lies down on the grass, looking up at the sky. You do the same, lying next to [the_person.possessive_title] for an hour."
        if the_person.energy > mc.energy:
            "When you're ready to head back home you make it a competition, and [the_person.title] beats you at a game of tag."
            mc.name "Next time, ah... I'll beat you next time..."
            the_person "I'm sure you will [the_person.mc_title]. I'll try not to tire you out so much next time."
        elif the_person.energy + 50 > mc.energy:
            "When you're ready to head back home you make it a competition, and [the_person.title] is surprised by how close you get to beating her."
            mc.name "Next time, ah... I'll beat you next time..."
            the_person "You actually might [the_person.mc_title]. I'll have to try to tire you out more next time."
        else:
            "When you're ready to head back home you make it a competition, and [the_person.title] is stunned when you beat her."
            the_person "Next time, ah... I'll beat you next time..."
            mc.name "I'm sorry [the_person.title]. I guess you already got your work out for the day."
    else:
        "She lies on her back on the grass, taking a deep breath."
        the_person "It's so nice to be out here. I used to go to the park every day, but there just isn't any time now."
        mc.name "We'll have to do this more often then. I'm sure there are a lot of things you could teach me."
        if the_person.sluttiness > 20:
            the_person "I'd like that. I certainly learned a lot back in high school, but I'm not sure it would be all that useful to you."
            mc.name "Oh? Like what?"
            the_person "We used to play games together every morning, and us being teenagers we were bursting with energy just as much as hormones."
            the_person "The guys couldn't keep their hands off us when we were playing together, and some of the girls were more than happy for the attention."
            the_person "So some of us got pretty good at sneaking in a little fun while the rest of us were playing. We'd be playing tag while some couple had a quick kiss behind a tree."
            $ mc.change_locked_clarity(5)
            mc.name "What about you, did you ever get up to that kind of stuff?"
            the_person "Me? Oh, nothing serious. I never worked up the courage to go all the way in public, the most I ever did was hold hands with a guy while we were walking."
            $ mc.change_locked_clarity(5)
            mc.name "Lucky guy."
            the_person "Oh stop. Come on, let's just relax for a little bit."
            "You and [the_person.title] sit together on a bench next to each other for an hour."
        else:
            the_person "I'd like that. Here, let me start with this."
            "[the_person.title] straightens up and walks close to you."
            the_person "You'll tire yourself out if you keep running around like that. Just take a deep breath and relax, move your legs slowly and let's take a walk."
            "You inhale and slow down a little. You stroll together through the park, enjoying the scenery."
            the_person "There you go. You could keep that up for hours if you had to."
            "[the_person.title] smiles and takes your hand, and the two of you just walk together for an hour."
        if the_person.energy > mc.energy:
            "When you're ready to head back home you make it a competition, and [the_person.title] beats you at a game of tag."
            mc.name "Next time, ah... I'll beat you next time..."
            the_person "I'm sure you will [the_person.mc_title]. I'll try not to tire you out so much next time."
        elif the_person.energy + 50 > mc.energy:
            "When you're ready to head back home you make it a competition, and [the_person.title] is surprised by how close you get to beating her."
            mc.name "Next time, ah... I'll beat you next time..."
            the_person "You actually might [the_person.mc_title]. I'll have to try to tire you out more next time."
        else:
            "When you're ready to head back home you make it a competition, and [the_person.title] is stunned when you beat her."
            the_person "Next time, ah... I'll beat you next time..."
            mc.name "I'm sorry [the_person.title]. I guess you already got your work out for the day."
    $ scene_manager.clear_scene()
    return

label park_to_chill_label(the_person, temp_outfit):
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person, temp_outfit, emotion = "happy")
    $ scene_manager.strip_to_underwear(the_person, visible_enough = False)
    "You head off to a quiet spot in the park and spread out a blanket."
    the_person "Is there anywhere for us to get some food? I didn't even think about bringing any."
    mc.name "Me neither. I didn't see anywhere that might have some."
    the_person "Oh well, we'll remember next time I guess."
    "Stranger" "Hey, I don't mean to eavesdrop, but we've got some extra sandwiches if you need some."
    "The couple on the blanket beside you has taken a break, and one of them has a basket of food in front of them."
    the_person "That would be great, actually! Thanks!"
    "Stranger" "No problem at all. Just send it back over when you're done."
    "He hands [the_person.title] a sandwich and turns back to his partner."
    the_person "Alright [the_person.mc_title], let's eat! Ready?"
    mc.name "Ready, dig in whenever you're ready."
    "[the_person.title] takes a bite of her sandwich and you follow suit. You eat together for a few minutes, chatting and laughing."
    "The couple beside you finishes their meal and starts to pack up. One of them turns to you and [the_person.title]."
    "Stranger" "You two are looking pretty cozy! What do you say to a little game, us vs. you two."
    the_person "Sure, let's do it. Come on [the_person.mc_title]. Get over here and let's do this!"
    if the_person.effective_sluttiness("bare_tits") > 70:
        mc.name "Alright, you can be on my team [the_person.title]."
        "You get set up across from the other couple. [the_person.title] suggests a game of rock-paper-scissors, and they agree."
        the_person "I'll go first. Rock, paper, or scissors?"
        "Stranger" "Rock."
        the_person "I choose paper. I win!"
        "The stranger looks at his partner, then back at [the_person.title]. He smiles."
        the_person "Now it's your turn [the_person.mc_title]."
        mc.name "I choose rock."
        the_person "I choose scissors. You win!"
        the_person "Now it's my turn again. Rock, paper, or scissors?"
        "Stranger" "Scissors."
        the_person "I choose rock. I win again!"
        the_person "I think we make a pretty good team [the_person.mc_title]."
        mc.name "Definitely. I think we're going to win this game."
        "You and [the_person.title] continue to play, with [the_person.title] getting more and more flirtatious as the game goes on."
        if the_person.is_willing(blowjob, private = False) and not the_person.has_taboo("sucking_cock"):
            the_person "I think we're going to win this game, and I think I know just how to celebrate."
            $ scene_manager.update_actor(the_person, position = "kissing")
            $ mc.change_locked_clarity(5)
            "[the_person.title] leans in and kisses you, then starts to make her way down to your crotch."
            "The other couple watches in shock as [the_person.title] starts to give you a blowjob."
            call get_fucked(the_person, the_goal = "get mc off", sex_path = None, private= False, start_position = blowjob, start_object = None, skip_intro = True, ignore_taboo = False, prohibit_tags = [], unit_test = False, allow_continue = False) from _call_get_fucked_parkpicnicblow
        elif the_person.effective_sluttiness(["bare_tits","bare_pussy"]) > 70:
            the_person "I think we're going to win this game, and I think I know just how to celebrate."
            $ scene_manager.strip_to_tits(the_person, visible_enough = True, prefer_half_off = True)
            $ scene_manager.update_actor(the_person, position = "stand5")
            $ mc.change_locked_clarity(5)
            "[the_person.title] pulls off her top and lets her tits out. She gives them a quick shake, then pulls you in for a kiss."
            "The other couple watches in shock as [the_person.title] starts to make out with you."
            $ scene_manager.update_actor(the_person, position = "doggy")
            $ scene_manager.strip_full_outfit(the_person)
            "You and [the_person.title] start to get into it, with the other couple watching in shock."
            call fuck_person(the_person, private = False, start_position = doggy, start_object = None, skip_intro = True, girl_in_charge = True, self_strip = False, hide_leave = False, position_locked = True, affair_ask_after = False, ignore_taboo = False, skip_condom = True) from _call_fuck_person_parkpicnicsex
        else:
            the_person "I think we're going to win this game, and I think I know just how to celebrate."
            $ scene_manager.update_actor(the_person, position = "kissing")
            $ mc.change_locked_clarity(5)
            "[the_person.title] leans in and kisses you, then pulls back and smiles."
            the_person "I think we make a pretty good team [the_person.mc_title]."
            mc.name "Definitely. I think we're going to win this game."
    elif the_person.effective_sluttiness("bare_tits") > 30:
        mc.name "Alright, you can be on my team [the_person.title]."
        "You get set up across from the other couple. [the_person.title] suggests a game of rock-paper-scissors, and they agree."
        the_person "I'll go first. Rock, paper, or scissors?"
        "Stranger" "Rock."
        the_person "I choose paper. I win!"
        "The stranger looks at his partner, then back at [the_person.title]. He smiles."
        the_person "Now it's your turn [the_person.mc_title]."
        mc.name "I choose rock."
        the_person "I choose scissors. You win!"
        the_person "Now it's my turn again. Rock, paper, or scissors?"
        "Stranger" "Scissors."
        the_person "I choose rock. I win again!"
        the_person "I think we make a pretty good team [the_person.mc_title]."
        mc.name "Definitely. I think we're going to win this game."
        "You and [the_person.title] continue to play, with [the_person.title] getting more and more flirtatious as the game goes on."
        if the_person.is_willing(handjob, private = False) and not the_person.has_taboo("touching_penis"):
            the_person "I think we're going to win this game, and I think I know just how to celebrate."
            $ scene_manager.update_actor(the_person, position = "handjob")
            $ mc.change_locked_clarity(5)
            "[the_person.title] reaches out and starts to stroke your cock."
            "The other couple watches in shock as [the_person.title] starts to give you a handjob."
            call get_fucked(the_person, the_goal = "get mc off", sex_path = None, private= False, start_position = handjob, start_object = None, skip_intro = True, ignore_taboo = False, prohibit_tags = [], unit_test = False, allow_continue = False) from _call_get_fucked_parkpicnichand
    else:
        mc.name "Alright, you can be on my team [the_person.title]."
        "You get set up across from the other couple. [the_person.title] suggests a game of rock-paper-scissors, and they agree."
        the_person "I'll go first. Rock, paper, or scissors?"
        "Stranger" "Rock."
        the_person "I choose paper. I win!"
        "The stranger looks at his partner, then back at [the_person.title]. He smiles."
        the_person "Now it's your turn [the_person.mc_title]."
        mc.name "I choose rock."
        the_person "I choose scissors. You win!"
        the_person "Now it's my turn again. Rock, paper, or scissors?"
        "Stranger" "Scissors."
        the_person "I choose rock. I win again!"
        the_person "I think we make a pretty good team [the_person.mc_title]."
        mc.name "Definitely. I think we're going to win this game."
        "You and [the_person.title] continue to play, with [the_person.title] getting more and more competitive as the game goes on."
    $ scene_manager.clear_scene()
    return

label park_picnic_label(the_person, temp_outfit):
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person, temp_outfit, emotion = "happy")
    "You and [the_person.title] head to a quiet spot in the park, looking for a nice grassy spot without many people around."
    "After a few minutes of walking you find an ideal spot. You and [the_person.title] lay out a blanket next to each other, facing towards a nearby pond."
    $ scene_manager.strip_to_underwear(the_person, visible_enough = False)
    $ scene_manager.update_actor(the_person, position = "stand2")
    "[the_person.title] sits down on the blanket, opening a basket of food she's brought with her."
    the_person "I packed some sandwiches and fruit. Help yourself!"
    mc.name "Thanks, I'm starving!"
    if the_person.sluttiness < 30:
        "[the_person.title] hands you a sandwich and you take a bite. You chat and eat together for a while, enjoying the peaceful atmosphere of the park."
    elif the_person.sluttiness < 50:
        if temp_outfit.get_bra():
            "[the_person.title] lifts the straps of her top a few times, then sighs and stands up. She pulls the straps over her shoulders, then pulls the entire thing off."
            the_person "I'm so glad we're alone here. I hate wearing this thing."
            if temp_outfit.get_bra().has_extension:
                $ scene_manager.strip_to_tits(the_person, visible_enough = True)
            else:
                $ scene_manager.strip_to_tits(the_person, visible_enough = False)
        else:
            the_person "I'm so glad we're alone here. I feel so free."
            $ scene_manager.strip_to_tits(the_person, visible_enough = False)
        $ scene_manager.update_actor(the_person, position = "stand3")
    else:
        if temp_outfit.get_bra():
            "[the_person.title] gives you a sandwich, then puts the basket down and stands up. She pulls the straps of her top over her shoulders, then pulls the whole thing down and off."
        else:
            "[the_person.title] gives you a sandwich, then puts the basket down and stands up. She grabs the waist of her pants, then pulls the whole thing down and off."
        $ scene_manager.strip_full_outfit(the_person)
        $ scene_manager.update_actor(the_person, position = "stand3")
        "She kicks her clothes to the side and sits back down, taking a bite of her sandwich. She looks at you with a mischievous glint in her eye."
        the_person "I'm so glad we're alone here. I was thinking we could have a little fun."
        $ vtselected_action = str(vt_select_action_grope_finger_bj(the_person))
        if vtselected_action == "blowjob":
            the_person "Thank you. Once you're finished eating, I'll make sure to repay the favour."
            "You take a sandwich and hand it to [the_person.title], who takes a bite and starts to chew."
            "You spend a while chatting and eating together, enjoying the peaceful atmosphere of the park."
            $ scene_manager.update_actor(the_person, position = "sitting")
            "Eventually she finishes her sandwich and sets it aside."
            the_person "Thank you [the_person.mc_title]. Now, I think it's time for dessert."
            "You look at her curiously, and she smiles mischievously."
            the_person "I'll take care of everything for you. Just lie back and relax."
            "You lie down on the blanket, and [the_person.title] kneels beside you. She starts to rub your chest, pausing for a brief moment to brush her thumbs over your nipples. Your erection rubs against her crotch, separated only by your pants."
            "[the_person.title] works her way lower, shuffling back as she goes. When she reaches your waist she pauses, hand resting on your hard shaft."
            the_person "Oh my. I'll have to take care of this while I'm at it I suppose."
            "She pulls your pants down, letting your cock spring free. She leans forward and licks your shaft from balls to tip. When she reaches the top she opens her mouth and slides you in, quickly sliding you to the back of her throat."
            mc.name "Oh god that feels good."
            "[the_person.title] places her hands on your thighs while she blows you, taking every inch of your hard cock down her throat with each pass."
            call fuck_person(the_person, private = True, start_position = blowjob, start_object = None, skip_intro = True, girl_in_charge = True, self_strip = False, hide_leave = False, position_locked = True, affair_ask_after = False, ignore_taboo = False, skip_condom = True) from _call_fuck_person_parkpicnicblow
            "She reaches for a napkin and uses it to clean her face off, then lies down next to you. Feeling completely relaxed, you spend an hour dozing in the warm sun."
        elif vtselected_action == "standing_finger":
            the_person "Thank you. Take as long as you need to finish eating, I'm in no hurry."
            "You take a sandwich and hand it to [the_person.title], who takes a bite and starts to chew."
            "You spend a while chatting and eating together, enjoying the peaceful atmosphere of the park."
            "As you eat, you can't help but notice [the_person.title]'s body. You reach out and start to rub her back, working your way down to her ass."
            "Heading her advice, you take a good long time on her ass. [the_person.title] sighs softly while you play with her."
            the_person "That feels really good. Keep doing that, please."
            "You kneed her butt a little harder, enjoying how it feels in your hands. [the_person.title] seems to be having just as much fun, sighing occasionally."
            $ the_person.change_arousal(10)
            the_person "Mmm, I think I've gotten a little wet. Could you check and make sure?"
            mc.name "Let's see..."
            "You reach a hand between [the_person.title]'s legs and run a finger along her pussy. She gasps when you brush past her clit."
            the_person "Oh, do that again."
            "You make little circles around [the_person.title]'s clit with your finger. She responds by arching her back and moaning quietly, her pussy now dripping wet."
            $ the_person.change_arousal(10)
            mc.name "Yes, you seem to be a little wet [the_person.title]."
            the_person "Keep touching me... Ah..."
            "She moans again, louder this time. You slide a pair of fingers into her cunt and start to finger her."
            "[the_person.title] grabs handfuls of the blanket and gasps, her hips twitching against your hand."
            the_person "Keep going! Ah!"
            call fuck_person(the_person, private = True, start_position = standing_finger, start_object = None, skip_intro = True, girl_in_charge = True, self_strip = False, hide_leave = False, position_locked = True, affair_ask_after = False, ignore_taboo = False, skip_condom = True) from _call_fuck_person_parkpicnicfinger
            the_person "Thank you [the_person.mc_title]. Ah..."
            "You lie down on the blanket next to her. You pass an hour and a half in the sun, enjoying the warm summer day while you stare at [the_person.title]'s body."
        elif vtselected_action == "standing_grope":
            "She sets the food aside, then sits back down. She rubs her hands over the front of her body, paying special attention to her breasts, then she lies face down on the blanket."
            $ scene_manager.update_actor(the_person, position = "walking_away")
            the_person "[the_person.mc_title], could you do me a favour and give me a massage?"
            mc.name "No problem. It would be great to help you relax after a great day like this."
            "You kneel behind [the_person.title] and start to rub her back, starting with her shoulder blades and working down to her waist."
            the_person "And my legs, if you don't mind."
            mc.name "Of course not."
            "She spreads her legs a little, letting you run your hands along the inside and outside of her thighs."
            the_person "A little higher too. I love having my butt massaged."
            $ the_person.change_arousal(10)
            "You move up to her ass, rubbing it in gently. [the_person.title] sighs softly while you kneed her butt cheeks."
            call fuck_person(the_person, private = True, start_position = standing_grope, start_object = None, skip_intro = True, girl_in_charge = True, self_strip = False, hide_leave = False, position_locked = True, affair_ask_after = False, ignore_taboo = False, skip_condom = True) from _call_fuck_person_parkpicnicgrope
            the_person "Thank you [the_person.mc_title]. That was a huge help."
            mc.name "My pleasure [the_person.title]."
            "You lie down on the blanket next to her. You pass an hour and a half in the sun, enjoying the warm summer day while you stare at [the_person.title]'s body."
        else:
            "Once she's finished eating she lies down on the blanket, face down this time."
            $ scene_manager.update_actor(the_person, position = "walking_away")
            the_person "Could you do me a favour and give me a massage [the_person.mc_title]?"
            mc.name "No problem. It would be great to help you relax after a great day like this."
            if temp_outfit.get_bra():
                "You take some massage oil and kneel next to [the_person.title]. You run your hands along her back, lifting up the straps on her top to get all of her shoulder blades."
            else:
                "You take some massage oil and kneel next to [the_person.title]. You run your hands along her bare back."
            the_person "Thank you. If you could get my legs too, it would be a huge help."
            "You move down and start to rub her legs."
            the_person "Perfect. Just a little higher."
            "You move your hands up, spreading the massage oil over her thighs. She spreads her legs a little, letting you reach her inner thighs."
            $ the_person.change_arousal(10)
            the_person "Ah... A little more, please."
            "You move higher still, now rubbing the lower part of [the_person.title]'s butt. She seems totally relaxed."
            the_person "Just pull my pants up a little if you have to, make sure you get some oil all around the edge."
            $ the_person.change_arousal(10)
            mc.name "Whatever you say [the_person.title]."
            "You work your hands around the periphery of her pants, fingers slipping under the edge. [the_person.title] sighs softly as you run your hands over her ass."
            $ the_person.change_arousal(10)
            "[the_person.title] shows no sign that you should stop. For another minute you play with her ass, making sure every inch is covered with oil. Eventually she rolls over onto her back again."
            $ scene_manager.update_actor(the_person, position = "stand3")
            the_person "Thank you [the_person.mc_title]. That was a huge help."
            mc.name "Any time [the_person.title]."
            "You lie down on the blanket next to her. You pass an hour and a half in the sun, just enjoying the warm summer day."
    $ scene_manager.clear_scene()
    return

label park_change_label(the_person, temp_outfit):
    $ scene_manager = Scene()
    "You and [the_person.title] head over to the food stand, joining a long line of hungry park goers."
    mc.name "This might take a while. There are some picnic tables up that way, you go save us one and I'll bring the food."
    the_person "Sure. Get me a hotdog, with mustard, and a drink."
    $ scene_manager.add_actor(the_person, temp_outfit, position = "back_peek")
    if the_person.sluttiness > 40:
        "[the_person.title] waves goodbye and starts off towards the group of tables. More than a few heads turn to watch as she goes."
    else:
        "[the_person.title] waves goodbye and starts off towards the group of tables."
    $ scene_manager.hide_actor(the_person)
    "After a few minutes waiting in line you've got food for you and [the_person.possessive_title]. You stop off at a small picnic table to get everything organized on the tray."
    menu:
        "Leave her meal alone":
            $ scene_manager.show_actor(the_person, position = "sitting")
            "You catch up with [the_person.possessive_title], sitting across from her at the picnic table."
            the_person "Thanks [the_person.mc_title], I think I really needed this!"
            mc.name "Me too. I'm starving!"
            "The two of you dig in, chatting with each other between bites. You end up talking long after you've finished your meals."
            $ the_person.change_stats(love = 5, happiness = 5)
        "Put some serum in her drink" if mc.inventory.total_serum_count > 0:
            call give_serum(the_person) from _call_give_serum_park
            $ scene_manager.show_actor(the_person, position = "sitting", emotion = "happy")
            if _return:
                $ dosed = True
                "You pull out some serum and mix it into [the_person.title]'s drink before catching up with her at the picnic tables."
            else:
                $ dosed = False
                "You change your mind and rush to catch up with [the_person.title] at the picnic tables."
            the_person "Thanks [the_person.mc_title], I think I really needed this!"
            mc.name "Me too. I'm starving!"
            "The two of you dig in. You wait a few minutes until [the_person.title]'s had most of her drink."
            $ the_person.change_stats(love = 2, happiness = 2)
            $ influence = the_person.suggestibility
            if the_person.has_role(trance_role):
                $ influence +=20
            if the_person.has_exact_role(heavy_trance_role):
                $ influence +=20
            elif the_person.has_exact_role(very_heavy_trance_role):
                $ influence +=40
            if influence > 20:
                "Between the serum and your other influences it seems like [the_person.title] might be suggestible enough to follow orders at the moment."
                mc.name "Hey [the_person.title], I think I forgot something in the car. Would you mind coming with me while I check?"
                "[the_person.title] looks at you and nods slowly."
                the_person "Okay."
                $ scene_manager.update_actor(the_person, position = "stand3")
                "You lead [the_person.title] to the car, finding it mostly empty at this time of day. You open up the door and motion for her to get in."
                mc.name "Get in for a second, I need to check something."
                the_person "What is it?"
                menu:
                    "Have her flash her tits":
                        mc.name "I just need to check something real quick. Can you pull your top up for me?"
                        if the_person.opinion.public_sex > 0:
                            "[the_person.title] barely even thinks about it before she pulls up her top and lets her tits fall free."
                            the_person "Is this what you needed to see?"
                            $ scene_manager.strip_to_tits(the_person, visible_enough = True, prefer_half_off = True)
                            $ scene_manager.update_actor(the_person, position = "stand4")
                            "She shakes her shoulders back and forth, jiggling her tits for you. You notice her nipples getting hard as you watch her."
                            $ mc.change_arousal(10)
                            $ the_person.change_arousal(10)
                            mc.name "Yeah, just like that. You look great [the_person.title]."
                            "She smiles and cups her tits, squeezing them together."
                            the_person "Thank you. Let me know when you've seen enough."
                            "You enjoy the view for a few more seconds, until you see another couple heading your way from the park."
                            $ mc.change_arousal(10)
                            mc.name "Okay [the_person.title], that will be enough for now."
                            $ vt_generalised_dressing_description(the_person, temp_outfit)
                            "Once dressed, she shakes her tits again to get them into place."
                        else:
                            "[the_person.title] thinks about it for a brief moment, then nods and steps into the car. She motions for you to follow, and closes the door behind her."
                            $ scene_manager.strip_to_tits(the_person, visible_enough = True, prefer_half_off = True)
                            $ scene_manager.update_actor(the_person, position = "stand5")
                            "Once you're in the car [the_person.title] pulls up her top, letting her tits fall free."
                            $ mc.change_arousal(10)
                            the_person "Is this what you needed to see?"
                            "She shakes her shoulders back and forth, jiggling her tits for you. You notice her nipples getting hard as you watch her."
                            $ the_person.change_arousal(10)
                            mc.name "Yeah, just like that. You look great [the_person.title]."
                            "She smiles and cups her tits, squeezing them together."
                            the_person "Thank you. Let me know when you've seen enough."
                            "You enjoy the view for a minute or two, watching [the_person.possessive_title]'s breasts bounce as she plays with them."
                            $ mc.change_arousal(10)
                            mc.name "Okay [the_person.title], that will be enough for now."
                            $ vt_generalised_dressing_description(the_person, temp_outfit)
                            "Once dressed, she shakes her tits one last time to get them into place."
                        mc.name "Let's head back to the picnic table and relax for a little while."
                        "You and [the_person.title] return to your seats."
                    "Have her get naked for you" if influence > 30:
                        mc.name "I think I might have left something in the trunk. Can you go check for me?"
                        if the_person.sluttiness > 15:
                            "[the_person.title] barely even thinks about it before stepping out of the car and heading to the trunk. You follow her and open it up."
                            the_person "What am I looking for?"
                            mc.name "Just take everything out and we'll sort through it."
                            "[the_person.title] starts to pull out the contents of the trunk, and you take the opportunity to admire her body."
                            $ scene_manager.strip_to_tits(the_person, visible_enough = False)
                            "She notices you staring and smiles, reaching behind her neck and undoing the top of her outfit."
                            $ mc.change_arousal(10)
                            mc.name "Yeah, that's it. You look amazing [the_person.title]."
                            the_person "Thank you. I guess I need to take these off too..."
                            $ scene_manager.strip_full_outfit(the_person)
                            "She pulls the rest of her outfit off, standing naked in front of you."
                            $ mc.change_arousal(10)
                            the_person "There you go [the_person.mc_title]. Anything else?"
                            mc.name "Turn around for me, so I can take a look at you from behind."
                            $ scene_manager.update_actor(the_person, position = "back_peek")
                            "She nods and turns around, planting her hands on the trunk and bending over as much as she can."
                            "You place a hand on her ass and give it a good squeeze, making [the_person.title] yelp."
                            $ mc.change_arousal(10)
                            the_person "Hey! Easy back there."
                            mc.name "Sorry. Just couldn't resist."
                            "You give her butt another squeeze, then let go entirely."
                            mc.name "Thank you [the_person.title], that was exactly what I wanted."
                            $ scene_manager.update_actor(the_person, position = "stand5")
                            "She turns back to you and picks up her outfit."
                            the_person "Good. Give me a moment to get dressed, please."
                            "You step back and wait until [the_person.title] has her outfit put back together. Once that's done, you head back to the picnic table and hang out a bit longer."
                        else:
                            "[the_person.title] thinks about it for a long moment, taking a slow step towards the trunk."
                            the_person "You want me to take everything out of the trunk?"
                            mc.name "That's right. I think I might have left something in there."
                            the_person "I'm not sure..."
                            mc.name "It's no big deal [the_person.title]. Just take everything out and we'll sort through it."
                            "She's quiet for another few seconds, then takes a step back and shakes her head."
                            the_person "I don't think I'm comfortable with that [the_person.mc_title]. If you can't find whatever you're looking for can we please just go?"
                            "She's got a sharp look in her eye now, pushing her any farther now would do more harm than good."
                            mc.name "Alright. Sorry [the_person.title], let's go get back to our seats."
                            "You and [the_person.title] return to the picnic table."
                    "Have her titfuck you" if the_person.has_large_tits and influence > 50:
                        mc.name "I think I might have left something in the glove compartment. Can you check for me?"
                        if the_person.sluttiness > 30:
                            "[the_person.title] thinks about it for a brief moment, then nods and steps into the car. You follow her in and close the door behind you."
                            the_person "What am I looking for?"
                            mc.name "Just check the glove compartment and see if there's anything in there."
                            "[the_person.title] opens the glove compartment and starts to dig through it. You take the opportunity to admire her body."
                            $ scene_manager.update_actor(the_person, position = "kneeling1")
                            mc.name "You know, I've been wanting to get a closer look at those tits of yours all day. Why don't you take them out for me?"
                            "[the_person.title] looks up at you and smiles, then pulls her top down and lets her tits fall free."
                            $ mc.change_arousal(10)
                            the_person "Is this what you wanted to see?"
                            "She shakes her shoulders back and forth, jiggling her tits for you. You notice her nipples getting hard as you watch her."
                            $ the_person.change_arousal(10)
                            mc.name "Yeah, that's it. Now I want you to use them to get me off."
                            "[the_person.title] nods and leans forward, taking your cock in her hands and starting to rub it between her tits."
                            call fuck_person(the_person, private = True, start_position = tit_fuck, start_object = None, skip_intro = True, girl_in_charge = True, self_strip = False, hide_leave = False, position_locked = True, affair_ask_after = False, ignore_taboo = False, skip_condom = True) from call_fuck_person_parkchangetit
                            "She catches a few drips of cum with a finger as they run out from the bottom of her cleavage."
                            mc.name "I think there are some napkins in the glove compartment if you want to get cleaned up."
                            "[the_person.title] gets onto her feet and nods. You wait until she's cleaned up, then head back to the picnic table and hang out a bit longer."
                            $ temp_outfit.remove_all_cum()
                            $ vt_generalised_dressing_description(the_person, temp_outfit)
                        else:
                            "[the_person.title] thinks about it for a long moment, taking a slow step towards the glove compartment."
                            the_person "You want me to check the glove compartment?"
                            mc.name "That's right. I think I might have left something in there."
                            the_person "I'm not sure..."
                            mc.name "It's no big deal [the_person.title]. Just check the glove compartment and see if there's anything in there."
                            "She's quiet for another few seconds, then takes a step back and shakes her head."
                            the_person "No, I don't think so [the_person.mc_title]. You just go ahead and check it yourself, I'm going to head back to the table."
                            "She's got a sharp look in her eye now, pushing her any farther now would do more harm than good."
                            mc.name "Alright, I'm sorry. Just forget I said anything at all, and let's get back to the table."
                            "You and [the_person.title] return to the picnic table."
                    "Have her blow you" if influence > 70:
                        mc.name "I think I might have left something in the glove compartment. Can you check for me?"
                        if the_person.sluttiness > 45 and not the_person.has_taboo("sucking_cock"):
                            "[the_person.title] thinks about it for a brief moment, then nods and steps into the car. You follow her in and close the door behind you."
                            the_person "What am I looking for?"
                            mc.name "Just check the glove compartment and see if there's anything in there. And while you're at it, why don't you suck me off?"
                            "[the_person.title] looks up at you and smiles, then pulls your cock out and starts to suck it."
                            $ scene_manager.update_actor(the_person, position = "kneeling1")
                            call fuck_person(the_person, private = True, start_position = blowjob, start_object = None, skip_intro = True, girl_in_charge = True, self_strip = False, hide_leave = False, position_locked = True, affair_ask_after = False, ignore_taboo = False, skip_condom = True) from call_fuck_person_parkchangeblow
                            if the_person.has_mouth_cum:
                                "After a few seconds you've finished filling [the_person.possessive_title]'s mouth up with semen. She lets go of your shaft and slides your tip away from her lips."
                                mc.name "Open up for me, please."
                                "[the_person.title] rolls her eyes, then opens her mouth to show off the pools of cum you just put there."
                                mc.name "God that's so hot."
                            if the_person.opinion.drinking_cum > 0:
                                "[the_person.title] leans back closing her mouth. You watch her throat work as she swallows a few times, then runs the back of her hand over her mouth."
                                the_person "All done. You tasted amazing [the_person.mc_title]."
                            else:
                                "[the_person.title] leans to the side and lets it all flow out onto the floor. She spits out the last few drops at the end, then runs the back of her hand over her mouth."
                                the_person "There, all done."
                            mc.name "Thank you [the_person.title], that was just what I needed. Let's head back to the table."
                            $ scene_manager.update_actor(the_person, position = "stand5")
                            "She gets up off her knees and follows you out of the car. You hang out together at the picnic table a bit longer."
                        else:
                            "[the_person.title] thinks about it for a long moment, taking a slow step towards the glove compartment."
                            the_person "You want me to suck you off? Here?"
                            mc.name "That's right. Something nice to finish the day off with."
                            the_person "I'm not sure..."
                            mc.name "It's no big deal [the_person.title]. A quick blowjob, then we can head back to the table."
                            "She's quiet for another few seconds, then takes a step back and shakes her head."
                            the_person "No, I don't think so [the_person.mc_title]. You just go ahead and jerk yourself off or something, I'm going to head back to the table."
                            "She's got a sharp look in her eye now, pushing her any farther now would do more harm than good."
                            mc.name "Alright, I'm sorry. Just forget I said anything at all, and let's get back to the table."
                            "You and [the_person.title] return to the picnic table."
                    "Fuck her" if influence > 90:
                            mc.name "I think I might have left something in the trunk. Can you go check for me?"
                            if the_person.sluttiness > 60 and not the_person.has_taboo("vaginal_sex"):
                                $ scene_manager.update_actor(the_person, position = "back_peek")
                                "[the_person.title] thinks about it for a brief moment, then steps past you to the trunk. By the time you've stepped up behind her and closed the trunk she's leaning against the car, wiggling her ass at you."
                                the_person "I'm so sorry, I didn't realise I was teasing you so badly."
                                "You step behind her and pull your cock out, bouncing it against one of her ass cheeks."
                                mc.name "Well you were, and I'm going to need to take care of this now."
                                "You give her ass a smack, and she moans in response."
                                the_person "Whatever you have to do [the_person.mc_title]..."
                                "You squeeze [the_person.title]'s ass a few times, letting your cock rest between her cheeks. After that you lean forward and cup her breasts, sliding your hands under her top."
                                "[the_person.title] rocks her hips against yours, grinding against your dick while you play with her tits."
                                mc.name "Turn around for me, I want to fuck you up against the car."
                                $ scene_manager.update_actor(the_person, position = "stand5")
                                $ scene_manager.strip_to_tits(the_person, visible_enough = False)
                                "[the_person.title] stands up and turns around. You pull her top up and play with her breasts some more, enjoying the way her nipples harden as you do."
                                $ scene_manager.strip_full_outfit(the_person)
                                "Next you reach down and pull her pants to the side, running a pair of fingers over her pussy. She gasps as you touch her, her cunt already dripping wet."
                                the_person "Oh [the_person.mc_title]... Ah..."
                                mc.name "Here, let's give you what you want."
                                "You lift one of her legs and step forward, pinning her between the car and your body. The tip of your penis brushes against her slit, making her moan again."
                                the_person "Please, please give it to me."
                                "You reach a hand down and line yourself up, then thrust forward slowly. [the_person.title] shivers against your body as you slide your cock as deep as you can into her."
                                mc.name "There we go. You're so wet [the_person.title], I can tell you need it."
                                "She nods and mumbles something, interrupted by a yelp as you start to pump in and out of her."
                                mc.name "What was that?"
                                the_person "Ah! I... I need your cock so badly!"
                                mc.name "I know you do, you dirty slut!"
                                "You lean forward and kiss [the_person.title]'s neck while you fuck her. She moans louder and rolls her hips to meet yours."
                                the_person "Oh god you feel so good! Ah! Yes!"
                                mc.name "Easy there [the_person.title], keep it down. Or maybe you want people to know how much you like getting fucked."
                                if the_person.opinion.public_sex > 0:
                                    the_person "Ah! Fuck, I don't care! Just keep fucking me, I need it so badly [the_person.mc_title]. You feel so... good!"
                                    "[the_person.title] moans loudly again, and you feel her pussy twitch around your cock."
                                else:
                                    "[the_person.title] shakes her head and bites her lip, stifling another moan. You feel her pussy twitch around your cock."
                                call fuck_person(the_person, private = True, start_position = against_wall, start_object = None, skip_intro = True, girl_in_charge = True, self_strip = False, hide_leave = False, position_locked = True, affair_ask_after = False, ignore_taboo = False, skip_condom = True) from call_fuck_person_parkchangefuck
                                "[the_person.title] follows you as you head back to the picnic table, pulling her pants back into place as you go. You hang out at the table until you've both recovered from the exertion."
                                $ vt_generalised_dressing_description(the_person, temp_outfit)
                            else:
                                "[the_person.title] thinks about it for a long moment, taking a slow step towards the trunk."
                                the_person "You really want to have sex with me? Right here?"
                                mc.name "That's right. I can't think of anything better to end the day with."
                                the_person "I'm not sure..."
                                mc.name "It's no big deal [the_person.title]. It's just a quickie, then we can head back to the picnic."
                                "She's quiet for another few seconds, then takes a step back and shakes her head."
                                the_person "No, I don't think so [the_person.mc_title]. You just go ahead and jerk yourself off or something, I'm going to head back to the picnic."
                                "She's got a sharp look in her eyes now, pushing her any farther now would do more harm than good."
                                mc.name "Alright, I'm sorry. Just forget I said anything at all, and let's get back to the picnic."
                                "You and [the_person.title] return to the picnic table."
    #$ scene_manager.clear_scene()
    return


# "Fuck her" if influence > 90:
                        # mc.name "I've been watching you all day, wanting to rip your clothes off. Let's just slip into the woods and have a quick fuck."
                        # if the_person.sluttiness > 60 and not the_person.has_taboo("vaginal_sex"):
                            # $ scene_manager.update_actor(the_person, position = "back_peek")
                            # "[the_person.title] thinks about it for a brief moment, then steps past you into the woods. By the time you've stepped in after her she's leaning against a tree, wiggling her ass at you."
                            # the_person "I'm so sorry, I didn't realise I was teasing you so badly."
                            # "You step behind her and pull your pants down, bouncing your hard cock against one of her ass cheeks."
                            # mc.name "Well you were, and I'm going to need to take care of this now."
                            # "You give her ass a smack, and she moans in response."
                            # the_person "Whatever you have to do [the_person.mc_title]..."
                            # "You squeeze [the_person.title]'s ass a few times, letting your cock rest between her cheeks. After that you lean forward and cup her breasts, sliding your hands under her top."
                            # "[the_person.title] rocks her hips against yours, grinding against your dick while you play with her tits."
                            # mc.name "Turn around for me, I want to fuck you up against the tree."
                            # $ scene_manager.update_actor(the_person, position = "stand5")
                            # $ scene_manager.strip_to_tits(the_person, visible_enough = False)
                            # "[the_person.title] stands up and turns around. You pull her top up and play with her breasts some more, enjoying the way her nipples harden as you do."
                            # $ scene_manager.strip_full_outfit(the_person)
                            # "Next you reach down and pull her pants to the side, running a pair of fingers over her pussy. She gasps as you touch her, her cunt already dripping wet."
                            # the_person "Oh [the_person.mc_title]... Ah..."
                            # mc.name "Here, let's give you what you want."
                            # "You lift one of her legs and step forward, pinning her between the tree and your body. The tip of your penis brushes against her slit, making her moan again."
                            # the_person "Please, please give it to me."
                            # "You reach a hand down and line yourself up, then thrust forward slowly. [the_person.title] shivers against your body as you slide your cock as deep as you can into her."
                            # mc.name "There we go. You're so wet [the_person.title], I can tell you need it."
                            # "She nods and mumbles something, interrupted by a yelp as you start to pump in and out of her."
                            # mc.name "What was that?"
                            # the_person "Ah! I... I need your cock so badly!"
                            # mc.name "I know you do, you dirty slut!"
                            # "You lean forward and kiss [the_person.title]'s neck while you fuck her. She moans louder and rolls her hips to meet yours."
                            # the_person "Oh god you feel so good! Ah! Yes!"
                            # mc.name "Easy there [the_person.title], keep it down. Or maybe you want people to know how much you like getting fucked."
                            # if the_person.opinion.public_sex > 0:
                                # the_person "Ah! Fuck, I don't care! Just keep fucking me, I need it so badly [the_person.mc_title]. You feel so... good!"
                                # "[the_person.title] moans loudly again, and you feel her pussy twitch around your cock."
                            # else:
                                # "[the_person.title] shakes her head and bites her lip, stifling another moan. You feel her pussy twitch around your cock."
                            # call fuck_person(the_person, private = True, start_position = against_wall, start_object = None, skip_intro = True, girl_in_charge = True, self_strip = False, hide_leave = False, position_locked = True, affair_ask_after = False, ignore_taboo = False, skip_condom = True) from call_fuck_person_parkchangefuck
                            # "[the_person.title] follows you as you head back to the picnic blanket, pulling her pants back into place as you go. You hang out at the blanket until you've both recovered from the exertion."
                            # $ generalised_dressing_description(the_person, temp_outfit)
                        # else:
                            # "[the_person.title] thinks about it for a long moment, taking a slow step towards the woods."
                            # the_person "You really want to have sex with me? Right here?"
                            # mc.name "That's right. I can't think of anything better to end the day with."
                            # the_person "I'm not sure..."
                            # mc.name "It's no big deal [the_person.title]. It's just a quickie, then we can head back to the picnic."
                            # "She's quiet for another few seconds, then takes a step back and shakes her head."
                            # the_person "No, I don't think so [the_person.mc_title]. You just go ahead and jerk yourself off or something, I'm going to head back to the picnic."
                            # "She's got a sharp look in her eyes now, pushing her any farther now would do more harm than good."
                            # mc.name "Alright, I'm sorry. Just forget I said anything at all, and let's get back to the picnic."
                            # "You and [the_person.title] return to the picnic blanket."