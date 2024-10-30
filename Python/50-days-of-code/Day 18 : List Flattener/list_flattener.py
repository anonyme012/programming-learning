# Test Variables
test_list = [[1, 2], [3, 4], [5, 6]]

# Function
def flatten(md_list) : 
    output_list = []
    for x in md_list : 
        output_list.extend(x)
    return output_list

# Execution
print(flatten(test_list))