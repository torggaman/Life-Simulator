from random import randint

population = {}
marriage_database = {}
birth_database = {}
list_of_diseases = {}

types_of_birth = ["natual", "c-section"]
types_of_gender = ["male", "female", "non-binary"]
types_of_shelter = ["apartment", "house", "homeless"]
types_life_style = ["low", "medium", "high"]
types_of_education = ["elementary school", "middle school", "high school", "college", "post-college"]

avg_age = 85
attend_college_rate = 50
drop_out_of_high_school = 10
drop_out_of_college = 20
get_married = 60
get_divorced = 40
get_job_rate = 80
days_per_year = 365
meals_per_day = 3
starting_population = 1
starting_year = 2016
current_year = 2016

current_month = ""
current_day = 0

pop_id = 0


human_template = {
    "first_name": "",
    "last_name": "",
    "current_age": 0,
    "birth_type": "",
    "relationship_length": 0,
    "relationship_status": "",
    "married_to": "",
    "has_job": False,
    "years_at_job": 0,
    "job_title": "",
    "going_to_school": False,
    "level_of_education": "",
    "disease_status": {},
    "gender": "",
    "account_balance": {"checking": 0, "savings": 0},
    "life_style": "",
    "life_status": "",
    "shelter_status": "",
    "health_status": {"hunger": 0, "tired": 0},
    "obligations": {},
    "life_goals": [],
    "is_alive": True}


def give_fist_name(number_for_human):
    first_name = "human %d" % number_for_human
    return first_name


def give_last_name(number_for_human):
    last_name = "Person %d" % number_for_human
    return last_name


def give_birth_type():
    birth_type = types_of_birth[randint(0, len(types_of_birth)-1)]
    return birth_type


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


def generate_human(number_of_human_created):
    temp_human = human_template
    temp_human["first_name"] = give_fist_name(number_of_human_created)
    temp_human["last_name"] = give_last_name(number_of_human_created)
    temp_human["birth_type"] = give_birth_type()
    temp_human["current_age"] = give_age()
    temp_human["gender"] = give_gender()
    temp_human["level_of_education"] = give_school_status()
    temp_human["life_goals"] = get_life_goals(temp_human)
    return temp_human


def create_population():
    for person in range(starting_population):
        population[person] = generate_human(person)
    print(population)


create_population()


def progress_day():
    global population
    population = {}


while len(population) > 0:
    progress_day()
