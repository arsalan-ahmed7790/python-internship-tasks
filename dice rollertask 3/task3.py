import random

def roll_dice(num_dice):
    results = []
    for _ in range(num_dice):
        roll_result = random.randint(1, 6)
        results.append(roll_result)
    return results

def main():
    print("Welcome to the Dice Rolling App!")

    while True:
        try:
            num_dice = int(input("How many dice would you like to roll? "))
            if num_dice <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        results = roll_dice(num_dice)
        print(f"Result of rolling {num_dice} dice:")
        for i, result in enumerate(results, start=1):
            print(f"Die {i}: {result}")

        roll_again = input("Roll again? (yes/no): ").lower()
        if roll_again != "yes":
            print("Thank you for using the Dice Rolling App. Goodbye!")
            break

if __name__ == "__main__":
    main()
