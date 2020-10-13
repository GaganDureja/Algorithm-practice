#Link:  https://edabit.com/challenge/tbEwDviZBadDSeGSz



def morse(txt):
	d = {"A":".-","B":"-...","C":"-.-.","D":"-..","E":".",
	"F":"..-.","G":"--.","H":"....","I":"..","J":".---",
	"K":"-.-","L":".-..","M":"--","N":"-.","O":"---",
	"P":".--.","Q":"--.-","R":".-.","S":"...","T":"-",
	"U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--..",
	" ":"....."}	
	if txt[0].isalpha():
		return ' '.join(d[x.upper()] for x in txt)		
	res = ''
	for x in txt.split():
		for y in d:
			if d[y]==x:
				res+= y
	return res




print(morse("Barack Obama"))
print(morse("..-. .-. .. . -.. .-. .. -.-. .... ..... ... -.-. .... .. .-.. .-.. . .-."))