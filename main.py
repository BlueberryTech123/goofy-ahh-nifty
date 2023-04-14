import csv

file_path = "fatal-police-shootings-data.csv"

column_names = []

with open(file_path, mode="r", newline="") as data:
    for row in csv.reader(data):
        column_names = row
        break

def get_col(id):
    for i in range(len(column_names)):
        if column_names[i] == id:
            return i
    return -1

def rows_by_column(identifier_name, identifier):
    return_value = []
    
    with open(file_path, mode="r", newline="") as data:
        for row in csv.reader(data):
            cur = row[get_col(identifier_name)]
            if cur == identifier:
                return_value.append(row)
    return return_value

# 1
print("\n=============\nID 1694\n=============\n")
print(rows_by_column("id", "1694")[0][get_col("name")])

# 2
print("\n=============\nFATAL POLICE SHOOTINGS IN MINNESOTA\n=============\n")
for row in rows_by_column("state", "MN"):
    print(row[get_col("name")])

# 3
total_shootings = 0
races = {}
print("\n=============\nRACE DICTIONARY\n=============\n") 
with open(file_path, mode="r", newline="") as data:
    for row in csv.reader(data):
        race = row[get_col("race")]

        if race == "race": 
            continue

        total_shootings += 1

        if race in races:
            races[race] += 1
            continue
        races[race] = 1

print(races)

# 4
print("\n=============\nBLACK SUBJECT FRACTION\n=============\n")
print(races["B"] / total_shootings)

# 5
unarmed_selection = {}
print("\n=============\nUNARMED SUBJECTS DICTIONARY\n=============\n")
with open(file_path, mode="r", newline="") as data:
    for row in csv.reader(data):
        unarmed = row[get_col("armed_with")] == "unarmed"

        if not unarmed: 
            continue
        
        unarmed
print(unarmed_selection)

"""

1. Print the name of the subject of the fatal police shooting with ID number 1694. If you’ve followed current events in the past few years, this should be a familiar name.

2. Print the name of all subjects of fatal police shootings in Minnesota in the dataset. This will require iteration using a for loop.

3. Create a new dictionary, called race counts, which is initialized as an empty dictionary, and built by iterating through database, and following an accumulator pattern. The purpose of this dictionary will be to count the number of occurrences of each race among subjects of fatal police shootings. The keys in this dictionary should be races, and the corresponding values should be the number of subjects of that race.

4. Print the fraction of fatal police shootings with a black subject. This should be a number between 0 and 1, and can be computed by dividing the number of fatal police shootings with a black subject (you can get this from the dictionary race counts), by the total number of fatal police shootings (how can you get this without hard coding?).

5. Create a new dictionary called unarmed_selection, which is initialized as an empty dictionary, and built by iterating through database, and following an accumulator pattern. This dictionary should have the same structure as database, except it will only contain entries for fatal police shootings where the subject was unarmed.

6. Create a new dictionary, called unarmed_race_counts, which is initialized as an empty dictionary, and built by iterating through unarmed selection, and following an accumulator pattern. The purpose of this dictionary will be to count the number of occurrences of each race among subjects of fatal police shootings, including only those where the subject is unarmed. The keys in this dictionary should be races, and the corresponding values should be the number of subjects of that race.

• Print the fraction of unarmed fatal police shootings with a black subject. This should
be a number between 0 and 1, and can be computed by dividing the number of unarmed fatal police shootings with a black subject (you can get this from the dictionary
unarmed race counts), by the total number of unarmed fatal police shootings (how
can you get this without hard coding?).

"""