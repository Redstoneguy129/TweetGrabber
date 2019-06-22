import GetOldTweets3
from textProcessing import *
username = input("Enter Username: ")
twitterSearchTerms = GetOldTweets3.manager.TweetCriteria()\
  .setUsername(username)\
  .setMaxTweets(10)
twitterData = GetOldTweets3.manager.TweetManager.getTweets(twitterSearchTerms)
print("Tweet:")
print(twitterData[0].text)
print("\n")
positiveWordList = loadFile('positive-words.txt')
negativeWordList = loadFile('negative-words.txt')
splitTweet = divideTweet(twitterData[0])
print("Tweet split into words:")
print(splitTweet)
print("\n")
positiveScore = 0
negativeScore = 0
for testWord in splitTweet:
  if testWord in positiveWordList:
    positiveScore = positiveScore + 1
  if testWord in negativeWordList:
    negativeScore = negativeScore + 1
print("Positive Score: " + str(positiveScore))
print("Negative Score: " + str(negativeScore))
if positiveScore > 5 and negativeScore > 5:
  print("This is a emotionaly Edgy Person, Nothing to see here")
elif positiveScore > negativeScore:
  print("This is a positive sentence")
elif negativeScore > positiveScore:
  print("This is a negative sentence")
elif positiveScore == negativeScore:
  print("This is a neutral sentence")
