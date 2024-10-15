# Inputs
valid_inputs = False
while valid_inputs == False : 
    mark_1 = input("Enter the 1st mark position (0 to 8) : ")
    mark_2 = input("Enter the 2nd mark position (0 to 8) : ")
    if mark_1.isdigit() and mark_2.isdigit() : 
        mark_1 = int(mark_1)
        mark_2 = int(mark_2)
    if mark_1 != mark_2 and mark_1 >= 0 and mark_1 <= 8 and mark_2 >= 0 and mark_2 <= 8 : 
        valid_inputs = True

# Formatting
if mark_1 > mark_2 : 
    mark_1, mark_2 = mark_2, mark_1

# Conditional Structures
if ((mark_2 - mark_1) // 2) == 0  and mark_1 != 4 and mark_2 != 4 : 
    blocking_mark = (mark_1 + mark_2) / 2
elif mark_2 == 1 or mark_2 == 3 or mark_2 == 4 : 
    blocking_mark = mark_2 + (mark_2 - mark_1)
elif mark_2 == 2 or mark_2 == 6 or mark_2 == 7 or mark_2 == 8 or mark_2 == 9 : 
    blocking_mark = mark_1 - (mark_2 - mark_1)
else : 
    blocking_mark = -1

# Output
if blocking_mark == -1 : 
    print("The adversary can't win in the next turn with the data provided.")
else : 
    print("To block the line in the Tic Tac Toe game, you must play in the spot Nº" + str(blocking_mark) + ".")