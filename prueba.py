letras = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ.,?"!'
cadena = "hola mundo".upper()  #para las mayusculas
simbolos = ['·—','—···','—·—·','————','—··','·','··—·','——·','····','··','·———','—·—','·—··','——','—·','——·——','———','·——·','——·—','·—·','···','—','··—','···—','·——','—··—','—·——','——··','—————','·————','··———','···——','····—','·····','—····','——···','———··','————·','·—·—·—','—·—·——','··——··','·—··—·','——··——']
posicion = 0
for letra in cadena:
    while posicion < len(letras):
        l = letras[posicion]
        if l == letra:
            break
        posicion += 1
    if posicion == len(letras):
        print ("no encontrado")
    else:
        #obtener simbolo morse de posicion = posicion
        pass
        print("{}: {}".format, (letra, simbolos[posicion]))