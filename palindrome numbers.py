#Link: https://edabit.com/challenge/9QbhjtbkXp3QZNuDu


def generate_palindromes(limit):
	res = []
	for x in range(limit,1,-1):
		if str(x)==str(x)[::-1]:
			res.append(x)
		if len(res)==15:
			break
	return res










print(generate_palindromes(151))