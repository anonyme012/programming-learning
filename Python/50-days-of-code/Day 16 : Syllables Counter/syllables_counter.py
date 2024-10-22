# Input
input_string = input("Enter a string : ")

# Function
def count(string) :
    if string[0] == "-" or string[-1] == "-" : 
        return "Your string is invalid." 
    output = string.count("-") + 1
    return output

# Execution
print(count(input_string))