from nicegui import ui

def custom_button(text="Click me!", color="primary", on_click=None):
    """Reusable button component."""
    radio1 = ui.radio([1, 2, 3], value=1).props('inline')
    radio2 = ui.radio({1: 'A', 2: 'B', 3: 'C'}).props('inline').bind_value(radio1, 'value')
    ui.button(text, color=color, on_click=on_click)
    ui.row().classes('q-gutter-sm q-pa-md')
    ui.button('Left', color=None).classes('col-6 bg-primary text-white')
    ui.button('Right', color=None).classes('col-6 bg-secondary text-white')
    sliderWidget = ui.slider(min=0, max=10, value=2)\
        .props('vertical label reverse :markers=10 :label-value="val => `${val} px`"')