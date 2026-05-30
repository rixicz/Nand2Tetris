@i // iterates i till it equals a - during the iteration: sum = sum+b
M=0 // declaring i=0
(LOOP) // beginning of the loop
@a 
D=M
@i
D=D-M //subtracting i from a to see if they are equal or not
@END
D;JEQ // condition checking if D is equal to zero (if a == i)
@b  
D=M // putting the value from b into the D reg
@sum
M=D+M // adding b into the sum
@i
M=M+1 // incrementing i
@LOOP // going for another iteration
0;JMP
(END)
@END
0;JMP   // infinite loop - ending the programme