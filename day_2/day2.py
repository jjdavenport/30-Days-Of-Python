import math

# Day 2: 30 Days of python programming

first_name = "John"
last_name = "Smith"
full_name = "John Smith"
country = "UK"
city = "London"
age = 29
year = 2025
is_married = False
is_true = True
is_light_on = True
multiple, same_line = True, True

# Level 2

vars = [first_name, last_name, full_name, country, city, age, year, is_married, is_true, is_light_on, multiple, same_line ]

for i in vars:
    print(type(i))

print(len(first_name), len(last_name))

num_one = 5
num_two = 4
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one //  num_two
radius = 30
pi = math.pi
area_of_circle = pi * radius**2
circum_of_circle = 2 * pi * radius
float(input("Enter Radius:"))
print(f"Area is: {area_of_circle}")

var_names = ["First name" , "last Name", "Country", "Age"]
vars2 = [first_name, last_name, country, age]

for i, var_name in enumerate(var_names):
    vars2[i] = input(f"Enter {var_name}: ")
    first_name, last_name, country, age = vars2

print(f"First name: {first_name}, last name: {last_name}, Country: {country}, age: {age}")

help('keywords')


    





