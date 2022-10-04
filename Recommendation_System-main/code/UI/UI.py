from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.append('../')
from PyQt5.QtCore import QDir
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import pandas as pd
from mainwindow import Ui_MainWindow as Main_Ui
from listwindow import Ui_MainWindow as List_Ui
from MF_recommendation.SVD_CF import LFM
import numpy as np
import random
class MyMainWin(QMainWindow,Main_Ui):
    def __init__(self):
        super(MyMainWin,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.display)
        self.userid = self.lineEdit.text()

    def display(self):

        Listwin.show()
        self.close()

class Table(QWidget):
    def __init__(self,userid):
        super(Table, self).__init__()
        #设置标题与初始大小
        self.setWindowTitle('给{}号用户推荐的电影'.format(userid))
        self.resize(500,300)

        #设置数据层次结构，4行4列
        self.model=QStandardItemModel(5,3)
        #设置水平方向四个头标签文本内容
        self.model.setHorizontalHeaderLabels(['电影编号','电影信息','电影主题标签'])
        dtype = [("userId", np.int32), ("movieId", np.int32), ("rating", np.float32)]
        dataset = pd.read_csv("../data/Moivelens/ml-latest-small/ratings.csv", usecols=range(3), dtype=dict(dtype))
        movies = pd.read_csv('../data/Moivelens/ml-latest-small/movies.csv')

        lfm = LFM(0.02, 0.01, 0.01, 10, 5, ["userId", "movieId", "rating"])
        lfm.fit(dataset)
        lists = lfm.Top_N(lfm,5,5,movies,dataset)
        df = pd.read_csv('../data/Moivelens/ml-latest-small/movies.csv')
        for row in range(len(lists)):
            for column in range(3):
                if column == 0:
                    item=QStandardItem(str(lists[row]))
                    self.model.setItem(row,column,item)
                elif column==1:
                    item=QStandardItem(str(df[df['movieId']==lists[row]]['title'].values[0]))
                    self.model.setItem(row,column,item)
                else:
                    item=QStandardItem(str(df[df['movieId']==lists[row]]['genres'].values[0]))
                    self.model.setItem(row,column,item)
        #实例化表格视图，设置模型为自定义的模型
        self.tableView=QTableView()
        self.tableView.setModel(self.model)

        #水平方向标签拓展剩下的窗口部分，填满表格
        self.tableView.horizontalHeader().setStretchLastSection(True)
        #水平方向，表格大小拓展到适当的尺寸
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


        #设置布局
        layout=QVBoxLayout()
        layout.addWidget(self.tableView)
        self.setLayout(layout)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    Mainwin = MyMainWin()
    Listwin = Table(Mainwin.userid)
    Mainwin.show()
    sys.exit(app.exec_())


