from PyQt6.QtWidgets import (
    QTableWidget,
    QTableWidgetItem,
    QSpinBox,
    QPushButton
)
from PyQt6.QtCore import Qt

from objects import (
    table,
    obj
)
from constants import number_of_teams
from teams import Teams

spin_boxes: list[QSpinBox] = obj.objects.get('spinbox')
buttons: list[QPushButton] = obj.objects.get('button')
teams: Teams = Teams()


def start() -> None:
    intensity: list[int] = []
    for item in spin_boxes:
        intensity.append(item.value())

    teams.fill()

    buttons[1].setEnabled(True)


def next_game() -> None:
    pass


def upd_table(game: int, results: dict) -> None:
    table.setWindowTitle('Game # ' + str(game))

    for index, (key, value) in enumerate(results.items()):
        table.insertRow(index)
        table.setItem(index, 0, QTableWidgetItem(key))
        for i in range(len(value)):
            table.setItem(index, i + 1, QTableWidgetItem(str(value[i])))
    # item = QTableWidgetItem()
    # item.setData(Qt.ItemDataRole, i)  # а так будет число
    # table.setItem(i, 2, item)


def clear_table() -> None:
    table.setRowCount(0)


buttons[0].clicked.connect(start)
buttons[1].clicked.connect(next_game)
