# 3과 5의 배수 합구하기

# result 초깃값을 0으로 저장
result = 0
for i in range(1,1000):     # i를 1부터 999까지 반복함 
    if i % 3 == 0 or i % 5 == 0:    # i가 3 또는 5의 배수일 경우에 result에 더해줌 
        result += i
print(result)   # 결과값 출력
