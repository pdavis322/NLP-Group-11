# NLPCodeProgress.py
# 4/11/2019

# author: NLP Group 11

# MATLAB STUFF # 
# matlab.engine.start_matlab();
# matlab.engine.find_matlab();
# eng=matlab.engine.connect_matlab();
# import matlab.engine;


## import statements

import nltk
import json
import tweepy
from nltk.tokenize.toktok import ToktokTokenizer
from random import randint

######################FUNCTION THAT GETS TWEETS FROM SPECIFIED USER OR HASHTAG#################################################
## PORTION 1 ##

# returns array of tweets to be put into a dictionary
def get_tweets(user, query):
    credentials = {}
    credentials['CONSUMER_KEY'] = 'qveFJi1yOD0H6xX7988lr6cB3'
    credentials['CONSUMER_SECRET'] = 'NkwwgQR0DYEcvg1m3vOZ1akHrNuNU4htlPfqtsK0Aov7b4qmX1'
    credentials['ACCESS_TOKEN'] = '1096111564351070210-Kz1S00wktxSNY4Ppfwj1FoiOIrTqXq'
    credentials['ACCESS_SECRET'] = 'lqWBazFnpeHnfKE0bDBvfhVgK0Wny0qPSN6e3zl0HVAtQ'

    with open("twitter_credentials.json", "w") as file:
        json.dump(credentials, file)

    auth = tweepy.OAuthHandler(credentials['CONSUMER_KEY'], credentials['CONSUMER_SECRET'])
    auth.set_access_token(credentials['ACCESS_TOKEN'], credentials['ACCESS_SECRET'])

    api = tweepy.API(auth)

    user_or_hashtag = user

    user = query

    hashtag = query

    trump_tweets = []

    if user_or_hashtag == 0:
        trump = api.get_user(user)
        # returns array of status objects
        tweet_statuses = api.user_timeline(trump.id, tweet_mode='extended', count='200', exclude_replies='true',
                                           include_rts='false', include_entities='false')
        for t in tweet_statuses:
            added_tweet = t.full_text
            if added_tweet[:4] != 'http':
                trump_tweets.append(added_tweet)
    else:
        search_results = api.search(hashtag, tweet_mode='extended', count='200', include_rts='false')
        for t in search_results:
            added_tweet = t.full_text
            if added_tweet[:4] != 'http':
                trump_tweets.append(added_tweet)
    return trump_tweets;


################################BUILDS TOKEN DICTIONARY TO BE USED FOR SENTENCE GENERATION#########################################
## PORTION 2 ##

#returns dictionary. This is still being worked on to filter out parts of tweets that we do not want to tokenize.
def build_dictionary(body_arr, n):
    # body is the data gathered from twitter, n is the number of previous words to be considered.

    # this is what the function will return once the dictionary has been assembled.

    tokenizer = ToktokTokenizer()

    raw_tokens = []  # our list of tokens to be added to dictionary

    # tokenize all of our tweets one at a time
    for tweet in body_arr:
        raw_tokens = raw_tokens + tokenizer.tokenize(tweet)



    tokens = [word for word in raw_tokens if not ('http' in word or '#' in word or '@' in word or 'RT' in word \
                                                  or '&amp' in word or ':' in word)]


    token_dict = {}

    post_words = n
    
    for i in range(len(tokens) - post_words):  # runs through all the words in our token list
        temp_str = ''
        temp_list = []  # allows us to have our dictionary values be lists of strings
        for j in range(1, post_words + 1):
                temp_str += tokens[i + j] + ' '
        temp_list.append(temp_str[0:len(temp_str) - 1])

        if tokens[i] in token_dict:
            token_dict[tokens[i]].append(temp_str[0:len(temp_str) - 1])
        else:
            token_dict[tokens[i]] = temp_list
    if tokens[-1] not in token_dict:
        token_dict[tokens[-1]] = ['.']

    return token_dict

#################################Builds our exportable tweet based off dictionary###################################

#this is not complete and needs more work to make sentences more intelligent


def gen_tweet(dictionary):
    tweet = ''
    sentence = []

    if 'I' in dictionary:
        first_word = dictionary['I'][randint(0, len(dictionary['I']) - 1)]
    else: 
        first_word = dictionary['the'][randint(0, len(dictionary['the']) - 1)]
    sentence.append(first_word)
    # 100 tokens
    for i in range(1, 100):
        previous_word = sentence[i - 1]
        second_word = previous_word.rpartition(' ')[2]
        new_word = dictionary[second_word][randint(0, len(dictionary[second_word]) - 1)]
        sentence.append(new_word)

    for i in range(len(sentence)):
        tweet += sentence[i] + ' '
    return 'I ' + tweet

##################################Tweets the completed string out using our twitter account##############################
## PORTION 2 ##

def tweet_generated(gen_tweet):
    credentials = {}
    credentials['CONSUMER_KEY'] = 'qveFJi1yOD0H6xX7988lr6cB3'
    credentials['CONSUMER_SECRET'] = 'NkwwgQR0DYEcvg1m3vOZ1akHrNuNU4htlPfqtsK0Aov7b4qmX1'
    credentials['ACCESS_TOKEN'] = '1096111564351070210-Kz1S00wktxSNY4Ppfwj1FoiOIrTqXq'
    credentials['ACCESS_SECRET'] = 'lqWBazFnpeHnfKE0bDBvfhVgK0Wny0qPSN6e3zl0HVAtQ'
    with open("twitter_credentials.json", "w") as file:
        json.dump(credentials, file)

    auth = tweepy.OAuthHandler(credentials['CONSUMER_KEY'], credentials['CONSUMER_SECRET'])
    auth.set_access_token(credentials['ACCESS_TOKEN'], credentials['ACCESS_SECRET'])

    api = tweepy.API(auth)

    api.update_status(gen_tweet)


def process_tweet(tweet):
    tweet = tweet.replace(' \' ', '\'').replace(' ’ ', '’').replace(' , ', ', ').replace(' ! ', '! ')
    return tweet + '.'
    



def final_tweet(user, userOr): 
    tweets = get_tweets(user, userOr)
    gen_dict = build_dictionary(tweets, 3)
    generated_tweet = gen_tweet(gen_dict)
    final_tweet = process_tweet(generated_tweet)
    return final_tweet



