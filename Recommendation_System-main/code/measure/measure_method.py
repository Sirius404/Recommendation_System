#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Feiniu

import numpy as np
import pandas as pd
from scipy.spatial.distance import pdist

class Similarity():

    def normalization(self,vector):
        _range = np.max(vector) - np.min(vector)
        return (vector-np.min(vector))/_range

    def cos_measure(self, feature_vector1, feature_vector2):
        """
        计算item之间的余弦夹角相似度
        :return: 待计算item与用户已评分的items的余弦夹角相识度的向量
        """

        num = float(np.dot(feature_vector1, feature_vector2))  # 向量点乘
        denom = np.linalg.norm(feature_vector1) * np.linalg.norm(feature_vector2)  # 求模长的乘积
        return 0.5 + 0.5 * (num / denom) if denom != 0 else 0



    def pearson_measure(self,feature_vector,feature_matrix):
        '''
        计算item之间的皮尔森相关系数
        :return:待计算item与用户已评分的items的皮尔森系数的向量
        '''
        return np.matrix(np.corrcoef(feature_vector,feature_matrix)[0,1:])
    def jaccard_measure(self,feature_vector,feature_matrix):
        '''
        jaccard距离
        :return:
        '''
        distanceArr = feature_matrix - feature_vector
        length = feature_matrix.shape[1]
        return self.normalization(length - np.matrix(np.count_nonzero(np.array(distanceArr),axis=1)))

# def cos_measure(feature_vector, feature_matrix):
#     """
#     计算item之间的余弦夹角相似度
#     :param feature_vector: 待测量的item特征向量
#     :param feature_matrix: 用户已评分的items的特征矩阵
#     :return: 待计算item与用户已评分的items的余弦夹角相识度的向量
#     """
#     x_c = (feature_vector * feature_matrix.T) + 0.0000001
#     mod_x = np.sqrt(feature_vector * feature_vector.T)
#     mod_c = np.sqrt((feature_matrix * feature_matrix.T).diagonal())
#     cos_xc = x_c / (mod_x * mod_c)
#
#     return cos_xc


def comp_mse(pred, actual):
    """
    计算根均方误差
    :param pred: 预测值
    :param actual: 真实值
    :return: 根均方误差
    """
    error = pred - actual
    count = error.nonzero()[0].shape
    MSE = (error).dot((error).T) / count

    return MSE

def comp_rmse(pred, actual):
    """
    计算根均方误差
    :param pred: 预测值
    :param actual: 真实值
    :return: 根均方误差
    """
    error = pred - actual
    count = error.nonzero()[0].shape
    RMSE = np.sqrt((error).dot((error).T) / count)

    return RMSE