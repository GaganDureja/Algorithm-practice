#Link: https://edabit.com/challenge/Nda8BQHhZSajpnt5z



def GCD(lst):
	return max(x for x in range(1,min(lst)+1) if all(y%x==0 for y in lst))

	







print(GCD([1024, 192, 2048, 512]))