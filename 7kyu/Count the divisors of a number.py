def divisors(n):
    c = 0
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            if n // i == i:
                c+=1
            else:
                c+=2
    return c  