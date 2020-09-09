#Link: https://edabit.com/challenge/BDcaZaqCuBCczeKZL


def arrow(num):
	res = ['>'*x for x in range(1,num)]
	middle = ['>'*num]*(1 if num%2 else 2)
	return res + middle + res[::-1]








print(arrow(4))