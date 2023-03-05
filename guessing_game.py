import random
import statistics

def start_game(high_score=0):
    # Upon starting the game the end-user will be greeted in four different languages, to be inclusive of people that come from diverse backgrounds.
    print("""
    * English: Welcome to the Number Guessing Game!
    * Tagalog: Maligayang pagdating sa laro ng paghula ng numero!
    * Japanese: 数当てゲームへようこそ!
    * Chinese: 歡迎來到猜數字遊戲!
    """)
    
    # Ask for the player's name
    name = input("What's your name? ")

    # Check if there's an existing high score for the player
    try:
        with open("high_scores.txt", "r") as f:
            high_scores = [line.strip().split(",") for line in f.readlines()]
            high_score = next((int(score) for player, score in high_scores if player == name), 0)
    except (FileNotFoundError, ValueError):
        high_score = 0

    # Print the high score if it exists
    if high_score > 0:
        print(f"The high score is {high_score} guesses.\n")

    lucky_number = random.randint(1, 100)
    attempts = []

    while True:
        guess = input("Guess a number between 1 and 100: ")
        try:
            guess = int(guess)
        except ValueError:
            print("Hmm...Something went wrong please try again!:(")
            continue

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100!")
            continue

        attempts.append(guess)

        if guess < lucky_number:
            print("Hint: the answer is higher!")
        elif guess > lucky_number:
            print("Hint: the answer is lower!")
        else:
            print("You Finally Got It! Take Some of This Dopamine Energy!!!")
            break

    num_attempts = len(attempts)
    mean_attempt = statistics.mean(attempts)
    median_attempt = statistics.median(attempts)
    mode_attempt = statistics.mode(attempts)

    print(f"You took {num_attempts} attempts to guess the number.")
    print(f"The mean of your attempts was {mean_attempt:.2f}.")
    print(f"The median of your attempts was {median_attempt:.2f}.")
    print(f"The mode of your attempts was {mode_attempt}.")

    # This line of code ask the end-user if (he/she/they) wishes to play again.
    play_again = input("Do you want to play again? (y/n) ")
    if play_again.lower() == "y":
        # Pass the high score to the next game if the player achieved a new high score
        high_score = num_attempts if high_score == 0 or num_attempts < high_score else high_score
        start_game(high_score)
    else:
        # If they enter "n" a message will pop up thanking them for playing.
        print("Thanks for playing!")
start_game()
