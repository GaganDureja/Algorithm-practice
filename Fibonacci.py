#Problem: Implement the function fib(n),\
# which returns the nth number in the Fibonacci sequence, using only O(1) space.







def fib(n):    
    return 0 if not n else 1 if n==1 else fib(n-1) + fib(n-2) 







print(fib(0))
print(fib(5))
print(fib(8))