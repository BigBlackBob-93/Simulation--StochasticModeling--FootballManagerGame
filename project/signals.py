from PyQt6.QtWidgets import (
    QTableWidgetItem,
    QSpinBox,
    QPushButton
)
from math import log as ln
from random import random
from objects import (
    table,
    obj
)
from constants import (
    number_of_teams,
    teams_names
)
from teams import Teams

spin_boxes: list[QSpinBox] = obj.objects.get('spinbox')
buttons: list[QPushButton] = obj.objects.get('button')
teams: Teams = Teams()


def start() -> None:
    intensity: list[int] = []
    for item in spin_boxes:
        intensity.append(item.value())

    teams.fill(intensity)
    upd_table(game=0)
    buttons[1].setEnabled(True)


def next_game() -> None:
    if len(teams.get_opposing_teams(teams_names[0])) == 0:
        finish()
    else:
        teams_in_the_game: list[int] = []
        second_team: int = 0
        for index, (key, value) in enumerate(teams.teams.items()):
            if index not in teams_in_the_game:
                teams_in_the_game.append(index)
                for team in value:
                    if team not in teams_in_the_game:
                        teams_in_the_game.append(team)
                        second_team = team
                        break
                first_goals: int = base_generator(teams.intensity[index] * -1)
                second_goals: int = base_generator(teams.intensity[second_team] * -1)
                teams.change_results(key, teams_names[second_team], first_goals, second_goals)
    upd_table(number_of_teams - len(teams.get_opposing_teams(teams_names[0])) - 1)


def base_generator(ly: int) -> int:
    m = 0
    s = 0
    while s > ly:
        alpha = random()
        s += ln(alpha)
        m += 1
    return m


def upd_table(game: int) -> None:
    clear_table()
    table.setWindowTitle('Game # ' + str(game))

    for index, (key, value) in enumerate(teams.results.items()):
        table.insertRow(index)
        table.setItem(index, 0, QTableWidgetItem(key))
        for i in range(len(value)):
            table.setItem(index, i + 1, QTableWidgetItem(str(value[i])))


def clear_table() -> None:
    table.setRowCount(0)


def finish() -> None:
    buttons[1].setEnabled(False)
    clear_table()


buttons[0].clicked.connect(start)
buttons[1].clicked.connect(next_game)
