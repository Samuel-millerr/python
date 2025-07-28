""" Encapsulamento é a prática dentro de orientação a objeto serve para a proteção de dados específicos, dados
sensíveis por exemplo. Usado para controlar o acesso em determinados dados do sistema."""

"""
_ ; Privado, porém com a recomendação de não ser acessado - protected
__ ; Totalmente privada, sem possibilidade de mudança ou acesso - private
"""

class BaseDados:
    def __init__(self): #Inicialização do "construtor"
        self.__dados = {}

    @property
    def get_dados(self):
        return self.__dados
    
    def post_client(self, id, nome):
        if "clientes" not in self.__dados:
            self.__dados["clientes"] = {id: nome}
        else:
            self.__dados["clientes"].update({id: nome})

    def get_clients(self):
        for key, value in self.__dados["clientes"].items():
            print(key, value)
            
    def delete_client(self, id):
        del self.__dados["clientes"][id]

bd = BaseDados()
bd.post_client(1, "Otávio")
bd.post_client(2, "Pedro")
bd.post_client(3, "Samuel")
print(bd.get_dados)


