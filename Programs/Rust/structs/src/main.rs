struct Usuario {
    activo: bool,
    nombre: String,
    email: String,
    num_accesos: u64,
}

struct Color(i32,i32,i32);
struct Point(i32,i32,i32);
struct SiempreIguales;

fn build_user(email:String,nombre: String) -> Usuario {
    Usuario {
        email,
        nombre,
        activo: true,
        num_accesos: 1,
    }
}

fn main(){
    let mut user1 = build_user(String::from("ElCorreoDeAlguien@ejemplo.com"),String::from("Alfonso Varela"));

    user1.nombre = String::from("LautaroAcosta11");
    
    let user2 = Usuario{
        email: String::from("OtroCorreo@ejemplo2.com"),
        nombre: String::from("VictoriaLaTora"),
        ..user1
    };

    println!("{0},{1},{2},{3}",user1.nombre, user1.email, user1.activo, user1.num_accesos);
    

    let black = Color(0,0,0);
    let origin = Point(0,0,0);

    let sujeto = SiempreIguales;


}

