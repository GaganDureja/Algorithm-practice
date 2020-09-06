#Link: https://www.hackerrank.com/challenges/two-characters/problem



from itertools import combinations as cb
def alternate(s):
	rest_aplha = sorted([sorted(x) for x in cb(set(s),2)])
	res =[]
	for x in rest_aplha:
		temp = ''.join(alphabet for alphabet in s if alphabet in x)				
		if ((x[0]+x[1])*len(temp)) [:len(temp)]==temp or ((x[1]+x[0])*len(temp)) [:len(temp)]==temp:
			res.append(temp)
	return len(max(res, key=len)) if res else 0





print(alternate('beabeefeab'))