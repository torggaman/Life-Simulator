from random import randint, choice
import json
import education
import job

population = {}
parents_needed = []
marriage_database = {}
birth_database = {}
list_of_diseases = {}
people_who_died = []
population_record = {}

types_of_birth = ["natural", "c-section"]
types_of_sex = ["male", "female"]
types_of_sexual_orientation = ["straight", "bi", "gay"]
types_of_shelter_status = [True, False]
types_of_housing = ["home", "apartment", "condo", "homeless"]
types_life_style = ["low", "medium", "high"]
types_of_relationship = ["single", "married", "dating", "divorced"]
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
get_job_rate = 96
death_rate = {"baby": 10, "child": 15, "teen": 20, "adult": 40, "elderly": 80}
days_per_year = 365
meals_per_day = 3
starting_year = 2016
current_year = 2016

current_month = "January"
current_day = 1

pop_id = 0
starting_population = 10


human_template = {
    "first_name": "",
    "last_name": "",
    "current_age": 0,
    "age_entered_simulator": 0,
    "birthday": {"month": "January", "day": 0, "year": 0000},
    "birth_type": "",
    "days_alive_in_simulator": 0,
    "relationship_length": 0,
    "relationship_status": False,
    "married_to": "",
    "has_job": False,
    "days_at_job": 0,
    "job_level": "",
    "job_title": "",
    "job_work_quality": "",
    "days_since_promotion": 0,
    "has_spouse": {},
    "going_to_school": False,
    "level_of_education": "",
    "disease_status": {},
    "sex": "",
    "account_balance": {"checking": 0, "savings": 0},
    "life_style": "",
    "life_status": "",
    "shelter_status": "",
    "health_status": {"hunger": 0, "tired": 0},
    "obligations": {},
    "addictions": [],
    "life_goals": [],
    "is_alive": True
}


def give_fist_name(number_for_human):
    # first_name = "human %d" % number_for_human
    return "human" + str(number_for_human)


def give_last_name(number_for_human):
    last_name = "Person" + str(number_for_human)
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


def give_parent_age(childs_age):
    age = randint(18, avg_age)
    return age + childs_age


def give_sex():
    sex = choice(types_of_sex)
    return sex


def give_housing(age):
    if age > 16:
        return choice(types_of_housing)
    return "none"


# def give_parent_housing(child):
#     if population[child][""]
#         return choice(types_of_housing)


def give_job_status():
    return


def give_relationship_status(age):
    if age > 18:
        return choice(types_of_relationship)
    return "single"


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


def generate_parents(child, person):
    first_name = give_fist_name(person)
    last_name = give_last_name(person)
    birth_type = give_birth_type()
    current_age = give_parent_age(population[child]["current_age"])
    birthday = give_birthday(current_age)
    sex = give_sex()
    level_of_education = education.give_level_of_education(current_age)
    # temp_human["life_goals"] = get_life_goals(temp_human)
    has_job = job.give_has_job(current_age)
    days_at_job = job.give_days_at_job(current_age, has_job)
    job_level = job.give_job_level(has_job, days_at_job)
    job_title = job.give_job_title(has_job, days_at_job)
    job_health_status = job.give_job_health_status(has_job)
    has_child = True
    child_id = [child]
    housing = give_housing(current_age)
    relationship_status = give_relationship_status(current_age)

    return {
        "first_name": first_name,
        "last_name": last_name,
        "birth_type": birth_type,
        "sex": sex,
        "current_age": current_age,
        "age_entered_simulator": current_age,
        "birthday": birthday,
        "days_alive_in_simulator": 0,
        "has_job": has_job,
        "days_at_job": days_at_job,
        "job_level": job_level,
        "job_title": job_title,
        "job_health_status": job_health_status,
        "housing": housing,
        "level_of_education": level_of_education,
        "has_child": has_child,
        "child_id": child_id,
        "parent": [],
        "relationship_status": relationship_status
    }


def generate_human(person):
    first_name = give_fist_name(person)
    last_name = give_last_name(person)
    birth_type = give_birth_type()
    current_age = give_age()
    birthday = give_birthday(current_age)
    sex = give_sex()
    level_of_education = education.give_level_of_education(current_age)
    # temp_human["life_goals"] = get_life_goals(temp_human)
    has_job = job.give_has_job(current_age)
    days_at_job = job.give_days_at_job(current_age, has_job)
    job_level = job.give_job_level(has_job, days_at_job)
    job_title = job.give_job_title(has_job, days_at_job)
    job_health_status = job.give_job_health_status(has_job)
    has_child = False
    child_id = []
    relationship_status = give_relationship_status(current_age)
    housing = give_housing(current_age)

    return {
        "first_name": first_name,
        "last_name": last_name,
        "birth_type": birth_type,
        "sex": sex,
        "current_age": current_age,
        "age_entered_simulator": current_age,
        "birthday": birthday,
        "days_alive_in_simulator": 0,
        "has_job": has_job,
        "days_at_job": days_at_job,
        "job_level": job_level,
        "job_title": job_title,
        "job_health_status": job_health_status,
        "housing": housing,
        "level_of_education": level_of_education,
        "has_child": has_child,
        "child_id": child_id,
        "parent": [],
        "relationship_status": relationship_status
    }


def create_population():
    for person in range(starting_population):
        population[person] = generate_human(person)
        if population[person]["current_age"] < 16:
            parents_needed.append(person)
    for person in parents_needed:
        population[str(person) + "a"] = generate_parents(person, str(person) + "a")
        population[str(person) + "b"] = generate_parents(person, str(person) + "b")
        population[person]["parent"].append(str(person) + "a")
        population[person]["parent"].append(str(person) + "b")
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


def check_living_status(human):
    return human["living_status"]


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


def check_birthday(day, month, person):
    if current_day == day:
        if current_month == month:
            population[person]["current_age"] += 1


def move_day():
    global current_day
    current_day += 1


def person_died(person):
    population_record[person] = population[person]
    population_record[person]["died_on"] = "%s %i, %i" % (current_month, current_day, current_year)
    del population[person]
    return


def check_if_died(age):
    chance_of_death = randint(0, 100000)
    if death_rate[age] > chance_of_death:
        return True
    return False


def check_deaths():
    global people_who_died
    if len(people_who_died) > 0:
        for person in people_who_died:
            person_died(person)
        people_who_died = []
    return


def check_personal_events(person):
    global people_who_died
    if check_if_died(check_age(population[person])):
        population[person]["is_alive"] = False
        people_who_died.append(person)
        return
    check_birthday(population[person]["birthday"]["day"], population[person]["birthday"]["month"], person)
    # check_job
    # check_health
    # check_needs
    # check_
    return


def progress_day():
    for person in population:
        check_personal_events(person)
        population[person]["days_alive_in_simulator"] += 1
        if population[person]["has_job"]:
            population[person]["days_at_job"] += 1


create_population()


while len(population) > 0:
    progress_day()
    check_deaths()
    move_day()
    check_month_change()

with open("results.json", "w") as output_file:
    json.dump(population_record, output_file)

# print(people_who_died)

# test_run_days()