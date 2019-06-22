import GetOldTweets3
retweetcheck = 
username = input("Enter Username: ")
while True:
  twitterSearchTerms = GetOldTweets3.manager.TweetCriteria()\
    .setUsername(username)\
    .setMaxTweets(100)
  twitterData = GetOldTweets3.manager.TweetManager.getTweets(twitterSearchTerms)
  totalRetweets = 0
  for tweet in twitterData:
    totalRetweets = totalRetweets + tweet.retweets
    ttweet = tweet

  if int(totalRetweets) != retweetcheck:
    print(totalRetweets)
    print("\n")
    retweetcheck = int(totalRetweets)
  else:pass
