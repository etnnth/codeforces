# Training script

import collections
import pandas
import numpy
import team
import model

train_data = pandas.read_csv('train.csv')

TEAMS = collections.defaultdict(team.Team) # dictionnary of team by id
TRAINING_SET = []
LABELS = []

def create_training_set(match):
    home_id = int(match["home_team"])
    away_id = int(match["away_team"])
    home_team_score = int(match["full_time_home_goals"])
    away_team_score = int(match["full_time_away_goals"])
    coeffs = [match["home_coef"], match["draw_coef"], match["away_coef"]]
    TRAINING_SET.append(
            TEAMS[home_id].factors() +
            TEAMS[away_id].factors() +
            coeffs
            )
    if home_team_score > away_team_score:
        TEAMS[home_id].wins += 1
        TEAMS[away_id].loses += 1
        prediction = 0
    elif home_team_score == away_team_score:
        TEAMS[home_id].draws += 1
        TEAMS[away_id].draws += 1
        prediction = 1
    else:
        TEAMS[home_id].loses += 1
        TEAMS[away_id].wins += 1
        prediction = 2
    LABELS.append(prediction)

train_data.apply(create_training_set, axis = 1)
TRAINING_SET = numpy.asarray(TRAINING_SET)
LABELS = numpy.asarray(LABELS)


m = model.Model()
m.fit(TRAINING_SET, LABELS, 100)
m.evaluate(TRAINING_SET, LABELS)
m.save("model.pth")
