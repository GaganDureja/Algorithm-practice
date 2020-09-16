#Link:  https://edabit.com/challenge/3A6x5GjWmT4t8pssL




def oldest(people):
	return max(people, key=lambda x: people[x])




print(oldest({
  "Emma": 71,
  "Jack": 45,
  "Amy": 15,
  "Ben": 29
}))
