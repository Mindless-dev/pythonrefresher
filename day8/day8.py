# def greet(name):
#     print(f"Hello {name}")
#     print("How are you?")
#     print("isn't the weather nice today?")


# greet("Angela")

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")


# greet_with("John Doe", "Nowhere")


# # keyword params
# greet_with(name="John Doe", location="Nowhere")


# # Write your code below this line 👇 challenge 1 day 6

# from math import ceil


# def paint_calc(height, width, cover):
#     number_of_cans = ceil(height * width / cover)

#     print(f"You'll need {number_of_cans} cans of paint.")


# # Write your code above this line 👆
# # Define a function called paint_calc() so that the code below works.
# # 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)


# Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime == True:
        print("It's a prime number")
    else:
        print("It's not a prime number")


# Write your code above this line 👆
# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
