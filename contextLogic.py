# This question was asked by ContextLogic.

# Implement division of two positive integers without using the division, multiplication, or modulus operators.
# Return the quotient as an integer, ignoring the remainder







def contextLogic(x,y):
	count=0
	num = y
	while num<=x:
		count+=1
		num+=y
	return count












print(contextLogic(15,2))
print(contextLogic(200,2))
print(contextLogic(15,7))
print(contextLogic(100,7))