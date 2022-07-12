# convert_gui.pyw
# gui 전용 쉘인 파이썬 확장자 pyw사용

# 섭씨온도를 화씨온도로 변환해주는 프로그램

# graphics.py를 import함
from graphics import*

# 클래스를 사용하여 섭씨-화씨온도를 변환해주는 main()함수 정의
def main():

     # 객체 win은  클래스 GraphWin의 인스턴스. 윈도우의 이름(Celsius Converter), 크기를 설정함.
     # setCoords메소드를 호출하여 좌측 하단 모서리 좌표(0,0)에서 우측 상단 모서리 좌표(3,4)로 직사각형 박스 생성.
     win = GraphWin("Celsius Converter", 400, 300)
     win.setCoords(0.0, 0.0, 3.0, 4.0)

     # Text()함수를 사용하여 출력할 문자열을 좌표(1,3)에 지정하고 draw메소드를 통해 출력. 
     Text(Point(1,3), "   Celsius Temperature:").draw(win)
     Text(Point(1,1), "Fahrenheit Temperature:").draw(win)

     # 객체 input은 클래스 Entry의 인스턴스. 숫자를 입력받을 박스를 윈도우에 만듦.
     # 초기값을 "0.0"으로, 박스 색과 글씨 색상, 너비 등 모양을 설정해줌. 
     input =  Entry(Point(2,3), 5)
     input.setText("0.0")
     input.draw(win)

     # 객체 output은 클래스 Text의 인스턴스로 섭씨를 화씨로 변환한 결과값을 지정된 좌표(2,1)에 출력해줌. 
     output = Text(Point(2,1), "")
     output.draw(win)

     # 객체 button은 클래스 Text의 인스턴스로 "convert it"문자열을 지정된 좌표(1.5,2)에 출력해줌. 
     button = Text(Point(1.5, 2.0), "Convert It")
     button.draw(win)

     # 좌측 하단 모서리 좌표값과 우측 상단 모서리 좌표값으로 사각형 버튼을 윈도우에 만들어줌.
     Rectangle(Point(1,1.5), Point(2, 2.5)).draw(win)

     # 사용자의 마우스클릭을 기다렸다가 클릭되면 다음으로 넘어감. 
     win.getMouse()
     
     # 사용자로부터 변환하고자 하는 섭씨온도를 입력받아 화씨로 계산하여 변수 fahrenheit에 저장.
     celsius = eval(input.getText())
     fahrenheit = 9.0/5.0*celsius + 32

     # setText메소드를 호출하여 output객체에 화씨온도를 출력하고, 객체 button에 써있던 문자열을 "Quit"으로 바꿈
     output.setText(fahrenheit)
     button.setText("Ouit")

     # 마우스클릭을 기다렸다가 마우스가 클릭되면 윈도우를 닫고 프로그램을 종료함.
     win.getMouse()
     win.close()

#main()함수 호출하여 프로그램 실행.
main()