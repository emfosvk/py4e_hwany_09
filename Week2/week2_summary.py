# πQ1. μ»΄ν¨ν°μ ν¨κ»νλ κ°μλ°μλ³΄ κ²μμ λ§λ€μ΄λ΄μλ€!
# 
# μ‘°κ±΄1 : ν¨μμ μΈμλ‘λ λμ κ°μλ°μλ³΄ μ νμ΄ λ€μ΄κ°
#     (0, 1 ,2 νΉμ "κ°μ", "λ°μ", "λ³΄" λ‘ μλ ₯ν  μ μμ΅λλ€. - μ΄ 6κ°μ§ λ°©λ²μΌλ‘ λ£μ μ μμ)		  
# μ‘°κ±΄2 : λκ° λ¬΄μμ λκ³ , λκ° μΉλ¦¬ νλμ§ μΆλ ₯μ΄ λμ΄μΌ ν¨
# hint: μ»΄ν¨ν°κ° κ°μλ°μλ³΄ νκ² λ§λλ λ²
#  μλμ μ½λλ₯Ό μΆκ°νλ©΄ λ©λλ€
# import random
#  0 ~ 2 μ«μλ₯Ό λλ€μΌλ‘ λ½μλ΄λ μ½λ
# computer = random.randint(0, 2)

import random

rpsList = ['κ°μ', 'λ°μ', 'λ³΄']
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
        elif userInputData == 'κ°μ' :
            userInputStr = '0'
        elif userInputData == 'λ°μ' :
            userInputStr = '1'
        elif userInputData == 'λ³΄'   :
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

# μλλ‘μ§μ μ μ , λλ€μΌλ‘ λ½μΈκ±Έ ν λλ‘ IFλ¬Έ μ°λ €κ³ νμΌλ, λλ¬΄ μ§μ λΆν΄μ§λκ² κ°μμ
# μλ¨μ μ μΈν λ°°μ΄λ‘ λ³κ²½
#def versusRpsResult(userRps, comRps) :
#    try :
#        if   userRps == comRps :
#            #λΉκΈΈκ²½μ°
#            return 'D'
#        elif (userRps == 0 and comRps == 1) or (userRps == 1 and comRps == 2) or (userRps == 2 and comRps == 0):
#            return 'W'
#        elif userInputData == 'λ³΄'   :
#            return 'L'
#        else :
#            return 'E'
#    except :
#        return 'E'
print('====================== [START] [Q1] κ°μλ°μλ³΄ ')
rpsRound = 1
rpsFinish = False
while rpsFinish == False :
    inputData = input('κ°μ(0) λ°μ(1) λ³΄(2) μ’λ£(done) > ' )
    userRps = convertInputToRps(inputData)
    if   userRps == -1 :
        print('μλͺ»λ κ°μ μλ ₯νμμ΅λλ€.')
        continue
    elif userRps == -2 :
        print('κ°μλ°μλ³΄λ₯Ό μ’λ£ν©λλ€. (done μλ ₯)')
        rpsFinish == True
        break
    elif userRps == -3 :
        print('κ°μλ°μλ³΄λ₯Ό Pass ν©λλ€. (λΉ κ° μλ ₯)')
        rpsFinish == True
        break

    comRps = random.randint(0, 2)
    result = rpsResultList[userRps][comRps]
    print(str(rpsRound), ' νμ°¨ κ²°κ³Ό >')
    if   result == 'W' :
        print('=====μΉ  λ¦¬=====')
    elif result == 'L' :
        print('=====ν¨  λ°°=====')
    elif result == 'D' :
        print('=====λ¬΄μΉλΆ=====')
    else :
        print('=====μ  λ¬=====')
    
    print('λΉ  μ  > ', rpsList[userRps])
    print('μ»΄ν¨ν° > ', rpsList[comRps])
    
    rpsRound += 1

print('====================== [E N D] [Q1] κ°μλ°μλ³΄ ')

 
# πQ2. μκΈμ μλ ₯νλ©΄ μ°λ΄μ κ³μ°ν΄μ£Όλ κ³μ°κΈ°λ₯Ό λ§λ€μ΄ λ΄μλ€. μΈμ  μ°λ΄κ³Ό μΈν μ°λ΄μ ν¨κ» μΆλ ₯νλλ‘ ν΄λ΄λλ€.
#    πμλμ μΈμ¨ νλ₯Ό ν λλ‘ λ§λ€μ΄μ£ΌμΈμ(λ¨, μ€μ  μΈμ¨κ³Ό λ€λ₯Ό μ μμ΅λλ€!)
#  1200 <=  6%
#  4600 <= 15%
#  8800 <= 35%
# 30000 <= 38%
# 50000 <= 40%
# 50000  > 42%
print('')
print('====================== [START] [Q2] μΈμ μΈν μ°λ΄ κ³μ°κΈ° (by μκΈ) ')

taxRange = [1200, 4600, 8800, 30000, 50000]
taxRate  = [   6,   15,   35,    38,    40,    42]
taxCalFinish = False

while taxCalFinish == False :
    salaryStr = input('νμ¬ λ°λ μκΈ(μΈμ )μ μλ ₯νμΈμ (λ§λ¨μ) > ')
    salary = 0
    if   salaryStr == '' : 
        print('μ°λ΄κ³μ°κΈ° ν¨μ€ (λΉ κ° μλ ₯)')
        taxCalFinish = True
        break
    elif salaryStr == 'done' :
        print('μ°λ΄κ³μ°κΈ° μ’λ£ (done μλ ₯)')
        taxCalFinish = True
        break
    try :
        salary = int(salaryStr)
        if salary < 0 : 
          print('μ«μλ μΈμ λ μμλ₯Ό μλ ₯ν΄μ£ΌμμΌν©λλ€. (0 μ΄κ³Ό)')
          continue
    except :
        print('μλͺ»λ κ°μ μλ ₯νμμ΅λλ€.')
        continue

    salYearIncTax = salary * 12
    taxLevel = 0;
    for maxSal in taxRange :
        if maxSal >= salYearIncTax :
            break
        taxLevel += 1
    realSalAmtRate = 1.00 - (taxRate[taxLevel] / 100)
    salYearExcTax = round(salYearIncTax * (realSalAmtRate), 2)

    print('μλ ₯ κΈμ¬ : ', str(salary), ' λ§μ')
    print('μΈμ  μ°λ΄ : ', str(salYearIncTax), ' λ§μ')
    print('μΈν μ°λ΄ : ', str(salYearExcTax), ' λ§μ')
    print('μ μ© μΈκΈ λ¨κ³ : ', str(taxLevel + 1), ' λ¨κ³')
    print('μ μ© μΈμ¨ : ', str(taxRate[taxLevel]), ' %')
    print('**********************************')

print('====================== [E N D] [Q2] μΈμ μΈν μ°λ΄ κ³μ°κΈ° (by μκΈ)  ') 

# πQ3. νμ μ΄λ¦κ³Ό μ μλ₯Ό μλ ₯νλ©΄ νμ μ μΆλ ₯νλ νμ  λ³νκΈ°λ₯Ό λ§λ€μ΄ λ΄μλ€.
# μ΄λ¦κ³Ό μ μ, νμ  λͺ¨λ μΆλ ₯νλλ‘ ν΄λ΄λλ€.
# 
#    πμλμ νμ νλ₯Ό ν λλ‘ λ§λ€μ΄μ£ΌμΈμ
# 100 ~ 95 : A+
#  94 ~ 90 : A
#  89 ~ 85 : B+
#  84 ~ 80 : B
#  79 ~ 75 : C+
#  74 ~ 70 : C
#  69 ~ 65 : D+
#  64 ~ 60 : D
#  60μ  λ―Έλ§: F 
print('')
print('====================== [START] [Q3] νμ  κ³μ°κΈ° ')

scoreLevelList= ['A+', 'A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F']
maxScore = 100
minScore = 0
scoreRange = 5
failScore = 60
newStuBool = True
scoreCalFinish = False

while scoreCalFinish == False :
    if newStuBool :
        stuName = input('νμμ μ΄λ¦μ μλ ₯ν΄μ£ΌμΈμ > ')
        newStuBool = False
    
    ouputMsg = stuName + ' νμμ΄ λ°μ μ μλ₯Ό μλ ₯ν΄μ£ΌμΈμ > '
    scoreStr = input(ouputMsg)
    scoreNum = 0
    if   scoreStr == '' : 
        print('νμ κ³μ°κΈ° ν¨μ€ (λΉ κ° μλ ₯)')
        scoreCalFinish = True
        break
    elif scoreStr == 'done' :
        print('νμ κ³μ°κΈ° μ’λ£ (done μλ ₯)')
        scoreCalFinish = True
        break
    try :
        scoreNum = int(scoreStr)
    except :
        print('μλͺ»λ κ°μ μλ ₯νμμ΅λλ€.')
        continue
    
    # 0 ~ 100 μ«μμΈμ§ μ²΄ν¬.
    if scoreNum > maxScore or scoreNum < minScore :
       print('μ μλ ', maxScore, 'κ³Ό ', minScore, ' μ¬μ΄μ μ«μλ₯Ό μλ ₯ν΄μ£ΌμΈμ.')
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
    print('μ΄λ¦ : ', stuName)
    print('μ μ : ', scoreStr)
    print('νμ  : ', scoreRank)
    print('**********************************')

    #κ³μ° λ€ νμΌλ―λ‘, λ€μ νμ μ΄λ¦ μλ ₯ λ°κΈ°μν Boolean κ°  λ³κ²½
    newStuBool = True


print('====================== [E N D] [Q3] νμ  κ³μ°κΈ° ') 
 

# πQ4. λμ΄μ νκΈ λλ μΉ΄λλ₯Ό μλ ₯νλ©΄ λ²μ€ μκΈμ΄ μΆλ ₯λλ λ²μ€ μκΈ κ³μ°κΈ°λ₯Ό λ§λ€μ΄λ΄μλ€. 
#  πμλμ μκΈνλ₯Ό ν λλ‘ λ§λ€μ΄μ£ΌμΈμ

#  8μΈ λ―Έλ§            : λ¬΄λ£
#  8μΈ μ΄μ ~ 14μΈ λ―Έλ§ : μΉ΄λ :  450μ / νκΈ :  450μ
# 14μΈ μ΄μ ~ 20μΈ λ―Έλ§ : μΉ΄λ :  720μ / νκΈ : 1000μ
# 20μΈ μ΄μ            : μΉ΄λ : 1200μ / νκΈ : 1300μ
# 75μΈ μ΄μ            : λ¬΄λ£

print(' ')
print('====================== [START] [Q4] λ²μ€ μκΈ κ³μ°κΈ°')

payTypeList = ['μΉ΄λ', 'νκΈ']
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
        #λ²μ€ μΉμ°¨μμ λμ΄ κ²°μ  
        ageStr = input("μΉμ°¨ κ³ κ°μ μ°λ Ήμ μλ ₯ν΄μ£ΌμΈμ >")
        ageNum = 0
    
        if   ageStr == '' : 
            print('λ²μ€μκΈ κ³μ°κΈ° ν¨μ€ (λΉ κ° μλ ₯)')
            payCalFinish = True
            break
        elif ageStr == 'done' :
            print('λ²μ€μκΈ κ³μ°κΈ° μ’λ£ (done μλ ₯)')
            payCalFinish = True
            break
        try :
            ageNum = int(ageStr)
            if ageNum < 0  or ageNum > 200 :
                print('λμ΄λ 0 ~ 200 κΉμ§λ§ μλ ₯ κ°λ₯ν©λλ€.')
                continue
        except :
            print('μλͺ»λ κ°μ μλ ₯νμμ΅λλ€.')
            continue
    
    inputAgeFinish = True

    #λ²μ€ μκΈ νμ κ²°μ  (μΉ΄λ/νκΈ)
    payTypeStr = input("μ§λΆμλ¨μ μλ ₯ν΄μ£ΌμΈμ μΉ΄λ(0)/νκΈ(1) >")
    payTypeNum = 0
  
    if   payTypeStr == '' : 
        print('λ²μ€μκΈ κ³μ°κΈ° ν¨μ€ (λΉ κ° μλ ₯)')
        payCalFinish = True
        break
    elif payTypeStr == 'done' :
        print('λ²μ€μκΈ κ³μ°κΈ° μ’λ£ (done μλ ₯)')
        payCalFinish = True
        break
    
    if    payTypeStr == 'μΉ΄λ' or payTypeStr == '0' :
        payTypeNum = 0
    elif  payTypeStr == 'νκΈ' or payTypeStr == '1' : 
        payTypeNum = 1
    else :
        print('μλͺ»λ κ°μ μλ ₯νμμ΅λλ€.')
        continue

    outPutAmtMsg = ''

    if ageNum < minAge or ageNum >= maxAge :
        outPutAmtMsg = 'λ¬΄λ£'   
    else : 
        level = 0
        for AgeLevel in AgeLevelList : 
            if ageNum < AgeLevel :
                if payTypeNum == 0 :
                    outPutAmtMsg = str(cardAmtList[level]) + ' μ'
                else :
                    outPutAmtMsg = str(cashAmtList[level]) + ' μ'
            level += 1
    
    print('**********************************')
    print('μ°    λ Ή : ', ageStr)
    print('μκΈνμ : ', payTypeList[payTypeNum])
    print('λ²μ€μκΈ : ', outPutAmtMsg)
    print('**********************************')

    inputAgeFinish = False

print('====================== [E N D] [Q4] λ²μ€ μκΈ κ³μ°κΈ°') 

print('second version')
print('')
print('')

# Q1. μ»΄ν¨ν°μ ν¨κ»νλ κ°μλ°μλ³΄ κ²μμ λ§λ€μ΄λ΄μλ€!
#
# μ‘°κ±΄1 : ν¨μμ μΈμλ‘λ λμ κ°μλ°μλ³΄ μ νμ΄ λ€μ΄κ°
#           (0, 1 ,2 νΉμ "κ°μ", "λ°μ", "λ³΄" λ‘ μλ ₯ν  μ μμ΅λλ€. - μ΄ 6κ°μ§ λ°©λ²μΌλ‘ λ£μ μ μμ)
#
# μ‘°κ±΄2 : λκ° λ¬΄μμ λκ³ , λκ° μΉλ¦¬ νλμ§ μΆλ ₯μ΄ λμ΄μΌ ν¨


# step4: μΉν¨λ₯Ό νμΈνλ€
# step5: λκ° μ΄κ²Όλμ§, λκ° λ¬΄μμ λλμ§ μΆλ ₯νλ€.


import random


# μλ ₯λ 0,1,2λ₯Ό κ°μ,λ°μ,λ³΄λ‘ λ³ννκΈ°
def converter(a):
    a = str(a)
    if a == '0':
        return 'κ°μ'
    elif a == '1':
        return 'λ°μ'
    elif a == '2':
        return 'λ³΄'
    else:
        return a


def winner(player, cpu):  # μΉν¨κ° λλ κ²½μ°μ μλ 6κ°μ§,
    battle = player + cpu
    if battle == 'κ°μλ°μ':
        return 'μ»΄ν¨ν°κ°'
    elif battle == 'κ°μλ³΄':
        return 'λΉμ μ΄'
    elif battle == 'λ°μλ³΄':
        return 'μ»΄ν¨ν°κ°'
    elif battle == 'λ°μκ°μ':
        return 'λΉμ μ΄'
    elif battle == 'λ³΄κ°μ':
        return 'μ»΄ν¨ν°κ°'
    elif battle == 'λ³΄λ°μ':
        return 'λΉμ μ΄'
    else:
        return 'λ§λ μλλ μΌμ΄ μΌμ΄λ¨'


print('###########Q1##########')
# playerμ cpuμ κ°μ,λ°μ,λ³΄ μλ ₯λ°κΈ°
while True:
    playerRcp = input('κ°μ λ°μ λ³΄!:')  # step1: λ΄κ° κ°μ, λ°μ, λ³΄ μ€μ νλλ₯Ό λΈλ€
    cpuRcp = random.randint(0, 2)  # step2: μ»΄ν¨ν°κ° κ°μ, λ°μ, λ³΄ μ€μ νλλ₯Ό λΈλ€

    # μλ ₯λ λ΄μ©μ΄ 'κ°μ', 'λ°μ', 'λ³΄', '0', '1', '2' κ° μλλ©΄, μ€λ₯ λ©μμ§ μΆλ ₯ ν λ€μ μλ ₯λ°κΈ°
    # step3: κ°μ, λ°μ,λ³΄κ° μ λλ‘ λ΄μ‘λμ§(μλ ₯μ΄ μ λλ‘ λ€μ΄κ°λμ§ νμΈνλ€)
    rcpList = ['κ°μ', 'λ°μ', 'λ³΄', '0', '1', '2']
    flag = 1

    if playerRcp in rcpList:  # μ μ ν κ°μ΄ μλ ₯λμμ κ²½μ°, μλ ₯κ°μ μ μ ν λ³ννκ³  playerμ cpuκ° λ¬΄μμ λλμ§ μλ €μ€.
        playerRcp = converter(playerRcp)
        cpuRcp = converter(cpuRcp)
        print('Y O U:', playerRcp)
        print('C P U:', cpuRcp)

        if playerRcp == cpuRcp:  # λ¬΄μΉλΆ λ¨Όμ  μ²λ¦¬νκΈ°
            print('λ¬΄μΉλΆ')
        else:  # λ¬΄μΉλΆκ° μλλ©΄ μΉμ μ ν΄μ£ΌκΈ°
            print(winner(playerRcp, cpuRcp), 'μ΄κ²Όμ')
            break
    else:
        print('invalid value input')

# Q2. μκΈμ μλ ₯νλ©΄ μ°λ΄μ κ³μ°ν΄μ£Όλ κ³μ°κΈ°λ₯Ό λ§λ€μ΄ λ΄μλ€. μΈμ  μ°λ΄κ³Ό μΈν μ°λ΄μ ν¨κ» μΆλ ₯νλλ‘ ν΄λ΄λλ€.
# 1200λ§μ μ΄ν 6%, 4600λ§μ μ΄ν 15%, 8800λ§μ μ΄ν 24%, 1μ΅ 5μ²λ§μ μ΄ν 35%, 3μ΅μ μ΄ν 38%, 5μ΅μ μ΄ν 40%, 5μ΅μ μ΄κ° 42%
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
    salary = input('μκΈ(λ§μ):')
    try:
        salary = float(salary)
    except:
        salary = -1

    if salary > 0:

        annualIncome = 12 * salary
        incomeAfterTax = round((1 - taxChecker(annualIncome)) * annualIncome,2)


        print('μΈμ :', annualIncome, 'λ§μ')
        print('ν¬κ΄μ  μ μ©μ μΈν:',incomeAfterTax, 'λ§μ')
        print('λμ§μ  μ μ©μ μΈν:',round((incomeAfterTax+progressiveDeduction(annualIncome)),2),'λ§μ')
        print('μΈμ¨:', int(taxChecker(annualIncome) * 100), '%')
        flag = 0
    else:
        print('invalid input value')
# Q3. νμ μ΄λ¦κ³Ό μ μλ₯Ό μλ ₯νλ©΄ νμ μ μΆλ ₯νλ νμ  λ³νκΈ°λ₯Ό λ§λ€μ΄ λ΄μλ€.
#
# μ΄λ¦κ³Ό μ μ, νμ  λͺ¨λ μΆλ ₯νλλ‘ ν΄λ΄λλ€.

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

    nameScore = input('μ΄λ¦κ³Ό μ μλ₯Ό μλ ₯νμΈμ:').split()

    name = nameScore[0]

    try:
        score = int(nameScore[1])
    except:
        score = -1

    if score > 0:

        print('νμμ΄λ¦:', name)
        print('μ μ:', score, 'μ ')
        print('νμ :', grader(score))
        break
    else:
        print('invalid value error')

# Q4. λμ΄μ νκΈ λλ μΉ΄λλ₯Ό μλ ₯νλ©΄ λ²μ€ μκΈμ΄ μΆλ ₯λλ λ²μ€ μκΈ κ³μ°κΈ°λ₯Ό λ§λ€μ΄λ΄μλ€.

print('###########Q4##########')


def feeChecker(age, method):
    if age < 8 or age >= 75:
        return 'λ¬΄λ£μλλ€.'
    elif age < 14:
        return '450'
    elif age < 20 and method == 'μΉ΄λ':
        return '720'
    elif age < 20 and method == 'νκΈ':
        return '1000'
    elif age < 75 and method == 'μΉ΄λ':
        return '1200'
    elif age < 75 and method == 'νκΈ':
        return '1300'


while 1:
    ageMethod = input('λμ΄μ μ§λΆ λ°©λ²μ μλ €μ£ΌμΈμ(νκΈ/μΉ΄λ)').split()  # μλ ₯κ°μ΄ 3κ°μ΄λ©΄?
    try:
        age = int(ageMethod[0])
        method = str(ageMethod[1])
    except:
        age = -1
        method = -1

    if age > 0 and method in ['μΉ΄λ', 'νκΈ']:
        print('λμ΄:', age, 'μΈ')
        print('μ§λΆμ ν:', method)
        print('λ²μ€μκΈ:', feeChecker(age, method))

        break
    else:
        print('invalid value error')