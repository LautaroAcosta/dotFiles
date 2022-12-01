package main

import (
    "fmt"
    "math"
)

func main(){
    //If i'm using exported names they have to start with a Capital letter, if not they are seen as not exported names and will not work.
    fmt.Println(math.Pi)
}
