A = [0]*30
cont = 0
for x in range(30):
    A[x] = int(input("Digite números: "))
X = int(input("Digite um número qualquer: "))

for y in range(30):
    if X == A[y]:
        cont+=1
print("A quantidade de vezes que esse número aparece é: ", cont)