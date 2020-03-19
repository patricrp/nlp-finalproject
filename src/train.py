import pandas as pd
import numpy as np
import re
import englishspacymodel as eng


def localize(pattern, text):
    #Localize where the pattern match the text
    x = re.search(pattern, text).span()
    return x



def matcherCat(text, categories):
    #Get dictionary key and word matching
    for categoria, lista in categories.items(): 
        for word in lista: 
            if word in text:
                return categoria, word 
    return ''

def category(text, categories):
    #Get dictionary category
    for categoria, lista in categories.items(): 
        for word in lista: 
            if word in text:
                return categoria 
        return ''

def entity(text, categories):
    #Create an entity for Training Data with text, index and category
    matcher = matcherCat(text, categories)
    if matcher != '':
        localizer = localize(matcher[1], text)
        tupla = []
        tupla.append(localizer[0]), tupla.append(localizer[1]), tupla.append(matcher[0])
        entities = [tuple(tupla)]
        entity = dict()
        entity.update({'entities': entities})
        data = [text, entity]
        return tuple(data)
    else:
        return (
        text,
        {"entities": []},)


def trainData(df, categories):
    #Create training data. Be sure your csv has a 'text' Serie
    
    #Select 20% of the dataset if it's higher than 1000
    length = df.shape
    if length[0] > 1000:
        df= df[:300]
    
        #Create training_data with text and entities
        training_data = []
        for i in df['text'].tolist():
            training_data.append(entity(i, categories))
        return eng.main(training_data, None, '../output/model', 100) 
    
    
    #Select 200 rows of the dataset if it's smaller than 1000
    else:
        training_data = []
        for i in df['text'][:300].tolist():
            training_data.append(entity(i, categories))
        return eng.main(training_data, None, '../output/model', 100)
