def gcd(m, n):
    # Assume m>n
    if m < n:
        (m, n) = (n, m)

    if (m % n) == 0:
        return n
    else:
        return gcd(n, m % n)  # m%n < n, always!


print(f"gcd(7,14) is : {gcd(7, 14)}")
print(f"gcd(7,63) is : {gcd(7, 63)}")
print(f"gcd(18,25) is : {gcd(18, 25)}")
