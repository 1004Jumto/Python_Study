# a,b,c�� ���������� �Է¹���.
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

#a,b,c �����.
print(a,b,c)

#if���� �̿��� a,b,c�� ����. a,b = b,a�� a��b�� ���� �ٲ۴ٴ� �ǹ���.

if a > b:
     a, b = b, a
if b > c:
     b, c = c, b
if a > b:
     a, b = b, a
     
#������������ �� a,b,c ���.
print(a,b,c)

