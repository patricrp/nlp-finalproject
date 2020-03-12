import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import seaborn as sns

def graphCategory(df):
    #Get a category graph 
    graph = sns.countplot(data=df, x = 'category')
    plt.title('Categories distribution')
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig('../output/barcategories') 
    print('Your category graph is ready in the output folder')


def graphSentiment(df):
    #Sentiment analysis
    df = sentimentAnalysis(df)

    #Get a sentiment graph 
    sentiment = pd.DataFrame([df['negative'].mean(), df['neutral'].mean(), df['positive'].mean()])
    colors = ['#C00202','#C6C6C6','#249B1F']
    labels = ['Negative', 'Neutral', 'Positive']
    explode = (0.05,0.05,0.05)
    centre_circle = plt.Circle((0,0),0.60,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    plt.pie(sentiment, labels=labels, colors = colors, autopct='%1.1f%%', startangle=90, pctdistance=0.85, explode=explode)
    
    plt.title('Sentiment Analysis')
    plt.tight_layout()
    plt.savefig('../output/sentiment') 
    
    print('Your sentiment graph is ready in the output folder')


def graphSentCat(df):
    #Sentiment analysis
    df = sentimentAnalysis(df)

    #Get sentiment by category graph
    df_group = df.groupby('category').agg({'negative':'mean', 'neutral':'mean', 'positive':'mean'})
    colors = ['#C00202','#C6C6C6','#249B1F']
    df_group.plot(colors = colors, kind='bar', stacked=True)
    plt.title('Sentiment by category')
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.gca()
    plt.xlabel('Categories')
    plt.legend(title='Sentiment', loc='best')
    plt.savefig('../output/sentimentcat') 

    print('Your sentiment/category graph is ready in the output folder')


def sentimentAnalysis(df):
    #Sentiment analysis
    sia = SentimentIntensityAnalyzer()
    df['sentiment'] = df['text'].apply(lambda x: sia.polarity_scores(x))
    df['negative'] = df['sentiment'].apply(lambda x: x['neg'])
    df['neutral'] = df['sentiment'].apply(lambda x: x['neu'])
    df['positive'] = df['sentiment'].apply(lambda x: x['pos'])

    return df