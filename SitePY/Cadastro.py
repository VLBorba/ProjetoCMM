listanome = []
listaperfil = [] #Criada as listas vazias para adicionar as variáveis
continuar = ' ' #Criado a variável vazia para iniciar o while
print('\033[1;35m='*40)
print('{:^40}'.format('CADASTRO CASA MENINA MULHER'))#Print para centralizar a String
print('='*40)
while True:
    continuar = input('\033[mDeseja adicionar cadastros? ').lower().split()[0]#Joga para minusculo evitando erros caso do usuario e retirar espaços caso ele aperte
    if continuar[0] == 's': #Pega a primeira letra do 'Sim com [0]'
        nome = (input('Digite o nome: '))
        sobrenome = input('Digite o sobrenome: ')
        responsável = input('Digite o nome do responsável: ')
        inscrição = input('Digite a inscrição: ')
        idade = int(input('Digite a idade: '))
        cpf = input('Digite o CPF(Se não houver digite 0): ')
        print('-'*40)
        listanome.append(nome + ' ' + sobrenome)
        listaperfil.append(nome + ' ' + sobrenome + '-' + responsável + ' ' + inscrição + ' ' + cpf) #Ambas são listas para juntar as variáveis como se fosse um perfil
    elif continuar[0] == 'n': #Caso o usuário deseja parar, só digitar 'Não' e o programa se encerra
        break
perfil = [nome, sobrenome, idade, responsável, inscrição, cpf]
print('-'*40)
print(f'A ultima pessoa no cadastro é \033[1;31m{perfil}\033[m') #Mostra as variáveis da ultima pessoa cadastrada
