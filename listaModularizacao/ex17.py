#FUNÇÃO
def jogofutebol(ingresso, qtdKid, qtdJovens, qtdAlimentos):
  global valorTotal, pessoasTotal
  valorJovens = ingresso / 2
  valorAlimentos = ingresso / 2

  totalInteira = ingresso * qtdInteira
  totalJovens = valorJovens * qtdJovens
  totalAlimentos = valorAlimentos * qtdAlimentos
  valorTotal = totalJovens + totalAlimentos + totalInteira
  pessoasTotal = qtdKid + qtdJovens + qtdAlimentos + qtdInteira

  return pessoasTotal, valorTotal

while True:
    print('='*25+'MENU DO PROGRAMA'+'='*25)
    escolha = input('Para rodar o programa digite [1]\nPara sair do programa digite qualquer outra tecla!\nDigite sua escolha: ')
    if escolha != '1':
        print('Você saiu do programa, até mais!')
        break
    else:
        print('='*25+'PROGRAMA INICIADO'+'='*25)
        #INGRESSO
        while True:
          try:
            ingresso = float(input('Digite o valor do ingresso: '))
            if ingresso < 0:
              print('-------------------------ATENÇÃO ERRO!---------------------------------------')
              print('ERRO: Você digitou um valor menor do que 0 no valor do ingresso!')
              #ingresso = float(input('Digite o valor do ingresso novamente(O VALOR DEVE SER MAIOR OU IGUAL A 0): '))
            else:
              break
          except:
            print('-------------------------ATENÇÃO ERRO!---------------------------------------')
            print('ERRO: Você digitou alguma letra ou caracter especial, lembre-se de que caso queira indicar as casas decimais use o "." no lugar da ","!')

        #CRIANÇAS
        while True:
          try:
            qtdKid = int(input('Digite a quantidade de crianças: '))
            if qtdKid < 0:
              print('-------------------------ATENÇÃO ERRO!---------------------------------------')
              print('ERRO: Você digitou a quantidade menor do que 0 na quantidade de crianças!')
            else:
              break
          except:
            print('-------------------------ATENÇÃO ERRO!---------------------------------------')
            print('ERRO: Você digitou alguma letra ou caracter especial, lembre-se também de digitar um numero inteiro!')

        #JOVENS
        while True:
          try:
            qtdJovens = int(input('Digite a quantidade de jovens: '))
            if qtdJovens < 0:
              print('-------------------------ATENÇÃO ERRO!---------------------------------------')
              print('ERRO: Você digitou a quantidade menor do que 0 na quantidade de jovens!')
            else:
              break
          except:
            print('-------------------------ATENÇÃO ERRO!---------------------------------------')
            print('ERRO: Você digitou alguma letra ou caracter especial, lembre-se também de digitar um numero inteiro!')

        #ALIMENTOS
        while True:
          try:
            qtdAlimentos = int(input('Digite quantos kgs inteiros de alimentos foram arrecadados:'))
            if qtdAlimentos < 0:
              print('-------------------------ATENÇÃO ERRO!---------------------------------------')
              print('ERRO: Você digitou a quantidade menor do que 0 na quantidade de alimento arrecadado!')
            else:
              break
          except:
            print('-------------------------ATENÇÃO ERRO!---------------------------------------')
            print('ERRO: Você digitou alguma letra ou caracter especial, lembre-se também de digitar um numero inteiro!')

        #INTEIRA
        while True:
          try:
            qtdInteira = int(input('Digite quantas pessoas compraram o ingresso inteiro: '))
            if qtdInteira < 0:
              print('-------------------------ATENÇÃO ERRO!---------------------------------------')
              print('ERRO: Você digitou a quantidade menor do que 0 na quantidade de ingressos inteiros!')
            else:
              break
          except:
            print('-------------------------ATENÇÃO ERRO!---------------------------------------')
            print('ERRO: Você digitou alguma letra ou caracter especial, lembre-se também de digitar um numero inteiro!')

        pessoasTotal, valorTotal = jogofutebol(ingresso, qtdKid, qtdJovens, qtdAlimentos)

        print(f'Quantidade de pessoas: {pessoasTotal} \nValor arrecadado: R${valorTotal:.2f}\nForam arrecados {qtdAlimentos} kgs de alimento não perecível')