mod module {
    pub struct I {
        a: i32,
        b: f32
    }

    impl I {
        pub fn new(int: i32, float: f32) -> Self {
            return Self{a: int, b: float};
        }

        pub fn asstr(&self) -> String {
            let var = self.a as f32 * self.b;
            return format!("{}, {}, var = {}", (self).a, (*self).b, var);
        }
    }

    pub trait Braces {
        fn asstr(&self) -> String;
        fn inbraces(&self) -> String {
            return format!("{}", self.asstr());
        }
    }

}

impl module::Braces for i32 {
    fn asstr(&self) -> String {
        format!("{}", self)
    }
}

fn main() {
    let var = module::I::new(1, 1.3);
    println!("integer {}\nfloating point number {}", var.asstr(), 1 as f32);
    use module::Braces;
    println!("{}", (1 as i32).inbraces());
}
