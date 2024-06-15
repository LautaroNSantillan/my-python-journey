# age = 23 ## var
# price = 19.95
# first_name = "Lautaro"  # snake_case
# is_online = False  # case Sensitive
# print("Hello World")  # single or double quotes for strings

#  input_name = input("Whats your name? ")
# print("Hello "+ input_name)

# birth_year = input("Birthyear? ")
# input_age = 2024 - int(birth_year)  # cannot subtract int - str
# print(input_age)

# int()
# float()
# bool()
# str()

# first = float(input("1st: "))
# second = input("2nd: ")

# sum = first + float(second)
# print("Sum: " + str(sum))

# my_string="My String"  # str are immutable
# print(my_string.replace("My", "Our"))  # new string : upper, lower, find, replace
# print("String" in my_string)  # boolean

# / = float
# // = int
# % (modulus) = remainder of division
# ** exponent

# x = 10
# x+=2


# COMPARISON OPERATORS
# <>,<=, >=, ==, !=

# LOGICAL OPERATORS
# and, or, not

# temp = 5
# if temp > 30:
#     print("hot")
#     print("press shift+tab to finish block of code")
# elif temp > 20:
#     print("20-30")
# elif temp > 10:
#     print("10-20")
# else:
#     print("cold")
# print("done")


# weight calculator
# # unit = input("Kg or Lbs ")
# if unit.upper() == "K":
#     print("your weight is " + str(float(input_weight) / .45) + "Lbs")
# elif unit.upper() == "L":
#     print("your weight is " + str(float(input_weight) * .45) + "Kg")
# else:
#     print("Error")


# LOOPS
# i = 1
# while i<=1_0:
#     print(i * "+")
#     i+=1

#LISTS
#numbers = ["1", "2", "3"]
# numbers[0]="0"
# print(numbers[0:-1])  # new list
# numbers.insert(0, -1)
# print(numbers)
# numbers.remove("2")
# print(numbers)
# print("1" in numbers)
# print(len(numbers))
# numbers.clear()
# print(numbers)

# FOR LOOPS (iterate over each item)
# for i in numbers:
#     print(i)
#
# item=0
# while item < len(numbers):
#     print(numbers[item])
#     item+=1

# RANGE
# range_numbers = range(5, 10, 2)  # range object, excludes 2nd, 3rd is the step
# print(range_numbers)
# for number in range(5):
#     print(number)

# TUPLES kinda like lists, **immutable**
numbers_tuple = (1, 2, 3, 3, 3, "1")
print(numbers_tuple.count(3))
print(numbers_tuple.index(3))
print(" ")
print("BASICS COVERED")