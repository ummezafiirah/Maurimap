from geopy.geocoders import Nominatim
from analysis import text_analysetwitter
import string
import warnings
warnings.filterwarnings("ignore")
import pymongo
import re
import datetime
#import connect_db to connect to cloud
from seachAPI import connect_db
geolocator = Nominatim(user_agent="my-application")
# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

#Import the tweepy library
import tweepy
import pymongo

#to connect to local mongo db
#myclient = pymongo.MongoClient('mongodb://localhost:27017/')
#db = myclient['twitter_db']
#collection = db['twitter_collection']


# Variables that contains the user credentials to access Twitter API
ACCESS_TOKEN = ''
ACCESS_SECRET = ''
CONSUMER_KEY = ''
CONSUMER_SECRET = ''

# Setup tweepy to authenticate with Twitter credentials:
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True)

#keywords to find in tweets
query = 'place:ee9d992aa12a6fa0  flu OR influenza OR coughing OR cough ' \
        'OR gastro OR toux OR gastroenteritis OR diarrhea OR conjunctivitis' \
        'éternuements OR sneezing OR conjonctivite OR fièvre OR grippe OR vomiting' \
        'diarrhée OR vomissement OR vertiges OR cramps OR crampes OR dizziness' \
        'fever OR gastro-entérite OR (pink AND eye) OR(respiratory AND Infection) OR (infection AND Respiratoire)'


for status in tweepy.Cursor(api.search,q=query\
             ,count=100).items():

     #print("Tweet Text:"+status.text)
     #print(status.geo)

     # if location(coordinates) are available >>search for location in tweet
     if (status.geo is None):
         print("geography is None")


         location_result = text_analysetwitter.extract_location(status.text.lower() ,90)
         dis = text_analysetwitter.extract_disease(status.text.lower(), 60)

         #replacing punctuations with whitespace for location_result and tweet
         for char in string.punctuation:
            s = location_result.replace(char, ' ')
            s1 = dis.replace(char, ' ')
         #removing numbers from location_result and tweet
         locresult = ''.join([i for i in s if not i.isdigit()])
         disresult = ''.join([i for i in s1 if not i.isdigit()])

         #location mentionned in tweet
         if locresult != "":
            values = dis.split(',')
            disease = values[-1]
            #get latitude and longitude of mentionned location in tweet using Nominatim
            location = geolocator.geocode(locresult+", Mauritius")
            lat = location.latitude
            long = location.longitude
            date = str(status.created_at.date())
            #inserting in MongoDB Cloud
            mylist = { "diseasetype":(disease),"date":(date),"Tweet": (status.text), "latitude":(location.latitude), "longitude":(location.longitude)}
            connect_db.save_tweet(mylist)

         if locresult == "":
             print("Location not found in tweet!!!")
             print("location")
             print(location_result)
             print("disease")
             print(dis)
             values = dis.split(',')
             disease = values[-1]
             date = str(status.created_at.date())
             print(date)
             latitude = "not found"
             longitude = "not found"
             mylist = {"diseasetype": (disease), "date": (date), "Tweet": (status.text),
                       "latitude": (latitude), "longitude": (longitude)}
             connect_db.save_tweet(mylist)


     #if location(coordinates) are available
     else:
             #print("geography is Available")
        # if (mycol.find_one({"date": status.created_at, "Tweet": status.text}) is None):
             # insertinMongoDB
             dis = text_analysetwitter.extract_disease(status.text.lower(), 60)
             #print(dis)
        # replacing punctuations with whitespace for location_result
             for char in string.punctuation:
                s1 = dis.replace(char, ' ')
                # removing numbers from s
                disresult = ''.join([i for i in s1 if not i.isdigit()])

             # example output: return value('dizziness', 100),influenza
             #a, b, c = dis.split(',', 3)
             values = dis.split(',')
             disease = values[-1]

             # ('dizziness'
             #print(a)
             # 100)
             #print(b)
             # influenza

             geo = status.geo.get("coordinates")
             lat = geo[0]
             long = geo[1]
             coordinates = lat, long
             ##print(coordinates)
             location = geolocator.reverse(coordinates)
             ##print(location)


             date = str(status.created_at.date())
             ##reverse
             location = geolocator.reverse(coordinates)


             #LOCATION COORDINATES ARE AVAILABLE
             print("DISEASE:")
             print(disease)
             print("TWEET:")
             print(status.text)
             print("DATE:")
             print(date)
             print("COORDINATES:")
             print(geo)

             mylist = {"diseasetype":(disease),"date": (date), "Tweet": (status.text),
                       "latitude": (lat), "longitude": (long)}
             connect_db.save_tweet(mylist)

             ##for Local Mongo db
             # x = mycol.insert_one(mylist)
