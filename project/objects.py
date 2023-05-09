from PyQt6.QtWidgets import (
    QMainWindow,
    QLabel,
    QPushButton,
    QSpinBox,
    QTableWidget
)
from base_object import Object
from constants import (
    number_of_teams,
    teams_names
)

obj: Object = Object()

window: QMainWindow = obj.set_obj(
    object=QMainWindow(),
    title="Simulation: Stochastic modeling"
)
table: QTableWidget = obj.set_obj(
    object=QTableWidget(),
    columns=4,
    title='Game # 0',
    h_headers=['Teams', 'Points', 'Goals', 'Opposing team']
)

obj.set_obj(
    object=QLabel(window),
    title=' team ',
    above=obj.indent
)
obj.set_obj(
    object=QLabel(window),
    title=' intensity ',
    left=200,
    above=obj.indent
)
obj.increase_indent()
for i in range(number_of_teams):
    obj.increase_indent()
    obj.set_obj(
        object=QLabel(window),
        title=teams_names[i],
        case=0,
        above=obj.indent
    )
    obj.add_obj(
        obj.set_obj(
            object=QSpinBox(window),
            left=200,
            above=obj.indent + 7,
            value=i
        ),
        key='spinbox'
    )
obj.increase_indent(3)
obj.add_obj(
    obj.set_obj(
        object=QPushButton(window),
        title='Start',
        above=obj.indent
    ),
    key='button'
)
obj.add_obj(
    obj.set_obj(
        object=QPushButton(window),
        title='Next',
        above=obj.indent,
        left=150
    ),
    key='button'
)
obj.objects.get('button')[1].setEnabled(False)

window.show()
table.show()
