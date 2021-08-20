##################################################################################
#📌Q1. 숫자를 입력 받고 그 숫자의 구구단을 출력하는 함수를 만들어 봅시다. 다만 아래의 조건을 만족해 주세요.
#조건 1: 홀 수 번째만 출력하기
#조건 2: 값이 50이하인 것만 출력하기
#
#🔽 출력 예시
## 입력
#number = int(input("몇 단? : "))
#gugudan(number)
#
## 출력
#몇 단? : 8
#8 단
#8 X 1 = 8
#8 X 3 = 24
#8 X 5 = 40

print('=================== [START] [Q1] 구구단')
def gugudan(num) :
  if num >= 1 and num <= 9 :
    for i in range(1,10) :
      gugudanResult = num * i
      if  gugudanResult < 50 :
        print(str(num) + '*' + str(i) + '=' + str(gugudanResult))
      else : break

number = int(input("몇 단? : "))
gugudan(number)

print('=================== [E N D] [Q1] 구구단')