#Link:  https://edabit.com/challenge/sfqudQHQ3HPpd7dZb



def rps(p1, p2):
	if p1==p2: return "It's a draw"
	winner = 'p1' 
	if p1=='Rock' and p2=='Paper': winner= 'p2'
	elif p1=='Paper' and p2=='Scissors': winner= 'p2'
	elif p1=='Scissors' and p2=='Rock': winner= 'p2'
	return 'The winner is %s'%winner







print(rps("Rock", "Paper"))