number_test_cases = int(input())

for _ in range(number_test_cases):
    number_gifts = int(input())
    candies = [int(n) for n in input().split()]
    oranges = [int(n) for n in input().split()]
    min_candies = min(candies)
    min_oranges = min(oranges)
    moves = 0
    for n in range(number_gifts):
        moves += max(candies[n]-min_candies, oranges[n]-min_oranges)
    print(moves)
