# Q1. 컴퓨터와 함께하는 가위바위보 게임을 만들어봅시다!
#
# 조건1 : 함수의 인자로는 나의 가위바위보 선택이 들어감
#           (0, 1 ,2 혹은 "가위", "바위", "보" 로 입력할 수 있습니다. - 총 6가지 방법으로 넣을 수 있음)
#
# 조건2 : 누가 무엇을 냈고, 누가 승리 했는지 출력이 되어야 함


# step4: 승패를 확인한다
# step5: 누가 이겼는지, 누가 무엇을 냈는지 출력한다.


import random


# 입력된 0,1,2를 가위,바위,보로 변환하기
def converter(a):
    a = str(a)
    if a == '0':
        return '가위'
    elif a == '1':
        return '바위'
    elif a == '2':
        return '보'
    else:
        return a


def winner(player, cpu):  # 승패가 나는 경우의 수는 6가지,
    battle = player + cpu
    if battle == '가위바위':
        return '컴퓨터가'
    elif battle == '가위보':
        return '당신이'
    elif battle == '바위보':
        return '컴퓨터가'
    elif battle == '바위가위':
        return '당신이'
    elif battle == '보가위':
        return '컴퓨터가'
    elif battle == '보바위':
        return '당신이'
    else:
        return '말도 안되는 일이 일어남'


print('###########Q1##########')
# player와 cpu의 가위,바위,보 입력받기
while True:
    playerRcp = input('가위 바위 보!:')  # step1: 내가 가위, 바위, 보 중에 하나를 낸다
    cpuRcp = random.randint(0, 2)  # step2: 컴퓨터가 가위, 바위, 보 중에 하나를 낸다

    # 입력된 내용이 '가위', '바위', '보', '0', '1', '2' 가 아니면, 오류 메시지 출력 후 다시 입력받기
    # step3: 가위, 바위,보가 제대로 내졌는지(입력이 제대로 들어갔는지 확인한다)
    rcpList = ['가위', '바위', '보', '0', '1', '2']
    flag = 1

    if playerRcp in rcpList:  # 적절한 값이 입력되었을 경우, 입력값을 적절히 변환하고 player와 cpu가 무엇을 냈는지 알려줌.
        playerRcp = converter(playerRcp)
        cpuRcp = converter(cpuRcp)
        print('Y O U:', playerRcp)
        print('C P U:', cpuRcp)

        if playerRcp == cpuRcp:  # 무승부 먼저 처리하기
            print('무승부')
        else:  # 무승부가 아니면 승자 정해주기
            print(winner(playerRcp, cpuRcp), '이겼음')
            break
    else:
        print('invalid value input')

# Q2. 월급을 입력하면 연봉을 계산해주는 계산기를 만들어 봅시다. 세전 연봉과 세후 연봉을 함께 출력하도록 해봅니다.
# 1200만원 이하 6%, 4600만원 이하 15%, 8800만원 이하 24%, 1억 5천만원 이하 35%, 3억원 이하 38%, 5억원 이하 40%, 5억원 초가 42%
print('###########Q2##########')

taxBase=[1200,  4600,  8800,  15000,  30000,  50000]
taxRate=[0.06,  0.15,  0.24,   0.35,   0.38,    0.40,  0.42]

def taxChecker(annualIncome):
    if annualIncome <= taxBase[0]:
        return 0.06
    elif annualIncome <= taxBase[1]:
        return 0.15
    elif annualIncome <= taxBase[2]:
        return 0.24
    elif annualIncome <= taxBase[3]:
        return 0.35
    elif annualIncome <= taxBase[4]:
        return 0.38
    elif annualIncome <= taxBase[5]:
        return 0.4
    else:
        return 0.42

def progressiveDeduction(annualIncome):
    progressiveDeduction = 0

    if annualIncome <= taxBase[0]:
        x=0
    elif annualIncome <= taxBase[1]:
        x=1
    elif annualIncome <= taxBase[2]:
        x=2
    elif annualIncome <= taxBase[3]:
        x=3
    elif annualIncome <= taxBase[4]:
        x=4
    elif annualIncome <= taxBase[5]:
        x=5
    else:
        x=6

    for i in range(0,x):
        progressiveDeduction = progressiveDeduction + taxBase[i]*(taxRate[i+1]-taxRate[i])

    return progressiveDeduction


flag = 1
while flag:
    salary = input('월급(만원):')
    try:
        salary = float(salary)
    except:
        salary = -1

    if salary > 0:

        annualIncome = 12 * salary
        incomeAfterTax = round((1 - taxChecker(annualIncome)) * annualIncome,2)


        print('세전:', annualIncome, '만원')
        print('포괄제 적용시 세후:',incomeAfterTax, '만원')
        print('누진제 적용시 세후:',round((incomeAfterTax+progressiveDeduction(annualIncome)),2),'만원')
        print('세율:', int(taxChecker(annualIncome) * 100), '%')
        flag = 0
    else:
        print('invalid input value')
# Q3. 학생 이름과 점수를 입력하면 학점을 출력하는 학점 변환기를 만들어 봅시다.
#
# 이름과 점수, 학점 모두 출력하도록 해봅니다.

print('###########Q3##########')


def grader(score):
    if score >= 95:
        return 'A+'
    elif score >= 90:
        return 'A'
    elif score >= 85:
        return 'B+'
    elif score >= 80:
        return 'B'
    elif score >= 75:
        return 'C+'
    elif score >= 70:
        return 'C'
    elif score >= 65:
        return 'D+'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


while True:

    nameScore = input('이름과 점수를 입력하세요:').split()

    name = nameScore[0]

    try:
        score = int(nameScore[1])
    except:
        score = -1

    if score > 0:

        print('학생이름:', name)
        print('점수:', score, '점')
        print('학점:', grader(score))
        break
    else:
        print('invalid value error')

# Q4. 나이와 현금 또는 카드를 입력하면 버스 요금이 출력되는 버스 요금 계산기를 만들어봅시다.

print('###########Q4##########')


def feeChecker(age, method):
    if age < 8 or age >= 75:
        return '무료입니다.'
    elif age < 14:
        return '450'
    elif age < 20 and method == '카드':
        return '720'
    elif age < 20 and method == '현금':
        return '1000'
    elif age < 75 and method == '카드':
        return '1200'
    elif age < 75 and method == '현금':
        return '1300'


while 1:
    ageMethod = input('나이와 지불 방법을 알려주세요(현금/카드)').split()  # 입력값이 3개이면?
    try:
        age = int(ageMethod[0])
        method = str(ageMethod[1])
    except:
        age = -1
        method = -1

    if age > 0 and method in ['카드', '현금']:
        print('나이:', age, '세')
        print('지불유형:', method)
        print('버스요금:', feeChecker(age, method))

        break
    else:
        print('invalid value error')