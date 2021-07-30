#step 1. 첫 메시지 띄우기(ex. 무엇을 낼까요?)
#step 2. 컴퓨터가 랜덤으로 가위바위보를 낼 수 있게 하기
#step 3. 경우의 수 파악 및 설정하기
#step 4. 각 경우의 수에 알맞은 메시지 출력하기
#★★★★ '가위','바위', '보' 가 아닌 다른걸 입력했을 때 잘못 입력했다는 메시지를 띄워야 함


my = input("무엇을 낼까요?")
mystr = str(my)
import random
computer = random.randint(0,2) # 0=가위, 1=바위, 2=보
if mystr == '가위' and computer == 0 :
  print('나: 가위')
  print('컴퓨터: 가위')
  print('무승부')
elif mystr == '가위' and computer == 1 : 
  print('나: 가위')
  print('컴퓨터: 바위')
  print('졌다...ㅜㅜ')
elif mystr == '가위' and computer == 2 : 
  print('나: 가위')
  print('컴퓨터: 보')
  print('이겼다 얏호!')
elif mystr == '바위' and computer == 0 :
  print('나: 바위')
  print('컴퓨터: 가위')
  print('이겼다 얏호!')
elif mystr == '바위' and computer == 1 :
  print('나: 바위')
  print('컴퓨터: 바위')
  print('무승부')
elif mystr == '바위' and computer == 2 :
  print('나: 바위')
  print('컴퓨터: 보')
  print('졌다...ㅜㅜ')
elif mystr == '보' and computer == 0 :
  print('나: 보')
  print('컴퓨터: 가위')
  print('졌다...ㅜㅜ')
elif mystr == '보' and computer == 1 :
  print('나: 보')
  print('컴퓨터: 바위')
  print('이겼다 얏호!')
elif mystr == '보' and computer == 2 :
  print('나: 보')
  print('컴퓨터: 보')
  print('무승부')
else :
  print('가위, 바위, 보 중에서 내야지!!')