# Lista de banco de dados de usuários
usuarios = []

# 2 Função para cadastrar usuários
def cadastrar():
    print("\n---- Cadastro de usuário ----")

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    email = input("Digite o email: ")

    usuario = {
        "nome": nome,
        "idade": idade,
        "email": email,
    }

    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")


# 3 Função para listar usuários
def listar():
    print("\n---- Lista de usuários ----")

    if len(usuarios) == 0:
        print("Nenhum usuário cadastrado.")
        return

    for i, user in enumerate(usuarios):
        print(f"\nUsuário {i + 1}")
        print("Nome:", user['nome'])
        print("Idade:", user['idade'])
        print("Email:", user['email'])


# 4 Função para buscar usuários
def buscar():
    print("\n---- Buscar usuário ----")

    nome_busca = input("Digite o nome: ")
    encontrado = False

    for user in usuarios:
        if user["nome"].lower() == nome_busca.lower():
            print("\nUsuário encontrado:")
            print("Nome:", user['nome'])
            print("Idade:", user['idade'])
            print("Email:", user['email'])
            encontrado = True

    if not encontrado:
        print("Usuário não encontrado.")


# 5 Função para atualizar usuários
def atualizar():
    print("\n---- Atualizar usuário ----")

    nome_busca = input("Digite o nome do usuário: ")

    for user in usuarios:
        if user["nome"].lower() == nome_busca.lower():

            print("Digite os novos dados:")

            user["nome"] = input("Novo nome: ")
            user["idade"] = int(input("Nova idade: "))
            user["email"] = input("Novo email: ")

            print("Usuário atualizado.")
            return

    print("Usuário não encontrado.")


# 6 Função para remover usuários
def remover():
    print("\n---- Remover usuário ----")

    nome_busca = input("Digite o nome: ")

    for user in usuarios:
        if user["nome"].lower() == nome_busca.lower():
            usuarios.remove(user)
            print("Usuário removido.")
            return

    print("Usuário não encontrado.")


# 1 Menu principal
def menu():
    while True:
        print("\n+++++++++++++++++++++++++++")
        print("|  SISTEMA DE CADASTRO     |")
        print("+++++++++++++++++++++++++++")
        print("[1] -> Cadastrar usuário")
        print("[2] -> Listar usuários")
        print("[3] -> Buscar usuário")
        print("[4] -> Atualizar usuário")
        print("[5] -> Remover usuário")
        print("[0] -> Sair")

        opcao = input("Informe a opção desejada: ")

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            buscar()
        elif opcao == "4":
            atualizar()+-:
        elif opcao == "5":
            remover()
        elif opcao == "0":
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida!")


# Iniciar sistema
menu()