import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    player_name = input("What's your name? ")
    print(f"Hello, {player_name}! I'm thinking of a number between 1 and 100.")

    while True:
        target_number = random.randint(1, 100)
        attempts = 0
        max_attempts = 10

        while attempts < max_attempts:
            try:
                user_guess = int(input("Take a guess: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            attempts += 1

            if user_guess < target_number:
                print("Too low. Try again.")
            elif user_guess > target_number:
                print("Too high. Try again.")
            else:
                print(f"Congratulations, {player_name}! You guessed the number ({target_number}) in {attempts} attempts!")
                break

        if attempts == max_attempts:
            print(f"Game over, {player_name}. The number was {target_number}.")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thank you for playing! Goodbye.")
            break

if __name__ == "__main__":
    number_guessing_game()