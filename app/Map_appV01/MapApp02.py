import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER
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
    # Use the manually entered date or fallback to current date if empty
    entered_date = app.date_input.value if app.date_input.value else datetime.now().strftime("%Y-%m-%d")
    
    # Get location details
    latlng, city, state, country = get_location()
    
    # Get user inputs from the GUI
    destination = app.destination_input.value
    transport_mode = app.transport_dropdown.value
    weather = app.weather_dropdown.value

    # Prepare data to write
    data = [entered_date, latlng, city, state, country, destination, transport_mode, weather]

    # Specify CSV file
    csv_file = '/Users/ulrike_imac_air/projects/maps/app/Map_appV01/recorded_data_2024.csv'
    file_exists = os.path.isfile(csv_file)

    # Write data to CSV
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Date', 'Latitude and Longitude', 'City', 'State', 'Country', 'Destination', 'Transportation Mode', 'Weather'])
        writer.writerow(data)

    # Update label to confirm entry
    app.label.text = f"Recorded entry for {destination} on {entered_date}"

def build_app(app):
    # Create the main container
    main_box = toga.Box(style=Pack(direction=COLUMN, alignment=CENTER))

    # Create a destination input field
    app.destination_input = toga.TextInput(placeholder="Enter destination", style=Pack(padding=10, width=300))

    # Create a dropdown for transportation mode
    transport_options = ['None', 'Foot', 'Bike', 'Public Transportation', 'Taxi', 'Car', 'Flight', 'Train', 'Other']
    app.transport_dropdown = toga.Selection(items=transport_options, style=Pack(padding=10, width=300))

    # Create a dropdown for weather
    weather_options = ['Hot and Sunny', 'Warm', 'Mild', 'Cool', 'Cold', 'Very Cold']
    app.weather_dropdown = toga.Selection(items=weather_options, style=Pack(padding=10, width=300))

    # Create a text input field for manual date entry (instead of DatePicker)
    app.date_input = toga.TextInput(placeholder="Enter date (YYYY-MM-DD)", style=Pack(padding=10, width=300))

    # Create a button to record entry
    record_button = toga.Button(
        "Record Entry",
        on_press=lambda widget: record_entry(widget, app),
        style=Pack(padding=10)
    )

    # Create a label to show messages
    app.label = toga.Label(
        "Click the button to record entry",
        style=Pack(padding=10)
    )

    # Add all the widgets to the main box
    main_box.add(app.destination_input)
    main_box.add(app.transport_dropdown)
    main_box.add(app.weather_dropdown)
    main_box.add(app.date_input)
    main_box.add(record_button)
    main_box.add(app.label)

    # Set up the main window with content
    app.main_window.content = main_box
    app.main_window.show()

def main():
    return toga.App("Daily Activity Recorder", "com.example.activityrecorder", startup=build_app)

if __name__ == '__main__':
    app = main()
    app.main_loop()
