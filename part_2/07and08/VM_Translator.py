
def reader(filename: str):
    with open("vm_programs/" + filename + ".vm", "r") as file:
        commands = []
        for line in file:
            check_line = line.strip()
            if line.startswith("/") or not check_line:
                continue
            commands.append(line)
        
        return commands

def code_constant(command_list: list, current_func: list):
    current_func.append(f"@{command_list[2]}")
    current_func.append("D=A")
    current_func.append("@SP")
    current_func.append("A=M")
    current_func.append("M=D")
    
    current_func.append("@SP")
    current_func.append("M=M+1")

def push_arg_local_this_that(c_list: list, current_func: list, pointer: str):
    current_func.append(f"@{c_list[2]}")
    current_func.append("D=A")
    current_func.append(f"{pointer}")
    current_func.append("A=D+M")
    current_func.append("D=M")
    
    current_func.append("@SP")
    current_func.append("A=M")
    current_func.append("M=D")
    
    current_func.append("@SP")
    current_func.append("M=M+1")

def pop_arg_local_this_that(c_list: list, current_func: list, pointer: str):
    current_func.append(f"@{c_list[2]}")
    current_func.append("D=A")
    current_func.append(f"{pointer}")
    current_func.append("A=D+M")
    current_func.append("D=A")
    
    current_func.append("@addr")
    current_func.append("M=D")

    current_func.append("@SP")
    current_func.append("M=M-1")
    current_func.append("A=M")
    current_func.append("D=M")
    
    current_func.append("@addr")
    current_func.append("A=M")
    current_func.append("M=D")

def pop_static(c_list: list, current_func: list, filename: str):
    current_func.append("@SP")
    current_func.append("M=M-1")
    current_func.append("A=M")
    current_func.append("D=M")

    current_func.append(f"@{filename}.{c_list[2]}")
    current_func.append("M=D")

def push_static(c_list: list, current_func: list, filename: str):
    current_func.append(f"@{filename}.{c_list[2]}")
    current_func.append("D=M")

    current_func.append("@SP")
    current_func.append("A=M")
    current_func.append("M=D")
    
    current_func.append("@SP")
    current_func.append("M=M+1")

def push_temp(c_list: list, current_func: list):
    current_func.append(f"@{c_list[2]}")
    current_func.append("D=A")
    current_func.append("@5")
    current_func.append("A=D+A")
    current_func.append("D=M")

    current_func.append("@SP")
    current_func.append("M=M+1")
    current_func.append("A=M-1")
    current_func.append("M=D")


def pop_temp(c_list: list, current_func: list):
    current_func.append(f"@{c_list[2]}")
    current_func.append("D=A")
    current_func.append("@5")
    current_func.append("A=D+A")
    current_func.append("D=A")

    current_func.append("@addr")
    current_func.append("M=D")

    current_func.append("@SP")
    current_func.append("M=M-1")
    current_func.append("A=M")
    current_func.append("D=M")

    current_func.append("@addr")
    current_func.append("A=M")
    current_func.append("M=D")

def add(current_func: list):
    current_func.append("@SP")
    current_func.append("M=M-1")
    current_func.append("A=M")
    current_func.append("D=M")
    current_func.append("A=A-1")
    current_func.append("M=D+M")


def subtract(current_func: list):
    current_func.append("@SP")
    current_func.append("M=M-1")
    current_func.append("A=M")
    current_func.append("D=M")

    current_func.append("A=A-1")
    current_func.append("M=M-D")  

def push_pointer(c_list: list, current_func: list):
    if c_list[2] == "0":
        pointer = "@THIS"
    else:
        pointer = "@THAT"

    current_func.append(pointer)     
    current_func.append("D=M")

    current_func.append("@SP")
    current_func.append("M=M+1")
    current_func.append("A=M-1")
    current_func.append("M=D")

def pop_pointer(c_list: list, current_func: list):
    if c_list[2] == "0":
            pointer = "@THIS"
    else:
            pointer = "@THAT"

    current_func.append("@SP")
    current_func.append("M=M-1")

    current_func.append("A=M")
    current_func.append("D=M")

    current_func.append(pointer)
    current_func.append("M=D")

def notfc(current_func: list):
    current_func.append("@SP")
    current_func.append("A=M-1")
    current_func.append("M=!M")

def andorfc(c_list: list, current_func: list):
    if c_list[0].strip() == "and":
        op = "&"

    else:
        op = "|"

    current_func.append("@SP")
    current_func.append("M=M-1")
    current_func.append("A=M")

    current_func.append("D=M")
    current_func.append("A=A-1")
    current_func.append(f"M=D{op}M")

def neg(current_func: list):
    current_func.append("@SP")
    current_func.append("A=M-1")
    current_func.append("M=-M")

def eqgtlt(c_list: list, current_func: list, i: int):
    if c_list[0].strip() == "eq":
        op = "JEQ"

    elif c_list[0].strip() == "gt":
        op = "JGT"

    elif c_list[0].strip() == "lt":
        op = "JLT"

    else:
        op = "not defined"

    current_func.append("@SP")
    current_func.append("M=M-1")
    current_func.append("A=M")

    current_func.append("D=M")
    current_func.append("A=A-1")
    current_func.append("D=M-D")

    current_func.append(f"@TRUE{i}")
    current_func.append(f"D;{op}")

    current_func.append("@SP")
    current_func.append("A=M-1")
    current_func.append("M=0")
    current_func.append(f"@FALSE{i}")
    current_func.append("0;JEQ")

    current_func.append(f"(TRUE{i})")
    current_func.append("@SP")
    current_func.append("A=M-1")
    current_func.append("M=-1")
    current_func.append(f"(FALSE{i})")

def goto(c_list: list, current_func: list):
    current_func.append(f"@{c_list[1]}")
    current_func.append("0;JEQ")

def ifgoto(c_list: list, current_func: list):
    current_func.append("@SP")
    current_func.append("M=M-1")
    current_func.append("A=M")
    current_func.append("D=M")

    current_func.append(f"@{c_list[1]}")
    current_func.append("D;JGT")

def save_pointer_state(current_func: list, pointer: str):
    current_func.append(pointer)
    current_func.append("D=M")
    
    current_func.append("@SP")
    current_func.append("M=M+1")
    current_func.append("A=M-1")

    current_func.append("M=D")

def call(c_list: list, current_func: list):
    # somehow need to save the return address
    save_pointer_state(current_func, "@LCL")
    save_pointer_state(current_func, "@ARG")
    save_pointer_state(current_func, "@THIS")
    save_pointer_state(current_func, "@THAT")

    current_func.append("@SP")
    current_func.append("D=M")
    current_func.append("@5")
    current_func.append("D=D-A")
    current_func.append(f"@{c_list[2]}")
    current_func.append("D=D-A") # repositions the ARG pointer

    current_func.append("@SP")
    current_func.append("D=M")
    current_func.append("@LCL")
    current_func.append("M=D") # repositions the LCL pointer

def search_for_functions(commands: list):
    functions = {}
    for cmd in commands:
        cmd = cmd.split(" ")
        if cmd[0] == "function":
            functions[cmd[1]] = []

    return functions
    
def coder(commands: list, filename: str):
    asm_ins = []
    current_func = []
    functions = search_for_functions(commands)
    i = 0
    for c in commands:
        c = c.strip()
        c_list = c.split(" ")
        asm_ins.append("// " + c + "\n")

        if c_list[0] == "push":
            if c_list[1] == "constant":
                code_constant(c_list, current_func)           
            
            elif c_list[1] == "argument":
                push_arg_local_this_that(c_list, current_func, "@ARG")

            elif c_list[1] == "local":
                push_arg_local_this_that(c_list, current_func, "@LCL")

            elif c_list[1] == "this":
                push_arg_local_this_that(c_list, current_func, "@THIS")

            elif c_list[1] == "that":
                push_arg_local_this_that(c_list, current_func, "@THAT")

            elif c_list[1] == "static":
                push_static(c_list, current_func, filename)

            elif c_list[1] == "temp":
                push_temp(c_list, current_func)

            elif c_list[1] == "pointer":
                push_pointer(c_list, current_func)

        elif c_list[0] == "pop":
            
            if c_list[1] == "argument":
                pop_arg_local_this_that(c_list, current_func, "@ARG")

            elif c_list[1] == "local":
                pop_arg_local_this_that(c_list, current_func, "@LCL")

            elif c_list[1] == "this":
                pop_arg_local_this_that(c_list, current_func, "@THIS")

            elif c_list[1] == "that":
                pop_arg_local_this_that(c_list, current_func, "@THAT")
        
            elif c_list[1] == "static":
                pop_static(c_list, current_func, filename)

            elif c_list[1] == "temp":
                pop_temp(c_list, current_func)

            elif c_list[1] == "pointer":
                pop_pointer(c_list, current_func)
        
        elif c_list[0].strip() == "add": # added .strip() to eliminate the \n at the end
            add(current_func)

        elif c_list[0].strip() == "sub":
            subtract(current_func)

        elif c_list[0].strip() == "not":
            notfc(current_func)

        elif c_list[0].strip() == "and" or c_list[0].strip() == "or":
            andorfc(c_list, current_func)

        elif c_list[0].strip() == "neg":
            neg(current_func)

        elif c_list[0].strip() == "eq" or c_list[0].strip() == "gt" or c_list[0].strip() == "lt":
            i += 1
            eqgtlt(c_list, current_func, i)

        elif c_list[0].strip() == "label":
            current_func.append(f"({c_list[1]})")

        elif c_list[0].strip() == "if-goto":
            ifgoto(c_list, current_func)

        elif c_list[0].strip() == "goto":
            goto(c_list, current_func)

        elif c_list[0].strip() == "call":
            call(c_list, current_func)

        elif c_list[0].strip() == "function":
            current_func = functions[c_list[1]]
            current_func.append(f"({c_list[1]})")

        current_func.append("\n")

    for function_instructions in functions.values():
        current_func.extend(function_instructions)

    return current_func

filename = input("Please specify the filename: ")

vm_commands = reader(filename)
final_instructions = coder(vm_commands, filename)

with open("asm_programs/" + filename + ".asm", "w") as file:
    for ins in final_instructions:
        if ins == "\n":
            file.write(ins)
        else:
            file.write(ins + "\n")