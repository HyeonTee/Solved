use std::io::{self, Read};

const MOD: i64 = 10007;

fn mod_pow(mut a: i64, mut b: i64) -> i64 {
    let mut res: i64 = 1;
    while b > 0 {
        if b & 1 == 1 {
            res = (res * a) % MOD;
        }
        a = (a * a) % MOD;
        b >>= 1;
    }
    res
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: i64 = input.trim().parse().unwrap();

    let mut result: i64 = 1;
    for i in 1..=9 {
        result = (result * (n + i)) % MOD;
    }

    let mut denom: i64 = 1;
    for i in 1..=9 {
        denom = (denom * i) % MOD;
    }

    result = (result * mod_pow(denom, MOD - 2)) % MOD;

    println!("{}", result);
}