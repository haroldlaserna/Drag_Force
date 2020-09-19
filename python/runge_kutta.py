
"""
Método numérico Runge-Kutta de cuarto orden para la aproximacion de una solucion para una ecuacion diferencial de segundo orden
"""

def RK4(f, h, t_i, x_i, v_i):
    
    """
    Método Runge-kutta para calcular un x_i+1 teniendo en cuenta un x_i, también, v_i+1 teniendo en cuenta v_i
    
    entrada:
            f: Ecuación diferencial para obtener x_i+1
            h: Incremento de paso
            t_i Tiempo en paso i
            x_i Posicion en paso i
            v_i Velocidad en posición i
          
    salida:
           xi1= Posición en paso i+1
           vi1= Velocidad en paso i+1
    """
    
    k1v = h*f(t_i, x_i, v_i)
    k1x = h*v_i
    k2v = h*f(t_i + (h/2), x_i + (k1x/2), v_i + (k1v/2))
    k2x = h*(v_i + (k1v/2))
    k3v = h*f(t_i + (h/2), x_i + (k2x/2), v_i + (k1v/2))
    k3x = h*(v_i + (k2v/2))
    k4v = h*f(t_i + h, x_i + k3x, v_i + k1v)
    k4x = h*(v_i + k3v)
    
    xi1 = x_i + ((k1x + 2*k2x + 2*k3x + k4x)/6)
    vi1 = v_i + ((k1v + 2*k2v + 2*k3v + k4v)/6)
    
    return xi1, vi1
    
def evol_RK4(f, N, t_o, Tt, x_o, v_o):
    
    """
    cálculo aproximado de una solucion bajo un tiempo Tt-t_o dado, con una grilla finita de número N, además,
    teniendo en cuenta las condiciones iniciales x_o, v_o
    
    entrada: 
            f: Ecuación diferencial para obtener su solución aproximada
            N: Número de pasos totales
            t_0: Tiempo inicial
            Tt: Tiempo final
            x_o: Posicion inicial
            v_o: Velocidad inicial
     
    salida:
           T: Arreglo con valor de tiempo de todos los pasos tomados
           X: Arreglo con valor de posición de todos los pasos tomados
           V: Arreglo con valor de velocidad de todos los pasos tomados
           A: Arreglo con valor de aceleración de todos los pasos tomados
    """
    
    h = (Tt - t_o)/N
    T = [t_o]
    V = [v_o]
    X = [x_o]
    A = [f(t_o, x_o, v_o)]
    v_i = v_o
    x_i = x_o
    t_i = t_o
    
    for i in range(N):
        
        xi1, vi1 = RK4(f, h, t_i, x_i, v_i)
        
        ti1 = t_i + h
        T.append(ti1)
        X.append(xi1)
        V.append(vi1)
        A.append(f(ti1, xi1, vi1))
        t_i = ti1 
        x_i = xi1
        v_i = vi1
    
    return T, X, V, A
    
    
