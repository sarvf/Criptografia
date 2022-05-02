def hexadecimalToDecimal(hexval):
    length = len(hexval)
    base = 1
    dec_val = 0
    for i in range(length - 1, -1, -1):
        if hexval[i] >= '0' and hexval[i] <= '9':
            dec_val += (ord(hexval[i]) - 48) * base
            base = base * 16
        elif hexval[i] >= 'A' and hexval[i] <= 'F':
            dec_val += (ord(hexval[i]) - 55) * base
            base = base * 16
    return dec_val
def stringHex(char):
    if(char != 'a' and char != 'b'and char != 'c'and char != 'd'and char != 'e'and char != 'f'):
        return int(char)
    else:
        if(char=='a'):
            return 10
        if(char=='b'):
            return 11
        if(char=='c'):
            return 12
        if(char=='d'):
            return 13
        if(char=='e'):
            return 14
        if(char=='f'):
            return 15
def ASCIItoHEX(ascii):   
    hexa = ""
    for i in range(len(ascii)):
        ch = ascii[i]
        in1 = ord(ch)
        part = hex(in1).lstrip("0x").rstrip("L")
        hexa += part
    return hexa
def hexToASCII(hexx):
    ascii=""
    for i in range(0, len(hexx), 2):
        part = hexx[i : i + 2]
        ch = chr(int(part, 16))
        ascii += ch
    return ascii
def ConstruirMatriz(h,indices):
    llave=[""]
    llave.clear()
    x=j=0
    hexL=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    matriz=[['','','',''],['','','',''],['','','',''],['','','','']]
    cnt=0
    e=0
    for letter in h:
        if (llave.count(letter)==0):
            llave.append(letter)
            hexL.pop(hexL.index(letter))
    for x in range(4):
        for j in range(4):
            if (cnt >=len(llave)):
                # print("if")
                matriz[x][j]= hexL.pop(0)
                # print("1 error N ",e)
                # e+=1
                indices[stringHex(matriz[x][j])][0]=x
                # print("2 error N ",e)
                # e+=1
                indices[stringHex(matriz[x][j])][1]=j

            else:
                # print("else")
                matriz[x][j]= llave[cnt]
                # print("3 error N ",e)
                # e+=1
                indices[stringHex(matriz[x][j])][0]=x
                # print("4 error N ",e)
                # e+=1
                indices[stringHex(matriz[x][j])][1]=j
                cnt+=1
    print(indices)
    return matriz
# def CifrarMensaje(matriz,mensaje):
#     return
if __name__ == "__main__":
    indices=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    indices1=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    print(hexToASCII("636c617665"))
    print(ASCIItoHEX("clave"))
    hex = '636c617665'
    llave=[""]
    llave.clear()
    for letter in hex:
        llave.append(letter)
    print(len(llave))
    print(ConstruirMatriz("636c617665",indices))
    print(ConstruirMatriz("631c5e4729f",indices1))