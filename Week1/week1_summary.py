#Q1. 파이썬으로 컴퓨터에게 우리가 원하는 일을 시킬 수 있다고 하였습니다.
#    파이썬으로 할 수 있는 일은 어떤 것들이 있고, 나는 그중에서 무엇을 하고 싶은지 적어봅시다.

 

#Computer Vision을 활용한 문자 인식 프로그램


#Q2. 파이썬 코딩을 하기에 앞서 하드웨어를 이해하는 것이 중요하다고 했습니다.
#    하드웨어 아키텍쳐에서 CPU와 Main Memory 그리고 Secondary Memory의 역할을 간단하게 정리하여 봅시다.

#  CPU
#  실제 연산작업을 진행하는 장치

#  Main Memory > 주 기억장치
#  연산할 작업물을 기억해두는 장치로서 전원이 날아가는 경우 
#  데이터가 사라져버리는 휘발성으로 인해 별도 장비가 필요함.

#  Secondary Memory > 보조 기억 장치
#  위에서 언급한 데이터의 보존을 위한 장치. 상대적으로 주기억장치에 비해 느리지만, 전원을 종료하더라도 데이터를 보존하고 있기에 사용하는 장기 보존 장치.


#Q3. 파이썬은 우리의 명령을 이해하지 못했을 때, 친절하게 Error Message를 통해
#    어떤 명령을 이해하지 못했는지 알려줍니다.  그것을 보고 코드의 버그를 수정해가는 과정을
#    Debugging이라고 합니다. 이것은 코딩에 있어서 매우 중요합니다.
#    따라서, Error Message에 대해서 이해하는 시간을 가져봅시다.
#    강의에서는 SyntaxError, ValueError, TypeError 3가지가 등장했습니다.
#    ①각각의 Error를 발생시키는 코드를 2가지씩 만들어보고
#    ②Debugging한 코드도 만들어 봅시다.
#    ③그리고 그 밖에 다른 Error도 3가지를 찾아 그 Error를 발생시키는 코드와
#    ④Debugging한 코드를 1가지씩 만들어 봅시다.

print('Week 1 / Quiz 3')
#① 에러코드
#①-1 SyntaxError
#print('①-1 SyntaxError 1) #1
#input('①-1 SyntaxError 2 - 'input Your Name'') #2

#①-2 ValueError
#print(int('Error MSG')) #1
#print(float('String')) #2

#①-3 TypeError
#print(int('123') + '123') #1
#print(float('19.0') + str(1234)) #2

#② 코드 Debugging
#②-1 SyntaxError - Debugging Code
print('①-1 SyntaxError 1')  #1
input('①-1 SyntaxError 2 - \'input Your Name\' : ') #2

#②-2 ValueError - Debugging Code
print(int('555')) #1
print(float('123.456')) #2

#②-3 TypeError - Debugging Code
print(int('123') + int('123')) #1
print(float('19.0') + int('1234')) #2


#③ 그밖의 Error
#③-1 NameError
# 정해진 함수명을 잘못 사용했을때
#ptint('①-1 SyntaxError 1')

#③-2 ZeroDivisionError
# 나누기의 분모가 0일 경우
#kk = 1000
#ll = 0
#zeroDiv = kk / ll

#④-1 FileNotFoundError
#Open 명령어 사용시 해당 파일이 없는 경우

#③ 그밖의 Error
#③-1 NameError - Debugging Code
# 정해진 함수명을 잘못 사용했을때
print('①-1 SyntaxError 1')

#④-2 ZeroDivisionError - Debugging Code
# 나누기의 분모가 0일 경우
kk = 1000
ll = 0
if ll != 0 :
    printResult = kk / ll
else :
    printResult = 0
print('3-4-2 계산결과 : ' + str(printResult))


#④-3 FileNotFoundError - Debugging Code
#Open 명령어 사용시 해당 파일이 없는 경우
#exec(open("없는파일.py").read())

#Q4. 강의에서 미국과 유럽의 엘리베이터 층수를 변환하는 프로그램이 나왔습니다.

#    그와 비슷하게 우리는 한국 나이를 미국 나이로 변환하는 프로그램을 코딩 해봅시다.
#    hint: 미국 나이는 생일이 지났는지 안지났는지가 중요하죠!
#    birth = int(input("생일이 지났습니까? 맞으면 0 아니면 -1 : "))

print('Week 1 / Quiz 4')
korAge = input('한국 나이를 입력해주세요 : ') 
birth = input('생일이 지났나요? 지났으면 0, 아니면 -1을 입력해주세요 : ')
usaAge = int(korAge) + int(birth) - 1
print('당신의 미국 나이는', usaAge, '입니다.')
