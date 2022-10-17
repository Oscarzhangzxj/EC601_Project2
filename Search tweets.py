from datetime import datetime, timedelta

today_datetime = datetime.today().now()
yesterday_datetime = today_datetime - timedelta(days=1)
today_date = today_datetime.strftime('%Y-%m-%d')
yesterday_date = yesterday_datetime.strftime('%Y-%m-%d')
api = authentication(CONS_KEY,CONS_SECRET,ACC_TOKEN,ACC_SECRET)
search_result = tweepy.Cursor(api.search,
                              q=keyword,
                              since=yesterday_date,
                              result_type='recent',
                              lang='en').items(total_tweets)
def search_tweets(keyword, total_tweets):
    today_datetime = datetime.today().now()
    yesterday_datetime = today_datetime - timedelta(days=1)
    today_date = today_datetime.strftime('%Y-%m-%d')
    yesterday_date = yesterday_datetime.strftime('%Y-%m-%d')
    api = authentication(CONS_KEY,CONS_SECRET,ACC_TOKEN,ACC_SECRET)
    search_result = tweepy.Cursor(api.search,
                                  q=keyword,
                                  since=yesterday_date,
                                  result_type='recent',
                                  lang='en').items(total_tweets)
    return search_result