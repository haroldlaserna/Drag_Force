include("metodos_numericos.jl")
include("soluciones_analiticas.jl")
using Plots

pyplot()
theme(:ggplot2)

ρ = 1.0 # Densidad del fluido
Cd = 1.0 # Coeficiente de arrastre
A = 1.0 # Area de la seccion trasversal
m = 1.0 # masa del objeto
v = 1.0 # volumen del objeto inmerso en el fluido
k = 1.0 # constante elastica
g = 9.8 # aceleracion de la gravedad

a = ρ*Cd*A/(2*m)
b = k/m

empuje_m = ρ*g*v/m #fuerza de empuje sobre masa
b = 0
empuje_m = 0
g = 0
t_o = 0.0 # tiempo inicial
Tt = 50.0 # tiempo final
N = 100 # número de pasos totales
v_o = 1.0 # velocidad inicial
x_o = -1.0 # posición inicial
h = (Tt - t_o)/float(N) #incremento por paso

U_o = [x_o, v_o]

function funcion(U_n, t_n)
	
	"""
	entradas:
	         t_n: Tiempo en el paso n
	         U_n: Arreglo con posicion y velocidad en el tiempo t_n
	salida:  
	         ecuaciones: Ecuaciones diferenciales  
	"""
	
    global g, a, b, empuje_m
    
    ecuaciones = zeros(2)
    ecuaciones[1]  = U_n[2]
    ecuaciones[2]  = -b*U_n[1] - g  + empuje_m - a*abs(U_n[2])*(U_n[2])
    
    return ecuaciones

end

T = tiempo_discretizado(N,t_o)

U = aproximacion_numerica(U_o, T, h, rk4)

#x = solo_x_g_empuje(T, U_o, b, g, empuje_m)
X, V = solo_arrastre(T, U_o, a)

U[2,:] = X
gr()
U = transpose(U)
#E = U[1,:] - U[2,:]
println("graficando...")
#p1 = plot(T, U, ylabel = "x(m)", xlabel = "t(s)", label = ["método numérico" "solución exacta"])
#p2 = plot(T, E, ylabel = "Error(m)", xlabel = "t(s)", label = "Error")
#p = plot(p1, p2)
display(plot(T,U))
#savefig(p, "v_square.png")
