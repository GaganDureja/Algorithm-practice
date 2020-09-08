#Link: https://edabit.com/challenge/Fe6wvtjcNFwuANuLu




def ping_pong(lst, win):
	res= []
	for x in lst:
		res+=[x,'Pong!']	
	return res if win else res[:-1]








print(ping_pong(["Ping!", "Ping!"], False))