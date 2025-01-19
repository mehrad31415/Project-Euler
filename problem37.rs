// fn main() {
//     // right digit can only be 2 or 3 or 5 or 7
//     // 2
//     let mut list = vec![vec![3]];
//     let mut index = 0;
//     while true {
//         let mut l = Vec::new();
//         for i in &list[index] {
//             for j in 1..5 {
//                 let x = i + j * 10i32.pow((index+1) as u32);
//                 if is_prime(x) {
//                     l.push(x);
//                 }
//             }
//         }
//         if l.is_empty() {
//             break;
//         } else {
//             list.push(l);
//         }
//         index +=1 ;
//     }
//     println!("{:#?}", list);
// }

// fn number_of_digits(number: i32) -> i32 {
//     let mut counter = 0;
//     let mut num = number;
//     while num != 0 {
//         num = num / 10;
//         counter += 1;
//     }
//     counter
// }

// fn is_prime(number: i32) -> bool {
//     for i in 2..(i32::isqrt(number) + 1) {
//         if number % i == 0 {
//             return false;
//         }
//     }
//     true
// }