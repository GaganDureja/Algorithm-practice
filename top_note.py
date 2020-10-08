#Link:  https://edabit.com/challenge/5KqHNS9wS97zN7Xyy



def top_note(student):
	return {'name': student['name'], 'top_note': max(student['notes'])}

	







print(top_note({"name": "Jacek", "notes":[5, 4, 3]}))