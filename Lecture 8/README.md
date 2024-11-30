# Lecture 8

This directory contains files and resources related to **Lecture 8**. Below is a summary of its contents:

- `taylor_green_poorly_written.py`: A very poorly written code to compute the flow-field of a Taylor-Greeen vortex. This code has multiple syntax errors and numerical errors. One should never write a code like this.
- `taylor_green_no_errors.py`: After resolving all the errors in taylor_green_poorly_written.py script.
- `taylor_green_best.py`: An example script that is written in a much better way following best practice.

The above python scripts demonstrate the common coding mistakes and the best practice coding with example codes that compute the Taylor-Green vortex fields and copares the numerically computed fields with repect to the values obtained from theoretical equations. This document highlights bad coding practices to avoid towards the end.

---

## Taylor-Green Vortex

The Taylor-Green vortex is an unsteady flow of decaying vortex with an exact closed-form analytical solution of the incompressible Navier-Stokes equations in Cartesian coordinates. This makes it an excellent benchmark for validating numerical models.

### Mathematical Formulation of Taylor-Green Vortex

- **Stream Function \($\psi$\)**:
  $$ \psi(x, y, t) = \sin(x) \sin(y) e^{-2\nu t} ,$$
  where, $x$ and $y$ are the Cartesian coordinates in the range $[0, 2\pi]$; $\nu$ is kinematic viscosity, and $t$ indicates time. Based on this stream function, the velocity fields can be derived as,

- **Velocity Fields \($u, v$\)**:
  $$ u \quad = \quad \frac{\partial \psi}{\partial y} \quad = \quad \sin(x) \cos(y) e^{-2\nu t} $$
  $$ v \quad =\quad-\frac{\partial \psi}{\partial x} \quad = \quad -\cos(x) \sin(y) e^{-2\nu t} $$

- **Vorticity ($\omega$) from Velocity Fields**:
  $$ \omega = \frac{\partial v}{\partial x} - \frac{\partial u}{\partial y} = 2 \sin(x) \sin(y) e^{-2\nu t} = 2 \psi $$

---

## Coding Steps

1. **Generate 2D Grid**:
   - Generate a uniformly spaced 2D Cartesian grid \((x_i, y_j)\), having \(N_x\) and \(N_y\) number of grid points along \(x\)- and \(y\)-directions respectively. Consider \[ N_x != N_y \], helps in debugging if there is a mistake with indexing. Use meshgrid.
   - Grid range: \(x, y \in [0, 2\pi]\).

2. **Compute Theoretical Fields**:
   - Compute velocity, stream function, and vorticity fields on the \((x_i, y_j)\) grid using the theoretical expressions considering kinematic viscosity (\(\nu = 0.1 \, \text{m}^2/\text{s}\)) at time (\(t = 1.0 \text{s}\)).

3. **Numerical Differentiation**:
   - Derive velocity fields from the stream function:
     \[
     u_x = \frac{\partial \psi}{\partial y}, \quad u_y = -\frac{\partial \psi}{\partial x}
     \]
   - Compute vorticity from velocity fields:
     \[
     \omega = \frac{\partial u_y}{\partial x} - \frac{\partial u_x}{\partial y}
     \]

4. **Error Analysis**:
   - Calculate numerical errors for each field compared to theoretical values:
     \[
     \text{Error} = \max | \phi_{\text{num}} - \phi_{\text{theo}} |
     \]
     where \(\phi\) is any field variable.

5. **Plot Results**:
   - Plot velocity and vorticity fields (theoretical and numerical).
   - Include error contours and velocity quiver.

---

## Bad Coding Practices to Avoid

### 1. **No Comments or Documentation**
   - Unexplained logic, lack of variable descriptions, and unclear equations make code hard to follow.

### 2. **Poor Variable Naming**
   - Avoid cryptic names like `t`, `v`, `v_th`.
   - Use clear, consistent, and descriptive names.

### 3. **Hardcoded Values**
   - Avoid embedding constants (e.g., grid size, viscosity) directly in the code.
   - Parameterize for flexibility.

### 4. **Poor Formatting**
   - Ensure proper indentation, consistent alignment, and readable spacing.

### 5. **Unformatted Plots**
   - Include axis labels, descriptive titles, and uniform scaling in plots.

### 6. **No Functions or Modularity**
   - Modularize repetitive logic into reusable functions.
   - Validate inputs for physical constraints.

### 7. **Inefficiency**
   - Explicit loops are computationally expensive for large grids. Avoid explicit loops for operations.
   - Code is harder to debug and maintain.
   - Use vectorized operations for performance.

### 9. **Repetition:**
   - Repeatation of coding blocks without using functions.

### 8. **No Error Handling**
   - The code assumes everything will work without exceptions. On should put checks and handle exceptions gracefully for edge cases or invalid inputs.

---

Adopting the best practices (avoiding the common pitfalls listed above) ensures code readability, flexibility, and efficiency. Use this as a guideline for developing robust and maintainable Python scripts.
