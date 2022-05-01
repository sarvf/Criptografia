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
def ConstruirMatriz(h):
    llave=[""]
    llave.clear()
    x=j=0
    hexL=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    matriz=[['','','',''],['','','',''],['','','',''],['','','','']]
    cnt=0
    for letter in h:
        if (llave.count(letter)==0):
            llave.append(letter)
            hexL.pop(hexL.index(letter))
    for x in range(4):
        for j in range(4):
            if (cnt >=len(llave)):
                # print("if")
                matriz[x][j]= hexL.pop(0)
            else:
                # print("else")
                matriz[x][j]= llave[cnt]
                cnt+=1
    return matriz
if __name__ == "__main__":
    print(hexToASCII("636c617665"))
    print(ASCIItoHEX("clave"))
    hex = '636c617665'
    llave=[""]
    llave.clear()
    for letter in hex:
        llave.append(letter)
    print(len(llave))
    print(ConstruirMatriz("636c617665"))
    print(ConstruirMatriz("631c5e4729f"))