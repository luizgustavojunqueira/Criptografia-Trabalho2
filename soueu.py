import random
import sys
import math

# Algoritmo de Euclides Estendido que calcula o minimo divisor comum 
# entre dois números além de outros dois valores "s" e "t" onde mdc(a, b) = s*a + t*b
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

# Algoritmo que calcula o inverso multiplicativo de um número "a" no módulo "n"
def inversoMul(a, n):
    m, s, t = euclidesEstendido(a, n)
    if m == 1:
        if s >= 0:
            return s
        else:
            return n + s
    else:
        return 0 # Falha
    
# Execução do código para Fabio
def Fabio():
    n, s, v, r = -1, 0, 0, -1
    respondido = 0
    identificado = 0

    x = 0

    entrada = input().split(" ")
    opcao = entrada[0]

    # Percorre a entrada
    while True:

       
        if opcao == "I":     # Tarefa de identificar 
            n = int(entrada[1])
            s = int(entrada[2])
            v = int(entrada[3])

            # Verifica se os valores de N, S e V passados são válidos
            if (s * s * v) % n == 1 and s < n and v < n:
                print("C")
                identificado = 1
            else:
                print("E")
        elif opcao == "X":   # Tarefa de iniciar 

            # Caso já tenha sido executado o passo de identificar
            if identificado == 1:
                # Essa tarefa calcula um valor de X a partir de um R gerado aleatóriamente

                # Gera um r aleatório entre 1 e n-1, os dois inclusos, até que o mdc de R com N seja igual a 1
                r = random.randint(1, n-1)
                m, s, t = euclidesEstendido(r, n)
                while m != 1:
                    r = random.randint(0, n-1)
                    m, s, t = euclidesEstendido(r, n)

                # Calcula X a partir de R
                x = (r * r) % n
                print("C ", x)
            else:
                print("E")
        elif opcao == "P":   # Tarefa de preparar 

            # Caso já tenha sido executado o passo de identificar
            if identificado == 1:
                r = int(entrada[1])

                # Verifica se o R lido é válido
                if r >= n or r == 0:
                    print("E")
                else:
                    # Calcula X a partir do R lido
                    x = (r * r) % n
                    print("C ", x)
                    respondido = 0
            else:
                print("E")
        elif opcao == "R":   # Tarefa de responder 

            # Caso já tenha sido executado o passo de identificar
            if identificado == 1:
                # Caso a tarefa de responder ainda não tenha sido executada
                if respondido == 0:
                    b = int(entrada[1])
                    xb = 0

                    # Calcula XB dependendo do valor de B lido
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
        elif opcao == "T":   # Tarefa de terminar o programa 
            print("C")
            break

        entrada = input().split(" ")
        opcao = entrada[0]

# Execução do código para Patricia
def Patricia():
    n, v, t, x, b = 0, 0, 0, 0, 0
    repetirQ = 1
    repeticoesParaConfiar = 0
    identificado = 0
    erroQ = 0

    entrada = input().split(" ")
    opcao = entrada[0]

    # Percorre a entrada
    while True:

        if opcao == "I":    # Tarefa de inicializar
            n = int(entrada[1])
            v = int(entrada[2])
            t = int(entrada[3])
            repeticoesParaConfiar = t
            repetirQ = 1
            erroQ = 0
            identificado = 0

            # Verifica se o valor de V lido é válido
            if v > n:
                print("E")
            else:
                # Verifica se o valor de T lido é válido
                if t >= 3 and t <= 50:
                    print("C")
                else:
                    print("E")
        elif opcao == "Q":  # Tarefa de receber compromisso
            # Esse comando só pode ser repetido após validar a resposta
            if repetirQ == 1:
                x = int(entrada[1]) 
                b = random.randint(0, 1) # Gera um bit B aleatório

                # Verifica se o valor de X lido é válido
                if x > n or x == 1 or (euclidesEstendido(int(x ** (1/2)), n)[0] != 1) or x > v:
                    print("E")
                    erroQ = 1
                else:
                    print("C ", b)
            else:
                print("E")
        elif opcao == "V":  # Tarefa de validar resposta
            
            # Caso já tenha sido identificado retorna erro
            if identificado == 1:
                print("E")
                entrada = input().split(" ")
                opcao = entrada[0]
                continue
            
            # Caso tenha recebido compromisso com erro dá erro
            if erroQ == 1:
                print("E ", repeticoesParaConfiar - 1)
                entrada = input().split(" ")
                opcao = entrada[0]
                continue                

            xb = int(entrada[1]) # Lê o valor de XB da entrada

            # Faz os calculos para validar a resposta com base no xb lido agora e o valor de X lido e o bit b gerado no passo de receber compromisso
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
        elif opcao == "C":  # Tarefa de testar compromisso

            # Essa tarefa simula a execução de validar resposta passando diretamente os valores de X, B e XB

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
        elif opcao == "T":  # Tarefa de terminar o programa
            break
        
        entrada = input().split(" ")
        opcao = entrada[0]

# Execução do código para Teodoro
def Teodoro():
    n = 0

    entrada = input().split(" ")
    opcao = entrada[0]

    # Percorre a entrada
    while True:

        if opcao == "I":    # Tarefa de inicializar

            # Realiza a leitura de P e Q passados e calcula N a partir destes

            p = int(entrada[1])
            q = int(entrada[2])

            n = p * q
            print("C ", n)
        elif opcao == "A":  # Tarefa de autenticar

            # Nessa tarefa um valor secreto S e um valor público V são gerados.
            s = random.randint(2, n-1)
            s = (s**2) % n
            v = inversoMul(s, n)
            print("C ", v, s)
        elif opcao == "F":  # Tarefa de forjar

            # Nessa tarefa é passado o valor de S esperado por Fábio e gera um valor de V correspondente

            s = int(entrada[1])
            v = inversoMul((s*s) % n, n) 
            if v == 0 or s >= n or s == 0:
                print("E")
            else:
                print("C ", v)
        elif opcao == "T":  # Tarefa de terminar o programa
            print("C")
            break

        entrada = input().split(" ")
        opcao = entrada[0]

# Execução do código para Teodoro
def Ester():
    n, v = 0, 0
    entrada = input().split(" ")
    opcao = entrada[0]

    # Percorre a entrada
    while True:

        if opcao == "I":    # Tarefa de inicializar

            # Faz a leitura de V e N e verifica se V é válido

            n = int(entrada[1])
            v = int(entrada[2])
            
            if v > n:
                print("E")
            else:
                print("C")
        elif opcao == "P":  # Tarefa de preparar
            b = int(entrada[1])
            
            # Gera os valores de X e XB com base no bit B passado
            if b == 0:
                xb = random.randint(1, n)
                x = (xb ** 2) % n
                print("C", xb, x)
            elif b == 1:
                xb = random.randint(1, n)    
                x =( xb ** 2 * v )% n
                print("C", xb, x)

        elif opcao == "S":  # Tarefa sorte

            # X1 é o valor de XB para o bit 0
            # X2 é o valor de XB para o bit 0

            # A partir de X1 e X2 lidos, calcula o valor de S que poderia validá-los

            x1 = int(entrada[1])
            x2 = int(entrada[2])

            if x1 > n or x2 > n:
                print("E")
            else:
                s = x2 * inversoMul(x1, n) % n
                print("C ", s)
        elif opcao == "T": # Tarefa de terminar o programa
            print("C")
            break

        entrada = input().split(" ")
        opcao = entrada[0]

# Verifica se foi passado um argumento identificando a pessoa
if len(sys.argv) > 1:
    pessoa = sys.argv[1]

    # Executa o código correspondente a pessoa passada como argumento
    if pessoa == "F":
        Fabio()
    elif pessoa == "P":
        Patricia()
    elif pessoa == "T":
        Teodoro()
    elif pessoa == "E":
        Ester()
    else:
        print("Essa pessoa não existe")

else:
    print("Identifique quem está executando.")