Q1. 파이썬으로 컴퓨터에게 우리가 원하는 일을 시킬 수 있다고 하였습니다.
    파이썬으로 할 수 있는 일은 어떤 것들이 있고, 나는 그중에서 무엇을 하고 싶은지 적어봅시다.

 

Computer Vision을 활용한 문자 인식 프로그램

 ##############################################################

Q2. 파이썬 코딩을 하기에 앞서 하드웨어를 이해하는 것이 중요하다고 했습니다.
    하드웨어 아키텍쳐에서 CPU와 Main Memory 그리고 Secondary Memory의 역할을
   간단하게 정리하여 봅시다.

 

CPU는 개발자(프로그래머)가 계획한 프로그램을 수행하는 물리적 장치,

MainMemory(=RAM)는 CPU가 실행할 프로그램을 일시적으로 저장하는 장치
 
SecondaryMemory는 MainMemory에 업로드되야 하는 프로그램을 보관하는 장치. 

 ##############################################################

Q3. 파이썬은 우리의 명령을 이해하지 못했을 때, 친절하게 Error Message를 통해
   어떤 명령을 이해하지 못했는지 알려줍니다.  그것을 보고 코드의 버그를 수정해가는 과정을
   Debugging이라고 합니다. 이것은 코딩에 있어서 매우 중요합니다.
   따라서, Error Message에 대해서 이해하는 시간을 가져봅시다.
    강의에서는 SyntaxError, ValueError, TypeError 3가지가 등장했습니다.
   ①각각의 Error를 발생시키는 코드를 2가지씩 만들어보고

 

1) SyntaxError

#case1
print('hello world')

#solve
print('hello world')

#case2
x = 10
if x > 10  # missing ':'
	print('x is bigger than 5')
    
#solve
x = 10
if x > 10 :
	print('x is bigger than 5')
 

2) ValueError

#case1
int('1.0')

#solve
int('1')

################################

#case2
Test_case1 = '1.0'
int(Test_case1)

#solve
Test_case1 = '1.0'
float(Test_case1) # or use str()
3)TypeError

int_a = 1
Cha_a = 'a'
sum_a = int_a + Cha_a

print(sum_a)
Float_a = 1.135
Float_a = chr(Float_a) #chr은 단일 문자만 변환시켜준다.
print(type(Float_a),Float_a)

  ②Debugging한 코드도 만들어 봅시다.
  ③그리고 그 밖에 다른 Error도 3가지를 찾아 그 Error를 발생시키는 코드와

1) NameError: name 'case2' is not defined

#case1
print('hello world')
case2 #forgot using '#'
print('hello world')

2) IndentationError: expected an indented block

x= 10
if x > 5 :
print('x is bigger than 5') #들여쓰기를 무시할 경우

3)ZeroDivisionError: division by zero

print(1/0)



##############################################################





Q4. 강의에서 미국과 유럽의 엘리베이터 층수를 변환하는 프로그램이 나왔습니다.
     그와 비슷하게 우리는 한국 나이를 미국 나이로 변환하는 프로그램을 코딩 해봅시다.

hint: 미국 나이는 생일이 지났는지 안지났는지가 중요하죠!
birth = int(input("생일이 지났습니까? 맞으면 0 아니면 -1 : "))
from datetime import datetime

now=datetime.now()


BirthAndAge=input('생년월일 8자리를 입력해주세요:') # 생년월일 입력받기, 8자리 넘는 에러는 나중에 추가.

KorAge= now.year - int(BirthAndAge[0:4]) + 1 #한국 나이= 현재년도 - 태어난 년도 +1

today = 100*now.month + now.day # 오늘의 월+일



if today > int(BirthAndAge[4:8]) : #오늘날짜가 생일보다 크면, 생일이 지났다는 의미.
    UsAge = KorAge -1
else :
    UsAge = KorAge -2


print('your Kor age is:',KorAge,'your Us age is:',UsAge)