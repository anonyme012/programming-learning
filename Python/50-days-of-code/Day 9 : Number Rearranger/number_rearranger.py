# Global Loop
while True : 

# Inputs
    valid_input = False
    while valid_input == False : 
        print("To quit, press ^C")
        number = input("Enter a number : ")
        if number.isdigit() : 
            valid_input = True
        if valid_input == False : 
            print("Please enter a valid number.")

# Set Creator Loop
    count = 0
    digit_list = []
    while count < len(number) : 
        digit_list.append(int(number[count]))
        count += 1

# Set Rearranger
    ascending_digit_list = sorted(digit_list)
    descending_digit_list = sorted(digit_list, reverse = True)

# Reassembler
    count = 0
    smallest_number = ""
    while count < len(number) : 
        smallest_number += str(ascending_digit_list[count])
        count += 1

    count = 0
    largest_number = ""
    while count < len(number) : 
        largest_number += str(descending_digit_list[count])
        count += 1

# Calculation
    difference = int(largest_number) - int(smallest_number)

# Output
    print("For the number" + number + ", the largest number we can compose with his digits is " + str(largest_number) + " and the smallest is " + str(smallest_number) + ".")
    print("So, their difference is : " + str(difference) + ".")

# My errors during programming : 
# - I used sort() instead of sorted() to sort the list.
# - I forgot some str() or int() type conversion.

# Possibles improvements : 
# - Make a challenge where is needed an other type of sorting.