"""
The game: Guess the number 
The computer makes its own guesses and guesses the number.
"""


import numpy as np


def random_predict(number: int=1) -> int:
    
    """Randomly guessing a number.

    Args:
        number (int, optional): Guess the number. Defaults to 1.

    Returns:
        int: The number of attempts
    """
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)          # The estimated number
        if number == predict_number:
            break                                           # Exit the loop if the number is guessed
    return(count)


def score_game(random_predict) -> int:
    """Average number of attempts to guess a number of 1000 times

    Args:
        random_predict (_type_): The guessing function

    Returns:
        int: Average number of attempts
    """

    count_ls = []
    np.random.seed(1)                                       # Fix the seed
    random_array = np.random.randint(1, 101, size=(1000))   # The list of numbers
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f"Your algorithm guesses a number in an average of: {score} tries")
    return(score)
    
if __name__="__main__":
    score_game(random_predict)