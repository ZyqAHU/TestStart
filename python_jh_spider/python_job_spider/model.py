from preprocessing import getXandY
import numpy as np
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import RandomOverSampler
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
import pickle

def save_model(filename):
    X,y = getXandY(filename+'.csv')
    #将列表转化为矩阵格式
    X = np.array(X)
    y = np.array(y)
    #分割数据，将20%的数据作为测试集，其余作为训练集
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=66)#random_state参数使得每次分割的结果一样
    #朴素随机过采样
    smo = RandomOverSampler(sampling_strategy={0:95, 1:550, 2:200, 3:20},random_state=66)
    X_train, y_train = smo.fit_sample(X_train, y_train)

    from sklearn.neighbors import KNeighborsClassifier
    #创建KNN分类器
    clf = KNeighborsClassifier(algorithm='brute',leaf_size=1,n_neighbors=9,weights='distance')
    clf.fit(X_train, y_train)
    print('KNN')
    print(clf.score(X_test,y_test))
    with open(filename+'_knn.model', 'wb', encoding='utf-8', errors='ignore') as fw:
        #序列化方法
        pickle.dump(clf, fw)

    from sklearn.linear_model import LogisticRegression
    #逻辑回归
    clf = LogisticRegression(multi_class='ovr',solver='newton-cg')
    clf.fit(X_train, y_train)
    print('LogisticRegression')
    print(clf.score(X_test,y_test))
    with open(filename+'_logistic.model', 'wb', encoding='utf-8', errors='ignore') as fw:
        pickle.dump(clf, fw)

    from sklearn.naive_bayes import MultinomialNB
    #朴素贝叶斯
    clf = MultinomialNB()
    clf.fit(X_train, y_train)
    print('MultinomialNB')
    print(clf.score(X_test,y_test))
    with open(filename+'_NB.model', 'wb', encoding='utf-8', errors='ignore') as fw:
        pickle.dump(clf, fw)

    from sklearn.ensemble import RandomForestClassifier
    #随机森林
    clf = RandomForestClassifier(n_estimators=17,criterion='gini',min_samples_leaf=1)
    clf.fit(X_train, y_train)
    print('RandomForestClassifier')
    print(clf.score(X_test,y_test))
    with open(filename+'_RF.model', 'wb', encoding='utf-8', errors='ignore') as fw:
        pickle.dump(clf, fw)

    from sklearn import tree
    #决策树
    clf = tree.DecisionTreeClassifier()
    clf.fit(X_train, y_train)
    print('DecisionTreeClassifier')
    print(clf.score(X_test,y_test))
    with open(filename+'_DT.model', 'wb', encoding='utf-8', errors='ignore') as fw:
        pickle.dump(clf, fw)

    from sklearn.svm import SVC
    #支持向量机
    clf = SVC(kernel='rbf', probability=True)
    clf.fit(X_train, y_train)
    print('SVM')
    print(clf.score(X_test,y_test))
    with open(filename + '_SVM.model', 'wb', encoding='utf-8', errors='ignore') as fw:
        pickle.dump(clf, fw)

    from sklearn.neural_network import MLPClassifier
    #神经网络
    mlp = MLPClassifier(hidden_layer_sizes=(200, ),activation='tanh',max_iter=1000,learning_rate_init = 0.01,solver='sgd')
    mlp.fit(X_train, y_train)
    print('MLP')
    print(mlp.score(X_test,y_test))
    with open(filename + '_NN.model', 'wb', encoding='utf-8', errors='ignore') as fw:
        pickle.dump(clf, fw)

filename = ['java','python','php','web','android','test','ios','ai','dba','ops','bi']
for i in filename:
    save_model(i)