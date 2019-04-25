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

    tokens = []  # our list of tokens to be added to dictionary

    # tokenize all of our tweets one at a time
    for tweet in body_arr:
        tokens = tokens + tokenizer.tokenize(tweet)

    # throw out unwanted tokens
    target_words = ['http', 'https', '@', 'RT', '&amp', '#', 't.co']
    for tok in tokens:
        for target in target_words:
            if target in tok.lower():
                while tok in tokens: tokens.remove(tok)

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
    return tweet
    

################################TESTING################################

# steve jobs commencement speech for testing
samp_text = '''It started before I was born. My biological mother was a young, unwed college graduate student, and she decided to put me up for adoption. She felt very strongly that I should be adopted by college graduates, so everything was all set for me to be adopted at birth by a lawyer and his wife. Except that when I popped out they decided at the last minute that they really wanted a girl. So my parents, who were on a waiting list, got a call in the middle of the night asking: “We have an unexpected baby boy; do you want him?” They said: “Of course.” My biological mother later found out that my mother had never graduated from college and that my father had never graduated from high school. She refused to sign the final adoption papers. She only relented a few months later when my parents promised that I would someday go to college.

And 17 years later I did go to college. But I naively chose a college that was almost as expensive as Stanford, and all of my working-class parents’ savings were being spent on my college tuition. After six months, I couldn’t see the value in it. I had no idea what I wanted to do with my life and no idea how college was going to help me figure it out. And here I was spending all of the money my parents had saved their entire life. So I decided to drop out and trust that it would all work out OK. It was pretty scary at the time, but looking back it was one of the best decisions I ever made. The minute I dropped out I could stop taking the required classes that didn’t interest me, and begin dropping in on the ones that looked interesting.

It wasn’t all romantic. I didn’t have a dorm room, so I slept on the floor in friends’ rooms, I returned Coke bottles for the 5¢ deposits to buy food with, and I would walk the 7 miles across town every Sunday night to get one good meal a week at the Hare Krishna temple. I loved it. And much of what I stumbled into by following my curiosity and intuition turned out to be priceless later on. Let me give you one example:

Reed College at that time offered perhaps the best calligraphy instruction in the country. Throughout the campus every poster, every label on every drawer, was beautifully hand calligraphed. Because I had dropped out and didn’t have to take the normal classes, I decided to take a calligraphy class to learn how to do this. I learned about serif and sans serif typefaces, about varying the amount of space between different letter combinations, about what makes great typography great. It was beautiful, historical, artistically subtle in a way that science can’t capture, and I found it fascinating.

None of this had even a hope of any practical application in my life. But 10 years later, when we were designing the first Macintosh computer, it all came back to me. And we designed it all into the Mac. It was the first computer with beautiful typography. If I had never dropped in on that single course in college, the Mac would have never had multiple typefaces or proportionally spaced fonts. And since Windows just copied the Mac, it’s likely that no personal computer would have them. If I had never dropped out, I would have never dropped in on this calligraphy class, and personal computers might not have the wonderful typography that they do. Of course it was impossible to connect the dots looking forward when I was in college. But it was very, very clear looking backward 10 years later.

Again, you can’t connect the dots looking forward; you can only connect them looking backward. So you have to trust that the dots will somehow connect in your future. You have to trust in something — your gut, destiny, life, karma, whatever. This approach has never let me down, and it has made all the difference in my life.

My second story is about love and loss.

I was lucky — I found what I loved to do early in life. Woz and I started Apple in my parents’ garage when I was 20. We worked hard, and in 10 years Apple had grown from just the two of us in a garage into a $2 billion company with over 4,000 employees. We had just released our finest creation — the Macintosh — a year earlier, and I had just turned 30. And then I got fired. How can you get fired from a company you started? Well, as Apple grew we hired someone who I thought was very talented to run the company with me, and for the first year or so things went well. But then our visions of the future began to diverge and eventually we had a falling out. When we did, our Board of Directors sided with him. So at 30 I was out. And very publicly out. What had been the focus of my entire adult life was gone, and it was devastating.

I really didn’t know what to do for a few months. I felt that I had let the previous generation of entrepreneurs down — that I had dropped the baton as it was being passed to me. I met with David Packard and Bob Noyce and tried to apologize for screwing up so badly. I was a very public failure, and I even thought about running away from the valley. But something slowly began to dawn on me — I still loved what I did. The turn of events at Apple had not changed that one bit. I had been rejected, but I was still in love. And so I decided to start over.

I didn’t see it then, but it turned out that getting fired from Apple was the best thing that could have ever happened to me. The heaviness of being successful was replaced by the lightness of being a beginner again, less sure about everything. It freed me to enter one of the most creative periods of my life.

During the next five years, I started a company named NeXT, another company named Pixar, and fell in love with an amazing woman who would become my wife. Pixar went on to create the world’s first computer animated feature film, Toy Story, and is now the most successful animation studio in the world. In a remarkable turn of events, Apple bought NeXT, I returned to Apple, and the technology we developed at NeXT is at the heart of Apple’s current renaissance. And Laurene and I have a wonderful family together.

I’m pretty sure none of this would have happened if I hadn’t been fired from Apple. It was awful tasting medicine, but I guess the patient needed it. Sometimes life hits you in the head with a brick. Don’t lose faith. I’m convinced that the only thing that kept me going was that I loved what I did. You’ve got to find what you love. And that is as true for your work as it is for your lovers. Your work is going to fill a large part of your life, and the only way to be truly satisfied is to do what you believe is great work. And the only way to do great work is to love what you do. If you haven’t found it yet, keep looking. Don’t settle. As with all matters of the heart, you’ll know when you find it. And, like any great relationship, it just gets better and better as the years roll on. So keep looking until you find it. Don’t settle.

My third story is about death.

When I was 17, I read a quote that went something like: “If you live each day as if it was your last, someday you’ll most certainly be right.” It made an impression on me, and since then, for the past 33 years, I have looked in the mirror every morning and asked myself: “If today were the last day of my life, would I want to do what I am about to do today?” And whenever the answer has been “No” for too many days in a row, I know I need to change something.

Remembering that I’ll be dead soon is the most important tool I’ve ever encountered to help me make the big choices in life. Because almost everything — all external expectations, all pride, all fear of embarrassment or failure — these things just fall away in the face of death, leaving only what is truly important. Remembering that you are going to die is the best way I know to avoid the trap of thinking you have something to lose. You are already naked. There is no reason not to follow your heart.

About a year ago I was diagnosed with cancer. I had a scan at 7:30 in the morning, and it clearly showed a tumor on my pancreas. I didn’t even know what a pancreas was. The doctors told me this was almost certainly a type of cancer that is incurable, and that I should expect to live no longer than three to six months. My doctor advised me to go home and get my affairs in order, which is doctor’s code for prepare to die. It means to try to tell your kids everything you thought you’d have the next 10 years to tell them in just a few months. It means to make sure everything is buttoned up so that it will be as easy as possible for your family. It means to say your goodbyes.

I lived with that diagnosis all day. Later that evening I had a biopsy, where they stuck an endoscope down my throat, through my stomach and into my intestines, put a needle into my pancreas and got a few cells from the tumor. I was sedated, but my wife, who was there, told me that when they viewed the cells under a microscope the doctors started crying because it turned out to be a very rare form of pancreatic cancer that is curable with surgery. I had the surgery and I’m fine now.

This was the closest I’ve been to facing death, and I hope it’s the closest I get for a few more decades. Having lived through it, I can now say this to you with a bit more certainty than when death was a useful but purely intellectual concept:

No one wants to die. Even people who want to go to heaven don’t want to die to get there. And yet death is the destination we all share. No one has ever escaped it. And that is as it should be, because Death is very likely the single best invention of Life. It is Life’s change agent. It clears out the old to make way for the new. Right now the new is you, but someday not too long from now, you will gradually become the old and be cleared away. Sorry to be so dramatic, but it is quite true.

Your time is limited, so don’t waste it living someone else’s life. Don’t be trapped by dogma — which is living with the results of other people’s thinking. Don’t let the noise of others’ opinions drown out your own inner voice. And most important, have the courage to follow your heart and intuition. They somehow already know what you truly want to become. Everything else is secondary.

When I was young, there was an amazing publication called The Whole Earth Catalog, which was one of the bibles of my generation. It was created by a fellow named Stewart Brand not far from here in Menlo Park, and he brought it to life with his poetic touch. This was in the late 1960s, before personal computers and desktop publishing, so it was all made with typewriters, scissors and Polaroid cameras. It was sort of like Google in paperback form, 35 years before Google came along: It was idealistic, and overflowing with neat tools and great notions.

Stewart and his team put out several issues of The Whole Earth Catalog, and then when it had run its course, they put out a final issue. It was the mid-1970s, and I was your age. On the back cover of their final issue was a photograph of an early morning country road, the kind you might find yourself hitchhiking on if you were so adventurous. Beneath it were the words: “Stay Hungry. Stay Foolish.” It was their farewell message as they signed off. Stay Hungry. Stay Foolish. And I have always wished that for myself. And now, as you graduate to begin anew, I wish that for you.

Stay Hungry. Stay Foolish.

Thank you all very much.'''

#samp_array = [samp_text]

#samp_dictionary = build_dictionary(samp_array, 4) #change this number for varying acuracy (2 - 4 reccomended)
#print(samp_dictionary)

# samp_tweet = gen_tweet(samp_dictionary)
# print('I '+ samp_tweet)
def final_tweet(user, userOr):
    samp_array = get_tweets(user, userOr)
#print(samp_array)
    samp_dict = build_dictionary(samp_array, 2)
#print(samp_dict)

    samp_text = gen_tweet(samp_dict)

    processed_text = process_tweet(samp_text)

    return processed_text


