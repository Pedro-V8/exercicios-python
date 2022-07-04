from unittest import result


x = int(input())
y = int(input())
z = int(input())
n = int(input())

def verifica(i , j , k, result_list):
    if not i + j + k == n:
        lista = [i,j,k]
        result_list.append(lista)
        return 


def verifica_parte_k(i , j , k, result_list):
    if not i + j + k == n:
        lista = [i,j,k]
        result_list.append(lista)
        k += 1
        return verifica_parte_k(i , j , k, result_list)
    else:

        return 


i = 0
j = 0
k = 0


lista = [i,j,k]
result_list = []

verifica_parte_k(i,j,k,result_list)
print(result_list)