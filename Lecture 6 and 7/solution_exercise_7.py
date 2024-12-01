import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

# Parameters
R = 0.5                   # Radius of the pipe in meters
dpdx = -0.1               # Pressure gradient (Pa/m)
mu = 0.001                # Dynamic viscosity (Pa·s) for water at ~20°C
u_max = -dpdx * R**2 / (4 * mu)    # Maximum velocity at the center
print(f'Theoretical average velocity is {(u_max / 2.0):.4f} m/s')

#%% Mesh generation

# 2D Grid for cross-section
Nx = 15                  # Number of grid points along x
Ny = 17                  # Number of grid points along y

# Define x-axis in the cross-section
linear_space = np.linspace(-1, 1, Nx)               # Define a uniform grid between -1 and 1 with Nx data points
x = np.tanh(2 * linear_space * np.arctanh(R))       # Convert the linear uniform mesh to a non-uniform using tanh functions
x = ( x/np.max(x) ) * R                             # Normalize appropriately to map between -R to R

# Define x-axis in the cross-section
linear_space = np.linspace(-1, 1, Ny)
y = np.tanh(2 * linear_space * np.arctanh(R))
y = ( y/np.max(y) ) * R

X, Y = np.meshgrid(x, y, indexing='ij')     # Create a 2D grid for the cross-section

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

#%% Calculation of the average velocity through the duct

# Method 1 (INCORRECT METHOD)
v_avg_numerical_1 = np.mean(u[r <= R])  # Average velocity
print(f'Computed average velocity using np.mean is {v_avg_numerical_1:.4f} m/s')


# Method 2 (CORRECT METHOD using 'for' loop)
area = 0;
total_flow = 0;
for i in range(Nx-1):
    for j in range(Ny-1):
        if r[i,j] <= R:
            area += (x[i+1]-x[i]) * (y[j+1]-y[j])
            total_flow += (x[i+1]-x[i]) * (y[j+1]-y[j]) * u[i,j]

v_avg_numerical2 = total_flow / area
print(f'The numerically computed average velocity is {v_avg_numerical2:.4f} m/s')


# Method 3 (BEST METHOD) - this is exactly same as Method 2 but written in vectorized form
dx = np.diff(x)[:, np.newaxis]  # Differences along the x-direction
dy = np.diff(y)[np.newaxis, :]  # Differences along the y-direction
cell_area = dx * dy

mask = r[:-1, :-1] <= R

area = np.sum(cell_area[mask])
total_flow = np.sum(cell_area[mask] * u[:-1, :-1][mask])
v_avg_numerical3 = total_flow / area
print(f'The numerically computed average velocity is {v_avg_numerical3:.4f} m/s')


# Method 4
x1 = np.linspace(-R, R, Nx)
y1 = np.linspace(-R, R, Ny)
X1, Y1 = np.meshgrid(x1, y1, indexing='ij')
r1 = np.sqrt(X1**2 + Y1**2)

# Interpolate u onto the new uniform grid (X1, Y1)
points = np.array([X.ravel(), Y.ravel()]).T                  # Flattened coordinate points from non-uniform grid
u_values = u.ravel()                                         # Flattened velocity values
u1 = griddata(points, u_values, (X1, Y1), method='linear')   # Interpolation using griddata
v_avg_numerical4 = np.mean(u1[r1 <= R])
print(f'The numerically computed average velocity is {v_avg_numerical4:.4f} m/s')

#%% Visualization of velocity field

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

#%% Convergence plot

error1 = []
error3 = []
error4 = []
Nstart = 3
Nmax = 101
for N in range(Nstart,Nmax):
    linear_space = np.linspace(-1, 1, N)
    x = np.tanh(2 * linear_space * np.arctanh(R))
    x = ( x/np.max(x) ) * R
    y = x
    X, Y = np.meshgrid(x, y, indexing='ij')
    
    r = np.sqrt(X**2 + Y**2)
    u = u_max * (1 - (r / R)**2)
    
    # Method 1
    error1.append( np.abs( np.mean(u[r <= R]) - (u_max / 2.0) ) )
    
    # Method 3
    dx = np.diff(x)[:, np.newaxis]  # Differences along the x-direction
    dy = np.diff(y)[np.newaxis, :]  # Differences along the y-direction
    cell_area = dx * dy

    mask = r[:-1, :-1] <= R

    area = np.sum(cell_area[mask])
    total_flow = np.sum(cell_area[mask] * u[:-1, :-1][mask])
    v_avg_numerical3 = total_flow / area
    error3.append( np.abs( v_avg_numerical3 - (u_max / 2.0) ) )
    
    # Method 4
    x1 = np.linspace(-R, R, N)
    y1 = x1
    X1, Y1 = np.meshgrid(x1, y1, indexing='ij')
    r1 = np.sqrt(X1**2 + Y1**2)

    points = np.array([X.ravel(), Y.ravel()]).T                  # Flattened coordinate points from non-uniform grid
    u_values = u.ravel()                                         # Flattened velocity values
    u1 = griddata(points, u_values, (X1, Y1), method='linear')   # Interpolation using griddata
    v_avg_numerical4 = np.mean(u1[r1 <= R])
    error4.append( np.abs( v_avg_numerical4 - (u_max / 2.0) ) )
    
# Plot the error
plt.figure()
plt.plot(range(Nstart,Nmax), error1, label='Method 1')
plt.plot(range(Nstart,Nmax), error3, label='Method 3')
plt.plot(range(Nstart,Nmax), error4, label='Method 4')
plt.xlabel("Grid Resolution (N)")
plt.ylabel("Absolute error in average velocity calculation")
plt.grid(True)
plt.legend()
plt.show()
