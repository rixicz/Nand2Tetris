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
@returnval67000
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
@0
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.init
0;JEQ
(returnval67000)
(Class1.set)

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

// pop static 0

@SP
M=M-1
A=M
D=M
@Class1.vm.0
M=D

// push argument 1

@1
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

// pop static 1

@SP
M=M-1
A=M
D=M
@Class1.vm.1
M=D

// push constant 0

@0
D=A
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
@5
D=A
@endFrame
D=M-D
A=D
D=M
@retAddr
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
@retAddr
A=M
0;JEQ

// function Class1.get 0

(Class1.get)

// push static 0

@Class1.vm.0
D=M
@SP
A=M
M=D
@SP
M=M+1

// push static 1

@Class1.vm.1
D=M
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

// return

@LCL
D=M
@endFrame
M=D
@5
D=A
@endFrame
D=M-D
A=D
D=M
@retAddr
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
@retAddr
A=M
0;JEQ

(Class2.set)

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

// pop static 0

@SP
M=M-1
A=M
D=M
@Class2.vm.0
M=D

// push argument 1

@1
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

// pop static 1

@SP
M=M-1
A=M
D=M
@Class2.vm.1
M=D

// push constant 0

@0
D=A
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
@5
D=A
@endFrame
D=M-D
A=D
D=M
@retAddr
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
@retAddr
A=M
0;JEQ

// function Class2.get 0

(Class2.get)

// push static 0

@Class2.vm.0
D=M
@SP
A=M
M=D
@SP
M=M+1

// push static 1

@Class2.vm.1
D=M
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

// return

@LCL
D=M
@endFrame
M=D
@5
D=A
@endFrame
D=M-D
A=D
D=M
@retAddr
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
@retAddr
A=M
0;JEQ

(Sys.init)

// push constant 6

@6
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 8

@8
D=A
@SP
A=M
M=D
@SP
M=M+1

// call Class1.set 2

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
@2
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class1.set
0;JEQ
(returnval0)

// pop temp 0 // dumps the return value

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

// push constant 23

@23
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 15

@15
D=A
@SP
A=M
M=D
@SP
M=M+1

// call Class2.set 2

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
@2
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class2.set
0;JEQ
(returnval1)

// pop temp 0 // dumps the return value

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

// call Class1.get 0

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
@0
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class1.get
0;JEQ
(returnval2)

// call Class2.get 0

@returnval3
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
@0
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class2.get
0;JEQ
(returnval3)

// label END

(END)

// goto END

@END
0;JEQ

