
import csv
import json

def convert_to_json(input_file, output_file):
    """
    Converts a CSV file of Leipzig stops to a JSON file.

    Args:
        input_file (str): The path to the input CSV file.
        output_file (str): The path to the output JSON file.
    """
    stops = []
    with open(input_file, 'r', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        for row in reader:
            if not row:  # Skip empty rows if any
                continue

            stop_id, full_name, lat, lon = row[0], row[1], row[2], row[3]
            
            # Split the full name into city and stop name
            name_parts = full_name.split(',', 1)
            city = name_parts[0].strip()
            name = name_parts[1].strip() if len(name_parts) > 1 else ''

            stops.append({
                'id': stop_id,
                'city': city,
                'name': name,
                'latitude': float(lat),
                'longitude': float(lon)
            })

    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(stops, outfile, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    convert_to_json('LeipzigStops.txt', 'LeipzigStops.json')
