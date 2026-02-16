def factorial(n,total):
    if n<=1:
        return total
    total = n * total
    factorial(n-1, total)

factorial(0,1)

def factorial_pro(n):
    if n<=1:
        return 1
    
    return n * factorial_pro(n-1)

print(factorial_pro(0))