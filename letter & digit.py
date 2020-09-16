#Link:  https://edabit.com/challenge/KEz3TAQfh9WxSZMLH



def count_all(txt):
	return {'LETTERS':sum(x.isalpha() for x in txt) , 'DIGITS':sum(x.isnumeric() for x in txt)}





print(count_all("H3ll0 Wor1d"))