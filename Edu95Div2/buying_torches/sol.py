number_tests = int(input())
for _ in range(number_tests):
    x,y,k = map(int, input().split())
    x -= 1
    n = k * (1 + y)
    count = k + n//x
    sticks = 1 + x*((n-1)//x)
    while sticks < n:
        sticks += x
        count += 1
    if n % x == 0:
        count -= 1
    print(count)
