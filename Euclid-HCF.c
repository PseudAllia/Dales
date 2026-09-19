#include <stdio.h>

int main()
{
    int a, b, temp;
    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);
    if (a > b)
    {
        a, b = b, a;
    }
    while (b != 0 && a != 0)
    {
        temp = a % b;
        a = b;
        b = temp;
    }
    if (a == 0)
    {
        printf("The HCF is: %d", b);
    }
    else
    {
        printf("The HCF is: %d", a);
    }
}