# data types
# string
# "some string"
# int
# 42
# float
# 23.2
# bool
# True

# last letter
print("hello"[-1])  # [4]

# type checks datatype


# str, int, float,  to convert something to a string

# coding challenge
# get a two digit number plus first digit with second

# number = input("give me a two digit number?")  # input is a string
# print(int(number[0]) + int(number[1]))

# math operators  + - * /
# ** opphøyning
# % modolo?
# Pemdas  paretehesis, exponents ,multiplaction division addition subtract

# () ** * /  + -


# BMI Calculator

##############################

# height = input("enter your height in meters: ")
# weight = input("enter your weight in kg: ")

# floated_height = float(height)
# floated_weight = float(weight)

# bmi = floated_weight / floated_height**2
# print(int(bmi))


############################


# rounding up  round function can be used for this round(8/3, 2) second argument how many decimals to have.
# floor division "//" answers with a int instead of float.
# += works the same.


# f strings same as `${}` in javascript

#####################################

# score = 0
# height = 1.8
# isWinning = True
# print(f"your score is {score}, your height is {height} you are winning  {isWinning}")

##########################################

# day 2 project your life in weeks until 90


#####################
#age = input("what is your current age?")


#years_left = 90 - int(age)
#months_left = years_left * 12
#weeks_left = years_left*52
#days_left = years_left*365
#######################

# print(
#   f"You have {days_left} days {weeks_left} weeks, {months_left} months left")


# tip calculator real final project
# tip percentages 10 12, 15

print("Welcome to the tip calculator.")
bill_total = float(input("what was the total bill? $"))
percentage_tip = int(input(
    "What percentage would you like to give? 10 ,12, or 15 ?"))
amount_of_people = int(input("How many people are splitting the bill? "))

total_per_person = round(
    bill_total * (1 + percentage_tip/100) / amount_of_people, 2)

final_amount = "{:.2f}".format(total_per_person)
print(f"Each person should pay: ${final_amount}")
