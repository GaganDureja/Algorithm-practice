#Link:  https://edabit.com/challenge/6BXmvwJ5SGjby3x9Z



def convet24(txt):
	if txt[-2:]=='AM' and txt[:2]=='12':
		return 0
	elif txt[-2:]=='PM' and txt[:2]!='12':
		return int(txt.split(':')[0])+12
	else:
		return int(txt.split(':')[0])





def hours_passed(time1, time2):	
	return 'no time passed' if time1==time2 else '%s hours' %(convet24(time2)- convet24(time1))





print(hours_passed("3:00 AM", "9:00 AM"))

print(hours_passed("1:00 AM", "3:00 PM"))

print(hours_passed("1:00 AM", "12:00 PM"))

print(hours_passed("1:00 PM", "12:00 AM"))

print(hours_passed("1:00 PM", "1:00 PM"))

print(hours_passed("12:00 AM", "11:00 PM"))