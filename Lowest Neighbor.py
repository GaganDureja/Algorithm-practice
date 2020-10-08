#Link:  https://edabit.com/challenge/iZQR8D7JwmfpHDPSP




def lowestElement(vec, x, y):
	res = []
	for i in range(x-1,x+2):
		for j in range(y-1,y+2):
			try:
				res.append(vec[abs(i)][abs(j)])
			except:
				pass
	return min(res)

	







print(lowestElement([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2, 2))
print(lowestElement([[50, 30, 10],[42, 69, 420],[9000, 3,16]], 0, 0))