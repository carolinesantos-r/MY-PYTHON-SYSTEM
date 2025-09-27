#sistema bancário com tuplas, listas e dicionários


def banco():
    banco_dados = {}
    #CADASTRO NO BANCO
    nome = input('Nome: \n')
    idade = int(input("Idade: \n"))
    senha = input('Senha: ')
    login = input('E-mail: ')
    banco_dados['Nome'] = nome
    banco_dados['Idade'] = idade
    banco_dados['Login'] = login
    banco_dados['Senha'] = senha
    lista = []
    banco_dados['Valores'] = lista

    return banco_dados

    # -----------------------------

   # ACESSO AO SISTEMA

def sistema_banco(saldo):

    banco_dados = banco()
    print('Digite senha e login para acessar:')
    senha_input = input('Senha: ')
    login_input = input('Login: ')

    if banco_dados['Senha'] == senha_input and banco_dados['Login'] == login_input:
        print("Logado no Banco Z.")
        sis = input("Deseja acessar o Banco Z?\n")
        while sis == 'sim' or sis == 'Sim' or sis == 'SIM' or sis == 's':
            escolha = input(f'''
                Bem-vindo(a) ao Banco Z, {banco_dados['Nome']}
                Escolha a operação que deseja fazer:

                 1 - Saque
                 2 - Depósito
                 3 - Extrato
                 0 - Sair\n''')

            match(escolha):
                case '0':
                    print("Desconectando do Banco Z. Volte sempre!")
                    break
                case '1':
                    val_saq = float(input("Valor do saque: R$ "))
                    saldo = saldo - val_saq
                    banco_dados['Valores'].append(f"Saque: -R${val_saq:.2f}")
                    print('Saldo Atual: R$', saldo)
                    sis = input("Deseja continuar no Banco Z?\n")

                case '2':
                    val_dep = float(input("Valor do Depósito: R$"))
                    saldo = saldo + val_dep
                    banco_dados['Valores'].append(f"Depósito: +R${val_dep:.2f}")
                    print('Saldo Atual: R$', saldo)
                    sis = input("Deseja continuar no Banco Z?\n")

                case '3':
                    print('Saldo Atual: R$', banco_dados['Valores'])

                    sis = input("Deseja continuar no Banco Z?\n")

                case _:
                    print("Digite algo válido.")
    else:
        print("Dados incorretos.")

sistema_banco(6000.00)