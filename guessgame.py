import random 
import random

def get_difficulty():
    print("\nPlease select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")

    while True:
        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            return 10, "Easy"
        elif choice == "2":
            return 5, "Medium"
        elif choice == "3":
            return 3, "Hard"
        else:
            print("Invalid input. Please enter 1, 2, or 3.")

def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number_to_guess = random.randint(1, 100)
    chances, difficulty = get_difficulty()

    print(f"\nGreat! You have selected the {difficulty} difficulty level.")
    print("Let's start the game!")

    attempts = 0
    while chances > 0:
        try:
            guess = int(input("\nEnter your guess: "))
            attempts += 1
            chances -= 1

            if guess == number_to_guess:
                print(f" Congratulations! You guessed the correct number in {attempts} attempts.")
                break
            elif guess < number_to_guess:
                print("Incorrect! The number is greater than your guess.")
            else:
                print("Incorrect! The number is less than your guess.")

            if chances > 0:
                print(f"You have {chances} chances left.")
            else:
                print(f"\n Game Over! You've used all your chances. The correct number was {number_to_guess}.")

        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    play_game()
