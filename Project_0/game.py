"""Guess the number game."""

import numpy as np

number = np.random.randint(1, 101) # Guess the number

# Number of guess attempts
count = 0

while True:
    count += 1
    predict_number = int(input("Guess the number from 1 to 100 -> "))
    
    if predict_number > number:
        print("The number must be less than it!")
        
    elif predict_number < number:
        print("The number must be greater than it!")
        
    else:
        print(f"Congratulations! You guessed it! This number is: {predict_number} The number of attempts:{count}")
        break