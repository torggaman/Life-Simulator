from random import choice, randint


types_of_education = ["none", "elementary school", "middle school", "high school", "college", "post-college"]


def give_level_of_education(age):
    if age < 4:
        return "none"
    elif age < 13:
        return types_of_education[randint(0,1)]
    elif age < 17:
        return types_of_education[randint(0,2)]
    elif age < 20:
        return types_of_education[randint(0,3)]
    return choice(types_of_education)