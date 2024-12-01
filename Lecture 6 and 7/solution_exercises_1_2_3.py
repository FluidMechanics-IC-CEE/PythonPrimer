#%% Import necessary packages
import numpy as np
import matplotlib.pyplot as plt

# Calculate the exact area
xbounds = [0.0, np.pi]
area_theo = (5.0*xbounds[1] - 10.0*np.cos(xbounds[1])) - (5.0*xbounds[0] - 10.0*np.cos(xbounds[0]))
print('\nExact area: ' + '{:.03f}'.format(area_theo) + ' m^2\n')

#%%
#Calculate integrals numerically using "for" loops:
    
n = 5
x = np.linspace(xbounds[0], xbounds[1], n)
dx = x[1] - x[0]

y = 5.0 + 10.0 * np.sin(x)              # river depth at different x locations

# Calculate area using method 2
area_2 = 0
for i in range(n-1):
    midpoint = (x[i] + x[i+1])/2.0
    f = 5.0 + 10.0 * np.sin(midpoint)
    area_2 += f*dx 
print('Area from method 2: ' + '{:.03f}'.format(area_2) + ' m^2')


# Calculate area using method 3
area_3 = 0
for i in range(n):
    area_3 += y[i]*dx 
print('Area from method 3: ' + '{:.03f}'.format(area_3) + ' m^2')


# Calculate area using method 4
area_4 = 0
for i in range(n):
    if i in [0, n-1]:
        area_4 += y[i]*dx/2.0
    else:
        area_4 += y[i]*dx      
print('Area from method 4: ' + '{:.03f}'.format(area_4) + ' m^2')


# Calculate area using method 5
area_5 = 0
for i in range(n-1):
    area_5 += dx * (y[i] + y[i+1])/2.0
print('Area from method 5: ' + '{:.03f}'.format(area_5) + ' m^2\n')

#%%
# Calculate integrals using vectorised operations

# Method 6 -- same as method 2 written in vectorized form
midpoints = (x[1:] + x[:-1])/2.0
y_mid = 5.0 + 10.0*np.sin(midpoints)
area_6 = dx * np.sum(y_mid)
print('Area from method 6:    ' + '{:.03f}'.format(area_6) + ' m^2')

# Method 7 -- same as method 3 written in vectorized form
area_7 = dx * np.sum(y)
print('Area from method 7:    ' + '{:.03f}'.format(area_7) + ' m^2')

# Method 8 -- same as method 4 written in vectorized form
area_8 = (dx/2.0) * (y[0] + y[n-1])  + dx * np.sum(y[1:-1])
print('Area from method 8:    ' + '{:.03f}'.format(area_8) + ' m^2')

# Method 9 -- same as method 5 written in vectorized form
area_9 = dx * np.sum( (y[1:] + y[:-1])/2.0 )
print('Area from method 9:    ' + '{:.03f}'.format(area_9) + ' m^2')
# or alternatively using the python library. (note that these are exactly the same!)
area_9 = dx * np.trapz(y)
print('Area from method 9:    ' + '{:.03f}'.format(area_9) + ' m^2\n')

#%% Now calculate the errors for each of these methods. Only need to consider methods 6, 7, and 8

n_values = np.arange(2, 101)
errors = np.zeros((4, len(n_values))) # Each row corresponds to a different method

for i in range(len(n_values)):
    n = n_values[i]
    x = np.linspace(xbounds[0], xbounds[1], n)
    dx = x[1] - x[0]
    
    y = 5.0 + 10.0 * np.sin(x)

    # Calculate error for method 6
    midpoints = (x[1:] + x[:-1])/2.0
    y_mid = 5.0 + 10.0*np.sin(midpoints)
    area_6 = dx * np.sum(y_mid)
    errors[0, i] = abs(area_6 - area_theo)

    # Calculate error for method 7
    area_7 = dx * np.sum(y)
    errors[1, i] = abs(area_7 - area_theo)
    
    # Calculate error for method 8
    area_8 = (dx/2.0) * (y[0] + y[n-1]) + dx * np.sum(y[1:-1])
    errors[2, i] = abs(area_8 - area_theo)

    # Calculate error for method 9
    area_9 = dx * np.trapz(y)
    errors[3, i] = abs(area_9 - area_theo)
    

# Plot the errors against n

labels = ['Method 6', 'Method 7', 'Method 8', 'Method 9'] # labels of each line
plt.figure()
for i in range(4):
    plt.plot(n_values, errors[i, :], label=labels[i])
plt.xlabel('n')
plt.ylabel('Absolute error (m^2)')
plt.title('Integration error for different values of n')
plt.legend()

# The following line will change the plot to log-log scale in order to compare convergence
# plt.xscale('log'); plt.yscale('log')

plt.show()
  
    
    