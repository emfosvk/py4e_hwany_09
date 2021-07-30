# step 1. 첫 메시지 띄우기(ex. 월급을 입력하세요)
# step 2. 월급에 따른 세율 구간 파악 및 설정하기
# step 3. 각 구간에 알맞은 메시지 출력하기
# ★★★★. 음수 혹은 숫자가 아닌 문자를 입력한 경우 잘못 입력했다는 메시지를 띄워야함

MP = input('월급을 입력하세요.')
MPint = int(MP)

while :
  try :
    MPint =int(MP)
  except :
    MPint = -1
    


  if MPint <= 1200/12 and MPint >= 0 :
    print('세전 연봉:', MPint*12, '만원')
    print('세후 연봉:', MPint*0.94*12, '만원')
  elif MPint > 1200/12 and MPint <= 4600/12 :
    print('세전 연봉:', MPint*12, '만원')
    print('세후 연봉:', MPint*0.85*12, '만원')
  elif MPint > 4600/12 and MPint <= 8800/12 :
    print('세전 연봉:', MPint*12,'만원')
    print('세후 연봉:', MPint*0.76*12, '만원')
  elif MPint > 8800/12 and MPint <= 15000/12 :
    print('세전 연봉:', MPint*12, '만원')
    print('세후 연봉:', MPint*0.65*12, '만원')
  elif MPint > 15000/12 and MPint <= 30000/12 : 
    print('세전 연봉:', MPint*12, '만원')
    print('세후 연봉:', MPint*0.62*12, '만원')   
  elif MPint > 30000/12 and MPint <= 50000/12 :
    print('세전 연봉:', MPint*12, '만원')
    print('세후 연봉:', MPint*0.60*12, '만원')
  elif MPint > 50000/12 :
    print('세전 연봉:', MPint*12, '만원')
    print('세후 연봉:', MPint*0.58*12, '만원')
  break

  else : 
    print('올바른 숫자를 입력하세요.')
  #Q. 숫자가 아닌 문자를 입력했을때 Traceback (most recent call last):
  #  File "main.py", line 2, in <module>
  #    MPint = int(MP)
  #ValueError: invalid literal for int() with base 10: 'dd'
  # 이런 오류메시지가 뜹니다. 
  #저는 'else'가 정해두지 않은 값이 입력됐을 시 실행하는 명령으로 이해해서 음수나, 문자를 입력했을 경우를 상정했는데, 음수를 입력하면 지정된 메시지가 뜨지만 문자를 입력했을 때는 오류가 뜹니다. 어떻게 해결해야 할까요? 