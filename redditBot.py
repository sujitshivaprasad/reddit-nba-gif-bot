import praw
from praw.objects import Comment, Submission
import logging
import sys
#import get_secret
r = praw.Reddit('Nba GIFS token grabber')
r.refresh_access_information()

logging.basicConfig(stream=sys.stdout)
log = logging.getLogger(__name__)
log.setLevel(level=logging.WARNING)

def getComments():
    subreddit = r.get_subreddit('giftester')
    subreddit_comments = subreddit.get_comments()
    flat_comments = praw.helpers.flatten_tree(subreddit_comments)
    for comment in flat_comments:
        if comment.body == "I found the post. Now let me find a good gif!":
            comment.reply('Found!')

getComments()