import funcAux as fAux
import json

with open("mappings.json") as jsonFile:
    # A variavel mappings tem os valores de um dictionary salvo como um json, 
    # onde as keys mais externas sao o valor do opcode e dentro da key "000000",
    # que seria opcode para tipo R, sao guardadas as keys com o valor do fn.
    mappings = json.load(jsonFile)
    jsonFile.close()

binary = fAux.hex_to_binary("0x02114020")

print(binary)

def identificadorInst(str):
    if fAux.getOpCode(str) == "000000":
        opCode = fAux.getOpCode(str)
        print(mappings[opCode][fAux.getFn(str)])

identificadorInst(binary)
