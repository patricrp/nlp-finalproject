import pandas as pd
import src.train as tr
import spacy
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import pickle


def dicttopkl(dictionary):
    #From dictionary to pkl
    output = open('myfile.pkl', 'wb')
    pickle.dump(dictionary, output)
    output.close()

def pkltodict(pkl_file):
    #From pkl to dictionary
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
    
    return df.to_csv('../output/predicted.csv')


def volumeCategories(pathcsv):
    #Two metrics from the DataFrame to incorporate  to the PDF
    df = pd.read_csv(pathcsv)
    volume = df['text'].count()
    percentage = df['category'].count()/df['text'].count()
    return volume, percentage



def dataReady(pathcsv,pathcategories):
    #From csv to id and text series DataFrame
    df = pd.read_csv(pathcsv)
    df = df[['id', 'text']]

    #From pkl file to categories dictionary
    categories = pkltodict(pathcategories)

    #Train model with a sample from the DataFrame and the categories, generating the list of text-entities needed for the model
    training = tr.trainData(df, categories)

    #Predicted df to csv applying the trained model
    dffinal = categoryColumn('./output/model', df) 

    #Graph of categories
    dffinal = pd.read_csv('predicted.csv') 
    graph = sns.countplot(data=dffinal, x = 'category')
    plt.xticks(rotation=45)
    plt.savefig('../output/barcategories') 

    #PDF 
    #incluir la función que llame a createpdf

    print('PDF in...') 