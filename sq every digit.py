#Link: https://edabit.com/challenge/QiPr3M5tsqfsbYcCQ



def square_digits(n):
	return int(''.join(str(int(x)**2) for x in str(n)))





print(square_digits(9119))