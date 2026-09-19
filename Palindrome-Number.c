#include <stdio.h>
#include <string.h>

int main()
{
    char num[20];
    printf("Enter a number: ");
    scanf("%s", num);
    char pal[20];
    int len = strlen(num);
    for (int i = 0; i < len; i++)
    {
        pal[i] = num[len - 1 - i];
    }
    pal[len] = '\0';
    printf("The reverse of the number is: %s", pal);
}