# 특정 디렉터리부터 그 하위 디렉토리파일을 순차적으로 검색하는 프로그램

# os모듈 import
import os

# 특정 디렉토리의 하위 디렉토리와 파일들을 모두 검색하는 함수 정의
def search(dirname): 
    flist = os.listdir(dirname) #listdir함수를 사용하여 해당 디렉토리에 있는 파일들의 리스트를 구함
    for f in flist:             # 리스트에서 파일을 꺼내 하나씩 아래를 반복함
        next = os.path.join(dirname, f) # os모듈의 path.join함수를 사용하여 디렉토리를 포함한 전체 경로를 포함한 파일이름을 구함. 
        if os.path.isdir(next):     
            search(next)    # 해당 파일이 디렉토리이면 다시 재귀함수를 호출
        else:
            doFileWork(next)    # 해당 파일이 파일이면 doFileWork함수 실행


# 파일 내용을 바꾸는 함수 doFileWork 정의  
def doFileWork(filename): 
    ext = os.path.splitext(filename)[-1] 
    
    if ext != ".py": 
        return          # 파일 확장자가 .py가 아니면 리턴
    
    if ext == '.py': 
        print(filename)   # 파일 확장자가 .py이면 파일이름 출력후 파일 오픈.
   
    f = open(filename)  
    before = f.read() 
    f.close()                 # 파일을 열어 기존 내용을 before에 저장한 후 보존.
    after = before.replace("ABC", "DEF")  #replace함수를 사용하여 ABC를 DEF로 바꾸어 저장함.
    
    f = open(filename, "w") 
    f.write(after) 
    f.close()     # 파일을 열어 기존 내용을 지우고 수정된 after를 쓴 후 클로즈.



search("d:/")       # D드라이브의 하위 파일들을 검색하도록 실행
