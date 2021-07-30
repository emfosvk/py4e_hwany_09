# Q4. 나이와 현금 또는 카드를 입력하면 버스 요금이 출력되는 버스 요금 계산기를 만들어봅시다.

print('###########Q4##########')

def feeChecker(age, method):
  if age < 8 or age >= 75 :
    return '무료입니다.'
  elif age < 14 :
     return '450'
  elif age < 20 and method == '카드':
     return '720'
  elif age < 20 and method == '현금':
    return '1000'
  elif age < 75 and method == '카드':
    return '1200'
  elif age < 75 and method == '현금':
     return '1300' 

while 1: #Q. 왜 while을 사용하셨는지 알고싶습니다.
  ageMethod =input('나이와 지불 방법을 알려주세요(현금/카드)').split()#Q. split의 용도와 사용의도를 좀 더 보충설명 해주시면 감사하겠습니다.
  try:#Q. try와 except를 사용하신 의도를 알고 싶고, 21~26열까지 이해가 잘 안돼서 해설해주시면 감사하겠습니다!
    age = int(ageMethod[0])
    method = str(ageMethod[1])
  except : 
    age = -1
    method = -1

  if age > 0 and method in ['카드', '현금'] :
    print('나이', age, '세')
    print('지불유형:', method)
    print('버스요금', feeChecker(age, method))

    break
  else:
    print('invalid value error')

#Q.어떤 값을 입력해도 else로 빠져서 되어서 'invalid value error'가 출력되는데 뭐가 문제일까요...?