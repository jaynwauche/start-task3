# Modified Guessing game
import random
initial_guess_number = random.randint(1, 100)
easy_number = random.randint(1, 10)
medium_number = random.randint(1, 20)
hard_number = random.randint(1, 50)
guess_count = 5

try:
    for a in range(5):
        guess_count -= 1
        user_guess_number = int(input('Guess a number: '))
        if user_guess_number == initial_guess_number:
            print('You got it right!!!')
            break
        else:
            print('That was Wrong')
            print(f'You have {guess_count} guesses remaining')
    else:
        print('Game Over')
except ValueError:
    user_guess_number1 = (input('There are three levels: easy, medium, and hard, choose: '))

    # a function that will be called by the different levels of the game avoiding repeatation of code
    def guessing(level_count, level_system_number, guess_count):
        for a in range(level_count):
            guess_count -= 1
            try:
                num1 = int(input('Make a guess: '))
                if num1 == level_system_number:
                    print("You got it right!!!")
                    break
                else:
                    print("That was wrong")
                    print(f"You have {guess_count} guesses remaining")
            except ValueError:
                print('please enter a valid number')
                print(f"You have {guess_count} guesses remaining")
        else:
            print("Game Over!!!")

     #Different levels of the game calling the guessing function           
    if user_guess_number1 == 'easy':
        guessing(6, easy_number, 6)
    elif user_guess_number1 == 'medium':
        guessing(4, medium_number, 4)
    elif user_guess_number1 == 'hard':
        guessing(3, hard_number, 3)
    
            
