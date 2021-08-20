# 📌Q1. 우리는 큰 수를 나타낼 때 3자리마다 ','' 를 찍어서 구분해 줍니다. 파이썬에서는 아래와 같이 쉽게 나타낼 수 있습니다.

# # f"{숫자:,}"
# print(f"{1000:,}")

# 하지만 이번 미션에서는 숫자를 입력 받고 3자리마다 ,를 찍어주는
# 함수를 만들어 봅시다.
# 🔽출력 예시

# make_comma(1000000)
# 1,000,000

print('====================== [START] [Q1] 콤마 삽입기')

def commaInserter (value) :
    commaNum = (len(value)-1)//3


    inverseValue = list(value[::-1])
    for i in range(0,commaNum) :

        inverseValue.insert((i*4+3),',')

    resultValue="".join(inverseValue[::-1])



    return resultValue
while 1 :
    inputValue=input('숫자를 입력해주세요:')

    try:
        inputValue=int(inputValue)
    except:
        inputValue=-1
    if inputValue < 0 :
        print('양의 정수를 입력해주세요')
    else:
        inputValue=str(inputValue)
        print(commaInserter(inputValue))
        break

print('====================== [E N D] [Q1] 콤마 삽입기 추출기 종료')
#📌Q2. 어느날 여러분이 어떤 글을 읽고 있는데, 갑자기 특정 글자가 전체 글에서 몇개 들어있는지 궁금해졌습니다. 그럼 한 번 파이썬 함수로 만들어 봅시다.
#글은 어떤 글이 좋습니다. 인터넷에서 검색해서 복사 붙여넣기로 변수에 넣어 줍니다.

#변수에 담긴 글을 함수에 넣어주면 txt 파일로 저장도 함께 되도록 해줍니다.

#출력 예시
#a ="""안녕하세요. 
#반갑습니다. 파이썬 공부는 정말 재밌습니다.
#"""
#
#count_word(a, "습니다")
#2
print('====================== [START] [Q2] 구문 계수기')

def wordCnter(inputText, checkText):
    filePath = "rosa/tempFiles/w3q2_GG_text.txt"
    text_save = open(filePath, "w", encoding="UTF8")
    text_save.write(inputText)
    text_save.close()
    print("다음 경로에 파일 저장 완료:", filePath)



    q2hand = open(filePath)
    repeatCnt = 0
    for line in q2hand:
        repeatCnt += line.count(checkText)

    print("Word Count You Find:", repeatCnt)

inputText = '''부스터 여러분들, 4주차 강의는 잘 들으셨나요(1)

학습한 내용을 토대로 풀이하여야 할 4주차 미션 내용을 아래와 같이 공개합니다!

미션 내용을 팀원들과 함께 풀이해주세요(2) 적극적인 토론이 필요(3)합니다'''
checkText="요"

wordCnter(inputText, checkText)

print('====================== [E N D] [Q2] 구문 계수기 종료')


#📌Q3. 요즘 식당에 들어가면 방명록을 적게 되어있습니다.

#어느 식당의 사장님이 여러분에게 방명록을 주면서 전화번호를 제대로 적었는지 검사해달라는 부탁을 했습니다.

#아래와 같은 방명록이 있을 때 방명록을 잘 못쓴 사람의 이름과 잘 못된 번호를 출력하는 함수를 만들어 봅시다.

#김갑,123456789
#이을,010-1234-5678
#박병,010-5678-111
#최정,111-1111-1111
#정무,010-3333-3333
 
#함수에 방명록을 넣으면 txt 파일로 저장되게 해줍니다.
#제대로 적은 방명록의 조건은 다음과 같습니다
#010 으로 시작함
#번호가 - 로 구분이 되어 있음
#-를 포함하여 길이가 13임

#🔽출력 예시

#guest_book = """김갑,123456789
#이을,010-1234-5678
#박병,010-5678-111
#최정,111-1111-1111
#정무,010-3333-3333"""
#wrong_guest_book(guest_book)
#
#잘못 쓴 사람: 김갑
#잘못 쓴 번호: 123456789
#
#잘못 쓴 사람: 박병
#잘못 쓴 번호: 010-5678-111
#
#잘못 쓴 사람: 최정
#잘못 쓴 번호: 111-1111-1111

print('====================== [START] [Q3] 방명록 오류 추출기')

#[START] wrong_guest_book_regex
def wrong_guest_book(guest_book) :
    print("일반 로직")

    filePath = "rosa/tempFiles/w3q3_rosa_text.txt"

    #[조건1]의 파일 저장은 다음 함수에서 처리.
    save_guest_book(filePath, guest_book)

    wrongInfo = ''

    q3hand = open(filePath)

    for line in q3hand :
      line = line.strip();
      # 내용 체크해서 아무런 내용도 없으면 해당 라인 패스 처리
      if line == '':
          continue

      #, 구분자 없이 라인이 등록되어있는지 체크
      commaPosition = line.find(',')
      # 결과값이 -1이면 해당 글자가 없는 것임. 이경우는 양식에 맞지 않으니 패스 처리
      if commaPosition == -1 :
          wrongInfo = wrongInfo + line + '\n'
          continue
      
      #아래부터 핸드폰 번호 체크
      #Step1.핸드폰 자리수가 13자리인지 체크    
      telNum = line[commaPosition + 1 :]
      if len(telNum) != 13 :
          wrongInfo = wrongInfo + line + '\n'
          continue


      #Step2.문자열의 시작이 010인지 체크
      if telNum.startswith('010') is False :
          wrongInfo = wrongInfo + line + '\n'
          continue


      #Step3.문자열 구분이 (-로 이루어졌는지 체크)
      #전제조건1 : 숫자 양식은 3,4,4 이다. 즉 하이픈의 위치는 4번째, 9번째 자리어야한다.
      #전제조건2 : 하이픈(-)은 2회만 사용한다.
      hyphenCnt = 0
      nowStep = 0
      passTextBool = True

      for text in telNum :
          #프로그램상 숫자의 시작은 0이지만, 아래로직으로 인해서 첫 시작을 1로 체크함.
          nowStep += 1
          try :
              #숫자로 강제 변환했을때, 정상이면 숫자이고 아니면 문자임. 
              #문자면 에러 발생하고, 그 값이 하이픈인지 체크함.
              int(text)

              # 현재 글자 위치가 4 혹은 9인 경우 하이픈이 와야하는데, 그렇지 않으므로 오류처리. 
              if nowStep == 4 or nowStep == 9 :
                  passTextBool = False
                  break                

          except :
              #문자인 경우 하이픈이아닌 경우에는 잘못 입력된 코드로 처리.
              if text != '-' :
                  passTextBool = False
                  #아래의 Break로는 전체로직의 중단이 아닌 글자 하나씩 꺼내서 체크하는 본 반복문만 중단됨.
                  break
              hyphenCnt += 1

              #하이픈 사용이 2회이상 초과일 경우에도 양식에 맞지 않는다 판단.
              if hyphenCnt > 2 : 
                  passTextBool = False
                  break
                  
              # 현재 글자 위치가 3 혹은 7이 아닌데, 하이픈이므로 오류처리. 
              if nowStep != 4 and nowStep != 9 :
                  passTextBool = False
                  nowStep += 1
                  break  
      
      if passTextBool == False :
          wrongInfo = wrongInfo + line + '\n'
          continue
      

    #체크 완료. # 최종 출력처리
    print('잘못등록된 목록 - 일반 로직')
    #아래 정규식에서도 동일하게 출력하기 때문에 함수로 분리.
    lastProc_guest_book(wrongInfo)
#[E N D] wrong_guest_book

#[START] wrong_guest_book_regex
import re #정규식 모듈

def wrong_guest_book_regex(guest_book) :
    print("정규식 사용 로직")

    filePath = "rosa/tempFiles/w3q3_rosa_text.txt"

    #[조건1]의 파일 저장은 다음 함수에서 처리.
    save_guest_book(filePath, guest_book)

    wrongInfo = ''
    
    q3hand = open(filePath)

    for line in q3hand :
        line = line.strip();
        
        # 내용 체크해서 아무런 내용도 없으면 해당 라인 패스 처리
        if line == '':
            continue
  
        #, 구분자 없이 라인이 등록되어있는지 체크
        commaPosition = line.find(',')
        # 결과값이 -1이면 해당 글자가 없는 것임. 이경우는 양식에 맞지 않으니 패스 처리
        if commaPosition == -1 :
            wrongInfo = wrongInfo + line + '\n'
            continue
        
        telNum = line[commaPosition + 1 :]
  
        #아래부터 핸드폰 번호 체크         
        #step Special : 이런게 있다는 것만 알고 넘어가세요
        #               정규식을 사용한 숫자양식 체크 010 -  4자리 - 4자리
        # 이 로직을 사용할 경우 13자리 체크와 동시에 양식폼 (010-4-4)체크가 가능함.
        # 상단에 import re를 등록하여 정규식 표현 사용을 위한 모듈 등록 필요.
        # 정규식 규정을 다음과 같이 설정 010 - 숫자4자리 - 숫자4자리 (\d는 정규식에서 숫자를 의미함.)
        regex = re.compile(r"010-\d\d\d\d-\d\d\d\d") 
        # 입력받은 번호에서 정규식 표현으로 전화번호 추출
        sResult = regex.search(telNum)
        #추출 받은 값과 원본의 값이 동일하다면 정상적으로 번호를 입력한 것이고, 
        # 자리수가 틀리든 양식에 맞지 않든 잘못 입력한거임.
  
        #양식에 맞는 문구가 없을 경우 아래에서 걸림.
        if sResult is None :
            wrongInfo = wrongInfo + line + '\n'
            continue
  
        #양식에 맞는 문구는 찾았으나, 그 이외의 다른내용이 들어갈 경우 아래에서 걸림.
        regexResult = sResult.group()
        if regexResult != telNum :
            wrongInfo = wrongInfo + line + '\n'
            continue
      
    print('잘못등록된 목록 - 정규식')
    lastProc_guest_book(wrongInfo)
#[E N D] wrong_guest_book_regex

#[START] save_guest_book
def save_guest_book(filePath, inputText) :

    # [조건1 - START] 문구를 매개변수로 받아, 텍스트 파일로 생성
    # 파일 저장 경로 지정

    # 아래 문구는 Python에서 제공하는 로직이므로, 
    # 정답 예시에 제시된 대로 그대로 사용
    text_save = open(filePath, "w", encoding="UTF8")
    text_save.write(inputText)
    text_save.close()
    
    print("다음 경로에 파일 저장 완료 :", filePath)
    # [조건1 - E N D] 문구를 매개변수로 받아, 텍스트 파일로 생성
#[E N D] save_guest_book

#[START] lastProc_guest_book
def lastProc_guest_book(wrongInfo) :
    
    #본격적으로 시작하기 전에 앞뒤의 공백 제거 처리.
    wrongInfo = wrongInfo.strip()

    #입력 받은 값이 빈값인지 체크 하여 없으면 정상처리
    if wrongInfo == '' :
        print('출력할 자료가 없습니다.')
        return

    lines = wrongInfo.split('\n')

    for line in lines :
        #, 구분 없이 입력된 경우 이름/핸드폰번호 분리 불가능. 하나의 라인으로 출력후 패스
        if line.find(',') < 0 : 
            print('잘못입력된 라인 : ', line)
            continue
        # 이 경우가 아니면 ,를 기준으로 앞은 이름, 뒤는 핸드폰번호로 규정되어있으므로 출력처리    
        info = line.split(',')
        print('잘못 쓴 사람 : ', info[0])
        print('잘못 쓴 번호 : ', info[1])
#[E N D] lastProc_guest_book

guest_book = """김갑,123456789
이을,010-1234-5678
박병,010-5678-111
최정,111-1111-1111
홍길동,0102-896-1236
홍길순,010--586-4567
막나가010-1122-3344
제갈말자,010-586-44567
정무,010-3333-3333"""

#일반 String 배열 비교를 사용한 구문
wrong_guest_book(guest_book)

print()

#정규표현식을 사용한 로직
wrong_guest_book_regex(guest_book)

print('====================== [E N D] [Q3] 방명록 오류 추출기')



# Q4.  주민등록번호의 앞 6자리는 생년월일이고 뒷자리의 시작번호는 성별을 나타냅니다. 주민등록번호를 입력하면 몇년 몇월 생인지 그리고 남자인지 여자인지 출력하는 함수를 만들어 봅시다.
# 주민등록번호는 6자리 이후에 -로 구분되어야 하고 길이는 -포함 14임
# 뒷자리는 1,3 은 남자 2,4는 여자
# 00 ~ 21로 시작할 경우 2000년 이후 출생자인지 물어 볼 것 (맞으면 o 틀리면 x)
# 뒷자리 3, 4를 가질 수 있는 사람은 00년생 이후 출생자 밖에 없음

# 주민등록번호 조건을 만족하지 않는 수가 입력되면 "잘 못된 번호입니다"를 출력해주세요.
print('====================== [START] [Q4] 주민정보 추출기')
def IDCheck(number) :
  Check2000 = 'Before'
  Gender = None

  while 1 : 

    #--------------올바른 주민등록번호인지 확인----------------
    MYID = input('주민등록번호 13자리를 입력하세요("-"포함)')
    
    ##1) 숫자로 제대로 입력했는지 확인
    try :
      numberA = int(MYID[:5])
      numberB = int(MYID[7:])
    except : 
      print('올바른 값을 입력하세요.1')
      continue

    ##2)1월~12월을 입력했는지 확인
    Check23 = int(MYID[2:4])
    if Check23 > 12  :
      print('올바른 값을 입력하세요.2')
      continue
    elif Check23 < 1 :
      print('올바른 값을 입력하세요.3')
      continue
    
    ##3) 1일~31일을 입력했는지 확인(월별 구분은 힘들어서 포기했습니다..ㅎㅎ)
    Check45 = int(MYID[4:6])
    if Check45 > 31 :
      print('올바른 값을 입력하세요.4')   
      continue
    elif Check45 < 1 :
      print('올바른 값을 입력하세요.5')  
      continue

    ##4) '-'를 제대로 입력했는지 확인
    if MYID[6] != '-' :
      print('올바른 값을 입력하세요.6')
      continue

    ##5) 자릿수가 맞는지, 뒷자리가 1~4에 포함되는지 확인
    Check7 = int(MYID[7])
    if len(MYID) != 14 :
      print('올바른 값을 입력하세요.7')
      continue
    elif Check7 > 4 :
      print('올바른 값을 입력하세요.8')
      continue
    elif Check7 < 1 :
      print('올바른 값을 입력하세요.9')
      continue

    #-------------------2000년생 이후 출생 확인-------------
    Check01 = int(MYID[:2])
    if Check01 < 22 : 
      while 2 : 
        Check1 = input('2000년 이후 출생자입니까? 맞으면 "1", 틀리면 "2"를 입력하세요.')
        if Check1 == '1' :
          Check2000 = 'After'
          break
        elif Check1 == '2' :
          Check2000 = 'Before'
          break    
        else : 
          print('올바른 값을 입력하세요.10')
          continue
  
    #------------성별, 성별과 뒷자리 일치 확인-------------
    if MYID[7] == '1' and Check2000 == 'Before' :
      Gender = '남성'
      break
    elif MYID[7] == '3' and Check2000 == 'After' :
      Gender = '남성'
      break
    elif MYID[7] == '2' and Check2000 == 'Before' :
      Gender = '여성'
      break
    elif MYID[7] == '4' and Check2000 == 'After' :
      Gender = '여성' 
      break
    else : 
      print('올바른 값을 입력하세요.11')
      continue 

  #-----------------출력부분-------------------------
  print('성별 : ', Gender)
  if Check2000 == 'Before' :
    print('19', MYID[:2], '년',' ', MYID[2:4], '월생',sep='' )
  elif Check2000 == 'After' :
    print('20', MYID[:2], '년',' ', MYID[2:4], '월생',sep='' )

#-----------------실행부분--------------------------
number = None
IDCheck(number)

print('====================== [E N D] [Q4] 주민정보 추출기 종료')