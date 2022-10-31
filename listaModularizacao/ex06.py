# Exercicio numero 06:
# Crie uma função que calcule o IMC (Índice de Massa Corpórea) de uma pessoa com base na sua idade,
# massa e sexo conforme tabela. Na célula do programa principal, use a função e exiba o IMC de 100
# entrevistados (um por um).

# Formulas
# IMC feminino: (0.95 * massa) / altura²
# IMC masculino: (1.05 * massa) / altura²

#ERROS POSSIVEIS:
# CASO O USUARIO DIGITE NUMEROS NO SEXO, O PROGRAMA CONTINUA RODANDO....
# CASO O USUARIO DIGITE UMA LETRA EM CM OU PESO O PROGRAMA CRASHA


import math

def imc(massa, altura, sexo):
    imcM = (0.95 * massa) / math.pow(altura, 2)
    imcH = (1.05 * massa) / math.pow(altura, 2)
    imcEx = 0
    if (sexo == "m" or sexo == "M"):
        imcEx = imcM
    elif (sexo == "h" or sexo == "H"):
        imcEx = imcH
    return imcEx

i = 0

for i in range (1, 101 ,1):
    print(f"{i}º entrevistado(a): ")
    while True:
        sexo = input("Digite (H) caso seja homem e (M) se for mulher: ")
        if (sexo != 'm') and (sexo != 'M') and (sexo != 'h') and (sexo != 'H'):
            print('=' * 100)
            print('ERRO DE DIGITAÇÃO: Por favor digite uma das letras solicitadas!')
            print('=' * 100)
        else:
            break
    while True:
        try:
            altura = int(input("Digite sua altura (em cm): ")) / 100  # A altura é dividido por 100 para que o usuario nao precise inserir com .
            if (altura <= 0) or (altura > 2.30):
                print('=' * 100)
                print('ERRO: Você inseriu uma altura invalida! Digite uma de 1 a 230!')
                print('=' * 100)
            else:
                break
        except:
            print('=' * 100)
            print('ERRO: Você digitou uma letra ou um caracter especial, por favor digite sua altura apenas em numeros e em CENTIMETROS!')
            print('=' * 100)
    while True:
        try:
            massa = float(input("Digite o seu peso (em kgs): "))
            if massa <= 0:
                print('ERRO: Você inseriu um peso menor ou igual a 0!')
            else:
                break
        except:
            print('='*100)
            print('ERRO: Você digitou uma letra ou um caracter especial, por favor digite seu peso apenas em numeros\ne caso seja necessario utilize "." para representar a casa decimal.')
            print('=' *100)
    print(f'O imc do entrevistado é de: {imc(massa, altura, sexo):.2f}')
    print('='*50)









