# Q3. 2개의 숫자를 입력하여 그 사이에 짝수만 출력하는 함수를 만들어 봅시다. 그리고 중앙값도 함께 출력 해봅시다.(중앙값이 홀수라면 제외)
# 중앙값: 정중앙에 있는 값
# 특정 두 숫자 사이의 수들을 리스트로 만드는 법
# n = 1
# m = 10
# numbers = [ i for i in range(n,m+1)] # [1,2,3,4,5,6,7,8,9,10]
# # range(시작 숫자, 끝 숫자 + 1)
# 🔽 출력 예시
# # 입력
# n = int(input("첫 번째 수 입력 : "))
# m = int(input("두 번째 수 입력 : "))
# find_even_number(n, m)
# # 출력
# 첫 번째 수 입력 : 1
# 두 번째 수 입력 : 11
# 2 짝수
# 4 짝수
# 6 짝수
# 6 중앙값
# 8 짝수
# 10 짝수

def evenPrinter(firstNum, secondNum) :
  numList = [i for i in range(firstNum, secondNum+1)]
  #Q."i for i" for 앞에 i가 붙으면 어떤 기능을 하는지 궁금합니다!
  for i in numList :
    if i == (firstNum + secondNum)/2 and i % 2 == 0:
      print(i, '중앙값')
    elif i % 2 == 0 :
      print(i, '짝수')
  
flag = 1
while flag:
  firstNum = input('첫 번째 수 입력:')
  secondNum = input('두 번째 수 입력:')

  try:
    firstNum = int(firstNum)
    secondNum = int(secondNum)
  except:
    firstNum = -1
    secondNum = -1

  if secondNum-firstNum > 0:
    print('첫 번째 입력값', firstNum)
    print('두 번째 입력값', secondNum)
    evenPrinter(firstNum, secondNum)
    flag = 0

  else :
    print('0이상의 정수를 입력해주세요(첫 번째 입력값은 두 번째 입력값보다 작아야 합니다.)')