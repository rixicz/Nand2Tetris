def reader(filename: str):
    with open("vm_programs/" + filename + ".vm", "r") as file:
        commands = []
        for line in file:
            check_line = line.strip()
            if line.startswith("/") or not check_line:
                continue
            commands.append(line)
        
        return commands

def code_constant(command_list: list, asm_ins: list):
    asm_ins.append(f"@{command_list[2]}")
    asm_ins.append("D=A")
    asm_ins.append("@SP")
    asm_ins.append("A=M")
    asm_ins.append("M=D")
    
    asm_ins.append("@SP")
    asm_ins.append("M=M+1")

def push_arg_local_this_that(c_list: list, asm_ins: list, pointer: str):
    asm_ins.append(f"@{c_list[2]}")
    asm_ins.append("D=A")
    asm_ins.append(f"{pointer}")
    asm_ins.append("A=D+M")
    asm_ins.append("D=M")
    
    asm_ins.append("@SP")
    asm_ins.append("A=M")
    asm_ins.append("M=D")
    
    asm_ins.append("@SP")
    asm_ins.append("M=M+1")

def pop_arg_local_this_that(c_list: list, asm_ins: list, pointer: str):
    asm_ins.append(f"@{c_list[2]}")
    asm_ins.append("D=A")
    asm_ins.append(f"{pointer}")
    asm_ins.append("A=D+M")
    asm_ins.append("D=A")
    
    asm_ins.append("@addr")
    asm_ins.append("M=D")

    asm_ins.append("@SP")
    asm_ins.append("M=M-1")
    asm_ins.append("A=M")
    asm_ins.append("D=M")
    
    asm_ins.append("@addr")
    asm_ins.append("A=M")
    asm_ins.append("M=D")

def pop_static(c_list: list, asm_ins: list, filename: str):
    asm_ins.append("@SP")
    asm_ins.append("M=M-1")
    asm_ins.append("A=M")
    asm_ins.append("D=M")

    asm_ins.append(f"@{filename}.{c_list[2]}")
    asm_ins.append("M=D")

def push_static(c_list: list, asm_ins: list, filename: str):
    asm_ins.append(f"@{filename}.{c_list[2]}")
    asm_ins.append("D=M")

    asm_ins.append("@SP")
    asm_ins.append("A=M")
    asm_ins.append("M=D")
    
    asm_ins.append("@SP")
    asm_ins.append("M=M+1")

def push_temp(c_list: list, asm_ins: list):
    asm_ins.append(f"@{c_list[2]}")
    asm_ins.append("D=A")
    asm_ins.append("@5")
    asm_ins.append("A=D+A")
    asm_ins.append("D=M")

    asm_ins.append("@SP")
    asm_ins.append("M=M+1")
    asm_ins.append("A=M-1")
    asm_ins.append("M=D")


def pop_temp(c_list: list, asm_ins: list):
    asm_ins.append(f"@{c_list[2]}")
    asm_ins.append("D=A")
    asm_ins.append("@5")
    asm_ins.append("A=D+A")
    asm_ins.append("D=A")

    asm_ins.append("@addr")
    asm_ins.append("M=D")

    asm_ins.append("@SP")
    asm_ins.append("M=M-1")
    asm_ins.append("A=M")
    asm_ins.append("D=M")

    asm_ins.append("@addr")
    asm_ins.append("A=M")
    asm_ins.append("M=D")

def add(asm_ins: list):
    asm_ins.append("@SP")
    asm_ins.append("M=M-1")
    asm_ins.append("A=M")
    asm_ins.append("D=M")
    asm_ins.append("A=A-1")
    asm_ins.append("M=D+M")


def subtract(asm_ins: list):
    asm_ins.append("@SP")
    asm_ins.append("M=M-1")
    asm_ins.append("A=M")
    asm_ins.append("D=M")

    asm_ins.append("A=A-1")
    asm_ins.append("M=M-D")  

def push_pointer(c_list: list, asm_ins: list):
    if c_list[2] == "0":
        pointer = "@THIS"
    elif c_list[2] == "1":
        pointer = "@THAT"

    asm_ins.append(pointer)     
    asm_ins.append("D=M")

    asm_ins.append("@SP")
    asm_ins.append("M=M+1")
    asm_ins.append("A=M-1")
    asm_ins.append("M=D")

def pop_pointer(c_list: list, asm_ins: list):
    if c_list[2] == "0":
            pointer = "@THIS"
    elif c_list[2] == "1":
            pointer = "@THAT"

    asm_ins.append("@SP")
    asm_ins.append("M=M-1")

    asm_ins.append("A=M")
    asm_ins.append("D=M")

    asm_ins.append(pointer)
    asm_ins.append("M=D")

def notfc(asm_ins: list):
    asm_ins.append("@SP")
    asm_ins.append("A=M-1")
    asm_ins.append("M=!M")

def andorfc(c_list: list, asm_ins: list):
    if c_list[0].strip() == "and":
        op = "&"

    else:
        op = "|"

    asm_ins.append("@SP")
    asm_ins.append("M=M-1")
    asm_ins.append("A=M")

    asm_ins.append("D=M")
    asm_ins.append("A=A-1")
    asm_ins.append(f"M=D{op}M")

def neg(asm_ins: list):
    asm_ins.append("@SP")
    asm_ins.append("A=M-1")
    asm_ins.append("M=-M")

def eqgtlt(c_list: list, asm_ins: list, i: int):
    if c_list[0].strip() == "eq":
        op = "JEQ"

    elif c_list[0].strip() == "gt":
        op = "JGT"

    elif c_list[0].strip() == "lt":
        op = "JLT"

    asm_ins.append("@SP")
    asm_ins.append("M=M-1")
    asm_ins.append("A=M")

    asm_ins.append("D=M")
    asm_ins.append("A=A-1")
    asm_ins.append("D=M-D")

    asm_ins.append(f"@TRUE{i}")
    asm_ins.append(f"D;{op}")

    asm_ins.append("@SP")
    asm_ins.append("A=M-1")
    asm_ins.append("M=0")
    asm_ins.append(f"@FALSE{i}")
    asm_ins.append("0;JEQ")

    asm_ins.append(f"(TRUE{i})")
    asm_ins.append("@SP")
    asm_ins.append("A=M-1")
    asm_ins.append("M=-1")
    asm_ins.append(f"(FALSE{i})")

def coder(commands: list, filename: str):
    asm_ins = []
    i = 0
    for c in commands:
        c = c.strip()
        c_list = c.split(" ")
        asm_ins.append("// " + c + "\n")
        
        if c_list[0] == "push":
            if c_list[1] == "constant":
                code_constant(c_list, asm_ins)           
            
            elif c_list[1] == "argument":
                push_arg_local_this_that(c_list, asm_ins, "@ARG")

            elif c_list[1] == "local":
                push_arg_local_this_that(c_list, asm_ins, "@LCL")

            elif c_list[1] == "this":
                push_arg_local_this_that(c_list, asm_ins, "@THIS")

            elif c_list[1] == "that":
                push_arg_local_this_that(c_list, asm_ins, "@THAT")

            elif c_list[1] == "static":
                push_static(c_list, asm_ins, filename)

            elif c_list[1] == "temp":
                push_temp(c_list, asm_ins)

            elif c_list[1] == "pointer":
                push_pointer(c_list, asm_ins)

        elif c_list[0] == "pop":
            
            if c_list[1] == "argument":
                pop_arg_local_this_that(c_list, asm_ins, "@ARG")

            elif c_list[1] == "local":
                pop_arg_local_this_that(c_list, asm_ins, "@LCL")

            elif c_list[1] == "this":
                pop_arg_local_this_that(c_list, asm_ins, "@THIS")

            elif c_list[1] == "that":
                pop_arg_local_this_that(c_list, asm_ins, "@THAT")
        
            elif c_list[1] == "static":
                pop_static(c_list, asm_ins, filename)

            elif c_list[1] == "temp":
                pop_temp(c_list, asm_ins)

            elif c_list[1] == "pointer":
                pop_pointer(c_list, asm_ins)
        
        elif c_list[0].strip() == "add": # added .strip() to eliminate the \n at the end
            add(asm_ins)

        elif c_list[0].strip() == "sub":
            subtract(asm_ins)

        elif c_list[0].strip() == "not":
            notfc(asm_ins)

        elif c_list[0].strip() == "and" or c_list[0].strip() == "or":
            andorfc(c_list, asm_ins)

        elif c_list[0].strip() == "neg":
            neg(asm_ins)

        elif c_list[0].strip() == "eq" or c_list[0].strip() == "gt" or c_list[0].strip() == "lt":
            i += 1
            eqgtlt(c_list, asm_ins, i)

        asm_ins.append("\n")

    return asm_ins

filename = input("Please specify the filename: ")

vm_commands = reader(filename)
asm_instructions = coder(vm_commands, filename)

with open("asm_programs/" + filename + ".asm", "w") as file:
    for ins in asm_instructions:
        if ins == "\n":
            file.write(ins)
        else:
            file.write(ins + "\n")