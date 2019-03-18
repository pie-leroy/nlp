from itertools import islice
import datetime
import os 
import math

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))

def write_result(wiki_vocab_tokenized, word_embedding, time_training,name_notebook_exported, epochs, fname):
    if not os.path.isfile(fname):
        f=open(fname, "a+")
        f.write("Nombre de mots;Model de word embedding;temps d'apprentissage;Nombre d'epochs; Notebook de référence" )
        f.close
    f=open(fname, "a+")
    f.write("\n" + str( str(len(wiki_vocab_tokenized)) + ";" +word_embedding + ";"+ str(time_training) + ";"+  str(epochs) + ";" + str(name_notebook_exported)))
    f.close
    
def get_model_name(word_embedding_model_name):
    model_name = word_embedding_model_name + "/"+ str(datetime.datetime.now().strftime("%m")) + "-" + str(datetime.datetime.now().strftime("%d")) + "-" + str(datetime.datetime.now().strftime("%H")) + "-" + str(datetime.datetime.now().strftime("%M")) 
    return model_name


def round_down(x):
    return int(math.ceil(x / 10.0)) * 10 - 10