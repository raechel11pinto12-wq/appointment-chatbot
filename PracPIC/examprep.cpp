#include <stdio.h>
#include <stdlib.h>
int main ()
{
    int i, j, a[3][3], sum=0;
    system("cls");
    printf("Enter elements for a matrix:\n");
    for(i=0;i<3;i)
    {
        for(j=0;j<3;j++)
        {
            scanf("%d",&a[i][j]);
        }
    }
    printf("Displaying matrix:\n");
    for(i=0;i<3;i++)
    {
        for(j=0;j<3;j++)
        {
            printf("%d ",a[i][j]);
        }
        printf("\n");
    }
    printf("Sum of diagonal elements:\n");
    for(i=0;i<3;i++)
    {
        for(j=0;j<3;j++)
        {
            if(i==j)
            {
                sum=sum+a[i][j];
            }
        }
    }
    printf("%d", sum);
    return 0;
}