import folium
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="specify_your_app_name_here")
location = geolocator.geocode("175 5th Avenue NYC")

m = folium.Map(titles = "Mapbox Bright")

tooltip = "Klick on me!"

folium.Marker([location.latitude, location.longitude], popup = 'УКУ Свєнца', tooltip = tooltip).add_to(m)
folium.Marker([49.8174143, 24.0216516], popup= 'УКУ Козельницька', tooltip = tooltip).add_to(m)


m.save("map.html")