(Sys.add12)

// push constant 4002

@4002
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop pointer 0

@SP
M=M-1
A=M
D=M
@THIS
M=D

// push constant 5002

@5002
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop pointer 1

@SP
M=M-1
A=M
D=M
@THAT
M=D

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

// push constant 12

@12
D=A
@SP
A=M
M=D
@SP
M=M+1

// add

@SP
M=M-1
A=M
D=M
A=A-1
M=D+M

// return


(Sys.main)
@SP
M=M+1
A=M-1
M=0
@SP
M=M+1
A=M-1
M=0
@SP
M=M+1
A=M-1
M=0
@SP
M=M+1
A=M-1
M=0
@SP
M=M+1
A=M-1
M=0

// push constant 4001

@4001
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop pointer 0

@SP
M=M-1
A=M
D=M
@THIS
M=D

// push constant 5001

@5001
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop pointer 1

@SP
M=M-1
A=M
D=M
@THAT
M=D

// push constant 200

@200
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop local 1

@1
D=A
@LCL
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

// push constant 40

@40
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop local 2

@2
D=A
@LCL
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

// push constant 6

@6
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop local 3

@3
D=A
@LCL
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

// push constant 123

@123
D=A
@SP
A=M
M=D
@SP
M=M+1

// call Sys.add12 1

@returnval1
D=M
@retAddr
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
@SP
D=M
@LCL
M=D
@Sys.add12
0;JEQ
(returnval1)

// pop temp 0

@0
D=A
@5
A=D+A
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

// push local 0

@0
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

// push local 1

@1
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

// push local 2

@2
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

// push local 3

@3
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

// push local 4

@4
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

// add

@SP
M=M-1
A=M
D=M
A=A-1
M=D+M

// add

@SP
M=M-1
A=M
D=M
A=A-1
M=D+M

// add

@SP
M=M-1
A=M
D=M
A=A-1
M=D+M

// add

@SP
M=M-1
A=M
D=M
A=A-1
M=D+M

// return


// function Sys.add12 0

(Sys.init)

// push constant 4000	// tests that THIS and THAT are handled correctly

@4000	//
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop pointer 0

@SP
M=M-1
A=M
D=M
@THIS
M=D

// push constant 5000

@5000
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop pointer 1

@SP
M=M-1
A=M
D=M
@THAT
M=D

// call Sys.main 0

@returnval0
D=M
@retAddr
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
@0
D=D-A
@SP
D=M
@LCL
M=D
@Sys.main
0;JEQ
(returnval0)

// pop temp 1

@1
D=A
@5
A=D+A
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

// label LOOP

(LOOP)

// goto LOOP

@LOOP
0;JEQ

// function Sys.main 5

