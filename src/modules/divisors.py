import math

def divisors(n):
    if n < 2:
        return set()
        
    if n == 2:
        return set([1])
    
    limit = math.ceil(math.sqrt(n))
        
    divisors = set()
    
    for d in range(2, limit + 1):
        if (n % d == 0):
            divisors.add(d)
            
            m = n // d
            
            divisors.add(m)
                
    divisors.add(1)
    
    return divisors