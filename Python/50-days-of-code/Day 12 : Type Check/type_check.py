# Function
def only_ints(var1, var2) : 
    is_int = False
    if isinstance(var1, int) and isinstance(var2, int) : 
        is_int = True
    return is_int

# Execution
print("only_ints(2, \"5\") :", only_ints(2, "5"))
print("only_ints(6, 58) :", only_ints(6, 58))
print("only_ints(6.0, 41) :", only_ints(6.0, 41))
print("only_ints([1, 2], 5) :", only_ints([1, 2], 5))

# My errors during programming : 
# - Mistake when using the isinstance() function.

# Possibles improvements : 
# - Make the same function for other types.
# - Add more examples.