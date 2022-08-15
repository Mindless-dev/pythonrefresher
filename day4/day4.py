import random


# import my_module
#modules in python
# random_integer = random.randint(1, 10000)
# print(random_integer)
# random_float = random.random()
# print(random_float)
# love_score = random.randint(1, 100)
# print(f"you're love score is {love_score}%")


# coin flipper
# heads_tails = random.randint(0, 1)

# if heads_tails == 1:
#     print("Heads")
# else:
#     print("Tails")


# states = ["delaware", "pennsylvania"]

# print(len(states))

# states[1] = "pencilvania"

# states.append("texas")
# print(states)

# states.extend(["wahsington", "utah"])
# print(states)


### banker roulette ###

# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇

# num_items = len(names)
# random_choice = random.randint(0, num_items-1)

# #alternativ løsning ##########

# # using random.choice(names)

# # print(names[person_paying_index])
# print(names[random_choice] + " is buying drinks")


# 🚨 Don't change the code below 👇
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

row = int(position[1])-1
col = int(position[0])-1

map[row][col] = "X"
# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
