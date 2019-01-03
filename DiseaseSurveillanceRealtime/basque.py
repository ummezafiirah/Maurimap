import json
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="my-application")

##



#This is the listener, resposible for receiving data
class StdOutListener(StreamListener):

    def on_connect(self):
        print('Stream starting...')


    def on_status(self, status):
        keyword = "flu", "gastro", "conjunctivitis", "respiratory infection", "love", "hate", "christmas"
        #print decoded
        random_user = ''
        #Check for presence of coordinates
        if status.geo is None:

              for word in keyword:
                if word in status.text:
                    if "plaines wilhems" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Plaines Wilhems, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "phoenix" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Vacoas-Phoenix, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "curepipe" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Curepipe, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "quatre bornes" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Quatre Bornes, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "palma" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Palma, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Rose Hill" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Beau Bassin - Rose Hill, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Beau Bassin" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Beau Bassin - Rose Hill, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Port Louis" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Port Louis, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Riviere du Rempart" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Rivière du Rempart, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Grand Baie" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Grand Baie, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Roches Noires" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Roches Noires, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Amuary" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Amaury, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Amitie" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Amitie, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Barlow" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Barlow, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Esperance" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Esperance Trebuchet, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Pouder d'Or Hamlet" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Poudre d'Or Hamlet, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Bain Boeuf" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Bain Boeuf, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Belle Vue Maurel" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Belle Vue Maurel, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Calodyne" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Calodyne, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Cap Malheureux" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Cap Malheureux, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Calodyne" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Calodyne, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Cottage" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Cottage, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Gokoola" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Gokoola, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Goodlands" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Goodlands, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Grand Gaube" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Grand Gaube, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Mapou" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Mapou, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Pereybere" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Pereybere, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Petit Raffray" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Petit Raffray, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Piton" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Piton, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Poudre d'Or" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Poudre d'Or, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Roche Terre" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Roche Terre, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Upper Vale" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Upper Vale, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Poudre d'Or Hamlet" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Poudre d'Or Hamlet, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Pamplemousses" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Pamplemousses, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Jin Fei" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Jin Fei, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Triolet" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Triolet, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                    if "Trou aux Biches" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Trou aux Biches, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Baie du Tombeau" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Baie du Tombeau, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Fond Du Sac" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Fond Du Sac, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                    if "Long Mountain" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Long Mountain, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Morcellement St. André" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Morcellement St. André, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Notre Dame" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Notre Dame, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Plaine des Papayes" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Plaine des Papayes, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Pointe aux Canonniers" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Pointe aux Canonniers, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Pointe aux Piments" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Pointe aux Piments, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                    if "Roche Bois" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Roche Bois, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Baillache" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Baillache, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "D'Epinay" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("D'Epinay, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                    if "Ilot" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Ilot, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Mont Choisy" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Mont Choisy, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Morcellement Balaclava" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Morcellement Balaclava, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                    if "Petite Julie" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Petite Julie, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Pointe aux Biches" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Pointe aux Biches, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Trou aux Biches" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Trou aux Biches, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                    if "Ilot" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Ilot, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Quartier Militaire" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Quartier Militaire, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Alma" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Alma, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "La Laura" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("La Laura, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Malenga" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Malenga, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Camp Thorel" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Camp Thorel, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Dagotiere" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Dagotiere, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Esperance" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Espérance, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "L'Avenir" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("L'Avenir	, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Montagne Blanche" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Montagne Blanche, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Nouvelle Decouverte" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Nouvelle Découverte, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Providence" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Providence, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "St Pierre" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("St Pierre, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))
                    if "Verdun" in status.text:
                        random_text = status.text
                        location = geolocator.geocode("Verdun, Mauritius")
                        lat = location.latitude
                        long = location.longitude
                        print(status.text)
                        print(location.address)
                        print((location.latitude, location.longitude))


                    final_data = [{'user': random_text, 'geo' :{
                                        'latitude': lat,
                                       'longitude' : long
                                       }}]
                    data_string = json.dumps(final_data, sort_keys = True)
                    fileobj = open('data.json', 'w')
                    fileobj.write(data_string)
        
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    listener = StdOutListener()
    auth = OAuthHandler("k2UjjnOtpDGRoWyjYNcJJo1rw", "3HcN7u1Jd0Gdb5iPuH8goyZ7LHzWyxCvhbFonTI82ntag6uApS")
    auth.set_access_token("1041265000659054592-TO9lxogdVoHRlYWxcHFqa52PTJe9nA",
                          "O3wOOdyPxABUkfvSd1CQMBZFZ3DVAUTh0ihfhsw2QuqvW")
    stream = Stream(auth, listener)

    print("Showing all new tweets:")
    # Stream filtering some frequent basque words
    stream.filter(locations=[56.567, -20.522, 73.567, 10.4])



