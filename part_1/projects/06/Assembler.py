# This code is supposed to take the assembly input, parse it into different fields and then code the assembly into binary
# Firstly, I need to declare the codes for each possible field in the instruction. For that I use dictionaries

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

symbol_table = {
    "R0": 0,
    "R1": 1,
    "R2": 2,
    "R3": 3,
    "R4": 4,
    "R5": 5,
    "R6": 6,
    "R7": 7,
    "R8": 8,
    "R9": 9,
    "R10": 10,
    "R11": 11,
    "R12": 12,
    "R13": 13,
    "R14": 14,
    "R15": 15,
    "SCREEN": 16384,
    "KBD": 24576,
    "SP": 0,
    "LCL": 1,
    "ARG": 2,
    "THIS": 3,
    "THAT": 4
}
    
def cleaner(filename): # takes all the instructions only and saves it into a list
    with open("asm_programs/" + filename) as asm:
        code = []
        for line in asm:
            line = line.strip()
            if not line:
                continue
            
            if line.startswith("//"): # deals only with comments on a new line
                continue
            
            elif "/" in line: # eliminates inline comments
                c_list = line.split("//", 1)
                line = c_list.pop(0)
                line = line.strip()
            
            code.append(line)

    return code

def scanner(code, table): # function that looks for labels or symbols and writes their value into the symbol_table
    ns_code = []
    i = 1
    n = 16
    for element in code:
        if "(" in element:
            
            label = element[1:-1]
            symbol_table[label] = i 
        
        elif "@" in element:
            val = element[1:]
            
            if not isinstance(val, int):
                
                if val not in symbol_table:
                    symbol_table[val] = n
                    n += 1
        else:   
            ns_code.append(element)
        
        i += 1
    
    return ns_code


def parser(instruction): # parses the instructions into fields

        if "@" in instruction:
            val = instruction[1:] # ignores the @ and puts the value into a var
        elif "=" in instruction:
            val = instruction.split("=")

        elif ";" in instruction:
            val = instruction.split(";")
        else:
            val = instruction

        return val
 
def coder(val, dest_values, comp_values, jump_values):
    if isinstance(val, int):
        bcode = bin(val)[2:].zfill(16) # converting the integer into a 16-bit binary string
    
    elif isinstance(val, str):
        val = symbol_table[val]
        bcode = bin(val)[2:].zfill(16)

    
    elif 'J' in val[1]:
        val[0] = comp_values[val[0]]
        val[1] = jump_values[val[1]]
        
        bcode = bin(int("".join(map(str, val))))[2:].zfill(16) # joins the bits together
    
    else:
        val[0] = dest_values[val[0]]
        val[1] = comp_values[val[1]]

        bcode = bin(int("".join(map(str, val))))[2:].zfill(16) # joins the bits together
    
    return bcode
                


        
file_in = input("Input file: ") # selecting the input file
file_out = input("Output file: ") # selecting the output file
pure_code = cleaner(file_in) # getting clean code without white space and comments
no_symbols = scanner(pure_code, symbol_table) # scans for symbols and labels and writes them into a dictionary

machine_list = []

while len(pure_code) > len(machine_list): # parsing and coding every instruction one by one and appending it into a list
    
    for instruction in no_symbols:
        val = parser(instruction)
        binary = coder(val, dest_values, comp_values, jump_values)
        machine_list.append(binary)

machine_instructions = "".join(map(str, machine_list)) # creating string out of the list

print(machine_instructions) # just to check what it outputs

with open("hack_programs/" + file_out, "w") as f: # writes into .hack file
  f.write(machine_instructions)

