alunos = int(input("Digite quantos alunos tem na sala: "))
vetorA = []

for i in range(alunos):
    nomes = input("Digite o nome dos alunos: ")
    vetorA.append(nomes)


for x in range(alunos):
    print("Nome: ",vetorA[x],"Posição: ",x)

buscar_nome = input("Digite um nome que você queira achar: ")
for z in range(alunos):
    if buscar_nome == vetorA[z]:
        print(buscar_nome, "Existe, na posição: ", z)