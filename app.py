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
prices = [1,2,3]
sum = 0
for price in prices:
    sum += price
print(f"Total: {sum}")

# NESTED LOOP

for x in range(4):  # excludes this digit
    for y in range(2):
        print(f"{x}, {y}")

# PRINT AN F
x_per_row = [5, 2, 5, 2, 2]
for x_count in x_per_row:
    output = ""
    for count in range(x_count):
        output += "x"
    print(output)

# FIND BIGGEST N
numberss = [1, 2, 3, 4, 5]
max = numberss[0]
for n in numberss:
    if n > max:
        max = n
print(max)

# 2D LISTS
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0][0])

for row in matrix:
    for item in row:
        print (item)