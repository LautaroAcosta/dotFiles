#include <stdio.h>

int division(int x, int y){
    if (x<y)
        return 0;
    else
        return 1 + division(x-y,y);
}

int main(){
    int x, y;
    printf("ingrese el dividendo: \n");
    scanf("%d",&x);
    printf("Ingrese el divisor: \n");
    scanf("%d",&y);
    printf("El resultado de la división entera entre %d y %d es de: %d", x, y, division(x,y));
}

Hola que 
