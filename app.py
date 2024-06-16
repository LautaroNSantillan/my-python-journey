choice = input("1 for guess game 2 for car game ")

if choice == "1":
    secret_number = 9
    guess_count = 0
    guess_limit = 3
    while guess_count < guess_limit:
        guess = int(input("Guess the number: "))
        guess_count+=1
        if guess == secret_number:
            print("Done")
            break
    else:
        print("no more attempts")

if choice == "2":
    command = ""
    started = False
    while True:
        command = input(">").lower()
        if command == "start":
            if started:
                print("already started")
            else:
                started=True
            print("car started")
        elif command == "stop":
            if not started:
                print("already stopped")
            else:
                started = False
            print("car stopped")
        elif command == "help":
            print("""
start
stop
quit
            """)
        elif command == "quit":
            break
        else:
            print("invalid command")
