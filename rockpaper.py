import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)


def get_user_choice():
    while True:
        user_choice = input("Enter rock, paper, or scissors: ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid input. Please choose 'rock', 'paper', or 'scissors'.")


def display_choice(choice):
    if choice == 'rock':
        print(rock)
    elif choice == 'paper':
        print(paper)
    elif choice == 'scissors':
        print(scissors)


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'paper' and computer_choice == 'rock') or \
            (user_choice == 'scissors' and computer_choice == 'paper'):
        return "user"
    else:
        return "computer"


def play_game():
    while True:
        user_score = 0
        computer_score = 0
        tie_score = 0
        rounds = 5

        print("Welcome to Rock, Paper, Scissors! Let's play 5 rounds.")

        for round_num in range(1, rounds + 1):
            print(f"\nRound {round_num}:")
            user_choice = get_user_choice()
            computer_choice = get_computer_choice()

            print(f"\nYou chose:")
            display_choice(user_choice)

            print(f"The computer chose:")
            display_choice(computer_choice)

            winner = determine_winner(user_choice, computer_choice)

            if winner == "user":
                user_score += 1
                print("You win this round!")
            elif winner == "computer":
                computer_score += 1
                print("You lose this round!")
            else:
                tie_score += 1
                print("It's a tie this round!")

        print("\nGame Over!")
        print(f"\nFinal Score:\nYou: {user_score} | Computer: {computer_score} | Ties: {tie_score}")

        if user_score > computer_score:
            print("You are the overall winner!")
        elif user_score < computer_score:
            print("The computer is the overall winner!")
        else:
            print("It's a tie overall!")

        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    play_game()
