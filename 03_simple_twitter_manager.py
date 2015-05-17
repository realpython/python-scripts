import twitter


TWITTER_CONSUMER_KEY = 'XXX'
TWITTER_CONSUMER_SECRET = 'XXX'
TWITTER_ACCESS_TOKEN_KEY = 'XXX'
TWITTER_ACCESS_TOKEN_SECRET = 'XXX'

twitter_api = twitter.Api(
    consumer_key=TWITTER_CONSUMER_KEY,
    consumer_secret=TWITTER_CONSUMER_SECRET,
    access_token_key=TWITTER_ACCESS_TOKEN_KEY,
    access_token_secret=TWITTER_ACCESS_TOKEN_SECRET
)

if __name__ == '__main__':
    follower_ids = twitter_api.GetFollowerIDs()
    following_ids = twitter_api.GetFriendIDs()
    zombie_follows = [following_id for following_id in
                      following_ids if following_id not in follower_ids]

    confirm = raw_input(
        "Are you sure you want to unfollow {0} tweeps [y|n]? ".format(
            (len(zombie_follows))))
    if confirm.lower() == 'y':
        for id in zombie_follows:
            user = twitter_api.DestroyFriendship(user_id=id)
            print("Unfollowed {0}".format(user.screen_name))
