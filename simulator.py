from random import randint, choice

population = {}
marriage_database = {}
birth_database = {}
list_of_diseases = {}
people_who_died = []

types_of_birth = ["natural", "c-section"]
types_of_gender = ["male", "female", "non-binary"]
types_of_shelter = ["apartment", "house", "homeless"]
types_life_style = ["low", "medium", "high"]
types_of_education = ["elementary school", "middle school", "high school", "college", "post-college"]
months = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

avg_age = 85
attend_college_rate = 50
drop_out_of_high_school = 10
drop_out_of_college = 20
get_married = 60
get_divorced = 40
get_job_rate = 80
death_rate = {"baby": 5, "child": 10, "teen": 15, "adult": 30, "elderly": 60}
days_per_year = 365
meals_per_day = 3
starting_year = 2016
current_year = 2016

current_month = "January"
current_day = 1

pop_id = 0
starting_population = 100


human_template = {
    "first_name": "",
    "last_name": "",
    "current_age": 0,
    "birthday": {"month": 0, "day": 0, "year": 0000},
    "birth_type": "",
    # "relationship_length": 0,
    # "relationship_status": False,
    # "married_to": "",
    # "has_job": False,
    # "years_at_job": 0,
    # "job_title": "",
    # "going_to_school": False,
    # "level_of_education": "",
    # "disease_status": {},
    # "gender": "",
    # "account_balance": {"checking": 0, "savings": 0},
    # "life_style": "",
    # "life_status": "",
    # "shelter_status": "",
    # "health_status": {"hunger": 0, "tired": 0},
    # "obligations": {},
    # "life_goals": [],
    "is_alive": True
}


def give_fist_name(number_for_human):
    # first_name = "human %d" % number_for_human
    return "human" + str(number_for_human)


def give_last_name(number_for_human):
    last_name = "Person %d" % number_for_human
    return last_name


def give_birth_type():
    birth_type = types_of_birth[randint(0, len(types_of_birth)-1)]
    return birth_type


def give_birthday(age):
    year = current_year - age
    month = choice(list(months.keys()))
    day = randint(1, months[month])
    return {"month": month, "day": day, "year": year}


def give_age():
    age = randint(1, avg_age)
    return age


def give_gender():
    gender = types_of_gender[randint(0, len(types_of_gender)-1)]
    return gender


def give_school_status():
    schooling = types_of_education[randint(0, len(types_of_education)-1)]
    return schooling


def give_job_status():
    return


def get_obligations(human):
    life_goals = []

    if human["level_of_education"] == "elementary school":
        life_goals.append("Attended up to Elementary")
    elif human["level_of_education"] == "middle school":
        life_goals.append("Attended up to Middle School")
    elif human["level_of_education"] == "highschool":
        life_goals.append("Attended up to Highschool")
    elif human["level_of_education"] == "college":
        life_goals.append("Attended up to College")
    elif human["level_of_education"] == "post-college":
        life_goals.append("Attended up to Post-College")
    return life_goals


def get_life_goals(human):
    life_goals = []

    if human["level_of_education"] == "elementary school":
        life_goals.append("Attended up to Elementary")
    elif human["level_of_education"] == "middle school":
        life_goals.append("Attended up to Middle School")
    elif human["level_of_education"] == "highschool":
        life_goals.append("Attended up to Highschool")
    elif human["level_of_education"] == "college":
        life_goals.append("Attended up to College")
    elif human["level_of_education"] == "post-college":
        life_goals.append("Attended up to Post-College")
    return life_goals


def generate_human(person):
    first_name = give_fist_name(person)
    last_name = give_last_name(person)
    birth_type = give_birth_type()
    current_age = give_age()
    birthday = give_birthday(human_template["current_age"])
    # temp_human["gender"] = give_gender()
    # temp_human["level_of_education"] = give_school_status()
    # temp_human["life_goals"] = get_life_goals(temp_human)
    print("human will be:")
    return {"first_name": first_name, "last_name": last_name, "birth_type": birth_type, "current_age": current_age, "birthday": birthday }


def create_population():
    for person in range(starting_population):
        print(person)
        population[person] = generate_human(person)
        print(population[person])
        print("current population: ")
        print(population)
        print("--------")
    print(population)
    return


def get_job():
    job = ""
    return job


def check_age(person):
    age = person["current_age"]

    if age < 3:
        return "baby"
    elif age < 13:
        return "child"
    elif age < 18:
        return "teen"
    elif age < 60:
        return "adult"
    else:
        return "elderly"


def check_living_status():
    return


def check_can_have_job(age):
    if age > 16:
        get_job()


def temp():
    return


def check_month_change():
    if current_day > months[current_month]:
        next_month()


def next_month():
    global current_month
    global current_year
    global current_day

    month = current_month

    if current_month == "January":
        current_month = "February"
    elif current_month == "February":
        current_month = "March"
    elif current_month == "March":
        current_month = "April"
    elif current_month == "April":
        current_month = "May"
    elif current_month == "May":
        current_month = "June"
    elif current_month == "June":
        current_month = "July"
    elif current_month == "July":
        current_month = "August"
    elif current_month == "August":
        current_month = "September"
    elif current_month == "September":
        current_month = "October"
    elif current_month == "October":
        current_month = "November"
    elif current_month == "November":
        current_month = "December"
    elif current_month == "December":
        current_month = "January"
        current_year += 1
    reset_day_on_month_change(month)


def reset_day_on_month_change(month):
    global current_day

    if month != current_month:
        current_day = 1
    return


def test_run_days():
    while current_year == 2016:
        print("Date: %s %d, %d" % (current_month, current_day, current_year))
        move_day()
        check_month_change()
    return


def move_day():
    global current_day
    current_day += 1


def person_died(person):
    information = population[person]

    print("Death Day: %s %d, %d" % (current_month, current_day, current_year))
    print("%s %s has DIED" % (information["first_name"], information["last_name"]))
    del population[person]
    return


def check_if_died(age):
    chance_of_death = randint(0, 10000)
    print("Chance of death: %d" % chance_of_death)
    print("Death Rate: %d" % death_rate[age])
    if death_rate[age] > chance_of_death:
        return True
    return False


def check_deaths():
    global people_who_died
    if len(people_who_died) > 0:
        for person in people_who_died:
            person_died(person)
        people_who_died = []
    else:
        print("No one died")
    return


def check_personal_events(person):
    global people_who_died
    print("Checking if they died")
    if check_if_died(check_age(population[person])):
        print("A person was added to death list")
        population[person]["is_alive"] = False
        people_who_died.append(person)
    return


def progress_day():
    for person in population:
        print("Checking Personal Events:")
        check_personal_events(person)
    move_day()
    check_month_change()


create_population()


while len(population) > 0:
    print("Current Population: %d" % len(population))
    print("Running progress day")
    progress_day()
    print("Checking if people died")
    check_deaths()

print(people_who_died)

# test_run_days()