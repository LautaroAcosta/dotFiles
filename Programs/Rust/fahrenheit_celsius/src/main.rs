use std::io;

fn convert(x:f32) -> f32{
    (x-32.0) * (5.0/9.0)
}


fn main() {

    println!("Ingrese la temperatura en Fahrenheit para convertirla a Celcius");
    
    let mut temp = String::new();

    io::stdin()
        .read_line(&mut temp)
        .expect("No se logró leer el número");

    let temp: f32 =temp.trim().parse().expect("Porfavor, ingresá un número");

    let result = convert(temp);
    println!("La conversión de Fahrenheit a Celcius es de: {result} °C");
}
