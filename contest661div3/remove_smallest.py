test_case_number = int(input())
for _ in range(test_case_number):
    liste_length = int(input())
    liste = sorted([int(number) for number in input().split()])
    diff = [a-b for (a,b) in zip(liste[1:],liste[:-1])]
    if liste_length == 1 or max(diff) < 2:
        print('YES')
    else:
        print('NO')

