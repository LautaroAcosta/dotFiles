package main

import "fmt"

func split(a int) (x, y int){
    x = a * 4
    y = a - x
    return
}

func main(){
    fmt.Println(split(18))
}
