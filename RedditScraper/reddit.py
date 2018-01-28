import praw, sys, json

def scrape(subred, queries, limit, outputFile, startTime = 0, endTime = 9999999999):
    # ARGUMENTS: str subred, [str] queries, uint limit, str outputFile, unixTime startTime, unixTime endTime
    reload(sys)
    sys.setdefaultencoding('utf8')
    bot = praw.Reddit(user_agent='CCPredictor',
                      client_id='zQdUF_lBvcrKXw',
                      client_secret='R5ffzPuBjyTW7SyLG7vFvRPeQFI',
                      username='CCPredictorBot',
                      password='CryptoBot')


    for II in bot.subreddit(subred).hot(limit=limit):
        recordSubmission(II, outputFile, queries)



def recordSubmission(sub, filename, queries):
    import main
    with open(filename, 'a') as fileObj:
        matches = []
        for I in queries:
            if I in sub.title:
                matches += [I]
        if matches:
            json.dump(main.post(sub.created, sub.title, 0, 'reddit', 'submission', ' '.join(matches)).dict, fileObj)
            fileObj.write('\n')
        for I in sub.comments:
            if type(I) != praw.models.reddit.comment.Comment: continue
            matches = []
            for II in queries:
                if II in I.body:
                    matches += [II]
            if matches:
                json.dump(main.post(I.created, I.body, 0, 'reddit', 'comment', ' '.join(matches)).dict, fileObj)
                fileObj.write('\n')
    return

if __name__ == '__main__': scrape('CryptoCurrency', ['bitcoin', 'crypto'], 50, 'output.json')