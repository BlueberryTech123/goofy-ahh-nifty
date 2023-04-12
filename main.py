import csv

file_path = "fatal-police-shootings-data.csv"
data = open(file_path, 
    mode="r",
    newline="")

column_names = []

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
    
    for row in csv.reader(data):
        cur = row[get_col(identifier_name)]
        if cur == identifier:
            return_value.append(row)
    return return_value

# 1
print(rows_by_column("id", "1694")[0][get_col("name")])
print(rows_by_column("id", "1694")[0][get_col("name")])

# 2
print(rows_by_column("id", "1694"))
for row in rows_by_column("state", "MN"):
    print(row[get_col("name")])


"""

1. Print the name of the subject of the fatal police shooting with ID number 1694. If you’ve followed current events in the past few years, this should be a familiar name.

2. Print the name of all subjects of fatal police shootings in Minnesota in the dataset. This will require iteration using a for loop.

3. Create a new dictionary, called race counts, which is initialized as an empty dictionary, and built by iterating through database, and following an accumulator pattern. The purpose of this dictionary will be to count the number of occurrences of each race among subjects of fatal police shootings. The keys in this dictionary should be races, and the corresponding values should be the number of subjects of that race.

4. Print the fraction of fatal police shootings with a black subject. This should be a number between 0 and 1, and can be computed by dividing the number of fatal police shootings with a black subject (you can get this from the dictionary race counts), by the total number of fatal police shootings (how can you get this without hard coding?).

"""