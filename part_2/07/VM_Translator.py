def reader(filename: str):
    with open("vm_programs/" + filename + ".vm", "r") as file:
        commands = []
        for line in file:
            check_line = line.strip()
            if line.startswith("/") or not check_line:
                continue
            commands.append(line)
        
        return commands

def parser(commands: list):
    asm_ins = []
    for c in commands:
        c = c.strip()
        c_list = c.split(" ")
        comment = "// " + c
        if c_list[0] == "push":
            if c_list[1] == "constant":
                print(c_list)
                asm_ins.append(comment + "\n")
                asm_ins.append(f"@{c_list[2]}")
                asm_ins.append("D=A")
                asm_ins.append("@SP")
                asm_ins.append("A=M")
                asm_ins.append("M=D")
                asm_ins.append("@SP")
                asm_ins.append("M=M+1")
                asm_ins.append("\n")

    return asm_ins

filename = input("Please specify the filename: ")

vm_commands = reader(filename)
asm_instructions = parser(vm_commands)

with open("asm_programs/" + filename + ".asm", "w") as file:
    for ins in asm_instructions:
        file.write(ins + "\n")