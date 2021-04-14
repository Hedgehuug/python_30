
"""
Use for/else or while/else to validate all numbers in a
list and print out whether or not there is an even number.
"""

def exercise_1(starter_num,stop_num,step_num):
    numbers = range(starter_num,stop_num,step_num)
    for i in numbers:
        print(i)
        if i % 2 == 0:
            return 'found even number'
            break
    else:
        return 'no even number found'
    return

print(exercise_1(1,11,1))


"""
Create a random number from 1 to 10 and by using a for/else
or while/else allow the user to enter their options, win if
the user guess it, lose after 3 attempts.
"""

# Creation of this game

# Tomorrow I should look at ways to make random number generators

# This number is gonna be random later
import random
number = random.randint(1,11)
attempts = 0
while attempts < 3:
    answer = int(input('Guess a number between 1-10:'))
    if not isinstance(answer,int):
        print('incorrect number')
    if answer != number:
        attempts += 1
        print(f'Incorrect answer, you have {3-attempts} attempts left')
    if answer == number:
        print(f'You guessed the number, it was: {number}. Congratulations!')
        break
else:
    print(f'you have run out of guesses, sorry. The answer is: {number}')





