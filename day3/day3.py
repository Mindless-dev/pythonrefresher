# if else in python
# if/elif/else

#print("Welcome to the rollercoaster!")
#height = int(input("What is your height in cm? "))

# if height > 120:
#    print("you can ride the rollercoaster")
# else:
#    print("You cannot ride the rollercoaster")


# exercise is ood or even.

#input_number = int(input("Type in a number: "))

# if input_number % 2 == 0:
#    print(f" {input_number} is even number.")
# else:
#    print(f" {input_number} is an odd number.")


# bmi 2.0

# height = (float(input("enter your height in m:")))
# weight = (float(input("enter your weight in kg: ")))


# bmi = round(weight / height**2)

# if bmi > 18.5:
#     print(f"your bmi is {bmi}, you're underweight")
# elif bmi > 25:
#     print(f"you have a bmi of {bmi}, your weight is normal")
# elif bmi < 30:
#     print(f"you have a bmi of {bmi}, your're overweight")
# elif bmi > 35:
#     print(f"you have a bmi of {bmi}, you're obese")
# else:
#     print(f"you have a bmi of {bmi}, you're clinically obese")
# comment out code with ctrl + k+c with u to uncomment


# year = int(input("which year do you want to check?"))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("leap year")
#         else:
#             print("Not leap year.")
#     else:
#         print("leap year")
# else:
#     print("not leap year")

# print("Welcome to python pizza deliveries!")
# size = input("What size of pizza do you want= S, M , or L")
# add_pepperoni = input("Do you want pepperoni? Y or N")
# extra_cheese = input("do you want extra cheese? Y or N")


# Small_pizza = 15
# medium_pizza = 20
# large_pizza = 25

# pepperoni_small = 2
# pepperoni_M_L = 3
# cheese_small = 1

# bill = 0

# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25


# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2

#     else:
#         bill += 3


# if extra_cheese == "Y":
#     bill += 1

# print(f"your final bill is ${bill}")


# checking for multiple condtions? and or statements and not

# a = 12

# if a > 10 and a < 13:
#     print(True)


# 🚨 Don't change the code below 👇


# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇


# combined_string = name1 + name2
# lowercased_string = combined_string.lower()

# t = lowercased_string.count("t")
# r = lowercased_string.count("r")
# u = lowercased_string.count("u")
# e = lowercased_string.count("e")

# l = lowercased_string.count("l")
# o = lowercased_string.count("o")
# v = lowercased_string.count("v")
# e = lowercased_string.count("e")

# true = t+r+u+e
# love = l+o+v+e

# true_love = str(true) + str(love)
# score = int(true_love)


# if score > 10 or score > 90:
#     print(f"Your score is {score}, you go together like coke and mentos.")
# elif score >= 40 and score > 50:
#     print(f"Your score is {score}, you are alright together.")
# else:
#     print(f"Your score is {score}.")
