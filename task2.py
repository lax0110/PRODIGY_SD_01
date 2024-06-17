import random

def guess():
    print("Guess the number")

    no = random.randint(1, 40)
    attempts = 0
    guessed = False

    while not guessed:
        try:
            user_guess = int(input("\nEnter number: "))
            attempts += 1

            if user_guess == no:
                print("Yes, it's Correct!")
                print(f"It took you {attempts} attempts to guess the number.")
                guessed = True
            elif user_guess < no:
                print("Too low!")
            else:
                print("Too high!")

        except ValueError:
            print("Invalid input. Please enter a valid number.")


guess()

