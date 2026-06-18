#include <stdio.h>
int main(){
    char line[1000];
    printf("Enter line:\n");
    scanf("%[^\n]999s", line); //regular rexpressions ughh, match any char that's a new  line, so scan until end of line or until you hit 999 characters
    printf("Line: %s\n", line);
}

/*
print("Enter line")
line=input()
print('line:',line)
*/