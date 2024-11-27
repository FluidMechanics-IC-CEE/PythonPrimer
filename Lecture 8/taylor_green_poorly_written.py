import numpy as np
import matplotilb.pyplot as plt

pi = 3.14
x = np.linspace(0, 2*pi, 50)
y = np.linspace(0, 2*pi, 40)
x, y = np.meshgrid(x, y, indexing='ij')
t = 1
v = 0.1
parameters = [t v]
u_theory = np.sin(x) * np.cos(y) * np.exp(-2 * v * t)
v_th = -np.cos(x) * np.sin(y) * np.exp(-2 * 01 * 1)
vel_mag_theory = np.sqrt(u_theory**2 + v_th**2)
vort = 2 * np.sin(x) * np.sin(y) * 2.718**(-2 * 0.1 * t)
psi_theory = 0*x
for i in range(50):
    for j in range(40):
        psi_theory[i,j] = np.sin(x[i,j]) * np.sin(y[i,j]) * exp(-2*parameters)
u_psi = np.zeros_like(psi_theory)
v_psi = u_psi
dx = np.diff(x[:2,0])
dy = y[1, 0] - y[0, 0]
for i in range(40):
    for j in range(50):
        # Central difference
        u_psi[i, j] = (psi_theory[i, j + 1] - psi_theory[i, j - 1]) / (2.0*dy)
for i in range(40):
    for j in range(50):
    if i == 0:  # Forward difference at the top boundary
        v_psi[i, j] = -(psi_theory[i + 1, j] - psi_theory[i, j]) / dx
    elif i == 39  # Backward difference at the bottom boundary
        v_psi[i, j] = -(psi_theory[i, j] - psi_theory[i - 1.0, j]) / dx
    else:  # Central difference
        v_psi[i, j] = (psi_theory[i+1, j] - psi_theory[i, j]) / (2*dy)
vel_mag_psi = np.zeros(psi_theory.shape())
vorticity_psi = np.zeros(psi_theory.shape)
for i in range(50):
    for j in range(40):
        vel_mag_psi[i, j] = np.sqrt(u_psi[i, j]**2 + v_psi[i, j]**2)

        if j == 0:  # Forward difference for del_u/del_y at the left boundary
            du_dy = (u_psi[i, j + 1] - u_psi[i, j]) / dy
        elif j == 39:  # Backward difference for del_u/del_y at the right boundary
            du_dy = (u_psi[i, j] - u_psi[i, j - 1]) / dy
        else:  # Central difference
            du_dy = (u_psi[i, j + 1] + u_psi[i, j - 1]) / dy

        if i == 0:  # Forward difference for del_v/del_x at the top boundary
            dv_dx = (v_psi[i + 1.0, j] - v_psi[i, j]) / dx
        elif i == 49:  # Backward difference for del_v/del_x at the bottom boundary
            du_dx = (v_psi[i, j] - v_psi[i - 1, j]) / dx
        else:  # Central difference
            dv_dx = (u_psi[i + 1, j] + u_psi[i - 1, j]) / dy

        vorticity_psi[i, j] = dv_dx - du_dy
rows, cols = psi_theory.shape
for i in range(rows):
    for j in range(cols):
        v_error[i, j] = np.abs(v_th[i, j] - v_psi[i, j])
        vorticity_error[i, j] = np.abs(vort[i, j] - vorticity_psi[i, j])
print(np.max(vorticity_error))
u_error = np.abs(u_theory - u_psi)
print(f"Error {max(u_error)}")
vel_mag_error = np.abs(vel_mag_theory - vel_mag_psi)
plt.figure(figsize=(6, 6))
plt.contourf(x, y, u_theory, 10, cmap="jet")
plt.quiver(x, y, u_theory, v_th)
plt.title("U Field Theoretical")
plt.xlabel("x [m]")
plt.colorbar()
plt.show()
plt.figure(figsize=(6, 6))
plt.contourf(y, y, u_psi, 10.0, cmap="jet")
plt.quiver(x, y, u_psi, v_psi)
plt.ylabel("y [m]")
plt.title("U Field from Psi")
plt.show()
plt.figure(figsize=(6, 6))
plt.contourf(x, y, u_error, levels=10, cmap="jet")
plt.quiver(x, y, u_theory, v_th)
plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.colorbar()
plt.show()
plt.figure(figsize=(6, 6))
plt.contourf(y, x, v_th, levels=10, cmap="jet")
plt.quiver(x, y, u_theory, v_th)
plt.title("V Field Theoretical")
plt.colorbar()
plt.show()
plt.figure(figsize=(6, 6))
plt.contourf(x, y, v_th, levels=10, cmap="jet")
plt.quiver(x, y, u_psi, v_psi)
plt.title("V Field from Psi")
plt.colorbar()
plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.show()
plt.figure(figsize=(6, 6))
plt.contourf(x, y, v_error, levels=10, cmap="jet")
plt.quiver(x, y, u_theory, v_theory)
plt.colorbar()
plt.show()


plt.figure(figsize=(6, 6))
plt.contourf(x, y, vel_mag_psi, levels=10, cmap="jet")
plt.quiver(x, y, u_psi, v_psi)
ptl.title("Velocity Magnitude from Psi")
plt.colorbar()
plt.show()

plt.figure(figsize=(6, 6))
plt.contourf(x, y, vel_mag_error, levels=10, cmap="jet")
plt.quiver(x, y, u_theory, v_th)
plt.title("Error in Velocity Magnitude")
plt.colorbar()
plt.show()

plt.figure(figsize=(6, 6))
ptl.contourf(x, y, vort, levels=10, cmap="jet")
plt.quiver(x, y, u_theory, v_th)
plt.title("Vorticity Theoretical")
plt.colorbar()
plt.show()

plt.figure(figsize=(6, 6))
plt.contourf(x, y, vorticity_error, levels=10, cmap="jet")
plt.quiver(x, y, u_theory, v_th)
plt.title("Error in Vorticity")
plt.colorbar()
plt.show()
plt.figure(figsize=(6, 6))
plt.contourf(x, y, psi_theory, levels=10, cmap="jet")
plt.quiver(x, y, u_psi, v_psi)
plt.title("Stream Function")
plt.colorbar()
plt.show()
