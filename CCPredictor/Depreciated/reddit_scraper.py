import praw
import sys

SEARCH_KEYWORD = 'Ethereum'

bot = praw.Reddit(user_agent='CCPredictor',
                  client_id='zQdUF_lBvcrKXw',
                  client_secret='R5ffzPuBjyTW7SyLG7vFvRPeQFI',
                  username='CCPredictorBot',
                  password='CryptoBot')

subreddit = bot.subreddit('CryptoCurrency')

sys.stdout = open('Output2.txt', 'wt')


for submission in subreddit.hot(limit=3):
    if not submission.stickied:

        if SEARCH_KEYWORD in submission.title: print(submission.title)

        submission.comments.replace_more(limit=0)
        comments = submission.comments

        if SEARCH_KEYWORD in submission.selftext: print(submission.selftext)

        for comment in comments:

            if SEARCH_KEYWORD in comment.body: print(comment.body)

            if len(comment.replies) > 0:

                for reply in comment.replies:

                    if SEARCH_KEYWORD in reply.body: print(reply.body)

