import re
from abc import ABC, abstractmethod

class Transporte(ABC):
    @abstractmethod
    def iniciar_viagem(self):
        pass

    @abstractmethod
    def finalizar_viagem(self, distancia_km: float):
        pass
        
    @property
    @abstractmethod
    def tipo(self):
        pass

class Onibus(Transporte):
    def __init__(self, nome: str):
        self.nome = nome

    def iniciar_viagem(self):
        self.inicio_viagem = input("Digite o horário do início da viagem: ")

        if re.match(r"^\d{2}\.\{2}$", self.iniciar_viagem):
            print("horário válido")
        else:
            print("horário inválido")
    def finalizar_viagem(self, distancia_km: float):
        self.distancia_km = distancia_km
        self.fim_viagem = input("Digite o horário do fim da viagem: ")
        self.valor_viagem = 4.5

    @property
    def tipo(self):
        return self.nome

def mostrar_informações(transporte: object):
    transporte.iniciar_viagem()
    transporte.finalizar_viagem(100)
    
    print(f"O transporte escolhido foi {transporte.nome}")

    print(f"A viagem começou as {transporte.inicio_viagem} horas e finalizou às {transporte.fim_viagem}")
    print(f"O valor da viagem total foi de R$ {transporte.valor_viagem}")

onibus = Onibus("Onibus")
mostrar_informações(onibus)