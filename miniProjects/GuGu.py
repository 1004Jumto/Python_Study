
# 구구단 프로그램

# 구구단을 할 함수 GuGu정의
def GuGu(n):
    result = []  # 빈 리스트를 하나 만든 후 for문을 통해 구구단값들을 리스트에 저장함.
    for i in range(1,10):  # i가 1부터 9까지 반복됨
        result.append(n*i)
    return result  # 구구단 값들이 저장된 리스트를 결과값으로 리턴함.

print("구구단 프로그램입니다.\n") # 사용자에게 프로그램 설명
t = int(input("구구단을 실행할 숫자를 입력해주세요: ")) # 구구단 값을 정수형으로 입력받음
result = GuGu(t) # 위에서 정의한 GuGu(n) 함수 호출하여 결과값 출력
print(result)
