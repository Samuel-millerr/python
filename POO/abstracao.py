""" Abstração se consiste na criação de atributos específicos que são obrigatorios para as classes que a herdam,
servem como forma de garantir que as classes possuam um certo metódo."""

from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def go(self):
        pass

    @property
    @abstractmethod
    def stop(self):
        pass

class Carro(Veiculo):
    
    def go(self):
        print("Você ta dirigindo um carro!")

    @property
    def stop(self):
        return "Você parou o carro!"

carro = Carro()
print(carro.stop)