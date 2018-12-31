from random import choice, randint


types_of_job_levels = ["beginner", "intermediate", "expert"]
types_of_job = ["manual labor", "tech", "government", "city"]
types_of_job_health = ["low", "medium", "high"]


def give_has_job(age):
    if age > 15 and age < 65:
        return choice([True, False])
    return False


def give_days_at_job(age, has_job):
    if has_job:
        return randint(0, 365*(age-13))
    return 0


def give_job_level(has_job, days_at_job):
    if has_job:
        return choice(types_of_job_levels)
    return ""


def give_job_title(has_job, days_at_job):
    if has_job:
        return choice(types_of_job)
    return ""


def give_job_health_status(has_job):
    if has_job:
        return choice(types_of_job_health)
    return ""