if __name__ == '__main__':
    n = int(input())
    arr = map(int, input())
    
    

    maior = arr[0]
    aux = arr[0]

    for x in arr:
        if x > maior:
            maior = x



    for y in arr:
        if y > aux and y < maior:
            aux = y

    print(aux)