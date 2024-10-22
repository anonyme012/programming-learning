# Input
input_string_add = input("Enter a string where add dots : ")
input_string_remove = input("Enter a string where remove dots : ")

# Functions
def add_dots(string) :
    output = ""
    count = 0
    while count < len(string) : 
        output += string[count] + "."
        count += 1
    output = output[:-1]
    return output

def remove_dots(string) :
    output = string.replace(".", "")
    return output

# Execution
print(add_dots(input_string_add))
print(remove_dots(input_string_remove))