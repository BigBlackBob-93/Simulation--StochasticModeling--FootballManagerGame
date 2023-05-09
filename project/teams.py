from constants import (
    number_of_teams,
    teams_names
)


class Teams:
    def __init__(self):
        self.teams = {}
        self.results = {}

    def fill(self):
        for i in range(number_of_teams):
            self.teams[teams_names[i]] = []
            self.results[teams_names[i]] = [0, 0, '-']
            for j in range(number_of_teams):
                self.teams.get(teams_names[i]).append(j)

    def kill_opposing_team(self, alive: str, dead: int):
        self.teams.get(alive).remove(dead)

    def change_results(self, team: str, points: int, goals: int, opposing_team: str):
        self.results.get(team)[0] += points
        self.results.get(team)[1] = goals
        self.results.get(team)[2] = opposing_team

