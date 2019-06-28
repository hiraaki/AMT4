from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
import numpy as np
import pandas as pd


def accuracy(y_true: object, y_pred: object) -> object:
    return np.mean(np.equal(y_true, y_pred))


def sortSecond(val):
    return val[1]


#carrega o arquivo do disco
data_frame = pd.read_csv("ct\\Base1.csv")
x = data_frame.iloc[:, 1:17].values
y = data_frame.iloc[:, 17].values
# #
# BestK = -1
# BKAcur = -1
# for i in range(1, 35):
#     Kacur = 0
#     for j in range(5):
#         # divide a base em 50% para treino, 25% para teste e 25% para validação
#         train_x, aux_x, train_y, aux_y = train_test_split(x, y, test_size=0.5)
#         validation_x, test_x, validation_y, test_y = train_test_split(aux_x, aux_y, test_size=0.5)
#         nbrs = KNeighborsClassifier(n_neighbors=i, algorithm='auto')
#         nbrs.fit(train_x, train_y)
#         Kacur += accuracy(test_y, nbrs.predict(test_x))
#     Kacur = Kacur / 5
#     if Kacur > BKAcur:
#         BKAcur = Kacur
#         BestK = i
# print(BestK)
# print(BKAcur)
# print("--------------------")
# # train_x, aux_x, train_y, aux_y = train_test_split(x, y, test_size=0.5)
# # validation_x, test_x, validation_y, test_y = train_test_split(aux_x, aux_y, test_size=0.5)
# # nbrs = KNeighborsClassifier(n_neighbors=1, algorithm='auto')
# # nbrs.fit(train_x, train_y)
# #
# # print(nbrs.predict((test_x[5], test_x[1000])))
# # print(test_y[500], test_y[1000])
# #
#
# TreeAcu = []
# TreeMed = []
# for i in range(10):
#     train_x, aux_x, train_y, aux_y = train_test_split(x, y, test_size=0.5)
#     validation_x, test_x, validation_y, test_y = train_test_split(aux_x, aux_y, test_size=0.5)
#     for j in range(1, 20):
#         decision = DecisionTreeClassifier(min_samples_leaf=j)
#         decision = decision.fit(train_x, train_y)
#         # print(accuracy(test_y, decision.predict(test_x)))
#         TreeAcu.append((j, accuracy(test_y, decision.predict(test_x))))
# for i in range(1, 20):
#     acu = 0
#     for treeacu in TreeAcu:
#         if treeacu[0] == i:
#             acu += treeacu[1]
#     TreeMed.append((i, acu/10))
# bestMF = [0, -1]
# for treemed in TreeMed:
#     if treemed[1] > bestMF[1]:
#         bestMF = treemed
#
# print(bestMF)
# print("--------------------")
# #
SVCacu = []
SVCMed = []
for i in range(10):
    train_x, aux_x, train_y, aux_y = train_test_split(x, y, test_size=0.5)
    validation_x, test_x, validation_y, test_y = train_test_split(aux_x, aux_y, test_size=0.5)
    for j in np.arange(0.05, 20.0, 0.05):
        svm = SVC(C=j, kernel='rbf', gamma='scale')
        svm.fit(train_x, train_y)
        SVCacu.append((j, 'rbf', accuracy(test_y, svm.predict(test_x))))
    for j in np.arange(0.05, 20.0, 0.5):
        svm = SVC(C=j, kernel='poly', gamma='scale')
        svm.fit(train_x, train_y)
        SVCacu.append((j, 'poly', accuracy(test_y, svm.predict(test_x))))
for i in np.arange(0.01, 2.0, 0.02):
    rbfacu = 0
    polyacu = 0
    for svcacu in SVCacu:
        if svcacu[0] == i:
            if svcacu[1] == 'poly':
               polyacu += svcacu[2]
            else:
                rbfacu += svcacu[2]
    SVCMed.append((i, 'poly', polyacu/10))
    SVCMed.append((i, 'rbf', rbfacu/10))
SVCBest = (0.0, '', -1)
for svcmed in SVCMed:
    if svcmed[2] > SVCBest[2]:
        SVCBest = svcmed
print(SVCBest)
#
Best = ((0, 0), 0)
Acur = []
for k in range(20):
    print(k)
    train_x, aux_x, train_y, aux_y = train_test_split(x, y, test_size=0.5)
    validation_x, test_x, validation_y, test_y = train_test_split(aux_x, aux_y, test_size=0.5)
    for i in range(1, 20):
        for j in np.arange(0.005, 0.1, 0.005):
            for l in range(100, 1000, 100):
                mlp = MLPClassifier(hidden_layer_sizes=(i,), learning_rate_init=j, max_iter=l)
                mlp.fit(train_x, train_y)
                Acur.append(((i, j, l), accuracy(test_y, mlp.predict(test_x))))

            # print(Acur)
# print(Acur)
Medias = []
for i in range(2, 10):
    for j in range(1, 10):
        for k in range(200, 300):
            Media = 0
            for acur in Acur:
                if acur[0] == (i, j, k):
                    Media += acur[1]
            Medias.append(((i, j), Media/10))
# print(Medias)
for acur in Acur:
    if acur[1]>Best[1]:
        Best = acur
print(Best)
