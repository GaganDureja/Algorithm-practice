
#Link: https://www.hackerrank.com/challenges/big-sorting/problem


n = int(input().strip())
unsorted = []
unsorted_i = 0
for unsorted_i in range(n):
   unsorted_t = str(input().strip())
   unsorted.append(unsorted_t)
unsorted.sort(key= lambda x:(len(x),x))
for i in unsorted:
    print(i)