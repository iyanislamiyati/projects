# pendulum-beemann.py
# this simulation is using beemann method
#
# Iyan Islamiyati
# Physics 2016
#
# Formulas:
# xnp1 = xn + vn*dt + ((4*an - anm1)*dt2)/6
# vnp1 = vn + ((2*anp1 + 5*an - anm1)*dt)/6
# vnp1b = vn + ((5*an - anm1)*dt)/6
# anp1 (xnp1)
# vnp1 = vnp1b + (2*anp1*dt)/6
#----------------------

import stddraw
from math import sin, cos, pi

# deklarasi variabel
n = 0
x0, xn = 0.0, 0.0
xnp1, xnm1 = 0.0, 0.0
v0, vn = 0.0, 0.0
a0, an = 0.0, 0.0
anp1, anm1 = 0.0, 0.0
tn, dt = 0.0, 0.05
dt2 = dt*dt
g = 9.81
L = 1.0

# posisi awal
x = 0.0
y = 0.0

# sudut awal dalam radian
x0 = 60*pi/180.0
v0 = 0.0
a0 = -(g/L)*sin(x0)

# nilai awal
anm1 = a0
anp1 = an
xn = x0 + v0*dt + 0.5*a0*dt2

# set window
stddraw.setXscale(-L, L)
stddraw.setYscale(-0.5, L + 0.5)

for n in range(1, 100):
    tn = n*dt
    
    # hitung an
    an = -(g/L)*sin(xn)
    
	# hitung xnp1
    xnp1 = xn + vn*dt + ((4*an - anm1)*dt2)/6
	
	# hitung vnp1
    vnp1 = vn + ((2*anp1 + 5*an - anm1)*dt)/6
	
	# hitung vnpi1 atau vnp1 bintang
    vnp1b = vn + ((5*an - anm1)*dt)/6
	
	# hitung anp1
    anp1 = -(g/L)*sin(xnp1)
	
	# hitung vnp1
    vnp1 = vnp1b + (2*anp1*dt)/6
    
	# simpan nilai
    xn = xnp1
    vn = vnp1
    anm1 = an
    an = anp1

    print (tn, "       ", vnp1)
    
    x = L*sin(xn)
    y = L*(1-cos(xn))
    
	# visualisasi
    stddraw.clear()
    stddraw.filledCircle(x, y, 0.1)
    stddraw.line(0, L, x, y)
    stddraw.line(-0.5, L, 0.5, L)
    stddraw.show(40)