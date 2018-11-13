import matplotlib.pyplot as plt
import numpy as np

def func(r, t, sigma = 10, R = 28, b = 8/3):
    x = r[0]
    y = r[1]
    z = r[2]
    fx = sigma*(y-x)
    fy = R*x - y - x*z
    fz = x*y- b*z
    return np.array([fx,fy,fz])

#sig = 10
#reynolds = 28
#nameless_b = 8/3
a = 0.0
b = 50.0
N = 10000
h = (b-a)/N
r = np.array([1.0,1.0,1.0])
xpoints = []
ypoints = []
zpoints = []
tpoints = np.arange(a,b,h)

for i in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[1])
    zpoints.append(r[2])
    k1 = h*func(r,i)
    k2 = h*func(r + (k1/2), i + (h/2))
    k3 = h*func(r + (k2/2), i + (h/2))
    k4 = h*func(r + k3, i + h)
    r += (k1 + (2*k2) + (2*k3) + k4)/6

print(xpoints)
"""plt.plot(tpoints, xpoints, 'b')
plt.hold
plt.plot(tpoints, ypoints, 'r')
plt.hold
plt.plot(xpoints, zpoints)
plt.grid()
plt.show()"""
