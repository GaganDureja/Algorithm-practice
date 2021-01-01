# Link:  https://edabit.com/challenge/3A3mHS5B3NNZddQL2










def interview(lst, tot):
	ideal_tym = [6,6,11,11,16,16,21,21]
	return 'qualified' if (all([x[0]<x[1] for x in zip(lst,ideal_tym)]) and tot<121 and len(lst)==8) else 'disqualified'





print(interview([5, 5, 10, 10, 15, 15, 20, 20], 120))
print(interview([5, 5, 10, 10, 25, 15, 20, 20], 120))
print(interview([5, 5, 10, 10, 15, 15, 20], 120))
