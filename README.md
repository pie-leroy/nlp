This repository contains the tests I perform for my master thesis that I am writing. The objective is to compare existing word embedding methods on a data set of about 10,000 documents (in order to simulate the data corpus of a reasoned-size company).

To do this I will use popular embedding methods like word2vec, GLove, etc.

I will also be able to rely on already trained embeddings and in this case test fine tuning.

I retrieved in French a little more than 10000 documents from the same wikipedia application domain (informatic) using a python script. This is available under the "wikipedia" folder.

The word2vec folder contains my implementation of the skip-gram algorithm under tensorflow as well as its use with the gensim library.

This is Ima todo-list:
-implement GLove under tensorflow
-define a performance measurement method to compare several embeddings
-Use a recurring template for an nlp task
------------------------------------------------------------------------------------------------------------------------
This repository is under construction, don't hesitate to make comments to me

