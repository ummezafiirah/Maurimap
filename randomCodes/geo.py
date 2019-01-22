from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="my-application")

location = geolocator.geocode("Plaines Wilhems, Mauritius")
print(location.address)
print((location.latitude, location.longitude))
print(location.raw)

location = geolocator.geocode("Port Louis, Mauritius")
print(location.address)
print((location.latitude, location.longitude))
print(location.raw)

location = geolocator.geocode("Rivière du Rempart, Mauritius")
print(location.address)
print((location.latitude, location.longitude))
print(location.raw)




##reverse
location = geolocator.reverse("52.509669, 13.376294")
print("Reverse")
print(location.address)
print((location.latitude, location.longitude))
print(location.raw)
