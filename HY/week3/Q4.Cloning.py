##################################################################################
#📌Q4. 2개의 숫자를 입력하여 그 사이에 소수가 몇 개인지 출력하는 함수를 만들어 봅시다.
#소수: 1과 자기 자신만을 약수로 가지는 수
#
#🔽 출력 예시
## 입력
#n = int(input("첫 번째 수 입력 : "))
#m = int(input("두 번째 수 입력 : "))
#count_prime_number(n, m)
#
## 출력
#소수개수  4

print()
print('=================[START] [Q4] 소수 갯수 출력기')


def count_prime_number(n, m):
    if m < n:
        frNum = m
        toNum = n
    else:
        frNum = n
        toNum = m

    numbers = [i for i in range(frNum, toNum + 1)]
    #Q. for 앞에 i가 붙는건 어떤 의미인가요?

    primeNumList = []

    for i in numbers:
        if i < 2:
            continue

        squareRoot = i**(1 / 2) #Q. 주석을 읽어봤는데도 이해가 잘 되지 않습니다...ㅜㅜ

        maxDevideNum = int(squareRoot)

        if maxDevideNum < 2:
            primeNumList += [i]
            continue
        else:
            primeNumBool = True

            for j in range(2, maxDevideNum + 1):
                if i % j == 0:
                    primeNumBool = False
                    break

            if primeNumBool == True:
                primeNumList += [i]

    primeNumOneLine = ''
    for i in range(0, len(primeNumList)): # len=객체의 갯수,길이를 출력 
        primeNumOneLine += str(primeNumList[i])
        if i < (len(primeNumList) - 1):
            primeNumOneLine += ', '
    #Q. 53~57줄까지 해설해주시면 감사하겠습니다.

    print('첫 번째 입력 값 : [ ' + str(n) + ' ]')
    print('두 번째 입력 값 : [ ' + str(m) + ' ]')
    print('검색된 소수의 갯수 : ' + str(len(primeNumList)))
    print('검색된 소수의 목록 : ' + ' [ ' + primeNumOneLine + ' ]')


n = int(input("첫 번째 수 입력(자연수) : "))
m = int(input("두 번째 수 입력(자연수) : "))
count_prime_number(n, m)

print('==================== [E N D] [Q] 소수 개수 출력기')