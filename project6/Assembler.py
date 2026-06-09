# This code is supposed to take the assembly input, parse it into different fields and then code the assembly into binary

comp_value = {"0": 42, "1": 63, "-1": 58, "D": 12, "A": } 
def instruction():
    with open(input("filename: ")) as asm:
        pure_code = []
        for line in asm:
            line = line.strip()
            if not line:
                continue
            if line.startswith("//"): # deals only with inline comments
                continue
            
            pure_code.append(line)

    return pure_code

def parser(code):
    for instruction in code:

        if "@" in instruction:
            
            val = int(instruction[1:]) # ignores the @ and puts the value into a var
            bcode = bin(val)[2:].zfill(16) # converting the integer into a 16-bit binary string
            print(bcode)

        else:
            bcode = instruction.split("=")
            print(bcode)
    
    return bcode 

pure_code = instruction()
binary = parser(pure_code)
print(pure_code)
list(pure_code[0])

def helper():
    uwu = list("D=D+A//comment")
    uwu = list("D=(celek a plus d)")

