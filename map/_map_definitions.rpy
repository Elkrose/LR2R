label instantiate_map_locations():
    python:
        ##PC's Home##
        mansion_name = str(last_name)+" Mansion"
        hall = Room("home_hall", "Living Room", house_background, [make_floor(), make_wall(), make_front_door()],
            map_pos = [1,1], lighting_conditions = standard_indoor_lighting)
        bedroom = Room("mc_bedroom", "Your Bedroom", bedroom_background, bedroom_objects,
            actions = [sleep_action, bedroom_masturbate_action],
            map_pos = [1,0], lighting_conditions = standard_indoor_lighting)
        lily_bedroom = Room("lily_bedroom", "Lily's Bedroom", bedroom_background,bedroom_objects,
            map_pos = [0,1], lighting_conditions = standard_indoor_lighting)
        mom_bedroom = Room("mom_bedroom", "Mom's Bedroom", bedroom_background, bedroom_objects,
            actions = [mom_room_search_action],
            map_pos = [0,2], lighting_conditions = standard_indoor_lighting)
        kitchen = Room("kitchen", "Kitchen", kitchen_background, [make_wall, make_floor(), make_chair(), make_table()],
            map_pos = [1,2], lighting_conditions = standard_indoor_lighting)
        home_bathroom = Room("bathroom", "Bathroom", home_bathroom_background, home_shower_objects,
            visible = False, darken = False)
        home_shower = Room("home_shower", "Home Shower", old_home_shower_background, home_shower_objects,
            visible = False, lighting_conditions = standard_indoor_lighting)
        her_hallway = Room("her_hallway", "Front hall", her_hallway_background, [make_floor(), make_wall(), make_front_door(), make_hall_carpet(), make_stairs()],
            visible = False, lighting_conditions = standard_indoor_lighting)
        laundry_room = Room("laundry_room", "Laundry Room", laundry_room_background, laundry_room_objects,
            visible = False, lighting_conditions = standard_indoor_lighting)
        dungeon = Room("dungeon", "Dungeon", dungeon_background, dungeon_objects, [dungeon_room_appoint_slave_action],
            map_pos = [2,1], visible = False, lighting_conditions = standard_indoor_lighting, darken = False)

        harem_mansion = Room("harem_mansion", str(mansion_name), harem_mansion_background, harem_objects,
            map_pos =[1, 1], visible = False, lighting_conditions = standard_indoor_lighting)

        ##PC's Work##
        ceo_office = Room("ceo_office", "CEO Office", ceo_office_background, ceo_office_objects,
            actions = [policy_purchase_action, set_uniform_action, set_serum_action],
            map_pos = [1,0], lighting_conditions = standard_indoor_lighting)
        lobby = Room("lobby", "Lobby", lobby_background, [make_floor(), make_wall(), make_reception(), make_chair(), make_front_door(), make_window()],
            map_pos = [1,1], tutorial_label = "lobby_tutorial_intro", lighting_conditions = standard_indoor_lighting, privacy_level = 2)
        office = Room("main_office", "Main Offices", office_background, [make_floor(), make_desk(), make_window(), make_chair(), make_wall()],
            actions = [hr_work_action,supplies_work_action,interview_action,pick_supply_goal_action],
            map_pos = [0,1], tutorial_label = "office_tutorial_intro", lighting_conditions = standard_indoor_lighting, privacy_level = 2)
        m_division = Room("market_div", "Marketing Division", marketing_background, [make_floor(), make_desk(), make_window(), make_chair(), make_wall()],
            actions = [sell_serum_action, market_work_action,set_company_model_action],
            map_pos = [2,1], tutorial_label = "marketing_tutorial_intro", lighting_conditions = standard_indoor_lighting, privacy_level = 2)
        rd_division = Room("rd_div", "R&D Division", research_background, [make_floor(), make_desk(), make_window(), make_chair(), make_wall(), make_examtable()],
            actions = [research_work_action,design_serum_action,pick_research_action,review_designs_action,set_head_researcher_action],
            map_pos = [2,2], tutorial_label = "research_tutorial_intro", lighting_conditions = standard_indoor_lighting, privacy_level = 2)
        p_division = Room("prod_div", "Production Division", production_background, [make_floor(), make_desk(), make_window(), make_chair(), make_wall()],
            actions = [production_work_action,pick_production_action,trade_serum_action],
            map_pos = [0,2], tutorial_label = "production_tutorial_intro", lighting_conditions = standard_indoor_lighting, privacy_level = 2)
        clone_facility = Room("clone_facility", "Cloning Facility", clone_facility_background, [make_floor(), make_desk(), make_chair(), make_wall()],
            map_pos = [1,2], visible = False, lighting_conditions = standard_indoor_lighting, darken = False)
        work_bathroom = Room("work_bathroom", "Work Bathroom", bathroom_background, [make_wall(), make_floor(), make_toilet(), make_sink()],
            visible = False, lighting_conditions = standard_indoor_lighting, privacy_level = 2, darken = False)
        testing_room = Room("testing_room", "Test Room", testing_room_background, [make_floor(), make_wall(), make_medical_table(), make_mirror()],
            visible = False, lighting_conditions = standard_indoor_lighting, darken = False)
        storage_room = Room("storage_room", "Storage Room", storage_room_background, [make_floor(), make_wall(), make_door()],
            visible = False, lighting_conditions = standard_indoor_lighting, privacy_level = 2, darken = False)
        break_room = Room("break_room", "Break Room", break_room_background, [make_floor(), make_wall(), make_table(), make_chair(), make_bench(), make_window()],
            visible = False, lighting_conditions = standard_indoor_lighting, privacy_level = 2, darken = False)

        ## Downtown ##
        downtown = Room("downtown", "Downtown Streets", outside_background, [make_floor(), make_bench(), make_alley()],
            actions = [downtown_search_action],
            map_pos = [1,1], lighting_conditions = standard_outdoor_lighting, privacy_level = 3)
        downtown_bar = Room("bar", "The Downtown Distillery", bar_background, downtown_bar_objects, [downtown_bar_drink_action],
            map_pos = [2,1], visible = True, lighting_conditions = standard_indoor_lighting, privacy_level = 3, darken = False, accessible_func = downtown_bar_is_open)
        downtown_hotel = Room("hotel_lobby", "The Hotel", hotel_background, downtown_hotel_lobby_objects,
            map_pos = [0,1], visible = True, lighting_conditions = standard_indoor_lighting, privacy_level = 3, darken = False)
        downtown_hotel_room = Room("hotel_room", "The Hotel Room", hotel_room_background, downtown_hotel_room_objects,
            visible = False, lighting_conditions = standard_indoor_lighting, darken = False)
        fancy_restaurant = Room("fancy_restaurant", "Restaurant", fancy_restaurant_background, [make_floor(), make_chair(), make_table()],
            visible = False, lighting_conditions = standard_indoor_lighting, privacy_level = 3, darken = False)
        coffee_shop = Room("coffee_shop", "Coffee Shop", coffee_shop_background, coffee_shop_objects, [coffee_shop_get_coffee_action],
            map_pos = [1,0], visible = True, lighting_conditions = standard_indoor_lighting, privacy_level = 3, accessible_func = coffee_shop_is_open)
        mom_office_lobby = Room("mom_office_lobby", "Vandenberg\u00A0Ltd. Lobby", lobby_background, [make_wall(), make_floor(), make_chair(), make_reception(), make_window()],
            actions = [mom_office_person_request_action],
            map_pos = [0,2], lighting_conditions = standard_indoor_lighting, privacy_level = 3, accessible_func = mom_office_is_open)
        mom_offices = Room("mom_office", "Vandenberg\u00A0Ltd. Offices", marketing_background, [make_wall(), make_floor(), make_chair(), make_desk(), make_window()],
            visible = False, lighting_conditions = standard_indoor_lighting, privacy_level = 2, accessible_func = mom_office_is_open)
        hospital = Room("hospital", "Atrium Hospital", hospital_background, hospital_objects,
            map_pos = [2,2], lighting_conditions = standard_outdoor_lighting, privacy_level = 3)
        hospital_room = Room("hospital_room", "Hospital Room", hospital_room_background, hospital_room_objects,
            visible = False, lighting_conditions = standard_indoor_lighting, darken = False)

        ## MALL ##
        mall = Room("mall", "Atrium", mall_background, [make_wall(), make_floor(), make_bench()],
            map_pos = [1,1], lighting_conditions = standard_indoor_lighting, privacy_level = 3, accessible_func = mall_is_open)
        home_store = Room("home_store", "Home Improvement Store", home_improvement_store_background, generic_store_objects,
            map_pos = [1,0], lighting_conditions = standard_indoor_lighting, privacy_level = 3, accessible_func = mall_is_open)
        clothing_store = Room("clothing_store", "Sak's Clothing Store", clothing_store_background, clothing_store_objects,
            map_pos = [2,2], lighting_conditions = standard_indoor_lighting, privacy_level = 3, accessible_func = mall_is_open)
        office_store = Room("supply_store", "Office Supply Store", office_store_background, generic_store_objects,
            map_pos = [2,1], lighting_conditions = standard_indoor_lighting, privacy_level = 3, accessible_func = mall_is_open)
        electronics_store = Room("electronics_store", "Electronics Store", electronics_store_background, generic_store_objects,
            map_pos = [0,1], lighting_conditions = standard_indoor_lighting, privacy_level = 3, accessible_func = mall_is_open)
        mall_salon = Room("salon", "Hair Salon", salon_background, hair_salon_objects,
            map_pos = [0,2], visible = True, lighting_conditions = standard_indoor_lighting, privacy_level = 3, accessible_func = hair_salon_is_open)
        gaming_cafe = Room("gaming_cafe", "Gaming Café", gaming_cafe_background, gaming_cafe_objects,
            actions = [gaming_cafe_grind_character_action, gaming_cafe_buy_max_level_token_action, gaming_cafe_adult_swim],
            map_pos = [1,2], visible = False, lighting_conditions = standard_indoor_lighting, privacy_level = 3, accessible_func = gaming_cafe_is_open)
        gaming_cafe_store_room = Room("gaming_cafe_store_room", "Gaming Café", gaming_cafe_store_room_background, [make_floor(), make_wall(), make_door(), make_chair(), make_table()],
            map_pos = [0,0], visible = False, lighting_conditions = standard_indoor_lighting, privacy_level = 0, darken = False)


        gym = Room("gym", "Gym", gym_background, [make_wall(), make_floor(), make_bench(), make_mirror()],
            map_pos = [1,1], lighting_conditions = standard_indoor_lighting, privacy_level = 3, accessible_func = gym_is_open, darken = False)
        gym_shower = Room("gym_shower", "Gym Shower", gym_shower_background, gym_shower_objects,
            map_pos = [2,1], visible = False, lighting_conditions = standard_indoor_lighting, privacy_level = 1, accessible_func = gym_is_open)

        sex_store = Room("sex_store", "Sex Store", sex_store_background, generic_store_objects,
            map_pos = [1,1], lighting_conditions = standard_indoor_lighting, privacy_level = 1, accessible_func = sex_shop_is_open)

        ## Mall supporting locations
        changing_room = Room("changing_room", "Changing Room", changing_room_background, changing_room_objects,
            visible = False, lighting_conditions = standard_indoor_lighting, privacy_level = 1, accessible_func = mall_is_open)

        ##Other Locations##
        aunt_apartment = Room("aunt_apartment", "Living Room", house_background, [make_floor(), make_wall(), make_couch(), make_table(), make_chair(), make_window()],
            map_pos = [1,1], visible = False, lighting_conditions = standard_indoor_lighting)
        aunt_bedroom = Room("aunt_bedroom", "Rebecca's Bedroom", standard_bedroom4_background, bedroom_objects,
            map_pos = [2,1],visible = False, lighting_conditions = standard_indoor_lighting)
        cousin_bedroom = Room("cousin_bedroom", "Gabrielle's Bedroom", cousin_bedroom_background, bedroom_objects,
            map_pos = [2,2], visible = False, lighting_conditions = standard_indoor_lighting, darken = False)

        university = Room("campus", "University Campus", campus_background, [make_grass(), make_bench()],
            map_pos = [1,1], visible = False, lighting_conditions = standard_outdoor_lighting, privacy_level = 2, accessible_func = university_is_open)
        university_library = Room("uni_library", "Library", university_library_background, [make_floor(), make_wall(), make_table(), make_chair(), make_couch()],
            map_pos = [0,1], visible = False, lighting_conditions = standard_indoor_lighting, privacy_level = 1, accessible_func = university_is_open)
        university_study_room = Room("study_room", "Study Room", university_study_room_background, [make_floor(), make_wall(), make_chair(), make_table(), make_window()],
            map_pos = [2,1], visible = False, lighting_conditions = standard_indoor_lighting, privacy_level = 1, accessible_func = university_is_open)

        strip_club_owner = Person.get_random_male_name()

        strip_club = Room("strip_club", strip_club_owner + "'s Gentlemen's Club", stripclub_background, [make_wall(), make_floor(), make_table(), make_chair(), make_stage(), make_pole()],
            actions = [strip_club_show_action, strip_club_set_uniforms_action],
            map_pos = [1,1], visible = False, lighting_conditions = standard_club_lighting, privacy_level = 1, accessible_func = strip_club_is_open, darken = False)
        bdsm_room = Room("bdsm_room", "BDSM\u00a0room", bdsm_room_background, bdsm_room_objects, [dungeon_room_appoint_slave_action],
            map_pos = [0,1], visible = False, lighting_conditions = standard_indoor_lighting, privacy_level = 1, accessible_func = strip_club_is_open, darken = False)


        police_station = Room("police_station", "Police Station", police_station_background, ceo_office_objects,
            map_pos = [0,1], visible = False, lighting_conditions = standard_indoor_lighting, privacy_level = 3, darken = False)
        police_jail = Room("police_jail", "Police Jail", police_jail_background, police_jail_objects,
            visible = False, lighting_conditions = standard_indoor_lighting, privacy_level = 1, darken = False)

        city_hall = Room("city_hall", "City Hall", outside_background, [make_wall(), make_floor(), make_chair(), make_reception(), make_window()],
            map_pos = [1,1], visible = False, lighting_conditions = standard_indoor_lighting, privacy_level = 3)

        # NOTE: People will not auto-leave purgatory -> to get her back in the game you need to change her location
        purgatory = Room("purgatory", "Hospital", outside_background, purgatory_objects,
            visible = False, lighting_conditions = standard_indoor_lighting)

        prostitute_bedroom = Room("Prostitute Bedroom", "Prostitute Bedroom", prostitute_bedroom_background, bedroom_objects + [make_love_rug],
            visible = False, lighting_conditions = standard_indoor_lighting)
        generic_bedroom_1 = Room("Generic Bedroom 1", "Bedroom", standard_bedroom1_background, bedroom_objects,
            visible = False, lighting_conditions = standard_indoor_lighting)
        generic_bedroom_2 = Room("Generic Bedroom 2", "Bedroom", standard_bedroom2_background, bedroom_objects,
            visible = False, lighting_conditions = standard_indoor_lighting)
        generic_bedroom_3 = Room("Generic Bedroom 3", "Bedroom", standard_bedroom3_background, bedroom_objects,
            visible = False, lighting_conditions = standard_indoor_lighting)
        generic_bedroom_4 = Room("Generic Bedroom 4", "Bedroom", standard_bedroom4_background, bedroom_objects,
            visible = False, lighting_conditions = standard_indoor_lighting)


        ##Keep a list of all the places##
        list_of_places = [
            bedroom,
            lily_bedroom,
            mom_bedroom,
            kitchen,
            hall,
            her_hallway,
            laundry_room,
            home_bathroom,
            home_shower,
            dungeon,
            harem_mansion,

            ceo_office,
            lobby,
            office,
            rd_division,
            testing_room,
            storage_room,
            break_room,
            p_division,
            m_division,
            work_bathroom,
            clone_facility,

            downtown,
            downtown_bar,
            downtown_hotel,
            downtown_hotel_room,
            fancy_restaurant,
            hospital,
            hospital_room,

            mall,
            office_store,
            clothing_store,
            changing_room,
            sex_store,
            home_store,
            gym,
            gym_shower,
            electronics_store,
            mall_salon,
            coffee_shop,
            gaming_cafe,
            gaming_cafe_store_room,

            aunt_apartment,
            aunt_bedroom,
            cousin_bedroom,

            university,
            university_library,
            university_study_room,

            strip_club,
            bdsm_room,

            mom_office_lobby,
            mom_offices,

            city_hall,
            police_station,
            police_jail,
            purgatory,

            prostitute_bedroom,
            generic_bedroom_1,
            generic_bedroom_2,
            generic_bedroom_3,
            generic_bedroom_4,
        ]

    return


label instantiate_map_hubs():
    python:
        # Map Hubs for grouped map locations
        mansion_name = str(last_name)+" Mansion"
        home_hub = MapHub("home", "Home", icon = "POI_House", position = Point(250, 475), locations = [hall, bedroom, lily_bedroom, mom_bedroom, kitchen, home_bathroom, dungeon, home_shower])
        aunt_home_hub = MapHub("aunt_home", "Rebecca's Apartment", icon = "POI_House", position = Point(150, 255), locations = [aunt_apartment,aunt_bedroom, cousin_bedroom])
        office_hub = MapHub("office", business_name, icon = "POI_Business", position = Point(1295, 365), locations = [lobby, m_division, p_division, rd_division, office, ceo_office, clone_facility, testing_room, work_bathroom, storage_room])
        mall_hub = MapHub("mall", "Shopping Mall", icon = "POI_Mall", position = Point(640, 360), locations = [mall, home_store, clothing_store, electronics_store, office_store, mall_salon, gaming_cafe, gaming_cafe_store_room], accessible_func = mall_is_open)
        sex_shop_hub = MapHub("sex_shop", "Starbuck's Sex\u00A0Shop", icon = "POI_Sexshop", position = Point(770, 120), locations = [sex_store], accessible_func = sex_shop_is_open)
        downtown_hub = MapHub("downtown", "Downtown", icon = "POI_Downtown", position = Point(560, 800), locations = [mom_office_lobby, mom_offices, downtown_bar, coffee_shop, downtown, downtown_hotel, downtown_hotel_room, fancy_restaurant, hospital, hospital_room])
        plaza_hub = MapHub("plaza", "City Plaza", icon = "POI_Police", position = Point(500, 550), locations = [city_hall, police_station, police_jail])
        gym_hub = MapHub("gym", "Gym", icon = "POI_Gym", position = Point(890, 615), locations = [gym, gym_shower], accessible_func = gym_is_open)
        university_hub = MapHub("university", "University", icon = "POI_Uni", position = Point(1165, 770), locations = [university, university_library, university_study_room], accessible_func = university_is_open)
        harem_hub = MapHub("mansion", str(mansion_name), icon = "POI_Brothel", position = Point(120, 660), locations = [harem_mansion])
        strip_club_hub = MapHub("stripclub", "Strip\u00A0Club", icon = "POI_Club", position = Point(800, 800), locations = [strip_club, bdsm_room], accessible_func = strip_club_is_open)

        residential_home_hub = HomeHub("residential", "Residential District", icon = "District_Residential", position = Point(380, 190),
            people = [camila, salon_manager, starbuck, emily, sakari, kaya, naomi],
            jobs = [doctor_job, lawyer_job, architect_job, interior_decorator_job, fashion_designer_job, prostitute_job,
                pro_gamer_job, stripper_job, secretary_job, nurse_job, night_nurse_job])

        industrial_home_hub = HomeHub("industrial", "Bay\u00A0Area Condos", icon = "District_Industrial", position = Point(1050, 210),
            people = [ellie, stephanie, ashley, sarah, alexia, candace],
            jobs = [hr_job, market_job, rd_job, supply_job, production_job, head_researcher_job, office_worker_job,
                home_improvement_support_job, electronics_support_job,
                stripclub_stripper_job, stripclub_waitress_job, stripclub_bdsm_performer_job, stripclub_manager_job, stripclub_mistress_job])

        downtown_home_hub = HomeHub("downtown_home", "Downtown Apartments", icon = "District_Downtown", position = Point(300, 765),
            people = [city_rep, myra, iris, police_chief],
            jobs = [unemployed_job, barista_job, bartender_job, waitress_job, hotel_receptionist_job, hotel_maid_job,
                hotel_maid_job2, hotel_chef_job, clothing_cashier_job, sex_cashier_job, electronics_cashier_job, supply_cashier_job,
                home_improvement_cashier_job, salon_hairdresser_job, store_assistant_job, store_clerk_job,
                gym_instructor_job, yoga_teacher_job, unemployed_job])

        university_home_hub = HomeHub("uni_home", "University Housing", icon = "District_ResidentialB", position = Point(1440, 820),
            people = [nora, erica],
            jobs = [university_professor_job, student_job, student_intern_market_job, student_intern_hr_job,
                student_intern_production_job, student_intern_rd_job, student_intern_supply_job])

        list_of_hubs = [home_hub, aunt_home_hub, office_hub, mall_hub, sex_shop_hub, downtown_hub, plaza_hub, strip_club_hub,
            gym_hub, university_hub, harem_hub, residential_home_hub, industrial_home_hub, downtown_home_hub, university_home_hub]

    return
