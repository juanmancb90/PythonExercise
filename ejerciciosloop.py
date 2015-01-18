# -*- coding: utf-8 -*-
__author__ = 'User'

def es_par(x):
    if x % 2 == 0:
        return True
    else:
        return False

def es_entero(n):
    if n - round(n) ==  0:
        return True
    elif n+1 == 0:
        return True
    else:
        return False

def suma_de_digitos(x):
    r = 0
    for i in range(len(str(x))):
        d = x % 10
        x //= 10
        r += d
    return r

def factorial(x):
    if x < 1:
        return 1
    else:
        return x * factorial(x-1)

def es_primo(x):
    if x < 2:
        return False

    for i in range(2, x):
        if x % i == 0:
            return False

    return True


def reverse(s):
    l = ""
    c = len(str(s))-1
    for i in s:
        l += s[c]
        c -= 1

    return l

def anti_vocal(txt):
    rst = ""
    for c in txt:
        if c in "aeiou" or c in "AEIOU":
            rst += ""
        else:
            rst += c

    return rst

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}


def puntaje_scrabble(txt):
    total = 0
    word = txt.lower()
    for c in word:
        total += score[c]

    return total

def censor(texto, palabra):
    tamPal = len(str(palabra))
    astCant = "*"*tamPal
    listText = texto.split()
    for i in range(len(listText)):
        if listText[i] == palabra:
            listText[i] = astCant

    rst = " ".join(listText)
    return rst

def contar(lista, item):
    c = 0
    for i in range(len(lista)):
        if lista[i] == item:
            c += 1

    return c

def purificar(lista):
    l = []
    for i in lista:
        if i % 2 == 0:
            l.append(i)
    return l

def producto(lista):
    total = 1
    for i in lista:
        total *= i

    return total


def quitar_repetidos(lista):
    l = []
    for i in lista:
        if i in l:
            continue
        else:
            l.append(i)

    return l


def mediana(lista):
    l = sorted(lista)
    print(l)
    rPar = 0
    rImpar = 0
    t = len(l)
    if t % 2 != 0:
        rImpar = l[round((t / 2) - 0.5)]
        return rImpar
    else:
        a = l[round(t / 2)]
        b = l[round(t / 2) - 1]
        media = (a + b) / 2.0
        rPar = media
        return rPar

print (mediana([8]))

#print (quitar_repetidos([1,1,2,2,3]))
#print (producto([4,5,5]))
#print (purificar([1,2,3,5,4,6]))
#print (contar([1,2,3,4,5,5,6],5))
#print (censor("this hack is wack hack", "hack"))
#print (puntaje_scrabble("Juan"))
#print (anti_vocal("Hola!"))
#print ("Pruebas")
#n = int(input("Ingresa el número: "))
#print (es_par(n))
#print (es_entero(7.00))
#print (factorial(4))
#print (suma_de_digitos(434))
#print (es_primo(263))
#print (reverse("Juan Manuel"))