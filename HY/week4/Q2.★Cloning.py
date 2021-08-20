#Q2. 어느날 여러분이 어떤 글을 읽고 있는데, 갑자기 특정 글자가 전체 글에서 몇개 들어있는지 궁금해졌습니다. 그럼 한 번 파이썬 함수로 만들어 봅시다.
#글은 어떤 글이 좋습니다. 인터넷에서 검색해서 복사 붙여넣기로 변수에 넣어 줍니다.

#변수에 담긴 글을 함수에 넣어주면 txt 파일로 저장도 함께 되도록 해줍니다.
#출력 예시
#a ="""안녕하세요. 
#반갑습니다. 파이썬 공부는 정말 재밌습니다.
#"""

#count_word(a, "습니다")
#2

def countWord(inputText, checkText) :

  filePath = "/Users/hyeonyeongkim/Desktop/python/text.txt"

  text_save = open(filePath, "w", encoding="UTF8")
  text_save.write(inputText)
  text_save.close()

  print("다음 경로에 파일 저장 완료: ", filePath )

  q2hand = open(filePath)

  repeatCnt = 0
  includLineCnt = 0

  for line in q2hand : 
    repeatCnt += line.count(checkText)

    if checkText in line :
      includLineCnt += 1  
  
  print("찾고자 하는 문구 : ", checkText)
  print("해당 문구 반복 라인 수 : ", includLineCnt)
  print("해당 문구 반복 횟수 : ", repeatCnt)



inputText = "Smooth like butterLike a criminal undercoverGon' pop like troubleBreakin' into your heart like thatCool shade stunnerYeah I owe it all to my motherHot like summerYeah I'm makin' you sweat like thatBreak it downOh when I look in the mirrorI'll melt your heart into 2I got that superstar glow soDo the boogie likeSide step right left to my beat (heartbeat)High like the moon rock with me babyKnow that I got that heatLet me show you 'cause talk is cheapSide step right left to my beat (heartbeat)Get it, let it rollSmooth like butterPull you in like no otherDon't need no UsherTo remind me you got it badAin't no otherThat can sweep you up like a robberStraight up, I got yaMakin' you fall like thatBreak it downOh when I look in the mirrorI'll melt your heart into 2I got that superstar glow soDo the boogie likeSide step right left to my beat (heartbeat)High like the moon rock with me babyKnow that I got that heatLet me show you 'cause talk is cheapSide step right left to my beat (heartbeat)Get it, let it rollGet it, let it rollGet it, let it rollNo ice on my wristI'm that n-ice guyGot that right body and that right mindRollin' up to party got the right vibeSmooth like butterHate us love usFresh boy pull up and we lay lowAll the playas get movin' when the bass lowGot ARMY right behind us when we say soLet's goSide step right left to my beat (heartbeat)High like the moon rock with me babyKnow that I got that heatLet me show you 'cause talk is cheapSide step right left to my beat (heartbeat)Get it, let it rollSmooth like (butter)Cool shade (stunner)And you know we don't stopHot like (summer)Ain't no (bummer)You be like oh my godWe gon' make you rock and you say (yeah)We gon' make you bounce and you say (yeah)Hotter?Sweeter!Cooler?Butter!Get it, let it roll"

checkText = 'butter'

countWord(inputText, checkText)