#!/usr/local/bin/python

import sys
import twitter
import argparse 

# OAuth keys for account and API access.
import keys

def main(args):
    api = twitter.Api(consumer_key=keys.consumer_key,
                      consumer_secret=keys.consumer_secret,
                      access_token_key=keys.access_token_key,
                      access_token_secret=keys.access_token_secret)

    tweet = ' '.join(args.message)

    if not args.long:
        try:
            status = api.PostUpdate(tweet)
            print('Posted: ' + tweet)
        except twitter.error.TwitterError:
            if len(tweet) == 0:
                print('No tweet found to post.')
            elif len(tweet) > 0 and len(tweet) < 140:
                print("Unexpected error posting. Invalid character?")
            elif len(tweet) > 140:
                print('Tweet too long, consider using -l.')
    elif args.long:
        status = api.PostUpdates(tweet, continuation='/')
        print('Posted long message over ' + str(len(status)) + ' tweets.')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Post tweets from the command'
                                                 ' line.')
    parser.add_argument('-l', '--long', action='store_true',
                        help='Post a longer (>140 chars) message over several '
                             'tweets.')
    parser.add_argument('-m', '--message', nargs='*', required=True,
                        help='Message to post. Advisable to enclose in'
                             ' quotation marks.')
    args = parser.parse_args()
    main(args)
