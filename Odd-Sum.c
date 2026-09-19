#include <stdio.h>

int main()
{
    int n, sum = 0;
    printf("Enter a number: ");
    scanf("%i", &n);
    for (int i = 1; i <= n; i += 2)
    {
        sum += i;
    }
    printf("The sum of odd numbers from 1 to %i is: %i\n", n, sum);
}