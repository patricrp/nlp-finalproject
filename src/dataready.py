import pandas as pd
import src.train as train
import spacy

def dataReady(pathcsv):
    #From csv to id and text series DataFrame
    df = pd.read_csv(pathcsv)
    df = df[['id', 'text']]
    return df

def dtocsv(dictionary):
    #From dictionary to csv
    with open('data.csv', 'w') as f:
        for key in dictionary.keys():
            f.write("%s, %s\n" % (key, dictionary[key]))


def categoryColumn(path, df):
    nlp = spacy.load(path)

    for index, row in df.iterrows():
        doc = nlp(row['text'])
        for ent in doc.ents:
            df.loc[index, 'category'] = [(ent.label_)]
    
    return df.to_csv(path)