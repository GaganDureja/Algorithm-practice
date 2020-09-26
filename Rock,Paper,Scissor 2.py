#Link:  https://edabit.com/challenge/z3wYnBQPgBTzy87WA



def rps(s1, s2):
	win = {'rock':1, 'paper':2, 'scissors':3}
	return ['TIE','Player 1 wins','Player 2 wins'] [win[s1]-win[s2]]






print(rps("rock", "paper"))