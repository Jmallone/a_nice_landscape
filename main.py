import tweepy
import random

#https://docs.tweepy.org/en/latest/authentication.html
auth = tweepy.OAuth1UserHandler(
   "API / Consumer Key here", "API / Consumer Secret here",
   "Access Token here", "Access Token Secret here"
)

api = tweepy.API(auth)

try:
    # 'images/frame0.jpg'
    emoji = ['🗺️', '🎑', '🪟', '🌸', '🌆', '🖼️', '🏞️', '⛰️', '🚞', '🏔️']
    emoji = ['🗺️', '🎑', '🪟', '🌸', '🌆', '🖼️', '🏞️', '⛰️', '🚞', '🏔️']
    idx = random.randint(0, len(emoji)-1)
    
    tweet = api.update_status_with_media(status=emoji[idx], filename="images/frame0.jpg")
    print(tweet)
except Exception as e:
    print("Erro ", e)
