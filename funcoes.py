from colorama import Fore, Back, Style, init
init()
def exibir_menu():
    print('-=-'*15)
    print('\tCalculadora Simples'.upper())
    print('-=-'*15)
    print(Fore.RED + 'Escolha a operação que você deseja realizar:' + Fore.RESET)
    print('\t1 - Adição')
    print('\t2 - Subtração')
    print('\t3 - Multiplicação')
    print('\t4 - Divisão')
    print('\t5 - Sair do Programa')
   
def obter_numeros(a=None, b=None):
    if a is None:
        try:
            a = int(input('Digite um Número: '))
        except ValueError:
            print("Por favor, digite um número válido.")
            return None, None

    if b is None:
        try:
            b = int(input('Digite outro Número: '))
        except ValueError:
            print("Por favor, digite um número válido.")
            return None, None

    return a, b
def soma(a,b):
    return (a + b)

def subtracao(a, b):
    return (a - b)

def multiplicar (a, b):
    return (a * b)

def divisao (a, b):
    return  (a/b)
