from __future__ import annotations
from game.main_character.MainCharacter_ren import mc
from game.major_game_classes.business_related.Policy_ren import Policy
from game.major_game_classes.character_related.Person_ren import Person
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
            desc = "Only seek applications from women who are oral virgins.\nRaises the cost of applicant screening by $250.",
            cost = 2500,
            toggleable = True,
            active_requirement = recruitment_knowledge_four_policy,
            dependant_policies = recruitment_knowledge_four_policy,
            #exclusive_tag = "mother_criteria",
            extra_data = {"oral_virgin": 0, "reveal_oral_virgin": True, "interview_cost_adjust": 250})

        global recruitment_anal_virgin_policy
        recruitment_anal_virgin_policy = Policy(name = "Screening Criteria: Anal Virgin",
            desc = "Only seek applications from women who are anal virgins.\nRaises the cost of applicant screening by $400.",
            cost = 3500,
            toggleable = True,
            active_requirement = recruitment_knowledge_four_policy,
            dependant_policies = recruitment_knowledge_four_policy,
            #exclusive_tag = "mother_criteria",
            extra_data = {"anal_virgin": 0, "reveal_anal_virgin": True, "interview_cost_adjust": 400})

        global recruitment_vaginal_virgin_policy
        recruitment_vaginal_virgin_policy = Policy(name = "Screening Criteria: Vaginal Virgin",
            desc = "Only seek applications from women who are vaginal virgins.\nRaises the cost of applicant screening by $1000.",
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
