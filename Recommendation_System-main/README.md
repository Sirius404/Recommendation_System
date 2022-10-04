# Recommondation-System
一些传统推荐算法的实现，包括基于内容的推荐，协同过滤，矩阵分解、神经网络


### 测试数据

测试数据使用的是movielens数据集



### 实现算法

* 基于内容的推荐算法
* 基于物品的协同过滤推荐算法
* 基于用户的协同过滤推荐算法
* 矩阵分解的推荐算法
* 神经网络的推荐算法



### 代码结构

main.py  这是各种算法的入口

----data_preprocessing  对原始数据进行预处理的代码

----CB_recommendation  包含基于内容的推荐算法实现代码

----Userbased_CF_recommendation  包含基于用户的协同过滤推荐算法实现代码

----ItemBased_CF_recommendation 包含基于物品的协同过滤推荐算法实现代码

----MF_recommendation  包含矩阵分解推荐算法实现代码

----NN__CF 基于神经网络的推荐算法实现代码

----UI 简单的UI界面实现代码

----measure  一些用于计算度量的方法

----main 计算算法性能




###To do
结构耦合优化