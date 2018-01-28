from SentimentNN.encoder import Model

model = Model()
file = open('RedditScraper/Output.txt', 'r')
text = file.readlines()
print(text)
#text_features = model.transform(text)

