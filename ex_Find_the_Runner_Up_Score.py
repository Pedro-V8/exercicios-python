if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input()))

    maior = arr[0]

    def achar_segundo_score(nl):
        maior_nl = nl[0]

        for i in nl:
            if i > maior_nl:
                maior_nl = i
        
    
        print(maior_nl)


    for x in arr:
        if x > maior:
            maior = x

    new_list = [val for val in arr if val != maior]

    achar_segundo_score(new_list)
    

