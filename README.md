# Python Fundamentals Reference

This folder contains `code.py`, a collection of small Python programs for learning the basics. It is a study and practice file, not one large application. Most examples are commented out so that each program can be studied and run separately.

## Run the File

From this directory, run:

```bash
python code.py
```

The active examples run from top to bottom. The last example asks for an employee ID. Enter `102` to find Alice.

To provide the input automatically:

```bash
printf '102\n' | python code.py
```

## How to Study the Programs

1. Open `code.py` and read the section comments.
2. Uncomment one complete example by removing the `#` characters at the beginning of its lines.
3. Run `python code.py` and observe the output.
4. Change the values or input and run it again.
5. Comment the example again before trying the next one if you want to keep the output easy to read.

The examples below follow the same order as the file.

## 1. Variables and User Input

```python
name = "Akarsh"
print("Hello, " + name + "!")

age = input("Please enter your age: ")
print("You are " + age + " years old.")
print(int(age) + 5)
```

`name` stores text. `input()` always returns text, so `int(age)` converts the input into an integer before adding `5`.

## 2. Adding Two Numbers

```python
a = input("Input a number: ")
b = input("Input another number: ")
result = float(a) + float(b)
print("The sum is: " + str(result))
```

`float()` allows decimal numbers. `str()` converts the result back to text for string concatenation.

## 3. String Methods

```python
name = "Tony Stark"
print(name.find("s"))
print(name.replace("Tony", "Iron"))
print("x" in name)
```

- `find()` returns the index of the first match, or `-1` if it is absent.
- `replace()` returns a new string with the replacement applied.
- `in` checks whether a value exists inside the string.

## 4. Product Bill

```python
product1 = float(input("Enter the price of product 1: "))
product2 = float(input("Enter the price of product 2: "))
product3 = float(input("Enter the price of product 3: "))

total_amount = product1 + product2 + product3
average_amount = total_amount / 3
```

This program reads three prices, calculates their total, and divides the total by `3` to find the average.

## 5. Conditional Statements

The active example sets `age = 17`:

```python
if age >= 18:
	print("You are eligible to vote.")

	print("You are eligible for a driving license.")
else:
	print("You are not eligible to vote or drive yet.")
```

Python checks conditions from top to bottom. Only the first matching branch runs. Indentation is required because it defines each branch's code block.

## 6. Simple Calculator

The calculator reads two numbers and an operator such as `+`, `-`, `*`, `/`, `%`, or `**`:

```python
if operator == "+":
	result = value1 + value2
elif operator == "/":
	if value2 != 0:
		result = value1 / value2
	else:
		result = "Error: Division by zero is not allowed."
```

The full version in `code.py` uses an `if`/`elif` chain to choose the calculation and checks for division by zero.

## 7. Ranges and `while` Loops

```python
numbers = range(1, 10, 5)
print(list(numbers))  # [1, 6]

i = 0
while i <= 5:
	print(i)
	i += 1
```

`range(start, stop, step)` includes `start` but excludes `stop`. The `while` loop repeats while its condition is true. `i += 1` is important because it eventually makes the condition false.

## 8. `for` Loops, Odd Numbers, and `continue`

```python
for i in range(1, 21):
	if i % 2 != 0:
		print(i)

for i in range(1, 50):
	if i % 3 == 0:
		if i == 15:
			continue
		print(i)
```

The first loop prints odd numbers. The `%` operator gives the remainder. `continue` skips the current iteration, so `15` is not printed.

## 9. Lists

```python
marks = [90, 80, 70, 60, 50]
print(marks[0])       # first item
print(marks[-1])      # last item
print(marks[1:4])    # indexes 1 through 3

marks.append(100)    # add to the end
marks.insert(2, 75)  # add at index 2
print(80 in marks)   # membership check
print(marks.pop())   # remove and return the last item
```

A list is ordered and mutable, meaning it can be changed after creation. Indexes start at `0`; negative indexes count from the end.

## 10. Tuples

```python
marks = (90, 80, 70, 60, 50)
print(marks.count(80))
```

A tuple is ordered like a list but immutable, so its values cannot be changed after creation. Use a tuple for a fixed collection of values.

## 11. Sets

```python
marks = {90, 80, 70, 60, 50, 95, 95, 95}
print(marks)
print(len(marks))
```

A set stores unique values. The repeated `95` appears only once. Sets are unordered, so their printed order can vary.

## 12. Dictionaries

```python
marks = {"Math": 90, "Science": 80, "English": 70}
print(marks["Math"])

for subject in marks:
	print(subject, marks[subject])
```

A dictionary stores values using keys. Here, subjects are keys and scores are values. Access a value with `dictionary[key]`.

## 13. Remove Duplicate Roll Numbers

```python
roll_numbers = [101, 105, 102, 101, 108, 105, 110]
unique_roll_numbers = set(roll_numbers)
print(unique_roll_numbers)
```

Converting the list to a set removes duplicate roll numbers. The output order is not guaranteed because sets are unordered.

## 14. Search Employee Records

Each record is a tuple containing `(employee_id, employee_name, employee_salary)`:

```python
records = [
	(101, "John", 50000),
	(102, "Alice", 60000),
	(103, "Bob", 55000),
	(104, "Eve", 70000),
]

emp_id = int(input("Enter employee ID to search: "))

for record in records:
	if record[0] == emp_id:
		print("Employee found:", record)
		break
else:
	print("Employee not found.")
```

`record[0]` is the employee ID. `break` stops the loop after a match. The `else` attached to the `for` loop runs only when the loop finishes without using `break`.

Try `102` to find Alice. Try `999` to see the not-found message.

## Core Rules to Remember

- Python uses indentation to define code blocks.
- `input()` returns a string; convert it with `int()` or `float()` when needed.
- `range()` excludes its stop value.
- Lists are mutable; tuples are immutable.
- Sets contain unique values and have no guaranteed display order.
- Dictionaries retrieve values through keys.
- `%` returns a remainder and is useful for even/odd checks.
