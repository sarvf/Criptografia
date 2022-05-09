# # la realizacion de la tarea fue en conjunto con:
# Felipe Ulloa e Iman jarufe, por lo que es posible que 
# los codigos se parescan bastante, dado que fue realizado entre los 3 al mismo tiempo(Trabajo en equipos Rules)
def ASCIItoHEX(ascii):   
    hexa = ""
    for i in range(len(ascii)):
        ch = ascii[i]
        in1 = ord(ch)
        part = hex(in1).lstrip("0x").rstrip("L")
        hexa += part
    return hexa
def stringHexToHex(char):
    if(char=='a'):return 10
    elif(char=='b'):return 11
    elif(char=='c'):return 12
    elif(char=='d'):return 13
    elif(char=='e'):return 14
    elif(char=='f'):return 15
    else: return int(char)
def ConstruirMatriz(hexLlave,indices):
    NorepeatHexllave=[]
    universoMatriz=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    matriz=[['','','',''],['','','',''],['','','',''],['','','','']]
    cnt=0

    #Agregamos la primera vez de aparicion de un hex en la llave y lo eliminamos del universo de caracteres de la matriz del MAL  
    for OneHex in hexLlave:   
        if (NorepeatHexllave.count(OneHex)==0):
            NorepeatHexllave.append(OneHex)
            universoMatriz.pop(universoMatriz.index(OneHex))
        
    #Ya con los hex de la llave sin repetir y quitados del universo de posibilidades de caracteres de la matriz, se procede a llenar los primeros elementos de la matriz, con los hex sin repetir, y luego con los elementos del universo que quedaron en orden secuencial.
    for x in range(4):#Filas
        for j in range(4):#Columnas
            if (cnt >=len(NorepeatHexllave)):
                matriz[x][j]= universoMatriz.pop(0)
                indices[stringHexToHex(matriz[x][j])]=[x,j]
            else:
                matriz[x][j]= NorepeatHexllave[cnt]
                indices[stringHexToHex(matriz[x][j])]=[x,j]
                cnt+=1
    return matriz 


def desplazamiento(FilaColumna1, FilaColumna2):
    if(FilaColumna1[0] == FilaColumna2[0] and FilaColumna1[1] != FilaColumna2[1]):
        return "V"
    elif(FilaColumna1[0] != FilaColumna2[0] and FilaColumna1[1] == FilaColumna2[1]):
        return "H"
    else:
        return "D" 



def CifrarMensaje(matriz,indices,mensaje):
    
    # 1.-Pasar Mensaje ASCII a Lista de String hex
    # Ciclo por cada par de hex de la lista
    # 2.-Para cada caracter ASCII, 2hex, Buscar los indices de cada hex (con la matriz indices)
    # 4.-A partir de los indices buscar que operacion se debe realizar deplazamiento()
    # 5.-Operar los indices segun la operacion, Ej: Diagonal indicesHex1=+1Fila -1 Columna, indicesHex2=-1Fila +1 Columna 
    # 6.-Para evitar indices fueras de rango, convertiremos las coordenadas a la matriz del Mal extendida, y ahi se buscaran el hex cifrado
    # 7.-Retorna el valor de la matriz(hex) que apunta los indices operados  
    index=0
    MessageHexList=ASCIItoHEX(mensaje)
    MatrizExtendida=HexMatrizExtendida(matriz)
    textoCifrado=""
    print(matriz)
    print('\nIndices : ', indices)
    print('\nMensajeHex : ', MessageHexList ,'\n')
    print('\nMatrix extendida:', MatrizExtendida, '\n')
    for OneParHex in range(int(len(MessageHexList)/2)):
        #FilaColumna -> FC
        FCFirstHex=indices[stringHexToHex(MessageHexList[index])]
        FCSecondHex=indices[stringHexToHex(MessageHexList[index+1])]
        desp=desplazamiento(FCFirstHex, FCSecondHex)
        print('Par Hex mensaje :[', MessageHexList[index], MessageHexList[index+1], '] Indices HexMensajes: ', FCFirstHex,FCSecondHex,  ' => Desplazamiento: ', desp)
        
        index+=2
        if(desp=="D"):
            #Operamos los indices de forma Diagonal
            FCFirstHexCifrado=[FCFirstHex[0]-1,FCFirstHex[1]-1]
            FCSecondHexCifrado=[FCSecondHex[0]+1,FCSecondHex[1]+1]
        elif(desp=="V"):
            FCFirstHexCifrado=[FCFirstHex[0]-1,FCFirstHex[1]]
            FCSecondHexCifrado=[FCSecondHex[0]+1,FCSecondHex[1]]
        elif(desp=="H"):
            FCFirstHexCifrado=[FCFirstHex[0],FCFirstHex[1]-1]
            FCSecondHexCifrado=[FCSecondHex[0],FCSecondHex[1]+1]

        #Conversion coordenadas del MAL a MALextendida
        FCFirstHexCifrado=[FCFirstHexCifrado[0]+1, FCFirstHexCifrado[1]+1]
        FCSecondHexCifrado=[FCSecondHexCifrado[0]+1, FCSecondHexCifrado[1]+1]

        #Obtemos los hex encriptados y los agregamos al mensaje cifrado
        textoCifrado+=MatrizExtendida[FCFirstHexCifrado[0]][FCFirstHexCifrado[1]]+MatrizExtendida[FCSecondHexCifrado[0]][FCSecondHexCifrado[1]]+" "

        print( 'IndicesDesplazados y en Extendida: ',FCFirstHexCifrado, FCSecondHexCifrado, 'Hex Cifrado: ',textoCifrado,'\n' )
    return textoCifrado

def HexMatrizExtendida(matriz):
    matrizExtendida=[["","","","","",""],["","","","","",""],["","","","","",""],["","","","","",""],["","","","","",""],["","","","","",""]]
    #LLenamos las esquinas de los bordes
    matrizExtendida[0][0]=matriz[3][3]
    matrizExtendida[0][5]=matriz[3][0]
    matrizExtendida[5][0]=matriz[0][3]
    matrizExtendida[5][5]=matriz[0][0]
    #Llenamos el resto de bordes
    for b1 in range(4):
        matrizExtendida[0][b1+1]=matriz[3][b1]
        matrizExtendida[b1+1][0]=matriz[b1][3]
        matrizExtendida[5][b1+1]=matriz[0][b1]
        matrizExtendida[b1+1][5]=matriz[b1][0]

    #LLenamos el resto con la matriz del MAL
    for i in range(4):  
        for j in range(4):
            matrizExtendida[i+1][j+1]=matriz[i][j]
    
    return matrizExtendida

if __name__ == "__main__":

    file1 = open('./LlaveMensajeDelMal.txt')
    LlaveDelMal = file1.readline()
    MensajeDelMal = file1.readline()
    indices2=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    print(CifrarMensaje(ConstruirMatriz(ASCIItoHEX(LlaveDelMal),indices2), indices2,MensajeDelMal))