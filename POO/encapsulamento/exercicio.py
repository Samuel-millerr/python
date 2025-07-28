# Sistema de conta bancária com segurança de acesso
import os
import time
from datetime import datetime

class ContaBancaria():
    def __init__(self, titular: str, senha: str, saldo: float = 0):
        self.__titular = titular
        self.__senha = senha
        self.__saldo = saldo

    @property
    def get_user(self):
        return self.__titular
    
    @property
    def get_key(self):
        return self.__senha
    
    def depositar(self, valor: float):
        try: 
            if not valor < 0:
                self.__saldo += valor
                print(f"O valor de {valor} foi depositado!!") 
            else:
                print("O valor a ser depositado precisa ser maior que R$ 0!")
        except:
            print("Erro no processamento! Contate o banco.")

    # Criação do método de autenticação, será utilizado para realizar as operações seguintes, sacar, ver_saldo, alterar senha
    def _autenticar(self, titular: str, senha: str) -> bool:
        if titular == self.__titular and senha == self.__senha: 
            return True
        else: 
            return False
        
    def ver_saldo (self, titular: str, senha: str):
        try:
            auth = self._autenticar(titular, senha)
            if auth:
                print(f"R$ {self.__saldo}")
            else:
                print("Acesso negado! Titular ou senha incorretas.")
        except:
            print("Erro no processamento! Contate o banco.")    

    def sacar(self, titular: str, senha: str, valor: float):
        try:
            auth = self._autenticar(titular, senha)
            if auth:
                if valor < 1: print("Valor inválido!! O valor a ser sacado precisa ser maior que R$ 0.")
                elif valor > self.__saldo: print("Valor inválido!! O valor a ser sacado é maior do que o existente na conta.")
                else: 
                    self.__saldo -= valor
                    print(f"Foi sacado R$ {valor} de sua conta!")
        except:
            print("Erro no processamento! Contate o banco.")
    
    def alterar_senha(self, titular: str, senha: str, nova_senha):
        try:
            auth = self._autenticar(titular, senha)
            
            if auth and senha == self.__senha:
                self.__senha = nova_senha
                print("Senha alterada com sucesso!")
            else:
                print("Acesso negado! Titular ou senha incorretas.")
        except:
            print("Erro no processamento! Contate o banco.")

def clear():
    return os.system('cls' if os.name == 'nt' else 'clear')

# Declaração de variaveis globais
data_inicial = datetime.now().strftime("%d/%m/%Y")
horario_inicial = datetime.now().strftime("%H:%M")
conta = ContaBancaria("teste", "1234")

# Criação da interface do banco
print(f"{data_inicial} -- Sessão iniciada às {horario_inicial}")
print("Seja bem vindo!! Você está no banco AXIUS!")
print("Antes de continuar entre com sua conta ou crie uma: ")
while True: 
    user_input = input("[ 1 ] Entrar na conta \n[ 2 ] Criar conta \n[ 0 ] Sair do sistema \n > ").strip() 

    if user_input == "1":
        clear()
        print("Insira as informações para realizar o login.")
        titular = input("Titular: ").strip()
        senha = input("Senha: ").strip() 
        if titular == conta.get_user and senha == conta.get_key:
            while True:
                print(f"Acesso liberado! As seguintes opções estão abertas à você {titular}:")
                print("[ 1 ] Depositar valor \n[ 2 ] Ver saldo\n[ 3 ] Sacar valor \n[ 4 ] Alterar senha \n[ 0 ] Sair da conta") 
                user_input = input(" > ").strip()
                if user_input == "1":
                    clear()
                    print("=== DEPOSITO ===")
                    valor = float(input("Digite o valor que você deseja depositar: "))
                    conta.depositar(valor)
                    time.sleep(3.5)
                elif user_input == "2":
                    clear()
                    print("=== SALDO ===")
                    conta.ver_saldo(titular, senha)
                    time.sleep(3.5)
                elif user_input == "3":
                    clear()
                    valor = float(input("Digite o valor que você deseja sacar: "))
                    conta.sacar(titular, senha, valor)
                    time.sleep(3.5)
                    clear()
                elif user_input == "4":
                    clear()
                    print("=== ALTERAR SENHA ===")
                    senha = input("Digite a senha atual: ")
                    nova_senha = input("Digite a nova senha: ")
                    conta.alterar_senha(titular, senha, nova_senha)  
                    time.sleep(3.5)
                elif user_input == "0":
                    clear()
                    print("Você acaba de sair da conta!")
                    break
                else:
                    clear()
                    print("Nenhuma das opções foi selecionada, tente novamente!")
        else:
            clear()
            print("Conta não encontrada ou não criada.")
    elif user_input == "2":
        clear()
        print("Para criar uma conta é necessário definir a usuário e senha: ")
        titular = input("Titular da conta: ").strip() 
        senha = input("Senha: ").strip()
        conta = ContaBancaria(titular, senha)
        print("Conta criada!! Para acessar as funcionalidades, realize o login.")
    elif user_input == "0":
        print("Até logo! Tenha um bom dia.")
        break
    else:
        print("Nenhuma das opções foi selecionada, tente novamente!")