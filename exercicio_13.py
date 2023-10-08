vetorNums = []
vetor_pares = []
soma_nums = 0
maior_num = 0
menor_num = 0
maiorMedia = 0

for i in range(3):
    num = int(input("Digite os números(com numeros menores que 0 ou 0): "))
    vetorNums += [num]
    soma_nums += num
for y in range(3):
    if vetorNums[y] % 2 == 0:
        vetor_pares += [vetorNums[y]]

for x in range(3):
    if vetorNums[x] >= maior_num:
        maior_num = vetorNums[x]
    if vetorNums[x] <= menor_num:
        menor_num = vetorNums[x]

media = soma_nums/3

for z in range(3):
    if vetorNums[z] > media:
        maiorMedia += 1

print(vetorNums)
print("Numeros pares:", vetor_pares)
print("maior:",maior_num,"menor:", menor_num)
print("Maiores que a média:",maiorMedia)