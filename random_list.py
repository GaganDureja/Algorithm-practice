# This question was asked by Google.

# Given an integer n and a list of integers l, write a function that randomly generates a
# number from 0 to n-1 that isn't in l (uniform).










from random import *

items = [5,10,15,20,25,30]

x = sample(items,  1)  
print(x[0])