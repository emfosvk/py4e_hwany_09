##################################################################################
#πQ4. 2κ°μ μ«μλ₯Ό μλ ₯νμ¬ κ·Έ μ¬μ΄μ μμκ° λͺ κ°μΈμ§ μΆλ ₯νλ ν¨μλ₯Ό λ§λ€μ΄ λ΄μλ€.
#μμ: 1κ³Ό μκΈ° μμ λ§μ μ½μλ‘ κ°μ§λ μ
#
#π½ μΆλ ₯ μμ
## μλ ₯
#n = int(input("μ²« λ²μ§Έ μ μλ ₯ : "))
#m = int(input("λ λ²μ§Έ μ μλ ₯ : "))
#count_prime_number(n, m)
#
## μΆλ ₯
#μμκ°μ  4

print()
print('=================[START] [Q4] μμ κ°―μ μΆλ ₯κΈ°')


def count_prime_number(n, m):
    if m < n:
        frNum = m
        toNum = n
    else:
        frNum = n
        toNum = m

    numbers = [i for i in range(frNum, toNum + 1)]
    #Q. for μμ iκ° λΆλκ±΄ μ΄λ€ μλ―ΈμΈκ°μ?

    primeNumList = []

    for i in numbers:
        if i < 2:
            continue

        squareRoot = i**(1 / 2) #Q. μ£Όμμ μ½μ΄λ΄€λλ°λ μ΄ν΄κ° μ λμ§ μμ΅λλ€...γγ

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
    for i in range(0, len(primeNumList)): # len=κ°μ²΄μ κ°―μ,κΈΈμ΄λ₯Ό μΆλ ₯ 
        primeNumOneLine += str(primeNumList[i])
        if i < (len(primeNumList) - 1):
            primeNumOneLine += ', '
    #Q. 53~57μ€κΉμ§ ν΄μ€ν΄μ£Όμλ©΄ κ°μ¬νκ² μ΅λλ€.

    print('μ²« λ²μ§Έ μλ ₯ κ° : [ ' + str(n) + ' ]')
    print('λ λ²μ§Έ μλ ₯ κ° : [ ' + str(m) + ' ]')
    print('κ²μλ μμμ κ°―μ : ' + str(len(primeNumList)))
    print('κ²μλ μμμ λͺ©λ‘ : ' + ' [ ' + primeNumOneLine + ' ]')


n = int(input("μ²« λ²μ§Έ μ μλ ₯(μμ°μ) : "))
m = int(input("λ λ²μ§Έ μ μλ ₯(μμ°μ) : "))
count_prime_number(n, m)

print('==================== [E N D] [Q] μμ κ°μ μΆλ ₯κΈ°')