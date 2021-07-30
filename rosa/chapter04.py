# exec(open("rosa/chapter04.py").read())

# input, print, int 등 기본적으로 사용하능한 사항은 내장함수 (BuiltIn Function)이라 부름.
# 이외 사용자 정의로 사용할경우 아래 문법으로 사용

#def 함수명 (입력변수 , ...) : 
#    실행문
#    return 반환값 (있을경우에만 사용)

def customCalculator (calMode, int1, int2) :
    if   calMode == 'A' : #Add
        return str(int1 + int2)
    elif calMode == 'S' : #Subtract
        return str(int1 - int2)
    elif calMode == 'M' : #Multiply
        return str(int1 * int2)
    elif calMode == 'D' : #Devide
        return str(int1 / int2)
    elif calMode == 'R' : #Reminder 
        return str(int1 % int2)
    else :
        return '계산기 모드 잘못 선택'

aa = 8
bb = 3
print("Add      : " + customCalculator('A', aa, bb))
print("Subtract : " + customCalculator('S', aa, bb))
print("Multiply : " + customCalculator('M', aa, bb))
print("Devide   : " + customCalculator('D', aa, bb))
print("Reminder : " + customCalculator('R', aa, bb))
print("Other    : " + customCalculator('X', aa, bb))