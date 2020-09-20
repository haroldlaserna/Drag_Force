from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')
plt.rcParams['legend.fontsize'] = 10
m_max = 0.01669*3
print(m_max)
m = np.arange(0.001, m_max, 0.0025)
t = np.arange(0, 8*np.pi, 0.0025)

m, t = np.meshgrid(m, t)
g = 9.8
p = 1
V = 3e-6
k = 1.0
x = 0.05

v = 0.007
Z = ((-m*g+p*g*V)*m/k)*(1-np.cos(np.sqrt(m/k)*t)) + x*np.cos(np.sqrt(m/k)*t) + (v/np.sqrt(m/k))*np.sin(np.sqrt(m/k)*t)

s = x*np.cos(np.sqrt(m/k)*t) + (v/np.sqrt(m/k))*np.sin(np.sqrt(m/k)*t)


c1 = ax.plot_surface(m, t, Z, label = "en el fluido")
c1._facecolors2d=c1._facecolors3d
c1._edgecolors2d=c1._edgecolors3d

c2 = ax.plot_surface(m, t, s, rstride=8, cstride=8, alpha=0.5, label = "en el vacio")
c2._facecolors2d=c2._facecolors3d
c2._edgecolors2d=c2._edgecolors3d
ax.set_xlabel('masa(kg)')
ax.set_ylabel('tiempo(s)')
ax.set_zlabel('posición(m)')

ax.legend()
"""
fig = plt.figure()
ax = fig.gca(projection='3d')
X, Y, Z = axes3d.get_test_data(0.05)
ax.plot_surface(X, Y, Z, rstride=8, cstride=8, alpha=0.3)
cset = ax.contour(X, Y, Z, zdir='z', offset=-100, cmap=cm.coolwarm)
cset = ax.contour(X, Y, Z, zdir='x', offset=-40, cmap=cm.coolwarm)
cset = ax.contour(X, Y, Z, zdir='y', offset=40, cmap=cm.coolwarm)


ax.set_xlim(-40, 40)
ax.set_ylabel('Y')
ax.set_ylim(-40, 40)
ax.set_zlabel('Z')
ax.set_zlim(-100, 100)
"""

plt.show()
