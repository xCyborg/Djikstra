from nicegui import ui
import requests

class AppState:
    clicked = False
    quote = ""
    author = ""

def fetch_quote():
    try:
        res = requests.get('https://api.api-ninjas.com/v1/quotes',
                            headers={'X-Api-Key': 'uD+lwzckMKXQfGcqRoIvjg==iQTwRGi1F2iFNLII'}, timeout=5)
        if res.status_code == 200:
            data = res.json()
            if data:
                AppState.quote = data[0]['quote']
                AppState.author = data[0]['author']
    except Exception as e:
        ui.notify(f"Error: {e}")

def my_component():
    with ui.card():
        ui.label("I'm MyComponent!").classes('text-lg font-bold')
        ui.button('Click me', on_click=lambda: ui.notify('Clicked!'), color='primary')

@ui.page('/')
def main_page():
    dark_mode_component = ui.dark_mode(value=False)
    # HEADER
    with ui.header().classes("bg-primary text-white"):
        with ui.row().classes("items-center justify-between w-full px-4"):
            ui.label("NiceGUI AppX").classes("text-lg font-bold")
            with ui.row().classes("gap-2"):
                ui.button("Toggle Dark", on_click=dark_mode_component.toggle)
                ui.button("Hello", on_click=lambda: ui.notify("Hello clicked!"))
    # BODY
    with ui.column().classes('items-center justify-center min-h-screen w-full bg-cover bg-center')\
        .style('background-image: url("https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1600&q=80");'):

        ui.label('Hello World!').classes('text-4xl font-bold')
        ui.label('Name is Cole, Rust Cole...').classes('text-xl mb-4')
        ui.label('This is a NiceGUI layout translated from Quasar CDN!')

        ui.button('Get Quote', on_click=fetch_quote, color='primary')

        my_component()

        global quote_output, author_output
        with ui.card().classes('bg-primary text-white mt-6'):
            with ui.column():
                ui.label('Our Changing Planet').classes('text-lg')
                author_output = ui.label().bind_text_from(AppState, 'author', lambda a: f'by {a}' if a else '').classes('text-sm')
                quote_output = ui.label().bind_text_from(AppState, 'quote').classes('mt-2')

        def open_modal():
            AppState.clicked = True
            modal.open()

        ui.button('Toggle Modal', on_click=open_modal, color='purple')

        with ui.dialog() as modal:
            with ui.card():
                ui.label('The Modal').classes('text-lg font-bold')
                ui.label('Here is some modal content.')
                ui.button('Close', on_click=modal.close, color='primary')
                
ui.run(host='0.0.0.0', port=8080)
