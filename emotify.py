#Link:  https://edabit.com/challenge/X5K95S2nEmTrsJCPD






def emotify(txt):
	dic = {'smile':':D', 'grin':':)', 'sad':':(', 'mad':':P'}
	return 'Make me '+ dic[txt.split()[-1]]



print(emotify("Make me smile"))
print(emotify("Make me grin"))
print(emotify("Make me sad"))
print(emotify("Make me mad"))

