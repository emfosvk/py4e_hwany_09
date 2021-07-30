#step 1. '나이를 입력하세요' 메시지 띄우기
#step 2. 연령별 지불수단별 버스요금 파악 및 설정하기
#step 3. 연령과 지불수단에 알맞은 메시지 띄우기
#★★★★ 버스요금이 무료인 연령구간의 나이를 입력한 경우 지불수단을 묻지 않고 바로 '무료' 메시지를 띄워야 함
#★★★★ 나이를 음수나 문자로 입력하거나 지불수단을 숫자나 '카드'나 '현금' 외의 문자로 입력한 경우 잘못 입력했다는 메시지를 띄워야함

age = input('나이를 입력하세요.')
ageint = int(age)

if ageint < 8 and ageint >= 0:
    print('나이:', ageint, '세')
    print('버스요금: 무료')
elif ageint >= 75:
    print('나이:', ageint, '세')
    print('버스요금: 무료')
else:
    print('올바른 숫자를 입력하세요.')

if ageint >= 8 and ageint < 75:
    CC = input('지불 수단을 입력하세요(카드/현금).')
    CCstr = str(CC)

    if ageint >= 8 and ageint < 14 and CCstr == '카드':
        print('나이:', ageint, '세')
        print('지불유형:', '카드')
        print('버스요금:', '450원')
    elif ageint >= 8 and ageint < 14 and CCstr == '현금':
        print('나이:', ageint, '세')
        print('지불유형:', '현금')
        print('버스요금:', '450원')
    elif ageint >= 14 and ageint < 20 and CCstr == '카드':
        print('나이:', ageint, '세')
        print('지불유형:', '카드')
        print('버스요금:', '720원')
    elif ageint >= 14 and ageint < 20 and CCstr == '현금':
        print('나이:', ageint, '세')
        print('지불유형:', '현금')
        print('버스요금:', '1000원')
    elif ageint >= 20 and ageint < 75 and CCstr == '카드':
        print('나이:', ageint, '세')
        print('지불유형:', '카드')
        print('버스요금:', '1200원')
    elif ageint >= 20 and ageint < 75 and CCstr == '현금':
        print('나이:', ageint, '세')
        print('지불유형:', '현금')
        print('버스요금:', '1300원')
    else:
        print('"카드", "현금" 중에서 입력하세요.')

#최초에 '나이를 입력하세요.'에서 숫자가 아닌 문자를 입력하면 유효하지 않은 문자라는 ValueError가 뜹니다.
# 9~10열에서 else를 활용해서 문자를 입력했을때 '숫자를 입력하세요' 라는 메시지를 출력하려고 했는데 잘 안되네요. 어떤 문제가 있는걸까요?
#잘못 입력하면 프로그램이 그대로 끝나버리는데, 다시 입력 메시지를 띄우려면 어떻게 해야 하나요?
