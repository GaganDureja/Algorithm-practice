#Link: https://edabit.com/challenge/kKFuf9hfo2qnu7pBe



primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
def is_prime(primes, num, left=0, right=None):
	for x in range(left,len(primes)):
		if primes[x]==num:
			return 'yes'
	return 'no'





print(is_prime(primes, 3))