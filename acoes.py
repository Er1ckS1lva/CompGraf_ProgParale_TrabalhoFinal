from os import urandom
import os
from PIL import Image, ImageFilter
from hashlib import sha256
import subprocess
import math

letras = ['','0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
size_largura = 0
picture = None
gamma = 1

######################################################################################################################################################################
#Função de Controle de Transformações
def process(number):
    option = int(number)
    global picture

    if option == 1:
        picture = blur()
    
    elif option == 2:
        picture = contour()
    
    elif option == 3:
        picture = negativo()
    
    elif option == 4:
        picture = detail()

    elif option == 5:
        picture = find_edges()

    elif option == 6:
        picture = deteccao_basica()

    elif option == 7:
        picture = deteccao_padrao()

    elif option == 8:
        picture = deteccao_avancada()

    elif option == 9:
        picture = edge_enhance()
    
    elif option == 10:
        picture = edge_enhance_more()

    elif option == 11:
        picture = emboss()
    
    elif option == 12:
        picture = cinza()

    elif option == 13:
        picture = logaritmica()

    elif option == 14:
        picture = preto_branco()

    elif option == 15:
        picture = rgb_vermelho()

    elif option == 16:
        picture = rgb_verde()

    elif option == 17:
        picture = rgb_azul()

    elif option == 18:
        picture = sharpen()

    elif option == 19:
        picture = smooth()

    elif option == 20:
        picture = smooth_more()
    
    return picture

######################################################################################################################################################################
#Transformações Possíveis

def imagem_init(imagem):
    global picture
    picture = Image.open(imagem)
    bands = picture.getbands()       
    if type(bands) == tuple:
        picture = picture.convert('RGBA')
    picture.save('Resultado\Final.png')
    picture = 'Resultado\Final.png'
    return picture


def blur():
    print('blur')
    global picture
    picture = Image.open(picture)
    picture = picture.filter(ImageFilter.BLUR)
    picture.save('Resultado\Final.png')
    picture = 'Resultado\Final.png'
    return picture


def contour():
    global picture
    picture = Image.open(picture)
    picture = picture.filter(ImageFilter.CONTOUR)
    picture.save('Resultado\Final.png')
    picture = 'Resultado\Final.png'
    return picture


def negativo():
    global picture
    picture = Image.open(picture)       
    matriz = picture.load()
    for i in range(picture.size[0]):
        for j in range(picture.size[1]):
            r = 255 - matriz[i,j][0]
            g = 255 - matriz[i,j][1]
            b = 255 - matriz[i,j][2]
            matriz[i,j] = (r,g,b)
    picture.save('Resultado\Final.png')
    picture = 'Resultado\Final.png'
    return picture


def detail():
    global picture
    picture = Image.open(picture)
    picture = picture.filter(ImageFilter.DETAIL)
    picture.save('Resultado\Final.png')
    picture = 'Resultado\Final.png'
    return picture


def find_edges():
    global picture
    picture = Image.open(picture)
    alpha = 0    
    matriz = list(picture.getdata())
    for x, y in enumerate(matriz):
        alpha = y[3]
        matriz[x] = (y[0],y[1],y[2])
                
    newPicture = Image.new('RGB', picture.size)
    newPicture.putdata(matriz)
    newPicture = newPicture.filter(ImageFilter.FIND_EDGES)
    newPicture.save('Resultado\Final.jpg')
        
    matriz = list(newPicture.getdata())
    for x, y in enumerate(matriz):
        matriz[x] = (y[0],y[1],y[2],alpha)
        
    newPicture2 = Image.new('RGBA', newPicture.size)
    newPicture2.putdata(matriz)
    newPicture2.save('Resultado\Final.png')
    picture = 'Resultado\Final.png'
    return picture


def deteccao_basica():
    global picture
    picture = Image.open(picture)
    alpha = 0
    kernel_basico = ImageFilter.Kernel((3,3),(1,0,-1,0,0,0,-1,0,1),1,0)    
    matriz = list(picture.getdata())
    for x, y in enumerate(matriz):
        alpha = y[3]
        matriz[x] = (y[0],y[1],y[2])
                
    newPicture = Image.new('RGB', picture.size)
    newPicture.putdata(matriz)
    newPicture = newPicture.filter(kernel_basico)
    newPicture.save('Resultado\Final.jpg')
        
    matriz = list(newPicture.getdata())
    for x, y in enumerate(matriz):
        matriz[x] = (y[0],y[1],y[2],alpha)
        
    newPicture2 = Image.new('RGBA', newPicture.size)
    newPicture2.putdata(matriz)
    newPicture2.save('Resultado\Final.png')
    picture = 'Resultado\Final.png'
    return picture


def deteccao_padrao():
    global picture
    picture = Image.open(picture)
    alpha = 0
    kernel_padrao = ImageFilter.Kernel((3,3),(0,1,0,1,-4,1,0,1,0),1,0) 
    matriz = list(picture.getdata())
    for x, y in enumerate(matriz):
        alpha = y[3]
        matriz[x] = (y[0],y[1],y[2])
                
    newPicture = Image.new('RGB', picture.size)
    newPicture.putdata(matriz)
    newPicture = newPicture.filter(kernel_padrao)
    newPicture.save('Resultado\Final.jpg')
        
    matriz = list(newPicture.getdata())
    for x, y in enumerate(matriz):
        matriz[x] = (y[0],y[1],y[2],alpha)
        
    newPicture2 = Image.new('RGBA', newPicture.size)
    newPicture2.putdata(matriz)
    newPicture2.save('Resultado\Final.png')
    picture = 'Resultado\Final.png'
    return picture


def deteccao_avancada():
    global picture
    picture = Image.open(picture)
    alpha = 0
    kernel_avancado = ImageFilter.Kernel((3,3),(-1,-1,-1,-1,8,-1,-1,-1,-1),1,0)
    matriz = list(picture.getdata())
    for x, y in enumerate(matriz):
        alpha = y[3]
        matriz[x] = (y[0],y[1],y[2])
                
    newPicture = Image.new('RGB', picture.size)
    newPicture.putdata(matriz)
    newPicture = newPicture.filter(kernel_avancado)
    newPicture.save('Resultado\Final.jpg')
        
    matriz = list(newPicture.getdata())
    for x, y in enumerate(matriz):
        matriz[x] = (y[0],y[1],y[2],alpha)
        
    newPicture2 = Image.new('RGBA', newPicture.size)
    newPicture2.putdata(matriz)
    newPicture2.save('Resultado\Final.png')
    picture = 'Resultado\Final.png'
    return picture
 

def edge_enhance():
    global picture
    picture = Image.open(picture)
    picture = picture.filter(ImageFilter.EDGE_ENHANCE)
    picture.save('Resultado\Final.png')
    picture = 'Resultado\Final.png'
    return picture


def edge_enhance_more():
    global picture
    picture = Image.open(picture)
    picture = picture.filter(ImageFilter.EDGE_ENHANCE_MORE)
    picture.save('Resultado\Final.png')
    picture = 'Resultado\Final.png'
    return picture


def emboss():
    global picture
    picture = Image.open(picture)
    picture = picture.filter(ImageFilter.EMBOSS)
    picture.save('Resultado\Final.png')
    picture = 'Resultado\Final.png'
    return picture
    

def cinza():
    global picture
    picture = Image.open(picture)
    matriz = picture.load()
    for i in range(picture.size[0]):
        for j in range(picture.size[1]):
            r = matriz[i,j][0]
            g = matriz[i,j][1]
            b = matriz[i,j][2]
            cinza = int((r+g+b)/3)
            matriz[i,j] = (cinza, cinza, cinza)
    picture.save('Resultado\Final.png')
    picture = 'Resultado\Final.png'
    return picture


def logaritmica():
    global picture,gamma
    picture = Image.open(picture)
    matriz = picture.load()

    gamma = (math.log(1+gamma))
     
    for i in range(picture.size[0]):
        for j in range(picture.size[1]):
            r = int((matriz[i,j][0]/255) ** gamma * 255)
            g = int((matriz[i,j][1]/255) ** gamma * 255)
            b = int((matriz[i,j][2]/255) ** gamma * 255)
            matriz[i,j] = (r,g,b)

    picture.save('Resultado\Final.png')
    picture = 'Resultado\Final.png'
    return picture


def preto_branco():
    global picture
    picture = Image.open(picture)
    var = 128
    filterr = lambda x : 255 if x > var else 0
    picture = picture.convert('L').point(filterr, mode='1')
    picture.save('Resultado\Final.png')
    picture = 'Resultado\Final.png'
    return picture


def rgb_vermelho():
    global picture
    picture = Image.open(picture)
    matriz = picture.load()
    for i in range(picture.size[0]):
        for j in range(picture.size[1]):
            r = matriz[i,j][0]
            g = 0
            b = 0
            matriz[i,j] = (r, g, b)
    picture.save('Resultado\Final.png')
    picture = 'Resultado\Final.png'
    return picture


def rgb_verde():
    global picture
    picture = Image.open(picture)
    matriz = picture.load()
    for i in range(picture.size[0]):
        for j in range(picture.size[1]):
            r = 0
            g = matriz[i,j][1]
            b = 0
            matriz[i,j] = (r, g, b)

    picture.save('Resultado\Final.png')
    picture = 'Resultado\Final.png'
    return picture


def rgb_azul():
    global picture
    picture = Image.open(picture)
    matriz = picture.load()
    for i in range(picture.size[0]):
        for j in range(picture.size[1]):
            r = 0
            g = 0
            b = matriz[i,j][2]
            matriz[i,j] = (r, g, b)

    picture.save('Resultado\Final.png')
    picture = 'Resultado\Final.png'
    return picture


def sharpen():
    global picture
    picture = Image.open(picture)
    picture = picture.filter(ImageFilter.SHARPEN)
    picture.save('Resultado\Final.png')
    picture = 'Resultado\Final.png'
    return picture


def smooth():
    global picture
    picture = Image.open(picture)
    picture = picture.filter(ImageFilter.SMOOTH)
    picture.save('Resultado\Final.png')
    picture = 'Resultado\Final.png'
    return picture


def smooth_more():
    global picture
    picture = Image.open(picture)
    picture = picture.filter(ImageFilter.SMOOTH_MORE)
    picture.save('Resultado\Final.png')
    picture = 'Resultado\Final.png'
    return picture


def transparencia(value):
    global picture
    picture = Image.open(picture)
    transp = int(value)
    bands = picture.getbands()
    if type(bands) == tuple:
        picture = picture.convert('RGBA')
    
    matriz = list(picture.getdata())

    for x, y in enumerate(matriz):
        matriz[x] = (y[0],y[1],y[2],transp)
    
    newPicture = Image.new('RGBA', picture.size)
    newPicture.putdata(matriz)
    newPicture.save('Resultado\Final.png')
    picture = 'Resultado\Final.png' 
    return picture


def inserir_msg(imagem,txt):

    global letras, size_largura

    picture = Image.open(imagem)
    bands = picture.getbands()
    
    if type(bands) == tuple:
        picture = picture.convert('RGBA')
    
    matriz = list(picture.getdata())
    size_largura = int(len(matriz)/2)

    TXT_ENCODED = txt.encode(encoding='UTF-8',errors='strict')
    caracteres = list(sha256(TXT_ENCODED.rstrip()).hexdigest())

    alpha = matriz[1][3]
    #print(caracteres)
    for x, y in enumerate(matriz):
        if x == size_largura:           
           for i in range(len(caracteres)):
                for j in range(len(letras)):
                    if letras[j] == caracteres[i]:                       
                        num = int(alpha-j)                                             
                        matriz[x+i] = (y[0],y[1],y[2],num)

    for x, y in enumerate(matriz):
        if (x != 1)and(x<size_largura)and(x>size_largura+100):  
            valor = urandom.randint(1, 3)
            if valor == 1:   # 30% de chance de qualquer pixel fora os não permitidos terem uma letra aleatoria oculta      
                letra = urandom.randint(20, 26)                       
                num = int(alpha-letra)                                             
                matriz[x] = (y[0],y[1],y[2],num)
                                            
    newPicture = Image.new('RGBA', picture.size)
    newPicture.putdata(matriz)
    newPicture.save('Resultado\Final.png')
    picture = 'Resultado\Final.png'
    return picture


def buscar_msg_img(imagem):
    global letras, size_largura

    picture = Image.open(imagem)
    bands = picture.getbands()
    if type(bands) == tuple:
        picture = picture.convert('RGBA')

    matriz = list(picture.getdata())
    size_largura = int(len(matriz)/2)
    
    alpha = matriz[1][3]
    txt = []
    possivel_letra = []
    i =1
    for x in range(len(matriz)):       
        if x == size_largura:
            for y in range(64):
                valor = int(alpha - matriz[x+y][3])
                possivel_letra.append(valor)

    
    for j in range(len(possivel_letra)):
        for i in range(len(letras)):
            if i == int(possivel_letra[j]):
                txt.append(letras[i])
    
    hash = ''.join(txt)
    
    command = "java -jar Trabalho_Final.jar "+str(hash)
    return subprocess.getoutput(command)


def gamma_turn(value):

    number = int(value)/10
    global picture

    picture = Image.open(picture)
    matriz = picture.load()

    gamma = number

    for i in range(picture.size[0]):
        for j in range(picture.size[1]):
            r = int((matriz[i,j][0]/255) ** gamma * 255)
            g = int((matriz[i,j][1]/255) ** gamma * 255)
            b = int((matriz[i,j][2]/255) ** gamma * 255)
            matriz[i,j] = (r,g,b)

    picture.save('Resultado\Final.png')
    picture = 'Resultado\Final.png'
    return picture

def set_gamma(value):
    global gamma
    gamma = value