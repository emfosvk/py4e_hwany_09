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

print('[베스킨라빈스31 게임!!]')
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
      regame = input('게임을 한 번 더 진행하고 싶다면 "re"를 입력하세요. 게임을 종료하고 싶다면 아무 키나 입력하세요.')
      print('')
      if regame == 're' :
        number = ['0']
        continue
      else : 
        print('게임을 종료합니다.')
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
      regame = input('게임을 한 번 더 진행하고 싶다면 "re"를 입력하세요. \n게임을 종료하고 싶다면 아무 키나 입력하세요.')
      print('')      
      if regame == 're' :
        number = ['0']
        continue
      else : 
        print('게임을 종료합니다.')
        break


#4. 컴퓨터 출력값 리스트에 추가---------------------------------
    number = number + compSplit
    number = list(map(int, number))
#---------------------bs31 함수 끝-------------------------  
    