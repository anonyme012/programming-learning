while True : # Global Loop

# Input
    valid = False
    while valid == False : 
        decimal_string = input("Enter a number to convert in hexadecimal (^C to quit) : ")
        if decimal_string.isdecimal() == True : 
            decimal_number = int(decimal_string)
            valid = True
        else : 
            print("Please enter a valid decimal number.")

# Execution
    hexadecimal_number = hex(decimal_number)
    hexadecimal_number = str(hexadecimal_number[2:])

    count = 1
    while count <= len(hexadecimal_number) / 3 : 
        hexadecimal_number = hexadecimal_number[0 : 1 - count * 3] + " " + hexadecimal_number[1 - count * 3 : ]
        count += 1

# Output
    print("In hexadecimal,", decimal_number, "is equal to :", hexadecimal_number)

# My errors during programming
# - I divided the length of "hexadecimal_number" by 2 then 4 but it was 3.

# Possibles improvements :
# - Nothing I think.