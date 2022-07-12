#점을 찍으면 그 좌표를 알려주는 프로그램

# graphics.py를 import함
from graphics import*

# 사용자가 클릭한 점의 좌표를 알려주는 main()함수를 클래스와 for문을 사용하여 정의함.
def main():

    # 객체 win은 클래스 GraphWin의 인스턴스. "Click Me!"라고 윈도우 창의 이름이 설정됨.
    # 반복문 for문을 통해 클릭한 마우스 좌표를 알려주는 실행을 10번 반복함.
     win = GraphWin("Click Me!")
     for i in range(10):
         # 클릭을 기다렸다가 클릭한 마우스 좌표값을 반환하는 메소드 getMouse를 호출. 좌표값을 변수 p에 반환하여 저장.
          p = win.getMouse()

         # getX(),getY() 함수는 각각 x좌표, y좌표값을 리턴하는 메소드.
          print("You clicked at: ", p.getX(), p.getY())

# main() 함수 호출
main()
