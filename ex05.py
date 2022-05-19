"""
Escreva um programa que imprima os números de 1 a 100. Mas para múltiplos de três imprima "Fizz" em vez do número e para os múltiplos de cinco imprima "Buzz". Para números que são múltiplos de três e cinco, imprima "FizzBuzz".
"""

for x in range(1,21):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)