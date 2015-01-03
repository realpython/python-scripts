import tweepy

# Authentication credentials - dev.twitter.com
cfg = {
    'consumer_key': 'VALUE',
    'consumer_secret': 'VALUE',
    'access_token': 'VALUE',
    'access_token_secret': 'VALUE'
}


def get_api_handler(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)


def main():
    api = get_api_handler(cfg)
    tweet = 'Hello, world from Tweepy!'
    api.update_status(status=tweet)


if __name__ == "__main__":
    main()
