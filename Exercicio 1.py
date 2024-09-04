print('Bem vindo a loja da Jhuly')
valor = int(input('Qual o valor do produto?'))
quantidade = int(input('Quantos produtos você quer?'))
print('O valor sem desconto é {} {}:'.format('R$',valor * quantidade))
#Essa condição verifica se a quantidade é menor ou igual a 9, caso seja o desconto será de 0%.
if (quantidade <= 9):
  print(('(Desconto de 0%)'))
# Essa condição verifica se a quantidade está entre 10 e 99, caso esteja o desconto será de 5%.
elif (99 >= quantidade >= 10):
  print('O valor com desconto é {} {}:' ' ' '(Desconto de 5%)'.format('R$', (valor * quantidade) - ((valor * quantidade) * ( 5 / 100))))
# Essa condição verifica se a quantidade está entre 100 e 999, caso esteja o desconto será de 10%.
elif (999 >= quantidade >= 100):
  print('O valor com desconto é {} {}:' ' ' '(Desconto de 10%)'.format('R$', (valor * quantidade) - ((valor * quantidade) * (10 / 100))))
# Essa condição verifica se a quantidade é maior ou igual a 1000, caso seja o desconto será de 15%.
else:
  print('O valor com desconto é {} {}:' ' ' '(Desconto de 15%)'.format('R$', (valor * quantidade) - ((valor * quantidade) * (15 / 100))))
