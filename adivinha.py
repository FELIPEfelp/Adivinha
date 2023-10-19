#randomificação
from random import randint
numero = randint (0 , 10)

#Pergunta da maquina
print('estou pensando em um numero de 0 a 10 tente adivinha.')
 
 #resposta
n=int(input('Qual o numero?'))

#error e acerto
if n == numero:
    print('parabéns você acertou')
else:
    print('você errou tente novamente')    