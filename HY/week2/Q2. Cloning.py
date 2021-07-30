print('')
print('============[START][Q2]세전세후 연봉 계산기[by 월급]')

taxRange = [1200, 4600, 8800, 30000, 50000]
taxRate  = [   6,   15,   35,    38,    40,    42]
taxCalFinish = False #Q. True와 False의 용도를 알고싶습니다.

while taxCalFinish == False : # Q. 이 줄에 대해서도 해설해주시면 감사하겠습니다.
  salaryStr = input('현재 받는 월급(세전)을 입력하세요(만단위)>')
  salary = 0 #Q. 이 줄은 어떤 기능을 한거죠...?
  if salaryStr == '':
    print('연봉계산기 패스 (빈 값 입력)')
    taxCalFinish == True
    break
  elif salaryStr == 'done':
    print('연봉계산기 종료(done 입력)')
    taxCalFinish = True
    break
  try : 
    salary = int(salaryStr)
    if salary < 0 :
      print('숫자는 언제나 양수를 입력해주셔야합니다.(0 초과)')
      continue
  except : 
    print('잘못된 값을 입력하셨습니다.')
    continue

  salYearIncTax = salary * 12
  taxLevel = 0; # Q. 37~43열도 해설해주시면 감사하겠습니다...ㅎㅎ
  for maxSal in taxRange : 
    if maxSal >= salYearIncTax :
      break
    taxLevel += 1
  realSalAmtRate = 1.00 - (taxRate[taxLevel] / 100)#Q. 파이썬이 taxRate를 어떻게 인지하죠? / 대괄호에 특별한 기능이 있나요?
  salYearExcTax = round(salYearIncTax *(realSalAmtRate), 2)

  print('입력급여:', str(salary), '만원')
  print('세전 연봉:', str(salYearIncTax), '만원' )
  print('세후 연봉:', str(salYearExcTax), '만원')
  print('적용 세금 단계:', str(taxLevel + 1), '단계')
  print('적용 세율 :', str(taxRate[taxLevel]), '%')
  print('**********************************')

print('=====================[E N D] [Q2] 세전세후 연봉 계산기(by 월급))')