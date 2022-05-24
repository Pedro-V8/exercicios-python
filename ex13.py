def miniMaxSum(arr):
    arr2 = []
    
    for x in arr:
        vl = sum(arr) - x
        arr2.append(vl)

    maior = arr2[0]
    menor = arr2[1]
    for i in arr2:
        if i > maior:
            maior = i
        elif i < menor:
            menor = i
    print(menor, maior)
    

arr = list(map(int, input().rstrip().split()))

miniMaxSum(arr)