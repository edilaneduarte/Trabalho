# Nome: Edilane Duarte da silva
# Matrícula: 20172143000155

import random

print("*******************JOGUE O DADO*******************")

numero_aleatorio=random.randint(1,6) # vai gerar um número aleatório de 1 a 6
numero_secreto = numero_aleatorio # vai armazenar o numero escolido
resposta = 1

while(resposta == 1):

	dado=random.randint(1,6)

	if(dado == numero_secreto):
		print("voce acertou o numero secreto" )
		print ("Valor do dado ", dado)
		print("O número secreto é: ",numero_secreto)
		break

	elif(dado != numero_secreto):
		
		print ("Valor do dado ", dado)
		print("Aperte 1 para jogar o dado novamente")
		resposta = int(input())
