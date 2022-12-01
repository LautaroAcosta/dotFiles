#include <stdio.h>
#define difference 32



float convert (float f){
    return (5.0/9.0) * (f-difference);
}


int main(){
    float x;
    printf("Ingrese la temperatura en Fahrenheit: \n");
    scanf("%f",&x);

    printf("La temperatura equivalente en Celcius es:\n%.2f °C\n", convert(x));
}
