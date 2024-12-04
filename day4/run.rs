use std::cmp;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
fn main() {

    let search_str = "XMAS";
    let search_str_reverse = search_str.chars().rev().collect::<String>();

    println!("Search string: {}, {}", search_str, search_str_reverse);

    if let Ok(lines) = read_lines("./demo.txt") {
        let lines_arr = lines.flatten().collect::<Vec<String>>();
        let mut verticals = lines_arr.clone();
        let mut horizontals = Vec::new();
        let mut inverted = Vec::new();

        for i in 0..lines_arr.len() {
            let mut horz = String::from("");
            let mut inv = String::from("");
            let line = lines_arr[i].clone();
            for j in 0..line.len() {
                let liney = lines_arr[j].clone();
                let char = liney.chars().nth(i).unwrap();
                horz.push(char);
                inv = char.to_string() + &inv;
            }
            inverted.push(inv);
            horizontals.push(horz.to_string());
        }

        let mut diagonalx = Vec::new();
        let mut diagonaly = Vec::new();

        let lenx = verticals.len();
        let leny = verticals[0].len();

        for i in 0..(lenx + leny - 1) {
            let mut curx = String::from("");
            let mut cury = String::from("");
            let lowest = if i < leny { 0 } else { i - leny + 1 };
            let highest = cmp::min(lenx, i + 1);
            for j in lowest..highest {
                curx.push(verticals[j].chars().nth(i - j).unwrap());
                cury.push(inverted[j].chars().nth(i - j).unwrap());
            }
            diagonalx.push(curx.to_string());
            diagonaly.push(cury.to_string());
        }


        // Part 1 solutions
        let ver = verticals.clone();
        let mut all = Vec::new();
        all.append(&mut verticals);
        all.append(&mut horizontals);
        all.append(&mut diagonalx);
        all.append(&mut diagonaly);

        let mut all_xmas_string = 0;
        let mut x_mas_string = 0;

        for i in 0..all.len() {
            all_xmas_string += all[i].matches(search_str).count();
            all_xmas_string+= all[i].matches(search_str_reverse.as_str()).count();
        }


        // Part 2 solution starts here

        for i in 0..ver.len() - 2 {
            let line1 = ver[i].clone();
            let line2 = ver[i + 1].clone();
            let line3 = ver[i + 2].clone();
            for j in 0..line1.len() - 2 {
                let left_top = line1.chars().nth(j).unwrap();
                let right_top = line1.chars().nth(j + 2).unwrap();
                let middle = line2.chars().nth(j + 1).unwrap();
                let left_bottom = line3.chars().nth(j).unwrap();
                let right_bottom = line3.chars().nth(j + 2).unwrap();

                let top = left_top.to_string() + &right_top.to_string();
                let bottom = left_bottom.to_string() + &right_bottom.to_string();
                let ms = "MS";
                let mm = "MM";
                let sm = "SM";
                let ss = "SS";
                if middle == 'A' {
                    if (top == ms && bottom == ms) 
                    || (top == mm && bottom == ss)
                    || (top == ss && bottom == mm) 
                    || (top == sm && bottom == sm) {
                        x_mas_string += 1;    
                    }
                    
                }
            }
        }
        println!("Found {} XMAS strings", all_xmas_string);
        println!("Found {} X-MAS ", x_mas_string);    
    }
}
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
