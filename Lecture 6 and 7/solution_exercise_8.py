import numpy as np
import matplotlib.pyplot as plt

#%% Function definitation

def compute_avg_velocity(mu, dpdx, R, Nx, Ny, lmeshplot, lvelplot):
    
    print(f'Inputs: mu = {mu:.4f} Pa-s, dpdx = {dpdx:.4f} Pa/m, R =  {R:.4f} m, Nx = {Nx:d}, Ny = {Ny:d}')

    u_max = -dpdx * R**2 / (4 * mu)    # Maximum velocity at the center
    print(f'Theoretical average velocity is {(u_max / 2.0):.4f} m/s')

    # Mesh generation
    
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
    if lmeshplot == True:
        plt.figure()
        plt.plot(X, Y, marker='.', color='black', linestyle='none')
        plt.xlabel('x (m)')
        plt.ylabel('y (m)')
        plt.title('Computational mesh')
        plt.axis('equal')
        plt.show()

    # Computation of velocity field
    r = np.sqrt(X**2 + Y**2)        # Compute the matrix of r (radial distance from center)
    u = u_max * (1 - (r / R)**2)    # Compute the matrix of u (velocity using Hagen-Poiseuille equation)

    # Visualization of velocity field
    if lvelplot == True:
        u[r > R] = np.nan       # Mask velocity outside the pipe cross-section with nan
        
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
    
    # Calculation of the average velocity through the duct
    dx = np.diff(x)[:, np.newaxis]  # Differences along the x-direction
    dy = np.diff(y)[np.newaxis, :]  # Differences along the y-direction
    cell_area = dx * dy
    
    mask = r[:-1, :-1] <= R
    
    area = np.sum(cell_area[mask])
    total_flow = np.sum(cell_area[mask] * u[:-1, :-1][mask])
    v_avg_numerical = total_flow / area
    print(f'The numerically computed average velocity is {v_avg_numerical:.4f} m/s\n')

#%% Call the functions as many times as you need

R = 0.5                   # Radius of the pipe in meters
dpdx = -0.1               # Pressure gradient (Pa/m)
mu = 0.001                # Dynamic viscosity (Pa·s) for water at ~20°C
Nx = 15                   # Number of grid points along x
Ny = 17                   # Number of grid points along y
lmeshplot = True
lvelplot = True
compute_avg_velocity(mu, dpdx, R, Nx, Ny, lmeshplot, lvelplot)


R = 0.5                   # Radius of the pipe in meters
dpdx = -0.1               # Pressure gradient (Pa/m)
mu = 0.025                # Dynamic viscosity (Pa·s) for water at ~20°C
Nx = 105                  # Number of grid points along x
Ny = 107                  # Number of grid points along y
lmeshplot = False
lvelplot = True
compute_avg_velocity(mu, dpdx, R, Nx, Ny, lmeshplot, lvelplot)

R = 0.2                   # Radius of the pipe in meters
dpdx = -0.8               # Pressure gradient (Pa/m)
mu = 0.001                # Dynamic viscosity (Pa·s) for water at ~20°C
Nx = 505                  # Number of grid points along x
Ny = 507                  # Number of grid points along y
lmeshplot = False
lvelplot = True
compute_avg_velocity(mu, dpdx, R, Nx, Ny, lmeshplot, lvelplot)