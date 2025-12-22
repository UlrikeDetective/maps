import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER
from datetime import datetime
import geocoder
import os
import csv  # Importing the csv module

def get_location():
    g = geocoder.ip('me')
    if g.ok:
        return g.latlng, g.city, g.state, g.country
    else:
        return None, None, None, None

def record_entry(widget, app):  # Add app to access the label
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")

    latlng, city, state, country = get_location()
    data = [current_time, latlng, city, state, country]

    csv_file = '/Users/ulrike_imac_air/projects/analysis_my_life/data/daily_activities/recorded_data_2024.csv'
    file_exists = os.path.isfile(csv_file)

    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Timestamp', 'Latitude and Longitude', 'City', 'State', 'Country'])
        writer.writerow(data)

    # Update the label text to show the recorded entry
    app.label.text = f"Recorded entry at {current_time}"

def build_app(app):
    # Create the main container
    main_box = toga.Box(style=Pack(direction=COLUMN, alignment=CENTER))

    # Create the button
    record_button = toga.Button(
        "Record Entry", 
        on_press=lambda widget: record_entry(widget, app),  # Pass the app instance
        style=Pack(padding=10)
    )

    # Create a label to show messages
    app.label = toga.Label(
        "Click the button to record entry",
        style=Pack(padding=10)
    )

    # Add the button and label to the main box
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
