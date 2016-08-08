import praw
import unicodedata
import random

#setup our reddit object
r = praw.Reddit('Nba GIFS token grabber')
#setup the oauth stuff
r.refresh_access_information()

#function to add replies to the relevant comments
def addComments(gif):
    subreddit = r.get_subreddit('giftester')
    subreddit_comments = subreddit.get_comments()
    flat_comments = praw.helpers.flatten_tree(subreddit_comments)
    for comment in flat_comments:
        if comment.body == "Show me a gif!":
            comment.reply(gif)


#function to get the newest 'hot' gifs from /r/nbaGifs
def getGif():
	gifList = []
	subreddit = r.get_subreddit('nbagifs')
	for submission in subreddit.get_hot(limit=10):
		subUrl = unicodedata.normalize('NFKD', submission.url).encode('ascii','ignore')
		#get rid of the self posts
		if 'reddit' not in subUrl:
			gifList.append(subUrl)
	#return a random gif from the list
	return random.choice(gifList)

if __name__ == "__main__":
	gif = getGif()
	addComments(gif)
