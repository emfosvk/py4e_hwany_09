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

def even(n, m) :

  if n > m :
    FirstNum = m
    SecondNum = n
  else : 
    FirstNum = n
    SecondNum = m

  NumList = [i for i in range(FirstNum, SecondNum+1)]

  for i in NumList :
    if i % 2 == 0 and i == (FirstNum + SecondNum) / 2 :
      print(i, '중앙값')
    elif i % 2 == 0 and i > 0 :
      print(i)

flag = 1 

while flag :
  n = input('첫 번째 숫자를 입력하세요. // 자연수만 입력 가능')
  m = input('두 번째 숫자를 입력하세요. // 자연수만 입력 가능')

  try :
    n = int(n)
    m = int(m)
  except : 
    n = -1
    m = -1

  if n > 0 and m > 0 :
    print('첫 번째 입력값', n)
    print('두 번째 입력값', m)

    even(n, m)
    flag = 0
    break

  else : 
    print('자연수를 입력하세요')