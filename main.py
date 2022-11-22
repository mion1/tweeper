from classes import UserTweet
from authorise import obtain_client_object
import click


client = obtain_client_object()
instance = UserTweet(client)

@click.group()
@click.option('--n', type = click.Choice(['create_tweet', 'get_tweet']))
@click.pass_context
def main(n: str = ''):
    user_option = n


@main.command()
@click.pass_context
def send_tweet(user_option):
    if user_option == 'create_tweet':
        tsend_tweet

if __name__ == '__main__':
    main()
