#Q1. 우리는 큰 수를 나타낼 때 3자리마다 , 를 찍어서 구분해 줍니다. 파이썬에서는 아래와 같이 쉽게 나타낼 수 있습니다.
#하지만 이번 미션에서는 숫자를 입력 받고 3자리마다 ,를 찍어주는 함수를 만들어 봅시다.
#출력 예시
#make_comma(1000000)
#1,000,000


def comma_make(number) :
  
  while 1 :
    inputNum = input("콤마를 삽입할 숫자를 입력하세요(종료하려면 엔터).")

    #-------------종료 기능--------------
    if inputNum == '' : 
      print('종료')
      break
    
    #------맨 앞자리 수가 0인 경우 대처------
    ##-> 맨 앞자리의 0을 지운 뒤 컴마 입력
    ##ex) 01000 -> 1,000
    while inputNum[0] == '0' :
      inputNum = inputNum[1:]

    numLength = len(inputNum)
    commaCnt = (numLength-1) // 3
    indent = numLength % 3
    loopRound = 0

    if indent == 0 :
      indent = 3

    #-------문자를 입력했을 경우 대처-------- 
    try : 
      inpuNum = int(inputNum)

    except : 
      print('올바른 숫자를 입력하세요')
      continue    

    #-----3자리 이하의 수를 입력한 경우----
    if len(inputNum) <= 3 :
      print(inputNum)
    
    #-----3자리 초과의 수를 입력한 경우----
    elif len(inputNum) > 3 :
      while loopRound < commaCnt :
        commaposition = indent + (loopRound*3) + loopRound
        inputNum = inputNum[:commaposition] + ',' + inputNum[commaposition:]
        loopRound += 1
      print(inputNum)

#-----------------실행----------------
number = None
comma_make(number)