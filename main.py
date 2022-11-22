from classes import UserTweet
from authorise import obtain_client_object
import click

client = obtain_client_object()
instance = UserTweet(client)

@click.command()
@click.option("--option", prompt = "choose procedure", 
              type = click.Choice(['create','get_tweet']),
              help = "choose the style of tweet")
def user_perform(option):
    if option == 'create':
        instance.tsend_tweet
    elif option == 'get_tweet':
        t_id = input('enter tweet id: ')
        instance.tget_tweet(t_id)

if __name__ == '__main__':
    user_perform()
