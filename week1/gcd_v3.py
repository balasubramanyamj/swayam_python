def gcd(m, n):
    for i in range(1, min(m, n) + 1):
        if (m % i) == 0 and (n % i) == 0:
            mrcf = i
    return mrcf


print(f"gcd(7,14) is : {gcd(7, 14)}")
print(f"gcd(7,63) is : {gcd(7, 63)}")
print(f"gcd(18,25) is : {gcd(18, 25)}")
