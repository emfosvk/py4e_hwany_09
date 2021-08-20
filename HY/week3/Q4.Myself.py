##################################################################################
#📌Q4. 2개의 숫자를 입력하여 그 사이에 소수가 몇 개인지 출력하는 함수를 만들어 봅시다.
#소수: 1과 자기 자신만을 약수로 가지는 수
#
#🔽 출력 예시
## 입력
#n = int(input("첫 번째 수 입력 : "))
#m = int(input("두 번째 수 입력 : "))
#count_prime_number(n, m)
#
## 출력
#소수개수  4
def primeNum(n, m) :
  if n > m :
    frNum = m
    ToNum = n
  else : 
    frNum = n
    ToNum = m

## frNum과 ToNum을 int로 변환해주지 않아도 range() 안에서는 정수로 인식하는건가요?

  Num_List = [i for i in range(frNum, ToNum+1)]
  PrimeNum_List = []

  for i in Num_List :
    if i < 2 :
      print('2 이상의 자연수가 아닙니다.')
      continue
    
    Check = True

    for j in range(2, i) :
      if i%j == 0 :
        Check = False
        continue
    
    if Check == True :
      PrimeNum_List += [i]

  print('소수 목록 : ', str(PrimeNum_List))
  print('소수 개수 :', len(PrimeNum_List), '개')

print('두 개의 자연수 사이에 존재하는 소수를 찾아봅시다!!')
n = int(input('2 이상의 자연수를 입력하세요.'))
m = int(input('2 이상의 자연수를 입력하세요.'))
primeNum(n, m)