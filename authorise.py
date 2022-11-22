from sys import stderr
from os import environ
import tweepy

consumer_key = environ['consumer_key']
client_id = environ['client_id']
consumer_secret = environ['consumer_secret']
client_secret = environ['client_secret']
access_token = environ['access_token']
access_token_secret = environ['access_token_secret']
bearer_token = environ['bearer_token']
redirect_uri = environ['redirect_uri']

oauth2_user_handle = tweepy.OAuth2UserHandler(client_id = client_id,
                                              redirect_uri = redirect_uri,
                                              scope=['tweet.read',
                                                     'tweet.write',
                                                     'users.read',
                                                     'tweet.moderate.write',
                                                     'users.read',
                                                     'follows.read',
                                                     'follows.write',
                                                     'offline.access',
                                                     'space.read',
                                                     'mute.read',
                                                     'mute.write',
                                                     'like.read',
                                                     'like.write'],
                                              client_secret=client_secret)

def obtain_client_object():
    try:
        client = tweepy.Client(return_type = dict,
                               bearer_token = bearer_token, 
                               consumer_key = consumer_key,
                               consumer_secret = consumer_secret,
                               access_token = access_token,
                               access_token_secret = access_token_secret)
    except tweepy.TweepyException as tw:
        stderr.write(f"exception: {tw}")
        stderr.write("exiting..")
        sys.exit()

    return client
