import random

class Pikachu():
    hp = 100
    ad = 55

    def win(self):
        print "Pikachu Win!"

class Pigglypuff():
    hp = 100
    ad = 45

    def win(self):
        print "Jigglypuff Win!"

pikachu = Pikachu()
jigglypuff = Pigglypuff()
turno = random.randint(0,1)

while pikachu.hp > 0 and jigglypuff.hp > 0:
    if turno == 1:
        jigglypuff.hp = jigglypuff.hp - pikachu.ad
        print "Ataque de pikachu"
        turno = 0
    else:
        pikachu.hp = pikachu.hp - jigglypuff.ad
        print "Ataque de jigglypuff"
        turno = 1

if pikachu.hp <= 0:
    jigglypuff.win()
else:
    pikachu.win()