def create_character(character_name, strength, intelligence, charisma):
    if not isinstance(character_name, str):
        return "The character name should be a string"
    elif len(character_name) == 0:
        return "The character should have a name"
    elif len(character_name) > 10:
        return "The character name is too long"
    elif character_name.count(" ") > 0:
        return "The character name should not contain spaces"

    stats = [strength, intelligence, charisma]
    
    if not all(isinstance(s, int) for s in stats):
        return "All stats should be integers"
    if any(s < 1 for s in stats):
        return "All stats should be no less than 1"
    if any(s > 4 for s in stats):
        return "All stats should be no more than 4"
    if sum(stats) != 7:
        return "The character should start with 7 points"

    return(
        f"{character_name}\n"
        f"STR {'●' * strength}{'○' * (10 - strength)}\n"
        f"INT {'●' * intelligence}{'○' * (10 - intelligence)}\n"
        f"CHA {'●' * charisma}{'○' * (10 - charisma)}"
    )

create_character('ren', 4, 2, 1)