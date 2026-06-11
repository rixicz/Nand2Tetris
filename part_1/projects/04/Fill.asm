(MAIN)
@SCREEN
D=A 
@arr // array having the value as the address of screen, behaves as pointers 
M=D 

@8192    // Total words in the screen map
D=A
@n // maximum of words
M=D
@i   // iterative var
M=0  // setting it to 0

@KBD  // checking the keyboard input, if zero, it goes to the whitening loop, otherwise it blackens 
D=M
@WLOOP    
D;JEQ
@BLOOP 
D;JNE

(BLOOP)
@arr
D=M
@i
A=D+M // calculating the address needed by adding arr + i 
M=-1 // setting the reg onto 1111111111111111 (-1 in decimal) - that is black color
@i
M=M+1 // i++

@KBD  // checking the keyboard input again, if zero - it goes to the beginning, otherwise, it continues in the loop
D=M
@MAIN    
D;JEQ

@n 
D=M
@i 
D=D-M 
@MAIN // jump to MAIN if it reaches the end of the screen, otherwise continue 
D;JEQ 
@BLOOP 
0;JMP

(WLOOP)
@arr
D=M
@i
A=D+M       // same pointing exercise as in BLOOP 
M=0  // setting the reg to 0 = it's white 
@i
M=M+1

@KBD    // checking the KBD input, if zero, the loop continues, otherwise it goes to the beginning
D=M
@MAIN    
D;JNE

@n 
D=M
@i 
D=D-M 
@MAIN
D;JEQ  
@WLOOP
0;JMP // jump to MAIN if it reaches the end of the screen, otherwise continue in the loop