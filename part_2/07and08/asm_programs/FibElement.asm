// function Main.fibonacci 0

// push argument 0

// push constant 2

// lt

// if-goto N_LT_2

// goto N_GE_2

// label N_LT_2               // if n < 2 returns n

// push argument 0

// return

// label N_GE_2               // if n >= 2 returns fib(n - 2) + fib(n - 1)

// push argument 0

// push constant 2

// sub

// call Main.fibonacci 1  // computes fib(n - 2)

// push argument 0

// push constant 1

// sub

// call Main.fibonacci 1  // computes fib(n - 1)

// add                    // returns fib(n - 1) + fib(n - 2)

// return

// function Sys.init 0

// // Computes fibonacci(4)

// push constant 4

// // Calls the function, informing that one argument was pushed onto the stack

// call Main.fibonacci 1

// label END

// goto END  // loops infinitely

(Sys.init)


@4
D=A
@SP
A=M
M=D
@SP
M=M+1


@LCL
D=M
@SP
M=M+1
A=M-1
M=D
@ARG
D=M
@SP
M=M+1
A=M-1
M=D
@THIS
D=M
@SP
M=M+1
A=M-1
M=D
@THAT
D=M
@SP
M=M+1
A=M-1
M=D
@SP
D=M
@5
D=D-A
@1
D=D-A
@SP
D=M
@LCL
M=D

(END)

@END
0;JEQ

(Main.fibonacci)

@0
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

@2
D=A
@SP
A=M
M=D
@SP
M=M+1

@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
@TRUE1
D;JLT
@SP
A=M-1
M=0
@FALSE1
0;JEQ
(TRUE1)
@SP
A=M-1
M=-1
(FALSE1)

@SP
M=M-1
A=M
D=M
@N_LT_2
D;JGT

@N_GE_2
0;JEQ

(N_LT_2)

@0
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1


(N_GE_2)

@0
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

@2
D=A
@SP
A=M
M=D
@SP
M=M+1

@SP
M=M-1
A=M
D=M
A=A-1
M=M-D

@LCL
D=M
@SP
M=M+1
A=M-1
M=D
@ARG
D=M
@SP
M=M+1
A=M-1
M=D
@THIS
D=M
@SP
M=M+1
A=M-1
M=D
@THAT
D=M
@SP
M=M+1
A=M-1
M=D
@SP
D=M
@5
D=D-A
@1
D=D-A
@SP
D=M
@LCL
M=D

@0
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

@1
D=A
@SP
A=M
M=D
@SP
M=M+1

@SP
M=M-1
A=M
D=M
A=A-1
M=M-D

@LCL
D=M
@SP
M=M+1
A=M-1
M=D
@ARG
D=M
@SP
M=M+1
A=M-1
M=D
@THIS
D=M
@SP
M=M+1
A=M-1
M=D
@THAT
D=M
@SP
M=M+1
A=M-1
M=D
@SP
D=M
@5
D=D-A
@1
D=D-A
@SP
D=M
@LCL
M=D

@SP
M=M-1
A=M
D=M
A=A-1
M=D+M


