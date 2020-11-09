from time import sleep
import string
import random
import string
import re
import base64
finalkey = ''
def criar():
    prek1 = ['a','b','c','d','e',]
    prek2 = ['a','b','c','d','e',]
    prek3 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x,','y','z']
    global finalKey
    random.shuffle(prek1)
    random.shuffle(prek2)
    random.shuffle(prek3)
    prek1 = str(prek1)
    prek1 = prek1.replace(',','')
    prek1 = prek1.replace(' ','')
    prek1 = prek1.replace("'",'')
    prek1 = prek1.strip("['']")
    prek2 = str(prek2)
    prek2 = prek2.replace(',','')
    prek2 = prek2.replace(' ','')
    prek2 = prek2.replace("'",'')
    prek2 = prek2.strip("['']")
    prek3 = str(prek3)
    prek3 = prek3.replace(',','')
    prek3 = prek3.replace(' ','')
    prek3 = prek3.replace("'",'')
    prek3 = prek3.strip("['']")
    numkey = str.maketrans(prek1,prek2)
    #print('\n\nA sua chave completa é: %s-%s'%(numkey, prek3) )
    encodedkey = '%s-%s'%(numkey, prek3)
    encodedBytes = base64.b64encode(encodedkey.encode("utf-8"))
    finalKey = str(encodedBytes, "utf-8")
    return finalKey



def encrypt(mensagem,chave):
    decodedBytes = base64.b64decode(chave)
    decodedStr = str(decodedBytes, "utf-8")

    input_key = decodedStr.split('-')
    numK, letterK = input_key[0], input_key[1]
    print (mensagem)
    encode = ''
    for i in mensagem:
        position = letterK.find(i)
        newposition = (position+5)%26
        encode += letterK[newposition]
    print(encode)
    mensagem_cript2 = encode.translate(numK)
    return mensagem_cript2

def decrypt(mensagem,chave):
    decodedBytes = base64.b64decode(chave)
    decodedStr = str(decodedBytes, "utf-8")

    input_key = decodedStr.split('-')
    numK, letterK = input_key[0], input_key[1]

    decode = ''
    mensagem_decrypt = mensagem.translate(numK)

    for i in mensagem_decrypt:
        pos = letterK.find(i)
        newpos = (pos-5)%26
        decode += letterK[newpos]
    return decode


