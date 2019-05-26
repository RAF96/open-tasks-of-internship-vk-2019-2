import numpy as np
import pandas as pd
import sklearn as sk
import matplotlib.pyplot as plt
import doctest
import implicit
from implicit.als import AlternatingLeastSquares
import sklearn
from sklearn.model_selection import train_test_split
import scipy
from scipy.sparse import csr_matrix


def to_sparce_matrix(pd_data):
    '''
    >>> to_sparce_matrix(pd.DataFrame({'rating': [3,5], 'userId' : [1, 2], 'movieId': [1, 2]})).toarray()
    array([[0., 0., 0.],
           [0., 0., 0.],
           [0., 0., 1.]])
    '''
    matrix = csr_matrix((pd_data['rating'].values, (pd_data['userId'].values, pd_data['movieId'].values)))
    matrix.data[matrix.data < 4] = 0
    matrix.eliminate_zeros()
    matrix.data = np.ones(len(matrix.data))
    return matrix

def split_train_test(data):
    users = data['userId'].unique()
    users_train, users_test = train_test_split(users, train_size = 0.8)
    data_train = data[data['userId'].isin(users_train)]
    data_test = data[data['userId'].isin(users_test)]
    return data_train, data_test

def ndcg(label, approx, k):
    '''
    >>> ndcg(np.array([1, 2, 3]), np.array([1,2,3]), 3)
    1.0
    '''
    res = pd.Series(approx[:k]).isin(label)
    def func(x):
        res = 0
        x = np.power(2, x) - 1
        for index, value in enumerate(x):
            res += value / np.log(index + 2)
        return res
    return func(res) / func(np.ones(k))
