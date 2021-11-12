# Grupo G2: Samuel Santos, Ana Clara Costa, Nicole Pereira, Aldenir Silva.

import funcAux as fAux
import json

with open("mappings.json") as jsonFile:
    # A variavel mappings tem os valores de um dictionary salvo como um json, 
    # onde as keys mais externas sao o valor do opcode e dentro da key "000000",
    # que seria opcode para tipo R, sao guardadas as keys com o valor do fn.
    mappings = json.load(jsonFile)
    jsonFile.close()

# Registradores
# REGS[$0=0;$1=0;$2=6;$3=5;$4=8;$5=10;$6=12;$7=15;$8=2;$9=8;$10=11;$11=4;$12=5;$13=0;$14=0;$15=0;$16=0;$17=0;
# $18=0;$19=0;$20=0;$21=0;$22=0;$23=0;$24=0;$25=0;$26=0;$27=0;$28=0;$29=0;$30=0;$31=0]
REGS = [0]*32
# iniciando os registradores.
REGS[2] = 6
REGS[3] = 5
REGS[4] = 8
REGS[5] = 10
REGS[6] = 12
REGS[7] = 15
REGS[8] = 2
REGS[9] = 8
REGS[10] = 11
REGS[11] = 4
REGS[12] = 5
# registrador ra = $28
REGS[28] = 0
# registrador pc = $29
REGS[29] = 0
# registrador hi = $30
REGS[30] = 0
# registrador lo = $31
REGS[31] = 0

# Memoria MEM com 1024 entradas de 8bits, ou seja 128 bytes.
aux = []
for x in range(128):
    aux.append(0x00)

MEM = bytearray(aux)

def printAux(MEM):
    aux = ""
    for i in range(128):
        aux += str(MEM[i]) + ", "
    return aux 

def printaREGS(REGS):
    aux1 = "REGS["
    aux2 = 0
    for i in REGS:
        if aux2 != 31:
            aux1 += "$" + str(aux2) + "=" + str(i) + ","
        else:
            aux1 += "$" + str(aux2) + "=" + str(i) + "]"
        #aux1 += "$" + str(aux2) + "=" + str(i) + ","
        aux2 += 1
    return aux1

def printMEM():
    aux = 0
    aux2 = 0
    for x in range(128):
        if MEM[x] != 0:
            aux = MEM[x]
            aux2 = x
            break
    
    string = 'MEM[{}:{}]'.format(aux2,aux)
    return string

# funcao Identificador de Instrucoes que recebe uma string em hexadecimal, 0x02114020,
# e retorna uma string como uma instrucao assembly
def identificadorInst(string):
    if fAux.getOpCode(string) == "000000":
        opCode = fAux.getOpCode(string)
        fn = mappings[opCode][fAux.getFn(string)]
        # mult $rs, $rt
        if fn == "mult":
            rs = str(fAux.binaryToDecimal(fAux.getRs(binary)))
            rt = str(fAux.binaryToDecimal(fAux.getRt(binary)))
            REGS[31] = REGS[int(rs)] * REGS[int(rt)]
            aux = fn + " $"+ rs + "," + " $" + rt  + "\n" + printMEM() + "\n" + printaREGS(REGS)
            return(aux)
        # multu $rs, $rt
        elif fn == "multu":
            rs = str(fAux.binaryToDecimal(fAux.getRs(binary)))
            rt = str(fAux.binaryToDecimal(fAux.getRt(binary)))
            REGS[31] = REGS[int(rs)] * REGS[int(rt)]
            aux = fn + " $"+ rs + "," + " $" + rt  + "\n" + printMEM() + "\n" + printaREGS(REGS)
            return(aux)
        # div $rs, $rt
        elif fn == "div":
            rs = str(fAux.binaryToDecimal(fAux.getRs(binary)))
            rt = str(fAux.binaryToDecimal(fAux.getRt(binary)))
            REGS[30] = REGS[int(rs)] % REGS[int(rt)]
            REGS[31] = REGS[int(rs)] / REGS[int(rt)]
            aux2 = fn + " $"+ rs + "," + " $" + rt  + "\n" + printMEM() + "\n" + printaREGS(REGS)
            return(aux2)
        # divu $rs, $rt
        elif fn == "divu":
            rs = str(fAux.binaryToDecimal(fAux.getRs(binary)))
            rt = str(fAux.binaryToDecimal(fAux.getRt(binary)))
            REGS[30] = REGS[int(rs)] % REGS[int(rt)]
            REGS[31] = REGS[int(rs)] / REGS[int(rt)]
            aux2 = fn + " $"+ rs + "," + " $" + rt + "\n"  + "\n" + printMEM() + printaREGS(REGS)
            return(aux2)
        # sll $rd, $rt, sa
        elif fn == "sll":
            rd = str(fAux.binaryToDecimal(fAux.getRd(binary)))
            rt = str(fAux.binaryToDecimal(fAux.getRt(binary)))
            sa = str(fAux.binaryToDecimal(fAux.getSh(binary)))
            # realizando instrucao
            aux = REGS[int(rt)] << REGS[int(sa)]
            REGS[int(rd)] = aux
            aux2 = fn + " $"+ rd + "," + " $" + rt +  ", "  + sa  + "\n" + printMEM() + "\n" + printaREGS(REGS)
            return(aux2)
        # sllv $rd, $rt, $rs
        elif fn == "sllv":
            rd = str(fAux.binaryToDecimal(fAux.getRd(binary)))
            rs = str(fAux.binaryToDecimal(fAux.getRs(binary)))
            rt = str(fAux.binaryToDecimal(fAux.getRt(binary)))
            # realizando instrucao
            aux = REGS[int(rt)] << REGS[int(rs)]
            REGS[int(rd)] = aux
            aux2 = fn + " $"+ rd + "," + " $"+ rt + "," + " $" + rs  + "\n" + printMEM() + "\n" + printaREGS(REGS)
            return (aux2)
        # srl $rd, $rt, sa
        elif fn == "srl":
            rd = str(fAux.binaryToDecimal(fAux.getRd(binary)))
            rt = str(fAux.binaryToDecimal(fAux.getRt(binary)))
            sa = str(fAux.binaryToDecimal(fAux.getSh(binary)))
            # realizando instrucao
            aux = REGS[int(rt)] >> REGS[int(sa)]
            REGS[int(rd)] = aux
            aux2 = fn + " $"+ rd + "," + " $" + rt +  ", "  + sa  + "\n" + printMEM() + "\n" + printaREGS(REGS)
            return(aux2)
        # srlv $rd, $rt, $rs
        elif fn == "srlv":
            rd = str(fAux.binaryToDecimal(fAux.getRd(binary)))
            rs = str(fAux.binaryToDecimal(fAux.getRs(binary)))
            rt = str(fAux.binaryToDecimal(fAux.getRt(binary)))
            # realizando instrucao
            aux = REGS[int(rt)] >> REGS[int(rs)]
            REGS[int(rd)] = aux
            aux2 = fn + " $"+ rd + "," + " $"+ rt + "," + " $" + rs  + "\n" + printMEM() + "\n" + printaREGS(REGS)
            return (aux2)
        # sra $rd, $rt, sa
        elif fn == "sra":
            rd = str(fAux.binaryToDecimal(fAux.getRd(binary)))
            rt = str(fAux.binaryToDecimal(fAux.getRt(binary)))
            sa = str(fAux.binaryToDecimal(fAux.getSh(binary)))
            # realizando instrucao
            aux = REGS[int(rt)] >> REGS[int(sa)]
            REGS[int(rd)] = aux
            aux2 = fn + " $"+ rd + "," + " $" + rt + ", " + sa  + "\n" + printMEM() + "\n" + printaREGS(REGS)
            return(aux2)
        # srav $rd, $rt, $rs
        elif fn == "srav":
            rd = str(fAux.binaryToDecimal(fAux.getRd(binary)))
            rs = str(fAux.binaryToDecimal(fAux.getRs(binary)))
            rt = str(fAux.binaryToDecimal(fAux.getRt(binary)))
            return (fn + " $"+ rd + "," + " $"+ rt + "," + " $" + rs + "\n" + printMEM() + "\n" + printaREGS(REGS))
        # jr $rs
        elif fn == "jr":
            rs = str(fAux.binaryToDecimal(fAux.getRs(binary)))
            
            # registrador pc = rs
            REGS[29] = int(rs)
            return (fn + " $"+ rs + "\n" + printMEM() + "\n" + printaREGS(REGS))
        # add $rd, $rs, $rt
        elif fn == "add":
            rd = str(fAux.binaryToDecimal(fAux.getRd(binary)))
            rs = str(fAux.binaryToDecimal(fAux.getRs(binary)))
            rt = str(fAux.binaryToDecimal(fAux.getRt(binary)))
            # realizando instrucao
            aux = REGS[int(rs)] + REGS[int(rt)]
            REGS[int(rd)] = aux
            aux2 = fn + " $"+ rd + "," + " $"+ rs + "," + " $" + rt + "\n" + printMEM() + "\n" + printaREGS(REGS) 
            return (aux2)
        # sub $rd, $rs, $rt
        elif fn == "sub":
            rd = str(fAux.binaryToDecimal(fAux.getRd(binary)))
            rs = str(fAux.binaryToDecimal(fAux.getRs(binary)))
            rt = str(fAux.binaryToDecimal(fAux.getRt(binary)))
            # realizando instrucao
            aux = REGS[int(rs)] - REGS[int(rt)]
            REGS[int(rd)] = aux
            aux2 = fn + " $"+ rd + "," + " $"+ rs + "," + " $" + rt + "\n" + printMEM() + "\n" + printaREGS(REGS) 
            return (aux2)
        # slt $rd, $rs, $rt
        elif fn == "slt":
            rd = str(fAux.binaryToDecimal(fAux.getRd(binary)))
            rs = str(fAux.binaryToDecimal(fAux.getRs(binary)))
            rt = str(fAux.binaryToDecimal(fAux.getRt(binary)))
            # realizando instrucao
            aux = int(REGS[int(rs)] < REGS[int(rt)])
            REGS[int(rd)] = aux
            aux2 = fn + " $"+ rd + "," + " $"+ rs + "," + " $" + rt + "\n" + printMEM() + "\n" + printaREGS(REGS) 
            return (aux2)
        # and $rd, $rs, $rt
        elif fn =="and":
            rd = str(fAux.binaryToDecimal(fAux.getRd(binary)))
            rs = str(fAux.binaryToDecimal(fAux.getRs(binary)))
            rt = str(fAux.binaryToDecimal(fAux.getRt(binary)))
            # realizando instrucao
            aux = REGS[int(rs)] & REGS[int(rt)]
            REGS[int(rd)] = aux
            aux2 = fn + " $"+ rd + "," + " $"+ rs + "," + " $" + rt + "\n" + printMEM() + "\n" + printaREGS(REGS) 
            return (aux2)
        # or $rd, $rs, $rt
        elif fn == "or":
            rd = str(fAux.binaryToDecimal(fAux.getRd(binary)))
            rs = str(fAux.binaryToDecimal(fAux.getRs(binary)))
            rt = str(fAux.binaryToDecimal(fAux.getRt(binary)))
            # realizando instrucao
            aux = REGS[int(rs)] | REGS[int(rt)]
            REGS[int(rd)] = aux
            aux2 = fn + " $"+ rd + "," + " $"+ rs + "," + " $" + rt + "\n" + printMEM() + "\n" + printaREGS(REGS) 
            return (aux2)
        # xor $rd, $rs, $rt
        elif fn == "xor":
            rd = str(fAux.binaryToDecimal(fAux.getRd(binary)))
            rs = str(fAux.binaryToDecimal(fAux.getRs(binary)))
            rt = str(fAux.binaryToDecimal(fAux.getRt(binary)))
            # realizando instrucao
            aux = REGS[int(rs)] ^ REGS[int(rt)]
            REGS[int(rd)] = aux
            aux2 = fn + " $"+ rd + "," + " $"+ rs + "," + " $" + rt + "\n" + printMEM() + "\n" + printaREGS(REGS) 
            return (aux2)
        # nor $rd, $rs, $rt
        elif fn == "nor":
            rd = str(fAux.binaryToDecimal(fAux.getRd(binary)))
            rs = str(fAux.binaryToDecimal(fAux.getRs(binary)))
            rt = str(fAux.binaryToDecimal(fAux.getRt(binary)))
            # realizando instrucao
            aux = ~(REGS[int(rs)] | REGS[int(rt)])
            REGS[int(rd)] = aux
            aux2 = fn + " $"+ rd + "," + " $"+ rs + "," + " $" + rt + "\n" + printMEM() + "\n" + printaREGS(REGS) 
            return (aux2)
        # mhfi $rd
        elif fn == "mfhi":
            rd = str(fAux.binaryToDecimal(fAux.getRd(binary)))
            # realizando instrucao
            aux = REGS[30]
            REGS[int(rd)] = aux
            aux2 = fn + " $"+ rd + "\n" + printMEM() + "\n" + printaREGS(REGS)
            return (aux2)
        # mflo $rd
        elif fn == "mflo":
            rd = str(fAux.binaryToDecimal(fAux.getRd(binary)))
            # realizando instrucao
            aux = REGS[31]
            REGS[int(rd)] = aux
            aux2 = fn + " $"+ rd + "\n" + printMEM() + "\n" + printaREGS(REGS)
            return (aux2)
        # addu $rd, $rs, $rt
        elif fn == "addu":
            rd = str(fAux.binaryToDecimal(fAux.getRd(binary)))
            rs = str(fAux.binaryToDecimal(fAux.getRs(binary)))
            rt = str(fAux.binaryToDecimal(fAux.getRt(binary)))
            # realizando instrucao
            aux = REGS[int(rs)] + REGS[int(rt)]
            REGS[int(rd)] = aux
            aux2 = fn + " $"+ rd + "," + " $"+ rs + "," + " $" + rt + "\n" + printMEM() + "\n" + printaREGS(REGS) 
            return (aux2)
        # subu $rd, $rs, $rt
        elif fn == "subu":
            rd = str(fAux.binaryToDecimal(fAux.getRd(binary)))
            rs = str(fAux.binaryToDecimal(fAux.getRs(binary)))
            rt = str(fAux.binaryToDecimal(fAux.getRt(binary)))
            # realizando instrucao
            aux = REGS[int(rs)] - REGS[int(rt)]
            REGS[int(rd)] = aux
            aux2 = fn + " $"+ rd + "," + " $"+ rs + "," + " $" + rt + "\n" + printMEM() + "\n" + printaREGS(REGS) 
            return (aux2)
        # syscall 
        elif fn == "syscall":
            return (fn)

    # lui $rt, offset
    if fAux.getOpCode(string) == "001111":
        opCode = mappings[fAux.getOpCode(string)]
        if opCode == "lui":
            rt = str(fAux.binaryToDecimal(fAux.getRt(binary)))
            offset = str(fAux.binaryToDecimal(fAux.getOffset(binary)))

            REGS[int(rt)] = int(offset) << 16
            return (opCode + " $"+ rt + ", " + offset + "\n" + printMEM() + "\n" + printaREGS(REGS))
    # addi $rt, $rs, offset 
    elif fAux.getOpCode(string) == "001000":
        opCode = mappings[fAux.getOpCode(string)]
        if opCode == "addi":
            rs = str(fAux.binaryToDecimal(fAux.getRs(binary)))
            rt = str(fAux.binaryToDecimal(fAux.getRt(binary)))
            offset = str(fAux.binaryToDecimal(fAux.getOffset(binary)))
            # realizando instrucao
            aux = REGS[int(rs)] + int(offset)
            REGS[int(rt)] = aux
            aux2 = opCode + " $"+ rt + "," + " $"+ rs + ", " + offset + "\n" + printMEM() + "\n" + printaREGS(REGS) 
            return (aux2)
    # addiu $rt, $rs, offset
    elif fAux.getOpCode(string) == "001001":
        opCode = mappings[fAux.getOpCode(string)]
        if opCode == "addiu":
            rs = str(fAux.binaryToDecimal(fAux.getRs(binary)))
            rt = str(fAux.binaryToDecimal(fAux.getRt(binary)))
            offset = str(fAux.binaryToDecimal(fAux.getOffset(binary)))
            # realizando instrucao
            aux = REGS[int(rs)] + int(offset)
            REGS[int(rt)] = aux
            aux2 = opCode + " $"+ rt + "," + " $"+ rs + ", " + offset + "\n" + printMEM() + "\n" + printaREGS(REGS) 
            return (aux2)
    # slti $rt, $rs, offset
    elif fAux.getOpCode(string) == "001010":
        opCode = mappings[fAux.getOpCode(string)]
        if opCode == "slti":
            rs = str(fAux.binaryToDecimal(fAux.getRs(binary)))
            rt = str(fAux.binaryToDecimal(fAux.getRt(binary)))
            offset = str(fAux.binaryToDecimal(fAux.getOffset(binary)))
            # realizando instrucao
            aux = int(REGS[int(rs)] < int(offset))
            REGS[int(rt)] = aux
            aux2 = opCode + " $"+ rt + "," + " $"+ rs + ", " + offset + "\n" + printMEM() + "\n" + printaREGS(REGS)
            return (aux2)
    # andi $rt, $rs, offset
    elif fAux.getOpCode(string) == "001100":
        opCode = mappings[fAux.getOpCode(string)]
        if opCode == "andi":
            rs = str(fAux.binaryToDecimal(fAux.getRs(binary)))
            rt = str(fAux.binaryToDecimal(fAux.getRt(binary)))
            offset = str(fAux.binaryToDecimal(fAux.getOffset(binary)))
            # realizando instrucao
            aux = REGS[int(rs)] & int(offset)
            REGS[int(rt)] = aux
            aux2 = opCode + " $"+ rt + "," + " $" + rs + ", " + offset + "\n" + printMEM() + "\n" + printaREGS(REGS) 
            return (aux2)
    # ori $rt, $rs, offset
    elif fAux.getOpCode(string) == "001101":
        opCode = mappings[fAux.getOpCode(string)]
        if opCode == "ori":
            rs = str(fAux.binaryToDecimal(fAux.getRs(binary)))
            rt = str(fAux.binaryToDecimal(fAux.getRt(binary)))
            offset = str(fAux.binaryToDecimal(fAux.getOffset(binary)))
            # realizando instrucao
            aux = REGS[int(rs)] | int(offset)
            REGS[int(rt)] = aux
            aux2 = opCode + " $"+ rt + "," + " $" + rs + ", " + offset + "\n" + printMEM() + "\n" + printaREGS(REGS) 
            return (aux2)
    # xori $rt, $rs, offset
    elif fAux.getOpCode(string) == "001110":
        opCode = mappings[fAux.getOpCode(string)]
        if opCode == "xori":
            rs = str(fAux.binaryToDecimal(fAux.getRs(binary)))
            rt = str(fAux.binaryToDecimal(fAux.getRt(binary)))
            offset = str(fAux.binaryToDecimal(fAux.getOffset(binary)))
            # realizando instrucao
            aux = REGS[int(rs)] ^ int(offset)
            REGS[int(rt)] = aux
            aux2 = opCode + " $"+ rt + "," + " $" + rs + ", " + offset + "\n" + printMEM() + "\n" + printaREGS(REGS) 
            return (aux2)
    # bltz $rs, start
    elif fAux.getOpCode(string) == "000001":
        opCode = mappings[fAux.getOpCode(string)]
        if opCode == "bltz":
            rs = str(fAux.binaryToDecimal(fAux.getRs(binary)))
            offset = "start"

            aux = REGS[29]
            if REGS[int(rs)] < 0:
                REGS[29] = aux + int(fAux.binaryToDecimal(fAux.getOffset(string)))*4
            return (opCode + " $"+ rs + ", " + offset + "\n" + printMEM() + "\n" + printaREGS(REGS))
    # beq $rs, $rt, start
    elif fAux.getOpCode(string) == "000100":
        opCode = mappings[fAux.getOpCode(string)]
        if opCode == "beq":
            rs = str(fAux.binaryToDecimal(fAux.getRs(binary)))
            rt = str(fAux.binaryToDecimal(fAux.getRt(binary)))
            offset = "start"

            aux = REGS[29]
            if REGS[int(rs)] == REGS[int(rt)]:
                REGS[29] = aux + int(fAux.binaryToDecimal(fAux.getOffset(string)))*4
            return (opCode + " $"+ rs + "," + " $"+ rt + ", " + offset + "\n" + printMEM() + "\n" + printaREGS(REGS))
    
    # bne $rs, $rt, start
    elif fAux.getOpCode(string) == "000101":
        opCode = mappings[fAux.getOpCode(string)]
        if opCode == "bne":
            rs = str(fAux.binaryToDecimal(fAux.getRs(binary)))
            rt = str(fAux.binaryToDecimal(fAux.getRt(binary)))
            offset = "start"

            aux = REGS[29]
            if REGS[int(rs)] != REGS[int(rt)]:
                REGS[29] = aux + int(fAux.binaryToDecimal(fAux.getOffset(string)))*4
            return (opCode + " $"+ rs + "," + " $"+ rt + ", " + offset + "\n" + printMEM() + "\n" + printaREGS(REGS)) 

    # lb $rt, offset($rs)
    elif fAux.getOpCode(string) == "100000":
        opCode = mappings[fAux.getOpCode(string)]
        if opCode == "lb":
            rs = str(fAux.binaryToDecimal(fAux.getRs(binary)))
            rt = str(fAux.binaryToDecimal(fAux.getRt(binary)))
            offset = str(fAux.binaryToDecimal(fAux.getOffset(binary)))

            aux = int(offset) + REGS[int(rs)]
            REGS[int(rt)] = MEM[aux]

            return (opCode + " $"+ rt + ", " + offset + "(" + "$"+ rs + ")" + "\n" + printMEM() + "\n" + printaREGS(REGS))     

    # lbu $rt, offset($rs)
    elif fAux.getOpCode(string) == "100100":
        opCode = mappings[fAux.getOpCode(string)]
        if opCode == "lbu":
            rs = str(fAux.binaryToDecimal(fAux.getRs(binary)))
            rt = str(fAux.binaryToDecimal(fAux.getRt(binary)))
            offset = str(fAux.binaryToDecimal(fAux.getOffset(binary)))

            aux = int(offset) + REGS[int(rs)]
            REGS[int(rt)] = MEM[aux]

            return (opCode + " $"+ rt + ", " + offset + "(" + "$"+ rs + ")" + "\n" + printMEM() + "\n" + printaREGS(REGS))   

    # lw $rt, offset($rs)
    elif fAux.getOpCode(string) == "100011":
        opCode = mappings[fAux.getOpCode(string)]
        if opCode == "lw":
            rs = str(fAux.binaryToDecimal(fAux.getRs(binary)))
            rt = str(fAux.binaryToDecimal(fAux.getRt(binary)))
            offset = str(fAux.binaryToDecimal(fAux.getOffset(binary)))

            aux = int(offset) + REGS[int(rs)]
            MEM[aux] = 12
            REGS[int(rt)] = MEM[aux]
            
            return (opCode + " $"+ rt + ", " + offset + "(" + "$"+ rs + ")" + "\n" + printMEM() + "\n" + printaREGS(REGS))
            

    # sw $rt, offset($rs)
    elif fAux.getOpCode(string) == "101011":
        opCode = mappings[fAux.getOpCode(string)]
        if opCode == "sw":
            rs = str(fAux.binaryToDecimal(fAux.getRs(binary)))
            rt = str(fAux.binaryToDecimal(fAux.getRt(binary)))
            offset = str(fAux.binaryToDecimal(fAux.getOffset(binary)))

            aux = int(offset) + REGS[int(rs)]
            MEM[aux] = REGS[int(rt)] 

            return (opCode + " $"+ rt + ", " + offset + "(" + "$"+ rs + ")" + "\n" + printMEM() + "\n" + printaREGS(REGS))

    # sb $rt, offset($rs)
    elif fAux.getOpCode(string) == "101000":
        opCode = mappings[fAux.getOpCode(string)]
        if opCode == "sb":
            rs = str(fAux.binaryToDecimal(fAux.getRs(binary)))
            rt = str(fAux.binaryToDecimal(fAux.getRt(binary)))
            offset = str(fAux.binaryToDecimal(fAux.getOffset(binary)))

            aux = int(offset) + REGS[int(rs)]
            MEM[aux] = REGS[int(rt)] 

            return (opCode + " $"+ rt + ", " + offset + "(" + "$"+ rs + ")" + "\n" + printMEM() + "\n" + printaREGS(REGS))
       
    # j offset
    elif fAux.getOpCode(string) == "000010":
        opCode = mappings[fAux.getOpCode(string)]
        if opCode == "j":
            offset = "start"

            aux = REGS[29]
            target = fAux.binaryToDecimal(string[6:])
            REGS[29] = (REGS[29]|(target << 2))
            return (opCode + " " + offset + "\n" + printMEM() + "\n" + printaREGS(REGS))
            
    # jal offset
    elif fAux.getOpCode(string) == "000011":
        opCode = mappings[fAux.getOpCode(string)]
        if opCode == "jal":
            offset = "start"

            target = fAux.binaryToDecimal(string[6:])
            # pc=target<<2
            REGS[29] = (target<<2)
            # ra=pc
            REGS[28] = REGS[29]
            return (opCode + " " + offset + "\n" + printMEM() + "\n" + printaREGS(REGS))

# Abre o arquivo com nome "entrada" contendo os hexadecimais
# Ignora as quebras de linha no final de cada linha do arquivo
# Transforma cada hexadecimal em binario
# Cria um arquivo chamado saida contendo as funcoes Assembly
with open('entrada.txt', 'r') as entrada:
    for line in entrada:
        valor = line[:10]
        binary = fAux.hex_to_binary(valor)
        with open('saida.txt', 'a') as saida:
            saida.write(str(identificadorInst(binary)))
            saida.write('\n')
    entrada.close()
    saida.close()
