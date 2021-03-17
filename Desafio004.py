class Desafio004:
    def somarNumeros(self):
        numeroUm = int(input("Digite o primairo numero: "))
        numeroDois = int(input("Digite o segundo numero: "))
        somar = numeroUm + numeroDois
        print(f"A soma dos numeros {numeroUm} + {numeroDois} é = {somar}")

    def mostraInformacao(self):
        valor = input("Digite qualquer coisa: ")
        if (valor.isalnum()):
            print("É um Alfa Numerico")
        elif (valor.isalpha()):
            print("É Alfabetico")
        else:
            print("Desconheço")
