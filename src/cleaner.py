import pandas as pd
import numpy as np
import spacy
import random
import re
from spacy.lang.en import English
from spacy.lang.en.stop_words import STOP_WORDS

def lowerize(text):
    #Text to lower
    return text.lower()

def cleaner(text):
    
    #Clean text Serie deleting stop_words and rare symbols
    stopwords = set(STOP_WORDS)
    raresymbols = re.compile(('[/()\[\]\|@,;]#_-'))
    text = raresymbols.sub('', text)
    text = ' '.join(word for word in text.split() if word not in stopwords)


    #Tokenize text
    #nlp = English()
    #tokenizer = nlp.Defaults.create_tokenizer(nlp)
    #tokens = tokenizer(text)

    return text