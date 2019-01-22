from geopy.geocoders import Nominatim
from analysis import text_analyse
import string
import pymongo
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
#print(myclient.list_database_names())
mydb = myclient['myproject']
mycol = mydb["tweets"]

geolocator = Nominatim(user_agent="my-application")
# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the tweepy library
import tweepy
import pymongo
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
db = myclient['twitter_db']
collection = db['twitter_collection']


# Variables that contains the user credentials to access Twitter API
ACCESS_TOKEN = '1041265000659054592-TO9lxogdVoHRlYWxcHFqa52PTJe9nA'
ACCESS_SECRET = 'O3wOOdyPxABUkfvSd1CQMBZFZ3DVAUTh0ihfhsw2QuqvW'
CONSUMER_KEY = 'k2UjjnOtpDGRoWyjYNcJJo1rw'
CONSUMER_SECRET = '3HcN7u1Jd0Gdb5iPuH8goyZ7LHzWyxCvhbFonTI82ntag6uApS'

# Setup tweepy to authenticate with Twitter credentials:

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
#csvFile = open('ua.csv', 'a')
#Use csv Writer
#csvWriter = csv.writer(csvFile)

query = 'place:ee9d992aa12a6fa0  influenza OR gotflu OR coughing OR cough OR caughtcold ' \
        'OR gastro OR toux OR gastroenteritis OR gas OR diarrhea OR gotgastro OR conjunctivitis' \
        'éternuements OR sneezing OR conjonctivite OR eyeswelling OR flu OR fièvre OR grippe OR eyeitching' \
        'diarrhée OR vomissement OR vertiges OR stomachpain OR cramps OR dizziness OR sorethroat OR headache' \
        'fever OR vomiting OR eyetearing OR runnynose OR gastro-entérite OR déshydratation OR rougeurdesyeux'


for status in tweepy.Cursor(api.search,q=query\
             ,count=100).items():
     #print(status.geo)
     #print (status.created_at)
     #print("Tweet Text:"+status.text)
     #print("Tweet place:"+status.place.name if status.place else "Undefined place")
     if (status.geo is None):
         location_result = text_analyse.extract_location(status.text ,80)

         #replacing punctuations with whitespace for location_result
         for char in string.punctuation:
            s = location_result.replace(char, ' ')
         #removing numbers from s
         result = ''.join([i for i in s if not i.isdigit()])

         location = geolocator.geocode(result+", Mauritius")
         lat = location.latitude
         long = location.longitude
         print(location.address)
         print((location.latitude, location.longitude))

         if (mycol.find_one({"date": status.created_at,"Tweet": status.text}) is None):
             #insertinMongoDB
             mylist = { "date":(status.created_at),"Tweet": (status.text), "address": (location.address), "latitude":(location.latitude), "longitude":(location.longitude)}
             x = mycol.insert_one(mylist)

     else:
         if (mycol.find_one({"date": status.created_at, "Tweet": status.text}) is None):
             # insertinMongoDB
             geo = status.geo.get("coordinates")
             lat = geo[0]
             long = geo[1]
             coordinates = lat, long
             print(coordinates)
             location = geolocator.reverse(coordinates)
             print(location)

             ##reverse
             location = geolocator.reverse(coordinates)
             mylist = {"date": (status.created_at), "Tweet": (status.text), "address": (location),
                       "latitude": (lat), "longitude": (long)}
             x = mycol.insert_one(mylist)



#for x in mycol.find({}, {"_id": 0, "date": 1, "Tweet": 1}):
 #   print(x)
