# 들여쓰기 기준은 1tab or 4spaces
# 탭이 툴에따라 다르게 표기될 가능성이 있으므로 4스페이스로 하는것을 추천
# exec(open("rosa/chapter03.py").read())

# if 조건 : 
#     실행문 1
# elif 조건 : 
#     실행문 2
# else
#     실행문 3

# try :
#     정상작동시 실행문
# except :
#     에러발생시 실행문


inputData = input('숫자 입력 하세요')

try :
    inputInt = int(inputData)

    if inputInt < 0 :
        print('입력 값은 음수')
    elif inputInt > 0 :
        print('입력 값은 양수')
    else :
        print('입력 값 0')

except :
  print('int 형 변환 실패 - 값 : ' + inputData)