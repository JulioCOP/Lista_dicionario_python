#Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também
# a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

aluno= dict()
aluno['NOME']=str(input("Nome do aluno: "))
aluno['MEDIA']=float(input("Qual foi media do aluno: "))
if aluno['MEDIA']<6:
    print(f"{aluno['NOME']} REPROVADO")
elif aluno['MEDIA']>=7:
    print(f"{aluno['NOME']} APROVADO")
else:
    print(f"{aluno['NOME']} RECUPERAÇÃO ")
for k,v in aluno.items():
    print(f"{k} é igual a {v}")


