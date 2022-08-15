# # for loops

# fruits = ["apple", "peach", "pear"]

# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")

##################average height without sum or len ####################
# # 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])

# # 🚨 Don't change the code above 👆


# # Write your code below this row 👇
# combined_heights = 0
# no_heights = 0
# for heights in student_heights:
#     combined_heights += heights
#     no_heights += 1

# average = combined_heights/no_heights
# print(f"the average height is {round(average)}cm")


# # 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆

# # Write your code below this row 👇
# high_score = 0
# for score in student_scores:
#     if high_score < score:
#         high_score = score

# print(f"the highest score in the class is: {high_score}")

# # max function returns the highest number in an array


# for n in range(1, 11, 3):
#     print(n)
# total = 0
# for number in range(1, 101):
#     total += number
# print(total)


# # even number add
# total = 0
# for n in range(2, 101, 2):
#     total += n
# print(total)

# total2 = 0
# for number in range(1, 101):
#     if number % 2 == 0:
#         total2 += number
# print(total2)


# fizzbuzz

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
