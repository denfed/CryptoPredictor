from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sentences = []

with open("Output.txt", "r") as ins:
    for line in ins:
        sentences.append(line)

analyzer = SentimentIntensityAnalyzer()
# sentences = *GET SENTENCE ARRAY FROM SCRAPER*
# sentences = ['Chocolate is the best thing in the world']
for sentence in sentences:
    vs = analyzer.polarity_scores(sentence)
    # str(vs['*INSERT DATA POINT YOU WANT*'])
    print("{:-<65} {}".format(sentence, str(vs)))
    val = vs['compound']
    print (val)
