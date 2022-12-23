#include <cs50.h>
#include <stdio.h>

int get_size(void);
void print_grid(int size);

int main(void) 
{
    int n = get_size();
    print_grid(n);
}

int get_size(void)
{
    int n;
    do
    {
        n = get_int("Height: ");
    } 
    while (n < 1);
    return n;
}

void print_grid(int n)
{
    for (int i = 1; i < (n + 1); i++)
    {
        for (int j = 1; j < (n + 1); j++)
        {
            if (j <= (n - i))
                printf(" ");
            else
                printf("#");
        }
        printf("\n");
    }
}