import gzip, cPickle
import numpy as np
import six.moves.cPickle as pickle

import gc
import sys
from logger import Logger
from ekstrak_csv import Ekstraktor
from DBN import test_DBN


ekstraktor = Ekstraktor()

def percobaan1_4l_1000e():
    finetune_lr=0.1
    pretraining_epochs=2000
    pretrain_lr=0.01
    k=1
    training_epochs=100
    dataset='./dataset/gse10072.pkl.gz'
    batch_size= 5
    n_v=22283
    n_output=2

    # percobaan 1 dengan layer 10k 5k 1k 500
    sys.stdout = Logger("./dataset/logout2000e_10k_5k_1k_500.txt")
    hidden_sizes=[10000, 5000, 1000, 500]
    model_hasil = test_DBN(finetune_lr, pretraining_epochs,
                  pretrain_lr, k, training_epochs,
                  dataset, batch_size,hidden_sizes, n_v,n_output)

    ekstraktor.simpanModel("./dataset/model2000e_10k_5k_1k_500.pkl.gz", model_hasil)
    del model_hasil
    gc.collect()

    # percobaan 2
    sys.stdout = Logger("./dataset/logout2000e_7k_10k_5k_1k.txt")

    hidden_sizes=[7000, 10000, 5000, 1000]
    model_hasil = test_DBN(finetune_lr, pretraining_epochs,
                 pretrain_lr, k, training_epochs,
                 dataset, batch_size,hidden_sizes, n_v,n_output)

    ekstraktor.simpanModel("./dataset/model2000e_7k_10k_5k_1k.pkl.gz", model_hasil)
    del model_hasil
    gc.collect()

    # percobaan 3
    sys.stdout = Logger("./dataset/logout2000e_3k_2k_1k_100.txt")
    hidden_sizes=[3000, 2000, 1000, 100]
    model_hasil = test_DBN(finetune_lr, pretraining_epochs,
                pretrain_lr, k, training_epochs,
                dataset, batch_size,hidden_sizes, n_v,n_output)

    ekstraktor.simpanModel("model2000e_3k_2k_1k_100.pkl.gz", model_hasil)
    del model_hasil
    gc.collect()




if __name__ == '__main__':
    percobaan1_4l_1000e()