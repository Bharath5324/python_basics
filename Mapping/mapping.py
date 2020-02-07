import folium
import pandas
data = pandas.read_csv("Volcanoes.csv")
lat = data["LAT"]
lon = data["LON"]
elev = data["ELEV"]
name = data["NAME"]
map = folium.Map(location = [48,-121], zoom_start = 20, tiles = "Stamen Terrain")
html = """Volcano name : <br>
<a href="https://www.google.com/search?q=%%22%s%%22" target = "_blank">%s</a><br>
Height : %s m
"""
fg = folium.FeatureGroup(name = "My Map")
def color_producer(el):
        if int(el) <= 2000:
            return "green"
        elif int(el) <= 3000:
            return "orange"
        else :
            return "red"
fg.add_child(folium.GeoJson(data = open("world.json", "r", encoding = "utf_8-sig")))
for lt, ln, el, nam in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (nam, nam, el), width=200, height=100)
    fg.add_child(folium.CircleMarker(location = [lt, ln], popup = folium.Popup(iframe), radius = 6, fill_opacity = 0.7, fill_color = color_producer(el), fill = True,color = "grey", tooltip = nam))
map.add_child(fg)
map.save("Map1.html")
