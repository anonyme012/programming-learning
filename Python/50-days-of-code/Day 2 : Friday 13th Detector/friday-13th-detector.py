# Imports
import datetime
from datetime import date

# Inputs
year = int(input("Enter the year : "))
month = int(input("Enter the month : "))

# Execution
if date(year, month, 13).isoweekday() == 5 : 
    print("The 13th is a friday in this month.")
else : 
    print("The 13th is not a friday in this month.")

# My errors during programming
# - I forgot to import date from datetime.

# Possibles improvements : 
# - Nothing i think.