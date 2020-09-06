#Link: https://edabit.com/challenge/TcJXTPJBsfJ2Wgkk4



def paths(n):
	if n<=1 : return 1
	return n* paths(n-1)


print(paths(5))