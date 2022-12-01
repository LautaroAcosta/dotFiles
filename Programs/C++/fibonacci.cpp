#include <ostream>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>

int Fibonacci(int x){
    if (x < 2){
        return x;
    }
    else{
         return  Fibonacci(x-1)+Fibonacci(x-2);
    }
};


int main()
{
    std::cout << Fibonacci(45) << std::endl;
}

