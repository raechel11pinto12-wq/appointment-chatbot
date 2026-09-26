#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main ()
{
    int i, j, a[5], temp=0;
    printf("Enter 5 random numbers for the array");
    for(i=0;i<5;i++)
    {
        scanf("%d",&a[i]);
    }
    printf("Displaying the array");
    for(i=0;i<5;i++)
    {
        printf("%d", a[i]);
    }
    printf("SOrting array into ascending order");
    for(i=0;i<5;i++)
    {
        for(j=0;j<5;j++)
        {
            if (a[i]>a[j])
            temp=a[i];
            a[i]=a[j];
            a[j]=temp;
        }
    }
printf("Displaying sorted arrays");
for(i=0;i<5;i++)
{
    printf("%d", a[i]);
}
return 0;
}