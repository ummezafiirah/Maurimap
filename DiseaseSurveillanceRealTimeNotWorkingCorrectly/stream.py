from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from info import data
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="my-application")

# OAuth process
auth = OAuthHandler("","")
auth.set_access_token("","")

# listener that handles streaming data
class listener(StreamListener):
    def on_connect(self):
        print('Stream starting...')

    def on_status(self, status):
        if status.geo is not None:
            t = dict()
            print(status.text)
            print(status.geo)
            geo=status.geo.get("coordinates")
            lat=geo[0]
            long=geo[1]
            coordinates = lat,long
            print(coordinates)
            location = geolocator.reverse(coordinates)
            print(location)
            t['text'] = status.text
            t['coordinates'] = status.coordinates
            data.append(t)

    def on_error(self, status):
        print(status)


#def main():
if __name__ == "__main__":
    twitterStream = Stream(auth, listener())
    twitterStream.filter(locations=[
        -130.78125, -31.3536369415, 140.625, 63.8600358954
    ])
