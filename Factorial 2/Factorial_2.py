# 1973 coding of a Factorial!
# n!=n (n-1) (n-2) ..... 1

def factorial(n):
    result = 1    
    for i in range (1,n + 1):
        result = i * result
    return result
print(factorial(6))

# 2023 coding of a Factorial!
# h!=h (h-1)!
def factorial2(h):
    if h == 1:
        return 1
    else:
        return h * factorial2(h - 1)
print(factorial2(10)) 
