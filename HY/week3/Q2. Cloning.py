##################################################################################
#๐Q2. ๊ฐ์๋ฐ์๋ณด ์๊ทธ๋ ์ด๋ ๋ฒ์ ผ์ ํจ์๋ก ๋ง๋ค์ด ๋ด์๋ค. ์๋์ ๊ฐ์ ์กฐ๊ฑด์ ๋ง์กฑํด ์ฃผ์ธ์.
#์กฐ๊ฑด 1: ๊ฒ์์ ๋ช ํ์ ์งํํ  ๊ฒ์ธ์ง ์๋ ฅ์ ๋ฐ์์ฃผ๊ธฐ
#์กฐ๊ฑด 2: 0, 1, 2, "๊ฐ์", "๋ฐ์", "๋ณด" ์ด์ธ์ ๋ค๋ฅธ ์๋ ฅ์ ๋ฐ์ผ๋ฉด ์ฌ์๋ ฅ ๋ฐ๊ธฐ
#์กฐ๊ฑด 3: ๊ฒ์์ข๋ฃ ํ ๋์ ์ปดํจํฐ์ ์ด ์ ์  ์ถ๋ ฅํ๊ธฐ
#
#๐ฝ ์ถ๋ ฅ ์์
## ์๋ ฅ
#games = int(input("๋ช ํ์ ์งํํ์๊ฒ ์ต๋๊น? : "))
#rsp_advanced(games)
#
## ์ถ๋ ฅ
#๊ฐ์ ๋ฐ์ ๋ณด : 0
#๋: ๊ฐ์
#์ปดํจํฐ: ๋ณด
#1 ๋ฒ์งธ ํ ๋์ ์น๋ฆฌ!
#
#๊ฐ์ ๋ฐ์ ๋ณด : 1
#๋: ๋ฐ์
#์ปดํจํฐ: ๊ฐ์
#2 ๋ฒ์งธ ํ ๋์ ์น๋ฆฌ!
#
#๋์ ์ ์ : 2์น 0๋ฌด 0ํจ
#์ปดํจํฐ์ ์ ์ : 0์น 0๋ฌด 2ํจ

print()
print('====================== [START] [Q2] ์๊ทธ๋ ์ด๋ ๊ฐ์๋ฐ์๋ณด')
import random

rpsList = ['๊ฐ์', '๋ฐ์', '๋ณด']
rpsResultList = [
  ['D','L','W'],
  ['W','D','L'],
  ['L','W','D']
] #Q. rpsResultList๋ฅผ ๋ฐ๋ก ๋ง๋  ์ด์ ์ ์ ์ด๋ฐ ๋ฐฉ์์ผ๋ก ํํํ๋์ง ์๊ณ  ์ถ์ต๋๋ค!

def rsp_advanced(number) : 

  gameRound = 0
  winCnt = 0
  drawCnt = 0
  loseCnt = 0

  while gameRound < number :
    userRspStr = input((str(gameRound + 1) + "ํ์ฐจ : ๊ฐ์(0) ๋ฐ์(1) ๋ณด(2)๋ฅผ ๋ด์ฃผ์ธ์>"))
    userRsp = convertInputToRsp(userRspStr)
    #Q1. convertInputToRsp(userRspStr)์์ ๊ดํธ์ userRspStr๋ฅผ ์๋ ฅํ ์ด์ ๊ฐ ๊ถ๊ธํฉ๋๋ค!
    if userRsp < 0 or userRsp > 2 :
      print('์ฌ๋ฐ๋ฅด์ง ์์ ์๋ ฅ์๋๋ค.')
      continue

    comRsp = random.randint(0, 2)

    print('์ฌ์ฉ์ : ' + rpsList[userRsp])
    print('์ปดํจํฐ : ' + rpsList[comRsp])

    #Q. roundResultCode๊ฐ W, D, L๋ก ์ถ๋ ฅ๋๋ ๊ณผ์ ์ด ๊ถ๊ธํฉ๋๋ค!
    roundResultCode = rpsResultList[userRsp][comRsp]
    if roundResultCode == 'W' :
      winCnt += 1
      print('๋น์ ์ ์น๋ฆฌ์๋๋ค.')
    elif roundResultCode == 'D' :
      drawCnt += 1
      print('๋น๊ฒผ์ต๋๋ค.')
    elif roundResultCode == 'L' :
      loseCnt += 1
      print('์ปดํจํฐ์ ์น๋ฆฌ์๋๋ค.')
    else :
      print('์ ์ ์๋ ์ฝ๋๊ฐ >' + str(gameRound + 1) + 'ํ์ฐจ๋ฅผ ๋ค์ ์คํํฉ๋๋ค.')
      continue
    print(str(gameRound + 1) + 'ํ์ฐจ ๊น์ง์ ๋์  ์ ์ ')
    print(str(winCnt) + '์น / ' + str(drawCnt) + '๋ฌด /' + str(loseCnt) + 'ํจ')
    gameRound += 1

def convertInputToRsp(userInputData) :
  try : 
    userInputStr = ''
    if userInputData == '๊ฐ์' :
      userInputStr = '0'
    if userInputData == '๋ฐ์' :
      userInputStr = '1'
    if userInputData == '๋ณด' :
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

#์ค์  ์คํ๋ฌธ
games = int(input("๋ช ํ์ ์งํํ์๊ฒ ์ต๋๊น? :"))
rsp_advanced(games)

print('====================== [E N D] [Q2] ์๊ทธ๋ ์ด๋ ๊ฐ์๋ฐ์๋ณด ')