#Link: https://edabit.com/challenge/2SPQuzZTskcBpXpv4



def euclidean(a, b):
	return max([x for x in range(1,min(a,b)+1) if a%x==b%x==0])








print(euclidean(280,64))