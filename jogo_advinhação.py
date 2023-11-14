# -*- coding: utf-8 -*-

import unicodedata
import random

# Versão do Jogo da Forca
Versão = "1.0"

#Versão do Python
Versão = "3.7.0"

# A lib unidecode está sendo utilizada para a remoção de acentos das palavras.

palpitesCertos=[]
palpitesErrados=[]

def menu():
    palpitesCertos.clear()
    palpitesErrados.clear()
    print("--------------------")
    print("JOGO DA ADVINHAÇÃO\n")
    print("1.Jogar")
    print("2.Sair do Jogo\n")
    print("--------------------")
    op =(input("Qual operação deseja? (1 ou 2)\n"))

    while(op != "1" and op != "2"):
        print("\n________________________\n")
        print("Operação Inválida!")
        print("________________________\n")
        menu()
        break
    if op == "1":
        print("\n/////////////////////////////////")
        print("\nJOGO: ADVINHE QUAL É A PALAVRA!\n")
        pegar_tentativas()
    elif op == "2":
        print("\n________________________\n")
        print("Até mais!!!")
        print("________________________\n")


def pegar_tentativas():
    tentativas = input("Quantas tentativas você deseja ter [1-25]?\n")
    if(tentativas.isdigit()):
        if (1<=int(tentativas)<=25):
            print("")
            return pegar_palavra_min(tentativas)

    print(tentativas + " não é um número inteiro entre 1 e 25\n")
    pegar_tentativas()

def pegar_palavra_min(tentativas):
    tamanho_min = input("Qual o tamanho mínimo da palavra [4-10]?\n")
    if (tamanho_min.isdigit()):
        if (4<=int(tamanho_min)<=10):
            print("\nEscolhendo uma palavra...\n")
            return pegar_random_palavra(tamanho_min, tentativas)
            
    print(tamanho_min + " não é um número inteiro entre 4 e 10\n")
    pegar_palavra_min(tentativas)

def pegar_random_palavra(tamanho_min, tentativas):
    palavras = []
    l = []

    with open ('palavras_forca.txt', 'r', encoding = 'utf-8') as f:
        palavras = f.readlines()
    for i in range(len(palavras)):
        if len(palavras[i])-1>=int(tamanho_min):
             l.append(palavras[i])
             ip = random.randint(0,len(l)-1)
             palavra_secreta = l[ip].replace('\n','')
    palavrasecreta(palavra_secreta, tentativas)
    
    
#Função de remoção de acentos e caracteres especiais

def removeAcentosEcaracteresEspeciais(palavra_secreta):
    palavra_secreta_f = unicodedata.normalize('NFD', palavra_secreta).encode('ascii','ignore').decode('utf8').casefold()
    return palavra_secreta_f
#/////////////////////////////////////////////////////

def pegar_prox_letra(palavra, secreta, tentativas, palavra_secreta):
  palpite = input("Escolha a próxima letra: ")
  if palpite in palpitesCertos or palpite in palpitesErrados:
    print(palpite.upper() +" já foi escolhido antes, escolha outra letra")
  else:
    if palpite in palavra:
        print(palpite.upper() +" está na palavra!")
        palpitesCertos.append(palpite)

        for indice, letra in enumerate(palavra):
            if palpite == letra:
                secreta = secreta[:indice] + palpite + secreta[indice+1:]
        tentativas = int(tentativas)
        tentativas-=1
        print("\nPalavra: " + secreta)
        print("Tentativas que restam: " + str(tentativas))
        print("Tentativa precedente: " + palpite)
        if  secreta == palavra:
            print("\nPARABÉNS!! VOCÊ ACERTOU!!!")
            print("A palavra era: " + mostrar_palavra(palavra_secreta))
            return menu()
        elif secreta!= palavra and tentativas == 0:
            print("\nVOCÊ PERDEU!!!")
            print("A palavra era: " + mostrar_palavra(palavra_secreta))
            return menu()
    else:
        tentativas = int(tentativas)
        tentativas-=1
        print(palpite.upper() + " não está na palavra!")
        print("\nPalavra: " + secreta)
        print("Tentativas que restam: " + str(tentativas))
        print("Tentativa precedente: " + palpite)
        if tentativas == 0:
            print("\nVOCÊ PERDEU!!!")
            print("A palavra era: " + mostrar_palavra(palavra_secreta))
            return menu()
        palpitesErrados.append(palpite)
  pegar_prox_letra(palavra, secreta, tentativas, palavra_secreta)

def palavrasecreta(palavra_secreta, tentativas):
   palpite=" "
   palavra = removeAcentosEcaracteresEspeciais(palavra_secreta)
   secreta = "*"*len(palavra)
   print("\nPalavra: " + secreta)
   print("Tentativas que restam: " + str(tentativas))
   print("Tentativa precedente: " + palpite)
   pegar_prox_letra(palavra, secreta,tentativas, palavra_secreta)

def mostrar_palavra(palavra_secreta):
   return palavra_secreta.upper()
   
menu()


