from geopy.geocoders import Nominatim
from analysis import text_analysetwitter
import string
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
#####United Airlines
# Open/Create a file to append data
#csvFile = open('ua.csv', 'a')
#Use csv Writer
#csvWriter = csv.writer(csvFile)

#keywords to find in tweets
query = 'place:ee9d992aa12a6fa0  flu OR influenza OR coughing OR cough ' \
        'OR gastro OR toux OR gastroenteritis OR diarrhea OR conjunctivitis' \
        'éternuements OR sneezing OR conjonctivite OR pinkEye OR eyeswelling OR fièvre OR grippe OR eyeitching' \
        'diarrhée OR vomissement OR vertiges OR cramps OR crampes OR dizziness' \
        'fever OR vomiting OR eyetearing OR gastro-entérite OR respiratoryInfection OR infectionRespiratoire'


for status in tweepy.Cursor(api.search,q=query\
             ,count=100).items():
     #print(status.geo)
     #print (status.created_at)
     #print("Tweet Text:"+status.text)
     #print("Tweet place:"+status.place.name if status.place else "Undefined place")

     # if location(coordinates) are available >>search for location in tweet
     if (status.geo is None):
         location_result = text_analysetwitter.extract_location(status.text.lower() ,60)
         dis = text_analysetwitter.extract_disease(status.text, 60)


         #replacing punctuations with whitespace for location_result
         for char in string.punctuation:
            s = location_result.replace(char, ' ')
            s1 = dis.replace(char, ' ')
         #removing numbers from s
         locresult = ''.join([i for i in s if not i.isdigit()])
         disresult = ''.join([i for i in s1 if not i.isdigit()])
         #print("disease removing special characters:"+re.sub('[^A-Za-z0-9]+', '', disresult))

         #condition to discard tweets with no location mentionned in it
         if locresult != "":
            #example output: return value('dizziness', 100),influenza
            a,b,c= dis.split(',',3)
            #('dizziness'
            #print(a)
            #100)
            #print(b)
            #influenza
            print("Disease:" + c)
            disease = c

            location = geolocator.geocode(locresult+", Mauritius")
            lat = location.latitude
            long = location.longitude
            #print(location.address)
            #print((location.latitude, location.longitude))
            date = str(status.created_at.date())
            print(date)
            # if (mycol.find_one({"date": status.created_at,"Tweet": status.text}) is None):
             #insertinMongoDBCloud
            #,"location":(location.address)
            mylist = { "diseasetype":(disease),"date":(date),"Tweet": (status.text), "latitude":(location.latitude), "longitude":(location.longitude)}
            connect_db.save_tweet(mylist)
            ##for Local Mongo db
            ##save_data(myList, 'twitter')
            ##x = mycol.insert_one(mylist)

     #if location(coordinates) are available
     else:
        # if (mycol.find_one({"date": status.created_at, "Tweet": status.text}) is None):
             # insertinMongoDB
             dis = text_analysetwitter.extract_disease(status.text.lower(), 60)
        # replacing punctuations with whitespace for location_result
             for char in string.punctuation:
                s = location_result.replace(char, ' ')
                s1 = dis.replace(char, ' ')
                # removing numbers from s
                locresult = ''.join([i for i in s if not i.isdigit()])
                disresult = ''.join([i for i in s1 if not i.isdigit()])

             # example output: return value('dizziness', 100),influenza
             a, b, c = dis.split(',', 3)
             # ('dizziness'
             #print(a)
             # 100)
             #print(b)
             # influenza
             print("Disease:" + c)
             disease = c

             geo = status.geo.get("coordinates")
             lat = geo[0]
             long = geo[1]
             coordinates = lat, long
             ##print(coordinates)
             location = geolocator.reverse(coordinates)
             ##print(location)
             date = str(status.created_at.date())
             print(date)
             ##reverse
             location = geolocator.reverse(coordinates)
             mylist = {"diseasetype":(disease),"date": (date), "Tweet": (status.text),
                       "latitude": (lat), "longitude": (long)}
             connect_db.save_tweet(mylist)

             ##for Local Mongo db
             # x = mycol.insert_one(mylist)

