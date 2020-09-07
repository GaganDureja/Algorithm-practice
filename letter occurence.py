#Link: https://edabit.com/challenge/cWQ5Qf98dQPoPJTjX


def find_occurrences(txt, ch):
	return {x.lower():x.lower().count(ch.lower()) for x in txt.split()}
	





print(find_occurrences("Hello World", "o"))