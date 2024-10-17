# Inputs
string = input("Enter a string : ")

# String to List Conversion
words_list = string.split()

# List to Sublists Conversion
letters_list = []
duplicate = False
count1 = 0
while count1 < len(words_list) : 
    count2 = 0
    letters_list.append([])
    while count2 < len(words_list[count1]) : 
        letters_list[count1].append(words_list[count1][count2])
        count2 += 1
    letters_list[count1].sort()
    count2 = 0
    while count2 < len(letters_list[count1]) : 
        if letters_list[count1][count2 - 1] == letters_list[count1][count2] : 
            duplicate = True
        count2 += 1
    count1 += 1

print(duplicate)