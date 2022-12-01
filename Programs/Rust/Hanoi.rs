use std::io;

fn hanoi (n:u32,strt:char,aux:char,end:char){
    if n == 1{
        println!("{}->{}", strt, end);
    }
    else{
        hanoi(n-1, strt, end, aux);
        println!("{}->{}", strt, end);
        hanoi(n-1, aux, strt, end);
    }
}

fn main(){
    let strt = 'A';
    let aux = 'B';
    let end = 'C';
    
    println!("Número de discos: ");

    let mut n = String::new();
    io::stdin()
        .read_line(&mut n)
        .expect("Failed to read line");
    let n:u32 = n.trim().parse().expect("Ingrese un número!");

    println!("Los movimientos a realizar son: ");
    hanoi(n, strt, end, aux);
}
