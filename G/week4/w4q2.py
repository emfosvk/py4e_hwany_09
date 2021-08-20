def wordCnter(inputText, checkText):
    filePath = "C:/week2lecture/w4q2_text.txt"
    text_save = open(filePath, "w", encoding="UTF8")
    text_save.write(inputText)
    text_save.close()
    print("다음 경로에 파일 저장 완료:", filePath)



    q2hand = open(filePath)
    repeatCnt = 0
    for line in q2hand:
        repeatCnt += line.count(checkText)

    print("Word Count You Find:", repeatCnt)

inputText = '''부스터 여러분들, 4주차 강의는 잘 들으셨나요(1)

학습한 내용을 토대로 풀이하여야 할 4주차 미션 내용을 아래와 같이 공개합니다!

미션 내용을 팀원들과 함께 풀이해주세요(2) 적극적인 토론이 필요(3)합니다'''


checkText = input('찾고 싶은 표현:')
while checkText in inputText:
    wordCnter(inputText, checkText)
    print('해당 표현은',repeatCnt,'번 나왔습니다.')
    break