use num_bigint::BigUint;

fn main() {
    let mut max = BigUint::from(0u32);
    for i in 1..100 {
        for j in 1..100 {
            let result: BigUint = BigUint::from(i as u32).pow(j);
            let sum = sum_of_numbers(&result);
            if sum > max {
                max = sum;
            }
        }
    }
    println!("{:?}", max);
}

fn sum_of_numbers(number: &BigUint) -> BigUint {
    number
        .to_string()
        .chars()
        .map(|c| c.to_digit(10).unwrap())
        .map(BigUint::from)
        .sum()
}
