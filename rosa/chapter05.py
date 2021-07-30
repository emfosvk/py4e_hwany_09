# exec(open("rosa/chapter05.py").read())

# infinate Loop 주의. (무한반복할경우 끝없이 자원을 사용함)

# while 조건문(false가 될때까지 무한 실행) :
#     실행문

n = 5

while n > 0 :
    print(n)
    if n == 2 :
        print ('break while')    
        break #Loop Stop Force
    else : 
        print ('continue while')
        n -= 1  #이 라인이 빠지면 무한루프가 되어버림.
        continue #현재 단계 중단후 바로 다음 루프 진행 
    print ('continue 사용시 여기까지 안옴.')
print ('end while / n = ' + str(n))

while True :
    print('문자열 출력기 : done 입력 종료 / # 입력시 아무것도 하지 않고 패스')
    line = input('> ')
    if line[0] == '#' :
        continue
    elif line == 'done' :
        break
    print(line)
print('Finished !! - input While STR') 

# for 변수명 in 배열 :
#     실행문

for num in [1,2,3,4,5] :
    print(num)
print('Finished !! - 1 to 5') 

friends = ['Connect', 'Korea', 'NHN']
for friend in friends :
    print(friend)
print('Finished !! - friends') 
# 1 ~ 5 차례대로 print 실행됨.

# 05-3,05-4 통합 (Loop 응용)
largestNum = -1
smallestNum = None
sumValue = 0
numCount = 0
numAvg = 0
numbers = [5,7,23,54,6,21]
findNumber = 6
findFlag = False
print('###############################################')
 
for number in numbers : 
    if largestNum < number :
        largestNum = number

    if smallestNum is None :
        smallestNum = number
    elif smallestNum > number :
        smallestNum = number

    if number == findNumber :
        findFlag = True
    numCount += 1
    sumValue = sumValue + number
    numAvg = sumValue / numCount
    print('#', numCount, ' Now Number  : '    , number)
    print('#', numCount, ' Largest     : ', largestNum )
    print('#', numCount, ' Smallest    : ', smallestNum )
    print('#', numCount, ' Largest     : ', largestNum )
    print('#', numCount, ' find Num YN : ', findFlag )
    print('#', numCount, ' Total       : ', sumValue)
    print('#', numCount, ' Avg         : ', numAvg)
    print('###############################################') 

print('Finished !! - largestNum  : ', largestNum) 
print('Finished !! - smallestNum : ', smallestNum) 
print('Finished !! - find Num YN : ', findFlag)
print('Finished !! - numCount    : ', numCount) 
print('Finished !! - sumValue    : ', sumValue) 
print('Finished !! - numAvg      : ', numAvg) 
print('###############################################') 


