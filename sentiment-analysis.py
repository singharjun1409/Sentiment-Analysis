import requests
from bs4 import BeautifulSoup
from nltk import word_tokenize, pos_tag , ne_chunk
from textblob import TextBlob
from collections import defaultdict

# Retrieving data from url
url = "https://www.gutenberg.org/cache/epub/55406/pg55406.txt"
response = requests.get(url)
soup = BeautifulSoup(response.content , "html.parser")

# Extracting text, tokenizing it into word tokens and getting named entities 
text = soup.get_text()
tokens = word_tokenize(text)
tags = pos_tag(tokens)
entities = ne_chunk(tags)

# Will need for breaking text into sentences to match a sentence to a person
blob = TextBlob(text)
person_sentences = defaultdict(list)

# Getting all elements labeled PERSON and their associated sentences
for sub in entities:
    if hasattr(sub , "label"):
        if(sub.label() == "PERSON"):
            name = sub[0][0]
            for sentence in blob.sentences:
                if name in sentence:
                    person_sentences[name].append(sentence)

# Sentiment Analysis 
print("Overall Sentiment Analysis for PERSON entities:")
for person_name, sentences in person_sentences.items():
    total_polarity = 0
    total_subjectivity = 0
    for sentence in sentences:
        sentiment = TextBlob(str(sentence)).sentiment
        total_polarity += sentiment.polarity
        # Optional: total_subjectivity += sentiment.subjectivity

    # Calculate average polarity and subjectivity
    avg_polarity = total_polarity / len(sentences)
    # Optional: avg_subjectivity = total_subjectivity / len(sentences)

    print(f"Person: {person_name}")
    print(f"Number of Sentences: {len(sentences)}")
    print(f"Average Polarity: {avg_polarity}")  
    # Optional: print(f"Average Subjectivity: {avg_subjectivity}") 
    print("-" * 50)