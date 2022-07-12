# 탭을 4개의 공백으로 바꾸는 프로그램

# re모듈, sys모듈을 import
import re 
import sys 

# 사용자에게 사용법(양식) 설명, sys.argv[0]은 프로그램 이름
def Usage(): 
    print("Usage: python %s filename" % sys.argv[0]) 

# 사용자가 입력한 파일(sys.argv[1])을 오픈.
# 없다면 예외처리로 usage()함수를 호출한 뒤 
try: 
    f = open(sys.argv[1]) 
except: 
    Usage() 
    sys.exit(2) 

msg = f.read() 
f.close()       # 파일을 읽어 하나의 문자열로 인식해 msg에 저장후 닫기

p = re.compile(r'\t')   # re모듈에서 complie함수를 사용하여 탭을 모두 찾아 p에 저장
changed = p.sub(" "*4, msg) # sub함수를 사용하여 탭(msg)을 4개의 공백으로 교환하여 changed에 저장

f = open(sys.argv[1], 'w') 
f.write(changed) 
f.close()           # 파일을 열어 기존의 내용을 지우고 changed에 저장되어 있는 대로 파일을 쓴 후 클로즈.

