'''
Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

'''
base = int(input("Base da operação: "))
expoente = int(input("Expoente da operação: "))
resultado = 1 #comentario

if expoente == 0:
    print("1")
else:

    for i in range(expoente):
        resultado *= base 
    print(resultado)