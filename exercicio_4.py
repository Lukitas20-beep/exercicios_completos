alunos = [0] * 5
notas = [0] * 5
soma = 0
for x in range(5):
    alunos[x] = input("Nome dos alunos: ")
    notas[x] = float(input("Digite as notas: "))
    soma += notas[x]
print(alunos, notas)
media = soma/5
print(media)
for z in range(5):
    if notas[z] >= media:
        print("Os alunos que passaram com nota acima da média foram: ", alunos[z])