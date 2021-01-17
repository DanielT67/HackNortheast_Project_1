from getLiveTweet import get_live_tweets
from getPastTweets import get_past_tweets

if __name__ == '__main__':
    stockName = request.form['text']
    isLive = request.form['isLive']
    if isLive == True:
        print("Now viewing live tweets:")
        get_live_tweets(stockName)
    else:
        tweets_to_open = request.form['tweets_to_open']
        days_past = request.form['days_past']
        get_past_tweets(stockName, int(tweets_to_open), int(days_past))
        print("\nAll tweets are stored in a json for easy access.")

