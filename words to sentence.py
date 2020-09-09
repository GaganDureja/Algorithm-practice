#Link: https://edabit.com/challenge/GP6CEr9a5CMqPHY7C



def words_to_sentence(words):
	if not words: return ''
	words = [x for x in words if x]	
	l = len(words)	
	return ''.join(words[x] +(' and ' if x==l-2 else '' if x==l-1 else ', ') for x in range(l))







print(words_to_sentence(None))