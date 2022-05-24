def birthdayCakeCandles(candles):
    max = candles[0]
    count = 0
    for i in candles:
        if i > max:
            max = i
    for x in candles:
        if x == max:
            count += 1
    return count

candles_count = int(input().strip())
candles = list(map(int, input().rstrip().split()))

result = birthdayCakeCandles(candles)
print(result)