#파일의 내용을 읽기 전에 파이썬에게 작업할 파일과
#파일로 어떤 작업을 할지 알려줘야 함
#• open() 함수가 해당 기능을 수행함
#• open()이 “파일 핸들”을 반환 - 파일에 대한 작업을 수행하기 위해
#사용하는 변수
#• 워드 프로세서에서 “File -> Open” 과 비슷함

# 문법
# 핸들 = open(파일명, 모드)
# 모드 > r = 읽기 / w = 쓰기
fhand = open('readingTestFile.txt', 'r') # 읽기모드
print(fhand)
#<_io.TextIOWrapper name='readingTestFile.txt' mode='r' encoding='UTF-8'>

# 개행문자
# 해당 Line이 끝났다는 것을 알리는 글자 표기상으로는 \n 사용
# \n은 우리가 봤을때는 2글자 이지만, len 함수 상에서는 1글자로 처리함.

#아래의 형태로된 txt 파일이 존재할때,
#Subject: [sakai] svn commit: r39772 - content/branches/
#
#Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39772

# 실제로는 다음과같이 저장되어있음
#Subject: [sakai] svn commit: r39772 - content/branches/\n
#\n
#Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39772\n

#위 핸들은 각줄의 문자열에 대한 시퀀스라고 보면됨.

#라인수 체크.
fhand = open('readingTestFile.txt')
count = 0
for line in fhand:
    #print(type(line))
    #<class 'str'>
    count = count + 1
print('Line Count:', count)

# 파일 전체를 하나의 문자열로 읽기
#read()
fhand = open('readingTestFile.txt')
inp = fhand.read()
print(len(inp))

#파일 내용 탐색
#시작문구 찾기
fhand = open('readingTestFile.txt')
for line in fhand :
    # 아래 rstrip이 없으면 각 라인의 개행문자가 한칸을 더 띄어버림.
    # \n을 공백제거 함수로 제거처리.
    # rstrip : 우측 / lstrip : 좌측 / strip : 양쪽
    line = line.rstrip()    
    if line.startswith('From:') :
        print(line)

print('\n특정문자 검색')

fhand = open('readingTestFile.txt')    
for line in fhand :
    line = line.rstrip()
    if not '@uct.ac.za' in line :
        continue
    print(line)
