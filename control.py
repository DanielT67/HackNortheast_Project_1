from getLiveTweet import get_live_tweets
from getPastTweets import get_past_tweets

if __name__ == '__main__':
    control_ticker = input("Enter Ticker Symbol for Company: ")
    selection = input("Type \'Live\' to see Live Tweets or type \'Past\' to see past tweets:")
    while selection == True or selection == False:
        if selection == True:
            print("Now viewing live tweets:")
            get_live_tweets(control_ticker)
            break
        if selection == False:
            tweets_to_open = int(input("How many tweets would you like to retrieve? "))
            days_past = int(input("What is the age limit of the tweets in days? "))
            get_past_tweets(control_ticker, tweets_to_open, days_past)
            print("\nAll tweets are stored in a json for easy access.")
            break
