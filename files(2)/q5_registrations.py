from pprint import pprint


def common_courses(registrations, target):
    result = {}
    target_courses = set(registrations[target])      # duplicates vanish here
    for student, courses in registrations.items():
        if student != target:                        # exclude the target
            common = target_courses & set(courses)   # set intersection
            if len(common) >= 2:                     # at least two courses
                result[student] = sorted(common)     # fixed alphabetical order
    return result


registrations = {
    "Arun": ["Python", "Java", "SQL", "Python"],
    "Bala": ["Python", "C", "SQL"],
    "Charan": ["Java", "Python", "SQL"],
    "Divya": ["Python", "Java"],
    "Ezhil": ["C", "Java", "Java"],
}

for target in ("Arun", "Divya"):
    print("Target:", target)
    pprint(common_courses(registrations, target))
    print()
