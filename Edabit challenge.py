#Link: https://edabit.com/challenge/t2WH2HdrQhCcJrezL





def eda_bit(start, end):
	res = []
	for x in range(start,end+1):
		if x==0 or (x%3==0 and x%5==0):
			res.append('EdaBit')
		elif x%3==0:
			res.append('Eda')
		elif x%5==0:
			res.append('Bit')
		else:
			res.append(x)
	return res





print(eda_bit(0,10))