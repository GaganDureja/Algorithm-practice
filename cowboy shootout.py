#Link:  https://edabit.com/challenge/TbhTAgZbNvBW2ecyt



def roger_shots(lst):
	res  = sum(0.5 for x in lst if x=='BangBang!')
	return res +  (6-res*4 )/2





print(roger_shots(["Bang!", "BangBangBang!", "Boom!", "Bang!", "BangBang!", "BangBang!"]))