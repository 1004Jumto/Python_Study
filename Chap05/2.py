# 원금과 이자율을 입력받아 10년동안 돈이 늘어나는 정도를 그래프를 통해 보여주는 프로그램.

# graphics.py파일을 import함. 
from graphics import*

# 원금, 이자율을 입력받아 성장율을 그래프로 보여주는 main() 함수를 클래스와 for문을 사용하여 정의함.  
def main():

     # 사용자에게 프로그램에 대한 설명 출력.
     print("THis program plots the growth of a 10-year investment.")

     # 원금과 이자율을 각각 input()함수를 통해 입력받는 변수 principal, apr을 선언함.
     # eval() 함수는 문자열로 저장된 데이터를 수의 형태로 변환시킴. 
     principal = eval(input("Enter the initial principal: "))
     apr = eval(input("Enter the annualized interest rate: "))

     # 객체 win은 GraphWin의 인스턴스로 윈도우의 이름, 크기를 정함. setBackground 메소드 호출. 
     # setBackground 메소드는 self 포함 두개의 매개변수를 입력받고, 윈도우의 배경색(흰색)을 설정함.
     # setCoords 메소드는 self포함 다섯개의 매개변수를 입력받음. 좌측 하단 모서리 좌표에서 우측 상단 모서리 좌표로 실행할 윈도우 설정.
     win = GraphWin("Investment Growth Chart", 320, 240)
     win.setBackground("white")
     win.setCoords(-1.75, -200, 11.5, 10400)

     # Text()함수는 문자열을 원하는 위치를 지정하는 함수로 y축 좌표 5개를 draw메소드를 사용해 윈도우에 써넣음.
     Text(Point(-1,0), ' 0.0k').draw(win)
     Text(Point(-1,2500), ' 2.5k').draw(win)
     Text(Point(-1,5000), ' 5.0k').draw(win)
     Text(Point(-1,7500), ' 7.5k').draw(win)
     Text(Point(-1,10000), ' 10.0k').draw(win)

     # 객체 bar는 사각형을 그리는 Rectangle클래스의 인스턴스로 좌측 하단 모서리 좌표와 우측 상단 모서리 좌표를 매개변수로 받음.
     # 여기에선 맨 첫번째 막대그래프의 모양과 크기를 설정. 
     # setFill, setWidth, draw 메소드를 호출하여 막대그래프의 색(초록), 선두께(2), 너비를 설정한 후 윈도우에 그림. 
     bar = Rectangle(Point(0, 0), Point(1, principal))
     bar.setFill("green")
     bar.setWidth(2)
     bar.draw(win)

     # 반복문 for문을 이용하여 돈을 계산하고, 그에 맞게 나머지 10개의 막대그래프를 그려줌.
     # 막대그래프의 모양은 길이를 제외하고 위의 첫번째 막대그래프와 같이 해줌.
     for year in range(1,11):
          principal = principal*(1 + apr)
          bar = Rectangle(Point(year, 0), Point(year+1, principal))
          bar.setFill("green")
          bar.setWidth(2)
          bar.draw(win)

     # close메소드를 통해 enter 치면 창을 닫고 프로그램을 종료함.
     input("Press <Enter> to quit")
     win.close()
     
# main()함수 호출하여 실행함.
main()

