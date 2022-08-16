#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde
# esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter
jogo={'JOGADOR Nº1':randint(1,6), 'JOGADOR Nº2':randint(1,6),
      'JOGADOR Nº3':randint(1,6), 'JOGADOR Nº4':randint(1,6)}
print("VALORES SORTEADOS:")
ranking=list()
for k,v in jogo.items():
    print(f"{k} é {v}")
    sleep(1)
#lista ranking criado para colocar os valores em ordem
#ordenado da seguinte forma, na posição 0 é o item - jogador e a posição 1- o valor jogado
ranking=sorted(jogo.items(), key=itemgetter(1), reverse=True)
print("#"*50)
for i,v in enumerate(ranking): #ranking é uma lista, é um usado um for enumrate por isso. mostrando o
    #indice(i) e o valor(v)
    print(f"{i+1}º lugar: {v[0]} com {v[1]}")
    sleep(1)