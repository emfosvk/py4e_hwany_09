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
def primeNum(n, m) :
  if n > m :
    frNum = m
    ToNum = n
  else : 
    frNum = n
    ToNum = m

## frNumκ³Ό ToNumμ intλ‘ λ³νν΄μ£Όμ§ μμλ range() μμμλ μ μλ‘ μΈμνλκ±΄κ°μ?

  Num_List = [i for i in range(frNum, ToNum+1)]
  PrimeNum_List = []

  for i in Num_List :
    if i < 2 :
      print('2 μ΄μμ μμ°μκ° μλλλ€.')
      continue
    
    Check = True

    for j in range(2, i) :
      if i%j == 0 :
        Check = False
        continue
    
    if Check == True :
      PrimeNum_List += [i]

  print('μμ λͺ©λ‘ : ', str(PrimeNum_List))
  print('μμ κ°μ :', len(PrimeNum_List), 'κ°')

print('λ κ°μ μμ°μ μ¬μ΄μ μ‘΄μ¬νλ μμλ₯Ό μ°Ύμλ΄μλ€!!')
n = int(input('2 μ΄μμ μμ°μλ₯Ό μλ ₯νμΈμ.'))
m = int(input('2 μ΄μμ μμ°μλ₯Ό μλ ₯νμΈμ.'))
primeNum(n, m)