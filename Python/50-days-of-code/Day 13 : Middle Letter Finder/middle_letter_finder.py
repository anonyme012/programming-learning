# Input
input_string = input("Enter a string : ")

# Function
def mid(string) : 
    if len(string) % 2 != 0 : 
        output = "a"
    else : 
        output = ""
    return output

# Execution
if mid(input_string) == "" : 
    print("The string \"" + input_string + "\" didn\'t have middle letter.")
else : 
    print("The middle letter of string \"" + input_string + "\" is \"" + mid(input_string) + "\".")