import numpy as np
import matplotlib.pyplot as plt
g = 9.8
p = 1000
V = 8e-5
k = 1
x = 0.05
m = 0.01669*3
v = 0.0007
t = np.arange(0,(k/m)*(2*np.pi),0.0025)

Z = ((-m*g+p*g*V)*m/k)*(1-np.cos(np.sqrt(m/k)*t)) + x*np.cos(np.sqrt(m/k)*t) + (v/np.sqrt(m/k))*np.sin(np.sqrt(m/k)*t)

s = x*np.cos(np.sqrt(m/k)*t) + (v/np.sqrt(m/k))*np.sin(np.sqrt(m/k)*t)

plt.plot(t, s, label = "en el vacío")
plt.plot(t,Z,label = "en el fluido")

mini = [min(Z), min(s)]
T = [t[5691-50], t[5691-50]]
plt.plot(T, mini, "r--",label ="$\\frac{2(-mg+\\rho gV)}{\\omega}$")

for i in [3,5,7]:
	T = [t[i*5691-50*i], t[i*5691-50*i]]
	
	plt.plot(T, mini, "r--")
	
plt.legend(loc = "upper right")
print(-m*g+p*g*V)
plt.grid()
plt.xlabel("tiempo(s)")
plt.xlim(min(t), max(t))
plt.ylabel("posición(m)")
plt.show()

min(Z)
