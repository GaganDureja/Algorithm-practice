#Link: https://www.hackerrank.com/challenges/happy-ladybugs/problem

from collections import Counter
def happyLadybugs(b):
    c = Counter(b)
    if any(c[x] == 1 for x in c if x != "_"):
        return "NO"
    elif "_" not in c and any(b[i - 1] != b[i] and b[i] != b[i + 1] for i in range(1, n - 1)):
        return "NO"
    else:
        return "YES"





print(happyLadybugs('AABBC'))