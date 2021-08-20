#tuple 10-1
#List와 유사하지만, 한번 선언이되면 순서, 값 모두 변경 불가능.
#List와 다르게 설정한 이유는 해당 데이터를 조회하는 속도로 인함.

#선언 방법
#list와 다르게 () 소괄호를 사용한다.
tp1 = (4, 'Fred')
print(tp1)
# > (4, 'Fred')

#좌변에 함수명들을 집어넣어 일괄적으로 삽입하는 기능이 존재 (Python 기능)
(x, y) = (4, 'Fred')
print(x)
# > 4
print(y)
# > Fred


#duple간 비교 가능 (숫자, 문자열 모두 가능)
(0, 1, 2) < (5, 1, 2)
# > True

(0, 1, 2) < (0, 3, 2)
# > True

#tuple 10-2
# Sort( tuples, Options )
# Option > reverse = True
tp1 = {'a' : 1, 'c': 2, 'b' : 3}
print(tp1.items())
# > dict_items([('a', 1), ('c', 2), ('b', 3)])

print(sorted(tp1.items()))
# > [('a', 1), ('b', 3), ('c', 2)]

print(sorted(tp1.items(), reverse=True))
# > [('c', 2), ('b', 3), ('a', 1)]

#만약 다른순서로의 정렬이 필요하다면 새로 생성해야함.
tp2 = {'a' : 15, 'c': 2, 'b' : 300}
tmp = list()
for k, v in tp2.items() :
    tmp.append( (v, k) )
print(tmp)

tmp = sorted(tmp, reverse=True)
print(tmp)

# 바로위의 짧은 로직은 다음과같이 줄일수 있다.
print( sorted( [(v,k) for k, v in tp2.items()], reverse=True ) )