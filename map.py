import folium
map = folium.Map(location=[22.49, 88.43], zoom_start = 6, tiles="Stamen Terrain")
fg = folium.FeatureGroup("Kestopur Map")
fg.add_child(folium.Marker(location=[22.49, 88.43], popup="I am a Marker", icon = folium.Icon(color = "green")))
map.add_child(fg)
map.save("Map.html")
