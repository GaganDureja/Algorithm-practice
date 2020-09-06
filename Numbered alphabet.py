#Link: https://edabit.com/challenge/e6fL5EiwGZcsW7C5D



def alph_num(txt):
	return ' '.join(str(ord(x)-65) for x in txt)






print(alph_num("XYZ"))