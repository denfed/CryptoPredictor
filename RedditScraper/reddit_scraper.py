import praw
import sys

reload(sys)
sys.setdefaultencoding('utf8')

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

sys.stdout = open('Output.txt', 'wt')

for submission in subreddit.hot(limit=4):
    if not submission.stickied:
        if 'Bitcoin' in submission.title:
            print(submission.title)

            submission.comments.replace_more(limit=0)
            comments = submission.comments
            print(submission.selftext)

            for comment in comments:
                #print(20*'-')
                print(comment.body)

                if len(comment.replies) > 0:
                    for reply in comment.replies:
                        #print('REPLY:')
                        print(reply.body)
