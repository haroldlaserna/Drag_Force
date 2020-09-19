import numpy as np
import matplotlib.pyplot as plt
from runge_kutta import *

ρ = 1 # Densidad del fluido
Cd = 1 # Coeficiente de arrastre
A = 1 # Area de la seccion trasversal
m = 1 # masa del objeto
v = 1 # volumen del objeto inmerso en el fluido
k = 1 # constante elastica
g = 9.8 # aceleracion de la gravedad

a = ρ*Cd*A/(2*m)
b = k/m
empuje_m = ρ*g*v/m #fuerza de empuje sobre masa

def funcion(t_i, x_i, v_i):

    global g, a, b, empuje_m
    return -g - a*np.sign(v_i)*(v_i**2) - b*x_i + empuje_m 

t_o = 0 # tiempo inicial
Tt = 50 # tiempo final
N = 1000000 # número de pasos totales
v_o = -3 # velocidad inicial
x_o = -.2 # posición inicial

print("iniciando método...")

T, X, V, A = evol_RK4(funcion, N, t_o, Tt, x_o, v_o)

print("método terminado")
print("graficando...")
    
plt.plot(T, X, label = "Posición")
plt.plot(T, V, label = "Velocidad")
plt.plot(T, A, label = "Aceleración")
plt.legend()
plt.grid()

print("graficado")

plt.show()
 


#    print(T[i],"    ", X[i])




    
    
    
    


