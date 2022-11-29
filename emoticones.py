seguirChateando = True
while seguirChateando:
    texto = input(':>')
    if texto == 'salir':
        seguirChateando=False
    texto = texto.replace(':)', '😊')
    texto = texto.replace(':(', '😞')
    texto = texto.replace(':*', '😘')
    texto = texto.replace(':P', '😛')
    texto = texto.replace(':o', '😱')
    texto = texto.replace('xd', '🤣')
    texto = texto.replace(':D', '😁')
    print(texto)

