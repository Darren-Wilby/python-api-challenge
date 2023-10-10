import random

def rock_paper_scissors(user_choice):
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)

    if user_choice.lower() == computer_choice:
        return f'{computer_choice}, it\'s a draw'
    elif (user_choice.lower() == 'rock' and computer_choice == 'scissors') or \
         (user_choice.lower() == 'paper' and computer_choice == 'rock') or \
         (user_choice.lower() == 'scissors' and computer_choice == 'paper'):
        return f'{computer_choice}, you win'
    else:
        return f'{computer_choice}, you lose'