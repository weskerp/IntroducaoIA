#Created on Tue Mar 19 09:59:56 2019
#===============================================================================
#=============================JOGO DA VELHA=====================================
#===============================================================================
#=========================equipe: IAGO E KELINE=================================
#===============================================================================

import random
import time
import os

x = 'X'
o = 'O'
empt = ' '
limpar = 'clear'

#função para imprimir o tabuleiro na tela
def Imprime(raiz):
    print("tabuleiro          mapa")
    print(raiz[0], "|", raiz[1],"|", raiz[2],"      1 | 2 | 3")
    print("----------      ---------")
    print(raiz[3], "|", raiz[4],"|", raiz[5],"      4 | 5 | 6")
    print("----------      ---------")
    print(raiz[6], "|", raiz[7],"|", raiz[8],"      7 | 8 | 9")


#função que verifica se há algum vencedor
def verificaJogo(tabuleiro):
    if(tabuleiro[0]==tabuleiro[3] and tabuleiro[3]==tabuleiro[6] and tabuleiro[0]!=empt):
        return tabuleiro[0]
    
    elif(tabuleiro[1]==tabuleiro[4] and tabuleiro[4]==tabuleiro[7] and tabuleiro[1]!=empt):
        return tabuleiro[1]
    
    elif(tabuleiro[2]==tabuleiro[5] and tabuleiro[5]==tabuleiro[8] and tabuleiro[2]!=empt):
            return tabuleiro[2]
        
    elif(tabuleiro[0]==tabuleiro[1] and tabuleiro[1]==tabuleiro[2] and tabuleiro[0]!=empt):
            return tabuleiro[0]
        
    elif(tabuleiro[3]==tabuleiro[4] and tabuleiro[4]==tabuleiro[5] and tabuleiro[3]!=empt):
            return tabuleiro[3]
        
    elif(tabuleiro[6]==tabuleiro[7] and tabuleiro[7]==tabuleiro[8] and tabuleiro[6]!=empt):
            return tabuleiro[6]
        
    elif(tabuleiro[0]==tabuleiro[4] and tabuleiro[4]==tabuleiro[8] and tabuleiro[0]!=empt):
            return tabuleiro[0]
        
    elif(tabuleiro[2]==tabuleiro[4] and tabuleiro[4]==tabuleiro[6] and tabuleiro[2]!=empt):
            return tabuleiro[2]        
    else:
        return 0    
    
#função para definir se há possibilidade do computador ganhar e fazer a jogada para vitória
def Estrategiav(tabuleiro):
    if(tabuleiro[0]==o and tabuleiro[1]==o and tabuleiro[2]==empt):
        tabuleiro[2]=o
        return 1
    elif(tabuleiro[0]==o and tabuleiro[2]==o and tabuleiro[1]==empt):
        tabuleiro[1]=o
        return 1
    elif(tabuleiro[1]==o and tabuleiro[2]==o and tabuleiro[0]==empt):
        tabuleiro[0]=o
        return 1
    elif(tabuleiro[3]==o and tabuleiro[4]==o and tabuleiro[5]==empt):
        tabuleiro[5]=o
        return 1
    elif(tabuleiro[3]==o and tabuleiro[5]==o and tabuleiro[4]==empt):
        tabuleiro[4]=o
        return 1
    elif(tabuleiro[4]==o and tabuleiro[5]==o and tabuleiro[3]==empt):
        tabuleiro[3]=o
        return 1
    elif(tabuleiro[6]==o and tabuleiro[7]==o and tabuleiro[8]==empt):
        tabuleiro[8]=o
        return 1
    elif(tabuleiro[6]==o and tabuleiro[8]==o and tabuleiro[7]==empt):
        tabuleiro[7]=o
        return 1
    elif(tabuleiro[7]==o and tabuleiro[8]==o and tabuleiro[6]==empt):
        tabuleiro[6]=o
        return 1
    elif(tabuleiro[0]==o and tabuleiro[4]==o and tabuleiro[8]==empt):
        tabuleiro[8]=o
        return 1
    elif(tabuleiro[0]==o and tabuleiro[8]==o and tabuleiro[4]==empt):
        tabuleiro[4]=o
        return 1
    elif(tabuleiro[4]==o and tabuleiro[8]==o and tabuleiro[0]==empt):
        tabuleiro[0]=o
        return 1
    elif(tabuleiro[2]==o and tabuleiro[4]==o and tabuleiro[6]==empt):
        tabuleiro[6]=o
        return 1
    elif(tabuleiro[2]==o and tabuleiro[6]==o and tabuleiro[4]==empt):
        tabuleiro[4]=o
        return 1
    elif(tabuleiro[4]==o and tabuleiro[6]==o and tabuleiro[2]==empt):
        tabuleiro[2]=o
        return 1
    elif(tabuleiro[0]==o and tabuleiro[3]==o and tabuleiro[6]==empt):
        tabuleiro[6]=o
        return 1
    elif(tabuleiro[0]==o and tabuleiro[6]==o and tabuleiro[3]==empt):
        tabuleiro[3]=o
        return 1
    elif(tabuleiro[3]==o and tabuleiro[6]==o and tabuleiro[0]==empt):
        tabuleiro[0]=o
        return 1
    elif(tabuleiro[1]==o and tabuleiro[4]==o and tabuleiro[7]==empt):
        tabuleiro[7]=o
        return 1
    elif(tabuleiro[1]==o and tabuleiro[7]==o and tabuleiro[4]==empt):
        tabuleiro[4]=o
        return 1
    elif(tabuleiro[4]==o and tabuleiro[7]==o and tabuleiro[1]==empt):
        tabuleiro[1]=o
        return 1
    elif(tabuleiro[2]==o and tabuleiro[5]==o and tabuleiro[8]==empt):
        tabuleiro[8]=o
        return 1
    elif(tabuleiro[2]==o and tabuleiro[8]==o and tabuleiro[5]==empt):
        tabuleiro[5]=o
        return 1
    elif(tabuleiro[5]==o and tabuleiro[8]==o and tabuleiro[2]==empt):
        tabuleiro[2]=o
        return 1
    
    else:
        return 0


#função para definir se há possibilidade do jogador ganhar e fazer uma jogada para tentar impedir
def Estrategia(tabuleiro):
    if(tabuleiro[0]==x and tabuleiro[1]==x and tabuleiro[2]==empt):
        tabuleiro[2]=o
        return 1
    elif(tabuleiro[0]==x and tabuleiro[2]==x and tabuleiro[1]==empt):
        tabuleiro[1]=o
        return 1
    elif(tabuleiro[1]==x and tabuleiro[2]==x and tabuleiro[0]==empt):
        tabuleiro[0]=o
        return 1
    elif(tabuleiro[3]==x and tabuleiro[4]==x and tabuleiro[5]==empt):
        tabuleiro[5]=o
        return 1
    elif(tabuleiro[3]==x and tabuleiro[5]==x and tabuleiro[4]==empt):
        tabuleiro[4]=o
        return 1
    elif(tabuleiro[4]==x and tabuleiro[5]==x and tabuleiro[3]==empt):
        tabuleiro[3]=o
        return 1
    elif(tabuleiro[6]==x and tabuleiro[7]==x and tabuleiro[8]==empt):
        tabuleiro[8]=o
        return 1
    elif(tabuleiro[6]==x and tabuleiro[8]==x and tabuleiro[7]==empt):
        tabuleiro[7]=o
        return 1
    elif(tabuleiro[7]==x and tabuleiro[8]==x and tabuleiro[6]==empt):
        tabuleiro[6]=o
        return 1
    elif(tabuleiro[0]==x and tabuleiro[4]==x and tabuleiro[8]==empt):
        tabuleiro[8]=o
        return 1
    elif(tabuleiro[0]==x and tabuleiro[8]==x and tabuleiro[4]==empt):
        tabuleiro[4]=o
        return 1
    elif(tabuleiro[4]==x and tabuleiro[8]==x and tabuleiro[0]==empt):
        tabuleiro[0]=o
        return 1
    elif(tabuleiro[2]==x and tabuleiro[4]==x and tabuleiro[6]==empt):
        tabuleiro[6]=o
        return 1
    elif(tabuleiro[2]==x and tabuleiro[6]==x and tabuleiro[4]==empt):
        tabuleiro[4]=o
        return 1
    elif(tabuleiro[4]==x and tabuleiro[6]==x and tabuleiro[2]==empt):
        tabuleiro[2]=o
        return 1
    elif(tabuleiro[0]==x and tabuleiro[3]==x and tabuleiro[6]==empt):
        tabuleiro[6]=o
        return 1
    elif(tabuleiro[0]==x and tabuleiro[6]==x and tabuleiro[3]==empt):
        tabuleiro[3]=o
        return 1
    elif(tabuleiro[3]==x and tabuleiro[6]==x and tabuleiro[0]==empt):
        tabuleiro[0]=o
        return 1
    elif(tabuleiro[1]==x and tabuleiro[4]==x and tabuleiro[7]==empt):
        tabuleiro[7]=o
        return 1
    elif(tabuleiro[1]==x and tabuleiro[7]==x and tabuleiro[4]==empt):
        tabuleiro[4]=o
        return 1
    elif(tabuleiro[4]==x and tabuleiro[7]==x and tabuleiro[1]==empt):
        tabuleiro[1]=o
        return 1
    elif(tabuleiro[2]==x and tabuleiro[5]==x and tabuleiro[8]==empt):
        tabuleiro[8]=o
        return 1
    elif(tabuleiro[2]==x and tabuleiro[8]==x and tabuleiro[5]==empt):
        tabuleiro[5]=o
        return 1
    elif(tabuleiro[5]==x and tabuleiro[8]==x and tabuleiro[2]==empt):
        tabuleiro[2]=o
        return 1
    
    else:
        return 0
               
def jogada1(tabuleiro, jogador):
    if(jogador == 0):
        num=int(input('digite a casa que quer jogar de acordo com o mapa ao lado do tabuleiro: '))
        while(tabuleiro[num-1]!=empt):
            num=int(input('casa ja preenchida, tente novamente: '))
        tabuleiro[num-1] = x
        os.system(limpar)
        Imprime(tabuleiro)
        jogador = 1
    else:
        tabuleiro[0]=o
        print("Computador jogando...")
        time.sleep(3)
        os.system(limpar)
        Imprime(tabuleiro)
        jogador = 0
    return jogador

def jogada2(tabuleiro, jogador):
    if(jogador == 0):
        num=int(input('digite a casa que quer jogar de acordo com o mapa ao lado do tabuleiro: '))
        while(tabuleiro[num-1]!=empt):
            num=int(input('casa ja preenchida, tente novamente: '))
        tabuleiro[num-1] = x
        os.system(limpar)
        Imprime(tabuleiro)
        jogador = 1
    else:
        if(tabuleiro[4]==empt):
            tabuleiro[4]=o
        else:
            tabuleiro[0]=o
        print("Computador jogando...")
        time.sleep(3)
        os.system(limpar)
        Imprime(tabuleiro)
        jogador = 0
    return jogador

def jogada3(tabuleiro, jogador):
    if(jogador == 0):
        num=int(input('digite a casa que quer jogar de acordo com o mapa ao lado do tabuleiro: '))
        while(tabuleiro[num-1]!=empt):
            num=int(input('casa ja preenchida, tente novamente: '))
        tabuleiro[num-1] = x
        os.system(limpar)
        Imprime(tabuleiro)
        jogador = 1
    else:
        if(tabuleiro[8]==empt):
            tabuleiro[8]=o
        else:
            tabuleiro[6]=o
        print("Computador jogando...")
        time.sleep(3)
        os.system(limpar)
        Imprime(tabuleiro)
        jogador = 0
    return jogador

def jogada4(tabuleiro, jogador):
    if(jogador == 0):
        num=int(input('digite a casa que quer jogar de acordo com o mapa ao lado do tabuleiro: '))
        while(tabuleiro[num-1]!=empt):
            num=int(input('casa ja preenchida, tente novamente: '))
        tabuleiro[num-1] = x
        os.system(limpar)
        Imprime(tabuleiro)
        jogador = 1
    else:
        if(Estrategia(tabuleiro)==0):
            if(tabuleiro[1]==empt and tabuleiro[7]==empt):
                tabuleiro[1]=o
            elif(tabuleiro[3]==empt and tabuleiro[5]==empt):
                tabuleiro[3]=o
            elif(tabuleiro[0]==empt and tabuleiro[8]==empt):
                tabuleiro[0]=o
        print("Computador jogando...")
        time.sleep(3)
        os.system(limpar)
        Imprime(tabuleiro)
        jogador = 0
    return jogador

def jogada5(tabuleiro, jogador):
    if(jogador == 0):
        num=int(input('digite a casa que quer jogar de acordo com o mapa ao lado do tabuleiro: '))
        while(tabuleiro[num-1]!=empt):
            num=int(input('casa ja preenchida, tente novamente: '))
        tabuleiro[num-1] = x
        os.system(limpar)
        Imprime(tabuleiro)
        jogador = 1
    else:
        if(Estrategiav(tabuleiro)==0):
            if(Estrategia(tabuleiro)==0):
                tabuleiro[2]=o
        print("Computador jogando...")
        time.sleep(3)
        os.system(limpar)
        Imprime(tabuleiro)
        jogador = 0
    return jogador

def jogada6(tabuleiro, jogador):
    if(jogador == 0):
        num=int(input('digite a casa que quer jogar de acordo com o mapa ao lado do tabuleiro: '))
        while(tabuleiro[num-1]!=empt):
            num=int(input('casa ja preenchida, tente novamente: '))
        tabuleiro[num-1] = x
        os.system(limpar)
        Imprime(tabuleiro)
        jogador = 1
    else:
        if(Estrategiav(tabuleiro)==0):
            if(Estrategia(tabuleiro)==0):
                if(tabuleiro==[o, empt, empt, x, x, o, empt, empt, x]):
                    tabuleiro[2]=o
                if(tabuleiro==[o, x, empt, x, o, empt, empt, empt, x]):
                    tabuleiro[2]=o
                if(tabuleiro==[empt, o, x, x, o, empt, empt, x, empt]):
                    tabuleiro[8]=o
                if(tabuleiro==[empt, o, empt, x, o, x, empt, x, empt]):
                    tabuleiro[0]=o
                if(tabuleiro==[x, o, empt, empt, o, x, empt, x, empt]):
                    tabuleiro[6]=o
                if(tabuleiro==[o, empt, empt, o, o, x, empt, x, empt]):
                    tabuleiro[2]=o
                elif(tabuleiro[1]==empt):
                    tabuleiro[1]=o
                elif(tabuleiro[3]==empt):
                    tabuleiro[3]=o
                elif(tabuleiro[5]==empt):
                    tabuleiro[5]=o
                elif(tabuleiro[6]==empt):
                    tabuleiro[6]=o
        print("Computador jogando...")
        time.sleep(3)
        os.system(limpar)
        Imprime(tabuleiro)
        jogador = 0
    return jogador


def jogada7(tabuleiro, jogador):
    if(jogador == 0):
        num=int(input('digite a casa que quer jogar de acordo com o mapa ao lado do tabuleiro: '))
        while(tabuleiro[num-1]!=empt):
            num=int(input('casa ja preenchida, tente novamente: '))
        tabuleiro[num-1] = x
        os.system(limpar)
        Imprime(tabuleiro)
        jogador = 1
    else:
        if(Estrategiav(tabuleiro)==0):
            print("Computador jogando...")
        if(Estrategia(tabuleiro)==0):
            print("Computador jogando...")
        time.sleep(3)
        os.system(limpar)
        Imprime(tabuleiro)
        jogador = 0
    return jogador

def jogada8(tabuleiro, jogador):
    if(jogador == 0):
        num=int(input('digite a casa que quer jogar de acordo com o mapa ao lado do tabuleiro: '))
        while(tabuleiro[num-1]!=empt):
            num=int(input('casa ja preenchida, tente novamente: '))
        tabuleiro[num-1] = x
        os.system(limpar)
        Imprime(tabuleiro)
        jogador = 1
    else:
        if(Estrategiav(tabuleiro)==0):
            if(Estrategia(tabuleiro)==0):
                if(tabuleiro[0]==empt):
                    tabuleiro[0]=o
                elif(tabuleiro[1]==empt):
                    tabuleiro[1]=o
                elif(tabuleiro[2]==empt):
                    tabuleiro[2]=o
                elif(tabuleiro[3]==empt):
                    tabuleiro[3]=o
                elif(tabuleiro[4]==empt):
                    tabuleiro[4]=o
                elif(tabuleiro[5]==empt):
                    tabuleiro[5]=o
                elif(tabuleiro[6]==empt):
                    tabuleiro[6]=o
                elif(tabuleiro[7]==empt):
                    tabuleiro[7]=o
                elif(tabuleiro[8]==empt):
                    tabuleiro[8]=o
        print("Computador jogando...")
        time.sleep(3)
        os.system(limpar)
        Imprime(tabuleiro)
        jogador = 0
    return jogador

def jogada9(tabuleiro, jogador):
    if(jogador == 0):
        num=int(input('digite a casa que quer jogar de acordo com o mapa ao lado do tabuleiro: '))
        while(tabuleiro[num-1]!=empt):
            num=int(input('casa ja preenchida, tente novamente: '))
        tabuleiro[num-1] = x
        os.system(limpar)
        Imprime(tabuleiro)
        jogador = 1
    else:
        if(tabuleiro[0]==empt):
            tabuleiro[0]=o
        elif(tabuleiro[1]==empt):
            tabuleiro[1]=o
        elif(tabuleiro[2]==empt):
            tabuleiro[2]=o
        elif(tabuleiro[3]==empt):
            tabuleiro[3]=o
        elif(tabuleiro[4]==empt):
            tabuleiro[4]=o
        elif(tabuleiro[5]==empt):
            tabuleiro[5]=o
        elif(tabuleiro[6]==empt):
            tabuleiro[6]=o
        elif(tabuleiro[7]==empt):
            tabuleiro[7]=o
        elif(tabuleiro[8]==empt):
            tabuleiro[8]=o
        print("Computador jogando...")
        time.sleep(3)
        os.system(limpar)
        Imprime(tabuleiro)
        jogador = 0
    return jogador

def Jogo(tabuleiro, jogador):
    Imprime(tabuleiro)
    vencedor=0
    jogador = jogada1(tabuleiro, jogador)
    jogador = jogada2(tabuleiro, jogador)
    jogador = jogada3(tabuleiro, jogador)
    jogador = jogada4(tabuleiro, jogador)
    jogador = jogada5(tabuleiro, jogador)
    vencedor=verificaJogo(tabuleiro)
    if(vencedor==0):
        jogador = jogada6(tabuleiro, jogador)
    vencedor=verificaJogo(tabuleiro)
    if(vencedor==0):
        jogador = jogada7(tabuleiro, jogador)
    vencedor=verificaJogo(tabuleiro)
    if(vencedor==0):
        jogador = jogada8(tabuleiro, jogador)
    vencedor=verificaJogo(tabuleiro)
    if(vencedor==0):
        jogador = jogada9(tabuleiro, jogador)
    vencedor = verificaJogo(tabuleiro)
    
    if(vencedor == x):
        print("O jogador venceu!")
    elif(vencedor==o):
        print("O computador venceu!")
    else:
        print("Empate!")
    
def SelecionaJogador():
    x=random.randint(0, 1000)
    return x % 2

def main():
    A = [empt] * 9  #Gera o tabuleiro vazio
    jogador = SelecionaJogador() #Seleciona qual jogador irá começar
    Jogo(A, jogador) #Inicia o jogo
    
main()