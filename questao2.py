# Nome: Edilane Duarte da silva
# Matrícula: 20172143000155

import random # importa a biblioteca de numero aleatório

print("*********************ADIVINHAÇÃO**********************\n")

numero_aleatorio =random.randint(1,20) #randint é uma das funções do modulo random. vai gerar numeros aleatórios de acordo com os paramentros que escolhi
chute = 0 #para que forca o programa a entrar no while

print("O número secreto está entre 1 e 20")

while(chute != numero_aleatorio):
    
    chute = int(input("Digite seu chute: "))
    
    if(chute == numero_aleatorio):
        print("O número secreto é: ", numero_aleatorio)
        print("PARABÉNS VOCÊ ACERTOU O NÚMERO SECRETO")
        break
    elif(chute > numero_aleatorio):
        print("Seu chute foi maior que o número secreto")
    elif(chute < numero_aleatorio):
        print("Seu chute foi menor que o número secreto")