#El cypher del cesar consiste en un cypher en el cual se toma en cuenta la posicion de las letras en el abecedario,
#y todas se mueven en cierta cantidad de posiciones, todas tienen el mismo shifteo con respecto a la posicion
#de la letra original

abcedario = 'abcdefghijklmñnopqrstuvwxyz'
largo_abc = len(abcedario)

def cesar(shifteo, mensaje):
    mensaje_cifrado = ""
    for letra in mensaje:
        #debemos tener cuidado de escapar el espacio del medio
        if letra == " ":
            mensaje_cifrado += " "
        else:
            #busco la posicion de la letra en el abecedario y obtengo la letra que le sigue shiteada cierta cantidad de posiciones
            index = abcedario.find(letra)
            #debo calcular el modulo del resultado con el abecedario, para no pasarme de largo
            new_index = (index + shifteo) % largo_abc
            #la letra cifrada es
            letra_cifrada = abcedario[new_index]
            #agrego la nueva letra cifrada al mensaje
            mensaje_cifrado += letra_cifrada
            
    return mensaje_cifrado

mensaje = "ave cesarz"
shifteo = 3
mensaje_cifrado = cesar(shifteo, mensaje)
print(mensaje_cifrado)
