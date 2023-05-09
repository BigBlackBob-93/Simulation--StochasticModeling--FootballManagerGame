from constants import (
    number_of_teams,
    teams_names
)


class Teams:
    def __init__(self):
        self.teams = {}
        self.results = {}
        self.intensity: list[int] = []

    def fill(self, intensity: list[int]):
        self.intensity = intensity
        for i in range(number_of_teams):
            self.teams[teams_names[i]] = []
            self.results[teams_names[i]] = [0, 0, '-']
            for j in range(number_of_teams):
                if j != i:
                    self.teams.get(teams_names[i]).append(j)

    def kill_opposing_team(self, first_team: str, second_team: str):
        self.teams.get(first_team).remove(teams_names.index(second_team))
        self.teams.get(second_team).remove(teams_names.index(first_team))

    def change_results(self, first_team: str, second_team: str, first_goals: int = 0, second_goals: int = 0):
        first_points = 0
        second_points = 0
        if first_goals > second_goals:
            first_points = 3
        elif first_goals < second_goals:
            second_points = 3
        else:
            first_points = 1
            second_points = 1

        self.results.get(first_team)[0] += first_points
        self.results.get(first_team)[1] = first_goals
        self.results.get(first_team)[2] = second_team

        self.results.get(second_team)[0] += second_points
        self.results.get(second_team)[1] = second_goals
        self.results.get(second_team)[2] = first_team

        self.kill_opposing_team(first_team, second_team)

    def get_opposing_teams(self, team: str) -> list[int]:
        return self.teams.get(team)
