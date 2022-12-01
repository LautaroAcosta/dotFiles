use std::io;

fn fibo(x: u64) -> u64 {
    if x < 2 {
        x
    } else {
        fibo(x - 1) + fibo(x - 2)
    }
}

fn main() {
    loop {
        println!("Ingrese el número de Fibonacci que busca");

        let mut numero = String::new();

        io::stdin()
            .read_line(&mut numero)
            .expect("No se logró leer el número");

        let numero: u64 = match numero.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        let result = fibo(numero);
        println!("El número de fibonacci en la posición {numero} es: {result}");
        break;
    }
}
