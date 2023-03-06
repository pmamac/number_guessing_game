import random
import statistics


def welcome_player():
    languages = {
        "English": "Welcome to the Number Guessing Game!",
        "Tagalog": "Maligayang pagdating sa laro ng paghula ng numero!",
        "Japanese": "数当てゲームへようこそ!",
        "Chinese": "歡迎來到猜數字遊戲!",
    }
    for language, message in languages.items():
        print(f"* {language}: {message}")


def get_player_name():
    name = input("What's your name? ")
    print(f"Hello, {name}! Let's start the game!")
    return name


def get_lucky_number():
    return random.randint(1, 100)


def get_guess():
    while True:
        guess = input("Guess a number between 1 and 100: ")
        try:
            guess = int(guess)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        return guess


def play_game():
    name = get_player_name()
    lucky_number = get_lucky_number()
    attempts = []

    while True:
        guess = get_guess()
        attempts.append(guess)

        if guess < lucky_number:
            print("Hint: the answer is higher!")
        elif guess > lucky_number:
            print("Hint: the answer is lower!")
        else:
            print(f"Congratulations, {name}! You guessed the number in {len(attempts)} attempts!")
            return attempts


def play_again():
    while True:
        choice = input("Do you want to play again? (y/n) ").lower()
        if choice in ["y", "n"]:
            return choice == "y"
        print("Invalid input. Please enter 'y' or 'n'.")


def display_stats(attempts):
    num_attempts = len(attempts)
    mean_attempt = statistics.mean(attempts)
    median_attempt = statistics.median(attempts)
    mode_attempt = statistics.mode(attempts)

    print(f"\nNumber of attempts: {num_attempts}")
    print(f"Mean: {mean_attempt:.2f}")
    print(f"Median: {median_attempt:.2f}")
    print(f"Mode: {mode_attempt}\n")


def main():
    welcome_player()
    high_score = 0

    while True:
        attempts = play_game()
        display_stats(attempts)

        if len(attempts) < high_score or high_score == 0:
            high_score = len(attempts)
            print("Congratulations! You've set a new high score!")
        else:
            print(f"Your current high score is {high_score} attempts.")

        if not play_again():
            print("Thank you for playing. Goodbye!")
            break


if __name__ == "__main__":
    main()
