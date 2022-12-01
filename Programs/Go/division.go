package main

import "fmt"

func division (a int, b int) int {
    if a < b{
        return 0
    }else{
        return 1 + division(a-b, b)
    }
}

func main(){
    a, b := 8,2
    fmt.Printf("El resultado de la division entre %g y % g es: %g",a,b, division(a, b))
}
