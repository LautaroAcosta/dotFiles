package main

import ("fmt")
        

func Fibo(n int) int {
    if n < 2{
        return n
    }else{
        return Fibo(n-2)+Fibo(n-1)
    }
}

func main(){
    var n int
    fmt.Println("Ingrese el nth número de la Sucesión de Fibonacci que busca: ")
    fmt.Scanln(&n)
    
    fmt.Printf("El número %d en la sucesión de fibonacci es: %d", n, Fibo(n))
}
