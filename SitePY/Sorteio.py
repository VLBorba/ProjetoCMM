from Cadastro import listanome #Importa a lista para poder sortear um nome dela
from random import choice #biblioteca usada para escolher um elemento aleatório
escolha = input('Deseja sortear alguém? ').lower().split()[0]
if escolha[0] == 's':
    print('\033[1;36mA pessoa sorteada foi {}.\033[m'.format(choice(listanome)))
elif escolha[0] == 'n':
    print('\033[1;35mVolte a qualquer hora!\033[m')
else:
    print('Não entendi sua resposta.')
