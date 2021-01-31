def gcd(m, n):
    i = min(m, n)
    while i > 0:
        if (m % i) == 0 and (n % i) == 0:
            return i
        else:
            i = i - 1


print(f"gcd(7,14) is : {gcd(7, 14)}")
print(f"gcd(7,63) is : {gcd(7, 63)}")
print(f"gcd(18,25) is : {gcd(18, 25)}")
