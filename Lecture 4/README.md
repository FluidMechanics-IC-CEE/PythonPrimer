# Lecture 4: Matplotlib Fundamentals

Matplotlib is the primary plotting library in Python for creating static, animated, and interactive visualizations. This lecture covers the essential skills for creating professional scientific plots.

## Learning Objectives

By the end of this lecture, you will be able to:
- Create basic line plots, scatter plots, and bar charts
- Customize plot appearance (colors, labels, legends, etc.)
- Create multiple subplots in a single figure
- Plot 2D data using contour plots and heatmaps
- Save plots in different formats
- Apply best practices for scientific visualization

---

## 1. Introduction to Matplotlib

### 1.1 Importing Matplotlib

```python
import matplotlib.pyplot as plt
import numpy as np

# Enable inline plotting in Jupyter notebooks
# %matplotlib inline
```

### 1.2 Basic Plot Structure

Every matplotlib plot has these key components:
- **Figure**: The entire plot window
- **Axes**: The actual plot area where data is displayed
- **Artists**: Everything you see on the plot (lines, text, etc.)

---

## 2. Basic Plotting

### 2.1 Simple Line Plot

```python
# Create data
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

# Create plot
plt.figure(figsize=(8, 6))
plt.plot(x, y)
plt.xlabel('Angle (radians)')
plt.ylabel('sin(x)')
plt.title('Sine Function')
plt.grid(True)
plt.show()
```

### 2.2 Multiple Lines on Same Plot

```python
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='sin(x)', color='blue', linewidth=2)
plt.plot(x, y2, label='cos(x)', color='red', linestyle='--')
plt.xlabel('Angle (radians)')
plt.ylabel('Amplitude')
plt.title('Trigonometric Functions')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

### 2.3 Scatter Plots

```python
# Generate sample data
np.random.seed(42)
x = np.random.normal(0, 1, 50)
y = 2*x + np.random.normal(0, 0.5, 50)

plt.figure(figsize=(8, 6))
plt.scatter(x, y, c='blue', alpha=0.6, s=50)
plt.xlabel('X Variable')
plt.ylabel('Y Variable')
plt.title('Scatter Plot Example')
plt.grid(True, alpha=0.3)
plt.show()
```

---

## 3. Customizing Plots

### 3.1 Colors and Styles

```python
x = np.linspace(0, 10, 50)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(12, 8))

# Different line styles and colors
plt.plot(x, y1, color='#FF6B6B', linestyle='-', linewidth=2, label='sin(x)')
plt.plot(x, y2, color='#4ECDC4', linestyle='--', linewidth=2, label='cos(x)')

# Customizing appearance
plt.xlabel('X values', fontsize=14, fontweight='bold')
plt.ylabel('Y values', fontsize=14, fontweight='bold')
plt.title('Customized Plot', fontsize=16, fontweight='bold')
plt.legend(fontsize=12, loc='upper right')

# Grid customization
plt.grid(True, linestyle=':', alpha=0.7)

# Axis limits
plt.xlim(0, 10)
plt.ylim(-1.5, 1.5)

plt.tight_layout()
plt.show()
```

### 3.2 Color Maps and Markers

```python
# Scatter plot with colormap
x = np.random.randn(100)
y = np.random.randn(100)
colors = np.random.randn(100)

plt.figure(figsize=(10, 8))
scatter = plt.scatter(x, y, c=colors, cmap='viridis', s=60, alpha=0.7)
plt.colorbar(scatter, label='Color Scale')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Scatter Plot with Colormap')
plt.show()
```

---

## 4. Subplots

### 4.1 Basic Subplots

```python
# Create sample data
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.sin(x) * np.cos(x)

# Create subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Top left
axes[0, 0].plot(x, y1, 'b-')
axes[0, 0].set_title('sin(x)')
axes[0, 0].grid(True)

# Top right
axes[0, 1].plot(x, y2, 'r-')
axes[0, 1].set_title('cos(x)')
axes[0, 1].grid(True)

# Bottom left
axes[1, 0].plot(x, y3, 'g-')
axes[1, 0].set_title('tan(x)')
axes[1, 0].set_ylim(-5, 5)
axes[1, 0].grid(True)

# Bottom right
axes[1, 1].plot(x, y4, 'm-')
axes[1, 1].set_title('sin(x)cos(x)')
axes[1, 1].grid(True)

plt.tight_layout()
plt.show()
```

### 4.2 Advanced Subplot Layouts

```python
# Mixed subplot sizes
fig = plt.figure(figsize=(12, 8))

# Create gridspec for custom layout
gs = fig.add_gridspec(2, 3, height_ratios=[2, 1], width_ratios=[1, 2, 1])

# Main plot (spans 2 columns)
ax1 = fig.add_subplot(gs[0, :2])
ax1.plot(x, np.sin(x), 'b-', linewidth=2)
ax1.set_title('Main Plot')
ax1.grid(True)

# Side plot
ax2 = fig.add_subplot(gs[0, 2])
ax2.plot(np.sin(x), x, 'r-')
ax2.set_title('Side')

# Bottom plots
ax3 = fig.add_subplot(gs[1, 0])
ax3.plot(x[:20], np.sin(x[:20]), 'go-')
ax3.set_title('Bottom Left')

ax4 = fig.add_subplot(gs[1, 1:])
ax4.plot(x, np.cos(x), 'orange', linewidth=2)
ax4.set_title('Bottom Right (wide)')

plt.tight_layout()
plt.show()
```

---

## 5. 2D Plotting

### 5.1 Contour Plots

```python
# Create 2D data
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y) * np.exp(-(X**2 + Y**2)/4)

# Contour plot
plt.figure(figsize=(12, 5))

# Filled contour plot
plt.subplot(1, 2, 1)
contour_filled = plt.contourf(X, Y, Z, levels=20, cmap='RdBu_r')
plt.colorbar(contour_filled)
plt.title('Filled Contour Plot')
plt.xlabel('X')
plt.ylabel('Y')

# Line contour plot
plt.subplot(1, 2, 2)
contour_lines = plt.contour(X, Y, Z, levels=15, colors='black', alpha=0.7)
plt.clabel(contour_lines, inline=True, fontsize=8)
plt.contourf(X, Y, Z, levels=20, cmap='RdBu_r', alpha=0.6)
plt.title('Contour Lines with Labels')
plt.xlabel('X')
plt.ylabel('Y')

plt.tight_layout()
plt.show()
```

### 5.2 Heatmaps and 3D Surface Plots

```python
# Heatmap
plt.figure(figsize=(12, 5))

# Simple heatmap
plt.subplot(1, 2, 1)
plt.imshow(Z, extent=[-3, 3, -3, 3], origin='lower', cmap='viridis')
plt.colorbar(label='Value')
plt.title('Heatmap')
plt.xlabel('X')
plt.ylabel('Y')

# 3D surface plot
from mpl_toolkits.mplot3d import Axes3D

plt.subplot(1, 2, 2, projection='3d')
ax = plt.gca()
surface = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
ax.set_title('3D Surface')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.tight_layout()
plt.show()
```

---

## 6. Engineering Applications

### 6.1 Velocity Profile Visualization

```python
def plot_pipe_velocity_profile():
    """Visualize velocity profile in a circular pipe."""
    
    # Create radial coordinates
    r = np.linspace(0, 0.05, 100)  # 5 cm pipe radius
    u_max = 2.0  # Maximum velocity
    R = 0.05     # Pipe radius
    
    # Calculate velocity profile
    u = u_max * (1 - (r/R)**2)
    
    # Create plot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Velocity vs radius plot
    ax1.plot(r*1000, u, 'b-', linewidth=3, label='Velocity Profile')
    ax1.axhline(y=u_max/2, color='r', linestyle='--', 
                label=f'Average Velocity = {u_max/2:.1f} m/s')
    ax1.set_xlabel('Radius (mm)')
    ax1.set_ylabel('Velocity (m/s)')
    ax1.set_title('Pipe Velocity Profile')
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    
    # 2D velocity field visualization
    y = np.linspace(-R, R, 50)
    z = np.linspace(-R, R, 50)
    Y, Z = np.meshgrid(y, z)
    R_field = np.sqrt(Y**2 + Z**2)
    
    # Velocity field (set to 0 outside pipe)
    U_field = np.where(R_field <= R, u_max * (1 - (R_field/R)**2), 0)
    
    im = ax2.imshow(U_field, extent=[-R*1000, R*1000, -R*1000, R*1000], 
                    cmap='jet', origin='lower')
    ax2.set_xlabel('Y (mm)')
    ax2.set_ylabel('Z (mm)')
    ax2.set_title('2D Velocity Field')
    
    # Add circular boundary
    circle = plt.Circle((0, 0), R*1000, fill=False, color='white', linewidth=2)
    ax2.add_patch(circle)
    
    plt.colorbar(im, ax=ax2, label='Velocity (m/s)')
    plt.tight_layout()
    plt.show()

plot_pipe_velocity_profile()
```

### 6.2 Temperature Distribution Analysis

```python
def plot_temperature_analysis():
    """Analyze and visualize temperature data."""
    
    # Generate synthetic temperature data
    np.random.seed(42)
    time = np.linspace(0, 24, 25)  # 24 hours
    temp_outdoor = 15 + 10*np.sin(2*np.pi*time/24) + np.random.normal(0, 2, 25)
    temp_indoor = 20 + 2*np.sin(2*np.pi*time/24 - np.pi/4) + np.random.normal(0, 1, 25)
    
    # Create comprehensive plot
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    
    # Time series plot
    axes[0, 0].plot(time, temp_outdoor, 'o-', color='blue', 
                    label='Outdoor', linewidth=2, markersize=6)
    axes[0, 0].plot(time, temp_indoor, 's-', color='red', 
                    label='Indoor', linewidth=2, markersize=6)
    axes[0, 0].set_xlabel('Time (hours)')
    axes[0, 0].set_ylabel('Temperature (°C)')
    axes[0, 0].set_title('Temperature vs Time')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)
    
    # Histogram
    axes[0, 1].hist(temp_outdoor, bins=8, alpha=0.7, color='blue', 
                    label='Outdoor', density=True)
    axes[0, 1].hist(temp_indoor, bins=8, alpha=0.7, color='red', 
                    label='Indoor', density=True)
    axes[0, 1].set_xlabel('Temperature (°C)')
    axes[0, 1].set_ylabel('Density')
    axes[0, 1].set_title('Temperature Distribution')
    axes[0, 1].legend()
    
    # Scatter plot
    axes[1, 0].scatter(temp_outdoor, temp_indoor, c=time, 
                       cmap='viridis', s=80, alpha=0.7)
    axes[1, 0].set_xlabel('Outdoor Temperature (°C)')
    axes[1, 0].set_ylabel('Indoor Temperature (°C)')
    axes[1, 0].set_title('Indoor vs Outdoor Temperature')
    
    # Add diagonal line
    min_temp = min(min(temp_outdoor), min(temp_indoor))
    max_temp = max(max(temp_outdoor), max(temp_indoor))
    axes[1, 0].plot([min_temp, max_temp], [min_temp, max_temp], 
                    'k--', alpha=0.5, label='Equal Temperature')
    axes[1, 0].legend()
    
    # Box plot
    axes[1, 1].boxplot([temp_outdoor, temp_indoor], 
                       labels=['Outdoor', 'Indoor'])
    axes[1, 1].set_ylabel('Temperature (°C)')
    axes[1, 1].set_title('Temperature Statistics')
    axes[1, 1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    # Print statistics
    print("Temperature Statistics:")
    print(f"Outdoor - Mean: {np.mean(temp_outdoor):.1f}°C, "
          f"Std: {np.std(temp_outdoor):.1f}°C")
    print(f"Indoor  - Mean: {np.mean(temp_indoor):.1f}°C, "
          f"Std: {np.std(temp_indoor):.1f}°C")

plot_temperature_analysis()
```

---

## 7. Saving Plots

### 7.1 Different File Formats

```python
# Create a sample plot
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2)
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Sample Plot for Saving')
plt.grid(True)

# Save in different formats
plt.savefig('plot.png', dpi=300, bbox_inches='tight')     # High-res PNG
plt.savefig('plot.pdf', bbox_inches='tight')              # Vector PDF
plt.savefig('plot.svg', bbox_inches='tight')              # Vector SVG
plt.savefig('plot.eps', bbox_inches='tight')              # Vector EPS

plt.show()
```

---

## Exercise 4: Matplotlib Practice

### Exercise 4.1: Function Visualization
Create a subplot with 4 different mathematical functions:
1. f(x) = x²
2. f(x) = e^x
3. f(x) = ln(x) (for x > 0)
4. f(x) = sin(x)/x

Use different colors and line styles for each, add proper labels and legends.

### Exercise 4.2: Data Analysis Plot
Given experimental data:
```python
time = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
pressure = np.array([101.3, 101.1, 100.8, 100.9, 101.2, 101.5, 101.3, 100.7, 100.9, 101.1, 101.0])
temperature = np.array([20, 22, 24, 23, 21, 19, 18, 20, 22, 21, 20])
```

Create a figure with:
1. Time series plot of pressure and temperature (dual y-axis)
2. Scatter plot showing pressure vs temperature correlation
3. Histogram of pressure measurements

### Exercise 4.3: 2D Field Visualization
Create a 2D temperature field for a heated square plate (0 ≤ x,y ≤ 1):
- Boundary conditions: T = 100°C at x=0, T = 0°C at other boundaries
- Use T(x,y) = 100 * (1-x) as a simple model
- Create both contour plot and 3D surface plot

### Exercise 4.4: Engineering Report Plot
Create a professional figure showing:
1. Velocity profile in a channel flow
2. Proper axis labels with units
3. Title and legend
4. Grid and annotations
5. Save as high-resolution PDF

---

## Key Takeaways

1. **Basic plots** include line plots, scatter plots, and bar charts
2. **Customization** involves colors, line styles, fonts, and layouts
3. **Subplots** allow multiple plots in one figure
4. **2D plotting** uses contour plots, heatmaps, and 3D surfaces
5. **Engineering applications** benefit from clear, professional visualization
6. **File formats** should match intended use (PNG for presentations, PDF for publications)
7. **Best practices** include proper labels, legends, and consistent styling

---

## What's Next?

In **Lecture 5**, we'll cover **Mathematical Concepts and Numerical Methods**:
- Review of calculus concepts
- Introduction to numerical differentiation and integration
- Grid generation techniques
- Error analysis

This will bridge the gap between programming skills and the numerical methods used in computational fluid dynamics!