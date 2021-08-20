#📌Q1. 우리는 큰 수를 나타낼 때 3자리마다 , 를 찍어서 구분해 줍니다. 파이썬에서는 아래와 같이 쉽게 나타낼 수 있습니다.

# f"{숫자:,}"
# print(f"{1000:,}")

#하지만 이번 미션에서는 숫자를 입력 받고 3자리마다 ,를 찍어주는 함수를 만들어 봅시다.

#🔽출력 예시
#make_comma(1000000)
#1,000,000

print('====================== [START] [Q1] 숫자 구분자 콤마 찍기 ')

#[START] make_comma
def make_comma(inputNum) :

    print(len(inputNum));
    numLength = len(inputNum)
    # 입력받은 글자의 자리수가 3이하면 작업할 필요가 없음.
    if numLength <= 3 :
        print(inputNum);
    
    #작업 회수와 들어갈 위치 체크
    #콤마가 들어가야하는 갯수 체크
    commaCnt = (numLength-1) // 3
    #콤마를 맨 앞자리부터 삽입을 하기때문에, 맨처음 에는 몇글자를 띄워야하는지 체크가 필요함. 이는, 나머지 값으로 체크하면 됨.
    indent = (numLength) % 3
    # 나머지가 0인 경우 자리수가 3,6,9 이므로 처음에 들어가는 위치는 3번째 숫자 뒤 이므로, 3칸 넘겨서 집어넣음.
    if indent == 0 : 
        indent = 3
    loopRound = 0

    while loopRound < commaCnt :
        commaPosition = indent + ((loopRound)*3) + loopRound
        inputNum = inputNum[:commaPosition] + ',' + inputNum[commaPosition:]
        loopRound += 1
    print(inputNum)
#[E N D] make_comma


while True:
    num = input('[숫자,생성기] input number (그냥 엔터시 종료) > ')
    if num == '' :
        break
    make_comma(num)

print('====================== [E N D] [Q1] 숫자 구분자 콤마 찍기 ')


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

print('====================== [START] [Q2] 문자열 파일 저장 및 특정문구 반복회수 계산기')

#[START] count_word
def count_word(inputText, checkText) :
    # [조건1 - START] 문구를 매개변수로 받아, 텍스트 파일로 생성
    # 파일 저장 경로 지정
    filePath = "rosa/tempFiles/w3q2_rosa_text.txt"

    # 아래 문구는 Python에서 제공하는 로직이므로, 
    # 정답 예시에 제시된 대로 그대로 사용
    text_save = open(filePath, "w", encoding="UTF8")
    text_save.write(inputText)
    text_save.close()
    
    print("다음 경로에 파일 저장 완료 :", filePath)
    # [조건1 - E N D] 문구를 매개변수로 받아, 텍스트 파일로 생성
    
    # [조건2 - START] 위에서 저장한 파일에서 특정 문구 반복회수 찾기
    q2hand = open(filePath)
    
    repeatCnt = 0
    includLineCnt = 0

    for line in q2hand :
        # 단순 글자 반복체크는 아래 count 내장함수 사용
        repeatCnt += line.count(checkText)
        # 들어가있는 라인 체크는 아래 로직 사용
        if checkText in line :
            includLineCnt += 1

    print("찾고자하는 문구 :", checkText)
    print("해당 문구 반복 라인수 : ", includLineCnt)
    print("해당 문구 반복 횟  수 : ", repeatCnt)
    # [조건2 - E N D] 위에서 저장한 파일에서 특정 문구 반복회수 찾기
#[E N D] count_word    

inputText = """하이요
굿굿굿
"""

checkText = '굿'

count_word(inputText, checkText)

print('====================== [E N D] [Q2] 문자열 파일 저장 및 특정문구 반복회수 계산기')




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


#📌Q4.  주민등록번호의 앞 6자리는 생년월일이고 뒷자리의 시작번호는 성별을 나타냅니다. #주민등록번호를 입력하면 몇년 몇월 생인지 그리고 남자인지 여자인지 출력하는 함수를 만들어 봅시다.
#
#
#주민등록번호는 6자리 이후에 -로 구분되어야 하고 길이는 -포함 14임
#뒷자리는 1,3 은 남자 2,4는 여자
#00 ~ 21로 시작할 경우 2000년 이후 출생자인지 물어 볼 것 (맞으면 o 틀리면 x)
#뒷자리 3, 4를 가질 수 있는 사람은 00년생 이후 출생자 밖에 없음
#
#주민등록번호 조건을 만족하지 않는 수가 입력되면 "잘 못된 번호입니다"를 출력해주세요.
#
#
#🔽출력 예시
#
#a = "500629-2222222"
#check_id(a)
#50년06월 여자
#
#a = "000629-2222222"
#check_id(a)
#2000년 이후 출생자 입니까? 맞으면 o 아니면 x : o
#잘못된 번호입니다.
#올바른 번호를 넣어주세요
#
#a = "000629-2222222"
#check_id(a)
#2000년 이후 출생자 입니까? 맞으면 o 아니면 x : x
#00년06월 여자

print('====================== [START] [Q4] 주민등록번호 오류 추출기')

#[START] check_id
def check_id(id) :
    #입력 받은 글자의 양쪽 공백 삭제
    id = id.strip()

    vaildIdResult      = checkIdFormat(id)
    vaildIdResultRegex = checkIdFormatRegex(id)

    print('유효성 검사 결과 - 일반   : ', vaildIdResult)
    print('유효성 검사 결과 - 정규식 : ', vaildIdResultRegex)
    
    #검사 결과가 정상일때만 이후 로직 실행
    if vaildIdResultRegex : 
        
        #성별 코드가 3,4 일 때, 몇년도인지 체크하기위함.
        # 3,4는 00 ~ 21년 만 소유 가능. 
        sexCode = int(id[7:8])
        year = int(id[0:2])
        validSexYear = True
        # 아래 문구는 삼항 연산자 라는 문법으로
        # 파이썬에서는 다음과 같은 문법이다. 
        # 간단한 if문으로 결과를 추출해내기 용이해 사용하는 문법임.
        # 문법 >  참 결과값  if (조건) else  거짓결과 값
        yearPrefix = '20' if (sexCode in [3,4]) else '19'

        if yearPrefix == '20' :
            if year < 22 :
                #성별코드가 3,4 이고 연도가 21이하 일때는 물어봐야함
                centuryInput = input('2000년 이후 출생자 입니까? 맞으면 o 아니면 x >')
                if centuryInput.lower() != 'o' :
                    yearPrefix = '19'

            else : 
                #여기 들어오려면, 성별코드가 3,4이고, 연도가 22 이상임.
                #조건절에 00년 부터 21년까지만 존재한다고 했으므로 에러로 처리.
                validSexYear = False
        
        if validSexYear == False :
           print('연도와 연도 코드 매핑이 잘못되었습니다.')  
           return
        
        #위에서 검증한 데이터를 토대로 연도 출력
        resultText = yearPrefix + id[0:2] + '년 ' + id[2:4] + '월 ' + id[4:6] + '일'
        if sexCode in [1,3] : 
            resultText += ' / 성별 : 남자'
        elif sexCode in [2,4] : 
            resultText += ' / 성별 : 여자'

        print(resultText)    
#[E N D] check_id


#[START] checkIdFormat
def checkIdFormat(id) :
    #Step 1. 자리수 체크
    if len(id) != 14 :
        print('입력한 값의 자리수가 14자리가 아님.')
        return False

    # Step 2. 양식에 맞게 입력했는지  글자 하나씩 체크 - 숫자6 + ',' + 숫자7
    step = 0
    for text in id :
        step += 1
        try : 
          #숫자로 형 변환이 가능한지 체크 가능하면 숫자임.
          int(text)

        except :
          #7번째 루프이고, 그 값이 - 인 경우는 통과처리.
          #이외에는 양식에러 임.
          if step == 7 and '-':
              continue
          print('정해진 양식 이외의 글자가 삽입되었습니다.')
          return False
    
    # Step 3. 연월일 (yymmdd) + 성별코드(1-4) 가 맞는지 체크
    month = int(id[2:4])
    date = int(id[4:6])
    sexCode = int(id[7:8])
    #month가 1 ~ 12 사이인지 체크
    if month < 1 or month > 12 :
        print('1 ~ 12월의 데이터를 입력하세요')
        return False  
    
    #date가 1 ~ 31 사이인지 체크
    if date < 1 or date > 31 :
        #날짜 제대로하려면 윤달도 체크해야하는데, 본 연습에서는 그렇게까지 할 필요는 없음.
        print('1 ~ 31일의 데이터를 입력하세요')
        return False  

    #정해진 성별코드인지 확인
    if sexCode < 1 or sexCode > 4 :
        #날짜 제대로하려면 윤달도 체크해야하는데, 본 연습에서는 그렇게까지 할 필요는 없음.
        print('뒷자리의 성별코드는 1 ~ 4 중에 입력해야합니다.')
        return False 
    
    #모든 로직 체크 완료했으므로 정상입력이라고 리턴
    return True
#[E N D] checkIdFormat


#[START] checkIdFormatRegex
def checkIdFormatRegex(id) :
    #규칙
    #1. 6숫자 + '-' + 7숫자 로 이루어진 총 14자리
    #2. 앞 6자리는 연 / 월 / 일로 이루어짐. 
        #연도는 모든 숫자 2자리
        #월은 01월 부터 12월 까지 존재
        #일은 모든 숫자 01일 ~ 31일 까지 존재.
    #3. 뒷 숫자의 첫자리는 1-4까지만 입력 가능하고, 
    #   나머지 6자리는 아무숫자나 가능. 
    # 위 정보가 아래 정규식에 다 포함되어있음.       
    regex = re.compile(r'\b(?:[0-9]{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[1,2][0-9]|3[0,1]))-[1-4][0-9]{6}\b')
    # 입력받은 번호에서 정규식 표현으로 전화번호 추출
    sResult = regex.search(id)
    #위 정규식으로 데이터를 없으면 양식에 맞지 않는 글이므로 부적합 판정
    if sResult is None :
        print('검색 결과 주민등록번호 발견 실패')
        return False     
    
    # 정규식을 돌린 결과값이 입력값과 같을 경우 딱 그번호만 입력했으므로, 
    # 통과처리하나, 그렇지 않으면 입력한 자료이외의 띄어쓰기를 포함한 다른 데이터도 포함하므로 에러 리턴
    if sResult.group() != id :
        print('주민등록번호를 발견하였지만, 양식에 맞지 않습니다.')
        return False

    #체크 완료했으므로 정상입력이라고 리턴
    return True
#[E N D] checkIdFormatRegex


while True:
    id = input('[주민번호분석기] input id (그냥 엔터시 종료) > ')
    if id == '' :
        break
    check_id(id)

print('====================== [E N D] [Q4] 주민등록번호 오류 추출기')

