
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import *
import pandas as pd
sys.path.append('..\..')
class Ui_MainWindow(QWidget):
    def __init__(self,parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        #设置标题与初始大小
        self.setWindowTitle('给{}号用户推荐的电影'.format(1))
        self.resize(500,300)

        #设置数据层次结构，4行4列
        self.model=QStandardItemModel(5,3)
        #设置水平方向四个头标签文本内容
        self.model.setHorizontalHeaderLabels(['电影编号','电影信息','电影主题标签'])
        df = pd.read_csv(r'C:\\Users\\Flown\\Desktop\\代码\\Recommondation-System-master\\code\\data\\Moivelens\\ml-latest-small\\movies.csv')
        for row in range(5):
            for column in range(3):
                if column == 0:
                    item=QStandardItem(str(row+1))
                    self.model.setItem(row,column,item)
                else:
                    item=QStandardItem(df.iloc[row,column])
                    self.model.setItem(row,column,item)
        #实例化表格视图，设置模型为自定义的模型
        self.tableView=QTableView()
        self.tableView.setModel(self.model)

        #水平方向标签拓展剩下的窗口部分，填满表格
        self.tableView.horizontalHeader().setStretchLastSection(True)
        #水平方向，表格大小拓展到适当的尺寸
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # #TODO 优化3 删除当前选中的数据
        # indexs=self.tableView.selectionModel().selection().indexes()
        # print(indexs)
        # if len(indexs)>0:
        #     index=indexs[0]
        #     self.model.removeRows(index.row(),1)


        #设置布局
        layout=QVBoxLayout()
        layout.addWidget(self.tableView)
        self.setLayout(layout)