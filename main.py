import time
import os
from arte import Logo
from api import *
distacia = 130
os.system('cls')

def carregando():
    def progress_bar(done):
        print("\rProgresso: [{0:50s}] {1:.1f}%".format('=' * int(done * 50), done * 100),end='')

    def test():
        for n in range(101):
            progress_bar(n/100)
            time.sleep(0.01)


    test()

linha = '_' * distacia
espaço1 = '\n\n\n'
espaço2 = '\n\n'
tempo = 0
sleep = 5
Logo(tempo, distacia)
time.sleep(1)
descriptar = '(de - descriptar)'
encriptar = '(en - encriptar )'
enc = '\n'+encriptar.center(distacia, ' ')
des = '\n'+descriptar.center(distacia, ' ')
perg = 'Você que "ENCRIPTAR" OU "DESCRIPTAR"?'
opcao = str(input('\n'+perg.center(distacia, ' ')+'\n'+enc+des+'\n\n\n===> '))
def opção_en():
    os.system('cls')
    if opcao == 'en':
        print(linha.center(distacia)+espaço1+'ENCRIPTADOR'.center(distacia)+espaço2+linha.center(distacia)+espaço1)
        chave = input(espaço1+'Você tem uma chave?(S/N)\n\n===> ')
        if chave =='N' or chave =='n':
            global finalkey
            finalkey = criar()
            print(espaço1+finalkey.center(distacia)+espaço2)
            message = str(input(espaço1+'Qual o texto que você gostaria de encriptar?\n\n\n===>'))
            print(espaço2)
            carregando()
            message_encrypt = encrypt(message,finalkey)
            print(espaço1+'Texto encriptado:'.center(distacia)+espaço2+message_encrypt.center(distacia)+espaço2)
            time.sleep(sleep)
        elif chave == 'S' or chave == 's':
            inkey = input(espaço1+'Qual chave você gostaria de ultilizar para encriptar?\n\n\n===>')
            msg = str(input(espaço1+'Qual o texto que você gostaria de encriptar?\n\n\n===>'))
            print(espaço2)
            carregando()
            final_msg = encrypt(msg,inkey)
            print(espaço1+'Texto encriptado:'.center(distacia)+espaço2+final_msg.center(distacia)+espaço2)
            time.sleep(sleep)

        else:
            return False

    

def opção_de():
    if opcao == 'de':
        os.system('cls')
        print(linha.center(distacia)+espaço1+'DESCRIPTADOR'.center(distacia)+espaço2+linha.center(distacia)+espaço1)
        inkey = input(espaço1+'Qual chave você gostaria de ultilizar para decriptar?\n\n\n===>')
        msg = str(input(espaço1+'Qual o texto que você gostaria de decriptar?\n\n\n===>'))
        print(espaço2)
        carregando()
        decrypt_msg = decrypt(msg,inkey)
        print(espaço1+'Texto decriptado:'.center(distacia)+espaço2+decrypt_msg.center(distacia)+espaço2)
        time.sleep(sleep)



if opção_en() == False:
    os.system('cls')
    print(linha.center(distacia)+espaço1+'Opção invalida.'.center(distacia)+espaço2+linha.center(distacia)+espaço1)
    time.sleep(2)
    while opção_en() == False:
        os.system('cls')
        print(linha.center(distacia)+espaço1+'Opção invalida.'.center(distacia)+espaço2+linha.center(distacia)+espaço1)
        time.sleep(2)
        opção_en()

if opção_de() == False:
    os.system('cls')
    print(linha.center(distacia)+espaço1+'Opção invalida.'.center(distacia)+espaço2+linha.center(distacia)+espaço1)
    time.sleep(2)
    while opção_en() == False:
        os.system('cls')
        print(linha.center(distacia)+espaço1+'Opção invalida.'.center(distacia)+espaço2+linha.center(distacia)+espaço1)
        time.sleep(2)
        opção_de()
