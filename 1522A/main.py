# Entry point

import predict


number_of_test_case = int(input())

for i in range(number_of_test_case):
    if i > 0:
        previous_results = input().split()
    current_match = input().split()
    division = int(current_match[0])
    match_time= current_match[1]
    home_team_id = int(current_match[2])
    away_team_id = int(current_match[3])
    referee_id = int(current_match[4])
    coeffs = [float(coeff) for coeff in current_match[5:]]
    print(coeffs)
    print(predict.predict(division,0,0, coeffs))
