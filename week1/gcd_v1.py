def gcd(m, n):
    fm = []
    for i in range(1, m + 1):
        if (m % i) == 0:
            fm.append(i)
    # print(fm)
    fn = []
    for j in range(1, n + 1):
        if (n % j) == 0:
            fn.append(j)
    # print(fn)
    cf = []
    for f in fm:
        if f in fn:
            cf.append(f)
    # print(cf)

    return cf[-1]


print(f"gcd(7,14) is : {gcd(7, 14)}")
print(f"gcd(7,63) is : {gcd(7, 63)}")
print(f"gcd(18,25) is : {gcd(18, 25)}")
