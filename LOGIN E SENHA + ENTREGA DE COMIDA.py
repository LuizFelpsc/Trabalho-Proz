# Criar um programa de i food, onde a a pessoa vai logar com senha e nome;
# vai escolher qual lanche vai querer e esse lanche será adicionado a um carrinho 
# adicionar opção para ver o carrinho
# quando ela selecionar tudo o que vai querer, pedir o endereço
# e o valor total da compra, além da forma de pagamento

from os.path import exists
from os import getcwd as getpath
from time import sleep
from random import randint

print('-=' * 15)
print(f"{'BEM VINDO AO LLS BURGUER!!':^30}")
print('-=' * 15)
sleep(1)
print('Primeiro faça login para fazer seu pedido!')
sleep(1)


#VERIFICAR SE O CADASTRO EXISTE OU ESTÁ CERTO
def verificar_login (nome, senha, cadastro):
    dados_conta = open('dados_conta', 'r').read().split()
    print('dados')
    for i in range(0, len(dados_conta), 2):
            dado_nome = dados_conta[i]
            dado_senha = dados_conta[i + 1]
       
            if dado_nome == nome:  
                if cadastro == True:
                    return False
                if dado_senha == senha:
                    return True    
                else: 
                    return False
    print('tureee')
    return True

#CRIAR CONTA
def criar_conta ():
    dados_conta = open('dados_conta', 'a')

    nome = str(input('Digite seu apelido sem espaços (Lembre-se dele): '))
    senha = str(input('Digite a senha: '))
    if verificar_login (nome, senha, True):
        dados_conta.write(f' {nome} {senha} ')
        dados_conta.close()

        sleep(1)
        dados_conta = open('dados_conta', 'r').read()
        print('CONTA REGISTRADA! AGORA FAÇA LOGIN!')
    else:
        sleep(0.5)
        print('-' * 15)
        print('APELIDO OU CONTA JÁ REGISTRADA!.... O QUE DESEJA FAZER? ')
        opcao = int(input('''
[1] Tentar criar conta novamente
[2] Fazer login
        '''))

        if opcao == 1:
            criar_conta()
        sleep(0.7)
    fazer_login()

#FAZER LOGIN
def fazer_login ():
    
    if not exists(f'{getpath()}\dados_conta'):
        
        print('VOCÊ NÃO TEM CONTA CADASTRADA! Crie sua conta logo abaixo: ')
        criar_conta()
    else:
        
        nome = str(input('Digite o seu apelido: '))
        senha = str(input('Digite sua senha: '))

        if verificar_login(nome, senha, False):
            sleep(0.7)
            print(f'CADASTRO EFETUADO COM SUCESSO! É bom te ver por aqui {nome}!')
        else:
            print('APELIDO OU SENHA INCORRETOS!')
            sleep(1)
            
            opcao_login = int(input('''O que deseja fazer?
[1] Para criar conta
[2] Para Tentar novamente'''))

            if opcao_login == 1:
                criar_conta()
            elif opcao_login == 2:
                fazer_login()
            else:
                print('VALOR INVÁLIDO DIGITADO!')

# O QUE O CLIENTE QUER FAZER
def inicio_login ():
    opcao_login = int(input('''Digite o que deseja:
[1] Para criar conta
[2] Para fazer login
    '''))

    match opcao_login:
        case 1:
            criar_conta()
        case 2:
            fazer_login()

inicio_login()

sleep(1)
print('-=' * 15)
print(f"{'CARDÁPIO':^30}")
print('-=' * 15)


def consultar_endereco ():
    print('-' * 15)
    print('Digite o endereço para entrega: ')
    rua = str(input('Rua: '))
    numero = str(input('Número: '))
    bairro = str(input('Bairro: '))
    cidade = str(input('Cidade: '))
    return [rua, numero, bairro, cidade]

def finalizar_compra ():
    print('-' * 15)
    print(f'TOTAL A PAGAR: R$ {consultar_carrinho_valor():.2f}')
    print('-' * 15)

    forma_pagamento = int(input('''Selecione a forma de pagamento:
[1] Pix
[2] Dinheiro

[4] VOLTAR AO MENU PRINCIPAL
    '''))

    if forma_pagamento == 4:
        cardapio()
    
    print(['Pix', 'Dinheiro'][forma_pagamento - 1], ' Selecionado!')
    sleep(0.8)

    endereco = consultar_endereco()

    print('Processando ...')
    sleep(1)

    print(f'PEDIDO EFETUADO! A entrega será feita na rua {endereco[0]}, número {endereco[1]}, bairro {endereco[2]} e cidade {endereco[3]}... \nA previsão de entrega é de {randint(30,60)} minutos')
    sleep(1)
    print('\nVOLTE SEMPRE!')


carrinho = []

def consultar_carrinho_valor ():
    valores = 0
    for elemento in carrinho:
        valores += elemento[1]
    return valores
def cardapio ():
    print('-=' * 15)
    print(f'Valor R$: {consultar_carrinho_valor()}')
    precos = [[['X TUDO', 20],['X MEDIO', 15],['X BASICO', 5]],
              [['Hotdog Grande', 15], ['Hotdog medio', 10], ['Hotdog pequeno', 5]],
              [['Coca-Cola 3L', 12.5], ['Coca-Cola 2L', 8], ['Coca-Cola 1L', 6]]
              ]
    
    opcao_cliente = int(input('''DIGITE O QUE VOCÊ DESEJA:
{1} Hamburgueres
{2} Hotdog
{3} Bebidas

{4} VER CARRINHO
    '''))
    sleep(1)

    match opcao_cliente:
        case 1:
            hamburgueres = int(input('''Hambúrgueres:
[1] R$ 20,00 - X TUDO (Alface, cheddar, tomate, milho, carne dupla, bacon, cebola)
[2] R$ 15,00 - X MEDIO (Alface, tomate, carne dupla, bacon)
[3] R$ 5,00 - X BASICO (Alface, tomate, carne)
            
[4] VOLTAR AO MENU
            '''))

            if hamburgueres == 4:
                cardapio()
            else:
                carrinho.append(precos[opcao_cliente - 1][hamburgueres - 1])
                print(f'--- O hambúrguer {precos[opcao_cliente - 1][hamburgueres - 1][0]} foi adicionado ao carrinho --- \n')
                cardapio()
        case 2:
            hotdog = int(input('''Hotdogs:
[1] R$ 15,00 - Hotdog grande (Salsicha, queijo, batata-palha, molho)
[2] R$ 10,00 - Hotdog medio (Salsicha, queijo, molho)
[3] R$ 5,00 - Hotdog pequeno (Salsicha, queijo)
            
[4] VOLTAR AO MENU
            '''))

            if hotdog == 4:
                cardapio()
            else:
                carrinho.append(precos[opcao_cliente - 1][hotdog - 1])
                print(f'--- O hambúrguer {precos[opcao_cliente - 1][hotdog - 1][0]} foi adicionado ao carrinho --- \n')
                cardapio()
                return
        case 3:
            bebidas = int(input('''Bebidas:
[1] R$ 12,50 - Coca-Cola 3L
[2] R$ 8,00 - Coca-Cola 2L
[3] R$ 6,00 - Coca-Cola 1L

[4] VOLTAR AO MENU
            '''))

            if bebidas == 4:
                cardapio()
            else:
                carrinho.append(precos[opcao_cliente - 1][bebidas - 1])
                print(f'--- O hambúrguer {precos[opcao_cliente - 1][bebidas - 1][0]} foi adicionado ao carrinho --- \n')
                cardapio() 
        case 4:
            print('-' * 8)
            print('CARRINHO:')
            print('-' * 8)

            for c in carrinho:
                print(f'Item: {c[0]} -  R$ {c[1]:.2F} \n')
            print(f'Total: R$ {consultar_carrinho_valor():.2f}')

            opcao = str(input('Deseja continuar e fazer o pagamento? (S/N)'))
            if opcao in 'Ss':
                finalizar_compra ()
            else:
                cardapio()
cardapio()