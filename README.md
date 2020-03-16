NLP-project aims to be a text classifier, thanks to a predictived model with spaCy dessigned for tweets.

Having a csv of publications and a csv with categories the model predict the category of each tweet.

1. From both csv the program create a training data for the model.
2. The model is created from scratch, based on a English blank model and trained with the training data.
3. The csv of publications is classified iterating over it.
4. Finally, the program generates a PDF with a few volume metrics a 3 graphs: volume of tweets by categories, sentiment analysis and sentiment by category.


Next step:

1. Create a multilanguage model.
2. Add few more metrics and example like tweet with best results or user with higher retweets to the PDF.