import os

print('Sabor Express - API de pedidos de comida\n')

print('1. Cadastar Restaurante ')
print('2. Listar Restaurantes')
print('3. Ativar restaurante')
print('4. sair\n')



opcao_escolhida = int(input('Escolha uma opção: ')) 

def finalizar_app():
    os.system('cls')
    print('Obrigado por usar o Sabor Express!')
    exit()

print(f'Você escolheu a opção: {opcao_escolhida} ')

if opcao_escolhida == 1:
    print('Cadastrar Restaurante') 
elif opcao_escolhida == 2:
    print('Listar Restaurantes')
elif opcao_escolhida == 3:
    print('Ativar Restaurante') 
else : 
    finalizar_app()




