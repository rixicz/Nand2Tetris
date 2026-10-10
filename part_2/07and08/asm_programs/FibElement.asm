@256
D=A
@SP
M=D
@300
D=A
@LCL
M=D
@400
D=A
@ARG
M=D
(Sys.init)

// // Computes fibonacci(4)


// push constant 4

@4
D=A
@SP
A=M
M=D
@SP
M=M+1

// // Calls the function, informing that one argument was pushed onto the stack


// call Main.fibonacci 1

@returnval2
D=A
@SP
M=M+1
A=M-1
M=D
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
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JEQ
(returnval2)

// label END

(END)

// goto END

@END
0;JEQ

(Main.fibonacci)

// push argument 0

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

// push constant 2

@2
D=A
@SP
A=M
M=D
@SP
M=M+1

// lt

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

// if-goto N_LT_2

@SP
M=M-1
A=M
D=M
@N_LT_2
D;JNE

// goto N_GE_2

@N_GE_2
0;JEQ

// label N_LT_2               // if n < 2 returns n

(N_LT_2)

// push argument 0

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

// return

@LCL
D=M
@endFrame
M=D
@0
D=A
@ARG
A=D+M
D=A
@addr
M=D
@SP
M=M-1
A=M
D=M
@addr
A=M
M=D
@ARG
D=M
@SP
M=D+1
@1
D=A
@endFrame
D=M-D
A=D
D=M
@THAT
M=D
@2
D=A
@endFrame
D=M-D
A=D
D=M
@THIS
M=D
@3
D=A
@endFrame
D=M-D
A=D
D=M
@ARG
M=D
@4
D=A
@endFrame
D=M-D
A=D
D=M
@LCL
M=D
@5
D=A
@endFrame
D=M-D
A=D
D=M
@retAddr
M=D
A=M
0;JEQ

// label N_GE_2               // if n >= 2 returns fib(n - 2) + fib(n - 1)

(N_GE_2)

// push argument 0

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

// push constant 2

@2
D=A
@SP
A=M
M=D
@SP
M=M+1

// sub

@SP
M=M-1
A=M
D=M
A=A-1
M=M-D

// call Main.fibonacci 1  // computes fib(n - 2)

@returnval0
D=A
@SP
M=M+1
A=M-1
M=D
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
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JEQ
(returnval0)

// push argument 0

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

// push constant 1

@1
D=A
@SP
A=M
M=D
@SP
M=M+1

// sub

@SP
M=M-1
A=M
D=M
A=A-1
M=M-D

// call Main.fibonacci 1  // computes fib(n - 1)

@returnval1
D=A
@SP
M=M+1
A=M-1
M=D
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
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JEQ
(returnval1)

// add                    // returns fib(n - 1) + fib(n - 2)

@SP
M=M-1
A=M
D=M
A=A-1
M=D+M

// return

@LCL
D=M
@endFrame
M=D
@0
D=A
@ARG
A=D+M
D=A
@addr
M=D
@SP
M=M-1
A=M
D=M
@addr
A=M
M=D
@ARG
D=M
@SP
M=D+1
@1
D=A
@endFrame
D=M-D
A=D
D=M
@THAT
M=D
@2
D=A
@endFrame
D=M-D
A=D
D=M
@THIS
M=D
@3
D=A
@endFrame
D=M-D
A=D
D=M
@ARG
M=D
@4
D=A
@endFrame
D=M-D
A=D
D=M
@LCL
M=D
@5
D=A
@endFrame
D=M-D
A=D
D=M
@retAddr
M=D
A=M
0;JEQ

// function Sys.init 0

