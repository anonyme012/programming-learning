# Import
import random

# Function
def random_number() : 
    return random.randint(1, 100)

# Global Loop
while True : 
    print("To quit, press ^C")
    input("Press \"Enter\" to generate a random number from 1 to 100 : ")

# Output
    print(random_number())