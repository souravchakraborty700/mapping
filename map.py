import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])

map = folium.Map(location=[22.49, 88.43], zoom_start = 6, tiles="Stamen Terrain")
fg = folium.FeatureGroup("Kestopur Map")
for lt, ln in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lt, ln], popup="I am a Marker", icon = folium.Icon(color = "green")))
map.add_child(fg)
map.save("Map.html")
