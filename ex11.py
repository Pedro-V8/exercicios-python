
def funcao(arr):
    positive = 0
    negative = 0
    zero = 0
    divisor = len(arr)
    for x in arr:
        if x < 0:
            negative += 1
        elif x > 0:
            positive += 1
        elif x == 0:
            zero += 1
    
    print("{:.6f}".format(positive/divisor))
    print("{:.6f}".format(negative/divisor))
    print("{:.6f}".format(zero/divisor))

n = int(input().strip())

arr = list(map(int, input().rstrip().split()))

funcao(arr)