import random
import sys
import math

def euclidesEstendido(a, b):
    s = 1
    t = 0
    x = 0
    y = 1

    while b != 0:
        c = a % b
        q = a // b
        i = s - (q * x)
        j = t - (q * y)

        a = b
        b = c
        s = x
        t = y
        x = i
        y = j
    
    return [a, s, t]

def inversoMul(a, n):
    m, s, t = euclidesEstendido(a, n)
    if m == 1:
        if s >= 0:
            return s
        else:
            return n + s
    else:
        return 0 # Falha
    
def Fabio():
    n, s, v, r = -1, 0, 0, -1
    respondido = 0

    x = 0

    entrada = input().split(" ")
    opcao = entrada[0]

    while True:

        if opcao == "I":
            n = int(entrada[1])
            s = int(entrada[2])
            v = int(entrada[3])

            if (s * s * v) % n == 1 and s < n and v < n:
                print("C")
            else:
                print("E")
        elif opcao == "X":
            
            r = random.randint(0, n-1)
            m, s, t = euclidesEstendido(r, n)

            while m != 1:
                r = random.randint(0, n-1)
                m, s, t = euclidesEstendido(r, n)

            x = (r * r) % n
            print("C ", x)
        elif opcao == "P":
            if n > 0:
                r = int(entrada[1])
                if r >= n:
                    print("E")
                else:
                    x = (r * r) % n
                    print("C ", x)
                    respondido = 0
            else:
                print("E")
        elif opcao == "R":
            if n > 0:
                if respondido == 0:
                    b = int(entrada[1])
                    xb = 0
                    if b == 0:
                        xb = r
                    elif b == 1:
                        xb = (r * s) % n
                    else:
                        print("E")
                        entrada = input().split(" ")
                        opcao = entrada[0]
                        continue
                
                    print("C ", xb)
                    r = 0
                    respondido = 1
                else:
                    print("E")
            else:
                print("E")
        elif opcao == "T":
            print("C")
            break

        entrada = input().split(" ")
        opcao = entrada[0]

def Patricia():
    n, v, t, x, b = 0, 0, 0, 0, 0
    repetirQ = 1
    repeticoesParaConfiar = 0
    identificado = 0
    erroQ = 0

    entrada = input().split(" ")
    opcao = entrada[0]

    while True:

        if opcao == "I":
            n = int(entrada[1])
            v = int(entrada[2])
            t = int(entrada[3])
            repeticoesParaConfiar = t
            repetirQ = 1
            erroQ = 0
            identificado = 0

            if v > n:
                print("E")
            else:
                if t >= 3 and t <= 50:
                    print("C")
                else:
                    print("E")
        elif opcao == "Q":
            if repetirQ == 1:
                x = int(entrada[1]) 
                b = random.randint(0, 1)
                if x > n or x == 1 or (euclidesEstendido(int(x ** (1/2)), n)[0] != 1) or x > v:
                    print("E")
                    erroQ = 1
                else:
                    print("C ", b)
            else:
                print("E")
        elif opcao == "V":

            if identificado == 1:
                print("E")
                entrada = input().split(" ")
                opcao = entrada[0]
                continue

            if erroQ == 1:
                print("E ", repeticoesParaConfiar - 1)
                entrada = input().split(" ")
                opcao = entrada[0]
                continue                

            xb = int(entrada[1])

            if b == 0:
                if (xb * xb) % n == (x % n):
                    if repeticoesParaConfiar == 0:
                       print("E ", repeticoesParaConfiar) 
                    else:
                        repeticoesParaConfiar -= 1
                        print("C ", repeticoesParaConfiar)
                else:
                    print("E ", repeticoesParaConfiar)
                    repeticoesParaConfiar = t
            elif b == 1:
                if(v * xb * xb) % n == (x % n):
                    if repeticoesParaConfiar == 0:
                       print("E ", repeticoesParaConfiar) 
                    else:
                        repeticoesParaConfiar -= 1
                        print("C ", repeticoesParaConfiar)
                else:
                    print("E ", repeticoesParaConfiar)
                    repeticoesParaConfiar = t
            else:
                print("E ", repeticoesParaConfiar)
                repeticoesParaConfiar = t

            if repeticoesParaConfiar == 0:
                identificado = 1
                repetirQ = 0
        elif opcao == "C":
            x = int(entrada[1])
            b = int(entrada[2])
            xb = int(entrada[3])

            if identificado == 1:
                print("E ", repeticoesParaConfiar)
                entrada = input().split(" ")
                opcao = entrada[0]
                continue

            if b == 0:
                if (xb * xb) % n == (x % n):
                    if repeticoesParaConfiar == 0:
                       print("E ", repeticoesParaConfiar) 
                    else:
                        repeticoesParaConfiar -= 1
                        print("C ", repeticoesParaConfiar)
                else:
                    print("E ", repeticoesParaConfiar)
                    repeticoesParaConfiar = t
            elif b == 1:
                if(v * xb * xb) % n == (x % n):
                    if repeticoesParaConfiar == 0:
                       print("E ", repeticoesParaConfiar) 
                    else:
                        repeticoesParaConfiar -= 1
                        print("C ", repeticoesParaConfiar)
                else:
                    print("E ", repeticoesParaConfiar)
                    repeticoesParaConfiar = t
            else:
                print("E ", repeticoesParaConfiar)
                repeticoesParaConfiar = t

            if repeticoesParaConfiar == 0:
                identificado = 1
        elif opcao == "T":
            print("C")
            break
        
        entrada = input().split(" ")
        opcao = entrada[0]

def Teodoro():
    n = 0

    entrada = input().split(" ")
    opcao = entrada[0]

    while True:

        if opcao == "I":
            p = int(entrada[1])
            q = int(entrada[2])

            n = p * q
            print("C ", n)
        elif opcao == "A":
            s = random.randint(2, n-1)
            s = (s**2) % n
            v = inversoMul(s, n)
            print("C ", v, s)
        elif opcao == "F":
            s = int(entrada[1])
            v = inversoMul((s*s) % n, n) 
            if v == 0 or s >= n or s == 0:
                print("E")
            else:
                print("C ", v)
        elif opcao == "T":
            print("C")
            break

        entrada = input().split(" ")
        opcao = entrada[0]

def Ester():
    n, v = 0, 0
    entrada = input().split(" ")
    opcao = entrada[0]

    while True:

        if opcao == "I":
            n = int(entrada[1])
            v = int(entrada[2])

            if v > n:
                print("E")
            else:
                print("C")
        elif opcao == "P":
            b = int(entrada[1])
            
            if b == 0:
                xb = random.randint(1, n)
                x = (xb ** 2) % n
                print("C", xb, x)
            elif b == 1:
                xb = random.randint(1, n)    
                x =( xb ** 2 * v )% n
                print("C", xb, x)

        elif opcao == "S":
            x1 = int(entrada[1])
            x2 = int(entrada[2])

            if x1 > n or x2 > n:
                print("E")
            else:
                s = x2 * inversoMul(x1, n) % n
                print("C ", s)
        elif opcao == "T":
            print("C")
            break

        entrada = input().split(" ")
        opcao = entrada[0]

if len(sys.argv) > 1:
    pessoa = sys.argv[1]

    if pessoa == "F":
        Fabio()
    elif pessoa == "P":
        Patricia()
    elif pessoa == "T":
        Teodoro()
    elif pessoa == "E":
        Ester()

else:
    print("Identifique quem está executando.")