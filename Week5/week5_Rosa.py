#πQ1. μ¬λ¬λΆ νΉμ λ² μ€ν¨λΌλΉμ€31 κ²μμ μμλμ? 1λΆν° 31κΉμ§ μ«μλ₯Ό νλ μ΄μ΄λ€λΌλ¦¬ λ²κ°μ μΈμΉλ€κ° 31μ μΈμΉλ μ¬λμ΄ ν¨λ°°νλ κ²μμΈλ°μ.
#μ΄λ²μ μ΄ κ²μμ νμ΄μ¬ ν¨μλ‘ λ§λ€μ΄ λ΄μλ€. μ§μ±μ΄ μμ΄ μ«μλ₯Ό λλ€νκ² μΈμΉλ μ»΄ν¨ν°μ λκ²°μ ν΄λ³΄κ² μ΅λλ€.

#π²μ‘°κ±΄1 - λμ ν΄μμλ μ«μλ₯Ό μ§μ  μλ ₯νλ©° ν λ² μλ ₯ νμ space ν λ²μΌλ‘ κ΅¬λΆ
#Ex)
#my = input("My turn - μ«μλ₯Ό μλ ₯νμΈμ: ")
#1 2 3
#π²μ‘°κ±΄2 - λμ μ»΄ν¨ν° λͺ¨λ ν ν΄μ 1ν ~ 3νκΉμ§λ§ μ«μλ₯Ό μΈμΉ  μ μμ
#π²μ‘°κ±΄3 - μΈμ³μ§ μ«μλ³΄λ€ 1ν° μλ§ μΈμΉ μ μμ (ex: 5 λ€μμ λ¬΄μ‘°κ±΄ 6) μ μ‘°κ±΄μ΄ μλ§μ κ²½μ° λ€μ μλ ₯

#π§hint
# μ»΄ν¨ν°κ° 1~3ν μ€μμ λͺ λ²μ μλν  κ²μΈμ§ λλ€νκ² κ³ λ₯΄λ λ°©λ²
#import random 
#computer_turn_num = random.randint(1,3)
#
## μ²«λ²μ§Έλ₯Ό λνλ΄λ μΈλ±μ€ 0, λ§μ§λ§μ λνλ΄λ μΈλ±μ€ -1
#example = [1,2,3]
#print(example[0]) # 1
#print(example[-1] # 3 
#βμΆλ ₯ μμ
#bs31()
#
#λ² μ€ν¨λΌλΉμ€ μ¨λ¦¬μ κ²μ
#------------------
#My turn - μ«μλ₯Ό μλ ₯νμΈμ: 1 2 3
#νμ¬ μ«μ : 3
#μ»΄ν¨ν° : 4
#νμ¬ μ«μ : 4
#
#My turn - μ«μλ₯Ό μλ ₯νμΈμ: 5
#νμ¬ μ«μ : 5
#μ»΄ν¨ν° : 6
#μ»΄ν¨ν° : 7
#νμ¬ μ«μ : 7

print('====================== [START] [Q1] λ² μ€ν¨ λΌλΉμ€ 31 κ²μ ')

import random

#λ² μ€ν¨λΌλΉμ€31 κ²μ μ’λ£ μ«μ
endNum = 31
#ν ν΄μ λΆλ₯Όμ μλ μ΅λ μ«μ
maxCntTurnNums = 3

lastNum = 0

def bs31():
    
    while True :
        print('νμ¬ μλ ₯κ°λ₯ν μ΅μ μ«μλ', lastNum + 1, 'μλλ€.')
        userInputText = input('μ«μλ₯Ό μλ ₯νμΈμ >')
        userSelectList = convertToBs31(lastNum, userInputText)
        if userSelectList is None :
            #print('μ μ μλ ₯κ°μ λ³νν μ μμ΅λλ€. λ€μ μλ ₯ν΄μ£ΌμΈμ')
            continue
        
        #μ μ  μλ ₯κ°μΌλ‘ κ²μ μ’λ£μ¬λΆ νλ¨
        finishGameBool = printBs31(0, userSelectList)

        #μ μ κ° λ§μ§λ§ μ«μλ₯Ό λΆλ μ κ²½μ° ν¨λ°° μ²λ¦¬ν κ²μ μ’λ£
        if finishGameBool == True :
            break

        #μ μ  ν΄ μ’λ£ν μ»΄ν¨ν° ν΄ μμ
        comSelNumCnt = random.randint(1, maxCntTurnNums)
        comSelectList = []
        
        #μ»΄ν¨ν°κ° μ νν κ°μμ
        for i in range(comSelNumCnt) :

            #μ»΄ν¨ν°κ° λ§μ§λ§ μ«μλ₯Ό λΆλ¬μΌλ§ νλ κ²½μ°
            #μ μ κ° μ’λ£μ«μ -1 κΉμ§ λΆλ μ λ. 
            if i == 0 and endNum == (lastNum + i + 1) :
                comSelectList.append(lastNum + i + 1)
                break
            
            # μ»΄ν¨ν°κ° λ¬΄μ§μ±μΌλ‘ λ§μ§λ§ μ«μλ₯Ό λΆλ₯΄μ§ μκ² νκΈ° μν΄ μλ λ‘μ§ μΆκ°
            if endNum == (lastNum + i + 1) : 
                break
            
            comSelectList.append(lastNum + i + 1)
        
        #μ μ  μλ ₯κ°μΌλ‘ κ²μ μ’λ£μ¬λΆ νλ¨
        finishGameBool = printBs31(1, comSelectList)

        #μ μ κ° λ§μ§λ§ μ«μλ₯Ό λΆλ μ κ²½μ° ν¨λ°° μ²λ¦¬ν κ²μ μ’λ£
        if finishGameBool == True :
            break
        

                
                
#μ μ  μλ ₯κ°μ Listλ‘ λ³κ²½νλ ν¨μ.
#μλͺ»λ μλ ₯κ°μΌ κ²½μ°μλ None νμμΌλ‘ λ¦¬ν΄μ²λ¦¬.
def convertToBs31 (lastNum, userInputText) :
    try :
        userSelectStrList = userInputText.split()
        userSelectNumList = []
        
        #μλ ₯κ°μ κ°μ μ²΄ν¬
        if len(userSelectStrList) <= 0 :
            print('λ³νλμ€ μλ¬ λ°μ - μλ ₯λ κ°μ΄ μμ΅λλ€.')
            return None
        if len(userSelectStrList) > maxCntTurnNums :
            print('λ³νλμ€ μλ¬ λ°μ - μλ ₯κ°λ₯ν κ°―μλ₯Ό μ΄κ³Όνμ΅λλ€. μλ ₯κ°―μ :', len(userSelectStrList), 'κ°')
            return None

        #λ¬Έμμ΄ > μ«μ λ³ν μμ
        for inputValue in userSelectStrList :
            try :
                #μ«μ λ³ν νμ€νΈ
                userSelectNumList.append(int(inputValue))
            except :
                print('λ³νλμ€ μλ¬ λ°μ - μ«μκ° μλ λ¬Έμκ°μ΄ μλ ₯λμμ΅λλ€.')
                return None
        
        #λ³νλ μ«μ μ λ ¬
        #userSelectNumList.sort()
        
        #μ«μκ° μμλλ‘, κ·Έλ¦¬κ³  λ§μ§λ§ μ«μλ€μ λμ€λ μ«μμΈμ§ μ²΄ν¬
        for i in range(len(userSelectNumList)) :
            if userSelectNumList[i] != (lastNum + i + 1) :
                print('λ³νλμ€ μλ¬ λ°μ - μμλλ‘ μ«μλ₯Ό μλ ₯ν΄μ£ΌμΈμ.')
                return None
            if userSelectNumList[i] > endNum :
                print('λ³νλμ€ μλ¬ λ°μ - μ’λ£ μ«μλ³΄λ€ ν° μ«μλ₯Ό μλ ₯νμ΅λλ€. λ°κ²¬ μ«μ : ', userSelectNumList[i])
                return None

        return userSelectNumList

    except :
        print('λ³νλμ€ μλ¬ λ°μ')
        return None

#μλ While λ¬Έμμ μ¬μ©ν  μ²΄ν¬λ‘μ§μ Func
def printBs31 (userOrCom, selectBsNumList) :

    userOrComList = ['μ¬μ©μ', 'μ»΄ν¨ν°']
    #μλ lastNumλ³μλ₯Ό μ μ­λ³μλ‘ μ¬μ©νκΈ° μν λ¬Έλ² 
    #μ΄ ν¨μμ κ²½μ° ν¨μμμμ νΈμΆνκΈ°λλ¬Έμ, μ μ­λ³μλ‘ μ μΈνμ§ μμΌλ©΄ μλͺ»λ κ°μ λ€μ λ£μ΄λ²λ¦Ό.
    global lastNum

    #μ μ  μλ ₯κ°μ 31μ΄ μ‘΄μ¬νλμ§ νμΈ ν μ‘΄μ¬νμ§ μμ κ²½μ° λ€μ λ¨κ³λ‘ λμ΄κ°.
    for i in range(len(selectBsNumList)) :
        print(userOrComList[userOrCom], ':', selectBsNumList[i])
        lastNum = selectBsNumList[i]

        #λ§μ§λ§ μ«μλ₯Ό λΆλ λμ§ μ²΄ν¬
        if selectBsNumList[i] == endNum :
            print('=== ', userOrComList[userOrCom], 'ν¨λ°° ===')
            return True   
    #λ§μ§λ§ μ«μλ₯Ό λΆλ₯΄μ§ μμμΌλ©΄ ν΄ λκΉ.
    return False

#κ²μ μ€ν
#λλ²κΉμ μν΄ μμ λΉνμ±ν
bs31()

print('====================== [E N D] [Q1] λ² μ€ν¨ λΌλΉμ€ 31 κ²μ ')



#πQ2. λ€μκ³Ό κ°μ΄ νμλ€μ μν λ΅μ§κ° μμ΅λλ€. κ·Έλ¦¬κ³  λ΅μμ§λ μμ΅λλ€.
#ν¨μλ₯Ό νλ λ§λ€μ΄ μ±μ μ νκ³  νμλ€μ μ μλ₯Ό μΆλ ₯νκ³  λ±μλ ν¨κ» μΆλ ₯ν΄μ£ΌμΈμ.

## νμ λ΅
#s = ["κΉκ°,3242524215",
#"μ΄μ,3242524223",
#"λ°λ³,2242554131",
#"μ΅μ ,4245242315",
#"μ λ¬΄,3242524315"]

## μ λ΅μ§
#a = [3,2,4,2,5,2,4,3,1,2]

#π§hint
## λ¬Έμμ΄λ μ«μ μ λ ¬ κ°λ₯
#a = ["5","2","3"]
#a.sort()
#["2", "3", "5"]
## λ΄λ¦Όμ°¨μ μ λ ¬ κ°λ₯
#a.sort(reverse=True)
#["5", "3", "2"]
#βμΆλ ₯ μμ
#grader(s, a)
#νμ: μ λ¬΄ μ μ: 90μ  1λ±
#νμ: κΉκ° μ μ: 80μ  2λ±
#νμ: μ΄μ μ μ: 70μ  3λ±
#νμ: λ°λ³ μ μ: 50μ  4λ±
#νμ: μ΅μ  μ μ: 40μ  5λ±


print('====================== [START] [Q2] μ μ μ±μ κΈ° ')


def grader(exAnswers, rightAnswers, pointAnswers) :
    print()
    
    #νμλ³ Listλ‘ λΆλ¦¬ μ μ₯. 
    #μ΅μ΄ μ μλ 0μ μΌλ‘ λ±λ‘.
    stuScores = []
    stuNames = []
    stuAnswers = []
    for infos in exAnswers :
        tempInfo = infos.split(',')
        stuNames.append(tempInfo[0])
        stuAnswers.append(tempInfo[1])
        stuScores.append(0)
    
    #i = λ¬Έμ  λ²νΈ
    for i in range(len(rightAnswers)) :
        # jλ νμ λ²νΈ
        for j in range(len(stuNames)) : 
            #print(rightAnswers[i], stuAnswers[j][i:i+1], pointAnswers[i], stuScores[j], rightAnswers[i] == stuAnswers[j][i:i+1])
            if str(rightAnswers[i]) == stuAnswers[j][i:i+1] :
                stuScores[j] += pointAnswers[i]

    #print(stuNames)
    #print(stuAnswers)
    #print(stuScores)

    # sort ν¨μ μ¬μ©μ μν νλμ λ¦¬μ€νΈ (μ΄μ€λ°°μ΄)λ‘ μ¬ κ²°ν©
    resultList = []
    for i in range(len(stuNames)) :
        resultList.append([stuScores[i], stuNames[i], stuAnswers[i]])
    
    #sortν¨μμ κ²½μ° λ³λ€λ₯Έ λ΄μ©μ§μ μ΄ μμ κ²½μ° λ¦¬μ€νΈ μμ΄ν μμλλ‘ μ λ ¬μ μ§ν.
    resultList.sort(reverse=True)
    
    #μ¬ κ²°ν©ν λ¦¬μ€νΈ
    nowRank = 1
    prePoint = sum(stuScores)    
    #μ²«λ²μ§Έ μΈμμ λ¬΄μ‘°κ±΄ 1λ± - μ λ ¬μ ν μνμ΄λ―λ‘. 1λ±μΌλ‘ λ±λ‘
    resultList[0].append(nowRank);
    
    #μμμ μ²«λ²μ§Έλ νμΌλ―λ‘ λλ²μ§Έ λΆν° μμ. (= 1)
    nowStep = 1
    for nowStep in range(len(resultList)) :
        #μ  μ¬λκ³Ό λμΌ μ μκ° μλκ²½μ° νμ¬ λ¨κ³λ₯Ό κ·Έλλ‘ μ½μ.
        if prePoint != resultList[nowStep][0] :
            nowRank = nowStep + 1

        # μμμ μ μ₯ν λ±μ μ μ₯.
        resultList[nowStep].append(nowRank) 
        # λμ μ²΄ν¬λ₯Ό μν λ§μ§λ§ μμ μ μ μμμ μ₯.
        prePoint = resultList[nowStep][0]     
    
    #λ±μ λ°°μ  μλ£ν μΆλ ₯
    for result in resultList :
        print(result[3], 'λ± >', 'νμλͺ :',  result[1], '/ μ μ :', result[0])


exAnswers = ["κΉκ°,3242524215",
"μ΄μ,2242554131",
"λ°λ³,2242554131",
"μ΅μ ,4245242315",
"μ λ¬΄,3242524315"]

#λ¬Έμ λ²νΈ         1,  2   3,  4,  5,  6,  7,  8,  9, 10
rightAnswers = [ 3,  2,  4,  2,  5,  2,  4,  3,  1,  2]
pointAnswers = [10,  4, 16, 15,  5,  7, 13, 11,  9, 10]

grader(exAnswers, rightAnswers, pointAnswers)

print('====================== [E N D] [Q2] μ μ μ±μ κΈ° ')


#πQ3. μ«μ λ§μΆκΈ° κ²μμ λ§λ€μ΄ λ³Όκ²μ. μ»΄ν¨ν°κ° μμμ μ«μλ₯Ό 3κ° λ§λ€κ³  μ°λ¦¬κ° κ·Έκ²μ #λ§μΆ°λ³΄κ² μ΅λλ€.
#
#π²μ‘°κ±΄1 - μ«μλ 0 ~ 100κΉμ§ μ«μλ₯Ό 3κ° λ§λ­λλ€(μ€λ³΅ λΆκ°).
#π²μ‘°κ±΄2 - 5ν, 10νκΉμ§ μ λ΅μ λͺ»λ§μΆλ©΄ μ΅μκ°, μ΅λκ°μ λν ννΈλ₯Ό μ€λλ€.
#π²μ‘°κ±΄3 - μ λ΅μ λ§μΆλ©΄, λ§μΆ μ λ΅μ΄ μ΅μκ°μΈμ§, μ€κ°κ°μΈμ§, μ΅λκ°μΈμ§ μλ €μ€λλ€.
#import random
#number = random.randint(0, 100)
#βμΆλ ₯ μμ
#guess_numbers()
#
#1μ°¨ μλ
#μ«μλ₯Ό μμΈ‘ν΄λ³΄μΈμ : 39
#μ«μλ₯Ό λ§μΆμ¨μ΅λλ€! 39λ μ΅μκ°μλλ€.
#2μ°¨ μλ
#μ«μλ₯Ό μμΈ‘ν΄λ³΄μΈμ : 48
#μ«μλ₯Ό λ§μΆμ¨μ΅λλ€! 48λ μ΅λκ°μλλ€.
#3μ°¨ μλ
#μ«μλ₯Ό μμΈ‘ν΄λ³΄μΈμ : 100
#μ«μλ₯Ό λ§μΆμ¨μ΅λλ€! 100λ μ΅λκ°μλλ€.
#κ²μμ’λ£
#3λ² μλλ§μ μμΈ‘ μ±κ³΅
#
#...
#5μ°¨ μλ
#μ«μλ₯Ό μμΈ‘ν΄λ³΄μΈμ : 9
#9λ μμ΅λλ€
#μ΅μκ°μ 9λ³΄λ€ μμ΅λλ€
#6μ°¨ μλ
#μ«μλ₯Ό μμΈ‘ν΄λ³΄μΈμ : 9
#μ΄λ―Έ μμΈ‘μ μ¬μ©ν μ«μμλλ€
#6μ°¨ μλ

print('====================== [START] [Q3] μ«μ λ§μΆκΈ° κ²μ ')

#2λ² λ¬Έμ μμ μ΄λ―Έ import νμμ.
#import random

def guess_numbers () :
    print()
    
    minNum = 0
    maxNum = 100
    nums = []
    answerBools = []
    selNums = 3
    hintRound = [5, 10, 15, 20]
    gameRound = 1
    
    #μ«μ 3κ° λ½κΈ°
    while len(nums) < selNums : 
        #0 ~ 100 μ¬μ΄μ μ«μ λλ€ μΆμΆ
        num = random.randint(minNum, maxNum)
        #μ΄λ―Έ λ½μ μ«μμΈμ§ μ²΄ν¬ν΄μ, μλ κ²½μ° λ°°μ΄μ λ£μ.
        if num not in nums :
            nums.append(num)
            answerBools.append(False)
    
    #λ¦¬μ€νΈμμ μ«μ μ λ ¬
    nums.sort()
    
    #λλ²κΉμ μν΄μ μ»΄ν¨ν° μ νμ νκΈ°
    print('Q3 μ»΄ν¨ν°μ μ ν :', nums)


    #λͺ»λ§μΆ μ«μκ° μμΌλ©΄ λ¬΄ν λ°λ³΅
    while False in answerBools :
        nowStatusText = ''
        for i in range(len(answerBools)) :
            if answerBools[i] == True :
                nowStatusText += str(nums[i])
            else :
                nowStatusText += 'XX'

            if i < (len(answerBools) - 1) :
                nowStatusText += ', '

        print('========== νμ¬ λΌμ΄λ : [', gameRound, ']')
        print('========== νμ¬ μ  ν© : [', nowStatusText, ']')

        try :
            userSelNum = int(input('λ²νΈλ₯Ό μ ννμΈμ > '))        
        except :
            print('μλ ₯ν κ°μ μ«μλ‘ λ³ννλ κ³Όμ μμ μλ¬ λ°μ. λ€μ μλ ₯ν΄μ£ΌμΈμ')
            continue
        
        idx = -1
        try : 
            #.indexλ‘ ν΄λΉ μ«μκ° μ‘΄μ¬νλμ§ μ²΄ν¬.
            # μλ κ²½μ° ValueError μλ¬λ¦¬ν΄.
            idx = nums.index(userSelNum)
        except : 
            # μλ¬λ₯Ό μ¬μ©νμ¬ νλ‘μΈμ€ μ²λ¦¬
            idx = -1
        
        # μ¬κΈ°μ κ±Έλ¦΄λ¦¬λ μμ. index ν¨μλ κ°μ΄ μμΌλ©΄ μλ¬ λ¦¬ν΄νλ―λ‘, 0λ―Έλ§μ κ°μ΄ λμ¬μ μμ.
        if idx < 0 :
            print('[', userSelNum, ']μ μ λ΅μ΄ μλλλ€.')
            
            #5ν, 10νμ λͺ»λ§μΆ κ²½μ° ννΈ λ¦¬ν΄
            printHint(gameRound, hintRound, userSelNum, nums)
            #λΌμ΄λ 1 μ¦κ°ν μλ¬λ¦¬ν΄
            gameRound += 1
            continue
        
        if answerBools[idx] == True :
            print('[', userSelNum, ']μ μ΄λ―Έ λ§μΆ λ΅μλλ€. - νμ°¨λ₯Ό μ¦κ°μν€μ§ μμ΅λλ€.')
            continue
        
        #μ λ΅μ λ§μ·μΌλ―λ‘ μ§νμν λ³κ²½
        answerBools[idx] = True

        if userSelNum == nums[0]:
            print('[', userSelNum, '] : μ΅μ κ°')
        elif userSelNum == nums[-1]  :
            print('[', userSelNum, '] : μ΅λ κ°')
        else :
            print('[', userSelNum, '] : μ€κ° κ°')
        
        #μμ§ μ’λ£κ° μλμμ κ²½μ° λΌμ΄λ 1 λλ¦Ό.
        if False in answerBools :
            gameRound += 1
        
        continue
    
    #μ κ²μμ΄ λλκ³  κ²°κ³Ό μ λ¦¬.
    print('[', gameRound, ']ν λ§μ λ§μΆμ¨μ΅λλ€.')
    print('μ λ΅ ===> ', nums)
    
# ννΈ μ²λ¦¬
def printHint(gameRound, hintRound, userSelNum, nums) :
    #νμ¬ λΌμ΄λκ° ννΈκ° μ£Όμ΄μ§λ λΌμ΄λκ° μλλ©΄ ν¨μ€ μ²λ¦¬
    if gameRound not in hintRound :
        return
    
    # νμ¬ λΌμ΄λκ° ννΈκ° μ£Όμ΄μ§λ λΌμ΄λ μΌ κ²½μ° μλ λ‘μ§ νμΈν΄μ μ²΄ν¬
    # μ΅μκ°λ³΄λ€ μμ κ²½μ°
    if userSelNum < nums[0] :
        print('μλ ₯ν [', userSelNum, ']μ μ΅μ κ°λ³΄λ€ μμ΅λλ€.')

    # μ΅λκ°λ³΄λ€ ν°μ«μμΈ κ²½μ°
    if userSelNum > nums[-1] :
        print('μλ ₯ν [', userSelNum, ']μ μ΅λ κ°λ³΄λ€ ν½λλ€.')
        
    # ν΄λΉ κ°μ΄ μ΅λ, μ΅μκ° μ€κ°μΈ κ²½μ° μ€κ°κ° μ°ΎκΈ°
    if userSelNum > nums[0] and userSelNum < nums[-1] : 
        print('μλ ₯ν [', userSelNum, ']μ μ΅λ κ°κ³Ό μ΅μκ° μ¬μ΄μ μ‘΄μ¬νλ μ«μμλλ€.')
        
        if userSelNum > nums[1] : 
            print('μλ ₯ν [', userSelNum, ']μ μ€κ° κ°λ³΄λ€ ν° μ«μμλλ€.')
        if userSelNum < nums[1] : 
            print('μλ ₯ν [', userSelNum, ']μ μ€κ° κ°λ³΄λ€ μμ μ«μμλλ€.')





guess_numbers()

print('====================== [E N D] [Q3] μ«μ λ§μΆκΈ° κ²μ ')


#πQ4. μ€λ μ μΈμ΄ μκ²Όλ€κ³  ν΄λ΄μλ€. 100μΌμ κΈ°λνκ³  μΆμλ°μ.
#
#λ μ§λ₯Ό λ£μΌλ©΄ 100μΌ λ€κ° λͺμ λ©°μΉ μΈμ§ κ³μ°ν΄μ£Όλ ν¨μλ₯Ό λ§λ€μ΄ λ³΄κ² μ΅λλ€.
#
#π²μ‘°κ±΄1 - "μ€λλΆν° 1μΌ"μ΄κΈ° λλ¬Έμ λ μ§λ₯Ό κ³μ°ν  λ μ€λμ ν¬ν¨ν©λλ€
#π²μ‘°κ±΄2 - λͺλλμΈμ§ κ΅¬λΆνμ§ μκ³  μ€λλ κ³ λ €νμ§ μκ³  2μμ λ¬΄μ‘°κ±΄ 28μΌλ‘ ν©λλ€.
#π§hint
## νΉμ  μμμ μμΉλ₯Ό μ°Ύλ λ°©λ²
#a = [1,2,3,4]
#a.index(1)
#0
#βμΆλ ₯ μμ
#after_100(6,21,"μ")
#6μ 21μΌ μμμΌλΆν° 100μΌ λ€λ 9μ 28μΌ νμμΌ


print('====================== [START] [Q4] 100μΌ κ³μ°κΈ° ')

def after_100(inputMonth, inputDate, inputDay) :

    resultMonth = inputMonth
    #ν΄λΉ λ μ§λ ν¬ν¨μ ν΄μΌνλ―λ‘ dateμμ 1λΉΌκ³  μμ. [μ‘°κ±΄1]
    resultDate = inputDate - 1
    leftDate = plusDate
    resultYear = 'μ¬ν΄'
    
    # 100μΌ μ΄ν μ, μΌ κ³μ°
    while 1 : 
        #μμ¬μΌμ΄ νμ¬ μμ λ μ§λ³΄λ€ λ§μ κ²½μ° λ€μ λ¬λ‘ ν¨μ€.
        if resultDate + leftDate > monthDates[resultMonth - 1] :
            #μμ¬μΌμ κ³μ°
            leftDate = leftDate - (monthDates[resultMonth - 1] - resultDate)
            resultDate = 0
            resultMonth += 1 
            #λ§μ½ 12μμ΄ μ§λ¬λ€λ©΄ 1μλ‘ λ€μ μ²λ¦¬.
            if resultMonth > 12 :
                resultMonth = 1
                resultYear = 'λ΄λ'
        #μ μΌμ΄μ€κ° μλλ©΄ ν΄λΉ μμ΄ μ’λ£μΌμ΄λ―λ‘ λ£¨νμμ μμ.
        else :
            resultDate = leftDate
            break

    #μμΌ κ³μ°.
    dayOrderInput = daysStr.index(inputDay)
    # μ€λ ν¬ν¨ 100μΌ μ΄λ―λ‘ -1μΌ ν΄μ€μΌ 99μΌλ€μ μμΌμ΄ κ΅¬ν΄μ§.
    dayOrderResult = (plusDate + dayOrderInput - 1) % len(daysStr)

    print('100μΌ λ€μ λ μ§ : ', resultYear, resultMonth,  'μ', resultDate, 'μΌ (', daysStr[dayOrderResult], ')')


daysStr = ['μΌ', 'μ', 'ν', 'μ', 'λͺ©', 'κΈ', 'ν ']

#μκ° λ μ§
#              1   2   3   4   5   6   7   8   9  10  11  12
monthDates = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

plusDate = 100

inputMonth = int(input('κΈ°μ€ μ μλ ₯ > '))
inputDate = int(input('κΈ°μ€ μΌ μλ ₯ > '))
inputDay = input('κΈ°μ€ μμΌ μλ ₯ (μ,ν,μ,λͺ©,κΈ,ν ,μΌ) > ')

after_100(inputMonth, inputDate, inputDay)

print('====================== [E N D] [Q4] 100μΌ κ³μ°κΈ° ')
