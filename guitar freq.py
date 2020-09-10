#Link: https://edabit.com/challenge/ADb5MFBAHiu5p83zv


def fret_freq(g_str, fret):
	return round([0,329.63,246.94,196,146.83,110,82.41][g_str]* 2**(fret/12),2)














print(fret_freq(3,21))