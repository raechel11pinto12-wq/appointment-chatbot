#include <stdio.h>
int main ()
{
char a;
printf("ENTER CHARACTER\n");
scanf("%d", &a);
switch(a)
{
    case 'a': printf("LOWERCASE a");
    break;
    case 'A': printf("UPPERCASE A");
    break;
    default: printf("INVALID");
    break
}
    return 0;
}