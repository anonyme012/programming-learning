# Functions Definition
def differences(string1, string2) : 
    global_string = ""
    count1 = 0
    while count1 < len(string2) : 
        count2 = 0
        is_not_found = True
        while count2 < len(string1) : 
            if count1 < len(string1) : 
                if string2[count1] == string1[count2] : 
                    global_string += string2[count1]
                    is_not_found = False
                    break
                    ###
            count2 += 1
            print(global_string, count1, count2, is_not_found) #####
        count1 += 1
        if is_not_found : 
            count1 += 1

# Inputs
string_1 = input("String 1 : ")
string_2 = input("String 2 : ")

# Execution
differences(string_1, string_2)

# My errors during programming : 
# - I forgot to increment counters in each iteration of the loops.
# - Many cases that wasn't handled.

# Possibles improvements : 
# - Do it simpler with specific functions.
# - Handle errors.

#############################################################################
# I skiped the today project because it's hard without the right functions. #
#############################################################################