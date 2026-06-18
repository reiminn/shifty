#include <stdio.h> //forgot the hashtag this time aagh
/*
print('Enter name')
name=input()
print('hello', name)
*/

int main(){
    char name[100];  /*cant say make a string, tell it to make a char array and tell the length too!!! no .append here, in python its an object, in c its an  char array with 100 elements, you can put 20 in, its fine, 80 fine, 1011 aandit blows up, but hey, its fast*/
    printf("Enter name:\n");
    scanf("%99s", name );
/*only read up to 100 characters... name with no & cuz name is an array with no name[], we are passing the address of the beginning of the array*/
    printf("Hello %s\n", name);
}