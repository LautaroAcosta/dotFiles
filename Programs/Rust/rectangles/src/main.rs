#[derive(Debug)]

struct Rectangulo{
    width: u32,
    height:u32,
}

impl Rectangulo {
   
    fn cuadrado (size:u32) -> Self{
        Self {
            width: size,
            height: size,
        }
    }

    fn area (&self) -> u32 {
        self.width * self.height
    }

    fn contener (&self, rectangulo: &Rectangulo) -> bool{
        self.width > rectangulo.width && self.height > rectangulo.height
    }
}

fn main (){
    let rect1 = Rectangulo::cuadrado(50);

    let rect2 = Rectangulo {
        width: 10,
        height: 40,
    };

    let rect3 = Rectangulo {
        width: 60,
        height: 45,
    };

    println!("Puede rect1 contener a rect2? {}", rect1.contener(&rect2));
    println!("Puede rect1 contener a rect3? {}", rect1.contener(&rect3));
}















// #[derive(Debug)]
// struct Rectangulo {
    // width: u32,
    // heigth: u32,
// }

// fn main(){
//     let escala = 2;

    // let rect1 = Rectangulo{
    // //     width: dbg!(30 * escala),
    //     heigth: 50,
    // };

    // dbg!(&rect1);


    // println!(
    //     "El área del rectángulo es de {} píxeles cuadrados",
        // area(&rect1)
    // );

    // println!("rect1 es: {:#?}", rect1);
// }

// fn area(rectangulo: &Rectangulo) -> u32{
//     rectangulo.width * rectangulo.heigth
// }


// fn main(){
//     let rect1 = (30,50);

//     println!(
        // "El area del rectángulo es de {} píxeles cuadrados",
        // area(rect1)
    // );
// }

// fn area (dimensiones: (u32,u32)) -> u32{
//     dimensiones.0 * dimensiones.1
// }


// fn main() {
//     let width1=30;
    // let height1 = 50;

    // println!(
    //     "El area del rectangulo es de {} pixeles cuadrados",
         // area(width1,height1)
    // );
// }

// fn area(width:u32, height:u32) -> u32{
//     width * height
//}
