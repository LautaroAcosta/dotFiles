use std::io;


fn division(x:u32, y:u32) -> u32{
    if x < y{
        0
    }
    else{
       1 + division(x-y, y)
    }
}

fn main(){
    
    println!("Porfavor, ingrese el dividendo: ");
    let mut dividendo = String::new(); 
    io::stdin()
        .read_line(&mut dividendo)
        .expect("Failed to read line");
   
    println!("Porfavor, ingrese el divisor: ");
    let mut divisor = String::new(); 
    io::stdin()
        .read_line(&mut divisor)
        .expect("Failed to read line");

    let dividendo: u32 = dividendo.trim().parse().expect("Porfavor, ingresa un número!");
    let divisor: u32 = divisor.trim().parse().expect("Porfavor, ingresa un número!");

    println!("El resultado de la división entera de {} por {} es: {}",dividendo,divisor,division(dividendo,divisor));
}
