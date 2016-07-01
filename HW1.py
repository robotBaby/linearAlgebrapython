from sympy import *
init_printing(use_unicode=True)

#Problem8
a = Matrix([[1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5]])
A3 = a*a*a
print "Answer to question 8: A^3= "
pprint(A3)
print "\n"

#Problem9
A = Matrix([[2,4,5], [2,6,1], [-2, 9, 15], [12, 0, 15], [3, 34, -52]])
B = Matrix([[2,4,5,4], [2,6,1,4], [-2,9,15,4]])
AB = A*B
ABt = AB.T
print "Answer to question 9: AB^t= "
pprint(ABt)
print "\n"

#Problem10
M = Matrix([[2,4,5], [2,6,1], [-2,9, 15], [12, 0, 15], [3, 34, -52]])
Mrank = M.rank()
print "Answer to question 10: Rank of matrix M= "
pprint(Mrank)
print "\n"

#Problem11
Mm = Matrix([[1,0,1,3], [2,3,4,7], [-1,-3,-3,-4]])
Mmrref= Mm.rref()[0]
print "Answer to question 11: Row echolon form of M= "
pprint(Mmrref)
