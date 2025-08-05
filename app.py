import os

restaurantes = ['Pizzaria do Mateus', 'Sushi do João', 'Churrascaria do Carlos']

def exibir_nome_do_programa():

    print('Sabor Express - API de pedidos de comida\n')
def exibir_opcoes():
    print('1. Cadastar Restaurante ')
    print('2. Listar Restaurantes')
    print('3. Ativar restaurante')
    print('4. sair\n')


def finalizar_app():
    exibir_subtitulo('Finalizando o aplicativo...')
    exit()
    
def voltar_ao_menu_principal():
    print('Voltando ao menu principal...\n')
    input('Pressione Enter para continuar...')
    main()
    
def opcao_invalida():
    print('Opção inválida, tente novamente.\n')
    voltar_ao_menu_principal()
    
def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print('\n' + '-' * len(texto) + '\n')

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastrar novo restaurante')
    nome = input('Nome do restaurante: ')
    restaurantes.append(nome)
    print(f'\nRestaurante {nome} cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listar Restaurantes')
    if not restaurantes:
        print('Nenhum restaurante cadastrado.\n')
    else:
        for restaurante in restaurantes:
            print(f'. {restaurante}')
    voltar_ao_menu_principal()

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