#Link: https://edabit.com/challenge/r7kZBzW3si9rJrLXh



def get_sentence_value(txt):
	alpha = '@abcdefghijklmnopqrstuvwxyz'	
	return sum(sum(alpha.index(y.lower()) if y.isalpha() else 0 for y in x)*(2 if x.isupper() else 1) for x in txt.split())

	

	
    





print(get_sentence_value("HELLO world!"))