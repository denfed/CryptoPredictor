
# === IMPORTS ===

import datetime
print(datetime.datetime.now())
import time
print(time.time())



# === FUNCTIONS ===

def convertTime(time):
    return datetime.datetime.fromtimestamp(time)



# === CLASSES ===

class post:
    dict = {'time' : '', 'message' : '', 'sentiment' : 0.0, 'platform' : '', 'type' : '', 'matched' : ''}

    def __init__(self, time, message, sentiment, platform, typ, matched):
        self.dict['time'] = time
        self.dict['message'] = message
        self.dict['sentiment'] = float(sentiment)
        self.dict['platform'] = platform
        self.dict['type'] = typ
        self.dict['matched'] = matched
        print(matched)


    def __str__(self):
        return 'time: '+self.time+', message: '+self.message+', sentiment: '+self.sentiment+', matched: '+self.matched

