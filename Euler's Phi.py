#Link: https://edabit.com/challenge/CZYyhsQ3ZmvN3Hq7X



def phi(n):
    if n==1: return 1
    div = [x for x in range(1,n+1) if n%x==0]  
    return sum(max(i for i in range(1,x+1) if x%i==0 and i in div)==1 for x in range(1,n))

    




print(phi(1))
print(phi(6))