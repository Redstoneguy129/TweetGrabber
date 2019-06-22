import GetOldTweets3
from time import sleep as sp
maxtweets = 1
username = input("Enter Twitter Account: ")
oldtweet = "undefined"
while True:
  twitterSearchTerms = GetOldTweets3.manager.TweetCriteria()\
    .setUsername(username)\
    .setMaxTweets(maxtweets)
  twitterData = GetOldTweets3.manager.TweetManager.getTweets(twitterSearchTerms)
  if twitterData[0].text != oldtweet:
    for i in range(maxtweets):
      print("\n")
      oldtweet = twitterData[i].text
      print(twitterData[i].text)
  else:pass
