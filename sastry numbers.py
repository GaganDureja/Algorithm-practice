#Link: https://edabit.com/challenge/JiLom4d6aBk7wAJcZ



def is_sastry(n):
	new_num = int(str(n)+str(n+1))**0.5
	return new_num==int(new_num)
	





print(is_sastry(106755))