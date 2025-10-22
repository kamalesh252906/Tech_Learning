# rainfall_data = {120, 150, 180, 120, 90, 110, 130}
# (This set represents the rainfall in mm recorded across various districts this week.)
# How many rainfall values are in the set?
# Can you directly change the value of an item in a set? 
# What output would you get when you try to change the value using its index ?
# Check if 150 is present inside rainfall_data. (hint: use in keyword and research)
# Convert the set to a list 
# Print every rainfall value by traversing through the set.
# Remove the value 120 from the above set.
# Add the value 110 to the above set and observe if any changes happen ? 
# Why does 110 not appear twice ?


# rainfall_data = {120, 150, 180, 120, 90, 110, 130}
# print(len(rainfall_data))
# No , we can't directly change the value of an item in a set.
# rainfall_data[1] = 130
# # 'set' object does not support item assignment
# if 150 in rainfall_data:
#     print('present')
# else:
#     print('not present')
# lists = list(rainfall_data)
# print(lists)
# for i in rainfall_data:
#     print(i)
# rainfall_data.add(110)
# print("After removing 120:", rainfall_data)
# It does not appear duplicate data

# rainfall_chennai = {120, 140, 160, 180}
# rainfall_madurai = {110, 130, 150, 180}
# rainfall_coimbatore = {100, 120, 180, 200}
# The Rainfall data starts from Monday to Thursday here, if added more data, it will be considered as the next day in the week.
# Print all unique rainfall measurements for Chennai and Madurai.
# Merge all three readings into a new set using both the update() and union() methods.
# Common Rainfall: Identify rainfall values present in all three cities.
# Unique Chennai Rainfall: Determine unique rainfall values observed exclusively in Chennai.
# Rainfall in at least Two Cities: Find rainfall values recorded in a minimum of two cities.
# Create a new set where every rainfall value is increased by 10. 
# For e.g. if input is {120, 140, 160,180}, then output has to be {130, 150, 170, 190}	


# Other Miscellaneous Methods:
# Delete the rainfall_coimbatore set in python.
# Clear the data inside rainfall_chennai set and make it empty.


rainfall_chennai = {120, 140, 160, 180}
rainfall_madurai = {110, 130, 150, 180}
rainfall_coimbatore = {100, 120, 180, 200}
# print(rainfall_chennai.union(rainfall_madurai))
# print(rainfall_chennai | rainfall_coimbatore | rainfall_madurai)
# print(rainfall_chennai & rainfall_coimbatore & rainfall_madurai)
# print(rainfall_chennai - rainfall_coimbatore - rainfall_madurai)
mtwo = rainfall_chennai & rainfall_coimbatore
ctwo = rainfall_chennai & rainfall_madurai
cetwo = rainfall_coimbatore & rainfall_madurai
total = mtwo | ctwo | cetwo
print(total)





