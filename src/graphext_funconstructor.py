import pandas as pd
import graphext_datatraining as tr
import spacy
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import graphext_graphs as gp
import graphext_createpdf as cpdf

def pkltodict(pkl_file):
    #From pkl to dictionary
    pkl_file = open('graphextmyfile.pkl', 'rb')
    mydict = pickle.load(pkl_file)
    pkl_file.close()
    return mydict


def invertDict(dictionary):
    #Reverse dictionary to get key,value pair
    new_categories = dict()

    for category, lista in dictionary.items():
        for word in lista:
            new_categories.update({word:category})
        
    return new_categories


def categoryColumn(path, df):
    #Predict category while iterate through text serie and save the final DataFrame 
    nlp = spacy.load(path)

    for index, row in df.iterrows():
        doc = nlp(row['text'])
        for ent in doc.ents:
            df.loc[index, 'category'] = [(ent.label_)]
    df.to_csv('../output/graphextpredicted.csv')
    print('Your predicted csv is in the output folder')


def volumeCategories(pathcsv):
    #Two metrics from the DataFrame to incorporate  to the PDF
    df = pd.read_csv(pathcsv)
    volume = df['text'].count()
    percentage = round((df['category'].count()/df['text'].count()) * 100)
    return volume, percentage



def dataReady(pathcsv,pathcategories):
    #From csv to id and text series DataFrame
    df = pd.read_csv(pathcsv)
    df = df[['id', 'text']]

    #From pkl file to categories dictionary
    categories = pkltodict(pathcategories)
    
    #To reversed dictionary
    categories = invertDict(categories)

    #Train model with a sample from the DataFrame and the categories, generating the list of text-entities needed for the model
    training = tr.trainData(df, categories)
    print('The model has been trained!')
    print('Training data is ready!')

    #Predicted df to csv applying the trained model
    categoryColumn('../output/modelgraphext', df)
    print('Predicted results are in the output folder')

    #Graphs
    dffinal = pd.read_csv('../output/graphextpredicted.csv') 
    gp.graphCategory(dffinal)
    gp.graphSentiment(dffinal)
    gp.graphSentCat(dffinal)
    print('Graphs ready')

    #PDF 
    cpdf.newPDF()

    print('The model, graphs and report are in the output folder') 
