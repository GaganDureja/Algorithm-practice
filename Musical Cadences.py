#Link : https://edabit.com/challenge/eoSXSf4C3gTbNJJEr



def find_cadence(chords):
	if chords[-1]=='V':
		return 'imperfect'
	elif chords[-2]=='V':
		return 'perfect' if chords[-1]=='I' else 'interrupted'
	elif chords[-2:]==['IV','I']:
		return 'plagal'
	else:
		return 'no cadence'

			







print(find_cadence(["I", "i", "I"]))