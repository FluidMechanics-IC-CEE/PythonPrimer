# Lecture 5: Mathematical Concepts and Numerical Methods

This lecture bridges the gap between programming fundamentals and computational fluid dynamics by covering essential mathematical concepts and introducing basic numerical methods.

## Learning Objectives

By the end of this lecture, you will be able to:
- Understand key calculus concepts relevant to fluid mechanics
- Implement numerical differentiation and integration methods
- Generate computational grids for solving PDEs
- Analyze numerical errors and convergence
- Apply finite difference methods to simple problems
- Prepare for advanced computational fluid dynamics topics

---

## 1. Mathematical Foundation Review

### 1.1 Vectors and Fields

In computational fluid dynamics, we work with scalar and vector fields:

```python
import numpy as np
import matplotlib.pyplot as plt

# Scalar field example: temperature T(x,y)
x = np.linspace(0, 1, 50)
y = np.linspace(0, 1, 50)
X, Y = np.meshgrid(x, y)

# Temperature field with heat source at center
T = 100 * np.exp(-((X-0.5)**2 + (Y-0.5)**2) / 0.1)

# Vector field example: velocity field u(x,y), v(x,y)
u = -2 * (Y - 0.5)  # x-component
v = 2 * (X - 0.5)   # y-component

# Visualization
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Scalar field
im1 = ax1.contourf(X, Y, T, levels=20, cmap='hot')
ax1.set_title('Scalar Field: Temperature')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
plt.colorbar(im1, ax=ax1, label='Temperature (°C)')

# Vector field
ax2.quiver(X[::5, ::5], Y[::5, ::5], u[::5, ::5], v[::5, ::5], 
           scale=10, alpha=0.7)
ax2.set_title('Vector Field: Velocity')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_aspect('equal')

plt.tight_layout()
plt.show()
```

### 1.2 Partial Derivatives

Partial derivatives are fundamental in fluid mechanics equations:

```python
def calculate_gradients(field, dx, dy):
    """Calculate gradients of a 2D field using finite differences."""
    
    # Initialize gradient arrays
    dfield_dx = np.zeros_like(field)
    dfield_dy = np.zeros_like(field)
    
    # Central differences for interior points
    dfield_dx[1:-1, 1:-1] = (field[1:-1, 2:] - field[1:-1, :-2]) / (2*dx)
    dfield_dy[1:-1, 1:-1] = (field[2:, 1:-1] - field[:-2, 1:-1]) / (2*dy)
    
    # Forward/backward differences for boundaries
    dfield_dx[0, :] = (field[1, :] - field[0, :]) / dx
    dfield_dx[-1, :] = (field[-1, :] - field[-2, :]) / dx
    dfield_dy[:, 0] = (field[:, 1] - field[:, 0]) / dy
    dfield_dy[:, -1] = (field[:, -1] - field[:, -2]) / dy
    
    return dfield_dx, dfield_dy

# Example: Calculate temperature gradients
dx = x[1] - x[0]
dy = y[1] - y[0]
dT_dx, dT_dy = calculate_gradients(T, dx, dy)

# Magnitude of gradient
grad_magnitude = np.sqrt(dT_dx**2 + dT_dy**2)

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.contourf(X, Y, dT_dx, levels=20, cmap='RdBu_r')
plt.title('∂T/∂x')
plt.colorbar()

plt.subplot(1, 3, 2)
plt.contourf(X, Y, dT_dy, levels=20, cmap='RdBu_r')
plt.title('∂T/∂y')
plt.colorbar()

plt.subplot(1, 3, 3)
plt.contourf(X, Y, grad_magnitude, levels=20, cmap='viridis')
plt.title('|∇T|')
plt.colorbar()

plt.tight_layout()
plt.show()
```

---

## 2. Numerical Differentiation

### 2.1 Finite Difference Schemes

```python
def finite_difference_demo():
    """Demonstrate different finite difference schemes."""
    
    # Test function: f(x) = sin(x), f'(x) = cos(x)
    x = np.linspace(0, 2*np.pi, 100)
    f = np.sin(x)
    f_exact = np.cos(x)
    
    dx = x[1] - x[0]
    
    # Forward difference
    f_prime_forward = np.zeros_like(x)
    f_prime_forward[:-1] = (f[1:] - f[:-1]) / dx
    
    # Backward difference
    f_prime_backward = np.zeros_like(x)
    f_prime_backward[1:] = (f[1:] - f[:-1]) / dx
    
    # Central difference
    f_prime_central = np.zeros_like(x)
    f_prime_central[1:-1] = (f[2:] - f[:-2]) / (2*dx)
    
    # Plot comparison
    plt.figure(figsize=(14, 8))
    
    plt.subplot(2, 1, 1)
    plt.plot(x, f_exact, 'k-', linewidth=3, label='Exact: cos(x)')
    plt.plot(x, f_prime_forward, 'r--', label='Forward Difference')
    plt.plot(x, f_prime_backward, 'b--', label='Backward Difference')
    plt.plot(x, f_prime_central, 'g--', label='Central Difference')
    plt.xlabel('x')
    plt.ylabel("f'(x)")
    plt.title('Numerical Differentiation Comparison')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Error analysis
    plt.subplot(2, 1, 2)
    error_forward = np.abs(f_prime_forward - f_exact)
    error_backward = np.abs(f_prime_backward - f_exact)
    error_central = np.abs(f_prime_central - f_exact)
    
    plt.semilogy(x[:-1], error_forward[:-1], 'r-', label='Forward Error')
    plt.semilogy(x[1:], error_backward[1:], 'b-', label='Backward Error')
    plt.semilogy(x[1:-1], error_central[1:-1], 'g-', label='Central Error')
    plt.xlabel('x')
    plt.ylabel('Absolute Error')
    plt.title('Differentiation Errors (log scale)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    # Print accuracy comparison
    print("Average Errors:")
    print(f"Forward:  {np.mean(error_forward[:-1]):.6f}")
    print(f"Backward: {np.mean(error_backward[1:]):.6f}")
    print(f"Central:  {np.mean(error_central[1:-1]):.6f}")

finite_difference_demo()
```

### 2.2 Higher-Order Derivatives

```python
def second_derivative_central(f, dx):
    """Calculate second derivative using central differences."""
    f_double_prime = np.zeros_like(f)
    f_double_prime[1:-1] = (f[2:] - 2*f[1:-1] + f[:-2]) / dx**2
    return f_double_prime

# Test with f(x) = sin(x), f''(x) = -sin(x)
x = np.linspace(0, 2*np.pi, 50)
f = np.sin(x)
f_exact_second = -np.sin(x)
dx = x[1] - x[0]

f_numerical_second = second_derivative_central(f, dx)

plt.figure(figsize=(10, 6))
plt.plot(x, f_exact_second, 'k-', linewidth=3, label='Exact: -sin(x)')
plt.plot(x, f_numerical_second, 'ro', markersize=4, label='Numerical')
plt.xlabel('x')
plt.ylabel("f''(x)")
plt.title('Second Derivative Comparison')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

---

## 3. Numerical Integration

### 3.1 Integration Methods Review

```python
def integration_methods_comparison():
    """Compare different numerical integration methods."""
    
    def test_function(x):
        return np.sin(x) * np.exp(-x/3)
    
    # Analytical integral from 0 to π
    a, b = 0, np.pi
    
    def rectangle_rule(func, a, b, n):
        dx = (b - a) / n
        x = np.linspace(a, b-dx, n)
        return np.sum(func(x + dx/2)) * dx
    
    def trapezoidal_rule(func, a, b, n):
        x = np.linspace(a, b, n+1)
        y = func(x)
        dx = (b - a) / n
        return dx * (0.5*y[0] + np.sum(y[1:-1]) + 0.5*y[-1])
    
    def simpson_rule(func, a, b, n):
        if n % 2 != 0:
            n += 1  # Simpson's rule requires even number of intervals
        dx = (b - a) / n
        x = np.linspace(a, b, n+1)
        y = func(x)
        return dx/3 * (y[0] + 4*np.sum(y[1::2]) + 2*np.sum(y[2:-1:2]) + y[-1])
    
    # Test with different numbers of intervals
    n_values = np.array([4, 8, 16, 32, 64, 128])
    errors_rect = []
    errors_trap = []
    errors_simp = []
    
    # Reference value (high-accuracy integration)
    reference = trapezoidal_rule(test_function, a, b, 10000)
    
    for n in n_values:
        rect_result = rectangle_rule(test_function, a, b, n)
        trap_result = trapezoidal_rule(test_function, a, b, n)
        simp_result = simpson_rule(test_function, a, b, n)
        
        errors_rect.append(abs(rect_result - reference))
        errors_trap.append(abs(trap_result - reference))
        errors_simp.append(abs(simp_result - reference))
    
    # Plot convergence
    plt.figure(figsize=(12, 8))
    
    plt.subplot(2, 1, 1)
    x_plot = np.linspace(a, b, 1000)
    plt.plot(x_plot, test_function(x_plot), 'k-', linewidth=2)
    plt.fill_between(x_plot, 0, test_function(x_plot), alpha=0.3)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Function to Integrate: sin(x)·exp(-x/3)')
    plt.grid(True, alpha=0.3)
    
    plt.subplot(2, 1, 2)
    plt.loglog(n_values, errors_rect, 'ro-', label='Rectangle Rule')
    plt.loglog(n_values, errors_trap, 'bs-', label='Trapezoidal Rule')
    plt.loglog(n_values, errors_simp, 'g^-', label='Simpson\'s Rule')
    
    # Add theoretical convergence lines
    plt.loglog(n_values, 0.1/n_values**2, 'r:', alpha=0.5, label='O(1/n²)')
    plt.loglog(n_values, 0.01/n_values**4, 'g:', alpha=0.5, label='O(1/n⁴)')
    
    plt.xlabel('Number of Intervals')
    plt.ylabel('Absolute Error')
    plt.title('Integration Error vs Number of Intervals')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

integration_methods_comparison()
```

---

## 4. Grid Generation

### 4.1 Structured Grids

```python
def generate_structured_grids():
    """Generate different types of structured grids."""
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 12))
    
    # Uniform Cartesian grid
    x_uniform = np.linspace(0, 1, 11)
    y_uniform = np.linspace(0, 1, 11)
    X_uniform, Y_uniform = np.meshgrid(x_uniform, y_uniform)
    
    axes[0, 0].plot(X_uniform, Y_uniform, 'b-', alpha=0.7)
    axes[0, 0].plot(X_uniform.T, Y_uniform.T, 'b-', alpha=0.7)
    axes[0, 0].set_title('Uniform Cartesian Grid')
    axes[0, 0].set_aspect('equal')
    axes[0, 0].grid(True, alpha=0.3)
    
    # Non-uniform grid (stretched)
    def stretch_function(xi, stretch_factor=2.0):
        """Stretch grid points toward boundaries."""
        return np.tanh(stretch_factor * xi) / np.tanh(stretch_factor)
    
    xi = np.linspace(-1, 1, 11)
    x_stretched = stretch_function(xi)
    x_stretched = (x_stretched + 1) / 2  # Map to [0, 1]
    
    X_stretched, Y_stretched = np.meshgrid(x_stretched, x_stretched)
    
    axes[0, 1].plot(X_stretched, Y_stretched, 'r-', alpha=0.7)
    axes[0, 1].plot(X_stretched.T, Y_stretched.T, 'r-', alpha=0.7)
    axes[0, 1].set_title('Stretched Grid')
    axes[0, 1].set_aspect('equal')
    axes[0, 1].grid(True, alpha=0.3)
    
    # Cylindrical grid
    r = np.linspace(0.1, 1, 8)
    theta = np.linspace(0, 2*np.pi, 25)
    R, THETA = np.meshgrid(r, theta)
    X_cyl = R * np.cos(THETA)
    Y_cyl = R * np.sin(THETA)
    
    axes[1, 0].plot(X_cyl, Y_cyl, 'g-', alpha=0.7)
    axes[1, 0].plot(X_cyl.T, Y_cyl.T, 'g-', alpha=0.7)
    axes[1, 0].set_title('Cylindrical Grid')
    axes[1, 0].set_aspect('equal')
    axes[1, 0].set_xlim(-1.2, 1.2)
    axes[1, 0].set_ylim(-1.2, 1.2)
    
    # Body-fitted grid around a circle
    def generate_circle_grid(n_radial=10, n_circumferential=20, inner_radius=0.5):
        r = np.linspace(inner_radius, 2.0, n_radial)
        theta = np.linspace(0, 2*np.pi, n_circumferential)
        R, THETA = np.meshgrid(r, theta)
        X = R * np.cos(THETA)
        Y = R * np.sin(THETA)
        return X, Y
    
    X_circle, Y_circle = generate_circle_grid()
    
    axes[1, 1].plot(X_circle, Y_circle, 'm-', alpha=0.7)
    axes[1, 1].plot(X_circle.T, Y_circle.T, 'm-', alpha=0.7)
    
    # Add the inner circle
    circle_boundary = plt.Circle((0, 0), 0.5, fill=False, color='black', linewidth=2)
    axes[1, 1].add_patch(circle_boundary)
    axes[1, 1].set_title('Body-fitted Grid (Around Circle)')
    axes[1, 1].set_aspect('equal')
    axes[1, 1].set_xlim(-2.2, 2.2)
    axes[1, 1].set_ylim(-2.2, 2.2)
    
    plt.tight_layout()
    plt.show()

generate_structured_grids()
```

---

## 5. Finite Difference Methods

### 5.1 1D Heat Equation

```python
def solve_1d_heat_equation():
    """Solve 1D heat equation using explicit finite differences."""
    
    # Problem parameters
    L = 1.0          # Length of rod
    alpha = 0.01     # Thermal diffusivity
    T_left = 100     # Left boundary temperature
    T_right = 0      # Right boundary temperature
    T_initial = 20   # Initial temperature
    
    # Numerical parameters
    nx = 51          # Number of grid points
    dx = L / (nx - 1)
    dt = 0.0001      # Time step
    t_final = 0.5    # Final time
    
    # Stability check
    r = alpha * dt / dx**2
    print(f"Stability parameter r = {r:.4f} (should be ≤ 0.5)")
    
    # Initialize arrays
    x = np.linspace(0, L, nx)
    T = np.full(nx, T_initial)
    T[0] = T_left   # Boundary conditions
    T[-1] = T_right
    
    # Time integration
    time = 0
    time_steps = []
    temperature_profiles = []
    
    save_times = [0, 0.01, 0.05, 0.1, 0.2, 0.5]
    
    while time <= t_final:
        if any(abs(time - save_time) < dt/2 for save_time in save_times):
            time_steps.append(time)
            temperature_profiles.append(T.copy())
        
        # Update interior points
        T_new = T.copy()
        T_new[1:-1] = T[1:-1] + r * (T[2:] - 2*T[1:-1] + T[:-2])
        T = T_new
        time += dt
    
    # Plot results
    plt.figure(figsize=(12, 8))
    
    colors = plt.cm.viridis(np.linspace(0, 1, len(time_steps)))
    
    for i, (t, T_profile) in enumerate(zip(time_steps, temperature_profiles)):
        plt.plot(x, T_profile, color=colors[i], 
                label=f't = {t:.3f}s', linewidth=2)
    
    plt.xlabel('Position (m)')
    plt.ylabel('Temperature (°C)')
    plt.title('1D Heat Equation Solution')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Add analytical solution for comparison (steady state)
    T_steady = T_left + (T_right - T_left) * x / L
    plt.plot(x, T_steady, 'k--', linewidth=2, 
             label='Steady State (Analytical)')
    plt.legend()
    
    plt.tight_layout()
    plt.show()

solve_1d_heat_equation()
```

### 5.2 2D Laplace Equation

```python
def solve_2d_laplace():
    """Solve 2D Laplace equation using iterative method."""
    
    # Problem setup: ∇²φ = 0 in unit square
    # Boundary conditions: φ = 100 on left edge, φ = 0 elsewhere
    
    nx, ny = 51, 51
    dx = 1.0 / (nx - 1)
    dy = 1.0 / (ny - 1)
    
    # Initialize solution
    phi = np.zeros((ny, nx))
    phi[:, 0] = 100  # Left boundary: φ = 100
    
    # Iterative solution (Gauss-Seidel)
    max_iterations = 1000
    tolerance = 1e-6
    
    for iteration in range(max_iterations):
        phi_old = phi.copy()
        
        # Update interior points
        phi[1:-1, 1:-1] = 0.25 * (phi[2:, 1:-1] + phi[:-2, 1:-1] + 
                                   phi[1:-1, 2:] + phi[1:-1, :-2])
        
        # Check convergence
        error = np.max(np.abs(phi - phi_old))
        if error < tolerance:
            print(f"Converged after {iteration+1} iterations")
            break
    else:
        print(f"Maximum iterations ({max_iterations}) reached")
    
    # Plot results
    x = np.linspace(0, 1, nx)
    y = np.linspace(0, 1, ny)
    X, Y = np.meshgrid(x, y)
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # Contour plot
    contour = axes[0].contourf(X, Y, phi, levels=20, cmap='hot')
    axes[0].set_title('2D Laplace Equation Solution')
    axes[0].set_xlabel('X')
    axes[0].set_ylabel('Y')
    plt.colorbar(contour, ax=axes[0], label='φ')
    
    # 3D surface plot
    ax_3d = fig.add_subplot(122, projection='3d')
    surface = ax_3d.plot_surface(X, Y, phi, cmap='hot', alpha=0.8)
    ax_3d.set_title('3D Surface')
    ax_3d.set_xlabel('X')
    ax_3d.set_ylabel('Y')
    ax_3d.set_zlabel('φ')
    
    plt.tight_layout()
    plt.show()

solve_2d_laplace()
```

---

## 6. Error Analysis

### 6.1 Convergence Study

```python
def convergence_study():
    """Study convergence of finite difference methods."""
    
    def analytical_solution(x):
        """Analytical solution for comparison."""
        return np.sin(np.pi * x)
    
    def analytical_second_derivative(x):
        """Analytical second derivative."""
        return -np.pi**2 * np.sin(np.pi * x)
    
    # Test different grid resolutions
    n_values = [11, 21, 41, 81, 161]
    errors = []
    dx_values = []
    
    for n in n_values:
        x = np.linspace(0, 1, n)
        dx = x[1] - x[0]
        dx_values.append(dx)
        
        # Compute numerical second derivative
        f = analytical_solution(x)
        f_double_prime_numerical = np.zeros_like(f)
        f_double_prime_numerical[1:-1] = (f[2:] - 2*f[1:-1] + f[:-2]) / dx**2
        
        # Exact second derivative
        f_double_prime_exact = analytical_second_derivative(x)
        
        # Calculate error (exclude boundaries)
        error = np.max(np.abs(f_double_prime_numerical[1:-1] - 
                              f_double_prime_exact[1:-1]))
        errors.append(error)
    
    # Plot convergence
    plt.figure(figsize=(10, 6))
    plt.loglog(dx_values, errors, 'bo-', linewidth=2, markersize=8, 
               label='Numerical Error')
    
    # Theoretical second-order convergence
    plt.loglog(dx_values, 0.1 * np.array(dx_values)**2, 'r--', 
               label='O(Δx²) - Theoretical')
    
    plt.xlabel('Grid Spacing (Δx)')
    plt.ylabel('Maximum Error')
    plt.title('Convergence Study: Second Derivative')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Calculate observed order of accuracy
    if len(errors) >= 2:
        orders = []
        for i in range(1, len(errors)):
            order = np.log(errors[i]/errors[i-1]) / np.log(dx_values[i]/dx_values[i-1])
            orders.append(order)
        
        print("Observed order of accuracy:")
        for i, order in enumerate(orders):
            print(f"  {dx_values[i+1]:.4f}: {order:.2f}")
    
    plt.show()

convergence_study()
```

---

## Exercise 5: Mathematical Methods Practice

### Exercise 5.1: Gradient Calculation
Create a 2D scalar field φ(x,y) = x² + y² - 2xy and:
1. Calculate ∇φ analytically
2. Implement numerical gradient calculation
3. Compare numerical and analytical results
4. Plot both the field and its gradient vectors

### Exercise 5.2: Heat Conduction Problem
Solve the 1D steady-state heat conduction equation:
- d²T/dx² = -q/k (constant heat generation)
- Boundary conditions: T(0) = 100°C, T(L) = 20°C
- Parameters: L = 0.1 m, q = 1000 W/m³, k = 50 W/m·K
- Compare numerical and analytical solutions

### Exercise 5.3: Grid Quality Analysis
Generate three different grids for a 2D domain and analyze:
1. Uniform grid
2. Stretched grid (concentrated near boundaries)
3. Random perturbation of uniform grid
Calculate and compare grid quality metrics (aspect ratio, skewness)

### Exercise 5.4: Numerical Integration Application
Calculate the flow rate through a circular pipe:
Q = ∫∫ u(r) dA, where u(r) = u_max(1 - r²/R²)
1. Implement using rectangular rule in Cartesian coordinates
2. Implement using cylindrical coordinates
3. Compare accuracy and efficiency
4. Verify against analytical result Q = πR²u_max/2

---

## Key Takeaways

1. **Mathematical foundations** include vector fields, partial derivatives, and integral calculus
2. **Numerical differentiation** uses finite difference schemes with different accuracy orders
3. **Numerical integration** methods have different convergence rates and stability properties
4. **Grid generation** is crucial for accurate numerical solutions
5. **Finite difference methods** discretize continuous equations on computational grids
6. **Error analysis** helps verify solution accuracy and method convergence
7. **Convergence studies** validate numerical implementations

---

## What's Next?

You're now ready for the advanced lectures on numerical methods in fluid mechanics! The next lectures will cover:

- **Lecture 6-7**: Numerical integration methods and applications to fluid flow problems
- **Lecture 8**: Advanced coding practices and Taylor-Green vortex validation

These foundational skills in Python programming, numerical methods, and mathematical analysis will enable you to tackle complex computational fluid dynamics problems involving the advection equation, Poisson equation, and ultimately the Navier-Stokes equations!