import csv

#Define Empty list to add names
list = []

#Make header for csv file
header = ["Name", "Last Name", "Suffix"]

file = open("coolguy.txt", "r")
#Loop over all contents of the file
while True:
    fullName = []
    contents = file.readline().strip()
    names = contents.split()
    #Stop when file hits empty space
    if contents == "":
        break
    #For names greater than 3 words (This only accounts for 1 Suffix and names with 1 Last Name and 1 First Name, so no Latin american names :( )
    # In other words, this is if the name has a suffix
    if len(names) >= 3:
        fname = names[0]
        lname = names[2]
        suffix = names[1]
        print(f"First Name: {fname}\nLast Name: {lname}\nSuffix: {suffix}")
        fullName.append(fname)
        fullName.append(lname)
        fullName.append(suffix)
        list.append(fullName)
    #For Names with a First and Last name
    elif len(names) == 2:
        fname = names[0]
        lname = names[1]
        print(f"First Name: {fname}\n Last Name: {lname}")
        fullName.append(fname)
        fullName.append(lname)
        list.append(fullName)
    #If somebody inputs a name that is too long, do this:
    else:
        limit = len(names)
        fname = names[0]
        lname = names[limit]
        print(f"First Name: {fname}\n Last Name: {lname}")
        fullName.append(fname)
        fullName.append(lname)
        list.append(fullName)
    print(list)
    #print(names)
#Close file to get it out of the RAM
file.close()

with  open("list.csv", "a+") as file:
    csvWriter = csv.writer(file)
    csvWriter.writerow(header)
    csvWriter.writerows(list)
