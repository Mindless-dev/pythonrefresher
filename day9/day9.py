# # dictionaries
# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.", }

# print(programming_dictionary)

# # adding to dictionary.
# programming_dictionary["Loop"] = "The action of doing something over and over again."

# print(programming_dictionary)


# # creating an empty dictionary / same as a javascript object

# empty_dictionary = {}

# # you can wipe a dictonary by setting the dictionary to empty.

# # edit dictionary:


# programming_dictionary["Bug"] = "A moth in your computer"

# # loop through a dictonary:

# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])


# ### challenge 1 ####

# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# # TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}


# # TODO-2: Write your code below to add the grades to student_grades.👇
# for student in student_scores:
#     if student_scores[student] > 90:
#         student_grades[student] = "outstanding"
#     elif student_scores[student] > 80 and student_scores[student] <= 90:
#         student_grades[student] = "Exceeds Expectations"
#     elif student_scores[student] > 70 and student_scores[student] <= 80:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"


# # 🚨 Don't change the code below 👇
# print(student_grades)


# #nesting in dictionaries

# travel_log = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#     "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
# }

# # nesting dictionaries in a list

# travel_log = [
#     {"country": "france",
#      "cities_visited": [ "Paris", "Lille", "Dijon"],
#      "total_visits": 12},
#     {"country": "france", "cities_visited": [
#         "Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
# ]


travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]
# 🚨 Do NOT change the code above

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇


def add_new_country(country, number_visits, cities):
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = number_visits
    new_country["cities"] = cities
    travel_log.append(new)


# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
