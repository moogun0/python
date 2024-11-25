## 3번째 일시
## 4번째 평균 기온

import csv

file_path = "test.csv"

with open(file_path,mode='r') as file:
    reader = csv.reader(file) ## 자바에서는 패키지, 파이썬에서는 모듈

    ##for i in range()
    ## 햫상된 for문 for v in 집합명

    ## 첫 출을 읽어버리고
    #시작해~

     ##if row[0]:
       ##    continue
    header = next(reader) # 그냥 첫줄을 읽는다(대부분 위에 있는 코드를 헤더라 부름"정형화 되어있음")

    
    for row in reader :
        #if 첫번째 시도면:
        #   continue
        #esle: print(row[일시]+row[평균기온])
        #print(row) # row 가 list 타입이라는 확인 가능 []이렇게 떠서!
        a = row[2]  ## 12월인 데이터만 출력
        b = row[-2]
        #if a가 Dec 시작하면 :
        if a.startswith("Dec"):
            print(a,b)

        
