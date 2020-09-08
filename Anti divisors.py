#Link: https://edabit.com/challenge/GGAKNYFg2JEwxzcqk



def anti_divisors(n):
	res = [x for x in range(1,n+1) if n%x]	
	return [x for x in res if (x%2 and ((n*2-1)%x==0 or (n*2+1)%x==0)) or n*2%x==0]










print(anti_divisors(20))