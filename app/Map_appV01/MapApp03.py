import toga
from toga.style import Pack
from toga.style.pack import COLUMN, LEFT
from datetime import datetime
import geocoder
import os
import csv

def get_location():
    g = geocoder.ip('me')
    if g.ok:
        return g.latlng, g.city, g.state, g.country
    else:
        return None, None, None, None

def record_entry(widget, app):
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")

    latlng, city, state, country = get_location()
    
    destination = app.destination_input.value
    transport_mode = app.transport_dropdown.value
    weather = app.weather_dropdown.value

    data = [current_time, latlng, city, state, country, destination, transport_mode, weather]

    # Open a "Save As" dialog using the new SaveFileDialog API
    async def save_file():
        save_dialog = toga.SaveFileDialog()
        save_path = await app.main_window.dialog(save_dialog)

        if save_path:
            file_exists = os.path.isfile(save_path)

            # Write the CSV data
            with open(save_path, mode='a', newline='') as file:
                writer = csv.writer(file)
                if not file_exists:
                    writer.writerow(['Timestamp', 'Latitude and Longitude', 'City', 'State', 'Country', 'Destination', 'Transportation Mode', 'Weather'])
                writer.writerow(data)

            app.label.text = f"Recorded entry for {destination} at {current_time}"
        else:
            app.label.text = "Save operation cancelled."

    # Run the save dialog as an asynchronous operation
    app.main_window.run_async(save_file)


def build_app(app):
    # Main box with layout and styling
    main_box = toga.Box(style=Pack(direction=COLUMN, alignment=LEFT, padding=20, background_color='#B7E3E0'))

    # Title label
    title_label = toga.Label(
        "Location Recorder",
        style=Pack(padding=(0, 0, 20, 0), alignment=LEFT, font_family='Helvetica', font_size=24, color='#B99372')
    )

    # Section heading for destination
    destination_heading = toga.Label(
        "Destination Information",
        style=Pack(padding=(10, 0), alignment=LEFT, font_family='Helvetica', font_size=18, color='#2A6BBD')
    )

    app.destination_input = toga.TextInput(placeholder="Enter destination", style=Pack(padding=10, width=300, alignment=LEFT, font_family='Helvetica', font_size=14, color='#242223'))

    # Section heading for transportation mode
    transport_heading = toga.Label(
        "Transportation Mode",
        style=Pack(padding=(20, 0), alignment=LEFT, font_family='Helvetica', font_size=18, color='#2A6BBD')
    )

    transport_options = ['None', 'Foot', 'Bike', 'Public Transportation', 'Taxi', 'Car', 'Flight', 'Train', 'Other']
    app.transport_dropdown = toga.Selection(items=transport_options, style=Pack(padding=10, width=300, alignment=LEFT, font_family='Helvetica', font_size=14, color='#E7DAD5'))

    # Section heading for weather
    weather_heading = toga.Label(
        "Weather Conditions",
        style=Pack(padding=(20, 0), alignment=LEFT, font_family='Helvetica', font_size=18, color='#2A6BBD')
    )

    weather_options = ['Hot and Sunny', 'Warm', 'Mild', 'Cool', 'Rainy', 'Cold', 'Very Cold']
    app.weather_dropdown = toga.Selection(items=weather_options, style=Pack(padding=10, width=300, alignment=LEFT, font_family='Helvetica', font_size=14, color='#E7DAD5'))

    # Record button (opens Save As dialog)
    record_button = toga.Button(
        "Save Entry",
        on_press=lambda widget: record_entry(widget, app),
        style=Pack(padding=10, background_color='#2A6BBD', color='#E7DAD5', font_size=16, width=200, alignment=LEFT)
    )

    # Confirmation label
    app.label = toga.Label(
        "Click the button to record and save entry",
        style=Pack(padding=(20, 0), alignment=LEFT, font_family='Helvetica', font_size=16, color='#B99372')
    )

    # Adding the labels and widgets to the main box
    main_box.add(title_label)
    main_box.add(destination_heading)
    main_box.add(app.destination_input)
    main_box.add(transport_heading)
    main_box.add(app.transport_dropdown)
    main_box.add(weather_heading)
    main_box.add(app.weather_dropdown)
    main_box.add(record_button)
    main_box.add(app.label)

    # Set up the main window
    app.main_window.content = main_box
    app.main_window.show()

def main():
    return toga.App("Daily Activity Recorder", "com.example.activityrecorder", startup=build_app)

if __name__ == '__main__':
    app = main()
    app.main_loop()
