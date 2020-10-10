#Link:  https://www.hackerrank.com/challenges/icecream-parlor/problem



def icecreamParlor(m, arr):
	for x in range(len(arr)):
		if m-arr[x] in arr[x+1:]:
			return [x+1, arr[x+1:].index(m-arr[x])+x+2]




print(icecreamParlor(4,[1, 4, 5, 3, 2]))