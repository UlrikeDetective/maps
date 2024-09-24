import toga
from datetime import datetime
import geocoder
import os

def get_location():
    g = geocoder.ip('me')
    if g.ok:
        return g.latlng, g.city, g.state, g.country
    else:
        return None, None, None, None

def record_entry(widget):
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
        print(f"Recorded: {data}")
        widget.label.text = f"Recorded entry at {current_time}"

def build_app():
    # Create the main window
    main_box = toga.Box()
    button = toga.Button("Record Entry", on_press=record_entry)
    label = toga.Label("Click the button to record entry")

    main_box.add(button)
    main_box.add(label)

    # Create a window with a button to trigger recording
    return toga.App("Daily Activity Recorder", "com.example.activityrecorder", startup=main_box)

if __name__ == "__main__":
    app = build_app()
    app.main_loop()
