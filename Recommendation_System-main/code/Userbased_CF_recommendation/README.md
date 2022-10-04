## 协同过滤推荐算法(Collaborative Filtering)

### user-user based

#### 1.Main Idea

对于某user，寻找与该user评分相似的集合D，然后基于D来估计用户的评分



#### 2.寻找相似用户

设r~x~ 为用户的评分向量

* 余弦夹角

* 皮尔逊相关系数


#### 3.评分预测

设集合D为K个与user最相似的users，并且都对item s作出了评分

那么对于user对item s的评分为：

* 直接平均



* 加权平均



* many tricks possible...



