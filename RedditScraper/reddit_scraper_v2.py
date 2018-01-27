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

sys.stdout = open('Outputtest.txt', 'wt')


submission = bot.submission(url="https://www.reddit.com/r/CryptoCurrency/comments/7teo2r/which_coins_do_you_think_are_undervalued_right/")
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
