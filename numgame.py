import random

difficulty = "easy"
in_Menu = True
is_Guessing = False
changing_Diff = False
player_chances = 10
player_attempts = 0

while in_Menu:
    print("WELCOME TO THE NUMBER GUESSING GAME!")
    print("Rules: Guess the number before your chances run out!\n")
    print("1. Start Game\n"
          f"2. Change Difficulty ({difficulty.capitalize()})\n"
          "3. Quit")
    user_input = input("Select an option (1-3): ")
    if user_input == "1":
        print("Let the guessing commence!")
        in_Menu = False
        is_Guessing = True
    elif user_input == "2":
        changing_Diff = True
        while changing_Diff:
            print("Difficulties:\n"
                  "1. Easy (10 chances)\n"
                  "2. Medium (5 chances)\n"
                  "3. Hard (2 chances)")
            user_difficulty = input("Select a difficulty (1-3): ")
            if user_difficulty.isdigit():
                user_difficulty = int(user_difficulty)
                if user_difficulty == 1:
                    difficulty = "easy"
                    player_chances = 10
                    changing_Diff = False
                    break
                elif user_difficulty == 2:
                    difficulty = "medium"
                    player_chances = 5
                    changing_Diff = False
                    break
                elif user_difficulty == 3:
                    difficulty = "hard"
                    player_chances = 2
                    changing_Diff = False
                    break
                else:
                    print("Please enter a valid difficulty.")
            else:
                print("Incorrect input.")
    elif user_input == "3":
        print("Thanks for playing!")
    else:
        print("Wrong input!")

input("Press ENTER to begin.")
for i in range(1,10):
    print("\n")
min_num = 1
max_num = 100
magic_num = random.randint(min_num, max_num)
print(f"I'm thinking of a number between {min_num} and {max_num}...")
print(f"You have {player_chances} chances to guess the number.")
is_Guessing = True
player_attempts = 0

while is_Guessing:
    player_guess = input("Enter your guess: ")
    # check digit
    if player_chances != 1:
        if player_guess.isdigit():
            player_guess = int(player_guess)
            if max_num >= player_guess >= min_num:
                if player_guess == magic_num:
                    print("\n")
                    print("******************* CONGRATULATIONS *******************")
                    print(f"*** You guessed the magic number {magic_num} in {player_attempts} attempts! ***")
                    print("          *** BOOM! FIREWORKS! CONFETTI'S! ***")
                    is_Guessing = False
                    break
                elif player_guess > magic_num:
                    player_attempts += 1
                    player_chances -= 1
                    print(f"The magic number is lower than {player_guess}..")
                elif player_guess < magic_num:
                    player_attempts += 1
                    player_chances -= 1
                    print(f"The magic number is higher than {player_guess}..")
            else:
                print(f"Hey hey! The magic number is between {min_num} and {max_num}!")
            print(f"You got {player_chances} chances left!")
        elif player_guess == "quit" or player_guess == "q" or player_guess == "exit":
            is_Guessing = False
            break
        else:
            print("Type a number.")
    else:
        print("Sorry, you're out of chances! The magic number disappears...")
        is_Guessing = False
        user_input = input("Play again? (y/n):")
        if user_input == "y":
            magic_num = random.randint(min_num, max_num)
            player_attempts = 0
            if difficulty == "easy":
                player_chances = 10
            elif difficulty == "medium":
                player_chances = 5
            elif difficulty == "hard":
                player_chances = 2
            print(f"You have gained {player_chances} chances this time..")
            print(f"I'm thinking of a new magic number between {min_num} and {max_num}...")
            is_Guessing = True
        elif user_input == "n":
            print("Thanks for playing!")
        else:
            print("Thanks for playing!")
