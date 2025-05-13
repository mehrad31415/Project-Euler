fn main() {
    let mut x = 26241;
    loop {
        let val = split_nums(x);
        println!("x = {}, percentage = {}", x, val); // Debug line
        if val <= 10.0 {
            println!("{}", x);
            break;
        }
        x += 2;
    }
}

fn is_prime(n: i32) -> bool {
    if n < 2 {
        return false;
    }
    for i in 2..=(n as f64).sqrt() as i32 {
        if n % i == 0 {
            return false;
        }
    }
    true
}

fn split_nums(depth: i32) -> f64 {
    let mut sq: i32 = 1;
    let mut last = 0;
    let mut count = 0;
    let mut all = 0;
    for i in 1..=depth.pow(2) {
        if i <= sq.pow(2) {
            if sq == 1 || (i - last) % (sq - 1) == 0 {
                if is_prime(i) {
                    count += 1;
                }
                all += 1;
            }
        } else {
            last = i - 1;
            sq += 2;
        }
    }
    (count as f64) * 100.0 / (all as f64)
}
