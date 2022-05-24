#Soma das diagonais de uma matriz
def funcao(arr):
    
    sumA = sum([arr[x][x] for x in range(len(arr))])
    sumB = sum([arr[x][n -1 - x] for x in range(len(arr))])

    diff = abs(sumA - sumB)
    
    return diff
n = int(input().strip())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))
funcao(arr)
