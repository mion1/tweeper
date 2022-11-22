import tweepy, json
import sys

class UserTweet:

    def __init__(self, client):
        self.client = client

    @property
    def tsend_tweet(self):
        user_text = input("tweet: ")
        r_id = input('id of the tweet to reply to: ') or None

        try:
            response = self.client.create_tweet(text = user_text, 
                                                in_reply_to_tweet_id = r_id,
                                                user_auth = True)

        except tweepy.errors.TooManyRequests:
            sys.stderr.write("429 too many requests!")
            sys.exit()

        except tweepy.errors.TweepyException as t:
            sys.stderr.write(f"error: {t}\n")
            sys.exit()

        sys.stdout.write(f"id of the tweet: {response['data']['id']}\n")
        
    def tget_tweet(self, t_id):

        try:
            response = self.client.get_tweet(t_id,
                                             tweet_fields=["created_at",
                                                           "attachments",
                                                           "referenced_tweets",
                                                           "source","author_id",
                                                           "context_annotations"
                                                           ,"conversation_id",
                                                           "edit_controls",
                                                           "edit_history_tweet_ids"
                                                           ,"entities","geo,id",
                                                           "in_reply_to_user_id",
                                                           "lang",
                                                           "possibly_sensitive",
                                                           "public_metrics",
                                                           "reply_settings",
                                                           "text","withheld"
                                                           ],
                                             media_fields = ["url","height",
                                                             "width","alt_text",
                                                             "duration_ms",
                                                             "media_key",
                                                             "preview_image_url"
                                                             ,"promoted_metrics"
                                                             ,"public_metrics",
                                                             "type","variants"],
                                             expansions =
                                             ["referenced_tweets.id",
                                              "attachments.media_keys"],
                                             user_auth = True)
        
        except tweepy.errors.TweepyException as t:
            sys.stderr.write(f"error: {t}\n")
            sys.exit()
    
        json_output = json.dumps(response, indent = 8)
        sys.stdout.write(json_output)

