from numpy import linalg as LA
import numpy as np


#Question 1

def get_determinant(m):
	return LA.det(m)

##### Examples
#Eg: 1
#a = np.array([[4,3,2], [1,2,6], [5,8,1]])
#print get_determinant(a)
#b = np.array([[1, 2], [1, 2]])
#print get_determinant(b)\

#Question 2

def find_area(three_points):
	m = np.array(three_points)
        return 0.5 * get_determinant(m)

####  Examples
#three_points = [[1,0,0], [1,3,0], [1,0,4]]
#print find_area(three_points)


#Question 3
a = np.array([[4,3,2], [1,2,6], [5,8,1]])
E = LA.eig(a)
print "Eigenvalues are " , E[0]
print "Corresponding eigenvectors are ", E[1]
