#Link: https://edabit.com/challenge/LuBtaT9dwStbd7mnK


def tallest_building_height(lst):
	for x in range(len(lst)):
		if '#' in lst[x]:
			break
	return '%sm'%(20*(len(lst)-x))		







print(tallest_building_height([
  "              ",
  "            ##",
  "            ##",
  "###   ###   ##",
  "###   ###   ###",
  "###   ###   ###",
  "###   ###   ###"
]))