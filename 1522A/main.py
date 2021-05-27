# Entry point


import collections
import model
import team

MODEL = model.Model()
MODEL.load("model.pth")

number_of_test_case = int(input())

for i in range(number_of_test_case):
    teams = collections.defaultdict(team.Team)
    if i > 0:
        previous_results = input().split()
        home_score = int(previous_results[0])
        away_score = int(previous_results[1])
        if home_score > away_score:
            teams[home_team_id].wins += 1
            teams[away_team_id].loses += 1
        elif home_score == away_score:
            teams[home_team_id].draws += 1
            teams[away_team_id].draws += 1
        else:
            teams[home_team_id].loses += 1
            teams[away_team_id].wins += 1
    current_match = input().split()
    division = int(current_match[0])
    match_time= current_match[1]
    home_team_id = int(current_match[2])
    away_team_id = int(current_match[3])
    referee_id = int(current_match[4])
    coeffs = [float(coeff) for coeff in current_match[5:]]

    print(MODEL.predict_bet(
        teams[home_team_id].previous +
        teams[away_team_id].previous + coeffs
        ), flush = True)
