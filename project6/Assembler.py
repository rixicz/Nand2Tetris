# This code is supposed to take the assembly input, parse it into different fields and then code the assembly into binary
# Firstly, I need to declare the codes for each possible field in the instruction
comp_values = {
    "0": 42,
    "1": 63,
    "-1": 58,
    "D": 12,
    "A": 48,
    "M": 48,
    "!D": 13,
    "!A": 49,
    "!M": 49,
    "-D": 15,
    "-A": 51,
    "-M": 51,
    "D+1": 31,
    "A+1": 55,
    "M+1": 55,
    "D-1": 14,
    "A-1": 50,
    "M-1": 50,
    "D+A": 2,
    "D+M": 2,
    "D-A": 19,
    "D-M": 19,
    "A-D": 7,
    "M-D": 7,
    "D&A": 0,
    "D&M": 0,
    "D|A": 21,
    "D|M": 21
}

dest_values = {
    "null": 0,  # 000
    "M": 1,     # 001
    "D": 2,     # 010
    "MD": 3,    # 011
    "A": 4,     # 100
    "AM": 5,    # 101
    "AD": 6,    # 110
    "AMD": 7    # 111
}

jump_values = {
    "null": 0,  # 000
    "JGT": 1,   # 001
    "JEQ": 2,   # 010
    "JGE": 3,   # 011
    "JLT": 4,   # 100
    "JNE": 5,   # 101
    "JLE": 6,   # 110
    "JMP": 7    # 111
}

def cleaner(filename): # takes all the instructions only and saves it into a list
    with open(filename) as asm:
        pure_code = []
        for line in asm:
            line = line.strip()
            if not line:
                continue
            if line.startswith("//"): # deals only with inline comments
                continue
            
            pure_code.append(line)

    return pure_code

def parser(instruction): # parses the instructions and codes the fields into binary

        if "@" in instruction:
            val = int(instruction[1:]) # ignores the @ and puts the value into a var
        else:
            val = instruction.split("=")

            if ";" in val:
               val[1].split(";")

        return val
 
def coder(val, dest_values, comp_values, jump_values):
    if isinstance(val, int):
        bcode = bin(val)[2:].zfill(16) # converting the integer into a 16-bit binary string
            

    else:
        val[0] = dest_values[val[0]]
        val[1] = comp_values[val[1]]

        if len(val) > 2:
                val[2] = jump_values[val[2]]
            
        bcode = bin(int("".join(map(str, val))))[2:].zfill(16) # joins the bits together
    
    return bcode
                


        
file_in = input("Input file: ")
file_out = input("Output file: ")
pure_code = cleaner(file_in)
print(pure_code)
machine_list = []
while len(pure_code) > len(machine_list):
    
    for instruction in pure_code:
        val = parser(instruction)
        print(val)
        binary = coder(val, dest_values, comp_values, jump_values)
        machine_list.append(binary)

print(machine_list)
machine_instructions = "".join(map(str, machine_list))
print(machine_instructions)
with open(file_out, "w") as f:
  f.write(machine_instructions)


    
        




def helper():
    uwu = list("D=D+A//comment")
    uwu = list("D=(celek a plus d)")

