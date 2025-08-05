import random

def random_number_generator():
    print("Welcome to the Random Number Generator!")
    print("It will generate a random number between 1 and 100.")
    try:
        lower_limit = 1
        upper_limit = 100
        
        random_number = random.randint(lower_limit, upper_limit)
        print(f"Your random number between {lower_limit} and {upper_limit} is: {random_number}")
        if random_number>90:
            print("Your Lucky one: That is a high number!")
        else:
            print("Try again for a lucky number!!")
    except ValueError:
        print("Please enter valid numbers for the limits.")

random_number_generator()
