#Link:  https://edabit.com/challenge/A8wX28kwTyPiz59AJ



def warp_tunnel(mtx, n):
	res = sum(mtx,[]) 
	n = n%len(res)
	lst = [[]]
	for x in res[-n:]+res[:-n]:
		if len(lst[-1])<len(mtx[0]):
			lst[-1].append(x)
		else:
			lst.append([x])
	return lst




print(warp_tunnel([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2))