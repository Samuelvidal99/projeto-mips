import funcAux as fAux
import json

with open("mappings.json") as jsonFile:
    # A variavel mappings tem os valores de um dictionary salvo como um json, 
    # onde as keys mais externas sao o valor do opcode e dentro da key "000000",
    # que seria opcode para tipo R, sao guardadas as keys com o valor do fn.
    mappings = json.load(jsonFile)
    jsonFile.close()

binary = fAux.hex_to_binary("0x02114020")
#binary = fAux.hex_to_binary("0x02114208")
print(binary)

# funcao Identificador de Instrucoes que recebe uma string em hexadecimal, 0x02114020,
# e retorna uma string como uma instrucao assembly
def identificadorInst(string):
    if fAux.getOpCode(string) == "000000":
        opCode = fAux.getOpCode(string)
        fn = mappings[opCode][fAux.getFn(string)]
        # mult $rs $rt
        if fn == "mult":
            rs = str(fAux.binaryToDecimal(fAux.getRs(binary)))
            rt = str(fAux.binaryToDecimal(fAux.getRt(binary)))
            print(fn + " $"+ rs + " $" + rt)
        # multu $rs $rt
        elif fn == "multu":
            rs = str(fAux.binaryToDecimal(fAux.getRs(binary)))
            rt = str(fAux.binaryToDecimal(fAux.getRt(binary)))
            print(fn + " $"+ rs + " $" + rt)
        # div $rs $rt
        elif fn == "div":
            rs = str(fAux.binaryToDecimal(fAux.getRs(binary)))
            rt = str(fAux.binaryToDecimal(fAux.getRt(binary)))
            print(fn + " $"+ rs + " $" + rt)
        # divu $rs $rt
        elif fn == "divu":
            rs = str(fAux.binaryToDecimal(fAux.getRs(binary)))
            rt = str(fAux.binaryToDecimal(fAux.getRt(binary)))
            print(fn + " $"+ rs + " $" + rt)
        # sll $rd $rt $sh
        elif fn == "sll":
            rd = str(fAux.binaryToDecimal(fAux.getRd(binary)))
            rt = str(fAux.binaryToDecimal(fAux.getRt(binary)))
            sa = str(fAux.binaryToDecimal(fAux.getSh(binary)))
            print(fn + " $"+ rd + " $" + rt + " $" + sa)
        # sllv $rd $rt $rs
        elif fn == "sllv":
            rd = str(fAux.binaryToDecimal(fAux.getRd(binary)))
            rs = str(fAux.binaryToDecimal(fAux.getRs(binary)))
            rt = str(fAux.binaryToDecimal(fAux.getRt(binary)))
            print (fn + " $"+ rd + " $"+ rt + " $" + rs)
        # srl $rd $rt $sh
        elif fn == "srl":
            rd = str(fAux.binaryToDecimal(fAux.getRd(binary)))
            rt = str(fAux.binaryToDecimal(fAux.getRt(binary)))
            sa = str(fAux.binaryToDecimal(fAux.getSh(binary)))
            print(fn + " $"+ rd + " $" + rt + " $" + sa)
        # srlv $rd $rt $rs
        elif fn == "srlv":
            rd = str(fAux.binaryToDecimal(fAux.getRd(binary)))
            rs = str(fAux.binaryToDecimal(fAux.getRs(binary)))
            rt = str(fAux.binaryToDecimal(fAux.getRt(binary)))
            print (fn + " $"+ rd + " $"+ rt + " $" + rs)
        # sra $rd $rt $sh
        elif fn == "sra":
            rd = str(fAux.binaryToDecimal(fAux.getRd(binary)))
            rt = str(fAux.binaryToDecimal(fAux.getRt(binary)))
            sa = str(fAux.binaryToDecimal(fAux.getSh(binary)))
            print(fn + " $"+ rd + " $" + rt + " $" + sa)
        # srav $rd $rt $rs
        elif fn == "srav":
            rd = str(fAux.binaryToDecimal(fAux.getRd(binary)))
            rs = str(fAux.binaryToDecimal(fAux.getRs(binary)))
            rt = str(fAux.binaryToDecimal(fAux.getRt(binary)))
            print (fn + " $"+ rd + " $"+ rt + " $" + rs)
        # jr $rs
        elif fn == "jr":
            rs = str(fAux.binaryToDecimal(fAux.getRs(binary)))
            print (fn + " $"+ rs)
        # add $rd $rs $rt
        elif fn == "add":
            rd = str(fAux.binaryToDecimal(fAux.getRd(binary)))
            rs = str(fAux.binaryToDecimal(fAux.getRs(binary)))
            rt = str(fAux.binaryToDecimal(fAux.getRt(binary)))
            print (fn + " $"+ rd + " $"+ rs + " $" + rt)


#add $8, $16, $17
print(fAux.getRd(binary) + " " + fAux.getRt(binary))

identificadorInst(binary)
