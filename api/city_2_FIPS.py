# Importing CSV file and converting to dictionary with zipcode as the key
# and county as the value

with open("uscities.csv") as file:
    data = file.read()
rows = data.split("\n")
# Create a dictionary
city_fip = {}
# Splitting the rows and putting the CSV data into a list
for row in rows:
    info = row.split(",")
    if len(info) == 6:      # Making sure that blank lines are ignored
        city = info[0]
        state = info[1]
        fip = info[2]
# Populate the dictionary from the new list city, state: FIPS
        city_fip[city+", "+state] = fip

print(city_fip)






