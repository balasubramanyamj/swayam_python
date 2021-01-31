def gcd(m, n):
    # Assume m>n
    if m < n:
        (m, n) = (n, m)

    while (m % n) != 0:
        diff = m - n
        # diff > n? Possible!
        (m, n) = (max(n, diff), min(n, diff))

    return n


print(f"gcd(7,14) is : {gcd(7, 14)}")
print(f"gcd(7,63) is : {gcd(7, 63)}")
print(f"gcd(18,25) is : {gcd(18, 25)}")
