import pandas as pd
import src.train as train
import spacy
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

def dataReady(pathcsv,pathcategories):
    #From csv to id and text series DataFrame
    df = pd.read_csv(pathcsv)
    df = df[['id', 'text']]

    #From pkl file to categories dictionary
    categories = pkltodict(pathcategories)

    #Trained model 
    training = train.trainData(df, categories)

    #Predicted df to csv
    dffinal = categoryColumn('./output/movies', df)

    #Graph
    dffinal = pd.read_csv('predicted.csv')
    p = sns.countplot(data=dffinal, x = 'category')
    plt.savefig('barcategories')

    #PDF 
    
    return 

def dicttopkl(dictionary):
    #From dictionary to pkl
    output = open('myfile.pkl', 'wb')
    pickle.dump(dictionary, output)
    output.close()

def pkltodict(pkl):
    pkl_file = open('myfile.pkl', 'rb')
    mydict = pickle.load(pkl_file)
    pkl_file.close()
    return mydict

def categoryColumn(path, df):
    #Predict category while iterate through text serie and save the final DataFrame 
    nlp = spacy.load(path)

    for index, row in df.iterrows():
        doc = nlp(row['text'])
        for ent in doc.ents:
            df.loc[index, 'category'] = [(ent.label_)]
    
    return df.to_csv('predicted.csv')