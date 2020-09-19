
#incremento de U_n+1 dependiento de U_n; A el algoritmo que incrementa; h incremento temporal.
function U_n1(U_n, A, h)
   
   return U_n + (A*h)
end  

# método de runge kutta 4to orden    
function rk4(f, U_n, t_n, h)
    
    K1 = f(U_n, t_n)
    K2 = f(U_n + (h*K1)/2.0, t_n + (h/2.0)) 
    K3 = f(U_n + (h*K2)/2.0, t_n + (h/2.0))
    K4 = f(U_n + (h*K3), t_n + h)
    
    A = (K1 + (2.0*K2) + (2.0K3) + K4)/6.0
    
    return U_n1(U_n, A, h) 
end

#método de euler
function euler(f, U_n, t_n, h)
    
    A = f(U_n, t_n)
    
    return U_n1(U_n, A, h)
end

#método de heun
function heun(f, U_n, t_n, h)
    
    A = (f(U_n, t_n) + f(U_n + (h*f(U_n, t_n)), t_n + h))/2.0
    
    return U_n1(U_n, A, h)
end

#método midpoint
function midpoint(f, U_n, t_n, h)
    
    A = f(U_n + (h*f(U_n, t_n)/2.0),t_n + (h/2.0))
    
    return U_n1(U_n, A, h)
end

function tiempo_discretizado(N,t_o)
	
	T = zeros(N+1)
	T[1] = t_o
	
	for i in 1:1:length(T)-1
		T[i+1] = T[i] + h
	end
	
	return T

end

function aproximacion_numerica(U_o, T, h, metodo)
	
	U = zeros((2, length(T)))
	U[1, 1] = U_o[1]
	U[2, 1] = U_o[2]

	for i in 1:1:length(T)-1
   
   		U_n = [U[1,i], U[2,i]]
		U[1,i+1], U[2,i+1]  = metodo(funcion, U_n, T[i], h) 

	end	
	
	return U
end





