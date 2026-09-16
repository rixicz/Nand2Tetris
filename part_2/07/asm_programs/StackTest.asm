// push constant 17

@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 17

@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// eq

@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
@TRUE1
D;JEQ
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

// push constant 17

@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 16

@16
D=A
@SP
A=M
M=D
@SP
M=M+1

// eq

@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
@TRUE2
D;JEQ
@SP
A=M-1
M=0
@FALSE2
0;JEQ
(TRUE2)
@SP
A=M-1
M=-1
(FALSE2)

// push constant 16

@16
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 17

@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// eq

@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
@TRUE3
D;JEQ
@SP
A=M-1
M=0
@FALSE3
0;JEQ
(TRUE3)
@SP
A=M-1
M=-1
(FALSE3)

// push constant 892

@892
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 891

@891
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
@TRUE4
D;JLT
@SP
A=M-1
M=0
@FALSE4
0;JEQ
(TRUE4)
@SP
A=M-1
M=-1
(FALSE4)

// push constant 891

@891
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 892

@892
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
@TRUE5
D;JLT
@SP
A=M-1
M=0
@FALSE5
0;JEQ
(TRUE5)
@SP
A=M-1
M=-1
(FALSE5)

// push constant 891

@891
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 891

@891
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
@TRUE6
D;JLT
@SP
A=M-1
M=0
@FALSE6
0;JEQ
(TRUE6)
@SP
A=M-1
M=-1
(FALSE6)

// push constant 32767

@32767
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 32766

@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// gt

@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
@TRUE7
D;JGT
@SP
A=M-1
M=0
@FALSE7
0;JEQ
(TRUE7)
@SP
A=M-1
M=-1
(FALSE7)

// push constant 32766

@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 32767

@32767
D=A
@SP
A=M
M=D
@SP
M=M+1

// gt

@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
@TRUE8
D;JGT
@SP
A=M-1
M=0
@FALSE8
0;JEQ
(TRUE8)
@SP
A=M-1
M=-1
(FALSE8)

// push constant 32766

@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 32766

@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// gt

@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
@TRUE9
D;JGT
@SP
A=M-1
M=0
@FALSE9
0;JEQ
(TRUE9)
@SP
A=M-1
M=-1
(FALSE9)

// push constant 57

@57
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 31

@31
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 53

@53
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

// push constant 112

@112
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

// neg

@SP
A=M-1
M=-M

// and

@SP
M=M-1
A=M
D=M
A=A-1
M=D&M

// push constant 82

@82
D=A
@SP
A=M
M=D
@SP
M=M+1

// or

@SP
M=M-1
A=M
D=M
A=A-1
M=D|M

// not

@SP
A=M-1
M=!M

