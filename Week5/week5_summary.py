#Q1. 여러분 혹시 베스킨라빈스31 게임을 아시나요? 1부터 31까지 숫자를 플레이어들끼리 번갈아 외치다가 31을 외치는 사람이 패배하는 게임인데요.

#이번엔 이 게임을 파이썬 함수로 만들어 봅시다. 지성이 없이 숫자를 랜덤하게 외치는 컴퓨터와 대결을 해보겠습니다.
#조건1 - 나의 턴에서는 숫자를 직접 입력하며 한 번 입력 후에 space 한 번으로 구분
#Ex)
#my = input("My turn - 숫자를 입력하세요: ")
#1 2 3

#조건2 - 나와 컴퓨터 모두 한 턴에 1회 ~ 3회까지만 숫자를 외칠 수 있음

#조건3 - 외쳐진 숫자보다 1큰 수만 외칠수 있음 (ex: 5 다음엔 무조건 6)

#위 조건이 안맞을 경우 다시 입력
#🧐hint
#출력예시
#bs31()

#베스킨라빈스 써리원 게임
#My turn - 숫자를 입력하세요: 1 2 3
#현재 숫자 : 3
#컴퓨터 : 4
#현재 숫자 : 4

#My turn - 숫자를 입력하세요: 5
#현재 숫자 : 5
#컴퓨터 : 6
#컴퓨터 : 7
#현재 숫자 : 7


####################################################
#---------------------MY RULE----------------------#
####################################################

# step 1 : 플레이어와 컴퓨터가 입력한 숫자들을 저장하는 리스트를 만든다.

# step 2 : 플레이어에게 숫자를 입력받는다.
#          1) 게임 진행순서에 맞는 숫자를 입력할 것
#          2) 숫자 사이에 스페이스를 입력할 것
#          3) 입력하는 숫자는 연속될 것

# step 3 : 플레이어가 잘못된 값을 입력하는 에러의 대처를 만든다.
#          1) 숫자가 아닌 문자를 입력한 경우
#          2) 스페이스를 빠뜨린 경우(자동으로 '3)'으로 인식)
#          3) 진행순서에 맞지 않는 숫자를 입력한 경우 
#          4) 한 개도 입력하지 않거나 네 개 이상을 입력한 경우

# step 4 : 플레이어가 입력한 숫자 뒤에 이어지는 숫자를 컴퓨터가 1~3개 외칠 수 있도록 한다(random.randit 사용).

# step 5 : 플레이어가 입력한 숫자와 컴퓨터가 출력한한 숫자인 문자열을 스페이스를 기준으로 split 한 뒤 리스트에 저장한다.

# step 6 : 일련의 과정을 반복문으로 설정한 뒤 플레이어나 컴퓨터가 31을 외치는 순간 게임을 종료하고 승자를 선언한다.
#          1) 31을 외쳐야 하는 차례면 31까지만 외칠 수 있어야 함
#          2) 만약 컴퓨터가 28~30 사이에서 출력을 시작한다면 30으로 마무리 지어야 함(난이도 업)
####################################################

# 베스킨라빈스31 게임 START#

import random

print('====================== [START] [Q1] 베스킨 라빈스 31 게임 ')
print('')
print('Rule 1 : 연속된 숫자를 한 개에서 세 개 까지 입력하세요("1"에서 시작).')
print('Rule 2 : 컴퓨터도 플레이어가 입력한 마지막 숫자에 이어 한 개에서 세 개의 숫자를 출력합니다.')
print('Rule 3 : 상대방이 출력한 마지막 숫자와 이어지는 숫자를 한 개에서 세 개 까지 번갈아가며 입력합니다.')
print('Rule 4 : "31"을 입력하는 사람이 패배합니다.')
print('****** : 숫자 사이는 스페이스바로 구분하세요.')
print('****** : 게임을 종료하려면 "done"을 입력하세요.')
print('')

def bs31() :

  number = ['0']

  while 1 : 
    user = input(' 숫자를 입력하세요 : ')
    userSplit = user.split()

#0. 게임을 종료하고 싶은 경우---------------------------------
    if user == 'done' :
      print('')
      print('게임을 종료합니다.')
      break

#1.플레이어 입력 에러 대처------------------------------------
#1-1) 정수가 아닌 값을 입력한 경우-----------------------------
    try : 
      list(map(int, userSplit))
    except : 
      print(' * Error : 정수를 입력하세요.')
      continue  

#1-2) 아무런 값을 입력하지 않은 경우---------------------------
    if len(userSplit) == 0 :
      print(' * Error : 최소 한 개 이상의 숫자를 입력하세요.')
      continue

#1-3)플레이어가 31을 외치는 차례인 경우 31을 초과하는 숫자 입력 불가--
    if max(number) == 29 :
      if len(userSplit) > 2 :
        print(' * Error : 31을 초과하는 숫자는 입력할 수 없습니다.')
        continue
    if max(number) == 30 :
      if len(userSplit) > 1 :
        print(' * Error : 31을 초과하는 숫자는 입력할 수 없습니다.')
        continue

#1-4) 네 개 이상의 숫자를 입력한 경우---------------------------
    if len(userSplit) > 3 : 
      print(' * Error : 세 개 이하의 숫자를 입력하세요.')
      continue

#1-5) 진행순서에 맞지 않는 숫자를 입력한 경우---------------------
    if int(max(number)) != int(userSplit[0]) - 1 :
      print(' * Error : 진행순서에 맞는 숫자를 입력하세요')
      continue  

#1-6) 입력한 숫자가 연속되지 않을 경우---------------------------
    if len(userSplit) == 2 :
      if int(userSplit[1]) - int(userSplit[0]) != 1 : 
        print(' * Error : 연속된 숫자를 입력하세요.')
        continue

    if len(userSplit) == 3 :
      if int(userSplit[2]) - int(userSplit[1]) != 1 : 
        print(' * Error : 연속된 숫자를 입력하세요.')
        continue

      if int(userSplit[2]) - int(userSplit[0]) != 2 : 
        print(' * Error : 연속된 숫자를 입력하세요.')
        continue

#★★★ 승자 판독 및 리게임 ★★★
    if '31' in userSplit :
      print('')
      print('컴퓨터의 승리ㅜㅜㅜㅜ')
      while 1:
        regame = input('게임을 한 번 더 진행하고 싶다면 "re"를 입력하세요.')
        print('')
        if regame == 're' :
          bs31()
        elif regame == 'done' :
          print('게임을 종료합니다.')        
          break
        else:
          print(''''re' 혹은 'done'을 입력해주세요.''')
          continue
      break


#2. 사용자 입력값 리스트에 추가---------------------------------
    number = number + userSplit
    number = list(map(int, number))


#3. 컴퓨터 입력값 설정----------------------------------------
#3-1) 컴퓨터 차례에 28~30을 외칠 순서가 온 경우-------------------
    comp = ''
    compRandNum = random.randint(1,3)

    if int(max(number)) == 27 :
      comp = '28 29 30' 
      print(' 컴퓨터 :' + comp)
      
    elif max(number) == 28 :
      comp = '29 30'
      print(' 컴퓨터 :' + comp)
    elif max(number) == 29 :
      comp = '30'
      print(' 컴퓨터 :' + comp)

#3-2 컴퓨터 차례에 31을 외칠 순서가 온 경우-----------------------
    elif max(number) == 30 :
      comp = '31'
      print(' 컴퓨터 :' + comp)
    

#3-3) 컴퓨터 기본 입력값 설정-----------------------------------
    elif compRandNum == 1 :
      comp = str(int(max(number)) + 1)
      print(' 컴퓨터 : ' + comp)
    elif compRandNum == 2 :
      comp = str(int(max(number)) + 1) + ' ' + str(int(max(number)) + 2)
      print(' 컴퓨터 : ' + comp)    
    elif compRandNum == 3 :
      comp = str(int(max(number)) + 1) + ' ' + str(int(max(number)) + 2)+ ' ' + str(int(max(number)) + 3)
      print(' 컴퓨터 : ' + comp)

#★★★ 승자 판독 및 리게임 ★★★
    compSplit = comp.split()
    if compSplit[0] == '31' : 
      print('')
      print('★★★ 플레이어의 승리! ★★★')
      regame = input('게임을 한 번 더 진행하고 싶다면 "re"를 입력하세요.')
      print('')      
      if regame == 're' :
        number = ['0']
        continue
      elif regame == 'done' :
        print('게임을 종료합니다.')
        break


#4. 컴퓨터 출력값 리스트에 추가---------------------------------
    number = number + compSplit
    number = list(map(int, number))
#---------------------bs31 함수 끝-------------------------  


#5. bs31 함수 실행------------------------------------------
bs31()
print('====================== [E N D] [Q1] 베스킨 라빈스 31 게임 ')

#1. 이름,답으로 구성된 문자열을 입력받음
#2. 채점기준이 되는 답을 받음
#3. 이름 답으로 구성된 문자열은 ','를 기준으로 이름과 답으로 구분
#4. 답과 답안은 개별 문자로 슬라이싱하고 각각을 비교함. 같으면 1, 틀리면 0을 반환
#5. 반환된 값을 모두 합쳐서 각각의 이름에 맵핑하면 학생의 점수가 나옴.
#6. 내림차순으로 정렬하면 등수가 됨.

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

print('====================== [START] [Q2] 채점기 ')
stdlist=[]

i=0
rank=1
while True:
    try:
        stdNum=int(input('정답을 매겨야 하는 학생은 몇명입니까?'))
        break
    except:
        print('숫자를 입력해주세요.')

while True:
    try:
        ans=int(input('정답을 입력하세요:'))
    except:
        print('정답은 숫자만 입력되야 합니다.')
        continue
    if len(str(ans)) == 10:
        break
    else:
        print('정확히 10개의 값을 입력해주세요.')




while stdNum-i:

    while True:


        stdNameScore=(input('이름과 답을 ,로 구분하여 입력해 주세요'))
        try:
          name,stdAns = stdNameScore.split(',')
        except:
          print(''' ','를 반드시 넣어주세요.''')

        try:
            stdAns=int(stdAns)
        except:
            print('답안 입력은 숫자만 허용됩니다.')
            continue
        if len(str(stdAns)) == 10:
            break
        else:
            print('입력된 답의 갯수는:',len(str(stdAns)),'개 입니다.')
            print('학생의 답안은 10 개여야 합니다.')


    stdlist.append(stdNameScore.split(','))
    stdlist[i][1]=list(stdlist[i][1])
    score = 0
    for j in range(0,10) :
        if stdlist[i][1][j] == str(ans)[j]:
            score +=1
    stdlist[i][1]=score*10


    print('이름:',stdlist[i][0],'/','점수:',stdlist[i][1]) #0번째 값의 이름은 [0][0] 이고 답안은 [0][1]
    i +=1


stdDes = sorted(stdlist, key= lambda x:x[1],reverse=True)

print('')
print('성적은 다음과 같습니다.')
print('')

for item in stdDes:
    item.append(rank)
    rank +=1

    print('이름:',item[0],'점수:',item[1],'등수:',item[2])

print('')
print('동점자의 경우, 이름순으로 등수가 표시됩니다.')
print('')
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


# 📌Q4. 오늘 애인이 생겼다고 해봅시다. 100일을 기념하고 싶은데요.
#
# 날짜를 넣으면 100일 뒤가 몇월 며칠인지 계산해주는 함수를 만들어 보겠습니다.
#
# 😲조건1 - "오늘부터 1일"이기 때문에 날짜를 계산할 때 오늘을 포함합니다
# 😲조건2 - 몇년도인지 구분하지 않고 윤년도 고려하지 않고 2월은 무조건 28일로 합니다.
# 🧐hint
## 특정 원소의 위치를 찾는 방법
# a = [1,2,3,4]
# a.index(1)
# 0
# ✅출력 예시
# after_100(6,21,"월")
# 6월 21일 월요일부터 100일 뒤는 9월 28일 화요일


print('====================== [START] [Q4] 100일 계산기 ')


def after_100(inputMonth, inputDate, inputDay):
    resultMonth = inputMonth
    # 해당 날짜는 포함을 해야하므로 date에서 1빼고 시작. [조건1]
    resultDate = inputDate - 1
    leftDate = plusDate
    resultYear = '올해'

    # 100일 이후 월, 일 계산
    while 1:
        # 잔여일이 현재 월의 날짜보다 많은 경우 다음 달로 패스.
        if resultDate + leftDate > monthDates[resultMonth - 1]:
            # 잔여일자 계산
            leftDate = leftDate - (monthDates[resultMonth - 1] - resultDate)
            resultDate = 0
            resultMonth += 1
            # 만약 12월이 지났다면 1월로 다시 처리.
            if resultMonth > 12:
                resultMonth = 1
                resultYear = '내년'
        # 위 케이스가 아니면 해당 월이 종료일이므로 루프에서 아웃.
        else:
            resultDate = leftDate
            break

    # 요일 계산.
    dayOrderInput = daysStr.index(inputDay)
    # 오늘 포함 100일 이므로 -1일 해줘야 99일뒤의 요일이 구해짐.
    dayOrderResult = (plusDate + dayOrderInput - 1) % len(daysStr)

    print('100일 뒤의 날짜 : ', resultYear, resultMonth, '월', resultDate, '일 (', daysStr[dayOrderResult], ')')


daysStr = ['일', '월', '화', '수', '목', '금', '토']

# 월간 날짜
#              1   2   3   4   5   6   7   8   9  10  11  12
monthDates = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

plusDate = 100

while 1:
    inputMonth = input('기준 월 입력 > ')
    try:
        inputMonth = int(inputMonth)
    except:
        print('''입력 '기준 월'은 숫자로만 입력해주세요.''')
        continue
    if 12 >= inputMonth >=1 :
        break
    else:
        print('입력 기준월은 1~12 사이여야 합니다.')

while 1:
    inputDate = input('기준 일 입력 > ')
    try:
        inputDate = int(inputDate)
    except:
        print('''입력 '기준 일'은 숫자로만 입력해주세요.''')
        continue
    if 31>=inputDate>=1:
        break
    else:
        print('입력 기준월은 1~31 사이여야 합니다.')

while 1:
    inputDay = input('기준 요일 입력 (월,화,수,목,금,토,일) > ')
    if inputDay in daysStr:
        break
    else:
        print('(월,화,수,목,금,토,일) 중 하나를 한 글자로 입력해주세요.')
        continue
after_100(inputMonth, inputDate, inputDay)

print('====================== [E N D] [Q4] 100일 계산기 ')
