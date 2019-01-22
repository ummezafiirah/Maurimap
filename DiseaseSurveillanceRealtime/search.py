import json
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

from geopy.geocoders import Nominatim
from analysis import text_analyse
import string
geolocator = Nominatim(user_agent="my-application")

##



#This is the listener, resposible for receiving data
class StdOutListener(StreamListener):

    def on_connect(self):
        print('Stream starting...')


    def on_status(self, status):
        keyword = "flu", "gastro", "conjunctivitis", "respiratory infection", "infectious disease", "diarrhea", "pink eye","got gastro","got flu","coughing","cough","caught cold","fever","headache","sore throat","dizziness","vomiting",
        "stomach pain","cramps","nausea","dehydration","eye redness","itching of eye","eye swelling","eye tearing","sneezing",
        "nasal congestion","runny nose","nasal breathing","diarrhée","conjonctivite","grippe","gastro-entérite","infection respiratoire",
        "maladie infectieuse","grippe","toux","fièvre","maux de tête","douleurs","maux de gorge","vertiges","vomissement","douleurs estomac",
        "crampes","nausées","déshydratation","rougeur des yeux","gonflement des yeux","larmoiement des yeux","éternuements","congestion nasale",
        "nez qui coule","respiration nasale"
        #print decoded
        random_user = ''
        #Check for presence of coordinates
        if status.geo is None:

              for word in keyword:
                if word in status.text:
                    random_text = status.text
                    location_result = text_analyse.extract_location(status.text, 80)
                    print(location_result)
                    # replacing punctuations with whitespace for location_result
                    for char in string.punctuation:
                        s = location_result.replace(char, ' ')
                    # removing numbers from s
                    result = ''.join([i for i in s if not i.isdigit()])
                    location = geolocator.geocode(result + ", Mauritius")
                    if (location.address is not "Mauritius"):
                        lat = location.latitude
                        long = location.longitude
                        print(location.address)
                        print((location.latitude, location.longitude))
                        final_data = [{'user': random_text, 'geo' :{
                                            'latitude': lat,
                                           'longitude' : long
                                           }}]
                        data_string = json.dumps(final_data, sort_keys = True)
                        fileobj = open('data.json', 'w')
                        fileobj.write(data_string)
        #return True
        else:
            for word in keyword:
                if word in status.text:
                    random_text = status.text
                    geo = status.geo.get("coordinates")
                    lat = geo[0]
                    long = geo[1]
                    coordinates = lat, long
                    print(coordinates)
                    final_data = [{'user': random_text, 'geo': {
                        'latitude': lat,
                        'longitude': long
                    }}]
                    data_string = json.dumps(final_data, sort_keys=True)
                    fileobj = open('data.json', 'w')
                    fileobj.write(data_string)

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







