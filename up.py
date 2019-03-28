#creditos reservados para leonardo e jorge gabriel
import os


def menu():
    c = True
    while c == True:
        print('Bem vindo!')
        print('')
        print('0 - Sair')
        print('1 - Atualizar Sistema')
        print('2 - Instalar Software')
        print('3 - Informação Sistema')
        print('4 - Cria Pasta')
        print('5 - Navegar em Pastas')
        print('')
        r = int(input('Opção : '))
        print('')
        if r == 1:
            atualiza()
        elif r == 2:
            instalar()
        elif r == 3:
            info()
        elif r == 4:
            criapasta()
        elif r == 5:
            navegapasta()
        elif r == 0:
            c = False



def atualiza():
    print(25*'-'+'COMANDO'+25*'-')
    print('')
    print('Comando para coletar Atualizar o sistema : apt upgrade')
    print('')
    print(25*'-'+'INFORMAÇÃO COMANDO'+25*'-')
    print('')
    desc = os.system('apt --help')
    print('')
    print(25*'-'+'ATUALIZAÇÃO'+25*'-')
    print('')
    x = os.system('sudo apt-get update')
    y = os.system('sudo apt-get upgrade')

def instalar():
    print(25*'-'+'COMANDO'+25*'-')
    print('')
    print('Comando para coletar info do sistema : apt install nomedoapp')
    print('')
    print(25*'-'+'INFORMAÇÃO COMANDO'+25*'-')
    print('')
    desc = os.system('apt --help')
    print('')
    print(25*'-'+'INFORMAÇÕES'+25*'-')
    print('')
    app = input('apt install :  ')
    g = os.system('sudo apt install {}'.format(app))

def info():
    print(25*'-'+'COMANDO'+25*'-')
    print('')
    print('Comando para coletar info do sistema : uname -a')
    print('')
    print(25*'-'+'INFORMAÇÃO COMANDO'+25*'-')
    print('')
    desc = os.system('uname --help')
    print('')
    print(25*'-'+'INFORMAÇÕES'+25*'-')
    print('')
    inf = os.system('uname -a')

def criapasta():
    print(25*'-'+'COMANDO'+25*'-')
    print('')
    print('Comando para criar Pasta : mkdir nomedapasta')
    print('')
    print(25*'-'+'INFORMAÇÃO COMANDO'+25*'-')
    print('')
    desc = os.system('mkdir --help')
    print('')
    print(25*'-'+'CRIANDO A PASTA'+25*'-')
    print('')
    fol = str(input('mkdir : '))
    cria = os.system('mkdir {}'.format(fol))

def navegapasta():
        print(25*'-'+'COMANDO'+25*'-')
        print('')
        print('Comando para criar Pasta : cd nomedapasta')
        print('')
        print(25*'-'+'INFORMAÇÃO COMANDO'+25*'-')
        print('')
        desc = os.system('cd --help')
        print('')
        print(25*'-'+'NAVEGANDO EM PASTAS'+25*'-')
        print('')
        fol = str(input('cd : '))
        cria = os.system('cd {}'.format(fol))


menu()
