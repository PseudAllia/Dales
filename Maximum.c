#include <stdio.h>

int main()
{
    int a, b, c;
    printf("Enter three numbers: ");
    scanf("%i %i %i", &a, &b, &c);
    if (a > b && a > c)
    {
        printf("%i is the largest number.", a);
    }
    else if (b > a && b > c)
    {
        printf("%i is the largest number.", b);
    }
    else
    {
        printf("%i is the largest number.", c);
    }
}