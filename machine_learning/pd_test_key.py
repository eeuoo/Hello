import pandas as pd

# 키, 몸무게, 유형 데이터프레임 생성
tbl = pd.DataFrame({
    'weight' : [80.0, 70.4, 65.5, 45.9, 51.2],
    'height' : [170, 180, 155, 143, 154],
    'type' : ['f', 'n', 'n', 't', 't'],
    'gender' : ['f', 'm', 'm', 'f', 'f']
})

# 몸무게 목록 추출
print('몸무게 목록')
print(tbl['weight'])

# 몸무게와 키 목록 추출
print('몸무게와 키 목록')
print( tbl[ ['weight', 'height'] ] )

# 0부터 세었을 때 2~3번째 데이터 추출
print( 'tbl[2:4]\n', tbl[2:4] )

# 0부터 세었을 때 3번째 이후의 데이터 출력
print( 'tbl[3:]\n', tbl[3:])
 
# 원하는 조건의 값 추출
print('------height 160 이상인 것')
print( tbl[tbl.height >= 160] )

print('------gender가 f인 것')
print( tbl[tbl.gender == 'f'] )

# 정렬
print('------키로 정렬')
print( tbl.sort_values(by='height') )

print('------몸무게로 정렬')
print( tbl.sort_values(by='weight'))



