import numpy as np
import matplotlib.pyplot as plt
import seaborn
from numpy.linalg import inv


# Property : Perpendicular bisector of Chord Passes through Center of Circle


#Given Two Points
A = np.array([2, 3])
B = np.array([4, 5])

#Midpoint of the Line passing through the given points
C = (A+B)/2 


# As seen From the Given information
mGiven1 = np.array([1, -1]) # Slope of line passing through A, B
kGiven1 = mGiven1.dot(A) # Contant term of that Line


#Perpendicular passing through C
mPerp = np.array([mGiven1[0], -mGiven1[1]]) # Slope of the line
kPerp = mPerp.dot(C) # Constant term of the line

# Given Line that passes through Center
mGiven = np.array([-1, 4])
kGiven = -3

# Using theorem, solution of the above 2 will give us the Centrer of Circle

D = []
D.append(mPerp)
D.append(mGiven)
D = np.asarray(D)
Dinv = inv(D)

E = []
E.append(kPerp)
E.append(kGiven)
E = np.asarray(E)


Center = np.matmul(Dinv, E) # Intersecting points
print("The Center of the Circle is ", Center )

# Required Calculation
Radius = np.linalg.norm(Center - B)

print("Radius of the Given Circle is :", Radius, "units")


fig,ax = plt.subplots(figsize = (5,4),dpi = 100)

Circle = plt.Circle(Center, Radius, alpha = 0.7)
plt.gca().add_patch(Circle)
plt.axis(xmin = 0, xmax = 20, ymin = -8, ymax = 8)
plt.grid()
plt.plot([A[0],B[0]],[A[1],B[1]], color = 'black', label = 'Chord A-B')
plt.plot([C[0], Center[0]], [C[1], Center[1]], color = 'blue', label = 'Perpendicular bisector of A-B')
plt.plot([35, -29], [8, -8], color = 'red', label = 'Given Line')


plt.legend()
           
plt.savefig('Figure.png')


       

plt.show()





