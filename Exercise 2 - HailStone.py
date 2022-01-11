def hailstone(n):
    print(n, end=" ")
    if n == 1:
        return 1
    elif n % 2 == 0:
        return hailstone(int(n/2))
    elif n % 2 == 1:
        return hailstone(int(3*n+1))

hailstone(5)