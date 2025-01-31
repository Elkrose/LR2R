from __future__ import annotations
from game.main_character.MainCharacter_ren import mc
from game.major_game_classes.business_related.Policy_ren import Policy
from game.major_game_classes.character_related.Person_ren import Person
from game.helper_functions.list_functions_ren import all_policies_in_the_game
from game.business_policies.clothing_policies_ren import uniform_disobedience_on_move
from game.map.MapHub_ren import MapHub

#recruitment_policies_list: list[Policy] = []
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 3 python:
"""
#### RECRUITMENT IMPROVEMENT POLICIES ####
VIRGIN_TRACKER_DEBUG = True

def vt_init_recruitment_policies(wrapped_func: Callable) -> Callable:
    def wrapping_func(*args, **kwargs):

        ret_val = wrapped_func(*args, **kwargs)

        global recruitment_oral_virgin_policy
        recruitment_oral_virgin_policy = Policy(name = "Screening Criteria: Oral Virgin",
            desc = f"{b_name} Screening Criteria: Oral Virgin\n\nAt {b_name}, we're committed to maintaining a workforce that is dedicated to our values and mission. As part of our screening process, we're introducing a new criteria: Oral Virgin.\n\nTo be eligible for employment with {b_name}, applicants must meet the following requirement:\n\n* Never have engaged in oral sex or other forms of oral stimulation\n\nWe believe that this criteria is essential to ensuring that our employees are aligned with our company's values and are able to maintain a professional and respectful work environment.\n\nBy applying for a position with {b_name}, you acknowledge that you meet this requirement and are willing to undergo a thorough screening process to verify your eligibility. Please note that failure to disclose any relevant information may result in termination of employment or other disciplinary action.\n\nWe're excited to welcome new team members who share our values and are committed to our mission. If you're a motivated and dedicated individual who meets our screening criteria, we encourage you to apply for a position with {b_name} today!",
            cost = 2500,
            toggleable = True,
            active_requirement = recruitment_knowledge_four_policy,
            dependant_policies = recruitment_knowledge_four_policy,
            #exclusive_tag = "mother_criteria",
            extra_data = {"oral_virgin": 0, "reveal_oral_virgin": True, "interview_cost_adjust": 250})

        global recruitment_anal_virgin_policy
        recruitment_anal_virgin_policy = Policy(name = "Screening Criteria: Anal Virgin",
            desc = f"{b_name} Screening Criteria: Anal Virgin\n\nAt {b_name}, we're committed to maintaining a workforce that is dedicated to our values and mission. As part of our screening process, we're introducing a new criteria: Anal Virgin.\n\nTo be eligible for employment with {b_name}, applicants must meet the following requirement:\n\n* Never have engaged in anal sex or other forms of anal penetration\n\nWe believe that this criteria is essential to ensuring that our employees are aligned with our company's values and are able to maintain a professional and respectful work environment.\n\nBy applying for a position with {b_name}, you acknowledge that you meet this requirement and are willing to undergo a thorough screening process to verify your eligibility. Please note that failure to disclose any relevant information may result in termination of employment or other disciplinary action.\n\nWe're excited to welcome new team members who share our values and are committed to our mission. If you're a motivated and dedicated individual who meets our screening criteria, we encourage you to apply for a position with {b_name} today!",
            cost = 3500,
            toggleable = True,
            active_requirement = recruitment_knowledge_four_policy,
            dependant_policies = recruitment_knowledge_four_policy,
            #exclusive_tag = "mother_criteria",
            extra_data = {"anal_virgin": 0, "reveal_anal_virgin": True, "interview_cost_adjust": 400})

        global recruitment_vaginal_virgin_policy
        recruitment_vaginal_virgin_policy = Policy(name = "Screening Criteria: Vaginal Virgin",
            desc = f"{b_name} Screening Criteria: Vaginal Virgin\n\nAt {b_name}, we're committed to maintaining a workforce that is dedicated to our values and mission. As part of our screening process, we're introducing a new criteria: Vaginal Virgin.\n\nTo be eligible for employment with {b_name}, applicants must meet the following requirement:\n\n* Never have engaged in vaginal sex or other forms of vaginal penetration\n\nWe believe that this criteria is essential to ensuring that our employees are aligned with our company's values and are able to maintain a professional and respectful work environment.\n\nBy applying for a position with {b_name}, you acknowledge that you meet this requirement and are willing to undergo a thorough screening process to verify your eligibility. Please note that failure to disclose any relevant information may result in termination of employment or other disciplinary action.\n\nWe're excited to welcome new team members who share our values and are committed to our mission. If you're a motivated and dedicated individual who meets our screening criteria, we encourage you to apply for a position with {b_name} today!",
            cost = 5000,
            toggleable = True,
            active_requirement = recruitment_knowledge_four_policy,
            dependant_policies = recruitment_knowledge_four_policy,
            exclusive_tag = "mother_criteria",
            extra_data = {"kids_ceiling":0, "reveal_vaginal_virgin": True, "vaginal_virgin": 0, "interview_cost_adjust": 1000})

        global recruitment_policies_list
        recruitment_policies_list.extend((
            recruitment_oral_virgin_policy,
            recruitment_anal_virgin_policy,
            recruitment_vaginal_virgin_policy,
        ))
        return ret_val # probably None, but core could change
    wrapping_func.__signature__ = inspect.signature(wrapped_func)
    return wrapping_func
init_recruitment_policies         = vt_init_recruitment_policies(init_recruitment_policies)

def mandatory_remove_collars():
    for person in [x for x in mc.business.employee_list + mc.business.intern_list]: 
        person.outfit.remove_all_collars()
        person.base_outfit.remove_all_collars()
    return


def mandatory_policy_collar(person: Person, collar: Clothing, base_colour = [.05, .05, .05, 1], pattern="Pattern_1", pattern_colour = [.05, .05, .05, 1]):
    person.outfit.remove_all_collars()
    person.base_outfit.remove_all_collars()
    new_collar = collar.get_copy()
    new_collar.colour = base_colour
    new_collar.pattern = pattern
    new_collar.colour_pattern = pattern_colour
    person.base_outfit.add_accessory(new_collar)
    return

def mandatory_fertility_collar_policy_on_day():
    def mandatory_fertility_collar_based_stats(person: Person, obedience: int, effectiveness: int):
        #print("Toy change: {} -> {} {}".format(person.name, happiness, effectiveness))
        person.change_obedience(obedience, max_amount = 300, add_to_log = False)
        mc.business.change_team_effectiveness(effectiveness, instant = True)
        return effectiveness

    efficiency_change = 0
    for person in [x for x in mc.business.employee_list + mc.business.intern_list]:   
        if mandatory_plug_policy.is_active and not person.has_anal_fetish:
            if person.sluttiness < 30:
                efficiency_change += mandatory_fertility_collar_based_stats(person, -10, -3)
            elif person.sluttiness < 50:
                efficiency_change += mandatory_fertility_collar_based_stats(person, -5, -2)
            elif person.sluttiness < 70:
                efficiency_change += mandatory_fertility_collar_based_stats(person, -2, -1)
            elif person.sluttiness >= 70:
                efficiency_change += mandatory_fertility_collar_based_stats(person, 2, 1)
        if mandatory_bullet_policy.is_active and not person.has_breeding_fetish:
            if person.sluttiness < 30:
                efficiency_change += mandatory_fertility_collar_based_stats(person, -5, -2)
            elif person.sluttiness < 50:
                efficiency_change += mandatory_fertility_collar_based_stats(person, -2, -1)
            elif person.sluttiness >= 50:
                efficiency_change += mandatory_fertility_collar_based_stats(person, 2, 1)
        if mandatory_vibe_policy.is_active:
            if person.sluttiness < 30:
                efficiency_change += mandatory_fertility_collar_based_stats(person, -2, -1)
            elif person.sluttiness >= 30:
                efficiency_change += mandatory_fertility_collar_based_stats(person, 2, 1)

    if efficiency_change < 0:
        mc.business.add_normal_message(f"Your employees are getting annoyed and Team Efficiency is down by {abs(efficiency_change):.0f}% due to Mandatory BIO-Collar policies.")
    if efficiency_change > 0:
        mc.business.add_normal_message(f"Your employees are generally obedient and Team Efficiency is up by {abs(efficiency_change):.0f}% due to Mandatory BIO-Collar policies.")
    return

def mandatory_fertility_collar_policy_on_turn():
    #don't apply collars when business is closed
    if not mc.business.is_open_for_business:
        return

    #if business is open apply collars
    for person in [x for x in mc.business.employee_list + mc.business.intern_list]:
        #Black: Infertile or Menstrual Phase
        if person.is_infertile or person.on_birth_control:
            if person.has_breeding_fetish:
                mandatory_policy_collar(person, breed_collar, [.04, .04, .04, 1], "Pattern_1", [.97, .97, 1, 1])
            elif person.has_cum_fetish:
                mandatory_policy_collar(person, cum_slut_collar, [.04, .04, .04, 1], "Pattern_1", [.97, .97, 1, 1])
            elif person.sluttiness > 70 or person.has_vaginal_fetish or person.has_anal_fetish:
                mandatory_policy_collar(person, fuck_doll_collar, [.04, .04, .04, 1], "Pattern_1", [.97, .97, 1, 1])
            else: #no writing on the collar
                mandatory_policy_collar(person, fuck_doll_collar, [.04, .04, .04, 1], "Pattern_1", [.04, .04, .04, 1])
        #White: Pregnant
        elif person.is_pregnant:
            if person.has_breeding_fetish:
                mandatory_policy_collar(person, breed_collar, [1, 1, 1, 1], "Pattern_1", [.04, .04, .04, 1])
            elif person.has_cum_fetish:
                mandatory_policy_collar(person, cum_slut_collar, [1, 1, 1, 1], "Pattern_1", [.04, .04, .04, 1])
            elif person.sluttiness > 70 or person.has_vaginal_fetish or person.has_anal_fetish:
                mandatory_policy_collar(person, fuck_doll_collar, [1, 1, 1, 1], "Pattern_1", [.04, .04, .04, 1])
            else: #no writing on the collar
                mandatory_policy_collar(person, fuck_doll_collar, [1, 1, 1, 1], "Pattern_1", [1, 1, .1, 1])
        #Pink: Ovulation Phase
        elif person.is_highly_fertile:
            if person.has_breeding_fetish:
                mandatory_policy_collar(person, breed_me_collar, [.96, .29, .54, 1], "Pattern_1", [.97, .97, 1, 1])
            elif person.has_cum_fetish:
                mandatory_policy_collar(person, cum_slut_collar, [.96, .29, .54, 1], "Pattern_1", [.97, .97, 1, 1])
            elif person.sluttiness > 70 or person.has_vaginal_fetish or person.has_anal_fetish:
                mandatory_policy_collar(person, fuck_doll_collar, [.96, .29, .54, 1], "Pattern_1", [.97, .97, 1, 1])
            else: #no writing on the collar
                mandatory_policy_collar(person, fuck_doll_collar, [.96, .29, .54, 1], "Pattern_1", [.96, .29, .54, 1])
        #Red: Prolific Phase
        elif person.days_from_ideal_fertility <= 6:
            if person.has_breeding_fetish:
                mandatory_policy_collar(person, breed_collar, [.65, .01, .01, 1], "Pattern_1", [.97, .97, 1, 1])
            elif person.has_cum_fetish:
                mandatory_policy_collar(person, cum_slut_collar, [.65, .01, .01, 1], "Pattern_1", [.97, .97, 1, 1])
            elif person.sluttiness > 70 or person.has_vaginal_fetish or person.has_anal_fetish:
                mandatory_policy_collar(person, fuck_doll_collar, [.65, .01, .01, 1], "Pattern_1", [.97, .97, 1, 1])
            else: #no writing on the collar
                mandatory_policy_collar(person, fuck_doll_collar, [.65, .01, .01, 1], "Pattern_1", [.65, .01, .01, 1])
        #Grey: Secretory Phase
        elif person.days_from_ideal_fertility > 6:
            if person.has_breeding_fetish:
                mandatory_policy_collar(person, breed_collar, [.36, .36, .36, 1], "Pattern_1", [.97, .97, 1, 1])
            elif person.has_cum_fetish:
                mandatory_policy_collar(person, cum_slut_collar, [.36, .36, .36, 1], "Pattern_1", [.97, .97, 1, 1])
            elif person.sluttiness > 70 or person.has_vaginal_fetish or person.has_anal_fetish:
                mandatory_policy_collar(person, fuck_doll_collar, [.36, .36, .36, 1], "Pattern_1", [.97, .97, 1, 1])
            else: #no writing on the collar
                mandatory_policy_collar(person, fuck_doll_collar, [.36, .36, .36, 1], "Pattern_1", [.36, .36, .36, 1])
        

    return

def mandatory_collar_policy_on_day():
    def mandatory_collar_based_stats(person: Person, obedience: int, effectiveness: int):
        #print("Toy change: {} -> {} {}".format(person.name, happiness, effectiveness))
        person.change_obedience(obedience, max_amount = 300, add_to_log = False)
        mc.business.change_team_effectiveness(effectiveness, instant = True)
        return effectiveness

    efficiency_change = 0
    for person in [x for x in mc.business.employee_list + mc.business.intern_list]:
        mandatory_policy_collar(person, fuck_doll_collar)
        if mandatory_plug_policy.is_active and not person.has_anal_fetish:
            if person.sluttiness < 30:
                efficiency_change += mandatory_collar_based_stats(person, -10, -3)
            elif person.sluttiness < 50:
                efficiency_change += mandatory_collar_based_stats(person, -5, -2)
            elif person.sluttiness < 70:
                efficiency_change += mandatory_collar_based_stats(person, -2, -1)
            elif person.sluttiness >= 70:
                efficiency_change += mandatory_collar_based_stats(person, 2, 1)
        if mandatory_bullet_policy.is_active and not person.has_breeding_fetish:
            if person.sluttiness < 30:
                efficiency_change += mandatory_collar_based_stats(person, -5, -2)
            elif person.sluttiness < 50:
                efficiency_change += mandatory_collar_based_stats(person, -2, -1)
            elif person.sluttiness >= 50:
                efficiency_change += mandatory_collar_based_stats(person, 2, 1)
        if mandatory_vibe_policy.is_active:
            if person.sluttiness < 30:
                efficiency_change += mandatory_collar_based_stats(person, -2, -1)
            elif person.sluttiness >= 30:
                efficiency_change += mandatory_collar_based_stats(person, 2, 1)

    if efficiency_change < 0:
        mc.business.add_normal_message(f"Your employees are getting annoyed and Team Efficiency is down by {abs(efficiency_change):.0f}% due to Mandatory Collar policies.")
    if efficiency_change > 0:
        mc.business.add_normal_message(f"Your employees are generally obedient and Team Efficiency is up by {abs(efficiency_change):.0f}% due to Mandatory policies.")
    return

def mandatory_collar_policy_on_turn():
    if not mc.business.is_open_for_business:
        return
    
    modifier_percent = 0
    if mandatory_vibe_policy.is_active:
        modifier_percent += 0.15
    if mandatory_bullet_policy.is_active:
        modifier_percent += 0.2
    if mandatory_plug_policy.is_active:
        modifier_percent += 0.25
    for person in [x for x in mc.business.employee_list + mc.business.intern_list]:
        mandatory_policy_collar(person, fuck_doll_collar)
    return

def vt_init_clothing_policies(wrapped_func: Callable) -> Callable:
    def wrapping_func(*args, **kwargs):

        ret_val = wrapped_func(*args, **kwargs)

        global mandatory_collar_policy
        mandatory_collar_policy = Policy(
        name = "Mandatory Collar Policy",
        cost = 250000,
        desc = f"{b_name} Mandatory Collar Policy: Symbolizing Loyalty and Commitment\n\nAt {b_name}, we value loyalty and commitment above all else. That's why we're introducing our Mandatory Collar Policy, designed to symbolize your dedication to our company and its values.\n\nAs part of this policy, all employees are required to wear a collar at all times while on company premises. The collar serves as a visible reminder of your commitment to our company and its mission.\n\nBy wearing the collar, you acknowledge that you are a representative of {b_name} and are expected to uphold our company's values and standards. You also acknowledge that you are willing to submit to the authority of our company and its leadership.\n\nWe believe that this policy will help to foster a sense of community and shared purpose among our employees. So, wear your collar with pride and join us in our mission to build a stronger, more loyal team!",
        toggleable = True,
        own_requirement = dress_code_policy,
        dependant_policies = dress_code_policy,
        on_remove_function = mandatory_remove_collars,
        on_turn_function = mandatory_collar_policy_on_turn,
        on_day_function = mandatory_collar_policy_on_day)

        global mandatory_fertility_collar_policy
        mandatory_fertility_collar_policy = Policy(
        name = "Mandatory BIO-Collar Policy",
        cost = 500000,
        desc = f"{b_name} Mandatory BIO-Collar Policy: Unlocking Your Fertility Potential\n\nAt {b_name}, we're committed to harnessing the power of fertility to drive our success. That's why we're introducing our Mandatory BIO-Collar Policy, designed to monitor and regulate your fertility status in real-time.\n\nThe BIO-Collar is a revolutionary device that uses advanced biotechnology to track your menstrual cycle and fertility phases. The collar will display the following colors to indicate your fertility status:\n\n* Black: Infertile or Menstrual Phase\n* Red: Prolific Phase\n* Pink: Ovulation Phase\n* Grey: Secretory Phase\n* White: Pregnant\n\nBy wearing the BIO-Collar, you agree to serve, breed for, and protect {b_name} with your loyalty, respect, and womb. This commitment is essential to our company's growth and success, and we expect all employees to take their fertility responsibilities seriously.\n\nWe're excited to see the positive impact that this policy will have on our workplace culture and productivity. With the BIO-Collar, we'll be able to optimize our breeding program and ensure a bright future for {b_name}. So, wear your BIO-Collar with pride and join us in our mission to build a stronger, more fertile community!",
        toggleable = True,
        own_requirement = dress_code_policy,
        dependant_policies = dress_code_policy,
        on_remove_function = mandatory_remove_collars,
        on_turn_function = mandatory_fertility_collar_policy_on_turn,
        on_day_function = mandatory_fertility_collar_policy_on_day)

        global uniform_policies_list
        uniform_policies_list.extend((
            mandatory_collar_policy,
                mandatory_fertility_collar_policy,
            ))
        return ret_val # probably None, but core could change
    wrapping_func.__signature__ = inspect.signature(wrapped_func)
    return wrapping_func
init_clothing_policies         = vt_init_clothing_policies(init_clothing_policies)
