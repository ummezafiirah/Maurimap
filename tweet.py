from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


class StdOutListener(StreamListener):


    def on_data(self, data):

            print(data)
            return True


    def on_error(self, status):
        print(status)

#Consumer API keys
#k2UjjnOtpDGRoWyjYNcJJo1rw (API key)
#3HcN7u1Jd0Gdb5iPuH8goyZ7LHzWyxCvhbFonTI82ntag6uApS (API secret key)
#Access token & access token secret
#1041265000659054592-TO9lxogdVoHRlYWxcHFqa52PTJe9nA (Access token)
#O3wOOdyPxABUkfvSd1CQMBZFZ3DVAUTh0ihfhsw2QuqvW (Access token secret)

if __name__ == "__main__":
    listener = StdOutListener()
    auth = OAuthHandler("","")
    auth.set_access_token("","")
    stream = Stream(auth, listener)
    #stream.filter(track=['flu'],locations=[-122.75,36.8,-121.75,37.8])
    #stream.filter(locations=[-10.087854,-20.745840,63.808594,56.315918])
    stream.filter(locations=[56.71, -21.03, 58.69, -19.09])

    #hello there my name is zafii:)
