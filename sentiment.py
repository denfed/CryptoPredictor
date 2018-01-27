from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sentences = []
numLines = 0

with open("./RedditScraper/Output.txt", "r") as ins:
    for line in ins:
        numLines += 1
        sentences.append(line)

analyzer = SentimentIntensityAnalyzer()
# sentences = *GET SENTENCE ARRAY FROM SCRAPER*
# sentences = ['Chocolate is the best thing in the world']
compVal = 0
for sentence in sentences:
    vs = analyzer.polarity_scores(sentence)
    # str(vs['*INSERT DATA POINT YOU WANT*'])
    print("{:-<65} {}".format(sentence, str(vs)))
    compVal += vs['compound']

sentResult = compVal/numLines

file2write=open("SentimentAndDate", 'w')
file2write.write(str(sentResult)+'\n')
file2write.close()