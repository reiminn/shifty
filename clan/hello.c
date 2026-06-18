#include <stdio.h>
/* I am a comment */
/*
every code starts with #include <stdio.h>, gonna do some input output here so include this library, we couldn't use the print function if this wasnt here

*/
// can use double slash too but only in some versions and c+
//a function named main and its definition
// 'vs"... "character array", 'single character'
//print function
//new line implicit in python, in c you have to add it explicitly,

// %d theres an integer as an other parameter
// %.1f - floating point with one digit of precision
// Sarah is actually 6 characters cuz theres always a terminating character 0 at last
int main() {
    printf("Hello world\n");
    printf("Answer %d\n", 42);
    printf("Name %s\n", "Sarah");
    printf("x %.1f i %d\n", 3.5, 100);
}
/*
make hello *compiles
./hello *runs
*/
//my first code in c!!!!!! so pretty