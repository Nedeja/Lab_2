import geopy
import folium
import time
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="specify_your_app_name_here")
m = folium.Map(titles = "Mapbox Bright")

year = input('Enter a year you would like to have a map for:')
current_location = input('Enter your current location(format: lat, long):')

path = 'locations1.list'
def open_file(path):
    lst = []
    with open(path, encoding='utf-8', errors='ignore') as f:
        line = f.readline()
        while not line.startswith("=============="):
            line = f.readline()
        for line in f:
            if '{' in line:
                ind_start, ind_last = line.find('{'), line.find('}')
                line = line[:ind_start- 1] + line[ind_last + 1:]
            ind = line[::-1].find('(')
            if line.find("(") != len(line) - ind - 1:
                line = line[:len(line) - ind - 1]
            lst.append(line.strip().split())
    return lst
film_list = open_file(path)
# print(film_list)

def finding_year_films(film_list, year):
    year_list = []
    year = "(" + year + ")"
    for i in film_list:
        if year in i:
            year_list.append(i)
    year_list_joined = []
    for j in year_list:
        for l in j:
            if '}' in l:
                ind1 = j.index(l)
                year_list_joined.append((j[:ind1 + 1], n))
            elif ')' in l:
                ind2 = j.index(l)
                n = j[:ind2 + 1] + [" ".join(j[ind2 + 1:])]
                year_list_joined.append(n)
    return year_list_joined
year_list_joined = finding_year_films(film_list, year)
# print(finding_year_films(film_list, year))

def find_my_location(current_location):
    location = geolocator.reverse(current_location)
    return location.address()

def create_location_list(year_list_joined):
    location_list = []
    for i in year_list_joined:
        time.sleep(2)
        location = geolocator.geocode(i[-1])
        location_list.append((i[0], location))
        print(location_list)
    return location_list
print(create_location_list(year_list_joined))


m.save("map.html")