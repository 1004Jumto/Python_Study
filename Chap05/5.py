# gui 전용 쉘인 파이썬 확장자 pyw사용

# 점을 세개 찍어 삼각형을 그리는 프로그램

# graphics.py를 import함
from graphics import*

# 클래스를 사용하여 점 세개를 찍어 삼각형을 그리는 main()함수를 정의함. 
def main():

     # 객체 win은  클래스 GraphWin의 인스턴스. 윈도우의 이름(Draw a Triangle)을 설정함.
     # setCoords메소드를 호출하여 좌측 하단 모서리 좌표(0,0)에서 우측 상단 모서리 좌표(10,10)로 윈도우 생성.
     win = GraphWin("Draw a Triangle")
     win.setCoords(0.0, 0.0, 10.0, 10.0)

     # Text()함수를 사용하여 좌표(5,0.5)에 해당 문자열(Click on three points)을 message에 저장.
     # message를 draw메소드를 호출하여 윈도우에 출력함. 
     message = Text(Point(5, 0.5), "Click on three points")
     message.draw(win)

     # 마우스로 클릭한 지점 좌표값을 반환하는 getMouse메소드를 사용함.
     # 사용자가 찍은 세개의 점의 좌표값을 객체 p1,p2,p3에 반환하여 draw메소드를 사용하여 윈도우에 그림.  
     p1 = win.getMouse()
     p1.draw(win)
     p2 = win.getMouse()
     p2.draw(win)
     p3 = win.getMouse()
     p3.draw(win)

     # 객체 triangle은 클래스 Polygon의 인스턴스로, 윈도우에 삼각형을 그림.
     # setFill, setOutline, draw 메소드를 사용하여 도형 색상채우기(peachpuff), 선 색상(cyan청록색)을 정하고 윈도우에 그림. 
     triangle = Polygon(p1,p2,p3)
     triangle.setFill("peachpuff")
     triangle.setOutline("cyan")
     triangle.draw(win)

     # 위에서 선언했던 message를 setText 메소드를 사용하여 문자를 "Click anywhere to quit."로 바꿈. 
     # 아무곳이나 클릭한 뒤 프로그램 종료.
     message.setText("Click anywhere to quit.")
     win.getMouse()

#main()함수 호출
main()