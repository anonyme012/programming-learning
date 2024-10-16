# Inputs
first_sentence = input("Enter the 1st sentence : ")
second_sentence = input("Enter the 2nd sentence : ")

# Strings to Lists
first_sentence_list = first_sentence.split()
second_sentence_list = second_sentence.split()

# Length Verifying
count = 0
length_condition = True
if len(first_sentence_list) == len(second_sentence_list) : 
    while count < len(first_sentence_list) : 
        if len(first_sentence_list[count]) != len(second_sentence_list[count]) : 
            length_condition = False
        count += 1
else : 
    length_condition = False

count = 0
length_condition = True
if len(first_sentence_list) == len(second_sentence_list) : 
    while count < len(second_sentence_list) : 
        if len(first_sentence_list[count]) != len(second_sentence_list[count]) : 
            length_condition = False
        count += 1
else : 
    length_condition = False

# No-duplicate Verfiying
duplicate_condition = True
if length_condition : 
    count1 = 0
    while count1 < len(first_sentence_list) : 
        count2 = 0
        while count2 < len(first_sentence_list[count1]) : 
            count3 = 0
            while count3 < len(second_sentence_list[count1]) : 
                if first_sentence_list[count1][count2] == second_sentence_list[count1][count3] : 
                    duplicate_condition = False
                count3 += 1
            count2 += 1
        count1 += 1

# Output
if length_condition and duplicate_condition : 
    print("The sentences \"" + first_sentence + "\" and \"" + second_sentence + "\" are shadow sentences.")
else : 
    print("The sentences provided aren't shadow sentences.")

# My errors during programming : 
# - Forgot to reset to 0 counters for each iteration of the parent loop.
# - Some logicals errors due to imbricated loops or conditions.

# Possibles improvements : 
# - Ingore "." at the end of the sentence.
# - Add a global loop to repeat the program endlessly.
