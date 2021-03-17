class Desafio005:
    def antecessorSucessor(self):
        numero = int(input("Digite o numero: "))
        print("{:*^20} Programa de Sucessor e Antecessor {:*^20}".format("", ""))
        print(f"{numero - 1} {numero} {numero + 1}")

    def dobloTliploRaiz(self):
        print("{:*^20} Programa Calcular Doblo, Tlipo e Raiz {:*^20}".format("", ""))
        numero = int(input("Digite o numero: "))
        print(f"O doblo é {numero ** 2} "
              f"\nO Tlipo é {(numero ** 2) * numero} "
              f"\nA Raiz é {numero ** (1 / 2)}")

    def mediaAluno(self):
        print("{:*^20} Programa da Média dos Alunos {:*^20}".format("", ""))
        notaUm = float(input("Digite a primeira Nota: "))
        notaDois = float(input("Digite a segunda Nota: "))
        print(f"A média é {(notaUm + notaDois) / 2}")

    def centimetroMinimetro(self):
        print("{:*^20}  Programa Converter Metro para Centimetro e Milimetro {:*^20}".format("", ""))
        metro = float(input("Digite o Metro: "))
        print(f"A conversão para Centimetro é {metro * 100}\n"
              f"A Conversão para Milimetro é {(metro * 100) * 10}")

    def tabuada(self):
        print("{:*^20} Programa tabuada de um numero Qualquer {:*^20}".format("", ""))
        numero = int(input("Digite o numero: "))

        for i in range(11):
            print(f"{numero} x {i} = {numero * i}")

    def dolar(self):
        print("{:$^20} Quantos Dolar o Real pode Comprar {:$^20}".format("", ""))
        real = float(input("Digite o valor do Dinheiro: "))
        print("Você pode comprar {:.2f} Dolar".format(real / 5.37), end=' ')
        print(f'com R$ {real}')

    def metrosQuadrado(self):
        print("{:*^20} Programar calcular quantidade de tinta Metros Quadrado {:*^20}".format("", ""))
        altura = float(input("Digite a Altura da Parede: "))
        largura = float(input("Digite a Largura da Parede: "))

        print(f"A quantidade de tinta usada para pintar essa parede é {(altura * largura) / 2} Litros por m².")

    def desconto(self):
        print("{:$^20} Programa para Calcular o Desconto {:$^20}".format("", ""))
        valor = float(input("Digite o valor: "))
        print(f"O valor de desconto com 5% é {valor - (valor * 0.05)}")

    def salario(self):
        print("{:*^20} Programa Aumento de Salario {:*^20}".format("", ""))
        valorSalario = float(input("Digite seu Salario: "))
        print(f"Seu salario com o aumento é {valorSalario + (valorSalario * 0.15)}")
