# 📌Q1. 숫자를 입력 받고 그 숫자의 구구단을 출력하는 함수를 만들어 봅시다. 다만 아래의 조건을 만족해 주세요.
# 조건 1: 홀 수 번째만 출력하기
# 조건 2: 값이 50이하인 것만 출력하기
# 🔽 출력 예시
# # 입력
# number = int(input("몇 단? : "))
# gugudan(number)
#
# # 출력
# 몇 단? : 8
# 8 단
# 8 X 1 = 8
# 8 X 3 = 24
# 8 X 5 = 40


def oddGuguMaker (Num):
    result = Num
    i=1
    print('몇 단? :', Num)
    print(Num,'단')
    while result <= 50 :
        print(Num,'X',i,'=',result)
        i +=2
        result = Num * i

while 1 :

    inputNum=input('숫자를 입력하세요:')
    try :
        inputNum=int(inputNum)
    except :
        inputNum = -1

    if inputNum >0:
        oddGuguMaker(inputNum)
        break
    else:
        print('입력값은 1이상의 정수로 입력해주세요')

# Q2. 가위바위보 업그레이드 버젼을 함어 봅시수로 만들다. 아래와 같은 조건을 만족해 주세요.
# 조건 1: 게임을 몇 판을 진행할 것인지 입력을 받아주기
# 조건 2: 0, 1, 2, "가위", "바위", "보" 이외에 다른 입력을 받으면 재입력 받기
# 조건 3: 게임종료 후 나와 컴퓨터의 총 전적 출력하기
# :작은_아래쪽_화살표: 출력 예시
# # 입력
# games = int(input("몇 판을 진행하시겠습니까? : "))
# rsp_advanced(games)
# # 출력
# 가위 바위 보 : 0
# 나: 가위
# 컴퓨터: 보
# 1 번째 판 나의 승리!
# 가위 바위 보 : 1
# 나: 바위
# 컴퓨터: 가위
# 2 번째 판 나의 승리!
# 나의 전적: 2승 0무 0패
# 컴퓨터의 전적: 0승 0무 2패

import random

winCnt= 0
drawCnt =0
loseCnt =0
round = 1
flag = -1

# 입력된 0,1,2를 가위,바위,보로 변환하기
def converter(a):
    a = str(a)
    if a == '0':
        return '가위'
    elif a == '1':
        return '바위'
    elif a == '2':
        return '보'
    else:
        return a

def winner(player, cpu):  # 승패가 나는 경우의 수는 6가지,
    battle = player + cpu
    global winCnt
    global  loseCnt
    if battle == '가위바위':
        loseCnt +=1
        return '컴퓨터가'
    elif battle == '가위보':
        winCnt +=1
        return '당신이'
    elif battle == '바위보':
        loseCnt += 1
        return '컴퓨터가'
    elif battle == '바위가위':
        winCnt += 1
        return '당신이'
    elif battle == '보가위':
        loseCnt += 1
        return '컴퓨터가'
    elif battle == '보바위':
        winCnt += 1
        return '당신이'
    else:
        return '말도 안되는 일이 일어남'

print('###########Q1##########')
# player와 cpu의 가위,바위,보 입력받기


while not flag > 0 :

    battleCnt = input("몇 판을 진행하시겠습니까? :")
    try :
        flag = int(battleCnt)
    except :
        flag = -1
    if flag >0:
        break
    else :
        print('게임 횟수는 양의 정수로 입력해주세요.')

while flag > 0 :
    playerRcp = input('가위 바위 보!:')  # step1: 내가 가위, 바위, 보 중에 하나를 낸다
    cpuRcp = random.randint(0, 2)  # step2: 컴퓨터가 가위, 바위, 보 중에 하나를 낸다

    # 입력된 내용이 '가위', '바위', '보', '0', '1', '2' 가 아니면, 오류 메시지 출력 후 다시 입력받기
    # step3: 가위, 바위,보가 제대로 내졌는지(입력이 제대로 들어갔는지 확인한다)
    rcpList = ['가위', '바위', '보', '0', '1', '2']


    if playerRcp in rcpList:  # 적절한 값이 입력되었을 경우, 입력값을 적절히 변환하고 player와 cpu가 무엇을 냈는지 알려줌.
        playerRcp = converter(playerRcp)
        cpuRcp = converter(cpuRcp)
        print('Round:', round)
        print('Y O U:', playerRcp)
        print('C P U:', cpuRcp)


        if playerRcp == cpuRcp:  # 무승부 먼저 처리하기
            print('무승부')
            drawCnt += 1
        else:  # 무승부가 아니면 승자 정해주기
            print(winner(playerRcp, cpuRcp), '이겼음')
        flag -= 1
        round += 1
        print('')

    else:
        print('가위,바위,보,0,1,2 중에서 입력해주세요')

print('당신의 전적:',winCnt,'승',drawCnt,'무',loseCnt,'패')
print('컴퓨터의 전적:',loseCnt,'승',drawCnt,'무',winCnt,'패')

# Q3. 2개의 숫자를 입력하여 그 사이에 짝수만 출력하는 함수를 만들어 봅시다. 그리고 중앙값도 함께 출력 해봅시다.(중앙값이 홀수라면 제외)
# 중앙값: 정중앙에 있는 값
# 특정 두 숫자 사이의 수들을 리스트로 만드는 법
# n = 1
# m = 10
# numbers = [ i for i in range(n,m+1)] # [1,2,3,4,5,6,7,8,9,10]
# # range(시작 숫자, 끝 숫자 + 1)
# 🔽 출력 예시
# # 입력
# n = int(input("첫 번째 수 입력 : "))
# m = int(input("두 번째 수 입력 : "))
# find_even_number(n, m)
# # 출력
# 첫 번째 수 입력 : 1
# 두 번째 수 입력 : 11
# 2 짝수
# 4 짝수
# 6 짝수
# 6 중앙값
# 8 짝수
# 10 짝수

def evenPrinter (firstNum,secondNum):
    numList = [i for i in range(firstNum,secondNum+1)]

    for i in numList:
        if i == (firstNum + secondNum)/2 and i % 2 ==0 :
            print(i, '중앙값')
        elif i %2 ==0:
            print(i,'짝수')
flag = 1
while flag:
    firstNum = input('첫 번째 수 입력:')
    secondNum = input('두 번째 수 입력:')

    try :
        firstNum = int(firstNum)
        secondNum = int(secondNum)
    except:
        firstNum = -1
        secondNum = -1

    if secondNum-firstNum > 0:
        print('첫번째 입력값:',firstNum)
        print('두번째 입력값:',secondNum)
        evenPrinter(firstNum,secondNum)
        flag = 0

    else :
        print('0이상의 정수를 입력해주세요(첫번째 입력값은 두번째 입력값보다 작아야 합니다)')



#
# 📌Q4. 2개의 숫자를 입력하여 그 사이에 소수가 몇 개인지 출력하는 함수를 만들어 봅시다.
#
# 소수: 1과 자기 자신만을 약수로 가지는 수
#
# 🔽 출력 예시
#
# # 입력
# n = int(input("첫 번째 수 입력 : "))
# m = int(input("두 번째 수 입력 : "))
# count_prime_number(n, m)
#
# # 출력
# 소수개수  4
import numpy as np

def primeNumCounter (firstNum,secondNum):
    intList=[False,False] + [True]*(secondNum-1)
    primeNum =[]
    primeNumAfter=[]

    for i in range(2,secondNum+1):
        if intList[i]:
            primeNum.append(i)
            for j in range(2*i, secondNum+1,i):
                intList[j] = False
    for k in primeNum:
        if k >= firstNum:
            primeNumAfter.append(k)

    print()
    print('소수목록:',primeNumAfter)
    print('소수갯수:',len(primeNumAfter))

flag = 1
while flag:
    firstNum = input('첫 번째 수 입력:')
    secondNum = input('두 번째 수 입력:')

    try :
        firstNum = int(firstNum)
        secondNum = int(secondNum)
    except:
        firstNum = -1
        secondNum = -1

    if secondNum-firstNum > 0:
        print('첫번째 입력값:',firstNum)
        print('두번째 입력값:',secondNum)
        primeNumCounter(firstNum,secondNum)

        flag = 0

    else :
        print('0이상의 정수를 입력해주세요(첫번째 입력값은 두번째 입력값보다 작아야 합니다)')