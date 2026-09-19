#include <stdio.h>

int main()
{
    int n, a = 0, b = 1, next;
    printf("Enter the how manyth Fibonacci number you want to find: ");
    scanf("%i", &n); 
    for (int i = 1; i <= n; i++)
    {
        next = a + b;
        a = b;
        b = next;
    }
    printf("The %i-th Fibonacci number is: %i\n", n, a);
}