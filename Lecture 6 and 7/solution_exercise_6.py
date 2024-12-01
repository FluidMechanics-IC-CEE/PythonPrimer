import numpy as np
import matplotlib.pyplot as plt

### Load Variables
cross_section = np.load('cross_section.npz')
y = cross_section['y']
z = cross_section['z']
u = cross_section['u']

#%% Plot the flow field including only the non-zero entries of u

u_plot = np.copy(u)
u_plot[u == 0] = np.nan

plt.figure()
plt.imshow(u_plot.T, origin='lower', extent=[y.min(), y.max(), z.min(), z.max()], aspect='auto')
plt.colorbar(label='u')
plt.xlabel('y')
plt.ylabel('z')
plt.show()

#%% Get the depth as a function of y

# First using for loops:
depth1 = np.zeros_like(y)
for ii in range(len(y)):
    for jj in range(len(z)):
        if u[ii, jj] != 0:
            depth1[ii] = -z[jj-1]
            break

# Next using vectorized methods:
mask = (u != 0)
depth = -z[np.argmax(mask, axis=1)-1]

plt.figure()
plt.plot(y, depth)
plt.xlabel('y')
plt.ylabel('Depth')
plt.show()

#%% Calculate the area of the river cross-section

dy = y[1]-y[0] # first check that this is constant across y
area = dy * np.trapz(depth)
print('The total area is: ' + '{:.04f}'.format(area))

#%% Now calculate the mean value of u (only where u is non-zero!)

avg_u = np.mean(u[mask])
print('The average velocity is: ' + '{:.04f}'.format(avg_u))

#%%  Now calculate the volume flux, first directly, and then by the product of the area and the mean velocity

# First directly:    
dz = z[1]-z[0] # again, check if dz this is constant across z
vol_flux_1 = np.sum(dy * dz * u)
print('Volume flux is: ' + '{:.04f}'.format(vol_flux_1) + ' (calculation 1)')

# Now as the product of mean velocity and area:
vol_flux_2 = np.mean(u[mask]) * np.sum(mask)*dy*dz      # avg_u * area
print('Volume flux is: ' + '{:.04f}'.format(vol_flux_2) + ' (calculation 2)')







