nomes = [0,0,0,0,0]
senhas = [0,0,0,0,0]

for x in range(5):
    nomes[x] = input("Digite o login: ")
    senhas[x] = input("Digite sua senha: ")
    #print("O login é:",nomes[x],"Está na posição:",x,"e a senha é:",senhas[x], "Na posição:", x)

tentativa_login = 0
while tentativa_login < 3:
    pedir_login = input("Digite o seu login cadastrado: ")
    for y in range(5):
        if nomes[y] == pedir_login:
            tentativa_login = 3
            print("Login encontrado")
            for z in range(3):
                pedir_senha = input("Senha para o login: ")
                if senhas[y] == pedir_senha:
                    print("Login efetuado com sucesso, bem-vindo")
                    break
                else:
                    print("Senha inválida")
    if tentativa_login < 3:
        print("Usuário não encontrado")
    tentativa_login += 1