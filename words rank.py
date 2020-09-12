#Link: https://edabit.com/challenge/fXS3JYMnk3yupk5En


def word_rank(txt):	
	res= max(txt.split(), key=lambda x: sum(ord(y.lower())-96 if y.isalpha() else 0 for y in x))
	return res if res[-1].isalpha() else ''.join(x for x in res if x.isalpha())
	

	
    





print(word_rank("Nancy is very pretty...."))