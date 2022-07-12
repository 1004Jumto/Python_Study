#1. append�Լ��� ����Ͽ� ����Ʈ�� ���ڿ��� �߰���
mylist = []
mylist.append(8)
mylist.append(5)
mylist.append(9)
mylist.append(7)

print(mylist)

# �̶� extend�Լ��� ����ϸ� ���� append�Լ��� �׹� ������� �ʾƵ� 8,5,7,9�� �ѹ��� ����Ʈ�� �߰��� �� ����.
# mylist = []
# mylist.extend([8,5,7,9]) �Ǵ� mylist += [8,5,7,9]
# print(mylist)


#2. ����Ʈ�� �� ��0��° �ڸ��� 'python'�� insert�Լ��� ����� �����ϰ�, 'perls'�� remove�Լ��� ����� ��������.
mylist = ['dot','perls']
mylist.insert(0, 'python')
mylist.remove('perls')

print(mylist)


#3. b����Ʈ�� a����Ʈ�� ��ĥ �� ����.
a = [1, 2, 3]
b = [4, 5, 6]
b = b+a

print(b)


#4. append�Լ��� ����Ͽ� ����Ʈ�� ���ʷ� 'cat','dog','mouse'�� �߰���.
#   len�Լ��� ����Ͽ� ����Ʈ���� ��� ������ ���� �� �����.
animals = []
animals.append('cat')
animals.append('dog')
animals.append('mouse')
count = len(animals)

print(animals)
print(count)


#5. reverse�Լ��� ����Ͽ� ����Ʈ�� ������ �������� ������ �� ����.
#   sort�Լ��� ����Ͽ� ����Ʈ�� ��Ҹ� ������� ������ �� ����.
mylist = [200, 300, 100, 50]
mylist.reverse()
print(mylist)

mylist.reverse()
print(mylist)

mylist.sort()
print(mylist)


#6.
# lastchar �Լ��� �����ϸ� ���� s�� [-1]�� ������� ��.
def lastchar(s):
    return s[-1]

values = ["abc","bca","cab"]

# ����Ʈ abc, bca, cab ���� -1�ڸ��� �ִ� c,a,b�� �������� �����Ͽ� bca, cab, abc�� �Ǵ� �� ����.
values.sort(key=lastchar)
print(values)

# lamda�� ���� s�� 1�ڸ��� ��������� �����ִ� ��ȸ�� �Լ��� �� ����. �� s[1]�� ���� ���Ͽ� �����Ͽ� cab, abc, bca�� �Ǵ� �� ����.
values.sort(key=lambda s: s[1])
print(values)


#7. remove�Լ��� ���� ����Ͽ� 'Bill'�� ���ʷ� �ϳ���, �׸��� 'Tommy'�� ������ �� ����. 
names = ["Bill","Tommy","Bill","Janet","Stacy"]

names.remove("Bill")
print(names)

names.remove("Bill")
print(names)

names.remove("Tommy")
print(names)

    #remove�Լ� ��� del�Լ��� ����� ���� ����.
names = ["Bill","Tommy","Bill","Janet","Stacy"]

del names[0]
print(names)

del names[1]
print(names)

del names[0]
print(names)


#8. count�Լ��� ����Ͽ� ����Ʈ�ȿ��� a�� �� �� �������� Ƚ���� �� �� ����.
names = ['a','a','b','c','a']
number = names.count('a')

print(number)


#9.
# Input list.
values = ["uno", "dos", "tres", "cuatro"]

# Locate string.
# �ε����Լ��� ����� ���� 'dos'����ġ 2�� n�� ��. 
n = values.index("dos")
print(n, values[n])

# Locate another string.
# �ε����Լ��� ����� ���� 'tres'����ġ 2�� n�� ��.
n = values.index("tres")
print(n, values[n])

# Handle nonexistent string.

# try~except�� ���ܸ� ó���ϴ� ��������, ����Ʈ�ȿ� ���� ��Ұ� �ԷµǴ��� ������ ���� �ʰ� except�� ���� 'not found'�� ��������ν� ���ܸ� ó���� �� ����.
# except�� �Բ� pass�� ����� ���� ����
try:
    n = values.index("?")
    # Not reached.
    print(n)
except:
    # Value not found.
    print("Not found")

    

#10. 
# �� ����Ʈ�� ������.
elements = []

# �� ����Ʈ�ȿ� �� ����Ʈ �ΰ��� ������.
elements.append([])
elements.append([])

# �� ����Ʈ ���� ù��° �� ����Ʈ�� 1�� 2�� �߰���.
elements[0].append(1)
elements[0].append(2)
# �� ����Ʈ ���� �ι�° �� ����Ʈ�� 3�� 4�� �߰���.
elements[1].append(3)
elements[1].append(4)

# ����Ʈ elements�� 0�ڸ��� ����Ʈ���� 0�ڸ��� ��Ҹ� �����.
print(elements[0][0])

# 2���� ����Ʈ elements ��ü�� �����.
print(elements)


#11. �����Լ��� ����Ͽ� [0],[1],[2]�� ���ʷ� 10,20,30�� ������ ���ڿ��� �����.
list = [10, 20, 30]

res = str.format("The values are {v[0]}, {v[1]} and {v[2]}", v=list)
print(res)

#12.
# all(x)�� x�� ��Ұ� ��� ���̸� true�� ������.
# items ����Ʈ���� True�� ��, False�� None�� �����̹Ƿ� ��� ���� �ƴϱ� ������ false�� �����ְ� not�� ���� ���������� ����Ǿ� False�� ����ߴٰ� ������.
items = [False, None, True]
if not all(items):
    print(False)

# items ����Ʈ 10,20,30�� ��� ���̹Ƿ� true�� �����ְ� ���� ������ ����Ǿ� True�� ����ߴٰ� ������.    
items = [10, 20, 30]
if all(items):
    print(True)

# any(x)�� x�� ��Ұ� ��� �����̸� false�� �����ְ� ��� �� �ϳ��� ���� �ִٸ� true�� ������.
# ����Ʈ elements ���� "Pomegranate"�� ���̹Ƿ� ��� ������ �ƴϱ⶧���� true�� �����ְ� ���������� ����Ǿ� True�� ����ߴٰ� ������.
elements = [False, None, "Pomegranate", 0]
if any(elements):
    print(True)
    
# ����Ʈ elements ���� 0�� False��� �����̹Ƿ� false�� �����ְ� not�� ���� ���� ������ ����Ǿ� False�� �����.
elements = [0, 0, False]
if not any(elements):
    print(False)


