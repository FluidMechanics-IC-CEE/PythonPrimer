# Lecture 3: NumPy Fundamentals

NumPy (Numerical Python) is the foundation of scientific computing in Python. This lecture introduces the essential concepts you need to work with numerical data efficiently.

## Learning Objectives

By the end of this lecture, you will be able to:
- Understand what NumPy arrays are and why they're important
- Create arrays using various methods
- Perform mathematical operations on arrays
- Use indexing and slicing to access array elements
- Understand broadcasting and vectorization
- Apply NumPy to solve basic engineering problems

---

## 1. Introduction to NumPy

### 1.1 Why NumPy?

NumPy provides:
- **Efficient storage**: Arrays use less memory than Python lists
- **Fast operations**: Mathematical operations are implemented in C
- **Broadcasting**: Operations between arrays of different shapes
- **Foundation**: Other scientific libraries (SciPy, Matplotlib) build on NumPy

### 1.2 Installing and Importing NumPy

```python
# Install NumPy (run in terminal/command prompt)
# pip install numpy

# Import NumPy
import numpy as np
```

---

## 2. Creating NumPy Arrays

### 2.1 From Python Lists

```python
import numpy as np

# 1D array from list
velocities = np.array([2.5, 3.1, 2.8, 3.4, 2.9])
print(f"Velocities: {velocities}")
print(f"Type: {type(velocities)}")

# 2D array from nested lists
pressure_field = np.array([[101.3, 101.1, 100.9],
                          [101.5, 101.2, 101.0],
                          [101.7, 101.4, 101.2]])
print(f"Pressure field shape: {pressure_field.shape}")
```

### 2.2 Using NumPy Functions

```python
# Array of zeros
zeros_array = np.zeros(5)                    # 1D array of 5 zeros
zeros_2d = np.zeros((3, 4))                  # 3x4 array of zeros

# Array of ones
ones_array = np.ones(5)                      # 1D array of 5 ones
ones_2d = np.ones((2, 3))                    # 2x3 array of ones

# Array with specific value
full_array = np.full((3, 3), 3.14)          # 3x3 array filled with π

# Identity matrix
identity = np.eye(3)                         # 3x3 identity matrix

# Arrays with ranges
linear_space = np.linspace(0, 10, 11)       # 11 points from 0 to 10
arange_array = np.arange(0, 10, 0.5)        # From 0 to 10, step 0.5

# Random arrays
random_array = np.random.random(5)          # 5 random numbers [0, 1)
normal_array = np.random.normal(0, 1, 10)   # 10 numbers from normal distribution
```

### 2.3 Array Properties

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

print(f"Shape: {arr.shape}")        # (2, 3) - 2 rows, 3 columns
print(f"Size: {arr.size}")          # 6 - total number of elements
print(f"Dimensions: {arr.ndim}")    # 2 - number of dimensions
print(f"Data type: {arr.dtype}")    # int64 or int32 (depends on system)
```

---

## 3. Array Indexing and Slicing

### 3.1 Basic Indexing

```python
# 1D array indexing
velocities = np.array([2.5, 3.1, 2.8, 3.4, 2.9])

first_velocity = velocities[0]      # 2.5
last_velocity = velocities[-1]     # 2.9
middle_velocity = velocities[2]     # 2.8

# 2D array indexing
pressure = np.array([[101.3, 101.1, 100.9],
                    [101.5, 101.2, 101.0]])

element = pressure[0, 1]            # 101.1 (row 0, column 1)
first_row = pressure[0, :]          # [101.3, 101.1, 100.9]
first_column = pressure[:, 0]       # [101.3, 101.5]
```

### 3.2 Array Slicing

```python
# 1D slicing
arr = np.arange(10)                 # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

first_five = arr[:5]                # [0, 1, 2, 3, 4]
last_three = arr[-3:]               # [7, 8, 9]
every_second = arr[::2]             # [0, 2, 4, 6, 8]
middle_elements = arr[3:7]          # [3, 4, 5, 6]

# 2D slicing
matrix = np.arange(12).reshape(3, 4)  # 3x4 matrix
print(matrix)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

submatrix = matrix[1:3, 1:3]        # Extract 2x2 submatrix
print(submatrix)
# [[ 5  6]
#  [ 9 10]]
```

### 3.3 Boolean Indexing

```python
temperatures = np.array([15, 22, 18, 25, 12, 28, 20])

# Create boolean mask
hot_days = temperatures > 20        # [False, True, False, True, False, True, False]

# Use mask to filter data
hot_temperatures = temperatures[hot_days]  # [22, 25, 28]

# Combined conditions
comfortable = (temperatures >= 18) & (temperatures <= 25)
comfortable_temps = temperatures[comfortable]  # [22, 18, 25, 20]
```

---

## 4. Mathematical Operations

### 4.1 Element-wise Operations

```python
# Basic arithmetic operations
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

addition = a + b        # [ 6  8 10 12]
subtraction = a - b     # [-4 -4 -4 -4]
multiplication = a * b  # [ 5 12 21 32]
division = a / b        # [0.2 0.33 0.43 0.5]
power = a ** 2          # [ 1  4  9 16]

# Operations with scalars
scaled = a * 2          # [2 4 6 8]
shifted = a + 10        # [11 12 13 14]
```

### 4.2 Mathematical Functions

```python
# Trigonometric functions
angles = np.array([0, np.pi/4, np.pi/2, np.pi])
sines = np.sin(angles)
cosines = np.cos(angles)

# Exponential and logarithmic
values = np.array([1, 2, 3, 4])
exponentials = np.exp(values)
logarithms = np.log(values)
square_roots = np.sqrt(values)

# Rounding functions
decimals = np.array([1.2, 2.7, 3.1, 4.9])
rounded = np.round(decimals)        # [1. 3. 3. 5.]
floored = np.floor(decimals)        # [1. 2. 3. 4.]
ceiled = np.ceil(decimals)          # [2. 3. 4. 5.]
```

### 4.3 Aggregate Functions

```python
data = np.array([2.5, 3.1, 2.8, 3.4, 2.9, 1.8, 4.2])

# Statistical functions
mean_value = np.mean(data)          # Average
median_value = np.median(data)      # Median
std_dev = np.std(data)              # Standard deviation
variance = np.var(data)             # Variance

# Min/max functions
minimum = np.min(data)              # Minimum value
maximum = np.max(data)              # Maximum value
min_index = np.argmin(data)         # Index of minimum
max_index = np.argmax(data)         # Index of maximum

# Sum and product
total = np.sum(data)                # Sum of all elements
cumsum = np.cumsum(data)            # Cumulative sum
product = np.prod(data)             # Product of all elements

print(f"Mean: {mean_value:.2f}")
print(f"Std Dev: {std_dev:.2f}")
print(f"Range: {minimum:.1f} to {maximum:.1f}")
```

---

## 5. Array Reshaping and Manipulation

### 5.1 Changing Array Shape

```python
# Create 1D array
arr_1d = np.arange(12)              # [0, 1, 2, ..., 11]

# Reshape to 2D
arr_2d = arr_1d.reshape(3, 4)       # 3x4 matrix
arr_2d_alt = arr_1d.reshape(4, 3)   # 4x3 matrix

# Reshape to 3D
arr_3d = arr_1d.reshape(2, 2, 3)    # 2x2x3 array

# Flatten back to 1D
flattened = arr_2d.flatten()        # Back to 1D array
raveled = arr_2d.ravel()            # Also flattens (but may share memory)
```

### 5.2 Joining and Splitting Arrays

```python
# Joining arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Concatenate along axis
concatenated = np.concatenate([a, b])           # [1, 2, 3, 4, 5, 6]

# Stack arrays
stacked_vertical = np.vstack([a, b])            # 2x3 array
stacked_horizontal = np.hstack([a, b])          # [1, 2, 3, 4, 5, 6]

# Splitting arrays
arr = np.arange(9)
split_arrays = np.split(arr, 3)                 # Split into 3 equal parts
```

---

## 6. Broadcasting

Broadcasting allows operations between arrays of different shapes.

```python
# Example 1: Array and scalar
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
result = arr + 10               # Adds 10 to every element

# Example 2: Different shaped arrays
a = np.array([[1],
              [2],
              [3]])             # 3x1 array

b = np.array([10, 20, 30])      # 1x3 array

result = a + b                  # Broadcasting creates 3x3 result
print(result)
# [[11 21 31]
#  [12 22 32]
#  [13 23 33]]

# Example 3: Velocity field calculation
x = np.linspace(0, 1, 5).reshape(5, 1)  # 5x1 array
y = np.linspace(0, 1, 4).reshape(1, 4)  # 1x4 array

# Calculate distance from origin for each point
distance = np.sqrt(x**2 + y**2)         # Broadcasting creates 5x4 array
```

---

## 7. Engineering Applications

### 7.1 Velocity Profile in a Pipe

```python
def pipe_velocity_profile(r_max, u_max, n_points=100):
    """
    Calculate velocity profile in a circular pipe.
    
    u(r) = u_max * (1 - (r/r_max)^2)
    """
    r = np.linspace(0, r_max, n_points)
    u = u_max * (1 - (r/r_max)**2)
    return r, u

# Example usage
radius_max = 0.05  # 5 cm pipe radius
velocity_max = 2.0  # 2 m/s maximum velocity

r, u = pipe_velocity_profile(radius_max, velocity_max)
average_velocity = np.mean(u)

print(f"Maximum velocity: {velocity_max:.1f} m/s")
print(f"Average velocity: {average_velocity:.2f} m/s")
print(f"Theoretical average: {velocity_max/2:.1f} m/s")
```

### 7.2 Temperature Distribution

```python
def temperature_distribution_1d(length, T_left, T_right, n_points=50):
    """
    Linear temperature distribution along a rod.
    """
    x = np.linspace(0, length, n_points)
    T = T_left + (T_right - T_left) * x / length
    return x, T

# Example: temperature distribution in a 1-meter rod
x, T = temperature_distribution_1d(1.0, 100, 20, 21)  # 100°C to 20°C

print(f"Temperature at x=0: {T[0]:.1f}°C")
print(f"Temperature at x=0.5m: {T[10]:.1f}°C")
print(f"Temperature at x=1m: {T[-1]:.1f}°C")
```

### 7.3 Grid Generation

```python
def create_2d_grid(x_range, y_range, nx, ny):
    """
    Create a 2D computational grid.
    """
    x = np.linspace(x_range[0], x_range[1], nx)
    y = np.linspace(y_range[0], y_range[1], ny)
    X, Y = np.meshgrid(x, y)
    return X, Y

# Create a 10x8 grid
X, Y = create_2d_grid([0, 2], [0, 1], 10, 8)

print(f"Grid shape: {X.shape}")
print(f"X range: {X.min():.1f} to {X.max():.1f}")
print(f"Y range: {Y.min():.1f} to {Y.max():.1f}")

# Calculate distance from origin for each grid point
distance_field = np.sqrt(X**2 + Y**2)
```

---

## Exercise 3: NumPy Practice

### Exercise 3.1: Array Creation and Manipulation
1. Create a 1D array of 20 equally spaced points from 0 to 2π
2. Calculate sin and cos of these points
3. Create a 2D array by stacking sin and cos vertically
4. Find the maximum and minimum values in each row

### Exercise 3.2: Velocity Field Analysis
Given velocity measurements at different positions:
```python
positions = np.array([0.1, 0.2, 0.3, 0.4, 0.5])  # meters
velocities = np.array([2.1, 2.8, 3.2, 2.9, 2.3])  # m/s
```
1. Calculate the average velocity
2. Find positions where velocity > 2.5 m/s
3. Calculate the velocity gradient (hint: use np.gradient())
4. Normalize velocities to range [0, 1]

### Exercise 3.3: Temperature Field
Create a 2D temperature field for a heated plate:
1. Create a 10x10 grid with coordinates from 0 to 1
2. Set boundary conditions: T=100°C on left edge, T=0°C on other edges
3. Calculate the distance from the center for each point
4. Find the average temperature in the field

### Exercise 3.4: Reynolds Number Calculation
For a set of flow conditions:
```python
velocities = np.array([0.5, 1.0, 1.5, 2.0, 2.5])  # m/s
diameters = np.array([0.01, 0.02, 0.05, 0.1])     # m
```
1. Use broadcasting to calculate Reynolds number for all combinations
2. Classify each flow as laminar (Re < 2300) or turbulent (Re > 4000)
3. Create a 2D array showing the flow type for each combination

---

## Key Takeaways

1. **NumPy arrays** are more efficient than Python lists for numerical data
2. **Array creation** can be done from lists or using NumPy functions
3. **Indexing and slicing** work similarly to Python lists but extend to multiple dimensions
4. **Mathematical operations** are element-wise by default
5. **Broadcasting** allows operations between arrays of different shapes
6. **Aggregate functions** provide statistical analysis capabilities
7. **Reshape and manipulation** functions provide flexibility in data organization

---

## What's Next?

In **Lecture 4**, we'll learn about **Matplotlib fundamentals**:
- Creating basic plots
- Customizing plot appearance
- Multiple subplots
- Plotting 2D data and contours

Visualization is crucial for understanding numerical results and communicating findings effectively!