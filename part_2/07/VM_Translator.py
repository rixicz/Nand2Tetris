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

def code_arg_local_this_that(c_list: list, asm_ins, pointer: str):
    asm_ins.append(f"@{c_list[2]}")
    asm_ins.append("D=A")
    asm_ins.append(pointer)
    asm_ins.append("A=D+M")
    asm_ins.append("D=M")
    asm_ins.append("@SP")
    asm_ins.append("A=M")
    asm_ins.append("M=D")
    asm_ins.append("@SP")
    asm_ins.append("M=M+1")

def coder(commands: list):
    asm_ins = []
    for c in commands:
        c = c.strip()
        c_list = c.split(" ")
        asm_ins.append("// " + c + "\n")
        if c_list[0] == "push":
            if c_list[1] == "constant":
                code_constant(c_list, asm_ins)            
            
            elif c_list[1] == "argument":
                code_arg_local_this_that(c_list, asm_ins, "@ARG")

            elif c_list[1] == "local":
                code_arg_local_this_that(c_list, asm_ins, "@LOC")

            elif c_list[1] == "this":
                code_arg_local_this_that(c_list, asm_ins, "@THIS")

            elif c_list[1] == "that":
                code_arg_local_this_that(c_list, asm_ins, "@THAT")
        
        if c_list[0] == "pop":
            
            if c_list[1] == "argument":
                pass

            elif c_list[1] == "local":
                pass

            elif c_list[1] == "this":
                pass

            elif c_list[1] == "that":
                pass
        
        asm_ins.append("\n")

    return asm_ins

filename = input("Please specify the filename: ")

vm_commands = reader(filename)
asm_instructions = coder(vm_commands)

with open("asm_programs/" + filename + ".asm", "w") as file:
    for ins in asm_instructions:
        file.write(ins + "\n")