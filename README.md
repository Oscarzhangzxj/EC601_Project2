# EC601_Project2

# Introduction:

My project aims to make it easier for people to find information on public platforms like Twitter and to do sentiment analysis on the content of Twitter texts. Furthermore, this project may be used to investigate current trends on Twitter as well as public attitude on the subject.





# Phase 1

Checking the tweets after discovering them online, update a few test methods, which will be implemented after they are more precisely described. And the Main Program is utilized to interact with API keys and achieve the project's objectives.

# Phase 2
# MVP:
My project can perform sentiment analysis for anyone desiring to determine the trend of information on the social media platform Twitter.
# User Story:
In real time, any tweeter or follower can learn about the most popular content or the hottest topic. Fans follow their favorite singers' real-time updates, such as where the singer has recently performed, what they are wearing, the star's personal life, and factual analysis of a hot topic.

+ As a musician, I want to know how well my new album is received by my fans.
+ As a politician, I am interested in knowing whether or not the public supports my new bill.
+ As the creator of a new product, I am interested in hearing everyone's thoughts on the product and how it feels to use.
# Procedure of building sentiment analyzer
Install the libraries by typing:
>pip3 install tweepy nltk google-cloud-language python-telegram-bot

I create the service account key:
>export GOOGLE_APPLICATION_CREDENTIALS='[PATH_TO_CREDS.JSON]'

Connect to the Twitter API
It means to define the keys that we generated earlier.
```
import tweepy
ACC_TOKEN = 'YOUR_ACCESS_TOKEN'
ACC_SECRET = 'YOUR_ACCESS_TOKEN_SECRET'
CONS_KEY = 'YOUR_CONSUMER_API_KEY'
CONS_SECRET = 'YOUR_CONSUMER_API_SECRET_KEY'
def authentication(cons_key, cons_secret, acc_token, acc_secret):
    auth = tweepy.OAuthHandler(cons_key, cons_secret)
    auth.set_access_token(acc_token, acc_secret)
    api = tweepy.API(auth)
    return api
```
The program using Google's score range, indicate if a certain score is negative, neutral, or favorable.
<img width="522" alt="image" src="https://user-images.githubusercontent.com/112965000/196082885-7a1e48ae-48fe-4a5f-b2af-ebbb95e1483f.png">

The subsequent step is rather straightforward. I have added the source code, so all that remains is to search for tweets, extract their sentiment, and evaluate them. Once the software transmits the score, we will obtain the text's score.

# Outcome of the program
Here is a snapshot of the application we must use to assess the user's phrase. Additionally, it can determine the tone of the writing. And we have their outcomes. Clearly, we have obtained the desired results by debugging the API, and we can deduce a sequence of answers from the user's words.
<img width="695" alt="image" src="https://user-images.githubusercontent.com/112965000/196082636-47e20e14-fa9a-4dc9-a2eb-55bf80904bb4.png">


