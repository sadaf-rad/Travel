import folium
from folium.plugins import MarkerCluster
import pandas as pd
import numpy as np
from country_data import load_country_data
import webbrowser

def calculate_visited_area(df):
    """Calculate the approximate visited area and percentage of Earth's surface."""
    min_latitude, max_latitude = df['Latitude'].min(), df['Latitude'].max()
    min_longitude, max_longitude = df['Longitude'].min(), df['Longitude'].max()

    earth_surface_area_km2 = 510100000
    mean_latitude = np.radians((min_latitude + max_latitude) / 2)
    width = (max_longitude - min_longitude) * np.cos(mean_latitude)
    height = max_latitude - min_latitude

    visited_area_km2 = height * width * (40008 / 360) ** 2
    percentage_visited = (visited_area_km2 / earth_surface_area_km2) * 100

    return visited_area_km2, percentage_visited

def create_map(df, percentage_visited):
    """Create an interactive map with visited locations."""
    m = folium.Map(location=[40, 25], zoom_start=3)
    marker_cluster = MarkerCluster().add_to(m)

    for city, details in df.iterrows():
        flag_icon_html = f"""
        <div style='background: white; border-radius: 50%; width: 40px; height: 40px; display: flex; justify-content: center; align-items: center;'>
            <img src='{details['Flag']}' style='border-radius: 50%; width: 30px; height: 30px;'>
        </div>
        """
        icon = folium.DivIcon(html=flag_icon_html)
        folium.Marker(
            location=[details['Latitude'], details['Longitude']],
            popup=f"{city}, {details['Country']}",
            icon=icon
        ).add_to(marker_cluster)

    # Add a percentage marker
    percentage_popup = f"""
        <div style="width: auto; max-width: 400px; margin: auto; text-align: center; border-radius: 10px; padding: 10px; white-space: nowrap;">
            <h3 style="color: #007BFF; font-family: 'Comic Sans MS'; text-align: center;">
                🌍 You have visited {percentage_visited:.2f}% of the Earth! 🌍
            </h3>
            <p style="font-size: 16px; text-align: center; color: #28A745;">
                Keep exploring the world! ✈️ 🌎
            </p>
        </div>
    """
    folium.Marker(
        location=[0, 0],
        popup=percentage_popup,
        icon=folium.Icon(color='blue', icon='globe')
    ).add_to(m)

    return m

def save_and_open_map(map_obj, filename="index.html"):
    """Save the map as an HTML file and add a favicon."""
    map_obj.save(filename)

    with open(filename, "r") as file:
        html_content = file.read()

    favicon_html = '<link rel="icon" href="favicon.ico" type="image/x-icon">'
    html_content = html_content.replace("<head>", f"<head>\n    {favicon_html}")

    with open(filename, "w") as file:
        file.write(html_content)

    print(f"Map saved as {filename}")
    webbrowser.open(filename)


def main():
    """Main function to execute the script."""
    print("Loading data...")
    df = load_country_data()

    print("Calculating visited area...")
    visited_area_km2, percentage_visited = calculate_visited_area(df)
    print(f"Visited area: {visited_area_km2:.2f} km²")
    print(f"Percentage of Earth's surface visited: {percentage_visited:.2f}%")

    print("Creating map...")
    m = create_map(df, percentage_visited)

    print("Saving and opening map...")
    save_and_open_map(m)

if __name__ == "__main__":
    main()
