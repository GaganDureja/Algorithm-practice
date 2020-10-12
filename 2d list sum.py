#Link: https://edabit.com/challenge/MbPpxYWMRihFeaNPB



def sum_of_evens(lst):
	return sum(sum(x for x in y if x%2==0) for y in lst)





print(sum_of_evens([
  [1, 0, 2],
  [5, 5, 7],
  [9, 4, 3]
]))