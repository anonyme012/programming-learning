# Inputs
str1 = input("Enter the 1st string : ")
str2 = input("Enter the 2nd string : ")

# Functions
def is_anagram(string1, string2) : 
    # Strings to Lists conversion
    list1 = list(string1)
    list2 = list(string2)
    # Lists sorting
    list1.sort()
    list2.sort()
    # Lists comparison
    if list1 == list2 : 
        output = True
    else : 
        output = False
    return output

# Execution
if is_anagram(str1, str2) : 
    print("✓ : The strings \"" + str1 + "\" and \"" + str2 + "\" are anagrams.")
else : 
    print("X : The strings \"" + str1 + "\" and \"" + str2 + "\" are not anagrams.")
