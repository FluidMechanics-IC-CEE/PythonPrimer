# Lecture 1: Python Basics

Welcome to your first Python lecture! This lecture introduces the fundamental concepts of Python programming for complete beginners.

## Learning Objectives

By the end of this lecture, you will be able to:
- Understand what Python is and why it's useful for scientific computing
- Work with different data types (numbers, strings, booleans)
- Perform basic mathematical operations
- Create and manipulate variables
- Understand Python's basic data structures (lists, tuples, dictionaries)

---

## 1. Introduction to Python

Python is a high-level, interpreted programming language that's particularly well-suited for scientific computing, data analysis, and numerical simulations. It's widely used in computational fluid dynamics and engineering applications because of its:

- **Simplicity**: Easy to read and write
- **Powerful libraries**: NumPy, SciPy, Matplotlib for scientific computing
- **Versatility**: Can be used for many different applications
- **Large community**: Extensive documentation and support

---

## 2. Variables and Data Types

### 2.1 Variables

Variables are containers that store data values. In Python, you don't need to declare the type of variable explicitly.

```python
# Creating variables
name = "Python"
age = 30
height = 5.9
is_student = True
```

### 2.2 Basic Data Types

#### Numbers
```python
# Integers (whole numbers)
count = 10
negative_number = -5

# Floating-point numbers (decimals)
temperature = 25.5
pi = 3.14159

# Scientific notation
large_number = 1.5e6  # 1,500,000
small_number = 2.3e-4  # 0.00023
```

#### Strings
```python
# Strings (text)
message = "Hello, World!"
name = 'Alice'
equation = "F = ma"

# Multi-line strings
description = """
This is a multi-line string
that can span several lines.
"""
```

#### Booleans
```python
# Boolean values (True or False)
is_working = True
is_finished = False
```

---

## 3. Basic Operations

### 3.1 Arithmetic Operations

```python
# Basic arithmetic
a = 10
b = 3

addition = a + b        # 13
subtraction = a - b     # 7
multiplication = a * b  # 30
division = a / b        # 3.333...
floor_division = a // b # 3 (integer division)
remainder = a % b       # 1 (modulo)
power = a ** b          # 1000 (a to the power of b)
```

### 3.2 String Operations

```python
first_name = "John"
last_name = "Doe"

# String concatenation
full_name = first_name + " " + last_name  # "John Doe"

# String repetition
separator = "-" * 10  # "----------"

# String formatting
age = 25
message = f"My name is {full_name} and I am {age} years old."
```

---

## 4. Data Structures

### 4.1 Lists

Lists are ordered collections that can store multiple items.

```python
# Creating lists
numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]
mixed = [1, "hello", 3.14, True]

# Accessing list elements (indexing starts from 0)
first_number = numbers[0]  # 1
last_number = numbers[-1]  # 5

# List slicing
first_three = numbers[0:3]  # [1, 2, 3]
last_two = numbers[-2:]     # [4, 5]

# Modifying lists
numbers.append(6)           # Add element: [1, 2, 3, 4, 5, 6]
numbers.insert(0, 0)        # Insert at position: [0, 1, 2, 3, 4, 5, 6]
numbers.remove(3)           # Remove element: [0, 1, 2, 4, 5, 6]
```

### 4.2 Tuples

Tuples are like lists but immutable (cannot be changed).

```python
# Creating tuples
coordinates = (3.5, 2.1)
rgb_color = (255, 128, 0)

# Accessing tuple elements
x = coordinates[0]  # 3.5
y = coordinates[1]  # 2.1

# Tuple unpacking
x, y = coordinates
```

### 4.3 Dictionaries

Dictionaries store key-value pairs.

```python
# Creating dictionaries
student = {
    "name": "Alice",
    "age": 20,
    "major": "Engineering"
}

# Accessing dictionary values
student_name = student["name"]        # "Alice"
student_age = student.get("age")      # 20

# Modifying dictionaries
student["grade"] = "A"                # Add new key-value pair
student["age"] = 21                   # Update existing value

# Dictionary keys and values
keys = student.keys()                 # dict_keys(['name', 'age', 'major', 'grade'])
values = student.values()             # dict_values(['Alice', 21, 'Engineering', 'A'])
```

---

## 5. Basic Input and Output

### 5.1 Printing Output

```python
# Basic printing
print("Hello, World!")
print("The value of x is:", 42)

# Formatted printing
name = "Alice"
score = 95.5
print(f"Student {name} scored {score}%")
```

### 5.2 Getting User Input

```python
# Getting input from user
name = input("Enter your name: ")
age_str = input("Enter your age: ")
age = int(age_str)  # Convert string to integer

print(f"Hello {name}, you are {age} years old.")
```

---

## Exercise 1: Basic Python Operations

Try to solve these exercises to practice what you've learned:

### Exercise 1.1: Variables and Calculations
Create variables for the following physical quantities and perform calculations:
- Density of water: 1000 kg/m³
- Volume of a container: 0.5 m³
- Calculate the mass of water in the container (mass = density × volume)
- Print the result with appropriate units

### Exercise 1.2: Temperature Conversion
Write code to convert temperature from Celsius to Fahrenheit and Kelvin:
- Formula: F = (C × 9/5) + 32
- Formula: K = C + 273.15
- Test with a temperature of 25°C

### Exercise 1.3: List Operations
Create a list of velocity measurements: [2.5, 3.1, 2.8, 3.4, 2.9, 3.2]
- Calculate the number of measurements
- Find the maximum and minimum velocities
- Calculate the average velocity (hint: use sum() and len())

### Exercise 1.4: Student Information
Create a dictionary containing information about a student:
- Name, age, course, grades for 3 subjects
- Calculate and add the average grade to the dictionary
- Print a formatted summary of the student information

---

## Key Takeaways

1. **Variables** store data and don't require type declaration in Python
2. **Data types** include numbers (int, float), strings, and booleans
3. **Lists** are ordered, mutable collections
4. **Tuples** are ordered, immutable collections
5. **Dictionaries** store key-value pairs
6. **String formatting** with f-strings is powerful and readable
7. **Indexing** starts from 0 in Python

---

## What's Next?

In **Lecture 2**, we'll learn about:
- Conditional statements (if/else)
- Loops (for/while)
- Functions
- Error handling basics

These control structures will allow you to write more complex and powerful programs!