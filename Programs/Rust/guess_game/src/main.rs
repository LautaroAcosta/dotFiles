use std::io;
use std::cmp::Ordering;
use rand::Rng;

fn main() {
    println!("Adiviná el número!");

    let secret_number = rand::thread_rng().gen_range(1..=100);

    loop{
        println!("Porfavor, ingrese qué número piensa que es.");

        let mut guess = String::new();

        io::stdin()
            .read_line(&mut guess)
            .expect("No se pudo leer la línea");
    
        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        println!("Adivinaste: {guess}");

        match guess.cmp(&secret_number){
            Ordering::Less => println!("Muy pequeño!"),
            Ordering::Greater => println!("Muy grande!"),
            Ordering::Equal => {
                println!("Ganaste!"); break;
            }
        }
    }
}
