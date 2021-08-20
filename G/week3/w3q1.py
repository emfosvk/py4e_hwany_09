#몇단을 입력할 것인지 묻는다
#입력 값을 수로 정의한다.
#반복문을 통해서 순차적으로 곱셈이 나타나는데 홀수만 곱하도록 설정
#그 값이 50이하인지 체크하기

print('Gugudan')
numStr = input('구구단을 외자, 몇 단?:')
numInt = int (numStr)
print(numInt,'단')
i = 1

while result < 50:
    result = numInt * i
    numInt * i
    print('numInt','x','i','=','result')
    i = i + 2


