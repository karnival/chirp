#!/usr/local/bin/python

import sys
import twitter
import keys

def main():
    api = twitter.Api(consumer_key=keys.consumer_key,
                      consumer_secret=keys.consumer_secret,
                      access_token_key=keys.access_token_key,
                      access_token_secret=keys.access_token_secret)

    tweet = ' '.join(sys.argv[1:])
    if len(tweet) > 0 and len(tweet) <= 140:
        api.PostUpdate(tweet)
        print('Posted: ' + tweet)
    elif len(tweet) == 0:
        print('No tweet found to post.')
    elif len(tweet) > 140:
        print('Tweet too long.')

if __name__ == "__main__":
    main()
