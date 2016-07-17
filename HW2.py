import string
import numpy as np
import pandas as pd
import heapq

votes_by_country = "UN_voting_data.txt"

init=pd.read_table(votes_by_country, skipinitialspace=True, index_col=0, sep=' ', header=None)
A=init.transpose()
AT = init
M=AT.dot(A)

num_countries = init.count()[1]

##Q1

M_stack=M.stack().nsmallest(1)

print "The most opposing pair of countries are", M_stack.index[0][0], "and", M_stack.index[0][1], ". Their agreement is", M_stack[0]
print
##Q2

M_stack = M.stack().nsmallest(20)

print "The ten most oppossing pairs of countries are as follows:"

for i in range(0,20,2):
	print i/2 + 1 ,":",  M_stack.index[i][0], "and", M_stack.index[i][1], ". Their agreement is", M_stack[i] 

print
##Q3

M_stack = M.stack().nlargest(num_countries + 1) 

for i in range(num_countries + 1):
	this = M_stack.index[i][0]
	that = M_stack.index[i][1]
	agreement = M_stack[i]
	if (this != that):
		print "The pair of countries in greatest agreement are", this, "and", that, ". Their agreement is", agreement
		break
