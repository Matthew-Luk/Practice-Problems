#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // long x = get_long("What's x? ");
    // long y = get_long("What's y? ");
    // printf("%li\n", x + y);

    float x = get_float("What's x? ");
    float y = get_float("What's y? ");
    printf("%.20f\n", x / y);
}