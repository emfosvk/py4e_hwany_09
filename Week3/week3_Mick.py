# ๐Q1. ์ซ์๋ฅผ ์๋ ฅ ๋ฐ๊ณ  ๊ทธ ์ซ์์ ๊ตฌ๊ตฌ๋จ์ ์ถ๋ ฅํ๋ ํจ์๋ฅผ ๋ง๋ค์ด ๋ด์๋ค. ๋ค๋ง ์๋์ ์กฐ๊ฑด์ ๋ง์กฑํด ์ฃผ์ธ์.
# ์กฐ๊ฑด 1: ํ ์ ๋ฒ์งธ๋ง ์ถ๋ ฅํ๊ธฐ
# ์กฐ๊ฑด 2: ๊ฐ์ด 50์ดํ์ธ ๊ฒ๋ง ์ถ๋ ฅํ๊ธฐ
# ๐ฝ ์ถ๋ ฅ ์์
# # ์๋ ฅ
# number = int(input("๋ช ๋จ? : "))
# gugudan(number)
#
# # ์ถ๋ ฅ
# ๋ช ๋จ? : 8
# 8 ๋จ
# 8 X 1 = 8
# 8 X 3 = 24
# 8 X 5 = 40


def oddGuguMaker (Num):
    result = Num
    i=1
    print('๋ช ๋จ? :', Num)
    print(Num,'๋จ')
    while result <= 50 :
        print(Num,'X',i,'=',result)
        i +=2
        result = Num * i

while 1 :

    inputNum=input('์ซ์๋ฅผ ์๋ ฅํ์ธ์:')
    try :
        inputNum=int(inputNum)
    except :
        inputNum = -1

    if inputNum >0:
        oddGuguMaker(inputNum)
        break
    else:
        print('์๋ ฅ๊ฐ์ 1์ด์์ ์ ์๋ก ์๋ ฅํด์ฃผ์ธ์')

# Q2. ๊ฐ์๋ฐ์๋ณด ์๊ทธ๋ ์ด๋ ๋ฒ์ ผ์ ํจ์ด ๋ด์์๋ก ๋ง๋ค๋ค. ์๋์ ๊ฐ์ ์กฐ๊ฑด์ ๋ง์กฑํด ์ฃผ์ธ์.
# ์กฐ๊ฑด 1: ๊ฒ์์ ๋ช ํ์ ์งํํ  ๊ฒ์ธ์ง ์๋ ฅ์ ๋ฐ์์ฃผ๊ธฐ
# ์กฐ๊ฑด 2: 0, 1, 2, "๊ฐ์", "๋ฐ์", "๋ณด" ์ด์ธ์ ๋ค๋ฅธ ์๋ ฅ์ ๋ฐ์ผ๋ฉด ์ฌ์๋ ฅ ๋ฐ๊ธฐ
# ์กฐ๊ฑด 3: ๊ฒ์์ข๋ฃ ํ ๋์ ์ปดํจํฐ์ ์ด ์ ์  ์ถ๋ ฅํ๊ธฐ
# :์์_์๋์ชฝ_ํ์ดํ: ์ถ๋ ฅ ์์
# # ์๋ ฅ
# games = int(input("๋ช ํ์ ์งํํ์๊ฒ ์ต๋๊น? : "))
# rsp_advanced(games)
# # ์ถ๋ ฅ
# ๊ฐ์ ๋ฐ์ ๋ณด : 0
# ๋: ๊ฐ์
# ์ปดํจํฐ: ๋ณด
# 1 ๋ฒ์งธ ํ ๋์ ์น๋ฆฌ!
# ๊ฐ์ ๋ฐ์ ๋ณด : 1
# ๋: ๋ฐ์
# ์ปดํจํฐ: ๊ฐ์
# 2 ๋ฒ์งธ ํ ๋์ ์น๋ฆฌ!
# ๋์ ์ ์ : 2์น 0๋ฌด 0ํจ
# ์ปดํจํฐ์ ์ ์ : 0์น 0๋ฌด 2ํจ

import random

winCnt= 0
drawCnt =0
loseCnt =0
round = 1
flag = -1

# ์๋ ฅ๋ 0,1,2๋ฅผ ๊ฐ์,๋ฐ์,๋ณด๋ก ๋ณํํ๊ธฐ
def converter(a):
    a = str(a)
    if a == '0':
        return '๊ฐ์'
    elif a == '1':
        return '๋ฐ์'
    elif a == '2':
        return '๋ณด'
    else:
        return a

def winner(player, cpu):  # ์นํจ๊ฐ ๋๋ ๊ฒฝ์ฐ์ ์๋ 6๊ฐ์ง,
    battle = player + cpu
    global winCnt
    global  loseCnt
    if battle == '๊ฐ์๋ฐ์':
        loseCnt +=1
        return '์ปดํจํฐ๊ฐ'
    elif battle == '๊ฐ์๋ณด':
        winCnt +=1
        return '๋น์ ์ด'
    elif battle == '๋ฐ์๋ณด':
        loseCnt += 1
        return '์ปดํจํฐ๊ฐ'
    elif battle == '๋ฐ์๊ฐ์':
        winCnt += 1
        return '๋น์ ์ด'
    elif battle == '๋ณด๊ฐ์':
        loseCnt += 1
        return '์ปดํจํฐ๊ฐ'
    elif battle == '๋ณด๋ฐ์':
        winCnt += 1
        return '๋น์ ์ด'
    else:
        return '๋ง๋ ์๋๋ ์ผ์ด ์ผ์ด๋จ'

print('###########Q1##########')
# player์ cpu์ ๊ฐ์,๋ฐ์,๋ณด ์๋ ฅ๋ฐ๊ธฐ


while not flag > 0 :

    battleCnt = input("๋ช ํ์ ์งํํ์๊ฒ ์ต๋๊น? :")
    try :
        flag = int(battleCnt)
    except :
        flag = -1
    if flag >0:
        break
    else :
        print('๊ฒ์ ํ์๋ ์์ ์ ์๋ก ์๋ ฅํด์ฃผ์ธ์.')

while flag > 0 :
    playerRcp = input('๊ฐ์ ๋ฐ์ ๋ณด!:')  # step1: ๋ด๊ฐ ๊ฐ์, ๋ฐ์, ๋ณด ์ค์ ํ๋๋ฅผ ๋ธ๋ค
    cpuRcp = random.randint(0, 2)  # step2: ์ปดํจํฐ๊ฐ ๊ฐ์, ๋ฐ์, ๋ณด ์ค์ ํ๋๋ฅผ ๋ธ๋ค

    # ์๋ ฅ๋ ๋ด์ฉ์ด '๊ฐ์', '๋ฐ์', '๋ณด', '0', '1', '2' ๊ฐ ์๋๋ฉด, ์ค๋ฅ ๋ฉ์์ง ์ถ๋ ฅ ํ ๋ค์ ์๋ ฅ๋ฐ๊ธฐ
    # step3: ๊ฐ์, ๋ฐ์,๋ณด๊ฐ ์ ๋๋ก ๋ด์ก๋์ง(์๋ ฅ์ด ์ ๋๋ก ๋ค์ด๊ฐ๋์ง ํ์ธํ๋ค)
    rcpList = ['๊ฐ์', '๋ฐ์', '๋ณด', '0', '1', '2']


    if playerRcp in rcpList:  # ์ ์ ํ ๊ฐ์ด ์๋ ฅ๋์์ ๊ฒฝ์ฐ, ์๋ ฅ๊ฐ์ ์ ์ ํ ๋ณํํ๊ณ  player์ cpu๊ฐ ๋ฌด์์ ๋๋์ง ์๋ ค์ค.
        playerRcp = converter(playerRcp)
        cpuRcp = converter(cpuRcp)
        print('Round:', round)
        print('Y O U:', playerRcp)
        print('C P U:', cpuRcp)


        if playerRcp == cpuRcp:  # ๋ฌด์น๋ถ ๋จผ์  ์ฒ๋ฆฌํ๊ธฐ
            print('๋ฌด์น๋ถ')
            drawCnt += 1
        else:  # ๋ฌด์น๋ถ๊ฐ ์๋๋ฉด ์น์ ์ ํด์ฃผ๊ธฐ
            print(winner(playerRcp, cpuRcp), '์ด๊ฒผ์')
        flag -= 1
        round += 1
        print('')

    else:
        print('๊ฐ์,๋ฐ์,๋ณด,0,1,2 ์ค์์ ์๋ ฅํด์ฃผ์ธ์')

print('๋น์ ์ ์ ์ :',winCnt,'์น',drawCnt,'๋ฌด',loseCnt,'ํจ')
print('์ปดํจํฐ์ ์ ์ :',loseCnt,'์น',drawCnt,'๋ฌด',winCnt,'ํจ')

# Q3. 2๊ฐ์ ์ซ์๋ฅผ ์๋ ฅํ์ฌ ๊ทธ ์ฌ์ด์ ์ง์๋ง ์ถ๋ ฅํ๋ ํจ์๋ฅผ ๋ง๋ค์ด ๋ด์๋ค. ๊ทธ๋ฆฌ๊ณ  ์ค์๊ฐ๋ ํจ๊ป ์ถ๋ ฅ ํด๋ด์๋ค.(์ค์๊ฐ์ด ํ์๋ผ๋ฉด ์ ์ธ)
# ์ค์๊ฐ: ์ ์ค์์ ์๋ ๊ฐ
# ํน์  ๋ ์ซ์ ์ฌ์ด์ ์๋ค์ ๋ฆฌ์คํธ๋ก ๋ง๋๋ ๋ฒ
# n = 1
# m = 10
# numbers = [ i for i in range(n,m+1)] # [1,2,3,4,5,6,7,8,9,10]
# # range(์์ ์ซ์, ๋ ์ซ์ + 1)
# ๐ฝ ์ถ๋ ฅ ์์
# # ์๋ ฅ
# n = int(input("์ฒซ ๋ฒ์งธ ์ ์๋ ฅ : "))
# m = int(input("๋ ๋ฒ์งธ ์ ์๋ ฅ : "))
# find_even_number(n, m)
# # ์ถ๋ ฅ
# ์ฒซ ๋ฒ์งธ ์ ์๋ ฅ : 1
# ๋ ๋ฒ์งธ ์ ์๋ ฅ : 11
# 2 ์ง์
# 4 ์ง์
# 6 ์ง์
# 6 ์ค์๊ฐ
# 8 ์ง์
# 10 ์ง์

def evenPrinter (firstNum,secondNum):
    numList = [i for i in range(firstNum,secondNum+1)]

    for i in numList:
        if i == (firstNum + secondNum)/2 and i % 2 ==0 :
            print(i, '์ค์๊ฐ')
        elif i %2 ==0:
            print(i,'์ง์')
            
flag = 1
while flag:
    firstNum = input('์ฒซ ๋ฒ์งธ ์ ์๋ ฅ:')
    secondNum = input('๋ ๋ฒ์งธ ์ ์๋ ฅ:')

    try :
        firstNum = int(firstNum)
        secondNum = int(secondNum)
    except:
        firstNum = -1
        secondNum = -1

    if secondNum-firstNum > 0:
        print('์ฒซ๋ฒ์งธ ์๋ ฅ๊ฐ:',firstNum)
        print('๋๋ฒ์งธ ์๋ ฅ๊ฐ:',secondNum)
        evenPrinter(firstNum,secondNum)
        flag = 0

    else :
        print('0์ด์์ ์ ์๋ฅผ ์๋ ฅํด์ฃผ์ธ์(์ฒซ๋ฒ์งธ ์๋ ฅ๊ฐ์ ๋๋ฒ์งธ ์๋ ฅ๊ฐ๋ณด๋ค ์์์ผ ํฉ๋๋ค)')



#
# ๐Q4. 2๊ฐ์ ์ซ์๋ฅผ ์๋ ฅํ์ฌ ๊ทธ ์ฌ์ด์ ์์๊ฐ ๋ช ๊ฐ์ธ์ง ์ถ๋ ฅํ๋ ํจ์๋ฅผ ๋ง๋ค์ด ๋ด์๋ค.
#
# ์์: 1๊ณผ ์๊ธฐ ์์ ๋ง์ ์ฝ์๋ก ๊ฐ์ง๋ ์
#
# ๐ฝ ์ถ๋ ฅ ์์
#
# # ์๋ ฅ
# n = int(input("์ฒซ ๋ฒ์งธ ์ ์๋ ฅ : "))
# m = int(input("๋ ๋ฒ์งธ ์ ์๋ ฅ : "))
# count_prime_number(n, m)
#
# # ์ถ๋ ฅ
# ์์๊ฐ์  4
import numpy as np

def primeNumCounter (firstNum,secondNum):
    intList=[False,False] + [True]*(secondNum-1)
    primeNum =[]
    primeNumAfter=[]

    for i in range(2,secondNum+1):
        if intList[i]:
            primeNum.append(i)
            for j in range(2*i, secondNum+1,i):
                intList[j] = False
    for k in primeNum:
        if k >= firstNum:
            primeNumAfter.append(k)

    print()
    print('์์๋ชฉ๋ก:',primeNumAfter)
    print('์์๊ฐฏ์:',len(primeNumAfter))

flag = 1
while flag:
    firstNum = input('์ฒซ ๋ฒ์งธ ์ ์๋ ฅ:')
    secondNum = input('๋ ๋ฒ์งธ ์ ์๋ ฅ:')

    try :
        firstNum = int(firstNum)
        secondNum = int(secondNum)
    except:
        firstNum = -1
        secondNum = -1

    if secondNum-firstNum > 0:
        print('์ฒซ๋ฒ์งธ ์๋ ฅ๊ฐ:',firstNum)
        print('๋๋ฒ์งธ ์๋ ฅ๊ฐ:',secondNum)
        primeNumCounter(firstNum,secondNum)

        flag = 0

    else :
        print('0์ด์์ ์ ์๋ฅผ ์๋ ฅํด์ฃผ์ธ์(์ฒซ๋ฒ์งธ ์๋ ฅ๊ฐ์ ๋๋ฒ์งธ ์๋ ฅ๊ฐ๋ณด๋ค ์์์ผ ํฉ๋๋ค)')