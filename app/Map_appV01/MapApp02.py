import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER, ROW
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
    # Automatically get the current date and time
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    # Get location details
    latlng, city, state, country = get_location()
    
    # Get user inputs from the GUI
    destination = app.destination_input.value
    transport_mode = app.transport_dropdown.value
    weather = app.weather_dropdown.value

    # Prepare data to write
    data = [current_time, latlng, city, state, country, destination, transport_mode, weather]

    # Specify CSV file
    csv_file = '/Users/ulrike_imac_air/projects/maps/app/Map_appV01/recorded_data_2024.csv'
    file_exists = os.path.isfile(csv_file)

    # Write data to CSV
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Timestamp', 'Latitude and Longitude', 'City', 'State', 'Country', 'Destination', 'Transportation Mode', 'Weather'])
        writer.writerow(data)

    # Update label to confirm entry
    app.label.text = f"Recorded entry for {destination} at {current_time}"

def build_app(app):
    # Main box with custom background color
    main_box = toga.Box(style=Pack(direction=COLUMN, alignment=CENTER, padding=20, background_color='#B7E3E0'))

    # Create a destination input field
    app.destination_input = toga.TextInput(placeholder="Enter destination", style=Pack(padding=10, width=300, font_family='Inter', font_size=14, color='#E7DAD5'))

    # Create a dropdown for transportation mode
    transport_options = ['None', 'Foot', 'Bike', 'Public Transportation', 'Taxi', 'Car', 'Flight', 'Train', 'Other']
    app.transport_dropdown = toga.Selection(items=transport_options, style=Pack(padding=10, width=300, font_family='Inter', font_size=14, color='#E7DAD5'))

    # Create a dropdown for weather
    weather_options = ['Hot and Sunny', 'Warm', 'Mild', 'Cool', 'Cold', 'Very Cold']
    app.weather_dropdown = toga.Selection(items=weather_options, style=Pack(padding=10, width=300, font_family='Inter', font_size=14, color='#E7DAD5'))

    # Create a button with custom styles
    record_button = toga.Button(
        "Record Entry",
        on_press=lambda widget: record_entry(widget, app),
        style=Pack(padding=10, background_color='#2A6BBD', color='#E7DAD5', font_size=16, width=200)
    )

    # Create a label with custom font and color
    app.label = toga.Label(
        "Click the button to record entry",
        style=Pack(padding=10, font_family='Inter', font_size=16, color='#B99372')
    )

    # Add all the widgets to the main box
    main_box.add(app.destination_input)
    main_box.add(app.transport_dropdown)
    main_box.add(app.weather_dropdown)
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
