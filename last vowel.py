#Link: https://edabit.com/challenge/9Kuah39g997SvZmex



def common_last_vowel(txt):
	return [x for x in txt[::-1] if x.lower() in 'aeiou'][0]








print(common_last_vowel("Hello World!"))