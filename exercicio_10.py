n = int(input("Digite o tamanho do vetor: "))
A = [0] * n
B = [0] * n
S = [0] * n

for x in range(n):
    A[x] = int(input("Digite os números: "))
    B[x] = int(input("Digite os números: "))
    S[x] = A[x] + B[x]
print(S)