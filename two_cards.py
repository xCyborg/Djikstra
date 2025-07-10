from nicegui import ui


def two_cards():
    with ui.row():
        ui.label('Hello').classes('blue-box')
        ui.label('world').classes('blue-box')

