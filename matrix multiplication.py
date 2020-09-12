#Link: https://edabit.com/challenge/dfep4NR2twAFTdt9k



def matrix_mult(m1, m2):
	m2 = list(map(list,zip(*m2)))
	res = []
	for x in range(2):
	 	res.append([m1[x][0]*m2[0][0] + m1[x][1]*m2[0][1], m1[x][0]*m2[1][0] + m1[x][1]*m2[1][1]])
	return res
	



    





print(matrix_mult([
	[4, 2],
	[3, 1]],
	[[5, 6],
	[3, 8]]))