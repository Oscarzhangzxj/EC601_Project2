import re
from nltk.tokenize import WordPunctTokenizer
user_removed = re.sub(r'@[A-Za-z0-9]+','',tweet.decode('utf-8'))
link_removed = re.sub('https?://[A-Za-z0-9./]+','',user_removed)
number_removed = re.sub('[^a-zA-Z]',' ',link_removed)
lower_case_tweet = number_removed.lower()
tok = WordPunctTokenizer()
words = tok.tokenize(lower_case_tweet)
clean_tweet = (' '.join(words)).strip()
def clean_tweets(tweet):
    user_removed = re.sub(r'@[A-Za-z0-9]+','',tweet.decode('utf-8'))
    link_removed = re.sub('https?://[A-Za-z0-9./]+','',user_removed)
    number_removed = re.sub('[^a-zA-Z]', ' ', link_removed)
    lower_case_tweet= number_removed.lower()
    tok = WordPunctTokenizer()
    words = tok.tokenize(lower_case_tweet)
    clean_tweet = (' '.join(words)).strip()
    return clean_tweet



from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
def get_sentiment_score(tweet):
    client = language.LanguageServiceClient()
    document = types\
               .Document(content=tweet,
                         type=enums.Document.Type.PLAIN_TEXT)
    sentiment_score = client\
                      .analyze_sentiment(document=document)\
                      .document_sentiment\
                      .score
    return sentiment_score


score = 0
tweets = search_tweets(keyword, total_tweets)
for tweet in tweets:
    cleaned_tweet = clean_tweets(tweet.text.encode('utf-8'))
for tweet in tweets:
    cleaned_tweet = clean_tweets(tweet.text.encode('utf-8'))
    sentiment_score = get_sentiment_score(cleaned_tweet)
    score += sentiment_score
for tweet in tweets:
    cleaned_tweet = clean_tweets(tweet.text.encode('utf-8'))
    sentiment_score = get_sentiment_score(cleaned_tweet)
    score += sentiment_score
    print('Tweet: {}'.format(cleaned_tweet))
    print('Score: {}\n'.format(sentiment_score))
def analyze_tweets(keyword, total_tweets):
    score = 0
    tweets = search_tweets(keyword, total_tweets)
    for tweet in tweets:
        cleaned_tweet = clean_tweets(tweet.text.encode('utf-8'))
        sentiment_score = get_sentiment_score(cleaned_tweet)
        score += sentiment_score
        print('Tweet: {}'.format(cleaned_tweet))
        print('Score: {}\n'.format(sentiment_score))
    final_score = round((score / float(total_tweets)),2)
    return final_score

keyword = update.message.text
final_score = analyze_tweets(keyword, 50)
if final_score <= -0.25:
    status = 'NEGATIVE ❌'
elif final_score <= 0.25:
    status = 'NEUTRAL ?'
else:
    status = 'POSITIVE ✅'
bot.send_message(chat_id=update.message.chat_id,
                 text='Average score for '
                       + str(keyword)
                       + ' is '
                       + str(final_score)
                       + ' '
                       + status)
def send_the_result(bot, update):
    keyword = update.message.text
    final_score = analyze_tweets(keyword, 50)
    if final_score <= -0.25:
        status = 'NEGATIVE ❌'
    elif final_score <= 0.25:
        status = 'NEUTRAL ?'
    else:
        status = 'POSITIVE ✅'
    bot.send_message(chat_id=update.message.chat_id,
                     text='Average score for '
                           + str(keyword)
                           + ' is '
                           + str(final_score)
                           + ' '
                           + status)
