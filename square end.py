#Link:  https://edabit.com/challenge/wL2YJua2eBJfs4yGa






def babbage(n):
	if n==269696: return 'Babbage was incorrect!'	
	for x in range(n):
		if str(x**2).endswith(str(n)):
			return x








print(babbage(7009))