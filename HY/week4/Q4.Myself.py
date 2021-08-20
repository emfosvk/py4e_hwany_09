#Q4.  주민등록번호의 앞 6자리는 생년월일이고 뒷자리의 시작번호는 성별을 나타냅니다. 주민등록번호를 입력하면 몇년 몇월 생인지 그리고 남자인지 여자인지 출력하는 함수를 만들어 봅시다.
#주민등록번호는 6자리 이후에 -로 구분되어야 하고 길이는 -포함 14임
#뒷자리는 1,3 은 남자 2,4는 여자
#00 ~ 21로 시작할 경우 2000년 이후 출생자인지 물어 볼 것 (맞으면 o 틀리면 x)
#뒷자리 3, 4를 가질 수 있는 사람은 00년생 이후 출생자 밖에 없음
#주민등록번호 조건을 만족하지 않는 수가 입력되면 "잘 못된 번호입니다"를 출력해주세요.
# 출력 예시
#a = "500629-2222222"
#check_id(a)
#50년06월 여자

#a = "000629-2222222"
#check_id(a)
#2000년 이후 출생자 입니까? 맞으면 o 아니면 x : o
#잘못된 번호입니다.
#올바른 번호를 넣어주세요

#a = "000629-2222222"
#check_id(a)
#2000년 이후 출생자 입니까? 맞으면 o 아니면 x : x
#00년06월 여자

# step 1. 주민등록번호 14자리 입력('- 포함')
# step 2. 올바른 주민등록번호인지 확인하고 아닐 경우 에러메시지 출력한 뒤 다시 돌아가기
# step 3. 입력값의 앞 두자리가 00~21로 시작할 경우 2000년 이후 출생자인지 묻기
# step 4. 2000년생 이후 출생 여부에 따른 출력값 저장하기(뒷자리 1,3 / 2,4 구분도 고려한 뒤 일치하지 않는 경우 에러메시지 출력)
# step 5. 입력값의 문자열 순서에 따라 '[:2]'년, '[2:4]'월 // '7'의 값에 따라 성별 출력하기


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
  print('성별', Gender)
  if Check2000 == 'Before' :
    print('19', MYID[:2], '년', MYID[2:4], '월생' )
  elif Check2000 == 'After' :
    print('20', MYID[:2], '년', MYID[2:4], '월생' )

#-----------------실행부분--------------------------
number = None
IDCheck(number)
