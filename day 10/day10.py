# # functions with output

# def format_name(f_name, l_name):

#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()

#     return f"{formated_f_name} {formated_l_name}"


# formated_string = format_name("kenny", "HOLMEN")

# print(formated_string)


# ###challenge 1 ####

# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False


# def days_in_month(year, month):
#     if month > 12 or month < 1:
#         return "invalid month"
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap(year) and month == 2:
#         return 29

#     return month_days[month-1]


# # 🚨 Do NOT change any of the code below
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

# why return at all?


# docstrings documentation of code first line of decleration after the ":" use """ take a first and last name and format it """ to document populates the documentaion like the
