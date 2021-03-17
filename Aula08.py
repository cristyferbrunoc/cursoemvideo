from math import trunc, hypot, cos, sin, tan
from random import randint
import pygame


class Aula08:
    def desafio016(self):
        print("{:*^20} Programar para mostrar somente a Parte inteira {:*^20}".format("", ""))
        numero = float(input("Digite o numero: "))
        print(f"A parte inteira é {trunc(numero)}")

    def desafio017(self):
        print("{:*^20} Programa para Calcular a Hipotenusa de um Triangulo {:*^20}".format("", ""))
        catetoadjacente = float(input("Digite o Cateto Adjacente: "))
        catetooposto = float(input("Digite o Cateto Oposto: "))
        print(f"A hipotenusa desse triangulo é {hypot(catetooposto, catetoadjacente)}")

    def desafio018(self):
        print("{:*^20} Programa calcula seno, conceno e tangente {:*^20}".format("", ""))
        numero = int(input("Digite o numero: "))
        print(f"O Consseno é {cos(numero)}, Seno {sin(numero)} e Tangente {tan(numero)}")

    def desafio019(self):
        print("{:*^20} Programa Sorteio Aluno {:*^20}".format("", ""))
        sorteio = randint(1, 4)
        if (sorteio == 1):
            print("João")
        elif (sorteio == 2):
            print("Maria")
        elif (sorteio == 3):
            print("Pedrinho")
        elif (sorteio == 4):
            print("Paulo")

    def desafio020(self):
        print("{:*^20} Programa tocar Musica!!! {:*^20}".format("", ""))
        pygame.init()
        pygame.mixer.music.load('aula.mp3')
        pygame.mixer.music.play()
        pygame.event.wait()
