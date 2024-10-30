# Inputs
input_list = [1, 2, 3]

# Function
def convert_long_version(numbers_list) : 
    for x in numbers_list : 
        numbers_list[x - 1] = str(numbers_list[x - 1])
    return numbers_list

def convert(numbers_list) : 
    return list(map(str, numbers_list)) # Thank you @sudo_404_hub ! 

# Execution
print(convert_long_version(input_list))
print(convert(input_list))