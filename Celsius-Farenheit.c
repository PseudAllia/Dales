#include <stdio.h>

int main()
{
    float celsius, farenheit;
    printf("Enter the temeprature in Celsius: ");
    scanf("%f", &celsius);
    farenheit = (celsius * 1.8) + 32;
    printf("%.2f Celsius = %.2f Farenheit", celsius, farenheit);
}
