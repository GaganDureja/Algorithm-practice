#Link: https://edabit.com/challenge/XYvyirQMkmPHGLaZi


def boom_intensity(n):
	txt = 'B%sm'%('o'*n)
	if n<2:
		return 'boom'	
	elif n%2==0 or n%5==0:		
		if n%2==0 and n%5==0:
			return txt.upper() + '!'		
		return txt +'!' if n%5 else txt.upper()
	else:
		return txt






print(boom_intensity(2))
