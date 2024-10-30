# Function
def list_xor(n, list1, list2) : 
    is_exclusive = True
    if n in list1 : 
        if n in list2 : 
            is_exclusive = False
    if not n in list1 : 
        if not n in list2 : 
            is_exclusive = False
    return is_exclusive

# Execution
print("Run \"list_xor(1, [2, 1, 3], [1, 5, 6])\" returns : " + str(list_xor(1, [2, 1, 3], [1, 5, 6])))
print("Run \"list_xor(3, [0, 8, 3], [2, 4, 0])\" returns : " + str(list_xor(3, [0, 8, 3], [2, 4, 0])))
print("Run \"list_xor(8, [10, 0, 0], [3, 5, 7])\" returns : " + str(list_xor(8, [10, 0, 0], [3, 25, 7])))
print("Run \"list_xor(\"a\", [\"g\", \"f\", \"l\"], [\"a\", \"b\", \"c\"])\" returns : " + str(list_xor("a", ["g", "f", "l"], ["a", "b", "c"])))