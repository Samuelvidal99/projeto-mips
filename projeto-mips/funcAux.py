# funcao que converte uma string de hexadecimal para binario.
# exemplo: 0x02114020 -> 00000010000100010100000000100000
def hex_to_binary(str):
    sliced = str[2:]
    end_length = len(sliced) * 4
    hex_as_int = int(sliced, 16)
    hex_as_binary = bin(hex_as_int)
    padded_binary = hex_as_binary[2:].zfill(end_length)
    return padded_binary

# funcap que converte uma string de binario para decimal
# exemplo: 01000 -> 8
def binaryToDecimal(str):
    return int(str, 2)

# funcao que retorna o opcode de uma string binaria.
# exemplo: 00000010000100010100000000100000 -> 000000
def getOpCode(str):
    return str[:6]

# funcao que retorna o Rs de uma string binaria.
# exemplo: 00000010000100010100000000100000 -> 10000
def getRs(str):
    return str[6:11]

# funcao que retorna o Rt de uma string binaria.
# exemplo: 00000010000100010100000000100000 -> 10001
def getRt(str):
    return str[11:16]

# funcao que retorna o Rd de uma string binaria.
# exemplo: 00000010000100010100000000100000 -> 01000
def getRd(str):
    return str[16:21]

# funcao que retorna o Sh de uma string binaria.
# exemplo: 00000010000100010100000000100000 -> 00000
def getSh(str):
    return str[21:26]

# funcao que retorna o Fn de uma string binaria.
# exemplo: 00000010000100010100000000100000 -> 100000
def getFn(str):
    return str[26:32]

# funcao que retorna o Operand/Offset de uma string binaria
# exemplo: 00000010000100010100000000100000 -> 0100000000100000
def getOffset(str):
    return str[16:32]

# funcao que retorna o Operand/Offset de uma string binaria
# exemplo: 00000010000100010100000000100000 -> 10000100010100000000100000
def getJTA(str):
    return str[6:32]