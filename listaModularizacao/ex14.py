def valorEstacionamento(horaEntra, minutoEntra, horaSai, minutoSai):
    if horaSai == 0 and minutoSai == 0:
        horaSai = 24

    horasTotais = int(horaSai) - int(horaEntra)
    minutosTotais = int(minutoSai) - int(minutoEntra)

    if (minutosTotais < 0):
        horasTotais -= 1
        minutosTotais = 60 + minutosTotais

    valorPagar = horasTotais * 7

    return horasTotais, minutosTotais, valorPagar

#HORARIO DE ENTRADA
while True: #TRATAMENTO DE ERRO
    try:
        horarioEntra = input("Digite o horario de entrada em (HH:MM): ")
        horaEntra, minutoEntra = horarioEntra.split(":")                                                          #SEPARANDO A HORA E MINUTO EM 2 VARIAVEIS
        horaEntra, minutoEntra = int(horaEntra), int(minutoEntra)                                                 #TRANSFORMANDO AS VARIAVEIS STRINGS EM INT
        if horaEntra < 0 or horaEntra > 24 or minutoEntra < 0 or minutoEntra > 59:
            print('ERRO: Você digitou um horario inválido. Tente inserir a hora de (0-23) e um minuto de (0-59)!')
        else:
            break
    except:
        print('ERRO: Você digitou uma letra, um caracter especial ou um formato de hora diferente de (HH:MM).')
#HORARIO DE SAÍDA
while True: #TRATAMENTO DE ERRO
    try:
        horarioSai = input("Digite o horario de saida em (HH:MM): ")
        horaSai, minutoSai = horarioSai.split(":")                                                                #SEPARANDO A HORA E MINUTO EM 2 VARIAVEIS
        horaSai, minutoSai = int(horaSai), int(minutoSai)                                                         #TRANSFORMANDO AS VARIAVEIS STRINGS EM INT
        if horaSai < 0 or horaSai > 24 or minutoSai < 0 or minutoSai > 59:
            print('ERRO: Você digitou um horario inválido. Tente inserir a hora de (0-23) e um minuto de (0-59)!')
        else:
            if (horaSai < horaEntra and horaSai != 0) or ((horaSai == horaEntra) and (minutoSai < minutoEntra and minutoSai != 0)):
                print('ERRO: Você digitou a hora de saida mais cedo que a de entrada!')
            elif (horaSai == horaEntra) and (minutoSai == minutoEntra) and (horaSai != 0 and horaEntra != 0 and minutoEntra != 0 and minutoSai != 0):
                print('ERRO: Você digitou a hora de saida igual a hora de entrada!')
            else:
                break
    except:
        print('ERRO: Você digitou uma letra, um caracter especial ou um formato de hora diferente de (HH:MM).')



horasTotais, minutosTotais, valorPagar = valorEstacionamento(horaEntra, minutoEntra, horaSai, minutoSai)

print(f"Você ficou {horasTotais} horas e {minutosTotais} minutos no estacionamento.")
print(f'Você deve pagar o total de R${valorPagar:.2f} reais.')
