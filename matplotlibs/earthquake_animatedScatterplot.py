from earthquake_scatterplot import minlongitude, maxlongitude, minlatitude, maxlatitude, get_quakes
import contextily as cx
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

quakes = get_quakes()

fig, ax = plt.subplots(layout="constrained", figsize=(6,5))
ax.set(xlim=[minlongitude, maxlongitude], ylim=[minlatitude, maxlatitude])
ax.set_title("The April 2015 Nepal earthquake and its aftershocks")

# add basemap
cx.add_basemap(ax, crs=quakes.crs, zoom=8, source="CartoDB.Voyager")

# the first point in the animation
points_opts = dict(alpha=0.5, linewidth=0, color="red")
points = ax.scatter(
    quakes["longitude"].iloc[0],
    quakes["latitude"].iloc[0],
    s=quakes["marker_size"].iloc[0],
    **points_opts
)

# the first label
# labels show the time of the earthquake
label_opts = dict(ha="center", va="center", fontsize=15, color="black", transform=ax.transAxes)
label = ax.text(
    0.25,
    0.95,
    quakes["time"].iloc[0].strftime("%Y-%m-%d %H:%M"),
    **label_opts
)

# loop through each point in the data and draw a marker and legend for that data point
def update(frame):
    # for each frame, update the data stored on each artist.
    x = quakes["longitude"].iloc[:frame]
    y = quakes["latitude"].iloc[:frame]

    # update the scatter plot:
    data = np.stack([x, y]).T
    points.set_offsets(data)

    # set the size of the earthquakes
    points.set_sizes(quakes["marker_size"].iloc[:frame])

    # update the label
    label.set_text(quakes["time"].iloc[frame - 1].strftime("%Y-%m-%d %H:%M"))

    return (points,)

# animate by looping through all datapoints.
ani = animation.FuncAnimation(
    fig=fig, func=update, frames=len(quakes), interval=600
)

# To save the animation using Pillow as a gif
writer = animation.PillowWriter(fps=10, bitrate=1800)
ani.save("animated-scatter-v1.gif", writer=writer)

plt.ioff
plt.close()