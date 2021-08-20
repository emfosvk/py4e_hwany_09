#📌Q1. 여러분 혹시 베스킨라빈스31 게임을 아시나요? 1부터 31까지 숫자를 플레이어들끼리 번갈아 외치다가 31을 외치는 사람이 패배하는 게임인데요.
#이번엔 이 게임을 파이썬 함수로 만들어 봅시다. 지성이 없이 숫자를 랜덤하게 외치는 컴퓨터와 대결을 해보겠습니다.

#😲조건1 - 나의 턴에서는 숫자를 직접 입력하며 한 번 입력 후에 space 한 번으로 구분
#Ex)
#my = input("My turn - 숫자를 입력하세요: ")
#1 2 3
#😲조건2 - 나와 컴퓨터 모두 한 턴에 1회 ~ 3회까지만 숫자를 외칠 수 있음
#😲조건3 - 외쳐진 숫자보다 1큰 수만 외칠수 있음 (ex: 5 다음엔 무조건 6) 위 조건이 안맞을 경우 다시 입력

#🧐hint
# 컴퓨터가 1~3회 중에서 몇 번을 시도할 것인지 랜덤하게 고르는 방법
#import random 
#computer_turn_num = random.randint(1,3)
#
## 첫번째를 나타내는 인덱스 0, 마지막을 나타내는 인덱스 -1
#example = [1,2,3]
#print(example[0]) # 1
#print(example[-1] # 3 
#✅출력 예시
#bs31()
#
#베스킨라빈스 써리원 게임
#------------------
#My turn - 숫자를 입력하세요: 1 2 3
#현재 숫자 : 3
#컴퓨터 : 4
#현재 숫자 : 4
#
#My turn - 숫자를 입력하세요: 5
#현재 숫자 : 5
#컴퓨터 : 6
#컴퓨터 : 7
#현재 숫자 : 7

print('====================== [START] [Q1] 베스킨 라빈스 31 게임 ')

import random

#베스킨라빈스31 게임 종료 숫자
endNum = 31
#한 턴에 부를수 있는 최대 숫자
maxCntTurnNums = 3

lastNum = 0

def bs31():
    
    while True :
        print('현재 입력가능한 최소 숫자는', lastNum + 1, '입니다.')
        userInputText = input('숫자를 입력하세요 >')
        userSelectList = convertToBs31(lastNum, userInputText)
        if userSelectList is None :
            #print('유저입력값을 변환할수 없습니다. 다시 입력해주세요')
            continue
        
        #유저 입력값으로 게임 종료여부 판단
        finishGameBool = printBs31(0, userSelectList)

        #유저가 마지막 숫자를 불렀을 경우 패배 처리후 게임 종료
        if finishGameBool == True :
            break

        #유저 턴 종료후 컴퓨터 턴 시작
        comSelNumCnt = random.randint(1, maxCntTurnNums)
        comSelectList = []
        
        #컴퓨터가 선택한 개수에
        for i in range(comSelNumCnt) :

            #컴퓨터가 마지막 숫자를 불러야만 하는 경우
            #유저가 종료숫자 -1 까지 불렀을 때. 
            if i == 0 and endNum == (lastNum + i + 1) :
                comSelectList.append(lastNum + i + 1)
                break
            
            # 컴퓨터가 무지성으로 마지막 숫자를 부르지 않게 하기 위해 아래 로직 추가
            if endNum == (lastNum + i + 1) : 
                break
            
            comSelectList.append(lastNum + i + 1)
        
        #유저 입력값으로 게임 종료여부 판단
        finishGameBool = printBs31(1, comSelectList)

        #유저가 마지막 숫자를 불렀을 경우 패배 처리후 게임 종료
        if finishGameBool == True :
            break
        

                
                
#유저 입력값을 List로 변경하는 함수.
#잘못된 입력값일 경우에는 None 타입으로 리턴처리.
def convertToBs31 (lastNum, userInputText) :
    try :
        userSelectStrList = userInputText.split()
        userSelectNumList = []
        
        #입력값의 개수 체크
        if len(userSelectStrList) <= 0 :
            print('변환도중 에러 발생 - 입력된 값이 없습니다.')
            return None
        if len(userSelectStrList) > maxCntTurnNums :
            print('변환도중 에러 발생 - 입력가능한 갯수를 초과했습니다. 입력갯수 :', len(userSelectStrList), '개')
            return None

        #문자열 > 숫자 변환 작업
        for inputValue in userSelectStrList :
            try :
                #숫자 변환 테스트
                userSelectNumList.append(int(inputValue))
            except :
                print('변환도중 에러 발생 - 숫자가 아닌 문자값이 입력되었습니다.')
                return None
        
        #변환된 숫자 정렬
        #userSelectNumList.sort()
        
        #숫자가 순서대로, 그리고 마지막 숫자뒤에 나오는 숫자인지 체크
        for i in range(len(userSelectNumList)) :
            if userSelectNumList[i] != (lastNum + i + 1) :
                print('변환도중 에러 발생 - 순서대로 숫자를 입력해주세요.')
                return None
            if userSelectNumList[i] > endNum :
                print('변환도중 에러 발생 - 종료 숫자보다 큰 숫자를 입력했습니다. 발견 숫자 : ', userSelectNumList[i])
                return None

        return userSelectNumList

    except :
        print('변환도중 에러 발생')
        return None

#아래 While 문에서 사용할 체크로직을 Func
def printBs31 (userOrCom, selectBsNumList) :

    userOrComList = ['사용자', '컴퓨터']
    #아래 lastNum변수를 전역변수로 사용하기 위한 문법 
    #이 함수의 경우 함수안에서 호출하기때문에, 전역변수로 선언하지 않으면 잘못된 값을 다시 넣어버림.
    global lastNum

    #유저 입력값에 31이 존재하는지 확인 후 존재하지 않을 경우 다음 단계로 넘어감.
    for i in range(len(selectBsNumList)) :
        print(userOrComList[userOrCom], ':', selectBsNumList[i])
        lastNum = selectBsNumList[i]

        #마지막 숫자를 불렀는지 체크
        if selectBsNumList[i] == endNum :
            print('=== ', userOrComList[userOrCom], '패배 ===')
            return True   
    #마지막 숫자를 부르지 않았으면 턴 넘김.
    return False

#게임 실행
#디버깅을 위해 임시 비활성화
bs31()

print('====================== [E N D] [Q1] 베스킨 라빈스 31 게임 ')



#📌Q2. 다음과 같이 학생들의 시험 답지가 있습니다. 그리고 답안지도 있습니다.
#함수를 하나 만들어 채점을 하고 학생들의 점수를 출력하고 등수도 함께 출력해주세요.

## 학생 답
#s = ["김갑,3242524215",
#"이을,3242524223",
#"박병,2242554131",
#"최정,4245242315",
#"정무,3242524315"]

## 정답지
#a = [3,2,4,2,5,2,4,3,1,2]

#🧐hint
## 문자열도 숫자 정렬 가능
#a = ["5","2","3"]
#a.sort()
#["2", "3", "5"]
## 내림차순 정렬 가능
#a.sort(reverse=True)
#["5", "3", "2"]
#✅출력 예시
#grader(s, a)
#학생: 정무 점수: 90점 1등
#학생: 김갑 점수: 80점 2등
#학생: 이을 점수: 70점 3등
#학생: 박병 점수: 50점 4등
#학생: 최정 점수: 40점 5등


print('====================== [START] [Q2] 점수 채점기 ')


def grader(exAnswers, rightAnswers, pointAnswers) :
    print()
    
    #학생별 List로 분리 저장. 
    #최초 점수는 0점으로 등록.
    stuScores = []
    stuNames = []
    stuAnswers = []
    for infos in exAnswers :
        tempInfo = infos.split(',')
        stuNames.append(tempInfo[0])
        stuAnswers.append(tempInfo[1])
        stuScores.append(0)
    
    #i = 문제 번호
    for i in range(len(rightAnswers)) :
        # j는 학생 번호
        for j in range(len(stuNames)) : 
            #print(rightAnswers[i], stuAnswers[j][i:i+1], pointAnswers[i], stuScores[j], rightAnswers[i] == stuAnswers[j][i:i+1])
            if str(rightAnswers[i]) == stuAnswers[j][i:i+1] :
                stuScores[j] += pointAnswers[i]

    #print(stuNames)
    #print(stuAnswers)
    #print(stuScores)

    # sort 함수 사용을 위한 하나의 리스트 (이중배열)로 재 결합
    resultList = []
    for i in range(len(stuNames)) :
        resultList.append([stuScores[i], stuNames[i], stuAnswers[i]])
    
    #sort함수의 경우 별다른 내용지정이 없을 경우 리스트 아이템 순서대로 정렬을 진행.
    resultList.sort(reverse=True)
    
    #재 결합한 리스트
    nowRank = 1
    prePoint = sum(stuScores)    
    #첫번째 인원은 무조건 1등 - 정렬을 한 상태이므로. 1등으로 등록
    resultList[0].append(nowRank);
    
    #위에서 첫번째는 했으므로 두번째 부터 시작. (= 1)
    nowStep = 1
    for nowStep in range(len(resultList)) :
        #전 사람과 동일 점수가 아닐경우 현재 단계를 그대로 삽입.
        if prePoint != resultList[nowStep][0] :
            nowRank = nowStep + 1

        # 위에서 저장한 등수 저장.
        resultList[nowStep].append(nowRank) 
        # 동점체크를 위한 마지막 순위 점수 임시저장.
        prePoint = resultList[nowStep][0]     
    
    #등수 배정 완료후 출력
    for result in resultList :
        print(result[3], '등 >', '학생명 :',  result[1], '/ 점수 :', result[0])


exAnswers = ["김갑,3242524215",
"이을,2242554131",
"박병,2242554131",
"최정,4245242315",
"정무,3242524315"]

#문제번호         1,  2   3,  4,  5,  6,  7,  8,  9, 10
rightAnswers = [ 3,  2,  4,  2,  5,  2,  4,  3,  1,  2]
pointAnswers = [10,  4, 16, 15,  5,  7, 13, 11,  9, 10]

grader(exAnswers, rightAnswers, pointAnswers)

print('====================== [E N D] [Q2] 점수 채점기 ')


#📌Q3. 숫자 맞추기 게임을 만들어 볼게요. 컴퓨터가 임의의 숫자를 3개 만들고 우리가 그것을 #맞춰보겠습니다.
#
#😲조건1 - 숫자는 0 ~ 100까지 숫자를 3개 만듭니다(중복 불가).
#😲조건2 - 5회, 10회까지 정답을 못맞추면 최솟값, 최대값에 대한 힌트를 줍니다.
#😲조건3 - 정답을 맞추면, 맞춘 정답이 최솟값인지, 중간값인지, 최댓값인지 알려줍니다.
#import random
#number = random.randint(0, 100)
#✅출력 예시
#guess_numbers()
#
#1차 시도
#숫자를 예측해보세요 : 39
#숫자를 맞추셨습니다! 39는 최솟값입니다.
#2차 시도
#숫자를 예측해보세요 : 48
#숫자를 맞추셨습니다! 48는 최댓값입니다.
#3차 시도
#숫자를 예측해보세요 : 100
#숫자를 맞추셨습니다! 100는 최댓값입니다.
#게임종료
#3번 시도만에 예측 성공
#
#...
#5차 시도
#숫자를 예측해보세요 : 9
#9는 없습니다
#최솟값은 9보다 작습니다
#6차 시도
#숫자를 예측해보세요 : 9
#이미 예측에 사용한 숫자입니다
#6차 시도

print('====================== [START] [Q3] 숫자 맞추기 게임 ')

#2번 문제에서 이미 import 하였음.
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
    
    #숫자 3개 뽑기
    while len(nums) < selNums : 
        #0 ~ 100 사이의 숫자 랜덤 추출
        num = random.randint(minNum, maxNum)
        #이미 뽑은 숫자인지 체크해서, 아닌 경우 배열에 넣음.
        if num not in nums :
            nums.append(num)
            answerBools.append(False)
    
    #리스트안의 숫자 정렬
    nums.sort()
    
    #디버깅을 위해서 컴퓨터 선택을 표기
    print('Q3 컴퓨터의 선택 :', nums)


    #못맞춘 숫자가 있으면 무한 반복
    while False in answerBools :
        nowStatusText = ''
        for i in range(len(answerBools)) :
            if answerBools[i] == True :
                nowStatusText += str(nums[i])
            else :
                nowStatusText += 'XX'

            if i < (len(answerBools) - 1) :
                nowStatusText += ', '

        print('========== 현재 라운드 : [', gameRound, ']')
        print('========== 현재 상  황 : [', nowStatusText, ']')

        try :
            userSelNum = int(input('번호를 선택하세요 > '))        
        except :
            print('입력한 값을 숫자로 변환하는 과정에서 에러 발생. 다시 입력해주세요')
            continue
        
        idx = -1
        try : 
            #.index로 해당 숫자가 존재하는지 체크.
            # 없는 경우 ValueError 에러리턴.
            idx = nums.index(userSelNum)
        except : 
            # 에러를 사용하여 프로세스 처리
            idx = -1
        
        # 여기에 걸릴리는 없음. index 함수는 값이 없으면 에러 리턴하므로, 0미만의 값이 나올수 없음.
        if idx < 0 :
            print('[', userSelNum, ']은 정답이 아닙니다.')
            
            #5회, 10회에 못맞춘 경우 힌트 리턴
            printHint(gameRound, hintRound, userSelNum, nums)
            #라운드 1 증가후 에러리턴
            gameRound += 1
            continue
        
        if answerBools[idx] == True :
            print('[', userSelNum, ']은 이미 맞춘 답입니다. - 회차를 증가시키지 않습니다.')
            continue
        
        #정답을 맞췄으므로 진행상태 변경
        answerBools[idx] = True

        if userSelNum == nums[0]:
            print('[', userSelNum, '] : 최소 값')
        elif userSelNum == nums[-1]  :
            print('[', userSelNum, '] : 최대 값')
        else :
            print('[', userSelNum, '] : 중간 값')
        
        #아직 종료가 안되었을 경우 라운드 1 늘림.
        if False in answerBools :
            gameRound += 1
        
        continue
    
    #위 게임이 끝나고 결과 정리.
    print('[', gameRound, ']회 만에 맞추셨습니다.')
    print('정답 ===> ', nums)
    
# 힌트 처리
def printHint(gameRound, hintRound, userSelNum, nums) :
    #현재 라운드가 힌트가 주어지는 라운드가 아니면 패스 처리
    if gameRound not in hintRound :
        return
    
    # 현재 라운드가 힌트가 주어지는 라운드 일 경우 아래 로직 확인해서 체크
    # 최소값보다 작은 경우
    if userSelNum < nums[0] :
        print('입력한 [', userSelNum, ']은 최소 값보다 작습니다.')

    # 최대값보다 큰숫자인 경우
    if userSelNum > nums[-1] :
        print('입력한 [', userSelNum, ']은 최대 값보다 큽니다.')
        
    # 해당 값이 최대, 최소값 중간인 경우 중간값 찾기
    if userSelNum > nums[0] and userSelNum < nums[-1] : 
        print('입력한 [', userSelNum, ']은 최대 값과 최소값 사이에 존재하는 숫자입니다.')
        
        if userSelNum > nums[1] : 
            print('입력한 [', userSelNum, ']은 중간 값보다 큰 숫자입니다.')
        if userSelNum < nums[1] : 
            print('입력한 [', userSelNum, ']은 중간 값보다 작은 숫자입니다.')





guess_numbers()

print('====================== [E N D] [Q3] 숫자 맞추기 게임 ')


#📌Q4. 오늘 애인이 생겼다고 해봅시다. 100일을 기념하고 싶은데요.
#
#날짜를 넣으면 100일 뒤가 몇월 며칠인지 계산해주는 함수를 만들어 보겠습니다.
#
#😲조건1 - "오늘부터 1일"이기 때문에 날짜를 계산할 때 오늘을 포함합니다
#😲조건2 - 몇년도인지 구분하지 않고 윤년도 고려하지 않고 2월은 무조건 28일로 합니다.
#🧐hint
## 특정 원소의 위치를 찾는 방법
#a = [1,2,3,4]
#a.index(1)
#0
#✅출력 예시
#after_100(6,21,"월")
#6월 21일 월요일부터 100일 뒤는 9월 28일 화요일


print('====================== [START] [Q4] 100일 계산기 ')

def after_100(inputMonth, inputDate, inputDay) :

    resultMonth = inputMonth
    #해당 날짜는 포함을 해야하므로 date에서 1빼고 시작. [조건1]
    resultDate = inputDate - 1
    leftDate = plusDate
    resultYear = '올해'
    
    # 100일 이후 월, 일 계산
    while 1 : 
        #잔여일이 현재 월의 날짜보다 많은 경우 다음 달로 패스.
        if resultDate + leftDate > monthDates[resultMonth - 1] :
            #잔여일자 계산
            leftDate = leftDate - (monthDates[resultMonth - 1] - resultDate)
            resultDate = 0
            resultMonth += 1 
            #만약 12월이 지났다면 1월로 다시 처리.
            if resultMonth > 12 :
                resultMonth = 1
                resultYear = '내년'
        #위 케이스가 아니면 해당 월이 종료일이므로 루프에서 아웃.
        else :
            resultDate = leftDate
            break

    #요일 계산.
    dayOrderInput = daysStr.index(inputDay)
    # 오늘 포함 100일 이므로 -1일 해줘야 99일뒤의 요일이 구해짐.
    dayOrderResult = (plusDate + dayOrderInput - 1) % len(daysStr)

    print('100일 뒤의 날짜 : ', resultYear, resultMonth,  '월', resultDate, '일 (', daysStr[dayOrderResult], ')')


daysStr = ['일', '월', '화', '수', '목', '금', '토']

#월간 날짜
#              1   2   3   4   5   6   7   8   9  10  11  12
monthDates = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

plusDate = 100

inputMonth = int(input('기준 월 입력 > '))
inputDate = int(input('기준 일 입력 > '))
inputDay = input('기준 요일 입력 (월,화,수,목,금,토,일) > ')

after_100(inputMonth, inputDate, inputDay)

print('====================== [E N D] [Q4] 100일 계산기 ')
