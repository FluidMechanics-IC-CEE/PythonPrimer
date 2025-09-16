# Lecture 2: Control Structures

This lecture covers the fundamental control structures in Python that allow you to create more complex and interactive programs.

## Learning Objectives

By the end of this lecture, you will be able to:
- Use conditional statements (if, elif, else) to make decisions in your code
- Implement loops (for and while) to repeat operations
- Create and use functions to organize your code
- Handle basic errors in your programs
- Apply these concepts to solve engineering problems

---

## 1. Conditional Statements

Conditional statements allow your program to make decisions based on different conditions.

### 1.1 Basic if Statement

```python
temperature = 25

if temperature > 20:
    print("It's warm today!")
```

### 1.2 if-else Statement

```python
velocity = 15

if velocity > 10:
    print("High velocity flow")
else:
    print("Low velocity flow")
```

### 1.3 if-elif-else Statement

```python
pressure = 101325  # Pa (atmospheric pressure)

if pressure < 101325:
    print("Low pressure")
elif pressure == 101325:
    print("Atmospheric pressure")
else:
    print("High pressure")
```

### 1.4 Comparison Operators

```python
# Comparison operators
a = 10
b = 5

# Equal to
result = (a == b)    # False

# Not equal to
result = (a != b)    # True

# Greater than / less than
result = (a > b)     # True
result = (a < b)     # False

# Greater than or equal to / less than or equal to
result = (a >= b)    # True
result = (a <= b)    # False
```

### 1.5 Logical Operators

```python
temperature = 25
humidity = 60

# AND operator
if temperature > 20 and humidity < 70:
    print("Comfortable conditions")

# OR operator
if temperature > 30 or humidity > 80:
    print("Uncomfortable conditions")

# NOT operator
is_raining = False
if not is_raining:
    print("Good weather for outdoor activities")
```

---

## 2. Loops

Loops allow you to repeat blocks of code multiple times.

### 2.1 For Loops

For loops are used when you know how many times you want to repeat something.

```python
# Simple for loop with range
for i in range(5):
    print(f"Iteration {i}")

# For loop with start, stop, and step
for i in range(2, 10, 2):  # Start at 2, stop before 10, step by 2
    print(f"Even number: {i}")

# Looping through a list
velocities = [2.5, 3.1, 2.8, 3.4, 2.9]
for velocity in velocities:
    print(f"Velocity: {velocity} m/s")

# Looping with index
for i, velocity in enumerate(velocities):
    print(f"Measurement {i+1}: {velocity} m/s")
```

### 2.2 While Loops

While loops continue as long as a condition is true.

```python
# Simple while loop
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1  # Increment count by 1

# While loop for convergence
error = 1.0
tolerance = 0.01
iteration = 0

while error > tolerance:
    # Simulate some calculation that reduces error
    error = error * 0.8
    iteration += 1
    print(f"Iteration {iteration}: Error = {error:.4f}")

print(f"Converged after {iteration} iterations")
```

### 2.3 Loop Control

```python
# Break statement - exits the loop
for i in range(10):
    if i == 5:
        break
    print(i)  # Prints 0, 1, 2, 3, 4

# Continue statement - skips to next iteration
for i in range(10):
    if i % 2 == 0:  # Skip even numbers
        continue
    print(i)  # Prints 1, 3, 5, 7, 9
```

---

## 3. Functions

Functions help organize your code and make it reusable.

### 3.1 Basic Function Definition

```python
def greet():
    """A simple function that prints a greeting."""
    print("Hello, World!")

# Call the function
greet()
```

### 3.2 Functions with Parameters

```python
def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    area = length * width
    return area

# Call the function with arguments
room_area = calculate_area(5.0, 3.0)
print(f"Room area: {room_area} m²")
```

### 3.3 Functions with Default Parameters

```python
def calculate_volume(length, width, height=1.0):
    """Calculate volume with default height of 1.0."""
    volume = length * width * height
    return volume

# Call with and without the optional parameter
area = calculate_volume(5.0, 3.0)        # Uses default height=1.0
volume = calculate_volume(5.0, 3.0, 2.5) # Uses height=2.5
```

### 3.4 Multiple Return Values

```python
def analyze_flow(velocity, diameter):
    """Analyze flow characteristics."""
    area = 3.14159 * (diameter/2)**2
    flow_rate = velocity * area
    
    # Reynolds number calculation (simplified)
    reynolds = velocity * diameter / 1e-6  # Assuming kinematic viscosity = 1e-6
    
    return flow_rate, reynolds

# Unpack multiple return values
q, re = analyze_flow(2.5, 0.1)
print(f"Flow rate: {q:.4f} m³/s")
print(f"Reynolds number: {re:.0f}")
```

### 3.5 Documentation Strings (Docstrings)

```python
def convert_temperature(celsius):
    """
    Convert temperature from Celsius to Fahrenheit and Kelvin.
    
    Parameters:
    celsius (float): Temperature in Celsius
    
    Returns:
    tuple: (fahrenheit, kelvin) temperatures
    """
    fahrenheit = celsius * 9/5 + 32
    kelvin = celsius + 273.15
    return fahrenheit, kelvin

# Using the function
f, k = convert_temperature(25)
print(f"25°C = {f}°F = {k}K")
```

---

## 4. Error Handling

Basic error handling helps make your programs more robust.

### 4.1 Try-Except Blocks

```python
def safe_division(a, b):
    """Safely divide two numbers."""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None

# Test the function
result1 = safe_division(10, 2)  # Works fine
result2 = safe_division(10, 0)  # Handles the error
```

### 4.2 Input Validation

```python
def get_positive_number(prompt):
    """Get a positive number from user input."""
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")

# Usage
# velocity = get_positive_number("Enter velocity (m/s): ")
```

---

## 5. Combining Concepts: Engineering Examples

### 5.1 Flow Classification Function

```python
def classify_flow(velocity, diameter, kinematic_viscosity=1e-6):
    """
    Classify fluid flow based on Reynolds number.
    
    Parameters:
    velocity (float): Flow velocity in m/s
    diameter (float): Pipe diameter in m
    kinematic_viscosity (float): Kinematic viscosity in m²/s
    
    Returns:
    str: Flow classification
    """
    reynolds = velocity * diameter / kinematic_viscosity
    
    if reynolds < 2300:
        classification = "Laminar"
    elif reynolds < 4000:
        classification = "Transitional"
    else:
        classification = "Turbulent"
    
    return reynolds, classification

# Test the function
velocities = [0.5, 1.0, 2.0, 5.0]
diameter = 0.05  # 5 cm pipe

for v in velocities:
    re, flow_type = classify_flow(v, diameter)
    print(f"Velocity: {v} m/s → Re = {re:.0f} → {flow_type} flow")
```

### 5.2 Numerical Integration Using Loops

```python
def integrate_function(func, a, b, n=1000):
    """
    Integrate a function using the trapezoidal rule.
    
    Parameters:
    func: Function to integrate
    a (float): Lower bound
    b (float): Upper bound
    n (int): Number of intervals
    
    Returns:
    float: Approximate integral value
    """
    dx = (b - a) / n
    total = 0.0
    
    for i in range(n + 1):
        x = a + i * dx
        
        if i == 0 or i == n:
            # First and last points get weight 1/2
            weight = 0.5
        else:
            # Middle points get weight 1
            weight = 1.0
            
        total += weight * func(x)
    
    return total * dx

# Example: integrate sin(x) from 0 to π
import math

def sine_function(x):
    return math.sin(x)

result = integrate_function(sine_function, 0, math.pi)
print(f"Integral of sin(x) from 0 to π: {result:.6f}")
print(f"Analytical result: {2:.6f}")
```

---

## Exercise 2: Control Structures Practice

### Exercise 2.1: Temperature Analysis
Write a program that:
1. Takes a list of daily temperatures
2. Classifies each day as "Cold" (< 10°C), "Mild" (10-25°C), or "Hot" (> 25°C)
3. Counts how many days fall into each category
4. Calculates the average temperature

### Exercise 2.2: Velocity Profile
Create a function that calculates the velocity profile in a pipe using the equation:
```
u(r) = u_max * (1 - (r/R)²)
```
Where:
- u(r) is velocity at radius r
- u_max is maximum velocity at center
- R is pipe radius

Test your function with different values and plot the results (if you know matplotlib).

### Exercise 2.3: Convergence Analysis
Write a program that:
1. Implements an iterative calculation (e.g., square root using Newton's method)
2. Continues until the error is below a specified tolerance
3. Counts the number of iterations required
4. Prints the convergence history

### Exercise 2.4: Data Validation
Create a function that validates experimental data:
1. Checks if all values are positive (for velocity measurements)
2. Identifies outliers (values more than 2 standard deviations from mean)
3. Returns cleaned data and a report of issues found

---

## Key Takeaways

1. **Conditional statements** (if/elif/else) control program flow based on conditions
2. **For loops** are ideal when you know the number of iterations
3. **While loops** continue until a condition becomes false
4. **Functions** organize code and make it reusable
5. **Error handling** with try-except makes programs more robust
6. **Documentation** with docstrings helps others understand your code
7. **Combining concepts** allows you to solve complex engineering problems

---

## What's Next?

In **Lecture 3**, we'll dive into **NumPy fundamentals**:
- Creating and manipulating arrays
- Mathematical operations on arrays
- Indexing and slicing
- Broadcasting

NumPy is the foundation for all scientific computing in Python, so this will be a crucial step toward solving numerical problems in fluid mechanics!