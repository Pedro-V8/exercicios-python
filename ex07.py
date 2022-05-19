'''
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E

O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
'''

def conceito_e(m):
    print("REPROVADO E")

def conceito_d(m):
    if not 6.0 > m >= 4.0:
        conceito_e(m)
        return
    print("REPROVADO D")

def conceito_c(m):
    if not 7.5 > m >= 6.0:
        conceito_d(m)
        return
    print("APROVADO C")

def conceito_b(m):
    if not 9.0 > m >= 7.5:
        conceito_c(m)
        return
    print("APROVADO B")

def conceito_a(m):
    if not 10.0 >= media >= 9.0:
        conceito_b(m)
        return
    print("APROVADO A")
    

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))

media = (n1 + n2) / 2

conceito_a(media)