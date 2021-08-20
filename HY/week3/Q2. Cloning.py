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
] #Q. rpsResultList를 따로 만든 이유와 왜 이런 방식으로 표현했는지 알고 싶습니다!

def rsp_advanced(number) : 

  gameRound = 0
  winCnt = 0
  drawCnt = 0
  loseCnt = 0

  while gameRound < number :
    userRspStr = input((str(gameRound + 1) + "회차 : 가위(0) 바위(1) 보(2)를 내주세요>"))
    userRsp = convertInputToRsp(userRspStr)
    #Q1. convertInputToRsp(userRspStr)에서 괄호에 userRspStr를 입력한 이유가 궁금합니다!
    if userRsp < 0 or userRsp > 2 :
      print('올바르지 않은 입력입니다.')
      continue

    comRsp = random.randint(0, 2)

    print('사용자 : ' + rpsList[userRsp])
    print('컴퓨터 : ' + rpsList[comRsp])

    #Q. roundResultCode가 W, D, L로 출력되는 과정이 궁금합니다!
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
      print('알 수 없는 코드값 >' + str(gameRound + 1) + '회차를 다시 실행합니다.')
      continue
    print(str(gameRound + 1) + '회차 까지의 누적 전적')
    print(str(winCnt) + '승 / ' + str(drawCnt) + '무 /' + str(loseCnt) + '패')
    gameRound += 1

def convertInputToRsp(userInputData) :
  try : 
    userInputStr = ''
    if userInputData == '가위' :
      userInputStr = '0'
    if userInputData == '바위' :
      userInputStr = '1'
    if userInputData == '보' :
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
games = int(input("몇 판을 진행하시겠습니까? :"))
rsp_advanced(games)

print('====================== [E N D] [Q2] 업그레이드 가위바위보 ')