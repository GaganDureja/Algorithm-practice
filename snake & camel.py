#Link: https://edabit.com/challenge/tMiJJkuAFDfsdmdZK


def to_snake_case(txt):	
	return ''.join('_'+x.lower() if x.isupper() else x for x in txt)

	

def to_camel_case(txt):
	txt = txt.split('_')
	return ''.join([txt[0]]+ [x.capitalize() for x in txt[1:]])













print(to_camel_case("hello_edabit"))

print(to_snake_case("helloEdabit"))