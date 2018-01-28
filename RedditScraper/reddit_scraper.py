import praw
import sys

#sys.setdefaultencoding('utf8')

bot = praw.Reddit(user_agent='CCPredictor',
                  client_id='zQdUF_lBvcrKXw',
                  client_secret='R5ffzPuBjyTW7SyLG7vFvRPeQFI',
                  username='CCPredictorBot',
                  password='CryptoBot')

subreddit = bot.subreddit('CryptoCurrency')

'''
for submission in subreddit.hot(limit=5):
    #if 'Bitcoin' in submission.title:

        print(submission.title)
        comments = submission.comments

        for comment in comments:
            print(20*"-")
            print(comment.body)
            if len(comment.replies) > 0:
                for reply in comment.replies:
                    print("REPLY:")
                    print("\t" + reply.body)

'''
sys.stdout = open('Output2.txt', 'wt')
search = 'Ethereum'

for submission in subreddit.hot(limit=30):
    if not submission.stickied:
    #submission = subreddit.submission(url="https://www.reddit.com/r/CryptoCurrency/comments/7teo2r/which_coins_do_you_think_are_undervalued_right/")

        if search in submission.title: print(submission.title)

        submission.comments.replace_more(limit=0)
        comments = submission.comments
        if search in submission.selftext: print(submission.selftext)

        for comment in comments:
            #print(20*'-')
            if search in comment.body: print(comment.body)

            if len(comment.replies) > 0:
                for reply in comment.replies:
                    #print('REPLY:')
                    if search in reply.body: print(reply.body)

