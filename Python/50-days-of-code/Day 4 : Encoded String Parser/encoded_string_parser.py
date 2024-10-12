# Input
encoded_string = input("Enter an encoded string : ")

# Zero Count
zero_count = 0

# First Name
count_fn = 0
first_name = ""
while count_fn < len(encoded_string) : 
    first_name += encoded_string[count_fn]
    count_fn += 1
    if encoded_string[count_fn] == "0" : 
        break
count_fn_2_ln = len(first_name)
while encoded_string[count_fn_2_ln] == "0" :
    zero_count += 1
    count_fn_2_ln += 1

# Last Name
count_ln = count_fn_2_ln
last_name = ""
while count_ln < len(encoded_string) : 
    last_name += encoded_string[count_ln]
    count_ln += 1
    if encoded_string[count_ln] == "0" : 
        break
count_ln_2_id_string = len(first_name) + len(last_name) + zero_count
while encoded_string[count_ln_2_id_string] == "0" :
    zero_count += 1
    count_ln_2_id_string += 1

# ID
count_id = count_ln_2_id_string
id_string = ""
while count_id < len(encoded_string) : 
    id_string += encoded_string[count_id]
    count_id += 1

# Dictionnnary & Output
dictionnary = {"first_name" : first_name, "last_name" : last_name, "id_string" : id_string}
print(dictionnary)

# My errors during programming : 
# - Logic errors : varibles confusion or loop oversight.

# Possibles improvements : 
# - Use "for" loops instead of "while" loops (I only know "while" now).
# - Use the split() function instead of my complex loop system.
