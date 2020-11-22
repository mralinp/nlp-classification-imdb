# nlp-classification-imdb

## Intro
The goal of this project is getting familiar with 'classification', by solving a natural language processing problem. Here we have a dataset in which any user has been written his/her oppinion about a movie. The sentences that users written has a posetive or nagative meaning that we can say whether they like the movie or not. each sentence has been read by a human and he/she labeled the data with 0 and 1 which means possetive or negative oppinion.

We have collected 3 kindes of datasets, testing, training and a validation dataset. we wanted you to first, build a feature vector of the written sentences and then train your classificator with the given datasets and then use your trained classificator to label the validation dataset sentences.

### Datasets
The dataset we are using is, *'IMDB dataset (sentiment analysis) in CSV format'*, and you can download it from here: [kaggle.com](https://kaggle.com/columbine/imdb-dataset-sentiment-analysis-in-csv-format)


## Steps
### preproccessing
First step ro solve the problem is data **preprocessing**. At this step data must be cleand and extra features has to be deleted. Genrally we start with some common data cleaning methods like, deleting stop words, punctuitions and etc.

Be aware, commonly some data sets contains **HTML tags** and they are consistent with the data deliverd by IMDB website. we will delete them first and then go throw.

## Feature mining
After preproccessing step, we have to obtain feature vectors from our cleaned data to train our model, remember that our model is working with mathmatical models not litteral centenses.

There are several method to obtain a feature vector from a text data as follows:

* Bag of words
* BERT Embedding
* TF-IDF
* Word2Vec

## Train the classifier
We train our classifier using feature vectors we just created during berevious steps for the **Training set** and the **Validation set**.

Using two classifiers **Bayes classifier** and **SVM classifier**, we want to solve this problem and then measure and compare their performance.

## Test

After training process, performances under **Test data** will be computed and the observation will represented as some analysis.

### final words
I hope this could help some people who want to see a simple AI university project and need some general knowledge about this concept.