number_tests = int(input())
for _ in range(number_tests):
    n = int(input())
    li = list(map(int, input().split()))
    lock = list(map(int, input().split()))
    ls = sorted([v for i,v in enumerate(li) if lock[i] == 0])[::-1]
    lr = []
    j = 0
    for i in range(n):
        if lock[i]:
            lr.append(li[i])
        else:
            lr.append(ls[j])
            j += 1
    print(*lr)
