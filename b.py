import random

def guess_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Ask the user to guess the number
    while True:
        guess = int(input("Guess the number between 1 and 100: "))
        
        # Check if the guess is correct
        if guess == secret_number:
            print("Congratulations! You've guessed the correct number:", secret_number)
            break
        # Provide feedback if the guess is too high
        elif guess > secret_number:
            print("Too high! Try again.")
        # Provide feedback if the guess is too low
        else:
            print("Too low! Try again.")

# Call the function to start the game
guess_number()
