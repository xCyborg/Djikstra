from nicegui import ui
from btn import custom_button
from two_cards import two_cards

@ui.page('/')
def home():
    ui.label('Welcome to NiceGUI! 🚀')
    ui.code('var : int = 3')
    
    with ui.card().tight():
        ui.image('https://picsum.photos/id/684/640/360')
        with ui.card_section():
            ui.label('Lorem ipsum dolor sit amet, consectetur adipiscing elit, ...')

    ui.button('Click Me', on_click=lambda: ui.notify('You clicked the button!'))
    ui.button("Purple Button", color=None).classes("bg-purple-600 text-white px-4 py-2 rounded")
    ui.button("Teal Button", color=None).classes("bg-teal-600 text-white px-4 py-2 rounded")
    ui.button("Rose Button", color=None).classes("bg-rose-600 text-white px-4 py-2 rounded")
    ui.button("Indigo Button", color=None).classes("bg-indigo-600 text-white px-4 py-2 rounded")
    # Indigo Button with hover animation

    custom_button(text="Greet", on_click=lambda: ui.notify("Hello there!"))
    two_cards()

ui.run()
 