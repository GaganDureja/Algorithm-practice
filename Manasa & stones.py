#Link: https://www.hackerrank.com/challenges/manasa-and-stones/problem




def stones(n, a, b):
    s= set()
    for i in range(n):
        s.add(b*i + (n-i-1)*a)
    return sorted(s)


print(stones(4,10,100))

