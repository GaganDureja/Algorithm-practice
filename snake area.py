#Link: https://edabit.com/challenge/Y5Ji2HDnQTX7MxeHt


def snakefill(n):
	res = 1
	count = 0
	while res*2<=n**2:
		count+=1
		res*=2		
	return count









print(snakefill(8))