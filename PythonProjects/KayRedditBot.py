# simple bot using Reddit API

import praw

# info below is available by making own app with Reddit Account
reddit = praw.Reddit(client_id='CLIENT_ID',
                     client_secret="CLIENT_SECRET", password='PASSWORD',
                     user_agent='USERAGENT', username='USERNAME')

subreddit = reddit.subreddit('Korean')

# grabs 5 comments from Korean Subreddit and prints out the authors
for comment in subreddit.comments(limit=5):
    print(comment.author)
