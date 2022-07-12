# a,b,c를 정수형으로 입력받음.
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

#a,b,c 출력함.
print(a,b,c)

#if문을 이용해 a,b,c를 비교함. a,b = b,a는 a와b의 값을 바꾼다는 의미임.

if a > b:
     a, b = b, a
if b > c:
     b, c = c, b
if a > b:
     a, b = b, a
     
#오름차순으로 된 a,b,c 출력.
print(a,b,c)

