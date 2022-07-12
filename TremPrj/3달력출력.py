# 연도와 월을 입력받아 그 달의 날짜 수를 알려주는 프로그램
# IsLeapYear 함수를 정의함. 윤년을 판별해줌. 2번과 같으므로 주석 생략.
def IsLeapYear(year):
     if year % 4 != 0:
          return False
     
     if year % 400 == 0:
          return True

     if year % 100 != 0:
          return True

     return False
 

# GetDayOfMonth 함수를 정의함. 연도와 월에 맞는 날짜 수를 결과값으로 갖는 함수.
# year, month 두 인자를 가지고, 조건문 if를 사용하여 정의함.

def GetDayOfMonth(year, month):
     
     # 먼저 입력받은 월이 2월인지 아닌지 확인함.
     if month == 2:

          # IsLeapYear함수를 호출하여 윤년인지 아닌지 판별함. 윤년이면 결과값이 True이므로 29를 리턴. 그렇지 않으면 28을 리턴함.
          if IsLeapYear(year):
               return 29
          else:
               return 28
          
     # 4,6,9,11월일 땐 무조건 30일이므로 30리턴. 해당 월 수가 더 적으므로 4,6,9,11월인지 먼저 조건문을 사용해 판단.
     if month == 4 or month == 6 or month == 9 or month == 11:
          return 30

     # 위의 조건문에 해당되지 않는 1,3,5,7,8,10,12월은 31을 리턴.
     return 31

# 먼저 사용자에게 프로그램에 대한 설명을 출력해줌.
print("해당 연도, 월의 날짜 수를 알려주는 프로그램입니다.\n")

# 메인코드. 무한루프를 만들어 계속해서 프로그램이 돌아가도록 설정함.
# y와 m 두 변수를 각각 입력받아 조건에 맞게 if문을 사용하여 코딩함.

while True:
     # 정수형으로 연도를 입력받음
     y = int(input("연도를 입력해주세요 : "))

     # -1이면 바로 종료 안내문구를 출력하고 break를 통해 루프를 빠져나가 종료됨.
     if y == -1:
          print("종료합니다.")
          break

     # 1이하의 값이 들어오면 1이상의 수로 입력하라는 문구 출력후 continue를 통해 while문의 처음으로 돌아가 다시 시작.
     if y < 1:
          print("연도를 1이상의 수로 입력해주세요.\n")
          continue

     #y와 같은 방식.
     m = int(input("월을 입력해주세요 : "))

     if m == -1:
          print("종료합니다.")
          break

     # m이 1이상 12이하의 수가 아닌 경우 해당 안내문자 출력후 while문 처음으로 돌아가 다시 입력받음.
     if  m < 1 or m > 12:
          print("월을 1이상 12이하의 수로 입력해주세요.\n")
          continue

     # GetDayOfMonth함수를 호출하여 각각 y와m을 대입하여 그 결과값을 result에 저장하고, 출력함.
     result = GetDayOfMonth(y, m)


     print(result)
     

