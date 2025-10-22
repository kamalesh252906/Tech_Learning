# # Activity 1: Tuples Basics
# Given the tuple: fruits = ("apple", "banana", "cherry", "mango", "banana")

# Address the following:
# Determine the length of the fruits tuple.
# Identify the index of the initial occurrence of "banana".
# Attempt to modify "cherry" to "grape" within the tuple. Explain the outcome and the reason behind it.
# Transform the tuple into a list, make a modification, and then convert it back to a tuple.


fruits = ("apple", "banana", "cherry", "mango", "banana")
print(len(fruits))
print(fruits.index('banana'))
fruits[2] = 'grape'
print(fruits)
# 'tuple' object does not support item assignment . It is a immutable.
lists = list(fruits)
lists[2] = 'grape'
tuples = tuple(lists)
print(tuples)



# # Activity 2: Tuples Grouping
# # Given the following tuples:
# colors = ("red", "green", "blue")
# shapes = ("circle", "square", "triangle")
# Perform the following operations:
# Combine colors and shapes to create a new tuple called art.
# Demonstrate how to repeat a tuple, specifically colors three times.
# Extract and print the middle element from the art tuple using slicing.
# Verify if the string "square" exists within the art tuple.


colors = ("red", "green", "blue")
shapes = ("circle", "square", "triangle")
add = ('Diamond',)
shapes += add
print(shapes)
art = colors + shapes
print(art)
print(colors*3)
middle_index = len(art) // 2
middle_element = art[middle_index : middle_index +1]
print(middle_element)
if 'square' in shapes:
    print('exists')
else:
    print('not exists')


# Activity 3: Tuple Operations

# Given the following list of student marks:

# marks = (78, 85, 69, 90, 85)

# Perform the following operations:
# Determine the highest and lowest marks.
# Count the occurrences of the mark 85.
# Calculate the average marks using the sum() and len() functions.


marks = (78, 85, 69, 90, 85)
high = max(marks)
low = min(marks)
print(high)
print(low)
t = marks.count(85)
print(t)
# another method:
count = 0
for i in marks:
    if i == 85:
        count += 1
print(count)
avg = sum(marks) / len(marks)
print(avg)



# Activity 4: Rainfall Data:

# The monthly_rainfall tuple provides the rainfall in millimeters for each month from January to December:

# monthly_rainfall = (120, 150, 120, 180, 120, 90, 110, 130, 100, 140, 120, 160)

# Calculate the total annual rainfall.
# Determine the average monthly rainfall.
# Identify the month(s) with exactly 120 mm of rainfall. (Hint: Consider using enumerate() or .count().)
# Find the highest and lowest rainfall values recorded.


monthly_rainfall = (120, 150, 120, 180, 120, 90, 110, 130, 100, 140, 120, 160)
print(sum(monthly_rainfall))
print(sum(monthly_rainfall) / len(monthly_rainfall))
# BONUS
monthly = {1:'jan',2:'feb',3:'mar',4:'apr',5:'may',6:'jun',7:'jul',8:'aug',9:'sep',10:'oct',11:'nov',12:'dec'}
months = []
for month, rain in enumerate(monthly_rainfall, start=1):
    if rain == 120:
        months.append(month)
for i in months:
    print(monthly[i])
# normal
count = 0
for i in monthly_rainfall:
    if i == 120:
        count += 1
print(count)

print(max(monthly_rainfall))
print(min(monthly_rainfall))




