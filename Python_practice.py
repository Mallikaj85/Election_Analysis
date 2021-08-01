print("Hello World")
counties = ["Arapahoe","Denver","Jefferson"]

#Index Lists
counties[0]
print(counties[2])

#Find the Length of a List
len(counties)

#Slice Lists
counties[0:2]
counties[0:1]
counties[:2]

#Add Items to a List
counties.append("El Paso")
counties
counties.insert(2, "El Paso")
counties
counties.pop(2)
counties
counties[2] = "El Paso"
counties

#Storing and accessing data in lists
counties_tuple = ("Arapahoe","Denver","Jefferson")
len(counties_tuple)

#Create a Dictionary
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
counties_dict
len(counties_dict)
counties_dict.items()
counties_dict.keys()
counties_dict.values()
counties_dict.get("Denver")
counties_dict['Arapahoe']
counties_dict["Arapahoe"]
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
voting_data

counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

counties = ["Arapahoe","Denver","Jefferson"] 
if "Arapahoe" in counties: print("True") 
else: print("False")

counties = ["Arapahoe","Denver","Jefferson"] 
if "El Paso" not in counties: print("True") 
else: print("False")

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

x = 5
y = 5
if x == 5 and y == 5: print("True") 
else: print("False")

x = 5
y = 5
if x == 3 or y == 5: print("True")
else: print("False")

x = 5
y = 5
if not(x > y): print("True") 
else: print("False")

x = 0
while x <= 5: print(x)
    x = x + 1


counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict: print(county)
for county in counties_dict.keys(): print(county)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},{"county":"Denver", "registered_voters": 463353},{"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data: print(county_dict)

#Using F-Strings with Dictionaries
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

#Multiline F-Strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")
print(message_to_candidate)