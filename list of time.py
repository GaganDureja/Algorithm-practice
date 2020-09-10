#Link: https://edabit.com/challenge/wyr9gCiBtFM7YLauK


def time_sum(times):
	hh,mm,ss =0,0,0
	for x in times:
		x=[int(i) for i in x.split(':')]
		hh+=x[0]
		mm+=x[1]
		ss+=x[2]				
	mm+= ss//60
	hh+= mm//60
	return [hh,mm%60,ss%60]









print(time_sum([]))
print(time_sum(["1:59:45", "1:23:49"]))