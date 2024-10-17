# Global Loop
while True :

    # Inputs
    valid_inputs = False
    while valid_inputs == False : 
        print("To quit, press ^C.")
        string1 = input("Enter the first string : ")
        string2 = input("Enter the second string : ")
        if len(string1) > len(string2) : 
            string1, string2 = string2, string1
        if string1.isalpha() and string2.isalpha() and (len(string1) + 1 == len(string2)) : 
            valid_inputs = True
        else : 
            print("Please enter valid strings (only with alphabetic characters).")

    # Function
    def find_extra_char(str1, str2) : 
    # String to List Conversion
        list1 = []
        for x in str1 : 
            list1.append(x)
        list2 = []
        for x in str2 : 
            list2.append(x)

    # Lists Sorting
        list1.sort()
        list2.sort()

    # Difference Searching
        found = False
        count = 0
        while count < len(list1) : 
            if list1[count] != list2[count] : 
                print("The difference between the two strings provided is : " + list2[count])
                found = True
                break
            count += 1
        if found == False : 
            print("The difference between the two strings provided is : " + list2[count])

    # Execution
    find_extra_char(string1, string2)

# My errors during programming : 
# - I forgot to handle the cases where the string are not valid.
# - I forgot to handle the case where the difference is on the end of the string2.
# - Simply unworking code as you can see below.

# Possibles improvements : 
# - Add a global loop.
# - Find multples differences.
# - Handle more cases where the strings aren't valid.

###################
# FIRST TRY BEGIN #
###################
## Functions Definition
#def differences(string1, string2) : 
#    global_string = ""
#    count1 = 0
#    while count1 < len(string2) : 
#        count2 = 0
#        is_not_found = True
#        while count2 < len(string1) : 
#            if count1 < len(string1) : 
#                if string2[count1] == string1[count2] : 
#                    global_string += string2[count1]
#                    is_not_found = False
#                    break
#                    ###
#            count2 += 1
#            print(global_string, count1, count2, is_not_found) #####
#        count1 += 1
#        if is_not_found : 
#            count1 += 1
#
## Inputs
#string_1 = input("String 1 : ")
#string_2 = input("String 2 : ")
#
## Execution
#differences(string_1, string_2)
#################
# FIRST TRY END #
#################