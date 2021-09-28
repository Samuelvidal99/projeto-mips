
#00000010000100010100000000100000

# funcao que converte uma string de hexadecimal para binario
def hex_to_binary(str):
    sliced = str[2:]
    end_length = len(sliced) * 4
    hex_as_int = int(sliced, 16)
    hex_as_binary = bin(hex_as_int)
    padded_binary = hex_as_binary[2:].zfill(end_length)
    return padded_binary


print(hex_to_binary("0x02114020"))