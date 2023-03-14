import requests
from bs4 import BeautifulSoup

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from heapq import nlargest # ????

# nltk.download("punkt")
# nltk.download("stopwords")

def summarize(text, num_sentences):
    """something is up"""
    # tokenize the text
    sentences = sent_tokenize(text)
    words = word_tokenize(text)

    # remove stopwords and punctuation
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word.lower() not in stop_words and word.isalnum()]

    # calculate word frequency
    freq_dist = nltk.FreqDist(words)

    # find the most frequent words
    most_freq_words = nlargest(10, freq_dist, key = freq_dist.get) # from heapq(finds 10 largest frequencies)

    # finds the sentences with the most frequent words
    summary_sentences = []
    for sentence in sentences:
        if any(word in sentence for word in most_freq_words):
            summary_sentences.append(sentence)

    # returns the summary
    summary = " ".join(nlargest(num_sentences, summary_sentences, key = len))


url = "https://www.nltk.org/book/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

chapter = soup.find("dd")
link = chapter.find("a").get("href")

# into the chapter
deeper_url = url + link
deeper_soup = BeautifulSoup(requests.get(deeper_url).content, "html.parser")

def make_gen():
    for i in deeper_soup.find_all("p"):
        yield i
