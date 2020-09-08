#Link: https://edabit.com/challenge/CqNoAPcQrckobTacs


def missing_letter(lst):
	return [chr(x) for x in range(ord(lst[0]),ord(lst[-1])) if chr(x) not in lst][0]











print(missing_letter(["a", "b", "c", "e", "f", "g"]))