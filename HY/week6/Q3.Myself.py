#Q3. 예금 금리가 너무 낮아서 주식을 시작했습니다. 아래와 같이 매수한 종목 이름, 수량, 매수 평균 금액이 있습니다. 판매가는 따로 주어집니다. 종목과 수익률만 출력하시고 종목별 수익률이 높은 순서대로 출력해주세요. (소수 둘째자리까지 출력)

#stocks = "삼성전자/10/85000,카카오/15/130000,LG화학/3/820000,NAVER/5/420000"
#sells = [82000, 160000, 835000, 410000]

# 소수 둘째자리까지 출력하는 방법
#a = 3.141592
#print(f"{a:.3}")
#3.14

# 출력예시
#stock_profit(stocks, sells)
#카카오의 수익률 23.1
#LG화학의 수익률 1.83
#NAVER의 수익률 -2.38
#삼성전자의 수익률 -3.53

stocks = "삼성전자/10/85000,카카오/15/130000,LG화학/3/820000,NAVER/5/420000"
sells = [82000, 160000, 835000, 410000]

def stocks_profit(stocks, sells) :

  stocksTup = []
  earnRate = []
  stocksSum = 0
  sellsSum = 0

  stocksSplit = stocks.split(',')

  for i in range(len(stocksSplit)) :
    stocksSplit2 = stocksSplit[i].split('/')
    stocksTup.append((stocksSplit2[0], stocksSplit2[1], stocksSplit2[2]))

  for i in range(len(stocksSplit)) :
    earnRate.append((stocksTup[i][0], stocksTup[i][1], float(f"{(sells[i] - int(stocksTup[i][2])) / int(stocksTup[i][2]) * 100 : .3}")))

  earnRate.sort(key = lambda x : x[2], reverse=True)

  for i in range(len(stocksSplit)) :
    print('', earnRate[i][0] + '의 수익률 : ', str(earnRate[i][2]) + '%')

  for i in range(len(stocksTup)) :
    stocksSum = stocksSum + int(stocksTup[i][1])*int(stocksTup[i][2])

  for i in range(len(sells)) :
    sellsSum = sellsSum + int(stocksTup[i][1])*sells[i]

  earnRateSum = str(f"{(sellsSum-stocksSum)/stocksSum*100:.3}" + '%')
  
  earnSum = sellsSum - stocksSum

  print('\n'' 총 매 입:', stocksSum, '\n'' 총 평 가:', sellsSum, '\n'' 총수익금:', earnSum, '\n'' 총수익률:', earnRateSum)

print('보유현황(KRW)''\n')
stocks_profit(stocks, sells)