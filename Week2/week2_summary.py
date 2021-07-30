# 📌Q1. 컴퓨터와 함께하는 가위바위보 게임을 만들어봅시다!
# 
# 조건1 : 함수의 인자로는 나의 가위바위보 선택이 들어감
#     (0, 1 ,2 혹은 "가위", "바위", "보" 로 입력할 수 있습니다. - 총 6가지 방법으로 넣을 수 있음)		  
# 조건2 : 누가 무엇을 냈고, 누가 승리 했는지 출력이 되어야 함
# hint: 컴퓨터가 가위바위보 하게 만드는 법
#  아래의 코드를 추가하면 됩니다
# import random
#  0 ~ 2 숫자를 랜덤으로 뽑아내는 코드
# computer = random.randint(0, 2)

import random

rpsList = ['가위', '바위', '보']
rpsResultList = [
  ['D','L','W'],
  ['W','D','L'],
  ['L','W','D']
]

def convertInputToRps(userInputData) :
    try :
        userInputStr = ''
        if   userInputData == 'done' :
            userInputStr = '-2'
        elif userInputData == '' :
            userInputStr = '-3'
        elif userInputData == '가위' :
            userInputStr = '0'
        elif userInputData == '바위' :
            userInputStr = '1'
        elif userInputData == '보'   :
            userInputStr = '2'
        else :
            userInputStr = userInputData
        userRps = int(userInputStr)
        if (userRps < 0 or userRps > 2) and (userInputData != 'done' and userInputData != '') :
            return -1
        else :  
            return userRps
    except :
        return -1

# 아래로직은 유저, 랜덤으로 뽑인걸 토대로 IF문 쓰려고했으나, 너무 지저분해지는것 같아서
# 상단에 선언한 배열로 변경
#def versusRpsResult(userRps, comRps) :
#    try :
#        if   userRps == comRps :
#            #비길경우
#            return 'D'
#        elif (userRps == 0 and comRps == 1) or (userRps == 1 and comRps == 2) or (userRps == 2 and comRps == 0):
#            return 'W'
#        elif userInputData == '보'   :
#            return 'L'
#        else :
#            return 'E'
#    except :
#        return 'E'
print('====================== [START] [Q1] 가위바위보 ')
rpsRound = 1
rpsFinish = False
while rpsFinish == False :
    inputData = input('가위(0) 바위(1) 보(2) 종료(done) > ' )
    userRps = convertInputToRps(inputData)
    if   userRps == -1 :
        print('잘못된 값을 입력하였습니다.')
        continue
    elif userRps == -2 :
        print('가위바위보를 종료합니다. (done 입력)')
        rpsFinish == True
        break
    elif userRps == -3 :
        print('가위바위보를 Pass 합니다. (빈 값 입력)')
        rpsFinish == True
        break

    comRps = random.randint(0, 2)
    result = rpsResultList[userRps][comRps]
    print(str(rpsRound), ' 회차 결과 >')
    if   result == 'W' :
        print('=====승  리=====')
    elif result == 'L' :
        print('=====패  배=====')
    elif result == 'D' :
        print('=====무승부=====')
    else :
        print('=====에  러=====')
    
    print('당  신 > ', rpsList[userRps])
    print('컴퓨터 > ', rpsList[comRps])
    
    rpsRound += 1

print('====================== [E N D] [Q1] 가위바위보 ')

 
# 📌Q2. 월급을 입력하면 연봉을 계산해주는 계산기를 만들어 봅시다. 세전 연봉과 세후 연봉을 함께 출력하도록 해봅니다.
#    📑아래의 세율 표를 토대로 만들어주세요(단, 실제 세율과 다를 수 있습니다!)
#  1200 <=  6%
#  4600 <= 15%
#  8800 <= 35%
# 30000 <= 38%
# 50000 <= 40%
# 50000  > 42%
print('')
print('====================== [START] [Q2] 세전세후 연봉 계산기 (by 월급) ')

taxRange = [1200, 4600, 8800, 30000, 50000]
taxRate  = [   6,   15,   35,    38,    40,    42]
taxCalFinish = False

while taxCalFinish == False :
    salaryStr = input('현재 받는 월급(세전)을 입력하세요 (만단위) > ')
    salary = 0
    if   salaryStr == '' : 
        print('연봉계산기 패스 (빈 값 입력)')
        taxCalFinish = True
        break
    elif salaryStr == 'done' :
        print('연봉계산기 종료 (done 입력)')
        taxCalFinish = True
        break
    try :
        salary = int(salaryStr)
        if salary < 0 : 
          print('숫자는 언제나 양수를 입력해주셔야합니다. (0 초과)')
          continue
    except :
        print('잘못된 값을 입력하였습니다.')
        continue

    salYearIncTax = salary * 12
    taxLevel = 0;
    for maxSal in taxRange :
        if maxSal >= salYearIncTax :
            break
        taxLevel += 1
    realSalAmtRate = 1.00 - (taxRate[taxLevel] / 100)
    salYearExcTax = round(salYearIncTax * (realSalAmtRate), 2)

    print('입력 급여 : ', str(salary), ' 만원')
    print('세전 연봉 : ', str(salYearIncTax), ' 만원')
    print('세후 연봉 : ', str(salYearExcTax), ' 만원')
    print('적용 세금 단계 : ', str(taxLevel + 1), ' 단계')
    print('적용 세율 : ', str(taxRate[taxLevel]), ' %')
    print('**********************************')

print('====================== [E N D] [Q2] 세전세후 연봉 계산기 (by 월급)  ') 

# 📌Q3. 학생 이름과 점수를 입력하면 학점을 출력하는 학점 변환기를 만들어 봅시다.
# 이름과 점수, 학점 모두 출력하도록 해봅니다.
# 
#    📑아래의 학점표를 토대로 만들어주세요
# 100 ~ 95 : A+
#  94 ~ 90 : A
#  89 ~ 85 : B+
#  84 ~ 80 : B
#  79 ~ 75 : C+
#  74 ~ 70 : C
#  69 ~ 65 : D+
#  64 ~ 60 : D
#  60점 미만: F 
print('')
print('====================== [START] [Q3] 학점 계산기 ')

scoreLevelList= ['A+', 'A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F']
maxScore = 100
minScore = 0
scoreRange = 5
failScore = 60
newStuBool = True
scoreCalFinish = False

while scoreCalFinish == False :
    if newStuBool :
        stuName = input('학생의 이름을 입력해주세요 > ')
        newStuBool = False
    
    ouputMsg = stuName + ' 학생이 받은 점수를 입력해주세요 > '
    scoreStr = input(ouputMsg)
    scoreNum = 0
    if   scoreStr == '' : 
        print('학점계산기 패스 (빈 값 입력)')
        scoreCalFinish = True
        break
    elif scoreStr == 'done' :
        print('학점계산기 종료 (done 입력)')
        scoreCalFinish = True
        break
    try :
        scoreNum = int(scoreStr)
    except :
        print('잘못된 값을 입력하였습니다.')
        continue
    
    # 0 ~ 100 숫자인지 체크.
    if scoreNum > maxScore or scoreNum < minScore :
       print('점수는 ', maxScore, '과 ', minScore, ' 사이의 숫자를 입력해주세요.')
       continue 
    
    scoreRank = 'F'
    
    nowRankMinScore = maxScore
    step = 1
    for scoreLevel in scoreLevelList : 
        if scoreNum >= (nowRankMinScore - scoreRange * step) :
            scoreRank = scoreLevel
            break
        step += 1
    
    print('**********************************')
    print('이름 : ', stuName)
    print('점수 : ', scoreStr)
    print('학점 : ', scoreRank)
    print('**********************************')

    #계산 다 했으므로, 다시 학생 이름 입력 받기위한 Boolean 값  변경
    newStuBool = True


print('====================== [E N D] [Q3] 학점 계산기 ') 
 

# 📌Q4. 나이와 현금 또는 카드를 입력하면 버스 요금이 출력되는 버스 요금 계산기를 만들어봅시다. 
#  📑아래의 요금표를 토대로 만들어주세요

#  8세 미만            : 무료
#  8세 이상 ~ 14세 미만 : 카드 :  450원 / 현금 :  450원
# 14세 이상 ~ 20세 미만 : 카드 :  720원 / 현금 : 1000원
# 20세 이상            : 카드 : 1200원 / 현금 : 1300원
# 75세 이상            : 무료

print(' ')
print('====================== [START] [Q4] 버스 요금 계산기')

payTypeList = ['카드', '현금']
minAge = 8
maxAge = 75
outRangeCashAmt  = 0
outRangeCardAmt  = 0
AgeLevelList = [ 14,   20,   75]
cardAmtList  = [450,  720, 1200]
cashAmtList  = [450, 1000, 1300]

payCalFinish = False
inputAgeFinish = False

while payCalFinish == False :
    
    if inputAgeFinish == False :
        #버스 승차자의 나이 결정 
        ageStr = input("승차 고객의 연령을 입력해주세요 >")
        ageNum = 0
    
        if   ageStr == '' : 
            print('버스요금 계산기 패스 (빈 값 입력)')
            payCalFinish = True
            break
        elif ageStr == 'done' :
            print('버스요금 계산기 종료 (done 입력)')
            payCalFinish = True
            break
        try :
            ageNum = int(ageStr)
            if ageNum < 0  or ageNum > 200 :
                print('나이는 0 ~ 200 까지만 입력 가능합니다.')
                continue
        except :
            print('잘못된 값을 입력하였습니다.')
            continue
    
    inputAgeFinish = True

    #버스 요금 타입 결정 (카드/현금)
    payTypeStr = input("지불수단을 입력해주세요 카드(0)/현금(1) >")
    payTypeNum = 0
  
    if   payTypeStr == '' : 
        print('버스요금 계산기 패스 (빈 값 입력)')
        payCalFinish = True
        break
    elif payTypeStr == 'done' :
        print('버스요금 계산기 종료 (done 입력)')
        payCalFinish = True
        break
    
    if    payTypeStr == '카드' or payTypeStr == '0' :
        payTypeNum = 0
    elif  payTypeStr == '현금' or payTypeStr == '1' : 
        payTypeNum = 1
    else :
        print('잘못된 값을 입력하였습니다.')
        continue

    outPutAmtMsg = ''

    if ageNum < minAge or ageNum >= maxAge :
        outPutAmtMsg = '무료'   
    else : 
        level = 0
        for AgeLevel in AgeLevelList : 
            if ageNum < AgeLevel :
                if payTypeNum == 0 :
                    outPutAmtMsg = str(cardAmtList[level]) + ' 원'
                else :
                    outPutAmtMsg = str(cashAmtList[level]) + ' 원'
            level += 1
    
    print('**********************************')
    print('연    령 : ', ageStr)
    print('요금타입 : ', payTypeList[payTypeNum])
    print('버스요금 : ', outPutAmtMsg)
    print('**********************************')

    inputAgeFinish = False

print('====================== [E N D] [Q4] 버스 요금 계산기') 

print('second version')
print('')
print('')

# Q1. 컴퓨터와 함께하는 가위바위보 게임을 만들어봅시다!
#
# 조건1 : 함수의 인자로는 나의 가위바위보 선택이 들어감
#           (0, 1 ,2 혹은 "가위", "바위", "보" 로 입력할 수 있습니다. - 총 6가지 방법으로 넣을 수 있음)
#
# 조건2 : 누가 무엇을 냈고, 누가 승리 했는지 출력이 되어야 함


# step4: 승패를 확인한다
# step5: 누가 이겼는지, 누가 무엇을 냈는지 출력한다.


import random


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
    if battle == '가위바위':
        return '컴퓨터가'
    elif battle == '가위보':
        return '당신이'
    elif battle == '바위보':
        return '컴퓨터가'
    elif battle == '바위가위':
        return '당신이'
    elif battle == '보가위':
        return '컴퓨터가'
    elif battle == '보바위':
        return '당신이'
    else:
        return '말도 안되는 일이 일어남'


print('###########Q1##########')
# player와 cpu의 가위,바위,보 입력받기
while True:
    playerRcp = input('가위 바위 보!:')  # step1: 내가 가위, 바위, 보 중에 하나를 낸다
    cpuRcp = random.randint(0, 2)  # step2: 컴퓨터가 가위, 바위, 보 중에 하나를 낸다

    # 입력된 내용이 '가위', '바위', '보', '0', '1', '2' 가 아니면, 오류 메시지 출력 후 다시 입력받기
    # step3: 가위, 바위,보가 제대로 내졌는지(입력이 제대로 들어갔는지 확인한다)
    rcpList = ['가위', '바위', '보', '0', '1', '2']
    flag = 1

    if playerRcp in rcpList:  # 적절한 값이 입력되었을 경우, 입력값을 적절히 변환하고 player와 cpu가 무엇을 냈는지 알려줌.
        playerRcp = converter(playerRcp)
        cpuRcp = converter(cpuRcp)
        print('Y O U:', playerRcp)
        print('C P U:', cpuRcp)

        if playerRcp == cpuRcp:  # 무승부 먼저 처리하기
            print('무승부')
        else:  # 무승부가 아니면 승자 정해주기
            print(winner(playerRcp, cpuRcp), '이겼음')
            break
    else:
        print('invalid value input')

# Q2. 월급을 입력하면 연봉을 계산해주는 계산기를 만들어 봅시다. 세전 연봉과 세후 연봉을 함께 출력하도록 해봅니다.
# 1200만원 이하 6%, 4600만원 이하 15%, 8800만원 이하 24%, 1억 5천만원 이하 35%, 3억원 이하 38%, 5억원 이하 40%, 5억원 초가 42%
print('###########Q2##########')

taxBase=[1200,  4600,  8800,  15000,  30000,  50000]
taxRate=[0.06,  0.15,  0.24,   0.35,   0.38,    0.40,  0.42]

def taxChecker(annualIncome):
    if annualIncome <= taxBase[0]:
        return 0.06
    elif annualIncome <= taxBase[1]:
        return 0.15
    elif annualIncome <= taxBase[2]:
        return 0.24
    elif annualIncome <= taxBase[3]:
        return 0.35
    elif annualIncome <= taxBase[4]:
        return 0.38
    elif annualIncome <= taxBase[5]:
        return 0.4
    else:
        return 0.42

def progressiveDeduction(annualIncome):
    progressiveDeduction = 0

    if annualIncome <= taxBase[0]:
        x=0
    elif annualIncome <= taxBase[1]:
        x=1
    elif annualIncome <= taxBase[2]:
        x=2
    elif annualIncome <= taxBase[3]:
        x=3
    elif annualIncome <= taxBase[4]:
        x=4
    elif annualIncome <= taxBase[5]:
        x=5
    else:
        x=6

    for i in range(0,x):
        progressiveDeduction = progressiveDeduction + taxBase[i]*(taxRate[i+1]-taxRate[i])

    return progressiveDeduction


flag = 1
while flag:
    salary = input('월급(만원):')
    try:
        salary = float(salary)
    except:
        salary = -1

    if salary > 0:

        annualIncome = 12 * salary
        incomeAfterTax = round((1 - taxChecker(annualIncome)) * annualIncome,2)


        print('세전:', annualIncome, '만원')
        print('포괄제 적용시 세후:',incomeAfterTax, '만원')
        print('누진제 적용시 세후:',round((incomeAfterTax+progressiveDeduction(annualIncome)),2),'만원')
        print('세율:', int(taxChecker(annualIncome) * 100), '%')
        flag = 0
    else:
        print('invalid input value')
# Q3. 학생 이름과 점수를 입력하면 학점을 출력하는 학점 변환기를 만들어 봅시다.
#
# 이름과 점수, 학점 모두 출력하도록 해봅니다.

print('###########Q3##########')


def grader(score):
    if score >= 95:
        return 'A+'
    elif score >= 90:
        return 'A'
    elif score >= 85:
        return 'B+'
    elif score >= 80:
        return 'B'
    elif score >= 75:
        return 'C+'
    elif score >= 70:
        return 'C'
    elif score >= 65:
        return 'D+'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


while True:

    nameScore = input('이름과 점수를 입력하세요:').split()

    name = nameScore[0]

    try:
        score = int(nameScore[1])
    except:
        score = -1

    if score > 0:

        print('학생이름:', name)
        print('점수:', score, '점')
        print('학점:', grader(score))
        break
    else:
        print('invalid value error')

# Q4. 나이와 현금 또는 카드를 입력하면 버스 요금이 출력되는 버스 요금 계산기를 만들어봅시다.

print('###########Q4##########')


def feeChecker(age, method):
    if age < 8 or age >= 75:
        return '무료입니다.'
    elif age < 14:
        return '450'
    elif age < 20 and method == '카드':
        return '720'
    elif age < 20 and method == '현금':
        return '1000'
    elif age < 75 and method == '카드':
        return '1200'
    elif age < 75 and method == '현금':
        return '1300'


while 1:
    ageMethod = input('나이와 지불 방법을 알려주세요(현금/카드)').split()  # 입력값이 3개이면?
    try:
        age = int(ageMethod[0])
        method = str(ageMethod[1])
    except:
        age = -1
        method = -1

    if age > 0 and method in ['카드', '현금']:
        print('나이:', age, '세')
        print('지불유형:', method)
        print('버스요금:', feeChecker(age, method))

        break
    else:
        print('invalid value error')