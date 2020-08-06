number_tests = int(input())
for _ in range(number_tests):
    number_participants = int(input())
    liste_weight = sorted([int(w) for w in input().split()])
    max_teams = 0
    for i0 in range(number_participants):
        for j0 in range(number_participants-1, i0 , -1):
            poids = liste_weight[i0] + liste_weight[j0]
            number_team = 1
            i = i0 + 1
            j = j0 - 1
            while i < j and (j - i) // 2 + 1 + number_team > max_teams:
                poid = liste_weight[i] + liste_weight[j]
                if  poid == poids:
                    i += 1
                    j -= 1
                    number_team += 1
                elif poid < poids:
                    i += 1
                else:
                    j -= 1
            if number_team > max_teams:
                max_teams = number_team
    print(max_teams)

