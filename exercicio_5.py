A = [0] * 10
for x in range(10):
    A[x] = int(input("Digite 10 números: "))
print(A)
X = int(input("Digite mais um número que vai ser guardado: "))

M = [0] * 10
for i in range(10):
    M[i] = X * A[i]
print(M)