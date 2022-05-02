from random import randint
letters = ["A","B","C","D"]
check = bool()
output = {"A":[" "," "," "," "],"B":[" "," "," "," "],"C":[" "," "," "," "],"D":[" "," "," "," "]}
yValues = {"0":[1,2,3,4],"1":[1,2,3,4],"2":[1,2,3,4],"3":[1,2,3,4],"4":[1,2,3,4]}

while check != True:
  for iL,letter in enumerate(output.keys()):
    xList = [1,2,3,4]  # mit jedem neuen Buchstaben des output dicts, ist die komplette x-Liste vorhanden
    for i in range(0,len(output["A"])): #index der die output position ansteuert, und die korrekte y liste erstellt X POSITION
      yList = yValues[str(i)]
      verfügbareZahlen = [x for x in xList if x in yList]
      if i == 3:
        output[letter][i] = verfügbareZahlen[0]
        yValues[str(i)].remove(verfügbareZahlen[0])
        xList.remove(verfügbareZahlen[0])
      else:
        yListN = yValues[str(i+1)]
        verfügbareZahlenNext = [x for x in xList if x in yListN]
        linksRechtsUngleich = [x for x in verfügbareZahlen if x not in verfügbareZahlenNext]
        if letter == "A":
          randm = randint(0,len(verfügbareZahlen)-1)
          output[letter][i] = verfügbareZahlen[randm]
          yValues[str(i)].remove(verfügbareZahlen[randm])
          xList.remove(verfügbareZahlen[randm])
          #xxyyzz
        elif (letter == "B" or letter == "C") and (len(linksRechtsUngleich)!=0):
          #xxyyzzz
          randm = randint(0,len(linksRechtsUngleich)-1)
          output[letter][i] = linksRechtsUngleich[randm]
          yValues[str(i)].remove(linksRechtsUngleich[randm])
          xList.remove(linksRechtsUngleich[randm])
        elif (letter == "B" or letter == "C") and len(linksRechtsUngleich)==0:
          randm = randint(0,len(verfügbareZahlen)-1)
          output[letter][i] = verfügbareZahlen[randm]
          yValues[str(i)].remove(verfügbareZahlen[randm])
          xList.remove(verfügbareZahlen[randm])
        elif letter == "D":
          output[letter][i] = verfügbareZahlen[0]
          yValues[str(i)].remove(verfügbareZahlen[0])
          xList.remove(verfügbareZahlen[0])
        else:
          print("gibt noch eine option...")
  check = True
for values in output.values():
  print(values)

'''
Dieses Problem habe ich "finally" gelöst, indem ich alle Möglichkeiten, die auftreten können , notiert habe, und daraus die versch. Algorithmen abgeleitet habe.
Am Ende sind es 5 verschiedene Algorithmen dass es funktioniert. 
Bei i == 3 kann ich nicht die nächsten verf. betrachten, da es das Letzte Item ist in X-Richtung. 
bei I == 3 gibt es zwangsläufig nur ein verfügbares Element deswegen [0]

bei "B" und "C" wird es knifflig, hier gibt es verschiedene Möglickeiten. 
1. Möglichkeit: links gibt es ein verfügbares item dass nicht im nächsten verf. ist. DIeses wird gesetzt.
2. Möglichkeit: es gibt keine Unterschiedlichen verf. Zhalen links und rechts. nun wird durch zufall eine Zahl gesetzt.

Bei "D" gibt es zwangsläufig nur eine verf. Zahl. Diese wird gesetzt [0]

'''
