
import sys
sys.path.append('./scripts/funcoes.py')
import funcoes  
from colorama import Fore, Back, Style, init

init() # Inicio do Môdulo colorama # 

#Programa Principal

inicio = 0
optionlist = [1, 2 , 3 , 4, 5]

while inicio not in  optionlist: #Basicamente o loop aplicado verifica se o número digitato está na "optionlist"# 

  funcoes.exibir_menu()# Mostra o menu de opções  # 
 
  user = (int(input(f'Digite sua opção {chr(187)} '))) # Pede ao usuário que digite um opção #

  if user == 1:
    a,b = funcoes.obter_numeros()
    resultado = funcoes.soma(a,b)
    print(f'Resultado:{resultado}')

  elif user == 2:
    a,b = funcoes.obter_numeros()
    resultado = funcoes.subtracao(a, b)
    print(f'Resultado:{resultado}')

  elif user == 3:
    a,b = funcoes.multiplicar()
    resultado = funcoes.multiplicar(a, b)
    print(f'Resultado:{resultado}')

  elif user == 4:
    a,b = funcoes.obter_numeros()
    resultado = funcoes.divisao(a, b)
    print(f'Resultado:{resultado}')
    
  elif user == 5:
    print(Fore.RED + 'Saindo do Programa...' + Style.RESET_ALL)
    inicio = 5
  else:
    print(f"Opção Inválida! Tente novamente.\n")



  