from textblob import TextBlob

test = TextBlob("Fuck you textblob.")
print(test.sentiment)
