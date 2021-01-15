# Link:  https://edabit.com/challenge/xG2KB9T7mHgycGCSz





def valid(txt):
	for x in txt:
		try:
			int(x)
		except ValueError:
			return False

	return (len(txt)==4 or len(txt)==6) and ' 'not in txt










print(valid(''))
print(valid(' 1234'))
print(valid('12a3'))
print(valid('1234'))
print(valid('12345'))