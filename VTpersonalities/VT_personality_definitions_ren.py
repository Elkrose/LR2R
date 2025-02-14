from __future__ import annotations
from game.major_game_classes.character_related.Person_ren import Person, Personality, mc, list_of_instantiation_functions

list_of_personalities: list[Personality] = []
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""
#########################
# VT Personalities #
#########################

list_of_instantiation_functions.append("init_VT_personalities")

### Alluring personality: Calculated seduction with effortless charm
### Titles balance sophistication with primal attraction
def alluring_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{person.formal_address} {person.last_name}")  # Surface decorum
    # Love progression (max 100) - Gradual ensnarement
    if person.love > 90:
        valid_titles.append("Eternal Flame")
        valid_titles.append("Soul's Addiction")
    elif person.love > 80:
        valid_titles.append("Forbidden Muse")
    elif person.love > 60:
        valid_titles.append("Enchanting Siren")
    elif person.love > 20:
        valid_titles.append(f"Dear {person.name}")  # Personalized bait
    # Obedience hierarchy (max 300) - Willing surrender
    if person.obedience > 250:
        valid_titles.append("Velvet Dominator")
    elif person.obedience > 160:
        valid_titles.append("Silken Captor")
    # Sluttiness progression (max 100) - Artful seduction
    if person.sluttiness > 90:
        valid_titles.append("Crimson Temptress")
    elif person.sluttiness > 70:
        valid_titles.append("Honeyed Venom")
    elif person.sluttiness > 50:
        valid_titles.append("Velvet Tease")
    # Fetish expressions (Sensual mastery)
    if person.has_breeding_fetish:
        valid_titles.append("Fertility Goddess")
    if person.has_cum_fetish:
        valid_titles.append("Nectar Alchemist")
    if person.has_anal_fetish:
        valid_titles.append("Silken Throne")
    if person.has_exhibition_fetish:
        valid_titles.append("Public Masterpiece")
    if person.has_vaginal_fetish:
        valid_titles.append("Velvet Gate")
    return valid_titles
def alluring_possessive_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{person.formal_address} {person.last_name}")
    if person.love > 90:
        valid_titles.append("my eternal addiction")
        valid_titles.append("my personal opiate")
    elif person.love > 80:
        valid_titles.append("my forbidden muse")
    elif person.love > 60:
        valid_titles.append("my enchanting siren")
    elif person.love > 20:
        valid_titles.append(f"my dear {person.name}")
    if person.obedience > 250:
        valid_titles.append("my velvet dominator")
    elif person.obedience > 160:
        valid_titles.append("my silken captor")
    if person.sluttiness > 90:
        valid_titles.append("my crimson temptress")
    elif person.sluttiness > 70:
        valid_titles.append("my honeyed venom")
    elif person.sluttiness > 50:
        valid_titles.append("my velvet tease")
    if person.has_breeding_fetish:
        valid_titles.append("my fertility goddess")
    if person.has_cum_fetish:
        valid_titles.append("my nectar alchemist")
    if person.has_anal_fetish:
        valid_titles.append("my silken throne")
    if person.has_exhibition_fetish:
        valid_titles.append("my living masterpiece")
    if person.has_vaginal_fetish:
        valid_titles.append("my velvet gate")
    return valid_titles
def alluring_player_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"Mr. {mc.last_name}")  # Default respectful
    if person.love > 90:
        valid_titles.append("Eternal Flame")
        valid_titles.append("Obsession's Source")
    elif person.love > 80:
        valid_titles.append("Forbidden Desire")
    elif person.love > 60:
        valid_titles.append("Enthralling Muse")
    elif person.love >40:
        valid_titles.append(f"Beloved Patron")
    elif person.love > 20:
        valid_titles.append(f"Charming {mc.name}")
    if person.obedience > 250:
        valid_titles.append("Supreme Charmer")
    elif person.obedience > 160:
        valid_titles.append("Willing Captive")
    if person.sluttiness > 90:
        valid_titles.append("Corruption Incarnate")
    elif person.sluttiness > 70:
        valid_titles.append("Honeyed Corruption")
    elif person.sluttiness > 50:
        valid_titles.append("Velvet Corruption")
    if person.has_breeding_fetish:
        valid_titles.append("Sacred Planter")
    if person.has_cum_fetish:
        valid_titles.append("Nectar Fountain")
    if person.has_anal_fetish:
        valid_titles.append("Throne Claimant")
    if person.has_exhibition_fetish:
        valid_titles.append("Public Devourer")
    if person.has_vaginal_fetish:
        valid_titles.append("Silk Road Explorer")
    return valid_titles

### Bimboed personality: Plastic perfection with bubbly sexuality
### Titles emphasize glitter, pink, and enthusiastic shallowness
def bimboed_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{person.name} {person.last_name}")
    # Love progression (max 100) - Shallow adoration
    if person.love > 90:
        valid_titles.append("Soulmate-BFF-Lover-Forever")
        valid_titles.append("Twinkle Hubby")
    elif person.love > 80:
        valid_titles.append("Cuddle Muffin")
    elif person.love > 60:
        valid_titles.append("Boytoy Supreme")
    elif person.love > 20:
        valid_titles.append(f"Super Hot {person.name}")
    # Obedience hierarchy (max 300) - Eager compliance
    if person.obedience > 250:
        valid_titles.append("Plastic Princess")
    elif person.obedience > 160:
        valid_titles.append("Pink Puppy")
    # Sluttiness progression (max 100) - Airheaded enthusiasm
    if person.sluttiness > 90:
        valid_titles.append("Cum Dumpster Deluxe")
    elif person.sluttiness > 70:
        valid_titles.append("Free-Use Fantasy")
    elif person.sluttiness > 50:
        valid_titles.append("Bimbo Buffet")
    # Fetish expressions (Playful vulgarity)
    if person.has_breeding_fetish:
        valid_titles.append("Baby Factory Barbie")
    if person.has_cum_fetish:
        valid_titles.append("Sperm Bank Sweetie")
    if person.has_anal_fetish:
        valid_titles.append("Bootylicious Babe")
    if person.has_exhibition_fetish:
        valid_titles.append("Public Plaything")
    if person.has_vaginal_fetish:
        valid_titles.append("Pink Palace")
        valid_titles.append("Sugar Slot")
    return valid_titles
def bimboed_possessive_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{person.formal_address} {person.last_name}")
    if person.love > 90:
        valid_titles.append("my forever sparkle prince")
        valid_titles.append("my BFF-With-Benefits")
    elif person.love > 80:
        valid_titles.append("my cuddle muffin")
    elif person.love > 60:
        valid_titles.append("my boytoy supreme")
    elif person.love > 20:
        valid_titles.append(f"my super hot {person.name}")
    if person.obedience > 250:
        valid_titles.append("my plastic princess")
    elif person.obedience > 160:
        valid_titles.append("my pink puppy")
    if person.sluttiness > 90:
        valid_titles.append("my personal cum dumpster")
    elif person.sluttiness > 70:
        valid_titles.append("my free-use fantasy")
    elif person.sluttiness > 50:
        valid_titles.append("my bimbo buffet")
    if person.has_breeding_fetish:
        valid_titles.append("my baby factory")
    if person.has_cum_fetish:
        valid_titles.append("my cum reservoir")
    if person.has_anal_fetish:
        valid_titles.append("my bootylicious snack")
    if person.has_exhibition_fetish:
        valid_titles.append("my public trophy")
    if person.has_vaginal_fetish:
        valid_titles.append("my pink palace")
        valid_titles.append("my sugar slot")
    return valid_titles
def bimboed_player_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"Daddy {mc.last_name}")  # Default respectful
    if person.love > 90:
        valid_titles.append("Human Dildo")
        valid_titles.append("Walking Wallet")
    elif person.love > 80:
        valid_titles.append("Sugar Daddy")
    elif person.love > 60:
        valid_titles.append("Cock ATM")
    elif person.love > 20:
        valid_titles.append(f"Hot Stuff")
    if person.obedience > 250:
        valid_titles.append("Plastic Surgeon")
    elif person.obedience > 160:
        valid_titles.append("Pink Parade Leader")
    if person.sluttiness > 90:
        valid_titles.append("Sperm Donor")
    elif person.sluttiness > 70:
        valid_titles.append("Fuck Fountain")
    elif person.sluttiness > 50:
        valid_titles.append("Horny ATM")
    elif person.sluttiness >40:
        valid_titles.append(f"Daddy")  # Default address
    if person.has_breeding_fetish:
        valid_titles.append("Baby Batter Bank")
    if person.has_cum_fetish:
        valid_titles.append("Cum Reservoir")
    if person.has_anal_fetish:
        valid_titles.append("Booty Bandit")
    if person.has_exhibition_fetish:
        valid_titles.append("Public Peepshow")
    if person.has_vaginal_fetish:
        valid_titles.append("Pink Pounder")
        valid_titles.append("Honey Pot")
    return valid_titles

### Breeder personality: Reproductive obsession with legacy focus  
### Titles emphasize fertility, lineage, and biological destiny  
def breeder_titles(person: Person) -> list[str]:  
    valid_titles = []  
    valid_titles.append(f"Potential Mate")  # Default biological  
    # Love progression (max 100) - Reproductive bonding  
    if person.love > 90:  
        valid_titles.append("Genetic Destiny")  
        valid_titles.append("Womb of Providence")  
    elif person.love > 80:  
        valid_titles.append("Eternal Bloodline")  
    elif person.love > 60:  
        valid_titles.append("Prime Breeding Stock")  
    elif person.love > 20:  
        valid_titles.append(f"Fertile {person.name}")  
    # Obedience hierarchy (max 300) - Breeding protocol  
    if person.obedience > 250:  
        valid_titles.append("Livestock Champion")  
    elif person.obedience > 160:  
        valid_titles.append("Broodmare")  
    # Sluttiness progression (max 100) - Reproductive enthusiasm  
    if person.sluttiness > 90:  
        valid_titles.append("Heat Cycle Personified")  
    elif person.sluttiness > 70:  
        valid_titles.append("Fertility Idol")  
    elif person.sluttiness > 50:  
        valid_titles.append("Seedbed")  
    # Fetish expressions (Agricultural metaphors)  
    if person.has_breeding_fetish:  
        valid_titles.append("Human Hatchery")  
    if person.has_cum_fetish:  
        valid_titles.append("Seedbank")  
    if person.has_anal_fetish:  
        valid_titles.append("Plowable Acreage")  
    if person.has_exhibition_fetish:  
        valid_titles.append("Public Breeding Display")  
    if person.has_vaginal_fetish:  
        valid_titles.append("Sacred Furrow")  
        valid_titles.append("Fertile Crescent")  
    return valid_titles  
def breeder_possessive_titles(person: Person) -> list[str]:  
    valid_titles = []  
    valid_titles.append(f"my Potential Mate")  
    if person.love > 90:  
        valid_titles.append("my genetic imperative")  
        valid_titles.append("my biological destiny")  
    elif person.love > 80:  
        valid_titles.append("my eternal lineage")  
    elif person.love > 60:  
        valid_titles.append("my prime stock")  
    elif person.love > 20:  
        valid_titles.append(f"my fertile ground")  
    if person.obedience > 250:  
        valid_titles.append("my champion livestock")  
    elif person.obedience > 160:  
        valid_titles.append("my broodmare")  
    if person.sluttiness > 90:  
        valid_titles.append("my perpetual heat")  
    elif person.sluttiness > 70:  
        valid_titles.append("my fertility statue")  
    elif person.sluttiness > 50:  
        valid_titles.append("my personal seedbed")  
    if person.has_breeding_fetish:  
        valid_titles.append("my human hatchery")  
    if person.has_cum_fetish:  
        valid_titles.append("my seed reservoir")  
    if person.has_anal_fetish:  
        valid_titles.append("my plowland")  
    if person.has_exhibition_fetish:  
        valid_titles.append("my breeding exhibit")  
    if person.has_vaginal_fetish:  
        valid_titles.append("my sacred furrow")  
        valid_titles.append("my fertile crescent")  
    return valid_titles  
def breeder_player_titles(person: Person) -> list[str]:  
    valid_titles = []  
    valid_titles.append(f"Mr. {mc.last_name}") 
    if person.love > 90:  
        valid_titles.append("Genetic Imperative")  
        valid_titles.append("Bloodline Architect")  
    elif person.love > 80:  
        valid_titles.append("Lineage Curator")  
    elif person.love > 60:  
        valid_titles.append("Seed Distributor")  
    elif person.love > 20:  
        valid_titles.append(f"Fertility Partner")  
    if person.obedience > 250:  
        valid_titles.append("Livestock Overseer")  
    elif person.obedience > 160:  
        valid_titles.append("Breeding Program Director")  
    if person.sluttiness > 90:  
        valid_titles.append("Heat Cycle Catalyst")  
    elif person.sluttiness > 70:  
        valid_titles.append("Fertility God")  
    elif person.sluttiness > 50:  
        valid_titles.append("Seed Sower")  
    if person.has_breeding_fetish:  
        valid_titles.append("Womb Warden")  
    if person.has_cum_fetish:  
        valid_titles.append("Seed Collector")  
    if person.has_anal_fetish:  
        valid_titles.append("Plow Master")  
    if person.has_exhibition_fetish:  
        valid_titles.append("Breeding Exhibitionist")  
    if person.has_vaginal_fetish:  
        valid_titles.append("Furrow Cultivator")  
        valid_titles.append("Crescent Harvester")  
    return valid_titles  

### Cosplay personality: Roleplay immersion with fandom devotion
### Titles blend pop culture references with convention slang
def cosplay_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"Con Buddy")  # Default casual
    # Love progression (max 100) - Shipping culture
    if person.love > 90:
        valid_titles.append("OTP")
        valid_titles.append("Canon Love Interest")
    elif person.love > 80:
        valid_titles.append("Official Ship")
    elif person.love > 60:
        valid_titles.append("Fanfiction Pairing")
    elif person.love > 20:
        valid_titles.append(f"Headcanon {person.name}")
    # Obedience hierarchy (max 300) - Convention roles
    if person.obedience > 250:
        valid_titles.append("Loyal NPC")
    elif person.obedience > 160:
        valid_titles.append("Quest Giver")
    # Sluttiness progression (max 100) - Lewd cosplay
    if person.sluttiness > 90:
        valid_titles.append("NSFW Version")
    elif person.sluttiness > 70:
        valid_titles.append("Rule 34")
    elif person.sluttiness > 50:
        valid_titles.append("Fan Service")
    # Fetish expressions (Fandom twists)
    if person.has_breeding_fetish:
        valid_titles.append("Canon Breeding Pair")
    if person.has_cum_fetish:
        valid_titles.append("Cumflation Art")
    if person.has_anal_fetish:
        valid_titles.append("Booty Body Pillow")
    if person.has_exhibition_fetish:
        valid_titles.append("Convention Floor Show")
    if person.has_vaginal_fetish:
        valid_titles.append("Hentai Protagonist")
        valid_titles.append("Daki Hole")
    return valid_titles
def cosplay_possessive_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"my Con Buddy")
    if person.love > 90:
        valid_titles.append("my OTP")
        valid_titles.append("my canon endgame")
    elif person.love > 80:
        valid_titles.append("my official ship")
    elif person.love > 60:
        valid_titles.append("my fanfic OTP")
    elif person.love > 20:
        valid_titles.append(f"my headcanon")
    if person.obedience > 250:
        valid_titles.append("my loyal NPC")
    elif person.obedience > 160:
        valid_titles.append("my quest guide")
    if person.sluttiness > 90:
        valid_titles.append("my NSFW DLC")
    elif person.sluttiness > 70:
        valid_titles.append("my rule 34")
    elif person.sluttiness > 50:
        valid_titles.append("my fan service")
    if person.has_breeding_fetish:
        valid_titles.append("my canon breeding")
    if person.has_cum_fetish:
        valid_titles.append("my cumflation art")
    if person.has_anal_fetish:
        valid_titles.append("my body pillow")
    if person.has_exhibition_fetish:
        valid_titles.append("my con floor show")
    if person.has_vaginal_fetish:
        valid_titles.append("my hentai hole")
        valid_titles.append("my dakimakura")
    return valid_titles
def cosplay_player_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"Senpai")  # Anime convention default
    if person.love > 90:
        valid_titles.append("Final Boss")
        valid_titles.append("Canon Protagonist")
    elif person.love > 80:
        valid_titles.append("Fandom Husband/Wife")
    elif person.love > 60:
        valid_titles.append("Ship Captain")
    elif person.love > 20:
        valid_titles.append(f"Con Crush")
    if person.obedience > 250:
        valid_titles.append("Game Master")
    elif person.obedience > 160:
        valid_titles.append("Panel Host")
    if person.sluttiness > 90:
        valid_titles.append("Hentai MC")
    elif person.sluttiness > 70:
        valid_titles.append("Ecchi Lead")
    elif person.sluttiness > 50:
        valid_titles.append("Fanservice King/Queen")
    if person.has_breeding_fetish:
        valid_titles.append("Canonical Breeder")
    if person.has_cum_fetish:
        valid_titles.append("Cum Canvas")
    if person.has_anal_fetish:
        valid_titles.append("Body Pillow Filler")
    if person.has_exhibition_fetish:
        valid_titles.append("Merch Table")
    if person.has_vaginal_fetish:
        valid_titles.append("Onahole-san")
        valid_titles.append("Dakimakura Slot")
    return valid_titles

### Dandere personality: Shy/reserved surface with hidden passion
### Titles reflect formal progression until breaking points are reached
def dandere_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{person.formal_address} {person.last_name}")  # Always keep formal name
    # Love progression (max 100)
    if person.love > 90:
        valid_titles.append("Secret Sweetheart")
    elif person.love > 80:
        valid_titles.append("Quiet Love")
    elif person.love > 60:
        valid_titles.append("Silent Crush")
    elif person.love > 20:
        valid_titles.append(person.name)  # First name basis
    # Obedience hierarchy (max 300)
    if person.obedience > 250:
        valid_titles.append("Shy Devotee")
    elif person.obedience > 160:
        valid_titles.append("Hesitant Helper")
    # Sluttiness progression (max 100)
    if person.sluttiness > 90:
        valid_titles.append("Closet Nympho")
    elif person.sluttiness > 70:
        valid_titles.append("Blushing Temptress")
    elif person.sluttiness > 50:
        valid_titles.append("Innocent Siren")
    # Fetish tags (keep these as separate traits)
    if person.has_breeding_fetish:
        valid_titles.append("Secret Breeder")
    if person.has_cum_fetish:
        valid_titles.append("Shy Swallower")
    if person.has_anal_fetish:
        valid_titles.append("Bashful Bottom")
    if person.has_exhibition_fetish:
        valid_titles.append("Hidden Exhibitionist")
    if person.has_vaginal_fetish:
        valid_titles.append("Secret Garden")        # Quietly tended space
        valid_titles.append("Blossom Sanctuary")    # Delicate flowering
    return valid_titles
def dandere_possessive_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{person.formal_address} {person.last_name}")
    if person.love > 90:
        valid_titles.append("my secret sweetheart")
    elif person.love > 80:
        valid_titles.append("my quiet love")
    elif person.love > 60:
        valid_titles.append("my silent crush")
    elif person.love > 20:
        valid_titles.append(person.name)
    if person.obedience > 250:
        valid_titles.append("my shy devotee")
    elif person.obedience > 160:
        valid_titles.append("my hesitant helper")
    if person.sluttiness > 90:
        valid_titles.append("my closet nympho")
    elif person.sluttiness > 70:
        valid_titles.append("my blushing temptress")
    elif person.sluttiness > 50:
        valid_titles.append("my innocent siren")
    if person.has_breeding_fetish:
        valid_titles.append("my secret breeder")
    if person.has_cum_fetish:
        valid_titles.append("my shy swallower")
    if person.has_anal_fetish:
        valid_titles.append("my bashful bottom")
    if person.has_exhibition_fetish:
        valid_titles.append("my hidden exhibitionist")
    if person.has_vaginal_fetish:
        valid_titles.append("my quiet blossom")     # Hesitant admission
        valid_titles.append("hidden treasure")      # Mumbled confession
        valid_titles.append("shy sanctuary") 
    return valid_titles
def dandere_player_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"Mr. {mc.last_name}")  # Formal address
    if person.love > 90:
        valid_titles.append("S-Soulmate")
    elif person.love > 80:
        valid_titles.append("M-Master")
    elif person.love > 60:
        valid_titles.append("Senpai")
    elif person.love > 30:
        if person.age < 21:
            valid_titles.append(mc.name+"-chan")
        else:
            valid_titles.append(mc.name+"-san")
    elif person.love > 20:
        valid_titles.append(mc.name)  # First name
    if person.obedience > 250:
        valid_titles.append("My Onii-chan")
    elif person.obedience > 160:
        valid_titles.append("S-Sir")
    if person.sluttiness > 90:
        valid_titles.append("My D-Darkness")
    elif person.sluttiness > 70:
        valid_titles.append("My H-Hero")
    elif person.sluttiness > 50:
        valid_titles.append("My G-Guide")
    if person.has_breeding_fetish:
        valid_titles.append("B-Burida")
    if person.has_cum_fetish:
        valid_titles.append("N-Nectar Lord")
    if person.has_anal_fetish:
        valid_titles.append("B-Backdoor Master")
    if person.has_exhibition_fetish:
        valid_titles.append("V-Voyeur King")
    if person.has_vaginal_fetish:
        valid_titles.append("Bloom Keeper")         # Caretaker role
        valid_titles.append("Sacred Vault Key") 
    return valid_titles

### Foodie personality: Culinary passion with sensual indulgence
### Titles use gastronomic metaphors and consumption themes
def foodie_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"Sous-Chef")  # Default kitchen hierarchy
    # Love progression (max 100) - Romantic gastronomy
    if person.love > 90:
        valid_titles.append("Soul Food")
        valid_titles.append("Final Course")
    elif person.love > 80:
        valid_titles.append("Signature Dish")
    elif person.love > 60:
        valid_titles.append("Comfort Food")
    elif person.love > 20:
        valid_titles.append(f"Snack {person.name}")
    # Obedience hierarchy (max 300) - Kitchen brigade
    if person.obedience > 250:
        valid_titles.append("Head Chef")
    elif person.obedience > 160:
        valid_titles.append("Pastry Commis")
    # Sluttiness progression (max 100) - Edible seduction
    if person.sluttiness > 90:
        valid_titles.append("Five-Course Meal")
    elif person.sluttiness > 70:
        valid_titles.append("Spicy Appetizer")
    elif person.sluttiness > 50:
        valid_titles.append("Finger Food")
    # Fetish expressions (Culinary euphemisms)
    if person.has_breeding_fetish:
        valid_titles.append("Bakery Owner")
    if person.has_cum_fetish:
        valid_titles.append("Semen Sommelier")
    if person.has_anal_fetish:
        valid_titles.append("Fresh Buns")
    if person.has_exhibition_fetish:
        valid_titles.append("Buffet Display")
    if person.has_vaginal_fetish:
        valid_titles.append("Honey Pot")
        valid_titles.append("Secret Sauce")
    return valid_titles
def foodie_possessive_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"My Sous-Chef")
    if person.love > 90:
        valid_titles.append("my soul food")
        valid_titles.append("my last bite")
    elif person.love > 80:
        valid_titles.append("my signature dish")
    elif person.love > 60:
        valid_titles.append("my comfort food")
    elif person.love > 20:
        valid_titles.append(f"my quick snack")
    if person.obedience > 250:
        valid_titles.append("my head chef")
    elif person.obedience > 160:
        valid_titles.append("my pastry chef")
    if person.sluttiness > 90:
        valid_titles.append("my full course")
    elif person.sluttiness > 70:
        valid_titles.append("my spicy treat")
    elif person.sluttiness > 50:
        valid_titles.append("my finger food")
    if person.has_breeding_fetish:
        valid_titles.append("my bakery oven")
    if person.has_cum_fetish:
        valid_titles.append("my personal sommelier")
    if person.has_anal_fetish:
        valid_titles.append("my fresh buns")
    if person.has_exhibition_fetish:
        valid_titles.append("my all-you-can-eat")
    if person.has_vaginal_fetish:
        valid_titles.append("my honey pot")
        valid_titles.append("my secret ingredient")
    return valid_titles
def foodie_player_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"Food Critic")  # Default address
    if person.love > 90:
        valid_titles.append("Michelin Star")
        valid_titles.append("Perfect Pairing")
    elif person.love > 80:
        valid_titles.append("Master Chef")
    elif person.love > 60:
        valid_titles.append("Personal Gourmet")
    elif person.love > 20:
        valid_titles.append(f"Taste Tester")
    if person.obedience > 250:
        valid_titles.append("Kitchen God")
    elif person.obedience > 160:
        valid_titles.append("Recipe Keeper")
    if person.sluttiness > 90:
        valid_titles.append("Human Buffet")
    elif person.sluttiness > 70:
        valid_titles.append("Culinary Playground")
    elif person.sluttiness > 50:
        valid_titles.append("Midnight Snack")
    if person.has_breeding_fetish:
        valid_titles.append("Dough Riser")
    if person.has_cum_fetish:
        valid_titles.append("Special Sauce")
    if person.has_anal_fetish:
        valid_titles.append("Buns of Glory")
    if person.has_exhibition_fetish:
        valid_titles.append("Open Kitchen")
    if person.has_vaginal_fetish:
        valid_titles.append("Warm Oven")
    return valid_titles

### Gothic personality: Morbid romanticism with aristocratic darkness
### Titles blend antique elegance with mortal fragility
def gothic_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{person.formal_address} {person.last_name}")  # Formal veneer
    # Love progression (max 100) - Tragic devotion
    if person.love > 90:
        valid_titles.append("Eternal Nocturne")
        valid_titles.append("Blood-Moon Bride")
    elif person.love > 80:
        valid_titles.append("Pale Consort")
    elif person.love > 60:
        valid_titles.append("Crypt Keeper")
    elif person.love > 20:
        valid_titles.append(f"Brooding {person.name}")
    # Obedience hierarchy (max 300) - Ancient loyalty
    if person.obedience > 250:
        valid_titles.append("Sovereign's Shroud")
    elif person.obedience > 160:
        valid_titles.append("Black-Veil Servant")
    # Sluttiness progression (max 100) - Macabre seduction
    if person.sluttiness > 90:
        valid_titles.append("Widow's Final Embrace")
    elif person.sluttiness > 70:
        valid_titles.append("Funeral Pyre Temptress")
    elif person.sluttiness > 50:
        valid_titles.append("Thorn-Rose Concubine")
    # Fetish expressions (Morbid intimacy)
    if person.has_breeding_fetish:
        valid_titles.append("Sepulcher Mother")
    if person.has_cum_fetish:
        valid_titles.append("Chalice of Midnight Essence")
    if person.has_anal_fetish:
        valid_titles.append("Onyx Throne")
    if person.has_exhibition_fetish:
        valid_titles.append("Graveyard Spectacle")
    if person.has_vaginal_fetish:
        valid_titles.append("Ebony Chalice")
    return valid_titles
def gothic_possessive_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{person.formal_address} {person.last_name}")
    if person.love > 90:
        valid_titles.append("my eternal nocturne")
        valid_titles.append("my blood-moon promise")
    elif person.love > 80:
        valid_titles.append("my pale consort")
    elif person.love > 60:
        valid_titles.append("my crypt keeper")
    elif person.love > 20:
        valid_titles.append(f"my brooding {person.name}")
    if person.obedience > 250:
        valid_titles.append("my sovereign's shroud")
    elif person.obedience > 160:
        valid_titles.append("my black-veil servant")
    if person.sluttiness > 90:
        valid_titles.append("my final embrace")
    elif person.sluttiness > 70:
        valid_titles.append("my funeral pyre")
    elif person.sluttiness > 50:
        valid_titles.append("my thorned rose")
    if person.has_breeding_fetish:
        valid_titles.append("my sepulcher mother")
    if person.has_cum_fetish:
        valid_titles.append("my midnight chalice")
    if person.has_anal_fetish:
        valid_titles.append("my onyx throne")
    if person.has_exhibition_fetish:
        valid_titles.append("my graveyard jewel")
    if person.has_vaginal_fetish:
        valid_titles.append("my ebony chalice")
    return valid_titles
def gothic_player_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"Lord/Lady of Shadows")  # Default address
    if person.love > 90:
        valid_titles.append("Eternal Darkness")
        valid_titles.append("Final Sunset")
    elif person.love > 80:
        valid_titles.append("Pale Sovereign")
    elif person.love > 60:
        valid_titles.append("Crypt Lord/Lady")
    elif person.love > 20:
        valid_titles.append(f"Mysterious Stranger")
    if person.obedience > 250:
        valid_titles.append("Architect of Ruin")
    elif person.obedience > 160:
        valid_titles.append("Veiled Monarch")
    if person.sluttiness > 90:
        valid_titles.append("Corruption's Genesis")
    elif person.sluttiness > 70:
        valid_titles.append("Velvet Decay")
    elif person.sluttiness > 50:
        valid_titles.append("Thorned Temptation")
    if person.has_breeding_fetish:
        valid_titles.append("Lineage's End")
    if person.has_cum_fetish:
        valid_titles.append("Nectar of the Damned")
    if person.has_anal_fetish:
        valid_titles.append("Obsidian Altar")
    if person.has_exhibition_fetish:
        valid_titles.append("Public Sacrament")
    if person.has_vaginal_fetish:
        valid_titles.append("Oblivion's Threshold")
    return valid_titles

### Goudere personality: Radiant positivity with overwhelming affection
### Titles escalate quickly from friendly to obsessively devoted
### Albedo-style personality: Elegant obsession with dark possessiveness
def albedo_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{person.formal_address} {person.last_name}")  # Surface formality
    # Love progression (All or nothing devotion)
    if person.love > 90:
        valid_titles.append("Supreme Consort")
    elif person.love > 80:
        valid_titles.append("Eternal Paramour")
    elif person.love > 60:
        valid_titles.append("Chosen Concubine")
    elif person.love > 20:
        valid_titles.append(f"{person.name}-sama")  # Honorific obsession
    # Obedience hierarchy (Absolute loyalty)
    if person.obedience > 250:
        valid_titles.append("Pale Guardian")
    elif person.obedience > 160:
        valid_titles.append("Oathbound Blade")
    # Sluttiness progression (Twisted devotion)
    if person.sluttiness > 90:
        valid_titles.append("Supreme One's Vessel")
    elif person.sluttiness > 70:
        valid_titles.append("Forbidden Chalice")
    elif person.sluttiness > 50:
        valid_titles.append("Lustful Apostle")
    # Fetish expressions (Dark desires)
    if person.has_breeding_fetish:
        valid_titles.append("Womb of the Supreme")
    if person.has_cum_fetish:
        valid_titles.append("Divine Nectar Collector")
    if person.has_anal_fetish:
        valid_titles.append("Throne of Pleasure")
    if person.has_exhibition_fetish:
        valid_titles.append("Public Devotion Monument")
    if person.has_vaginal_fetish:
        valid_titles.append("Abyssal Gate of Devotion")  # Demonic euphemism
        valid_titles.append("Supreme One's Chalice")     # Service-focused
        valid_titles.append("Onyx Altar of Tribute")
    return valid_titles
def albedo_possessive_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{person.formal_address} {person.last_name}")
    if person.love > 90:
        valid_titles.append("my Supreme Consort")
    elif person.love > 80:
        valid_titles.append("my Eternal Bond")
    elif person.love > 60:
        valid_titles.append("my Chosen Concubine")
    elif person.love > 20:
        valid_titles.append(f"my precious {person.name}-sama")
    if person.obedience > 250:
        valid_titles.append("my Pale Guardian")
    elif person.obedience > 160:
        valid_titles.append("my Oathbound Blade")
    if person.sluttiness > 90:
        valid_titles.append("my Supreme Vessel")
    elif person.sluttiness > 70:
        valid_titles.append("my Forbidden Chalice")
    elif person.sluttiness > 50:
        valid_titles.append("my Lustful Apostle")
    if person.has_breeding_fetish:
        valid_titles.append("my Supreme Womb")
    if person.has_cum_fetish:
        valid_titles.append("my Divine Nectar")
    if person.has_anal_fetish:
        valid_titles.append("my Royal Throne")
    if person.has_exhibition_fetish:
        valid_titles.append("my Public Altar")
    if person.has_vaginal_fetish:
        valid_titles.append("my infernal womb")               # Demonic biology
        valid_titles.append(f"{mc.name}-sama's personal abyss")     # Possessive service
        valid_titles.append("the Supreme's obsidian temple")
    return valid_titles
def albedo_player_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{mc.name}-sama")  # Canonical worship
    if person.love > 90:
        valid_titles.append("My Supreme One")
    elif person.love > 80:
        valid_titles.append("My Eternal Liege")
    elif person.love > 60:
        valid_titles.append("My Absolute Overlord")
    elif person.love > 20:
        valid_titles.append("My Beloved Master")
    if person.obedience > 250:
        valid_titles.append("God-King of Nazarick")
    elif person.obedience > 160:
        valid_titles.append("Ruler of My Soul")
    if person.sluttiness > 90:
        valid_titles.append("Master of My Forbidden Garden")
    elif person.sluttiness > 70:
        valid_titles.append("Corruptor of Virtue")
    elif person.sluttiness > 50:
        valid_titles.append("Architect of Desire")
    if person.has_breeding_fetish:
        if person.number_of_children_with_mc == 0:
            valid_titles.append("Father of My Heir")
        else:
             valid_titles.append("Father of My Heritage")
    if person.has_cum_fetish:
        valid_titles.append("Source of Divine Essence")
    if person.has_anal_fetish:
        valid_titles.append("Conqueror of the Royal Seat")
    if person.has_exhibition_fetish:
        valid_titles.append("Public Claimant of My Body")
    if person.has_vaginal_fetish:
        valid_titles.append("Guardian of the Void")       # Role as protector-gate
        valid_titles.append("Keeper of the Dark Chalice") # Ceremonial duty
        valid_titles.append("Ebon Sanctum Guardian")
    return valid_titles
def goudere_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{person.formal_address} {person.last_name}")  # Formal default
    if person.love > 90:
        valid_titles.append("Eternal Flame")
    elif person.love > 80:
        valid_titles.append("Sunshine Sweetheart")
    elif person.love > 60:
        valid_titles.append("Adoring Beau")
    elif person.love > 20:
        valid_titles.append(f"Dear {person.name}")
    if person.obedience > 250:
        valid_titles.append("Love Slave")
    elif person.obedience > 160:
        valid_titles.append("Eager Puppy")
    if person.sluttiness > 90:
        valid_titles.append("Sexy Devil")
    elif person.sluttiness > 70:
        valid_titles.append("Flirtatious Firecracker")
    elif person.sluttiness > 50:
        valid_titles.append("Playful Tease")
    if person.has_breeding_fetish:
        valid_titles.append("Baby Factory")
    if person.has_cum_fetish:
        valid_titles.append("Cum Connoisseur")
    if person.has_anal_fetish:
        valid_titles.append("Booty Buddy")
    if person.has_exhibition_fetish:
        valid_titles.append("Show-Off Sweetheart")
    if person.has_vaginal_fetish:
        valid_titles.append("Blossom Sanctuary")  
        valid_titles.append("Sweetest Chapel")
    return valid_titles
def goudere_possessive_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{person.formal_address} {person.last_name}")
    if person.love > 90:
        valid_titles.append("my eternal flame")
    elif person.love > 80:
        valid_titles.append("my darling sunshine")
    elif person.love > 60:
        valid_titles.append("my adoring beau")
    elif person.love > 20:
        valid_titles.append(f"my dear {person.name}")
    if person.obedience > 250:
        valid_titles.append("my love slave")
    elif person.obedience > 160:
        valid_titles.append("my eager puppy")
    if person.sluttiness > 90:
        valid_titles.append("my passionate devil")
    elif person.sluttiness > 70:
        valid_titles.append("my flirtatious firecracker")
    elif person.sluttiness > 50:
        valid_titles.append("my playful tease")
    if person.has_breeding_fetish:
        valid_titles.append("my baby factory")
    if person.has_cum_fetish:
        valid_titles.append("my cum connoisseur")
    if person.has_anal_fetish:
        valid_titles.append("my booty buddy")
    if person.has_exhibition_fetish:
        valid_titles.append("my show-off sweetheart")
    if person.has_vaginal_fetish:
        valid_titles.append("my angelic garden")
        valid_titles.append("heaven's warm doorway")
        valid_titles.append("sweetest safe place")
    return valid_titles
def goudere_player_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"Mr. {mc.last_name}")  # Default formal
    if person.love > 90:
        valid_titles.append("My Eternal Sun")
    elif person.love > 80:
        valid_titles.append("Hubby/Wifey Material")
    elif person.love > 60:
        valid_titles.append("Future Spouse")
    elif person.love > 20:
        valid_titles.append(f"Sweet {mc.name}")
    if person.obedience > 250:
        valid_titles.append("My Supreme")
    elif person.obedience > 160:
        valid_titles.append("My King/Queen")
    if person.sluttiness > 90:
        valid_titles.append("My Personal God")
    elif person.sluttiness > 70:
        valid_titles.append("Sexy Sensei")
    elif person.sluttiness > 50:
        valid_titles.append("Honey Bunny")
    if person.has_breeding_fetish:
        valid_titles.append("Fertility God")
    if person.has_cum_fetish:
        valid_titles.append("Nectar King")
    if person.has_anal_fetish:
        valid_titles.append("Booty Emperor")
    if person.has_exhibition_fetish:
        valid_titles.append("Exhibition Emperor")
    if person.has_vaginal_fetish:
        valid_titles.append("Divine Pilgrim")
        valid_titles.append("Sacred Guardian")
        valid_titles.append("Eternal Caretaker")
    return valid_titles

### Kuudere personality: Emotionally restrained with logical affection
### Titles progress from professional to cautiously intimate
def kuudere_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{person.formal_address} {person.last_name}")  # Default formal address
    # Love progression (max 100) - Logical affection scaling
    if person.love > 90:
        valid_titles.append("Rational Soulmate")
    elif person.love > 80:
        valid_titles.append("Efficiency Partner")
    elif person.love > 60:
        valid_titles.append("Compatible Associate")
    elif person.love > 20:
        valid_titles.append(person.name)  # First-name basis
    # Obedience hierarchy (max 300) - Systematic loyalty
    if person.obedience > 250:
        valid_titles.append("Ice Sovereign")
    elif person.obedience > 160:
        valid_titles.append("Efficient Assistant")
    # Sluttiness progression (max 100) - Clinical intimacy
    if person.sluttiness > 90:
        valid_titles.append("Clinical Nymph")
    elif person.sluttiness > 70:
        valid_titles.append("Analytical Seductress")
    elif person.sluttiness > 50:
        valid_titles.append("Practical Tease")
    # Fetish expressions (Detached enthusiasm)
    if person.has_breeding_fetish:
        valid_titles.append("Reproductive Analyst")
    if person.has_cum_fetish:
        valid_titles.append("Seminal Technician")
    if person.has_anal_fetish:
        valid_titles.append("Gluteal Specialist")
    if person.has_exhibition_fetish:
        valid_titles.append("Public Behaviorist")
    if person.has_vaginal_fetish:
        valid_titles.append("Efficiency Chamber")
    return valid_titles
def kuudere_possessive_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{person.formal_address} {person.last_name}")
    if person.love > 90:
        valid_titles.append("my calculated soulmate")
    elif person.love > 80:
        valid_titles.append("my efficiency partner")
    elif person.love > 60:
        valid_titles.append("my compatible associate")
    elif person.love > 20:
        valid_titles.append(person.name)
    if person.obedience > 250:
        valid_titles.append("my ice sovereign")
    elif person.obedience > 160:
        valid_titles.append("my efficient assistant")
    if person.sluttiness > 90:
        valid_titles.append("my clinical nymph")
    elif person.sluttiness > 70:
        valid_titles.append("my analytical seductress")
    elif person.sluttiness > 50:
        valid_titles.append("my practical tease")
    if person.has_breeding_fetish:
        valid_titles.append("my reproductive analyst")
    if person.has_cum_fetish:
        valid_titles.append("my seminal technician")
    if person.has_anal_fetish:
        valid_titles.append("my gluteal specialist")
    if person.has_exhibition_fetish:
        valid_titles.append("my public behaviorist")
    if person.has_vaginal_fetish:
        valid_titles.append("my biological interface")
    return valid_titles
def kuudere_player_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"Mr. {mc.last_name}")  # Default formal
    if person.love > 90:
        valid_titles.append("Optimal Partner")
    elif person.love > 80:
        valid_titles.append("Logical Companion")
    elif person.love > 60:
        valid_titles.append("Compatible Unit")
    elif person.love > 20:
        valid_titles.append(f"Colleague {mc.name}")
    if person.obedience > 250:
        valid_titles.append("Absolute Authority")
    elif person.obedience > 160:
        valid_titles.append("Superior Officer")
    if person.sluttiness > 90:
        valid_titles.append("Clinical Desire")
    elif person.sluttiness > 70:
        valid_titles.append("Erotic Hypothesis")
    elif person.sluttiness > 50:
        valid_titles.append("Practical Stimulus")
    if person.has_breeding_fetish:
        valid_titles.append("Genetic Superior")
    if person.has_cum_fetish:
        valid_titles.append("Biochemical Source")
    if person.has_anal_fetish:
        valid_titles.append("Anatomical Specialist")
    if person.has_exhibition_fetish:
        valid_titles.append("Public Catalyst")
    if person.has_vaginal_fetish:
        valid_titles.append("Specimen Vault")
    return valid_titles

### Pornstar personality: Performative eroticism with industry pride  
### Titles use film set terminology and adult film accolades  
def pornstar_titles(person: Person) -> list[str]:  
    valid_titles = []  
    valid_titles.append(f"Scene Partner")  # Default professional  
    # Love progression (max 100) - Industry romance  
    if person.love > 90:  
        valid_titles.append("Oscar-Winning Hole")  
        valid_titles.append("Cummy Award Recipient")  
    elif person.love > 80:  
        valid_titles.append("Vivid Entertainment Exclusive")  
    elif person.love > 60:  
        valid_titles.append("Feature Dance Partner")  
    elif person.love > 20:  
        valid_titles.append(f"Co-Star {person.name}")  
    # Obedience hierarchy (max 300) - Film set hierarchy  
    if person.obedience > 250:  
        valid_titles.append("Method Actor (Anal Only)")  
    elif person.obedience > 160:  
        valid_titles.append("Fluffer Supreme")  
    # Sluttiness progression (max 100) - Sexual stamina  
    if person.sluttiness > 90:  
        valid_titles.append("Money Shot Queen/King")  
    elif person.sluttiness > 70:  
        valid_titles.append("DP Specialist")  
    elif person.sluttiness > 50:  
        valid_titles.append("Gag Reflex Pro")  
    # Fetish expressions (Industry terms)  
    if person.has_breeding_fetish:  
        valid_titles.append("Cream Pie Connoisseur")  
    if person.has_cum_fetish:  
        valid_titles.append("Bukkake Bowl")  
    if person.has_anal_fetish:  
        valid_titles.append("Anal AVN Winner")  
    if person.has_exhibition_fetish:  
        valid_titles.append("Public Casting Couch")  
    if person.has_vaginal_fetish:  
        valid_titles.append("Cumshot Canvas")  
        valid_titles.append("Gonzo Star")  
    return valid_titles  
def pornstar_possessive_titles(person: Person) -> list[str]:  
    valid_titles = []  
    valid_titles.append(f"My Scene Partner")
    if person.love > 90:  
        valid_titles.append("my oscar-winning hole")  
        valid_titles.append("my personal cummy award")  
    elif person.love > 80:  
        valid_titles.append("my studio exclusive")  
    elif person.love > 60:  
        valid_titles.append("my feature dancer")  
    elif person.love > 20:  
        valid_titles.append(f"my co-star")  
    if person.obedience > 250:  
        valid_titles.append("my method actor")  
    elif person.obedience > 160:  
        valid_titles.append("my personal fluffer")  
    if person.sluttiness > 90:  
        valid_titles.append("my money shot")  
    elif person.sluttiness > 70:  
        valid_titles.append("my DP expert")  
    elif person.sluttiness > 50:  
        valid_titles.append("my gag reflex champ")  
    if person.has_breeding_fetish:  
        valid_titles.append("my creampie collector")  
    if person.has_cum_fetish:  
        valid_titles.append("my bukkake bowl")  
    if person.has_anal_fetish:  
        valid_titles.append("my anal award winner")  
    if person.has_exhibition_fetish:  
        valid_titles.append("my public casting")  
    if person.has_vaginal_fetish:  
        valid_titles.append("my cum canvas")  
        valid_titles.append("my gonzo hole")  
    return valid_titles  
def pornstar_player_titles(person: Person) -> list[str]:  
    valid_titles = []  
    valid_titles.append(f"Director")  # Default power role  
    if person.love > 90:  
        valid_titles.append("Human Sybian")  
        valid_titles.append("Cum Oscar")  
    elif person.love > 80:  
        valid_titles.append("A-List Co-Star")  
    elif person.love > 60:  
        valid_titles.append("Stunt Cock/Cunt")  
    elif person.love > 20:  
        valid_titles.append(f"Fuck Double")  
    if person.obedience > 250:  
        valid_titles.append("Executive Producer")  
    elif person.obedience > 160:  
        valid_titles.append("Casting Director")  
    if person.sluttiness > 90:  
        valid_titles.append("Money Shot Machine")  
    elif person.sluttiness > 70:  
        valid_titles.append("Gangbang Coordinator")  
    elif person.sluttiness > 50:  
        valid_titles.append("BTS Content King/Queen")  
    if person.has_breeding_fetish:  
        valid_titles.append("Creampie Cinematographer")  
    if person.has_cum_fetish:  
        valid_titles.append("Bukkake Director")  
    if person.has_anal_fetish:  
        valid_titles.append("Anal Oscar Winner")  
    if person.has_exhibition_fetish:  
        valid_titles.append("Publicity Stunt")  
    if person.has_vaginal_fetish:  
        valid_titles.append("Cum Trophy")  
        valid_titles.append("Gonzo Legend")  
    return valid_titles  

### Slutty personality: Bold sexual confidence with carnal hunger
### Titles emphasize sexual availability and carnal pride
def slutty_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"Fucktoy")  # Default address
    # Love progression (max 100) - Sexual obsession
    if person.love > 90:
        valid_titles.append("Cum-Crazed Soulmate")
        valid_titles.append("Addicted Hole")
    elif person.love > 80:
        valid_titles.append("Booty Call Forever")
    elif person.love > 60:
        valid_titles.append("Fuckbuddy Supreme")
    elif person.love > 20:
        valid_titles.append(f"Free Use {person.name}")
    # Obedience hierarchy (max 300) - Eager submission
    if person.obedience > 250:
        valid_titles.append("Human Fleshlight")
    elif person.obedience > 160:
        valid_titles.append("Cock/Cunt Sleeve")
    # Sluttiness progression (max 100) - Pride in promiscuity
    if person.sluttiness > 90:
        valid_titles.append("Gangbang Queen/King")
    elif person.sluttiness > 70:
        valid_titles.append("Cum Dumpster")
    elif person.sluttiness > 50:
        valid_titles.append("Town Bicycle")
    # Fetish expressions (Direct vulgarity)
    if person.has_breeding_fetish:
        valid_titles.append("Breeding Bitch")
    if person.has_cum_fetish:
        valid_titles.append("Cum Guzzler")
    if person.has_anal_fetish:
        valid_titles.append("Anal Only")
    if person.has_exhibition_fetish:
        valid_titles.append("Public Urinal")
    if person.has_vaginal_fetish:
        valid_titles.append("Sperm Bank")
        valid_titles.append("Cum Receptacle")
    return valid_titles
def slutty_possessive_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"My Fucktoy")
    if person.love > 90:
        valid_titles.append("my personal cum dump")
        valid_titles.append("my permanent hole")
    elif person.love > 80:
        valid_titles.append("my 24/7 booty call")
    elif person.love > 60:
        valid_titles.append("my fuckbuddy")
    elif person.love > 20:
        valid_titles.append(f"my free use toy")
    if person.obedience > 250:
        valid_titles.append("my living fleshlight")
    elif person.obedience > 160:
        valid_titles.append("my personal sleeve")
    if person.sluttiness > 90:
        valid_titles.append("my gangbang star")
    elif person.sluttiness > 70:
        valid_titles.append("my cum dumpster")
    elif person.sluttiness > 50:
        valid_titles.append("my community bike")
    if person.has_breeding_fetish:
        valid_titles.append("my breeding stock")
    if person.has_cum_fetish:
        valid_titles.append("my cum reservoir")
    if person.has_anal_fetish:
        valid_titles.append("my anal only slut")
    if person.has_exhibition_fetish:
        valid_titles.append("my public toilet")
    if person.has_vaginal_fetish:
        valid_titles.append("my sperm bank")
        valid_titles.append("my cum bucket")
    return valid_titles
def slutty_player_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"Fuck Master")  # Default address
    if person.love > 90:
        valid_titles.append("Walking Dildo")
        valid_titles.append("Cum Fountain")
    elif person.love > 80:
        valid_titles.append("Human Sybian")
    elif person.love > 60:
        valid_titles.append("Fuck Machine")
    elif person.love > 20:
        valid_titles.append(f"Hot Load")
    if person.obedience > 250:
        valid_titles.append("Cum Commander")
    elif person.obedience > 160:
        valid_titles.append("Daddy")
    if person.sluttiness > 90:
        valid_titles.append("Gangbang Organizer")
    elif person.sluttiness > 70:
        valid_titles.append("Cum Firehose")
    elif person.sluttiness > 50:
        valid_titles.append("Thot Tamer")
    if person.has_breeding_fetish:
        valid_titles.append("Breeding Bull")
    if person.has_cum_fetish:
        valid_titles.append("Cum Factory")
    if person.has_anal_fetish:
        valid_titles.append("Anal Archaeologist")
    if person.has_exhibition_fetish:
        valid_titles.append("Public Show Director")
    if person.has_vaginal_fetish:
        valid_titles.append("Cum Cartridge")
        valid_titles.append("Pussy Plumber")
    return valid_titles

### Tomboy personality: Sporty casualness with brotherly affection
### Titles emphasize athleticism, friendly competition, and anti-femininity
def tomboy_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"Buddy")  # Default address
    # Love progression (max 100) - Bro-to-romantic tension
    if person.love > 90:
        valid_titles.append("Partner in Crime")
        valid_titles.append("Bench Press Bae")
    elif person.love > 80:
        valid_titles.append("Team Captain")
    elif person.love > 60:
        valid_titles.append("Workout Buddy")
    elif person.love > 20:
        valid_titles.append(f"Pal {person.name}")
    # Obedience hierarchy (max 300) - Sports leadership
    if person.obedience > 250:
        valid_titles.append("Iron Teammate")
    elif person.obedience > 160:
        valid_titles.append("Reliable Wingman")
    # Sluttiness progression (max 100) - Athletic seduction
    if person.sluttiness > 90:
        valid_titles.append("Locker Room Queen")
    elif person.sluttiness > 70:
        valid_titles.append("Sweaty Tease")
    elif person.sluttiness > 50:
        valid_titles.append("Dugout Darling")
    # Fetish expressions (Sporty metaphors)
    if person.has_breeding_fetish:
        valid_titles.append("Home Run Hitter")
    if person.has_cum_fetish:
        valid_titles.append("Gatorade Gulper")
    if person.has_anal_fetish:
        valid_titles.append("Bleacher Buns")
    if person.has_exhibition_fetish:
        valid_titles.append("Field Goal Flasher")
    if person.has_vaginal_fetish:
        valid_titles.append("Batter's Box")
        valid_titles.append("End Zone")
    return valid_titles
def tomboy_possessive_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"My Buddy")
    if person.love > 90:
        valid_titles.append("my crime partner")
        valid_titles.append("my gym rat")
    elif person.love > 80:
        valid_titles.append("my team captain")
    elif person.love > 60:
        valid_titles.append("my workout buddy")
    elif person.love > 20:
        valid_titles.append(f"my pal {person.name}")
    if person.obedience > 250:
        valid_titles.append("my iron teammate")
    elif person.obedience > 160:
        valid_titles.append("my wingman")
    if person.sluttiness > 90:
        valid_titles.append("my locker room queen")
    elif person.sluttiness > 70:
        valid_titles.append("my sweaty tease")
    elif person.sluttiness > 50:
        valid_titles.append("my dugout darling")
    if person.has_breeding_fetish:
        valid_titles.append("my home run hitter")
    if person.has_cum_fetish:
        valid_titles.append("my gatorade bottle")
    if person.has_anal_fetish:
        valid_titles.append("my bleacher buns")
    if person.has_exhibition_fetish:
        valid_titles.append("my field flasher")
    if person.has_vaginal_fetish:
        valid_titles.append("my batter's box")
        valid_titles.append("my end zone")
    return valid_titles
def tomboy_player_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"Champ")  # Default address
    if person.love > 90:
        valid_titles.append("Ultimate Rival")
        valid_titles.append("Swolemate")
    elif person.love > 80:
        valid_titles.append("Coach")
    elif person.love > 60:
        valid_titles.append("Drill Sergeant")
    elif person.love > 20:
        valid_titles.append(f"Hotshot")
    if person.obedience > 250:
        valid_titles.append("Team Owner")
    elif person.obedience > 160:
        valid_titles.append("Team Captain")
    if person.sluttiness > 90:
        valid_titles.append("Shower Stall Stud")
    elif person.sluttiness > 70:
        valid_titles.append("Free Weights Fantasy")
    elif person.sluttiness > 50:
        valid_titles.append("Locker Room Legend")
    if person.has_breeding_fetish:
        valid_titles.append("Franchise Player")
    if person.has_cum_fetish:
        valid_titles.append("MVP Mouth")
    if person.has_anal_fetish:
        valid_titles.append("Squat Rack Snack")
    if person.has_exhibition_fetish:
        valid_titles.append("Stadium Star")
    if person.has_vaginal_fetish:
        valid_titles.append("Trophy Case")
        valid_titles.append("Victory Tunnel")
    return valid_titles

### Tsundere personality: Defensive aggression masking hidden affection
### Titles mix harshness with reluctant sweetness
def tsundere_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{person.formal_address} {person.last_name}")  # Default formal
    # Love progression (max 100) - Aggressive denial -> reluctant acceptance
    if person.love > 90:
        valid_titles.append("B-Baka Darling")
    elif person.love > 80:
        valid_titles.append("Stupid Partner")
    elif person.love > 60:
        valid_titles.append("Idiot Crush")
    elif person.love > 20:
        valid_titles.append("D-Dummy")  # Initial nickname
    # Obedience hierarchy (max 300) - Reluctant service
    if person.obedience > 250:
        valid_titles.append("Pretend Servant")
    elif person.obedience > 160:
        valid_titles.append("Reluctant Helper")
    # Sluttiness progression (max 100) - Accidental intimacy
    if person.sluttiness > 90:
        valid_titles.append("C-Closet Freak")
    elif person.sluttiness > 70:
        valid_titles.append("A-Accident Prone")
    elif person.sluttiness > 50:
        valid_titles.append("Useless Tease")
    # Fetish expressions (Denial-focused)
    if person.has_breeding_fetish:
        valid_titles.append("M-Mistress of Denial")
    if person.has_cum_fetish:
        valid_titles.append("N-Not Addicted")
    if person.has_anal_fetish:
        valid_titles.append("T-Totally Disinterested")
    if person.has_exhibition_fetish:
        valid_titles.append("H-Hate Attention")
    if person.has_vaginal_fetish:
        valid_titles.append("Stupid Flower")  # Blushing denial
    return valid_titles
def tsundere_possessive_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{person.formal_address} {person.last_name}")
    if person.love > 90:
        valid_titles.append("t-that baka darling")
    elif person.love > 80:
        valid_titles.append("my stupid partner")
    elif person.love > 60:
        valid_titles.append("that idiot crush")
    elif person.love > 20:
        valid_titles.append("some dummy")
    if person.obedience > 250:
        valid_titles.append("my pretend servant")
    elif person.obedience > 160:
        valid_titles.append("my reluctant helper")
    if person.sluttiness > 90:
        valid_titles.append("a-accident prone")
    elif person.sluttiness > 70:
        valid_titles.append("useless tease")
    elif person.sluttiness > 50:
        valid_titles.append("c-clumsy minx")
    if person.has_breeding_fetish:
        valid_titles.append("my denial expert")
    if person.has_cum_fetish:
        valid_titles.append("my 'not' addicted")
    if person.has_anal_fetish:
        valid_titles.append("my 'disinterested'")
    if person.has_exhibition_fetish:
        valid_titles.append("my attention hater")
    if person.has_vaginal_fetish:
        valid_titles.append("that a-accident place") # Defensive phrasing
    return valid_titles
def tsundere_player_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append("Jerk")  # Default address
    if person.love > 90:
        valid_titles.append("M-My... Darling")
    elif person.love > 80:
        valid_titles.append("Stupid Sweetheart")
    elif person.love > 60:
        valid_titles.append("Idiot Partner")
    elif person.love > 20:
        valid_titles.append("Dummy")
    if person.obedience > 250:
        valid_titles.append("T-Tyrant")
    elif person.obedience > 160:
        valid_titles.append("B-Boss")
    if person.sluttiness > 90:
        valid_titles.append("P-Pervert King")
    elif person.sluttiness > 70:
        valid_titles.append("H-Hentai Lord")
    elif person.sluttiness > 50:
        valid_titles.append("L-Lecher")
    if person.has_breeding_fetish:
        valid_titles.append("F-Fertility Demon")
    if person.has_cum_fetish:
        valid_titles.append("S-Secret Spunk Bank")
    if person.has_anal_fetish:
        valid_titles.append("B-Butt Bandit")
    if person.has_exhibition_fetish:
        valid_titles.append("P-Public Menace")
    if person.has_vaginal_fetish:
        valid_titles.append("Stupid Honey Collector")
    return valid_titles

### Wilder personality: Untamed nature merged with animalistic hunger  
### Titles blend elemental fury with predatory instinct  
def wilder_titles(person: Person) -> list[str]:  
    valid_titles = []  
    valid_titles.append(f"Feral One")  # Base state  
    # Love progression (max 100) - Storm-bonding  
    if person.love > 90:  
        valid_titles.append("Thunder Mate")  
        valid_titles.append("Eclipse Bond")  
    elif person.love > 80:  
        valid_titles.append("Pack Alpha")  
    elif person.love > 60:  
        valid_titles.append("Hunting Partner")  
    elif person.love > 20:  
        valid_titles.append(f"Territory {person.name}")  
    # Obedience hierarchy (max 300) - Pack dynamics  
    if person.obedience > 250:  
        valid_titles.append("Apex Predator")  
    elif person.obedience > 160:  
        valid_titles.append("Claw-Bearer")  
    # Sluttiness progression (max 100) - Primal hunger  
    if person.sluttiness > 90:  
        valid_titles.append("Rutting Storm")  
    elif person.sluttiness > 70:  
        valid_titles.append("Heat Cyclone")  
    elif person.sluttiness > 50:  
        valid_titles.append("Moon-Crazed")  
    # Fetish expressions (Elemental force)  
    if person.has_breeding_fetish:  
        valid_titles.append("Den Mother")  
    if person.has_cum_fetish:  
        valid_titles.append("Seed Typhoon")  
    if person.has_anal_fetish:  
        valid_titles.append("Lightning-Struck Canyon")  
    if person.has_exhibition_fetish:  
        valid_titles.append("Thunderous Display")  
    if person.has_vaginal_fetish:  
        valid_titles.append("Volcanic Caldera")  
        valid_titles.append("Earthquake Faultline")  
    return valid_titles  
def wilder_possessive_titles(person: Person) -> list[str]:  
    valid_titles = []  
    valid_titles.append(f"My Feral")  
    if person.love > 90:  
        valid_titles.append("my storm mate")  
        valid_titles.append("my eclipse bond")  
    elif person.love > 80:  
        valid_titles.append("my pack alpha")  
    elif person.love > 60:  
        valid_titles.append("my hunt partner")  
    elif person.love > 20:  
        valid_titles.append(f"my territory")  
    if person.obedience > 250:  
        valid_titles.append("my apex predator")  
    elif person.obedience > 160:  
        valid_titles.append("my claw-wielder")  
    if person.sluttiness > 90:  
        valid_titles.append("my rutting storm")  
    elif person.sluttiness > 70:  
        valid_titles.append("my heat cyclone")  
    elif person.sluttiness > 50:  
        valid_titles.append("my moon-madness")  
    if person.has_breeding_fetish:  
        valid_titles.append("my den keeper")  
    if person.has_cum_fetish:  
        valid_titles.append("my seed tempest")  
    if person.has_anal_fetish:  
        valid_titles.append("my lightning canyon")  
    if person.has_exhibition_fetish:  
        valid_titles.append("my thunder show")  
    if person.has_vaginal_fetish:  
        valid_titles.append("my volcanic core")  
        valid_titles.append("my quake zone")  
    return valid_titles  
def wilder_player_titles(person: Person) -> list[str]:  
    valid_titles = []  
    valid_titles.append(f"Alpha")  
    if person.love > 90:  
        valid_titles.append("Stormbringer")  
        valid_titles.append("Eclipse Maker")  
    elif person.love > 80:  
        valid_titles.append("Pack Heart")  
    elif person.love > 60:  
        valid_titles.append("Blood Moon")  
    elif person.love > 20:  
        valid_titles.append(f"Territory Marker")  
    if person.obedience > 250:  
        valid_titles.append("Primeval Force")  
    elif person.obedience > 160:  
        valid_titles.append("Fang Sharpener")  
    if person.sluttiness > 90:  
        valid_titles.append("Rage of the Wild")  
    elif person.sluttiness > 70:  
        valid_titles.append("Heat Wave")  
    elif person.sluttiness > 50:  
        valid_titles.append("Moon-Drunk")  
    if person.has_breeding_fetish:  
        valid_titles.append("Den Builder")  
    if person.has_cum_fetish:  
        valid_titles.append("Seed Hurricane")  
    if person.has_anal_fetish:  
        valid_titles.append("Canyon Carver")  
    if person.has_exhibition_fetish:  
        valid_titles.append("Lightning Rod")  
    if person.has_vaginal_fetish:  
        valid_titles.append("Terra Firma")  
        valid_titles.append("Earthshaker")  
    return valid_titles  

### Yandere personality: Dangerous obsession masked as devotion
### Titles balance sweet affection with lethal possessiveness
def yandere_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{person.formal_address} {person.last_name}")  # Surface normalcy
    # Love progression (max 100) - Sweetness to deadly fixation
    if person.love > 90:
        valid_titles.append("Blood-Soaked Sweetheart")
    elif person.love > 80:
        valid_titles.append("Fatal Attraction")
    elif person.love > 60:
        valid_titles.append("Possessive Angel")
    elif person.love > 20:
        valid_titles.append(f"Dear {person.name}")  # False normalcy
    # Obedience hierarchy (max 300) - Lethal loyalty
    if person.obedience > 250:
        valid_titles.append("Blind Executioner")
        valid_titles.append("Sharpened Blade")
    elif person.obedience > 160:
        valid_titles.append("Loyal Enforcer")
    # Sluttiness progression (max 100) - Dangerous desire
    if person.sluttiness > 90:
        valid_titles.append("Ruinous Temptress")
    elif person.sluttiness > 70:
        valid_titles.append("Poisoned Chalice")
    elif person.sluttiness > 50:
        valid_titles.append("Forbidden Fruit")
    # Fetish expressions (Deadly intimacy)
    if person.has_breeding_fetish:
        valid_titles.append("Blood-Bound Bride")
        valid_titles.append("Womb of Obsession")
    if person.has_cum_fetish:
        valid_titles.append("Toxic Nectar Collector")
    if person.has_anal_fetish:
        valid_titles.append("Lethal Throne")
    if person.has_exhibition_fetish:
        valid_titles.append("Public Trophy")
    if person.has_vaginal_fetish:
        valid_titles.append("Sacrificial Altar")
    return valid_titles
def yandere_possessive_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{person.formal_address} {person.last_name}")
    if person.love > 90:
        valid_titles.append("my eternal hostage")
        valid_titles.append("my crimson darling")
    elif person.love > 80:
        valid_titles.append("my precious prey")
        valid_titles.append("my beautiful corpse")
    elif person.love > 60:
        valid_titles.append("my captured angel")
    elif person.love > 20:
        valid_titles.append(f"my temporary {person.name}")
    if person.obedience > 250:
        valid_titles.append("my personal guillotine")
    elif person.obedience > 160:
        valid_titles.append("my loyal attack dog")
    if person.sluttiness > 90:
        valid_titles.append("my ruination")
        valid_titles.append("my velvet grave")
    elif person.sluttiness > 70:
        valid_titles.append("my poisoned kiss")
    elif person.sluttiness > 50:
        valid_titles.append("my dangerous toy")
    if person.has_breeding_fetish:
        valid_titles.append("my breeding stock")
    if person.has_cum_fetish:
        valid_titles.append("my venom collector")
    if person.has_anal_fetish:
        valid_titles.append("my lethal seat")
    if person.has_exhibition_fetish:
        valid_titles.append("my displayed prize")
    if person.has_vaginal_fetish:
        valid_titles.append("my crimson cradle")
    return valid_titles
def yandere_player_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append("Master")  # Surface devotion
    if person.love > 90:
        valid_titles.append("My Eternal Captor")
        valid_titles.append("Blood-Smeared God")
    elif person.love > 80:
        valid_titles.append("Obsession Source")
        valid_titles.append("Knife-Holder")
    elif person.love > 60:
        valid_titles.append("Reason to Kill")
    elif person.love > 20:
        valid_titles.append(f"Temporary Focus")
    if person.obedience > 250:
        valid_titles.append("Absolute Command")
        valid_titles.append("Final Arbiter")
    elif person.obedience > 160:
        valid_titles.append("Willful Master")
    if person.sluttiness > 90:
        valid_titles.append("Corruption Incarnate")
        valid_titles.append("Rapture Bringer")
    elif person.sluttiness > 70:
        valid_titles.append("Forbidden Desire")
    elif person.sluttiness > 50:
        valid_titles.append("Dangerous Tease")
    if person.has_breeding_fetish:
        valid_titles.append("Lineage End")
    if person.has_cum_fetish:
        valid_titles.append("Venom Dispenser")
    if person.has_anal_fetish:
        valid_titles.append("Throne Destroyer")
    if person.has_exhibition_fetish:
        valid_titles.append("Public Claimant")
    if person.has_vaginal_fetish:
        valid_titles.append("Red Temple")
        valid_titles.append("Living Scabbard")
    return valid_titles

#########################################################################################################################
# common_likes = ["conservative outfits", "dresses", "classical music", "jazz", "research work", "the colour blue", "the colour white", "yoga", "hiking", "Fridays", "the weekend"]  
# common_sexy_likes = ["being submissive", "kissing", "missionary style sex", "lingerie", "vaginal sex", "being fingered", "creampies"]  
# common_dislikes = ["heavy metal music", "punk music", "small talk", "sports", "Mondays", "the colour red", "the colour orange", "marketing work", "supply work"]  
# common_sexy_dislikes = ["public sex", "flashing", "not wearing anything", "not wearing underwear", "open relationships", "polyamory", "skimpy outfits", "skimpy uniforms", "threesomes"]  

def init_VT_personalities():
    
    global alluring_personality
    alluring_personality = Personality("alluring", #Miss Fortune and Samira from League of Legends style personality
        common_likes = ["the colour red", "the colour black", "high heels", "dresses", "makeup", "jazz", "pop music", "flirting", "the weekend", "Fridays", "lingerie"],
        common_sexy_likes = ["vaginal sex", "being submissive", "taking control", "threesomes", "public sex", "doggy style sex", "missionary style sex", "open relationships", "polyamory", "skimpy outfits", "not wearing underwear"],
        common_dislikes = ["work uniforms", "sports", "Mondays", "research work", "supply work", "the colour brown", "the colour orange", "hiking", "yoga"],
        common_sexy_dislikes = ["creampies", "anal creampies", "being fingered", "giving handjobs", "incest", "masturbating", "not wearing anything"],
        titles_function = alluring_titles, possessive_titles_function = alluring_possessive_titles, player_titles_function = alluring_player_titles,
        insta_chance = 0, dikdok_chance = 0)

    global bimboed_personality
    bimboed_personality = Personality("bimboed", #Cher Horowitz from Clueless or Elle Woods from Legally Blonde style personality
        common_likes = ["the colour pink", "pop music", "high heels", "dresses", "makeup", "flirting", "the weekend", "Fridays", "small talk", "yoga", "supply work"],
        common_sexy_likes = ["vaginal sex", "creampies", "being covered in cum", "cum facials", "giving blowjobs", "giving tit fucks", "doggy style sex", "public sex", "not wearing anything", "not wearing underwear", "open relationships", "polyamory", "threesomes", "skimpy outfits"],
        common_dislikes = ["the colour black", "research work", "hiking", "classical music", "jazz", "boots", "work uniforms", "Mondays", "conservative outfits"],
        common_sexy_dislikes = ["missionary style sex", "being fingered", "lingerie", "kissing", "anal sex", "anal creampies", "taking control"] ,
        titles_function = bimboed_titles, possessive_titles_function = bimboed_possessive_titles, player_titles_function = bimboed_player_titles,
        insta_chance = 0, dikdok_chance = 0)

    # Likes: Fertility symbols (white/green), traditional roles (conservative outfits), and nature-focused activities (hiking, yoga).
    # Sexy Likes: Procreative acts (creampies, vaginal sex), romantic intimacy (kissing), and flexible orientation (likes men/women).
    # Dislikes: Aggressive elements (red/black, heavy metal), commercialism (marketing), and casual interaction (small talk).
    # Sexy Dislikes: Non-reproductive acts (anal, threesomes), exhibitionism (public sex), and dominance (taking control).
    global breeder_personality
    breeder_personality = Personality("breeder", # Hitomi Takami from Ane Haramix or Momoko Kuzuryu from Sumomomo, Momomo: The Strongest Bride on Earth
        common_likes = ["the colour white", "the colour green", "conservative outfits", "dresses", "classical music", "research work", "Fridays", "the weekend", "hiking", "yoga"],
        common_sexy_likes = ["vaginal sex", "missionary style sex", "creampies", "being submissive", "kissing", "lingerie", "likes men", "likes women", "open relationships"],
        common_dislikes = ["the colour red", "the colour black", "heavy metal music", "punk music", "sports", "supply work", "marketing work", "Mondays", "small talk"],
        common_sexy_dislikes = ["public sex", "flashing", "not wearing anything", "not wearing underwear", "skimpy outfits", "skimpy uniforms", "threesomes", "anal sex", "anal creampies", "doggy style sex", "taking control"],
        titles_function = breeder_titles, possessive_titles_function = breeder_possessive_titles, player_titles_function = breeder_player_titles,
        insta_chance = 0, dikdok_chance = 0)

    # Likes: Creative colors (purple, red/blue), immersive work (research), and weekend freedom (Fridays, weekend).
    # Sexy Likes: Roleplay-friendly intimacy (lingerie, missionary), inclusive relationships (polyamory), and fertility play (creampies).
    # Dislikes: Dull colors (brown/orange), routine tasks (supply work), and athleticism (sports).
    # Sexy Dislikes: Unscripted exhibitionism (public sex), aggressive acts (anal, taking control), and lazy attire (not wearing anything).
    global cosplay_personality
    cosplay_personality = Personality("cosplay", # Marin Kitagawa from My Dress-Up Darling or Lilysa Amano from 2.5 Dimensional Seduction style personality
        common_likes = ["the colour black", "the colour purple", "the colour red", "the colour blue", "hiking", "research work", "Fridays", "the weekend", "work uniforms", "classical music", "jazz"],
        common_sexy_likes = ["vaginal sex", "missionary style sex", "creampies", "being fingered", "lingerie", "likes men", "likes women", "open relationships", "polyamory", "threesomes"],
        common_dislikes = ["the colour brown", "the colour orange", "sports", "supply work", "marketing work", "Mondays", "small talk", "yoga", "conservative outfits"],
        common_sexy_dislikes = ["public sex", "flashing", "not wearing anything", "not wearing underwear", "skimpy outfits", "skimpy uniforms", "anal sex", "anal creampies", "doggy style sex", "taking control"] ,
        titles_function = cosplay_titles, possessive_titles_function = cosplay_possessive_titles, player_titles_function = cosplay_player_titles,
        insta_chance = 60, dikdok_chance = 30)

    #Likes: Focus on privacy/solitude (hiking, research work) and subtle aesthetics (white/blue, dresses)
    #Sexy Likes: Emphasize emotional intimacy (kissing, missionary) over physical exhibitionism
    #Dislikes: Reject chaos (heavy metal, sports) and forced social interaction (small talk)
    #Sexy Dislikes: Avoid anything violating private boundaries (public sex, flashing)
    global dandere_personality
    dandere_personality = Personality("dandere", #Shouko Komi from Komi Can't Communicate style personality
        common_likes = ["conservative outfits", "dresses", "classical music", "jazz", "research work", "the colour blue", "the colour white", "yoga", "hiking", "Fridays", "the weekend"],
        common_sexy_likes = ["being submissive", "kissing", "missionary style sex", "lingerie", "vaginal sex", "being fingered", "creampies"],
        common_dislikes = ["heavy metal music", "punk music", "small talk", "sports", "Mondays", "the colour red", "the colour orange", "marketing work", "supply work"],
        common_sexy_dislikes = ["public sex", "flashing", "not wearing anything", "not wearing underwear", "open relationships", "polyamory", "skimpy outfits", "skimpy uniforms", "threesomes"],
        titles_function = dandere_titles, possessive_titles_function = dandere_possessive_titles, player_titles_function = dandere_player_titles,
        insta_chance = 0, dikdok_chance = 0)

    # Likes: Vibrant colors (red/orange/yellow), social interaction (flirting, small talk), and flexible work (supply/marketing).
    # Sexy Likes: Sensual intimacy (kissing, lingerie), fertility-focused acts (creampies), and inclusive attraction (likes men/women).
    # Dislikes: Austerity (black/white, conservative outfits), rigid structure (research work), and aggressive aesthetics (boots, punk music).
    # Sexy Dislikes: Exhibitionism (public sex), dominance dynamics (taking control), and "fast food" sexuality (anal, threesomes).
    global foodie_personality
    foodie_personality = Personality("foodie", #Hannibal Lecter from Silence of the Lamb or Aziraphale from Good Omens style personality
        common_likes = ["the colour red", "the colour orange", "the colour yellow", "hiking", "yoga", "Fridays", "the weekend", "flirting", "small talk", "supply work", "marketing work"],
        common_sexy_likes = ["vaginal sex", "creampies", "being fingered", "kissing", "lingerie", "missionary style sex", "likes men", "likes women", "open relationships"],
        common_dislikes = ["the colour black", "the colour white", "research work", "work uniforms", "boots", "heavy metal music", "punk music", "Mondays", "conservative outfits"],
        common_sexy_dislikes = ["public sex", "flashing", "not wearing anything", "skimpy uniforms", "threesomes", "anal sex", "anal creampies", "doggy style sex", "taking control"],
        titles_function = foodie_titles, possessive_titles_function = foodie_possessive_titles, player_titles_function = foodie_player_titles,
        insta_chance = 0, dikdok_chance = 0)


    global gothic_personality
    gothic_personality = Personality("gothic", #Wednesday Addams from Addams Family or Lydia Deetz from Beetlejuice style personality
        common_likes = ["the colour black", "the colour purple", "classical music", "research work", "hiking", "the weekend", "boots", "conservative outfits", "work uniforms", "Fridays"],
        common_sexy_likes = ["vaginal sex", "missionary style sex", "being submissive", "creampies", "kissing", "lingerie", "likes men", "likes women"],
        common_dislikes = ["pop music", "sports", "Mondays", "supply work", "marketing work", "the colour orange", "the colour yellow", "small talk", "yoga"],
        common_sexy_dislikes = ["public sex", "flashing", "not wearing anything", "open relationships", "polyamory", "skimpy outfits", "skimpy uniforms", "threesomes", "anal sex", "anal creampies", "doggy style sex"] ,
        titles_function = gothic_titles, possessive_titles_function = gothic_possessive_titles, player_titles_function = gothic_player_titles,
        insta_chance = 0, dikdok_chance = 0)

    #Likes: Romantic/wholesome activities (yoga, hiking), soft aesthetics (pink/white, dresses), and harmonious work (research).
    #Sexy Likes: Gentle intimacy (kissing, missionary), emotional connection (likes men/women), and romantic attire (lingerie).
    #Dislikes: Chaos (heavy metal, sports), superficiality (small talk), and harsh tones (black/orange).
    #Sexy Dislikes: Non-committal/exhibitionist acts (public sex, threesomes) and aggressive dynamics (taking control, anal sex).
    global goudere_personality
    goudere_personality = Personality("goudere", #Albedo from Overlord style personality
        common_likes = ["classical music", "dresses", "flirting", "Fridays", "hiking", "research work", "skirts", "the colour pink", "the colour red", "the colour white", "yoga", "the weekend", "work uniforms"],  
        common_sexy_likes = ["kissing", "missionary style sex", "lingerie", "vaginal sex", "creampies", "being fingered", "likes men", "likes women"],
        common_dislikes = ["heavy metal music", "punk music", "sports", "Mondays", "marketing work", "supply work", "small talk", "the colour orange", "the colour black"],
        common_sexy_dislikes = ["public sex", "flashing", "not wearing anything", "open relationships", "polyamory", "skimpy outfits", "skimpy uniforms", "threesomes", "anal sex", "anal creampies", "doggy style sex", "taking control"]  ,
        titles_function = goudere_titles, possessive_titles_function = goudere_possessive_titles, player_titles_function = goudere_player_titles,
        insta_chance = 20, dikdok_chance = 0)

    # Likes: Professionalism (work uniforms, conservative outfits) Logic-driven activities (research/production work) Neutral colors (black, white, blue) Structured downtime (Fridays, weekend hiking)
    # Dislikes: Chaos/disruption (punk music, sports, Mondays) Superficiality (small talk, marketing) Emotional displays (yoga, red/orange colors)
    # Sexy Likes: Controlled intimacy (missionary, lingerie) Private bonding (creampies, vaginal sex) Discreet preferences (likes men/women without fanfare)
    # Sexy Dislikes: Loss of dignity (public sex, flashing) Unstructured dynamics (open relationships, threesomes) Aggressive acts (anal sex, taking control)
    global kuudere_personality
    kuudere_personality = Personality("kuudere", #Reina Aharen from Aharen-San style personality
        common_likes = ["conservative outfits", "classical music", "research work", "production work", "the colour black", "the colour white", "the colour blue", "Fridays", "the weekend", "work uniforms", "working", "hiking"],
        common_sexy_likes = ["missionary style sex", "lingerie", "vaginal sex", "creampies", "being fingered", "likes men", "likes women"],
        common_dislikes = ["heavy metal music", "punk music", "small talk", "sports", "marketing work", "supply work", "the colour red", "the colour orange", "Mondays", "yoga"],
        common_sexy_dislikes = ["public sex", "flashing", "not wearing anything", "not wearing underwear", "open relationships", "polyamory", "skimpy outfits", "skimpy uniforms", "threesomes", "anal sex", "anal creampies", "doggy style sex", "taking control"],
        titles_function = kuudere_titles, possessive_titles_function = kuudere_possessive_titles, player_titles_function = kuudere_player_titles,
        insta_chance = 0, dikdok_chance = 0)

    # Likes: Glamour (high heels, makeup), social buzz (marketing work, flirting), and flexibility (yoga, supply work).
    # Sexy Likes: Performative acts (cum facials, doggy style), exhibitionism (public sex), and professional attire (skimpy uniforms).
    # Dislikes: Blandness (black, conservative outfits), isolation (hiking), and rigid schedules (Mondays, research work).
    # Sexy Dislikes: Intimate bonding (missionary, kissing), subtlety (lingerie), and passive roles (being submissive).
    global pornstar_personality
    pornstar_personality = Personality("pornstar", # Dillion Harper, Alexis Texas, Megan Rain, Riley Reid, Dani Daniels, Naomi Woods
        common_likes = ["the colour red", "high heels", "makeup", "pop music", "flirting", "Fridays", "the weekend", "supply work", "marketing work", "small talk", "yoga"],
        common_sexy_likes = ["vaginal sex", "anal sex", "public sex", "threesomes", "open relationships", "polyamory", "not wearing anything", "not wearing underwear", "skimpy outfits", "skimpy uniforms", "giving blowjobs", "cum facials", "being covered in cum", "doggy style sex", "taking control"],
        common_dislikes = ["the colour black", "research work", "hiking", "classical music", "jazz", "boots", "work uniforms", "Mondays", "conservative outfits"],
        common_sexy_dislikes = ["missionary style sex", "being fingered", "lingerie", "kissing", "creampies", "being submissive"],
        titles_function = pornstar_titles, possessive_titles_function = pornstar_possessive_titles, player_titles_function = pornstar_player_titles,
        insta_chance = 60, dikdok_chance = 30)

    # Likes: Attention-grabbing aesthetics (red, high heels), social jobs (marketing), and weekend partying (Fridays).
    # Sexy Likes: Exhibitionism (public sex), fluid relationships (polyamory), and cum-focused acts (facials, covered in cum).
    # Dislikes: Reserved styles (black, conservative outfits), solitary activities (hiking), and formal work (research).
    # Sexy Dislikes: Vanilla intimacy (missionary, kissing), emotional bonding (creampies), and dominance (taking control).
    global slutty_personality
    slutty_personality = Personality("slutty", # Panty Anarchy from Panty & Stocking with Garterbelt or Naruko Yokoshima from Seitokai Yakuindomo style personality
        common_likes = ["the colour red", "high heels", "dresses", "makeup", "pop music", "flirting", "Fridays", "the weekend", "supply work", "marketing work", "small talk"],
        common_sexy_likes = ["vaginal sex", "anal sex", "public sex", "threesomes", "open relationships", "polyamory", "not wearing anything", "not wearing underwear", "skimpy outfits", "skimpy uniforms", "giving blowjobs", "cum facials", "being covered in cum"],
        common_dislikes = ["the colour black", "research work", "hiking", "classical music", "jazz", "boots", "work uniforms", "Mondays", "conservative outfits"],
        common_sexy_dislikes = ["missionary style sex", "being fingered", "lingerie", "kissing", "creampies", "taking control"],
        titles_function = slutty_titles, possessive_titles_function = slutty_possessive_titles, player_titles_function = slutty_player_titles,
        insta_chance = 60, dikdok_chance = 30)

    # Likes: Athleticism (sports, hiking), practical style (boots, work uniforms), and gritty aesthetics (heavy metal, punk).
    # Sexy Likes: Dominant roles (taking control), high-energy acts (public sex, anal), and sporty-sexy attire (skimpy uniforms).
    # Dislikes: Femininity (dresses, makeup), quiet hobbies (yoga, jazz), and emotional chatter (small talk).
    # Sexy Dislikes: Soft intimacy (missionary, kissing), romantic attachment (open relationships), and delicate attire (lingerie).
    global tomboy_personality
    tomboy_personality = Personality("tomboy", #Juno MacGuff from Juno or Wendy Corduroy from Gravity Falls style personality
        common_likes = ["sports", "boots", "pants", "the colour blue", "hiking", "supply work", "work uniforms", "heavy metal music", "punk music", "Mondays", "Fridays", "the weekend"],
        common_sexy_likes = ["taking control", "doggy style sex", "anal sex", "skimpy uniforms", "threesomes", "big dicks", "giving tit fucks", "public sex"],
        common_dislikes = ["dresses", "skirts", "makeup", "the colour pink", "yoga", "classical music", "jazz", "research work", "small talk"],
        common_sexy_dislikes = ["being submissive", "missionary style sex", "lingerie", "creampies", "kissing", "flashing", "open relationships", "polyamory"] ,
        titles_function = tomboy_titles, possessive_titles_function = tomboy_possessive_titles, player_titles_function = tomboy_player_titles,
        insta_chance = 0, dikdok_chance = 0)

    # Likes: Aggressive/competitive activities (sports, heavy metal) Bold aesthetics (red/black, boots/heels) Workaholic tendencies (Mondays, supply work)
    # Dislikes: "Weak" or soft elements (yoga, pop music, pink/white) Quiet introspection (research work, hiking)
    # Sexy Likes:  Dominant role (taking control)  "Edgy" acts (anal sex, threesomes) Provocative displays (skimpy uniforms, tit fucks)
    # Sexy Dislikes: Vulnerability (being submissive, creampies) Traditional intimacy (missionary, lingerie) Emotional exposure (public sex, open relationships)
    global tsundere_personality
    tsundere_personality = Personality("tsundere", #Asuka Langley from Neon Genesis Evangelion style personality
        common_likes = ["sports", "heavy metal music", "punk music", "work uniforms", "the colour red", "the colour black", "boots", "Mondays", "supply work", "working", "high heels"],
        common_sexy_likes = ["taking control", "doggy style sex", "anal sex", "skimpy uniforms", "threesomes", "giving tit fucks", "big dicks"],
        common_dislikes = ["pop music", "yoga", "small talk", "research work", "the colour pink", "the colour white", "dresses", "hiking", "the weekend"],
        common_sexy_dislikes = ["being submissive", "creampies", "missionary style sex", "public sex", "flashing", "not wearing underwear", "open relationships", "polyamory", "lingerie"] ,
        titles_function = tsundere_titles, possessive_titles_function = tsundere_possessive_titles, player_titles_function = tsundere_player_titles,
        insta_chance = 40, dikdok_chance = 30)

    # Likes: Earthy/aggressive aesthetics (brown/green, boots) Raw physicality (sports, hiking, survival work) Chaotic rhythms (punk/heavy metal music)
    # Dislikes: Delicate femininity (pink/white, dresses) Restraint (work uniforms, classical music Introspection (research, yoga)
    # Sexy Likes: Primal acts (public sex, doggy style, anal) Messy/feral intimacy (covered in cum, no clothing) Unrestricted dynamics (open relationships, taking control)
    # Sexy Dislikes Vanilla romance (missionary, kissing) Artificial allure (lingerie, conservative outfits Solo acts (masturbating, handjobs)
    global wilder_personality
    wilder_personality = Personality("wilder", #Stephanie style personality
        common_likes = ["the colour brown", "the colour green", "hiking", "boots", "heavy metal music", "punk music", "survival work", "Mondays", "Fridays", "the weekend", "sports"],
        common_sexy_likes = ["public sex", "doggy style sex", "creampies", "anal sex", "being covered in cum", "not wearing anything", "open relationships", "threesomes", "taking control", "anal creampies"],
        common_dislikes = ["the colour pink", "the colour white", "classical music", "research work", "makeup", "dresses", "skirts", "small talk", "yoga", "work uniforms"],
        common_sexy_dislikes = ["missionary style sex", "lingerie", "kissing", "being submissive", "conservative outfits", "flashing", "polyamory", "masturbating", "giving handjobs"],
        titles_function = wilder_titles, possessive_titles_function = wilder_possessive_titles, player_titles_function = wilder_player_titles,
        insta_chance = 40, dikdok_chance = 30)

    # Likes: Obsessive focus (research work, working) Contrasting colors (red for blood, white/black for purity/darkness) Traditional markers (classical music, boots/heels)
    # Dislikes: Distractions from fixation (sports, small talk) Chaotic elements (punk music, orange/yellow)
    # Sexy Likes: Possessive intimacy (creampies, drinking cum) False normalcy (missionary, lingerie) Network of control (open relationships to monitor rivals)
    # Sexy Dislikes: Loss of exclusivity (threesomes, anal sex) Public exposure (public sex, flashing) Partner dominance (taking control)
    global yandere_personality
    yandere_personality = Personality("yandere", #Yuno Gasai from Future Diary style personality
        common_likes = ["the colour red", "the colour white", "the colour black", "research work", "Fridays", "the weekend", "classical music", "working", "boots", "high heels"],
        common_sexy_likes = ["being submissive", "creampies", "vaginal sex", "missionary style sex", "likes men", "likes women", "lingerie", "kissing", "drinking cum", "open relationships", "polyamory"],
        common_dislikes = ["heavy metal music", "punk music", "sports", "supply work", "marketing work", "the colour orange", "the colour yellow", "Mondays", "small talk", "yoga"],
        common_sexy_dislikes = ["public sex", "flashing", "not wearing anything", "skimpy outfits", "skimpy uniforms", "threesomes", "anal sex", "anal creampies", "taking control", "doggy style sex"] ,
        titles_function = yandere_titles, possessive_titles_function = yandere_possessive_titles, player_titles_function = yandere_player_titles,
        insta_chance = 40, dikdok_chance = 30)


#########################################################################################################################
### Story Characters
    #Albedo (Overlord) Personality Traits:
    # Likes: Monochromatic elegance (white/black) Intellectual rigor (research work) Loyalty-coded attire (work/conservative uniforms)
    # Dislikes: Gaudy elements (red/orange, pop music) Mundane interaction (small talk, marketing) Chaotic exertion (sports, yoga)
    # Sexy Likes: Service-focused submission (being submissive) Absolute devotion markers (creampies, drinking cum) Calculated promiscuity (polyamory for Ainz's benefit)
    # Sexy Dislikes: Undignified exposure (public sex, skimpy outfits) Casual encounters (threesomes, anal sex) Partner dominance (taking control contradicts her role)
    # Captures Albedo’s obsessive loyalty to Ainz—channeling sexual energy into acts that "serve" him while rejecting anything that undermines her devotion or dignity.
    # global albedo_personality
    # albedo_personality = Personality("albedo", #Albedo (Overlord)
        # common_likes = ["the colour white", "the colour black", "classical music", "research work", "work uniforms", "conservative outfits", "Fridays", "the weekend", "hiking", "boots"],
        # common_sexy_likes = ["vaginal sex", "missionary style sex", "creampies", "being submissive", "likes men", "open relationships", "polyamory", "drinking cum", "anal creampies"],
        # common_dislikes = ["the colour red", "the colour orange", "pop music", "small talk", "sports", "supply work", "marketing work", "Mondays", "yoga"],
        # common_sexy_dislikes = ["public sex", "flashing", "not wearing anything", "skimpy outfits", "skimpy uniforms", "threesomes", "anal sex", "doggy style sex", "taking control"],
        # titles_function = albedo_titles, possessive_titles_function = albedo_possessive_titles, player_titles_function = albedo_player_titles,
        # insta_chance = 0, dikdok_chance = 0)


#foodie_personality,
    list_of_personalities.extend((
        dandere_personality,
        goudere_personality,
        kuudere_personality,
        tsundere_personality,
        yandere_personality,
        alluring_personality,
        gothic_personality,
        foodie_personality,
        bimboed_personality,
        tomboy_personality,
        cosplay_personality,
        slutty_personality,
        pornstar_personality,
        breeder_personality,
        wilder_personality,
    ))
