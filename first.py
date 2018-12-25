from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


# # # # TWITTER STREAMER # # # #
class TwitterStreamer():
    """
    Class for streaming and processing live tweets.
    """

    def __init__(self):
        pass

    def stream_tweets(self, fetched_tweets_filename):
        # This handles Twitter authetification and the connection to Twitter Streaming API
        listener = StdOutListener(fetched_tweets_filename)
        auth = OAuthHandler("k2UjjnOtpDGRoWyjYNcJJo1rw", "3HcN7u1Jd0Gdb5iPuH8goyZ7LHzWyxCvhbFonTI82ntag6uApS")
        auth.set_access_token("1041265000659054592-TO9lxogdVoHRlYWxcHFqa52PTJe9nA",
                              "O3wOOdyPxABUkfvSd1CQMBZFZ3DVAUTh0ihfhsw2QuqvW")
        stream = Stream(auth, listener)

        # This line filter Twitter Streams to capture data by the keywords:
        stream.filter(locations=[56.567, -20.522, 73.567, 10.4])


# # # # TWITTER STREAM LISTENER # # # #
class StdOutListener(StreamListener):

    """
    This is a basic listener that just prints received tweets to stdout.
    """

    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        keyword = "flu","influenza","conjunctivitis","rain","trump","hillary clinton","rain"
        try:
             for word in keyword:
                    if word in data:
                        print(data)
                        with open(self.fetched_tweets_filename, 'a') as tf:
                            tf.write(data)
                            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    # Authenticate using config.py and connect to Twitter Streaming API.
    fetched_tweets_filename = "tweets.txt"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename)
