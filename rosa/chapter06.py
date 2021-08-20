fruit = 'banana'

# String : b a n a n a 
# index  : 0 1 2 3 4 5
# fruit[2] >>> 'n'
# fruit[5] >>> 'a'
# fruit[7] >>> IndexError: string index out of range

# len 해당 문자열의 글자 길이 체크 함수
# len(fruit) >> 6 

index = 0
while index < len(fruit) :
  letter = fruit[index]
  print(index, letter)
  index += 1
#출력 결과 
#0 b
#1 a
#2 n
#3 a
#4 n
#5 a

for letter in fruit :
   print(letter)

#출력 결과 
#b
#a
#n
#a
#n
#a
# >> index 변수 오타, 이외의 오타등 단순 조회에는 for문이 조금더 안전 (인적사고 방지)
#    시작과 종료시점을 for문이 기계적으로 체크해주므로 ....


#6-2

mystring = 'Monty Python'
# String : M o n t y   P y t h  o  n 
# index  : 0 1 2 3 4 5 6 7 8 9 10 11
# 종료숫자는 포함하지 않음.
# mystring[0:4]
# >> Mont
# mystring[6:7]
# >> P
# mystring[6:20]
# >> Python  >> 인덱스 초과하는 숫자이지만, 에러를 발생시키지 않음.

# 특정 칸을 비울경우 각각 맨앞, 맨끝을 의미.
# mystring[:2]
# >> Mo      == [0:2]
# mystring[6:]
# >> Python  == [6:12]
# mystring[:]
# >> Monty Python  == [0:12]


#문자열 병합
#a = 'Hello'
#b = a + 'There'
#b  == 'HelloThere'
#c = a + ' ' + 'There'
#c  == 'Hello There'

#논리연산자 in
#fruit = 'banana'
#'n' in fruit >>> True
#'m' in fruit >>> False
#'nan' in fruit >>> True

#문자열 비교
#word = 'banana'
#if word == 'banana':
# print('All right, bananas.')

#if word < 'banana':
# print('Your word,' + word + ', comes before banana.')
#elif word > 'banana':
# print('Your word,' + word + ', comes after banana.')
#else:
# print('All right, bananas.')

#class str의 Method들.
dir('str')

#.find('문자열') > 입력한 글자의 위치값을 리턴. 찾지 못하면 -1
#.upper()      > 대문자로 변환    
#.lower()      > 소문자로 변환 
#.replace('변경전문자열', '변경후문자열') > 해당 문자열에서 특정 문구를 찾은뒤 변경. 
#.lstrip() / .rstrip() .strip() > 왼쪽/오른쪽/양쪽 공백 제거 
#.startswith('문자열') > 접두사 체크 


#>>> data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
#>>> atpos = data.find('@')
#>>> print(atpos)
#21
#>>> sppos = data.find(' ',atpos)
#>>> print(sppos)
#31
#>>> host = data[atpos+1 : sppos]
#>>> print(host)
#uct.ac.za


# python 2 에서는 unicode가 별도의 문자열타입으로 존재했지만,
# python 3 부터는 동일한 str 타입으로 변경됨. 모든 str 타입이 unicode로 변경됨.

#>>> x = '이광춘'
#>>> type(x)
#<type 'str'>
#>>> x = u'이광춘'
#>>> type(x)
#python2  :  <type 'unicode'>
#python3  :  <type 'str'>

#str = 'X-DSPM-Confidence: 0.8475'
#ipos = str.find(':')
#piece = str[ipos+1:]
#value = float(piece.strip())
#print(value)
# >> 0.8475

# 아래 Quiz6 은 에러 발생함.
# 따라서 정답도 Error가 맞음.
#words = 'Connect Foundation'
#if 'F' in words :
#  words.lower()
#  words[7]='&' >> 이 방식이 구문에서 틀린것으로 추정됨. replace 혹은 다른 방식으로 변경해야만 하는 것으로 보임.
#else : 
#  print(words)
#print(words)