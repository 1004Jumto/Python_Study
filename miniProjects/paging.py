# paging.py
# 게시판 프로그램 - 필요한 총 페이지 수를 알려주는 프로그램

# 게시물 총 건수(m)와 한 페이지에 보여줄 게시물 수(n)를 입력받아 총 페이지 수를 리턴해주는 함수 정의
def getPage(m, n): 
    page, remainder = divmod(m, n) # divmod 함수를 통해 입력받은 수 m을 n으로 나눈 몫과 나머지를 각각 변수에 저장함 
    if remainder > 0: # 만약 0으로 나누어 떨어지지 않는 경우 페이지 수를 하나 더해줌
        page += 1 
    return page  # 총 페이지 수를 결과값으로 리턴

print("필요한 총 게시판페이지 수를 알려주는 프로그램입니다.\n")    # 프로그램 설명
a = int(input("게시물 총 건수를 입력해주세요: "))        # 게시물 총 건수, 게시물 수를 입력받음
b = int(input("한 페이지에 보여줄 게시물 수를 입력해주세요: "))

result = getPage(a, b)    # getPage 함수 호출하여 결과값 출력 
print(result)
