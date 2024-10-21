# Function
def online_count(dictionnary) : 
    count = 0
    for x in dictionnary : 
        if dictionnary[x] == "online" : 
            count += 1
    return count

# Execution
example = {"Alice": "online", "Bob": "offline", "Eve": "online"}
print(online_count(example))