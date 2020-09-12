#Link: https://edabit.com/challenge/Q7oecYfjkq7tHwPoA


def climb(stamina, obstacles):
	count = 0
	x = 1
	while True:		
		try:
			prev = obstacles[x-1]
			now = obstacles[x]
		except IndexError:
			return count
		if prev==now:
			count+=1
			x+=1
		elif prev>now and stamina>=int((prev-now)+0.999):			
			stamina-=int((prev-now)+0.999)
			count+=1
			x+=1
		elif prev<now and stamina>=int((now-prev)+0.999)*2:			
			stamina-=int((now-prev)+0.999)*2
			count+=1
			x+=1
		else:
			return count

    





print(climb(11,[0.3, 2, 2.8, 3, 3, 0.8, 3.2,2,0]))