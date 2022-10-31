'''
----------------------------------------EXERCICIO 15------------------------------------------------
Crie uma função e seu protótipo que determine 𝐴𝑛 e 𝑆𝑛 de uma Progressão Geométrica (P.G). Após
isso, use a função 50 vezes para calcular os dados de 50 P.G's com valores de 𝑎 , e lidos do usuário.
'''
import math
def pg(a, q, n):
    an = a * math.pow(q, (n-1))
    sn = (a * (math.pow(q, n) - 1)) / (q - 1)
    return an, sn
i = 0

for i in range(1, 51, 1):
    print('='*25+f'{i}º PG'+'='*25)
    i += 1
    while True:
        try:
            a = float(input('Digite o primeiro termo da P.G: '))
            q = float(input('Digite a razão da P.G: '))
            n = float(input('Digite a quantidade de termos: '))
            an, sn = pg(a, q, n)
            break
        except:
            print('='*25+'ATENÇÃO ERRO'+'='*25)
            print('ERRO: Erro de digitação, você digitou alguma letra, caracter especial ou um numero não suportavel.\nINSIRA OS DADOS NOVAMENTE...')
    print(f'O enésimo termo da P.G é: {an:.1f}\n'
          f'A soma dos termos da P.G resulta em: {sn:.1f}')
