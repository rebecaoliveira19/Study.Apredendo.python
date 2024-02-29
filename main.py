# Mensagem de boas-vindas
print("Bem-vindo(a), SeuNome!")

# Variáveis globais
lista_colaboradores = []
id_global = 0

# Função para cadastrar um novo colaborador
def cadastrar_colaborador(id):
    global id_global
    nome = input("Digite o nome do colaborador: ")
    setor = input("Digite o setor do colaborador: ")
    salario = float(input("Digite o salário do colaborador: "))

    colaborador = {
        "ID": id,
        "Nome": nome,
        "Setor": setor,
        "Salário": salario
    }

    lista_colaboradores.append(colaborador)
    id_global += 1

# Função para consultar colaboradores
def consultar_colaborador():
    while True:
        print("\nOpções de consulta:")
        print("1. Consultar Todos")
        print("2. Consultar por Id")
        print("3. Consultar por Setor")
        print("4. Retornar ao menu")
        opcao = input("Digite sua escolha: ")

        if opcao == "1":
            print("\nLista de todos os colaboradores:")
            for colaborador in lista_colaboradores:
                print(colaborador)
        elif opcao == "2":
            id_colaborador = int(input("Digite o ID do colaborador: "))
            for colaborador in lista_colaboradores:
                if colaborador["ID"] == id_colaborador:
                    print("\nDados do colaborador:")
                    print(colaborador)
                    break
            else:
                print("Colaborador não encontrado.")
        elif opcao == "3":
            setor = input("Digite o setor desejado: ")
            print(f"\nColaboradores do setor {setor}:")
            for colaborador in lista_colaboradores:
                if colaborador["Setor"] == setor:
                    print(colaborador)
        elif opcao == "4":
            break
        else:
            print("Opção inválida.")

# Função para remover colaborador
def remover_colaborador():
    id_colaborador = int(input("Digite o ID do colaborador a ser removido: "))
    for colaborador in lista_colaboradores:
        if colaborador["ID"] == id_colaborador:
            lista_colaboradores.remove(colaborador)
            print("Colaborador removido com sucesso.")
            break
    else:
        print("Colaborador não encontrado.")

# Menu principal
while True:
    print("\nMenu Principal:")
    print("1. Cadastrar Colaborador")
    print("2. Consultar Colaborador")
    print("3. Remover Colaborador")
    print("4. Encerrar Programa")

    opcao_menu = input("Digite sua escolha: ")

    if opcao_menu == "1":
        cadastrar_colaborador(id_global)
    elif opcao_menu == "2":
        consultar_colaborador()
    elif opcao_menu == "3":
        remover_colaborador()
    elif opcao_menu == "4":
        break
    else:
        print("Opção inválida.")

# Cadastro de colaboradores
cadastrar_colaborador(id_global)
cadastrar_colaborador(id_global)
cadastrar_colaborador(id_global)

# Consulta de colaboradores
consultar_colaborador()

# Consulta por ID
print("\nConsulta por ID:")
consultar_colaborador()

# Consulta por Setor
print("\nConsulta por Setor:")
consultar_colaborador()

# Remoção de colaborador e consulta de todos os colaboradores
print("\nRemoção de um colaborador:")
remover_colaborador()
print("\nConsulta de todos os colaboradores após a remoção:")
consultar_colaborador()
