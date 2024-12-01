import numpy as np
import matplotlib.pyplot as plt

# Parameters
R = 0.5                   # Radius of the pipe in meters
dpdx = -0.1               # Pressure gradient (Pa/m)
mu = 0.001                # Dynamic viscosity (Pa·s) for water at ~20°C
u_max = -dpdx * R**2 / (4 * mu)    # Maximum velocity at the center
print(f'Theoretical average velocity is {(u_max / 2.0):.4f} m/s')

#%% Mesh generation

# 2D Grid for cross-section
Nx = 15                    # Number of grid points along x
Ny = 17                    # Number of grid points along y

x = np.linspace(-R, R, Nx)               # Define x-axis in the cross-section
y = np.linspace(-R, R, Ny)               # Define y-axis in the cross-section
X, Y = np.meshgrid(x, y, indexing='ij')  # Create a 2D grid for the cross-section

# Visualization of mesh
plt.figure()
plt.plot(X, Y, marker='.', color='black', linestyle='none')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Computational mesh')
plt.axis('equal')
plt.show()

#%% Computation of velocity field

r = np.sqrt(X**2 + Y**2)        # Compute the matrix of r (radial distance from center)
u = u_max * (1 - (r / R)**2)    # Compute the matrix of u (velocity using Hagen-Poiseuille equation)


# Visualization of velocity field

# Mask velocity outside the pipe cross-section with nan i.e. set values outside r=R to nan
u[r > R] = np.nan
# r > R gives an logical array of the same shape as r with ones where r>R, and zeros elsewhere
# u[r > R] = np.nan sets u to nan at all the locations where r>R equals 1

plt.figure()
contour = plt.contourf(X, Y, u, 20, cmap='jet')  # Filled contour plot
plt.colorbar(contour, label='Velocity (m/s)')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Velocity Profile across Pipe Cross-Section')
plt.axis('equal')
plt.show()

plt.figure()
plt.plot(u[:,int(np.ceil(Nx/2))], x, linewidth=2)
plt.xlabel(r'$u$ [m/s]', fontsize=22)
plt.ylabel(r'$y$ [m]', fontsize=22)
plt.xlim([0, 10])
plt.xticks(np.arange(0, 11, 2))
plt.yticks(np.arange(-0.5, 0.55, 0.25))
plt.show()

#%% Calculation of the average velocity through the duct

# Calculate dx and dy based on the grid
dx = x[1] - x[0]
dy = y[1] - y[0]

# Method 1
area = np.sum(r <= R) * dx * dy              # Area of circular region in the grid
total_flow = np.sum(u[r<=R]) * dx * dy       # Total flow rate (sum of velocities * area element)
v_avg_numerical_1 = total_flow / area
print(f'The numerically computed average velocity is {v_avg_numerical_1:.4f} m/s')


# Method 2
v_avg_numerical_2 = np.mean(u[r <= R])
print(f'Computed average velocity using np.mean is {v_avg_numerical_2:.4f} m/s')

#%% COnvergence plot

error = []
Nstart = 3
Nmax = 101
for N in range(Nstart,Nmax):
    x = np.linspace(-R, R, N)
    y = np.linspace(-R, R, N)
    X, Y = np.meshgrid(x, y, indexing='ij')
    
    r = np.sqrt(X**2 + Y**2)
    u = u_max * (1 - (r / R)**2)
    
    dx = x[1] - x[0]
    dy = y[1] - y[0]

    area = np.sum(r <= R) * dx * dy
    total_flow = np.sum(u[r<=R]) * dx * dy
    
    error.append( np.abs( (total_flow / area) - (u_max / 2.0) ) )
    
# Plot the error
plt.plot(range(Nstart,Nmax), error)
plt.xlabel("Grid Resolution (N)")
plt.ylabel("Error in Average Velocity")
plt.title("Error in Numerical vs. Theoretical Average Velocity")
plt.grid(True)
plt.show()
