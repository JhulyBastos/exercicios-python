print('Bem vindo a lanchonete da Jhuly Bastos')
#tabela de valores, foi usado as aspas simples para organizar os espaços entre os produtos
print('***************Cardápio***************')
print('| Código  |' '      ' 'Descrição''       ' '| Valor |')
print('|  100    |' '   ' 'Cachorro quente''    ' '| 9,00  |')
print('|  101    |' 'Cachorro quente duplo'' '  '| 11,00 |')
print('|  102    |' '   ' '     X-EGG     ''    ' '| 12,00 |')
print('|  103    |' '   ' '   X-Salada    ''    ' '| 13,00 |')
print('|  104    |' '   ' '    X-Bacon    ''    ' '| 14,00 |')
print('|  105    |' '   ' '    X-Tudo     ''    ' '| 17,00 |')
print('|  200    |' '   ' 'Refrigerante lata''  ' '| 5,00  |')
print('|  201    |' '   ' '   Chá gelado   ''   ' '| 4,00  |')
#esse total foi usado para somar os valores dos pedidos, está em 0 porque dele começa a contagem.
total = 0
#qhile true, para ser feita a repetiçao
while True:
#if e elif foram usados para condicionar os pedidos que eram válidos para serem feitos pelo cliente.
    pedido1 = int(input('Entre com o código desejado:'))
    if (pedido1 == 100):
        print('Você pediu um cachorro quente no valor de 9,00 reais')
        total += 9
    elif (pedido1 == 101):
        print('Você pediu um cachorro quente duplo no valor de 11,00 reais')
        total += 11
    elif (pedido1 == 102):
        print('Você pediu um X-EGG no valor de 12,00 reais')
        total += 12
    elif (pedido1 == 103):
        print('Você pediu um X-Salada no valor de 13,00 reais')
        total += 13
    elif (pedido1 == 104):
        print('Você pediu um X-Bacon no valor de 14,00 reais')
        total += 14
    elif (pedido1 == 105):
        print('Você pediu um X-Tudo no valor de 17,00 reais')
        total += 17
    elif (pedido1 == 200):
        print('Você pediu um Refrigerante lata no valor de 5,00 reais')
        total += 5
    elif (pedido1 == 201):
        print('Você pediu um Chá gelado no valor de 4,00 reais')
        total += 4
#else, para se caso digite um codigo que não existe no cardápio.
    else:
        print('Opção inválida')
        continue
    pedido2 = input('Deseja pedir mais alguma coisa? (S/N)')
#se escolher a opção "S" vai aparecer a mensagem do print avisando que será feita mais escolhas.
    if (pedido2 == 'S'):
        print('Você optou por pedir por mais coisa.')
#se escolher a opção "N" o break vai quebrar o "loop" e não será feito mais pedidos.
    elif (pedido2 == 'N'):
        break
#print com o aviso que acabou os pedidos e o valor total já somado.
print('Não será pedido mais nada.')
print('O total a ser pago é {}:'.format(total))

