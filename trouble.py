#Link: https://edabit.com/challenge/CNpZrDFf3Ct7MzQrw


def trouble(num1, num2):
	num1 = str(num1)
	num2 = str(num2)
	return any(num1[x:x+3]==num1[x]*3 and num2[y:y+2]==num2[y]*2 and\
	 num1[x]==num2[y] for x in range(len(num1)) for y in range(len(num2)))














print(trouble(451999277, 41177722899))