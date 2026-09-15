def reader(filename: str):
    with open("vm_programs/" + filename + ".vm", "r") as file:
        commands = []
        for line in file:
            check_line = line.strip()
            if line.startswith("/") or not check_line:
                continue
            commands.append(line)
        
        return commands

def commenter(commands: list):
    return ["// " + x for x in commands]

filename = input("Please specify the filename: ")

vm_commands = reader(filename)
asm_instructions = commenter(vm_commands)

with open("asm_programs/" + filename + ".asm", "w") as file:
    for ins in asm_instructions:
        file.write(ins)