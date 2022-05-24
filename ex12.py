def teste(n):
    nE = n
    for x in range(1,n+1):
       print(" "*(nE-1),end="")
       print("#"*(x),end="\n")
       nE -= 1
       

n = int(input())
teste(n)