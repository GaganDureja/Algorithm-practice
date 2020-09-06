#Link: https://edabit.com/challenge/MhQbon8XzsG3wJHdP



def solve_for_exp(a, b):	
	count =1
	while b!=a:
		b/=a
		count+=1
	return count






print(solve_for_exp(4,1024))