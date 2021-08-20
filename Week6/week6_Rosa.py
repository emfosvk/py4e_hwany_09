#📌Q1. 역사 문제를 하나 내보겠습니다. 고려시대와 조선시대 왕 이름 중에서 고려에도 있고 조선에도 있는 이름은 몇개 일까요? 한 번에 딱 안 떠오른다면 왕 이름을 드릴테니 파이썬 함수로 만들어서 출력 해봅시다.
#
#😲조건1 - 중복되는 왕 이름 출력
#😲조건2 - 중복되는 왕 이름의 수 출력

## 왕이름
#korea_king = "태조,혜종,정종,광종,경종,성종,목종,현종,덕종,정종,문종,순종,선종,헌종,숙종,예종,인종,의종,명종,신종,희종,강종,고종,원조,충렬왕,충선왕,충숙왕,충혜왕,충목왕,충정왕,공민왕,우왕,창왕,공양왕"
#chosun_king = "태조,정종,태종,세종,문종,단종,세조,예종,성종,연산군,중종,인종,명종,선조,광해군,인조,효종,현종,숙종,경종,영조,정조,순조,헌종,철종,고종,순종"

#✅출력 예시
#king(korea_king, chosun_king)
#조선과 고려에 모두 있는 왕 이름 : 태조
#조선과 고려에 모두 있는 왕 이름 : 정종
#조선과 고려에 모두 있는 왕 이름 : 경종
#조선과 고려에 모두 있는 왕 이름 : 성종
#조선과 고려에 모두 있는 왕 이름 : 현종
#조선과 고려에 모두 있는 왕 이름 : 문종
#조선과 고려에 모두 있는 왕 이름 : 순종
#조선과 고려에 모두 있는 왕 이름 : 헌종
#조선과 고려에 모두 있는 왕 이름 : 정종
#조선과 고려에 모두 있는 왕 이름 : 숙종
#조선과 고려에 모두 있는 왕 이름 : 예종
#조선과 고려에 모두 있는 왕 이름 : 인종
#조선과 고려에 모두 있는 왕 이름 : 명종
#조선과 고려에 모두 있는 왕 이름 : 고종
#조선과 고려에 모두 있는 왕 이름은 총 13개 입니다

print('====================== [START] [Q1] 조선왕 중복 이름 찾기 ')

def duplKings(korea_king, chosun_king) :

    koreaKingList = korea_king.split(',')
    chosunKingList = chosun_king.split(',')
    duplKings = []

    for koreaKing in koreaKingList :
        # 고려와 조선왕 비교 동시에, 이미 나온 결과에 중복되는 값이 있는지 체크
        if koreaKing in chosunKingList and koreaKing not in duplKings :
            # 없으면 값 추가
            duplKings.append(koreaKing)

    for duplKing in duplKings :
        print('조선과 고려에 모두있는 왕 : ', duplKing)
    
    print('조선과 고려에 모두 있는 왕 이름은 총', len(duplKings), '개 입니다.')


korea_king = "태조,혜종,정종,광종,경종,성종,목종,현종,덕종,정종,문종,순종,선종,헌종,숙종,예종,인종,의종,명종,신종,희종,강종,고종,원조,충렬왕,충선왕,충숙왕,충혜왕,충목왕,충정왕,공민왕,우왕,창왕,공양왕"
chosun_king = "태조,정종,태종,세종,문종,단종,세조,예종,성종,연산군,중종,인종,명종,선조,광해군,인조,효종,현종,숙종,경종,영조,정조,순조,헌종,철종,고종,순종"

duplKings(korea_king, chosun_king)

print('====================== [E N D] [Q1] 조선왕 중복 이름 찾기 ')


#📌Q2.  여러분은 6명의 멤버를 거느리는 영업팀의 영업관리자 입니다. 각 멤버별로 올해 실적을 보고 잘한 멤버는 보너스를 주고 못한 멤버는 면담을 하려고 합니다. 파이썬을 이용하여 함수를 만들어 보너스 대상자와 면담 대상자를 골라주세요.
#
#😲조건 1 - 예비 보너스 대상자는 평균 실적 1등 2등 입니다.
#😲조건 2 - 예비 면담 대상자는 평균 실적 5등 6등 입니다.
#😲조건 3 - 보너스 대상자의 평균 실적이 5보다 크지 않으면 보너스 대상자에서 제외 됩니다.
#😲조건 4 - 면담 대상자의 평균 실적이 3보다 크면 면담 대상자에서 제외 됩니다.
## 이름, 실적
#member_names = ["갑돌이", "갑순이", "을돌이", "을순이", "병돌이", "병순이"]
#member_records = [[4,5,3,5,6,5,3,4,1,3,4,5],[2,3,4,3,1,2,0,3,2,5,7,2], 
#           [1,3,0,3,3,4,5,6,7,2,2,1],[3,2,9,2,3,5,6,6,4,6,9,9],
#           [8,7,7,5,6,7,5,8,8,6,10,9],[7,8,4,9,5,10,3,3,2,2,1,3]]
#✅출력 예시
#sales_management(member_names, member_records)
#보너스 대상자 병돌이
#보너스 대상자 을순이
#
#면담 대상자 갑순이

print('====================== [START] [Q2] 실적 계산기 - 포상/면담 대상 추출 ')

def sales_management(member_names, member_records) :
    
    # 1, 2등 면담이므로 2명
    rewardCnt = 2

    # 5, 6등 면담이므로 2명
    interviewCnt = 2

    membResult = []

    for i in range(len(member_names)) :
        score = 0
        for j in member_records[i] :
            score = score + j

        scoreAvg = round(score / len(member_records[i]), 2)

        membResult.append((scoreAvg, member_names[i]))
    
    membResult = sorted(membResult, reverse=True)
    
    #채점결과
    print('채첨 결과 : ', membResult)

    #포상 대상 추출
    for i in range(rewardCnt) :
        (result, name) = membResult[i]
        print('보너스 대상자 :', name, '/ 평균실적 :', result)

    #포상 대상 추출
    for i in range(len(membResult) - interviewCnt, len(membResult)) :
        (result, name) = membResult[i]
        print('면  담 대상자 :', name, '/ 평균실적 :', result)


member_names = ["갑돌이", "갑순이", "을돌이", "을순이", "병돌이", "병순이"]
member_records = [[4,5,3,5,6,5,3,4,1,3,4,5],[2,3,4,3,1,2,0,3,2,5,7,2], 
           [1,3,0,3,3,4,5,6,7,2,2,1],[3,2,9,2,3,5,6,6,4,6,9,9],
           [8,7,7,5,6,7,5,8,8,6,10,9],[7,8,4,9,5,10,3,3,2,2,1,3]]

sales_management(member_names, member_records)

print('====================== [E N D] [Q2] 실적 계산기 - 포상/면담 대상 추출 ')


#📌Q3. 예금 금리가 너무 낮아서 주식을 시작했습니다. 아래와 같이 매수한 종목 이름, 수량, 매수 평균 금액이 있습니다. 판매가는 따로 주어집니다. 종목과 수익률만 출력하시고 종목별 수익률이 높은 순서대로 출력해주세요. (소수 둘째자리까지 출력)
#
#stocks = "삼성전자/10/85000,카카오/15/130000,LG화학/3/820000,NAVER/5/420000"
#sells = [82000, 160000, 835000, 410000]
## 소수 둘째자리까지 출력하는 방법
#a = 3.141592
#print(f"{a:.3}")
#3.14
#✅출력 예시
#stock_profit(stocks, sells)
#카카오의 수익률 23.1
#LG화학의 수익률 1.83
#NAVER의 수익률 -2.38
#삼성전자의 수익률 -3.53

print('====================== [START] [Q3] 주식 수익률 계산기 ')

def stock_profit(stocks, sells) :
    returnRates = []

    stockList = stocks.split(',')

    for i in range(len(stockList)) : 
        splitTmp = stockList[i].split('/')
        resultRate = round( sells[i] / int(splitTmp[2]) * 100 - 100, 2)
        returnRates.append((resultRate, splitTmp[0]))
    
    returnRates = sorted(returnRates, reverse=True)

    for v,k in returnRates :
        print(k, '의 수익률 : ', v, '%')


stocks = "삼성전자/10/85000,카카오/15/130000,LG화학/3/820000,NAVER/5/420000"
sells = [82000, 160000, 835000, 410000]
stock_profit(stocks, sells)

print('====================== [E N D] [Q3] 주식 수익률 계산기 ')


#📌Q4. 여러분은 어떤 상품을 판매하고 있습니다. 매월 상품을 많이 구매해준 VIP회원에게 할인 쿠폰을 제공해주려고 합니다. 아래와 같은 회원 정보가 있을 때 회원 정보를 출력하고 할인 쿠폰을 받을 회원이 누구인지 출력하는 함수를 만들어 주세요.
#
#😲조건1 - 8회 이상 구매한 회원이 VIP대상
#😲조건2 - 전화번호가 없으면 쿠폰을 받을 수 없음
#😲조건3 - 전화번호가 없으면 000-0000-0000으로 출력할 것
#
## 6명의 회원이고 "아이디,나이,전화번호,성별,지역,구매횟수" 순서로 입력되어 있음
#info = "abc,21세,010-1234-5678,남자,서울,5,cdb,25세,x,남자,서울,4,bbc,30세,010-2222-3333,여자,서울,3,ccb,29세,x,여자,경기,9,dab,26세,x,남자,인천,8,aab,23세,010-3333-1111,여자,경기,10"
#✅출력 예시
#good_customer(info)
#{'아이디': ['abc', 'cdb', 'bbc', 'ccb', 'dab', 'aab'], '나이': ['21세', '25세', '30세', '29세', '26세', '23세'], '전화번호': ['010-1234-5678', '000-0000-0000', '010-2222-3333', '000-0000-0000', '000-0000-0000', '010-3333-1111'], '성별': ['남자', '남자', '여자', '여자', '남자', '여자'], '지역': ['서울', '서울', '서울', '경기', '인천', '경기'], '구매횟수': [5, 4, 3, 9, 8, 10]}
#할인 쿠폰을 받을 회원정보 아이디:aab, 나이:23세, 전화번호:010-3333-1111, 성별:여자, 지역:경기, 구매횟수: 10

print('====================== [START] [Q4] VIP 쿠폰 지급 대상 추출 ')

def getCponSendVipList (info) :
    #list Dict로 우선 변환
    keyNames = ['아이디', '나이', '전화번호', '성별', '지역', '구매회수']
    splitTxt = info.split(',')
    defaultTelNum = '000-0000-0000'
    minVipPurCnt = 8
    lenKey = len(keyNames)
    custmInfoList = list()

    for i in range(lenKey) :
        custmInfos = dict()
        j = 0
        for key in keyNames :
            value = splitTxt[i * lenKey + j]

            #조건 2의 값이 없을 경우 000-0000-0000으로 삽입하라는 멘트에 집어넣은 조건.
            if key == '전화번호' and value in [None, '', 'x', 'X'] :
                value = defaultTelNum
            
            custmInfos[key] = value

            j += 1

        custmInfoList.append(custmInfos)

    #print()
    #print('list(dictionaty) : ', custmInfoList)
    
    #사실 이미 dict에서 꺼내서 체크해도되지만
    #그렇게하면 tuple은 별로 사용하지 못하므로 일부러 한번더 전환......
    #형태상으로는 list[list[tuples(key,value), ...], ...]
    custmInfoListTuples = []
    for infos in custmInfoList :
        infosTupleList = []
        for key, value in infos.items():
            infosTupleList.append((key, value))
        custmInfoListTuples.append(infosTupleList)

    #print()
    #print('list(list(tuple)) : ', custmInfoListTuples)
    
    # 회원 리스트 출력
    # 예제의 방식으로 변경후 출력
    # 위에서 언급한대로, 이런 로직은 사실 불필요함. 공부를 위해 형태를 바꾸는 것임.
    # {key : list[?,?,....] , key : list[?,?,....], ....}
    print('=================== 전체 회원 목록 ===================')
    custmInfoDict = dict()
    for i in range(len(keyNames)) :
        newInfos = []
        for userinfo in custmInfoListTuples :
            newInfos.append(userinfo[i][1])

        custmInfoDict[keyNames[i]] = newInfos

    print(custmInfoDict)


    #마지막에 만든 튜플 형태의 데이터를 토대로 계산
    cponSendCustmList = []
    for infos in custmInfoListTuples :
        #print(infos)
        #조건1 - VIP 는 구매회수가 8회 이상인 사람.
        if minVipPurCnt > int(infos[keyNames.index('구매회수')][1]) :
            #print('구매회수 부족', int(infos[keyNames.index('구매회수')][1]))
            continue

        #조건3 - 전화번호 없으면 쿠폰 못받음.
        #위에서 이미 010-0000-0000으로 그 값을 변경,저장하였으므로 해당 값인지만 체크하면됨.
        if defaultTelNum == infos[keyNames.index('전화번호')][1] :
            #print('전화번호 누락', infos[keyNames.index('전화번호')][1])
            continue
        cponSendCustmList.append(infos)

    #print()
    #print('VIP List : ', cponSendCustmList)
    
    print('=================== 할인 쿠폰 받을 회원 ===================')
    for infos in cponSendCustmList :
        print(convertTupleListToText(infos))
    
    #당첨자 리스트 출력
    
def convertTupleListToText(tupleList) :
    rtnStr = ''
    for i in range(len(tupleList)) :
        info = tupleList[i]
        rtnStr += info[0] + ' : ' + info[1]
        if i < len(tupleList) - 1 :
            rtnStr += ', '
    
    return rtnStr


info = "abc,21세,010-1234-5678,남자,서울,5,cdb,25세,x,남자,서울,4,bbc,30세,010-2222-3333,여자,서울,3,ccb,29세,x,여자,경기,9,dab,26세,x,남자,인천,8,aab,23세,010-3333-1111,여자,경기,10"

getCponSendVipList(info)

print('====================== [E N D] [Q4] VIP 쿠폰 지급 대상 추출 ')