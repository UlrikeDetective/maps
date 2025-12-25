from flask import Flask, render_template
import folium

app = Flask(__name__)

@app.route('/')
def map_view():
    # Create a map centered at a specific location
    m = folium.Map(location=[37.7749, -122.4194], zoom_start=12)  # Example: San Francisco
    
    # Add a marker
    folium.Marker([37.7749, -122.4194], popup="San Francisco").add_to(m)
    
    # Save the map as an HTML file
    m.save('templates/map.html')
    
    return render_template('map.html')

if __name__ == '__main__':
    app.run()