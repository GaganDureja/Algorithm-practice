#Link: https://edabit.com/challenge/RJySHrDkBjSAj5gzq

def factorial(num):
	if num<=1: return 1
	return num* factorial(num-1)
def prod(lst):
	p = 1
	for x in lst:
		p*=x
	return p

def nespers(lst):
	return factorial(len(lst))* prod([nespers(x) for x in lst if isinstance(x,list)])







print(nespers([1, 2, 3]))