import random
from D12art import logo
game_start = logo
print(game_start)
complete_list = list(range(101))
number = random.choice(complete_list)

print(f"pssst, the number is {number}\n")
def guess(pick):
    if pick > number:
        print("Too high ")
    elif pick < number:
        print("Too low ")
    else:
        print('Correct!')
    

decision = True
# guess(40)

print("Welcome to the guessing game, I'm thinking of a number between 0 and 100 ")
level = input("choose a difficulty level, type 'easy' or 'hard'. ")
ATTEMPTS = 0
if level == 'easy':
    ATTEMPTS = 10
elif level == 'hard':
    ATTEMPTS = 5
else:
    ("That is an incorrect input, try again. ")

while decision:
    chances = ATTEMPTS
    print(f"you have {ATTEMPTS} left ")
    user_guess = int(input("Make a guess: "))
    guess(user_guess)
    ATTEMPTS -= 1
   
    if ATTEMPTS == 0:
        print('you are out of attempts. Sorry!')
        decision = False
    elif user_guess == number:
        decision = False
   
        
    

    

    
    
    
