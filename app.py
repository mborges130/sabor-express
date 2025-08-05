import os

restaurantes = ['Pizzaria do Mateus', 'Sushi do João', 'Churrascaria do Carlos']
endereco = ['Rua das Flores, 123', 'Avenida Brasil, 456', 'Praça Central, 789']
telefone = [111, 2222, 3333]

def exibir_nome_do_programa():

    print('Sabor Express - API de pedidos de comida\n')
def exibir_opcoes():
    print('1. Cadastar Restaurante ')
    print('2. Listar Restaurantes')
    print('3. Ativar restaurante')
    print('4. sair\n')


def finalizar_app():
    os.system('cls')
    print('Obrigado por usar o Sabor Express!')
    exit()
    
def opcao_invalida():
    print('Opção inválida, tente novamente.\n')
    input('Pressione Enter para continuar...')
    main()

def cadastrar_novo_restaurante():
    os.system('cls')
    print('Cadastrar novo restaurante\n')
    nome = input('Nome do restaurante: ')
    restaurantes.append(nome)
    endereco = input('Endereço do restaurante: ')
    restaurantes.append(endereco)
    telefone = input('Telefone do restaurante: ')
    restaurantes.append(telefone)
    print(f'\nRestaurante {nome} cadastrado com sucesso!\n')
    input('Pressione Enter para continuar...')
    main()

def listar_restaurantes():
    os.system('cls')
    print('Listar Restaurantes\n')
    if not restaurantes:
        print('Nenhum restaurante cadastrado.\n')
    else:
        for i, restaurante in enumerate(restaurantes):
            print(f'{i + 1}. {restaurante} - Endereço: {endereco} - Telefone: {telefone[i]}')
    input('Pressione Enter para continuar...')
    main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: ')) 
        print(f'Você escolheu a opção: {opcao_escolhida} ')
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar Restaurante') 
        elif opcao_escolhida == 4:
            finalizar_app()    
        else: 
            opcao_invalida()
    except ValueError:
        opcao_invalida()
    

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()