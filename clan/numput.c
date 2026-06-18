#include <stdio.h> //i forgot stdio.h and wrote stdio instead woops
int main() {
    int usf, euf; //gotta declare variiabs and type
    printf("Enter US Floor\n");
    scanf("%d", &usf); //scan and find a number
    euf=usf-1;
    printf("EU Floor %d\n", euf);
}

/*
Remarks
har ek line ke baad ;
int=initialize??
 python2 ka input is like scanf("%d", ...)
 & i want you to change it... & give it the address of usf not the value of usf... call by value vs call by reference

*/