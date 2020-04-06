#get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pylab as plt
import math

def koch_cl(a,b,height,it):
    a1 = a[0]   
    a2 = a[1] 
    b1 = b[0] 
    b2 = b[1]
    c1 = (a1+b1)/2.
    c2 = (a2+b2)/2.
    c = np.array([c1,c2])
    theta = np.arctan((b2-a2)/(b1-a1))
    length = np.sqrt((a1-b1)**2+(a2-b2)**2)
    height = length/3.5
    if c1 > a1:
        m1 = c1 - height*math.sin(theta)
        m2 = c2 + height*math.cos(theta)
    elif c1 < a1:
        m1 = c1 + height*math.sin(math.pi-theta)
        m2 = c2 + height*math.cos(math.pi+theta)
    else:
        if c2 > a2:
            m1 = a1 - height
            m2 = a2 + length/2.
        if c2 < a2:
            m1 = a1 + height
            m2 = a2 - length/2.
    m = np.array([m1,m2])
    points = []
    if it == 0:
        points.extend([a,b])
    elif it == 1:
        points.extend([a, c, m, m, c, b])
    else:
        points.extend(koch_cl(a,c,height,it-1))
        points.extend(koch_cl(c,m,height,it-1))
        points.extend(koch_cl(m,c,height,it-1))
        points.extend(koch_cl(c,b,height,it-1))
    return points

a = np.array([0.5,np.sqrt(3)/2.])
b = np.array([0,0])
c = np.array([1,0])
a1 = a[0]   
a2 = a[1] 
b1 = b[0] 
b2 = b[1]
c1 = c[0] 
c2 = c[1]
h = np.sqrt(3)/6.
it = 7

points1 = koch_cl(a,b,h,it)
points2 = koch_cl(b,c,h,it)
points3 = koch_cl(c,a,h,it)

fig, ax = plt.subplots(1,figsize=(5,5))
plt.plot([p[0] for p in points1], [p[1] for p in points1], 'r')
plt.plot([p[0] for p in points2], [p[1] for p in points2], 'b')
plt.plot([p[0] for p in points3], [p[1] for p in points3], 'y')
plt.axis('equal')
plt.axis('off')
plt.show()
