#Link: https://edabit.com/challenge/pSrCZFim6Y8HcS9Yc



def convert(deg):
	if len(deg)<3 or ('C' in deg and 'F' in deg): return 'Error'
	else:
		num = int(deg[:-2])
		to_fer = str(round(num*1.8 +32))+'*F'
		to_cel = str(round((num-32)/1.8))+'*C'
		return to_fer if 'C' in deg else to_cel

	
	
	













print(convert("0*F"))