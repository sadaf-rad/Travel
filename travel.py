import folium
import pandas as pd
import numpy as np

# Data stored in dictionaries (you already have this)
data = {
    'Istanbul': {'Country': 'Turkey', 'Latitude': 41.0082, 'Longitude': 28.9784},
    'Dubai': {'Country': 'UAE', 'Latitude': 25.276987, 'Longitude': 55.296249},
    'Sharjah': {'Country': 'UAE', 'Latitude': 25.346255, 'Longitude': 55.420924},
    'Makkah': {'Country': 'Saudi Arabia', 'Latitude': 21.4225, 'Longitude': 39.8262},
    'Madinah': {'Country': 'Saudi Arabia', 'Latitude': 24.4714, 'Longitude': 39.6117},
    'Beirut': {'Country': 'Lebanon', 'Latitude': 33.8888, 'Longitude': 35.4955},
    'Damascus': {'Country': 'Syria', 'Latitude': 33.5138, 'Longitude': 36.2765},
    'Leiden': {'Country': 'Netherlands', 'Latitude': 52.1601, 'Longitude': 4.4970},
    'Den Haag': {'Country': 'Netherlands', 'Latitude': 52.0705, 'Longitude': 4.3007},
    'Delft': {'Country': 'Netherlands', 'Latitude': 52.0116, 'Longitude': 4.3571},
    'Utrecht': {'Country': 'Netherlands', 'Latitude': 52.0907, 'Longitude': 5.1214},
    'Maastricht': {'Country': 'Netherlands', 'Latitude': 50.8514, 'Longitude': 5.6900},
    'Amsterdam': {'Country': 'Netherlands', 'Latitude': 52.3676, 'Longitude': 4.9041},
    'Rotterdam': {'Country': 'Netherlands', 'Latitude': 51.9225, 'Longitude': 4.47917},
    'Valkenburg': {'Country': 'Netherlands', 'Latitude': 50.8686, 'Longitude': 5.8233},
    # Add the rest of your cities here...
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame.from_dict(data, orient='index')

# Calculate the bounding box (min/max latitude and longitude)
min_latitude = df['Latitude'].min()
max_latitude = df['Latitude'].max()
min_longitude = df['Longitude'].min()
max_longitude = df['Longitude'].max()

# Earth's surface area (in square kilometers)
earth_surface_area_km2 = 510100000  # Earth's surface area in km^2

# Calculate the height and width of the bounding box
height = max_latitude - min_latitude
# Adjust the width for the curvature of the Earth (cosine of the average latitude)
mean_latitude = np.radians((min_latitude + max_latitude) / 2)  # convert to radians
width = max_longitude - min_longitude
adjusted_width = width * np.cos(mean_latitude)

# Approximate the area visited using the bounding box
visited_area_km2 = height * adjusted_width * 40008 / 360 * 40008 / 360  # km² approximation

# Calculate the percentage of the Earth visited
percentage_visited = (visited_area_km2 / earth_surface_area_km2) * 100

# Print out the results
print(f"Bounding box coordinates: {min_latitude}, {max_latitude}, {min_longitude}, {max_longitude}")
print(f"Visited area (approx.): {visited_area_km2:.2f} km²")
print(f"Percentage of the Earth's surface visited: {percentage_visited:.2f}%")

# Create a map centered around a central location (for example, the middle of the world)
map = folium.Map(location=[20, 0], zoom_start=2)

# Add markers for cities to the map
for city, details in df.iterrows():
    folium.Marker([details['Latitude'], details['Longitude']], popup=f"{city}, {details['Country']}").add_to(map)

# Add a cute marker to show the percentage of the Earth's surface visited
percentage_popup = f"""
    <h3 style="color: #ff69b4; font-family: 'Comic Sans MS'; text-align: center;">
        🌍 You have visited {percentage_visited:.2f}% of the Earth! 🌍
    </h3>
    <p style="font-size: 16px; text-align: center; color: #ff4500;">
        Keep exploring the world! ✈️ 🌎
    </p>
"""

# Add a special marker to show the percentage visited
folium.Marker(
    location=[0, 0],  # Place it at the center of the map
    popup=percentage_popup,
    icon=folium.Icon(icon="cloud", color="pink", icon_color="white")  # Cute cloud icon
).add_to(map)

# Save the map to an HTML file
map.save("countries_visited_map.html")

# Open the map in your default browser automatically
import webbrowser
webbrowser.open("countries_visited_map.html")
