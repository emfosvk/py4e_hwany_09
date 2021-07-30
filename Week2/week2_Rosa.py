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