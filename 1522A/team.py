

class Team:
    def __init__(self):
        self.wins = 0
        self.draws = 0
        self.loses = 0

    def win_factor(self):
        return self.wins / (self.wins + self.draws + self.loses + 1e-3)

    def draw_factor(self):
        return self.draws / (self.wins + self.draws + self.loses + 1e-3)

    def loses_factor(self):
        return self.loses / (self.wins + self.draws + self.loses + 1e-3)

    def factors(self):
        return [self.win_factor(), self.draw_factor(), self.loses_factor()]
