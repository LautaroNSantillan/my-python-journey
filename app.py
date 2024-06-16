# choice = input("1 for guess game 2 for car game ")
#
# if choice == "1":
#     secret_number = 9
#     guess_count = 0
#     guess_limit = 3
#     while guess_count < guess_limit:
#         guess = int(input("Guess the number: "))
#         guess_count+=1
#         if guess == secret_number:
#             print("Done")
#             break
#     else:
#         print("no more attempts")
#
# if choice == "2":
#     command = ""
#     started = False
#     while True:
#         command = input(">").lower()
#         if command == "start":
#             if started:
#                 print("already started")
#             else:
#                 started=True
#             print("car started")
#         elif command == "stop":
#             if not started:
#                 print("already stopped")
#             else:
#                 started = False
#             print("car stopped")
#         elif command == "help":
#             print("""
# start
# stop
# quit
#             """)
#         elif command == "quit":
#             break
#         else:
#             print("invalid command")

# FOR LOOP
# prices = [1,2,3]
# sum = 0
# for price in prices:
#     sum += price
# print(f"Total: {sum}")

# NESTED LOOP

# for x in range(4):  # excludes this digit
#     for y in range(2):
#         print(f"{x}, {y}")
#
# PRINT AN F
# x_per_row = [5, 2, 5, 2, 2]
# for x_count in x_per_row:
#     output = ""
#     for count in range(x_count):
#         output += "x"
#     print(output)

# FIND BIGGEST N
# numbers = [1, 3, 3, 3, 2, 4, 5]
# max = numbers[0]
# for n in numbers:
#     if n > max:
#         max = n
# print(max)

# 2D LISTS
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print(matrix[0][0])
#
# for row in matrix:
#     for item in row:
#         print(item)
#
# numbers.append(13)
# numbers.insert(0, 0)
# numbers.remove(3)
# numbers.pop()  # removes last item
# print(50 in numbers)
# print(numbers.count(1))
# numbers.sort()
# numbers.reverse()
# numbers2 = numbers.copy()
# print(numbers2)
#
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)
#
# unpacking
# coor = (1, 2, 3)
# x, y, z = coor
#
# dictionaries
# customer = {  # keys should be unique
#     "name": "Doe",
#     "age": 30,
#     "bool": True
# }
# print(customer["name"])
# print(customer.get("default", "default"))
#
# phone = input("phone")
# digits_mapping = {
#     "1": "one",
#     "2": "two",
#     "3": "three",
#     "4": "four"
# }
# output = ""
# for ch in phone:
#     output += digits_mapping.get(ch, "?")+" "
# print(output)

# EMOJI
def emoji_conv(msg):
    split = msg.split(" ")
    emojis_dict = {
        ":)": "smile",
        ":(": "sad"
    }
    output = ""
    for word in split:
        output += emojis_dict.get(word, word)
    return output


# msgg = input(">")
# print(emoji_conv(msgg))

# def greet_user(name, last):
#     print("Hi")
#     print(f"Hi {name} {last}")
# greet_user("john", last="doe")

# def square(n):
#     return n*n
# print(square(2))

try:
    age = int(input("age "))
    income = 200
    risk = income / age
    print(age)
except ValueError:
    print("invalid")
except ZeroDivisionError:
    print("age cannot be 0")