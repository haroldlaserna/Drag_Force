function solo_x_g_empuje(T, U_o, b, g, empuje_m)
    
    x = zeros(length(T))
    v = zeros(length(T))
    
	for i in 1:1:length(T)

		x_resorte_objeto = U_o[1]*cos(sqrt(b)*T[i]) + U_o[2]*sqrt(b)*sin(sqrt(b)*T[i])
		x[i] =  ((-g + empuje_m)/sqrt(b))*(1 - cos(sqrt(b)*T[i])) + x_resorte_objeto 
		
		v_resorte_objeto = - (U_o[1]/sqrt(b))*sin(sqrt(b)*T[i]) + U_o[2]*b*cos(sqrt(b)*T[i])
		v[i] = ((-g + empuje_m)/b)*(sin(sqrt(b)*T[i])) + v_resorte_objeto  

	end
	
	return x, v

end

function solo_arrastre(T, U_o, a)
    
    x = zeros(length(T))
    v = zeros(length(T))
    
	for i in 1:1:length(T)
			
			x[i] = U_o[1] + sign(U_o[2])*log(1  + (a)*abs(U_o[2])*T[i] )/a
			v[i] = U_o[2]/(1 + (a*sign(U_o[2])*T[i]))
			
		end
	
	return x, v

end
