import folium
import pandas
data = pandas.read_csv("Volcanoes.csv")
lat = data["LAT"]
lon = data["LON"]
elev = data["ELEV"]
map = folium.Map(location = [48,-121], zoom_start = 20, tiles = "Stamen Terrain")
fg = folium.FeatureGroup(name = "My Map")
for lt, ln, el in zip(lat, lon, elev):
    popup = folium.Popup(str(el) + " m", parse_html = True)
    fg.add_child(folium.Marker(location = [lt, ln], popup = popup, icon = folium.Icon(color = "green")))
map.add_child(fg)
map.save("Map1.html")
