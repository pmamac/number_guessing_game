"""
Project 1 - Number Guessing Game
--------------------------------

For this first project you can use Workspaces. 

NOTE: If you prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""


"""Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Save their attempt number to a list.
    6. At the end of the game, show the player, 1) their number of attempts, 2) the mean, median, and mode of the saved attempts list.
    7. Ask the player if they want to play again.
    
    ( You can add more features/enhancements if you'd like to. )
    """
  
    # write your code inside this function.
  
import random
import statistics

def start_game():
  print("""
    * English: Welcome to the Number Guessing Game!
    * Tagalog: Maligayang pagdating sa laro ng paghula ng numero!
    * Japanese: 数当てゲームへようこそ!
    * Chinese: 歡迎來到猜數字遊戲!
    """)
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

  print("You took {} attempts to guess the number.".format(num_attempts))
  print("The mean of your attempts was {}.".format(mean_attempt))
  print("The median of your attempts was {}.".format(median_attempt))
  print("The mode of your attempts was {}.".format(mode_attempt))

  play_again = input("Do you want to play again? (y/n) ")
  if play_again.lower() == "y":
      start_game()
  else:
      print("Thanks for playing!")

# Kick off the program by calling the start_game function.
start_game()
