#Link: https://edabit.com/challenge/HDGiiCmSgJeeu3388




def choose_fuse(fuses, current):
	return str(min([int(x[:-1]) for x in fuses if int(x[:-1])>=float(current[:-1])]))+'V'







print(choose_fuse(["17V", "15V", "12V"], "9V"))