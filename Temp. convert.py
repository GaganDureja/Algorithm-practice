# Link: https://edabit.com/challenge/tL7KkXikEZKFDurwD

def converter(a, b):
	if a[0]=='celsius':
		if b=='kelvin':
			return round(a[1]+273.15,1)
		else:
			return round((a[1]*1.8)+32,1)
	elif a[0]=='kelvin':
		if b=='celsius':
			return round(a[1]-273.15,1)
		else:
			return round(a[1]*1.8 -459.67,1)
	else:
		if b=='celsius':
			return round((a[1]-32)/1.8,1)
		else:
			return round((a[1]+459.67)/1.8,1)
	






print(converter(["celsius", 20], "kelvin"))