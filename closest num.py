#Link: https://www.hackerrank.com/challenges/closest-numbers/problem


from itertools import combinations as cb
def closestNumbers(arr):
	combin = [x for x in cb(sorted(arr),2)]
	res = []	
	for x in combin:
		if x[1]-x[0]== min(y[1]-y[0] for y in combin):
			res.append(x[0])
			res.append(x[1])
	return res
	







print(closestNumbers([5, 4, 3, 2]))