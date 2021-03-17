from random import randint


def desafio28():
    pensamento = randint(0, 5)

    numero = int(input('Digite um Numero: '))
    print("Voce acertou!!!" if numero == pensamento else f'Voce Errou!!! o numero era {pensamento}')


def desafio29():
    velocimetro = int(input('Digite a Velocidade: '))
    if velocimetro > 80:
        print('Você foi multado. O valor da multa é: {} R$.'.format((velocimetro - 80) * 7))
    else:
        print('Você não recebeu a Multa.')


def desafio30():
    numero = int(input('Digite o numero: '))
    print('Esse numero é Par.' if numero % 2 == 0 else 'Esse numero é Impar.')


def desafio31():
    distancia = int(input('Digite a Distancia da Velocidade: '))
    if distancia <= 200:
        print('Você ira pagar {:.2f} R$'.format(float(distancia * 0.5)))
    else:
        print('Você irá pagar 0.45 por cada Km. O valor da Viagem é {:.2f} R$'.format(float(distancia * 0.45)))


def desafio32():
    ano = int(input('Digite o Ano: '))
    print('Bissexto' if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0) else print('Não é bissexto'))


def desafio33():
    lista = []
    for i in range(3):
        numero = int(input('Digite o número: '))
        lista.append(numero)
    lista.sort()
    print(lista[0])
    lista.sort(reverse=True)
    print(lista[0])


def desafio34():
    salario = float(input('Digite o salario: '))
    if salario <= 1250:
        print('O aumento foi de {:.2f} R$'.format(salario * 0.15))
    else:
        print('O aumento foi de {:.2f} R$'.format(salario * 0.1))


def desafio35():
    medidaA = float(input('Digite o lado A: '))
    medidaB = float(input('Digite o lado B: '))
    medidaC = float(input('Digite o lado C: '))

    if (medidaA + medidaB > medidaC and medidaB + medidaC > medidaA and medidaA + medidaC > medidaB):
        print('Essa medida forma um Triangulo')
    else:
        print('Essa medida não forma um Triangulo')


desafio35()
