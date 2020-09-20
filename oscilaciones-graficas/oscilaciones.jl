#using Plots; pyplot()


g = 1.0
p = 1.0
V = 1.0
k = 1.0

m = range(1.0, stop = 10.0, length = 100)
t = range(0.0, stop= 2*pi, length = 100 )
f(m) = cos(k/m)


println(f(m))
#display(plot(t, f))


