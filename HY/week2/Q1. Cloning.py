# Q1. 컴퓨터와 함께하는 가위바위보 게임을 만들어봅시다!
#조건1 : 함수의 인자로는 나의 가위바위보 조건이들어감(0, 1, 2 혹은 "가위", "바위", "보")로 입력할 수 있습니다. = 총 6가지 방법 가능
#조건2 : 누가 무엇을 냈고, 누가 승리 했는지 출력되어야 함

import random
#입력된 0, 1, 2를 가위, 바위, 보로 변환하기
def converter(a) :
    a = str(a)
    if a =='0' :
        return '가위'
    elif a =='1':
        return '바위'
    elif a == '2':
        return '보'
    else:
        return a

# Q. 마지막 "else : return a"의 의도가 궁금합니다. 
# Q. 들여쓰기를 두 번 하신 건 가독성 때문인지, 아니면 기능적 이유 때문인지 궁금합니다.


def winner(player, cpu): 
    battle = player + cpu
    if battle == '가위바위':
        return '컴퓨터가'
    elif battle == '가위보':
        return '당신이'
    elif battle == '바위보':
        return '컴퓨터가'
    elif battle == '바위가위':
        return '당신이'
    elif battle =='보가위' : 
        return '컴퓨터가'
    elif battle =='보바위' :
        return '당신이'
    else:
        return '말도 안되는 일이 일어남'


while True :
    playerRcp = input('가위 바위 보!:')
    cpuRcp = random.randint(0, 2)
    rcpList = ['가위', '바위', '보', '0', '1', '2']
    

    if playerRcp in rcpList: 
        playerRcp = converter(playerRcp)
        cpuRcp = converter(cpuRcp)
        print('Y O U:', playerRcp)
        print('C P U', cpuRcp)

        if playerRcp == cpuRcp:
          print('무승부')
        else:
          print(winner(playerRcp, cpuRcp), '이겼음')
          flag = 0
          break #Q: 요건 어떤 의도인지 알고싶습니다.
    else:
        print('invalidvalue input')
        
