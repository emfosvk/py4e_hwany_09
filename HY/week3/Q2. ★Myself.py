#Q2. 가위바위보 업그레이드 버젼을 함수로 만들어 봅시다. 아래와 같은 조건을 만족해 주세요.
#조건 1: 게임을 몇 판을 진행할 것인지 입력을 받아주기
#조건 2: 0, 1, 2, "가위", "바위", "보" 이외에 다른 입력을 받으면 재입력 받기
#조건 3: 게임종료 후 나와 컴퓨터의 총 전적 출력하기

# 입력
#games = int(input("몇 판을 진행하시겠습니까? : "))
#rsp_advanced(games)
# 출력
#가위 바위 보 : 0
#나: 가위
#컴퓨터: 보
#1 번째 판 나의 승리!

#가위 바위 보 : 1
#나: 바위
#컴퓨터: 가위
#2 번째 판 나의 승리!

#나의 전적: 2승 0무 0패
#컴퓨터의 전적: 0승 0무 2패

import random
CompRsp = random.randint(0, 2)#0=가위, 1=바위, 2=보

print('============[업그레이드 가위바위보 게임][START]============')

# '몇 판을 진행할까요?' 에 입력하는 값이 자연수가 아닌 경우에 에러메시지를 출력하고 '다시 몇 판을 진행할까요?' 메시지를 띄우고 싶은데, 여기저기 시도해봤는데도 계속 문제가 생겨서 그 부분을 비워놨습니다. 어떤 텍스트를 어디에 삽입해야 할까요?


def Advanced_Rsp(number) :

  GameRound = 0
  UserWin = 0
  CompWin = 0
  Draw = 0
  numberint = int(number)

  while GameRound < numberint :

    UserRsp = input('무엇을 낼까요?("가위", "바위", "보" 중에서 하나를 입력하세요.)')
    GameRound += 1

    if UserRsp == '가위' and CompRsp == 0 :
      print('컴퓨터: 가위 // 결과 : 무승부')
      Draw += 1
    elif UserRsp == '가위' and CompRsp == 1 :
      CompWin += 1
      print('컴퓨터 : 바위 // 결과 : 패배')
    elif UserRsp == '가위' and CompRsp == 2 :
      UserWin += 1
      print('컴퓨터 : 보 // 결과 : 승리')
  
    elif UserRsp == '바위' and CompRsp == 0 :
      UserWin += 1
      print('컴퓨터 : 가위 // 결과 : 승리')
    elif UserRsp == '바위' and CompRsp == 1 :
      Draw += 1
      print('컴퓨터 : 바위 // 결과 : 무승부')
    elif UserRsp == '바위' and CompRsp == 2 :
      CompWin += 1
      print('컴퓨터 : 보 // 결과 : 패배')

    elif UserRsp == '보' and CompRsp == 0 :
      CompWin += 1
      print('컴퓨터 : 가위 // 결과 : 패배')
    elif UserRsp == '보' and CompRsp == 1 :
      UserWin += 1
      print('컴퓨터 : 바위 // 결과 : 승리')
    elif UserRsp == '보' and CompRsp == 2 :
      Draw += 1
      print('컴퓨터 : 보 // 결과 무승부')

    else : 
      print('"가위", "바위", "보" 중에서 하나를 입력하세요.')
      GameRound -= 1
      continue
      
    
  print('전적 : ', GameRound, '전 ', UserWin, '승 ', Draw, '무 ', CompWin, '패')
  print('============[업그레이드 가위바위보 게임][E N D]============')

games = input('몇 판을 진행할까요?')
Advanced_Rsp(games)
