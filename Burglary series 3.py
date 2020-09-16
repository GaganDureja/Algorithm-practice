#Link:  https://edabit.com/challenge/2wQPKcSipXmK4idwD


def find_it(items, name):
	return name.capitalize() + (' is here!' if name not in items else ' is gone...')




print(find_it({
  "tv": 30,
  "stereo": 50,
}, "rocky"))