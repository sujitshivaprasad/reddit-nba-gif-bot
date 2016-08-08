# reddit-nba-gif-bot
## Introduction
I like seeing gifs, especially entertaining ones while browsing Reddit. So I created this bot.

The bot looks on /r/nba (I'm going to add this as soon as I ensure I'm not breaking any API rules) for any comments with the words 'Show me a gif!', and posts a random gif from the top 10 hottest posts on /r/nbagifs. 

I also realized that /r/nbagifs isn't a very active subreddit, so I might have to find a new place for good nba gifs.

# Setup

##Dependencies:
```
pip install praw
pip install unicodedata
pip install random
```
Use the example praw.ini file, rename it to 'praw.ini' and fill out the necessary information. You can get your client id and client secret from https://ssl.reddit.com/prefs/apps/
With the help of the get_secret.py file, you will only have to set up the Oauth stuff once, which is convenient if you have different uses for your app. So use the following commands after editing the praw.ini file:
```
python get_secret.py
```
You should be redirected to a webpage in your browser asking for permission to access your reddit account.
Then,

```
python redditBot.py
```

You're all set!
