"""Python fundamentals reference examples.

This file is an executable collection of small examples rather than a single
application. Uncomment one of the commented examples to experiment with it.

Topics covered:
    - Variables, input, type conversion, and strings
    - Arithmetic and a simple calculator
    - Conditional statements
    - ``range``, ``while`` loops, ``for`` loops, ``break``, and ``continue``
    - Lists, tuples, sets, and dictionaries
    - Searching a list of employee records

Running the file executes the active examples from top to bottom. The final
example asks for an employee ID, so it requires user input.
"""


# Variables, input, and type conversion
# name = "Akarsh"
# print("Hello, " + name + "! Welcome to the program.")
# print(type(name))
# age = input("Please enter your age: ")
# print("You are " + age + " years old.")
# print(int(age) + 5) 



# Adding two numbers

# result = 0
# a = input ("Input a numer: ")
# b = input ("Input another number: ")
# result = float(a) + float(b)
# print("The sum of " + a + " and " + b + " is: " + str(result))


# name = "Tony stark"
# print(name.find("s"))  # returns the index of the first occurrence of "s"
# print(name.replace("Tony", "Iron"))  # replaces "Tony" with "Iron"
# print("x" in name )


# Read three product prices and calculate the total and average.

# product1 = float(input("Enter the price of product 1: "))
# product2 = float(input("Enter the price of product 2: "))
# product3 = float(input("Enter the price of product 3: "))

# total_amount = product1 + product2 + product3
# average_amount = total_amount / 3

# print("Total bill amount: $" + str(total_amount))
# print("Average amount: $" + str(average_amount))



# Conditional statements: indentation defines each code block.

age = 17 

if age >= 18:
    print("You are eligible to vote.")
elif age >= 16:
    print("You are eligible for a driving license.")
else:
    print("You are not eligible to vote or drive yet.")

print("Outside the conditional block")



# Simple calculator program

# value1 = float(input("Enter the first number: "))
# value2 = float(input("Enter the second number: "))
# operator = input("Enter the operator (+, -, *, /): ")

# result = None

# if operator == "+":
#     result = value1 + value2
# elif operator == "-":
#     result = value1 - value2
# elif operator == "*":
#     result = value1 * value2
# elif operator == "/":
#     if value2 != 0:
#         result = value1 / value2
#     else:
#         result = "Error: Division by zero is not allowed."
# elif operator == "%":
#     if value2 != 0:
#         result = value1 % value2
#     else:
#         result = "Error: Division by zero is not allowed."
# elif operator == "**":
#     result = value1 ** value2
# else:
#     result = "Error: Invalid operator."

# print(result)


# Ranges and loops

num = range(1, 10, 5)  # generates 1, then 6; the stop value is exclusive
print(list(num))  # convert the range to a list before printing it

i = 0
while i <=5:
    print(i)
    i += 1

# for loops

range1 = range(1,11)
# even numbers from 1 to 10

# for i in range1:
#     if i%2 == 0:
#         print("even number is :" + str(i))
#     else:
#         print("odd number: " + str(i))

# multiples of 3 [1 to 50] => stop when we get 21 if we use continue insted of break then it will skip 21 and continue to print the multiples of 3

# for i in range(1,51):
#      if(i%3 ==0):
#          print("multiple of 3 is: " + str(i))
#      if(i == 21):
#         continue



# Print all oddd numbers from 1 to 20;

# print the table of 57

# print all multipled of 3 from 1 to 50 but skip 15



for i in range(1, 21):
    if i%2 != 0:
        print("the odd numbers are:" + str(i))


for i in range(1,50):
    if i%3 == 0:
        if i == 15:
            continue
        print("multiple of 3 is: " + str(i))



# Lists are mutable, ordered collections defined with square brackets.
# They can contain values of different data types.

marks = [90, 80, 70, 60, 50]
print(marks[0])  # prints the first element of the list
print(len(marks))  # prints the length of the list
print(marks[0])  
print(marks[-1])  # prints the last element of the list

#slicing a list - list[start:end] - returns a new list containing elements from index start to end-1

print(marks[1:4])  # prints elements from index 1 to 3


for score in marks:
    print(score)  # prints each element of the list

marks.append(100)  # adds an element to the end of the list


marks.insert(2, 75)  # inserts an element at index 2
print(marks)

print(80 in marks)  # checks if 80 is in the list and returns True or False

print(marks.pop())  # removes and returns the last element of the list
print(marks)

# marks.clear()  # removes all elements from the list?
print(marks.count(80))  # counts the number of occurrences of 80 in the list


# Tuples are immutable, ordered collections defined with parentheses.


marks = (90, 80, 70, 60, 50)
print('This is tuples',marks)

print(marks.count(80))  # prints the first element of the tuple



# Sets are unordered collections that keep only unique values.

marks = {90, 80, 70, 60, 50,95,95,95}
print('This is a set',marks)
print(len(marks))  # prints the length of the set only unique


# Dictionaries store values by key. They are mutable and preserve insertion
# order in modern Python. They are defined with curly braces.

marks = {"Math": 90, "Science": 80, "English": 70}
print('This is a dictionary',marks)
print(marks["Math"] )  # prints the value associated with the key "Math"

for key in marks:
    print(key, marks[key])  # prints each key-value pair in the dictionary




# Practice problem: remove duplicate roll numbers with a set.

# Given a a list of roll numbers: [101,105,102,101,108,105,110] print all the unique roll numbers in the list.



roll_numbers = [101, 105, 102, 101, 108, 105, 110]
unique_roll_numbers = set(roll_numbers)  # convert the list to a set to get unique values
print("Unique roll numbers:", unique_roll_numbers)  # print the unique roll numbers


# Employee records are tuples of:
# (employee_id, employee_name, employee_salary)
records =[
    (101, "John", 50000),
     (102, "Alice", 60000), 
     (103, "Bob", 55000), 
     (104, "Eve", 70000)
]

# Ask for an employee ID and search every record until it is found.


emp_id = int(input("Enter employee ID to search: "))

for record in records:
    if record[0] == emp_id:
        print("Employee found:", record)
        break
else:
    # A for-else block runs its else clause only when the loop never breaks.
    print("Employee not found.")

