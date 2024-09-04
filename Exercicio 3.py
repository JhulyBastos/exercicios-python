print('Bem vindo a Companhia de Logística Jhuly Bastos S.A.')
#Perguntas que devem ser respondidas pelo o usuario sobre as dimenssões do objeto
def dimensoesObjeto():
#laço de repetição
    while True:
        try:
            altura = float(input("Digite a altura do objeto (em cm): "))
            comprimento = float(input("Digite o comprimento do objeto (em cm): "))
            largura = float(input("Digite a largura do objeto (em cm): "))
#O cálculo que será feito
            volume = altura * comprimento * largura
#As condições para que o serviço possa ser feito
            if volume < 1000:
                return 10
            elif volume < 10000:
                return 20
            elif volume < 30000:
                return 30
            elif volume < 100000:
                return 50
#Se as dimensões do objeto excederem o limite essa mensagem aparece
            else:
                print("As dimensões do objeto excedem o limite aceito. Tente novamente.")
#Caso o usuário digite um valor inválido, essa mensagem aparece
        except ValueError:
            print("Valor inválido. Digite um valor numérico para as dimensões.")
#Perguntas que devem ser respondidas pelo o usuario sobre o peso do objeto
def pesoObjeto():
    while True:
        try:
            peso = float(input("Digite o peso do objeto (em kg): "))
#as condições de limite de peso e para calcular o valor final
            if peso <= 0.1:
                return 1
            elif peso < 1:
                return 1.5
            elif peso < 10:
                return 2
            elif peso < 30:
                return 3
#Caso o peso exceder i limmite aceito, essa mensagem aparece na tela
            else:
                print("O peso do objeto excede o limite aceito. Tente novamente.")
# Caso o usuário digite um valor inválido, essa mensagem aparece
        except ValueError:
            print("Valor inválido. Digite um valor numérico para o peso.")
# Para o usuário escolher a rota do objeto
def rotaObjeto():
    while True:
        rota = input("Digite a rota do objeto (RS, SR, BS, SB, BR, RB): ")

        if rota == "RS" or rota == "SR":
            return 1
        elif rota == "BS" or rota == "SB":
            return 1.2
        elif rota == "BR" or rota == "RB":
            return 1.5
# Caso o usuário digite uma rota que não está na lista, essa mensagem aparece
        else:
            print("Rota inválida. Digite uma rota válida.")

# Programa principal
# função para obter as dimensões do objeto
dimensoes = dimensoesObjeto()
peso = pesoObjeto() #função para obter o peso do objeto
rota = rotaObjeto() #função para obter a rota do objeto
# Calcula o total a ser pago com base nas informações fornecidas
total = dimensoes * peso * rota
print("Total a ser pago: R$ %.2f" % total) #Mostra na tela o total a ser pago com duas casas decimais