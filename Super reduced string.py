#Link: https://www.hackerrank.com/challenges/reduced-string/problem

temp = ''
s = input()

while(temp != s):
    temp = s
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            s = s[:i]+s[i+2:]
            break
print(s if s else 'Empty String')