import matplotlib.pyplot as plt

# Load your map image or use lat-long coordinates on a blank plot
fig, ax = plt.subplots()
ax.set_xlim(-180, 180)
ax.set_ylim(-90, 90)

# Place a pin with custom shape (marker) and color
plt.plot(-122.4194, 37.7749, marker='o', color='red', markersize=10)

# Add more pins with different shapes and colors
plt.plot(-74.0060, 40.7128, marker='v', color='blue', markersize=12)  # Triangle pin

# Show the plot
plt.show()
