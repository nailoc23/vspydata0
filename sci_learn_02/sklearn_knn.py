import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()

iris_data = iris.data # numpy data
col_name = iris.feature_names # columns

df_iris = pd.DataFrame(data=iris_data, columns=col_name)
print(len(df_iris))
#print(df_iris) # 데이터를 가공=데이터처리 - 비정형데이터

# 지도학습 = 데이터 + 답(타겟)
#print(iris.target) # 150개의 훈련및테스트 데이터

# 학습하기 위해 훈련데이터 + 테스트데이터
x_train, x_test, y_train, y_test = train_test_split(iris['data'], iris['target'], random_state=0) # 랜덤시드 고정

print('x_test갯수:', x_test.shape)
print('y_test갯수:', y_test.shape)

# KNN 객체를 호출
super_knn = KNeighborsClassifier(n_neighbors=9)