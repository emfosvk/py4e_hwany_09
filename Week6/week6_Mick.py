import operator

print('Q2')
print('')

member_names = ["갑돌이", "갑순이", "을돌이", "을순이", "병돌이", "병순이"]
member_records = [[4,5,3,5,6,5,3,4,1,3,4,5],[2,3,4,3,1,2,0,3,2,5,7,2],
           [1,3,0,3,3,4,5,6,7,2,2,1],[3,2,9,2,3,5,6,6,4,6,9,9],
           [8,7,7,5,6,7,5,8,8,6,10,9],[7,8,4,9,5,10,3,3,2,2,1,3]]

def resultChecker(names,records):
    bonusNum = 2
    interviewNum =2
    for i in range(len(records)):
        target=records.pop()
        avg=sum(target)/len(target)
        records.insert(0,avg)

    members={name:record for name,record in zip(names,records)}
    sMembers=sorted(members.items(),key=operator.itemgetter(1),reverse=True)

    for j in range(bonusNum) :
        if sMembers[j][1] > 5:
            print('보너스 대상자',sMembers[j][0])
    print('')

    for k in range(interviewNum):
        if sMembers[len(sMembers) - k -1][1] <= 3:
            print('면담 대상자',sMembers[len(sMembers) - k -1][0])


resultChecker(member_names,member_records)


#Q3
print('')
print('Q3')
print('')


stocks = "삼성전자/10/85000,카카오/15/130000,LG화학/3/820000,NAVER/5/420000"
sells = [82000, 160000, 835000, 410000]
def profitCalculator (stocksL,sellL):
    stocksDict = dict()
    cnt=0

    stocksList=stocks.split(',')

    for item in stocksList:
        stockSep=item.split('/')
        stocksDict[stockSep[0]]=int(stockSep[2])

    for stock in stocksDict:
        profit=((sells[cnt]-stocksDict[stock])/stocksDict[stock])*100
        cnt+=1
        stocksDict[stock]=round(profit,2)

    sStocksDict=sorted(stocksDict.items(),key=operator.itemgetter(1),reverse=True)

    for name,profit in sStocksDict:
        print(name,'의 수익률은 ',profit,sep='')

profitCalculator(stocks,sells)

