from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from info import data
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="my-application")

# OAuth process
auth = OAuthHandler("k2UjjnOtpDGRoWyjYNcJJo1rw","3HcN7u1Jd0Gdb5iPuH8goyZ7LHzWyxCvhbFonTI82ntag6uApS")
auth.set_access_token("1041265000659054592-TO9lxogdVoHRlYWxcHFqa52PTJe9nA","O3wOOdyPxABUkfvSd1CQMBZFZ3DVAUTh0ihfhsw2QuqvW")

keyword = "flu","gastro","conjunctivitis","respiratory infection","love","hate","christmas"
# listener that handles streaming data
class listener(StreamListener):
    def on_connect(self):
        print('Stream starting...')

    def on_status(self, status):
        if status.geo is not None:
            print("geo text available")
            print(status.text)
            for word in keyword:
                if word in status.text:
                    t = dict()
                    t['text'] = status.text
                    t['coordinates'] = status.coordinates
                    data.append(t)


    def on_error(self, status):
        print(status)




#if __name__ == "__main__":
#    twitterStream = Stream(auth, listener())
#    #twitterStream.filter(locations=[56.71, -21.03, 58.69, -19.09])
#    twitterStream.filter(locations=[-130.78125, -31.3536369415, 140.625, 63.8600358954])

def main():
    twitterStream = Stream(auth, listener())
    twitterStream.filter(locations=[
        -130.78125, -31.3536369415, 140.625, 63.8600358954
    ])