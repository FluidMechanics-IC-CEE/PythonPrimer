# The following code is the same as in the first solution, but has been modified to take into account non-uniform grids
# The main difference is that now, dx is not constant across the grid, so this has to be calculated at each point

#%% Import necessary packages
import numpy as np
import matplotlib.pyplot as plt

# Calculate the exact area
xbounds = [0, np.pi]
area_theo = (5.0*xbounds[1] - 10.0*np.cos(xbounds[1])) - (5.0*xbounds[0] - 10.0*np.cos(xbounds[0]))
print('\nExact area: ' + '{:.03f}'.format(area_theo) + ' m^2\n')

#%%
#Calculate integrals using "for" loops:

n = 5
x = xbounds[0] + np.linspace(0, 1, n)**2 * (xbounds[1] - xbounds[0])

y = 5.0 + 10.0 * np.sin(x)              # river depth at different x locations

# Calculate area using method 2
area_2 = 0
for i in range(n-1):
    midpoint = (x[i] + x[i+1])/2
    f = 5.0 + 10.0 * np.sin(midpoint)
    dx = x[i+1] - x[i] # We now have to calculate this at each point!
    area_2 += f*dx
print('Area from method 2: ' + '{:.03f}'.format(area_2) + ' m^2')


# Method 3 doesn't really make sense for nonuniform mesh so we will skip it


# Calculate area using method 4
area_4 = 0
for i in range(n):
    
    # The easiest way to think about this dx is by taking half the distace to the next point, and half the distance to the previous point    
    if i == 0:
        dx = (x[1]-x[0])/2.0
    elif i == n-1:
        dx = (x[-1]-x[-2])/2.0
    else:
        dx = (x[i]-x[i-1])/2.0 + (x[i+1]-x[i])/2.0
    
    area_4 += y[i]*dx      
print('Area from method 4: ' + '{:.03f}'.format(area_4) + ' m^2')


# Calculate area using method 5
area_5 = 0
for i in range(n-1):
    area_5 += (x[i+1] - x[i]) * (y[i] + y[i+1])/2.0
print('Area from method 5: ' + '{:.03f}'.format(area_5) + ' m^2\n')

# Note that methods 4 and 5 still give the same values

#%%
# Calculate integrals using vectorised operations


# Method 6 -- same as method 2 written in vectorized form
midpoints = (x[1:] + x[:-1])/2
dx = x[1:] - x[:-1] # dx is now a vector! Note its shape
print(dx.shape)
f_vec = 5.0 + 10.0*np.sin(midpoints)
area_6 = np.sum(dx * f_vec)     # Note dx must be inside the sum. First dx*f_vec element wise product will be computed, and then sum will be done
print('Area from method 6:    ' + '{:.03f}'.format(area_6) + ' m^2')


# Method 7 -- same as method 3


# Method 8 -- same as method 4 written in vectorized form
dx = 0*y
dx[0] = (x[1]-x[0])/2.0
dx[1:-1] = (x[1:-1]-x[:-2])/2.0 + (x[2:]-x[1:-1])/2.0
dx[n-1] = (x[-1]-x[-2])/2.0
print(dx.shape)                     # dx is now a vector! Note its shape
area_8 = np.sum(dx * y)             # Note dx must be inside the sum. First dx*y element wise product will be computed, and then sum will be done
print('Area from method 8:    ' + '{:.03f}'.format(area_8) + ' m^2')


# Method 9 -- same as method 5 written in vectorized form
dx = []
dx = x[1:] - x[:-1] # dx is now a vector! Note its shape
print(dx.shape)
area_9 = np.sum(dx * (y[1:] + y[:-1])/2.0 )         # Note dx must be inside the sum. First dx*y element wise product will be computed, and then sum will be done
print('Area from method 9:    ' + '{:.03f}'.format(area_9) + ' m^2')

# or alternatively using the python library. (note that these are exactly the same!)
dx = []
dx = np.gradient(x)         # dx is now a vector! Note its shape
print(dx.shape)
area_9 = np.trapz(dx * y)   # Note dx must be inside the sum. First dx*y element wise product will be computed, and then sum will be done
print('Area from method 9:    ' + '{:.03f}'.format(area_9) + ' m^2\n')


# IMPORTANT: check that the two ways of calculating for methods 9 above give the same results
# Try and convice yourself why from the definitions of np.gradient and np.trapz


#%% Now calculate the errors for each of these methods. Only need to consider methods 6, 7, and 8

n_values = np.arange(2, 16)
errors = np.zeros((3, len(n_values))) # Each row corresponds to a different method

for i in range(len(n_values)):
    n = n_values[i]
    x = xbounds[0] + np.linspace(0, 1, n)**2 * (xbounds[1] - xbounds[0])
    y = 5.0 + 10.0 * np.sin(x)

    # Calculate error for method 6
    midpoints = (x[1:] + x[:-1])/2
    dx = x[1:] - x[:-1]
    f_vec = 5.0 + 10.0*np.sin(midpoints)
    area_6 = np.sum(dx * f_vec)
    errors[0, i] = abs(area_6 - area_theo)

    # Calculate error for method 8
    dx = 0*y
    dx[0] = (x[1]-x[0])/2.0
    dx[1:-1] = (x[1:-1]-x[:-2])/2.0 + (x[2:]-x[1:-1])/2.0
    dx[n-1] = (x[-1]-x[-2])/2.0
    area_8 = np.sum(dx * y)
    errors[1, i] = abs(area_8 - area_theo)

    # Calculate error for method 9
    dx = np.gradient(x)
    area_9 = np.trapz(dx * y)
    errors[2, i] = abs(area_9 - area_theo)


# And plot the errors against n

labels = ['Method 6', 'Method 8', 'Method 9'] # labels of each line
plt.figure()
for i in range(3):
    plt.plot(n_values, errors[i, :], label=labels[i])
plt.xlabel('n')
plt.ylabel('Absolute error (m^2)')
plt.title('Integration error for different values of n')
plt.legend()

# The following line will change the plot to log-log scale in order to compare convergence
# plt.xscale('log'); plt.yscale('log')

plt.show()
  
    
    