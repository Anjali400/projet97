import random

print('Number Guessing Game 🤔 ') 

number = random.randint(1,9)
 
chances = 0 
print("Guess a number (between 1 and 9):")
while chances < 5:
    guess = int(input('Enter your guess  ↪ : ')) 

    if guess == number:  
        print('Congratulations! you won 😻' )
    elif guess < number:
        print('Your guess is too low.😢' )
    else:
        print('Your guess was too high.😿', ) 

    chances = chances + 1
 
if not chances < 5:
    print('You lose 😭 ! and the number is', number) 
