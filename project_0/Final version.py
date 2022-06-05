import numpy as np
number = np.random.randint(1,101) 
count = 0
guess_number = int(input("Guess the number from 1 to 100 "))
left_boundry = 0
right_boundry = 100
while True:
    count += 1
    if guess_number == number:
        print(f"You succeeded! This number = {number}")
        break 
    elif guess_number > number:
        print(f"Your guess {guess_number} is incorrect.Number should be smaller")
        right_boundry = guess_number
    else: 
       print(f"Your guess {guess_number} is incorrect.Number should be bigger")
       left_boundry = guess_number
    guess_number = (left_boundry + right_boundry) // 2
print(f"It took you {count} guesses")  
    
       
        


