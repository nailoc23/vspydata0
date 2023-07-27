import numpy as np
import pandas as pd

# 1번: csv 파일읽기
csv_file = 'data/movies.csv'
df = pd.read_csv(csv_file, encoding='utf-8')
# movieId, title, genres
# 인덱스번호
print(df) 

# 2번: 장르 종류 가져오기
# print(df['genres'].count())
# print(df.loc[10,:'genres'])
genres = [] # 장르의 정보를 저장
for gen in df['genres'] :
    genres.extend(gen.split('|')) # 입력없으면 공백으로 분리
# print(genres)
# print(len(genres))

# 3번: 장르들이 중복됨 - 중복제거
uni_genres = pd.unique(genres)
print( len(uni_genres))

# 4번: 장르별로 영화가 몇개씩 인가?
zero_result = np.zeros( len(uni_genres) ) # 20개의 영화갯수 np
result = pd.DataFrame(zero_result, index=uni_genres, columns=['갯수'])

# for gen in df['genres'] : 이거 대신 아래 처럼 코드가 된 이유?
for g in genres: # 장르를 | 로 분리해서 다 저장한 목록
    result.loc[g] += 1
print(result)    