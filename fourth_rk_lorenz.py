def Lorenz(start,end,step_count,initial, sigma=10, R=28, b_param=8/3):
    #import matplotlib.pyplot as plt
    import numpy as np

    def func(r, t):
        x = r[0]
        y = r[1]
        z = r[2]
        fx = sigma*(y-x)
        fy = R*x - y - x*z
        fz = x*y- b_param*z
        return np.array([fx,fy,fz])
    
    a = float(start)
    b = float(end)
    N = int(step_count)
    r = initial.copy()
    h = (b-a)/N
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
    
    return xpoints
    #plt.plot(xpoints, zpoints)
    #plt.grid()
    #plt.show()