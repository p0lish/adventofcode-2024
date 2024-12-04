use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
fn main() {
    if let Ok(lines) = read_lines("./input.txt") {
        let mut report_counter = 0;
        for line in lines.flatten() {
            let numbers: Vec<i32> = line
                .split_whitespace()
                .map(|x| -> i32 { x.parse().unwrap() })
                .collect();
            if numbers.len() > 1 {
                if check_it(&numbers) {
                    report_counter += 1;
                } else {
                    if make_it_safe(&line) {
                        report_counter += 1;
                    }
                }
            }
        }
        println!("Safe reports: {}", report_counter);
    }
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn check_it(line: &Vec<i32>) -> bool {
    let numbers: Vec<i32> = line.clone();
    let mut prev_item = 0;
    let mut prev_diff = 0;
    let mut is_first = true;
    let mut min = 0;
    let mut max = 0;
    for i in numbers {
        if is_first {
            is_first = false;
            prev_item = i;
        } else {
            let diff = prev_item - i;
            prev_item = i;
            if diff == 0 {
                return false;
            }
            if diff * prev_diff < 0 {
                return false;
            }
            prev_diff = diff;

            if diff > max {
                max = diff;
            }
            if diff < min {
                min = diff;
            }
        }
    }
    if min < -3 || max > 3 {
        return false;
    }
    return true;
}

fn make_it_safe(line: &str) -> bool {
    let numbers: Vec<i32> = line
        .split_whitespace()
        .map(|x| -> i32 { x.parse().unwrap() })
        .collect();
    let mut fixed = false;
    for i in 0..numbers.len() {
        let mut numbers_pre = numbers.clone();
        numbers_pre.remove(i);
        fixed = fixed || check_it(&numbers_pre);
    }
    return fixed;
}
