from PyQt5 import QtCore, uic, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QAction, QApplication, QLabel, QMenu, QTextEdit, QVBoxLayout,QPushButton,QSlider
from PIL import Image
import acoes


imagem_inicial = 'inicial_image.jpg'
infos = 'Ui\img_info.png'
options = acoes.imagem_init(imagem_inicial)

################################################################################################################################################################################################
#Metodos da Janela Principal

def gamma(value):
    global options
    options = acoes.gamma_turn(value)
    acoes.set_gamma(GAMMA)
    Imagem1.setPixmap(QPixmap(options).scaled(941, 471))
    Imagem_princ_mensagem.setPixmap(QPixmap(options).scaled(411, 451))


def transparencia(value):
    global options
    options = acoes.transparencia(value)
    Imagem1.setPixmap(QPixmap(options).scaled(941, 471))
    Imagem_princ_mensagem.setPixmap(QPixmap(options).scaled(411, 451))


def save_image():
    global options
    arquivo = Image.open(options)
    filename, _ = QtWidgets.QFileDialog.getSaveFileName(caption = 'Salvando Imagens',
                                                        directory = '',
                                                        filter = 'Todos os Arquivos (*.*);;Imagens(*png;*jpg;*.ppm;*.pgm);;PNG(*png);;Text files (*.txt)',
                                                        initialFilter= 'PNG(*png)')
    arquivo.save(filename)

def rotacionar_imagem_90():
    global options
    image = Image.open(options)
    image = image.transpose(Image.ROTATE_90)
    image.save('Resultado\Final.png')
    options = 'Resultado\Final.png'
    Imagem1.setPixmap(QPixmap(options).scaled(941, 471))
    Imagem_princ_mensagem.setPixmap(QPixmap(options).scaled(411, 451))

def rotacionar_imagem_270():
    global options
    image = Image.open(options)
    image = image.transpose(Image.ROTATE_270)
    image.save('Resultado\Final.png')
    options = 'Resultado\Final.png'
    Imagem1.setPixmap(QPixmap(options).scaled(941, 471))
    Imagem_princ_mensagem.setPixmap(QPixmap(options).scaled(411, 451))


def espelhar_horizontal():
    global options
    image = Image.open(options)
    image = image.transpose(Image.FLIP_LEFT_RIGHT)
    image.save('Resultado\Final.png')
    options = 'Resultado\Final.png'
    Imagem1.setPixmap(QPixmap(options).scaled(941, 471))
    Imagem_princ_mensagem.setPixmap(QPixmap(options).scaled(411, 451))

def espelhar_vertical():
    global options
    image = Image.open(options)
    image = image.transpose(Image.FLIP_TOP_BOTTOM)
    image.save('Resultado\Final.png')
    options = 'Resultado\Final.png'
    Imagem1.setPixmap(QPixmap(options).scaled(941, 471))
    Imagem_princ_mensagem.setPixmap(QPixmap(options).scaled(411, 451))

def reset():
    global imagem_inicial,options
    options = imagem_inicial
    options = acoes.imagem_init(options)
    TRANSPARENCIA.setValue(255)
    GAMMA.setValue(10)
    Imagem1.setPixmap(QPixmap(imagem_inicial).scaled(941, 471))
    Imagem_princ_mensagem.setPixmap(QPixmap(options).scaled(411, 451))

def process(num):
    global options
    opcao = int(num)
    options = acoes.process(opcao)
    Imagem1.setPixmap(QPixmap(options).scaled(941, 471))
    Imagem_princ_mensagem.setPixmap(QPixmap(options).scaled(411, 451))

def escolher_imagem():
    global imagem_inicial,options
    filename, _ = QtWidgets.QFileDialog.getOpenFileName(caption = 'Buscando Imagens',
                                                        directory = '',
                                                        filter = 'Todos os Arquivos (*.*);;Imagens(*png;*jpg;*.ppm;*.pgm)',
                                                        initialFilter= 'Imagens(*png;*jpg;*.ppm;*.pgm)')
    imagem_inicial = filename
    options = imagem_inicial
    att_img_info(options)
    options = acoes.imagem_init(options)
    Imagem1.setPixmap(QPixmap(imagem_inicial).scaled(941, 471))
    Imagem_princ_mensagem.setPixmap(QPixmap(options).scaled(411, 451))


def inserir_mensagem_oculta():
    global options
    text =Input_msg.toPlainText()
    Input_msg.setText('')
    options = acoes.inserir_msg(options,text)
    Imagem1.setPixmap(QPixmap(options).scaled(941, 471))
    Imagem_princ_mensagem.setPixmap(QPixmap(options).scaled(411, 451))


def buscar_msg_oculta():
    global options
    text = acoes.buscar_msg_img(options)
    Output_msg.setText(str(text))


###################################################################################################################################################################################
#Função Atualizar Informações da Imagem

def att_img_info(img):
    picture = Image.open(img)
    tamanho = picture.size
    img_name = img.split(".")
    name = "n"
    img_name2 = str(img_name[0])

    if img_name2.find("/"):
        name = img_name2.split("/")
    elif img_name2.find("\\"):
        name = img_name2.split("\\")
    elif img_name2.find("//"):
        name = img_name2.split("//")

    Nome_Img.setText("Nome : "+str(name[len(name)-1]))
    Tamanho_Img.setText("Tamanho : altura("+str(tamanho[1])+") x largura("+str(tamanho[0])+")")
    Tipo_Img.setText("Tipo : "+str(img_name[len(img_name)-1]))


###################################################################################################################################################################################
#Janela Principal

if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication([])

    window = uic.loadUi("Ui\layout.ui")

    Imagem1 = window.findChild(QLabel, 'img1')
    Imagem1.setPixmap(QPixmap(imagem_inicial).scaled(941, 471))

    Info = window.findChild(QLabel, 'info')
    Info.setPixmap(QPixmap(infos).scaled(471, 321))
    Info.setVisible(False)

#MENU ARQUIVOS
    Arquivos = window.findChild(QMenu, 'menuArquivos')

    Abrir_Imagem = window.findChild(QAction, 'abrir_imagem')
    Abrir_Imagem.triggered.connect(escolher_imagem)

    Salvar_Imagem = window.findChild(QAction, 'actionSalvar_Imagem')
    Salvar_Imagem.triggered.connect(save_image)

    Fechar_App = window.findChild(QAction, 'fechar_app') 
    Fechar_App.triggered.connect(lambda: app.quit())

#MENU TRANSFORMAÇÕES
    Transformacoes = window.findChild(QMenu, 'menuTransformacoes')

    #Blur
    Aplicar_Efeito = window.findChild(QAction, 'actionBlour')
    Aplicar_Efeito.triggered.connect(lambda: process(1))

    #Contour
    Contour = window.findChild(QAction, 'actionContour')
    Contour.triggered.connect(lambda: process(2))

    #Cor Negativa
    Aplicar_Negativo = window.findChild(QAction, 'actionCor_Ngeativa')
    Aplicar_Negativo.triggered.connect(lambda: process(3))

    #Detail
    Detail = window.findChild(QAction, 'actionDetail')
    Detail.triggered.connect(lambda: process(4))

    #Detecção Bordas
    Deteccao = window.findChild(QMenu, 'deteccao')
    
    Find_Edges = window.findChild(QAction, 'actionFind_Edges')
    Find_Edges.triggered.connect(lambda: process(5))
    
    Deteccao_Basica = window.findChild(QAction, 'godeteccao')
    Deteccao_Basica.triggered.connect(lambda: process(6))
    
    Deteccao_Padrao = window.findChild(QAction, 'actionDetec_o_Padr_o')
    Deteccao_Padrao.triggered.connect(lambda: process(7))
    
    Deteccao_Avancada = window.findChild(QAction, 'actionDetec_o_Avan_ada')
    Deteccao_Avancada.triggered.connect(lambda: process(8))

    #Edges
    Edge_Menu = window.findChild(QMenu, 'menuEdge')

    Enhance = window.findChild(QAction, 'actionEnhance')
    Enhance.triggered.connect(lambda: process(9))

    Enhance_More = window.findChild(QAction, 'actionEnhance_More')
    Enhance_More.triggered.connect(lambda: process(10))

    #Emboss
    Emboss = window.findChild(QAction, 'actionEmboss')
    Emboss.triggered.connect(lambda: process(11))

    #Cinza
    Cinza = window.findChild(QAction, 'actionEscala_de_Cinza')
    Cinza.triggered.connect(lambda: process(12))

    #Logaritmica
    Logaritmica = window.findChild(QAction, 'actionLogar_tmica')
    Logaritmica.triggered.connect(lambda: process(13))

    #Preto Branco
    Preto_Branco = window.findChild(QAction, 'actionPreto_e_Branco')
    Preto_Branco.triggered.connect(lambda: process(14))

    #Camadas RGB
    Separar_RGB = window.findChild(QMenu, 'menuSeparar_Camadas_RGB')
    
    Separar_Vermelho = window.findChild(QAction, 'actionCamada_Vermelha')
    Separar_Vermelho.triggered.connect(lambda: process(15))
    
    Separar_Verde = window.findChild(QAction, 'actionCamada_Verde')
    Separar_Verde.triggered.connect(lambda: process(16))
    
    Separar_Azul = window.findChild(QAction, 'actionCamada_Azul')
    Separar_Azul.triggered.connect(lambda: process(17))

    #Sharpen
    Sharpen = window.findChild(QAction, 'actionSharpen')
    Sharpen.triggered.connect(lambda: process(18))

    #Smooth
    Smooth = window.findChild(QMenu, 'menuSmooth')
    
    Smooth_Basic = window.findChild(QAction, 'actionBasic')
    Smooth_Basic.triggered.connect(lambda: process(19))

    Smooth_More = window.findChild(QAction, 'actionSmooth_More')
    Smooth_More.triggered.connect(lambda: process(20))

#MENU OPÇÕES

    OPÇÕES = window.findChild(QVBoxLayout, 'menu_vertical')
    TITULO_MENU = window.findChild(QLabel, 'label_titulo')
    ROTACIONAR_DIREITA = window.findChild(QPushButton, 'direita')
    ROTACIONAR_DIREITA.clicked.connect(rotacionar_imagem_270)
    ROTACIONAR_ESQUERDA = window.findChild(QPushButton, 'esquerda')
    ROTACIONAR_ESQUERDA.clicked.connect(rotacionar_imagem_90)
    RESETAR = window.findChild(QPushButton, 'resetar')
    RESETAR.clicked.connect(reset)
    ESPELHAR_VERTICAL = window.findChild(QPushButton, 'espelharver')
    ESPELHAR_VERTICAL.clicked.connect(espelhar_vertical)
    ESPELHAR_HORIZONTAL = window.findChild(QPushButton, 'espelharh')
    ESPELHAR_HORIZONTAL.clicked.connect(espelhar_horizontal)
    MENSAGENS_OCULTAS = window.findChild(QPushButton, 'msg_oculta')
    MENSAGENS_OCULTAS.clicked.connect(lambda: window_mensagens.show() )

    TRANSPARENCIA = window.findChild(QSlider, 'transparencia')
    TRANSPARENCIA.valueChanged.connect(lambda:transparencia(TRANSPARENCIA.value()))

    GAMMA = window.findChild(QSlider, 'gamma')
    GAMMA.valueChanged.connect(lambda:gamma(GAMMA.value()))
    acoes.set_gamma(GAMMA.value())

#MENU INFORMAÇÕES

    Sobre_Menu = window.findChild(QMenu, 'menuSobre')

    Info_App = window.findChild(QAction, 'actionInforma_es_do_App')
    Info_App.triggered.connect(lambda: window_info_app.show())

    Info_Imagem = window.findChild(QAction, 'actionInforma_es_da_Imagem')
    Info_Imagem.triggered.connect(lambda: window_Info_img.show())


##################################################################################################################################################################
#Janela Mensagens Ocultas

    
    mensagens = QApplication([])
    window_mensagens = uic.loadUi("Ui\imagem.ui")

    Imagem_princ_mensagem = window_mensagens.findChild(QLabel, 'Imagem_principal')
    Imagem_princ_mensagem.setPixmap(QPixmap(imagem_inicial).scaled(411, 451))

    Titulo_buscar = window_mensagens.findChild(QLabel, 'titulo_procurar')
    Titulo_inserir = window_mensagens.findChild(QLabel, 'titulo_inserir')
    Output_msg = window_mensagens.findChild(QLabel, 'Outpu_mensagem')
    

    Input_msg = window_mensagens.findChild(QTextEdit, 'Input_text')
    
    Salvar_nova = window_mensagens.findChild(QPushButton, 'salvar')
    Salvar_nova.clicked.connect(save_image)

    Procurar_msg = window_mensagens.findChild(QPushButton, 'procurar')
    Procurar_msg.clicked.connect(buscar_msg_oculta)

    Inserir_msg = window_mensagens.findChild(QPushButton, 'enviar_msg')
    Inserir_msg.clicked.connect(inserir_mensagem_oculta)


##################################################################################################################################################################
#Janela Info_App

    
    Informacao_App = QApplication([])
    window_info_app = uic.loadUi("Ui\info_App.ui")



##################################################################################################################################################################
#Janela Info_Imagem

    
    Informacao_Img = QApplication([])
    window_Info_img = uic.loadUi("Ui\info_Img.ui")

    Nome_Img = window_Info_img.findChild(QLabel, 'label_2')
    Tipo_Img = window_Info_img.findChild(QLabel, 'label')
    Tamanho_Img = window_Info_img.findChild(QLabel, 'label_4')
    att_img_info(imagem_inicial)

######################################################################################################################################################################################################
#Execução das Janelas
    window_mensagens.hide()
    window_info_app.hide()
    window_Info_img.hide()
    window.show()
    Informacao_App.exec_()
    Informacao_Img.exec_()
    mensagens.exec_()
    app.exec_()