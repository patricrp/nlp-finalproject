import pandas as pd
import numpy as np
import re
import graphext_enspacymodel as eng

def localize(pattern, text):
    #Localize where the pattern match the text
    x = re.search(pattern, text).span()
    return x


def findCategory(text, reverseddict):
    #Get reversed dictionary key and word matching
    sentence = re.findall(r'\w+', text)

    category = []
    for word in sentence:
        topic = reverseddict.get(word, None)
        if topic:
            category.append((word,topic))

    return category

def entity(text, reverseddict):
    #Create entity text and matching
    matcher = findCategory(text, reverseddict)
    if matcher != '':
    
        tupla = []
        #Locate word matching
        for i in range(len(matcher)):
            localizer = localize(matcher[i][0], text)
            group = []
            group.append(localizer[0]), group.append(localizer[1]), group.append(matcher[i][1])
            tupla.append(tuple(group))

        entity = dict()
        entity.update({'entities': tupla})
        data = [text, entity]
        return data
    else:
        return (
        text,
        {"entities": []},)

def trainData(df, categories):
    #Create training data. Be sure your csv has a 'text' Serie
    
    #Select 300 rows of the dataset if it's higher than 1000
    length = df.shape
    if length[0] > 1000:
        df= df[:300]
    
        #Create training_data with text and entities
        training_data = []
        for i in df['text'].tolist():
            training_data.append(entity(i, categories))
        return eng.main(training_data, None, '../output/modelgraphext', 100) 
    
    
    #Select 200 rows of the dataset if it's smaller than 1000
    else:
        training_data = []
        for i in df['text'][:200].tolist():
            training_data.append(entity(i, categories))
        return eng.main(training_data, None, '../output/modelgraphext', 100)

