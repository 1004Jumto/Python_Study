#-*- coding: utf-8 -*-

# 클래스, 오버로딩, 상속을 사용해 문장을 완성하는 프로그램.
# HousePark 클래스 생성. 
class HousePark:

     # 클래스 변수 lastname 선언. 객체변수와 달리 모든 객체에 공유됨.  
     lastname = "박"

     # 문장을 만들기 위한 여러 메소드 생성.
     # __init__메소드는 생성자로 객체가 생성되면 자동으로 호출됨. self와 name을 매개변수로 입력받음.
     # 멤버변수 self.fullname 선언.  
     def __init__(self,name):
          self.fullname = self.lastname + name

     # travel, love, fight 메소드를 만듦. 각각 self를 포함한 두개의 매개변수를 입력받음
     # 문자열 포맷팅을 사용해 각각 상황에 맞는 문자열을 출력함. 
     def travel(self,where):
          print("%s, %s여행을 가다." %(self.fullname, where))
     def love(self,other):
          print("%s, %s 사랑에 빠졌네" %(self.fullname, other.fullname))
     def fight(self,other):
          print("%s, %s 싸우네" %(self.fullname, other.fullname))

          
     def __add__(self,other): # + 연산자 오버라이딩 메소드.
          print("%s, %s 결혼했네" %(self.fullname, other.fullname))
     def __sub__(self,other): # - 연산자 오버라이딩 메소드.
          print("%s, %s 이혼했네" %(self.fullname, other.fullname))

# HouseKim클래스에 HousePark클래스를 상속하여 같은 기능을 물려주고 그 외 메소드를 생성하여 기능 확장. 
class HouseKim(HousePark):

     
     lastname = "김"  # 부모 클래스의 동일한 클래스 변수 오버라이딩.

     # 메소드를 추가하여 HouseKim 클래스의 기능을 확장시킴. 세개의 매개변수(self.fullname, where, day)를 입력받음.
     # 포맷팅을 사용하여 문자열 출력.
     def travel(self,where,day):   # 메소드의 Signature 가 다르므로 오버로딩.
          print("%s, %s 여행 %d일 가네." %(self.fullname, where, day))


# 객체 pey는 HousePark 클래스의 인스턴스.
# __init__메소드가 자동으로 호출되어 self.fullname이 "박응용"으로 생성됨. 같은 방식으로 클래스 HouseKim에서 "김줄리엣"이 self.fullname에 반환.
pey = HousePark("응용")  # "박응용" 
juliet = HouseKim("줄리엣") # "김줄리엣"

# 객체.메소드 형태로 호출되므로 self는 생략.
# travel메소드가 호출되어 "박응용, 부산여행을 가다.", "김줄리엣, 부산 여행 3일 가네."가 출력됨.
pey.travel("부산")
juliet.travel("부산",3)

# love, fight메소드가 호출되어 "박응용, 김줄리엣 사랑에 빠졌네", "박응용, 김줄리엣 싸우네"가 출력됨.
# 연산자 메소드가 호출되어 "박응용, 김줄리엣 결혼했네", "박응용, 김줄리엣 이혼했네"가 출력됨. 
pey.love(juliet)
pey + juliet
pey.fight(juliet)
pey - juliet



