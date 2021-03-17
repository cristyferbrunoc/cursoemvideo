from Aula08 import Aula08
from Desafio004 import Desafio004
from Desafio005 import Desafio005

if __name__ == '__main__':
    desafio = input("Digite o numero do desafio: ")

    if (desafio == "004"):
        questao = input("Digite a questão: ")
        if (questao == "somar"):
            Desafio004().somarNumeros()
        elif (questao == "informação"):
            Desafio004.mostraInformacao(self=2)
    elif (desafio == "005"):
        questao = input("Digite a questão: ")
        if (questao == "sucessor"):
            Desafio005().antecessorSucessor()
        elif (questao == "doblo"):
            Desafio005.dobloTliploRaiz(self=1)
        elif (questao == "nota"):
            Desafio005.mediaAluno(self=0)
        elif (questao == "conversão"):
            Desafio005.centimetroMinimetro(self=0)
        elif (questao == "tabuada"):
            Desafio005.tabuada(self=0)
        elif (questao == "dolar"):
            Desafio005.dolar(self=0)

        elif (questao == "metros"):
            Desafio005.metrosQuadrado(self=0)
        elif (questao == "desconto"):
            Desafio005.desconto(self=0)
        elif(questao == "salario"):
            Desafio005.salario(self=0)
        else:
            print("Valor não reconhecido")
    elif (desafio == 'Aula08'):
        questao = input("Digite o Exercicio: ")
        if(questao == "016"):
            Aula08.desafio016(self=0)
        elif(questao == "017"):
            Aula08.desafio017(self=1)
        elif (questao == "018"):
            Aula08.desafio018(self=2)
        elif questao == "019":
            Aula08.desafio019(self=3)
        elif questao == '020':
            Aula08.desafio020(self=6)

