#Link : https://edabit.com/challenge/MFteyMABeuGaga3a7


def color_pattern_times(cols):
	return len(cols)*2 + sum(cols[x]!=cols[x-1] for x in range(1,len(cols)))
			







print(color_pattern_times(["Blue", "Blue", "Blue", "Red", "Red", "Red"]))