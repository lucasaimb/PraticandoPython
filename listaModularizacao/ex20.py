def contracheque(salarioBruto, dependentes):
    # DESCONTOS
    inss = 0.11 * salarioBruto
    planoSaude = 0.02 * salarioBruto
    descontoT = inss + planoSaude

    # BENEFICIOS
    valeAlimentacao = 1212 + ((0.05 * salarioBruto) * dependentes)

    # RESULTADOS
    salarioLiquido = salarioBruto - inss - planoSaude

    return descontoT, salarioLiquido, valeAlimentacao

#MENU
while True:
    print('='*25+'MENU DO PROGRAMA'+'='*25)
    escolha = input('Para rodar o programa digite [1]\nPara sair do programa digite qualquer outra tecla!\nDigite sua escolha: ')
    if escolha != '1':
        print('Você saiu do programa, até mais!')
        break
    else:
        print('='*25+'PROGRAMA INICIADO'+'='*25)
        #ENTRADAS
        while True:
            try:
                salarioBruto = float(input('Digite o salário bruto: '))
                if salarioBruto < 600 or salarioBruto > 500000:
                    print('ERRO: Digite um salário de R$600,00 a R$500000,00 reais.')
                else:
                    break
            except:
                print('ERRO: Você digitou uma letra, um caracter especial ou então o salário em uma formatação inválida! Lembre-se de usar o "." invés da "," para representar a casa decimal.')

        while True:
            try:
                dependentes = int(input('Digite o numero de dependentes: '))
                if dependentes < 0:
                    print('ERRO: Você digitou uma quantidade de dependentes menor do que 0!')
                else:
                    break
            except:
                print('ERRO: Você digitou uma letra, um caracter especial ou então uma quantidade de dependentes em valor quebrado!')

        descontoT, salarioLiquido, valeAlimentacao = contracheque(salarioBruto, dependentes)
        print(f'Com os descontos de INSS e plano de saúde totalizando em R${descontoT:.2f}\n'
        f'o salário líquido do funcionário é de R${salarioLiquido:.2f} mais o beneficio do\nvale alimentação totalizados em R${valeAlimentacao:.2f}.')
        print(f'Salário líquido + beneficios: R${(salarioLiquido + valeAlimentacao):.2f}')