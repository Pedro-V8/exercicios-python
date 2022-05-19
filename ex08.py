'''
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
'''

aux = 0
lista = []
while aux < 10:
    valor = int(input())
    lista.append(valor)
    aux += 1

menor = lista[0]
maior = menor
for i in lista:
    if i < menor:
        menor = i
    if i > maior:
        maior = i

soma = maior + menor
print(f"Menor é: " + str(menor))
print(f"Maior é: " + str(maior))
print(f"Soma: " + str(soma))