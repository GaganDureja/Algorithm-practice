#Link: https://edabit.com/challenge/fyyJRDHcTe9REs4Ni


dict_a = {'sky':'blue', 'road':'broken', 'sun': 'star', 'tree':'tall', 'car':'noisy', 'study':'hard', 'price': 500}
dict_b = {'sun': 'star', 'book': 'bad', 'sky': 'temple', 'people': 12, 'price': 500, 'car':'auto', 'study':'hard'}

def check(d1, d2, k):
	try:
		return True if d1[k]==d2[k] else 'Not the same'
	except KeyError:
		return "One's empty"








print(check(dict_a, dict_b, 'tree'))