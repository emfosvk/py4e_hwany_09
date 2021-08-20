# 09 - 1
#Dictionary > Java의 Hash Map 처럼 Key : Value의 한쌍으로 이루어진 collection의 일종

ddd = dict() # dict() 는 {} 라는 표현식으로 생략해서 사용해도 가능하다.
ddd['age'] = 21
ddd['cource'] = 182
print(ddd)
# > {'cource':182, 'age':21}
ddd['age'] = 23
print(ddd)
# > {'cource':182, 'age':23}

jjj = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
print(jjj)
# > {'chuck' : 1, 'fred' : 42, 'jan' : 100}

ooo = { }
print(ooo)
# > {}

# 09 - 2
ccc = dict()
#print(ccc['someKeyValue'])
# > valueError 발생함 해당 키를 찾지 못했으므로 에러 발생.
print('someKeyValue' in ccc)
# > False

cnts = dict()
names = ['aaa', 'bbb', 'ccc', 'aaa', 'ddd']

for name in names :
    if name not in cnts :
        cnts[name] = 1
    else :
        cnts[name] = cnts[name] + 1

print(cnts)

name = 'aaa'
if name in cnts :
    x = cnts[name]
else :
    x = 0

print(x)

# 위 로직을 줄이면 다음과 같이 표현이 가능하다.
# .get(Key Name, Default Value)
x = cnts.get(name, 0)
print(x)
#이를 활용하면 위의 이름반복수 구하는 로직을 다음과 같이 수정 가능하다.
print(x)

cnts = dict()

for name in names :
        cnts[name] = cnts.get(name, 0) + 1

print(cnts)


#.items() duple 로 각각 꺼내오는 것이 가능
for (key, value) in cnts.items() :
    print('전통방식 루프 : ', key, cnts[key])
    print('duple을 사용한 루프 : ', key, value)