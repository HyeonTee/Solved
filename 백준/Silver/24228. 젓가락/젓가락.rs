use std::io;

fn main() {
    let mut b = String::new();
    io::stdin().read_line(&mut b).unwrap();
    let v: Vec<u128> = b.split_whitespace().map(|x| x.parse().unwrap()).collect();
    print!("{}", v[0] + v[1] * 2 - 1);
}