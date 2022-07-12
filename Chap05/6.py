# 2114267_이예진_프로그래밍 리포트 #3
# 퀴즈 점수 분포 그래프를 나타내는 프로그램


from graphics import*

 
def main():

     print("퀴즈 점수 분포도를 그래프로 나타내주는 프로그램입니다.")

     principal = eval(input("Enter the initial principal: "))
     apr = eval(input("Enter the annualized interest rate: "))

    
     win = GraphWin("Quiz Score histogram", 700, 400)
     win.setBackground("white")
     win.setCoords(-1.75, -200, 11.5, 20000)

     
     Text(Point(0,-1), ' 0.0k').draw(win)
     Text(Point(2500,-1), ' 2.5k').draw(win)
     Text(Point(5000,-1), ' 5.0k').draw(win)
     Text(Point(7500,-1), ' 7.5k').draw(win)
     Text(Point(10000,-1), ' 10.0k').draw(win)

 
     bar = Rectangle(Point(0, 0), Point(1, principal))
     bar.setFill("white")
     bar.setWidth(2)
     bar.draw(win)

     for year in range(1,11):
          principal = principal*(1 + apr)
          bar = Rectangle(Point(year, 0), Point(year+1, principal))
          bar.setFill("white")
          bar.setWidth(2)
          bar.draw(win)

     input("Press <Enter> to quit")
     win.close()

main()




