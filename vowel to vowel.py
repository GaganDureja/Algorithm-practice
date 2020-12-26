# Link:  https://edabit.com/challenge/PxxZprxCjDrzaTcLQ








def vowel_links(txt):
	txt = txt.split()
	return any(txt[x][0] in 'aeiou' and txt[x-1][-1] in 'aeiou' for x in range(1,len(txt)))
	






print(vowel_links('a very large appliance'))
print(vowel_links('go to edabit'))
print(vowel_links('an open fire'))