import os

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

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: ')) 
        print(f'Você escolheu a opção: {opcao_escolhida} ')
        if opcao_escolhida == 1:
            print('Cadastrar Restaurante') 
        elif opcao_escolhida == 2:
            print('Listar Restaurantes')
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