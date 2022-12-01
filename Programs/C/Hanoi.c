#include <stdlib.h>
#include <stdio.h>

void hanoi (int n, char com, char aux, char fin){
    if (n == 1) {
        printf("%c->%c\n", com, fin); 
    }
    else {
        hanoi(n-1, com, fin, aux); 

        printf("%c->%c\n", com, fin); 
         
        hanoi(n-1, aux, com, fin);
    }
}

int main() {
    char com ='A'; 
    char aux ='B'; 
    char fin ='C'; 
    int n; 

    printf("Numero de discos: \n"); 
    scanf("%d",&n); 

    printf("Movimientos a realizar son los siguientes: \n"); 
    hanoi(n,com,aux,fin); 
    return 0; 
}


