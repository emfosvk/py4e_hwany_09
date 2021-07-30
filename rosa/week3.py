##################################################################################
#📌Q1. 숫자를 입력 받고 그 숫자의 구구단을 출력하는 함수를 만들어 봅시다. 다만 아래의 조건을 만족해 주세요.
#조건 1: 홀 수 번째만 출력하기
#조건 2: 값이 50이하인 것만 출력하기
#
#🔽 출력 예시
## 입력
#number = int(input("몇 단? : "))
#gugudan(number)
#
## 출력
#몇 단? : 8
#8 단
#8 X 1 = 8
#8 X 3 = 24
#8 X 5 = 40


print('====================== [START] [Q1] 구구단 ')
def gugudan(num) : 
    if num >= 1 and num <= 9 : 
        for i in range(1, 10) :
            gugudanResult = num * i
            # 조건2의 50이상 미출력 떄문에 조건문 추가
            if gugudanResult < 50 :
                print(str(num) + ' * ' + str(i) + ' = ' + str(gugudanResult))
            else :
                break
    else :
        print('구구단은 1 ~ 9 사이의 숫자를 입력해주세요.')

#실제 실행문
number = int(input("몇 단? : "))
gugudan(number)

print('====================== [E N D] [Q1] 구구단 ')


##################################################################################
#📌Q2. 가위바위보 업그레이드 버젼을 함수로 만들어 봅시다. 아래와 같은 조건을 만족해 주세요.
#조건 1: 게임을 몇 판을 진행할 것인지 입력을 받아주기
#조건 2: 0, 1, 2, "가위", "바위", "보" 이외에 다른 입력을 받으면 재입력 받기
#조건 3: 게임종료 후 나와 컴퓨터의 총 전적 출력하기
#
#🔽 출력 예시
## 입력
#games = int(input("몇 판을 진행하시겠습니까? : "))
#rsp_advanced(games)
#
## 출력
#가위 바위 보 : 0
#나: 가위
#컴퓨터: 보
#1 번째 판 나의 승리!
#
#가위 바위 보 : 1
#나: 바위
#컴퓨터: 가위
#2 번째 판 나의 승리!
#
#나의 전적: 2승 0무 0패
#컴퓨터의 전적: 0승 0무 2패
print()
print('====================== [START] [Q2] 업그레이드 가위바위보')
import random

rpsList = ['가위', '바위', '보']
rpsResultList = [
  ['D','L','W'],
  ['W','D','L'],
  ['L','W','D']
]

def rsp_advanced(number) : 
    
    gameRound = 0
    winCnt = 0
    drawCnt = 0
    loseCnt = 0

    while gameRound < number :
        userRspStr = input((str(gameRound + 1) + "회차 : 가위(0) 바위(1) 보(2)를 내주세요 >"))
        userRsp = convertInputToRsp(userRspStr)
        if userRsp < 0 or userRsp > 2 : 
            print('올바르지 않은 입력입니다.')
            continue
        
        comRsp = random.randint(0, 2)

        print('사용자 : ' + rpsList[userRsp])
        print('컴퓨터 : ' + rpsList[comRsp])
        roundResultCode = rpsResultList[userRsp][comRsp]
        if roundResultCode == 'W' :
            winCnt += 1
            print('당신의 승리입니다.')  
        elif roundResultCode == 'D' :
            drawCnt += 1
            print('비겼습니다.')
        elif roundResultCode == 'L' :
            loseCnt += 1
            print('컴퓨터의 승리입니다.')
        else :
            print('알수 없는 코드값 > ' + str(gameRound + 1) + '회차를 다시 실행합니다.')
            continue
        print(str(gameRound + 1) + '회차 까지의 누적 전적')
        print(str(winCnt) + '승 / ' + str(drawCnt) + '승 / ' + str(loseCnt) + '패')
        gameRound += 1
        
def convertInputToRsp(userInputData) :
    try :
        userInputStr = ''
        if userInputData == '가위' :
            userInputStr = '0'
        elif userInputData == '바위' :
            userInputStr = '1'
        elif userInputData == '보'   :
            userInputStr = '2'
        else :
            userInputStr = userInputData

        userRsp = int(userInputStr)
        if userRsp < 0 or userRsp > 2 :
            return -1
        else :  
            return userRsp

    except :
        return -1

#실제 실행문
games = int(input("몇 판을 진행하시겠습니까? : "))
rsp_advanced(games)

print('====================== [E N D] [Q2] 업그레이드 가위바위보 ')


##################################################################################
#📌Q3. 2개의 숫자를 입력하여 그 사이에 짝수만 출력하는 함수를 만들어 봅시다. 
#그리고 중앙값도 함께 출력 해봅시다.(중앙값이 홀수라면 제외)
#중앙값: 정중앙에 있는 값
#특정 두 숫자 사이의 수들을 리스트로 만드는 법
#
#n = 1
#m = 10
#numbers = [ i for i in range(n,m+1)] # [1,2,3,4,5,6,7,8,9,10]
## range(시작 숫자, 끝 숫자 + 1)
#🔽 출력 예시
#
## 입력
#n = int(input("첫 번째 수 입력 : "))
#m = int(input("두 번째 수 입력 : "))
#find_even_number(n, m)
#
## 출력
#첫 번째 수 입력 : 1
#두 번째 수 입력 : 11
#2 짝수
#4 짝수
#6 짝수
#6 중앙값
#8 짝수
#10 짝수
#
#
print()
print('====================== [START] [Q3] 짝수만 출력 및 중간숫자 출력')
def find_even_number(n, m) : 
    
    if m < n : 
        frNum = m
        toNum = n
    else : 
        frNum = n
        toNum = m
        
    numbers = [ i for i in range(frNum,toNum+1)]
    
    print('첫 번째 입력 값 : [ ' + str(n) + ' ]')
    print('두 번째 입력 값 : [ ' + str(m) + ' ]')

    centerNum = int(round((frNum + toNum) / 2, 0))
    for i in numbers :
        if i % 2 == 0 :
            print('[ ' + str(i) + ' ] 짝수' )
            
        if i == centerNum :
            # 중간값의 의미가 모호하여 그냥 평균값의 반올림을 표기하도록 처리
            # 예를 들어 1과 12의 가운데 값은 6.5인데 처리 방법이 없음.
            # 우선 표기를 위해 반올림해서 7에서 루프가 걸리도록 처리하였음.
            print('[ ' + str(i) + ' ] 중간값 (반올림)' )


#실제 실행문
n = int(input("첫 번째 수 입력 : "))
m = int(input("두 번째 수 입력 : "))
find_even_number(n, m)

print('====================== [E N D] [Q3] 짝수만 출력 및 중간숫자 출력')

##################################################################################
#📌Q4. 2개의 숫자를 입력하여 그 사이에 소수가 몇 개인지 출력하는 함수를 만들어 봅시다.
#소수: 1과 자기 자신만을 약수로 가지는 수
#
#🔽 출력 예시
## 입력
#n = int(input("첫 번째 수 입력 : "))
#m = int(input("두 번째 수 입력 : "))
#count_prime_number(n, m)
#
## 출력
#소수개수  4
print()
print('====================== [START] [Q4] 소수 갯수 출력기')
def count_prime_number(n, m) :
    if m < n : 
        frNum = m
        toNum = n
    else : 
        frNum = n
        toNum = m
    
    numbers = [ i for i in range(frNum,toNum+1)]
    
    primeNumList = []
    

    ####[Calculator Prime Number - START]
    for i in numbers :
        
        # 소수중에서 제일 작은 숫자는 2 이므로 그 이하값일 경우 계산 필요 없이 패스 처리
        if i < 2 : 
            continue

        # 모든 약수는 사실상 제곱근 보다 작은 숫자에서 걸림.
        # n-1까지는 계산할 필요가 없으므로, 제곱근에서 버림값을 최대 검사 숫자로 지정한다.
        squareRoot = i**(1/2)
        # math 모듈의 다른기능을 굳이 사용하지 않고
        # int로 씌우기만해도 바로 버림 기능이 작동함
        maxDevideNum = int(squareRoot) 

        # 제곱근이 2보다 작으면 무조건 소수임.
        if maxDevideNum < 2 :
            primeNumList += [i]
            continue    
        else :
            #소수인지 아닌지 검증을 위한 변수
            primeNumBool = True

            for j in range(2, maxDevideNum + 1) :
                #나눠서 딱 떨어지는 숫자가 나오는 경우는 소수 아님.
                if i % j == 0 :
                    primeNumBool = False
                    break

            if primeNumBool == True :
                primeNumList += [i]
    
    primeNumOneLine = ''
    for i in range(0,len(primeNumList)) :
        primeNumOneLine += str(primeNumList[i])
        if i < (len(primeNumList) - 1) :
            primeNumOneLine += ', '
    ####[Calculator Prime Number - E N D]
    
    print('첫 번째 입력 값 : [ ' + str(n) + ' ]')
    print('두 번째 입력 값 : [ ' + str(m) + ' ]')
    print('검색된 소수의 갯수 : ' + str(len(primeNumList)))
    print('검색된 소수의 목록 : ' + '[ '+ primeNumOneLine + ' ]')
        

#실제 실행문
n = int(input("첫 번째 수 입력 (자연수) : "))
m = int(input("두 번째 수 입력 (자연수) : "))
count_prime_number(n, m)

print('====================== [E N D] [Q4] 소수 개수 출력기')