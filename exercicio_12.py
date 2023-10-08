nomes = [0,0,0,0,0]

for x in range(5):
    nomes[x] = input("Digite um nome: ")
print(nomes)

for y in range(4,-1,-1):
    print("Os nomes em ordem reversa são: ",nomes[y])