# 간단한 메모장

# sys모듈,time모듈을 import함
import sys 
import time 

# 조건문을 통해 메모장을 보거나 메모장에 내용을 추가하도록 프로그래밍
# 메모장 사용법을 설명하는 usage()함수 정의
def usage(): 
    print(""" 
Usage 
===== 
python %s -v : View memo 
python %s -a : Add memo 
""" % (sys.argv[0], sys.argv[0]))  # -v는 메모장을 보여주는 옵션, -a는 메모를 추가하는 옵션.
                                   # sys.argv[0]은 명령프롬프트에서 입력받은 값 중에서 프로그램 이름임

if not sys.argv[1:] or sys.argv[1] not in ['-v', '-a']: 
    usage()     # 만약 프로그램 이름만 치거나 옵션이 없다면 usage 함수를 호출하여 설명법을 알려줌 
                

elif sys.argv[1] == '-v': 
    try: 
        print(open("memo.txt").read()) 
    except IOError: 
        print("memo does not exist!")     # 옵션이 -v이면 사용자의 memo텍스트파일을 열어 읽고 
                                          # 에러는 예외처리로 돌려 존재하지 않는다고 출력

elif sys.argv[1] == '-a': 
    word = input("Enter memo: ") 
    f = open("memo.txt", 'a') 
    f.write('\n' + '[' + time.ctime() + '] ' + word) 
    f.close() 
    print("Added")          # 옵션이 -a이면 메모 내용을 입력받아 word에 저장한 후 텍스트파일을 열어 그 내용을 시간과 함께 추가함.
                            # 추가되면 사용자에게 추가되었다고 알린 후 종료.
