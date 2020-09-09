#Link: https://edabit.com/challenge/MfypAQedEAun4oQFA



def perrin(n):	
	count = 2
	p = [3,0,2]
	if n<3: return p[n]
	while count!=n:
		p.append(p[count-1]+p[count-2])
		count+=1
	return p[n]








print(perrin(1))