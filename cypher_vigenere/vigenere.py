"""
Este cypher toma un mensaje y una clave, siendo la clave una string. 
Lo que hace es usar los indices de la clave para hacer offset en los indices del mensaje, haciendo que sea muy dificil de crackear
si no se tiene la clave.
Se recorre letra por letra y se usa la clave letra por letra tambien. Cuando se acaba la clave se empieza desde el principio de la misma nuevamente.
"""

abcedario = 'abcdefghijklmñnopqrstuvwxyz'
largo_abc = len(abcedario)

def vigenere(mensaje, clave):
    largo_clave = len(clave)
    #seteo el indice primero de la clave para empezar desde esa primera letra con el cifrado
    index_clave = 0
    mensaje_cifrado = ""
    for letra in mensaje:
        #si hay un espacio debo agregarlo
        if letra == " ":
            mensaje_cifrado += " "
        else:
            #uso a la letra actual de la clave para shiftear a la letra del mensaje
            #es necesario usar modulo para no pasarme de los indices de la clave y empezar desde el principio
            #cuando el index_clave aumente mas alla de la cantidad de letras de la clave
            letra_clave = clave[index_clave % largo_clave]
            #busco la posicion que ocupa esta letra en el abcedario. Eso me dara el nuevo shifteo
            shifteo = abcedario.find(letra_clave)
            #busco la posicion de la letra del mensaje en el abcedario
            index_letra = abcedario.find(letra)
            #obengo la letra shifteada. Debo hacer modulo el largo del abcedario para no pasarme
            letra_cifrada = abcedario[(index_letra + shifteo) % largo_abc]
            #agrego la letra cifrada al mensaje cifrado
            mensaje_cifrado += letra_cifrada
            #aumento el indice de la clave para usar la proxima letra de la misma en la siguiente iteracion
            index_clave += 1
            
    return mensaje_cifrado

mensaje = "ave vigenere loco"
clave = "abc"
mensaje_cifrado = vigenere(mensaje, clave)
print(mensaje_cifrado)
"""
Parece que funciona bien porque en los lugares donde se usa la a como letra de la clave para el shifteo las letras del mensaje original se mantienen igual,
es decir, hay un shifteo de 0, pues es la posicion que ocupa la a en el abcedario.
"""
