#include <cs50.h>
#include <stdio.h>

int main(void)
{   
    // Solicitando ao usuário o valor do primeiro número
    int x = get_int("x: ");

    // Solicitando ao usuário o valor do segundo número
    int y = get_int("y: ");

    // Imprimindo a soma dos dois números
    printf("%i\n", x + y);
}